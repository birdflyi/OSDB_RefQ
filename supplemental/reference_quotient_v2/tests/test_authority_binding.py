"""C3.7-E.2 authority-root and stage-root binding regression tests."""

from __future__ import annotations

import copy
import hashlib

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.manifest import (
    ManifestContractError,
    build_corrected_package_manifest,
    validate_package_manifest,
)
from supplemental.reference_quotient_v2.scripts.s6_figure_ready import (
    CORRECTED_P0,
    CORRECTED_SUPPLEMENTAL_V2,
    S6ContractError,
    serialize_s6_figure_ready_bundle,
    validate_s6_manifest_sha_closure,
)
from supplemental.reference_quotient_v2.scripts.stage_io import (
    AuthorityRoots,
    CORRECTED_AGGREGATE,
    StageIOError,
    StageReceiptContractError,
    StageReceiptContractError,
    fixture_authority_roots,
    production_authority_roots,
    validate_input_artifact_records,
    validate_stage_receipt,
)
from supplemental.reference_quotient_v2.tests.test_manifest_v2 import _valid_package
from supplemental.reference_quotient_v2.tests.test_s6_figure_ready import _fixture


def _context(tmp_path):
    return fixture_authority_roots(
        corrected_aggregate=tmp_path / "aggregate",
        corrected_p0=tmp_path / "p0",
        corrected_supplemental=tmp_path / "supplemental",
    )


def _record(root, authority, relative):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("value\n1\n", encoding="utf-8")
    return {
        "path": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "authority_class": authority,
        "root": str(root),
        "version": {
            CORRECTED_P0: "corrected_p0_v3",
            CORRECTED_SUPPLEMENTAL_V2: "corrected_supplemental_v2",
            CORRECTED_AGGREGATE: "corrected_aggregate_v2",
        }[authority],
    }


def test_production_authority_roots_are_derived_from_config():
    context = production_authority_roots()
    assert context.fixture is False
    assert context.corrected_p0 == paths.CORRECTED_P0_ROOT
    assert context.corrected_supplemental == paths.CORRECTED_OUTPUTS_ROOT
    assert context.corrected_aggregate == paths.canonical_path(
        paths.load_config()["corrected_aggregate_root"]
    )


def test_arbitrary_temp_p0_is_rejected_in_production_context(tmp_path):
    record = _record(tmp_path / "arbitrary", CORRECTED_P0, "not_p0.csv")
    with pytest.raises(StageReceiptContractError, match="root does not match authority class"):
        validate_input_artifact_records([record], "S1")


def test_same_fixture_is_accepted_only_with_explicit_fixture_context(tmp_path):
    context = _context(tmp_path)
    record = _record(context.corrected_p0, CORRECTED_P0, "source.csv")
    assert validate_input_artifact_records([record], "S1", authority_roots=context)["status"] == "PASS"


def test_external_test_root_requires_explicit_fixture_context(tmp_path):
    record = _record(tmp_path / "p0", CORRECTED_P0, "source.csv")
    with pytest.raises(StageIOError, match="explicit fixture authority context"):
        from supplemental.reference_quotient_v2.scripts.stage_io import write_stage_outputs

        write_stage_outputs(
            tmp_path / "outputs",
            "S1",
            {"table.csv": pd.DataFrame({"value": [1]})},
            implementation_commit="fixture",
            input_artifacts=(record,),
            allow_external_test_root=True,
        )


def test_non_fixture_context_cannot_be_hand_constructed_for_arbitrary_roots(tmp_path):
    context = AuthorityRoots(
        corrected_aggregate=tmp_path / "aggregate",
        corrected_p0=tmp_path / "p0",
        corrected_supplemental=tmp_path / "supplemental",
        fixture=False,
    )
    record = _record(context.corrected_p0, CORRECTED_P0, "source.csv")
    with pytest.raises(StageIOError, match="production authority roots"):
        validate_input_artifact_records([record], "S1", authority_roots=context)


def test_declared_root_cannot_override_p0_authority_root(tmp_path):
    context = _context(tmp_path)
    record = _record(context.corrected_p0, CORRECTED_P0, "source.csv")
    record["root"] = str(tmp_path / "override")
    with pytest.raises(StageReceiptContractError, match="root does not match authority class"):
        validate_input_artifact_records([record], "S1", authority_roots=context)


