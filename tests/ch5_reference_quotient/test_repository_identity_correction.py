import pandas as pd
import pytest

from script.build_dataset.granular_aggregation import granu_agg_with_event_provenance
from script.build_dataset.repository_identity_provenance import (
    ADMITTED_SOURCE_OBSERVATION,
    LEGACY_EVENT_REPOSITORY_UNAVAILABLE,
    MATCHED_UNIQUE,
    OUT_OF_SEED_SOURCE_OBSERVATION,
    RELATION_EVENT_MULTI_MATCH,
    RELATION_EVENT_UNMATCHED,
    assert_provenance_join_pass,
    adapt_legacy_relation_schema,
    attach_event_repository_provenance,
    normalize_repository_id,
    require_corrected_relation_schema,
)
from script.ch5_reference_quotient.source_observation import build_refq_source_observation_view


def _relation(event_id="e1", event_repo_id=None):
    row = {
        "event_id": event_id,
        "relation_type": "Reference",
        "src_entity_id": "I_679889516#1",
        "src_entity_type": "Issue",
        "tar_entity_id": "R_600271677",
        "tar_entity_type": "Repo",
        "tar_entity_objnt_prop_dict": {"repo_id": 600271677},
    }
    if event_repo_id is not None:
        row["event_repo_id"] = event_repo_id
    return row


def _raw(event_id="e1", repo_id=679889516, repo_name="fireproof-storage/fireproof"):
    return {"id": event_id, "repo_id": repo_id, "repo_name": repo_name}


def test_same_name_different_numeric_ids_remain_distinct():
    assert normalize_repository_id("600271677") != normalize_repository_id("679889516")
    assert normalize_repository_id("600271677.0") == "600271677"


def test_event_repo_fields_survive_relation_serialization(tmp_path):
    relations = pd.DataFrame([_relation()])
    raw = pd.DataFrame([_raw()])
    enriched = attach_event_repository_provenance(relations, raw)
    path = tmp_path / "relation.csv"
    enriched.to_csv(path, index=False)
    loaded = pd.read_csv(path, dtype={"event_repo_id": "string"})
    assert loaded.loc[0, "event_repo_id"] == "679889516"
    assert loaded.loc[0, "event_repo_name"] == "fireproof-storage/fireproof"


def test_relation_raw_provenance_invariant_and_unique_status():
    enriched = attach_event_repository_provenance(
        pd.DataFrame([_relation()]),
        pd.DataFrame([_raw()]),
    )
    assert enriched.loc[0, "event_repo_provenance_status"] == MATCHED_UNIQUE
    assert enriched.loc[0, "event_repo_id"] == "679889516"


def test_legacy_relation_adapter_is_explicitly_unavailable():
    legacy = adapt_legacy_relation_schema(pd.DataFrame([_relation()]))
    assert legacy.loc[0, "event_repo_id"] is pd.NA
    assert legacy.loc[0, "event_repo_provenance_status"] == LEGACY_EVENT_REPOSITORY_UNAVAILABLE
    with pytest.raises(ValueError, match="legacy relation schema"):
        require_corrected_relation_schema(legacy)


def test_non_actor_aggregate_uses_event_repo_not_caller_context():
    row = pd.Series(_relation(event_repo_id="600271677"))
    aggregated = granu_agg_with_event_provenance(row, expected_source_context_repo_id="679889516")
    assert aggregated["src_entity_id_agg"] == "R_600271677"
    assert aggregated["expected_source_context_repo_id"] == "679889516"
    assert aggregated["source_admission_status"] == OUT_OF_SEED_SOURCE_OBSERVATION


def test_caller_context_cannot_overwrite_event_repo_id():
    row = pd.Series(_relation(event_repo_id="679889516"))
    aggregated = granu_agg_with_event_provenance(row, expected_source_context_repo_id="600271677")
    assert aggregated["event_repo_id"] == "679889516"
    assert aggregated["src_entity_id_agg"] == "R_679889516"
    assert aggregated["source_provenance_mismatch"] is True


def test_source_view_filters_before_membership_and_keeps_rejected_rows():
    records = pd.DataFrame([
        _relation("out", "600271677"),
        _relation("in", "679889516"),
        {**_relation("event", "679889516"), "relation_type": "EventAction"},
    ])
    all_rows, admitted, summary = build_refq_source_observation_view(
        records,
        expected_source_context_repo_id="679889516",
    )
    assert len(all_rows) == 3
    assert len(admitted) == 1
    assert admitted.iloc[0]["event_id"] == "in"
    assert summary["admitted_rows"] == 1
    assert summary[OUT_OF_SEED_SOURCE_OBSERVATION] == 1


