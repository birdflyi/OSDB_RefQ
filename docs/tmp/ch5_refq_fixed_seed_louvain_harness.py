"""Fresh-process fixed-seed Louvain reproducibility audit harness.

This tool reads frozen S2 threshold graphs and the official P0-v3 node
registry. It never writes scientific stage outputs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable, Sequence

import networkx as nx
import pandas as pd


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
S2_ROOT = REPOSITORY_ROOT / "supplemental" / "reference_quotient_v2" / "outputs_p0v3" / "S2_weight_sensitivity"
P0_ROOT = REPOSITORY_ROOT / "outputs" / "reference_quotient_p0_corrected_v3"
THRESHOLDS = (1, 2, 5, 10)
RANDOM_SEED = 20260731
HASHSEED_RUNS = {0: 20, 1: 5, 2: 5, 42: 5, 20260731: 5}


def _digest_records(records: Iterable[Sequence[object]]) -> str:
    digest = hashlib.sha256()
    for record in records:
        payload = json.dumps(list(record), ensure_ascii=True, separators=(",", ":"))
        digest.update(payload.encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def _weight(value: object) -> str:
    return format(float(value), ".17g")


def _node_digest(graph: nx.Graph) -> str:
    return _digest_records((str(node),) for node in graph.nodes)


def _edge_digest(graph: nx.Graph) -> str:
    return _digest_records(
        (str(node_u), str(node_v), _weight(data.get("weight", 1.0)))
        for node_u, node_v, data in graph.edges(data=True)
    )


def _adjacency_digest(graph: nx.Graph) -> str:
    return _digest_records(
        (str(node), str(neighbor), _weight(data.get("weight", 1.0)))
        for node in graph
        for neighbor, data in graph[node].items()
    )


def _canonical_communities(communities: Iterable[Iterable[object]]) -> list[list[str]]:
    normalized = [sorted(str(node) for node in community) for community in communities]
    return sorted(normalized, key=lambda values: (-len(values), values[0]))


def _partition_digest(communities: Iterable[Iterable[object]]) -> str:
    return _digest_records(tuple(values) for values in _canonical_communities(communities))


def _load_inputs(threshold: int) -> tuple[pd.DataFrame, tuple[str, ...]]:
    edge_path = S2_ROOT / ("threshold_%s_undirected_edges.csv" % threshold)
    edges = pd.read_csv(edge_path, dtype={"node_u": "string", "node_v": "string"})
    registry = pd.read_csv(P0_ROOT / "reference_quotient_node_registry.csv", dtype={"project_id": "string"})
    return edges, tuple(registry["project_id"].astype(str))


def _production_graph(edges: pd.DataFrame, node_ids: Sequence[str]) -> tuple[nx.Graph, nx.Graph]:
    graph = nx.Graph()
    graph.add_nodes_from(str(node) for node in node_ids)
    for row in edges.itertuples(index=False):
        graph.add_edge(str(row.node_u), str(row.node_v), weight=float(row.weight))
    components = sorted(nx.connected_components(graph), key=len, reverse=True)
    lcc_nodes = components[0] if components else set()
    return graph, graph.subgraph(lcc_nodes).copy()


def _canonical_graph(lcc: nx.Graph) -> nx.Graph:
    nodes = sorted(str(node) for node in lcc.nodes)
    edges = sorted(
        (
            min(str(node_u), str(node_v)),
            max(str(node_u), str(node_v)),
            float(data.get("weight", 1.0)),
        )
        for node_u, node_v, data in lcc.edges(data=True)
    )
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    for node_u, node_v, weight in edges:
        graph.add_edge(node_u, node_v, weight=weight)
    return graph


def analyze_one(threshold: int, graph_mode: str, process_index: int) -> dict[str, object]:
    edges, node_ids = _load_inputs(threshold)
    full_graph, raw_lcc = _production_graph(edges, node_ids)
    analysis_graph = raw_lcc if graph_mode == "raw" else _canonical_graph(raw_lcc)
    communities = list(
        nx.community.louvain_communities(
            analysis_graph,
            weight="weight",
            seed=RANDOM_SEED,
        )
    )
    modularity = nx.community.modularity(analysis_graph, communities, weight="weight")
    return {
        "graph_mode": graph_mode,
        "threshold": threshold,
        "process_index": process_index,
        "pythonhashseed": os.environ.get("PYTHONHASHSEED", ""),
        "random_seed": RANDOM_SEED,
        "python_version": sys.version.split()[0],
        "networkx_version": nx.__version__,
        "node_count": analysis_graph.number_of_nodes(),
        "edge_count": analysis_graph.number_of_edges(),
        "community_count": len(communities),
        "modularity": float(modularity),
        "partition_digest": _partition_digest(communities),
        "input_node_registry_order_digest": _digest_records((node,) for node in node_ids),
        "input_threshold_edge_order_digest": _digest_records(
            (str(row.node_u), str(row.node_v), _weight(row.weight), int(row.directed_edge_count))
            for row in edges.itertuples(index=False)
        ),
        "full_graph_node_order_digest": _node_digest(full_graph),
        "full_graph_edge_order_digest": _edge_digest(full_graph),
        "raw_lcc_node_order_digest": _node_digest(raw_lcc),
        "raw_lcc_edge_order_digest": _edge_digest(raw_lcc),
        "raw_lcc_adjacency_order_digest": _adjacency_digest(raw_lcc),
        "analysis_graph_node_order_digest": _node_digest(analysis_graph),
        "analysis_graph_edge_order_digest": _edge_digest(analysis_graph),
        "analysis_graph_adjacency_order_digest": _adjacency_digest(analysis_graph),
    }


def _child_command(threshold: int, graph_mode: str, process_index: int) -> list[str]:
    return [
        sys.executable,
        str(Path(__file__).resolve()),
        "--child",
        "--threshold",
        str(threshold),
        "--graph-mode",
        graph_mode,
        "--process-index",
        str(process_index),
    ]


def _run_child(job: tuple[int, int, str, int]) -> dict[str, object]:
    hashseed, threshold, graph_mode, process_index = job
    environment = os.environ.copy()
    environment["PYTHONHASHSEED"] = str(hashseed)
    result = subprocess.run(
        _child_command(threshold, graph_mode, process_index),
        cwd=str(REPOSITORY_ROOT),
        env=environment,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    lines = [line for line in result.stdout.splitlines() if line.lstrip().startswith("{")]
    if not lines:
        raise RuntimeError("child process did not emit a JSON record: %s" % result.stderr)
    return json.loads(lines[-1])


def run_matrix(graph_modes: Sequence[str], max_workers: int) -> list[dict[str, object]]:
    jobs = [
        (hashseed, threshold, graph_mode, process_index)
        for graph_mode in graph_modes
        for threshold in THRESHOLDS
        for hashseed, run_count in HASHSEED_RUNS.items()
        for process_index in range(1, run_count + 1)
    ]
    rows: list[dict[str, object]] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_run_child, job): job for job in jobs}
        for future in as_completed(futures):
            rows.append(future.result())
    return sorted(
        rows,
        key=lambda row: (
            str(row["graph_mode"]),
            int(row["threshold"]),
            int(str(row["pythonhashseed"])),
            int(row["process_index"]),
        ),
    )


def write_matrix(path: Path, rows: Sequence[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def matrix_summary(rows: Sequence[dict[str, object]]) -> dict[str, object]:
    summary: dict[str, object] = {"run_count": len(rows), "profiles": []}
    profiles = summary["profiles"]
    assert isinstance(profiles, list)
    for graph_mode in sorted({str(row["graph_mode"]) for row in rows}):
        for threshold in THRESHOLDS:
            selected = [
                row
                for row in rows
                if row["graph_mode"] == graph_mode and int(row["threshold"]) == threshold
            ]
            profiles.append(
                {
                    "graph_mode": graph_mode,
                    "threshold": threshold,
                    "runs": len(selected),
                    "partition_digests": len({str(row["partition_digest"]) for row in selected}),
                    "community_counts": sorted({int(row["community_count"]) for row in selected}),
                    "modularity_values": sorted({float(row["modularity"]) for row in selected}),
                    "full_graph_node_orders": len({str(row["full_graph_node_order_digest"]) for row in selected}),
                    "full_graph_edge_orders": len({str(row["full_graph_edge_order_digest"]) for row in selected}),
                    "raw_lcc_node_orders": len({str(row["raw_lcc_node_order_digest"]) for row in selected}),
                    "raw_lcc_edge_orders": len({str(row["raw_lcc_edge_order_digest"]) for row in selected}),
                    "raw_lcc_adjacency_orders": len({str(row["raw_lcc_adjacency_order_digest"]) for row in selected}),
                    "analysis_graph_node_orders": len({str(row["analysis_graph_node_order_digest"]) for row in selected}),
                    "analysis_graph_edge_orders": len({str(row["analysis_graph_edge_order_digest"]) for row in selected}),
                    "analysis_graph_adjacency_orders": len({str(row["analysis_graph_adjacency_order_digest"]) for row in selected}),
                }
            )
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--child", action="store_true")
    parser.add_argument("--threshold", type=int, choices=THRESHOLDS)
    parser.add_argument("--graph-mode", choices=("raw", "canonical"))
    parser.add_argument("--process-index", type=int, default=1)
    parser.add_argument("--matrix-output", type=Path)
    parser.add_argument("--matrix-modes", choices=("raw", "canonical", "both"), default="both")
    parser.add_argument("--max-workers", type=int, default=8)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.child:
        if args.threshold is None or args.graph_mode is None:
            raise SystemExit("--child requires --threshold and --graph-mode")
        print(json.dumps(analyze_one(args.threshold, args.graph_mode, args.process_index), sort_keys=True))
        return 0
    if args.matrix_output is None:
        raise SystemExit("matrix mode requires --matrix-output")
    graph_modes = ("raw", "canonical") if args.matrix_modes == "both" else (args.matrix_modes,)
    rows = run_matrix(graph_modes, args.max_workers)
    write_matrix(args.matrix_output, rows)
    print(json.dumps(matrix_summary(rows), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
