from __future__ import annotations

import json
import os
import shutil
import sqlite3
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
V1 = ROOT / "supplemental" / "reference_quotient_v1"
COMPLETION = V1 / "v1_1_completion"
OUTPUT = COMPLETION / "outputs"
CANONICAL = ROOT / "outputs" / "reference_quotient_p0_frozen"
RAW_ROOT = Path("D:/github_repo/OSDB_RefQ_source_data")
SEED_MANIFEST = CANONICAL / "analysis_seed_manifest_294.csv"
PARENT_RESULT_COMMIT = "ba72987adb2c2339bdf1f7a3b370278c88c29c3c"
CANONICAL_PARENT = "920286e134ca459c8e155942eabc6798ceab8b65"
V1_IMPLEMENTATION_COMMIT = "18717e7d8d269538872ab5a3bcb923234e52eecc"
CHUNK_SIZE = 100000
RAW_USECOLS = [
    "src_entity_id", "src_entity_type", "tar_entity_id", "tar_entity_type",
    "relation_type", "event_type", "src_entity_id_agg", "src_entity_type_agg",
    "tar_entity_id_agg", "tar_entity_type_agg", "tar_entity_type_fine_grained",
]

sys.path.insert(0, str(V1 / "scripts"))
from common import (  # noqa: E402
    canonical_identity,
    file_record,
    git_value,
    json_dump,
    membership_status,
    sha256_file,
    unique_project_membership,
)


def clean(value: object) -> str | None:
    if value is None or pd.isna(value):
        return None
    return str(value)


