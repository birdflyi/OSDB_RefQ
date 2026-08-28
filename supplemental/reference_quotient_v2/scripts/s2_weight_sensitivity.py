"""Corrected S2 directed-weight sensitivity implementation.

The functions in this module separate corrected-P0 input loading, validation,
computation, and in-memory future-table finalization.  No function writes a
scientific output file.  Corrected-P0 computation is intentionally not called
by the C3.7-C implementation tests.
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import pandas as pd
import pandas.testing as pdt

from script.ch5_reference_quotient.network_views import (
    analyze_undirected_view,
    directed_to_undirected_edges,
)

from .manifest import sha256_file, validate_scaffold_provenance
from .paths import CORRECTED_P0_ROOT, DEFAULT_CONFIG_PATH, canonical_path, load_config
from .schema import SOURCE_ADMISSION_STATUSES


class S2ContractError(ValueError):
    """Raised when a prospective corrected S2 input/result is invalid."""


S2_DIRECTED_EDGE_REQUIRED_COLUMNS: tuple[str, ...] = (
    "source_project_id",
    "target_project_id",
    "weight",
)
S2_DIRECTED_EDGE_OPTIONAL_COLUMNS: tuple[str, ...] = ("multiplicity", "is_self_loop")
S2_NODE_REQUIRED_COLUMNS: tuple[str, ...] = ("project_id",)
S2_THRESHOLDS: tuple[int, ...] = (1, 2, 5, 10)

S2_SUMMARY_COLUMNS: tuple[str, ...] = (
    "view",
    "operator_order",
    "nodes",
    "edge_observed_nodes",
    "undirected_edges",
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
S2_SENSITIVITY_COLUMNS: tuple[str, ...] = (
    "threshold",
    "directed_edges_retained",
    "directed_weight_retained",
    "directed_weight_share",
    *S2_SUMMARY_COLUMNS,
)
S2_UNDIRECTED_EDGE_COLUMNS: tuple[str, ...] = (
    "node_u",
    "node_v",
    "weight",
    "directed_edge_count",
)
S2_OUTPUT_CONTRACT: Mapping[str, tuple[str, ...]] = {
    "edge_weight_sensitivity.csv": S2_SENSITIVITY_COLUMNS,
    **{
        "threshold_%s_undirected_edges.csv" % threshold: S2_UNDIRECTED_EDGE_COLUMNS
        for threshold in S2_THRESHOLDS
    },
}


def load_corrected_p0_s2_inputs(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load and validate only the explicit corrected-P0 S2 input files."""

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
    validate_directed_cross_project_edges(edges)
    validate_node_registry(node_registry)
    return edges, node_registry


@dataclass(frozen=True)
class S2WeightSensitivityResult:
    """S2 summary and threshold edge tables held only in memory."""

    thresholds: tuple[int, ...]
    node_ids: tuple[str, ...]
    sensitivity: pd.DataFrame
    undirected_edges_by_threshold: Mapping[int, pd.DataFrame]
    random_seed: int
    brokerage_sample_size: int


def validate_s2_thresholds(thresholds: Iterable[object]) -> tuple[int, ...]:
    values = list(thresholds)
    if not values:
        raise S2ContractError("S2 thresholds must not be empty")
    normalized: list[int] = []
    for value in values:
        if isinstance(value, bool):
            raise S2ContractError("S2 thresholds must be positive integers")
        try:
            numeric = float(value)
        except (TypeError, ValueError) as exc:
            raise S2ContractError("S2 thresholds must be positive integers") from exc
        if not math.isfinite(numeric) or not numeric.is_integer() or numeric <= 0:
            raise S2ContractError("S2 thresholds must be positive integers")
        normalized.append(int(numeric))
    if len(set(normalized)) != len(normalized):
        raise S2ContractError("S2 thresholds must be unique")
    if normalized != sorted(normalized):
        raise S2ContractError("S2 thresholds must be strictly increasing")
    return tuple(normalized)


def _positive_integral_series(frame: pd.DataFrame, column: str) -> pd.Series:
    values: list[int] = []
    for value in frame[column].tolist():
        if isinstance(value, bool):
            raise S2ContractError("%s must be finite positive integral" % column)
        try:
            numeric = float(value)
        except (TypeError, ValueError) as exc:
            raise S2ContractError("%s must be finite positive integral" % column) from exc
        if not math.isfinite(numeric) or not numeric.is_integer() or numeric <= 0:
            raise S2ContractError("%s must be finite positive integral" % column)
        values.append(int(numeric))
    return pd.Series(values, index=frame.index, dtype="int64")


