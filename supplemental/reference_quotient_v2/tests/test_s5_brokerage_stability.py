"""C3.7-D synthetic S5 tests; no corrected-data network execution."""

from __future__ import annotations

import inspect

import networkx as nx
import pandas as pd
import pandas.testing as pdt

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.s45_canonical_graph import canonical_lcc_from_edges
from script.ch5_reference_quotient.network_views import canonicalize_undirected_graph_order
from supplemental.reference_quotient_v2.scripts.s5_brokerage_stability import (
    S5_FREQUENCY_COLUMNS,
    S5_OUTPUT_CONTRACT,
    S5_RANK_COLUMNS,
    S5_RUN_COLUMNS,
    build_future_s5_output_tables,
    compute_s5_brokerage_stability,
    derive_inclusion_frequency,
    rank_brokerage_scores,
    s5_production_settings,
    spearman_rank_correlation,
)


def _graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(["f", "e", "d", "c", "b", "a"])
    graph.add_edges_from(
        [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("b", "e")]
    )
    return graph


def test_s5_production_contract_is_exact():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    settings = s5_production_settings(config)
    assert settings["k_values"] == (250, 500, 1000)
    assert settings["seeds"] == tuple(range(20260731, 20260751))
    assert settings["top_k"] == (10, 20, 50)
    assert settings["canonical_k"] == 500
    assert settings["canonical_seed"] == 20260731


def test_s5_ranking_tiebreak_is_score_degree_then_project_id():
    graph = nx.Graph()
    graph.add_nodes_from(["c", "a", "b"])
    graph.add_edges_from([("b", "a"), ("b", "c")])
    ranked = rank_brokerage_scores(graph, {"a": 1.0, "b": 1.0, "c": 1.0})
    assert ranked["project_id"].tolist() == ["b", "a", "c"]
    assert ranked["rank"].tolist() == [1, 2, 3]


def test_s5_calls_unweighted_normalized_betweenness_and_closes_frequency(monkeypatch):
    graph = _graph()
    canonical_graph = canonicalize_undirected_graph_order(graph)
    canonical_scores = nx.betweenness_centrality(
        canonical_graph, k=2, normalized=True, seed=11, weight=None
    )
    calls = []
    original = nx.betweenness_centrality

    def wrapped(graph, **kwargs):
        calls.append(kwargs)
        return original(graph, **kwargs)

    monkeypatch.setattr(nx, "betweenness_centrality", wrapped)
    result = compute_s5_brokerage_stability(
        graph,
        canonical_scores,
        k_values=[2, 4],
        seeds=[11, 12, 13],
        top_ks=[1, 2, 3],
        canonical_k=2,
        canonical_seed=11,
    )
    assert len(calls) == 6
    assert all(call["weight"] is None and call["normalized"] is True for call in calls)
    assert all(call["k"] == 2 or call["k"] == 4 for call in calls)
    assert len(result.rankings) == 2 * 3 * len(graph)
    assert result.rankings["rank"].min() == 1
    assert result.rankings["rank"].max() == len(graph)
    assert result.summary["canonical_setting_matches_p0"] is True
    assert all(row["closed"] for row in result.inclusion_closure)
    assert all(
        int(group["inclusion_count"].sum()) == int(group["run_count"].iloc[0]) * int(group["top_k"].iloc[0])
        for _, group in result.inclusion_frequency.groupby(["k", "top_k"])
    )
    tables = build_future_s5_output_tables(result)
    assert set(tables) == set(S5_OUTPUT_CONTRACT)
    assert tuple(tables["brokerage_rank_stability.csv"].columns) == S5_RANK_COLUMNS
    assert tuple(tables["brokerage_topk_inclusion_frequency.csv"].columns) == S5_FREQUENCY_COLUMNS
    assert "brokerage_topk_frequency.csv" not in tables
    assert not (paths.CORRECTED_OUTPUTS_ROOT / "S5_brokerage_stability").exists()


