"""C3.7-E temporary-source tests for corrected S6 derivation."""

from __future__ import annotations

import copy
import json
from dataclasses import replace

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.s4_community_stability import S4_OUTPUT_CONTRACT
from supplemental.reference_quotient_v2.scripts.s5_brokerage_stability import S5_OUTPUT_CONTRACT
from supplemental.reference_quotient_v2.scripts.s6_figure_ready import (
    CORRECTED_P0,
    CORRECTED_SUPPLEMENTAL_V2,
    S6_DEPRECATED_OUTPUTS,
    S6_OUTPUT_INVENTORY,
    build_s6_figure_ready_bundle,
    preflight_corrected_p0_s6_inputs,
    resolve_s6_source_bundle,
    serialize_s6_figure_ready_bundle,
    validate_s6_manifest_sha_closure,
)
from supplemental.reference_quotient_v2.scripts.s6_figure_ready import S6ContractError


def _write_csv(root, name, frame):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def _fixture(tmp_path):
    p0 = tmp_path / "corrected_p0"
    v2 = tmp_path / "corrected_supplemental_v2_outputs"
    simple = {
        "rq1_referencing_entity_distribution.csv": pd.DataFrame({"referencing_entity_type": ["Repository"], "count": [2], "share": [1.0]}),
        "rq1_referenced_entity_distribution.csv": pd.DataFrame({"referenced_entity_type": ["Repository"], "count": [2], "share": [1.0]}),
        "rq1_event_type_distribution.csv": pd.DataFrame({"event_type": ["Issue"], "count": [2], "share": [1.0]}),
        "rq1_project_age_cross_sectional_association.csv": pd.DataFrame({"metric": ["x"], "n": [2], "spearman_rho": [0.5], "p_value": [0.1], "design": ["fixture"]}),
        "rq3_subdomain_descriptive_comparison.csv": pd.DataFrame({"label_mode": ["a"], "feature": ["x"], "category": ["c"], "n": [2], "mean": [1.0], "median": [1.0], "std": [0.0]}),
        "rq3_kruskal_fdr_effect_sizes.csv": pd.DataFrame({"label_mode": ["a"], "feature": ["x"], "groups": [2], "n_with_replacement": [2], "categories": ["c"], "kruskal_h": [1.0], "p_value": [0.5], "epsilon_squared": [0.1], "test_status": ["PASS"], "fdr_bh_p_value": [0.5], "fdr_bh_reject_0_05": [False]}),
        "rq1_project_reference_profiles.csv": pd.DataFrame({
            "self_reference_ratio": [0.0, 1.0], "external_reference_share": [1.0, 0.0], "non_project_reference_share": [0.0, 0.0],
            "unresolved_target_reference_records": [0, 1], "comment_reference_density": [0.0, 0.5], "project_age_years_at_2023_end": [1.0, 3.0],
        }),
        "rq2a_source_role_metrics.csv": pd.DataFrame({
            "out_degree": [1, 2], "out_strength": [2, 4], "seed_to_seed_weight": [1, 2], "seed_to_expanded_weight": [1, 2],
            "source_concentration_hhi": [0.25, 0.5], "top_target_weight_share": [0.5, 1.0],
        }),
        "rq2b_target_role_metrics.csv": pd.DataFrame({
            "in_degree": [1, 2], "in_strength": [2, 4], "target_coverage": [0.5, 1.0], "cumulative_weight_share": [0.25, 1.0],
        }),
        "reference_quotient_cross_project_edges.csv": pd.DataFrame({"source_project_id": ["a", "b"], "target_project_id": ["b", "a"], "weight": [2, 4]}),
        "rq2c_algorithmic_communities.csv": pd.DataFrame({"project_id": ["a", "b", "c"], "community_id": [0, 0, 1], "community_size": [2, 2, 1]}),
        "rq2c_structural_brokerage_candidates.csv": pd.DataFrame({"project_id": ["a", "b"], "betweenness_brokerage": [0.2, 0.1]}),
        "rq2c_structural_brokerage_top50.csv": pd.DataFrame({"project_id": ["a", "b"], "betweenness_brokerage": [0.2, 0.1]}),
    }
    for name, frame in simple.items():
        _write_csv(p0, name, frame)
    (p0 / "rq2c_undirected_view_summary.json").write_text(
        json.dumps({"modularity": 0.5, "random_seed": 20260731, "brokerage_sample_size": 500, "nodes": 3}, indent=2),
        encoding="utf-8",
    )
    _write_csv(v2 / "S4_community_stability", "louvain_stability_runs.csv", pd.DataFrame({"seed": [1], "community_count": [2]}))
    _write_csv(v2 / "S5_brokerage_stability", "brokerage_stability_runs.csv", pd.DataFrame({"k": [2], "seed": [1], "top50_overlap": [1.0]}))
    bundle = resolve_s6_source_bundle(corrected_p0_root=p0, corrected_supplemental_root=v2, allow_fixture_roots=True)
    return p0, v2, bundle


