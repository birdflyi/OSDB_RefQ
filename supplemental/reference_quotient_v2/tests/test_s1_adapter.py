"""C3.7-B tests for the corrected S1 source-observation boundary only."""

from __future__ import annotations

import os

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts.paths import CORRECTED_OUTPUTS_ROOT, canonical_path
from supplemental.reference_quotient_v2.scripts.s1_adapter import (
    ADMITTED,
    CORRECTED_AGGREGATE_SCHEMA_VERSION,
    INVALID,
    MISSING,
    OUT_OF_SEED,
    S1SourceObservationAdapter,
    SeedPartitionContext,
    SourceBoundaryContractError,
    SourceBoundaryStaging,
)
from supplemental.reference_quotient_v2.scripts.schema import (
    REQUIRED_S1_SOURCE_BOUNDARY_FIELDS,
    SOURCE_ADMISSION_STATUSES,
)


SEED_ID = "101"


def _row(**overrides):
    row = {
        "event_id": "evt-1",
        "event_repo_id": SEED_ID,
        "expected_source_context_repo_id": SEED_ID,
        "source_admission_status": ADMITTED,
        "source_provenance_mismatch": False,
        "relation_type": "Reference",
        "event_type": "IssuesEvent",
        "src_entity_id": "src-1",
        "src_entity_type": "Issue",
        "tar_entity_id": "tar-1",
        "tar_entity_type": "Repository",
        "src_entity_id_agg": "src-agg-1",
        "src_entity_type_agg": "Issue",
        "tar_entity_id_agg": "tar-agg-1",
        "tar_entity_type_agg": "Repository",
        "tar_entity_type_fine_grained": "Repository",
        "event_repo_name": "display-only/example",
        "event_repo_provenance_status": "MATCHED_UNIQUE",
        "aggregate_schema_version": CORRECTED_AGGREGATE_SCHEMA_VERSION,
    }
    row.update(overrides)
    return row


@pytest.fixture()
def adapter(tmp_path):
    aggregate_root = tmp_path / "corrected-aggregate"
    aggregate_root.mkdir()
    partition = aggregate_root / "partition.csv"
    partition.touch()
    key = os.path.normcase(os.fspath(canonical_path(partition)))
    context = SeedPartitionContext(seed_project=SEED_ID, evidence_path=canonical_path(partition))
    return S1SourceObservationAdapter({key: context}, aggregate_root), partition


def _validate(adapter, partition, *rows):
    return adapter.validate_reference_chunk(partition, pd.DataFrame(rows))


def test_required_provenance_and_boundary_fields_are_accepted(adapter):
    source, partition = adapter
    assert source.validate_headers(REQUIRED_S1_SOURCE_BOUNDARY_FIELDS) == REQUIRED_S1_SOURCE_BOUNDARY_FIELDS
    validated = _validate(source, partition, _row())
    assert len(validated.admitted_rows) == 1


def test_missing_required_field_is_rejected(adapter):
    source, partition = adapter
    row = _row()
    del row["event_repo_id"]
    with pytest.raises(SourceBoundaryContractError, match="event_repo_id"):
        _validate(source, partition, row)


def test_exactly_four_frozen_statuses_are_accepted_with_their_contracts(adapter):
    source, partition = adapter
    validated = _validate(
        source,
        partition,
        _row(source_admission_status=ADMITTED),
        _row(event_id="evt-2", event_repo_id="202", source_admission_status=OUT_OF_SEED, source_provenance_mismatch=True),
        _row(event_id="evt-3", event_repo_id=pd.NA, source_admission_status=MISSING, source_provenance_mismatch=True),
        _row(event_id="evt-4", event_repo_id=pd.NA, source_admission_status=INVALID, source_provenance_mismatch=True),
    )
    assert validated.status_counts == {status: 1 for status in SOURCE_ADMISSION_STATUSES}
    assert validated.admitted_rows["event_id"].tolist() == ["evt-1"]


def test_unknown_or_blank_status_fails_closed(adapter):
    source, partition = adapter
    for status in ("UNRECOGNIZED", "", pd.NA):
        with pytest.raises(SourceBoundaryContractError, match="unknown source_admission_status"):
            _validate(source, partition, _row(source_admission_status=status))


