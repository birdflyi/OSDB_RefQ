"""Read-only manifest helpers for the future corrected supplemental package."""

from __future__ import annotations

import hashlib
import json
import sys
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Mapping, Optional

from .paths import PathGuardError, canonical_path, validate_scaffold_config
from .stage_io import (
    AuthorityRoots,
    COMPLETED_STAGE_STATUSES,
    StageReceiptContractError,
    production_authority_roots,
    validate_stage_receipt,
)


class S7Status(str, Enum):
    KEPT_FIXED_OBJECT = "KEPT_FIXED_OBJECT"
    REGENERATE_REQUIRED = "REGENERATE_REQUIRED"
    NOT_EVALUATED = "NOT_EVALUATED"


class ManifestContractError(ValueError):
    """Raised when a corrected package manifest is incomplete or inconsistent."""


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: str | Path) -> Dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("manifest root must be an object")
    return value


def validate_corrected_p0_manifest(
    manifest_path: str | Path,
    corrected_p0_root: str | Path,
    corrected_p0_config: str | Path,
    expected_config_sha256: Optional[str] = None,
) -> Dict[str, Any]:
    manifest_file = canonical_path(manifest_path)
    p0_root = canonical_path(corrected_p0_root)
    p0_config = canonical_path(corrected_p0_config)
    if not manifest_file.is_file():
        raise PathGuardError("corrected P0 manifest does not exist: %s" % manifest_file)
    if not manifest_file.is_relative_to(p0_root):
        raise PathGuardError("corrected P0 manifest is outside corrected P0 root")
    manifest = load_json(manifest_file)
    if manifest.get("status") != "PASS":
        raise PathGuardError("corrected P0 manifest status must be PASS")
    output_directory = manifest.get("output_directory")
    if not isinstance(output_directory, str) or canonical_path(output_directory) != p0_root:
        raise PathGuardError("corrected P0 manifest output_directory does not match configured root")
    record = manifest.get("config")
    if not isinstance(record, Mapping):
        raise PathGuardError("corrected P0 manifest config record is missing")
    recorded_path = record.get("path")
    recorded_sha = record.get("sha256")
    if not isinstance(recorded_path, str) or canonical_path(recorded_path) != p0_config:
        raise PathGuardError("corrected P0 manifest config path does not match configured P0 config")
    actual_sha = sha256_file(p0_config)
    expected_sha = expected_config_sha256 or actual_sha
    if recorded_sha != expected_sha or actual_sha != expected_sha:
        raise PathGuardError("corrected P0 config SHA-256 does not close")
    # The frozen C3 design explicitly accepts the legacy manifest schema label.
    # entry_point is recorded metadata, never an executable authority.
    return manifest


def validate_scaffold_provenance(config: Mapping[str, Any]) -> Dict[str, Any]:
    paths = validate_scaffold_config(config)
    manifest = validate_corrected_p0_manifest(
        paths["corrected_p0_manifest"],
        paths["corrected_p0_root"],
        paths["corrected_p0_config"],
    )
    return {
        "status": "SCAFFOLD_VALID",
        "corrected_p0_manifest": str(paths["corrected_p0_manifest"]),
        "corrected_p0_manifest_status": manifest["status"],
        "corrected_p0_config_sha256": sha256_file(paths["corrected_p0_config"]),
        "corrected_p0_config": str(paths["corrected_p0_config"]),
        "corrected_p0_root": str(paths["corrected_p0_root"]),
        "corrected_aggregate_root": str(paths["corrected_aggregate_root"]),
        "corrected_output_root": str(paths["corrected_output_root"]),
        "entry_point_used_as_authority": False,
    }


PACKAGE_STAGE_NAMES: tuple[str, ...] = (
    "S1_evidence_universe",
    "S2_weight_sensitivity",
    "S3_observation_sensitivity",
    "S4_community_stability",
    "S5_brokerage_stability",
    "S6_figure_ready",
)
PACKAGE_MANIFEST_REQUIRED_KEYS: tuple[str, ...] = (
    "schema_version",
    "package_version",
    "status",
    "release_status",
    "implementation_commit",
    "branch",
    "corrected_p0",
    "corrected_aggregate",
    "corrected_output_root",
    "weight_multiplicity_contract",
    "random_seed",
    "brokerage_sample_size",
    "s2_directed_weight_thresholds",
    "s3_network_authority",
    "s4_seed_contract",
    "s5_k_seed_top_k_contract",
    "s5_inclusion_frequency_authority",
    "s6_structural_summary_authority",
    "s6_figure_ready_manifest_authority",
    "stage_receipts",
    "runtime_versions",
    "historical_comparison_baseline",
    "historical_write_audit",
    "s7_status",
    "entry_point_used_as_authority",
)

