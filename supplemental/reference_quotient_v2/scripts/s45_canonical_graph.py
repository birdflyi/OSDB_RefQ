"""Corrected-P0 canonical graph authority shared by S4 and S5.

The preflight in this module reads only metadata and CSV headers.  The full
loader is a future execution boundary and is deliberately separate from that
preflight.  No function in this module writes a scientific output.
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

import networkx as nx
import pandas as pd

from .manifest import validate_scaffold_provenance
from .paths import (
    CORRECTED_P0_ROOT,
    DEFAULT_CONFIG_PATH,
    PathGuardError,
    canonical_path,
    load_config,
)


class S45ContractError(ValueError):
    """Raised when a prospective S4/S5 authority violates its contract."""


CANONICAL_EDGE_COLUMNS: tuple[str, ...] = (
    "node_u",
    "node_v",
    "weight",
    "directed_edge_count",
)
NODE_REGISTRY_COLUMNS: tuple[str, ...] = ("project_id",)
COMMUNITY_COLUMNS: tuple[str, ...] = (
    "project_id",
    "community_id",
    "community_size",
)
BROKERAGE_COLUMNS: tuple[str, ...] = (
    "project_id",
    "undirected_degree",
    "undirected_strength",
    "local_clustering",
    "betweenness_brokerage",
    "community_id",
)

CANONICAL_AUTHORITY_FILES: Mapping[str, str] = {
    "canonical_edges": "rq2c_undirected_view_edges.csv",
    "canonical_lcc_edges": "rq2c_undirected_view_lcc_edges.csv",
    "node_registry": "reference_quotient_node_registry.csv",
    "canonical_communities": "rq2c_algorithmic_communities.csv",
    "canonical_summary": "rq2c_undirected_view_summary.json",
    "canonical_brokerage": "rq2c_structural_brokerage_candidates.csv",
}


def _require_corrected_root(value: str | Path) -> Path:
    root = canonical_path(value)
    if os.path.normcase(os.fspath(root)) != os.path.normcase(os.fspath(CORRECTED_P0_ROOT)):
        raise S45ContractError("S4/S5 authority must be the corrected P0 root")
    return root


def corrected_p0_s45_authority_paths(root: str | Path = CORRECTED_P0_ROOT) -> dict[str, Path]:
    """Return the approved authority paths, all under corrected P0."""

    root_path = _require_corrected_root(root)
    result = {name: root_path / filename for name, filename in CANONICAL_AUTHORITY_FILES.items()}
    for name, path in result.items():
        if not path.is_relative_to(root_path):
            raise S45ContractError("authority path escaped corrected P0 root: %s" % name)
    return result


def _header(path: Path) -> tuple[str, ...]:
    try:
        return tuple(pd.read_csv(path, nrows=0).columns)
    except Exception as exc:  # pragma: no cover - error text is the contract
        raise S45ContractError("unable to read authority header: %s" % path) from exc


def preflight_corrected_p0_s45_inputs(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> dict[str, Any]:
    """Validate corrected-P0 metadata and headers without loading rows.

    This function is the C3.7-D input preflight.  It intentionally does not
    construct a graph, invoke Louvain or invoke betweenness.
    """

    config = load_config(config_path)
    try:
        provenance = validate_scaffold_provenance(config)
    except PathGuardError as exc:
        raise S45ContractError(str(exc)) from exc
    root = _require_corrected_root(provenance["corrected_p0_root"])
    paths = corrected_p0_s45_authority_paths(root)
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        raise S45ContractError("corrected P0 S4/S5 authority is incomplete: %s" % ", ".join(missing))

    required_headers = {
        "canonical_edges": CANONICAL_EDGE_COLUMNS,
        "canonical_lcc_edges": CANONICAL_EDGE_COLUMNS,
        "node_registry": NODE_REGISTRY_COLUMNS,
        "canonical_communities": COMMUNITY_COLUMNS,
        "canonical_brokerage": BROKERAGE_COLUMNS,
    }
    observed_headers: dict[str, list[str]] = {}
    for name, required in required_headers.items():
        observed = _header(paths[name])
        observed_headers[name] = list(observed)
        missing_columns = [column for column in required if column not in observed]
        if missing_columns:
            raise S45ContractError(
                "%s authority header is incomplete: %s" % (name, ", ".join(missing_columns))
            )

    try:
        summary = json.loads(paths["canonical_summary"].read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - malformed external file
        raise S45ContractError("canonical summary is not valid JSON") from exc
    if not isinstance(summary, dict):
        raise S45ContractError("canonical summary must be a JSON object")
    for key in ("algorithmic_communities", "modularity", "random_seed", "brokerage_sample_size"):
        if key not in summary:
            raise S45ContractError("canonical summary is missing %s" % key)
    if summary["random_seed"] != config["random_seed"]:
        raise S45ContractError("canonical summary random_seed does not match configured seed")
    if summary["brokerage_sample_size"] != config["brokerage_sample_size"]:
        raise S45ContractError("canonical summary brokerage_sample_size does not match configuration")

    return {
        "C3_7D_INPUT_PREFLIGHT": "PASS",
        "corrected_p0_manifest_status": provenance["corrected_p0_manifest_status"],
        "corrected_p0_manifest_sha256": _sha256(provenance["corrected_p0_manifest"]),
        "corrected_p0_config_sha256": provenance["corrected_p0_config_sha256"],
        "corrected_p0_root": str(root),
        "required_files": {name: str(path) for name, path in paths.items()},
        "required_headers": observed_headers,
        "canonical_summary_metadata": {
            key: summary[key]
            for key in ("algorithmic_communities", "modularity", "random_seed", "brokerage_sample_size")
        },
        "random_seed": config["random_seed"],
        "brokerage_sample_size": config["brokerage_sample_size"],
        "s4_louvain_seed_start": config["s4_louvain_seed_start"],
        "s4_louvain_run_count": config["s4_louvain_run_count"],
        "s4_louvain_seed_end": config["s4_louvain_seed_start"] + config["s4_louvain_run_count"] - 1,
        "s5_brokerage_k": list(config["s5_brokerage_k"]),
        "s5_seed_start": config["s5_seed_start"],
        "s5_run_count": config["s5_run_count"],
        "s5_seed_end": config["s5_seed_start"] + config["s5_run_count"] - 1,
        "s5_top_k": list(config["s5_top_k"]),
        "headers_only": True,
        "corrected_data_s4_run": False,
        "corrected_data_s5_run": False,
        "network_corrected_data_run": 0,
        "parity_gates_invoked": False,
        "supplemental_v2_outputs_root_created": False,
    }


def _sha256(path: str | Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_canonical_edges(edges: pd.DataFrame) -> pd.DataFrame:
    missing = [column for column in CANONICAL_EDGE_COLUMNS if column not in edges]
    if missing:
        raise S45ContractError("canonical edge table is missing: %s" % ", ".join(missing))
    work = edges.loc[:, CANONICAL_EDGE_COLUMNS].copy()
    for column in ("node_u", "node_v"):
        if work[column].isna().any() or work[column].astype(str).str.strip().eq("").any():
            raise S45ContractError("canonical edge table has an empty %s" % column)
        work[column] = work[column].astype(str)
    if (work["node_u"] == work["node_v"]).any():
        raise S45ContractError("canonical edge table contains a self-loop")
    if (work["node_u"] > work["node_v"]).any():
        raise S45ContractError("canonical edge endpoints must be ordered")
    for column in CANONICAL_EDGE_COLUMNS[2:]:
        numeric = pd.to_numeric(work[column], errors="coerce")
        if numeric.isna().any() or (~numeric.map(math.isfinite)).any():
            raise S45ContractError("canonical edge %s must be finite" % column)
        if (numeric <= 0).any() or (~numeric.eq(numeric.round())).any():
            raise S45ContractError("canonical edge %s must be positive integral" % column)
        work[column] = numeric.astype("int64")
    if work.duplicated(["node_u", "node_v"]).any():
        raise S45ContractError("canonical edge endpoints must be unique")
    return work.sort_values(["node_u", "node_v"], kind="stable").reset_index(drop=True)


def validate_node_registry(node_registry: pd.DataFrame) -> tuple[str, ...]:
    missing = [column for column in NODE_REGISTRY_COLUMNS if column not in node_registry]
    if missing:
        raise S45ContractError("node registry is missing: %s" % ", ".join(missing))
    values = node_registry["project_id"]
    if values.isna().any() or values.astype(str).str.strip().eq("").any():
        raise S45ContractError("node registry contains an empty project_id")
    node_ids = tuple(values.astype(str))
    if len(node_ids) != len(set(node_ids)):
        raise S45ContractError("node registry project_id values must be unique")
    return node_ids


def canonical_lcc_from_edges(
    edges: pd.DataFrame,
    node_registry: pd.DataFrame | Iterable[object],
) -> nx.Graph:
    """Construct the deterministic corrected canonical LCC graph."""

    canonical_edges = validate_canonical_edges(edges)
    if isinstance(node_registry, pd.DataFrame):
        node_ids = validate_node_registry(node_registry)
    else:
        node_ids = tuple(str(node) for node in node_registry)
        if len(node_ids) != len(set(node_ids)):
            raise S45ContractError("canonical node IDs must be unique")
    node_position = {node: index for index, node in enumerate(node_ids)}
    graph = nx.Graph()
    graph.add_nodes_from(node_ids)
    for row in canonical_edges.itertuples(index=False):
        if row.node_u not in node_position or row.node_v not in node_position:
            raise S45ContractError("canonical edge references a node outside the registry")
        graph.add_edge(row.node_u, row.node_v, weight=float(row.weight))

    components = list(nx.connected_components(graph))
    if not components:
        return nx.Graph()
    lcc_nodes = max(
        components,
        key=lambda component: (len(component), -min(node_position[node] for node in component)),
    )
    lcc = nx.Graph()
    lcc.add_nodes_from(node for node in node_ids if node in lcc_nodes)
    for row in canonical_edges.itertuples(index=False):
        if row.node_u in lcc_nodes and row.node_v in lcc_nodes:
            lcc.add_edge(row.node_u, row.node_v, weight=float(row.weight))
    return lcc


def canonical_lcc_edges(edges: pd.DataFrame, lcc: nx.Graph) -> pd.DataFrame:
    work = validate_canonical_edges(edges)
    nodes = set(lcc.nodes)
    return work.loc[work["node_u"].isin(nodes) & work["node_v"].isin(nodes)].reset_index(drop=True)


def canonical_partition_from_frame(frame: pd.DataFrame) -> dict[str, int]:
    missing = [column for column in COMMUNITY_COLUMNS if column not in frame]
    if missing:
        raise S45ContractError("canonical community table is missing: %s" % ", ".join(missing))
    work = frame.loc[:, COMMUNITY_COLUMNS].copy()
    if work["project_id"].isna().any() or work["project_id"].astype(str).str.strip().eq("").any():
        raise S45ContractError("canonical communities contain an empty project_id")
    if work["project_id"].astype(str).duplicated().any():
        raise S45ContractError("canonical communities contain duplicate project_id")
    labels = pd.to_numeric(work["community_id"], errors="coerce")
    sizes = pd.to_numeric(work["community_size"], errors="coerce")
    if labels.isna().any() or (~labels.eq(labels.round())).any() or sizes.isna().any():
        raise S45ContractError("canonical communities have invalid labels or sizes")
    result = {
        str(project_id): int(label)
        for project_id, label in zip(work["project_id"], labels)
    }
    observed_sizes = work.assign(_label=labels.astype(int)).groupby("_label").size()
    recorded_sizes = work.assign(_label=labels.astype(int)).groupby("_label")["community_size"].first()
    if any(int(observed_sizes[label]) != int(recorded_sizes[label]) for label in observed_sizes.index):
        raise S45ContractError("canonical community_size does not close")
    return result


@dataclass(frozen=True)
class CorrectedP0S45Authority:
    """Full corrected authority loaded only by a future scientific stage."""

    root: Path
    edges: pd.DataFrame
    node_registry: pd.DataFrame
    canonical_communities: pd.DataFrame
    canonical_summary: Mapping[str, Any]
    canonical_brokerage: pd.DataFrame
    lcc: nx.Graph
    lcc_edges: pd.DataFrame
    canonical_partition: Mapping[str, int]


def load_corrected_p0_s45_authority(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> CorrectedP0S45Authority:
    """Load complete corrected-P0 S4/S5 authority for a future run."""

    preflight = preflight_corrected_p0_s45_inputs(config_path)
    paths = corrected_p0_s45_authority_paths(preflight["corrected_p0_root"])
    edges = pd.read_csv(paths["canonical_edges"], dtype={"node_u": "string", "node_v": "string"})
    registry = pd.read_csv(paths["node_registry"], dtype={"project_id": "string"})
    communities = pd.read_csv(paths["canonical_communities"], dtype={"project_id": "string"})
    brokerage = pd.read_csv(paths["canonical_brokerage"], dtype={"project_id": "string"})
    summary = json.loads(paths["canonical_summary"].read_text(encoding="utf-8"))
    normalized_edges = validate_canonical_edges(edges)
    recorded_lcc_edges = validate_canonical_edges(
        pd.read_csv(paths["canonical_lcc_edges"], dtype={"node_u": "string", "node_v": "string"})
    )
    node_ids = validate_node_registry(registry)
    lcc = canonical_lcc_from_edges(normalized_edges, node_ids)
    partition = canonical_partition_from_frame(communities)
    if set(partition) != set(lcc.nodes):
        raise S45ContractError("canonical community project IDs do not equal graph-derived LCC IDs")
    if tuple(node for node in node_ids if node in partition) != tuple(lcc.nodes):
        raise S45ContractError("canonical LCC node order is not registry-deterministic")
    derived_lcc_edges = canonical_lcc_edges(normalized_edges, lcc)
    if not recorded_lcc_edges.equals(derived_lcc_edges):
        raise S45ContractError("recorded canonical LCC edges do not close against the graph-derived LCC")
    missing = [column for column in BROKERAGE_COLUMNS if column not in brokerage]
    if missing:
        raise S45ContractError("canonical brokerage table is missing: %s" % ", ".join(missing))
    if brokerage["project_id"].astype(str).duplicated().any():
        raise S45ContractError("canonical brokerage table contains duplicate project_id")
    if set(brokerage["project_id"].astype(str)) != set(lcc.nodes):
        raise S45ContractError("canonical brokerage project IDs do not equal graph-derived LCC IDs")
    score = pd.to_numeric(brokerage["betweenness_brokerage"], errors="coerce")
    if score.isna().any() or (~score.map(math.isfinite)).any():
        raise S45ContractError("canonical brokerage scores must be finite")
    return CorrectedP0S45Authority(
        root=Path(preflight["corrected_p0_root"]),
        edges=normalized_edges,
        node_registry=registry,
        canonical_communities=communities,
        canonical_summary=summary,
        canonical_brokerage=brokerage,
        lcc=lcc,
        lcc_edges=derived_lcc_edges,
        canonical_partition=partition,
    )