def test_admitted_contract_requires_equal_ids_and_false_mismatch(adapter):
    source, partition = adapter
    assert len(_validate(source, partition, _row()).admitted_rows) == 1
    with pytest.raises(SourceBoundaryContractError, match="admitted"):
        _validate(source, partition, _row(event_repo_id="202"))
    with pytest.raises(SourceBoundaryContractError, match="admitted"):
        _validate(source, partition, _row(source_provenance_mismatch=True))


def test_out_of_seed_contract_is_retained_only_as_an_audit_row(adapter):
    source, partition = adapter
    validated = _validate(
        source,
        partition,
        _row(event_repo_id="202", source_admission_status=OUT_OF_SEED, source_provenance_mismatch=True),
    )
    assert len(validated.audit_rows) == 1
    assert validated.admitted_rows.empty
    with pytest.raises(SourceBoundaryContractError, match="out-of-seed"):
        _validate(
            source,
            partition,
            _row(source_admission_status=OUT_OF_SEED, source_provenance_mismatch=True),
        )


def test_missing_and_invalid_materialized_null_contracts_never_enter_admitted_view(adapter):
    source, partition = adapter
    for status in (MISSING, INVALID):
        validated = _validate(
            source,
            partition,
            _row(event_repo_id=pd.NA, source_admission_status=status, source_provenance_mismatch=True),
        )
        assert validated.admitted_rows.empty
    for status in (MISSING, INVALID):
        with pytest.raises(SourceBoundaryContractError):
            _validate(
                source,
                partition,
                _row(event_repo_id=SEED_ID, source_admission_status=status, source_provenance_mismatch=True),
            )
    with pytest.raises(SourceBoundaryContractError, match="invalid-event-repository"):
        _validate(
            source,
            partition,
            _row(event_repo_id="not-a-repository-id", source_admission_status=INVALID, source_provenance_mismatch=True),
        )


def test_expected_context_must_match_authoritative_seed(adapter):
    source, partition = adapter
    with pytest.raises(SourceBoundaryContractError, match="authoritative current seed"):
        _validate(source, partition, _row(expected_source_context_repo_id="999"))


def test_repo_name_and_filename_cannot_authorize_source_identity(adapter):
    source, partition = adapter
    with pytest.raises(SourceBoundaryContractError, match="admitted"):
        _validate(source, partition, _row(event_repo_id="202", event_repo_name="101"))
    unlisted = partition.parent / "101_named_partition.csv"
    unlisted.touch()
    with pytest.raises(SourceBoundaryContractError, match="not authorized"):
        _validate(source, unlisted, _row())


def test_historical_schema_is_rejected_and_corrected_schema_is_accepted(adapter):
    source, partition = adapter
    with pytest.raises(SourceBoundaryContractError, match="schema version"):
        _validate(source, partition, _row(aggregate_schema_version="reference_aggregate_schema_v1"))
    assert len(_validate(source, partition, _row()).admitted_rows) == 1


def test_non_reference_rows_do_not_enter_the_boundary_views(adapter):
    source, partition = adapter
    validated = _validate(source, partition, _row(relation_type="Actor"))
    assert validated.audit_rows.empty
    assert validated.admitted_rows.empty
    assert validated.status_counts == {status: 0 for status in SOURCE_ADMISSION_STATUSES}


def test_transient_staging_preserves_rejected_rows_and_admitted_view_excludes_them(adapter):
    source, partition = adapter
    validated = _validate(
        source,
        partition,
        _row(),
        _row(event_id="evt-fireproof", event_repo_id="600271677", source_admission_status=OUT_OF_SEED, source_provenance_mismatch=True),
        _row(event_id="evt-missing", event_repo_id=pd.NA, source_admission_status=MISSING, source_provenance_mismatch=True),
    )
    staging = SourceBoundaryStaging()
    try:
        staging.stage(validated)
        audit_ids = [record["event_id"] for record in staging.iterate_audit_reference_rows()]
        admitted_ids = [record["event_id"] for record in staging.iterate_admitted_reference_rows()]
    finally:
        staging.close()
    assert audit_ids == ["evt-1", "evt-fireproof", "evt-missing"]
    assert admitted_ids == ["evt-1"]


def test_source_boundary_staging_and_validation_create_no_v2_outputs_root(adapter):
    source, partition = adapter
    before = CORRECTED_OUTPUTS_ROOT.exists()
    validated = _validate(source, partition, _row())
    staging = SourceBoundaryStaging()
    try:
        staging.stage(validated)
    finally:
        staging.close()
    assert CORRECTED_OUTPUTS_ROOT.exists() is before
