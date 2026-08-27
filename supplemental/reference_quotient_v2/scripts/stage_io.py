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
    validate_scaffold_config,
)


class StageIOError(ValueError):
    """Raised when a future stage serialization contract is violated."""


class StageReceiptContractError(StageIOError):
    """Raised when a completed stage receipt is malformed or not closed."""


STAGE_DIRECTORY_NAMES: Mapping[str, str] = {
    "S1": "S1_evidence_universe",
    "S2": "S2_weight_sensitivity",
    "S3": "S3_observation_sensitivity",
    "S4": "S4_community_stability",
    "S5": "S5_brokerage_stability",
    "S6": "S6_figure_ready",
}
STAGE_RECEIPT_NAME = "stage_receipt.json"
STAGE_CONTRACT_VERSION = "C3.7-F"
CORRECTED_AGGREGATE = "CORRECTED_AGGREGATE"
CORRECTED_P0 = "CORRECTED_P0"
CORRECTED_SUPPLEMENTAL_V2 = "CORRECTED_SUPPLEMENTAL_V2"
COMPLETED_STAGE_STATUSES = frozenset({"PASS", "COMPLETE", "STAGE_COMPLETE"})
STAGE_INPUT_AUTHORITIES: Mapping[str, frozenset[str]] = {
    "S1_evidence_universe": frozenset({CORRECTED_AGGREGATE, CORRECTED_P0}),
    "S2_weight_sensitivity": frozenset({CORRECTED_P0}),
    "S3_observation_sensitivity": frozenset({CORRECTED_P0}),
    "S4_community_stability": frozenset({CORRECTED_P0}),
    "S5_brokerage_stability": frozenset({CORRECTED_P0}),
    "S6_figure_ready": frozenset({CORRECTED_P0, CORRECTED_SUPPLEMENTAL_V2}),
}
S6_APPROVED_SUPPLEMENTAL_INPUTS: Mapping[str, str] = {
    "s4/louvain_stability_runs.csv": "S4_community_stability/louvain_stability_runs.csv",
    "s5/brokerage_stability_runs.csv": "S5_brokerage_stability/brokerage_stability_runs.csv",
}
RECEIPT_REQUIRED_KEYS = (
    "stage",
    "status",
    "implementation_commit",
    "input_artifacts",
    "output_artifacts",
    "parameters",
    "runtime_versions",
    "completed_at",
)
_VALID_STAGE_NAMES = set(STAGE_DIRECTORY_NAMES) | set(STAGE_DIRECTORY_NAMES.values())


def stage_output_inventory(stage_name: str) -> tuple[str, ...]:
    """Return the authoritative scientific output names for one stage.

    Imports are intentionally lazy because the scientific modules import this
    module for their writer helpers.
    """

    stage = canonical_stage_name(stage_name)
    if stage == "S1_evidence_universe":
        from .s1_evidence_universe import FUTURE_S1_OUTPUT_CONTRACT

        # The validation JSON entry is a receipt/diagnostic contract, not a
        # scientific output artifact; the frozen S1 writer emits eight CSVs.
        return tuple(sorted(name for name in FUTURE_S1_OUTPUT_CONTRACT if name.endswith(".csv")))
    if stage == "S2_weight_sensitivity":
        from .s2_weight_sensitivity import S2_OUTPUT_CONTRACT

        return tuple(sorted(S2_OUTPUT_CONTRACT))
    if stage == "S3_observation_sensitivity":
        from .s3_observation_sensitivity import S3_OUTPUT_CONTRACT

        return tuple(sorted(S3_OUTPUT_CONTRACT))
    if stage == "S4_community_stability":
        from .s4_community_stability import S4_OUTPUT_CONTRACT

        return tuple(sorted(S4_OUTPUT_CONTRACT))
    if stage == "S5_brokerage_stability":
        from .s5_brokerage_stability import S5_OUTPUT_CONTRACT

        return tuple(sorted(S5_OUTPUT_CONTRACT))
    from .s6_figure_ready import S6_MANIFEST_NAME, S6_OUTPUT_INVENTORY

    return tuple(S6_OUTPUT_INVENTORY) + (S6_MANIFEST_NAME,)


