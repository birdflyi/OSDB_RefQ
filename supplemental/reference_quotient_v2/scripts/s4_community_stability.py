"""Corrected S4 weighted Louvain community-stability design.

Computation returns compact in-memory tables. Scientific output writing is
intentionally outside this C3.7-D module boundary.
"""

from __future__ import annotations

import itertools
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

import networkx as nx
import pandas as pd
from script.ch5_reference_quotient.network_views import canonicalize_undirected_graph_order

from .paths import CORRECTED_P0_ROOT, DEFAULT_CONFIG_PATH, PathGuardError, canonical_path, validate_scaffold_config
from .s45_canonical_graph import (
    S45ContractError,
    canonical_partition_from_frame,
    load_corrected_p0_s45_authority,
    preflight_corrected_p0_s45_inputs,
)


class S4ContractError(ValueError):
    """Raised when a prospective S4 input or result is invalid."""


S4_RUN_COLUMNS: tuple[str, ...] = (
    "seed",
    "community_count",
    "modularity",
    "ari_to_canonical",
    "is_canonical_seed",
)
S4_PAIRWISE_COLUMNS: tuple[str, ...] = ("seed_left", "seed_right", "ari")
S4_OUTPUT_CONTRACT: Mapping[str, tuple[str, ...] | None] = {
    "louvain_stability_runs.csv": S4_RUN_COLUMNS,
    "louvain_stability_pairwise.csv": S4_PAIRWISE_COLUMNS,
    "louvain_stability_summary.json": None,
}
S4_SEED_START = 20260731
S4_RUN_COUNT = 50
S4_SEED_END = S4_SEED_START + S4_RUN_COUNT - 1
S4_CANONICAL_SEED = S4_SEED_START
S4_ARI_ALERT_THRESHOLD = 0.9


def validate_s4_seeds(seeds: Iterable[object]) -> tuple[int, ...]:
    values = list(seeds)
    if not values:
        raise S4ContractError("S4 seed list must not be empty")
    normalized: list[int] = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise S4ContractError("S4 seeds must be integers")
        normalized.append(value)
    if len(set(normalized)) != len(normalized):
        raise S4ContractError("S4 seeds must be unique")
    if normalized != sorted(normalized):
        raise S4ContractError("S4 seeds must be in deterministic ascending order")
    return tuple(normalized)


def s4_production_seeds(config: Mapping[str, Any]) -> tuple[int, ...]:
    validate_scaffold_config(config)
    start = config["s4_louvain_seed_start"]
    count = config["s4_louvain_run_count"]
    seeds = tuple(range(start, start + count))
    if seeds != tuple(range(S4_SEED_START, S4_SEED_END + 1)):
        raise S4ContractError("S4 production seed range is not the frozen 50-run range")
    return seeds


def canonical_partition_labels(
    communities: Iterable[Iterable[object]],
    node_order: Iterable[object] | None = None,
) -> dict[str, int]:
    """Assign deterministic labels while preserving partition semantics."""

    ordered_nodes = tuple(str(node) for node in (node_order or ()))
    position = {node: index for index, node in enumerate(ordered_nodes)}
    normalized = [frozenset(str(node) for node in community) for community in communities]
    if len({node for community in normalized for node in community}) != sum(len(c) for c in normalized):
        raise S4ContractError("Louvain communities overlap")
    if any(node_order is not None and node not in position for community in normalized for node in community):
        raise S4ContractError("Louvain community contains an unknown node")
    if node_order is None:
        position = {node: index for index, node in enumerate(sorted({node for c in normalized for node in c}))}
    ordered_communities = sorted(
        normalized,
        key=lambda community: (-len(community), min(position[node] for node in community)),
    )
    labels = {node: label for label, community in enumerate(ordered_communities) for node in community}
    return {node: labels[node] for node in (ordered_nodes or tuple(sorted(labels)))}


def _partition_mapping(value: Mapping[object, object] | pd.DataFrame) -> dict[str, int]:
    if isinstance(value, pd.DataFrame):
        try:
            return canonical_partition_from_frame(value)
        except S45ContractError as exc:
            raise S4ContractError(str(exc)) from exc
    result: dict[str, int] = {}
    for node, label in value.items():
        if node is None or label is None:
            raise S4ContractError("partition contains a null node or label")
        result[str(node)] = int(label)
    if len(result) != len(value):
        raise S4ContractError("partition contains duplicate normalized node IDs")
    return result


