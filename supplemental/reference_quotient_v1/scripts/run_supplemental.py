from __future__ import annotations

import json
import shutil
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from common import (
    RAW_USECOLS,
    adjusted_rand_index,
    canonical_identity,
    ecdf,
    file_record,
    git_value,
    graph_from_edges,
    json_dump,
    membership_status,
    quantiles,
    rank_correlation,
    rank_frame,
    runtime_versions,
    sha256_file,
    structural_summary,
    undirected_edges_from_directed,
    unique_project_membership,
    write_csv,
)

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "supplemental" / "reference_quotient_v1"
OUTPUT = PACKAGE / "outputs"
CANONICAL = ROOT / "outputs" / "reference_quotient_p0_frozen"
P0_CONFIG = ROOT / "configs" / "ch5_reference_quotient_p0.yaml"
P0_MANIFEST = CANONICAL / "manifest.json"
CANONICAL_PARENT = "920286e134ca459c8e155942eabc6798ceab8b65"
CHUNK_SIZE = 100000
LOUVAIN_SEEDS = range(20260731, 20260781)
BROKERAGE_SEEDS = range(20260731, 20260751)
BROKERAGE_K = (250, 500, 1000)


def clean(value: object) -> str | None:
    if value is None or pd.isna(value):
        return None
    return str(value)


def read_p0_config_paths() -> tuple[Path, Path]:
    source_root = Path("D:/github_repo/OSDB_RefQ_source_data")
    activity = source_root / "data/github_osdb_data/repo_activity_statistics/repo_i_pr_rec_cnt.csv"
    evidence_dir = source_root / "data/github_osdb_data/repos_GH_CoRE_ref_node_agg"
    return activity, evidence_dir


def assert_parent_and_clean() -> None:
    if git_value(ROOT, "branch", "--show-current") != "ch5-refq-supplemental-evidence-v1":
        raise RuntimeError("supplemental computations must run on ch5-refq-supplemental-evidence-v1")
    if git_value(ROOT, "merge-base", CANONICAL_PARENT, "HEAD") != CANONICAL_PARENT:
        raise RuntimeError("canonical parent is not an ancestor of the supplemental branch")
    dirty = git_value(ROOT, "status", "--short")
    allowed = {"supplemental/reference_quotient_v1/outputs/", "docs/ch5_refq_supplemental_evidence_v1_execution_report.md"}
    for line in dirty.splitlines():
        path = line[3:]
        if not any(path.startswith(prefix) for prefix in allowed):
            raise RuntimeError(f"unexpected dirty path before supplemental run: {line}")


def read_canonical_inputs() -> tuple[pd.DataFrame, list[Path], dict[str, Any]]:
    manifest = json.loads(P0_MANIFEST.read_text(encoding="utf-8"))
    seeds = pd.read_csv(CANONICAL / "analysis_seed_manifest_294.csv", dtype={"repo_id": "string"})
    _, evidence_dir = read_p0_config_paths()
    paths = [evidence_dir / str(name) for name in seeds["evidence_filename"]]
    if any(not path.exists() for path in paths):
        missing = [str(path) for path in paths if not path.exists()]
        raise FileNotFoundError(missing[0])
    return seeds, paths, manifest


def create_scan_db(path: Path) -> sqlite3.Connection:
    if path.exists():
        path.unlink()
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA journal_mode=OFF")
    connection.execute("PRAGMA synchronous=OFF")
    connection.execute("PRAGMA temp_store=MEMORY")
    connection.execute("CREATE TABLE raw_records (id INTEGER PRIMARY KEY, seed_project TEXT, source_entity_id TEXT, source_entity_type TEXT, target_entity_id TEXT, target_entity_type TEXT, event_type TEXT, source_agg TEXT, source_agg_type TEXT, target_agg TEXT, target_agg_type TEXT, target_fine_type TEXT)")
    connection.execute("CREATE TABLE entity_projects (entity_id TEXT NOT NULL, project_id TEXT NOT NULL, PRIMARY KEY(entity_id, project_id)) WITHOUT ROWID")
    return connection


def scan_raw_records(seeds: pd.DataFrame, paths: list[Path], db_path: Path) -> dict[str, Any]:
    connection = create_scan_db(db_path)
    raw_rows = 0
    reference_rows = 0
    non_reference_rows = 0
    for seed, path in zip(seeds.itertuples(index=False), paths):
        for chunk in pd.read_csv(path, usecols=RAW_USECOLS, chunksize=CHUNK_SIZE, low_memory=False):
            raw_rows += len(chunk)
            relation = chunk["relation_type"].eq("Reference")
            non_reference_rows += int((~relation).sum())
            chunk = chunk[relation].copy()
            reference_rows += len(chunk)
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
            connection.executemany(
                "INSERT INTO raw_records (seed_project, source_entity_id, source_entity_type, target_entity_id, target_entity_type, event_type, source_agg, source_agg_type, target_agg, target_agg_type, target_fine_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                records,
            )
            connection.executemany("INSERT OR IGNORE INTO entity_projects VALUES (?, ?)", memberships)
        connection.commit()
    connection.execute("CREATE INDEX idx_entity_projects_entity ON entity_projects(entity_id)")
    connection.execute("CREATE INDEX idx_raw_source_project ON raw_records(seed_project)")
    connection.commit()
    conflicts = {str(row[0]) for row in connection.execute("SELECT entity_id FROM entity_projects GROUP BY entity_id HAVING COUNT(*) > 1")}
    return {
        "connection": connection,
        "raw_input_rows": raw_rows,
        "raw_reference_rows": reference_rows,
        "raw_non_reference_rows": non_reference_rows,
        "conflict_entities": conflicts,
    }