def required_input_inventory(stage_name: str) -> dict[str, Any]:
    """Describe the minimum machine-checkable input coverage for a stage."""

    stage = canonical_stage_name(stage_name)
    p0 = {
        "reference_quotient_cross_project_edges.csv",
        "reference_quotient_node_registry.csv",
    }
    canonical = {
        "rq2c_undirected_view_edges.csv",
        "rq2c_undirected_view_lcc_edges.csv",
        "reference_quotient_node_registry.csv",
        "rq2c_algorithmic_communities.csv",
        "rq2c_undirected_view_summary.json",
        "rq2c_structural_brokerage_candidates.csv",
    }
    if stage == "S1_evidence_universe":
        return {
            "aggregate_authority": True,
            "minimum_aggregate_partitions": 294,
            "optional_corrected_p0_relative_paths": frozenset(
                {"manifest.json", "analysis_seed_manifest_294.csv"}
            ),
        }
    if stage == "S2_weight_sensitivity":
        return {"corrected_p0_relative_paths": frozenset(p0)}
    if stage == "S3_observation_sensitivity":
        return {
            "corrected_p0_relative_paths": frozenset(
                p0 | {"analysis_seed_manifest_294.csv"}
            )
        }
    if stage in {"S4_community_stability", "S5_brokerage_stability"}:
        return {"corrected_p0_relative_paths": frozenset(canonical)}
    from .s6_figure_ready import P0_SOURCE_FILES

    return {
        "corrected_p0_relative_paths": frozenset(P0_SOURCE_FILES),
        "supplemental_relative_paths": frozenset(S6_APPROVED_SUPPLEMENTAL_INPUTS.values()),
    }


@dataclass(frozen=True)
class AuthorityRoots:
    """Explicit roots used to bind authority classes to filesystem paths."""

    corrected_aggregate: Path
    corrected_p0: Path
    corrected_supplemental: Path
    fixture: bool = False

    def __post_init__(self) -> None:
        for field in ("corrected_aggregate", "corrected_p0", "corrected_supplemental"):
            object.__setattr__(self, field, canonical_path(getattr(self, field)))
        if not isinstance(self.fixture, bool):
            raise StageIOError("authority root fixture flag is invalid")

    def root_for(self, authority_class: str) -> Path:
        roots = {
            CORRECTED_AGGREGATE: self.corrected_aggregate,
            CORRECTED_P0: self.corrected_p0,
            CORRECTED_SUPPLEMENTAL_V2: self.corrected_supplemental,
        }
        try:
            return roots[authority_class]
        except KeyError as exc:
            raise StageIOError("unknown authority class: %s" % authority_class) from exc


def production_authority_roots(config: Optional[Mapping[str, Any]] = None) -> AuthorityRoots:
    """Derive production authority roots from the validated scaffold config."""

    configured = dict(config) if config is not None else load_config()
    try:
        paths = validate_scaffold_config(configured)
    except Exception as exc:  # pragma: no cover - configuration failures are contract failures
        raise StageIOError("unable to resolve configured authority roots") from exc
    return AuthorityRoots(
        corrected_aggregate=paths["corrected_aggregate_root"],
        corrected_p0=paths["corrected_p0_root"],
        corrected_supplemental=paths["corrected_output_root"],
        fixture=False,
    )


def fixture_authority_roots(
    *,
    corrected_aggregate: str | Path,
    corrected_p0: str | Path,
    corrected_supplemental: str | Path,
) -> AuthorityRoots:
    """Create an explicit temporary-root context for synthetic tests only."""

    return AuthorityRoots(
        corrected_aggregate=corrected_aggregate,
        corrected_p0=corrected_p0,
        corrected_supplemental=corrected_supplemental,
        fixture=True,
    )


def _authority_context(authority_roots: Optional[AuthorityRoots]) -> AuthorityRoots:
    if authority_roots is None:
        return production_authority_roots()
    if not isinstance(authority_roots, AuthorityRoots):
        raise StageIOError("authority_roots must be an AuthorityRoots context")
    if not authority_roots.fixture:
        configured = production_authority_roots()
        if (
            authority_roots.corrected_aggregate != configured.corrected_aggregate
            or authority_roots.corrected_p0 != configured.corrected_p0
            or authority_roots.corrected_supplemental != configured.corrected_supplemental
        ):
            raise StageIOError("production authority roots must match validated configuration")
    return authority_roots


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
    output_root: str = ""

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
            "output_root": self.output_root,
        }