def adjusted_rand_index(left: Mapping[object, object], right: Mapping[object, object]) -> float:
    """Compute the historical pair-count ARI without depending on labels."""

    common = sorted(set(str(node) for node in left) & set(str(node) for node in right))
    if len(common) < 2:
        return 1.0
    left_labels = {str(node): label for node, label in left.items()}
    right_labels = {str(node): label for node, label in right.items()}

    def combinations_two(value: int) -> float:
        return value * (value - 1) / 2.0

    cells: dict[tuple[object, object], int] = {}
    left_margins: dict[object, int] = {}
    right_margins: dict[object, int] = {}
    for node in common:
        cell = (left_labels[node], right_labels[node])
        cells[cell] = cells.get(cell, 0) + 1
        left_margins[left_labels[node]] = left_margins.get(left_labels[node], 0) + 1
        right_margins[right_labels[node]] = right_margins.get(right_labels[node], 0) + 1
    total = combinations_two(len(common))
    index = sum(combinations_two(value) for value in cells.values())
    expected = (
        sum(combinations_two(value) for value in left_margins.values())
        * sum(combinations_two(value) for value in right_margins.values())
        / total
        if total
        else 0.0
    )
    maximum = (
        sum(combinations_two(value) for value in left_margins.values())
        + sum(combinations_two(value) for value in right_margins.values())
    ) / 2.0
    denominator = maximum - expected
    if denominator == 0:
        return 1.0
    return float((index - expected) / denominator)


def _summary(values: Iterable[float]) -> dict[str, float]:
    series = pd.Series(list(values), dtype="float64")
    if series.empty:
        raise S4ContractError("cannot summarize an empty S4 metric")
    return {
        "min": float(series.min()),
        "q1": float(series.quantile(0.25)),
        "median": float(series.quantile(0.5)),
        "q3": float(series.quantile(0.75)),
        "max": float(series.max()),
        "mean": float(series.mean()),
    }


@dataclass(frozen=True)
class S4CommunityStabilityResult:
    graph: nx.Graph
    canonical_seed: int
    canonical_partition: Mapping[str, int]
    partitions_by_seed: Mapping[int, Mapping[str, int]]
    runs: pd.DataFrame
    pairwise: pd.DataFrame
    summary: Mapping[str, Any]


def compute_s4_community_stability(
    canonical_lcc: nx.Graph,
    canonical_partition: Mapping[object, object] | pd.DataFrame,
    *,
    seeds: Iterable[object],
    canonical_seed: int = S4_CANONICAL_SEED,
    ari_alert_threshold: float = S4_ARI_ALERT_THRESHOLD,
    canonical_modularity: float | None = None,
) -> S4CommunityStabilityResult:
    """Run fixture/future S4 computations and retain only in-memory tables."""

    if not isinstance(canonical_lcc, nx.Graph):
        raise S4ContractError("S4 input must be a NetworkX graph")
    seed_values = validate_s4_seeds(seeds)
    if canonical_seed not in seed_values:
        raise S4ContractError("canonical seed must occur in the S4 seed list")
    if isinstance(ari_alert_threshold, bool) or not isinstance(ari_alert_threshold, (int, float)):
        raise S4ContractError("ARI alert threshold must be numeric")
    if not 0.0 <= float(ari_alert_threshold) <= 1.0:
        raise S4ContractError("ARI alert threshold must be between 0 and 1")
    graph = canonicalize_undirected_graph_order(canonical_lcc)
    expected_partition = _partition_mapping(canonical_partition)
    graph_nodes = tuple(str(node) for node in graph.nodes)
    if set(expected_partition) != set(graph_nodes):
        raise S4ContractError("canonical partition does not cover the canonical LCC")

    run_rows: list[dict[str, Any]] = []
    partitions: dict[int, dict[str, int]] = {}
    for seed in seed_values:
        if graph.number_of_nodes() == 0:
            communities: list[set[str]] = []
            modularity = 0.0
        else:
            communities = list(nx.community.louvain_communities(graph, weight="weight", seed=seed))
            modularity = float(nx.community.modularity(graph, communities, weight="weight"))
        labels = canonical_partition_labels(communities, graph_nodes)
        if set(labels) != set(graph_nodes):
            raise S4ContractError("Louvain partition does not cover the canonical LCC")
        partitions[seed] = labels
        run_rows.append(
            {
                "seed": seed,
                "community_count": len(communities),
                "modularity": modularity,
                "ari_to_canonical": adjusted_rand_index(labels, expected_partition),
                "is_canonical_seed": seed == canonical_seed,
            }
        )
    runs = pd.DataFrame(run_rows, columns=S4_RUN_COLUMNS)
    pairwise_rows = [
        {
            "seed_left": left,
            "seed_right": right,
            "ari": adjusted_rand_index(partitions[left], partitions[right]),
        }
        for left, right in itertools.combinations(seed_values, 2)
    ]
    pairwise = pd.DataFrame(pairwise_rows, columns=S4_PAIRWISE_COLUMNS)
    canonical_row = runs.loc[runs["seed"].eq(canonical_seed)].iloc[0]
    partition_matches = float(canonical_row["ari_to_canonical"]) == 1.0
    modularity_matches = (
        canonical_modularity is not None
        and math.isclose(
            float(canonical_row["modularity"]),
            float(canonical_modularity),
            rel_tol=0.0,
            abs_tol=1e-12,
        )
    )
    summary = {
        "canonical_seed": canonical_seed,
        "canonical_community_count": int(canonical_row["community_count"]),
        "canonical_modularity": float(canonical_row["modularity"]),
        "canonical_seed_matches_p0": (bool(partition_matches and modularity_matches) if canonical_modularity is not None else None),
        "ari_to_canonical_summary": _summary(runs["ari_to_canonical"]),
        "pairwise_ari_summary": _summary(pairwise["ari"] if not pairwise.empty else [1.0]),
        "robustness_alert": bool(float(runs["ari_to_canonical"].min()) < float(ari_alert_threshold)),
        "ari_alert_threshold": float(ari_alert_threshold),
    }
    return S4CommunityStabilityResult(
        graph=graph,
        canonical_seed=canonical_seed,
        canonical_partition=expected_partition,
        partitions_by_seed=partitions,
        runs=runs,
        pairwise=pairwise,
        summary=summary,
    )