def test_s6_exact_inventory_and_historical_transform_semantics(tmp_path):
    _, _, source_bundle = _fixture(tmp_path)
    result = build_s6_figure_ready_bundle(source_bundle)
    assert tuple(result.tables) == S6_OUTPUT_INVENTORY
    assert all(name.endswith(".csv") for name in result.tables)
    assert not set(S6_DEPRECATED_OUTPUTS).intersection(result.tables)
    assert result.tables["rq1_profile_quantiles.csv"]["quantile"].tolist() == ["min", "q25", "median", "q75", "max"] * 6
    assert result.tables["rq2a_source_role_ecdf_ccdf.csv"]["value"].tolist() == [1.0, 2.0, 2.0, 4.0, 1.0, 2.0, 1.0, 2.0, 0.25, 0.5, 0.5, 1.0]
    assert result.tables["rq2a_source_role_ecdf_ccdf.csv"]["ccdf"].iloc[-1] == pytest.approx(0.5)
    assert result.tables["community_size_distribution.csv"].to_dict("records") == [
        {"community_id": 0, "community_size": 2}, {"community_id": 1, "community_size": 1}
    ]
    assert tuple(result.tables["structural_summary.csv"].columns) == ("brokerage_sample_size", "modularity", "nodes", "random_seed")
    assert result.transformations["structural_summary.csv"] == "corrected_p0_summary_json_to_csv"
    assert result.output_sources["structural_summary.csv"][0].authority_class == CORRECTED_P0
    assert result.output_sources["louvain_stability_plot.csv"][0].authority_class == CORRECTED_SUPPLEMENTAL_V2


def test_s6_temp_serialization_manifest_and_sha_closure(tmp_path):
    _, _, source_bundle = _fixture(tmp_path)
    _, receipt, manifest = serialize_s6_figure_ready_bundle(
        source_bundle,
        tmp_path / "output_root",
        implementation_commit="fixture",
        completed_at="2026-08-26T00:00:00+00:00",
    )
    manifest_path = tmp_path / "output_root" / "S6_figure_ready" / "figure_ready_manifest_v2.json"
    assert receipt.stage == "S6_figure_ready"
    assert manifest["schema_version"] == "figure_ready_manifest_v2"
    assert validate_s6_manifest_sha_closure(manifest_path)["status"] == "PASS"
    assert "structural_summary.json" not in [entry["output"] for entry in manifest["entries"]]
    assert (manifest_path.parent / "structural_summary.csv").is_file()
    assert not (manifest_path.parent / "structural_summary.json").exists()


def test_s6_sha_closure_rejects_wrong_output_and_source_hash(tmp_path):
    _, _, source_bundle = _fixture(tmp_path)
    _, _, manifest = serialize_s6_figure_ready_bundle(source_bundle, tmp_path / "output_root")
    manifest_path = tmp_path / "output_root" / "S6_figure_ready" / "figure_ready_manifest_v2.json"
    bad_output = copy.deepcopy(manifest)
    bad_output["entries"][0]["output_sha256"] = "0" * 64
    with pytest.raises(S6ContractError, match="output SHA"):
        validate_s6_manifest_sha_closure(bad_output, manifest_directory=manifest_path.parent)
    source = source_bundle.source("p0/rq1_referencing_entity_distribution.csv").path
    original = source.read_text(encoding="utf-8")
    source.write_text(original + "\n", encoding="utf-8")
    try:
        with pytest.raises(S6ContractError, match="source SHA"):
            validate_s6_manifest_sha_closure(manifest_path)
    finally:
        source.write_text(original, encoding="utf-8")


def test_s6_rejects_historical_roots_and_cross_root_source_records(tmp_path):
    with pytest.raises(S6ContractError):
        resolve_s6_source_bundle(corrected_p0_root=paths.HISTORICAL_P0_ROOT, corrected_supplemental_root=tmp_path / "v2", allow_fixture_roots=True)
    with pytest.raises(S6ContractError):
        resolve_s6_source_bundle(corrected_p0_root=tmp_path / "p0", corrected_supplemental_root=paths.HISTORICAL_SUPPLEMENTAL_ROOT / "v1_1_completion", allow_fixture_roots=True)
    _, _, bundle = _fixture(tmp_path)
    source = bundle.source("p0/rq1_referencing_entity_distribution.csv")
    altered = replace(source, root=tmp_path / "other_root")
    bad_sources = dict(bundle.sources)
    bad_sources[source.key] = altered
    bad_bundle = replace(bundle, sources=bad_sources)
    with pytest.raises(S6ContractError, match="crosses"):
        build_s6_figure_ready_bundle(bad_bundle)


def test_s6_corrected_p0_preflight_is_header_only_and_contracts_are_v2():
    result = preflight_corrected_p0_s6_inputs()
    assert result["C3_7E_INPUT_PREFLIGHT"] == "PASS"
    assert result["headers_only"] is True
    assert result["corrected_data_s6_run"] is False
    assert result["future_s4_s5_sources_resolved_under_v2"] is True
    assert result["historical_fallback_present"] is False
    assert result["s6_output_inventory"] == list(S6_OUTPUT_INVENTORY)
    assert set(S4_OUTPUT_CONTRACT) == {"louvain_stability_runs.csv", "louvain_stability_pairwise.csv", "louvain_stability_summary.json"}
    assert "brokerage_topk_frequency.csv" not in S5_OUTPUT_CONTRACT
    assert paths.CORRECTED_OUTPUTS_ROOT.exists() is False