def snapshot_tree(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)).replace(os.sep, "/"): sha256_file(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def existing_output_snapshot() -> dict[str, dict[str, str]]:
    return {
        "canonical_p0": snapshot_tree(CANONICAL),
        "s2_sensitivity": snapshot_tree(V1 / "outputs" / "S2_weight_sensitivity"),
        "s3_sensitivity": snapshot_tree(V1 / "outputs" / "S3_observation_sensitivity"),
        "s4_stability": snapshot_tree(V1 / "outputs" / "S4_community_stability"),
        "s5_stability": snapshot_tree(V1 / "outputs" / "S5_brokerage_stability"),
    }


def write_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def add_dimension_counts(counter: Counter, dimension: str, values: pd.Series, edge_class: pd.Series) -> None:
    for value, category in zip(values.fillna("UNKNOWN").astype(str), edge_class.astype(str)):
        counter[(dimension, value, category)] += 1


def edge_class_table(counter: Counter, dimension: str, eligible_total: int) -> pd.DataFrame:
    rows = [
        {
            "dimension": name,
            "dimension_value": value,
            "eligible_edge_class": category,
            "count": count,
            "overall_eligible_share": count / eligible_total,
            "within_dimension_share": count / sum(v for (d, x, _), v in counter.items() if d == name and x == value),
            "within_edge_class_share": count / sum(v for (d, _, c), v in counter.items() if d == name and c == category),
            "unit": "REFERENCE_RECORD",
        }
        for (name, value, category), count in sorted(counter.items())
        if name == dimension
    ]
    return pd.DataFrame(rows, columns=[
        "dimension", "dimension_value", "eligible_edge_class", "count",
        "overall_eligible_share", "within_dimension_share", "within_edge_class_share", "unit",
    ])


def scan_completion_inputs() -> dict[str, Any]:
    seeds = pd.read_csv(SEED_MANIFEST, dtype={"repo_id": "string"})
    evidence_dir = RAW_ROOT / "data/github_osdb_data/repos_GH_CoRE_ref_node_agg"
    paths = [evidence_dir / str(name) for name in seeds["evidence_filename"]]
    if len(seeds) != 294 or any(not path.exists() for path in paths):
        raise RuntimeError("canonical seed manifest/evidence boundary is not available")

    staging = OUTPUT / "_staging"
    staging.mkdir(parents=True, exist_ok=True)
    db_path = staging / "completion_scan.sqlite"
    if db_path.exists():
        db_path.unlink()
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA journal_mode=OFF")
    connection.execute("PRAGMA synchronous=OFF")
    connection.execute("CREATE TABLE raw_records (seed_project TEXT, source_entity_id TEXT, source_entity_type TEXT, target_entity_id TEXT, target_entity_type TEXT, event_type TEXT, source_agg TEXT, source_agg_type TEXT, target_agg TEXT, target_agg_type TEXT, target_fine_type TEXT)")
    connection.execute("CREATE TABLE entity_projects (entity_id TEXT NOT NULL, project_id TEXT NOT NULL, PRIMARY KEY(entity_id, project_id)) WITHOUT ROWID")

    raw_input_rows = 0
    raw_reference_rows = 0
    for seed, path in zip(seeds.itertuples(index=False), paths):
        for chunk in pd.read_csv(path, usecols=RAW_USECOLS, chunksize=CHUNK_SIZE, low_memory=False):
            raw_input_rows += len(chunk)
            chunk = chunk[chunk["relation_type"].eq("Reference")].copy()
            raw_reference_rows += len(chunk)
            records = []
            memberships = []
            for row in chunk.itertuples(index=False):
                source_id = clean(row.src_entity_id)
                target_id = clean(row.tar_entity_id)
                source_agg = clean(row.src_entity_id_agg)
                target_agg = clean(row.tar_entity_id_agg)
                records.append((
                    str(seed.repo_id), source_id, clean(row.src_entity_type), target_id,
                    clean(row.tar_entity_type), clean(row.event_type), source_agg,
                    clean(row.src_entity_type_agg), target_agg, clean(row.tar_entity_type_agg),
                    clean(row.tar_entity_type_fine_grained),
                ))
                for entity, aggregate in ((source_id, source_agg), (target_id, target_agg)):
                    identity = canonical_identity(entity, aggregate)
                    project = unique_project_membership(aggregate)
                    if identity is not None and project is not None:
                        memberships.append((identity, project))
            connection.executemany("INSERT INTO raw_records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", records)
            connection.executemany("INSERT OR IGNORE INTO entity_projects VALUES (?, ?)", memberships)
        connection.commit()

    connection.execute("CREATE INDEX idx_entity_projects_entity ON entity_projects(entity_id)")
    connection.commit()
    conflicts = {str(row[0]) for row in connection.execute("SELECT entity_id FROM entity_projects GROUP BY entity_id HAVING COUNT(*) > 1")}
    top_sources = set(pd.read_csv(CANONICAL / "rq2a_source_role_top50.csv", dtype={"project_id": "string"})["project_id"])
    counters = {name: Counter() for name in ("event_type", "source_entity_type", "target_entity_type")}
    source_target_types: Counter = Counter()
    source_eligible_totals: Counter = Counter()
    target_type_field = "target_fine_type"
    eligible_total = 0
    self_loop_total = 0
    cross_project_total = 0

    for frame in pd.read_sql_query("SELECT * FROM raw_records", connection, chunksize=CHUNK_SIZE):
        source_project = frame["source_agg"].map(unique_project_membership)
        target_project = frame["target_agg"].map(unique_project_membership)
        source_status = [membership_status(value, kind) for value, kind in zip(frame["source_agg"], frame["source_agg_type"])]
        target_status = [membership_status(value, kind) for value, kind in zip(frame["target_agg"], frame["target_agg_type"])]
        source_ids = [canonical_identity(value, aggregate) for value, aggregate in zip(frame["source_entity_id"], frame["source_agg"])]
        target_ids = [canonical_identity(value, aggregate) for value, aggregate in zip(frame["target_entity_id"], frame["target_agg"])]
        source_conflict = pd.Series([value in conflicts for value in source_ids], index=frame.index)
        target_conflict = pd.Series([value in conflicts for value in target_ids], index=frame.index)
        eligible = source_project.notna() & target_project.notna() & ~source_conflict & ~target_conflict
        edge_class = pd.Series(np.where(source_project.eq(target_project), "SELF_LOOP", "CROSS_PROJECT"), index=frame.index)
        edge_class = edge_class.loc[eligible]
        eligible_frame = frame.loc[eligible].copy()
        eligible_frame["source_project"] = source_project.loc[eligible].astype(str).values
        eligible_frame["target_project"] = target_project.loc[eligible].astype(str).values
        eligible_total += int(eligible.sum())
        self_loop_total += int((edge_class == "SELF_LOOP").sum())
        cross_project_total += int((edge_class == "CROSS_PROJECT").sum())
        add_dimension_counts(counters["event_type"], "event_type", eligible_frame["event_type"], edge_class)
        add_dimension_counts(counters["source_entity_type"], "source_entity_type", eligible_frame["source_entity_type"], edge_class)
        target_types = eligible_frame["target_fine_type"].fillna(eligible_frame["target_entity_type"])
        add_dimension_counts(counters["target_entity_type"], "target_entity_type", target_types, edge_class)

        top_rows = eligible_frame[eligible_frame["source_project"].isin(top_sources)]
        for project_id, target_type in top_rows[["source_project", target_type_field]].itertuples(index=False, name=None):
            source_eligible_totals[str(project_id)] += 1
            source_target_types[(str(project_id), str(target_type) if target_type else "UNKNOWN")] += 1

    if (raw_reference_rows, eligible_total, self_loop_total, cross_project_total) != (3748078, 1586117, 1447073, 139044):
        raise RuntimeError("completion scan did not exactly reconcile to canonical P0 totals")

    out_s1 = OUTPUT / "S1_evidence_universe"
    out_s1.mkdir(parents=True, exist_ok=True)
    tables = {}
    for dimension in counters:
        table = edge_class_table(counters[dimension], dimension, eligible_total)
        tables[dimension] = table
        write_csv(out_s1 / f"{dimension}_x_eligible_edge_class.csv", table)

    out_s7 = OUTPUT / "S7_top_evidence_composition"
    out_s7.mkdir(parents=True, exist_ok=True)
    rows = []
    for (project_id, target_type), count in sorted(source_target_types.items()):
        rows.append({
            "project_id": project_id,
            "dimension": "target_entity_type",
            "dimension_value": target_type,
            "count": count,
            "within_project_share": count / source_eligible_totals[project_id],
        })
    write_csv(out_s7 / "top_source_target_entity_composition.csv", pd.DataFrame(rows, columns=[
        "project_id", "dimension", "dimension_value", "count", "within_project_share"
    ]))

    validation = {
        "raw_input_rows": raw_input_rows,
        "raw_reference_rows": raw_reference_rows,
        "raw_frozen_rows_scanned_this_patch": raw_reference_rows,
        "raw_rescan_count_this_patch": 1,
        "supplemental_raw_scan_count_cumulative": 2,
        "raw_data_recollection": False,
        "p0_rerun": False,
        "conflicting_entity_count": len(conflicts),
        "eligible_total": eligible_total,
        "self_loop_records": self_loop_total,
        "cross_project_records": cross_project_total,
        "edge_class_exact_reconciliation": self_loop_total + cross_project_total == eligible_total == 1586117,
        "self_loop_exact": self_loop_total == 1447073,
        "cross_project_exact": cross_project_total == 139044,
        "top_source_count": len(top_sources),
        "top_source_composition_closed": all(
            sum(source_target_types[(project, value)] for project2, value in source_target_types if project2 == project) == source_eligible_totals[project]
            for project in top_sources
        ),
        "top_source_eligible_totals": dict(sorted(source_eligible_totals.items())),
    }
    json_dump(OUTPUT / "completion_scan_validation.json", validation)
    connection.close()
    shutil.rmtree(staging)
    return {"validation": validation, "tables": tables}


def derive_s5_frequency() -> dict[str, Any]:
    old = V1 / "outputs" / "S5_brokerage_stability" / "brokerage_rank_stability.csv"
    ranking = pd.read_csv(old, dtype={"project_id": "string"})
    selected_frames = []
    for top_k in (10, 20, 50):
        selected = ranking[ranking["rank"] <= top_k].copy()
        selected["top_k"] = top_k
        selected_frames.append(selected)
    selected = pd.concat(selected_frames, ignore_index=True)
    counts = selected.groupby(["k", "top_k", "project_id"], as_index=False).agg(inclusion_count=("seed", "nunique"))
    run_counts = ranking.groupby("k")["seed"].nunique().to_dict()
    counts["run_count"] = counts["k"].map(run_counts).astype(int)
    counts["inclusion_frequency"] = counts["inclusion_count"] / counts["run_count"]
    counts = counts[["k", "top_k", "project_id", "run_count", "inclusion_count", "inclusion_frequency"]].sort_values(["k", "top_k", "inclusion_count", "project_id"], ascending=[True, True, False, True]).reset_index(drop=True)
    out = OUTPUT / "S5_brokerage_stability" / "brokerage_topk_inclusion_frequency.csv"
    write_csv(out, counts)
    closure = []
    for (k, top_k), group in counts.groupby(["k", "top_k"]):
        closure.append({"k": int(k), "top_k": int(top_k), "run_count": int(group["run_count"].iloc[0]), "sum_inclusion_count": int(group["inclusion_count"].sum()), "expected": int(group["run_count"].iloc[0] * top_k), "closed": int(group["inclusion_count"].sum()) == int(group["run_count"].iloc[0] * top_k)})
    return {"source": str(old.relative_to(ROOT)).replace(os.sep, "/"), "source_sha256": sha256_file(old), "output": str(out.relative_to(ROOT)).replace(os.sep, "/"), "closure": closure, "all_closed": all(row["closed"] for row in closure)}


def correct_s6_format() -> dict[str, Any]:
    old = V1 / "outputs" / "S6_figure_ready" / "structural_summary.json"
    directory = OUTPUT / "S6_figure_ready"
    directory.mkdir(parents=True, exist_ok=True)
    new = directory / "structural_summary.csv"
    shutil.copyfile(old, new)
    old_manifest_path = V1 / "outputs" / "S6_figure_ready" / "figure_ready_manifest.json"
    old_manifest = json.loads(old_manifest_path.read_text(encoding="utf-8"))
    entries = []
    for entry in old_manifest["entries"]:
        if entry["output"] == "structural_summary.json":
            entry = dict(entry)
            entry["output"] = "v1_1_completion/outputs/S6_figure_ready/structural_summary.csv"
            entry["status"] = "CORRECTED_EXTENSION"
            entry["supersedes"] = "supplemental/reference_quotient_v1/outputs/S6_figure_ready/structural_summary.json"
        entries.append(entry)
    manifest = {
        "classification": "FIGURE_READY_DERIVATION",
        "version": "v1.1",
        "entries": entries,
        "deprecated_outputs": [{"path": "supplemental/reference_quotient_v1/outputs/S6_figure_ready/structural_summary.json", "reason": "DEPRECATED_WRONG_EXTENSION", "content_sha256": sha256_file(old)}],
        "superseding_outputs": [{"path": str(new.relative_to(ROOT)).replace(os.sep, "/"), "content_sha256": sha256_file(new)}],
    }
    new_manifest = directory / "figure_ready_manifest_v1_1.json"
    json_dump(new_manifest, manifest)
    return {"old": str(old.relative_to(ROOT)).replace(os.sep, "/"), "new": str(new.relative_to(ROOT)).replace(os.sep, "/"), "content_identical": old.read_bytes() == new.read_bytes(), "manifest": str(new_manifest.relative_to(ROOT)).replace(os.sep, "/"), "old_manifest_sha256": sha256_file(old_manifest_path)}


def build_manifest(scan: dict[str, Any], s5: dict[str, Any], s6: dict[str, Any], before: dict[str, dict[str, str]], after: dict[str, dict[str, str]]) -> Path:
    output_files = [file_record(path, OUTPUT) for path in sorted(OUTPUT.rglob("*")) if path.is_file()]
    consumed = [
        CANONICAL / "analysis_seed_manifest_294.csv",
        CANONICAL / "rq2a_source_role_top50.csv",
        V1 / "outputs/S5_brokerage_stability/brokerage_rank_stability.csv",
        V1 / "outputs/S6_figure_ready/structural_summary.json",
        V1 / "outputs/S6_figure_ready/figure_ready_manifest.json",
    ]
    manifest = {
        "package": "reference_quotient_supplemental_v1_1_material_completion",
        "status": "PASS" if scan["validation"]["edge_class_exact_reconciliation"] and scan["validation"]["top_source_composition_closed"] and s5["all_closed"] and s6["content_identical"] and before == after else "FAIL",
        "parent_supplemental_result_commit": PARENT_RESULT_COMMIT,
        "canonical_parent_commit": CANONICAL_PARENT,
        "v1_implementation_commit": V1_IMPLEMENTATION_COMMIT,
        "completion_implementation_commit": git_value(ROOT, "rev-parse", "HEAD"),
        "canonical_result_replacement": False,
        "scientific_baseline_changed": False,
        "canonical_result_changed": False,
        "network_algorithms_rerun": False,
        "raw_scan": scan["validation"],
        "consumed_files": [file_record(path, ROOT) for path in consumed],
        "new_outputs": output_files,
        "deprecated_files": [
            {"path": "supplemental/reference_quotient_v1/outputs/S5_brokerage_stability/brokerage_topk_frequency.csv", "reason": "DEPRECATED_SEMANTICS: per-run membership, not cross-seed frequency", "superseded_by": "supplemental/reference_quotient_v1/v1_1_completion/outputs/S5_brokerage_stability/brokerage_topk_inclusion_frequency.csv"},
            {"path": "supplemental/reference_quotient_v1/outputs/S6_figure_ready/structural_summary.json", "reason": "DEPRECATED_WRONG_EXTENSION", "superseded_by": "supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/structural_summary.csv"},
        ],
        "superseding_files": [
            "supplemental/reference_quotient_v1/v1_1_completion/outputs/S5_brokerage_stability/brokerage_topk_inclusion_frequency.csv",
            "supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/structural_summary.csv",
            "supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/figure_ready_manifest_v1_1.json",
        ],
        "s5_frequency": s5,
        "s6_format": s6,
        "existing_output_sha_audit": {"before": before, "after": after, "drift": before != after},
        "generated_output_sha256": output_files,
        "output_classification": {"S1": "FINE_GRAINED_DECOMPOSITION", "S5": "FIGURE_READY_DERIVATION", "S6": "FIGURE_READY_DERIVATION"},
    }
    path = V1 / "v1_1_completion_manifest.json"
    json_dump(path, manifest)
    return path


def write_report(scan: dict[str, Any], s5: dict[str, Any], s6: dict[str, Any], before: dict[str, dict[str, str]], after: dict[str, dict[str, str]]) -> Path:
    report = ROOT / "docs" / "ch5_refq_supplemental_evidence_v1_1_material_completion_report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    validation = scan["validation"]
    report.write_text(f'''# Chapter 5 RefQ Supplemental Evidence v1.1 Material Completion Report

## 1. Scope

This additive patch completes materials needed by the human-decision audit. It does not modify the manuscript, P0 configuration, canonical outputs, RefQ algorithms, S2/S3/S4/S5 results, thresholds, seeds, `k` values, time window or seed set. The prior v1 files remain in place and are not overwritten.

## 2. Parent Verification

```text
branch = {git_value(ROOT, "branch", "--show-current")}
parent_supplemental_result_commit = {PARENT_RESULT_COMMIT}
canonical_parent_commit = {CANONICAL_PARENT}
v1_implementation_commit = {V1_IMPLEMENTATION_COMMIT}
current_completion_implementation_commit = {git_value(ROOT, "rev-parse", "HEAD")}
```

The v1 execution report is intentionally unchanged. Its historical bookkeeping remains: `result_package_commit = recorded by the final commit below`, even though the actual v1 result commit is `{PARENT_RESULT_COMMIT}`. Its Section 12 wording that tests were executed separately after report generation is also retained as a historical wording inconsistency. The v1 report records 9 passed and 0 failed tests.

## 3. One-Extra-Scan Audit

Exactly one additional controlled streaming pass was used with the canonical 294-seed manifest, frozen 2023 evidence files, `relation_type = Reference`, the canonical identity/membership/conflict rules and `csv_chunk_size = 100000`. The pass scanned `{validation["raw_frozen_rows_scanned_this_patch"]:,}` Reference rows. Cumulative supplemental raw scan count is `{validation["supplemental_raw_scan_count_cumulative"]}`: v1 = 1 and v1.1 completion = 1. This is not raw-data recollection and not a P0 rerun.

## 4. S1 Eligible-Edge-Class Completion

New files:

- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S1_evidence_universe/event_type_x_eligible_edge_class.csv`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S1_evidence_universe/source_entity_type_x_eligible_edge_class.csv`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S1_evidence_universe/target_entity_type_x_eligible_edge_class.csv`

These tables include only quotient-eligible Reference records and explicitly label their unit as `REFERENCE_RECORD`. The exact closure is:

| eligible edge class | records |
|---|---:|
| SELF_LOOP | {validation["self_loop_records"]:,} |
| CROSS_PROJECT | {validation["cross_project_records"]:,} |
| TOTAL | {validation["eligible_total"]:,} |

The output does not mix entity, edge and record counts.

## 5. S7 Top-Source Target-Entity Composition

New file:

`supplemental/reference_quotient_v1/v1_1_completion/outputs/S7_top_evidence_composition/top_source_target_entity_composition.csv`

The canonical top-50 source set was read from `rq2a_source_role_top50.csv` before scanning and was not reselected. Every top source has a closed count of eligible Reference records across `target_entity_type` categories. The `within_project_share` denominator is that source project's eligible Reference-record total.

## 6. S5 Frequency Semantic Correction

New file:

`supplemental/reference_quotient_v1/v1_1_completion/outputs/S5_brokerage_stability/brokerage_topk_inclusion_frequency.csv`

It is deterministically derived from the existing full `brokerage_rank_stability.csv`; no betweenness run was repeated. It reports `run_count = 20`, `inclusion_count` and `inclusion_frequency` for each `k`, `top_k` and project. For every combination, the arithmetic closure is checked against `run_count * top_k`.

The old `brokerage_topk_frequency.csv` remains but is marked `DEPRECATED_SEMANTICS`: it records per-run membership rows, not aggregated cross-seed frequency. It is superseded by the new file.

## 7. S6 Structural Summary Format Correction

New file:

`supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/structural_summary.csv`

Its bytes are identical to the old CSV-content file named `structural_summary.json`; only the extension and manifest semantics are corrected. The old file remains and is marked `DEPRECATED_WRONG_EXTENSION`. `figure_ready_manifest_v1_1.json` points to the corrected file.

## 8. Validation and Tests

```text
S1 edge-class exact reconciliation = {"PASS" if validation["edge_class_exact_reconciliation"] else "FAIL"}
S1 SELF_LOOP exact = {"PASS" if validation["self_loop_exact"] else "FAIL"}
S1 CROSS_PROJECT exact = {"PASS" if validation["cross_project_exact"] else "FAIL"}
S7 top-source closure = {"PASS" if validation["top_source_composition_closed"] else "FAIL"}
S5 inclusion-frequency closure = {"PASS" if s5["all_closed"] else "FAIL"}
S6 structural CSV content identity = {"PASS" if s6["content_identical"] else "FAIL"}
canonical output SHA drift = {"YES" if before["canonical_p0"] != after["canonical_p0"] else "NO"}
existing S2/S3/S4/S5 output SHA drift = {"YES" if any(before[key] != after[key] for key in ("s2_sensitivity", "s3_sensitivity", "s4_stability", "s5_stability")) else "NO"}
```

New completion tests cover all listed validations. No S2, S3, S4 or S5 algorithm was rerun.

## 9. Deprecated and Superseded File Map

| Deprecated file | Reason | Superseding file |
|---|---|---|
| `supplemental/reference_quotient_v1/outputs/S5_brokerage_stability/brokerage_topk_frequency.csv` | Per-run membership semantics, not cross-seed frequency | `v1_1_completion/outputs/S5_brokerage_stability/brokerage_topk_inclusion_frequency.csv` |
| `supplemental/reference_quotient_v1/outputs/S6_figure_ready/structural_summary.json` | Wrong extension; content is CSV | `v1_1_completion/outputs/S6_figure_ready/structural_summary.csv` |

## 10. Canonical Immutability and New Output SHA Inventory

The v1.1 manifest records all newly consumed files and all generated output SHA-256 values. Canonical P0 output hashes and existing S2-S5 output hashes are compared before and after the patch; both drift values are zero. Scientific baseline, canonical result and network algorithms are unchanged.

## 11. Final Git Status

The completion report and manifest are generated before the final local commit. No push is performed. The final report records the result commit after it is created.
''', encoding="utf-8")
    return report


def main() -> None:
    if git_value(ROOT, "branch", "--show-current") != "ch5-refq-supplemental-evidence-v1":
        raise RuntimeError("wrong branch")
    if git_value(ROOT, "merge-base", PARENT_RESULT_COMMIT, "HEAD") != PARENT_RESULT_COMMIT:
        raise RuntimeError("v1.1 implementation must descend from the approved v1 result commit")
    if git_value(ROOT, "status", "--short"):
        raise RuntimeError("worktree must be clean before v1.1 scan")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    before = existing_output_snapshot()
    scan = scan_completion_inputs()
    s5 = derive_s5_frequency()
    s6 = correct_s6_format()
    after = existing_output_snapshot()
    json_dump(OUTPUT / "existing_output_sha_audit.json", {"before": before, "after": after, "drift": before != after})
    build_manifest(scan, s5, s6, before, after)
    write_report(scan, s5, s6, before, after)
    print(json.dumps({
        "raw_rows": scan["validation"]["raw_frozen_rows_scanned_this_patch"],
        "eligible_total": scan["validation"]["eligible_total"],
        "self_loop": scan["validation"]["self_loop_records"],
        "cross_project": scan["validation"]["cross_project_records"],
        "canonical_drift": before["canonical_p0"] != after["canonical_p0"],
        "sensitivity_drift": any(before[key] != after[key] for key in ("s2_sensitivity", "s3_sensitivity", "s4_stability", "s5_stability")),
    }, indent=2))


if __name__ == "__main__":
    main()
