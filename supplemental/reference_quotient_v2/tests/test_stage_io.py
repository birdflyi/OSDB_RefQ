"""C3.7-E temporary-directory tests for controlled stage serialization."""

from __future__ import annotations

import hashlib
import json

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.stage_io import (
    CORRECTED_P0,
    STAGE_RECEIPT_NAME,
    StageIOError,
    StageReceiptContractError,
    fixture_authority_roots,
    load_stage_receipt,
    serialize_artifact,
    validate_stage_receipt,
    validate_output_artifact_records,
    write_stage_outputs,
)


def _input_artifacts(tmp_path):
    root = tmp_path / "corrected_p0_fixture"
    root.mkdir(exist_ok=True)
    source = root / "source.csv"
    source.write_text("value\n1\n", encoding="utf-8")
    return (
        {
            "path": str(source),
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "authority_class": CORRECTED_P0,
            "root": str(root),
            "version": "corrected_p0_v2",
        },
    )


def _fixture_context(tmp_path):
    return fixture_authority_roots(
        corrected_aggregate=tmp_path / "corrected_aggregate_fixture",
        corrected_p0=tmp_path / "corrected_p0_fixture",
        corrected_supplemental=tmp_path / "corrected_supplemental_fixture",
    )


def _write(tmp_path, stage="S6", frame=None, output_root=None):
    target = output_root or tmp_path / "outputs"
    return write_stage_outputs(
        target,
        stage,
        {"table.csv": frame if frame is not None else pd.DataFrame({"value": [1, 2]})},
        implementation_commit="fixture",
        input_artifacts=_input_artifacts(tmp_path),
        completed_at="2026-08-26T00:00:00+00:00",
        allow_external_test_root=True,
        authority_roots=_fixture_context(tmp_path),
        expected_output_root=target,
    )


def test_deterministic_csv_and_json_serialization():
    frame = pd.DataFrame({"b": [2, 1], "a": ["x", "y"]})
    first = serialize_artifact("table.csv", frame)
    second = serialize_artifact("table.csv", frame)
    assert first.payload == second.payload
    assert first.row_count == 2
    assert first.bytes == len(first.payload)

    json_first = serialize_artifact("meta.json", {"z": 1, "a": [2, 1]})
    json_second = serialize_artifact("meta.json", {"a": [2, 1], "z": 1})
    assert json_first.payload == json_second.payload
    assert json.loads(json_first.payload.decode("utf-8")) == {"a": [2, 1], "z": 1}
    assert json_first.row_count is None


def test_stage_writer_allows_parent_but_rejects_existing_stage(tmp_path):
    output_root = tmp_path / "outputs"
    receipt = _write(tmp_path, output_root=output_root)
    assert output_root.is_dir()
    assert (output_root / "S6_figure_ready" / "table.csv").is_file()
    assert receipt.stage == "S6_figure_ready"
    assert receipt.output_artifacts[0]["row_count"] == 2
    assert (output_root / "S6_figure_ready" / STAGE_RECEIPT_NAME).is_file()
    assert load_stage_receipt(output_root / "S6_figure_ready")["stage"] == "S6_figure_ready"
    assert validate_stage_receipt(
        receipt.as_dict(),
        "S6",
        authority_roots=_fixture_context(tmp_path),
        expected_output_root=output_root,
    )["status"] == "PASS"
    with pytest.raises(StageIOError, match="overwrite"):
        _write(tmp_path, output_root=output_root, frame=pd.DataFrame({"value": [3]}))


def test_stage_writer_rejects_protected_and_undeclared_repository_roots(tmp_path):
    with pytest.raises(StageIOError):
        write_stage_outputs(paths.CORRECTED_P0_ROOT, "S6", {"table.csv": pd.DataFrame({"x": [1]})})
    with pytest.raises(StageIOError):
        write_stage_outputs(paths.HISTORICAL_P0_ROOT, "S6", {"table.csv": pd.DataFrame({"x": [1]})})
    with pytest.raises(StageIOError):
        write_stage_outputs(paths.HISTORICAL_SUPPLEMENTAL_ROOT, "S6", {"table.csv": pd.DataFrame({"x": [1]})})
    with pytest.raises(StageIOError):
        write_stage_outputs(paths.REPOSITORY_ROOT / "undeclared_outputs", "S6", {"table.csv": pd.DataFrame({"x": [1]})})


