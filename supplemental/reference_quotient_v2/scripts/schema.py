"""Frozen corrected aggregate schema contracts for future S1 work.

No row adapter or aggregate scan belongs in C3.7-A. These helpers only define
and validate names used by the later status-aware adapter.
"""

from __future__ import annotations

from typing import Iterable, FrozenSet, Sequence


SOURCE_ADMISSION_STATUSES: tuple[str, ...] = (
    "ADMITTED_SOURCE_OBSERVATION",
    "OUT_OF_SEED_SOURCE_OBSERVATION",
    "MISSING_EVENT_REPOSITORY_ID",
    "INVALID_EVENT_REPOSITORY_ID",
)
SOURCE_ADMISSION_STATUS_SET: FrozenSet[str] = frozenset(SOURCE_ADMISSION_STATUSES)
REQUIRED_CORRECTED_AGGREGATE_PROVENANCE_FIELDS: tuple[str, ...] = (
    "event_id",
    "event_repo_id",
    "expected_source_context_repo_id",
    "source_admission_status",
    "source_provenance_mismatch",
)
OPTIONAL_CORRECTED_PROVENANCE_FIELDS: tuple[str, ...] = (
    "event_repo_name",
    "event_repo_provenance_status",
    "aggregate_schema_version",
)
REQUIRED_S1_SOURCE_BOUNDARY_FIELDS: tuple[str, ...] = (
    "event_id",
    "event_repo_id",
    "expected_source_context_repo_id",
    "source_admission_status",
    "source_provenance_mismatch",
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


class SchemaContractError(ValueError):
    """Raised when a future corrected aggregate violates the frozen contract."""


def validate_required_fields(fields: Iterable[str]) -> tuple[str, ...]:
    present = set(fields)
    missing = tuple(field for field in REQUIRED_CORRECTED_AGGREGATE_PROVENANCE_FIELDS if field not in present)
    if missing:
        raise SchemaContractError("missing corrected aggregate provenance fields: %s" % ", ".join(missing))
    return tuple(field for field in REQUIRED_CORRECTED_AGGREGATE_PROVENANCE_FIELDS if field in present)


def validate_source_admission_status(status: str) -> str:
    if status not in SOURCE_ADMISSION_STATUS_SET:
        raise SchemaContractError("unknown source_admission_status: %r" % status)
    return status


def validate_s1_source_boundary_fields(fields: Iterable[str]) -> tuple[str, ...]:
    present = set(fields)
    missing = tuple(field for field in REQUIRED_S1_SOURCE_BOUNDARY_FIELDS if field not in present)
    if missing:
        raise SchemaContractError("missing S1 source-boundary fields: %s" % ", ".join(missing))
    return tuple(field for field in REQUIRED_S1_SOURCE_BOUNDARY_FIELDS if field in present)


def validate_status_vocabulary(statuses: Sequence[str]) -> tuple[str, ...]:
    if tuple(statuses) != SOURCE_ADMISSION_STATUSES:
        raise SchemaContractError("source-admission vocabulary must contain exactly the frozen four statuses")
    return tuple(statuses)
