from pathlib import Path

import json
import pandas as pd


ROOT = Path(__file__).parents[3]
OUTPUT = ROOT / "supplemental" / "reference_quotient_v1" / "outputs"
CANONICAL = ROOT / "outputs" / "reference_quotient_p0_frozen"


def test_s1_flow_closes_exactly():
    flow = pd.read_csv(OUTPUT / "S1_evidence_universe" / "evidence_universe_flow.csv")
    values = dict(zip(flow["stage"], flow["count"]))
    assert values["all_observable_reference_records"] == 3748078
    assert values["target_project_mappable_records"] + values["target_non_project_records"] + values["target_unresolved_records"] == 3748078
    assert values["quotient_eligible_records"] == 1586117
    assert values["self_loop_evidence_weight"] + values["cross_project_evidence_weight"] == 1586117


def test_s1_cross_tabs_reconcile():
    audit = json.loads((OUTPUT / "S1_evidence_universe" / "evidence_universe_validation.json").read_text(encoding="utf-8"))
    assert audit["cross_tab_total_reconciliation"] is True
    assert audit["raw_reference_rows"] == 3748078


def test_s2_threshold_one_matches_canonical():
    row = pd.read_csv(OUTPUT / "S2_weight_sensitivity" / "edge_weight_sensitivity.csv")
    one = row[row["threshold"] == 1].iloc[0]
    summary = json.loads((CANONICAL / "rq2c_undirected_view_summary.json").read_text(encoding="utf-8"))
    assert int(one["undirected_edges"]) == summary["undirected_edges"]
    assert int(one["lcc_nodes"]) == summary["lcc_nodes"]
    assert int(one["lcc_edges"]) == summary["lcc_edges"]
    assert abs(float(one["modularity"]) - summary["modularity"]) < 1e-12


def test_s2_threshold_is_before_undirected_collapse():
    row = pd.read_csv(OUTPUT / "S2_weight_sensitivity" / "edge_weight_sensitivity.csv")
    assert (row["directed_edges_retained"] >= row["undirected_edges"]).all()


def test_s3_seed_only_domain_is_exactly_294():
    rows = pd.read_csv(OUTPUT / "S3_observation_sensitivity" / "observation_boundary_sensitivity.csv")
    seed_only = rows[rows["view"] == "SEED_ONLY_INDUCED"].iloc[0]
    assert int(seed_only["nodes"]) == 294


def test_s4_canonical_seed_matches():
    rows = pd.read_csv(OUTPUT / "S4_community_stability" / "louvain_stability_runs.csv")
    canonical = rows[rows["seed"] == 20260731].iloc[0]
    assert int(canonical["community_count"]) == 34
    assert abs(float(canonical["modularity"]) - 0.7973095950243088) < 1e-12


def test_s5_canonical_setting_matches():
    rows = pd.read_csv(OUTPUT / "S5_brokerage_stability" / "brokerage_stability_runs.csv")
    canonical = rows[(rows["seed"] == 20260731) & (rows["k"] == 500)].iloc[0]
    assert canonical["canonical_score_match"]
    assert canonical["top50_overlap"] == 1.0


def test_no_second_order_operator_appears():
    paths = [OUTPUT / "manifest.json"] + list((OUTPUT / "S6_figure_ready").rglob("*"))
    for path in paths:
        if path.is_file() and path.suffix in {".json", ".csv", ".md"}:
            assert "QQ^T" not in path.read_text(encoding="utf-8")
            assert "Q^TQ" not in path.read_text(encoding="utf-8")


def test_canonical_output_hash_audit_passes():
    audit = json.loads((OUTPUT / "canonical_immutability_audit.json").read_text(encoding="utf-8"))
    assert audit["canonical_output_bytes_changed"] == 0
