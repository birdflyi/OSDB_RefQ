from pathlib import Path

import pandas as pd
import pytest

from script.build_dataset.granular_aggregation import granu_agg_with_event_provenance
from script.ch5_reference_quotient.config import RefQConfig, load_config, resolved_inputs, validate_config
from script.ch5_reference_quotient.membership import MembershipRegistry
from script.ch5_reference_quotient.pipeline import RefQPipeline, _prepare_reference_evidence_chunk


def _row(*, event_repo_id="1", status="ADMITTED_SOURCE_OBSERVATION", expected="1", source_aggregate="R_1"):
    return {
        "src_entity_id": "I_1#1",
        "src_entity_type": "Issue",
        "tar_entity_id": "I_2#1",
        "tar_entity_type": "Issue",
        "relation_type": "Reference",
        "relation_label_repr": "ref",
        "event_id": "event-1",
        "event_type": "IssuesEvent",
        "event_time": "2023-01-01T00:00:00Z",
        "tar_entity_match_text": "#1",
        "tar_entity_match_pattern_type": "issue",
        "src_entity_id_agg": source_aggregate,
        "src_entity_type_agg": "Repo",
        "tar_entity_id_agg": "R_2",
        "tar_entity_type_agg": "Repo",
        "tar_entity_type_fine_grained": "Issue",
        "event_repo_id": event_repo_id,
        "source_admission_status": status,
        "expected_source_context_repo_id": expected,
    }


def _strict_pipeline(tmp_path: Path) -> RefQPipeline:
    config = RefQConfig(
        raw={
            "relation_type": "Reference",
            "csv_chunk_size": 100,
            "provenance_sample_size": 10,
            "identity_policy": "STRICT_REPOSITORY_IDENTITY",
            "input_paths": {},
            "frozen_output_root": "outputs/test",
        }
    )
    return RefQPipeline(config, tmp_path)


def _seed(path: Path) -> pd.DataFrame:
    return pd.DataFrame(
        [{"repo_id": "1", "repo_name": "seed", "evidence_path": str(path), "evidence_filename": path.name}]
    )


# T15: legacy v1 remains relation-type only and does not require v2 columns.
def test_v1_reference_filter_remains_historical():
    frame = pd.DataFrame([
        {"relation_type": "Reference", "event_id": "ref"},
        {"relation_type": "EventAction", "event_id": "event"},
    ])
    retained, counters = _prepare_reference_evidence_chunk(
        frame, "1", strict_source_admission=False
    )
    assert retained["event_id"].tolist() == ["ref"]
    assert counters["retained_reference_rows"] == 1


# T16: strict v2 has no legacy fallback when admission schema is incomplete.
def test_v2_missing_source_admission_schema_blocks():
    frame = pd.DataFrame([{"relation_type": "Reference", "event_repo_id": "1"}])
    with pytest.raises(ValueError, match="strict v2 aggregate schema missing"):
        _prepare_reference_evidence_chunk(frame, "1", strict_source_admission=True)


# T17: rejected records are filtered before MembershipRegistry can observe them.
def test_v2_membership_input_excludes_out_of_seed_records(tmp_path):
    path = tmp_path / "evidence.csv"
    pd.DataFrame([
        _row(),
        _row(event_repo_id="9", status="OUT_OF_SEED_SOURCE_OBSERVATION", source_aggregate="R_9"),
    ]).to_csv(path, index=False)
    pipeline = _strict_pipeline(tmp_path)
    registry = MembershipRegistry(tmp_path / "membership.sqlite")
    try:
        pipeline._audit_memberships(_seed(path), registry)
        assert registry.conflicting_entities() == set()
        assert registry.summary()["unique_project_mappable_entities"] == 2
    finally:
        registry.close()


# T18: profiles and quotient counters consume the same admitted logical view.
def test_v2_scan_and_profile_input_excludes_rejected_records(tmp_path):
    path = tmp_path / "evidence.csv"
    pd.DataFrame([
        _row(),
        _row(event_repo_id="9", status="OUT_OF_SEED_SOURCE_OBSERVATION", source_aggregate="R_9"),
    ]).to_csv(path, index=False)
    pipeline = _strict_pipeline(tmp_path)
    pipeline._scan_evidence(_seed(path))
    assert pipeline.audit["input_reference_rows_before_source_admission"] == 2
    assert pipeline.audit["source_admitted_reference_rows"] == 1
    assert pipeline.audit["source_out_of_seed_reference_rows"] == 1
    assert pipeline.audit["retained_reference_rows"] == 1
    assert pipeline.project_profiles["1"]["total_reference_records"] == 1
    assert pipeline.edge_weights == {("1", "2"): 1}


