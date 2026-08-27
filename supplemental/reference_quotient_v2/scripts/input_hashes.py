"""Read-only accepted-hash closure for corrected P0 and aggregate inputs."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

from .manifest import sha256_file, validate_scaffold_provenance
from .paths import DEFAULT_CONFIG_PATH, canonical_path, load_config


class CorrectedInputHashError(ValueError):
    """Raised when current corrected inputs diverge from accepted provenance."""


EXPECTED_P0_MANIFEST_SHA256 = "21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7"
EXPECTED_P0_CONFIG_SHA256 = "e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658"
EXPECTED_AGGREGATE_PARTITIONS = 294


def _load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise CorrectedInputHashError("corrected P0 manifest is unavailable or invalid") from exc
    if not isinstance(value, dict) or value.get("status") != "PASS":
        raise CorrectedInputHashError("corrected P0 manifest status is not PASS")
    return value


def _check_record(path: Path, record: Mapping[str, Any], label: str) -> None:
    if not path.is_file():
        raise CorrectedInputHashError("%s is missing: %s" % (label, path))
    recorded_sha = record.get("sha256")
    if not isinstance(recorded_sha, str) or sha256_file(path) != recorded_sha:
        raise CorrectedInputHashError("%s SHA does not match accepted provenance: %s" % (label, path))
    recorded_bytes = record.get("bytes")
    if recorded_bytes is not None and int(recorded_bytes) != path.stat().st_size:
        raise CorrectedInputHashError("%s byte count does not match accepted provenance: %s" % (label, path))


def verify_corrected_input_hash_closure(
    config_path: str | Path = DEFAULT_CONFIG_PATH,
) -> dict[str, Any]:
    """Revalidate all accepted corrected P0 outputs and all 294 partitions."""

    config = load_config(config_path)
    provenance = validate_scaffold_provenance(config)
    manifest_path = canonical_path(provenance["corrected_p0_manifest"])
    config_file = canonical_path(provenance["corrected_p0_config"])
    if sha256_file(manifest_path) != EXPECTED_P0_MANIFEST_SHA256:
        raise CorrectedInputHashError("corrected P0 manifest SHA is not the accepted C3.7-F authority")
    if sha256_file(config_file) != EXPECTED_P0_CONFIG_SHA256:
        raise CorrectedInputHashError("corrected P0 config SHA is not the accepted C3.7-F authority")
    manifest = _load_manifest(manifest_path)
    p0_root = canonical_path(provenance["corrected_p0_root"])
    output_records = manifest.get("output_files")
    if not isinstance(output_records, list) or not output_records:
        raise CorrectedInputHashError("corrected P0 manifest has no accepted output inventory")
    for record in output_records:
        if not isinstance(record, Mapping) or not isinstance(record.get("path"), str):
            raise CorrectedInputHashError("corrected P0 output inventory is malformed")
        path = canonical_path(record["path"], base=p0_root)
        if not path.is_relative_to(p0_root):
            raise CorrectedInputHashError("corrected P0 output escaped its accepted root")
        _check_record(path, record, "corrected P0 output")

    aggregate_root = canonical_path(provenance["corrected_aggregate_root"])
    input_records = manifest.get("input_files")
    if not isinstance(input_records, list):
        raise CorrectedInputHashError("corrected P0 manifest has no accepted input inventory")
    aggregate_records: list[Mapping[str, Any]] = []
    for record in input_records:
        if not isinstance(record, Mapping) or not isinstance(record.get("path"), str):
            continue
        path = canonical_path(record["path"])
        if path.parent == aggregate_root:
            aggregate_records.append(record)
    if len(aggregate_records) != EXPECTED_AGGREGATE_PARTITIONS:
        raise CorrectedInputHashError(
            "accepted corrected aggregate inventory is incomplete: %s/%s"
            % (len(aggregate_records), EXPECTED_AGGREGATE_PARTITIONS)
        )
    accepted_paths: set[str] = set()
    for record in aggregate_records:
        path = canonical_path(record["path"])
        _check_record(path, record, "corrected aggregate partition")
        accepted_paths.add(os.path.normcase(os.fspath(path)))
    current_paths = {
        os.path.normcase(os.fspath(canonical_path(path)))
        for path in aggregate_root.iterdir()
        if path.is_file()
    }
    if current_paths != accepted_paths:
        raise CorrectedInputHashError("current corrected aggregate file set does not equal the accepted 294-partition inventory")
    return {
        "C3_7F_CORRECTED_P0_HASH_CLOSURE": "PASS",
        "corrected_p0_output_records": len(output_records),
        "corrected_p0_manifest_sha256": EXPECTED_P0_MANIFEST_SHA256,
        "corrected_p0_config_sha256": EXPECTED_P0_CONFIG_SHA256,
        "corrected_aggregate_partitions": len(aggregate_records),
        "C3_7F_CORRECTED_AGGREGATE_294_HASH_CLOSURE": "PASS",
    }