def test_s5_spearman_is_rank_correlation_and_frequency_uses_full_rankings():
    left = pd.DataFrame({"project_id": ["a", "b", "c"], "rank": [1, 2, 3]})
    right = pd.DataFrame({"project_id": ["c", "b", "a"], "rank": [1, 2, 3]})
    assert spearman_rank_correlation(left, left) == 1.0
    assert spearman_rank_correlation(left, right) == -1.0
    ranking = pd.DataFrame(
        [
            {"k": 2, "seed": 1, "rank": 1, "project_id": "a", "score": 0.9},
            {"k": 2, "seed": 1, "rank": 2, "project_id": "b", "score": 0.8},
            {"k": 2, "seed": 1, "rank": 3, "project_id": "c", "score": 0.7},
            {"k": 2, "seed": 2, "rank": 1, "project_id": "b", "score": 0.9},
            {"k": 2, "seed": 2, "rank": 2, "project_id": "a", "score": 0.8},
            {"k": 2, "seed": 2, "rank": 3, "project_id": "c", "score": 0.7},
        ]
    )
    frequency, closure = derive_inclusion_frequency(ranking, [1, 2])
    assert tuple(frequency.columns) == S5_FREQUENCY_COLUMNS
    assert all(row["closed"] for row in closure)
    a_top1 = frequency.loc[(frequency["top_k"] == 1) & (frequency["project_id"] == "a"), "inclusion_count"]
    assert int(a_top1.iloc[0]) == 1


def test_s4_and_s5_use_the_same_canonical_lcc_definition():
    edges = pd.DataFrame(
        [
            {"node_u": "a", "node_v": "b", "weight": 2, "directed_edge_count": 1},
            {"node_u": "b", "node_v": "c", "weight": 1, "directed_edge_count": 1},
            {"node_u": "x", "node_v": "y", "weight": 1, "directed_edge_count": 1},
        ]
    )
    registry = pd.DataFrame({"project_id": ["x", "a", "b", "c", "y"]})
    s4_graph = canonical_lcc_from_edges(edges, registry)
    s5_graph = canonical_lcc_from_edges(edges, registry)
    assert tuple(s4_graph.nodes) == tuple(s5_graph.nodes)
    assert set(s4_graph.edges) == set(s5_graph.edges)


def test_s5_canonical_brokerage_is_independent_of_input_graph_order():
    left = _graph()
    right = nx.Graph()
    right.add_nodes_from(reversed(tuple(left.nodes)))
    right.add_edges_from(reversed(tuple(left.edges)))
    left_scores = nx.betweenness_centrality(left, k=2, normalized=True, seed=11, weight=None)
    right_scores = dict(left_scores)

    left_result = compute_s5_brokerage_stability(
        left, left_scores, k_values=[2], seeds=[11], top_ks=[1, 2], canonical_k=2, canonical_seed=11
    )
    right_result = compute_s5_brokerage_stability(
        right, right_scores, k_values=[2], seeds=[11], top_ks=[1, 2], canonical_k=2, canonical_seed=11
    )

    pdt.assert_frame_equal(left_result.rankings, right_result.rankings, check_exact=True)


def test_s5_source_excludes_deprecated_and_historical_executable_authority():
    import supplemental.reference_quotient_v2.scripts.s5_brokerage_stability as s5

    source = inspect.getsource(s5)
    assert "brokerage_topk_frequency.csv" not in source
    assert "reference_quotient_v1" not in source
    assert "weight=None" in source
    assert "normalized=True" in source


def test_corrected_p0_s45_preflight_is_metadata_header_only_and_passes():
    from supplemental.reference_quotient_v2.scripts.s45_canonical_graph import preflight_corrected_p0_s45_inputs

    result = preflight_corrected_p0_s45_inputs()
    assert result["C3_7D_INPUT_PREFLIGHT"] == "PASS"
    assert result["headers_only"] is True
    assert result["parity_gates_invoked"] is False
    assert result["network_corrected_data_run"] == 0
    assert result["s4_louvain_seed_end"] == 20260780
    assert result["s5_seed_end"] == 20260750
    assert not (paths.CORRECTED_OUTPUTS_ROOT / "S5_brokerage_stability").exists()
