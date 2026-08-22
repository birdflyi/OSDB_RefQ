from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).parents[4]
PATCH = ROOT / "supplemental" / "reference_quotient_v1" / "v1_2_s3_reproducibility_patch"
OUTPUT = PATCH / "outputs" / "S3_observation_sensitivity_corrected"


def test_canonical_row_exactly_recovers_p0():
    frame = pd.read_csv(OUTPUT / "observation_boundary_sensitivity_corrected.csv")
    row = frame.loc[frame["view"] == "CANONICAL_SEED_CENTERED_OBSERVED"].iloc[0]
    assert int(row["nodes"]) == 6515
    assert int(row["undirected_edges"]) == 9557
    assert int(row["lcc_nodes"]) == 6376
    assert int(row["lcc_edges"]) == 9472
    assert abs(float(row["average_clustering_lcc"]) - 0.042197888645088825) < 1e-12
    assert abs(float(row["transitivity_lcc"]) - 0.008046186665820756) < 1e-12
    assert int(row["algorithmic_communities"]) == 34
    assert abs(float(row["modularity"]) - 0.7973095950243088) < 1e-12
    assert int(row["random_seed"]) == 20260731


def test_non_stochastic_metrics_do_not_drift_from_old_s3():
    comparison = pd.read_csv(PATCH / "old_vs_corrected_s3_summary.csv")
    columns = [
        "directed_edges", "directed_weight", "undirected_edges", "nodes",
        "edge_observed_nodes", "components", "isolates", "lcc_nodes",
        "lcc_edges", "lcc_coverage", "average_clustering_lcc",
        "transitivity_lcc", "random_seed",
    ]
    for column in columns:
        assert comparison[f"delta_{column}"].abs().max() < 1e-12


def test_all_three_views_exist_and_retain_fixed_domains():
    frame = pd.read_csv(OUTPUT / "observation_boundary_sensitivity_corrected.csv")
    assert set(frame["view"]) == {
        "CANONICAL_SEED_CENTERED_OBSERVED",
        "SEED_ONLY_INDUCED",
        "MULTI_SEED_TARGET_VIEW",
    }
    assert int(frame.loc[frame["view"] == "SEED_ONLY_INDUCED", "nodes"].iloc[0]) == 294


def test_immutability_and_s2_exclusion():
    manifest = json.loads((PATCH / "s3_reproducibility_patch_manifest.json").read_text(encoding="utf-8"))
    assert manifest["canonical_p0_sha_drift"] is False
    assert manifest["other_supplemental_sha_drift"] is False
    assert manifest["existing_s3_sha_drift"] is False
    assert manifest["raw_rescan_count"] == 0
    assert manifest["s2_status"] == "EXCLUDED_PENDING_WEIGHT_SEMANTICS_AUDIT"
