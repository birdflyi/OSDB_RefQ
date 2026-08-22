from pathlib import Path

import networkx as nx
import pandas as pd

from script.ch5_reference_quotient.edge_table import edge_frame
from script.ch5_reference_quotient.network_views import directed_to_undirected_edges
from script.complex_network_analysis.build_network.build_Graph import DG2G, MDG2DG


REPO_ROOT = Path(__file__).parents[2]
CORRECTED_FLOW = (
    REPO_ROOT
    / "supplemental"
    / "reference_quotient_v1"
    / "v1_3_weight_multiplicity_contract_patch"
    / "outputs"
    / "S1_evidence_universe"
    / "evidence_universe_flow_corrected.csv"
)


def test_equality_is_local_to_refq_construction_not_generic_graph_conversion():
    refq = edge_frame({("a", "b"): 37}, analysis_seed_ids=[])
    assert refq.loc[0, "weight"] == refq.loc[0, "multiplicity"] == 37

    multi = nx.MultiDiGraph()
    multi.add_edge("a", "b", weight=1, multiplicity=37)
    directed = MDG2DG(multi, multiplicity=True)
    assert directed.edges["a", "b"]["weight"] == 1
    assert directed.edges["a", "b"]["multiplicity"] == 37

    undirected = DG2G(directed, multiplicity=True, double_self_loop=False)
    assert undirected.edges["a", "b"]["weight"] == 1
    assert undirected.edges["a", "b"]["multiplicity"] == 37


def test_undirected_weight_and_directed_edge_count_are_distinct():
    result = directed_to_undirected_edges(
        pd.DataFrame(
            [
                {"source": "a", "target": "b", "weight": 37},
                {"source": "b", "target": "a", "weight": 8},
            ]
        ),
        source_col="source",
        target_col="target",
        weight_col="weight",
    )

    row = result.iloc[0]
    assert row["weight"] == 45
    assert row["directed_edge_count"] == 2
    assert row["directed_edge_count"] != row["weight"]


def test_corrected_s1_flow_separates_record_weight_and_edge_count_units():
    flow = pd.read_csv(CORRECTED_FLOW)

    record_weight = flow[flow["stage"].isin(["self_loop_evidence_weight", "cross_project_evidence_weight"])]
    assert set(record_weight["count"]) == {1447073, 139044}
    assert set(record_weight["unit"]) == {"REFERENCE_RECORD"}
    assert set(record_weight["measure"]) == {"AGGREGATED_EDGE_WEIGHT"}

    edge_counts = flow[flow["unit"] == "EDGE_COUNT"]
    assert edge_counts.set_index("stage").loc["self_loop_edge_count", "count"] == 289
    assert edge_counts.set_index("stage").loc["cross_project_directed_edge_count", "count"] == 9605