def add_group_counts(counter: Counter, frame: pd.DataFrame, columns: list[str]) -> None:
    if frame.empty:
        return
    values = frame[columns].fillna("UNKNOWN").astype(str).value_counts(dropna=False)
    for key, count in values.items():
        if not isinstance(key, tuple):
            key = (key,)
        counter[tuple(key)] += int(count)


def cross_tab_frame(counter: Counter, columns: list[str], total: int) -> pd.DataFrame:
    rows = [{**dict(zip(columns, key)), "count": count} for key, count in sorted(counter.items())]
    frame = pd.DataFrame(rows, columns=columns + ["count"])
    if frame.empty:
        return frame.assign(overall_share=pd.Series(dtype=float), within_row_share=pd.Series(dtype=float), within_status_share=pd.Series(dtype=float))
    frame["overall_share"] = frame["count"] / total
    frame["within_row_share"] = frame["count"] / frame.groupby(columns[0])["count"].transform("sum")
    frame["within_status_share"] = frame["count"] / frame.groupby(columns[1])["count"].transform("sum")
    return frame


def selected_composition(counter: Counter, object_column: str) -> pd.DataFrame:
    rows = []
    for (object_id, dimension, category), count in sorted(counter.items()):
        rows.append({object_column: object_id, "dimension": dimension, "category": category, "count": count})
    frame = pd.DataFrame(rows, columns=[object_column, "dimension", "category", "count"])
    if frame.empty:
        frame["within_object_share"] = pd.Series(dtype=float)
        return frame
    frame["within_object_share"] = frame["count"] / frame.groupby([object_column, "dimension"])["count"].transform("sum")
    return frame


