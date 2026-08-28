"""Corrected S5 unweighted approximate-betweenness stability design.

The full ranking table is the sole source for future inclusion-frequency
derivation. This module computes only in memory and never writes stage output.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import networkx as nx
import pandas as pd
from script.ch5_reference_quotient.network_views import canonicalize_undirected_graph_order

from .paths import CORRECTED_P0_ROOT, DEFAULT_CONFIG_PATH, PathGuardError, canonical_path, validate_scaffold_config
from .s45_canonical_graph import (
    S45ContractError,
    load_corrected_p0_s45_authority,
    preflight_corrected_p0_s45_inputs,
)


class S5ContractError(ValueError):
    """Raised when a prospective S5 input or result is invalid."""


S5_RANK_COLUMNS: tuple[str, ...] = ("k", "seed", "rank", "project_id", "score")
S5_RUN_BASE_COLUMNS: tuple[str, ...] = (
    "k",
    "seed",
    "spearman_to_canonical",
)
S5_DEFAULT_TOP_K: tuple[int, ...] = (10, 20, 50)
S5_RUN_COLUMNS: tuple[str, ...] = (
    "k",
    "seed",
    "spearman_to_canonical",
    "top10_overlap",
    "top20_overlap",
    "top50_overlap",
    "canonical_score_match",
)
S5_FREQUENCY_COLUMNS: tuple[str, ...] = (
    "k",
    "top_k",
    "project_id",
    "run_count",
    "inclusion_count",
    "inclusion_frequency",
)
S5_OUTPUT_CONTRACT: Mapping[str, tuple[str, ...] | None] = {
    "brokerage_rank_stability.csv": S5_RANK_COLUMNS,
    "brokerage_stability_runs.csv": S5_RUN_COLUMNS,
    "brokerage_topk_inclusion_frequency.csv": S5_FREQUENCY_COLUMNS,
    "brokerage_stability_summary.json": None,
}
S5_K_VALUES: tuple[int, ...] = (250, 500, 1000)
S5_SEED_START = 20260731
S5_RUN_COUNT = 20
S5_SEED_END = S5_SEED_START + S5_RUN_COUNT - 1
S5_CANONICAL_K = 500
S5_CANONICAL_SEED = S5_SEED_START
S5_SPEARMAN_ALERT_THRESHOLD = 0.9
S5_TOP50_OVERLAP_ALERT_THRESHOLD = 0.8


def validate_s5_values(values: Iterable[object], name: str) -> tuple[int, ...]:
    raw = list(values)
    if not raw:
        raise S5ContractError("%s must not be empty" % name)
    normalized: list[int] = []
    for value in raw:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise S5ContractError("%s must contain positive integers" % name)
        normalized.append(value)
    if len(set(normalized)) != len(normalized):
        raise S5ContractError("%s must be unique" % name)
    if normalized != sorted(normalized):
        raise S5ContractError("%s must be in deterministic ascending order" % name)
    return tuple(normalized)


def validate_s5_k_values(values: Iterable[object]) -> tuple[int, ...]:
    return validate_s5_values(values, "S5 k values")


def validate_s5_seeds(values: Iterable[object]) -> tuple[int, ...]:
    return validate_s5_values(values, "S5 seeds")


def validate_s5_top_k(values: Iterable[object]) -> tuple[int, ...]:
    return validate_s5_values(values, "S5 top_k values")


def s5_production_settings(config: Mapping[str, Any]) -> dict[str, Any]:
    validate_scaffold_config(config)
    k_values = validate_s5_k_values(config["s5_brokerage_k"])
    seeds = tuple(range(config["s5_seed_start"], config["s5_seed_start"] + config["s5_run_count"]))
    top_k = validate_s5_top_k(config["s5_top_k"])
    if k_values != S5_K_VALUES:
        raise S5ContractError("S5 k contract is not 250, 500, 1000")
    if seeds != tuple(range(S5_SEED_START, S5_SEED_END + 1)):
        raise S5ContractError("S5 production seed range is not the frozen 20-run range")
    if top_k != S5_DEFAULT_TOP_K:
        raise S5ContractError("S5 top_k contract is not 10, 20, 50")
    if config["random_seed"] != S5_CANONICAL_SEED or config["brokerage_sample_size"] != S5_CANONICAL_K:
        raise S5ContractError("S5 canonical setting does not match corrected P0 configuration")
    return {
        "k_values": k_values,
        "seeds": seeds,
        "top_k": top_k,
        "canonical_k": S5_CANONICAL_K,
        "canonical_seed": S5_CANONICAL_SEED,
        "spearman_alert_threshold": float(config["s5_spearman_alert_threshold"]),
        "top50_overlap_alert_threshold": float(config["s5_top50_overlap_alert_threshold"]),
    }


def _score_mapping(value: Mapping[object, object] | pd.DataFrame) -> dict[str, float]:
    if isinstance(value, pd.DataFrame):
        if "project_id" not in value or "betweenness_brokerage" not in value:
            raise S5ContractError("canonical brokerage input requires project_id and betweenness_brokerage")
        project_ids = value["project_id"].astype(str)
        scores = pd.to_numeric(value["betweenness_brokerage"], errors="coerce")
        if project_ids.duplicated().any() or scores.isna().any() or (~scores.map(math.isfinite)).any():
            raise S5ContractError("canonical brokerage input has duplicate or invalid scores")
        return {project_id: float(score) for project_id, score in zip(project_ids, scores)}
    result: dict[str, float] = {}
    for project_id, score in value.items():
        if project_id is None:
            raise S5ContractError("canonical brokerage input has a null project_id")
        numeric = float(score)
        if not math.isfinite(numeric):
            raise S5ContractError("canonical brokerage scores must be finite")
        result[str(project_id)] = numeric
    if len(result) != len(value):
        raise S5ContractError("canonical brokerage input has duplicate normalized project IDs")
    return result


def rank_brokerage_scores(
    graph: nx.Graph,
    scores: Mapping[object, object],
) -> pd.DataFrame:
    """Rank scores using score, unweighted degree, then project ID."""

    node_ids = tuple(str(node) for node in graph.nodes)
    normalized = _score_mapping(scores)
    if set(normalized) != set(node_ids):
        raise S5ContractError("brokerage scores do not cover the complete canonical LCC")
    degree = {str(node): int(graph.degree(node)) for node in graph.nodes}
    ordered = sorted(
        node_ids,
        key=lambda node: (-float(normalized[node]), -degree[node], node),
    )
    return pd.DataFrame(
        [
            {"rank": rank, "project_id": project_id, "score": float(normalized[project_id])}
            for rank, project_id in enumerate(ordered, start=1)
        ],
        columns=("rank", "project_id", "score"),
    )


def spearman_rank_correlation(left: pd.DataFrame, right: pd.DataFrame) -> float:
    """Compare ordinal ranks on the common complete project set."""

    for frame in (left, right):
        if "project_id" not in frame or "rank" not in frame:
            raise S5ContractError("ranking table requires project_id and rank")
    left_ids = set(left["project_id"].astype(str))
    right_ids = set(right["project_id"].astype(str))
    if left_ids != right_ids:
        raise S5ContractError("Spearman comparison requires the complete common node set")
    joined = (
        left.assign(project_id=left["project_id"].astype(str))[["project_id", "rank"]]
        .merge(
            right.assign(project_id=right["project_id"].astype(str))[["project_id", "rank"]],
            on="project_id",
            suffixes=("_left", "_right"),
        )
    )
    if len(joined) < 2:
        return 1.0
    left_rank = joined["rank_left"].astype(float)
    right_rank = joined["rank_right"].astype(float)
    denominator = float((left_rank - left_rank.mean()).pow(2).sum())
    right_denominator = float((right_rank - right_rank.mean()).pow(2).sum())
    if denominator == 0.0 or right_denominator == 0.0:
        return 1.0
    covariance = float(((left_rank - left_rank.mean()) * (right_rank - right_rank.mean())).sum())
    return covariance / math.sqrt(denominator * right_denominator)


def top_k_overlap(left: pd.DataFrame, right: pd.DataFrame, top_k: int) -> float:
    if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k <= 0:
        raise S5ContractError("top_k must be a positive integer")
    if top_k > len(left) or top_k > len(right):
        raise S5ContractError("top_k exceeds the complete ranking size")
    left_ids = set(left.nsmallest(top_k, "rank")["project_id"].astype(str))
    right_ids = set(right.nsmallest(top_k, "rank")["project_id"].astype(str))
    return float(len(left_ids & right_ids) / top_k)


def _metric_summary(values: Iterable[float]) -> dict[str, float]:
    series = pd.Series(list(values), dtype="float64")
    if series.empty:
        raise S5ContractError("cannot summarize an empty S5 metric")
    return {
        "min": float(series.min()),
        "q1": float(series.quantile(0.25)),
        "median": float(series.quantile(0.5)),
        "q3": float(series.quantile(0.75)),
        "max": float(series.max()),
        "mean": float(series.mean()),
    }


def derive_inclusion_frequency(
    ranking: pd.DataFrame,
    top_ks: Iterable[object],
) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    """Derive frequency from full ranking rows and fail closed on closure."""

    top_values = validate_s5_top_k(top_ks)
    missing = [column for column in S5_RANK_COLUMNS if column not in ranking]
    if missing:
        raise S5ContractError("full ranking is missing: %s" % ", ".join(missing))
    work = ranking.loc[:, S5_RANK_COLUMNS].copy()
    work["project_id"] = work["project_id"].astype(str)
    for column in ("k", "seed", "rank"):
        numeric = pd.to_numeric(work[column], errors="coerce")
        if numeric.isna().any() or (~numeric.eq(numeric.round())).any():
            raise S5ContractError("full ranking %s must be integral" % column)
        work[column] = numeric.astype("int64")
    if work.duplicated(["k", "seed", "rank"]).any():
        raise S5ContractError("full ranking has duplicate ordinal ranks")
    for (k, seed), group in work.groupby(["k", "seed"], sort=False):
        ranks = sorted(group["rank"].tolist())
        if ranks != list(range(1, len(ranks) + 1)):
            raise S5ContractError("full ranking must contain one complete ordinal ranking per seed")
        if group["project_id"].duplicated().any():
            raise S5ContractError("full ranking contains duplicate project IDs in one seed-run")
    for k, group in work.groupby("k", sort=False):
        node_sets = {
            tuple(sorted(seed_group["project_id"].tolist()))
            for _, seed_group in group.groupby("seed", sort=False)
        }
        if len(node_sets) != 1:
            raise S5ContractError("full ranking node set must be complete and stable for each k")
    run_counts = work.groupby("k")["seed"].nunique().to_dict()
    frames: list[pd.DataFrame] = []
    closure: list[dict[str, Any]] = []
    for k in sorted(work["k"].unique()):
        k_work = work.loc[work["k"].eq(k)]
        run_count = int(run_counts[k])
        for top_k in top_values:
            selected = k_work.loc[k_work["rank"].le(top_k)]
            counts = (
                selected.groupby("project_id", as_index=False)["seed"]
                .nunique()
                .rename(columns={"seed": "inclusion_count"})
            )
            counts["k"] = int(k)
            counts["top_k"] = int(top_k)
            counts["run_count"] = run_count
            counts["inclusion_frequency"] = counts["inclusion_count"] / run_count
            frames.append(counts.loc[:, S5_FREQUENCY_COLUMNS])
            observed = int(counts["inclusion_count"].sum())
            expected = run_count * int(top_k)
            closure.append(
                {
                    "k": int(k),
                    "top_k": int(top_k),
                    "run_count": run_count,
                    "sum_inclusion_count": observed,
                    "expected": expected,
                    "closed": observed == expected,
                }
            )
            if observed != expected:
                raise S5ContractError("S5 inclusion-frequency closure failed")
    frequency = (
        pd.concat(frames, ignore_index=True)
        if frames
        else pd.DataFrame(columns=S5_FREQUENCY_COLUMNS)
    )
    if not frequency.empty:
        frequency = frequency.sort_values(
            ["k", "top_k", "inclusion_count", "project_id"],
            ascending=[True, True, False, True],
            kind="stable",
        ).reset_index(drop=True)
    return frequency.loc[:, S5_FREQUENCY_COLUMNS], closure


@dataclass(frozen=True)
class S5BrokerageStabilityResult:
    graph: nx.Graph
    canonical_k: int
    canonical_seed: int
    top_ks: tuple[int, ...]
    rankings: pd.DataFrame
    runs: pd.DataFrame
    inclusion_frequency: pd.DataFrame
    inclusion_closure: tuple[Mapping[str, Any], ...]
    summary: Mapping[str, Any]


def compute_s5_brokerage_stability(
    canonical_lcc: nx.Graph,
    canonical_scores: Mapping[object, object] | pd.DataFrame,
    *,
    k_values: Iterable[object],
    seeds: Iterable[object],
    top_ks: Iterable[object] = S5_DEFAULT_TOP_K,
    canonical_k: int = S5_CANONICAL_K,
    canonical_seed: int = S5_CANONICAL_SEED,
    spearman_alert_threshold: float = S5_SPEARMAN_ALERT_THRESHOLD,
    top50_overlap_alert_threshold: float = S5_TOP50_OVERLAP_ALERT_THRESHOLD,
    float_tolerance: float = 1e-12,
) -> S5BrokerageStabilityResult:
    """Run future/fixture S5 settings with explicit unweighted semantics."""

    if not isinstance(canonical_lcc, nx.Graph):
        raise S5ContractError("S5 input must be a NetworkX graph")
    k_values_tuple = validate_s5_k_values(k_values)
    seed_values = validate_s5_seeds(seeds)
    top_values = validate_s5_top_k(top_ks)
    if canonical_k not in k_values_tuple or canonical_seed not in seed_values:
        raise S5ContractError("canonical S5 setting must occur in k and seed inputs")
    for value, name in ((spearman_alert_threshold, "Spearman alert threshold"), (top50_overlap_alert_threshold, "top50 overlap alert threshold")):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0.0 <= float(value) <= 1.0:
            raise S5ContractError("%s must be between 0 and 1" % name)
    if float_tolerance < 0:
        raise S5ContractError("S5 floating tolerance must be non-negative")
    graph = canonicalize_undirected_graph_order(canonical_lcc)
    if graph.number_of_nodes() == 0:
        raise S5ContractError("S5 canonical LCC must not be empty")
    expected_scores = _score_mapping(canonical_scores)
    node_ids = tuple(str(node) for node in graph.nodes)
    if set(expected_scores) != set(node_ids):
        raise S5ContractError("canonical brokerage scores do not cover the canonical LCC")
    canonical_rank = rank_brokerage_scores(graph, expected_scores)

    ranking_rows: list[dict[str, Any]] = []
    run_rows: list[dict[str, Any]] = []
    for k in k_values_tuple:
        for seed in seed_values:
            values = nx.betweenness_centrality(
                graph,
                k=min(k, len(graph)),
                normalized=True,
                seed=seed,
                weight=None,
            )
            normalized_values = {str(node): float(score) for node, score in values.items()}
            ranked = rank_brokerage_scores(graph, normalized_values)
            for row in ranked.itertuples(index=False):
                ranking_rows.append(
                    {
                        "k": k,
                        "seed": seed,
                        "rank": int(row.rank),
                        "project_id": str(row.project_id),
                        "score": float(row.score),
                    }
                )
            row_data: dict[str, Any] = {
                "k": k,
                "seed": seed,
                "spearman_to_canonical": spearman_rank_correlation(ranked, canonical_rank),
            }
            for top_k in top_values:
                if top_k > len(graph):
                    raise S5ContractError("S5 top_k exceeds the canonical LCC size")
                row_data["top%s_overlap" % top_k] = top_k_overlap(ranked, canonical_rank, top_k)
            score_match = False
            if (k, seed) == (canonical_k, canonical_seed):
                score_match = all(
                    math.isclose(
                        normalized_values[project_id],
                        expected_scores[project_id],
                        rel_tol=0.0,
                        abs_tol=float_tolerance,
                    )
                    for project_id in node_ids
                )
            row_data["canonical_score_match"] = score_match
            run_rows.append(row_data)
    rankings = pd.DataFrame(ranking_rows, columns=S5_RANK_COLUMNS)
    run_columns = S5_RUN_BASE_COLUMNS + tuple("top%s_overlap" % top_k for top_k in top_values) + ("canonical_score_match",)
    runs = pd.DataFrame(run_rows, columns=run_columns)
    frequency, closure = derive_inclusion_frequency(rankings, top_values)
    summary_top_k = 50 if 50 in top_values else max(top_values)
    summary = {
        "canonical_setting": {
            "k": canonical_k,
            "seed": canonical_seed,
            "normalized": True,
            "weight": None,
        },
        "canonical_setting_matches_p0": bool(
            runs.loc[(runs["k"] == canonical_k) & (runs["seed"] == canonical_seed), "canonical_score_match"].iloc[0]
        ),
        "spearman_summary": _metric_summary(runs["spearman_to_canonical"]),
        "top50_overlap_summary": _metric_summary(runs["top%s_overlap" % summary_top_k]),
        "robustness_alert": bool(
            _metric_summary(runs["top%s_overlap" % summary_top_k])["median"] < float(top50_overlap_alert_threshold)
            or _metric_summary(runs["spearman_to_canonical"])["median"] < float(spearman_alert_threshold)
        ),
        "spearman_alert_threshold": float(spearman_alert_threshold),
        "top50_overlap_alert_threshold": float(top50_overlap_alert_threshold),
        "inclusion_closure": closure,
    }
    return S5BrokerageStabilityResult(
        graph=graph,
        canonical_k=canonical_k,
        canonical_seed=canonical_seed,
        top_ks=top_values,
        rankings=rankings,
        runs=runs,
        inclusion_frequency=frequency,
        inclusion_closure=tuple(closure),
        summary=summary,
    )


def build_future_s5_output_tables(result: S5BrokerageStabilityResult) -> dict[str, Any]:
    """Finalize future S5 tables and summary in memory only."""

    expected_run_columns = S5_RUN_BASE_COLUMNS + tuple("top%s_overlap" % top_k for top_k in result.top_ks) + ("canonical_score_match",)
    if tuple(result.rankings.columns) != S5_RANK_COLUMNS:
        raise S5ContractError("S5 full ranking schema mismatch")
    if tuple(result.runs.columns) != expected_run_columns:
        raise S5ContractError("S5 run table schema mismatch")
    if tuple(result.inclusion_frequency.columns) != S5_FREQUENCY_COLUMNS:
        raise S5ContractError("S5 inclusion-frequency schema mismatch")
    if any(not bool(row["closed"]) for row in result.inclusion_closure):
        raise S5ContractError("S5 inclusion-frequency closure is not closed")
    return {
        "brokerage_rank_stability.csv": result.rankings.copy(),
        "brokerage_stability_runs.csv": result.runs.copy(),
        "brokerage_topk_inclusion_frequency.csv": result.inclusion_frequency.copy(),
        "brokerage_stability_summary.json": dict(result.summary),
    }


def assert_s5_canonical_setting_matches_corrected_p0(
    result: S5BrokerageStabilityResult,
    corrected_p0_root: str | Path = CORRECTED_P0_ROOT,
    *,
    float_tolerance: float = 1e-12,
) -> dict[str, Any]:
    """Future dynamic parity gate; this function is not called in C3.7-D."""

    root = canonical_path(corrected_p0_root)
    if os.path.normcase(os.fspath(root)) != os.path.normcase(os.fspath(CORRECTED_P0_ROOT)):
        raise S5ContractError("S5 parity authority must be official corrected P0 v3 root")
    try:
        authority = load_corrected_p0_s45_authority()
    except (S45ContractError, PathGuardError) as exc:
        raise S5ContractError(str(exc)) from exc
    if tuple(result.graph.nodes) != tuple(authority.lcc.nodes):
        raise S5ContractError("S5 canonical LCC node order mismatch")
    if (result.canonical_k, result.canonical_seed) != (S5_CANONICAL_K, S5_CANONICAL_SEED):
        raise S5ContractError("S5 canonical setting is not 500/20260731")
    expected_scores = _score_mapping(authority.canonical_brokerage)
    expected_rank = rank_brokerage_scores(authority.lcc, expected_scores)
    actual = result.rankings.loc[
        result.rankings["k"].eq(S5_CANONICAL_K) & result.rankings["seed"].eq(S5_CANONICAL_SEED),
        ["rank", "project_id", "score"],
    ].reset_index(drop=True)
    if len(actual) != len(expected_rank):
        raise S5ContractError("S5 canonical ranking size mismatch")
    if actual["project_id"].astype(str).tolist() != expected_rank["project_id"].astype(str).tolist():
        raise S5ContractError("S5 canonical project ranking mismatch")
    if actual["rank"].astype(int).tolist() != expected_rank["rank"].astype(int).tolist():
        raise S5ContractError("S5 canonical ordinal ranking mismatch")
    for observed, expected in zip(actual["score"], expected_rank["score"]):
        if not math.isclose(float(observed), float(expected), rel_tol=0.0, abs_tol=float_tolerance):
            raise S5ContractError("S5 canonical brokerage score mismatch")
    return {
        "status": "PASS",
        "canonical_k": S5_CANONICAL_K,
        "canonical_seed": S5_CANONICAL_SEED,
        "canonical_score_match": True,
        "ranking_tiebreak": "score_desc,undirected_degree_desc,project_id_asc",
        "float_tolerance": float_tolerance,
        "dynamic_root": str(root),
    }


def preflight_corrected_p0_s5_inputs(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """Expose the shared metadata/header-only preflight under the S5 name."""

    return preflight_corrected_p0_s45_inputs(config_path)


def load_corrected_p0_s5_inputs(config_path: str | Path = DEFAULT_CONFIG_PATH):
    """Future full S5 loader; scientific stages must call it explicitly."""

    return load_corrected_p0_s45_authority(config_path)
