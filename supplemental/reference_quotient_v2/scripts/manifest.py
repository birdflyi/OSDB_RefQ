"""Read-only manifest helpers for the future corrected supplemental package."""

from __future__ import annotations

import hashlib
import json
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Mapping, Optional

from .paths import PathGuardError, canonical_path, validate_scaffold_config


class S7Status(str, Enum):
    KEPT_FIXED_OBJECT = "KEPT_FIXED_OBJECT"
    REGENERATE_REQUIRED = "REGENERATE_REQUIRED"
    NOT_EVALUATED = "NOT_EVALUATED"


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
        "corrected_p0_root": str(paths["corrected_p0_root"]),
        "corrected_aggregate_root": str(paths["corrected_aggregate_root"]),
        "corrected_output_root": str(paths["corrected_output_root"]),
        "entry_point_used_as_authority": False,
    }