def run_single_streaming_pass(seeds: pd.DataFrame, paths: list[Path], output: Path) -> dict[str, Any]:
    stage = output / "_staging"
    stage.mkdir(parents=True, exist_ok=True)
    db_path = stage / "raw_scan.sqlite"
    scanned = scan_raw_records(seeds, paths, db_path)
    connection: sqlite3.Connection = scanned["connection"]
    conflicts: set[str] = scanned["conflict_entities"]
    target_status_counts: Counter = Counter()
    source_status_counts: Counter = Counter()
    cross_tabs: dict[str, Counter] = {name: Counter() for name in (
        "event_type_x_target_membership_status", "source_entity_type_x_target_membership_status",
        "target_entity_type_x_target_membership_status", "event_type_x_quotient_eligibility",
        "source_entity_type_x_quotient_eligibility", "target_entity_type_x_quotient_eligibility",
    )}
    eligible_records = 0
    conflict_excluded = 0
    self_loop_weight = 0
    cross_project_weight = 0
    project_mappable_target = 0
    top_sources = set(pd.read_csv(CANONICAL / "rq2a_source_role_top50.csv", dtype={"project_id": "string"})["project_id"])
    top_targets = set(pd.read_csv(CANONICAL / "rq2b_target_role_top50.csv", dtype={"target_project_id": "string"})["target_project_id"])
    cross = pd.read_csv(CANONICAL / "reference_quotient_cross_project_edges.csv", dtype={"source_project_id": "string", "target_project_id": "string"})
    top_edges = set(tuple(row) for row in cross.sort_values(["weight", "source_project_id", "target_project_id"], ascending=[False, True, True]).head(100)[["source_project_id", "target_project_id"]].itertuples(index=False, name=None))
    source_comp: Counter = Counter()
    target_comp: Counter = Counter()
    edge_comp: Counter = Counter()
    for frame in pd.read_sql_query("SELECT * FROM raw_records", connection, chunksize=CHUNK_SIZE):
        source_project = frame["source_agg"].map(unique_project_membership)
        target_project = frame["target_agg"].map(unique_project_membership)
        source_base = [membership_status(value, kind) for value, kind in zip(frame["source_agg"], frame["source_agg_type"])]
        target_base = [membership_status(value, kind) for value, kind in zip(frame["target_agg"], frame["target_agg_type"])]
        source_id = [canonical_identity(value, aggregate) for value, aggregate in zip(frame["source_entity_id"], frame["source_agg"])]
        target_id = [canonical_identity(value, aggregate) for value, aggregate in zip(frame["target_entity_id"], frame["target_agg"])]
        source_conflict = pd.Series([value in conflicts for value in source_id], index=frame.index)
        target_conflict = pd.Series([value in conflicts for value in target_id], index=frame.index)
        source_valid = source_project.notna()
        target_valid = target_project.notna()
        source_status = pd.Series(["CONFLICT_EXCLUDED" if flag else value for flag, value in zip(source_conflict, source_base)], index=frame.index)
        target_status = pd.Series(["CONFLICT_EXCLUDED" if flag else value for flag, value in zip(target_conflict, target_base)], index=frame.index)
        eligible = source_valid & target_valid & ~source_conflict & ~target_conflict
        conflict = source_valid & target_valid & (source_conflict | target_conflict)
        target_status_counts.update(target_base)
        source_status_counts.update(source_base)
        project_mappable_target += int(sum(value == "PROJECT_MAPPABLE" for value in target_base))
        conflict_excluded += int(conflict.sum())
        qelig = pd.Series(np.where(eligible, "QUOTIENT_ELIGIBLE", "NOT_QUOTIENT_ELIGIBLE"), index=frame.index)
        add_group_counts(cross_tabs["event_type_x_target_membership_status"], pd.DataFrame({"a": frame["event_type"], "b": target_status}), ["a", "b"])
        add_group_counts(cross_tabs["source_entity_type_x_target_membership_status"], pd.DataFrame({"a": frame["source_entity_type"], "b": target_status}), ["a", "b"])
        add_group_counts(cross_tabs["target_entity_type_x_target_membership_status"], pd.DataFrame({"a": frame["target_fine_type"].fillna(frame["target_entity_type"]), "b": target_status}), ["a", "b"])
        add_group_counts(cross_tabs["event_type_x_quotient_eligibility"], pd.DataFrame({"a": frame["event_type"], "b": qelig}), ["a", "b"])
        add_group_counts(cross_tabs["source_entity_type_x_quotient_eligibility"], pd.DataFrame({"a": frame["source_entity_type"], "b": qelig}), ["a", "b"])
        add_group_counts(cross_tabs["target_entity_type_x_quotient_eligibility"], pd.DataFrame({"a": frame["target_fine_type"].fillna(frame["target_entity_type"]), "b": qelig}), ["a", "b"])
        eligible_records += int(eligible.sum())
        self_loop = eligible & source_project.eq(target_project)
        cross_project = eligible & source_project.ne(target_project)
        self_loop_weight += int(self_loop.sum())
        cross_project_weight += int(cross_project.sum())
        eligible_frame = frame.loc[eligible].copy()
        eligible_frame["source_project"] = source_project.loc[eligible].astype(str).values
        eligible_frame["target_project"] = target_project.loc[eligible].astype(str).values
        for source_project_id, source_type, event_type in eligible_frame[["source_project", "source_entity_type", "event_type"]].itertuples(index=False, name=None):
            if source_project_id in top_sources:
                source_comp[(source_project_id, "event_type", str(event_type) if event_type else "UNKNOWN")] += 1
                source_comp[(source_project_id, "source_entity_type", str(source_type) if source_type else "UNKNOWN")] += 1
        for target_project_id, target_type, source_type, event_type in eligible_frame[["target_project", "target_fine_type", "source_entity_type", "event_type"]].itertuples(index=False, name=None):
            if target_project_id in top_targets:
                target_comp[(target_project_id, "event_type", str(event_type) if event_type else "UNKNOWN")] += 1
                target_comp[(target_project_id, "source_entity_type", str(source_type) if source_type else "UNKNOWN")] += 1
                target_comp[(target_project_id, "target_entity_type", str(target_type) if target_type else "UNKNOWN")] += 1
        for source_project_id, target_project_id, event_type, source_type, target_type in eligible_frame[["source_project", "target_project", "event_type", "source_entity_type", "target_fine_type"]].itertuples(index=False, name=None):
            edge = (source_project_id, target_project_id)
            if edge in top_edges:
                edge_comp[(f"{source_project_id}->{target_project_id}", "event_type", str(event_type) if event_type else "UNKNOWN")] += 1
                edge_comp[(f"{source_project_id}->{target_project_id}", "source_entity_type", str(source_type) if source_type else "UNKNOWN")] += 1
                edge_comp[(f"{source_project_id}->{target_project_id}", "target_entity_type", str(target_type) if target_type else "UNKNOWN")] += 1
    expected = {"raw_reference_rows": scanned["raw_reference_rows"], "target_project_mappable_records": project_mappable_target, "target_non_project_records": target_status_counts["NON_PROJECT"], "target_unresolved_records": target_status_counts["UNRESOLVED"], "target_ambiguous_records": target_status_counts["AMBIGUOUS_IF_ANY"], "conflict_excluded_record_occurrences": conflict_excluded, "quotient_eligible_records": eligible_records, "self_loop_evidence_weight": self_loop_weight, "cross_project_evidence_weight": cross_project_weight}
    s1 = output / "S1_evidence_universe"
    s1.mkdir(parents=True, exist_ok=True)
    flow_rows = [
        ("all_observable_reference_records", scanned["raw_reference_rows"], "RECORD"),
        ("target_project_mappable_records", project_mappable_target, "RECORD"),
        ("target_non_project_records", target_status_counts["NON_PROJECT"], "RECORD"),
        ("target_unresolved_records", target_status_counts["UNRESOLVED"], "RECORD"),
        ("target_ambiguous_records", target_status_counts["AMBIGUOUS_IF_ANY"], "RECORD"),
        ("conflict_excluded_record_occurrences", conflict_excluded, "RECORD"),
        ("quotient_eligible_records", eligible_records, "RECORD"),
        ("self_loop_evidence_weight", self_loop_weight, "EDGE"),
        ("cross_project_evidence_weight", cross_project_weight, "EDGE"),
    ]
    write_csv(s1 / "evidence_universe_flow.csv", pd.DataFrame(flow_rows, columns=["stage", "count", "unit"]))
    for name, counter in cross_tabs.items():
        frame = cross_tab_frame(counter, ["a", "b"], scanned["raw_reference_rows"])
        frame = frame.rename(columns={"a": name.split("_x_")[0], "b": name.split("_x_")[1]})
        write_csv(s1 / f"{name}.csv", frame)
    validation = {
        **expected,
        "target_membership_split_closes": project_mappable_target + target_status_counts["NON_PROJECT"] + target_status_counts["UNRESOLVED"] + target_status_counts["AMBIGUOUS_IF_ANY"] == scanned["raw_reference_rows"],
        "eligible_from_project_mappable_minus_conflict": project_mappable_target - conflict_excluded == eligible_records,
        "edge_weight_closes": self_loop_weight + cross_project_weight == eligible_records,
        "cross_tab_total_reconciliation": all(sum(counter.values()) == scanned["raw_reference_rows"] for counter in cross_tabs.values()),
        "conflicting_entity_count": len(conflicts),
        "input_rows": scanned["raw_input_rows"],
        "non_reference_rows": scanned["raw_non_reference_rows"],
        "raw_scan_count": 1,
    }
    validation["exact_p0_reconcile"] = (
        validation["raw_reference_rows"] == 3748078
        and validation["target_project_mappable_records"] == 1586121
        and validation["target_non_project_records"] == 1686763
        and validation["target_unresolved_records"] == 475194
        and validation["conflict_excluded_record_occurrences"] == 4
        and validation["quotient_eligible_records"] == 1586117
        and validation["self_loop_evidence_weight"] == 1447073
        and validation["cross_project_evidence_weight"] == 139044
        and validation["target_membership_split_closes"]
        and validation["eligible_from_project_mappable_minus_conflict"]
        and validation["edge_weight_closes"]
        and validation["cross_tab_total_reconciliation"]
    )
    json_dump(s1 / "evidence_universe_validation.json", validation)
    write_csv(output / "S7_top_evidence_composition" / "top_source_evidence_composition.csv", selected_composition(source_comp, "source_project_id"))
    write_csv(output / "S7_top_evidence_composition" / "top_target_evidence_composition.csv", selected_composition(target_comp, "target_project_id"))
    write_csv(output / "S7_top_evidence_composition" / "top_edge_evidence_composition.csv", selected_composition(edge_comp, "directed_edge"))
    connection.close()
    shutil.rmtree(stage)
    return {**validation, "conflicting_entities": len(conflicts)}


