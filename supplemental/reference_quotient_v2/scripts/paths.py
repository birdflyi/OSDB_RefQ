"""Fail-closed path and authority guards for corrected supplemental v2.

This module only resolves and validates paths. It never creates output roots,
reads aggregate rows, or executes a scientific stage.
"""

from __future__ import annotations

import ast
import json
import os
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
V2_ROOT = REPOSITORY_ROOT / "supplemental" / "reference_quotient_v2"
DEFAULT_CONFIG_PATH = V2_ROOT / "configs" / "supplemental_v2_corrected.yaml"
CORRECTED_P0_ROOT = REPOSITORY_ROOT / "outputs" / "reference_quotient_p0_corrected_v2"
HISTORICAL_P0_ROOT = REPOSITORY_ROOT / "outputs" / "reference_quotient_p0_frozen"
HISTORICAL_SUPPLEMENTAL_ROOT = REPOSITORY_ROOT / "supplemental" / "reference_quotient_v1"
CORRECTED_OUTPUTS_ROOT = V2_ROOT / "outputs"


class AuthorityRole(str, Enum):
    EXECUTABLE_CORRECTED_AUTHORITY = "EXECUTABLE_CORRECTED_AUTHORITY"
    COMPARISON_ONLY_HISTORICAL = "COMPARISON_ONLY_HISTORICAL"
    WRITE_TARGET = "WRITE_TARGET"
    UNKNOWN = "UNKNOWN"


class PathGuardError(ValueError):
    """Raised when a path crosses a frozen authority boundary."""


@dataclass(frozen=True)
class PathAuthority:
    path: Path
    role: AuthorityRole
    comparison_only: bool = False


def canonical_path(value: str | Path, base: str | Path = REPOSITORY_ROOT) -> Path:
    """Resolve relative, traversal, case, and symlink aliases before comparison."""

    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = Path(base) / candidate
    return Path(os.path.realpath(os.path.abspath(os.fspath(candidate))))


def _same_path(left: Path, right: Path) -> bool:
    return os.path.normcase(os.fspath(left)) == os.path.normcase(os.fspath(right))


def _is_within(candidate: Path, root: Path, include_root: bool = True) -> bool:
    candidate_text = os.path.normcase(os.fspath(candidate))
    root_text = os.path.normcase(os.fspath(root))
    if include_root and candidate_text == root_text:
        return True
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _load_simple_yaml(text: str) -> Dict[str, Any]:
    """Load the small scalar/nested YAML subset used by repository configs."""

    root: Dict[str, Any] = {}
    maps: list[tuple[int, Dict[str, Any]]] = [(-1, root)]
    for raw_line in text.splitlines():
        line = _strip_comment(raw_line).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, value = line.strip().split(":", 1)
        while maps[-1][0] >= indent:
            maps.pop()
        target = maps[-1][1]
        value = value.strip()
        if not value:
            nested: Dict[str, Any] = {}
            target[key.strip()] = nested
            maps.append((indent, nested))
        else:
            target[key.strip()] = _parse_scalar(value)
    return root


def _strip_comment(line: str) -> str:
    in_single = False
    in_double = False
    for index, char in enumerate(line):
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            return line[:index]
    return line


