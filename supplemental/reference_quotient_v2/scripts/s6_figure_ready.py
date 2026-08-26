"""Corrected v2 S6 figure-ready derivation and provenance contracts.

S6 only transforms already-authorized P0/S4/S5 tables.  Source resolution is
explicit and fail-closed; there is no historical fallback discovery.  The
default preflight reads metadata and headers only.  Full derivation and
serialization are future-stage operations and are exercised here only with
temporary test roots.
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional

import pandas as pd

from .manifest import validate_scaffold_provenance
from .paths import (
    CORRECTED_OUTPUTS_ROOT,
    CORRECTED_P0_ROOT,
    DEFAULT_CONFIG_PATH,
    PathGuardError,
    canonical_path,
    load_config,
)
from .s4_community_stability import S4_OUTPUT_CONTRACT
from .s5_brokerage_stability import S5_OUTPUT_CONTRACT
from .stage_io import (
    SerializedArtifact,
    StageReceipt,
    serialize_artifacts,
    write_stage_outputs,
)


class S6ContractError(ValueError):
    """Raised when the corrected S6 source or output contract is invalid."""


CORRECTED_P0 = "CORRECTED_P0"
CORRECTED_SUPPLEMENTAL_V2 = "CORRECTED_SUPPLEMENTAL_V2"
S6_MANIFEST_NAME = "figure_ready_manifest_v2.json"
S6_STAGE_NAME = "S6_figure_ready"

P0_SOURCE_FILES: tuple[str, ...] = (
    "rq1_referencing_entity_distribution.csv",
    "rq1_referenced_entity_distribution.csv",
    "rq1_event_type_distribution.csv",
    "rq1_project_age_cross_sectional_association.csv",
    "rq1_project_reference_profiles.csv",
    "rq2a_source_role_metrics.csv",
    "rq2b_target_role_metrics.csv",
    "rq3_subdomain_descriptive_comparison.csv",
    "rq3_kruskal_fdr_effect_sizes.csv",
    "reference_quotient_cross_project_edges.csv",
    "rq2c_algorithmic_communities.csv",
    "rq2c_undirected_view_summary.json",
    "rq2c_structural_brokerage_candidates.csv",
    "rq2c_structural_brokerage_top50.csv",
)

S6_STABLE_COPY_OUTPUTS: tuple[str, ...] = (
    "rq1_referencing_entity_distribution_plot.csv",
    "rq1_referenced_entity_distribution_plot.csv",
    "rq1_event_type_distribution_plot.csv",
    "rq1_project_age_cross_sectional_association_plot.csv",
    "rq2a_source_role_metrics_plot.csv",
    "rq2b_target_role_metrics_plot.csv",
    "rq3_subdomain_descriptive_comparison_plot.csv",
    "rq3_kruskal_fdr_effect_sizes_plot.csv",
)
S6_DERIVED_OUTPUTS: tuple[str, ...] = (
    "rq1_profile_quantiles.csv",
    "rq2a_source_role_quantiles.csv",
    "rq2a_source_role_ecdf_ccdf.csv",
    "rq2b_target_role_quantiles.csv",
    "edge_weight_ecdf_ccdf.csv",
    "edge_weight_quantiles.csv",
    "community_size_distribution.csv",
    "structural_summary.csv",
    "brokerage_plot.csv",
    "brokerage_top50_plot.csv",
    "louvain_stability_plot.csv",
    "brokerage_stability_plot.csv",
)
S6_OUTPUT_INVENTORY: tuple[str, ...] = S6_STABLE_COPY_OUTPUTS + S6_DERIVED_OUTPUTS
S6_DEPRECATED_OUTPUTS: tuple[str, ...] = (
    "structural_summary.json",
    "figure_ready_manifest.json",
    "figure_ready_manifest_v1_1.json",
)
S6_SOURCE_KEYS: tuple[str, ...] = tuple("p0/" + filename for filename in P0_SOURCE_FILES) + (
    "s4/louvain_stability_runs.csv",
    "s5/brokerage_stability_runs.csv",
)

PROFILE_QUANTILE_METRICS: tuple[str, ...] = (
    "self_reference_ratio",
    "external_reference_share",
    "non_project_reference_share",
    "unresolved_target_reference_records",
    "comment_reference_density",
    "project_age_years_at_2023_end",
)
SOURCE_QUANTILE_METRICS: tuple[str, ...] = (
    "out_degree",
    "out_strength",
    "seed_to_seed_weight",
    "seed_to_expanded_weight",
    "source_concentration_hhi",
    "top_target_weight_share",
)
TARGET_QUANTILE_METRICS: tuple[str, ...] = (
    "in_degree",
    "in_strength",
    "target_coverage",
    "cumulative_weight_share",
)


@dataclass(frozen=True)
class S6SourceArtifact:
    key: str
    path: Path
    authority_class: str
    root: Path
    version: str

    def record(self) -> dict[str, Any]:
        if not self.path.is_file():
            raise S6ContractError("S6 source does not exist: %s" % self.path)
        return {
            "path": str(self.path).replace(os.sep, "/"),
            "sha256": sha256_file(self.path),
            "authority_class": self.authority_class,
            "root": str(self.root).replace(os.sep, "/"),
            "version": self.version,
        }


@dataclass(frozen=True)
class S6SourceBundle:
    sources: Mapping[str, S6SourceArtifact]
    corrected_p0_root: Path
    corrected_supplemental_root: Path

    def source(self, key: str) -> S6SourceArtifact:
        try:
            return self.sources[key]
        except KeyError as exc:
            raise S6ContractError("S6 source key is undeclared: %s" % key) from exc


@dataclass(frozen=True)
class S6FigureReadyBundle:
    tables: Mapping[str, pd.DataFrame]
    output_sources: Mapping[str, tuple[S6SourceArtifact, ...]]
    transformations: Mapping[str, str]


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_root_pair(p0_root: Path, supplemental_root: Path, allow_fixture_roots: bool) -> None:
    if not allow_fixture_roots and p0_root != canonical_path(CORRECTED_P0_ROOT):
        raise S6ContractError("S6 P0 authority must be corrected P0 v2")
    if not allow_fixture_roots and supplemental_root != canonical_path(CORRECTED_OUTPUTS_ROOT):
        raise S6ContractError("S6 supplemental authority must be corrected v2 outputs")
    forbidden_fragments = (
        "reference_quotient_p0_frozen",
        "reference_quotient_v1",
        "v1_1_completion",
        "v1_2_s3_reproducibility_patch",
    )
    for root in (p0_root, supplemental_root):
        lowered = str(root).replace("\\", "/").lower()
        if any(fragment in lowered for fragment in forbidden_fragments):
            raise S6ContractError("historical root cannot be an S6 authority: %s" % root)


def resolve_s6_source_bundle(
    *,
    corrected_p0_root: str | Path = CORRECTED_P0_ROOT,
    corrected_supplemental_root: str | Path = CORRECTED_OUTPUTS_ROOT,
    allow_fixture_roots: bool = False,
) -> S6SourceBundle:
    """Resolve the explicit corrected P0 and future corrected v2 source map."""

    p0_root = canonical_path(corrected_p0_root)
    supplemental_root = canonical_path(corrected_supplemental_root)
    _validate_root_pair(p0_root, supplemental_root, allow_fixture_roots)
    sources: dict[str, S6SourceArtifact] = {}
    for filename in P0_SOURCE_FILES:
        key = "p0/" + filename
        sources[key] = S6SourceArtifact(
            key=key,
            path=p0_root / filename,
            authority_class=CORRECTED_P0,
            root=p0_root,
            version="corrected_p0_v2",
        )
    s4_key = "s4/louvain_stability_runs.csv"
    sources[s4_key] = S6SourceArtifact(
        key=s4_key,
        path=supplemental_root / "S4_community_stability" / "louvain_stability_runs.csv",
        authority_class=CORRECTED_SUPPLEMENTAL_V2,
        root=supplemental_root,
        version="corrected_supplemental_v2",
    )
    s5_key = "s5/brokerage_stability_runs.csv"
    sources[s5_key] = S6SourceArtifact(
        key=s5_key,
        path=supplemental_root / "S5_brokerage_stability" / "brokerage_stability_runs.csv",
        authority_class=CORRECTED_SUPPLEMENTAL_V2,
        root=supplemental_root,
        version="corrected_supplemental_v2",
    )
    bundle = S6SourceBundle(
        sources=sources,
        corrected_p0_root=p0_root,
        corrected_supplemental_root=supplemental_root,
    )
    validate_s6_source_bundle(bundle, require_exists=False)
    return bundle


def validate_s6_source_bundle(bundle: S6SourceBundle, *, require_exists: bool) -> None:
    """Fail closed on undeclared, historical, or cross-root S6 sources."""

    if not isinstance(bundle, S6SourceBundle):
        raise S6ContractError("S6 source bundle has an invalid type")
    _validate_root_pair(bundle.corrected_p0_root, bundle.corrected_supplemental_root, allow_fixture_roots=True)
    expected_classes = {CORRECTED_P0, CORRECTED_SUPPLEMENTAL_V2}
    if set(bundle.sources) != set(S6_SOURCE_KEYS):
        raise S6ContractError("S6 source map does not match the declared source inventory")
    for key, source in bundle.sources.items():
        if key != source.key or source.authority_class not in expected_classes:
            raise S6ContractError("S6 source has an invalid authority declaration: %s" % key)
        root = bundle.corrected_p0_root if source.authority_class == CORRECTED_P0 else bundle.corrected_supplemental_root
        if source.root != root or not source.path.is_relative_to(root):
            raise S6ContractError("S6 source crosses its declared root: %s" % source.path)
        if key.startswith("p0/"):
            expected_path = root / key.removeprefix("p0/")
            expected_version = "corrected_p0_v2"
        elif key == "s4/louvain_stability_runs.csv":
            expected_path = root / "S4_community_stability" / "louvain_stability_runs.csv"
            expected_version = "corrected_supplemental_v2"
        else:
            expected_path = root / "S5_brokerage_stability" / "brokerage_stability_runs.csv"
            expected_version = "corrected_supplemental_v2"
        if source.path != expected_path:
            raise S6ContractError("S6 source path does not match declared key: %s" % key)
        if source.version != expected_version:
            raise S6ContractError("S6 source version does not match declared key: %s" % key)
        lowered = str(source.path).replace("\\", "/").lower()
        if any(fragment in lowered for fragment in ("reference_quotient_p0_frozen", "reference_quotient_v1", "v1_1_completion", "v1_2_s3_reproducibility_patch")):
            raise S6ContractError("historical source cannot be used for S6 derivation: %s" % source.path)
        if require_exists and not source.path.is_file():
            raise S6ContractError("required S6 source is unavailable: %s" % source.path)


def _source_key(filename: str) -> str:
    return "p0/" + filename


def _require_columns(frame: pd.DataFrame, columns: Iterable[str], label: str) -> None:
    missing = [column for column in columns if column not in frame]
    if missing:
        raise S6ContractError("%s is missing columns: %s" % (label, ", ".join(missing)))


def quantiles(values: pd.Series, metric: str) -> pd.DataFrame:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return pd.DataFrame(columns=["metric", "quantile", "value"])
    points = (("min", 0.0), ("q25", 0.25), ("median", 0.5), ("q75", 0.75), ("max", 1.0))
    return pd.DataFrame(
        [{"metric": metric, "quantile": name, "value": float(numeric.quantile(point))} for name, point in points],
        columns=("metric", "quantile", "value"),
    )


def ecdf(values: pd.Series, metric: str) -> pd.DataFrame:
    numeric = pd.to_numeric(values, errors="coerce").dropna().sort_values().reset_index(drop=True)
    if numeric.empty:
        return pd.DataFrame(columns=["metric", "rank", "value", "cdf", "ccdf"])
    count = len(numeric)
    ranks = range(1, count + 1)
    return pd.DataFrame(
        {
            "metric": metric,
            "rank": ranks,
            "value": numeric,
            "cdf": [rank / count for rank in ranks],
            "ccdf": [(count - rank + 1) / count for rank in ranks],
        },
        columns=("metric", "rank", "value", "cdf", "ccdf"),
    )


def _concat_metric_tables(frame: pd.DataFrame, metrics: Iterable[str], function: Any) -> pd.DataFrame:
    _require_columns(frame, metrics, "S6 metric source")
    return pd.concat([function(frame[metric], metric) for metric in metrics], ignore_index=True)


def _community_size_distribution(frame: pd.DataFrame) -> pd.DataFrame:
    _require_columns(frame, ("project_id", "community_id", "community_size"), "canonical communities")
    labels = pd.to_numeric(frame["community_id"], errors="coerce")
    recorded = pd.to_numeric(frame["community_size"], errors="coerce")
    if labels.isna().any() or (~labels.eq(labels.round())).any() or recorded.isna().any() or (~recorded.eq(recorded.round())).any():
        raise S6ContractError("canonical community sizes or labels are invalid")
    work = frame.assign(_community_id=labels.astype("int64"), _recorded_size=recorded.astype("int64"))
    observed = work.groupby("_community_id", sort=True).size()
    declared = work.groupby("_community_id", sort=True)["_recorded_size"].first()
    if any(int(observed[label]) != int(declared[label]) for label in observed.index):
        raise S6ContractError("canonical community_size does not close")
    return pd.DataFrame(
        {"community_id": observed.index.astype("int64"), "community_size": observed.astype("int64").values},
        columns=("community_id", "community_size"),
    )


def _structural_summary(frame: Mapping[str, Any]) -> pd.DataFrame:
    if not isinstance(frame, Mapping) or not frame:
        raise S6ContractError("canonical structural summary must be a non-empty object")
    if any(isinstance(value, (dict, list, tuple, set)) for value in frame.values()):
        raise S6ContractError("structural summary contains a non-scalar value")
    columns = tuple(sorted(frame))
    return pd.DataFrame([[frame[column] for column in columns]], columns=columns)


def build_s6_figure_ready_bundle(source_bundle: S6SourceBundle) -> S6FigureReadyBundle:
    """Load and transform the explicit source map into future S6 tables."""

    validate_s6_source_bundle(source_bundle, require_exists=True)
    def read_p0(filename: str) -> pd.DataFrame:
        return pd.read_csv(source_bundle.source(_source_key(filename)).path)

    tables: dict[str, pd.DataFrame] = {}
    output_sources: dict[str, tuple[S6SourceArtifact, ...]] = {}
    transformations: dict[str, str] = {}

    stable_sources = (
        "rq1_referencing_entity_distribution.csv",
        "rq1_referenced_entity_distribution.csv",
        "rq1_event_type_distribution.csv",
        "rq1_project_age_cross_sectional_association.csv",
        "rq2a_source_role_metrics.csv",
        "rq2b_target_role_metrics.csv",
        "rq3_subdomain_descriptive_comparison.csv",
        "rq3_kruskal_fdr_effect_sizes.csv",
    )
    for filename in stable_sources:
        output = filename[:-4] + "_plot.csv"
        tables[output] = read_p0(filename)
        output_sources[output] = (source_bundle.source(_source_key(filename)),)
        transformations[output] = "stable_copy_for_plotting"

    profiles_name = "rq1_project_reference_profiles.csv"
    profiles = read_p0(profiles_name)
    output = "rq1_profile_quantiles.csv"
    tables[output] = _concat_metric_tables(profiles, PROFILE_QUANTILE_METRICS, quantiles)
    output_sources[output] = (source_bundle.source(_source_key(profiles_name)),)
    transformations[output] = "project_profile_metric_quantiles"

    source_name = "rq2a_source_role_metrics.csv"
    source_frame = read_p0(source_name)
    output = "rq2a_source_role_quantiles.csv"
    tables[output] = _concat_metric_tables(source_frame, SOURCE_QUANTILE_METRICS, quantiles)
    output_sources[output] = (source_bundle.source(_source_key(source_name)),)
    transformations[output] = "source_role_quantiles"
    output = "rq2a_source_role_ecdf_ccdf.csv"
    tables[output] = _concat_metric_tables(source_frame, SOURCE_QUANTILE_METRICS, ecdf)
    output_sources[output] = (source_bundle.source(_source_key(source_name)),)
    transformations[output] = "source_role_ecdf_ccdf"

    target_name = "rq2b_target_role_metrics.csv"
    target_frame = read_p0(target_name)
    output = "rq2b_target_role_quantiles.csv"
    tables[output] = _concat_metric_tables(target_frame, TARGET_QUANTILE_METRICS, quantiles)
    output_sources[output] = (source_bundle.source(_source_key(target_name)),)
    transformations[output] = "target_role_quantiles"

    edge_name = "reference_quotient_cross_project_edges.csv"
    edge_frame = read_p0(edge_name)
    _require_columns(edge_frame, ("weight",), edge_name)
    output = "edge_weight_ecdf_ccdf.csv"
    tables[output] = ecdf(edge_frame["weight"], "directed_cross_project_edge_weight")
    output_sources[output] = (source_bundle.source(_source_key(edge_name)),)
    transformations[output] = "directed_cross_project_edge_weight_ecdf_ccdf"
    output = "edge_weight_quantiles.csv"
    tables[output] = quantiles(edge_frame["weight"], "directed_cross_project_edge_weight")
    output_sources[output] = (source_bundle.source(_source_key(edge_name)),)
    transformations[output] = "directed_cross_project_edge_weight_quantiles"

    community_name = "rq2c_algorithmic_communities.csv"
    community_frame = read_p0(community_name)
    output = "community_size_distribution.csv"
    tables[output] = _community_size_distribution(community_frame)
    output_sources[output] = (source_bundle.source(_source_key(community_name)),)
    transformations[output] = "community_size_distribution"

    summary_name = "rq2c_undirected_view_summary.json"
    summary_source = source_bundle.source(_source_key(summary_name))
    summary = json.loads(summary_source.path.read_text(encoding="utf-8"))
    output = "structural_summary.csv"
    tables[output] = _structural_summary(summary)
    output_sources[output] = (summary_source,)
    transformations[output] = "corrected_p0_summary_json_to_csv"

    brokerage_name = "rq2c_structural_brokerage_candidates.csv"
    output = "brokerage_plot.csv"
    tables[output] = read_p0(brokerage_name)
    output_sources[output] = (source_bundle.source(_source_key(brokerage_name)),)
    transformations[output] = "stable_brokerage_plot_table"
    brokerage_top_name = "rq2c_structural_brokerage_top50.csv"
    output = "brokerage_top50_plot.csv"
    tables[output] = read_p0(brokerage_top_name)
    output_sources[output] = (source_bundle.source(_source_key(brokerage_top_name)),)
    transformations[output] = "stable_brokerage_top50_plot_table"

    s4_source = source_bundle.source("s4/louvain_stability_runs.csv")
    output = "louvain_stability_plot.csv"
    tables[output] = pd.read_csv(s4_source.path)
    output_sources[output] = (s4_source,)
    transformations[output] = "supplemental_stability_plot_table"
    s5_source = source_bundle.source("s5/brokerage_stability_runs.csv")
    output = "brokerage_stability_plot.csv"
    tables[output] = pd.read_csv(s5_source.path)
    output_sources[output] = (s5_source,)
    transformations[output] = "supplemental_stability_plot_table"

    if tuple(tables) != S6_OUTPUT_INVENTORY:
        raise S6ContractError("S6 output inventory does not match the frozen derivation inventory")
    if any(name.endswith(".json") for name in tables):
        raise S6ContractError("S6 scientific output contract contains a JSON data artifact")
    return S6FigureReadyBundle(tables=tables, output_sources=output_sources, transformations=transformations)


def _manifest_entry(output: SerializedArtifact, source_artifacts: tuple[S6SourceArtifact, ...], transformation: str) -> dict[str, Any]:
    return {
        "output": output.name,
        "output_sha256": output.sha256,
        "output_bytes": output.bytes,
        "row_count": output.row_count,
        "transformation": transformation,
        "source_artifacts": [source.record() for source in source_artifacts],
    }


def build_figure_ready_manifest_v2(
    source_bundle: S6SourceBundle | S6FigureReadyBundle,
    serialized_outputs: Mapping[str, SerializedArtifact] | Iterable[SerializedArtifact],
) -> dict[str, Any]:
    """Build the future S6 manifest from deterministic output payloads."""

    if isinstance(source_bundle, S6SourceBundle):
        source_bundle = build_s6_figure_ready_bundle(source_bundle)
    return build_s6_manifest_for_bundle(source_bundle, serialized_outputs)


def build_s6_manifest_for_bundle(
    bundle: S6FigureReadyBundle,
    serialized_outputs: Mapping[str, SerializedArtifact] | Iterable[SerializedArtifact],
) -> dict[str, Any]:
    if isinstance(serialized_outputs, Mapping):
        artifacts = dict(serialized_outputs)
    else:
        artifacts = {artifact.name: artifact for artifact in serialized_outputs}
    if set(artifacts) != set(S6_OUTPUT_INVENTORY):
        raise S6ContractError("S6 manifest output set is incomplete")
    entries = [
        _manifest_entry(artifacts[output], bundle.output_sources[output], bundle.transformations[output])
        for output in S6_OUTPUT_INVENTORY
    ]
    return {
        "schema_version": "figure_ready_manifest_v2",
        "package_version": "corrected_supplemental_v2",
        "classification": "FIGURE_READY_DERIVATION",
        "status": "STAGE_PACKAGE_PENDING",
        "stage": S6_STAGE_NAME,
        "entries": entries,
        "authority_roots": {
            CORRECTED_P0: str(bundle.output_sources[S6_OUTPUT_INVENTORY[0]][0].root).replace(os.sep, "/"),
            CORRECTED_SUPPLEMENTAL_V2: str(bundle.output_sources["louvain_stability_plot.csv"][0].root).replace(os.sep, "/"),
        },
        "deprecated_outputs_excluded": list(S6_DEPRECATED_OUTPUTS),
        "manifest_self_hash_not_embedded": True,
    }


build_s6_figure_ready_manifest = build_figure_ready_manifest_v2


def serialize_s6_figure_ready_bundle(
    source_bundle: S6SourceBundle,
    output_root: str | Path,
    *,
    implementation_commit: str = "",
    parameters: Optional[Mapping[str, Any]] = None,
    versions: Optional[Mapping[str, str]] = None,
    completed_at: Optional[str] = None,
    allow_external_test_root: bool = False,
) -> tuple[S6FigureReadyBundle, StageReceipt, dict[str, Any]]:
    """Future S6 writer; tests must pass a temporary output root."""

    bundle = build_s6_figure_ready_bundle(source_bundle)
    data_payloads = serialize_artifacts(bundle.tables)
    payload_map = {artifact.name: artifact for artifact in data_payloads}
    manifest = build_s6_manifest_for_bundle(bundle, payload_map)
    manifest_payload = serialize_artifacts({S6_MANIFEST_NAME: manifest})[0]
    all_payloads = dict(bundle.tables)
    all_payloads[S6_MANIFEST_NAME] = manifest
    receipt = write_stage_outputs(
        output_root,
        "S6",
        all_payloads,
        implementation_commit=implementation_commit,
        input_artifacts=tuple(source.record() for source in _unique_sources(bundle)),
        parameters=parameters,
        versions=versions,
        completed_at=completed_at,
        allow_external_test_root=allow_external_test_root,
    )
    # The writer serializes deterministically; assert the manifest payload was
    # the same payload used to compute its own output records.
    if manifest_payload.sha256 != sha256_bytes((canonical_path(output_root) / S6_STAGE_NAME / S6_MANIFEST_NAME).read_bytes()):
        raise S6ContractError("serialized S6 manifest payload changed during write")
    return bundle, receipt, manifest


def _unique_sources(bundle: S6FigureReadyBundle) -> tuple[S6SourceArtifact, ...]:
    result: list[S6SourceArtifact] = []
    seen: set[str] = set()
    for output in S6_OUTPUT_INVENTORY:
        for source in bundle.output_sources[output]:
            identifier = str(source.path)
            if identifier not in seen:
                seen.add(identifier)
                result.append(source)
    return tuple(result)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _load_manifest(value: str | Path | Mapping[str, Any]) -> tuple[dict[str, Any], Path]:
    if isinstance(value, Mapping):
        return dict(value), canonical_path(Path.cwd())
    path = canonical_path(value)
    return json.loads(path.read_text(encoding="utf-8")), path.parent


def validate_s6_manifest_sha_closure(
    manifest: str | Path | Mapping[str, Any],
    *,
    manifest_directory: str | Path | None = None,
) -> dict[str, Any]:
    """Verify every S6 source SHA, output SHA, byte count and row count."""

    value, inferred_directory = _load_manifest(manifest)
    base = canonical_path(manifest_directory) if manifest_directory is not None else inferred_directory
    if value.get("schema_version") != "figure_ready_manifest_v2":
        raise S6ContractError("invalid S6 figure-ready manifest schema")
    entries = value.get("entries")
    if not isinstance(entries, list) or len(entries) != len(S6_OUTPUT_INVENTORY):
        raise S6ContractError("S6 manifest entry count does not match output inventory")
    seen_outputs: set[str] = set()
    source_count = 0
    authority_roots = value.get("authority_roots")
    if not isinstance(authority_roots, Mapping) or set(authority_roots) != {CORRECTED_P0, CORRECTED_SUPPLEMENTAL_V2}:
        raise S6ContractError("S6 manifest authority roots are incomplete")
    resolved_authority_roots = {key: canonical_path(authority_roots[key]) for key in authority_roots}
    for entry in entries:
        required = ("output", "output_sha256", "output_bytes", "row_count", "transformation", "source_artifacts")
        if any(key not in entry for key in required):
            raise S6ContractError("S6 manifest entry is incomplete")
        output = entry["output"]
        if output not in S6_OUTPUT_INVENTORY or output in seen_outputs:
            raise S6ContractError("S6 manifest output is undeclared or duplicated: %s" % output)
        seen_outputs.add(output)
        output_path = canonical_path(output, base=base)
        if not output_path.is_relative_to(base) or not output_path.is_file():
            raise S6ContractError("S6 recorded output is unavailable: %s" % output_path)
        if sha256_file(output_path) != entry["output_sha256"]:
            raise S6ContractError("S6 output SHA mismatch: %s" % output)
        if output_path.stat().st_size != int(entry["output_bytes"]):
            raise S6ContractError("S6 output byte count mismatch: %s" % output)
        if entry["row_count"] is None or int(entry["row_count"]) != len(pd.read_csv(output_path)):
            raise S6ContractError("S6 output row count mismatch: %s" % output)
        sources = entry["source_artifacts"]
        if not isinstance(sources, list) or not sources:
            raise S6ContractError("S6 manifest source artifact list is empty: %s" % output)
        for source in sources:
            for key in ("path", "sha256", "authority_class", "root", "version"):
                if key not in source:
                    raise S6ContractError("S6 source record is incomplete")
            source_path = canonical_path(source["path"])
            source_root = canonical_path(source["root"])
            if source_path == source_root or not source_path.is_relative_to(source_root):
                raise S6ContractError("S6 source record crosses its declared root")
            if source["authority_class"] not in (CORRECTED_P0, CORRECTED_SUPPLEMENTAL_V2):
                raise S6ContractError("S6 source has invalid authority class")
            if source_root != resolved_authority_roots[source["authority_class"]]:
                raise S6ContractError("S6 source root does not match its authority class")
            expected_version = "corrected_p0_v2" if source["authority_class"] == CORRECTED_P0 else "corrected_supplemental_v2"
            if source["version"] != expected_version:
                raise S6ContractError("S6 source version does not match its authority class")
            if "reference_quotient_v1" in str(source_path).replace("\\", "/"):
                raise S6ContractError("historical S6 source is forbidden")
            if not source_path.is_file() or sha256_file(source_path) != source["sha256"]:
                raise S6ContractError("S6 source SHA mismatch: %s" % source_path)
            source_count += 1
    if seen_outputs != set(S6_OUTPUT_INVENTORY):
        raise S6ContractError("S6 manifest output inventory is incomplete")
    return {"status": "PASS", "entries_checked": len(entries), "source_records_checked": source_count}


def preflight_corrected_p0_s6_inputs(config_path: str | Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """Run only corrected-P0 metadata/header/source-map S6 preflight."""

    config = load_config(config_path)
    try:
        provenance = validate_scaffold_provenance(config)
    except PathGuardError as exc:
        raise S6ContractError(str(exc)) from exc
    source_bundle = resolve_s6_source_bundle()
    p0_sources = [source for source in source_bundle.sources.values() if source.authority_class == CORRECTED_P0]
    missing = [str(source.path) for source in p0_sources if not source.path.is_file()]
    if missing:
        raise S6ContractError("corrected P0 S6 source is unavailable: %s" % ", ".join(missing))
    headers: dict[str, list[str]] = {}
    for source in p0_sources:
        if source.path.suffix.lower() == ".csv":
            headers[source.key] = pd.read_csv(source.path, nrows=0).columns.tolist()
            if not headers[source.key]:
                raise S6ContractError("corrected P0 S6 source has no header: %s" % source.path)
    summary_source = source_bundle.source(_source_key("rq2c_undirected_view_summary.json"))
    summary = json.loads(summary_source.path.read_text(encoding="utf-8"))
    if not isinstance(summary, dict) or not {"random_seed", "brokerage_sample_size", "modularity"}.issubset(summary):
        raise S6ContractError("corrected P0 structural summary schema is incomplete")
    if set(S4_OUTPUT_CONTRACT) != {
        "louvain_stability_runs.csv",
        "louvain_stability_pairwise.csv",
        "louvain_stability_summary.json",
    }:
        raise S6ContractError("S4 output contract is not the frozen v2 contract")
    if set(S5_OUTPUT_CONTRACT) != {
        "brokerage_rank_stability.csv",
        "brokerage_stability_runs.csv",
        "brokerage_topk_inclusion_frequency.csv",
        "brokerage_stability_summary.json",
    }:
        raise S6ContractError("S5 output contract is not the frozen v2 contract")
    return {
        "C3_7E_INPUT_PREFLIGHT": "PASS",
        "corrected_p0_manifest_status": provenance["corrected_p0_manifest_status"],
        "corrected_p0_manifest_sha256": sha256_file(provenance["corrected_p0_manifest"]),
        "corrected_p0_config_sha256": provenance["corrected_p0_config_sha256"],
        "corrected_p0_root": str(source_bundle.corrected_p0_root),
        "required_p0_source_count": len(p0_sources),
        "required_p0_headers": headers,
        "future_s4_source": str(source_bundle.source("s4/louvain_stability_runs.csv").path),
        "future_s5_source": str(source_bundle.source("s5/brokerage_stability_runs.csv").path),
        "future_s4_s5_sources_resolved_under_v2": True,
        "historical_fallback_present": False,
        "s6_output_inventory": list(S6_OUTPUT_INVENTORY),
        "deprecated_outputs_excluded": list(S6_DEPRECATED_OUTPUTS),
        "headers_only": True,
        "corrected_data_s6_run": False,
        "network_corrected_data_run": 0,
        "real_output_root_created": False,
    }