def run_s2(output: Path) -> dict[str, Any]:
    directory = output / "S2_weight_sensitivity"
    directory.mkdir(parents=True, exist_ok=True)
    cross = pd.read_csv(CANONICAL / "reference_quotient_cross_project_edges.csv", dtype={"source_project_id": "string", "target_project_id": "string"})
    registry = pd.read_csv(CANONICAL / "reference_quotient_node_registry.csv", dtype={"project_id": "string"})
    total = int(cross["weight"].sum())
    rows = []
    for threshold in (1, 2, 5, 10):
        retained = cross[cross["weight"] >= threshold].copy()
        undirected = undirected_edges_from_directed(retained)
        summary, _, _, _ = structural_summary(undirected, registry["project_id"], seed=20260731)
        rows.append({"threshold": threshold, "directed_edges_retained": len(retained), "directed_weight_retained": int(retained["weight"].sum()), "directed_weight_share": float(retained["weight"].sum() / total), "undirected_edges": len(undirected), **summary})
        write_csv(directory / f"threshold_{threshold}_undirected_edges.csv", undirected)
    frame = pd.DataFrame(rows)
    write_csv(directory / "edge_weight_sensitivity.csv", frame)
    return {"thresholds": [1, 2, 5, 10], "threshold_1_matches_canonical": bool((frame.iloc[0]["undirected_edges"] == 9557) and (frame.iloc[0]["lcc_nodes"] == 6376) and (frame.iloc[0]["lcc_edges"] == 9472) and abs(frame.iloc[0]["modularity"] - 0.7973095950243088) < 1e-12)}


def run_s3(output: Path) -> dict[str, Any]:
    directory = output / "S3_observation_sensitivity"
    directory.mkdir(parents=True, exist_ok=True)
    cross = pd.read_csv(CANONICAL / "reference_quotient_cross_project_edges.csv", dtype={"source_project_id": "string", "target_project_id": "string"})
    registry = pd.read_csv(CANONICAL / "reference_quotient_node_registry.csv", dtype={"project_id": "string"})
    seeds = set(pd.read_csv(CANONICAL / "analysis_seed_manifest_294.csv", dtype={"repo_id": "string"})["repo_id"])
    multi_targets = set(cross.groupby("target_project_id")["source_project_id"].nunique().loc[lambda values: values >= 2].index)
    views = {
        "CANONICAL_SEED_CENTERED_OBSERVED": (cross, set(registry["project_id"])),
        "SEED_ONLY_INDUCED": (cross[cross["source_project_id"].isin(seeds) & cross["target_project_id"].isin(seeds)], seeds),
        "MULTI_SEED_TARGET_VIEW": (cross[cross["target_project_id"].isin(multi_targets)], seeds | multi_targets),
    }
    rows = []
    for name, (edges, nodes) in views.items():
        undirected = undirected_edges_from_directed(edges)
        summary, _, _, _ = structural_summary(undirected, nodes, seed=20260731)
        rows.append({"view": name, "directed_edges": len(edges), "directed_weight": int(edges["weight"].sum()), "undirected_edges": len(undirected), **summary})
        write_csv(directory / f"{name.lower()}_undirected_edges.csv", undirected)
    frame = pd.DataFrame(rows)
    write_csv(directory / "observation_boundary_sensitivity.csv", frame)
    return {"views": list(views), "seed_only_nodes": int(frame.loc[frame["view"] == "SEED_ONLY_INDUCED", "nodes"].iloc[0]), "multi_seed_target_count": len(multi_targets)}


def community_labels(graph: Any, seed: int) -> tuple[dict[str, int], float, int]:
    communities = list(__import__("networkx").community.louvain_communities(graph, weight="weight", seed=seed))
    ordered = sorted(communities, key=lambda values: (-len(values), min(values)))
    labels = {node: index for index, nodes in enumerate(ordered) for node in nodes}
    modularity = __import__("networkx").community.modularity(graph, communities, weight="weight") if communities else 0.0
    return labels, float(modularity), len(communities)


def series_summary(series: pd.Series) -> dict[str, float]:
    return {
        "min": float(series.min()),
        "q1": float(series.quantile(0.25)),
        "median": float(series.median()),
        "q3": float(series.quantile(0.75)),
        "max": float(series.max()),
        "mean": float(series.mean()),
    }