@pytest.mark.parametrize("authority,relative", [(CORRECTED_AGGREGATE, "aggregate.csv"), (CORRECTED_P0, "p0.csv")])
def test_authority_path_outside_configured_root_is_rejected(tmp_path, authority, relative):
    context = _context(tmp_path)
    record = _record(tmp_path / "outside", authority, relative)
    with pytest.raises(StageReceiptContractError, match="root does not match authority class"):
        validate_input_artifact_records([record], "S1", authority_roots=context)


def test_supplemental_path_outside_configured_root_is_rejected(tmp_path):
    context = _context(tmp_path)
    record = _record(tmp_path / "outside", CORRECTED_SUPPLEMENTAL_V2, "S4_community_stability/runs.csv")
    with pytest.raises(StageReceiptContractError, match="root does not match authority class"):
        validate_input_artifact_records([record], "S6", authority_roots=context)


@pytest.mark.parametrize(
    "stage",
    ["S2_weight_sensitivity", "S3_observation_sensitivity", "S4_community_stability", "S5_brokerage_stability"],
)
def test_s2_to_s5_reject_supplemental_authority(stage, tmp_path):
    context = _context(tmp_path)
    record = _record(context.corrected_supplemental, CORRECTED_SUPPLEMENTAL_V2, "declared.csv")
    with pytest.raises(StageReceiptContractError, match="authority is not allowed"):
        validate_input_artifact_records([record], stage, authority_roots=context)


def test_s6_accepts_p0_and_exact_s4_s5_sources(tmp_path):
    context = _context(tmp_path)
    records = [
        _record(context.corrected_p0, CORRECTED_P0, "p0.csv"),
        _record(context.corrected_supplemental, CORRECTED_SUPPLEMENTAL_V2, "S4_community_stability/louvain_stability_runs.csv"),
        _record(context.corrected_supplemental, CORRECTED_SUPPLEMENTAL_V2, "S5_brokerage_stability/brokerage_stability_runs.csv"),
    ]
    assert validate_input_artifact_records(records, "S6", authority_roots=context)["status"] == "PASS"


@pytest.mark.parametrize("relative", ["S4_community_stability/other.csv", "S1_evidence_universe/stage.csv"])
def test_s6_rejects_undeclared_supplemental_sources(tmp_path, relative):
    context = _context(tmp_path)
    record = _record(context.corrected_supplemental, CORRECTED_SUPPLEMENTAL_V2, relative)
    with pytest.raises(StageReceiptContractError, match="approved source map"):
        validate_input_artifact_records([record], "S6", authority_roots=context)


def test_production_receipt_output_root_cannot_be_self_declared(tmp_path):
    context = production_authority_roots()
    p0_path = paths.CORRECTED_P0_ROOT / "manifest.json"
    record = {
        "path": str(p0_path),
        "sha256": hashlib.sha256(p0_path.read_bytes()).hexdigest(),
        "authority_class": CORRECTED_P0,
        "root": str(paths.CORRECTED_P0_ROOT),
        "version": "corrected_p0_v3",
    }
    receipt = {
        "stage": "S1_evidence_universe",
        "status": "PASS",
        "implementation_commit": "fixture",
        "input_artifacts": [record],
        "output_artifacts": [{"path": "S1_evidence_universe/x.csv", "sha256": "0" * 64, "bytes": 1, "row_count": 1}],
        "parameters": {},
        "runtime_versions": {"python": "fixture"},
        "completed_at": "fixture",
        "output_root": str(tmp_path / "self_declared_output"),
    }
    with pytest.raises(StageReceiptContractError, match="production receipt output_root"):
        validate_stage_receipt(receipt, "S1", authority_roots=context)