def _bool_value(value: object, column: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str):
        text = value.strip().lower()
        if text in {"true", "1"}:
            return True
        if text in {"false", "0"}:
            return False
    raise S2ContractError("%s must be a boolean" % column)


def validate_directed_cross_project_edges(edges: pd.DataFrame) -> pd.DataFrame:
    """Validate and normalize the corrected-P0 directed cross-project table."""

    missing = [column for column in S2_DIRECTED_EDGE_REQUIRED_COLUMNS if column not in edges]
    if missing:
        raise S2ContractError("missing S2 edge columns: %s" % ", ".join(missing))
    work = edges.copy()
    for column in ("source_project_id", "target_project_id"):
        if work[column].isna().any() or work[column].astype(str).str.strip().eq("").any():
            raise S2ContractError("%s contains a missing project ID" % column)
        work[column] = work[column].astype(str)
    if (work["source_project_id"] == work["target_project_id"]).any():
        raise S2ContractError("S2 cross-project input contains a self-loop")
    work["weight"] = _positive_integral_series(work, "weight")
    if "multiplicity" in work.columns:
        work["multiplicity"] = _positive_integral_series(work, "multiplicity")
        if not work["weight"].eq(work["multiplicity"]).all():
            raise S2ContractError("weight must equal multiplicity for current P0 semantics")
    if "is_self_loop" in work.columns:
        self_loop = work["is_self_loop"].map(lambda value: _bool_value(value, "is_self_loop"))
        if self_loop.any():
            raise S2ContractError("S2 cross-project input contains an is_self_loop row")
        work["is_self_loop"] = self_loop.astype(bool)
    else:
        work["is_self_loop"] = False
    return work


def validate_node_registry(node_registry: pd.DataFrame) -> tuple[str, ...]:
    """Validate and return the complete corrected-P0 node order."""

    missing = [column for column in S2_NODE_REQUIRED_COLUMNS if column not in node_registry]
    if missing:
        raise S2ContractError("missing S2 node registry columns: %s" % ", ".join(missing))
    values = node_registry["project_id"]
    if values.isna().any() or values.astype(str).str.strip().eq("").any():
        raise S2ContractError("node registry contains a missing project_id")
    node_ids = tuple(values.astype(str))
    if len(set(node_ids)) != len(node_ids):
        raise S2ContractError("node registry project_id values must be unique")
    return node_ids


def validate_network_parameters(random_seed: object, brokerage_sample_size: object) -> tuple[int, int]:
    if isinstance(random_seed, bool) or not isinstance(random_seed, int):
        raise S2ContractError("random_seed must be an integer")
    if isinstance(brokerage_sample_size, bool) or not isinstance(brokerage_sample_size, int):
        raise S2ContractError("brokerage_sample_size must be an integer")
    if brokerage_sample_size <= 0:
        raise S2ContractError("brokerage_sample_size must be positive")
    return random_seed, brokerage_sample_size