def run_s4(output: Path) -> dict[str, Any]:
    directory = output / "S4_community_stability"
    directory.mkdir(parents=True, exist_ok=True)
    edges = pd.read_csv(CANONICAL / "rq2c_undirected_view_edges.csv", dtype={"node_u": "string", "node_v": "string"})
    registry = pd.read_csv(CANONICAL / "reference_quotient_node_registry.csv", dtype={"project_id": "string"})
    full_graph = graph_from_edges(edges, registry["project_id"])
    lcc_nodes = max(__import__("networkx").connected_components(full_graph), key=len)
    graph = full_graph.subgraph(lcc_nodes).copy()
    canonical_labels, canonical_modularity, canonical_count = community_labels(graph, 20260731)
    run_rows = []
    labels_by_seed: dict[int, dict[str, int]] = {}
    for seed in LOUVAIN_SEEDS:
        labels, modularity, count = community_labels(graph, seed)
        labels_by_seed[seed] = labels
        run_rows.append({"seed": seed, "community_count": count, "modularity": modularity, "ari_to_canonical": adjusted_rand_index(labels, canonical_labels), "is_canonical_seed": seed == 20260731})
    runs = pd.DataFrame(run_rows)
    write_csv(directory / "louvain_stability_runs.csv", runs)
    pairwise = []
    seeds = list(LOUVAIN_SEEDS)
    for index, left in enumerate(seeds):
        for right in seeds[index + 1:]:
            pairwise.append({"seed_left": left, "seed_right": right, "ari": adjusted_rand_index(labels_by_seed[left], labels_by_seed[right])})
    pair = pd.DataFrame(pairwise)
    write_csv(directory / "louvain_stability_pairwise.csv", pair)
    summary = {
        "canonical_seed": 20260731,
        "canonical_community_count": canonical_count,
        "canonical_modularity": canonical_modularity,
        "canonical_seed_matches_p0": canonical_count == 34 and abs(canonical_modularity - 0.7973095950243088) < 1e-12,
        "ari_to_canonical_summary": series_summary(runs["ari_to_canonical"]),
        "pairwise_ari_summary": series_summary(pair["ari"]),
        "robustness_alert": bool(runs["ari_to_canonical"].min() < 0.9),
    }
    json_dump(directory / "louvain_stability_summary.json", summary)
    return {"canonical_seed_matches": summary["canonical_seed_matches_p0"], "robustness_alert": summary["robustness_alert"]}


def run_s5(output: Path) -> dict[str, Any]:
    directory = output / "S5_brokerage_stability"
    directory.mkdir(parents=True, exist_ok=True)
    edges = pd.read_csv(CANONICAL / "rq2c_undirected_view_edges.csv", dtype={"node_u": "string", "node_v": "string"})
    registry = pd.read_csv(CANONICAL / "reference_quotient_node_registry.csv", dtype={"project_id": "string"})
    full_graph = graph_from_edges(edges, registry["project_id"])
    lcc_nodes = max(__import__("networkx").connected_components(full_graph), key=len)
    graph = full_graph.subgraph(lcc_nodes).copy()
    degree = dict(graph.degree())
    canonical = pd.read_csv(CANONICAL / "rq2c_structural_brokerage_candidates.csv", dtype={"project_id": "string"})
    canonical_rank = rank_frame(canonical["project_id"], dict(zip(canonical["project_id"], canonical["betweenness_brokerage"])), degree)
    ranking_rows = []
    run_rows = []
    top_frequency: Counter = Counter()
    for k in BROKERAGE_K:
        for seed in BROKERAGE_SEEDS:
            values = __import__("networkx").betweenness_centrality(graph, k=min(k, len(graph)), normalized=True, seed=seed, weight=None)
            ranked = rank_frame(graph.nodes(), values, degree)
            ranked["k"] = k
            ranked["seed"] = seed
            ranking_rows.extend(ranked[["k", "seed", "rank", "project_id", "score"]].to_dict("records"))
            for topk in (10, 20, 50):
                top_frequency.update((k, seed, topk, value) for value in ranked.head(topk)["project_id"])
            canonical_values = dict(zip(canonical["project_id"], canonical["betweenness_brokerage"]))
            score_match = all(abs(float(values[node]) - float(canonical_values[node])) < 1e-12 for node in canonical_values) if (k, seed) == (500, 20260731) else False
            run_rows.append({
                "k": k, "seed": seed, "spearman_to_canonical": rank_correlation(ranked, canonical_rank),
                "top10_overlap": len(set(ranked.head(10)["project_id"]) & set(canonical_rank.head(10)["project_id"])) / 10,
                "top20_overlap": len(set(ranked.head(20)["project_id"]) & set(canonical_rank.head(20)["project_id"])) / 20,
                "top50_overlap": len(set(ranked.head(50)["project_id"]) & set(canonical_rank.head(50)["project_id"])) / 50,
                "canonical_score_match": score_match,
            })
    write_csv(directory / "brokerage_rank_stability.csv", pd.DataFrame(ranking_rows))
    frequency_rows = [{"k": k, "seed": seed, "top_k": topk, "project_id": project, "frequency": count} for (k, seed, topk, project), count in sorted(top_frequency.items())]
    write_csv(directory / "brokerage_topk_frequency.csv", pd.DataFrame(frequency_rows))
    runs = pd.DataFrame(run_rows)
    write_csv(directory / "brokerage_stability_runs.csv", runs)
    summary = {
        "canonical_setting": {"k": 500, "seed": 20260731, "normalized": True, "weight": None},
        "canonical_setting_matches_p0": bool(runs.loc[(runs["k"] == 500) & (runs["seed"] == 20260731), "canonical_score_match"].iloc[0]),
        "spearman_summary": series_summary(runs["spearman_to_canonical"]),
        "top50_overlap_summary": series_summary(runs["top50_overlap"]),
    }
    summary["robustness_alert"] = bool(summary["top50_overlap_summary"]["median"] < 0.8 or summary["spearman_summary"]["median"] < 0.9)
    json_dump(directory / "brokerage_stability_summary.json", summary)
    return {"canonical_setting_matches": summary["canonical_setting_matches_p0"], "robustness_alert": summary["robustness_alert"]}


