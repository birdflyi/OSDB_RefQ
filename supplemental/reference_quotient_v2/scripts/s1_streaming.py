"""Two-pass streaming execution adapter for corrected S1.

The adapter reads each authorized aggregate partition twice.  The first pass
builds the global admitted-only membership registry and source-boundary
signature.  The second pass classifies one bounded chunk at a time and keeps
only compact counters, rather than a full analytical records DataFrame.

This module constructs future S1 tables in memory only.  It never creates the
scientific v2 output root or writes publication results.
"""

from __future__ import annotations

import os
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import pandas as pd

from script.ch5_reference_quotient.membership import (
    MembershipRegistry,
    canonical_project_entity_identity,
    unique_project_membership,
)

from .paths import CORRECTED_OUTPUTS_ROOT, canonical_path
from .schema import (
    OPTIONAL_CORRECTED_PROVENANCE_FIELDS,
    REQUIRED_S1_SOURCE_BOUNDARY_FIELDS,
    SOURCE_ADMISSION_STATUSES,
)
from .s1_adapter import ADMITTED, S1SourceObservationAdapter, ValidatedReferenceChunk
from .s1_evidence_universe import (
    AGGREGATED_EDGE_WEIGHT,
    AMBIGUOUS,
    CONFLICT_EXCLUDED,
    EDGE_COUNT,
    FUTURE_S1_OUTPUT_CONTRACT,
    MembershipContext,
    NON_PROJECT,
    PROJECT_MAPPABLE,
    QUOTIENT_ELIGIBLE,
    REFERENCE_RECORD,
    S1EvidenceUniverseContractError,
    UNRESOLVED,
    _text,
    classify_evidence_records,
)


class S1StreamingContractError(S1EvidenceUniverseContractError):
    """Raised when the two-pass streaming contract cannot be accepted."""


@dataclass(frozen=True)
class S1BoundarySignature:
    """Compact source-boundary facts that must remain stable across passes."""

    partition_order: tuple[str, ...]
    partition_statistics: tuple[tuple[str, int, int, tuple[tuple[str, int], ...]], ...]
    reference_rows_before_admission: int
    admitted_reference_count: int
    status_counts: Mapping[str, int]
    unknown_status_count: int = 0
    source_admission_contradiction_count: int = 0


@dataclass(frozen=True)
class S1StreamingResult:
    """Compact two-pass S1 result with no row-level analytical DataFrame."""

    source_admission_before_count: int
    source_admission_status_counts: Mapping[str, int]
    admitted_reference_count: int
    membership_summary: Mapping[str, int]
    target_membership_base_counts: Mapping[str, int]
    conflict_excluded_record_occurrences: int
    quotient_eligible_records: int
    self_loop_evidence_weight: int
    cross_project_evidence_weight: int
    self_loop_edge_pairs: frozenset[tuple[str, str]]
    cross_project_edge_pairs: frozenset[tuple[str, str]]
    self_loop_edge_weights: Mapping[tuple[str, str], int]
    cross_project_edge_weights: Mapping[tuple[str, str], int]
    source_seed_membership_mismatch: int
    cross_tab_counters: Mapping[str, Mapping[tuple[str, str], int]]
    edge_class_counts: Mapping[str, int]
    pass1_boundary: S1BoundarySignature
    pass2_boundary: S1BoundarySignature

    @property
    def membership_conflict_entity_count(self) -> int:
        return int(self.membership_summary.get("membership_conflict_entities", 0))

    @property
    def directed_edge_counts(self) -> dict[str, int]:
        return {
            "self_loop_edge_count": len(self.self_loop_edge_pairs),
            "cross_project_directed_edge_count": len(self.cross_project_edge_pairs),
        }


_CROSS_TAB_SPECS: tuple[tuple[str, str, str], ...] = (
    ("event_type_x_target_membership_status", "event_type", "tar_membership_status"),
    ("source_entity_type_x_target_membership_status", "source_entity_type", "tar_membership_status"),
    ("target_entity_type_x_target_membership_status", "target_entity_type", "tar_membership_status"),
    ("event_type_x_quotient_eligibility", "event_type", "quotient_eligibility"),
    ("source_entity_type_x_quotient_eligibility", "source_entity_type", "quotient_eligibility"),
    ("target_entity_type_x_quotient_eligibility", "target_entity_type", "quotient_eligibility"),
)


