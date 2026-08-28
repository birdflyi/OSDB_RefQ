"""C3.7-E.1 receipt, G19 and package-release contract tests."""

from __future__ import annotations

import copy
import hashlib
import json

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.manifest import (
    ManifestContractError,
    S7Status,
    build_corrected_package_manifest,
    validate_package_manifest,
)
from supplemental.reference_quotient_v2.scripts.s6_figure_ready import serialize_s6_figure_ready_bundle
from supplemental.reference_quotient_v2.scripts.stage_io import (
    CORRECTED_P0,
    STAGE_RECEIPT_NAME,
    StageReceiptContractError,
    fixture_authority_roots,
    validate_stage_receipt,
    write_stage_outputs,
)
from supplemental.reference_quotient_v2.tests.test_s6_figure_ready import _fixture


STAGES = (
    "S1_evidence_universe",
    "S2_weight_sensitivity",
    "S3_observation_sensitivity",
    "S4_community_stability",
    "S5_brokerage_stability",
)
_UNSET = object()


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


def _fake_receipts() -> dict[str, dict]:
    return {stage: _receipt(stage) for stage in STAGES + ("S6_figure_ready",)}


def _input_record(tmp_path, root=None) -> dict:
    root = root or (tmp_path / "corrected_p0_fixture")
    root.mkdir(parents=True, exist_ok=True)
    source = root / "source.csv"
    source.write_text("value\n1\n", encoding="utf-8")
    return {
        "path": str(source),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "authority_class": CORRECTED_P0,
        "root": str(root),
        "version": "corrected_p0_v3",
    }


def _fixture_context(tmp_path):
    return fixture_authority_roots(
        corrected_aggregate=tmp_path / "corrected_aggregate_fixture",
        corrected_p0=tmp_path / "corrected_p0_fixture",
        corrected_supplemental=tmp_path / "corrected_supplemental_v2_outputs",
    )


def _package_context(tmp_path):
    return fixture_authority_roots(
        corrected_aggregate=tmp_path / "corrected_aggregate_fixture",
        corrected_p0=tmp_path / "corrected_p0",
        corrected_supplemental=tmp_path / "corrected_supplemental_v2_outputs",
    )


def _valid_package(tmp_path, *, s7_status=S7Status.NOT_EVALUATED, historical_write_audit=_UNSET):
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    p0_root, supplemental_root, source_bundle = _fixture(tmp_path)
    input_record = _input_record(tmp_path, root=p0_root)
    stage_root = tmp_path / "stage_outputs"
    authority_roots = fixture_authority_roots(
        corrected_aggregate=tmp_path / "corrected_aggregate_fixture",
        corrected_p0=p0_root,
        corrected_supplemental=supplemental_root,
    )
    receipts = {}
    for index, stage in enumerate(STAGES, start=1):
        receipt = write_stage_outputs(
            stage_root,
            stage,
            {"stage.csv": pd.DataFrame({"value": [index]})},
            implementation_commit="fixture",
            input_artifacts=(input_record,),
            completed_at="2026-08-26T00:00:00+00:00",
            allow_external_test_root=True,
            authority_roots=authority_roots,
            expected_output_root=stage_root,
        )
        receipts[stage] = receipt.as_dict()

    _, s6_receipt, _ = serialize_s6_figure_ready_bundle(
        source_bundle,
        stage_root,
        implementation_commit="fixture",
        completed_at="2026-08-26T00:00:00+00:00",
        allow_external_test_root=True,
        authority_roots=authority_roots,
        expected_output_root=stage_root,
    )
    receipts["S6_figure_ready"] = s6_receipt.as_dict()
    audit = historical_write_audit
    if audit is _UNSET:
        audit = {
            "status": "PASS",
            "historical_roots_modified": False,
            "no_overwrite": True,
            "before_sha256_inventory": {},
            "after_sha256_inventory": {},
        }
    return build_corrected_package_manifest(
        config,
        receipts,
        implementation_commit="fixture",
        branch="fixture",
        s7_status=s7_status,
        runtime_versions={"python": "fixture"},
        historical_write_audit=audit,
        authority_roots=authority_roots,
        expected_output_root=stage_root,
    )


def _validate_fixture_package(manifest, tmp_path):
    return validate_package_manifest(
        manifest,
        authority_roots=_package_context(tmp_path),
        expected_output_root=tmp_path / "stage_outputs",
    )


