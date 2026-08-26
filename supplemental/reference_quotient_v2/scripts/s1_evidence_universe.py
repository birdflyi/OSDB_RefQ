"""Corrected S1 evidence-universe computation without runtime output execution.

This C3.7-B2 module accepts only the C3.7-B admitted source-observation
interface.  It implements the historical S1 membership, evidence, and unit
semantics as pure DataFrame transformations, without reading aggregate files,
writing outputs, selecting S7 objects, or executing a scientific regeneration.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Iterable, Mapping

import pandas as pd

from script.ch5_reference_quotient.membership import (
    canonical_project_entity_identity,
    classify_membership,
    unique_project_membership,
)

from .s1_adapter import ADMITTED, ValidatedReferenceChunk


REFERENCE_RECORD = "REFERENCE_RECORD"
AGGREGATED_EDGE_WEIGHT = "AGGREGATED_EDGE_WEIGHT"
EDGE_COUNT = "EDGE_COUNT"
QUOTIENT_ELIGIBLE = "QUOTIENT_ELIGIBLE"
NOT_QUOTIENT_ELIGIBLE = "NOT_QUOTIENT_ELIGIBLE"
PROJECT_MAPPABLE = "PROJECT_MAPPABLE"
NON_PROJECT = "NON_PROJECT"
UNRESOLVED = "UNRESOLVED"
AMBIGUOUS = "AMBIGUOUS"
CONFLICT_EXCLUDED = "CONFLICT_EXCLUDED"
SELF_INTERNAL_PROJECT_REFERENCE = "SELF_INTERNAL_PROJECT_REFERENCE"
CROSS_PROJECT_REFERENCE = "CROSS_PROJECT_REFERENCE"
NOT_QUOTIENT_ELIGIBLE_REFERENCE = "NOT_QUOTIENT_ELIGIBLE_REFERENCE"


class S1EvidenceUniverseContractError(ValueError):
    """Raised when a prospective S1 analytical input is not admitted-only."""


ANALYTICAL_COLUMNS: tuple[str, ...] = (
    "event_id",
    "event_repo_id",
    "expected_source_context_repo_id",
    "source_admission_status",
    "source_provenance_mismatch",
    "authoritative_seed_project",
    "relation_type",
    "event_type",
    "src_entity_id",
    "src_entity_type",
    "tar_entity_id",
    "tar_entity_type",
    "src_entity_id_agg",
    "src_entity_type_agg",
    "tar_entity_id_agg",
    "tar_entity_type_agg",
    "tar_entity_type_fine_grained",
)

FUTURE_S1_OUTPUT_CONTRACT: Mapping[str, tuple[str, ...]] = {
    "evidence_universe_flow.csv": ("stage", "count", "unit", "measure"),
    "event_type_x_target_membership_status.csv": (
        "event_type", "target_membership_status", "count", "overall_share", "within_row_share", "within_status_share",
    ),
    "source_entity_type_x_target_membership_status.csv": (
        "source_entity_type", "target_membership_status", "count", "overall_share", "within_row_share", "within_status_share",
    ),
    "target_entity_type_x_target_membership_status.csv": (
        "target_entity_type", "target_membership_status", "count", "overall_share", "within_row_share", "within_status_share",
    ),
    "event_type_x_quotient_eligibility.csv": (
        "event_type", "quotient_eligibility", "count", "overall_share", "within_row_share", "within_status_share",
    ),
    "source_entity_type_x_quotient_eligibility.csv": (
        "source_entity_type", "quotient_eligibility", "count", "overall_share", "within_row_share", "within_status_share",
    ),
    "target_entity_type_x_quotient_eligibility.csv": (
        "target_entity_type", "quotient_eligibility", "count", "overall_share", "within_row_share", "within_status_share",
    ),
    "edge_class_counts.csv": ("edge_class", "count", "unit"),
    "evidence_universe_validation.json": (),
}


@dataclass(frozen=True)
class MembershipContext:
    """Single-valued membership audit derived solely from admitted rows."""

    conflicting_entity_ids: frozenset[str]
    summary: Mapping[str, int]


@dataclass(frozen=True)
class S1EvidenceUniverse:
    """Pure S1 computation result and future-output table inputs."""

    records: pd.DataFrame
    membership: MembershipContext
    source_admission_status_counts: Mapping[str, int]
    source_admission_before_count: int
    edge_class_counts: Mapping[str, int]
    directed_edge_counts: Mapping[str, int]


def _text(value: Any) -> str:
    if value is None or pd.isna(value):
        return "UNKNOWN"
    text = str(value).strip()
    return text if text else "UNKNOWN"


def _status_label(aggregate: Any, aggregate_type: Any) -> str:
    return {
        "project_mappable": PROJECT_MAPPABLE,
        "non_project": NON_PROJECT,
        "unresolved": UNRESOLVED,
        "ambiguous": AMBIGUOUS,
    }[classify_membership(aggregate, aggregate_type)]


def require_admitted_reference_records(records: pd.DataFrame) -> pd.DataFrame:
    """Fail closed unless records satisfy the C3.7-B admitted analytical view."""

    missing = tuple(column for column in ANALYTICAL_COLUMNS if column not in records.columns)
    if missing:
        raise S1EvidenceUniverseContractError(
            "S1 analytical input is missing admitted-view fields: %s" % ", ".join(missing)
        )
    work = records.copy()
    if not work["relation_type"].eq("Reference").all():
        raise S1EvidenceUniverseContractError("S1 analytical input contains a non-Reference row")
    admitted = work["source_admission_status"].eq(ADMITTED)
    mismatch = work["source_provenance_mismatch"].eq(False)
    same_event_context = work["event_repo_id"].eq(work["expected_source_context_repo_id"])
    same_context_seed = work["expected_source_context_repo_id"].eq(work["authoritative_seed_project"])
    if not bool((admitted & mismatch & same_event_context & same_context_seed).all()):
        raise S1EvidenceUniverseContractError(
            "S1 analytical input contains a row outside the admitted source-observation view"
        )
    return work


def admitted_records_from_chunks(chunks: Iterable[ValidatedReferenceChunk]) -> tuple[pd.DataFrame, dict[str, int], int]:
    """Collect admitted-only records and source-admission audit counts from B1 chunks."""

    admitted_frames: list[pd.DataFrame] = []
    counts: Counter[str] = Counter()
    for chunk in chunks:
        for status, count in chunk.status_counts.items():
            counts[str(status)] += int(count)
        if not chunk.admitted_rows.empty:
            admitted_frames.append(require_admitted_reference_records(chunk.admitted_rows))
    if not admitted_frames:
        empty = pd.DataFrame(columns=ANALYTICAL_COLUMNS)
        return empty, dict(counts), int(sum(counts.values()))
    records = pd.concat(admitted_frames, ignore_index=True)
    return records, dict(counts), int(sum(counts.values()))


def build_membership_context(records: pd.DataFrame) -> MembershipContext:
    """Apply the shared RefQ membership identity and global conflict semantics."""

    work = require_admitted_reference_records(records)
    pairs: set[tuple[str, str]] = set()
    for side in ("src", "tar"):
        for entity_id, aggregate in zip(work[f"{side}_entity_id"], work[f"{side}_entity_id_agg"]):
            identity = canonical_project_entity_identity(entity_id, aggregate)
            project = unique_project_membership(aggregate)
            if identity is not None and project is not None:
                pairs.add((identity, project))
    by_entity: dict[str, set[str]] = {}
    for identity, project in pairs:
        by_entity.setdefault(identity, set()).add(project)
    conflicting = frozenset(identity for identity, projects in by_entity.items() if len(projects) > 1)
    unique_entities = len(by_entity)
    conflict_count = len(conflicting)
    summary = {
        "unique_project_mappable_entities": unique_entities,
        "membership_conflict_entities": conflict_count,
        "retained_single_membership_entities": unique_entities - conflict_count,
        "maximum_memberships_per_entity": max((len(projects) for projects in by_entity.values()), default=0),
        "maximum_memberships_per_retained_entity": 1 if unique_entities > conflict_count else 0,
    }
    return MembershipContext(conflicting_entity_ids=conflicting, summary=summary)


def classify_evidence_records(records: pd.DataFrame, membership: MembershipContext) -> pd.DataFrame:
    """Classify admitted Reference records with the unchanged RefQ eligibility rule."""

    work = require_admitted_reference_records(records)
    result = work.copy()
    for side in ("src", "tar"):
        aggregate = result[f"{side}_entity_id_agg"]
        aggregate_type = result[f"{side}_entity_type_agg"]
        result[f"{side}_project_id"] = aggregate.map(unique_project_membership).astype("string")
        result[f"{side}_canonical_entity_id"] = pd.Series(
            [
                canonical_project_entity_identity(entity_id, aggregate_id)
                for entity_id, aggregate_id in zip(result[f"{side}_entity_id"], aggregate)
            ],
            index=result.index,
            dtype="string",
        )
        result[f"{side}_membership_status"] = pd.Series(
            [_status_label(value, kind) for value, kind in zip(aggregate, aggregate_type)],
            index=result.index,
            dtype="string",
        )
        project_mappable = result[f"{side}_project_id"].notna()
        conflict = project_mappable & result[f"{side}_canonical_entity_id"].isin(membership.conflicting_entity_ids)
        result[f"{side}_membership_conflict"] = conflict.astype(bool)
        result.loc[conflict, f"{side}_membership_status"] = CONFLICT_EXCLUDED

    source_valid = result["src_project_id"].notna()
    target_valid = result["tar_project_id"].notna()
    eligible = source_valid & target_valid & ~result["src_membership_conflict"] & ~result["tar_membership_conflict"]
    result["quotient_eligibility"] = pd.Series(
        [QUOTIENT_ELIGIBLE if value else NOT_QUOTIENT_ELIGIBLE for value in eligible],
        index=result.index,
        dtype="string",
    )
    result["edge_class"] = pd.Series(NOT_QUOTIENT_ELIGIBLE_REFERENCE, index=result.index, dtype="string")
    result.loc[eligible & result["src_project_id"].eq(result["tar_project_id"]), "edge_class"] = SELF_INTERNAL_PROJECT_REFERENCE
    result.loc[eligible & result["src_project_id"].ne(result["tar_project_id"]), "edge_class"] = CROSS_PROJECT_REFERENCE
    result["source_seed_membership_mismatch"] = (
        source_valid & result["src_project_id"].ne(result["authoritative_seed_project"])
    ).astype(bool)
    result["target_entity_type"] = result["tar_entity_type_fine_grained"].fillna(
        result["tar_entity_type"]
    ).map(_text)
    result["source_entity_type"] = result["src_entity_type"].map(_text)
    result["event_type"] = result["event_type"].map(_text)
    return result


def compute_evidence_universe(chunks: Iterable[ValidatedReferenceChunk]) -> S1EvidenceUniverse:
    """Compute the future S1 evidence universe from C3.7-B validated chunks."""

    records, status_counts, before_count = admitted_records_from_chunks(chunks)
    membership = build_membership_context(records)
    classified = classify_evidence_records(records, membership)
    edge_class_counts = Counter(classified["edge_class"].astype(str))
    eligible = classified.loc[classified["quotient_eligibility"].eq(QUOTIENT_ELIGIBLE)]
    directed_edge_counts = {
        "self_loop_edge_count": int(
            eligible.loc[eligible["edge_class"].eq(SELF_INTERNAL_PROJECT_REFERENCE), ["src_project_id", "tar_project_id"]]
            .drop_duplicates()
            .shape[0]
        ),
        "cross_project_directed_edge_count": int(
            eligible.loc[eligible["edge_class"].eq(CROSS_PROJECT_REFERENCE), ["src_project_id", "tar_project_id"]]
            .drop_duplicates()
            .shape[0]
        ),
    }
    return S1EvidenceUniverse(
        records=classified,
        membership=membership,
        source_admission_status_counts=status_counts,
        source_admission_before_count=before_count,
        edge_class_counts={key: int(value) for key, value in sorted(edge_class_counts.items())},
        directed_edge_counts=directed_edge_counts,
    )


def cross_tab(records: pd.DataFrame, dimension: str, classification: str) -> pd.DataFrame:
    """Build a Reference-record cross-tab with historical share semantics."""

    records = require_admitted_reference_records(records)
    if dimension not in records.columns or classification not in records.columns:
        raise KeyError("cross-tab columns are unavailable")
    columns = [dimension, classification]
    table = records.groupby(columns, dropna=False).size().rename("count").reset_index()
    table[dimension] = table[dimension].map(_text)
    table[classification] = table[classification].map(_text)
    table = table.sort_values(columns, kind="stable").reset_index(drop=True)
    total = int(len(records))
    if table.empty:
        return table.assign(
            overall_share=pd.Series(dtype=float),
            within_row_share=pd.Series(dtype=float),
            within_status_share=pd.Series(dtype=float),
        )
    table["overall_share"] = table["count"] / total if total else 0.0
    table["within_row_share"] = table["count"] / table.groupby(dimension)["count"].transform("sum")
    table["within_status_share"] = table["count"] / table.groupby(classification)["count"].transform("sum")
    return table


def composition_table(records: pd.DataFrame, object_column: str, dimensions: Iterable[str]) -> pd.DataFrame:
    """Aggregate Reference-record composition without selecting any S7 object set."""

    work = require_admitted_reference_records(records)
    if object_column not in work.columns:
        raise KeyError("composition object column is unavailable: %s" % object_column)
    rows: list[pd.DataFrame] = []
    for dimension in dimensions:
        if dimension not in work.columns:
            raise KeyError("composition dimension is unavailable: %s" % dimension)
        grouped = work.groupby([object_column, dimension], dropna=False).size().rename("count").reset_index()
        grouped = grouped.rename(columns={dimension: "category"})
        grouped["dimension"] = dimension
        grouped[object_column] = grouped[object_column].map(_text)
        grouped["category"] = grouped["category"].map(_text)
        rows.append(grouped[[object_column, "dimension", "category", "count"]])
    if not rows:
        return pd.DataFrame(columns=[object_column, "dimension", "category", "count", "within_object_share"])
    result = pd.concat(rows, ignore_index=True)
    result["within_object_share"] = result["count"] / result.groupby([object_column, "dimension"])["count"].transform("sum")
    return result.sort_values([object_column, "dimension", "category"], kind="stable").reset_index(drop=True)


def build_evidence_universe_flow(result: S1EvidenceUniverse) -> pd.DataFrame:
    """Construct, but do not write, the unit-explicit future S1 flow table."""

    records = result.records
    target_base = records["tar_membership_status"].replace({CONFLICT_EXCLUDED: PROJECT_MAPPABLE})
    conflict_records = records["src_membership_conflict"] | records["tar_membership_conflict"]
    rows = [
        ("reference_records_before_source_admission", result.source_admission_before_count, "RECORD", ""),
        ("admitted_source_observation_reference_records", len(records), "RECORD", ""),
        ("out_of_seed_source_observation_reference_records", result.source_admission_status_counts.get("OUT_OF_SEED_SOURCE_OBSERVATION", 0), "RECORD", ""),
        ("missing_event_repository_id_reference_records", result.source_admission_status_counts.get("MISSING_EVENT_REPOSITORY_ID", 0), "RECORD", ""),
        ("invalid_event_repository_id_reference_records", result.source_admission_status_counts.get("INVALID_EVENT_REPOSITORY_ID", 0), "RECORD", ""),
        ("target_project_mappable_records", int(target_base.eq(PROJECT_MAPPABLE).sum()), "RECORD", ""),
        ("target_non_project_records", int(target_base.eq(NON_PROJECT).sum()), "RECORD", ""),
        ("target_unresolved_records", int(target_base.eq(UNRESOLVED).sum()), "RECORD", ""),
        ("target_ambiguous_records", int(target_base.eq(AMBIGUOUS).sum()), "RECORD", ""),
        ("conflict_excluded_record_occurrences", int(conflict_records.sum()), "RECORD", ""),
        ("quotient_eligible_records", int(records["quotient_eligibility"].eq(QUOTIENT_ELIGIBLE).sum()), "RECORD", ""),
        ("self_loop_evidence_weight", int(result.edge_class_counts.get(SELF_INTERNAL_PROJECT_REFERENCE, 0)), REFERENCE_RECORD, AGGREGATED_EDGE_WEIGHT),
        ("cross_project_evidence_weight", int(result.edge_class_counts.get(CROSS_PROJECT_REFERENCE, 0)), REFERENCE_RECORD, AGGREGATED_EDGE_WEIGHT),
        ("self_loop_edge_count", int(result.directed_edge_counts["self_loop_edge_count"]), EDGE_COUNT, "SELF_LOOP_EDGE_COUNT"),
        ("cross_project_directed_edge_count", int(result.directed_edge_counts["cross_project_directed_edge_count"]), EDGE_COUNT, "CROSS_PROJECT_DIRECTED_EDGE_COUNT"),
    ]
    return pd.DataFrame(rows, columns=FUTURE_S1_OUTPUT_CONTRACT["evidence_universe_flow.csv"])


def reconcile_evidence_universe(result: S1EvidenceUniverse) -> dict[str, Any]:
    """Return generic closure checks for a future authorized corrected S1 run."""

    records = result.records
    flow = build_evidence_universe_flow(result).set_index("stage")["count"]
    status_total = int(sum(result.source_admission_status_counts.values()))
    admitted = int(len(records))
    eligible = int(records["quotient_eligibility"].eq(QUOTIENT_ELIGIBLE).sum())
    self_weight = int(result.edge_class_counts.get(SELF_INTERNAL_PROJECT_REFERENCE, 0))
    cross_weight = int(result.edge_class_counts.get(CROSS_PROJECT_REFERENCE, 0))
    target_split = sum(
        int(flow[name])
        for name in (
            "target_project_mappable_records",
            "target_non_project_records",
            "target_unresolved_records",
            "target_ambiguous_records",
        )
    )
    return {
        "reference_records_before_source_admission": result.source_admission_before_count,
        "admitted_source_observation_reference_records": admitted,
        "source_admission_status_total": status_total,
        "source_admission_closes": result.source_admission_before_count == status_total,
        "admitted_count_matches_status": admitted == int(result.source_admission_status_counts.get(ADMITTED, 0)),
        "target_membership_split_closes": target_split == admitted,
        "quotient_eligible_records": eligible,
        "source_mismatch_after_admission": int(records["source_seed_membership_mismatch"].sum()),
        "source_mismatch_after_admission_is_zero": not bool(records["source_seed_membership_mismatch"].any()),
        "self_loop_evidence_weight": self_weight,
        "cross_project_evidence_weight": cross_weight,
        "edge_weight_closes": self_weight + cross_weight == eligible,
        "self_loop_edge_count": int(result.directed_edge_counts["self_loop_edge_count"]),
        "cross_project_directed_edge_count": int(result.directed_edge_counts["cross_project_directed_edge_count"]),
        "reference_record_unit": REFERENCE_RECORD,
        "aggregated_edge_weight_measure": AGGREGATED_EDGE_WEIGHT,
        "edge_count_unit": EDGE_COUNT,
    }


def assert_s1_runtime_acceptance(result: S1EvidenceUniverse) -> dict[str, Any]:
    """Fail closed before a future S1 writer can accept analytical tables."""

    reconciliation = reconcile_evidence_universe(result)
    mandatory_checks = (
        "source_admission_closes",
        "admitted_count_matches_status",
        "target_membership_split_closes",
        "source_mismatch_after_admission_is_zero",
        "edge_weight_closes",
    )
    failed = tuple(name for name in mandatory_checks if not reconciliation[name])
    if failed:
        raise S1EvidenceUniverseContractError(
            "S1 runtime acceptance failed: %s" % ", ".join(failed)
        )
    return reconciliation


def build_future_s1_output_tables(result: S1EvidenceUniverse) -> dict[str, pd.DataFrame]:
    """Construct future S1 tables in memory; this function deliberately never writes."""

    assert_s1_runtime_acceptance(result)
    records = result.records
    tables = {
        "evidence_universe_flow.csv": build_evidence_universe_flow(result),
        "event_type_x_target_membership_status.csv": cross_tab(records, "event_type", "tar_membership_status").rename(columns={"tar_membership_status": "target_membership_status"}),
        "source_entity_type_x_target_membership_status.csv": cross_tab(records, "source_entity_type", "tar_membership_status").rename(columns={"tar_membership_status": "target_membership_status"}),
        "target_entity_type_x_target_membership_status.csv": cross_tab(records, "target_entity_type", "tar_membership_status").rename(columns={"tar_membership_status": "target_membership_status"}),
        "event_type_x_quotient_eligibility.csv": cross_tab(records, "event_type", "quotient_eligibility"),
        "source_entity_type_x_quotient_eligibility.csv": cross_tab(records, "source_entity_type", "quotient_eligibility"),
        "target_entity_type_x_quotient_eligibility.csv": cross_tab(records, "target_entity_type", "quotient_eligibility"),
        "edge_class_counts.csv": pd.DataFrame(
            [
                (edge_class, count, REFERENCE_RECORD)
                for edge_class, count in sorted(result.edge_class_counts.items())
            ],
            columns=FUTURE_S1_OUTPUT_CONTRACT["edge_class_counts.csv"],
        ),
    }
    for name, table in tables.items():
        expected = FUTURE_S1_OUTPUT_CONTRACT[name]
        if tuple(table.columns) != expected:
            raise S1EvidenceUniverseContractError("future S1 output contract mismatch: %s" % name)
    return tables