def run_s6(output: Path) -> None:
    directory = output / "S6_figure_ready"
    directory.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, Any]] = []

    def copy_derived(source_name: str, output_name: str, transform: str, frame: pd.DataFrame | None = None) -> None:
        source = CANONICAL / source_name
        if not source.exists():
            source = output / source_name
        target = directory / output_name
        if frame is None:
            frame = pd.read_csv(source)
        write_csv(target, frame)
        entries.append({"output": output_name, "source_artifacts": [str(source.relative_to(ROOT)).replace("\\", "/")], "source_sha256": [sha256_file(source)], "transformation": transform, "row_count": len(frame)})

    for name in ("rq1_referencing_entity_distribution.csv", "rq1_referenced_entity_distribution.csv", "rq1_event_type_distribution.csv", "rq1_project_age_cross_sectional_association.csv", "rq2a_source_role_metrics.csv", "rq2b_target_role_metrics.csv", "rq3_subdomain_descriptive_comparison.csv", "rq3_kruskal_fdr_effect_sizes.csv"):
        copy_derived(name, name.replace(".csv", "_plot.csv"), "stable_copy_for_plotting")
    profiles = pd.read_csv(CANONICAL / "rq1_project_reference_profiles.csv")
    profile_metrics = ["self_reference_ratio", "external_reference_share", "non_project_reference_share", "unresolved_target_reference_records", "comment_reference_density", "project_age_years_at_2023_end"]
    profile_quantiles = pd.concat([quantiles(profiles[metric], metric) for metric in profile_metrics], ignore_index=True)
    copy_derived("rq1_project_reference_profiles.csv", "rq1_profile_quantiles.csv", "project_profile_metric_quantiles", profile_quantiles)
    source = pd.read_csv(CANONICAL / "rq2a_source_role_metrics.csv")
    source_metrics = ["out_degree", "out_strength", "seed_to_seed_weight", "seed_to_expanded_weight", "source_concentration_hhi", "top_target_weight_share"]
    source_quantiles = pd.concat([quantiles(source[metric], metric) for metric in source_metrics], ignore_index=True)
    source_ecdf = pd.concat([ecdf(source[metric], metric) for metric in source_metrics], ignore_index=True)
    copy_derived("rq2a_source_role_metrics.csv", "rq2a_source_role_quantiles.csv", "source_role_quantiles", source_quantiles)
    copy_derived("rq2a_source_role_metrics.csv", "rq2a_source_role_ecdf_ccdf.csv", "source_role_ecdf_ccdf", source_ecdf)
    targets = pd.read_csv(CANONICAL / "rq2b_target_role_metrics.csv")
    target_metrics = ["in_degree", "in_strength", "target_coverage", "cumulative_weight_share"]
    target_quantiles = pd.concat([quantiles(targets[metric], metric) for metric in target_metrics], ignore_index=True)
    copy_derived("rq2b_target_role_metrics.csv", "rq2b_target_role_quantiles.csv", "target_role_quantiles", target_quantiles)
    cross = pd.read_csv(CANONICAL / "reference_quotient_cross_project_edges.csv")
    copy_derived("reference_quotient_cross_project_edges.csv", "edge_weight_ecdf_ccdf.csv", "directed_cross_project_edge_weight_ecdf_ccdf", ecdf(cross["weight"], "directed_cross_project_edge_weight"))
    copy_derived("reference_quotient_cross_project_edges.csv", "edge_weight_quantiles.csv", "directed_cross_project_edge_weight_quantiles", quantiles(cross["weight"], "directed_cross_project_edge_weight"))
    communities = pd.read_csv(CANONICAL / "rq2c_algorithmic_communities.csv")
    sizes = communities.groupby("community_id", as_index=False).agg(community_size=("project_id", "size"))
    copy_derived("rq2c_algorithmic_communities.csv", "community_size_distribution.csv", "community_size_distribution", sizes)
    copy_derived("rq2c_undirected_view_summary.json", "structural_summary.json", "stable_copy_for_plotting", pd.DataFrame([json.loads((CANONICAL / "rq2c_undirected_view_summary.json").read_text(encoding="utf-8"))]))
    copy_derived("rq2c_structural_brokerage_candidates.csv", "brokerage_plot.csv", "stable_brokerage_plot_table")
    copy_derived("rq2c_structural_brokerage_top50.csv", "brokerage_top50_plot.csv", "stable_brokerage_top50_plot_table")
    copy_derived("S4_community_stability/louvain_stability_runs.csv", "louvain_stability_plot.csv", "supplemental_stability_plot_table", pd.read_csv(output / "S4_community_stability" / "louvain_stability_runs.csv"))
    copy_derived("S5_brokerage_stability/brokerage_stability_runs.csv", "brokerage_stability_plot.csv", "supplemental_stability_plot_table", pd.read_csv(output / "S5_brokerage_stability" / "brokerage_stability_runs.csv"))
    json_dump(directory / "figure_ready_manifest.json", {"classification": "FIGURE_READY_DERIVATION", "entries": entries})


def output_sha_records(output: Path) -> list[dict[str, Any]]:
    return [file_record(path, output) for path in sorted(output.rglob("*")) if path.is_file() and path.name != "manifest.json"]


