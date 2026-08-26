"""C3.7-E temporary-directory tests for controlled stage serialization."""

from __future__ import annotations

import json

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.stage_io import (
    StageIOError,
    serialize_artifact,
    validate_output_artifact_records,
    write_stage_outputs,
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
    receipt = write_stage_outputs(
        output_root,
        "S6",
        {"table.csv": pd.DataFrame({"value": [1, 2]})},
        implementation_commit="fixture",
        completed_at="2026-08-26T00:00:00+00:00",
    )
    assert output_root.is_dir()
    assert (output_root / "S6_figure_ready" / "table.csv").is_file()
    assert receipt.stage == "S6_figure_ready"
    assert receipt.output_artifacts[0]["row_count"] == 2
    with pytest.raises(StageIOError, match="overwrite"):
        write_stage_outputs(output_root, "S6", {"table.csv": pd.DataFrame({"value": [3]})})


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
    receipt = write_stage_outputs(
        tmp_path / "outputs",
        "S2",
        {"table.csv": pd.DataFrame({"value": [1, 2, 3]})},
    )
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
        write_stage_outputs(tmp_path / "outputs", "S7", {"table.csv": pd.DataFrame({"x": [1]})})
    with pytest.raises(StageIOError, match="simple filenames"):
        write_stage_outputs(tmp_path / "outputs", "S6", {"nested/table.csv": pd.DataFrame({"x": [1]})})