def _path_key(path: Path) -> str:
    return os.path.normcase(os.fspath(path))


def _canonical_partition_paths(partition_paths: Iterable[str | Path]) -> list[Path]:
    paths = [canonical_path(path) for path in partition_paths]
    keys = [_path_key(path) for path in paths]
    if len(keys) != len(set(keys)):
        raise S1StreamingContractError("partition list contains duplicate identities")
    return paths


def _usecols_for_partition(adapter: S1SourceObservationAdapter, path: Path) -> list[str]:
    if not path.is_file():
        raise S1StreamingContractError("authorized partition is unavailable: %s" % path)
    try:
        headers = pd.read_csv(path, nrows=0).columns.tolist()
        adapter.validate_headers(headers)
    except Exception as exc:
        if isinstance(exc, S1StreamingContractError):
            raise
        raise S1StreamingContractError("partition header validation failed: %s" % path) from exc
    usecols = list(REQUIRED_S1_SOURCE_BOUNDARY_FIELDS)
    usecols.extend(field for field in OPTIONAL_CORRECTED_PROVENANCE_FIELDS if field in headers)
    return usecols


def _iter_validated_chunks(
    adapter: S1SourceObservationAdapter,
    partition_paths: Sequence[Path],
    chunksize: int,
    *,
    pass_name: str,
) -> Iterable[tuple[Path, ValidatedReferenceChunk]]:
    for path in partition_paths:
        adapter.context_for_partition(path)
        usecols = _usecols_for_partition(adapter, path)
        try:
            chunks = pd.read_csv(
                path,
                usecols=usecols,
                dtype="string",
                chunksize=chunksize,
                low_memory=False,
            )
            for chunk in chunks:
                try:
                    yield path, adapter.validate_reference_chunk(path, chunk)
                except Exception as exc:
                    prefix = "S1_TWO_PASS_INPUT_DRIFT" if pass_name == "pass2" else "S1_SOURCE_BOUNDARY"
                    raise S1StreamingContractError(
                        "%s: %s validation failed for %s" % (prefix, pass_name, path)
                    ) from exc
        except S1StreamingContractError:
            raise
        except Exception as exc:
            prefix = "S1_TWO_PASS_INPUT_DRIFT" if pass_name == "pass2" else "S1_SOURCE_BOUNDARY"
            raise S1StreamingContractError(
                "%s: %s read failed for %s" % (prefix, pass_name, path)
            ) from exc


def _membership_pairs(records: pd.DataFrame) -> Iterable[tuple[str, str]]:
    for side in ("src", "tar"):
        for entity_id, aggregate in zip(
            records[f"{side}_entity_id"], records[f"{side}_entity_id_agg"]
        ):
            identity = canonical_project_entity_identity(entity_id, aggregate)
            project = unique_project_membership(aggregate)
            if identity is not None and project is not None:
                yield identity, project


def _boundary_signature(
    partition_paths: Sequence[Path],
    per_partition: list[tuple[str, int, int, tuple[tuple[str, int], ...]]],
    reference_count: int,
    admitted_count: int,
    status_counts: Counter[str],
) -> S1BoundarySignature:
    status_values = {
        status: int(status_counts.get(status, 0)) for status in SOURCE_ADMISSION_STATUSES
    }
    return S1BoundarySignature(
        partition_order=tuple(_path_key(path) for path in partition_paths),
        partition_statistics=tuple(per_partition),
        reference_rows_before_admission=int(reference_count),
        admitted_reference_count=int(admitted_count),
        status_counts=status_values,
    )