def canonical_stage_name(stage_name: str) -> str:
    if not isinstance(stage_name, str) or stage_name not in _VALID_STAGE_NAMES:
        raise StageIOError("stage must be one of S1-S6")
    if stage_name in STAGE_DIRECTORY_NAMES:
        return STAGE_DIRECTORY_NAMES[stage_name]
    return stage_name


def _safe_output_root(
    output_root: str | Path,
    *,
    allow_external_test_root: bool = False,
    expected_output_root: str | Path | None = None,
    fixture_context: bool = False,
) -> Path:
    candidate = canonical_path(output_root)
    expected = canonical_path(expected_output_root or CORRECTED_OUTPUTS_ROOT)
    repository = canonical_path(REPOSITORY_ROOT)
    inside_repository = candidate == repository or candidate.is_relative_to(repository)
    try:
        config = load_config()
        protected = protected_write_roots(config)
    except Exception as exc:  # pragma: no cover - configuration is validated by callers
        raise StageIOError("unable to resolve protected write roots") from exc
    for root in protected:
        if candidate == root or candidate.is_relative_to(root):
            raise StageIOError("stage output root crosses protected authority: %s" % root)
    if fixture_context and candidate == canonical_path(CORRECTED_OUTPUTS_ROOT):
        raise StageIOError("fixture stage output root cannot be the production corrected v2 outputs")
    if fixture_context and not allow_external_test_root:
        raise StageIOError("fixture stage output root requires explicit external-root opt-in")
    if not allow_external_test_root and candidate != expected:
        raise StageIOError("production stage output root must be exactly corrected v2 outputs")
    if allow_external_test_root and not fixture_context and candidate != expected:
        raise StageIOError("external test stage root requires an explicit fixture authority context")
    if allow_external_test_root and inside_repository and candidate != expected:
        raise StageIOError("external test stage root must be outside the repository")
    if candidate == expected:
        return candidate
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
    allow_external_test_root: bool = False,
    authority_roots: Optional[AuthorityRoots] = None,
    expected_output_root: str | Path | None = None,
    enforce_contract: bool | None = None,
) -> StageReceipt:
    """Write one stage once and persist its receipt after output closure."""

    context = _authority_context(authority_roots)
    configured_output_root = canonical_path(expected_output_root or context.corrected_supplemental)
    if not context.fixture and configured_output_root != context.corrected_supplemental:
        raise StageIOError("production output root cannot override configured supplemental root")
    root = _safe_output_root(
        output_root,
        allow_external_test_root=allow_external_test_root,
        expected_output_root=configured_output_root,
        fixture_context=context.fixture,
    )
    stage = canonical_stage_name(stage_name)
    stage_dir = root / stage
    if stage_dir.exists():
        raise StageIOError("stage directory already exists; overwrite is forbidden: %s" % stage_dir)
    payloads = serialize_artifacts(artifacts)
    input_records = tuple(dict(item) for item in input_artifacts)
    receipt_versions = dict(versions or runtime_versions())
    receipt_completed_at = completed_at or datetime.now(timezone.utc).isoformat()
    _validate_receipt_shape(
        {
            "stage": stage,
            "status": "PASS",
            "implementation_commit": implementation_commit,
            "input_artifacts": list(input_records),
            "output_artifacts": [
                {
                    "path": str((stage_dir / artifact.name).relative_to(root)).replace(os.sep, "/"),
                    "sha256": artifact.sha256,
                    "bytes": artifact.bytes,
                    "row_count": artifact.row_count,
                }
                for artifact in payloads
            ],
            "parameters": dict(parameters or {}),
            "runtime_versions": receipt_versions,
            "completed_at": receipt_completed_at,
            "output_root": str(root),
        },
        stage,
    )
    strict_contract = (not context.fixture) if enforce_contract is None else bool(enforce_contract)
    if not context.fixture and enforce_contract is False:
        raise StageIOError("production stage contract enforcement cannot be disabled")
    if strict_contract and set(artifacts) != set(stage_output_inventory(stage)):
        raise StageIOError("stage artifacts do not match the exact frozen output contract for %s" % stage)
    validate_required_input_coverage(input_records, stage, authority_roots=context, enforce_contract=strict_contract)
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
    receipt = StageReceipt(
        stage=stage,
        status="PASS",
        implementation_commit=implementation_commit,
        input_artifacts=input_records,
        output_artifacts=tuple(records),
        parameters=dict(parameters or {}),
        runtime_versions=receipt_versions,
        completed_at=receipt_completed_at,
        output_root=str(root),
    )
    validate_stage_receipt(
        receipt.as_dict(),
        stage,
        output_root=root,
        require_durable_marker=False,
        authority_roots=context,
        expected_output_root=root,
        enforce_contract=strict_contract,
    )
    receipt_path = stage_dir / STAGE_RECEIPT_NAME
    if receipt_path.exists():
        raise StageIOError("stage receipt already exists: %s" % receipt_path)
    receipt_path.write_bytes(_serialize_json(receipt.as_dict()))
    validate_stage_receipt(
        receipt.as_dict(),
        stage,
        output_root=root,
        require_durable_marker=True,
        authority_roots=context,
        expected_output_root=root,
        enforce_contract=strict_contract,
    )
    return receipt


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
        required = ("path", "sha256", "bytes", "row_count")
        if any(key not in record for key in required):
            raise StageIOError("output record is incomplete")
        path_value = record.get("path")
        if not isinstance(path_value, str):
            raise StageIOError("output record path is missing")
        path = _resolve_record_path(path_value, root)
        if path.name == STAGE_RECEIPT_NAME:
            raise StageIOError("stage receipt cannot be an output artifact")
        if not path.is_file():
            raise StageIOError("recorded output does not exist: %s" % path)
        actual_sha = _sha256(path)
        if not _valid_sha256(record.get("sha256")):
            raise StageIOError("output SHA is missing or invalid: %s" % path)
        if record.get("sha256") != actual_sha:
            raise StageIOError("output SHA mismatch: %s" % path)
        actual_bytes = path.stat().st_size
        bytes_value = record.get("bytes")
        if isinstance(bytes_value, bool) or not isinstance(bytes_value, int):
            raise StageIOError("output byte count is missing or invalid: %s" % path)
        if bytes_value != actual_bytes:
            raise StageIOError("output byte count mismatch: %s" % path)
        row_count = record.get("row_count")
        if path.suffix.lower() == ".csv":
            if isinstance(row_count, bool) or not isinstance(row_count, int):
                raise StageIOError("CSV output row count is missing or invalid: %s" % path)
            try:
                actual_rows = len(pd.read_csv(path))
            except Exception as exc:
                raise StageIOError("unable to read recorded CSV row count: %s" % path) from exc
            if row_count != actual_rows:
                raise StageIOError("output row count mismatch: %s" % path)
        elif row_count is not None and (isinstance(row_count, bool) or not isinstance(row_count, int)):
            raise StageIOError("output row count is invalid: %s" % path)
        checked.append({"path": str(path), "sha256": actual_sha, "bytes": actual_bytes, "row_count": row_count})
    return {"status": "PASS", "checked": checked}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _valid_sha256(value: object) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def _validate_receipt_shape(receipt: Mapping[str, Any], expected_stage: str | None = None) -> str:
    if not isinstance(receipt, Mapping):
        raise StageReceiptContractError("stage receipt must be a mapping")
    missing = [key for key in RECEIPT_REQUIRED_KEYS if key not in receipt]
    if missing:
        raise StageReceiptContractError("stage receipt is missing: %s" % ", ".join(missing))
    try:
        stage = canonical_stage_name(receipt["stage"])
    except StageIOError as exc:
        raise StageReceiptContractError(str(exc)) from exc
    if expected_stage is not None:
        try:
            expected = canonical_stage_name(expected_stage)
        except StageIOError as exc:
            raise StageReceiptContractError(str(exc)) from exc
        if stage != expected:
            raise StageReceiptContractError("receipt stage does not match manifest stage")
    if receipt["status"] not in COMPLETED_STAGE_STATUSES:
        raise StageReceiptContractError("receipt is not a completed stage receipt")
    if not isinstance(receipt["implementation_commit"], str) or not receipt["implementation_commit"].strip():
        raise StageReceiptContractError("receipt implementation_commit is missing")
    if not isinstance(receipt["input_artifacts"], (list, tuple)) or not receipt["input_artifacts"]:
        raise StageReceiptContractError("completed receipt input_artifacts must be non-empty")
    if not isinstance(receipt["output_artifacts"], (list, tuple)) or not receipt["output_artifacts"]:
        raise StageReceiptContractError("completed receipt output_artifacts must be non-empty")
    if not isinstance(receipt["parameters"], Mapping):
        raise StageReceiptContractError("receipt parameters must be a mapping")
    if not isinstance(receipt["runtime_versions"], Mapping) or not receipt["runtime_versions"]:
        raise StageReceiptContractError("receipt runtime_versions must be a non-empty mapping")
    if not isinstance(receipt["completed_at"], str) or not receipt["completed_at"].strip():
        raise StageReceiptContractError("receipt completed_at is missing")
    if "output_root" in receipt and receipt["output_root"] != "" and not isinstance(receipt["output_root"], str):
        raise StageReceiptContractError("receipt output_root is invalid")
    for artifact in receipt["input_artifacts"]:
        _validate_input_artifact_shape(artifact, stage)
    for artifact in receipt["output_artifacts"]:
        _validate_output_artifact_shape(artifact)
    return stage


