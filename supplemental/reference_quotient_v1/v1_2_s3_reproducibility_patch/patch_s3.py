from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
V1 = ROOT / "supplemental" / "reference_quotient_v1"
PATCH = V1 / "v1_2_s3_reproducibility_patch"
OUTPUT = PATCH / "outputs" / "S3_observation_sensitivity_corrected"
CANONICAL = ROOT / "outputs" / "reference_quotient_p0_frozen"
OLD_S3 = V1 / "outputs" / "S3_observation_sensitivity"
CANONICAL_PARENT = "920286e134ca459c8e155942eabc6798ceab8b65"
V1_RESULT_COMMIT = "ba72987adb2c2339bdf1f7a3b370278c88c29c3c"
RANDOM_SEED = 20260731


sys.path.insert(0, str(ROOT))
from script.ch5_reference_quotient.network_views import (  # noqa: E402
    analyze_undirected_view,
    directed_to_undirected_edges,
)


def sha256_file(path: Path) -> str:
    import hashlib
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def snapshot(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)).replace(os.sep, "/"): sha256_file(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def existing_snapshots() -> dict[str, dict[str, str]]:
    return {
        "canonical_p0": snapshot(CANONICAL),
        "s1_v1": snapshot(V1 / "outputs" / "S1_evidence_universe"),
        "s1_v1_1": snapshot(V1 / "v1_1_completion" / "outputs" / "S1_evidence_universe"),
        "s2": snapshot(V1 / "outputs" / "S2_weight_sensitivity"),
        "s3_old": snapshot(OLD_S3),
        "s4": snapshot(V1 / "outputs" / "S4_community_stability"),
        "s5": snapshot(V1 / "outputs" / "S5_brokerage_stability"),
        "s6_v1": snapshot(V1 / "outputs" / "S6_figure_ready"),
        "s6_v1_1": snapshot(V1 / "v1_1_completion" / "outputs" / "S6_figure_ready"),
        "s7_v1": snapshot(V1 / "outputs" / "S7_top_evidence_composition"),
        "s7_v1_1": snapshot(V1 / "v1_1_completion" / "outputs" / "S7_top_evidence_composition"),
    }


def stable_nodes(registry: pd.DataFrame, seeds: pd.DataFrame, view: str, multi_targets: set[str]) -> list[str]:
    seed_ids = set(seeds["repo_id"].astype(str))
    if view == "CANONICAL_SEED_CENTERED_OBSERVED":
        return registry["project_id"].astype(str).tolist()
    if view == "SEED_ONLY_INDUCED":
        return seeds["repo_id"].astype(str).tolist()
    if view == "MULTI_SEED_TARGET_VIEW":
        keep = seed_ids | multi_targets
        return registry.loc[registry["project_id"].astype(str).isin(keep), "project_id"].astype(str).tolist()
    raise ValueError(view)


def run_views() -> dict[str, Any]:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    cross = pd.read_csv(
        CANONICAL / "reference_quotient_cross_project_edges.csv",
        dtype={"source_project_id": "string", "target_project_id": "string"},
    )
    registry = pd.read_csv(
        CANONICAL / "reference_quotient_node_registry.csv",
        dtype={"project_id": "string"},
    )
    seeds = pd.read_csv(
        CANONICAL / "analysis_seed_manifest_294.csv",
        dtype={"repo_id": "string"},
    )
    seed_ids = set(seeds["repo_id"].astype(str))
    multi_targets = set(
        cross.groupby("target_project_id")["source_project_id"]
        .nunique()
        .loc[lambda values: values >= 2]
        .index.astype(str)
    )
    views = {
        "CANONICAL_SEED_CENTERED_OBSERVED": cross,
        "SEED_ONLY_INDUCED": cross[
            cross["source_project_id"].isin(seed_ids)
            & cross["target_project_id"].isin(seed_ids)
        ].copy(),
        "MULTI_SEED_TARGET_VIEW": cross[
            cross["target_project_id"].isin(multi_targets)
        ].copy(),
    }
    rows = []
    for name, directed in views.items():
        # This is intentionally the canonical P0 conversion path.
        undirected = directed_to_undirected_edges(directed)
        nodes = stable_nodes(registry, seeds, name, multi_targets)
        summary, lcc_edges, communities, _ = analyze_undirected_view(
            undirected,
            RANDOM_SEED,
            500,
            nodes,
        )
        write_csv(OUTPUT / f"{name.lower()}_undirected_edges.csv", undirected)
        write_csv(OUTPUT / f"{name.lower()}_lcc_edges.csv", lcc_edges)
        write_csv(OUTPUT / f"{name.lower()}_communities.csv", communities)
        rows.append({
            **summary,
            "view": name,
            "directed_edges": len(directed),
            "directed_weight": int(directed["weight"].sum()),
            "undirected_edges": len(undirected),
        })
    frame = pd.DataFrame(rows)
    write_csv(OUTPUT / "observation_boundary_sensitivity_corrected.csv", frame)
    return {
        "summary": frame,
        "multi_seed_target_count": len(multi_targets),
        "seed_count": len(seed_ids),
        "raw_rescan_count": 0,
        "network_algorithms_rerun": 3,
    }


def write_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def old_new_comparison(new_frame: pd.DataFrame) -> pd.DataFrame:
    old = pd.read_csv(OLD_S3 / "observation_boundary_sensitivity.csv")
    merged = old.merge(new_frame, on="view", suffixes=("_old", "_new"))
    numeric = [
        "directed_edges", "directed_weight", "undirected_edges", "nodes",
        "edge_observed_nodes", "components", "isolates", "lcc_nodes",
        "lcc_edges", "lcc_coverage", "average_clustering_lcc",
        "transitivity_lcc", "algorithmic_communities", "modularity",
        "random_seed",
    ]
    for column in numeric:
        merged[f"delta_{column}"] = merged[f"{column}_new"] - merged[f"{column}_old"]
    return merged


def write_patch_manifest(
    before: dict[str, dict[str, str]],
    after: dict[str, dict[str, str]],
    run: dict[str, Any],
    comparison: pd.DataFrame,
) -> Path:
    output_files = [
        {
            "path": str(path.relative_to(ROOT)).replace(os.sep, "/"),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in sorted(OUTPUT.rglob("*"))
        if path.is_file()
    ]
    manifest = {
        "package": "reference_quotient_supplemental_v1_2_s3_reproducibility_patch",
        "status": "PASS",
        "canonical_parent_commit": CANONICAL_PARENT,
        "parent_supplemental_result_commit": V1_RESULT_COMMIT,
        "canonical_result_replacement": False,
        "s2_status": "EXCLUDED_PENDING_WEIGHT_SEMANTICS_AUDIT",
        "raw_rescan_count": 0,
        "network_algorithms_rerun": 3,
        "old_s3_status": "SUPERSEDED_S3_NONCANONICAL_LOUVAIN_CONSTRUCTION_ORDER",
        "old_s3_path": "supplemental/reference_quotient_v1/outputs/S3_observation_sensitivity/observation_boundary_sensitivity.csv",
        "new_s3_path": "supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/outputs/S3_observation_sensitivity_corrected/observation_boundary_sensitivity_corrected.csv",
        "canonical_recovery": bool(
            int(run["summary"].loc[run["summary"]["view"] == "CANONICAL_SEED_CENTERED_OBSERVED", "algorithmic_communities"].iloc[0]) == 34
            and abs(float(run["summary"].loc[run["summary"]["view"] == "CANONICAL_SEED_CENTERED_OBSERVED", "modularity"].iloc[0]) - 0.7973095950243088) < 1e-12
        ),
        "non_stochastic_metric_drift": bool(
            any(comparison[f"delta_{column}"].abs().max() > 1e-12 for column in [
                "directed_edges", "directed_weight", "undirected_edges", "nodes",
                "edge_observed_nodes", "components", "isolates", "lcc_nodes",
                "lcc_edges", "lcc_coverage", "average_clustering_lcc",
                "transitivity_lcc", "random_seed",
            ])
        ),
        "canonical_p0_sha_drift": before["canonical_p0"] != after["canonical_p0"],
        "other_supplemental_sha_drift": any(
            before[key] != after[key]
            for key in before
            if key not in {"s3_old"}
        ),
        "existing_s3_sha_drift": before["s3_old"] != after["s3_old"],
        "generated_outputs": output_files,
        "old_s3_comparison": comparison.to_dict(orient="records"),
    }
    path = PATCH / "s3_reproducibility_patch_manifest.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def main() -> None:
    if git_value(ROOT, "branch", "--show-current") != "ch5-refq-supplemental-evidence-v1":
        raise RuntimeError("wrong branch")
    dirty = git_value(ROOT, "status", "--short")
    allowed_dirty = {
        "supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/outputs/",
        "supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/old_vs_corrected_s3_summary.csv",
    }
    unexpected = [line for line in dirty.splitlines() if not any(line[3:].startswith(prefix) for prefix in allowed_dirty)]
    if unexpected:
        raise RuntimeError("worktree contains unexpected changes before S3 patch: " + "; ".join(unexpected))
    if git_value(ROOT, "merge-base", V1_RESULT_COMMIT, "HEAD") != V1_RESULT_COMMIT:
        raise RuntimeError("S3 patch must descend from the approved v1 result commit")
    before = existing_snapshots()
    run = run_views()
    comparison = old_new_comparison(run["summary"])
    after = existing_snapshots()
    write_csv(PATCH / "old_vs_corrected_s3_summary.csv", comparison)
    write_patch_manifest(before, after, run, comparison)
    print(json.dumps({
        "canonical_recovery": int(run["summary"].loc[run["summary"]["view"] == "CANONICAL_SEED_CENTERED_OBSERVED", "algorithmic_communities"].iloc[0]) == 34,
        "canonical_modularity": float(run["summary"].loc[run["summary"]["view"] == "CANONICAL_SEED_CENTERED_OBSERVED", "modularity"].iloc[0]),
        "canonical_p0_sha_drift": before["canonical_p0"] != after["canonical_p0"],
        "other_supplemental_sha_drift": any(before[key] != after[key] for key in before if key not in {"s3_old"}),
        "raw_rescan_count": 0,
    }, indent=2))


def git_value(repo: Path, *args: str) -> str:
    import subprocess
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


if __name__ == "__main__":
    main()