def test_s6_manifest_rejects_arbitrary_supplemental_source(tmp_path):
    p0_root, supplemental_root, source_bundle = _fixture(tmp_path)
    context = fixture_authority_roots(
        corrected_aggregate=tmp_path / "aggregate",
        corrected_p0=p0_root,
        corrected_supplemental=supplemental_root,
    )
    _, _, manifest = serialize_s6_figure_ready_bundle(
        source_bundle,
        tmp_path / "output",
        implementation_commit="fixture",
        authority_roots=context,
        expected_output_root=tmp_path / "output",
        allow_external_test_root=True,
    )
    fake = supplemental_root / "S4_community_stability" / "not_declared.csv"
    fake.write_text("value\n1\n", encoding="utf-8")
    tampered = copy.deepcopy(manifest)
    entry = next(item for item in tampered["entries"] if item["output"] == "louvain_stability_plot.csv")
    source = entry["source_artifacts"][0]
    source["path"] = str(fake)
    source["sha256"] = hashlib.sha256(fake.read_bytes()).hexdigest()
    with pytest.raises(S6ContractError, match="approved source map"):
        validate_s6_manifest_sha_closure(
            tampered,
            manifest_directory=tmp_path / "output" / "S6_figure_ready",
        )


def test_s6_manifest_authority_roots_can_be_checked_against_explicit_context(tmp_path):
    p0_root, supplemental_root, source_bundle = _fixture(tmp_path)
    context = fixture_authority_roots(
        corrected_aggregate=tmp_path / "aggregate",
        corrected_p0=p0_root,
        corrected_supplemental=supplemental_root,
    )
    _, _, manifest = serialize_s6_figure_ready_bundle(
        source_bundle,
        tmp_path / "output",
        implementation_commit="fixture",
        authority_roots=context,
        expected_output_root=tmp_path / "output",
        allow_external_test_root=True,
    )
    assert validate_s6_manifest_sha_closure(
        manifest,
        manifest_directory=tmp_path / "output" / "S6_figure_ready",
        authority_roots=context,
    )["status"] == "PASS"


def test_s6_closure_rejects_hand_constructed_non_fixture_context(tmp_path):
    context = AuthorityRoots(
        corrected_aggregate=tmp_path / "aggregate",
        corrected_p0=tmp_path / "p0",
        corrected_supplemental=tmp_path / "supplemental",
        fixture=False,
    )
    with pytest.raises(S6ContractError, match="production S6 authority roots"):
        validate_s6_manifest_sha_closure({}, authority_roots=context)


def test_production_build_cannot_complete_from_external_fixture_receipts(tmp_path):
    fixture_manifest = _valid_package(tmp_path)
    config = paths.load_config()
    rebuilt = build_corrected_package_manifest(
        config,
        fixture_manifest["stage_receipts"],
        implementation_commit="fixture",
        branch="fixture",
        historical_write_audit=fixture_manifest["historical_write_audit"],
    )
    assert rebuilt["status"] == "STAGE_PACKAGE_INCOMPLETE"
    with pytest.raises(ManifestContractError, match="package output root"):
        validate_package_manifest(fixture_manifest)


def test_production_receipt_root_mismatch_is_rejected_even_when_package_root_is_correct(tmp_path):
    fixture_manifest = _valid_package(tmp_path)
    tampered = copy.deepcopy(fixture_manifest)
    tampered["corrected_output_root"] = str(paths.CORRECTED_OUTPUTS_ROOT)
    with pytest.raises(ManifestContractError, match="stage receipt closure"):
        validate_package_manifest(tampered)


def test_explicit_fixture_package_context_validates_synthetic_package(tmp_path):
    fixture_manifest = _valid_package(tmp_path)
    context = fixture_authority_roots(
        corrected_aggregate=tmp_path / "corrected_aggregate_fixture",
        corrected_p0=tmp_path / "corrected_p0",
        corrected_supplemental=tmp_path / "corrected_supplemental_v2_outputs",
    )
    result = validate_package_manifest(
        fixture_manifest,
        authority_roots=context,
        expected_output_root=tmp_path / "stage_outputs",
    )
    assert result["stage_package_complete"] is True


def test_fixture_package_root_mismatch_is_rejected_when_explicitly_expected(tmp_path):
    fixture_manifest = _valid_package(tmp_path)
    context = fixture_authority_roots(
        corrected_aggregate=tmp_path / "corrected_aggregate_fixture",
        corrected_p0=tmp_path / "corrected_p0",
        corrected_supplemental=tmp_path / "corrected_supplemental_v2_outputs",
    )
    with pytest.raises(ManifestContractError, match="expected output root"):
        validate_package_manifest(
            fixture_manifest,
            authority_roots=context,
            expected_output_root=tmp_path / "wrong_package_root",
        )