def _parse_scalar(value: str) -> Any:
    lowered = value.lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    if lowered in {"null", "none"}:
        return None
    if value.startswith("[") or value.startswith("{"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return ast.literal_eval(value)
    for converter in (int, float):
        try:
            return converter(value)
        except ValueError:
            pass
    return value.strip('"').strip("'")


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> Dict[str, Any]:
    config_path = canonical_path(path)
    if not config_path.is_file():
        raise PathGuardError("configuration file does not exist: %s" % config_path)
    return _load_simple_yaml(config_path.read_text(encoding="utf-8"))


def _mapping_path(config: Mapping[str, Any], key: str) -> Path:
    value = config.get(key)
    if isinstance(value, Mapping):
        value = value.get("path")
    if not isinstance(value, str) or not value.strip():
        raise PathGuardError("missing configured path: %s" % key)
    return canonical_path(value)


def _p0_config_source_roots(config: Mapping[str, Any]) -> list[Path]:
    p0_config_path = _mapping_path(config, "corrected_p0_config")
    if not p0_config_path.is_file():
        return []
    p0_config = _load_simple_yaml(p0_config_path.read_text(encoding="utf-8"))
    roots: list[Path] = []
    source_repository = p0_config.get("source_repository")
    if isinstance(source_repository, Mapping) and isinstance(source_repository.get("path"), str):
        roots.append(canonical_path(source_repository["path"]))
    input_paths = p0_config.get("input_paths")
    if isinstance(input_paths, Mapping):
        for value in input_paths.values():
            if isinstance(value, str) and Path(value).is_absolute():
                roots.append(canonical_path(value))
    return roots


def protected_write_roots(config: Optional[Mapping[str, Any]] = None) -> list[Path]:
    roots = [HISTORICAL_P0_ROOT, CORRECTED_P0_ROOT, HISTORICAL_SUPPLEMENTAL_ROOT]
    if config is not None:
        roots.extend(_p0_config_source_roots(config))
        manuscript_roots = config.get("manuscript_roots", [])
        if isinstance(manuscript_roots, Sequence) and not isinstance(manuscript_roots, (str, bytes)):
            roots.extend(canonical_path(value) for value in manuscript_roots if isinstance(value, str))
    for name in ("manuscript", "paper", "thesis"):
        candidate = REPOSITORY_ROOT / name
        if candidate.exists():
            roots.append(canonical_path(candidate))
    unique: list[Path] = []
    for root in roots:
        if not any(_same_path(root, existing) for existing in unique):
            unique.append(root)
    return unique


def classify_path(value: str | Path, config: Optional[Mapping[str, Any]] = None) -> PathAuthority:
    candidate = canonical_path(value)
    corrected_p0 = canonical_path(config.get("corrected_p0_root")) if config else CORRECTED_P0_ROOT
    corrected_aggregate = _mapping_path(config, "corrected_aggregate_root") if config else None
    corrected_config = canonical_path(config.get("corrected_p0_config")) if config else REPOSITORY_ROOT / "configs" / "ch5_reference_quotient_p0_v2.yaml"
    corrected_outputs = canonical_path(config.get("corrected_output_root")) if config else CORRECTED_OUTPUTS_ROOT
    if _is_within(candidate, corrected_p0):
        return PathAuthority(candidate, AuthorityRole.EXECUTABLE_CORRECTED_AUTHORITY)
    if corrected_aggregate is not None and _is_within(candidate, corrected_aggregate):
        return PathAuthority(candidate, AuthorityRole.EXECUTABLE_CORRECTED_AUTHORITY)
    if _same_path(candidate, corrected_config):
        return PathAuthority(candidate, AuthorityRole.EXECUTABLE_CORRECTED_AUTHORITY)
    if _is_within(candidate, corrected_outputs):
        return PathAuthority(candidate, AuthorityRole.WRITE_TARGET)
    if _is_within(candidate, HISTORICAL_P0_ROOT) or _is_within(candidate, HISTORICAL_SUPPLEMENTAL_ROOT):
        return PathAuthority(candidate, AuthorityRole.COMPARISON_ONLY_HISTORICAL, comparison_only=True)
    return PathAuthority(candidate, AuthorityRole.UNKNOWN)


def validate_comparison_only(value: str | Path | Mapping[str, Any], comparison_only: bool, config: Optional[Mapping[str, Any]] = None) -> Path:
    candidate = None
    if isinstance(value, Mapping):
        raw_path = value.get("path")
        if not isinstance(raw_path, str):
            raise PathGuardError("comparison-only mapping must contain a path")
        candidate = canonical_path(raw_path)
    authority = classify_path(candidate or value, config)
    if authority.role == AuthorityRole.COMPARISON_ONLY_HISTORICAL and not comparison_only:
        raise PathGuardError("historical path requires explicit comparison_only=true: %s" % authority.path)
    return authority.path


def validate_write_target(value: str | Path, config: Optional[Mapping[str, Any]] = None) -> Path:
    candidate = canonical_path(value)
    corrected_outputs = canonical_path(config.get("corrected_output_root")) if config else CORRECTED_OUTPUTS_ROOT
    if not _is_within(candidate, corrected_outputs):
        raise PathGuardError("write target must be under corrected v2 outputs: %s" % candidate)
    for protected in protected_write_roots(config):
        if _is_within(candidate, protected):
            raise PathGuardError("write target crosses protected authority root: %s" % protected)
    return candidate


def validate_corrected_output_root(config: Mapping[str, Any]) -> Path:
    candidate = _mapping_path(config, "corrected_output_root")
    expected = canonical_path(CORRECTED_OUTPUTS_ROOT)
    if not _is_within(candidate, expected):
        raise PathGuardError("corrected_output_root must be under supplemental/reference_quotient_v2/outputs")
    validate_write_target(candidate, config)
    return candidate


def validate_config_paths(config: Mapping[str, Any]) -> Dict[str, Path]:
    required = {
        "corrected_p0_root",
        "corrected_p0_manifest",
        "corrected_p0_config",
        "corrected_aggregate_root",
        "corrected_output_root",
        "historical_p0_root",
        "historical_supplemental_root",
    }
    missing = sorted(required - set(config))
    if missing:
        raise PathGuardError("missing path keys: %s" % ", ".join(missing))
    corrected_p0 = _mapping_path(config, "corrected_p0_root")
    if not _same_path(corrected_p0, CORRECTED_P0_ROOT):
        raise PathGuardError("corrected_p0_root does not resolve to corrected P0 authority")
    corrected_manifest = _mapping_path(config, "corrected_p0_manifest")
    if not _is_within(corrected_manifest, corrected_p0):
        raise PathGuardError("corrected_p0_manifest must be inside corrected P0 root")
    corrected_config = _mapping_path(config, "corrected_p0_config")
    expected_config = REPOSITORY_ROOT / "configs" / "ch5_reference_quotient_p0_v2.yaml"
    if not _same_path(corrected_config, expected_config):
        raise PathGuardError("corrected_p0_config does not resolve to the approved P0 v2 config")
    corrected_aggregate = _mapping_path(config, "corrected_aggregate_root")
    if not corrected_aggregate.is_dir():
        raise PathGuardError("corrected aggregate root does not exist: %s" % corrected_aggregate)
    p0_config = _load_simple_yaml(corrected_config.read_text(encoding="utf-8"))
    p0_inputs = p0_config.get("input_paths", {})
    if not isinstance(p0_inputs, Mapping):
        raise PathGuardError("corrected P0 input_paths is not a mapping")
    expected_aggregate = p0_inputs.get("gh_core_ref_node_agg_v2_dir")
    executable_aggregate = p0_inputs.get("gh_core_ref_node_agg_dir")
    historical_aggregate = p0_inputs.get("gh_core_ref_node_agg_v1_dir")
    if not isinstance(expected_aggregate, str) or not _same_path(corrected_aggregate, canonical_path(expected_aggregate)):
        raise PathGuardError("corrected aggregate root does not match corrected P0 v2 aggregate authority")
    if isinstance(executable_aggregate, str) and not _same_path(corrected_aggregate, canonical_path(executable_aggregate)):
        raise PathGuardError("corrected aggregate root does not match executable P0 aggregate input")
    if isinstance(historical_aggregate, str) and _is_within(corrected_aggregate, canonical_path(historical_aggregate)):
        raise PathGuardError("corrected aggregate root resolves to historical aggregate")
    historical_p0 = _mapping_path(config, "historical_p0_root")
    historical_supplemental = _mapping_path(config, "historical_supplemental_root")
    if not _same_path(historical_p0, HISTORICAL_P0_ROOT):
        raise PathGuardError("historical_p0_root does not resolve to the approved frozen root")
    if not _same_path(historical_supplemental, HISTORICAL_SUPPLEMENTAL_ROOT):
        raise PathGuardError("historical_supplemental_root does not resolve to the approved v1 root")
    for key, value in (("historical_p0_root", config.get("historical_p0_root")), ("historical_supplemental_root", config.get("historical_supplemental_root"))):
        if not isinstance(value, Mapping) or value.get("comparison_only") is not True:
            raise PathGuardError("%s must be explicitly marked comparison_only" % key)
    output = validate_corrected_output_root(config)
    return {
        "corrected_p0_root": corrected_p0,
        "corrected_p0_manifest": corrected_manifest,
        "corrected_p0_config": corrected_config,
        "corrected_aggregate_root": corrected_aggregate,
        "corrected_output_root": output,
        "historical_p0_root": historical_p0,
        "historical_supplemental_root": historical_supplemental,
    }


def validate_scaffold_config(config: Mapping[str, Any]) -> Dict[str, Path]:
    paths = validate_config_paths(config)
    if config.get("identity_policy") != "STRICT_REPOSITORY_IDENTITY":
        raise PathGuardError("identity_policy must be STRICT_REPOSITORY_IDENTITY")
    if config.get("source_admission_rule") != "event_repo_id == annotated_primary_github_repo_id":
        raise PathGuardError("source_admission_rule is not the frozen strict identity rule")
    if not str(config.get("weight_multiplicity_contract", "")).strip():
        raise PathGuardError("weight_multiplicity_contract must be declared")
    if config.get("historical_tag") != "chapter5-refq-freeze-v1.0":
        raise PathGuardError("historical_tag is not the immutable approved tag")
    if not str(config.get("s3_network_authority", "")).strip():
        raise PathGuardError("s3_network_authority must be declared")
    if not str(config.get("s5_inclusion_frequency_authority", "")).strip():
        raise PathGuardError("s5_inclusion_frequency_authority must be declared")
    if not str(config.get("s6_structural_summary_authority", "")).strip():
        raise PathGuardError("s6_structural_summary_authority must be declared")
    if config.get("event_rejoin_required") is not False:
        raise PathGuardError("event_rejoin_required must be false")
    if config.get("scientific_execution_authorized") is not False:
        raise PathGuardError("scientific execution must remain unauthorized in C3.7-A")
    if int(config.get("random_seed", 0)) != 20260731:
        raise PathGuardError("random_seed must be 20260731")
    return paths
