"""C3.7-B3 two-pass streaming S1 parity and boundary tests."""

from __future__ import annotations

import os
from dataclasses import fields

import pandas as pd
import pandas.testing as pdt
import pytest

from supplemental.reference_quotient_v2.scripts.paths import (
    CORRECTED_OUTPUTS_ROOT,
    canonical_path,
)
from supplemental.reference_quotient_v2.scripts.s1_adapter import (
    ADMITTED,
    OUT_OF_SEED,
    S1SourceObservationAdapter,
    SeedPartitionContext,
)
from supplemental.reference_quotient_v2.scripts.s1_evidence_universe import (
    compute_evidence_universe,
    build_future_s1_output_tables,
)
from supplemental.reference_quotient_v2.scripts.s1_streaming import (
    S1StreamingContractError,
    S1StreamingResult,
    assert_s1_streaming_runtime_acceptance,
    build_future_s1_streaming_output_tables,
    run_s1_streaming,
)


SCHEMA = "reference_aggregate_schema_v2_event_repository_provenance"


def _row(
    event_id: str,
    seed: str,
    *,
    src_agg: str = "R_101",
    tar_agg: str = "R_101",
    src_entity_id: str | None = None,
    tar_entity_id: str | None = None,
    src_agg_type: str = "Repo",
    tar_agg_type: str = "Repo",
    tar_entity_type: str | None = "Repository",
    tar_fine_type: str | None = "Repository",
    status: str = ADMITTED,
    event_repo_id: str | None = None,
    mismatch: bool = False,
    relation_type: str = "Reference",
    event_type: str = "IssuesEvent",
) -> dict[str, object]:
    return {
        "event_id": event_id,
        "event_repo_id": event_repo_id if event_repo_id is not None else seed,
        "expected_source_context_repo_id": seed,
        "source_admission_status": status,
        "source_provenance_mismatch": mismatch,
        "relation_type": relation_type,
        "event_type": event_type,
        "src_entity_id": src_entity_id if src_entity_id is not None else "src-%s" % event_id,
        "src_entity_type": "Issue",
        "tar_entity_id": tar_entity_id if tar_entity_id is not None else "tar-%s" % event_id,
        "tar_entity_type": tar_entity_type,
        "src_entity_id_agg": src_agg,
        "src_entity_type_agg": src_agg_type,
        "tar_entity_id_agg": tar_agg,
        "tar_entity_type_agg": tar_agg_type,
        "tar_entity_type_fine_grained": tar_fine_type,
        "aggregate_schema_version": SCHEMA,
    }


def _write_partition(path, rows: list[dict[str, object]]) -> None:
    pd.DataFrame(rows).to_csv(path, index=False)


def _make_adapter(tmp_path, partitions: list[tuple[str, str, list[dict[str, object]]]]):
    root = tmp_path / "aggregate"
    root.mkdir()
    contexts = {}
    paths = []
    for name, seed, rows in partitions:
        path = root / name
        _write_partition(path, rows)
        canonical = canonical_path(path)
        contexts[os.path.normcase(os.fspath(canonical))] = SeedPartitionContext(
            seed_project=seed,
            evidence_path=canonical,
        )
        paths.append(canonical)
    return S1SourceObservationAdapter(contexts, root), paths


def _validated_chunks(adapter, paths, chunksize=2):
    chunks = []
    for path in paths:
        for chunk in pd.read_csv(path, dtype="string", chunksize=chunksize, low_memory=False):
            chunks.append(adapter.validate_reference_chunk(path, chunk))
    return chunks


