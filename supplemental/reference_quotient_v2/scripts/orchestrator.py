"""Fail-closed, one-stage-at-a-time production orchestration for C4."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Any, Callable, Mapping, Optional

from .historical_immutability import CLEAN_DEFAULT_BASELINE_PATH, compare_historical_immutability
from .input_hashes import (
    EXPECTED_P0_CONFIG_SHA256,
    EXPECTED_P0_MANIFEST_SHA256,
    verify_corrected_input_hash_closure,
)
from .manifest import sha256_file, validate_scaffold_provenance
from .paths import DEFAULT_CONFIG_PATH, canonical_path, load_config
from .stage_io import (
    CORRECTED_AGGREGATE,
    CORRECTED_AGGREGATE_VERSION,
    CORRECTED_P0,
    CORRECTED_P0_VERSION,
    CORRECTED_SUPPLEMENTAL_VERSION,
    STAGE_DIRECTORY_NAMES,
    STAGE_RECEIPT_NAME,
    StageIOError,
    StageReceiptContractError,
    AuthorityRoots,
    production_authority_roots,
    stage_output_inventory,
    validate_stage_receipt,
    write_stage_outputs,
)


class OrchestrationError(ValueError):
    """Raised when a C4 stage cannot be authorized or closed."""


STAGE_PHASES = {canonical: "C4-%s" % short for short, canonical in STAGE_DIRECTORY_NAMES.items()}
AUTHORIZED_BRANCH = "ch5-refq-repository-identity-correction-v1"
STAGE_DEPENDENCIES = {
    "S1_evidence_universe": (),
    "S2_weight_sensitivity": ("S1_evidence_universe",),
    "S3_observation_sensitivity": ("S1_evidence_universe", "S2_weight_sensitivity"),
    "S4_community_stability": ("S1_evidence_universe", "S2_weight_sensitivity", "S3_observation_sensitivity"),
    "S5_brokerage_stability": ("S1_evidence_universe", "S2_weight_sensitivity", "S3_observation_sensitivity", "S4_community_stability"),
    "S6_figure_ready": ("S1_evidence_universe", "S2_weight_sensitivity", "S3_observation_sensitivity", "S4_community_stability", "S5_brokerage_stability"),
}


def _git_head() -> str:
    import subprocess

    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=str(Path(__file__).resolve().parents[3]),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def _git_value(*arguments: str) -> str:
    import subprocess

    result = subprocess.run(
        ["git", *arguments],
        cwd=str(Path(__file__).resolve().parents[3]),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def _implementation_diff(expected_commit: str) -> tuple[str, ...]:
    import subprocess

    result = subprocess.run(
        [
            "git", "diff", "--name-only", expected_commit, "--",
            "supplemental/reference_quotient_v2/scripts",
            "supplemental/reference_quotient_v2/configs",
        ],
        cwd=str(Path(__file__).resolve().parents[3]),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return tuple(line.strip() for line in result.stdout.splitlines() if line.strip())


def _is_ancestor(commit: str) -> bool:
    import subprocess

    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit, "HEAD"],
        cwd=str(Path(__file__).resolve().parents[3]),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.returncode == 0


def _canonical_stage(stage: str) -> str:
    if stage in STAGE_DIRECTORY_NAMES:
        return STAGE_DIRECTORY_NAMES[stage]
    if stage in STAGE_DIRECTORY_NAMES.values():
        return stage
    raise OrchestrationError("stage must be one of S1-S6")


def authorize_stage(
    stage: str,
    *,
    authorization_phase: str,
    expected_implementation_commit: str,
) -> str:
    canonical = _canonical_stage(stage)
    if _git_value("branch", "--show-current") != AUTHORIZED_BRANCH:
        raise OrchestrationError("current branch is not the authorized Chapter 5 correction branch")
    if _git_value("status", "--porcelain"):
        raise OrchestrationError("production stage execution requires a clean worktree")
    if authorization_phase != STAGE_PHASES[canonical]:
        raise OrchestrationError("authorization phase does not match requested stage")
    if not isinstance(expected_implementation_commit, str) or len(expected_implementation_commit) != 40:
        raise OrchestrationError("expected implementation commit must be a full SHA-1")
    if not _is_ancestor(expected_implementation_commit):
        raise OrchestrationError("expected implementation commit is not an ancestor of the execution HEAD")
    changed = _implementation_diff(expected_implementation_commit)
    if changed:
        raise OrchestrationError(
            "scientific/integration implementation differs from the frozen implementation commit: %s"
            % ", ".join(changed)
        )
    return canonical


def _input_record(path: str | Path, authority_class: str, root: str | Path, version: str) -> dict[str, Any]:
    resolved = canonical_path(path)
    authority_root = canonical_path(root)
    if not resolved.is_file() or not resolved.is_relative_to(authority_root):
        raise OrchestrationError("required input is unavailable or outside authority root: %s" % resolved)
    return {
        "path": str(resolved).replace("\\", "/"),
        "sha256": sha256_file(resolved),
        "authority_class": authority_class,
        "root": str(authority_root).replace("\\", "/"),
        "version": version,
    }


def _s1_input_records(config: Mapping[str, Any]) -> tuple[dict[str, Any], ...]:
    from .s1_adapter import S1SourceObservationAdapter

    adapter = S1SourceObservationAdapter.from_config(config)
    root = canonical_path(config["corrected_aggregate_root"])
    return tuple(
        _input_record(context.evidence_path, CORRECTED_AGGREGATE, root, CORRECTED_AGGREGATE_VERSION)
        for context in adapter._partition_contexts.values()
    )


def _p0_records(config: Mapping[str, Any], filenames: tuple[str, ...]) -> tuple[dict[str, Any], ...]:
    root = canonical_path(config["corrected_p0_root"])
    return tuple(_input_record(root / filename, CORRECTED_P0, root, CORRECTED_P0_VERSION) for filename in filenames)


def _stage_parameters(stage: str, config: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "stage": stage,
        "corrected_data": True,
        "p0_authority_version": CORRECTED_P0_VERSION,
        "p0_manifest_sha256": EXPECTED_P0_MANIFEST_SHA256,
        "p0_config_sha256": EXPECTED_P0_CONFIG_SHA256,
        "clean_output_root": str(canonical_path(config["corrected_output_root"])),
        "supplemental_authority_version": CORRECTED_SUPPLEMENTAL_VERSION,
        "scientific_logic_change_count": 0,
    }


def _validate_upstream_receipts(
    output_root: Path,
    stage: str,
    config: Mapping[str, Any],
    *,
    authority_roots: AuthorityRoots | None = None,
) -> dict[str, Any]:
    checked: list[str] = []
    for dependency in STAGE_DEPENDENCIES[stage]:
        receipt_path = output_root / dependency / STAGE_RECEIPT_NAME
        if not receipt_path.is_file():
            raise OrchestrationError("upstream durable receipt is missing: %s" % dependency)
        try:
            receipt = __import__("json").loads(receipt_path.read_text(encoding="utf-8"))
            validate_stage_receipt(
                receipt, dependency, output_root=output_root,
                expected_output_root=output_root, authority_roots=authority_roots,
                enforce_contract=True,
            )
        except (OSError, ValueError, StageReceiptContractError) as exc:
            raise OrchestrationError("upstream receipt blocks %s: %s" % (stage, dependency)) from exc
        checked.append(dependency)
    return {"status": "PASS", "checked": checked}


def _run_scientific_stage(stage: str, config: Mapping[str, Any], output_root: Path, implementation_commit: str):
    """Dispatch exactly one stage; downstream stages are never called here."""

    if stage == "S1_evidence_universe":
        from .s1_adapter import S1SourceObservationAdapter
        from .s1_streaming import build_future_s1_streaming_output_tables, run_s1_streaming

        adapter = S1SourceObservationAdapter.from_config(config)
        paths = [context.evidence_path for context in adapter._partition_contexts.values()]
        fd, raw_registry = tempfile.mkstemp(prefix="refq_s1_registry_", suffix=".sqlite")
        os.close(fd)
        Path(raw_registry).unlink()
        try:
            result = run_s1_streaming(adapter, paths, raw_registry, chunksize=int(config.get("csv_chunk_size", 100000)))
            artifacts = build_future_s1_streaming_output_tables(result)
        finally:
            Path(raw_registry).unlink(missing_ok=True)
        return write_stage_outputs(
            output_root,
            stage,
            artifacts,
            implementation_commit=implementation_commit,
            input_artifacts=_s1_input_records(config),
            parameters=_stage_parameters("S1", config),
        )
    if stage == "S2_weight_sensitivity":
        from .s2_weight_sensitivity import (
            assert_s2_threshold_one_matches_corrected_p0,
            build_future_s2_output_tables,
            compute_s2_weight_sensitivity,
            load_corrected_p0_s2_inputs,
        )

        edges, registry = load_corrected_p0_s2_inputs()
        result = compute_s2_weight_sensitivity(
            edges, registry,
            thresholds=config["s2_directed_weight_thresholds"],
            random_seed=config["random_seed"],
            brokerage_sample_size=config["brokerage_sample_size"],
        )
        assert_s2_threshold_one_matches_corrected_p0(result)
        return write_stage_outputs(
            output_root, stage, build_future_s2_output_tables(result),
            implementation_commit=implementation_commit,
            input_artifacts=_p0_records(config, ("reference_quotient_cross_project_edges.csv", "reference_quotient_node_registry.csv")),
            parameters=_stage_parameters("S2", config),
        )
    if stage == "S3_observation_sensitivity":
        from .s3_observation_sensitivity import (
            assert_s3_canonical_view_matches_corrected_p0,
            build_future_s3_output_tables,
            compute_s3_observation_sensitivity,
            load_corrected_p0_s3_inputs,
        )

        edges, registry, seeds = load_corrected_p0_s3_inputs()
        result = compute_s3_observation_sensitivity(
            edges, registry, seeds,
            random_seed=config["random_seed"],
            brokerage_sample_size=config["brokerage_sample_size"],
        )
        assert_s3_canonical_view_matches_corrected_p0(result)
        return write_stage_outputs(
            output_root, stage, build_future_s3_output_tables(result),
            implementation_commit=implementation_commit,
            input_artifacts=_p0_records(config, ("reference_quotient_cross_project_edges.csv", "reference_quotient_node_registry.csv", "analysis_seed_manifest_294.csv")),
            parameters=_stage_parameters("S3", config),
        )
    if stage == "S4_community_stability":
        from .s4_community_stability import assert_s4_canonical_seed_matches_corrected_p0, build_future_s4_output_tables, compute_s4_community_stability, s4_production_seeds
        from .s45_canonical_graph import load_corrected_p0_s45_authority

        authority = load_corrected_p0_s45_authority()
        result = compute_s4_community_stability(
            authority.lcc, authority.canonical_partition,
            seeds=s4_production_seeds(config),
            canonical_seed=config["random_seed"],
            ari_alert_threshold=config["s4_ari_alert_threshold"],
            canonical_modularity=float(authority.canonical_summary["modularity"]),
        )
        assert_s4_canonical_seed_matches_corrected_p0(result)
        return write_stage_outputs(
            output_root, stage, build_future_s4_output_tables(result),
            implementation_commit=implementation_commit,
            input_artifacts=_p0_records(config, ("rq2c_undirected_view_edges.csv", "rq2c_undirected_view_lcc_edges.csv", "reference_quotient_node_registry.csv", "rq2c_algorithmic_communities.csv", "rq2c_undirected_view_summary.json", "rq2c_structural_brokerage_candidates.csv")),
            parameters=_stage_parameters("S4", config),
        )
    if stage == "S5_brokerage_stability":
        from .s45_canonical_graph import load_corrected_p0_s45_authority
        from .s5_brokerage_stability import assert_s5_canonical_setting_matches_corrected_p0, build_future_s5_output_tables, compute_s5_brokerage_stability, s5_production_settings

        authority = load_corrected_p0_s45_authority()
        settings = s5_production_settings(config)
        result = compute_s5_brokerage_stability(
            authority.lcc, authority.canonical_brokerage,
            k_values=settings["k_values"], seeds=settings["seeds"], top_ks=settings["top_k"],
            canonical_k=settings["canonical_k"], canonical_seed=settings["canonical_seed"],
            spearman_alert_threshold=settings["spearman_alert_threshold"],
            top50_overlap_alert_threshold=settings["top50_overlap_alert_threshold"],
        )
        assert_s5_canonical_setting_matches_corrected_p0(result)
        return write_stage_outputs(
            output_root, stage, build_future_s5_output_tables(result),
            implementation_commit=implementation_commit,
            input_artifacts=_p0_records(config, ("rq2c_undirected_view_edges.csv", "rq2c_undirected_view_lcc_edges.csv", "reference_quotient_node_registry.csv", "rq2c_algorithmic_communities.csv", "rq2c_undirected_view_summary.json", "rq2c_structural_brokerage_candidates.csv")),
            parameters=_stage_parameters("S5", config),
        )
    if stage == "S6_figure_ready":
        from .s6_figure_ready import resolve_s6_source_bundle, serialize_s6_figure_ready_bundle

        bundle = resolve_s6_source_bundle()
        _, receipt, _ = serialize_s6_figure_ready_bundle(
            bundle, output_root, implementation_commit=implementation_commit,
            parameters=_stage_parameters("S6", config),
        )
        return receipt
    raise OrchestrationError("unsupported stage: %s" % stage)


def execute_stage_control_plane(
    stage: str,
    *,
    output_root: str | Path,
    authority_roots: AuthorityRoots,
    executor: Callable[[], Any],
    historical_check: Callable[[], Mapping[str, Any]],
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Exercise the same fail-closed G18/G19 shell with an injected executor.

    This surface exists for deterministic fixture-only end-to-end testing; a
    production caller uses :func:`run_stage` and cannot inject scientific work.
    """

    if not isinstance(authority_roots, AuthorityRoots) or not authority_roots.fixture:
        raise OrchestrationError("injected stage control plane requires explicit fixture authority roots")
    canonical = _canonical_stage(stage)
    root = canonical_path(output_root)
    if (root / canonical).exists():
        raise OrchestrationError("target stage directory already exists; overwrite is forbidden: %s" % canonical)
    selected_config = dict(config or load_config())
    upstream = _validate_upstream_receipts(
        root, canonical, selected_config, authority_roots=authority_roots
    )
    before = dict(historical_check())
    if before.get("status") != "HISTORICAL_IMMUTABILITY_MATCH":
        raise OrchestrationError("fixture historical pre-stage comparison failed")
    receipt = executor()
    if not hasattr(receipt, "as_dict"):
        raise OrchestrationError("stage executor did not return a receipt")
    validate_stage_receipt(
        receipt.as_dict(), canonical, output_root=root,
        authority_roots=authority_roots, expected_output_root=root,
        enforce_contract=True,
    )
    after = dict(historical_check())
    if after.get("status") != "HISTORICAL_IMMUTABILITY_MATCH":
        raise OrchestrationError("fixture historical post-stage comparison failed")
    return {
        "status": "STAGE_EXECUTION_PASS",
        "stage": canonical,
        "upstream": upstream,
        "historical_before": before,
        "historical_after": after,
        "receipt": receipt.as_dict(),
    }