def _validate_input_artifact_shape(artifact: object, stage: str) -> None:
    if not isinstance(artifact, Mapping):
        raise StageReceiptContractError("input artifact record must be a mapping")
    required = ("path", "sha256", "authority_class")
    if any(key not in artifact for key in required):
        raise StageReceiptContractError("input artifact record is incomplete")
    if not isinstance(artifact["path"], str) or not artifact["path"]:
        raise StageReceiptContractError("input artifact path is invalid")
    if not _valid_sha256(artifact["sha256"]):
        raise StageReceiptContractError("input artifact SHA is invalid")
    authority = artifact["authority_class"]
    if not isinstance(authority, str) or authority not in STAGE_INPUT_AUTHORITIES[stage]:
        raise StageReceiptContractError("input artifact authority is not allowed for %s" % stage)
    if ("root" in artifact) != ("version" in artifact):
        raise StageReceiptContractError("input artifact root and version must be paired")
    if "root" in artifact and (
        not isinstance(artifact["root"], str)
        or not artifact["root"].strip()
        or not isinstance(artifact["version"], str)
        or not artifact["version"].strip()
    ):
        raise StageReceiptContractError("input artifact root/version is invalid")


def _validate_output_artifact_shape(artifact: object) -> None:
    if not isinstance(artifact, Mapping):
        raise StageReceiptContractError("output artifact record must be a mapping")
    required = ("path", "sha256", "bytes", "row_count")
    if any(key not in artifact for key in required):
        raise StageReceiptContractError("output artifact record is incomplete")
    if not isinstance(artifact["path"], str) or not artifact["path"]:
        raise StageReceiptContractError("output artifact path is invalid")
    if not _valid_sha256(artifact["sha256"]):
        raise StageReceiptContractError("output artifact SHA is invalid")
    if isinstance(artifact["bytes"], bool) or not isinstance(artifact["bytes"], int) or artifact["bytes"] < 0:
        raise StageReceiptContractError("output artifact bytes is invalid")
    if artifact["row_count"] is not None and (
        isinstance(artifact["row_count"], bool) or not isinstance(artifact["row_count"], int) or artifact["row_count"] < 0
    ):
        raise StageReceiptContractError("output artifact row_count is invalid")
    if Path(artifact["path"]).name == STAGE_RECEIPT_NAME:
        raise StageReceiptContractError("stage receipt cannot be an output artifact")


