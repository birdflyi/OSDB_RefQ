"""C3.7-B2 S1 evidence-universe semantics on deterministic fixture data."""

from __future__ import annotations

import os

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts.paths import CORRECTED_OUTPUTS_ROOT, canonical_path
from supplemental.reference_quotient_v2.scripts.s1_adapter import (
    ADMITTED,
    OUT_OF_SEED,
    S1SourceObservationAdapter,
    SeedPartitionContext,
)
from supplemental.reference_quotient_v2.scripts.s1_evidence_universe import (
    AGGREGATED_EDGE_WEIGHT,
    AMBIGUOUS,
    CONFLICT_EXCLUDED,
    CROSS_PROJECT_REFERENCE,
    EDGE_COUNT,
    FUTURE_S1_OUTPUT_CONTRACT,
    NON_PROJECT,
    NOT_QUOTIENT_ELIGIBLE,
    PROJECT_MAPPABLE,
    QUOTIENT_ELIGIBLE,
    REFERENCE_RECORD,
    SELF_INTERNAL_PROJECT_REFERENCE,
    S1EvidenceUniverseContractError,
    UNRESOLVED,
    build_future_s1_output_tables,
    composition_table,
    compute_evidence_universe,
    cross_tab,
    reconcile_evidence_universe,
)


SEED_ID = "101"
SCHEMA = "reference_aggregate_schema_v2_event_repository_provenance"


def _row(event_id, *, src_agg="R_101", tar_agg="R_101", tar_agg_type="Repo", status=ADMITTED, event_repo_id=SEED_ID, mismatch=False, tar_entity_id=None, event_type="IssuesEvent"):
    return {
        "event_id": event_id,
        "event_repo_id": event_repo_id,
        "expected_source_context_repo_id": SEED_ID,
        "source_admission_status": status,
        "source_provenance_mismatch": mismatch,
        "relation_type": "Reference",
        "event_type": event_type,
        "src_entity_id": "src-%s" % event_id,
        "src_entity_type": "Issue",
        "tar_entity_id": tar_entity_id if tar_entity_id is not None else "tar-%s" % event_id,
        "tar_entity_type": "Repository",
        "src_entity_id_agg": src_agg,
        "src_entity_type_agg": "Repo",
        "tar_entity_id_agg": tar_agg,
        "tar_entity_type_agg": tar_agg_type,
        "tar_entity_type_fine_grained": "Repository",
        "aggregate_schema_version": SCHEMA,
    }


@pytest.fixture()
def adapter(tmp_path):
    root = tmp_path / "aggregate"
    root.mkdir()
    partition = root / "fixture.csv"
    partition.touch()
    key = os.path.normcase(os.fspath(canonical_path(partition)))
    context = SeedPartitionContext(seed_project=SEED_ID, evidence_path=canonical_path(partition))
    return S1SourceObservationAdapter({key: context}, root), partition


@pytest.fixture()
def universe(adapter):
    source, partition = adapter
    rows = [
        _row("self", tar_agg="R_101"),
        _row("cross", tar_agg="R_202", event_type="PullRequestEvent"),
        _row("non-project", tar_agg="N_1", tar_agg_type="Object"),
        _row("unresolved", tar_agg="unknown-target", tar_agg_type="Repo"),
        _row("rejected", tar_agg="R_303", status=OUT_OF_SEED, event_repo_id="600271677", mismatch=True),
    ]
    return compute_evidence_universe([source.validate_reference_chunk(partition, pd.DataFrame(rows))])


def test_c3_7b_admitted_rows_enter_s1_and_rejected_rows_have_zero_analytical_contribution(universe):
    assert universe.source_admission_before_count == 5
    assert len(universe.records) == 4
    assert "rejected" not in set(universe.records["event_id"])
    assert universe.source_admission_status_counts[OUT_OF_SEED] == 1


def test_self_cross_non_project_and_unresolved_classifications_are_explicit(universe):
    records = universe.records.set_index("event_id")
    assert records.loc["self", "edge_class"] == SELF_INTERNAL_PROJECT_REFERENCE
    assert records.loc["cross", "edge_class"] == CROSS_PROJECT_REFERENCE
    assert records.loc["non-project", "tar_membership_status"] == NON_PROJECT
    assert records.loc["unresolved", "tar_membership_status"] == UNRESOLVED
    assert records.loc["non-project", "quotient_eligibility"] == NOT_QUOTIENT_ELIGIBLE
    assert records.loc["unresolved", "quotient_eligibility"] == NOT_QUOTIENT_ELIGIBLE


def test_quotient_eligibility_and_edge_classes_preserve_reference_record_units(universe):
    reconciliation = reconcile_evidence_universe(universe)
    assert reconciliation["quotient_eligible_records"] == 2
    assert reconciliation["self_loop_evidence_weight"] == 1
    assert reconciliation["cross_project_evidence_weight"] == 1
    assert reconciliation["edge_weight_closes"] is True
    assert reconciliation["reference_record_unit"] == REFERENCE_RECORD
    assert reconciliation["aggregated_edge_weight_measure"] == AGGREGATED_EDGE_WEIGHT
    assert reconciliation["edge_count_unit"] == EDGE_COUNT