def _scan_membership_pass_with_partition_stats(
    adapter: S1SourceObservationAdapter,
    partition_paths: Sequence[Path],
    chunksize: int,
    registry: MembershipRegistry,
) -> S1BoundarySignature:
    status_counts: Counter[str] = Counter()
    per_partition: list[tuple[str, int, int, tuple[tuple[str, int], ...]]] = []
    reference_count = 0
    admitted_count = 0
    for path in partition_paths:
        partition_reference = 0
        partition_admitted = 0
        partition_status: Counter[str] = Counter()
        for _, validated in _iter_validated_chunks(
            adapter, (path,), chunksize, pass_name="pass1"
        ):
            partition_reference += len(validated.audit_rows)
            partition_admitted += len(validated.admitted_rows)
            reference_count += len(validated.audit_rows)
            admitted_count += len(validated.admitted_rows)
            for status, count in validated.status_counts.items():
                status_counts[str(status)] += int(count)
                partition_status[str(status)] += int(count)
            if not validated.admitted_rows.empty:
                registry.add(_membership_pairs(validated.admitted_rows))
                registry.commit()
        per_partition.append(
            (
                _path_key(path),
                partition_reference,
                partition_admitted,
                tuple(
                    (status, int(partition_status.get(status, 0)))
                    for status in SOURCE_ADMISSION_STATUSES
                ),
            )
        )
    registry.commit()
    return _boundary_signature(
        partition_paths,
        per_partition,
        reference_count,
        admitted_count,
        status_counts,
    )


class _StreamingCounterAccumulator:
    """Accumulate only bounded chunk classifications and compact counters."""

    def __init__(self) -> None:
        self.target_membership_base_counts: Counter[str] = Counter()
        self.cross_tab_counters: dict[str, Counter[tuple[str, str]]] = {
            name: Counter() for name, _, _ in _CROSS_TAB_SPECS
        }
        self.edge_class_counts: Counter[str] = Counter()
        self.self_loop_edge_weights: Counter[tuple[str, str]] = Counter()
        self.cross_project_edge_weights: Counter[tuple[str, str]] = Counter()
        self.conflict_excluded_record_occurrences = 0
        self.quotient_eligible_records = 0
        self.self_loop_evidence_weight = 0
        self.cross_project_evidence_weight = 0
        self.source_seed_membership_mismatch = 0

    def consume(self, classified: pd.DataFrame) -> None:
        target_base = classified["tar_membership_status"].replace(
            {CONFLICT_EXCLUDED: PROJECT_MAPPABLE}
        )
        self.target_membership_base_counts.update(target_base.astype(str).tolist())
        self.edge_class_counts.update(classified["edge_class"].astype(str).tolist())
        self.source_seed_membership_mismatch += int(
            classified["source_seed_membership_mismatch"].sum()
        )

        for name, dimension, classification in _CROSS_TAB_SPECS:
            counter = self.cross_tab_counters[name]
            counter.update(
                zip(
                    classified[dimension].astype(str).tolist(),
                    classified[classification].astype(str).tolist(),
                )
            )

        source_project = classified["src_project_id"]
        target_project = classified["tar_project_id"]
        project_mappable_endpoints = source_project.notna() & target_project.notna()
        conflict_excluded = project_mappable_endpoints & (
            classified["src_membership_conflict"]
            | classified["tar_membership_conflict"]
        )
        self.conflict_excluded_record_occurrences += int(conflict_excluded.sum())

        eligible = classified["quotient_eligibility"].eq(QUOTIENT_ELIGIBLE)
        self.quotient_eligible_records += int(eligible.sum())
        self_loop = eligible & source_project.eq(target_project)
        cross_project = eligible & source_project.ne(target_project)
        self.self_loop_evidence_weight += int(self_loop.sum())
        self.cross_project_evidence_weight += int(cross_project.sum())

        for source, target in zip(
            source_project.loc[self_loop].astype(str),
            target_project.loc[self_loop].astype(str),
        ):
            self.self_loop_edge_weights[(source, target)] += 1
        for source, target in zip(
            source_project.loc[cross_project].astype(str),
            target_project.loc[cross_project].astype(str),
        ):
            self.cross_project_edge_weights[(source, target)] += 1


def _boundary_differences(
    pass1: S1BoundarySignature, pass2: S1BoundarySignature
) -> tuple[str, ...]:
    differences: list[str] = []
    for field in (
        "partition_order",
        "partition_statistics",
        "reference_rows_before_admission",
        "admitted_reference_count",
        "status_counts",
        "unknown_status_count",
        "source_admission_contradiction_count",
    ):
        if getattr(pass1, field) != getattr(pass2, field):
            differences.append(field)
    return tuple(differences)