def validate_input_artifact_records(
    records: list[Mapping[str, Any]] | tuple[Mapping[str, Any], ...],
    stage_name: str,
    *,
    authority_roots: Optional[AuthorityRoots] = None,
) -> dict[str, Any]:
    """Verify corrected input provenance records and their source hashes."""

    stage = canonical_stage_name(stage_name)
    context = _authority_context(authority_roots)
    if not isinstance(records, (list, tuple)) or not records:
        raise StageReceiptContractError("completed receipt input_artifacts must be non-empty")
    checked: list[dict[str, Any]] = []
    forbidden_fragments = (
        "reference_quotient_p0_frozen",
        "reference_quotient_v1",
        "v1_1_completion",
        "v1_2_s3_reproducibility_patch",
    )
    for artifact in records:
        _validate_input_artifact_shape(artifact, stage)
        expected_root = context.root_for(artifact["authority_class"])
        declared_root = canonical_path(artifact["root"]) if "root" in artifact else expected_root
        if declared_root != expected_root:
            raise StageReceiptContractError(
                "input artifact root does not match authority class: %s" % artifact["authority_class"]
            )
        raw_path = Path(artifact["path"])
        path = canonical_path(raw_path, base=declared_root) if declared_root and not raw_path.is_absolute() else canonical_path(raw_path)
        lowered = str(path).replace("\\", "/").lower()
        if any(fragment in lowered for fragment in forbidden_fragments):
            raise StageReceiptContractError("historical input authority is forbidden")
        if path == expected_root or not path.is_relative_to(expected_root):
            raise StageReceiptContractError("input artifact crosses its authority root")
        if stage == "S6_figure_ready" and artifact["authority_class"] == CORRECTED_SUPPLEMENTAL_V2:
            relative = path.relative_to(expected_root).as_posix()
            if relative not in S6_APPROVED_SUPPLEMENTAL_INPUTS.values():
                raise StageReceiptContractError("S6 supplemental input is not in the approved source map")
        if not path.is_file():
            raise StageReceiptContractError("input artifact does not exist: %s" % path)
        actual_sha = _sha256(path)
        if actual_sha != artifact["sha256"]:
            raise StageReceiptContractError("input artifact SHA mismatch: %s" % path)
        checked.append({"path": str(path), "sha256": actual_sha, "authority_class": artifact["authority_class"]})
    return {"status": "PASS", "checked": checked}


