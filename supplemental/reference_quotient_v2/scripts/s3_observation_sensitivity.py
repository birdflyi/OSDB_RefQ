"""Corrected S3 first-order observation-boundary implementation.

S3 builds three deterministic directed observation views and sends every view
through the shared RefQ directed-to-undirected and network analysis authority.
It returns future output tables in memory only; corrected-P0 scientific
computation is not invoked by C3.7-C tests.
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import pandas as pd
import pandas.testing as pdt

from script.ch5_reference_quotient.network_views import (
    analyze_undirected_view,
    directed_to_undirected_edges,
)

from .paths import CORRECTED_P0_ROOT, DEFAULT_CONFIG_PATH, canonical_path
from .s2_weight_sensitivity import (
    S2ContractError,
    S2_UNDIRECTED_EDGE_COLUMNS,
    analyze_with_shared_network_authority,
    _normalize_undirected_parity_frame,
    preflight_corrected_p0_sensitivity_inputs,
    validate_directed_cross_project_edges,
    validate_network_parameters,
    validate_node_registry,
)


class S3ContractError(S2ContractError):
    """Raised when a prospective corrected S3 view is invalid."""


CANONICAL_SEED_CENTERED_OBSERVED = "CANONICAL_SEED_CENTERED_OBSERVED"
SEED_ONLY_INDUCED = "SEED_ONLY_INDUCED"
MULTI_SEED_TARGET_VIEW = "MULTI_SEED_TARGET_VIEW"
S3_VIEW_NAMES: tuple[str, ...] = (
    CANONICAL_SEED_CENTERED_OBSERVED,
    SEED_ONLY_INDUCED,
    MULTI_SEED_TARGET_VIEW,
)
S3_VIEW_STEMS: Mapping[str, str] = {
    CANONICAL_SEED_CENTERED_OBSERVED: "canonical_seed_centered_observed",
    SEED_ONLY_INDUCED: "seed_only_induced",
    MULTI_SEED_TARGET_VIEW: "multi_seed_target_view",
}
S3_SUMMARY_COLUMNS: tuple[str, ...] = (
    "view",
    "directed_edges",
    "directed_weight",
    "undirected_edges",
    "operator_order",
    "nodes",
    "edge_observed_nodes",
    "components",
    "isolates",
    "lcc_nodes",
    "lcc_edges",
    "lcc_coverage",
    "average_clustering_lcc",
    "transitivity_lcc",
    "algorithmic_community_method",
    "algorithmic_communities",
    "modularity",
    "brokerage_method",
    "brokerage_sample_size",
    "random_seed",
)
S3_COMMUNITY_COLUMNS: tuple[str, ...] = (
    "project_id",
    "community_id",
    "community_size",
)
S3_OUTPUT_CONTRACT: Mapping[str, tuple[str, ...]] = {
    "observation_boundary_sensitivity.csv": S3_SUMMARY_COLUMNS,
    **{
        "%s_%s.csv" % (stem, suffix): columns
        for stem in S3_VIEW_STEMS.values()
        for suffix, columns in (
            ("undirected_edges", S2_UNDIRECTED_EDGE_COLUMNS),
            ("lcc_edges", S2_UNDIRECTED_EDGE_COLUMNS),
            ("communities", S3_COMMUNITY_COLUMNS),
        )
    },
}


def load_corrected_p0_s3_inputs(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load and validate only the explicit corrected-P0 S3 input files."""

    preflight = preflight_corrected_p0_sensitivity_inputs(config_path)
    root = canonical_path(preflight["corrected_p0_root"])
    edges = pd.read_csv(
        root / "reference_quotient_cross_project_edges.csv",
        dtype={"source_project_id": "string", "target_project_id": "string"},
    )
    node_registry = pd.read_csv(
        root / "reference_quotient_node_registry.csv",
        dtype={"project_id": "string"},
    )
    seeds = pd.read_csv(
        root / "analysis_seed_manifest_294.csv",
        dtype={"repo_id": "string"},
    )
    validate_directed_cross_project_edges(edges)
    node_ids = validate_node_registry(node_registry)
    _validate_seed_manifest(seeds, node_ids)
    return edges, node_registry, seeds


@dataclass(frozen=True)
class S3ViewResult:
    """One first-order observation view and its shared-authority outputs."""

    name: str
    node_ids: tuple[str, ...]
    directed_edges: pd.DataFrame
    undirected_edges: pd.DataFrame
    lcc_edges: pd.DataFrame
    communities: pd.DataFrame
    brokerage: pd.DataFrame
    network_summary: Mapping[str, Any]


