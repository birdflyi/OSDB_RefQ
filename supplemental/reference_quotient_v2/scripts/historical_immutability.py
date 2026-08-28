"""Byte-level G19 historical immutability baseline and comparator."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Iterable, Mapping

from .paths import (
    CORRECTED_P0_ROOT,
    HISTORICAL_P0_ROOT,
    HISTORICAL_SUPPLEMENTAL_ROOT,
    LEGACY_CORRECTED_P0_V2_ROOT,
    LEGACY_SUPPLEMENTAL_V2_OUTPUTS_ROOT,
    REPOSITORY_ROOT,
    canonical_path,
    load_config,
)


class HistoricalImmutabilityError(ValueError):
    """Raised when the protected historical state cannot be closed."""


DEFAULT_BASELINE_PATH = REPOSITORY_ROOT / "docs" / "freeze" / "ch5_refq_c3_7f_historical_immutability_baseline_v1.json"
CLEAN_DEFAULT_BASELINE_PATH = REPOSITORY_ROOT / "docs" / "freeze" / "ch5_refq_p0v3_clean_supplemental_immutability_baseline_v1.json"
HISTORICAL_TAG = "chapter5-refq-freeze-v1.0"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def historical_tag_commit(tag: str = HISTORICAL_TAG) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-list", "-n", "1", tag],
            cwd=str(REPOSITORY_ROOT),
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise HistoricalImmutabilityError("historical tag cannot be resolved: %s" % tag) from exc
    commit = result.stdout.strip()
    if not commit:
        raise HistoricalImmutabilityError("historical tag resolved to an empty commit: %s" % tag)
    return commit


def _root_inventory(label: str, root: str | Path) -> dict[str, Any]:
    resolved = canonical_path(root)
    if not resolved.is_dir():
        raise HistoricalImmutabilityError("historical root does not exist: %s" % resolved)
    files: list[dict[str, Any]] = []
    for path in sorted((item for item in resolved.rglob("*") if item.is_file()), key=lambda item: item.relative_to(resolved).as_posix()):
        files.append(
            {
                "root": label,
                "relative_path": path.relative_to(resolved).as_posix(),
                "sha256": _sha256(path),
                "bytes": path.stat().st_size,
            }
        )
    return {
        "root": label,
        "path": str(resolved).replace("\\", "/"),
        "file_count": len(files),
        "aggregate_bytes": sum(int(item["bytes"]) for item in files),
        "files": files,
    }


def build_historical_immutability_baseline(
    *,
    baseline_path: str | Path = DEFAULT_BASELINE_PATH,
    historical_tag: str = HISTORICAL_TAG,
    roots: Iterable[tuple[str, str | Path]] | None = None,
    schema_version: str = "ch5_refq_c3_7f_historical_immutability_baseline_v1",
) -> dict[str, Any]:
    """Create deterministic pre-C4 inventories without touching protected files."""

    selected_roots = tuple(roots or (
        ("outputs/reference_quotient_p0_frozen", HISTORICAL_P0_ROOT),
        ("supplemental/reference_quotient_v1", HISTORICAL_SUPPLEMENTAL_ROOT),
    ))
    tag_commit = historical_tag_commit(historical_tag)
    inventories = [_root_inventory(label, root) for label, root in selected_roots]
    payload = {
        "schema_version": schema_version,
        "historical_tag": historical_tag,
        "historical_tag_commit": tag_commit,
        "roots": inventories,
        "deterministic_path_order": True,
        "comparison_result": "PRE_C4_BASELINE_ONLY",
    }
    target = canonical_path(baseline_path)
    freeze_root = canonical_path(REPOSITORY_ROOT / "docs" / "freeze")
    if not target.is_relative_to(freeze_root):
        raise HistoricalImmutabilityError("baseline must be written under docs/freeze")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def build_clean_supplemental_immutability_baseline(
    *,
    baseline_path: str | Path = CLEAN_DEFAULT_BASELINE_PATH,
    historical_tag: str = HISTORICAL_TAG,
) -> dict[str, Any]:
    """Freeze every pre-existing P0/supplemental asset before clean execution."""

    config = load_config()
    payload = build_historical_immutability_baseline(
        baseline_path=baseline_path,
        historical_tag=historical_tag,
        schema_version="ch5_refq_p0v3_clean_supplemental_immutability_baseline_v1",
        roots=(
            ("outputs/reference_quotient_p0_frozen", HISTORICAL_P0_ROOT),
            ("outputs/reference_quotient_p0_corrected_v2", LEGACY_CORRECTED_P0_V2_ROOT),
            ("outputs/reference_quotient_p0_corrected_v3", CORRECTED_P0_ROOT),
            ("supplemental/reference_quotient_v1", HISTORICAL_SUPPLEMENTAL_ROOT),
            ("supplemental/reference_quotient_v2/outputs", LEGACY_SUPPLEMENTAL_V2_OUTPUTS_ROOT),
            ("corrected_aggregate_v2", canonical_path(config["corrected_aggregate_root"])),
        ),
    )
    payload["authorities"] = {
        "official_p0_v3_result_commit": "2d284f4bc83c42ba6555a09a2e42693c5490b827",
        "official_p0_v3_scientific_implementation_commit": "25c6ef3f49af04e916f10e129d976ce7c2119fd8",
        "legacy_supplemental_s1_result_commit": "edb9441c7b276051224087fdf26d2e0cfcb78dba",
        "legacy_supplemental_s2_result_commit": "08a3c11a42a58958d0c60afe2f79a9d469c0ec5d",
        "legacy_supplemental_s3_result_commit": "0c73d5f6e95c1fa8227b11aec8c8f1643476e662",
    }
    target = canonical_path(baseline_path)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def load_historical_baseline(path: str | Path = DEFAULT_BASELINE_PATH) -> dict[str, Any]:
    target = canonical_path(path)
    try:
        value = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise HistoricalImmutabilityError("historical baseline is unavailable or invalid") from exc
    accepted_schemas = {
        "ch5_refq_c3_7f_historical_immutability_baseline_v1",
        "ch5_refq_p0v3_clean_supplemental_immutability_baseline_v1",
    }
    if not isinstance(value, dict) or value.get("schema_version") not in accepted_schemas:
        raise HistoricalImmutabilityError("historical baseline schema is invalid")
    return value


def compare_historical_immutability(
    baseline: str | Path | Mapping[str, Any] = DEFAULT_BASELINE_PATH,
) -> dict[str, Any]:
    """Compare current protected roots and tag identity against a baseline."""

    value = load_historical_baseline(baseline) if not isinstance(baseline, Mapping) else dict(baseline)
    differences: list[dict[str, Any]] = []
    expected_tag = value.get("historical_tag")
    expected_commit = value.get("historical_tag_commit")
    if not isinstance(expected_tag, str) or not isinstance(expected_commit, str):
        raise HistoricalImmutabilityError("historical baseline tag record is incomplete")
    actual_commit = historical_tag_commit(expected_tag)
    if actual_commit != expected_commit:
        differences.append({"kind": "tag_movement", "expected": expected_commit, "actual": actual_commit})
    expected_roots = value.get("roots")
    if not isinstance(expected_roots, list):
        raise HistoricalImmutabilityError("historical baseline roots are invalid")
    for expected_root in expected_roots:
        if not isinstance(expected_root, Mapping) or not isinstance(expected_root.get("root"), str) or not isinstance(expected_root.get("path"), str):
            raise HistoricalImmutabilityError("historical baseline root record is invalid")
        current = _root_inventory(str(expected_root["root"]), expected_root["path"])
        expected_files = {item["relative_path"]: item for item in expected_root.get("files", []) if isinstance(item, Mapping)}
        current_files = {item["relative_path"]: item for item in current["files"]}
        for relative in sorted(current_files.keys() - expected_files.keys()):
            differences.append({"kind": "added_historical_file", "root": expected_root["root"], "relative_path": relative})
        for relative in sorted(expected_files.keys() - current_files.keys()):
            differences.append({"kind": "removed_historical_file", "root": expected_root["root"], "relative_path": relative})
        for relative in sorted(current_files.keys() & expected_files.keys()):
            expected_file = expected_files[relative]
            current_file = current_files[relative]
            if current_file.get("sha256") != expected_file.get("sha256"):
                differences.append({"kind": "modified_sha", "root": expected_root["root"], "relative_path": relative})
            if int(current_file.get("bytes", -1)) != int(expected_file.get("bytes", -2)):
                differences.append({"kind": "modified_bytes", "root": expected_root["root"], "relative_path": relative})
    return {
        "status": "HISTORICAL_IMMUTABILITY_MATCH" if not differences else "FAIL_CLOSED",
        "differences": differences,
        "historical_tag": expected_tag,
        "historical_tag_commit": expected_commit,
    }


compare_historical_state = compare_historical_immutability