# T19: a Fireproof-like rejected collection cannot affect membership or edges.
def test_rejected_records_cannot_contribute_to_membership_or_edge_counters(tmp_path):
    path = tmp_path / "evidence.csv"
    rejected = [
        _row(
            event_repo_id="600271677",
            status="OUT_OF_SEED_SOURCE_OBSERVATION",
            source_aggregate="R_600271677",
        )
        for _ in range(120)
    ]
    pd.DataFrame([_row(), *rejected]).to_csv(path, index=False)
    pipeline = _strict_pipeline(tmp_path)
    registry = MembershipRegistry(tmp_path / "membership.sqlite")
    try:
        pipeline._audit_memberships(_seed(path), registry)
        pipeline._scan_evidence(_seed(path))
        assert registry.conflicting_entities() == set()
        assert pipeline.audit["source_out_of_seed_reference_rows"] == 120
        assert pipeline.audit["quotient_eligible_records"] == 1
        assert pipeline.edge_weights == {("1", "2"): 1}
    finally:
        registry.close()


# T20: valid admitted records still reach all downstream logical inputs.
def test_admitted_record_is_retained_for_v2_processing():
    retained, counters = _prepare_reference_evidence_chunk(
        pd.DataFrame([_row()]), "1", strict_source_admission=True
    )
    assert len(retained) == 1
    assert counters["source_admitted_reference_rows"] == 1
    assert counters["retained_reference_rows"] == 1


# T21: the aggregate's declared context is an assertion against the current seed.
def test_v2_expected_context_must_match_current_seed():
    with pytest.raises(ValueError, match="expected_source_context_repo_id"):
        _prepare_reference_evidence_chunk(
            pd.DataFrame([_row(expected="2")]), "1", strict_source_admission=True
        )


def test_v2_declared_status_must_match_event_repository_identity():
    with pytest.raises(ValueError, match="admitted row does not match"):
        _prepare_reference_evidence_chunk(
            pd.DataFrame([_row(event_repo_id="9", status="ADMITTED_SOURCE_OBSERVATION")]),
            "1",
            strict_source_admission=True,
        )


# T22: the executable v2 alias is the corrected candidate aggregate root.
def test_v2_config_resolves_candidate_aggregate_root():
    config = load_config("configs/ch5_reference_quotient_p0_v2.yaml")
    inputs = resolved_inputs(config)
    assert inputs["gh_core_ref_node_agg_dir"] == inputs["gh_core_ref_node_agg_v2_dir"]
    assert validate_config(config, Path.cwd()) == []


# T23: v1 retains the historical aggregate root and has no strict opt-in mode.
def test_v1_config_resolves_historical_aggregate_root():
    config = load_config("configs/ch5_reference_quotient_p0.yaml")
    inputs = resolved_inputs(config)
    assert "v2_identity_corrected" not in str(inputs["gh_core_ref_node_agg_dir"])
    assert config.raw.get("identity_policy") is None
    assert validate_config(config, Path.cwd()) == []


# T24 and T25: the v2 admission boundary does not alter annotation timestamps or Titan IDs.
def test_repo_created_at_and_titan_identity_remain_untouched():
    row = pd.Series({
        "event_id": "titan-event",
        "relation_type": "Reference",
        "src_entity_id": "I_157514605#1",
        "src_entity_type": "Issue",
        "tar_entity_id": "R_2",
        "tar_entity_type": "Repo",
        "tar_entity_objnt_prop_dict": {"repo_id": 2},
        "event_repo_id": "157514605",
        "repo_created_at": "2018-11-14T08:18:40Z",
    })
    aggregated = granu_agg_with_event_provenance(row, "157514605")
    assert aggregated["repo_created_at"] == "2018-11-14T08:18:40Z"
    assert aggregated["src_entity_id_agg"] == "R_157514605"


# T26: preflight is read-only and does not create output or staging roots.
def test_v2_preflight_cannot_create_p0_output(tmp_path, monkeypatch):
    evidence = tmp_path / "evidence.csv"
    pd.DataFrame([_row()]).to_csv(evidence, index=False)
    base = load_config("configs/ch5_reference_quotient_p0_v2.yaml")
    raw = dict(base.raw)
    raw["frozen_output_root"] = "outputs/preflight_must_not_write"
    pipeline = RefQPipeline(RefQConfig(raw=raw), tmp_path)
    monkeypatch.setattr(pipeline, "_load_seed_manifests", lambda: (_seed(evidence), pd.DataFrame()))
    summary = pipeline.preflight()
    assert summary["retained_reference_rows"] == 1
    assert not pipeline.final_root.exists()
    assert not pipeline.staging_root.exists()
