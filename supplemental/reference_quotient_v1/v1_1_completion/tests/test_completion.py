from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).parents[4]
COMPLETION = ROOT / "supplemental" / "reference_quotient_v1" / "v1_1_completion"
OUTPUT = COMPLETION / "outputs"


def test_edge_class_tables_close_exactly():
    validation = json.loads((OUTPUT / "completion_scan_validation.json").read_text(encoding="utf-8"))
    assert validation["edge_class_exact_reconciliation"]
    assert validation["self_loop_records"] == 1447073
    assert validation["cross_project_records"] == 139044
    assert validation["eligible_total"] == 1586117
    for path in (OUTPUT / "S1_evidence_universe").glob("*_x_eligible_edge_class.csv"):
        frame = pd.read_csv(path)
        assert set(frame["eligible_edge_class"]) <= {"SELF_LOOP", "CROSS_PROJECT"}
        assert set(frame["unit"]) == {"REFERENCE_RECORD"}
        assert int(frame["count"].sum()) == 1586117


def test_top_source_target_composition_closes_for_all_50():
    frame = pd.read_csv(OUTPUT / "S7_top_evidence_composition" / "top_source_target_entity_composition.csv", dtype={"project_id": "string"})
    assert frame["project_id"].nunique() == 50
    assert (frame.groupby("project_id")["within_project_share"].sum().sub(1).abs() < 1e-12).all()


def test_frequency_arithmetic_closes():
    frame = pd.read_csv(OUTPUT / "S5_brokerage_stability" / "brokerage_topk_inclusion_frequency.csv")
    assert set(frame["k"]) == {250, 500, 1000}
    assert set(frame["top_k"]) == {10, 20, 50}
    assert (frame["run_count"] == 20).all()
    assert ((frame["inclusion_frequency"] >= 0) & (frame["inclusion_frequency"] <= 1)).all()
    closure = frame.groupby(["k", "top_k"], as_index=False).agg(run_count=("run_count", "first"), inclusion_count=("inclusion_count", "sum"))
    assert (closure["inclusion_count"] == closure["run_count"] * closure["top_k"]).all()


def test_structural_summary_csv_is_byte_identical_and_manifest_correct():
    old = ROOT / "supplemental" / "reference_quotient_v1" / "outputs" / "S6_figure_ready" / "structural_summary.json"
    new = OUTPUT / "S6_figure_ready" / "structural_summary.csv"
    assert old.read_bytes() == new.read_bytes()
    manifest = json.loads((OUTPUT / "S6_figure_ready" / "figure_ready_manifest_v1_1.json").read_text(encoding="utf-8"))
    entry = next(item for item in manifest["entries"] if item["output"].endswith("structural_summary.csv"))
    assert entry["status"] == "CORRECTED_EXTENSION"


def test_existing_outputs_have_no_hash_drift():
    audit = json.loads((OUTPUT / "existing_output_sha_audit.json").read_text(encoding="utf-8"))
    assert audit["drift"] is False


def test_completion_manifest_protects_baselines():
    manifest = json.loads((ROOT / "supplemental" / "reference_quotient_v1" / "v1_1_completion_manifest.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "PASS"
    assert manifest["scientific_baseline_changed"] is False
    assert manifest["canonical_result_changed"] is False
    assert manifest["network_algorithms_rerun"] is False