@dataclass(frozen=True)
class S3ObservationSensitivityResult:
    """All three S3 views and their in-memory contract tables."""

    view_results: Mapping[str, S3ViewResult]
    summary: pd.DataFrame
    random_seed: int
    brokerage_sample_size: int
    seed_ids: tuple[str, ...]


def _validate_seed_manifest(seeds: pd.DataFrame, node_ids: tuple[str, ...]) -> tuple[str, ...]:
    if "repo_id" not in seeds.columns:
        raise S3ContractError("analysis seed manifest requires repo_id")
    values = seeds["repo_id"]
    if values.isna().any() or values.astype(str).str.strip().eq("").any():
        raise S3ContractError("analysis seed manifest contains a missing repo_id")
    seed_ids = tuple(values.astype(str))
    if len(set(seed_ids)) != len(seed_ids):
        raise S3ContractError("analysis seed manifest repo_id values must be unique")
    if not set(seed_ids).issubset(set(node_ids)):
        raise S3ContractError("analysis seed manifest is not contained in node registry")
    return seed_ids


def _empty_community_frame() -> pd.DataFrame:
    return pd.DataFrame(columns=S3_COMMUNITY_COLUMNS)


def _normalize_community_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return _empty_community_frame()
    return frame.loc[:, S3_COMMUNITY_COLUMNS].reset_index(drop=True)


def build_s3_view_inputs(
    edges: pd.DataFrame,
    node_registry: pd.DataFrame,
    seeds: pd.DataFrame,
) -> Mapping[str, tuple[pd.DataFrame, tuple[str, ...]]]:
    """Build the three directed first-order views with deterministic nodes."""

    directed = validate_directed_cross_project_edges(edges)
    node_ids = validate_node_registry(node_registry)
    seed_ids = _validate_seed_manifest(seeds, node_ids)
    seed_set = set(seed_ids)
    multi_targets = set(
        directed.groupby("target_project_id")["source_project_id"]
        .nunique()
        .loc[lambda values: values >= 2]
        .index.astype(str)
    )
    canonical = directed.copy()
    seed_only = directed.loc[
        directed["source_project_id"].isin(seed_set)
        & directed["target_project_id"].isin(seed_set)
    ].copy()
    multi_target = directed.loc[directed["target_project_id"].isin(multi_targets)].copy()
    multi_node_set = seed_set | multi_targets
    multi_node_ids = tuple(node for node in node_ids if node in multi_node_set)
    return {
        CANONICAL_SEED_CENTERED_OBSERVED: (canonical, node_ids),
        SEED_ONLY_INDUCED: (seed_only, seed_ids),
        MULTI_SEED_TARGET_VIEW: (multi_target, multi_node_ids),
    }


def compute_s3_observation_sensitivity(
    edges: pd.DataFrame,
    node_registry: pd.DataFrame,
    seeds: pd.DataFrame,
    *,
    random_seed: int,
    brokerage_sample_size: int,
) -> S3ObservationSensitivityResult:
    """Compute all S3 views through the shared network authority."""

    seed, brokerage_sample = validate_network_parameters(random_seed, brokerage_sample_size)
    view_inputs = build_s3_view_inputs(edges, node_registry, seeds)
    view_results: dict[str, S3ViewResult] = {}
    summary_rows: list[dict[str, Any]] = []
    for name in S3_VIEW_NAMES:
        directed, node_ids = view_inputs[name]
        undirected = directed_to_undirected_edges(directed).reset_index(drop=True)
        network_summary, lcc_edges, communities, brokerage = analyze_with_shared_network_authority(
            undirected,
            seed,
            brokerage_sample,
            node_ids,
        )
        communities = _normalize_community_frame(communities)
        view_result = S3ViewResult(
            name=name,
            node_ids=tuple(node_ids),
            directed_edges=directed.reset_index(drop=True),
            undirected_edges=undirected,
            lcc_edges=lcc_edges.reset_index(drop=True),
            communities=communities,
            brokerage=brokerage.reset_index(drop=True),
            network_summary=dict(network_summary),
        )
        view_results[name] = view_result
        summary_rows.append(
            {
                **network_summary,
                "view": name,
                "directed_edges": int(len(directed)),
                "directed_weight": int(directed["weight"].sum()),
                "undirected_edges": int(len(undirected)),
            }
        )
    summary = pd.DataFrame(summary_rows, columns=S3_SUMMARY_COLUMNS)
    return S3ObservationSensitivityResult(
        view_results=view_results,
        summary=summary,
        random_seed=seed,
        brokerage_sample_size=brokerage_sample,
        seed_ids=tuple(_validate_seed_manifest(seeds, validate_node_registry(node_registry))),
    )


