"""Single-run P0 recalculation for the Chapter 5 Reference Quotient study."""

from __future__ import annotations

import json
import math
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
from scipy import stats

from .config import RefQConfig, resolved_inputs, validate_config
from .edge_table import edge_frame
from .manifest import file_record, file_records, git_info, runtime_versions, sha256_file, utc_now, write_json
from .membership import (
    MembershipRegistry,
    canonical_project_entity_identity,
    classify_membership,
    normalized_entity_identity,
    unique_project_membership,
)
from .network_views import analyze_undirected_view, cross_project_edges, directed_to_undirected_edges
from .seed_selection import assert_seed_boundary, build_seed_manifests, relative_evidence_path
from .statistics import describe_columns, kruskal_fdr
from script.build_dataset.repository_identity_provenance import (
    ADMITTED_SOURCE_OBSERVATION,
    INVALID_EVENT_REPOSITORY_ID,
    MISSING_EVENT_REPOSITORY_ID,
    OUT_OF_SEED_SOURCE_OBSERVATION,
    normalize_repository_id,
)


ISSUE_PREFIXES = ("I_", "IC_", "PR_", "PRR_", "PRRC_")
ISSUE_KEY = re.compile(r"_(\d+#\d+)")

V2_SOURCE_ADMISSION_COLUMNS = {
    "event_repo_id",
    "source_admission_status",
    "expected_source_context_repo_id",
}
V2_SOURCE_ADMISSION_STATUSES = {
    ADMITTED_SOURCE_OBSERVATION,
    OUT_OF_SEED_SOURCE_OBSERVATION,
    MISSING_EVENT_REPOSITORY_ID,
    INVALID_EVENT_REPOSITORY_ID,
}


def _normalize_repository_series(values: pd.Series, field_name: str) -> tuple[pd.Series, pd.Series, pd.Series]:
    normalized: list[str | None] = []
    missing: list[bool] = []
    invalid: list[bool] = []
    for value in values.tolist():
        try:
            value = normalize_repository_id(value, field_name=field_name)
        except ValueError:
            value = None
            invalid.append(True)
            missing.append(False)
            normalized.append(value)
            continue
        normalized.append(value)
        missing.append(value is None)
        invalid.append(False)
    return (
        pd.Series(normalized, index=values.index, dtype="string"),
        pd.Series(missing, index=values.index, dtype="bool"),
        pd.Series(invalid, index=values.index, dtype="bool"),
    )


def _prepare_reference_evidence_chunk(
    chunk: pd.DataFrame,
    expected_source_repo_id: object,
    *,
    strict_source_admission: bool,
    relation_type: str = "Reference",
) -> tuple[pd.DataFrame, dict[str, int]]:
    """Select the logical Reference view before membership/profile processing.

    Legacy v1 intentionally keeps its historical relation-only filter. Strict
    v2 requires the annotated source-admission contract and returns only rows
    admitted to the current seed's event-repository observation context.
    """
    if "relation_type" not in chunk.columns:
        raise ValueError("reference evidence is missing relation_type")
    reference = chunk.loc[chunk["relation_type"].eq(relation_type)].copy()
    base = {
        "input_reference_rows_before_source_admission": int(len(reference)),
        "source_admitted_reference_rows": int(len(reference)),
        "source_out_of_seed_reference_rows": 0,
        "source_missing_event_repo_reference_rows": 0,
        "source_invalid_event_repo_reference_rows": 0,
        "retained_reference_rows": int(len(reference)),
        "source_mismatch_after_admission": 0,
    }
    if not strict_source_admission:
        return reference, base

    missing = sorted(V2_SOURCE_ADMISSION_COLUMNS - set(reference.columns))
    if missing:
        raise ValueError("strict v2 aggregate schema missing: " + ", ".join(missing))
    try:
        expected = normalize_repository_id(
            expected_source_repo_id,
            field_name="current seed repository ID",
        )
    except ValueError as exc:
        raise ValueError(str(exc)) from exc
    if expected is None:
        raise ValueError("current seed repository ID is required for strict v2 source admission")

    event_repo, event_missing, event_invalid = _normalize_repository_series(
        reference["event_repo_id"], "event_repo_id"
    )
    expected_context, context_missing, context_invalid = _normalize_repository_series(
        reference["expected_source_context_repo_id"], "expected_source_context_repo_id"
    )
    if bool((context_missing | context_invalid | expected_context.ne(expected)).any()):
        raise ValueError("expected_source_context_repo_id does not match the current seed repository ID")

    statuses = reference["source_admission_status"].astype("string")
    unknown_statuses = sorted(set(statuses.dropna().astype(str)) - V2_SOURCE_ADMISSION_STATUSES)
    if unknown_statuses or statuses.isna().any():
        values = unknown_statuses or ["<NA>"]
        raise ValueError("strict v2 source_admission_status contains unsupported values: " + ", ".join(values))

    declared_admitted = statuses.eq(ADMITTED_SOURCE_OBSERVATION)
    declared_out_of_seed = statuses.eq(OUT_OF_SEED_SOURCE_OBSERVATION)
    declared_missing = statuses.eq(MISSING_EVENT_REPOSITORY_ID)
    declared_invalid = statuses.eq(INVALID_EVENT_REPOSITORY_ID)
    status_mismatch = (
        declared_out_of_seed & (event_missing | event_invalid | event_repo.eq(expected))
    ) | (
        declared_missing & ~event_missing
    ) | (
        declared_invalid & ~event_invalid
    )
    if bool(status_mismatch.any()):
        raise ValueError("SOURCE_ADMISSION_CONTRACT_VIOLATION: status does not match event repository identity")
    admitted_mismatch = declared_admitted & (event_missing | event_invalid | event_repo.ne(expected))
    if bool(admitted_mismatch.any()):
        raise ValueError("SOURCE_ADMISSION_CONTRACT_VIOLATION: admitted row does not match current seed")

    admitted = (
        declared_admitted
        & event_repo.eq(expected)
        & expected_context.eq(expected)
    )
    out_of_seed = event_repo.notna() & event_repo.ne(expected)
    reference["event_repo_id"] = event_repo
    reference["expected_source_context_repo_id"] = expected_context
    base.update(
        {
            "source_admitted_reference_rows": int(admitted.sum()),
            "source_out_of_seed_reference_rows": int(out_of_seed.sum()),
            "source_missing_event_repo_reference_rows": int(event_missing.sum()),
            "source_invalid_event_repo_reference_rows": int(event_invalid.sum()),
            "retained_reference_rows": int(admitted.sum()),
        }
    )
    return reference.loc[admitted].copy(), base