HISTORICAL_WRITE_AUDIT_REQUIRED_KEYS: tuple[str, ...] = (
    "status",
    "historical_roots_modified",
    "no_overwrite",
)


def _manifest_runtime_versions() -> dict[str, str]:
    versions: dict[str, str] = {"python": sys.version.split()[0]}
    for module in ("numpy", "pandas", "scipy", "networkx"):
        try:
            versions[module] = str(__import__(module).__version__)
        except Exception:  # pragma: no cover - optional environment metadata
            versions[module] = "unavailable"
    return versions


def _stage_receipt_key(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    if value in PACKAGE_STAGE_NAMES:
        return value
    if value in {"S1", "S2", "S3", "S4", "S5", "S6"}:
        return PACKAGE_STAGE_NAMES[int(value[1]) - 1]
    return None


def _normalized_stage_receipts(receipts: Mapping[str, Mapping[str, Any]]) -> dict[str, dict[str, Any]]:
    if not isinstance(receipts, Mapping):
        raise ManifestContractError("stage_receipts must be a mapping")
    normalized: dict[str, dict[str, Any]] = {}
    for key, receipt in receipts.items():
        stage = _stage_receipt_key(key)
        if stage is None or not isinstance(receipt, Mapping):
            raise ManifestContractError("stage receipt has an invalid stage or value")
        if stage in normalized:
            raise ManifestContractError("duplicate stage receipt: %s" % stage)
        normalized[stage] = dict(receipt)
    return normalized


def validate_historical_write_audit(audit: object) -> dict[str, Any]:
    """Validate the G19 immutable-history write audit contract."""

    if not isinstance(audit, Mapping):
        raise ManifestContractError("historical_write_audit must be a mapping")
    missing = [key for key in HISTORICAL_WRITE_AUDIT_REQUIRED_KEYS if key not in audit]
    if missing:
        raise ManifestContractError("historical_write_audit is missing: %s" % ", ".join(missing))
    if audit["status"] != "PASS":
        raise ManifestContractError("historical_write_audit status is not PASS")
    if audit["historical_roots_modified"] is not False:
        raise ManifestContractError("historical roots must be unmodified")
    if audit["no_overwrite"] is not True:
        raise ManifestContractError("historical write audit no_overwrite must be true")
    for key in ("before_sha256_inventory", "after_sha256_inventory"):
        if key in audit and not isinstance(audit[key], (Mapping, list, tuple)):
            raise ManifestContractError("historical_write_audit %s is malformed" % key)
    return {"status": "PASS"}


def _receipt_is_complete(
    stage: str,
    receipt: object,
    *,
    authority_roots: AuthorityRoots,
    expected_output_root: str | Path | None = None,
    enforce_stage_contract: bool | None = None,
) -> bool:
    if not isinstance(receipt, Mapping) or receipt.get("status") not in COMPLETED_STAGE_STATUSES:
        return False
    try:
        validate_stage_receipt(
            receipt,
            stage,
            authority_roots=authority_roots,
            expected_output_root=expected_output_root,
            enforce_contract=enforce_stage_contract,
        )
    except (StageReceiptContractError, OSError, TypeError, ValueError):
        return False
    return True


def _stage_output_root(receipt: object) -> str | None:
    if isinstance(receipt, Mapping) and isinstance(receipt.get("output_root"), str) and receipt["output_root"]:
        return receipt["output_root"]
    return None


def _s6_manifest_authority(path_value: str | Path) -> dict[str, Any]:
    path = canonical_path(path_value)
    return {
        "path": str(path),
        "sha256": sha256_file(path) if path.is_file() else None,
    }


def _validate_s6_manifest_authority(
    authority: object,
    *,
    expected_path: str | Path | None = None,
    authority_roots: AuthorityRoots | None = None,
) -> bool:
    if not isinstance(authority, Mapping):
        raise ManifestContractError("S6 figure-ready manifest authority must be a mapping")
    path_value = authority.get("path")
    sha_value = authority.get("sha256")
    if not isinstance(path_value, str) or not isinstance(sha_value, str):
        raise ManifestContractError("S6 figure-ready manifest path/SHA record is incomplete")
    if expected_path is not None and canonical_path(path_value) != canonical_path(expected_path):
        raise ManifestContractError("S6 figure-ready manifest path does not match configured S6 stage root")
    try:
        actual_sha = sha256_file(path_value)
    except (OSError, TypeError, ValueError) as exc:
        raise ManifestContractError("S6 figure-ready manifest is unavailable") from exc
    if actual_sha != sha_value:
        raise ManifestContractError("S6 figure-ready manifest SHA does not close")
    try:
        from .s6_figure_ready import validate_s6_manifest_sha_closure

        validate_s6_manifest_sha_closure(path_value, authority_roots=authority_roots)
    except (OSError, TypeError, ValueError) as exc:
        raise ManifestContractError("S6 figure-ready manifest closure failed") from exc
    return True


def build_corrected_package_manifest(
    config: Mapping[str, Any],
    stage_receipts: Mapping[str, Mapping[str, Any]],
    *,
    implementation_commit: str,
    branch: str,
    s7_status: str | S7Status = S7Status.NOT_EVALUATED,
    runtime_versions: Optional[Mapping[str, str]] = None,
    historical_write_audit: Optional[Mapping[str, Any]] = None,
    s6_manifest_path: Optional[str] = None,
    authority_roots: Optional[AuthorityRoots] = None,
    expected_output_root: str | Path | None = None,
    enforce_stage_contract: bool | None = None,
) -> dict[str, Any]:
    """Construct a future package manifest without persisting it."""

    provenance = validate_scaffold_provenance(config)
    context = authority_roots or production_authority_roots(config)
    if not isinstance(context, AuthorityRoots):
        raise ManifestContractError("authority_roots must be an AuthorityRoots context")
    if not context.fixture and context != production_authority_roots(config):
        raise ManifestContractError("production authority roots must match validated configuration")
    receipts = _normalized_stage_receipts(stage_receipts)
    try:
        status_value = S7Status(s7_status).value
    except ValueError as exc:
        raise ManifestContractError("invalid S7 status") from exc
    # The supplemental config already carries the immutable governance values;
    # corrected-P0 paths and hashes come from the validated provenance object.
    configured_output_value = config["corrected_output_root"]
    if isinstance(configured_output_value, Mapping):
        configured_output_value = configured_output_value.get("path")
    configured_output_root = canonical_path(configured_output_value)
    if context.fixture:
        if expected_output_root is None:
            raise ManifestContractError("fixture package output root must be explicit")
        output_root = canonical_path(expected_output_root)
    else:
        if context.corrected_supplemental != configured_output_root:
            raise ManifestContractError("configured supplemental authority root does not match package output root")
        if expected_output_root is not None and canonical_path(expected_output_root) != configured_output_root:
            raise ManifestContractError("production package output root cannot be overridden")
        output_root = configured_output_root
    receipt_complete = all(
        _receipt_is_complete(
            stage,
            receipts.get(stage),
            authority_roots=context,
            expected_output_root=output_root,
            enforce_stage_contract=enforce_stage_contract,
        )
        for stage in PACKAGE_STAGE_NAMES
    )
    audit = dict(historical_write_audit or {
        "status": "NOT_EXECUTED",
        "no_overwrite": False,
        "historical_roots_modified": None,
    })
    s6_receipt_root = _stage_output_root(receipts.get("S6_figure_ready"))
    s6_default_root = s6_receipt_root if context.fixture and s6_receipt_root else str(output_root)
    s6_default_path = Path(s6_default_root) / "S6_figure_ready" / "figure_ready_manifest_v2.json"
    s6_authority = _s6_manifest_authority(s6_manifest_path or s6_default_path)
    s6_complete = False
    if receipt_complete and s6_authority["sha256"] is not None:
        try:
            s6_complete = _validate_s6_manifest_authority(
                s6_authority,
                expected_path=None
                if context.fixture
                else output_root / "S6_figure_ready" / "figure_ready_manifest_v2.json",
                authority_roots=None if context.fixture else context,
            )
        except ManifestContractError:
            s6_complete = False
    audit_complete = False
    try:
        audit_complete = validate_historical_write_audit(audit)["status"] == "PASS"
    except ManifestContractError:
        audit_complete = False
    complete = receipt_complete and audit_complete and s6_complete
    manifest = {
        "schema_version": "corrected_supplemental_package_manifest_v2",
        "package_version": "corrected_supplemental_v2",
        "status": "STAGE_PACKAGE_COMPLETE" if complete else "STAGE_PACKAGE_INCOMPLETE",
        "release_status": "RELEASE_READY" if complete and status_value == S7Status.KEPT_FIXED_OBJECT.value else "NOT_RELEASE_READY",
        "implementation_commit": implementation_commit,
        "branch": branch,
        "corrected_p0": {
            "root": provenance["corrected_p0_root"],
            "manifest_path": provenance["corrected_p0_manifest"],
            "manifest_sha256": sha256_file(provenance["corrected_p0_manifest"]),
            "config_path": provenance["corrected_p0_config"],
            "config_sha256": provenance["corrected_p0_config_sha256"],
        },
        "corrected_aggregate": {
            "root": provenance["corrected_aggregate_root"],
            "identity_policy": config["identity_policy"],
            "source_admission_rule": config["source_admission_rule"],
        },
        "corrected_output_root": str(output_root),
        "weight_multiplicity_contract": config["weight_multiplicity_contract"],
        "random_seed": config["random_seed"],
        "brokerage_sample_size": config["brokerage_sample_size"],
        "s2_directed_weight_thresholds": list(config["s2_directed_weight_thresholds"]),
        "s3_network_authority": config["s3_network_authority"],
        "s4_seed_contract": {
            "seed_start": config["s4_louvain_seed_start"],
            "run_count": config["s4_louvain_run_count"],
            "seed_end": config["s4_louvain_seed_start"] + config["s4_louvain_run_count"] - 1,
            "ari_alert_threshold": config["s4_ari_alert_threshold"],
        },
        "s5_k_seed_top_k_contract": {
            "k": list(config["s5_brokerage_k"]),
            "seed_start": config["s5_seed_start"],
            "run_count": config["s5_run_count"],
            "seed_end": config["s5_seed_start"] + config["s5_run_count"] - 1,
            "top_k": list(config["s5_top_k"]),
            "spearman_alert_threshold": config["s5_spearman_alert_threshold"],
            "top50_overlap_alert_threshold": config["s5_top50_overlap_alert_threshold"],
        },
        "s5_inclusion_frequency_authority": config["s5_inclusion_frequency_authority"],
        "s6_structural_summary_authority": "S6_figure_ready/structural_summary.csv",
        "s6_figure_ready_manifest_authority": s6_authority,
        "stage_receipts": receipts,
        "runtime_versions": dict(runtime_versions or _manifest_runtime_versions()),
        "historical_comparison_baseline": {
            "tag": config["historical_tag"],
            "commit": config.get("historical_baseline_commit"),
            "comparison_only": True,
        },
        "historical_write_audit": audit,
        "s7_status": status_value,
        "entry_point_used_as_authority": False,
        "manifest_self_hash_not_embedded": True,
    }
    return manifest


build_package_manifest = build_corrected_package_manifest


def validate_package_manifest(
    manifest: Mapping[str, Any],
    *,
    config: Optional[Mapping[str, Any]] = None,
    authority_roots: Optional[AuthorityRoots] = None,
    expected_output_root: str | Path | None = None,
    enforce_stage_contract: bool | None = None,
) -> dict[str, Any]:
    """Validate package-level required keys and release-status semantics."""

    if not isinstance(manifest, Mapping):
        raise ManifestContractError("package manifest must be a mapping")
    missing = [key for key in PACKAGE_MANIFEST_REQUIRED_KEYS if key not in manifest]
    if missing:
        raise ManifestContractError("package manifest is missing: %s" % ", ".join(missing))
    try:
        s7_status = S7Status(manifest["s7_status"]).value
    except ValueError as exc:
        raise ManifestContractError("invalid S7 status") from exc
    context = authority_roots or production_authority_roots(config)
    if not isinstance(context, AuthorityRoots):
        raise ManifestContractError("authority_roots must be an AuthorityRoots context")
    if not context.fixture and context != production_authority_roots(config):
        raise ManifestContractError("production authority roots must match validated configuration")
    package_root_value = manifest.get("corrected_output_root")
    if not isinstance(package_root_value, str) or not package_root_value.strip():
        raise ManifestContractError("corrected_output_root is missing")
    package_root = canonical_path(package_root_value)
    if expected_output_root is not None and package_root != canonical_path(expected_output_root):
        raise ManifestContractError("package output root does not match expected output root")
    if not context.fixture and package_root != context.corrected_supplemental:
        raise ManifestContractError("package output root does not match configured corrected v2 outputs")
    receipts = _normalized_stage_receipts(manifest["stage_receipts"])
    receipt_complete = True
    for stage in PACKAGE_STAGE_NAMES:
        receipt = receipts.get(stage)
        if receipt is None:
            receipt_complete = False
            continue
        if receipt.get("status") in COMPLETED_STAGE_STATUSES:
            try:
                recorded_root = receipt.get("output_root")
                if not isinstance(recorded_root, str) or canonical_path(recorded_root) != package_root:
                    raise StageReceiptContractError("receipt output_root does not match package output root")
                validate_stage_receipt(
                    receipt,
                    stage,
                    output_root=receipt.get("output_root") or manifest.get("corrected_output_root"),
                    authority_roots=context,
                    expected_output_root=package_root,
                    enforce_contract=enforce_stage_contract,
                )
            except (StageReceiptContractError, OSError, TypeError, ValueError) as exc:
                raise ManifestContractError("stage receipt closure failed for %s" % stage) from exc
        else:
            receipt_complete = False
    try:
        audit_complete = validate_historical_write_audit(manifest["historical_write_audit"])["status"] == "PASS"
    except ManifestContractError:
        audit_complete = False
    s6_complete = False
    authority = manifest["s6_figure_ready_manifest_authority"]
    if isinstance(authority, Mapping) and isinstance(authority.get("sha256"), str):
        s6_path = canonical_path(authority.get("path")) if isinstance(authority.get("path"), str) else None
        s6_receipt = receipts.get("S6_figure_ready")
        s6_root = _stage_output_root(s6_receipt)
        if s6_path is not None and s6_root is not None:
            expected_s6_root = package_root / "S6_figure_ready" if not context.fixture else canonical_path(s6_root) / "S6_figure_ready"
            if not context.fixture and s6_path != expected_s6_root / "figure_ready_manifest_v2.json":
                raise ManifestContractError("S6 figure-ready manifest path does not match package output root")
            if not s6_path.is_relative_to(expected_s6_root):
                raise ManifestContractError("S6 figure-ready manifest is outside the S6 stage root")
        s6_complete = _validate_s6_manifest_authority(
            authority,
            expected_path=None
            if context.fixture
            else package_root / "S6_figure_ready" / "figure_ready_manifest_v2.json",
            authority_roots=None if context.fixture else context,
        )
    complete = receipt_complete and audit_complete and s6_complete
    expected_status = "STAGE_PACKAGE_COMPLETE" if complete else "STAGE_PACKAGE_INCOMPLETE"
    if manifest["status"] != expected_status:
        raise ManifestContractError("package status does not close against stage receipts")
    expected_release = "RELEASE_READY" if complete and s7_status == S7Status.KEPT_FIXED_OBJECT.value else "NOT_RELEASE_READY"
    if manifest["release_status"] != expected_release:
        raise ManifestContractError("release status does not close against stage/S7 status")
    if manifest["entry_point_used_as_authority"] is not False:
        raise ManifestContractError("stale P0 entry_point cannot be executable authority")
    corrected_p0 = manifest["corrected_p0"]
    if not isinstance(corrected_p0, Mapping):
        raise ManifestContractError("corrected_p0 must be a mapping")
    for path_key, sha_key, label in (
        ("manifest_path", "manifest_sha256", "corrected P0 manifest"),
        ("config_path", "config_sha256", "corrected P0 config"),
    ):
        path_value = corrected_p0.get(path_key)
        sha_value = corrected_p0.get(sha_key)
        if not isinstance(path_value, str) or not isinstance(sha_value, str):
            raise ManifestContractError("%s path/SHA record is incomplete" % label)
        try:
            actual_sha = sha256_file(path_value)
        except (OSError, TypeError, ValueError) as exc:
            raise ManifestContractError("%s is unavailable" % label) from exc
        if sha_value != actual_sha:
            raise ManifestContractError("%s SHA does not close" % label)
    if not context.fixture:
        if not isinstance(corrected_p0.get("root"), str) or canonical_path(corrected_p0["root"]) != context.corrected_p0:
            raise ManifestContractError("corrected P0 root does not match configured authority root")
        corrected_aggregate = manifest["corrected_aggregate"]
        if not isinstance(corrected_aggregate, Mapping) or not isinstance(corrected_aggregate.get("root"), str):
            raise ManifestContractError("corrected aggregate root record is incomplete")
        if canonical_path(corrected_aggregate["root"]) != context.corrected_aggregate:
            raise ManifestContractError("corrected aggregate root does not match configured authority root")
    return {
        "status": "PASS",
        "stage_package_complete": complete,
        "release_ready": expected_release == "RELEASE_READY",
        "s7_status": s7_status,
    }