def build_future_s4_output_tables(result: S4CommunityStabilityResult) -> dict[str, pd.DataFrame]:
    """Finalize future S4 tables without creating an output directory."""

    if tuple(result.runs.columns) != S4_RUN_COLUMNS:
        raise S4ContractError("S4 run table schema mismatch")
    if tuple(result.pairwise.columns) != S4_PAIRWISE_COLUMNS:
        raise S4ContractError("S4 pairwise table schema mismatch")
    expected_pairs = len(result.runs) * (len(result.runs) - 1) // 2
    if len(result.pairwise) != expected_pairs:
        raise S4ContractError("S4 pairwise row count does not close")
    for row in result.pairwise.itertuples(index=False):
        if row.seed_left >= row.seed_right:
            raise S4ContractError("S4 pairwise seeds are not ordered")
    return {
        "louvain_stability_runs.csv": result.runs.copy(),
        "louvain_stability_pairwise.csv": result.pairwise.copy(),
        "louvain_stability_summary.json": dict(result.summary),
    }


def assert_s4_canonical_seed_matches_corrected_p0(
    result: S4CommunityStabilityResult,
    corrected_p0_root: str | Path = CORRECTED_P0_ROOT,
    *,
    float_tolerance: float = 1e-12,
) -> dict[str, Any]:
    """Future dynamic parity gate; this function is not called in C3.7-D."""

    root = canonical_path(corrected_p0_root)
    if os.path.normcase(os.fspath(root)) != os.path.normcase(os.fspath(CORRECTED_P0_ROOT)):
        raise S4ContractError("S4 parity authority must be official corrected P0 v3 root")
    try:
        authority = load_corrected_p0_s45_authority()
    except (S45ContractError, PathGuardError) as exc:
        raise S4ContractError(str(exc)) from exc
    if (result.canonical_seed, result.summary.get("canonical_seed")) != (S4_CANONICAL_SEED, S4_CANONICAL_SEED):
        raise S4ContractError("S4 canonical setting is not the corrected-P0 canonical seed")
    if tuple(result.graph.nodes) != tuple(authority.lcc.nodes):
        raise S4ContractError("S4 canonical LCC node order mismatch")
    canonical = result.partitions_by_seed.get(S4_CANONICAL_SEED)
    if canonical is None or adjusted_rand_index(canonical, authority.canonical_partition) != 1.0:
        raise S4ContractError("S4 canonical seed partition mismatch")
    row = result.runs.loc[result.runs["seed"].eq(S4_CANONICAL_SEED)]
    if len(row) != 1:
        raise S4ContractError("S4 result has no unique canonical seed row")
    expected_modularity = float(authority.canonical_summary["modularity"])
    observed_modularity = float(row.iloc[0]["modularity"])
    if not math.isclose(observed_modularity, expected_modularity, rel_tol=0.0, abs_tol=float_tolerance):
        raise S4ContractError("S4 canonical modularity mismatch")
    expected_count = int(authority.canonical_summary["algorithmic_communities"])
    if int(row.iloc[0]["community_count"]) != expected_count:
        raise S4ContractError("S4 canonical community count mismatch")
    return {
        "status": "PASS",
        "canonical_seed": S4_CANONICAL_SEED,
        "canonical_partition_label_invariant": True,
        "float_tolerance": float_tolerance,
        "dynamic_root": str(root),
    }


def preflight_corrected_p0_s4_inputs(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """Expose the shared metadata/header-only preflight under the S4 name."""

    return preflight_corrected_p0_s45_inputs(config_path)


def load_corrected_p0_s4_inputs(config_path: str | Path = DEFAULT_CONFIG_PATH):
    """Future full S4 loader; scientific stages must call it explicitly."""

    return load_corrected_p0_s45_authority(config_path)