def test_stage_writer_records_and_validates_sha_bytes_and_rows(tmp_path):
    receipt = _write(tmp_path, stage="S2", frame=pd.DataFrame({"value": [1, 2, 3]}))
    result = validate_output_artifact_records(tmp_path / "outputs", receipt.output_artifacts)
    assert result["status"] == "PASS"
    assert result["checked"][0]["bytes"] == receipt.output_artifacts[0]["bytes"]
    bad = dict(receipt.output_artifacts[0])
    bad["sha256"] = "0" * 64
    with pytest.raises(StageIOError, match="SHA"):
        validate_output_artifact_records(tmp_path / "outputs", [bad])

    assert validate_output_artifact_records(
        tmp_path / "outputs", {"table.csv": receipt.output_artifacts[0]}
    )["status"] == "PASS"
    with pytest.raises(StageIOError, match="mapping"):
        validate_output_artifact_records(tmp_path / "outputs", {"table.csv": "invalid"})
    invalid_bytes = dict(receipt.output_artifacts[0])
    invalid_bytes["bytes"] = "not-an-integer"
    with pytest.raises(StageIOError, match="byte count"):
        validate_output_artifact_records(tmp_path / "outputs", invalid_bytes)


def test_stage_name_and_artifact_path_guards(tmp_path):
    with pytest.raises(StageIOError, match="S1-S6"):
        write_stage_outputs(
            tmp_path / "outputs", "S7", {"table.csv": pd.DataFrame({"x": [1]})},
            implementation_commit="fixture", input_artifacts=_input_artifacts(tmp_path), allow_external_test_root=True,
            authority_roots=_fixture_context(tmp_path), expected_output_root=tmp_path / "outputs",
        )
    with pytest.raises(StageIOError, match="simple filenames"):
        write_stage_outputs(
            tmp_path / "outputs", "S6", {"nested/table.csv": pd.DataFrame({"x": [1]})},
            implementation_commit="fixture", input_artifacts=_input_artifacts(tmp_path), allow_external_test_root=True,
            authority_roots=_fixture_context(tmp_path), expected_output_root=tmp_path / "outputs",
        )


def test_external_root_requires_explicit_opt_in_and_production_root_is_accepted(tmp_path):
    with pytest.raises(StageIOError, match="exactly corrected v2 outputs"):
        write_stage_outputs(
            tmp_path / "outputs", "S6", {"table.csv": pd.DataFrame({"x": [1]})},
            implementation_commit="fixture", input_artifacts=_input_artifacts(tmp_path),
        )
    receipt = _write(tmp_path, output_root=tmp_path / "explicit_test_outputs")
    assert receipt.status == "PASS"

    # Authority validation happens before any production directory is created.
    from supplemental.reference_quotient_v2.scripts.stage_io import _safe_output_root

    assert _safe_output_root(paths.CORRECTED_OUTPUTS_ROOT) == paths.canonical_path(paths.CORRECTED_OUTPUTS_ROOT)
    assert paths.CORRECTED_OUTPUTS_ROOT.exists() is True


def test_missing_durable_marker_is_partial_and_cannot_be_retried(tmp_path):
    receipt = _write(tmp_path)
    marker = tmp_path / "outputs" / "S6_figure_ready" / STAGE_RECEIPT_NAME
    marker.unlink()
    with pytest.raises(StageReceiptContractError, match="missing"):
        validate_stage_receipt(
            receipt.as_dict(),
            "S6",
            authority_roots=_fixture_context(tmp_path),
        )
    with pytest.raises(StageIOError, match="overwrite"):
        _write(tmp_path)


def test_tampered_durable_marker_fails_closed(tmp_path):
    receipt = _write(tmp_path)
    marker = tmp_path / "outputs" / "S6_figure_ready" / STAGE_RECEIPT_NAME
    durable = json.loads(marker.read_text(encoding="utf-8"))
    durable["parameters"] = {"tampered": True}
    marker.write_text(json.dumps(durable), encoding="utf-8")
    with pytest.raises(StageReceiptContractError, match="does not match"):
        validate_stage_receipt(
            receipt.as_dict(),
            "S6",
            authority_roots=_fixture_context(tmp_path),
        )


def test_relative_input_path_is_resolved_against_declared_root(tmp_path):
    root = tmp_path / "relative_input"
    root.mkdir()
    source = root / "source.csv"
    source.write_text("value\n1\n", encoding="utf-8")
    record = {
        "path": "source.csv",
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "authority_class": CORRECTED_P0,
        "root": str(root),
        "version": "corrected_p0_v2",
    }
    write_stage_outputs(
        tmp_path / "relative_outputs",
        "S1",
        {"table.csv": pd.DataFrame({"value": [1]})},
        implementation_commit="fixture",
        input_artifacts=(record,),
        allow_external_test_root=True,
        authority_roots=fixture_authority_roots(
            corrected_aggregate=tmp_path / "aggregate",
            corrected_p0=root,
            corrected_supplemental=tmp_path / "supplemental",
        ),
        expected_output_root=tmp_path / "relative_outputs",
    )
