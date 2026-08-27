"""C3.7-C synthetic S3 first-order observation-view tests."""

from __future__ import annotations

import inspect

import pandas as pd
import pandas.testing as pdt
import pytest

from script.ch5_reference_quotient import network_views
from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.s3_observation_sensitivity import (
    CANONICAL_SEED_CENTERED_OBSERVED,
    MULTI_SEED_TARGET_VIEW,
    S3_COMMUNITY_COLUMNS,
    S3_OUTPUT_CONTRACT,
    S3_VIEW_NAMES,
    SEED_ONLY_INDUCED,
    build_future_s3_output_tables,
    build_s3_view_inputs,
    compute_s3_observation_sensitivity,
)


def _edges() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"source_project_id": "20", "target_project_id": "10", "weight": 1, "multiplicity": 1, "is_self_loop": False},
            {"source_project_id": "10", "target_project_id": "20", "weight": 2, "multiplicity": 2, "is_self_loop": False},
            {"source_project_id": "20", "target_project_id": "30", "weight": 3, "multiplicity": 3, "is_self_loop": False},
            {"source_project_id": "10", "target_project_id": "30", "weight": 4, "multiplicity": 4, "is_self_loop": False},
            {"source_project_id": "40", "target_project_id": "30", "weight": 1, "multiplicity": 1, "is_self_loop": False},
            {"source_project_id": "30", "target_project_id": "50", "weight": 1, "multiplicity": 1, "is_self_loop": False},
            {"source_project_id": "10", "target_project_id": "50", "weight": 1, "multiplicity": 1, "is_self_loop": False},
            {"source_project_id": "40", "target_project_id": "10", "weight": 1, "multiplicity": 1, "is_self_loop": False},
        ]
    )


def _registry() -> pd.DataFrame:
    return pd.DataFrame({"project_id": ["99", "30", "10", "20", "40", "50", "60"]})


def _seeds() -> pd.DataFrame:
    return pd.DataFrame({"repo_id": ["20", "10", "40", "60"]})


def test_s3_defines_exact_three_views_and_first_order_edges():
    views = build_s3_view_inputs(_edges(), _registry(), _seeds())
    assert tuple(views) == S3_VIEW_NAMES
    assert set(views[CANONICAL_SEED_CENTERED_OBSERVED][0]["source_project_id"]) == {"10", "20", "30", "40"}
    seed_edges = views[SEED_ONLY_INDUCED][0]
    assert set(zip(seed_edges["source_project_id"], seed_edges["target_project_id"])) == {
        ("20", "10"), ("10", "20"), ("40", "10")
    }
    multi_edges = views[MULTI_SEED_TARGET_VIEW][0]
    assert set(multi_edges["target_project_id"]) == {"10", "30", "50"}


def test_s3_node_domains_and_orders_are_deterministic():
    views = build_s3_view_inputs(_edges(), _registry(), _seeds())
    assert views[CANONICAL_SEED_CENTERED_OBSERVED][1] == ("99", "30", "10", "20", "40", "50", "60")
    assert views[SEED_ONLY_INDUCED][1] == ("20", "10", "40", "60")
    assert views[MULTI_SEED_TARGET_VIEW][1] == ("30", "10", "20", "40", "50", "60")
    repeat = build_s3_view_inputs(_edges(), _registry(), _seeds())
    assert {name: value[1] for name, value in views.items()} == {
        name: value[1] for name, value in repeat.items()
    }


def test_s3_shared_network_authority_and_parameters_are_used():
    import supplemental.reference_quotient_v2.scripts.s3_observation_sensitivity as s3

    assert s3.directed_to_undirected_edges is network_views.directed_to_undirected_edges
    assert s3.analyze_undirected_view is network_views.analyze_undirected_view
    result = compute_s3_observation_sensitivity(
        _edges(),
        _registry(),
        _seeds(),
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    assert result.random_seed == 20260731
    assert result.brokerage_sample_size == 500
    assert set(result.summary["random_seed"]) == {20260731}
    assert set(result.summary["view"]) == set(S3_VIEW_NAMES)


def test_s3_repeated_identical_ordered_execution_is_identical():
    first = compute_s3_observation_sensitivity(
        _edges(), _registry(), _seeds(), random_seed=20260731, brokerage_sample_size=500
    )
    second = compute_s3_observation_sensitivity(
        _edges(), _registry(), _seeds(), random_seed=20260731, brokerage_sample_size=500
    )
    pdt.assert_frame_equal(first.summary, second.summary, check_dtype=False, check_exact=True)
    for name in S3_VIEW_NAMES:
        left = first.view_results[name]
        right = second.view_results[name]
        assert left.node_ids == right.node_ids
        pdt.assert_frame_equal(left.undirected_edges, right.undirected_edges, check_dtype=False, check_exact=True)
        pdt.assert_frame_equal(left.lcc_edges, right.lcc_edges, check_dtype=False, check_exact=True)
        pdt.assert_frame_equal(left.communities, right.communities, check_dtype=False, check_exact=True)


def test_s3_output_contract_contains_summary_and_three_view_tables():
    result = compute_s3_observation_sensitivity(
        _edges(), _registry(), _seeds(), random_seed=20260731, brokerage_sample_size=500
    )
    tables = build_future_s3_output_tables(result)
    assert set(tables) == set(S3_OUTPUT_CONTRACT)
    assert tuple(tables["observation_boundary_sensitivity.csv"].columns) == S3_OUTPUT_CONTRACT["observation_boundary_sensitivity.csv"]
    for name in S3_VIEW_NAMES:
        stem = name.lower()
        assert tuple(tables[stem + "_communities.csv"].columns) == S3_COMMUNITY_COLUMNS
    assert not (paths.CORRECTED_OUTPUTS_ROOT / "S3_observation_sensitivity").exists()


def test_s3_module_has_no_historical_or_second_order_authority():
    import supplemental.reference_quotient_v2.scripts.s3_observation_sensitivity as s3

    source = inspect.getsource(s3)
    assert "reference_quotient_v1" not in source
    assert "v1_2_s3_reproducibility_patch" not in source
    assert "X^T" not in source
    assert "network_views" in source