def validate_required_input_coverage(
    records: list[Mapping[str, Any]] | tuple[Mapping[str, Any], ...],
    stage_name: str,
    *,
    authority_roots: Optional[AuthorityRoots] = None,
    enforce_contract: bool = True,
) -> dict[str, Any]:
    """Require every scientific/provenance source used by the stage loader."""

    stage = canonical_stage_name(stage_name)
    context = _authority_context(authority_roots)
    validate_input_artifact_records(records, stage, authority_roots=context)
    paths_by_class: dict[str, set[str]] = {}
    for record in records:
        authority = str(record["authority_class"])
        root = context.root_for(authority)
        path = canonical_path(record["path"], base=root) if not Path(record["path"]).is_absolute() else canonical_path(record["path"])
        paths_by_class.setdefault(authority, set()).add(path.relative_to(root).as_posix())
    required = required_input_inventory(stage)
    if not enforce_contract:
        return {"status": "PASS", "stage": stage, "required_input_inventory": required, "recorded_input_count": len(records), "contract_enforced": False}
    if required.get("aggregate_authority"):
        aggregate_paths = paths_by_class.get(CORRECTED_AGGREGATE, set())
        expected_partitions = 1 if context.fixture else int(required["minimum_aggregate_partitions"])
        if len(aggregate_paths) != expected_partitions:
            raise StageReceiptContractError(
                "%s requires %s corrected aggregate partition inputs (recorded %s)"
                % (stage, expected_partitions, len(aggregate_paths))
            )
    required_p0 = required.get("corrected_p0_relative_paths")
    if required_p0:
        observed_p0 = paths_by_class.get(CORRECTED_P0, set())
        missing = sorted(set(required_p0) - observed_p0)
        if missing:
            raise StageReceiptContractError(
                "%s required corrected P0 inputs are missing: %s" % (stage, ", ".join(missing))
            )
        undeclared = sorted(observed_p0 - set(required_p0))
        if undeclared:
            raise StageReceiptContractError(
                "%s undeclared corrected P0 inputs are recorded: %s" % (stage, ", ".join(undeclared))
            )
    optional_p0 = required.get("optional_corrected_p0_relative_paths")
    if optional_p0 is not None:
        observed_p0 = paths_by_class.get(CORRECTED_P0, set())
        undeclared = sorted(observed_p0 - set(optional_p0))
        if undeclared:
            raise StageReceiptContractError(
                "%s undeclared optional corrected P0 inputs are recorded: %s" % (stage, ", ".join(undeclared))
            )
    required_supplemental = required.get("supplemental_relative_paths")
    if required_supplemental:
        observed_supplemental = paths_by_class.get(CORRECTED_SUPPLEMENTAL_V2, set())
        missing = sorted(set(required_supplemental) - observed_supplemental)
        if missing:
            raise StageReceiptContractError(
                "%s required supplemental inputs are missing: %s" % (stage, ", ".join(missing))
            )
        undeclared = sorted(observed_supplemental - set(required_supplemental))
        if undeclared:
            raise StageReceiptContractError(
                "%s undeclared supplemental inputs are recorded: %s" % (stage, ", ".join(undeclared))
            )
    return {
        "status": "PASS",
        "stage": stage,
        "required_input_inventory": required,
        "recorded_input_count": len(records),
    }