def test_prior_empty_receipt_gap_is_confirmed_and_cannot_complete_package():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    manifest = build_corrected_package_manifest(
        config,
        _fake_receipts(),
        implementation_commit="fixture",
        branch="fixture",
        historical_write_audit={"status": "PASS", "historical_roots_modified": False, "no_overwrite": True},
    )
    assert manifest["status"] == "STAGE_PACKAGE_INCOMPLETE"
    with pytest.raises(ManifestContractError, match="stage receipt closure"):
        validate_package_manifest(manifest)


def test_valid_receipts_and_g19_pass_package_complete_but_s7_not_ready(tmp_path):
    manifest = _valid_package(tmp_path)
    assert manifest["status"] == "STAGE_PACKAGE_COMPLETE"
    assert manifest["release_status"] == "NOT_RELEASE_READY"
    context = _fixture_context(tmp_path)
    assert _validate_fixture_package(manifest, tmp_path)["stage_package_complete"] is True
    assert _validate_fixture_package(manifest, tmp_path)["release_ready"] is False


@pytest.mark.parametrize("field", ("input_artifacts", "output_artifacts"))
def test_empty_receipt_artifact_lists_fail_closed(field, tmp_path):
    receipt = _receipt("S1_evidence_universe")
    if field == "output_artifacts":
        receipt["input_artifacts"] = [_input_record(tmp_path)]
    with pytest.raises(StageReceiptContractError, match="non-empty"):
        validate_stage_receipt(receipt, "S1", authority_roots=_fixture_context(tmp_path))


def test_receipt_stage_mismatch_and_missing_field_fail_closed(tmp_path):
    receipt = _receipt("S1_evidence_universe")
    receipt["input_artifacts"] = [_input_record(tmp_path)]
    receipt["output_artifacts"] = [{"path": "S1_evidence_universe/x.csv", "sha256": "0" * 64, "bytes": 1, "row_count": 1}]
    receipt.pop("completed_at")
    with pytest.raises(StageReceiptContractError, match="completed_at"):
        validate_stage_receipt(receipt, "S1", authority_roots=_fixture_context(tmp_path))
    receipt["completed_at"] = "fixture"
    with pytest.raises(StageReceiptContractError, match="stage"):
        validate_stage_receipt(receipt, "S2", authority_roots=_fixture_context(tmp_path))


@pytest.mark.parametrize("field", ("parameters", "runtime_versions"))
def test_missing_receipt_field_fails_closed(field, tmp_path):
    receipt = _receipt("S1_evidence_universe")
    receipt["input_artifacts"] = [_input_record(tmp_path)]
    receipt["output_artifacts"] = [{"path": "S1_evidence_universe/x.csv", "sha256": "0" * 64, "bytes": 1, "row_count": 1}]
    receipt.pop(field)
    with pytest.raises(StageReceiptContractError, match=field):
        validate_stage_receipt(receipt, "S1", authority_roots=_fixture_context(tmp_path))


def test_malformed_input_and_output_artifacts_fail_closed(tmp_path):
    receipt = _receipt("S1_evidence_universe")
    receipt["input_artifacts"] = [{"path": "x", "sha256": "0" * 64}]
    receipt["output_artifacts"] = [{"path": "S1_evidence_universe/x.csv", "sha256": "0" * 64, "bytes": 1, "row_count": 1}]
    with pytest.raises(StageReceiptContractError, match="input artifact"):
        validate_stage_receipt(receipt, "S1", authority_roots=_fixture_context(tmp_path))
    receipt["input_artifacts"] = [_input_record(tmp_path)]
    receipt["output_artifacts"] = [{"path": "S1_evidence_universe/x.csv", "sha256": "0" * 64, "bytes": 1}]
    with pytest.raises(StageReceiptContractError, match="output artifact"):
        validate_stage_receipt(receipt, "S1", authority_roots=_fixture_context(tmp_path))


def test_input_hash_and_historical_authority_fail_closed(tmp_path):
    input_record = _input_record(tmp_path)
    input_record["sha256"] = "0" * 64
    with pytest.raises(StageReceiptContractError, match="input artifact SHA mismatch"):
        from supplemental.reference_quotient_v2.scripts.stage_io import validate_input_artifact_records

        validate_input_artifact_records([input_record], "S1", authority_roots=_fixture_context(tmp_path))
    historical = _input_record(tmp_path)
    historical["authority_class"] = CORRECTED_P0
    historical["path"] = str(paths.HISTORICAL_P0_ROOT / "manifest.json")
    with pytest.raises(StageReceiptContractError, match="historical"):
        from supplemental.reference_quotient_v2.scripts.stage_io import validate_input_artifact_records

        validate_input_artifact_records([historical], "S1", authority_roots=_fixture_context(tmp_path))


