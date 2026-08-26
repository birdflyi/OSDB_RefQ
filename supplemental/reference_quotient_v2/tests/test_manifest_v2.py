"""C3.7-E corrected package manifest contract tests."""

from __future__ import annotations

import copy

import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.manifest import (
    ManifestContractError,
    S7Status,
    build_corrected_package_manifest,
    validate_package_manifest,
)


def _receipt(stage: str, status: str = "PASS") -> dict:
    return {
        "stage": stage,
        "status": status,
        "implementation_commit": "fixture",
        "input_artifacts": [],
        "output_artifacts": [],
        "parameters": {},
        "runtime_versions": {"python": "fixture"},
        "completed_at": "2026-08-26T00:00:00+00:00",
    }


def _receipts() -> dict[str, dict]:
    return {
        stage: _receipt(stage)
        for stage in (
            "S1_evidence_universe",
            "S2_weight_sensitivity",
            "S3_observation_sensitivity",
            "S4_community_stability",
            "S5_brokerage_stability",
            "S6_figure_ready",
        )
    }


def test_package_manifest_required_schema_and_s7_release_distinction():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    manifest = build_corrected_package_manifest(
        config,
        _receipts(),
        implementation_commit="fixture",
        branch="fixture-branch",
        runtime_versions={"python": "fixture"},
    )
    assert manifest["status"] == "STAGE_PACKAGE_COMPLETE"
    assert manifest["release_status"] == "NOT_RELEASE_READY"
    assert manifest["s7_status"] == S7Status.NOT_EVALUATED.value
    assert manifest["entry_point_used_as_authority"] is False
    assert validate_package_manifest(manifest)["stage_package_complete"] is True
    assert validate_package_manifest(manifest)["release_ready"] is False


def test_missing_or_failed_stage_prevents_package_completion():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    receipts = _receipts()
    receipts.pop("S5_brokerage_stability", None)
    manifest = build_corrected_package_manifest(
        config, receipts, implementation_commit="fixture", branch="fixture"
    )
    assert manifest["status"] == "STAGE_PACKAGE_INCOMPLETE"
    assert validate_package_manifest(manifest)["stage_package_complete"] is False

    receipts = _receipts()
    receipts["S5_brokerage_stability"]["status"] = "FAIL"
    failed = build_corrected_package_manifest(
        config, receipts, implementation_commit="fixture", branch="fixture"
    )
    assert failed["status"] == "STAGE_PACKAGE_INCOMPLETE"


def test_s7_invalid_value_and_inconsistent_status_fail_closed():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    with pytest.raises(ManifestContractError, match="S7"):
        build_corrected_package_manifest(
            config, _receipts(), implementation_commit="fixture", branch="fixture", s7_status="INVALID"
        )
    manifest = build_corrected_package_manifest(
        config,
        _receipts(),
        implementation_commit="fixture",
        branch="fixture",
        s7_status=S7Status.KEPT_FIXED_OBJECT,
    )
    assert manifest["release_status"] == "RELEASE_READY"
    tampered = copy.deepcopy(manifest)
    tampered["release_status"] = "NOT_RELEASE_READY"
    with pytest.raises(ManifestContractError, match="release status"):
        validate_package_manifest(tampered)


def test_manifest_rejects_missing_required_key_and_stale_entry_point():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    manifest = build_corrected_package_manifest(
        config, _receipts(), implementation_commit="fixture", branch="fixture"
    )
    missing = copy.deepcopy(manifest)
    del missing["s6_structural_summary_authority"]
    with pytest.raises(ManifestContractError, match="missing"):
        validate_package_manifest(missing)
    stale = copy.deepcopy(manifest)
    stale["entry_point_used_as_authority"] = True
    with pytest.raises(ManifestContractError, match="entry_point"):
        validate_package_manifest(stale)


def test_manifest_rejects_malformed_nested_records_with_contract_error():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    manifest = build_corrected_package_manifest(
        config, _receipts(), implementation_commit="fixture", branch="fixture"
    )
    malformed = copy.deepcopy(manifest)
    malformed["corrected_p0"] = None
    with pytest.raises(ManifestContractError, match="corrected_p0"):
        validate_package_manifest(malformed)

    malformed = copy.deepcopy(manifest)
    malformed["stage_receipts"] = []
    with pytest.raises(ManifestContractError, match="stage_receipts"):
        validate_package_manifest(malformed)
