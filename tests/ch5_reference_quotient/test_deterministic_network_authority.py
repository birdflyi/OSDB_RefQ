from __future__ import annotations

import math
from pathlib import Path

import networkx as nx
import pandas as pd
import pandas.testing as pdt

from script.ch5_reference_quotient.network_views import analyze_undirected_view


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
P0_ROOT = REPOSITORY_ROOT / "outputs" / "reference_quotient_p0_corrected_v3"
FROZEN_S2_ROOT = REPOSITORY_ROOT / "supplemental" / "reference_quotient_v2" / "outputs" / "S2_weight_sensitivity"


def _load_registry() -> pd.DataFrame:
    return pd.read_csv(P0_ROOT / "reference_quotient_node_registry.csv", dtype={"project_id": "string"})


def _analyze_threshold(threshold: int):
    edges = pd.read_csv(
        FROZEN_S2_ROOT / ("threshold_%s_undirected_edges.csv" % threshold),
        dtype={"node_u": "string", "node_v": "string"},
    )
    registry = _load_registry()
    return analyze_undirected_view(
        edges,
        random_seed=20260731,
        brokerage_sample_size=500,
        node_ids=registry["project_id"].astype(str),
    )


def test_frozen_s2_threshold_summaries_have_one_deterministic_clean_profile():
    expected = {
        1: (35, 0.7969220043681785),
        2: (31, 0.7970287474802773),
        5: (28, 0.7962674935766076),
        10: (21, 0.7851714821417686),
    }
    for threshold, (community_count, modularity) in expected.items():
        summary, _, _, _ = _analyze_threshold(threshold)
        assert summary["algorithmic_communities"] == community_count
        assert math.isclose(summary["modularity"], modularity, rel_tol=0.0, abs_tol=1e-12)


def test_deterministic_threshold_one_preserves_p0v3_partition_modularity_brokerage_and_sizes():
    summary, _, communities, brokerage = _analyze_threshold(1)
    expected_communities = pd.read_csv(
        P0_ROOT / "rq2c_algorithmic_communities.csv", dtype={"project_id": "string"}
    ).sort_values("project_id").reset_index(drop=True)
    expected_brokerage = pd.read_csv(
        P0_ROOT / "rq2c_structural_brokerage_candidates.csv", dtype={"project_id": "string"}
    ).sort_values("project_id").reset_index(drop=True)
    actual_communities = communities.sort_values("project_id").reset_index(drop=True)
    actual_brokerage = brokerage.sort_values("project_id").reset_index(drop=True)

    pdt.assert_frame_equal(actual_communities, expected_communities, check_dtype=False, check_exact=True)
    pdt.assert_series_equal(
        actual_brokerage["betweenness_brokerage"],
        expected_brokerage["betweenness_brokerage"],
        check_names=False,
        check_exact=False,
        rtol=0.0,
        atol=1e-12,
    )
    assert summary["algorithmic_communities"] == 35
    assert math.isclose(summary["modularity"], 0.7969220043681785, rel_tol=0.0, abs_tol=1e-12)
    observed_sizes = actual_communities.groupby("community_id").size()
    recorded_sizes = actual_communities.groupby("community_id")["community_size"].first()
    assert observed_sizes.to_dict() == recorded_sizes.to_dict()


def test_deterministic_analysis_ignores_threshold_edge_and_node_row_order():
    edges = pd.read_csv(
        FROZEN_S2_ROOT / "threshold_5_undirected_edges.csv",
        dtype={"node_u": "string", "node_v": "string"},
    )
    registry = _load_registry()
    left = analyze_undirected_view(edges, 20260731, 500, registry["project_id"])
    right = analyze_undirected_view(
        edges.sample(frac=1, random_state=91).reset_index(drop=True),
        20260731,
        500,
        registry.sample(frac=1, random_state=37)["project_id"],
    )
    assert left[0] == right[0]
    pdt.assert_frame_equal(
        left[2].sort_values("project_id").reset_index(drop=True),
        right[2].sort_values("project_id").reset_index(drop=True),
        check_exact=True,
    )