def test_wrong_stage_output_bytes_and_row_count_fail_package_validation(tmp_path):
    manifest = _valid_package(tmp_path)
    tampered = copy.deepcopy(manifest)
    tampered["stage_receipts"]["S1_evidence_universe"]["output_artifacts"][0]["bytes"] += 1
    with pytest.raises(ManifestContractError, match="stage receipt closure"):
        _validate_fixture_package(tampered, tmp_path)
    tampered = copy.deepcopy(manifest)
    tampered["stage_receipts"]["S3_observation_sensitivity"]["output_artifacts"][0]["sha256"] = "0" * 64
    with pytest.raises(ManifestContractError, match="stage receipt closure"):
        _validate_fixture_package(tampered, tmp_path)
    tampered = copy.deepcopy(manifest)
    tampered["stage_receipts"]["S2_weight_sensitivity"]["output_artifacts"][0]["row_count"] += 1
    with pytest.raises(ManifestContractError, match="stage receipt closure"):
        _validate_fixture_package(tampered, tmp_path)


def test_g19_missing_not_executed_or_fail_prevents_package_completion(tmp_path):
    for index, audit in enumerate((None, {"status": "NOT_EXECUTED"}, {"status": "FAIL", "historical_roots_modified": False, "no_overwrite": True})):
        manifest = _valid_package(tmp_path / ("case_%s" % index), historical_write_audit=audit)
        assert manifest["status"] == "STAGE_PACKAGE_INCOMPLETE"
        assert manifest["release_status"] == "NOT_RELEASE_READY"


def test_s7_regenerate_required_is_not_release_ready(tmp_path):
    manifest = _valid_package(tmp_path, s7_status=S7Status.REGENERATE_REQUIRED)
    assert manifest["status"] == "STAGE_PACKAGE_COMPLETE"
    assert manifest["release_status"] == "NOT_RELEASE_READY"
    assert _validate_fixture_package(manifest, tmp_path)["release_ready"] is False


def test_s7_kept_fixed_object_closes_release_ready(tmp_path):
    manifest = _valid_package(tmp_path, s7_status=S7Status.KEPT_FIXED_OBJECT)
    assert manifest["status"] == "STAGE_PACKAGE_COMPLETE"
    assert manifest["release_status"] == "RELEASE_READY"
    assert _validate_fixture_package(manifest, tmp_path)["release_ready"] is True


def test_s6_manifest_authority_is_path_and_sha_and_tampering_fails(tmp_path):
    manifest = _valid_package(tmp_path)
    authority = manifest["s6_figure_ready_manifest_authority"]
    assert set(authority) == {"path", "sha256"}
    assert isinstance(authority["sha256"], str)
    tampered = copy.deepcopy(manifest)
    tampered["s6_figure_ready_manifest_authority"]["sha256"] = "0" * 64
    with pytest.raises(ManifestContractError, match="S6 figure-ready manifest SHA"):
        _validate_fixture_package(tampered, tmp_path)


def test_invalid_nested_manifest_records_are_contract_errors(tmp_path):
    manifest = _valid_package(tmp_path)
    malformed = copy.deepcopy(manifest)
    malformed["corrected_p0"] = None
    with pytest.raises(ManifestContractError, match="corrected_p0"):
        _validate_fixture_package(malformed, tmp_path)


def test_durable_marker_is_last_and_not_an_output_artifact(tmp_path):
    stage_root = tmp_path / "marker_outputs"
    receipt = write_stage_outputs(
        stage_root,
        "S1",
        {"table.csv": pd.DataFrame({"value": [1]})},
        implementation_commit="fixture",
        input_artifacts=(_input_record(tmp_path),),
        allow_external_test_root=True,
        authority_roots=_fixture_context(tmp_path),
        expected_output_root=stage_root,
    )
    marker_path = stage_root / "S1_evidence_universe" / STAGE_RECEIPT_NAME
    assert marker_path.is_file()
    assert STAGE_RECEIPT_NAME not in {item["path"].split("/")[-1] for item in receipt.output_artifacts}
    data = json.loads(marker_path.read_text(encoding="utf-8"))
    assert data["output_artifacts"] == list(receipt.output_artifacts)
