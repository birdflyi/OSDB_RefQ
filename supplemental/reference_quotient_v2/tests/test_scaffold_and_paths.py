"""C3.7-A tests for scaffold boundaries only.

These tests do not execute P0, S1-S7, aggregate scans, or network routines.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from supplemental.reference_quotient_v2.scripts import manifest, paths, schema
from supplemental.reference_quotient_v2.scripts.run_supplemental_v2 import main


CONFIG_PATH = paths.DEFAULT_CONFIG_PATH


@pytest.fixture()
def config():
    return paths.load_config(CONFIG_PATH)


def test_v2_config_loads(config):
    assert config["schema_version"] == "supplemental_v2_corrected_scaffold_v1"
    assert config["corrected_p0_root"] == "outputs/reference_quotient_p0_corrected_v2"


def test_corrected_p0_root_resolves_to_corrected_v2(config):
    resolved = paths.validate_config_paths(config)
    assert resolved["corrected_p0_root"] == paths.CORRECTED_P0_ROOT


def test_historical_p0_root_is_explicit_comparison_only(config):
    historical = paths.validate_comparison_only(config["historical_p0_root"], comparison_only=True, config=config)
    assert historical == paths.HISTORICAL_P0_ROOT
    assert paths.classify_path(historical, config).role == paths.AuthorityRole.COMPARISON_ONLY_HISTORICAL


def test_historical_supplemental_root_is_explicit_comparison_only(config):
    historical = paths.validate_comparison_only(config["historical_supplemental_root"], comparison_only=True, config=config)
    assert historical == paths.HISTORICAL_SUPPLEMENTAL_ROOT
    assert paths.classify_path(historical, config).comparison_only is True


def test_corrected_output_root_is_v2_only(config):
    output = paths.validate_corrected_output_root(config)
    assert output == paths.CORRECTED_OUTPUTS_ROOT
    assert paths.classify_path(output, config).role == paths.AuthorityRole.WRITE_TARGET


@pytest.mark.parametrize(
    "candidate",
    [
        paths.HISTORICAL_P0_ROOT / "new.csv",
        paths.HISTORICAL_SUPPLEMENTAL_ROOT / "outputs" / "new.csv",
        paths.CORRECTED_P0_ROOT / "new.csv",
    ],
)
def test_protected_roots_rejected_as_write_targets(config, candidate):
    with pytest.raises(paths.PathGuardError):
        paths.validate_write_target(candidate, config)


def test_corrected_aggregate_cannot_be_historical_root(config):
    bad = dict(config)
    bad["corrected_aggregate_root"] = "D:/github_repo/OSDB_RefQ_source_data/data/github_osdb_data/repos_GH_CoRE_ref_node_agg"
    with pytest.raises(paths.PathGuardError):
        paths.validate_config_paths(bad)


def test_stale_p0_entry_point_is_not_executable_authority(config):
    result = manifest.validate_scaffold_provenance(config)
    assert result["entry_point_used_as_authority"] is False
    p0_manifest = manifest.load_json(paths.CORRECTED_P0_ROOT / "manifest.json")
    assert "--execute" in p0_manifest["entry_point"]


def test_corrected_p0_manifest_status_must_be_pass(tmp_path):
    p0_root = tmp_path / "p0"
    p0_root.mkdir()
    manifest_path = p0_root / "manifest.json"
    config_path = paths.REPOSITORY_ROOT / "configs" / "ch5_reference_quotient_p0_v2.yaml"
    manifest_path.write_text(
        json.dumps(
            {
                "status": "FAIL",
                "output_directory": str(p0_root),
                "config": {"path": str(config_path), "sha256": manifest.sha256_file(config_path)},
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(paths.PathGuardError, match="status must be PASS"):
        manifest.validate_corrected_p0_manifest(manifest_path, p0_root, config_path)


def test_corrected_p0_config_hash_validation_works(config):
    result = manifest.validate_scaffold_provenance(config)
    assert result["corrected_p0_config_sha256"] == "e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658"
    with pytest.raises(paths.PathGuardError, match="SHA-256"):
        manifest.validate_corrected_p0_manifest(
            paths.CORRECTED_P0_ROOT / "manifest.json",
            paths.CORRECTED_P0_ROOT,
            paths.REPOSITORY_ROOT / "configs" / "ch5_reference_quotient_p0_v2.yaml",
            expected_config_sha256="0" * 64,
        )


def test_source_admission_vocabulary_is_exactly_frozen_four():
    assert schema.SOURCE_ADMISSION_STATUSES == (
        "ADMITTED_SOURCE_OBSERVATION",
        "OUT_OF_SEED_SOURCE_OBSERVATION",
        "MISSING_EVENT_REPOSITORY_ID",
        "INVALID_EVENT_REPOSITORY_ID",
    )
    assert len(schema.SOURCE_ADMISSION_STATUS_SET) == 4


def test_unknown_admission_status_fails_closed():
    with pytest.raises(schema.SchemaContractError):
        schema.validate_source_admission_status("UNKNOWN_STATUS")


def test_orchestrator_blocks_scientific_stage_execution(tmp_path):
    before = paths.CORRECTED_OUTPUTS_ROOT.exists()
    assert main(["--run-s1"]) == 2
    assert paths.CORRECTED_OUTPUTS_ROOT.exists() is before
    assert not (tmp_path / "outputs").exists()


def test_s7_has_no_active_execution_path():
    assert main(["--run-s7"]) == 2
    assert not paths.CORRECTED_OUTPUTS_ROOT.exists()


def test_scaffold_validation_does_not_create_outputs(config):
    assert not paths.CORRECTED_OUTPUTS_ROOT.exists()
    manifest.validate_scaffold_provenance(config)
    assert not paths.CORRECTED_OUTPUTS_ROOT.exists()


def test_windows_traversal_cannot_bypass_historical_write_protection(config):
    traversal = paths.V2_ROOT / "outputs" / ".." / ".." / "reference_quotient_v1" / "outputs" / "new.csv"
    with pytest.raises(paths.PathGuardError):
        paths.validate_write_target(traversal, config)


def test_required_schema_fields_are_contract_only():
    fields = schema.REQUIRED_CORRECTED_AGGREGATE_PROVENANCE_FIELDS
    assert schema.validate_required_fields(fields) == fields
    assert "event_repo_id" in fields
    assert "expected_source_context_repo_id" in fields
    assert "source_admission_status" in fields
    assert "source_provenance_mismatch" in fields


def test_show_plan_is_non_executable(capsys):
    assert main(["--show-plan"]) == 0
    output = capsys.readouterr().out
    assert "S1 -> S2 -> S3 -> S4/S5 -> S6" in output
    assert "NOT_AUTHORIZED_IN_C3_7A" in output