class RefQPipeline:
    def __init__(self, config: RefQConfig, workspace_root: str | Path) -> None:
        self.config = config
        self.workspace = Path(workspace_root).resolve()
        self.inputs = resolved_inputs(config)
        self.final_root = (self.workspace / config.output_root).resolve()
        self.staging_root = self.final_root.with_name(self.final_root.name + "_staging")
        self.started_at = utc_now()
        self.audit = Counter()
        self.source_types = Counter()
        self.target_types = Counter()
        self.event_types = Counter()
        self.edge_weights = Counter()
        self.project_profiles: dict[str, Counter] = defaultdict(Counter)
        self.active_issue_keys: dict[str, set[str]] = defaultdict(set)
        self.comment_source_ids: dict[str, set[str]] = defaultdict(set)
        self.provenance: list[dict[str, Any]] = []
        self.conflicting_entity_ids: set[str] = set()

    @property
    def strict_source_admission(self) -> bool:
        return self.config.raw.get("identity_policy") == "STRICT_REPOSITORY_IDENTITY"

    def _evidence_usecols(self, *, membership_only: bool = False) -> list[str]:
        if membership_only:
            columns = [
                "src_entity_id", "tar_entity_id", "relation_type",
                "src_entity_id_agg", "tar_entity_id_agg",
            ]
        else:
            columns = [
                "src_entity_id", "src_entity_type", "tar_entity_id", "tar_entity_type",
                "relation_type", "relation_label_repr", "event_id", "event_type", "event_time",
                "tar_entity_match_text", "tar_entity_match_pattern_type", "src_entity_id_agg",
                "src_entity_type_agg", "tar_entity_id_agg", "tar_entity_type_agg",
                "tar_entity_type_fine_grained",
            ]
        if self.strict_source_admission:
            columns.extend(sorted(V2_SOURCE_ADMISSION_COLUMNS))
        return columns

    def _load_seed_manifests(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        seeds, candidates = build_seed_manifests(
            self.inputs["repo_activity_statistics"],
            self.inputs["gh_core_ref_node_agg_dir"],
            self.config.get_int("study_year"),
            self.config.get_int("analysis_seed_activity_threshold"),
        )
        assert_seed_boundary(
            seeds,
            candidates,
            self.config.get_int("expected_analysis_seed_count"),
            self.config.get_int("expected_candidate_seed_count"),
        )
        return seeds, candidates

    def preflight(self) -> dict[str, int]:
        """Read-only input-boundary check; never creates P0 artifacts."""
        errors = validate_config(self.config, self.workspace)
        if errors:
            raise ValueError("; ".join(errors))
        seeds, _ = self._load_seed_manifests()
        summary = Counter()
        affected_seed_count = 0
        for seed in seeds.itertuples(index=False):
            for chunk in pd.read_csv(
                seed.evidence_path,
                usecols=self._evidence_usecols(),
                chunksize=self.config.get_int("csv_chunk_size", 100000),
                low_memory=False,
            ):
                summary["input_rows"] += len(chunk)
                summary["non_reference_rows"] += int(
                    (~chunk["relation_type"].eq(self.config.raw["relation_type"])).sum()
                )
                _, boundary = _prepare_reference_evidence_chunk(
                    chunk,
                    seed.repo_id,
                    strict_source_admission=self.strict_source_admission,
                    relation_type=self.config.raw["relation_type"],
                )
                for key, value in boundary.items():
                    summary[key] += value
                if boundary["source_out_of_seed_reference_rows"]:
                    affected_seed_count += 1
        summary["affected_source_seeds"] = affected_seed_count
        summary["source_mismatch_after_admission"] = 0
        return {key: int(value) for key, value in summary.items()}

    def run(self) -> Path:
        errors = validate_config(self.config, self.workspace)
        if errors:
            raise ValueError("; ".join(errors))
        if self.final_root.exists() or self.staging_root.exists():
            raise FileExistsError(f"frozen or staging output already exists: {self.final_root}")
        self.staging_root.mkdir(parents=True)
        registry = MembershipRegistry(self.staging_root / "membership_registry.sqlite")
        try:
            seeds, candidates = self._freeze_seeds()
            self._audit_memberships(seeds, registry)
            registry_summary = registry.summary()
            self.conflicting_entity_ids = registry.conflicting_entities()
            self._scan_evidence(seeds)
            edges = self._write_quotient_outputs(seeds)
            role_frames = self._write_role_outputs(seeds, edges)
            self._write_seed_observability_audit(seeds, *role_frames[:2])
            self._write_membership_audit(seeds, candidates, registry_summary)
            self._write_quotient_audit(edges)
            self._write_rq1_outputs(seeds)
            self._write_rq3_outputs(seeds, *role_frames)
            self._write_provenance()
            registry.close()
            (self.staging_root / "membership_registry.sqlite").unlink()
            self._write_manifest(seeds)
            self.staging_root.rename(self.final_root)
            return self.final_root
        except Exception:
            registry.close()
            raise

    def _freeze_seeds(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        seeds, candidates = self._load_seed_manifests()
        source_root = self.config.source_repository["path"]
        seed_output = seeds.copy()
        candidate_output = candidates.copy()
        seed_output["evidence_path"] = seed_output["evidence_path"].map(
            lambda path: relative_evidence_path(path, source_root)
        )
        candidate_output["evidence_path"] = candidate_output["evidence_path"].map(
            lambda path: relative_evidence_path(path, source_root)
        )
        seed_output.to_csv(self.staging_root / "analysis_seed_manifest_294.csv", index=False)
        candidate_output.to_csv(self.staging_root / "candidate_seed_observation_audit.csv", index=False)
        return seeds, candidates

    def _audit_memberships(self, seeds: pd.DataFrame, registry: MembershipRegistry) -> None:
        chunk_size = self.config.get_int("csv_chunk_size", 100000)
        for seed in seeds.itertuples(index=False):
            for chunk in pd.read_csv(
                seed.evidence_path,
                usecols=self._evidence_usecols(membership_only=True),
                chunksize=chunk_size,
                low_memory=False,
            ):
                chunk, _ = _prepare_reference_evidence_chunk(
                    chunk,
                    seed.repo_id,
                    strict_source_admission=self.strict_source_admission,
                    relation_type=self.config.raw["relation_type"],
                )
                for side in ("src", "tar"):
                    identities = pd.Series(
                        [
                            canonical_project_entity_identity(entity, aggregate)
                            for entity, aggregate in zip(
                                chunk[f"{side}_entity_id"], chunk[f"{side}_entity_id_agg"]
                            )
                        ],
                        index=chunk.index,
                    )
                    projects = chunk[f"{side}_entity_id_agg"].map(unique_project_membership)
                    pairs = pd.DataFrame({"entity": identities, "project": projects}).dropna().drop_duplicates()
                    registry.add(
                        (str(row.entity), str(row.project)) for row in pairs.itertuples(index=False)
                    )
            registry.commit()

    def _scan_evidence(self, seeds: pd.DataFrame) -> None:
        chunk_size = self.config.get_int("csv_chunk_size", 100000)
        sample_limit = self.config.get_int("provenance_sample_size", 100)
        seed_ids = set(seeds["repo_id"].astype(str))
        for seed in seeds.itertuples(index=False):
            expected_source = str(seed.repo_id)
            for chunk in pd.read_csv(
                seed.evidence_path,
                usecols=self._evidence_usecols(),
                chunksize=chunk_size,
                low_memory=False,
            ):
                self.audit["input_rows"] += len(chunk)
                relation_ok = chunk["relation_type"].eq(self.config.raw["relation_type"])
                self.audit["non_reference_rows"] += int((~relation_ok).sum())
                chunk, boundary = _prepare_reference_evidence_chunk(
                    chunk,
                    expected_source,
                    strict_source_admission=self.strict_source_admission,
                    relation_type=self.config.raw["relation_type"],
                )
                if self.strict_source_admission:
                    for key, value in boundary.items():
                        self.audit[key] += value
                else:
                    self.audit["retained_reference_rows"] += len(chunk)
                self.source_types.update(chunk["src_entity_type"].fillna("UNKNOWN").astype(str))
                target_type = chunk["tar_entity_type_fine_grained"].fillna(chunk["tar_entity_type"]).fillna("UNKNOWN")
                self.target_types.update(target_type.astype(str))
                self.event_types.update(chunk["event_type"].fillna("UNKNOWN").astype(str))

                source_project = chunk["src_entity_id_agg"].map(unique_project_membership)
                target_project = chunk["tar_entity_id_agg"].map(unique_project_membership)
                source_raw_identity = chunk["src_entity_id"].map(normalized_entity_identity)
                target_raw_identity = chunk["tar_entity_id"].map(normalized_entity_identity)
                source_identity = pd.Series(
                    [
                        canonical_project_entity_identity(entity, aggregate)
                        for entity, aggregate in zip(chunk["src_entity_id"], chunk["src_entity_id_agg"])
                    ],
                    index=chunk.index,
                )
                target_identity = pd.Series(
                    [
                        canonical_project_entity_identity(entity, aggregate)
                        for entity, aggregate in zip(chunk["tar_entity_id"], chunk["tar_entity_id_agg"])
                    ],
                    index=chunk.index,
                )
                source_status = [classify_membership(v, t) for v, t in zip(chunk["src_entity_id_agg"], chunk["src_entity_type_agg"])]
                target_status = [classify_membership(v, t) for v, t in zip(chunk["tar_entity_id_agg"], chunk["tar_entity_type_agg"])]
                self.audit.update(f"source_{status}" for status in source_status)
                self.audit.update(f"target_{status}" for status in target_status)
                source_valid = source_project.notna()
                target_valid = target_project.notna()
                source_canonical_fallback = source_valid & source_raw_identity.isna()
                target_canonical_fallback = target_valid & target_raw_identity.isna()
                source_conflict = source_valid & source_identity.isin(self.conflicting_entity_ids)
                target_conflict = target_valid & target_identity.isin(self.conflicting_entity_ids)
                self.audit["source_canonical_identity_fallback"] += int(source_canonical_fallback.sum())
                self.audit["target_canonical_identity_fallback"] += int(target_canonical_fallback.sum())
                self.audit["source_membership_conflict"] += int(source_conflict.sum())
                self.audit["target_membership_conflict"] += int(target_conflict.sum())
                eligible = (
                    source_valid & target_valid
                    & ~source_conflict & ~target_conflict
                )
                self.audit["quotient_eligible_records"] += int(eligible.sum())
                source_mismatch = source_valid & source_project.ne(expected_source)
                self.audit["source_seed_membership_mismatch"] += int(source_mismatch.sum())
                if self.strict_source_admission:
                    self.audit["source_mismatch_after_admission"] += int(source_mismatch.sum())

                grouped = pd.DataFrame(
                    {"source": source_project[eligible].astype(str), "target": target_project[eligible].astype(str)}
                ).value_counts()
                for (source, target), count in grouped.items():
                    self.edge_weights[(str(source), str(target))] += int(count)

                profile = self.project_profiles[expected_source]
                profile["total_reference_records"] += len(chunk)
                self_loop = source_valid & target_valid & source_project.eq(target_project)
                external_project = source_valid & target_valid & source_project.ne(target_project)
                non_project = pd.Series(target_status, index=chunk.index).eq("non_project")
                unresolved = pd.Series(target_status, index=chunk.index).eq("unresolved")
                profile["self_reference_records"] += int(self_loop.sum())
                profile["external_project_reference_records"] += int(external_project.sum())
                profile["non_project_reference_records"] += int(non_project.sum())
                profile["unresolved_target_reference_records"] += int(unresolved.sum())

                issue_related = chunk["src_entity_id"].fillna("").astype(str).str.startswith(ISSUE_PREFIXES)
                issue_ids = chunk.loc[issue_related, "src_entity_id"].astype(str)
                self.comment_source_ids[expected_source].update(issue_ids)
                self.active_issue_keys[expected_source].update(
                    match.group(1) for value in issue_ids for match in [ISSUE_KEY.search(value)] if match
                )
                profile["comment_body_ref_count"] += int(issue_related.sum())

                if len(self.provenance) < sample_limit:
                    for index in chunk.index[eligible]:
                        if len(self.provenance) >= sample_limit:
                            break
                        row = chunk.loc[index]
                        self.provenance.append(
                            {
                                "source_project_id": str(source_project.loc[index]),
                                "target_project_id": str(target_project.loc[index]),
                                "src_entity_id": row["src_entity_id"],
                                "src_entity_type": row["src_entity_type"],
                                "tar_entity_id": row["tar_entity_id"],
                                "tar_entity_type": row["tar_entity_type_fine_grained"],
                                "event_id": row["event_id"],
                                "event_type": row["event_type"],
                                "event_time": row["event_time"],
                                "relation_label_repr": row["relation_label_repr"],
                                "source_evidence_file": seed.evidence_filename,
                            }
                        )
        if self.audit["source_seed_membership_mismatch"]:
            if self.strict_source_admission:
                raise ValueError("SOURCE_SEED_MISMATCH_AFTER_ADMISSION")
            raise ValueError("source artifact membership is inconsistent with the frozen seed manifest")

    def _write_quotient_outputs(self, seeds: pd.DataFrame) -> pd.DataFrame:
        edges = edge_frame(self.edge_weights, seeds["repo_id"], preserve_self_loops=True)
        edges.to_csv(self.staging_root / "reference_quotient_edges.csv", index=False)
        cross = cross_project_edges(edges)
        cross.to_csv(self.staging_root / "reference_quotient_cross_project_edges.csv", index=False)
        seed_ids = set(seeds["repo_id"].astype(str))
        edge_nodes = set(edges["source_project_id"].astype(str)) | set(edges["target_project_id"].astype(str))
        node_rows = []
        for project_id in sorted(seed_ids | edge_nodes):
            node_rows.append(
                {
                    "project_id": project_id,
                    "node_role": "seed_project" if project_id in seed_ids else "expanded_target_project",
                    "edge_observed": project_id in edge_nodes,
                    "zero_edge_seed": project_id in seed_ids and project_id not in edge_nodes,
                }
            )
        pd.DataFrame(node_rows).to_csv(
            self.staging_root / "reference_quotient_node_registry.csv", index=False
        )
        return edges

    def _write_role_outputs(self, seeds: pd.DataFrame, edges: pd.DataFrame):
        cross = cross_project_edges(edges)
        seed_ids = set(seeds["repo_id"].astype(str))
        source_rows = []
        for seed in seeds.itertuples(index=False):
            project_id = str(seed.repo_id)
            outgoing = cross[cross["source_project_id"] == project_id]
            seed_edges = outgoing[outgoing["target_is_seed"]]
            expanded_edges = outgoing[~outgoing["target_is_seed"]]
            weights = outgoing["weight"]
            source_rows.append(
                {
                    "project_id": project_id,
                    "repo_name": seed.repo_name,
                    "out_degree": len(outgoing),
                    "out_strength": int(weights.sum()),
                    "seed_to_seed_relation_count": len(seed_edges),
                    "seed_to_seed_weight": int(seed_edges["weight"].sum()),
                    "seed_to_expanded_relation_count": len(expanded_edges),
                    "seed_to_expanded_weight": int(expanded_edges["weight"].sum()),
                    "target_diversity": len(outgoing["target_project_id"].unique()),
                    "source_concentration_hhi": float(((weights / weights.sum()) ** 2).sum()) if weights.sum() else 0.0,
                    "top_target_weight_share": float(weights.max() / weights.sum()) if weights.sum() else 0.0,
                }
            )
        source_frame = pd.DataFrame(source_rows).sort_values(
            ["out_strength", "out_degree", "project_id"], ascending=[False, False, True]
        )
        source_frame.to_csv(self.staging_root / "rq2a_source_role_metrics.csv", index=False)
        source_frame.head(50).to_csv(self.staging_root / "rq2a_source_role_top50.csv", index=False)

        targets = (
            cross.groupby("target_project_id", as_index=False)
            .agg(in_degree=("source_project_id", "nunique"), in_strength=("weight", "sum"))
        )
        targets["target_coverage"] = targets["in_degree"] / len(seeds)
        targets["target_role"] = targets["target_project_id"].map(lambda value: "seed_project" if value in seed_ids else "expanded_target_project")
        category_by_seed = dict(zip(seeds["repo_id"].astype(str), seeds["category_label"]))
        metadata = pd.read_csv(
            self.inputs["dbms_repos_key_features"],
            usecols=["github_repo_id", "category_label"],
            dtype={"github_repo_id": "string"},
        )
        metadata["github_repo_id"] = metadata["github_repo_id"].str.replace(r"\.0$", "", regex=True)
        metadata = metadata[
            metadata["github_repo_id"].notna()
            & metadata["github_repo_id"].str.fullmatch(r"\d+")
            & metadata["category_label"].notna()
        ]
        category_by_known_dbms = (
            metadata.groupby("github_repo_id")["category_label"]
            .agg(lambda values: "|".join(sorted(set(map(str, values)))))
            .to_dict()
        )
        targets["target_category_label"] = targets["target_project_id"].map(category_by_known_dbms)
        targets["target_category_label"] = targets["target_category_label"].fillna(
            targets["target_project_id"].map(category_by_seed)
        ).fillna("not_in_dbms_metadata")
        targets["target_category_source"] = targets["target_project_id"].map(
            lambda value: "seed_manifest" if value in category_by_seed else (
                "dbms_metadata" if value in category_by_known_dbms else "unavailable"
            )
        )
        total_weight = targets["in_strength"].sum()
        targets = targets.sort_values(["in_strength", "in_degree", "target_project_id"], ascending=[False, False, True])
        targets["cumulative_weight_share"] = targets["in_strength"].cumsum() / total_weight if total_weight else 0.0
        targets.to_csv(self.staging_root / "rq2b_target_role_metrics.csv", index=False)
        targets.head(50).to_csv(self.staging_root / "rq2b_target_role_top50.csv", index=False)
        target_breakdown = (
            targets.groupby(
                ["target_role", "target_category_label", "target_category_source"],
                as_index=False,
                dropna=False,
            )
            .agg(
                target_count=("target_project_id", "nunique"),
                total_in_degree=("in_degree", "sum"),
                total_in_strength=("in_strength", "sum"),
            )
        )
        target_breakdown["weight_share"] = (
            target_breakdown["total_in_strength"] / total_weight if total_weight else 0.0
        )
        target_breakdown.to_csv(
            self.staging_root / "rq2b_target_category_type_breakdown.csv", index=False
        )
        concentration = {
            "observable_targets": len(targets),
            "total_cross_project_weight": int(total_weight),
            "top_1_weight_share": float(targets.head(1)["in_strength"].sum() / total_weight) if total_weight else 0.0,
            "top_10_weight_share": float(targets.head(10)["in_strength"].sum() / total_weight) if total_weight else 0.0,
            "top_50_weight_share": float(targets.head(50)["in_strength"].sum() / total_weight) if total_weight else 0.0,
        }
        write_json(self.staging_root / "rq2b_target_concentration.json", concentration)

        undirected = directed_to_undirected_edges(cross)
        undirected.to_csv(self.staging_root / "rq2c_undirected_view_edges.csv", index=False)
        node_registry = pd.read_csv(
            self.staging_root / "reference_quotient_node_registry.csv", dtype={"project_id": str}
        )
        structural_summary, lcc_edges, communities, brokerage = analyze_undirected_view(
            undirected,
            self.config.get_int("random_seed"),
            self.config.get_int("brokerage_sample_size", 500),
            node_registry["project_id"],
        )
        lcc_nodes = set(communities["project_id"].astype(str))
        directed_lcc = cross[
            cross["source_project_id"].isin(lcc_nodes)
            & cross["target_project_id"].isin(lcc_nodes)
        ]
        structural_summary.update(
            {
                "directed_cross_project_edges_full": int(len(cross)),
                "directed_cross_project_weight_full": int(cross["weight"].sum()),
                "directed_cross_project_edges_lcc_sensitivity": int(len(directed_lcc)),
                "directed_cross_project_weight_lcc_sensitivity": int(directed_lcc["weight"].sum()),
            }
        )
        write_json(self.staging_root / "rq2c_undirected_view_summary.json", structural_summary)
        lcc_edges.to_csv(self.staging_root / "rq2c_undirected_view_lcc_edges.csv", index=False)
        communities.to_csv(self.staging_root / "rq2c_algorithmic_communities.csv", index=False)
        brokerage.to_csv(self.staging_root / "rq2c_structural_brokerage_candidates.csv", index=False)
        brokerage.head(50).to_csv(self.staging_root / "rq2c_structural_brokerage_top50.csv", index=False)
        return source_frame, targets, brokerage

    def _write_seed_observability_audit(self, seeds, source_frame, targets) -> None:
        positive = int(source_frame["out_degree"].gt(0).sum())
        expanded_targets = targets[targets["target_role"].eq("expanded_target_project")]
        seed_ids = set(seeds["repo_id"].astype(str))
        target_nodes = set(targets["target_project_id"].astype(str))
        target_only_nodes = target_nodes - seed_ids
        payload = {
            "status": "PASS",
            "observation_design": "294_seed_project_sources_with_project_targets_expanded_from_observed_references",
            "seed_count": int(len(seeds)),
            "positive_out_degree_seeds": positive,
            "zero_out_degree_seeds": int(len(seeds) - positive),
            "expanded_target_count": int(expanded_targets["target_project_id"].nunique()),
            "target_only_count": int(len(target_only_nodes)),
            "target_only_expanded_target_count": int(len(target_only_nodes)),
            "unresolved_membership_count": int(
                self.audit["source_unresolved"] + self.audit["target_unresolved"]
            ),
            "ambiguous_membership_count": int(
                self.audit["source_ambiguous"] + self.audit["target_ambiguous"]
                + self.audit["source_membership_conflict"]
                + self.audit["target_membership_conflict"]
            ),
            "expanded_targets_are_source_complete": False,
            "non_project_external_targets_enter_refqn": False,
        }
        write_json(self.staging_root / "seed_observability_audit.json", payload)

    def _write_membership_audit(self, seeds, candidates, registry_summary) -> None:
        payload = {
            "status": "PASS",
            "formal_invariant": "forall retained v in V_P, exists! p in P: pi(v)=p; every retained M row has row-sum 1",
            "conflict_policy": "exclude every endpoint occurrence of globally conflicting artifact identities from Q",
            "canonical_identity_policy": "when a project-mappable endpoint lacks a usable fine-grained ID, use its unique R_<repo_id> aggregate project node as the canonical identity",
            "excluded_conflicting_entity_ids": sorted(self.conflicting_entity_ids),
            "membership_rule": self.config.raw["membership_rule"],
            "candidate_seed_count": len(candidates),
            "analysis_seed_count": len(seeds),
            "endpoint_counts": {key: int(value) for key, value in sorted(self.audit.items()) if key.startswith(("source_", "target_"))},
            **registry_summary,
        }
        write_json(self.staging_root / "membership_audit.json", payload)

    def _write_quotient_audit(self, edges: pd.DataFrame) -> None:
        cross = cross_project_edges(edges)
        edge_nodes = set(edges["source_project_id"]) | set(edges["target_project_id"])
        node_registry = pd.read_csv(
            self.staging_root / "reference_quotient_node_registry.csv", dtype={"project_id": str}
        )
        payload = {
            "status": "PASS",
            "formalization": "Q=M^T R_P M",
            "operator_order": "first_order_membership_induced_directed_quotient",
            "direction_preserved": True,
            "edge_aggregation_rule": self.config.raw["edge_aggregation_rule"],
            "quotient_self_loop_policy": self.config.raw["quotient_self_loop_policy"],
            "rq2_cross_project_self_loop_policy": self.config.raw["rq2_cross_project_self_loop_policy"],
            "fine_grained_reference_records": int(self.audit["retained_reference_rows"]),
            "scanned_input_rows": int(self.audit["input_rows"]),
            "retained_reference_records": int(self.audit["retained_reference_rows"]),
            "quotient_eligible_records": int(self.audit["quotient_eligible_records"]),
            "refq_node_domain": int(len(node_registry)),
            "refq_edge_observed_nodes": int(len(edge_nodes)),
            "refq_zero_edge_seed_nodes": int(node_registry["zero_edge_seed"].sum()),
            "refq_directed_edges_including_self_loops": len(edges),
            "refq_directed_cross_project_edges": len(cross),
            "refq_self_loops": int(edges["is_self_loop"].sum()),
            "refq_weight_including_self_loops": int(edges["weight"].sum()),
            "refq_cross_project_weight": int(cross["weight"].sum()),
            "second_order_projection_executed": False,
            "excluded_operators": ["QQ^T", "Q^TQ", "K=X Phi X^T"],
        }
        write_json(self.staging_root / "quotient_construction_audit.json", payload)

    def _write_rq1_outputs(self, seeds: pd.DataFrame) -> None:
        def distribution(counter: Counter, name: str) -> pd.DataFrame:
            total = sum(counter.values())
            return pd.DataFrame(
                [{name: key, "count": count, "share": count / total if total else 0.0} for key, count in counter.most_common()]
            )
        distribution(self.source_types, "referencing_entity_type").to_csv(self.staging_root / "rq1_referencing_entity_distribution.csv", index=False)
        distribution(self.target_types, "referenced_entity_type").to_csv(self.staging_root / "rq1_referenced_entity_distribution.csv", index=False)
        distribution(self.event_types, "event_type").to_csv(self.staging_root / "rq1_event_type_distribution.csv", index=False)

        rows = []
        for seed in seeds.itertuples(index=False):
            project_id = str(seed.repo_id)
            profile = self.project_profiles[project_id]
            total = profile["total_reference_records"]
            comment_sources = len(self.comment_source_ids[project_id])
            active_issues = len(self.active_issue_keys[project_id])
            created = pd.to_datetime(seed.repo_created_at, errors="coerce", utc=True)
            project_age = (pd.Timestamp("2023-12-31", tz="UTC") - created).days / 365.25 if pd.notna(created) else math.nan
            rows.append(
                {
                    "project_id": project_id,
                    "repo_name": seed.repo_name,
                    "category_label": seed.category_label,
                    "total_reference_records": total,
                    "self_reference_records": profile["self_reference_records"],
                    "external_project_reference_records": profile["external_project_reference_records"],
                    "non_project_reference_records": profile["non_project_reference_records"],
                    "unresolved_target_reference_records": profile["unresolved_target_reference_records"],
                    "self_reference_ratio": profile["self_reference_records"] / total if total else 0.0,
                    "external_reference_share": (total - profile["self_reference_records"]) / total if total else 0.0,
                    "non_project_reference_share": profile["non_project_reference_records"] / total if total else 0.0,
                    "active_issue_pr_count": active_issues,
                    "comment_related_unique_source_count": comment_sources,
                    "comment_body_ref_count": profile["comment_body_ref_count"],
                    "comment_per_issue": comment_sources / active_issues if active_issues else 0.0,
                    "comment_reference_density": profile["comment_body_ref_count"] / comment_sources if comment_sources else 0.0,
                    "project_age_years_at_2023_end": project_age,
                }
            )
        profiles = pd.DataFrame(rows)
        profiles.to_csv(self.staging_root / "rq1_project_reference_profiles.csv", index=False)
        metrics = [
            "total_reference_records", "self_reference_ratio", "external_reference_share",
            "non_project_reference_share", "active_issue_pr_count", "comment_per_issue",
            "comment_reference_density", "project_age_years_at_2023_end",
        ]
        describe_columns(profiles, metrics).to_csv(self.staging_root / "rq1_descriptive_statistics.csv", index=False)
        age_rows = []
        for metric in ["self_reference_ratio", "external_reference_share", "non_project_reference_share", "comment_reference_density"]:
            clean = profiles[["project_age_years_at_2023_end", metric]].dropna()
            if len(clean) > 2:
                rho, p_value = stats.spearmanr(clean["project_age_years_at_2023_end"], clean[metric])
                age_rows.append({"metric": metric, "n": len(clean), "spearman_rho": rho, "p_value": p_value, "design": "cross_sectional_2023"})
        pd.DataFrame(age_rows).to_csv(self.staging_root / "rq1_project_age_cross_sectional_association.csv", index=False)

    def _write_rq3_outputs(self, seeds, source_frame, targets, brokerage) -> None:
        profiles = pd.read_csv(self.staging_root / "rq1_project_reference_profiles.csv", dtype={"project_id": str})
        target_seed = targets.rename(columns={"target_project_id": "project_id"})[["project_id", "in_degree", "in_strength", "target_coverage"]]
        structural = brokerage[["project_id", "undirected_degree", "undirected_strength", "local_clustering", "betweenness_brokerage"]]
        combined = profiles.merge(source_frame.drop(columns=["repo_name"]), on="project_id", how="left")
        combined = combined.merge(target_seed, on="project_id", how="left").merge(structural, on="project_id", how="left")
        combined["in_lcc"] = combined["project_id"].isin(set(brokerage["project_id"].astype(str)))
        for column in ("in_degree", "in_strength", "target_coverage"):
            combined[column] = combined[column].fillna(0)
        combined.to_csv(self.staging_root / "rq3_seed_role_aware_features.csv", index=False)
        features = [
            "self_reference_ratio", "external_reference_share", "non_project_reference_share",
            "comment_reference_density", "out_degree", "out_strength", "in_degree", "in_strength",
            "local_clustering", "betweenness_brokerage", "project_age_years_at_2023_end",
        ]
        all_tests = []
        all_descriptions = []
        for mode in ("include_mixed", "exclude_mixed_or_multilabel"):
            tests, descriptions = kruskal_fdr(combined, features, mode, self.config.get_int("rq3_min_group_size", 5))
            all_tests.append(tests)
            all_descriptions.append(descriptions)
        pd.concat(all_tests, ignore_index=True).to_csv(self.staging_root / "rq3_kruskal_fdr_effect_sizes.csv", index=False)
        pd.concat(all_descriptions, ignore_index=True).to_csv(self.staging_root / "rq3_subdomain_descriptive_comparison.csv", index=False)

    def _write_provenance(self) -> None:
        pd.DataFrame(self.provenance).to_csv(self.staging_root / "refq_provenance_sample.csv", index=False)

    def _write_manifest(self, seeds: pd.DataFrame) -> None:
        source_repo = Path(str(self.config.source_repository["path"]))
        configured_source = {
            "path": str(source_repo),
            "expected_branch": self.config.source_repository.get("branch"),
            "expected_commit": self.config.source_repository.get("commit"),
            "observed_git": git_info(source_repo),
        }
        if configured_source["observed_git"]["commit"] != configured_source["expected_commit"]:
            raise ValueError("source repository commit drifted during the run")
        if configured_source["observed_git"]["branch"] != configured_source["expected_branch"]:
            raise ValueError("source repository branch drifted during the run")
        implementation_git = git_info(self.workspace)
        if not implementation_git["commit"]:
            raise ValueError("writable RefQ implementation must have a frozen Git commit")
        input_files = [self.inputs["dbms_repos_key_features"], self.inputs["repo_activity_statistics"], *map(Path, seeds["evidence_path"])]
        implementation_files = [
            *sorted((self.workspace / "script" / "ch5_reference_quotient").glob("*.py")),
            self.config.path,
        ]
        output_files = [path for path in self.staging_root.iterdir() if path.is_file() and path.name != "manifest.json"]
        manifest = {
            "schema": "reference_quotient_p0_frozen_manifest_v1",
            "status": "PASS",
            "run_started_at_utc": self.started_at,
            "run_completed_at_utc": utc_now(),
            "study_year": self.config.get_int("study_year"),
            "data_version": self.config.raw["data_version"],
            "entry_point": "python -m script.ch5_reference_quotient.cli --config configs/ch5_reference_quotient_p0.yaml --execute",
            "output_directory": str(self.final_root).replace("\\", "/"),
            "theory": {
                "construct": "Reference Quotient",
                "network": "Project-level Reference Quotient Network",
                "formalization": "Q=M^T R_P M",
                "membership_rule": self.config.raw["membership_rule"],
                "self_loop_policy": self.config.raw["quotient_self_loop_policy"],
                "edge_aggregation_rule": self.config.raw["edge_aggregation_rule"],
                "second_order_projection_executed": False,
            },
            "seed_manifest": {"count": len(seeds), "path": "analysis_seed_manifest_294.csv", "sha256": sha256_file(self.staging_root / "analysis_seed_manifest_294.csv")},
            "source_repository": configured_source,
            "implementation_repository": {
                "path": str(self.workspace).replace("\\", "/"),
                "code_commit": implementation_git["commit"],
                "observed_git": implementation_git,
            },
            "runtime_versions": runtime_versions(),
            "config": file_record(self.config.path),
            "implementation_files": file_records(implementation_files, self.workspace),
            "input_files": file_records(input_files),
            "output_files": file_records(output_files, self.staging_root),
            "validation": {
                "membership_audit": "PASS",
                "quotient_construction_audit": "PASS",
                "seed_observability_audit": "PASS",
                "rq_role_separation": "PASS",
                "single_run_output_chain": "PASS",
            },
        }
        write_json(self.staging_root / "manifest.json", manifest)
