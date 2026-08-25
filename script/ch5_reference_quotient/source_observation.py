"""Explicit v2 seed-centered source observation view."""

from __future__ import annotations

from typing import Any

import pandas as pd

from script.build_dataset.repository_identity_provenance import (
    ADMITTED_SOURCE_OBSERVATION,
    annotate_source_admission,
    source_admission_summary,
)


def build_refq_source_observation_view(
    records: pd.DataFrame,
    expected_source_context_repo_id: Any,
    *,
    relation_col: str = "relation_type",
    relation_type: str = "Reference",
    event_time_col: str | None = None,
    study_start: Any = None,
    study_end: Any = None,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, int]]:
    """Return ``(annotated_all, admitted_view, summary)``.

    Rejected records stay in ``annotated_all`` for provenance auditing. Only
    rows with direct Reference type, valid event repository identity, and an
    admitted source context are returned in ``admitted_view``.
    """

    if relation_col not in records.columns:
        raise KeyError(f"missing relation column: {relation_col}")
    annotated = annotate_source_admission(
        records,
        expected_source_context_repo_id,
    )
    relation_mask = annotated[relation_col].eq(relation_type)
    time_mask = pd.Series(True, index=annotated.index)
    if event_time_col is not None and (study_start is not None or study_end is not None):
        if event_time_col not in annotated.columns:
            raise KeyError(f"missing event time column: {event_time_col}")
        event_time = pd.to_datetime(annotated[event_time_col], errors="coerce", utc=True)
        if study_start is not None:
            time_mask &= event_time.ge(pd.to_datetime(study_start, utc=True))
        if study_end is not None:
            time_mask &= event_time.lt(pd.to_datetime(study_end, utc=True))
    admitted_mask = (
        relation_mask
        & time_mask
        & annotated["source_admission_status"].eq(ADMITTED_SOURCE_OBSERVATION)
    )
    admitted = annotated.loc[admitted_mask].copy()
    summary = source_admission_summary(annotated)
    summary["reference_rows"] = int(relation_mask.sum())
    summary["admitted_rows"] = int(admitted_mask.sum())
    summary["rejected_rows"] = int(len(annotated) - admitted_mask.sum())
    return annotated, admitted, summary