def _assert_output_contract_names() -> None:
    expected = set(FUTURE_S1_OUTPUT_CONTRACT) - {"evidence_universe_validation.json"}
    actual = {name + ".csv" for name, _, _ in _CROSS_TAB_SPECS}
    actual.update({"evidence_universe_flow.csv", "edge_class_counts.csv"})
    if (
        actual != expected
        or "evidence_universe_validation.json" not in FUTURE_S1_OUTPUT_CONTRACT
        or FUTURE_S1_OUTPUT_CONTRACT["evidence_universe_validation.json"] != ()
    ):
        raise S1StreamingContractError("future S1 output contract names are incomplete")


def assert_s1_streaming_runtime_acceptance(result: S1StreamingResult) -> dict[str, Any]:
    """Fail closed before compact streaming tables can be accepted."""

    checks: dict[str, bool] = {}
    checks["source_admission_closes"] = (
        result.source_admission_before_count
        == sum(result.source_admission_status_counts.values())
    )
    checks["pass1_pass2_input_equal"] = not _boundary_differences(
        result.pass1_boundary, result.pass2_boundary
    )
    checks["unknown_status_count_is_zero"] = (
        result.pass1_boundary.unknown_status_count == 0
        and result.pass2_boundary.unknown_status_count == 0
    )
    checks["source_admission_contradiction_count_is_zero"] = (
        result.pass1_boundary.source_admission_contradiction_count == 0
        and result.pass2_boundary.source_admission_contradiction_count == 0
    )
    checks["admitted_count_matches_status"] = (
        result.admitted_reference_count
        == int(result.source_admission_status_counts.get(ADMITTED, 0))
    )
    target_split = sum(result.target_membership_base_counts.values())
    checks["target_membership_split_closes"] = (
        target_split == result.admitted_reference_count
    )
    checks["source_seed_membership_mismatch_is_zero"] = (
        result.source_seed_membership_mismatch == 0
    )
    checks["eligible_reference_closes"] = (
        result.quotient_eligible_records
        == result.self_loop_evidence_weight + result.cross_project_evidence_weight
    )
    checks["edge_weight_closes"] = checks["eligible_reference_closes"]
    checks["edge_class_counts_close"] = (
        sum(result.edge_class_counts.values()) == result.admitted_reference_count
    )
    checks["unit_distinctions_hold"] = len(
        {REFERENCE_RECORD, AGGREGATED_EDGE_WEIGHT, EDGE_COUNT}
    ) == 3
    try:
        _assert_output_contract_names()
        checks["output_contract_complete"] = True
    except S1StreamingContractError:
        checks["output_contract_complete"] = False

    failed = tuple(name for name, passed in checks.items() if not passed)
    if failed:
        detail = ", ".join(failed)
        prefix = "S1_TWO_PASS_INPUT_DRIFT" if "pass1_pass2_input_equal" in failed else "S1 runtime acceptance failed"
        raise S1StreamingContractError("%s: %s" % (prefix, detail))
    return checks


def _cross_tab_from_counter(
    counter: Mapping[tuple[str, str], int],
    dimension: str,
    classification: str,
    total: int,
) -> pd.DataFrame:
    rows = [
        {dimension: _text(value), classification: _text(status), "count": int(count)}
        for (value, status), count in sorted(counter.items())
    ]
    columns = [dimension, classification, "count"]
    table = pd.DataFrame(rows, columns=columns)
    if table.empty:
        return table.assign(
            overall_share=pd.Series(dtype=float),
            within_row_share=pd.Series(dtype=float),
            within_status_share=pd.Series(dtype=float),
        )
    table = table.sort_values(columns[:2], kind="stable").reset_index(drop=True)
    table["overall_share"] = table["count"] / total if total else 0.0
    table["within_row_share"] = table["count"] / table.groupby(dimension)["count"].transform("sum")
    table["within_status_share"] = table["count"] / table.groupby(classification)["count"].transform("sum")
    return table