def test_valid_source_is_admitted():
    result = build_refq_source_observation_view(
        pd.DataFrame([_relation(event_repo_id="679889516")]),
        expected_source_context_repo_id="679889516",
    )[1]
    assert result.iloc[0]["source_admission_status"] == ADMITTED_SOURCE_OBSERVATION


def test_related_repository_remains_project_mappable_target():
    aggregated = granu_agg_with_event_provenance(
        pd.Series(_relation(event_repo_id="679889516")),
        expected_source_context_repo_id="679889516",
    )
    assert aggregated["src_entity_id_agg"] == "R_679889516"
    assert aggregated["tar_entity_id_agg"] == "R_600271677"
    assert aggregated["tar_entity_type_agg"] == "Repo"


def test_missing_event_repo_does_not_fallback_to_context_or_filename():
    aggregated = granu_agg_with_event_provenance(
        pd.Series(_relation(event_repo_id="")),
        expected_source_context_repo_id="679889516",
    )
    assert aggregated["source_admission_status"] == "MISSING_EVENT_REPOSITORY_ID"
    assert pd.isna(aggregated["src_entity_id_agg"])
    assert aggregated["src_entity_id_agg"] != "R_679889516"


def test_ambiguous_provenance_join_is_blocking():
    relations = pd.DataFrame([_relation()])
    raw = pd.DataFrame([_raw(), _raw(repo_name="fireproof-storage/fireproof")])
    enriched = attach_event_repository_provenance(relations, raw)
    assert enriched.loc[0, "event_repo_provenance_status"] == RELATION_EVENT_MULTI_MATCH
    with pytest.raises(ValueError, match="blocking"):
        assert_provenance_join_pass(enriched)


def test_raw_repository_id_missing_is_not_treated_as_unique_provenance():
    enriched = attach_event_repository_provenance(
        pd.DataFrame([_relation()]),
        pd.DataFrame([_raw(repo_id="")]),
    )
    assert enriched.loc[0, "event_repo_provenance_status"] == "RAW_REPO_ID_MISSING"


def test_invalid_raw_repository_id_is_blocking_without_fallback():
    enriched = attach_event_repository_provenance(
        pd.DataFrame([_relation()]),
        pd.DataFrame([_raw(repo_id="600271677.5")]),
    )
    assert enriched.loc[0, "event_repo_provenance_status"] == "REPO_ID_CONFLICT"
    assert pd.isna(enriched.loc[0, "event_repo_id"])


def test_existing_relation_repository_conflict_is_blocking():
    enriched = attach_event_repository_provenance(
        pd.DataFrame([_relation(event_repo_id="600271677")]),
        pd.DataFrame([_raw(repo_id="679889516")]),
    )
    assert enriched.loc[0, "event_repo_provenance_status"] == "REPO_ID_CONFLICT"
    with pytest.raises(ValueError, match="blocking"):
        assert_provenance_join_pass(enriched)


def test_unmatched_provenance_join_is_blocking():
    enriched = attach_event_repository_provenance(
        pd.DataFrame([_relation("missing")]),
        pd.DataFrame([_raw()]),
    )
    assert enriched.loc[0, "event_repo_provenance_status"] == RELATION_EVENT_UNMATCHED
    with pytest.raises(ValueError, match="blocking"):
        assert_provenance_join_pass(enriched)


def test_admitted_rows_have_zero_source_mismatch():
    rows = pd.DataFrame([_relation("in", "679889516")])
    admitted = build_refq_source_observation_view(rows, "679889516")[1]
    assert not admitted["source_provenance_mismatch"].any()


def test_seed_boundary_contract_remains_294():
    from script.ch5_reference_quotient.config import load_config, resolved_inputs
    from script.ch5_reference_quotient.seed_selection import assert_seed_boundary, build_seed_manifests

    config = load_config("configs/ch5_reference_quotient_p0.yaml")
    inputs = resolved_inputs(config)
    seeds, candidates = build_seed_manifests(
        inputs["repo_activity_statistics"],
        inputs["gh_core_ref_node_agg_dir"],
        config.get_int("study_year"),
        config.get_int("analysis_seed_activity_threshold"),
    )
    assert_seed_boundary(seeds, candidates, 294, 301)


def test_repo_created_at_passes_through_unchanged():
    row = pd.Series({
        **_relation(event_repo_id="679889516"),
        "repo_created_at": "2018-11-14T08:18:40Z",
    })
    aggregated = granu_agg_with_event_provenance(row, "679889516")
    assert aggregated["repo_created_at"] == "2018-11-14T08:18:40Z"


def test_titan_is_not_special_cased_or_changed():
    row = pd.Series(_relation(event_repo_id="157514605"))
    aggregated = granu_agg_with_event_provenance(row, "157514605")
    assert aggregated["event_repo_id"] == "157514605"
    assert aggregated["src_entity_id_agg"] == "R_157514605"
