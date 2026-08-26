"""Corrected S1 source-observation boundary adapter.

This C3.7-B module validates the corrected aggregate's materialized provenance
contract and exposes separated audit/admitted views. It does not build
membership, calculate quotient eligibility, construct edges, or write
scientific supplemental outputs.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import subprocess
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, Mapping, Optional, Sequence

import pandas as pd

from script.build_dataset.repository_identity_provenance import normalize_repository_id

from .manifest import load_json, sha256_file, validate_scaffold_provenance
from .paths import DEFAULT_CONFIG_PATH, PathGuardError, canonical_path, load_config
from .schema import (
    OPTIONAL_CORRECTED_PROVENANCE_FIELDS,
    REQUIRED_S1_SOURCE_BOUNDARY_FIELDS,
    SOURCE_ADMISSION_STATUSES,
    SchemaContractError,
    validate_s1_source_boundary_fields,
    validate_source_admission_status,
)


ADMITTED = "ADMITTED_SOURCE_OBSERVATION"
OUT_OF_SEED = "OUT_OF_SEED_SOURCE_OBSERVATION"
MISSING = "MISSING_EVENT_REPOSITORY_ID"
INVALID = "INVALID_EVENT_REPOSITORY_ID"
CORRECTED_AGGREGATE_SCHEMA_VERSION = "reference_aggregate_schema_v2_event_repository_provenance"
FIREPROOF_CONTEXT = "679889516"
FIREPROOF_OUT_OF_SEED_EVENT_REPO = "600271677"


class SourceBoundaryContractError(ValueError):
    """Raised when a materialized corrected source-admission contract fails."""


@dataclass(frozen=True)
class SeedPartitionContext:
    """Authoritative numeric seed and corrected aggregate partition mapping."""

    seed_project: str
    evidence_path: Path


@dataclass(frozen=True)
class ValidatedReferenceChunk:
    """All Reference audit rows plus the strictly admitted analytical subset."""

    audit_rows: pd.DataFrame
    admitted_rows: pd.DataFrame
    status_counts: Mapping[str, int]


def _path_key(path: Path) -> str:
    return os.path.normcase(os.fspath(path))


def _is_within(candidate: Path, root: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _normalise_expected(value: Any) -> str:
    try:
        normalized = normalize_repository_id(value, field_name="expected_source_context_repo_id")
    except ValueError as exc:
        raise SourceBoundaryContractError(str(exc)) from exc
    if normalized is None:
        raise SourceBoundaryContractError("expected_source_context_repo_id is required")
    return normalized


def _normalise_event(value: Any) -> tuple[Optional[str], bool, bool]:
    try:
        normalized = normalize_repository_id(value, field_name="event_repo_id")
    except ValueError:
        return None, False, True
    return normalized, normalized is None, False


def _normalise_bool(value: Any, *, field_name: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1"}:
            return True
        if normalized in {"false", "0"}:
            return False
    raise SourceBoundaryContractError("%s must be a materialized boolean" % field_name)


def _validate_row(
    status: Any,
    event_value: Any,
    expected_value: Any,
    mismatch_value: Any,
    authoritative_seed_project: str,
) -> tuple[str, Optional[str], str, bool]:
    try:
        normalized_status = validate_source_admission_status(str(status))
    except (SchemaContractError, TypeError) as exc:
        raise SourceBoundaryContractError("unknown source_admission_status: %r" % status) from exc
    expected = _normalise_expected(expected_value)
    if expected != authoritative_seed_project:
        raise SourceBoundaryContractError(
            "expected_source_context_repo_id does not match authoritative current seed repository ID"
        )
    event, event_missing, event_invalid = _normalise_event(event_value)
    mismatch = _normalise_bool(mismatch_value, field_name="source_provenance_mismatch")

    if normalized_status == ADMITTED:
        if event_missing or event_invalid or event != expected or mismatch:
            raise SourceBoundaryContractError("admitted source-observation contract contradiction")
    elif normalized_status == OUT_OF_SEED:
        if event_missing or event_invalid or event == expected or not mismatch:
            raise SourceBoundaryContractError("out-of-seed source-observation contract contradiction")
    elif normalized_status == MISSING:
        if not event_missing or event_invalid or not mismatch:
            raise SourceBoundaryContractError("missing-event-repository source-observation contract contradiction")
    elif normalized_status == INVALID:
        # The corrected materialization replaces an invalid raw lexical value
        # with a null normalized ID and preserves its category in the status.
        # A later consumer cannot recover or accept the original invalid text.
        if not event_missing or event_invalid or not mismatch:
            raise SourceBoundaryContractError("invalid-event-repository source-observation contract contradiction")
    return normalized_status, event, expected, mismatch


def load_authoritative_seed_contexts(config: Mapping[str, Any]) -> tuple[Dict[str, SeedPartitionContext], Path]:
    """Load the P0-v2 seed manifest without reconstructing identity from names."""

    paths = validate_scaffold_provenance(config)
    p0_root = canonical_path(paths["corrected_p0_root"])
    aggregate_root = canonical_path(paths["corrected_aggregate_root"])
    p0_manifest = load_json(paths["corrected_p0_manifest"])
    seed_record = p0_manifest.get("seed_manifest")
    source_record = p0_manifest.get("source_repository")
    if not isinstance(seed_record, Mapping) or not isinstance(seed_record.get("path"), str):
        raise SourceBoundaryContractError("corrected P0 manifest has no seed manifest record")
    if not isinstance(source_record, Mapping) or not isinstance(source_record.get("path"), str):
        raise SourceBoundaryContractError("corrected P0 manifest has no source repository record")
    seed_manifest = canonical_path(seed_record["path"], p0_root)
    source_root = canonical_path(source_record["path"])
    if not _is_within(seed_manifest, p0_root) or not seed_manifest.is_file():
        raise SourceBoundaryContractError("corrected P0 seed manifest is not available under corrected P0 root")
    if not source_root.is_dir():
        raise SourceBoundaryContractError("corrected P0 source repository root is unavailable")

    contexts: Dict[str, SeedPartitionContext] = {}
    seed_ids: set[str] = set()
    with seed_manifest.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or {"repo_id", "evidence_path"} - set(reader.fieldnames):
            raise SourceBoundaryContractError("corrected P0 seed manifest lacks repo_id/evidence_path mapping")
        for row in reader:
            seed_project = _normalise_expected(row.get("repo_id"))
            evidence_text = str(row.get("evidence_path") or "").strip()
            if not evidence_text:
                raise SourceBoundaryContractError("corrected P0 seed manifest has a blank evidence_path")
            evidence_path = canonical_path(evidence_text, source_root)
            if not _is_within(evidence_path, aggregate_root):
                raise SourceBoundaryContractError("seed manifest partition is outside corrected aggregate authority")
            if not evidence_path.is_file():
                raise SourceBoundaryContractError("seed manifest partition does not exist: %s" % evidence_path)
            key = _path_key(evidence_path)
            if seed_project in seed_ids or key in contexts:
                raise SourceBoundaryContractError("corrected P0 seed manifest mapping is not one-to-one")
            seed_ids.add(seed_project)
            contexts[key] = SeedPartitionContext(seed_project=seed_project, evidence_path=evidence_path)
    expected_count = seed_record.get("count")
    if isinstance(expected_count, int) and len(contexts) != expected_count:
        raise SourceBoundaryContractError("corrected P0 seed manifest count does not close")
    return contexts, aggregate_root


class S1SourceObservationAdapter:
    """Validate corrected aggregate rows against a frozen seed context map."""

    def __init__(self, partition_contexts: Mapping[str, SeedPartitionContext], aggregate_root: str | Path) -> None:
        self._partition_contexts = dict(partition_contexts)
        self._aggregate_root = canonical_path(aggregate_root)

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "S1SourceObservationAdapter":
        contexts, aggregate_root = load_authoritative_seed_contexts(config)
        return cls(contexts, aggregate_root)

    @property
    def partition_count(self) -> int:
        return len(self._partition_contexts)

    def context_for_partition(self, partition_path: str | Path) -> SeedPartitionContext:
        candidate = canonical_path(partition_path)
        if not _is_within(candidate, self._aggregate_root):
            raise SourceBoundaryContractError("partition is outside corrected aggregate authority")
        try:
            return self._partition_contexts[_path_key(candidate)]
        except KeyError as exc:
            raise SourceBoundaryContractError(
                "partition is not authorized by the corrected P0 seed manifest mapping"
            ) from exc

    def validate_headers(self, fields: Iterable[str]) -> tuple[str, ...]:
        try:
            return validate_s1_source_boundary_fields(fields)
        except SchemaContractError as exc:
            raise SourceBoundaryContractError(str(exc)) from exc

    def validate_reference_chunk(self, partition_path: str | Path, chunk: pd.DataFrame) -> ValidatedReferenceChunk:
        context = self.context_for_partition(partition_path)
        self.validate_headers(chunk.columns)
        reference = chunk.loc[chunk["relation_type"].eq("Reference")].copy()
        if reference.empty:
            return ValidatedReferenceChunk(reference, reference, {status: 0 for status in SOURCE_ADMISSION_STATUSES})
        statuses: list[str] = []
        event_ids: list[Optional[str]] = []
        expected_ids: list[str] = []
        mismatches: list[bool] = []
        for row in reference[[
            "source_admission_status",
            "event_repo_id",
            "expected_source_context_repo_id",
            "source_provenance_mismatch",
        ]].itertuples(index=False, name=None):
            status, event, expected, mismatch = _validate_row(*row, context.seed_project)
            statuses.append(status)
            event_ids.append(event)
            expected_ids.append(expected)
            mismatches.append(mismatch)
        reference["source_admission_status"] = pd.Series(statuses, index=reference.index, dtype="string")
        reference["event_repo_id"] = pd.Series(event_ids, index=reference.index, dtype="string")
        reference["expected_source_context_repo_id"] = pd.Series(expected_ids, index=reference.index, dtype="string")
        reference["source_provenance_mismatch"] = pd.Series(mismatches, index=reference.index, dtype="bool")
        reference["authoritative_seed_project"] = context.seed_project
        if "aggregate_schema_version" in reference.columns:
            versions = set(reference["aggregate_schema_version"].dropna().astype(str))
            if versions != {CORRECTED_AGGREGATE_SCHEMA_VERSION}:
                raise SourceBoundaryContractError("corrected aggregate schema version is missing or unsupported")
        admitted_mask = (
            reference["source_admission_status"].eq(ADMITTED)
            & ~reference["source_provenance_mismatch"]
            & reference["event_repo_id"].eq(reference["expected_source_context_repo_id"])
            & reference["expected_source_context_repo_id"].eq(reference["authoritative_seed_project"])
        )
        counts = Counter(reference["source_admission_status"].astype(str))
        return ValidatedReferenceChunk(
            audit_rows=reference,
            admitted_rows=reference.loc[admitted_mask].copy(),
            status_counts={status: int(counts.get(status, 0)) for status in SOURCE_ADMISSION_STATUSES},
        )


class SourceBoundaryStaging:
    """Transient SQLite audit table and admitted-only analytical view."""

    _columns = (*REQUIRED_S1_SOURCE_BOUNDARY_FIELDS, *OPTIONAL_CORRECTED_PROVENANCE_FIELDS, "authoritative_seed_project")

    def __init__(self) -> None:
        # C3.7-B audit staging is deliberately transient; persistent staging
        # belongs to a separately authorized future scientific stage.
        self._connection = sqlite3.connect(":memory:")
        self._connection.row_factory = sqlite3.Row
        self._create_schema()

    def _create_schema(self) -> None:
        fields = ", ".join('"%s" TEXT' % field for field in self._columns)
        self._connection.executescript(
            "CREATE TABLE reference_provenance_staging (%s);" % fields
            + "CREATE VIEW admitted_reference_records AS "
            + "SELECT * FROM reference_provenance_staging "
            + "WHERE source_admission_status = 'ADMITTED_SOURCE_OBSERVATION' "
            + "AND source_provenance_mismatch IN ('0', 'False', 'false') "
            + "AND event_repo_id = expected_source_context_repo_id "
            + "AND expected_source_context_repo_id = authoritative_seed_project;"
        )

    def stage(self, validated: ValidatedReferenceChunk) -> None:
        if validated.audit_rows.empty:
            return
        rows = []
        for record in validated.audit_rows.reindex(columns=self._columns).to_dict(orient="records"):
            values = []
            for field in self._columns:
                value = record.get(field)
                if pd.isna(value):
                    values.append(None)
                elif isinstance(value, bool):
                    values.append("1" if value else "0")
                else:
                    values.append(str(value))
            rows.append(tuple(values))
        placeholders = ", ".join("?" for _ in self._columns)
        self._connection.executemany(
            "INSERT INTO reference_provenance_staging (%s) VALUES (%s)"
            % (", ".join('"%s"' % column for column in self._columns), placeholders),
            rows,
        )
        self._connection.commit()

    def iterate_audit_reference_rows(self) -> Iterator[Mapping[str, Any]]:
        for row in self._connection.execute("SELECT * FROM reference_provenance_staging"):
            yield dict(row)

    def iterate_admitted_reference_rows(self) -> Iterator[Mapping[str, Any]]:
        for row in self._connection.execute("SELECT * FROM admitted_reference_records"):
            yield dict(row)

    def close(self) -> None:
        self._connection.close()


def preflight_source_boundary(config_path: str | Path = DEFAULT_CONFIG_PATH) -> Dict[str, Any]:
    """Run the authorized read-only full-data corrected source-boundary preflight."""

    config = load_config(config_path)
    provenance = validate_scaffold_provenance(config)
    adapter = S1SourceObservationAdapter.from_config(config)
    contexts = list(adapter._partition_contexts.values())
    counters: Counter[str] = Counter()
    observed_statuses: set[str] = set()
    schema_versions: set[str] = set()
    affected_seed_projects: set[str] = set()
    fireproof_context_rows = 0
    fireproof_event_rows = 0
    for context in contexts:
        headers = pd.read_csv(context.evidence_path, nrows=0).columns.tolist()
        adapter.validate_headers(headers)
        usecols = list(REQUIRED_S1_SOURCE_BOUNDARY_FIELDS)
        usecols.extend(field for field in OPTIONAL_CORRECTED_PROVENANCE_FIELDS if field in headers)
        for chunk in pd.read_csv(context.evidence_path, usecols=usecols, dtype="string", chunksize=100000, low_memory=False):
            validated = adapter.validate_reference_chunk(context.evidence_path, chunk)
            counters["reference_rows_before_admission"] += int(len(validated.audit_rows))
            for status, count in validated.status_counts.items():
                counters[status] += count
                if count:
                    observed_statuses.add(status)
            if "aggregate_schema_version" in validated.audit_rows.columns:
                schema_versions.update(validated.audit_rows["aggregate_schema_version"].dropna().astype(str))
            out_of_seed = validated.audit_rows.loc[
                validated.audit_rows["source_admission_status"].eq(OUT_OF_SEED)
            ]
            if not out_of_seed.empty:
                affected_seed_projects.add(context.seed_project)
                if context.seed_project == FIREPROOF_CONTEXT:
                    fireproof_context_rows += int(len(out_of_seed))
                    fireproof_event_rows += int(out_of_seed["event_repo_id"].eq(FIREPROOF_OUT_OF_SEED_EVENT_REPO).sum())
    return {
        "status": "PASS",
        "preflight_kind": "C3_7B_READ_ONLY_SOURCE_BOUNDARY",
        "corrected_aggregate_root": provenance["corrected_aggregate_root"],
        "corrected_p0_manifest": provenance["corrected_p0_manifest"],
        "corrected_p0_manifest_sha256": sha256_file(provenance["corrected_p0_manifest"]),
        "corrected_p0_config_sha256": provenance["corrected_p0_config_sha256"],
        "partition_count": adapter.partition_count,
        "reference_rows_before_admission": int(counters["reference_rows_before_admission"]),
        "source_admission_status_counts": {status: int(counters[status]) for status in SOURCE_ADMISSION_STATUSES},
        "source_admission_status_observed": sorted(observed_statuses),
        "aggregate_schema_versions_observed": sorted(schema_versions),
        "unknown_source_admission_status_count": 0,
        "status_identity_contradiction_count": 0,
        "admitted_identity_contradiction_count": 0,
        "affected_source_seed_count": len(affected_seed_projects),
        "affected_source_seed_projects": sorted(affected_seed_projects),
        "fireproof_context_679889516_out_of_seed_rows": fireproof_context_rows,
        "fireproof_event_repo_600271677_out_of_seed_rows": fireproof_event_rows,
        "event_rejoin_performed": False,
        "membership_build_run": 0,
        "quotient_build_run": 0,
        "network_algorithms_run": 0,
    }


def _git_head() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(Path(__file__).resolve().parents[3]),
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def write_preflight_report(result: Mapping[str, Any], path: str | Path) -> Path:
    target = canonical_path(path)
    freeze_root = canonical_path(Path(__file__).resolve().parents[3] / "docs" / "freeze")
    if not _is_within(target, freeze_root):
        raise PathGuardError("C3.7-B preflight metadata may be written only under docs/freeze")
    payload = dict(result)
    payload["implementation_commit_candidate"] = _git_head()
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="C3.7-B read-only corrected S1 boundary preflight")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="v2 scaffold config")
    parser.add_argument("--preflight", action="store_true", help="run the authorized read-only boundary preflight")
    parser.add_argument("--report", help="optional docs/freeze JSON report path")
    args = parser.parse_args(argv)
    if not args.preflight:
        parser.print_help()
        return 0
    result = preflight_source_boundary(args.config)
    if args.report:
        write_preflight_report(result, args.report)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