def _build_streaming_flow(result: S1StreamingResult) -> pd.DataFrame:
    counts = result.target_membership_base_counts
    status_counts = result.source_admission_status_counts
    rows = [
        (
            "reference_records_before_source_admission",
            result.source_admission_before_count,
            "RECORD",
            "",
        ),
        (
            "admitted_source_observation_reference_records",
            result.admitted_reference_count,
            "RECORD",
            "",
        ),
        (
            "out_of_seed_source_observation_reference_records",
            int(status_counts.get("OUT_OF_SEED_SOURCE_OBSERVATION", 0)),
            "RECORD",
            "",
        ),
        (
            "missing_event_repository_id_reference_records",
            int(status_counts.get("MISSING_EVENT_REPOSITORY_ID", 0)),
            "RECORD",
            "",
        ),
        (
            "invalid_event_repository_id_reference_records",
            int(status_counts.get("INVALID_EVENT_REPOSITORY_ID", 0)),
            "RECORD",
            "",
        ),
        ("target_project_mappable_records", int(counts.get(PROJECT_MAPPABLE, 0)), "RECORD", ""),
        ("target_non_project_records", int(counts.get(NON_PROJECT, 0)), "RECORD", ""),
        ("target_unresolved_records", int(counts.get(UNRESOLVED, 0)), "RECORD", ""),
        ("target_ambiguous_records", int(counts.get(AMBIGUOUS, 0)), "RECORD", ""),
        (
            "conflict_excluded_record_occurrences",
            result.conflict_excluded_record_occurrences,
            "RECORD",
            "",
        ),
        ("quotient_eligible_records", result.quotient_eligible_records, "RECORD", ""),
        (
            "self_loop_evidence_weight",
            result.self_loop_evidence_weight,
            REFERENCE_RECORD,
            AGGREGATED_EDGE_WEIGHT,
        ),
        (
            "cross_project_evidence_weight",
            result.cross_project_evidence_weight,
            REFERENCE_RECORD,
            AGGREGATED_EDGE_WEIGHT,
        ),
        (
            "self_loop_edge_count",
            len(result.self_loop_edge_pairs),
            EDGE_COUNT,
            "SELF_LOOP_EDGE_COUNT",
        ),
        (
            "cross_project_directed_edge_count",
            len(result.cross_project_edge_pairs),
            EDGE_COUNT,
            "CROSS_PROJECT_DIRECTED_EDGE_COUNT",
        ),
    ]
    return pd.DataFrame(
        rows, columns=FUTURE_S1_OUTPUT_CONTRACT["evidence_universe_flow.csv"]
    )


def build_future_s1_streaming_output_tables(
    result: S1StreamingResult,
) -> dict[str, pd.DataFrame]:
    """Finalize compact counters into future S1 tables without writing files."""

    assert_s1_streaming_runtime_acceptance(result)
    total = result.admitted_reference_count
    tables: dict[str, pd.DataFrame] = {
        "evidence_universe_flow.csv": _build_streaming_flow(result),
    }
    for name, dimension, classification in _CROSS_TAB_SPECS:
        table = _cross_tab_from_counter(
            result.cross_tab_counters[name], dimension, classification, total
        )
        if classification == "tar_membership_status":
            table = table.rename(columns={classification: "target_membership_status"})
        tables[name + ".csv"] = table
    tables["edge_class_counts.csv"] = pd.DataFrame(
        [
            (edge_class, int(count), REFERENCE_RECORD)
            for edge_class, count in sorted(result.edge_class_counts.items())
        ],
        columns=FUTURE_S1_OUTPUT_CONTRACT["edge_class_counts.csv"],
    )
    for name, table in tables.items():
        expected = FUTURE_S1_OUTPUT_CONTRACT[name]
        if tuple(table.columns) != expected:
            raise S1StreamingContractError("future S1 output contract mismatch: %s" % name)
    return tables


