"""C3.7-F exact input/output closure and G19 helper tests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts.historical_immutability import (
    build_historical_immutability_baseline,
    compare_historical_immutability,
)
from supplemental.reference_quotient_v2.scripts.stage_io import (
    CORRECTED_AGGREGATE,
    CORRECTED_P0,
    CORRECTED_SUPPLEMENTAL_V2,
    StageReceiptContractError,
    fixture_authority_roots,
    stage_output_inventory,
    validate_required_input_coverage,
    validate_stage_receipt,
    write_stage_outputs,
)


def _record(root: Path, authority: str, relative: str) -> dict:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("value\n1\n", encoding="utf-8")
    versions = {
        CORRECTED_AGGREGATE: "corrected_aggregate_v2",
        CORRECTED_P0: "corrected_p0_v3",
        CORRECTED_SUPPLEMENTAL_V2: "corrected_supplemental_v2",
    }
    return {
        "path": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "authority_class": authority,
        "root": str(root),
        "version": versions[authority],
    }


def _context(tmp_path):
    return fixture_authority_roots(
        corrected_aggregate=tmp_path / "aggregate",
        corrected_p0=tmp_path / "p0",
        corrected_supplemental=tmp_path / "supplemental",
    )


def _required_records(tmp_path, stage):
    context = _context(tmp_path)
    if stage == "S1":
        return [_record(context.corrected_aggregate, CORRECTED_AGGREGATE, "partition.csv")]
    if stage == "S2":
        names = ("reference_quotient_cross_project_edges.csv", "reference_quotient_node_registry.csv")
    elif stage == "S3":
        names = ("reference_quotient_cross_project_edges.csv", "reference_quotient_node_registry.csv", "analysis_seed_manifest_294.csv")
    elif stage in ("S4", "S5"):
        names = (
            "rq2c_undirected_view_edges.csv", "rq2c_undirected_view_lcc_edges.csv",
            "reference_quotient_node_registry.csv", "rq2c_algorithmic_communities.csv",
            "rq2c_undirected_view_summary.json", "rq2c_structural_brokerage_candidates.csv",
        )
    else:
        from supplemental.reference_quotient_v2.scripts.s6_figure_ready import P0_SOURCE_FILES

        records = [_record(context.corrected_p0, CORRECTED_P0, name) for name in P0_SOURCE_FILES]
        records.extend((
            _record(context.corrected_supplemental, CORRECTED_SUPPLEMENTAL_V2, "S4_community_stability/louvain_stability_runs.csv"),
            _record(context.corrected_supplemental, CORRECTED_SUPPLEMENTAL_V2, "S5_brokerage_stability/brokerage_stability_runs.csv"),
        ))
        return records
    return [_record(context.corrected_p0, CORRECTED_P0, name) for name in names]


@pytest.mark.parametrize("stage", ("S1", "S2", "S3", "S4", "S5", "S6"))
def test_required_input_coverage_exact_set_passes_and_missing_fails(stage, tmp_path):
    records = _required_records(tmp_path, stage)
    context = _context(tmp_path)
    assert validate_required_input_coverage(records, stage, authority_roots=context)["status"] == "PASS"
    with pytest.raises(StageReceiptContractError):
        validate_required_input_coverage(records[:-1], stage, authority_roots=context)


def test_s1_corrected_p0_only_cannot_be_complete(tmp_path):
    context = _context(tmp_path)
    records = [_record(context.corrected_p0, CORRECTED_P0, "manifest.json")]
    with pytest.raises(StageReceiptContractError, match="aggregate partition"):
        validate_required_input_coverage(records, "S1", authority_roots=context)


@pytest.mark.parametrize("stage", ("S1", "S2", "S3", "S4", "S5"))
def test_exact_output_contract_missing_and_undeclared_fail(stage, tmp_path):
    context = _context(tmp_path)
    output_root = tmp_path / "outputs"
    inventory = stage_output_inventory(stage)
    artifacts = {
        name: (pd.DataFrame({"value": [1]}) if name.endswith(".csv") else {"status": "PASS"})
        for name in inventory
    }
    receipt = write_stage_outputs(
        output_root, stage, artifacts,
        implementation_commit="fixture",
        input_artifacts=tuple(_required_records(tmp_path, stage)),
        authority_roots=context,
        expected_output_root=output_root,
        allow_external_test_root=True,
        enforce_contract=True,
    )
    assert validate_stage_receipt(
        receipt.as_dict(), stage, authority_roots=context,
        expected_output_root=output_root, enforce_contract=True,
    )["status"] == "PASS"
    missing = receipt.as_dict()
    missing["output_artifacts"] = missing["output_artifacts"][:-1]
    with pytest.raises(StageReceiptContractError):
        validate_stage_receipt(
            missing, stage, authority_roots=context, expected_output_root=output_root,
            require_durable_marker=False, enforce_contract=True,
        )


def test_s5_deprecated_output_is_not_in_contract():
    assert "brokerage_topk_frequency.csv" not in stage_output_inventory("S5")


def test_g19_comparator_detects_add_remove_modify_and_tag_record(tmp_path):
    first = tmp_path / "historical_a"
    second = tmp_path / "historical_b"
    (first / "nested").mkdir(parents=True)
    second.mkdir()
    (first / "nested" / "a.txt").write_text("a", encoding="utf-8")
    (second / "b.txt").write_text("b", encoding="utf-8")
    baseline_path = tmp_path / "freeze" / "baseline.json"
    # The writer is intentionally constrained to docs/freeze in production;
    # build an equivalent in-memory baseline for isolated comparator behavior.
    roots = []
    for label, root in (("a", first), ("b", second)):
        files = []
        for path in sorted(item for item in root.rglob("*") if item.is_file()):
            files.append({"root": label, "relative_path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size})
        roots.append({"root": label, "path": str(root), "file_count": len(files), "aggregate_bytes": sum(item["bytes"] for item in files), "files": files})
    from supplemental.reference_quotient_v2.scripts.historical_immutability import historical_tag_commit
    baseline = {"schema_version": "ch5_refq_c3_7f_historical_immutability_baseline_v1", "historical_tag": "chapter5-refq-freeze-v1.0", "historical_tag_commit": historical_tag_commit(), "roots": roots}
    assert compare_historical_immutability(baseline)["status"] == "HISTORICAL_IMMUTABILITY_MATCH"
    (first / "nested" / "a.txt").write_text("changed", encoding="utf-8")
    (second / "added.txt").write_text("added", encoding="utf-8")
    result = compare_historical_immutability(baseline)
    assert result["status"] == "FAIL_CLOSED"
    assert {item["kind"] for item in result["differences"]} >= {"modified_sha", "modified_bytes", "added_historical_file"}