def analyze_with_shared_network_authority(
    undirected_edges: pd.DataFrame,
    random_seed: int,
    brokerage_sample_size: int,
    node_ids: Iterable[object],
) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Use shared analysis, with a defined zero-edge isolate fallback.

    The current shared implementation raises during Louvain modularity for a
    graph containing nodes but no edges.  The fallback only handles that
    degenerate graph; every non-empty edge view still uses the shared method.
    """

    ordered_nodes = tuple(str(node) for node in node_ids)
    try:
        return analyze_undirected_view(
            undirected_edges,
            random_seed,
            brokerage_sample_size,
            ordered_nodes,
        )
    except ZeroDivisionError:
        if not undirected_edges.empty:
            raise
        node_count = len(ordered_nodes)
        lcc_nodes = 1 if node_count else 0
        lcc_edges = undirected_edges.iloc[:0].copy()
        communities = pd.DataFrame(
            [{"project_id": ordered_nodes[0], "community_id": 0, "community_size": 1}]
            if node_count
            else [],
            columns=("project_id", "community_id", "community_size"),
        )
        brokerage = pd.DataFrame(
            [
                {
                    "project_id": ordered_nodes[0],
                    "undirected_degree": 0,
                    "undirected_strength": 0.0,
                    "local_clustering": 0.0,
                    "betweenness_brokerage": 0.0,
                    "community_id": 0,
                }
            ]
            if node_count
            else [],
            columns=(
                "project_id",
                "undirected_degree",
                "undirected_strength",
                "local_clustering",
                "betweenness_brokerage",
                "community_id",
            ),
        )
        summary = {
            "view": "U(G_RefQ)",
            "operator_order": "first_order_undirected_view",
            "nodes": node_count,
            "edge_observed_nodes": 0,
            "undirected_edges": 0,
            "components": node_count,
            "isolates": node_count,
            "lcc_nodes": lcc_nodes,
            "lcc_edges": 0,
            "lcc_coverage": (lcc_nodes / node_count if node_count else 0.0),
            "average_clustering_lcc": 0.0,
            "transitivity_lcc": 0.0,
            "algorithmic_community_method": "networkx_louvain",
            "algorithmic_communities": int(bool(node_count)),
            "modularity": 0.0,
            "brokerage_method": "unweighted_approximate_betweenness",
            "brokerage_sample_size": 0,
            "random_seed": random_seed,
        }
        return summary, lcc_edges, communities, brokerage


def compute_s2_weight_sensitivity(
    edges: pd.DataFrame,
    node_registry: pd.DataFrame,
    *,
    thresholds: Iterable[object],
    random_seed: int,
    brokerage_sample_size: int,
) -> S2WeightSensitivityResult:
    """Compute future S2 threshold views from explicit in-memory inputs."""

    thresholds_tuple = validate_s2_thresholds(thresholds)
    seed, brokerage = validate_network_parameters(random_seed, brokerage_sample_size)
    directed = validate_directed_cross_project_edges(edges)
    node_ids = validate_node_registry(node_registry)
    total_weight = int(directed["weight"].sum())
    summaries: list[dict[str, Any]] = []
    undirected_by_threshold: dict[int, pd.DataFrame] = {}
    for threshold in thresholds_tuple:
        retained = directed.loc[directed["weight"].ge(threshold)].copy()
        undirected = directed_to_undirected_edges(retained)
        summary, _, _, _ = analyze_with_shared_network_authority(
            undirected,
            seed,
            brokerage,
            node_ids,
        )
        summaries.append(
            {
                "threshold": threshold,
                "directed_edges_retained": int(len(retained)),
                "directed_weight_retained": int(retained["weight"].sum()),
                "directed_weight_share": (
                    float(retained["weight"].sum() / total_weight) if total_weight else 0.0
                ),
                **summary,
            }
        )
        undirected_by_threshold[threshold] = undirected.reset_index(drop=True)
    sensitivity = pd.DataFrame(summaries, columns=S2_SENSITIVITY_COLUMNS)
    return S2WeightSensitivityResult(
        thresholds=thresholds_tuple,
        node_ids=node_ids,
        sensitivity=sensitivity,
        undirected_edges_by_threshold=undirected_by_threshold,
        random_seed=seed,
        brokerage_sample_size=brokerage,
    )


def build_future_s2_output_tables(result: S2WeightSensitivityResult) -> dict[str, pd.DataFrame]:
    """Build future S2 tables in memory without writing files."""

    expected_thresholds = validate_s2_thresholds(result.thresholds)
    if tuple(result.sensitivity.columns) != S2_SENSITIVITY_COLUMNS:
        raise S2ContractError("S2 sensitivity schema mismatch")
    if set(result.undirected_edges_by_threshold) != set(expected_thresholds):
        raise S2ContractError("S2 threshold edge tables are incomplete")
    tables: dict[str, pd.DataFrame] = {
        "edge_weight_sensitivity.csv": result.sensitivity.copy(),
    }
    for threshold in expected_thresholds:
        table = result.undirected_edges_by_threshold[threshold].copy()
        if tuple(table.columns) != S2_UNDIRECTED_EDGE_COLUMNS:
            raise S2ContractError("S2 undirected edge schema mismatch at threshold %s" % threshold)
        tables["threshold_%s_undirected_edges.csv" % threshold] = table
    return tables


def _normalize_undirected_parity_frame(frame: pd.DataFrame) -> pd.DataFrame:
    """Normalize opaque node IDs before deterministic exact parity checks."""

    columns = list(S2_UNDIRECTED_EDGE_COLUMNS)
    work = frame.loc[:, columns].copy()
    for column in ("node_u", "node_v"):
        if work[column].isna().any():
            raise S2ContractError("S2 parity edge IDs must not be missing: %s" % column)
        normalized = work[column].astype("string")
        if normalized.str.strip().eq("").any():
            raise S2ContractError("S2 parity edge IDs must not be empty: %s" % column)
        work[column] = normalized
    for column in ("weight", "directed_edge_count"):
        work[column] = _positive_integral_series(work, column)
    return work.sort_values(["node_u", "node_v"], kind="stable").reset_index(drop=True)


def assert_s2_threshold_one_matches_corrected_p0(
    result: S2WeightSensitivityResult,
    corrected_p0_root: str | Path = CORRECTED_P0_ROOT,
    *,
    float_tolerance: float = 1e-12,
) -> dict[str, Any]:
    """Compare a future threshold-1 result with dynamic corrected-P0 authority."""

    if 1 not in result.undirected_edges_by_threshold:
        raise S2ContractError("threshold 1 is required for canonical S2 parity")
    root = canonical_path(corrected_p0_root)
    if os.path.normcase(os.fspath(root)) != os.path.normcase(os.fspath(CORRECTED_P0_ROOT)):
        raise S2ContractError("S2 parity authority must be the official corrected P0 root (v3)")
    expected_edges = _normalize_undirected_parity_frame(
        pd.read_csv(root / "rq2c_undirected_view_edges.csv")
    )
    actual_edges = _normalize_undirected_parity_frame(
        result.undirected_edges_by_threshold[1]
    )
    pdt.assert_frame_equal(expected_edges, actual_edges, check_dtype=False, check_exact=True)

    expected_summary = json.loads((root / "rq2c_undirected_view_summary.json").read_text(encoding="utf-8"))
    row = result.sensitivity.loc[result.sensitivity["threshold"].eq(1)]
    if len(row) != 1:
        raise S2ContractError("S2 sensitivity has no unique threshold-1 row")
    actual_summary = row.iloc[0]
    for column in S2_SUMMARY_COLUMNS:
        if column not in expected_summary:
            continue
        expected = expected_summary[column]
        actual = actual_summary[column]
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            if not math.isclose(float(actual), float(expected), rel_tol=0.0, abs_tol=float_tolerance):
                raise S2ContractError("threshold-1 canonical metric mismatch: %s" % column)
        elif actual != expected:
            raise S2ContractError("threshold-1 canonical metric mismatch: %s" % column)
    return {
        "status": "PASS",
        "threshold": 1,
        "dynamic_edge_authority": str(root / "rq2c_undirected_view_edges.csv"),
        "dynamic_summary_authority": str(root / "rq2c_undirected_view_summary.json"),
        "float_tolerance": float_tolerance,
    }


def preflight_corrected_p0_sensitivity_inputs(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> dict[str, Any]:
    """Read only corrected-P0 metadata and headers for S2/S3 readiness."""

    config = load_config(config_path)
    provenance = validate_scaffold_provenance(config)
    root = canonical_path(provenance["corrected_p0_root"])
    required_files = {
        "s2_edges": root / "reference_quotient_cross_project_edges.csv",
        "node_registry": root / "reference_quotient_node_registry.csv",
        "analysis_seed_manifest": root / "analysis_seed_manifest_294.csv",
        "canonical_undirected_edges": root / "rq2c_undirected_view_edges.csv",
        "canonical_undirected_summary": root / "rq2c_undirected_view_summary.json",
        "canonical_lcc_edges": root / "rq2c_undirected_view_lcc_edges.csv",
        "canonical_communities": root / "rq2c_algorithmic_communities.csv",
    }
    for path in required_files.values():
        if not path.is_file():
            raise S2ContractError("corrected P0 preflight file is unavailable: %s" % path)
        if not path.is_relative_to(root):
            raise S2ContractError("corrected P0 preflight escaped corrected P0 root")
    edge_headers = pd.read_csv(required_files["s2_edges"], nrows=0).columns.tolist()
    node_headers = pd.read_csv(required_files["node_registry"], nrows=0).columns.tolist()
    seed_headers = pd.read_csv(required_files["analysis_seed_manifest"], nrows=0).columns.tolist()
    missing_edge = [column for column in S2_DIRECTED_EDGE_REQUIRED_COLUMNS if column not in edge_headers]
    missing_node = [column for column in S2_NODE_REQUIRED_COLUMNS if column not in node_headers]
    if missing_edge or missing_node or "repo_id" not in seed_headers:
        raise S2ContractError("corrected P0 sensitivity input headers are incomplete")
    return {
        "C3_7C_INPUT_PREFLIGHT": "PASS",
        "corrected_p0_manifest_status": provenance["corrected_p0_manifest_status"],
        "corrected_p0_config_sha256": provenance["corrected_p0_config_sha256"],
        "corrected_p0_manifest_sha256": sha256_file(provenance["corrected_p0_manifest"]),
        "corrected_p0_root": str(root),
        "s2_thresholds": list(validate_s2_thresholds(config["s2_directed_weight_thresholds"])),
        "random_seed": config["random_seed"],
        "brokerage_sample_size": config["brokerage_sample_size"],
        "required_files": {name: str(path) for name, path in required_files.items()},
        "headers_only": True,
        "corrected_data_s2_run": False,
        "corrected_data_s3_run": False,
        "network_corrected_data_run": 0,
        "event_rejoin_performed": False,
        "source_admission_status_vocabulary": list(SOURCE_ADMISSION_STATUSES),
    }
