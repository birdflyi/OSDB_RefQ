"""C3.7-D synthetic S4 tests; no corrected-data network execution."""

from __future__ import annotations

import inspect

import networkx as nx
import pandas as pd
import pandas.testing as pdt

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.s4_community_stability import (
    S4_OUTPUT_CONTRACT,
    adjusted_rand_index,
    build_future_s4_output_tables,
    canonical_partition_labels,
    compute_s4_community_stability,
    s4_production_seeds,
)
from supplemental.reference_quotient_v2.scripts.s45_canonical_graph import canonical_lcc_from_edges


def _graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(["z", "a", "b", "c", "d", "e"])
    graph.add_edge("z", "a", weight=5)
    graph.add_edge("a", "b", weight=5)
    graph.add_edge("b", "z", weight=5)
    graph.add_edge("c", "d", weight=4)
    graph.add_edge("d", "e", weight=4)
    graph.add_edge("e", "c", weight=4)
    graph.add_edge("b", "c", weight=0.2)
    return graph


def _partition() -> dict[str, int]:
    return {"z": 0, "a": 0, "b": 0, "c": 1, "d": 1, "e": 1}


def _production_stage_snapshot(stage: str) -> dict[str, bytes]:
    root = paths.CORRECTED_OUTPUTS_ROOT / stage
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def test_s4_production_seed_contract_is_exact():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    seeds = s4_production_seeds(config)
    assert len(seeds) == 50
    assert seeds == tuple(range(20260731, 20260781))
    assert seeds.count(20260731) == 1


def test_ari_is_identical_and_label_permutation_invariant():
    left = {"a": 0, "b": 0, "c": 1, "d": 1}
    permuted = {"a": 9, "b": 9, "c": 4, "d": 4}
    different = {"a": 0, "b": 1, "c": 0, "d": 1}
    assert adjusted_rand_index(left, left) == 1.0
    assert adjusted_rand_index(left, permuted) == 1.0
    assert adjusted_rand_index(left, different) < 1.0


def test_s4_uses_weighted_louvain_and_builds_deterministic_tables(monkeypatch):
    before = _production_stage_snapshot("S4_community_stability")
    calls = []
    original = nx.community.louvain_communities

    def wrapped(graph, **kwargs):
        calls.append(kwargs)
        return original(graph, **kwargs)

    monkeypatch.setattr(nx.community, "louvain_communities", wrapped)
    result = compute_s4_community_stability(
        _graph(), _partition(), seeds=[11, 12, 13, 14], canonical_seed=11
    )
    repeat = compute_s4_community_stability(
        _graph(), _partition(), seeds=[11, 12, 13, 14], canonical_seed=11
    )
    assert len(calls) == 8
    assert all(call["weight"] == "weight" for call in calls)
    assert len(result.runs) == 4
    assert len(result.pairwise) == 4 * 3 // 2
    assert result.pairwise[["seed_left", "seed_right"]].values.tolist() == [
        [11, 12], [11, 13], [11, 14], [12, 13], [12, 14], [13, 14]
    ]
    assert result.runs.loc[result.runs["seed"] == 11, "is_canonical_seed"].tolist() == [True]
    pdt.assert_frame_equal(result.runs, repeat.runs, check_exact=True)
    pdt.assert_frame_equal(result.pairwise, repeat.pairwise, check_exact=True)

    tables = build_future_s4_output_tables(result)
    assert set(tables) == set(S4_OUTPUT_CONTRACT)
    assert tuple(tables["louvain_stability_runs.csv"].columns) == S4_OUTPUT_CONTRACT["louvain_stability_runs.csv"]
    assert tuple(tables["louvain_stability_pairwise.csv"].columns) == S4_OUTPUT_CONTRACT["louvain_stability_pairwise.csv"]
    assert _production_stage_snapshot("S4_community_stability") == before


def test_s4_same_seed_is_independent_of_input_graph_order_and_other_seeds_remain_supported():
    left = _graph()
    right = nx.Graph()
    right.add_nodes_from(reversed(tuple(left.nodes)))
    right.add_edges_from(reversed(tuple((u, v, dict(data)) for u, v, data in left.edges(data=True))))

    left_result = compute_s4_community_stability(
        left, _partition(), seeds=[11, 12], canonical_seed=11
    )
    right_result = compute_s4_community_stability(
        right, _partition(), seeds=[11, 12], canonical_seed=11
    )

    pdt.assert_frame_equal(left_result.runs, right_result.runs, check_exact=True)
    assert left_result.partitions_by_seed[11] == right_result.partitions_by_seed[11]
    assert set(left_result.partitions_by_seed) == {11, 12}


def test_s4_canonical_lcc_preserves_registry_order_and_is_shared_definition():
    edges = pd.DataFrame(
        [
            {"node_u": "a", "node_v": "b", "weight": 2, "directed_edge_count": 1},
            {"node_u": "b", "node_v": "c", "weight": 1, "directed_edge_count": 1},
            {"node_u": "x", "node_v": "y", "weight": 1, "directed_edge_count": 1},
        ]
    )
    registry = pd.DataFrame({"project_id": ["x", "a", "b", "c", "y", "z"]})
    graph = canonical_lcc_from_edges(edges, registry)
    assert tuple(graph.nodes) == ("a", "b", "c")
    assert {(u, v) for u, v in graph.edges} == {("a", "b"), ("b", "c")}
    assert tuple(canonical_partition_labels([{"a", "b"}, {"c"}], graph.nodes)) == tuple(graph.nodes)


def test_s4_source_has_no_historical_executable_authority():
    import supplemental.reference_quotient_v2.scripts.s4_community_stability as s4

    source = inspect.getsource(s4)
    assert "reference_quotient_v1" not in source
    assert "outputs/reference_quotient_p0_frozen" not in source
    assert "0.797309595" not in source