def _assert_result_parity(in_memory, streaming):
    assert streaming.source_admission_before_count == in_memory.source_admission_before_count
    assert dict(streaming.source_admission_status_counts) == dict(
        in_memory.source_admission_status_counts
    )
    assert streaming.admitted_reference_count == len(in_memory.records)
    assert dict(streaming.membership_summary) == dict(in_memory.membership.summary)
    assert dict(streaming.target_membership_base_counts) == {
        str(key): int(value)
        for key, value in (
            in_memory.records["tar_membership_status"]
            .replace({"CONFLICT_EXCLUDED": "PROJECT_MAPPABLE"})
            .astype(str)
            .value_counts()
            .items()
        )
    }
    assert streaming.conflict_excluded_record_occurrences == int(
        in_memory.records["src_project_id"].notna()
        .mul(in_memory.records["tar_project_id"].notna())
        .mul(
            in_memory.records["src_membership_conflict"]
            | in_memory.records["tar_membership_conflict"]
        )
        .sum()
    )
    assert streaming.quotient_eligible_records == int(
        in_memory.records["quotient_eligibility"].eq("QUOTIENT_ELIGIBLE").sum()
    )
    assert streaming.self_loop_evidence_weight == int(
        in_memory.edge_class_counts.get("SELF_INTERNAL_PROJECT_REFERENCE", 0)
    )
    assert streaming.cross_project_evidence_weight == int(
        in_memory.edge_class_counts.get("CROSS_PROJECT_REFERENCE", 0)
    )
    assert dict(streaming.edge_class_counts) == dict(in_memory.edge_class_counts)
    assert streaming.directed_edge_counts == in_memory.directed_edge_counts

    in_memory_tables = build_future_s1_output_tables(in_memory)
    streaming_tables = build_future_s1_streaming_output_tables(streaming)
    assert list(streaming_tables) == list(in_memory_tables)
    for name in in_memory_tables:
        left = in_memory_tables[name].reset_index(drop=True)
        right = streaming_tables[name].reset_index(drop=True)
        pdt.assert_frame_equal(left, right, check_dtype=False, check_exact=True)


def test_streaming_matches_b2_for_all_compact_outputs_and_duplicate_edges(tmp_path):
    adapter, paths = _make_adapter(
        tmp_path,
        [
            (
                "seed-101.csv",
                "101",
                [
                    _row("self", "101", src_agg="R_101", tar_agg="R_101"),
                    _row("cross-a", "101", src_agg="R_101", tar_agg="R_202", event_type="PullRequestEvent"),
                    _row("cross-b", "101", src_agg="R_101", tar_agg="R_202", event_type="PullRequestEvent"),
                    _row("non-project", "101", src_agg="R_101", tar_agg="N_1", tar_agg_type="Object"),
                    _row("unresolved", "101", src_agg="R_101", tar_agg="unknown", tar_agg_type="Repo"),
                    _row("fallback", "101", src_agg="R_101", tar_agg="R_101", tar_fine_type=None),
                    _row("both-missing", "101", src_agg="R_101", tar_agg="R_101", tar_fine_type=None, tar_entity_type=None),
                    _row("rejected", "101", tar_agg="R_303", status=OUT_OF_SEED, event_repo_id="999", mismatch=True),
                    _row("actor", "101", relation_type="Actor"),
                ],
            ),
            (
                "seed-202.csv",
                "202",
                [_row("second-self", "202", src_agg="R_202", tar_agg="R_202")],
            ),
        ],
    )
    in_memory = compute_evidence_universe(_validated_chunks(adapter, paths))
    registry = tmp_path / "staging" / "membership.sqlite"
    streaming = run_s1_streaming(adapter, paths, registry, chunksize=2)

    _assert_result_parity(in_memory, streaming)
    assert streaming.cross_project_edge_weights[("101", "202")] == 2
    assert len(streaming.cross_project_edge_pairs) == 1
    assert registry.exists() is False
    assert all(not isinstance(getattr(streaming, field.name), pd.DataFrame) for field in fields(streaming))
    assert CORRECTED_OUTPUTS_ROOT.exists() is False


