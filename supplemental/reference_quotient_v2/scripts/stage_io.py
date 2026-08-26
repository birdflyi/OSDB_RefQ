"""Controlled, deterministic serialization for future corrected v2 stages.

This module is intentionally independent of the scientific stage runners. It
only serializes already-computed tables/metadata into an explicitly supplied
stage directory and records byte-level receipts. A failed write is never
cleaned up automatically, so a later retry cannot overwrite a partial stage.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Optional

import pandas as pd

from .paths import (
    CORRECTED_OUTPUTS_ROOT,
    REPOSITORY_ROOT,
    canonical_path,
    load_config,
    protected_write_roots,
)


class StageIOError(ValueError):
    """Raised when a future stage serialization contract is violated."""


STAGE_DIRECTORY_NAMES: Mapping[str, str] = {
    "S1": "S1_evidence_universe",
    "S2": "S2_weight_sensitivity",
    "S3": "S3_observation_sensitivity",
    "S4": "S4_community_stability",
    "S5": "S5_brokerage_stability",
    "S6": "S6_figure_ready",
}
_VALID_STAGE_NAMES = set(STAGE_DIRECTORY_NAMES) | set(STAGE_DIRECTORY_NAMES.values())


@dataclass(frozen=True)
class SerializedArtifact:
    """A deterministic payload before it is written to a stage directory."""

    name: str
    payload: bytes
    row_count: Optional[int]

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.payload).hexdigest()

    @property
    def bytes(self) -> int:
        return len(self.payload)


@dataclass(frozen=True)
class StageReceipt:
    """In-memory provenance receipt for one future completed stage."""

    stage: str
    status: str
    implementation_commit: str
    input_artifacts: tuple[Mapping[str, Any], ...]
    output_artifacts: tuple[Mapping[str, Any], ...]
    parameters: Mapping[str, Any]
    runtime_versions: Mapping[str, str]
    completed_at: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "stage": self.stage,
            "status": self.status,
            "implementation_commit": self.implementation_commit,
            "input_artifacts": [dict(item) for item in self.input_artifacts],
            "output_artifacts": [dict(item) for item in self.output_artifacts],
            "parameters": dict(self.parameters),
            "runtime_versions": dict(self.runtime_versions),
            "completed_at": self.completed_at,
        }


def canonical_stage_name(stage_name: str) -> str:
    if not isinstance(stage_name, str) or stage_name not in _VALID_STAGE_NAMES:
        raise StageIOError("stage must be one of S1-S6")
    if stage_name in STAGE_DIRECTORY_NAMES:
        return STAGE_DIRECTORY_NAMES[stage_name]
    return stage_name


def _safe_output_root(output_root: str | Path) -> Path:
    candidate = canonical_path(output_root)
    expected = canonical_path(CORRECTED_OUTPUTS_ROOT)
    inside_repository = candidate == canonical_path(REPOSITORY_ROOT) or candidate.is_relative_to(canonical_path(REPOSITORY_ROOT))
    if inside_repository and not candidate.is_relative_to(expected):
        raise StageIOError("stage output root inside repository must be corrected v2 outputs")
    try:
        config = load_config()
        protected = protected_write_roots(config)
    except Exception as exc:  # pragma: no cover - configuration is validated by callers
        raise StageIOError("unable to resolve protected write roots") from exc
    for root in protected:
        if candidate == root or candidate.is_relative_to(root):
            raise StageIOError("stage output root crosses protected authority: %s" % root)
    if candidate == expected or candidate.is_relative_to(expected):
        return candidate
    # A temp directory outside the repository is the only non-production root
    # accepted by tests. It remains explicit because the caller supplies it.
    return candidate


def _serialize_json(value: Mapping[str, Any]) -> bytes:
    try:
        text = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, separators=(",", ": ")) + "\n"
    except (TypeError, ValueError) as exc:
        raise StageIOError("JSON artifact is not serializable") from exc
    return text.encode("utf-8")


def serialize_artifact(name: str, value: Any) -> SerializedArtifact:
    """Serialize a DataFrame as CSV or a mapping as deterministic JSON."""

    if not isinstance(name, str) or not name or Path(name).name != name:
        raise StageIOError("artifact names must be simple filenames")
    suffix = Path(name).suffix.lower()
    if suffix == ".csv":
        if not isinstance(value, pd.DataFrame):
            raise StageIOError("CSV artifact must be a pandas DataFrame: %s" % name)
        try:
            text = value.to_csv(index=False, lineterminator="\n")
        except Exception as exc:  # pragma: no cover - pandas serialization error
            raise StageIOError("unable to serialize CSV artifact: %s" % name) from exc
        return SerializedArtifact(name=name, payload=text.encode("utf-8"), row_count=len(value))
    if suffix == ".json":
        if not isinstance(value, Mapping):
            raise StageIOError("JSON artifact must be a mapping: %s" % name)
        return SerializedArtifact(name=name, payload=_serialize_json(value), row_count=None)
    raise StageIOError("only CSV and JSON artifacts are supported: %s" % name)


def serialize_artifacts(artifacts: Mapping[str, Any]) -> tuple[SerializedArtifact, ...]:
    if not isinstance(artifacts, Mapping) or not artifacts:
        raise StageIOError("stage artifacts must be a non-empty mapping")
    names = sorted(artifacts)
    if len(names) != len(set(names)):
        raise StageIOError("stage artifact names must be unique")
    return tuple(serialize_artifact(name, artifacts[name]) for name in names)


def runtime_versions() -> dict[str, str]:
    versions: dict[str, str] = {"python": sys.version.split()[0]}
    for module in ("numpy", "pandas", "scipy", "networkx"):
        try:
            imported = __import__(module)
            versions[module] = str(imported.__version__)
        except Exception:  # pragma: no cover - optional environment metadata
            versions[module] = "unavailable"
    return versions


def write_stage_outputs(
    output_root: str | Path,
    stage_name: str,
    artifacts: Mapping[str, Any],
    *,
    implementation_commit: str = "",
    input_artifacts: tuple[Mapping[str, Any], ...] = (),
    parameters: Optional[Mapping[str, Any]] = None,
    versions: Optional[Mapping[str, str]] = None,
    completed_at: Optional[str] = None,
) -> StageReceipt:
    """Write one stage once, refusing any pre-existing stage directory."""

    root = _safe_output_root(output_root)
    stage = canonical_stage_name(stage_name)
    stage_dir = root / stage
    if stage_dir.exists():
        raise StageIOError("stage directory already exists; overwrite is forbidden: %s" % stage_dir)
    payloads = serialize_artifacts(artifacts)
    # No cleanup is performed after mkdir or any subsequent write failure.
    stage_dir.mkdir(parents=True, exist_ok=False)
    records: list[Mapping[str, Any]] = []
    for artifact in payloads:
        target = stage_dir / artifact.name
        if target.exists():
            raise StageIOError("stage artifact already exists: %s" % target)
        target.write_bytes(artifact.payload)
        records.append(
            {
                "path": str(target.relative_to(root)).replace(os.sep, "/"),
                "sha256": artifact.sha256,
                "bytes": artifact.bytes,
                "row_count": artifact.row_count,
            }
        )
    return StageReceipt(
        stage=stage,
        status="PASS",
        implementation_commit=implementation_commit,
        input_artifacts=tuple(dict(item) for item in input_artifacts),
        output_artifacts=tuple(records),
        parameters=dict(parameters or {}),
        runtime_versions=dict(versions or runtime_versions()),
        completed_at=completed_at or datetime.now(timezone.utc).isoformat(),
    )


def _resolve_record_path(record_path: str | Path, base: Path) -> Path:
    candidate = canonical_path(record_path, base=base)
    if not candidate.is_relative_to(base):
        raise StageIOError("artifact record path escaped its root: %s" % record_path)
    return candidate


def validate_output_artifact_records(
    output_root: str | Path,
    records: Mapping[str, Any] | list[Mapping[str, Any]] | tuple[Mapping[str, Any], ...],
) -> dict[str, Any]:
    """Verify recorded output SHA, byte count, and CSV row count."""

    root = canonical_path(output_root)
    if isinstance(records, Mapping):
        # Accept either one record or a name -> record mapping.  Normalizing
        # here keeps malformed receipts fail-closed with StageIOError.
        iterable = (records,) if "path" in records else tuple(records.values())
    elif isinstance(records, (list, tuple)):
        iterable = tuple(records)
    else:
        raise StageIOError("output records must be a record or a sequence")
    if not iterable:
        raise StageIOError("output records must not be empty")
    checked: list[dict[str, Any]] = []
    for record in iterable:
        if not isinstance(record, Mapping):
            raise StageIOError("output record must be a mapping")
        path_value = record.get("path")
        if not isinstance(path_value, str):
            raise StageIOError("output record path is missing")
        path = _resolve_record_path(path_value, root)
        if not path.is_file():
            raise StageIOError("recorded output does not exist: %s" % path)
        actual_sha = _sha256(path)
        if record.get("sha256") != actual_sha:
            raise StageIOError("output SHA mismatch: %s" % path)
        actual_bytes = path.stat().st_size
        bytes_value = record.get("bytes")
        if isinstance(bytes_value, bool) or not isinstance(bytes_value, (int, str)):
            raise StageIOError("output byte count is missing or invalid: %s" % path)
        try:
            recorded_bytes = int(bytes_value)
        except (TypeError, ValueError) as exc:
            raise StageIOError("output byte count is invalid: %s" % path) from exc
        if recorded_bytes != actual_bytes:
            raise StageIOError("output byte count mismatch: %s" % path)
        row_count = record.get("row_count")
        if row_count is not None:
            if path.suffix.lower() != ".csv":
                raise StageIOError("non-CSV output cannot declare row_count: %s" % path)
            try:
                actual_rows = len(pd.read_csv(path))
            except Exception as exc:
                raise StageIOError("unable to read recorded CSV row count: %s" % path) from exc
            if isinstance(row_count, bool) or not isinstance(row_count, (int, str)):
                raise StageIOError("output row count is invalid: %s" % path)
            try:
                recorded_rows = int(row_count)
            except (TypeError, ValueError) as exc:
                raise StageIOError("output row count is invalid: %s" % path) from exc
            if recorded_rows != actual_rows:
                raise StageIOError("output row count mismatch: %s" % path)
        checked.append({"path": str(path), "sha256": actual_sha, "bytes": actual_bytes, "row_count": row_count})
    return {"status": "PASS", "checked": checked}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
