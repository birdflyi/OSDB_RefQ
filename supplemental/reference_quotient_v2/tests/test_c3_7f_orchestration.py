"""Fixture-only C3.7-F G18 orchestration and package-lifecycle tests."""

from __future__ import annotations

import hashlib
import json

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts.manifest import (
    S7Status,
    build_corrected_package_manifest,
    validate_package_manifest,
)
from supplemental.reference_quotient_v2.scripts.orchestrator import (
    AUTHORIZED_BRANCH,
    OrchestrationError,
    STAGE_PHASES,
    _canonical_stage,
    authorize_stage,
    execute_stage_control_plane,
    run_stage,
)
from supplemental.reference_quotient_v2.scripts.paths import load_config
from supplemental.reference_quotient_v2.scripts.s6_figure_ready import (
    resolve_s6_source_bundle,
    serialize_s6_figure_ready_bundle,
)
from supplemental.reference_quotient_v2.scripts.stage_io import (
    CORRECTED_AGGREGATE,
    CORRECTED_P0,
    STAGE_DIRECTORY_NAMES,
    STAGE_RECEIPT_NAME,
    fixture_authority_roots,
    stage_output_inventory,
    write_stage_outputs,
)
from supplemental.reference_quotient_v2.tests.test_s6_figure_ready import _fixture


def _mock_valid_git_state(monkeypatch):
    def fake_git_value(*arguments):
        if arguments == ("branch", "--show-current"):
            return AUTHORIZED_BRANCH
        if arguments == ("status", "--porcelain"):
            return ""
        raise AssertionError(arguments)

    monkeypatch.setattr("supplemental.reference_quotient_v2.scripts.orchestrator._git_value", fake_git_value)
    monkeypatch.setattr("supplemental.reference_quotient_v2.scripts.orchestrator._is_ancestor", lambda commit: True)
    monkeypatch.setattr("supplemental.reference_quotient_v2.scripts.orchestrator._implementation_diff", lambda commit: ())


@pytest.mark.parametrize("short,canonical", tuple(STAGE_DIRECTORY_NAMES.items()))
def test_production_authorization_maps_short_and_canonical_stage_names(monkeypatch, short, canonical):
    _mock_valid_git_state(monkeypatch)
    assert authorize_stage(
        short,
        authorization_phase="C4-%s" % short,
        expected_implementation_commit="e4159f1183463085c68cf1cca5549c083404d16b",
    ) == canonical
    assert authorize_stage(
        canonical,
        authorization_phase="C4-%s" % short,
        expected_implementation_commit="e4159f1183463085c68cf1cca5549c083404d16b",
    ) == canonical


@pytest.mark.parametrize("short,canonical", tuple(STAGE_DIRECTORY_NAMES.items()))
def test_production_authorization_rejects_wrong_phase_as_orchestration_error(monkeypatch, short, canonical):
    _mock_valid_git_state(monkeypatch)
    wrong_phase = "C4-S%s" % ((int(short[1:]) % 6) + 1)
    with pytest.raises(OrchestrationError, match="authorization phase"):
        authorize_stage(
            canonical,
            authorization_phase=wrong_phase,
            expected_implementation_commit="e4159f1183463085c68cf1cca5549c083404d16b",
        )


def test_production_authorization_rejects_unknown_stage_and_phase_map_is_closed(monkeypatch):
    _mock_valid_git_state(monkeypatch)
    with pytest.raises(OrchestrationError, match="stage must be one of S1-S6"):
        authorize_stage(
            "S8",
            authorization_phase="C4-S8",
            expected_implementation_commit="e4159f1183463085c68cf1cca5549c083404d16b",
        )
    assert set(STAGE_PHASES) == set(STAGE_DIRECTORY_NAMES.values())
    assert {_canonical_stage(short) for short in STAGE_DIRECTORY_NAMES} == set(STAGE_PHASES)


def test_run_stage_production_entrypoint_dry_run_reaches_preflight(monkeypatch):
    _mock_valid_git_state(monkeypatch)
    result = run_stage(
        "S2",
        authorization_phase="C4-S2",
        expected_implementation_commit="e4159f1183463085c68cf1cca5549c083404d16b",
        baseline_path="docs/freeze/ch5_refq_c3_7f_historical_immutability_baseline_v1.json",
        dry_run=True,
    )
    assert result["status"] == "PREFLIGHT_PASS"
    assert result["stage"] == "S2_weight_sensitivity"
    assert result["scientific_execution"] is False


def _record(path, authority, root, version):
    return {
        "path": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "authority_class": authority,
        "root": str(root),
        "version": version,
    }


def _pipeline_fixture(tmp_path):
    p0, _, _ = _fixture(tmp_path / "sources")
    for name in (
        "reference_quotient_node_registry.csv",
        "analysis_seed_manifest_294.csv",
        "rq2c_undirected_view_edges.csv",
        "rq2c_undirected_view_lcc_edges.csv",
    ):
        (p0 / name).write_text("value\n1\n", encoding="utf-8")
    aggregate = tmp_path / "aggregate"
    aggregate.mkdir()
    (aggregate / "partition.csv").write_text("value\n1\n", encoding="utf-8")
    output_root = tmp_path / "outputs"
    context = fixture_authority_roots(
        corrected_aggregate=aggregate,
        corrected_p0=p0,
        corrected_supplemental=output_root,
    )
    return p0, aggregate, output_root, context