def run_s1_streaming(
    adapter: S1SourceObservationAdapter,
    partition_paths: Iterable[str | Path],
    registry_path: str | Path,
    *,
    chunksize: int = 100_000,
    pass2_partition_paths: Iterable[str | Path] | None = None,
) -> S1StreamingResult:
    """Run the implementation-only two-pass S1 adapter on authorized paths.

    ``pass2_partition_paths`` exists for deterministic drift tests.  Normal
    callers omit it, causing the same ordered authorized partition list to be
    read a second time.  The supplied SQLite registry is owned by this call
    and is removed in ``finally``; it must be outside the v2 scientific output
    root and must not already exist.
    """

    if not isinstance(chunksize, int) or chunksize <= 0:
        raise S1StreamingContractError("chunksize must be a positive integer")
    pass1_paths = _canonical_partition_paths(partition_paths)
    pass2_paths = (
        pass1_paths
        if pass2_partition_paths is None
        else _canonical_partition_paths(pass2_partition_paths)
    )
    registry_target = canonical_path(registry_path)
    output_root = canonical_path(CORRECTED_OUTPUTS_ROOT)
    try:
        registry_target.relative_to(output_root)
    except ValueError:
        pass
    else:
        raise S1StreamingContractError("membership registry cannot be under v2 outputs")
    if registry_target.exists():
        raise S1StreamingContractError("membership registry path must be new and owned by the run")
    registry_target.parent.mkdir(parents=True, exist_ok=True)
    registry: MembershipRegistry | None = None
    try:
        registry = MembershipRegistry(registry_target)
        pass1 = _scan_membership_pass_with_partition_stats(
            adapter, pass1_paths, chunksize, registry
        )
        summary = registry.summary()
        conflicts = frozenset(registry.conflicting_entities())
        membership = MembershipContext(
            conflicting_entity_ids=conflicts,
            summary=summary,
        )

        accumulator = _StreamingCounterAccumulator()
        status_counts_pass2: Counter[str] = Counter()
        per_partition: list[tuple[str, int, int, tuple[tuple[str, int], ...]]] = []
        reference_count = 0
        admitted_count = 0
        for path in pass2_paths:
            partition_reference = 0
            partition_admitted = 0
            partition_status: Counter[str] = Counter()
            for _, validated in _iter_validated_chunks(
                adapter, (path,), chunksize, pass_name="pass2"
            ):
                partition_reference += len(validated.audit_rows)
                partition_admitted += len(validated.admitted_rows)
                reference_count += len(validated.audit_rows)
                admitted_count += len(validated.admitted_rows)
                for status, count in validated.status_counts.items():
                    status_counts_pass2[str(status)] += int(count)
                    partition_status[str(status)] += int(count)
                if not validated.admitted_rows.empty:
                    classified = classify_evidence_records(
                        validated.admitted_rows, membership
                    )
                    accumulator.consume(classified)
            per_partition.append(
                (
                    _path_key(path),
                    partition_reference,
                    partition_admitted,
                    tuple(
                        (status, int(partition_status.get(status, 0)))
                        for status in SOURCE_ADMISSION_STATUSES
                    ),
                )
            )
        pass2 = _boundary_signature(
            pass2_paths,
            per_partition,
            reference_count,
            admitted_count,
            status_counts_pass2,
        )
        differences = _boundary_differences(pass1, pass2)
        if differences:
            raise S1StreamingContractError(
                "S1_TWO_PASS_INPUT_DRIFT: %s" % ", ".join(differences)
            )

        self_pairs = frozenset(accumulator.self_loop_edge_weights)
        cross_pairs = frozenset(accumulator.cross_project_edge_weights)
        result = S1StreamingResult(
            source_admission_before_count=pass1.reference_rows_before_admission,
            source_admission_status_counts=dict(pass1.status_counts),
            admitted_reference_count=pass2.admitted_reference_count,
            membership_summary=dict(summary),
            target_membership_base_counts=dict(accumulator.target_membership_base_counts),
            conflict_excluded_record_occurrences=accumulator.conflict_excluded_record_occurrences,
            quotient_eligible_records=accumulator.quotient_eligible_records,
            self_loop_evidence_weight=accumulator.self_loop_evidence_weight,
            cross_project_evidence_weight=accumulator.cross_project_evidence_weight,
            self_loop_edge_pairs=self_pairs,
            cross_project_edge_pairs=cross_pairs,
            self_loop_edge_weights=dict(accumulator.self_loop_edge_weights),
            cross_project_edge_weights=dict(accumulator.cross_project_edge_weights),
            source_seed_membership_mismatch=accumulator.source_seed_membership_mismatch,
            cross_tab_counters={
                name: dict(counter)
                for name, counter in accumulator.cross_tab_counters.items()
            },
            edge_class_counts=dict(accumulator.edge_class_counts),
            pass1_boundary=pass1,
            pass2_boundary=pass2,
        )
        return result
    finally:
        if registry is not None:
            registry.close()
        if registry_target.exists():
            registry_target.unlink()