def run_stage(
    stage: str,
    *,
    authorization_phase: str,
    expected_implementation_commit: str,
    config_path: str | Path = DEFAULT_CONFIG_PATH,
    baseline_path: str | Path = CLEAN_DEFAULT_BASELINE_PATH,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run or preflight exactly one explicitly authorized C4 stage."""

    canonical = authorize_stage(
        stage,
        authorization_phase=authorization_phase,
        expected_implementation_commit=expected_implementation_commit,
    )
    config = load_config(config_path)
    provenance = validate_scaffold_provenance(config)
    input_hashes = verify_corrected_input_hash_closure(config_path)
    output_root = canonical_path(provenance["corrected_output_root"])
    if canonical == "S1_evidence_universe" and output_root.exists():
        raise OrchestrationError("clean output root must be absent before S1 execution")
    stage_dir = output_root / canonical
    if stage_dir.exists():
        raise OrchestrationError("target stage directory already exists; overwrite is forbidden: %s" % stage_dir)
    upstream = _validate_upstream_receipts(output_root, canonical, config)
    try:
        before = compare_historical_immutability(baseline_path)
    except Exception as exc:
        raise OrchestrationError("historical pre-stage comparison failed") from exc
    if before["status"] != "HISTORICAL_IMMUTABILITY_MATCH":
        raise OrchestrationError("historical pre-stage comparison is not an exact match")
    result: dict[str, Any] = {
        "status": "PREFLIGHT_PASS" if dry_run else "STAGE_EXECUTION_PASS",
        "stage": canonical,
        "authorization_phase": authorization_phase,
        "implementation_commit": expected_implementation_commit,
        "output_root": str(output_root),
        "target_stage_absent": True,
        "upstream": upstream,
        "corrected_input_hashes": input_hashes,
        "historical_before": before,
    }
    if dry_run:
        result["scientific_execution"] = False
        return result
    receipt = _run_scientific_stage(canonical, config, output_root, expected_implementation_commit)
    try:
        validate_stage_receipt(receipt.as_dict(), canonical, output_root=output_root, expected_output_root=output_root)
        after = compare_historical_immutability(baseline_path)
    except Exception as exc:
        raise OrchestrationError("post-stage closure failed") from exc
    if after["status"] != "HISTORICAL_IMMUTABILITY_MATCH":
        raise OrchestrationError("historical post-stage comparison is not an exact match")
    result["receipt"] = receipt.as_dict()
    result["historical_after"] = after
    result["scientific_execution"] = True
    return result