def validate_stage_receipt(
    receipt: Mapping[str, Any],
    stage_name: str,
    *,
    output_root: str | Path | None = None,
    require_durable_marker: bool = True,
    authority_roots: Optional[AuthorityRoots] = None,
    expected_output_root: str | Path | None = None,
    enforce_contract: bool | None = None,
) -> dict[str, Any]:
    """Validate a completed receipt, including source/output hash closure."""

    context = _authority_context(authority_roots)
    stage = _validate_receipt_shape(receipt, stage_name)
    strict_contract = (not context.fixture) if enforce_contract is None else bool(enforce_contract)
    if not context.fixture and enforce_contract is False:
        raise StageReceiptContractError("production stage contract enforcement cannot be disabled")
    root_value = output_root or receipt.get("output_root")
    if not isinstance(root_value, (str, Path)) or not str(root_value):
        raise StageReceiptContractError("completed receipt output_root is required for hash closure")
    root = canonical_path(root_value)
    configured_output_root = canonical_path(expected_output_root or context.corrected_supplemental)
    if not context.fixture and root != configured_output_root:
        raise StageReceiptContractError("production receipt output_root does not match configured package root")
    if expected_output_root is not None and root != configured_output_root:
        raise StageReceiptContractError("receipt output_root does not match expected output root")
    recorded_root = receipt.get("output_root")
    if isinstance(recorded_root, str) and recorded_root and canonical_path(recorded_root) != root:
        raise StageReceiptContractError("receipt output_root does not match validation root")
    stage_root = root / stage
    for artifact in receipt["output_artifacts"]:
        artifact_path = canonical_path(artifact["path"], base=root)
        if not artifact_path.is_relative_to(stage_root) or artifact_path == stage_root:
            raise StageReceiptContractError("output artifact is outside its stage directory")
    output_result = validate_output_artifact_records(root, receipt["output_artifacts"])
    recorded_outputs = {
        canonical_path(item["path"], base=root).relative_to(stage_root).as_posix()
        for item in receipt["output_artifacts"]
    }
    expected_outputs = set(stage_output_inventory(stage))
    if strict_contract and recorded_outputs != expected_outputs:
        missing = sorted(expected_outputs - recorded_outputs)
        undeclared = sorted(recorded_outputs - expected_outputs)
        detail = []
        if missing:
            detail.append("missing=" + ",".join(missing))
        if undeclared:
            detail.append("undeclared=" + ",".join(undeclared))
        raise StageReceiptContractError(
            "stage output contract is incomplete for %s (%s)" % (stage, "; ".join(detail))
        )
    validate_required_input_coverage(
        receipt["input_artifacts"], stage, authority_roots=context, enforce_contract=strict_contract
    )
    receipt_path = root / stage / STAGE_RECEIPT_NAME
    if require_durable_marker:
        if not receipt_path.is_file():
            raise StageReceiptContractError("durable stage_receipt.json is missing: %s" % receipt_path)
        durable = load_stage_receipt(root / stage)
        if durable != dict(receipt):
            raise StageReceiptContractError("durable stage receipt does not match validated receipt")
    return {
        "status": "PASS",
        "stage": stage,
        "input_artifacts_checked": len(receipt["input_artifacts"]),
        "output_artifacts_checked": len(output_result["checked"]),
        "durable_receipt": str(receipt_path),
    }


def load_stage_receipt(stage_directory: str | Path) -> dict[str, Any]:
    path = canonical_path(stage_directory) / STAGE_RECEIPT_NAME
    if not path.is_file():
        raise StageReceiptContractError("durable stage_receipt.json is missing: %s" % path)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise StageReceiptContractError("durable stage receipt is not valid JSON") from exc
    if not isinstance(value, dict):
        raise StageReceiptContractError("durable stage receipt must be an object")
    return value