def build_future_s3_output_tables(
    result: S3ObservationSensitivityResult,
) -> dict[str, pd.DataFrame]:
    """Build future corrected S3 tables in memory without writing files."""

    if tuple(result.summary.columns) != S3_SUMMARY_COLUMNS:
        raise S3ContractError("S3 summary schema mismatch")
    if set(result.view_results) != set(S3_VIEW_NAMES):
        raise S3ContractError("S3 view set is incomplete")
    tables: dict[str, pd.DataFrame] = {
        "observation_boundary_sensitivity.csv": result.summary.copy()
    }
    for name in S3_VIEW_NAMES:
        view = result.view_results[name]
        stem = S3_VIEW_STEMS[name]
        tables[stem + "_undirected_edges.csv"] = view.undirected_edges.copy()
        tables[stem + "_lcc_edges.csv"] = view.lcc_edges.copy()
        tables[stem + "_communities.csv"] = view.communities.copy()
    for name, table in tables.items():
        if tuple(table.columns) != S3_OUTPUT_CONTRACT[name]:
            raise S3ContractError("S3 output contract mismatch: %s" % name)
    return tables


def _normalize_community_parity_frame(frame: pd.DataFrame) -> pd.DataFrame:
    """Normalize opaque project IDs while retaining integer community fields."""

    columns = list(S3_COMMUNITY_COLUMNS)
    work = frame.loc[:, columns].copy()
    if work["project_id"].isna().any():
        raise S3ContractError("S3 parity community project IDs must not be missing")
    project_ids = work["project_id"].astype("string")
    if project_ids.str.strip().eq("").any():
        raise S3ContractError("S3 parity community project IDs must not be empty")
    work["project_id"] = project_ids
    for column in ("community_id", "community_size"):
        numeric = pd.to_numeric(work[column], errors="coerce")
        if numeric.isna().any() or (~numeric.eq(numeric.round())).any():
            raise S3ContractError("S3 parity community field must be integral: %s" % column)
        work[column] = numeric.astype("int64")
    return work.reset_index(drop=True)


def assert_s3_canonical_view_matches_corrected_p0(
    result: S3ObservationSensitivityResult,
    corrected_p0_root: str | Path = CORRECTED_P0_ROOT,
    *,
    float_tolerance: float = 1e-12,
) -> dict[str, Any]:
    """Compare a future canonical S3 result with dynamic corrected-P0 files."""

    root = canonical_path(corrected_p0_root)
    if os.path.normcase(os.fspath(root)) != os.path.normcase(os.fspath(CORRECTED_P0_ROOT)):
        raise S3ContractError("S3 parity authority must be corrected P0 root")
    expected_registry = pd.read_csv(
        root / "reference_quotient_node_registry.csv",
        dtype={"project_id": "string"},
    )
    expected_nodes = validate_node_registry(expected_registry)
    actual = result.view_results[CANONICAL_SEED_CENTERED_OBSERVED]
    if actual.node_ids != expected_nodes:
        raise S3ContractError("canonical S3 node domain/order mismatch")
    file_map = {
        "undirected_edges": "rq2c_undirected_view_edges.csv",
        "lcc_edges": "rq2c_undirected_view_lcc_edges.csv",
        "communities": "rq2c_algorithmic_communities.csv",
    }
    actual_map = {
        "undirected_edges": actual.undirected_edges,
        "lcc_edges": actual.lcc_edges,
        "communities": actual.communities,
    }
    for key, filename in file_map.items():
        if key != "communities":
            expected = _normalize_undirected_parity_frame(
                pd.read_csv(
                    root / filename,
                    dtype={"node_u": "string", "node_v": "string"},
                )
            )
            observed = _normalize_undirected_parity_frame(actual_map[key])
        else:
            expected = _normalize_community_parity_frame(
                pd.read_csv(root / filename, dtype={"project_id": "string"})
            )
            observed = _normalize_community_parity_frame(actual_map[key])
        pdt.assert_frame_equal(expected, observed, check_dtype=False, check_exact=True)
    expected_summary = json.loads((root / "rq2c_undirected_view_summary.json").read_text(encoding="utf-8"))
    for column, expected in expected_summary.items():
        if column not in actual.network_summary:
            continue
        observed = actual.network_summary[column]
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            if not math.isclose(float(observed), float(expected), rel_tol=0.0, abs_tol=float_tolerance):
                raise S3ContractError("canonical S3 metric mismatch: %s" % column)
        elif observed != expected:
            raise S3ContractError("canonical S3 metric mismatch: %s" % column)
    return {
        "status": "PASS",
        "view": CANONICAL_SEED_CENTERED_OBSERVED,
        "dynamic_root": str(root),
        "float_tolerance": float_tolerance,
    }
