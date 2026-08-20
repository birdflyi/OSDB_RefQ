from __future__ import annotations

import hashlib
import json
import math
import os
import re
import sqlite3
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

import networkx as nx
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

PROJECT_MEMBERSHIP = re.compile(r"R_(\d+)")
PLACEHOLDER_IDENTITY = re.compile(r"(?:^|_)None(?:#|$)", re.IGNORECASE)
RAW_USECOLS = [
    "src_entity_id", "src_entity_type", "tar_entity_id", "tar_entity_type",
    "relation_type", "event_type", "src_entity_id_agg", "src_entity_type_agg",
    "tar_entity_id_agg", "tar_entity_type_agg", "tar_entity_type_fine_grained",
]


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def json_dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def project_memberships(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    return tuple(dict.fromkeys(PROJECT_MEMBERSHIP.findall(str(value))))


def unique_project_membership(value: object) -> str | None:
    memberships = project_memberships(value)
    return memberships[0] if len(memberships) == 1 else None


def normalized_identity(value: object) -> str | None:
    if value is None:
        return None
    identity = str(value).strip()
    if not identity or identity.lower() == "nan" or PLACEHOLDER_IDENTITY.search(identity):
        return None
    return identity


def canonical_identity(entity: object, aggregate: object) -> str | None:
    identity = normalized_identity(entity)
    if identity is not None:
        return identity
    project = unique_project_membership(aggregate)
    return f"R_{project}" if project is not None else None


def membership_status(aggregate: object, aggregate_type: object) -> str:
    memberships = project_memberships(aggregate)
    if len(memberships) == 1:
        return "PROJECT_MAPPABLE"
    if len(memberships) > 1:
        return "AMBIGUOUS_IF_ANY"
    if str(aggregate_type) == "Object":
        return "NON_PROJECT"
    return "UNRESOLVED"


def write_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def file_record(path: Path, root: Path | None = None) -> dict[str, Any]:
    stat = path.stat()
    name = str(path.relative_to(root)).replace(os.sep, "/") if root else str(path)
    return {"path": name, "bytes": stat.st_size, "sha256": sha256_file(path)}


def runtime_versions() -> dict[str, str]:
    versions: dict[str, str] = {"python": sys.version.split()[0]}
    for module in ("numpy", "pandas", "scipy", "networkx"):
        loaded = __import__(module)
        versions[module] = str(loaded.__version__)
    try:
        from importlib.metadata import version
        versions["GH_CoRE"] = version("gh-core")
    except Exception:
        versions["GH_CoRE"] = "unavailable"
    return versions


def git_value(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def graph_from_edges(edges: pd.DataFrame, nodes: Iterable[object]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(str(node) for node in nodes)
    for row in edges.itertuples(index=False):
        graph.add_edge(str(row.node_u), str(row.node_v), weight=float(row.weight))
    return graph


def undirected_edges_from_directed(edges: pd.DataFrame) -> pd.DataFrame:
    work = edges.loc[edges["source_project_id"] != edges["target_project_id"], [
        "source_project_id", "target_project_id", "weight"
    ]].copy()
    if work.empty:
        return pd.DataFrame(columns=["node_u", "node_v", "weight", "directed_edge_count"])
    pairs = [(min(str(source), str(target)), max(str(source), str(target))) for source, target in work[["source_project_id", "target_project_id"]].itertuples(index=False, name=None)]
    work["node_u"] = [pair[0] for pair in pairs]
    work["node_v"] = [pair[1] for pair in pairs]
    return (
        work.groupby(["node_u", "node_v"], as_index=False)
        .agg(weight=("weight", "sum"), directed_edge_count=("weight", "size"))
        .sort_values(["node_u", "node_v"])
        .reset_index(drop=True)
    )


def structural_summary(edges: pd.DataFrame, node_ids: Iterable[object], seed: int, brokerage_k: int | None = None) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame]:
    graph = graph_from_edges(edges, node_ids)
    components = sorted(nx.connected_components(graph), key=len, reverse=True)
    lcc_nodes = components[0] if components else set()
    lcc = graph.subgraph(lcc_nodes).copy()
    lcc_edges = edges[edges["node_u"].isin(lcc_nodes) & edges["node_v"].isin(lcc_nodes)].copy()
    communities = list(nx.community.louvain_communities(lcc, weight="weight", seed=seed)) if lcc else []
    modularity = nx.community.modularity(lcc, communities, weight="weight") if communities else 0.0
    summary = {
        "nodes": graph.number_of_nodes(),
        "edge_observed_nodes": sum(1 for node in graph if graph.degree(node) > 0),
        "undirected_edges": graph.number_of_edges(),
        "components": len(components),
        "isolates": nx.number_of_isolates(graph),
        "lcc_nodes": lcc.number_of_nodes(),
        "lcc_edges": lcc.number_of_edges(),
        "lcc_coverage": lcc.number_of_nodes() / graph.number_of_nodes() if graph else 0.0,
        "average_clustering_lcc": nx.average_clustering(lcc) if lcc else 0.0,
        "transitivity_lcc": nx.transitivity(lcc) if lcc else 0.0,
        "algorithmic_communities": len(communities),
        "modularity": float(modularity),
        "random_seed": seed,
    }
    community_sizes = pd.DataFrame(
        [{"community_id": index, "community_size": len(nodes)} for index, nodes in enumerate(sorted(communities, key=lambda x: (-len(x), min(x))))]
    )
    if brokerage_k is not None and len(lcc) > 1:
        values = nx.betweenness_centrality(lcc, k=min(brokerage_k, len(lcc)), normalized=True, seed=seed, weight=None)
        brokerage = pd.DataFrame([{"project_id": node, "betweenness_brokerage": value} for node, value in values.items()])
    else:
        brokerage = pd.DataFrame(columns=["project_id", "betweenness_brokerage"])
    return summary, lcc_edges, community_sizes, brokerage


def quantiles(values: pd.Series, metric: str) -> pd.DataFrame:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return pd.DataFrame(columns=["metric", "quantile", "value"])
    points = [("min", 0.0), ("q25", 0.25), ("median", 0.5), ("q75", 0.75), ("max", 1.0)]
    return pd.DataFrame([{"metric": metric, "quantile": name, "value": float(numeric.quantile(q))} for name, q in points])


def ecdf(values: pd.Series, metric: str) -> pd.DataFrame:
    numeric = pd.to_numeric(values, errors="coerce").dropna().sort_values().reset_index(drop=True)
    if numeric.empty:
        return pd.DataFrame(columns=["metric", "rank", "value", "cdf", "ccdf"])
    n = len(numeric)
    return pd.DataFrame({"metric": metric, "rank": range(1, n + 1), "value": numeric, "cdf": np.arange(1, n + 1) / n, "ccdf": (n - np.arange(n)) / n})


def adjusted_rand_index(left: dict[str, int], right: dict[str, int]) -> float:
    labels = sorted(set(left) & set(right))
    if len(labels) < 2:
        return 1.0
    table: dict[tuple[int, int], int] = Counter((left[node], right[node]) for node in labels)
    a = Counter(left[node] for node in labels)
    b = Counter(right[node] for node in labels)
    comb = lambda n: n * (n - 1) / 2
    total = comb(len(labels))
    index = sum(comb(value) for value in table.values())
    expected = sum(comb(value) for value in a.values()) * sum(comb(value) for value in b.values()) / total if total else 0.0
    maximum = (sum(comb(value) for value in a.values()) + sum(comb(value) for value in b.values())) / 2
    return float((index - expected) / (maximum - expected)) if maximum != expected else 1.0


def rank_frame(project_ids: Iterable[object], scores: dict[str, float], degree: dict[str, int] | None = None) -> pd.DataFrame:
    degree = degree or {}
    rows = [{"project_id": str(node), "score": float(score)} for node, score in scores.items()]
    frame = pd.DataFrame(rows)
    if frame.empty:
        return frame.assign(rank=pd.Series(dtype="int64"))
    frame["degree"] = frame["project_id"].map(degree).fillna(0).astype(int)
    frame = frame.sort_values(["score", "degree", "project_id"], ascending=[False, False, True]).reset_index(drop=True)
    frame["rank"] = frame.index + 1
    return frame[["project_id", "score", "rank"]]


def rank_correlation(left: pd.DataFrame, right: pd.DataFrame) -> float:
    joined = left[["project_id", "rank"]].merge(right[["project_id", "rank"]], on="project_id", suffixes=("_left", "_right"))
    return float(spearmanr(joined["rank_left"], joined["rank_right"]).statistic) if len(joined) > 1 else 1.0