def test_target_membership_conflict_is_excluded_from_quotient_eligibility(adapter):
    source, partition = adapter
    rows = [
        _row("conflict-a", tar_agg="R_202", tar_entity_id="shared-target"),
        _row("conflict-b", tar_agg="R_303", tar_entity_id="shared-target"),
    ]
    result = compute_evidence_universe([source.validate_reference_chunk(partition, pd.DataFrame(rows))])
    assert result.membership.summary["membership_conflict_entities"] == 1
    assert set(result.records["tar_membership_status"]) == {CONFLICT_EXCLUDED}
    assert set(result.records["quotient_eligibility"]) == {NOT_QUOTIENT_ELIGIBLE}


def test_ambiguous_target_remains_explicit_and_non_quotient_eligible(adapter):
    source, partition = adapter
    chunk = source.validate_reference_chunk(
        partition,
        pd.DataFrame([_row("ambiguous", tar_agg="R_202 R_303", tar_agg_type="Repo")]),
    )
    result = compute_evidence_universe([chunk])
    assert result.records.iloc[0]["tar_membership_status"] == AMBIGUOUS
    assert result.records.iloc[0]["quotient_eligibility"] == NOT_QUOTIENT_ELIGIBLE


def test_event_entity_cross_tabs_and_output_contract_are_in_memory_only(universe):
    before = CORRECTED_OUTPUTS_ROOT.exists()
    tables = build_future_s1_output_tables(universe)
    assert set(tables) == set(FUTURE_S1_OUTPUT_CONTRACT) - {"evidence_universe_validation.json"}
    assert tuple(tables["event_type_x_quotient_eligibility.csv"].columns) == FUTURE_S1_OUTPUT_CONTRACT["event_type_x_quotient_eligibility.csv"]
    assert int(tables["event_type_x_quotient_eligibility.csv"]["count"].sum()) == 4
    assert int(tables["source_entity_type_x_target_membership_status.csv"]["count"].sum()) == 4
    assert int(tables["edge_class_counts.csv"]["count"].sum()) == 4
    assert set(tables["edge_class_counts.csv"]["unit"]) == {REFERENCE_RECORD}
    assert CORRECTED_OUTPUTS_ROOT.exists() is before


def test_non_admitted_dataframe_is_rejected_before_membership_or_analytics(adapter):
    source, partition = adapter
    valid = source.validate_reference_chunk(partition, pd.DataFrame([_row("admitted")]))
    rejected = valid.admitted_rows.copy()
    rejected.loc[:, "source_admission_status"] = OUT_OF_SEED
    with pytest.raises(S1EvidenceUniverseContractError, match="outside the admitted"):
        compute_evidence_universe([
            type(valid)(audit_rows=rejected, admitted_rows=rejected, status_counts={ADMITTED: 1})
        ])
    with pytest.raises(S1EvidenceUniverseContractError, match="outside the admitted"):
        cross_tab(rejected, "event_type", "source_admission_status")
    with pytest.raises(S1EvidenceUniverseContractError, match="outside the admitted"):
        composition_table(rejected, "authoritative_seed_project", ("event_type",))


def test_historical_constants_are_not_generic_runtime_requirements(universe):
    reconciliation = reconcile_evidence_universe(universe)
    assert reconciliation["source_admission_closes"] is True
    assert reconciliation["target_membership_split_closes"] is True
    assert reconciliation["source_mismatch_after_admission_is_zero"] is True
    assert reconciliation["reference_records_before_source_admission"] == 5


def test_s1_has_no_s7_output_or_selection_surface(universe):
    tables = build_future_s1_output_tables(universe)
    assert all("s7" not in name.lower() for name in tables)
    assert all("fixed_" not in column for table in tables.values() for column in table.columns)


def test_composition_is_generic_and_does_not_reselect_s7_objects(universe):
    composition = composition_table(universe.records, "src_project_id", ("event_type", "source_entity_type"))
    assert int(composition["count"].sum()) == 8
    assert "fixed_source" not in composition.columns
    assert "s7" not in " ".join(composition.columns).lower()


def test_empty_reference_chunk_is_a_valid_zero_contribution_boundary(adapter):
    source, partition = adapter
    empty = source.validate_reference_chunk(partition, pd.DataFrame([_row("non-reference") | {"relation_type": "Actor"}]))
    result = compute_evidence_universe([empty])
    assert result.records.empty
    assert result.source_admission_before_count == 0


def test_module_has_no_historical_input_path_or_csv_reader_surface():
    import supplemental.reference_quotient_v2.scripts.s1_evidence_universe as s1

    assert not hasattr(s1, "read_canonical_inputs")
    assert not hasattr(s1, "read_csv")