def test_cross_partition_global_conflict_is_applied_in_pass_two_and_matches_b2(tmp_path):
    adapter, paths = _make_adapter(
        tmp_path,
        [
            (
                "seed-101.csv",
                "101",
                [_row("conflict-a", "101", src_agg="R_101", tar_agg="R_202", tar_entity_id="shared")],
            ),
            (
                "seed-202.csv",
                "202",
                [_row("conflict-b", "202", src_agg="R_202", tar_agg="R_303", tar_entity_id="shared")],
            ),
        ],
    )
    in_memory = compute_evidence_universe(_validated_chunks(adapter, paths))
    streaming = run_s1_streaming(adapter, paths, tmp_path / "membership.sqlite", chunksize=1)

    _assert_result_parity(in_memory, streaming)
    assert streaming.membership_conflict_entity_count == 1
    assert streaming.conflict_excluded_record_occurrences == 2
    assert streaming.quotient_eligible_records == 0


def test_rejected_only_and_empty_reference_boundaries_are_compact_and_closed(tmp_path):
    adapter, paths = _make_adapter(
        tmp_path,
        [
            (
                "rejected.csv",
                "101",
                [_row("rejected", "101", status=OUT_OF_SEED, event_repo_id="202", mismatch=True)],
            ),
            (
                "empty.csv",
                "202",
                [_row("actor", "202", relation_type="Actor")],
            ),
        ],
    )
    result = run_s1_streaming(adapter, paths, tmp_path / "registry.sqlite", chunksize=1)
    assert result.source_admission_before_count == 1
    assert result.source_admission_status_counts[OUT_OF_SEED] == 1
    assert result.admitted_reference_count == 0
    assert result.target_membership_base_counts == {}
    assert_s1_streaming_runtime_acceptance(result)
    assert build_future_s1_streaming_output_tables(result)["evidence_universe_flow.csv"].loc[0, "count"] == 1


def test_source_seed_mismatch_is_counted_and_streaming_acceptance_fails_closed(tmp_path):
    adapter, paths = _make_adapter(
        tmp_path,
        [
            (
                "mismatch.csv",
                "101",
                [_row("mismatch", "101", src_agg="R_202", tar_agg="R_101")],
            )
        ],
    )
    result = run_s1_streaming(adapter, paths, tmp_path / "registry.sqlite", chunksize=1)
    assert result.source_seed_membership_mismatch == 1
    with pytest.raises(S1StreamingContractError, match="source_seed_membership_mismatch_is_zero"):
        assert_s1_streaming_runtime_acceptance(result)
    with pytest.raises(S1StreamingContractError, match="source_seed_membership_mismatch_is_zero"):
        build_future_s1_streaming_output_tables(result)


def test_two_pass_partition_order_drift_fails_closed_and_registry_is_cleaned(tmp_path):
    adapter, paths = _make_adapter(
        tmp_path,
        [
            ("seed-101.csv", "101", [_row("a", "101")]),
            ("seed-202.csv", "202", [_row("b", "202", src_agg="R_202", tar_agg="R_202")]),
        ],
    )
    registry = tmp_path / "registry.sqlite"
    with pytest.raises(S1StreamingContractError, match="S1_TWO_PASS_INPUT_DRIFT"):
        run_s1_streaming(
            adapter,
            paths,
            registry,
            chunksize=1,
            pass2_partition_paths=list(reversed(paths)),
        )
    assert registry.exists() is False


def test_registry_path_under_scientific_outputs_is_rejected_without_creation(tmp_path):
    adapter, paths = _make_adapter(tmp_path, [("seed.csv", "101", [_row("a", "101")])])
    registry = CORRECTED_OUTPUTS_ROOT / "_staging" / "membership.sqlite"
    with pytest.raises(S1StreamingContractError, match="under v2 outputs"):
        run_s1_streaming(adapter, paths, registry, chunksize=1)
    assert registry.exists() is False


def test_streaming_module_has_no_s7_or_historical_authority_surface():
    import supplemental.reference_quotient_v2.scripts.s1_streaming as streaming

    assert not hasattr(streaming, "read_canonical_inputs")
    assert not hasattr(streaming, "RAW_USECOLS")
    assert not hasattr(streaming, "select_s7_objects")
    assert "reference_quotient_v1" not in streaming.__file__