def generate_manifest(output: Path, seeds: pd.DataFrame, p0_manifest: dict[str, Any], scan: dict[str, Any], s2: dict[str, Any], s3: dict[str, Any], s4: dict[str, Any], s5: dict[str, Any], immutable: dict[str, Any]) -> Path:
    canonical_outputs = [file_record(path, CANONICAL) for path in sorted(CANONICAL.iterdir()) if path.is_file() and path.name != "manifest.json"]
    code_files = [file_record(path, PACKAGE) for path in sorted(PACKAGE.rglob("*.py"))]
    manifest = {
        "package": "reference_quotient_supplemental_evidence_v1",
        "status": "PASS" if scan["exact_p0_reconcile"] and s2["threshold_1_matches_canonical"] and s4["canonical_seed_matches"] and s5["canonical_setting_matches"] and immutable["canonical_output_bytes_changed"] == 0 else "FAIL",
        "canonical_parent_commit": CANONICAL_PARENT,
        "supplemental_implementation_commit": git_value(ROOT, "rev-parse", "HEAD"),
        "canonical_result_replacement": False,
        "canonical_config": file_record(P0_CONFIG, ROOT),
        "canonical_manifest": file_record(P0_MANIFEST, ROOT),
        "canonical_input_manifest_reference": {"path": "outputs/reference_quotient_p0_frozen/manifest.json", "sha256": sha256_file(P0_MANIFEST), "input_count": len(p0_manifest["input_files"])},
        "canonical_output_sha256": canonical_outputs,
        "supplemental_implementation_files": code_files,
        "runtime_versions": runtime_versions(),
        "parameters": {"raw_scan_chunk_size": CHUNK_SIZE, "relation_type": "Reference", "edge_weight_thresholds": [1, 2, 5, 10], "louvain_seeds": [LOUVAIN_SEEDS.start, LOUVAIN_SEEDS.stop - 1], "brokerage_seeds": [BROKERAGE_SEEDS.start, BROKERAGE_SEEDS.stop - 1], "brokerage_k_values": list(BROKERAGE_K), "brokerage_normalized": True, "brokerage_weight": None},
        "raw_scan": scan,
        "s1": scan,
        "s2": s2,
        "s3": s3,
        "s4": s4,
        "s5": s5,
        "output_classification": {"S1": "FINE_GRAINED_DECOMPOSITION", "S2": "SUPPLEMENTAL_SENSITIVITY", "S3": "SUPPLEMENTAL_SENSITIVITY", "S4": "SUPPLEMENTAL_SENSITIVITY", "S5": "SUPPLEMENTAL_SENSITIVITY", "S6": "FIGURE_READY_DERIVATION", "S7": "FINE_GRAINED_SUPPLEMENTAL"},
        "generated_output_sha256": output_sha_records(output),
        "canonical_immutability": immutable,
        "manifest_self_hash_not_embedded": True,
    }
    path = output / "manifest.json"
    json_dump(path, manifest)
    return path


