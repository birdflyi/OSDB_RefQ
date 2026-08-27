"""C4 positive-path dynamic parity-gate regression tests.

These tests use small temporary authority roots and monkeypatch only the
production root/authority boundary.  They execute the real comparison bodies
and verify that both matching and mutated authority artifacts fail closed.
"""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import networkx as nx
import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import (
    s2_weight_sensitivity as s2,
    s3_observation_sensitivity as s3,
    s4_community_stability as s4,
    s5_brokerage_stability as s5,
)


def _write_frame(root: Path, name: str, frame: pd.DataFrame) -> None:
    frame.to_csv(root / name, index=False)


def _s2_inputs() -> tuple[pd.DataFrame, pd.DataFrame]:
    edges = pd.DataFrame(
        [
            {"source_project_id": "2", "target_project_id": "10", "weight": 1},
            {"source_project_id": "10", "target_project_id": "2", "weight": 2},
            {"source_project_id": "10", "target_project_id": "100", "weight": 1},
        ]
    )
    return edges, pd.DataFrame({"project_id": ["2", "10", "100"]})


def test_s2_positive_parity_path_and_mutations_fail_closed(tmp_path, monkeypatch):
    edges, registry = _s2_inputs()
    result = s2.compute_s2_weight_sensitivity(
        edges,
        registry,
        thresholds=[1],
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    monkeypatch.setattr(s2, "CORRECTED_P0_ROOT", tmp_path)
    _write_frame(tmp_path, "rq2c_undirected_view_edges.csv", result.undirected_edges_by_threshold[1])
    _write_frame(tmp_path, "reference_quotient_node_registry.csv", registry)
    (tmp_path / "rq2c_undirected_view_summary.json").write_text(
        json.dumps(result.sensitivity.loc[result.sensitivity["threshold"].eq(1)].iloc[0].to_dict()),
        encoding="utf-8",
    )
    assert pd.api.types.is_integer_dtype(
        pd.read_csv(tmp_path / "rq2c_undirected_view_edges.csv")["node_u"]
    )

    assert s2.assert_s2_threshold_one_matches_corrected_p0(result, tmp_path)["status"] == "PASS"

    changed = pd.read_csv(tmp_path / "rq2c_undirected_view_edges.csv")
    changed.loc[0, "weight"] = int(changed.loc[0, "weight"]) + 1
    _write_frame(tmp_path, "rq2c_undirected_view_edges.csv", changed)
    with pytest.raises(AssertionError):
        s2.assert_s2_threshold_one_matches_corrected_p0(result, tmp_path)

    changed = pd.read_csv(tmp_path / "rq2c_undirected_view_edges.csv")
    changed.loc[0, "directed_edge_count"] = int(changed.loc[0, "directed_edge_count"]) + 1
    _write_frame(tmp_path, "rq2c_undirected_view_edges.csv", changed)
    with pytest.raises(AssertionError):
        s2.assert_s2_threshold_one_matches_corrected_p0(result, tmp_path)

    _write_frame(tmp_path, "rq2c_undirected_view_edges.csv", result.undirected_edges_by_threshold[1].iloc[:-1])
    with pytest.raises(AssertionError):
        s2.assert_s2_threshold_one_matches_corrected_p0(result, tmp_path)


def _s3_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    edges = pd.DataFrame(
        [
            {"source_project_id": "2", "target_project_id": "10", "weight": 1},
            {"source_project_id": "10", "target_project_id": "2", "weight": 1},
            {"source_project_id": "10", "target_project_id": "100", "weight": 1},
            {"source_project_id": "100", "target_project_id": "10", "weight": 1},
        ]
    )
    registry = pd.DataFrame({"project_id": ["2", "10", "100"]})
    seeds = pd.DataFrame({"repo_id": ["2", "10"]})
    return edges, registry, seeds


def test_s3_positive_dynamic_parity_path_and_mutation_fail_closed(tmp_path, monkeypatch):
    edges, registry, seeds = _s3_inputs()
    result = s3.compute_s3_observation_sensitivity(
        edges,
        registry,
        seeds,
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    monkeypatch.setattr(s3, "CORRECTED_P0_ROOT", tmp_path)
    actual = result.view_results[s3.CANONICAL_SEED_CENTERED_OBSERVED]
    _write_frame(tmp_path, "reference_quotient_node_registry.csv", registry)
    _write_frame(tmp_path, "rq2c_undirected_view_edges.csv", actual.undirected_edges)
    _write_frame(tmp_path, "rq2c_undirected_view_lcc_edges.csv", actual.lcc_edges)
    _write_frame(tmp_path, "rq2c_algorithmic_communities.csv", actual.communities)
    (tmp_path / "rq2c_undirected_view_summary.json").write_text(
        json.dumps(dict(actual.network_summary)),
        encoding="utf-8",
    )
    assert pd.api.types.is_integer_dtype(
        pd.read_csv(tmp_path / "reference_quotient_node_registry.csv")["project_id"]
    )

    assert s3.assert_s3_canonical_view_matches_corrected_p0(result, tmp_path)["status"] == "PASS"

    changed = pd.read_csv(tmp_path / "rq2c_undirected_view_edges.csv")
    changed.loc[0, "weight"] = int(changed.loc[0, "weight"]) + 1
    _write_frame(tmp_path, "rq2c_undirected_view_edges.csv", changed)
    with pytest.raises(AssertionError):
        s3.assert_s3_canonical_view_matches_corrected_p0(result, tmp_path)


def _two_node_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(["a", "b"])
    graph.add_edge("a", "b", weight=1.0)
    return graph


def test_s4_positive_dynamic_parity_path_and_mutation_fail_closed(tmp_path, monkeypatch):
    graph = _two_node_graph()
    partition = {"a": 0, "b": 0}
    result = s4.compute_s4_community_stability(
        graph,
        partition,
        seeds=[s4.S4_CANONICAL_SEED],
        canonical_seed=s4.S4_CANONICAL_SEED,
    )
    authority = SimpleNamespace(
        lcc=graph,
        canonical_partition=partition,
        canonical_summary={
            "algorithmic_communities": int(result.runs.iloc[0]["community_count"]),
            "modularity": float(result.runs.iloc[0]["modularity"]),
        },
    )
    monkeypatch.setattr(s4, "CORRECTED_P0_ROOT", tmp_path)
    monkeypatch.setattr(s4, "load_corrected_p0_s45_authority", lambda: authority)

    assert s4.assert_s4_canonical_seed_matches_corrected_p0(result, tmp_path)["status"] == "PASS"

    authority.canonical_partition["b"] = 1
    with pytest.raises(s4.S4ContractError):
        s4.assert_s4_canonical_seed_matches_corrected_p0(result, tmp_path)


def test_s5_positive_dynamic_parity_path_and_mutation_fail_closed(tmp_path, monkeypatch):
    graph = _two_node_graph()
    scores = nx.betweenness_centrality(
        graph,
        k=len(graph),
        normalized=True,
        seed=s5.S5_CANONICAL_SEED,
        weight=None,
    )
    result = s5.compute_s5_brokerage_stability(
        graph,
        scores,
        k_values=[s5.S5_CANONICAL_K],
        seeds=[s5.S5_CANONICAL_SEED],
        top_ks=[1, 2],
        canonical_k=s5.S5_CANONICAL_K,
        canonical_seed=s5.S5_CANONICAL_SEED,
    )
    brokerage = pd.DataFrame(
        {
            "project_id": list(scores),
            "betweenness_brokerage": [float(scores[node]) for node in scores],
        }
    )
    authority = SimpleNamespace(lcc=graph, canonical_brokerage=brokerage)
    monkeypatch.setattr(s5, "CORRECTED_P0_ROOT", tmp_path)
    monkeypatch.setattr(s5, "load_corrected_p0_s45_authority", lambda: authority)

    assert s5.assert_s5_canonical_setting_matches_corrected_p0(result, tmp_path)["status"] == "PASS"

    authority.canonical_brokerage.loc[0, "betweenness_brokerage"] = 1.0
    with pytest.raises(s5.S5ContractError):
        s5.assert_s5_canonical_setting_matches_corrected_p0(result, tmp_path)
