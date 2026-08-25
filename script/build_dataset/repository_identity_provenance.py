"""Repository-identity provenance helpers for the versioned RefQ correction.

The helpers in this module are opt-in. Historical v1 relation and aggregate
files remain readable and are never treated as corrected v2 inputs merely
because they can be loaded by an adapter.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from numbers import Integral, Real
from typing import Any, Optional

import pandas as pd


MATCHED_UNIQUE = "MATCHED_UNIQUE"
RAW_REPO_ID_MISSING = "RAW_REPO_ID_MISSING"
RELATION_EVENT_UNMATCHED = "RELATION_EVENT_UNMATCHED"
RELATION_EVENT_MULTI_MATCH = "RELATION_EVENT_MULTI_MATCH"
REPO_ID_CONFLICT = "REPO_ID_CONFLICT"
LEGACY_EVENT_REPOSITORY_UNAVAILABLE = "LEGACY_EVENT_REPOSITORY_UNAVAILABLE"

ADMITTED_SOURCE_OBSERVATION = "ADMITTED_SOURCE_OBSERVATION"
OUT_OF_SEED_SOURCE_OBSERVATION = "OUT_OF_SEED_SOURCE_OBSERVATION"
MISSING_EVENT_REPOSITORY_ID = "MISSING_EVENT_REPOSITORY_ID"
INVALID_EVENT_REPOSITORY_ID = "INVALID_EVENT_REPOSITORY_ID"

_INTEGER_TEXT = re.compile(r"^[+]?(\d+)$")
_INTEGRAL_DECIMAL_TEXT = re.compile(r"^[+]?(\d+)\.0+$")
_MISSING_TEXT = {"", "nan", "none", "null", "<na>"}


def normalize_repository_id(value: Any, *, field_name: str = "repository_id") -> Optional[str]:
    """Normalize an integral GitHub repository ID to a decimal string.

    Blank/null values return ``None``. Non-integral, negative, placeholder, or
    ambiguous values raise ``ValueError`` so callers cannot silently fall back
    to a filename or caller-supplied context.
    """

    if value is None or value is pd.NA:
        return None
    if isinstance(value, bool):
        raise ValueError(f"{field_name} must not be boolean")
    if isinstance(value, str):
        text = value.strip()
        if text.lower() in _MISSING_TEXT:
            return None
        if _INTEGER_TEXT.fullmatch(text):
            return str(int(text))
        if _INTEGRAL_DECIMAL_TEXT.fullmatch(text):
            return str(int(text.split(".", 1)[0]))
        raise ValueError(f"invalid {field_name}: {value!r}")
    if isinstance(value, Integral):
        if value < 0:
            raise ValueError(f"invalid {field_name}: {value!r}")
        return str(value)
    if isinstance(value, Real):
        value = float(value)
        if math.isnan(value):
            return None
        if not math.isfinite(value) or not value.is_integer() or value < 0:
            raise ValueError(f"invalid {field_name}: {value!r}")
        return str(int(value))
    try:
        if pd.isna(value):
            return None
    except (TypeError, ValueError):
        pass
    raise ValueError(f"invalid {field_name}: {value!r}")


def _event_key(value: Any) -> Optional[str]:
    """Create a stable join key without changing the event ID payload."""

    if value is None or value is pd.NA:
        return None
    text = str(value).strip()
    if text.lower() in _MISSING_TEXT:
        return None
    if _INTEGER_TEXT.fullmatch(text):
        return str(int(text))
    if _INTEGRAL_DECIMAL_TEXT.fullmatch(text):
        return str(int(text.split(".", 1)[0]))
    return text


@dataclass(frozen=True)
class SourceAdmissionResult:
    status: str
    event_repo_id: Optional[str]
    expected_source_context_repo_id: Optional[str]

    @property
    def admitted(self) -> bool:
        return self.status == ADMITTED_SOURCE_OBSERVATION


def admit_source_record(
    event_repo_id: Any,
    expected_source_context_repo_id: Any,
) -> SourceAdmissionResult:
    """Classify a row against its expected seed source context.

    The expected context is an assertion only. It is never used to fill or
    replace the event repository identity.
    """

    try:
        expected = normalize_repository_id(
            expected_source_context_repo_id,
            field_name="expected_source_context_repo_id",
        )
    except ValueError as exc:
        raise ValueError(str(exc)) from exc
    if expected is None:
        raise ValueError("expected_source_context_repo_id is required")
    try:
        event = normalize_repository_id(event_repo_id, field_name="event_repo_id")
    except ValueError:
        return SourceAdmissionResult(INVALID_EVENT_REPOSITORY_ID, None, expected)
    if event is None:
        return SourceAdmissionResult(MISSING_EVENT_REPOSITORY_ID, None, expected)
    if event == expected:
        return SourceAdmissionResult(ADMITTED_SOURCE_OBSERVATION, event, expected)
    return SourceAdmissionResult(OUT_OF_SEED_SOURCE_OBSERVATION, event, expected)


def annotate_source_admission(
    records: pd.DataFrame,
    expected_source_context_repo_id: Any,
    *,
    event_repo_id_col: str = "event_repo_id",
) -> pd.DataFrame:
    """Add v2 source-admission fields while retaining rejected rows."""

    if event_repo_id_col not in records.columns:
        raise KeyError(f"missing event repository column: {event_repo_id_col}")
    result = records.copy()
    statuses = []
    normalized_ids = []
    expected_ids = []
    mismatches = []
    for value in result[event_repo_id_col].tolist():
        admission = admit_source_record(value, expected_source_context_repo_id)
        statuses.append(admission.status)
        normalized_ids.append(admission.event_repo_id)
        expected_ids.append(admission.expected_source_context_repo_id)
        mismatches.append(not admission.admitted)
    result[event_repo_id_col] = pd.Series(normalized_ids, index=result.index, dtype="string")
    result["expected_source_context_repo_id"] = pd.Series(expected_ids, index=result.index, dtype="string")
    result["source_admission_status"] = statuses
    result["source_provenance_mismatch"] = mismatches
    return result


def attach_event_repository_provenance(
    relations: pd.DataFrame,
    raw_events: pd.DataFrame,
    *,
    relation_event_id_col: str = "event_id",
    raw_event_id_col: str = "id",
    raw_repo_id_col: str = "repo_id",
    raw_repo_name_col: str = "repo_name",
    partition_col: Optional[str] = None,
) -> pd.DataFrame:
    """Attach authoritative raw event repository fields to relation rows.

    The function retains one output row per relation row and writes a
    ``event_repo_provenance_status`` column. It never infers identity from a
    filename or caller context. A partition column is required when event IDs
    are only unique within a source partition.
    """

    required_relation = {relation_event_id_col}
    required_raw = {raw_event_id_col, raw_repo_id_col, raw_repo_name_col}
    if partition_col:
        required_relation.add(partition_col)
        required_raw.add(partition_col)
    missing_relation = sorted(required_relation - set(relations.columns))
    missing_raw = sorted(required_raw - set(raw_events.columns))
    if missing_relation:
        raise KeyError(f"missing relation columns: {', '.join(missing_relation)}")
    if missing_raw:
        raise KeyError(f"missing raw event columns: {', '.join(missing_raw)}")

    result = relations.copy()
    raw_groups: dict[tuple[Optional[str], Optional[str]], list[dict[str, Any]]] = {}
    for raw in raw_events.to_dict("records"):
        key = (
            _event_key(raw[partition_col]) if partition_col else None,
            _event_key(raw[raw_event_id_col]),
        )
        raw_groups.setdefault(key, []).append(raw)

    event_repo_ids = []
    event_repo_names = []
    statuses = []
    for relation in result.to_dict("records"):
        key = (
            _event_key(relation[partition_col]) if partition_col else None,
            _event_key(relation[relation_event_id_col]),
        )
        matches = raw_groups.get(key, [])
        existing_id = relation.get("event_repo_id")
        if len(matches) == 0:
            status = RELATION_EVENT_UNMATCHED
            event_id = None
            event_name = None
        elif len(matches) > 1:
            status = RELATION_EVENT_MULTI_MATCH
            event_id = None
            event_name = None
        else:
            raw_row = matches[0]
            event_name = raw_row[raw_repo_name_col]
            try:
                event_id = normalize_repository_id(raw_row[raw_repo_id_col], field_name="raw_event_repo_id")
            except ValueError:
                status = REPO_ID_CONFLICT
                event_id = None
            else:
                status = RAW_REPO_ID_MISSING if event_id is None else MATCHED_UNIQUE
                if existing_id is not None and str(existing_id).strip().lower() not in _MISSING_TEXT:
                    try:
                        existing = normalize_repository_id(existing_id, field_name="relation_event_repo_id")
                    except ValueError:
                        status = REPO_ID_CONFLICT
                    else:
                        if existing != event_id:
                            status = REPO_ID_CONFLICT
        event_repo_ids.append(event_id)
        event_repo_names.append(event_name)
        statuses.append(status)
    result["event_repo_id"] = pd.Series(event_repo_ids, index=result.index, dtype="string")
    result["event_repo_name"] = event_repo_names
    result["event_repo_provenance_status"] = statuses
    return result


def validate_relation_event_repository_provenance(
    relations: pd.DataFrame,
    raw_events: pd.DataFrame,
    **kwargs: Any,
) -> pd.DataFrame:
    """Return only the compact row-level provenance validation result."""

    enriched = attach_event_repository_provenance(relations, raw_events, **kwargs)
    columns = [
        kwargs.get("relation_event_id_col", "event_id"),
        *( [kwargs["partition_col"]] if kwargs.get("partition_col") else [] ),
        "event_repo_id",
        "event_repo_name",
        "event_repo_provenance_status",
    ]
    return enriched[columns].copy()


def assert_provenance_join_pass(validation: pd.DataFrame) -> None:
    """Block corrected materialization on unsafe relation/raw joins."""

    blocking = {
        RELATION_EVENT_UNMATCHED,
        RELATION_EVENT_MULTI_MATCH,
        REPO_ID_CONFLICT,
    }
    observed = set(validation["event_repo_provenance_status"].dropna().astype(str))
    failures = sorted(observed & blocking)
    if failures:
        raise ValueError("blocking event repository provenance statuses: " + ", ".join(failures))


def adapt_legacy_relation_schema(relations: pd.DataFrame) -> pd.DataFrame:
    """Expose v1 relation files explicitly as non-corrected legacy data."""

    result = relations.copy()
    result["event_repo_id"] = pd.Series(pd.NA, index=result.index, dtype="string")
    result["event_repo_name"] = pd.NA
    result["event_repo_provenance_status"] = LEGACY_EVENT_REPOSITORY_UNAVAILABLE
    result["relation_schema_version"] = "reference_relation_schema_v1_legacy"
    return result


def require_corrected_relation_schema(relations: pd.DataFrame) -> None:
    """Reject legacy or incomplete relation frames for corrected v2 use."""

    required = {"event_id", "event_repo_id", "event_repo_name", "event_repo_provenance_status"}
    missing = sorted(required - set(relations.columns))
    if missing:
        raise ValueError("corrected relation schema missing: " + ", ".join(missing))
    if relations["event_repo_provenance_status"].eq(LEGACY_EVENT_REPOSITORY_UNAVAILABLE).any():
        raise ValueError("legacy relation schema is not eligible for corrected v2 inputs")


def source_admission_summary(records: pd.DataFrame) -> dict[str, int]:
    """Summarize an annotated source observation frame."""

    counts = records["source_admission_status"].value_counts(dropna=False).to_dict()
    return {str(key): int(value) for key, value in counts.items()}