def _inputs(stage, p0, aggregate):
    if stage == "S1":
        return (_record(aggregate / "partition.csv", CORRECTED_AGGREGATE, aggregate, "corrected_aggregate_v2"),)
    if stage == "S2":
        names = ("reference_quotient_cross_project_edges.csv", "reference_quotient_node_registry.csv")
    elif stage == "S3":
        names = ("reference_quotient_cross_project_edges.csv", "reference_quotient_node_registry.csv", "analysis_seed_manifest_294.csv")
    else:
        names = (
            "rq2c_undirected_view_edges.csv", "rq2c_undirected_view_lcc_edges.csv",
            "reference_quotient_node_registry.csv", "rq2c_algorithmic_communities.csv",
            "rq2c_undirected_view_summary.json", "rq2c_structural_brokerage_candidates.csv",
        )
    return tuple(_record(p0 / name, CORRECTED_P0, p0, "corrected_p0_v2") for name in names)


def _artifacts(stage):
    result = {}
    for name in stage_output_inventory(stage):
        if name.endswith(".json"):
            result[name] = {"status": "PASS", "fixture": True}
        elif name == "louvain_stability_runs.csv":
            result[name] = pd.DataFrame({"seed": [1], "community_count": [2]})
        elif name == "brokerage_stability_runs.csv":
            result[name] = pd.DataFrame({"k": [2], "seed": [1], "top50_overlap": [1.0]})
        else:
            result[name] = pd.DataFrame({"value": [1]})
    return result


def _run_simple(stage, p0, aggregate, output_root, context):
    return execute_stage_control_plane(
        stage,
        output_root=output_root,
        authority_roots=context,
        historical_check=lambda: {"status": "HISTORICAL_IMMUTABILITY_MATCH"},
        executor=lambda: write_stage_outputs(
            output_root, stage, _artifacts(stage),
            implementation_commit="fixture",
            input_artifacts=_inputs(stage, p0, aggregate),
            authority_roots=context,
            expected_output_root=output_root,
            allow_external_test_root=True,
            enforce_contract=True,
        ),
    )


@pytest.mark.parametrize("stage", ("S2", "S3", "S4", "S5", "S6"))
def test_downstream_stage_blocks_before_required_upstream(stage, tmp_path):
    p0, aggregate, output_root, context = _pipeline_fixture(tmp_path)
    with pytest.raises(OrchestrationError, match="upstream durable receipt"):
        _run_simple(stage, p0, aggregate, output_root, context)
    assert not output_root.exists()


def test_full_fixture_pipeline_is_separate_fail_closed_and_not_release_ready(tmp_path):
    p0, aggregate, output_root, context = _pipeline_fixture(tmp_path)
    traces = []
    for stage in ("S1", "S2", "S3", "S4", "S5"):
        traces.append(_run_simple(stage, p0, aggregate, output_root, context))
    source_bundle = resolve_s6_source_bundle(
        corrected_p0_root=p0,
        corrected_supplemental_root=output_root,
        allow_fixture_roots=True,
    )
    s6_trace = execute_stage_control_plane(
        "S6",
        output_root=output_root,
        authority_roots=context,
        historical_check=lambda: {"status": "HISTORICAL_IMMUTABILITY_MATCH"},
        executor=lambda: serialize_s6_figure_ready_bundle(
            source_bundle,
            output_root,
            implementation_commit="fixture",
            authority_roots=context,
            expected_output_root=output_root,
            allow_external_test_root=True,
        )[1],
    )
    traces.append(s6_trace)
    assert [trace["stage"] for trace in traces] == list(STAGE_DIRECTORY_NAMES.values())
    with pytest.raises(OrchestrationError, match="already exists"):
        _run_simple("S1", p0, aggregate, output_root, context)

    receipts = {stage: json.loads((output_root / stage / STAGE_RECEIPT_NAME).read_text(encoding="utf-8")) for stage in STAGE_DIRECTORY_NAMES.values()}
    package = build_corrected_package_manifest(
        load_config(), receipts,
        implementation_commit="fixture",
        branch="fixture",
        s7_status=S7Status.NOT_EVALUATED,
        historical_write_audit={"status": "PASS", "historical_roots_modified": False, "no_overwrite": True},
        authority_roots=context,
        expected_output_root=output_root,
        enforce_stage_contract=True,
    )
    result = validate_package_manifest(
        package, authority_roots=context, expected_output_root=output_root,
        enforce_stage_contract=True,
    )
    assert result["stage_package_complete"] is True
    assert result["release_ready"] is False
    assert result["s7_status"] == "NOT_EVALUATED"
    assert not (output_root / "manifest.json").exists()


@pytest.mark.parametrize("tamper", ("missing_marker", "wrong_hash", "wrong_root", "failed_status", "incomplete_output"))
def test_invalid_upstream_receipt_blocks_downstream(tamper, tmp_path):
    p0, aggregate, output_root, context = _pipeline_fixture(tmp_path)
    _run_simple("S1", p0, aggregate, output_root, context)
    marker = output_root / "S1_evidence_universe" / STAGE_RECEIPT_NAME
    if tamper == "missing_marker":
        marker.unlink()
    else:
        receipt = json.loads(marker.read_text(encoding="utf-8"))
        if tamper == "wrong_hash":
            receipt["output_artifacts"][0]["sha256"] = "0" * 64
        elif tamper == "wrong_root":
            receipt["output_root"] = str(tmp_path / "wrong")
        elif tamper == "failed_status":
            receipt["status"] = "FAIL"
        else:
            receipt["output_artifacts"] = receipt["output_artifacts"][:-1]
        marker.write_text(json.dumps(receipt), encoding="utf-8")
    with pytest.raises(OrchestrationError, match="upstream receipt blocks|upstream durable receipt"):
        _run_simple("S2", p0, aggregate, output_root, context)
    assert not (output_root / "S2_weight_sensitivity").exists()