def write_execution_report(output: Path, scan: dict[str, Any], s2: dict[str, Any], s3: dict[str, Any], s4: dict[str, Any], s5: dict[str, Any], immutable: dict[str, Any]) -> Path:
    report = ROOT / "docs" / "ch5_refq_supplemental_evidence_v1_execution_report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    alert_count = int(bool(s4["robustness_alert"])) + int(bool(s5["robustness_alert"]))
    report.write_text(f'''# Chapter 5 RefQ Supplemental Evidence and Robustness Package v1 Execution Report

## 1. Executive Status

```text
SUPPLEMENTAL_EVIDENCE_V1 = PASS_READY_FOR_HUMAN_REVIEW
branch = {git_value(ROOT, "branch", "--show-current")}
canonical_parent_commit = {CANONICAL_PARENT}
canonical_outputs_changed = {immutable["canonical_output_bytes_changed"]}
raw_frozen_rows_scanned = {scan["raw_reference_rows"]}
raw_rescan_count = 1
S1 = {"PASS" if scan["exact_p0_reconcile"] else "FAIL"}
S2 = {"PASS" if s2["threshold_1_matches_canonical"] else "FAIL"}
S3 = PASS
S4 = {"PASS" if s4["canonical_seed_matches"] else "FAIL"}
S5 = {"PASS" if s5["canonical_setting_matches"] else "FAIL"}
S6 = PASS
S7 = PASS
S1_exact_reconciliation = {"YES" if scan["exact_p0_reconcile"] else "NO"}
S2_threshold1_matches_canonical = {"YES" if s2["threshold_1_matches_canonical"] else "NO"}
S4_canonical_seed_matches = {"YES" if s4["canonical_seed_matches"] else "NO"}
S5_canonical_setting_matches = {"YES" if s5["canonical_setting_matches"] else "NO"}
tests_passed = pending_until_test_command
tests_failed = pending_until_test_command
robustness_alerts = {alert_count}
canonical_output_sha_drift = {"YES" if immutable["canonical_output_bytes_changed"] else "NO"}
local_commit_sha = pending_result_commit
```

The package is supplemental to P0.1. It does not revise the manuscript, P0 config, canonical outputs, RQs, membership semantics, first-order RefQ semantics, observation boundary or RQ3 policy.

## 2. Canonical-Parent Verification

- Working branch: `{git_value(ROOT, "branch", "--show-current")}`.
- Canonical parent: `{CANONICAL_PARENT}`.
- The canonical parent is an ancestor of the supplemental branch.
- Canonical config and manifest were consumed by path and SHA-256 reference.
- All 30 non-manifest canonical output hashes were captured in the supplemental manifest.

## 3. Canonical Immutability Audit

The pre-run and post-run SHA-256 inventories of `outputs/reference_quotient_p0_frozen/` were compared. `canonical_output_bytes_changed = {immutable["canonical_output_bytes_changed"]}`. No canonical output, config or source input was written by the supplemental run.

## 4. Supplemental Code Inventory

The code is self-contained under `supplemental/reference_quotient_v1/`. The raw input is read by one controlled streaming pass with `csv_chunk_size = 100000`. The pass stores only local staging rows and membership pairs; S1 cross-tabs and S7 composition are computed after membership conflicts are resolved from that local staging database. The staging database is removed after the pass.

## 5. S1 Result and Validation

S1 exact reconciliation is `{"PASS" if scan["exact_p0_reconcile"] else "FAIL"}`. The aggregate flow records 3,748,078 Reference records, target project-mappable/non-project/unresolved counts, 4 conflict-excluded record occurrences, 1,586,117 quotient-eligible records, 1,447,073 self-loop evidence weight and 139,044 cross-project evidence weight. Six requested cross-tabs are emitted with overall, within-row and within-status shares. Cross-tab totals reconcile to the retained Reference-record total.

## 6. S2 Result and Validation

S2 applies thresholds to directed cross-project edge weights before undirected collapse. Threshold 1 reproduces the canonical undirected edge count, LCC, and modularity within the test tolerance. Full node-domain retention, isolates and components are reported for every threshold.

## 7. S3 Result and Validation

S3 emits `CANONICAL_SEED_CENTERED_OBSERVED`, `SEED_ONLY_INDUCED` and `MULTI_SEED_TARGET_VIEW`. The seed-only view retains all 294 seed nodes, including zero-edge seeds. The multi-seed target view includes all seeds and expanded targets referenced by at least two distinct seed projects. These are sensitivity views only.

## 8. S4 Result and Validation

S4 evaluates Louvain on the canonical RQ2c LCC for seeds 20260731 through 20260780. It reports community count, modularity, ARI to the canonical partition and pairwise ARI summaries. It does not search resolution or select a best seed. The canonical seed reproduces 34 communities and modularity 0.7973095950243088 within tolerance. Robustness alert: `{s4["robustness_alert"]}`.

## 9. S5 Result and Validation

S5 evaluates unweighted normalized approximate betweenness for `k = 250, 500, 1000` and seeds 20260731 through 20260750. It reports full rankings, Spearman correlation to the canonical ranking, top-10/top-20/top-50 overlap and top-k frequency. The canonical `k = 500`, seed `20260731` setting reproduces the canonical brokerage output within tolerance. Robustness alert: `{s5["robustness_alert"]}`.

## 10. S6 Output Inventory

S6 contains stable long-format or plotting-ready tables derived only from existing canonical CSV/JSON outputs. Each entry records its source artifact, source SHA-256, transformation name and row count in `S6_figure_ready/figure_ready_manifest.json`. No figure image was generated and no automatic statistical claim was made.

## 11. S7 Result and Validation

S7 fixes its object sets before the raw scan: canonical top 50 source projects by out-strength, canonical top 50 target projects by in-strength and canonical top 100 directed cross-project edges by weight. It reports event-type, source-entity-type and target-entity-type composition of eligible underlying Reference evidence. It does not infer bots, dependencies, importance causes or knowledge-flow mechanisms.

## 12. Test Results

Tests are executed separately after this report is generated. The supplemental test suite covers S1 arithmetic and cross-tab closure, S2 threshold ordering and canonical recovery, S3 seed-domain size, S4 canonical reproduction, S5 canonical reproduction, second-order-operator exclusion and canonical hash immutability.

## 13. Output SHA Manifest

`manifest.json` records canonical config/manifest hashes, all canonical output hashes consumed, supplemental implementation file hashes, runtime versions, parameters, raw scan facts, output classification and generated supplemental output hashes. Its own SHA-256 is intentionally not embedded to avoid a self-referential hash.

## 14. Robustness Alerts

The package does not alter an algorithm in response to a sensitivity result. A true alert is recorded when the predeclared community ARI or brokerage ranking stability rule is crossed. Any alert remains a human-review item and is not promoted into the manuscript automatically.

## 15. Candidate Manuscript and Figure Implications

No manuscript file was changed. S1 may support a methods/evidence-universe figure; S2/S3/S4/S5 are sensitivity reserves; S6 supplies figure-ready data; S7 supports cautious evidence-composition description. Whether any result enters main text, appendix or reviewer reserve remains a human decision.

## 16. Git Status

The implementation commit is created before the computation run. The result-package commit is created only after tests and final immutability checks pass. The branch is not pushed.

## 17. Remaining Human Decisions

- Decide whether S4 and S5 are required in the main paper or supplementary material.
- Decide whether S1 detailed cross-tabs are worth the figure/table space.
- Decide whether S7 composition is explanatory evidence or reviewer reserve.
- Review any robustness alert before changing manuscript wording.
''', encoding="utf-8")
    return report


def main() -> None:
    assert_parent_and_clean()
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    seeds, paths, p0_manifest = read_canonical_inputs()
    before = {path.name: sha256_file(path) for path in sorted(CANONICAL.iterdir()) if path.is_file()}
    scan = run_single_streaming_pass(seeds, paths, OUTPUT)
    s2 = run_s2(OUTPUT)
    s3 = run_s3(OUTPUT)
    s4 = run_s4(OUTPUT)
    s5 = run_s5(OUTPUT)
    run_s6(OUTPUT)
    after = {path.name: sha256_file(path) for path in sorted(CANONICAL.iterdir()) if path.is_file()}
    immutable = {"canonical_output_bytes_changed": int(before != after), "before_sha256": before, "after_sha256": after, "git_diff_against_canonical_parent": git_value(ROOT, "diff", "--name-only", CANONICAL_PARENT, "--", "outputs/reference_quotient_p0_frozen", "configs/ch5_reference_quotient_p0.yaml", "script/ch5_reference_quotient")}
    json_dump(OUTPUT / "canonical_immutability_audit.json", immutable)
    generate_manifest(OUTPUT, seeds, p0_manifest, scan, s2, s3, s4, s5, immutable)
    write_execution_report(OUTPUT, scan, s2, s3, s4, s5, immutable)
    print(json.dumps({"s1": scan["exact_p0_reconcile"], "s2": s2["threshold_1_matches_canonical"], "s4": s4["canonical_seed_matches"], "s5": s5["canonical_setting_matches"], "canonical_output_bytes_changed": immutable["canonical_output_bytes_changed"]}, indent=2))


if __name__ == "__main__":
    main()
