"""C3.7-C synthetic S2 threshold and network-authority tests."""

from __future__ import annotations

import inspect

import pandas as pd
import pytest

from supplemental.reference_quotient_v2.scripts import paths
from supplemental.reference_quotient_v2.scripts.s2_weight_sensitivity import (
    S2_OUTPUT_CONTRACT,
    S2ContractError,
    build_future_s2_output_tables,
    compute_s2_weight_sensitivity,
    preflight_corrected_p0_sensitivity_inputs,
    validate_directed_cross_project_edges,
    validate_s2_thresholds,
)


def _edges() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"source_project_id": "1", "target_project_id": "2", "weight": 2, "multiplicity": 2, "is_self_loop": False},
            {"source_project_id": "2", "target_project_id": "1", "weight": 1, "multiplicity": 1, "is_self_loop": False},
            {"source_project_id": "1", "target_project_id": "3", "weight": 5, "multiplicity": 5, "is_self_loop": False},
            {"source_project_id": "3", "target_project_id": "1", "weight": 1, "multiplicity": 1, "is_self_loop": False},
            {"source_project_id": "3", "target_project_id": "4", "weight": 1, "multiplicity": 1, "is_self_loop": False},
        ]
    )


def _registry() -> pd.DataFrame:
    return pd.DataFrame({"project_id": ["1", "2", "3", "4"]})


def test_s2_thresholds_are_applied_to_directed_rows_before_undirected_collapse():
    result = compute_s2_weight_sensitivity(
        _edges(),
        _registry(),
        thresholds=[1, 2, 5, 10],
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    threshold_one = result.undirected_edges_by_threshold[1]
    threshold_two = result.undirected_edges_by_threshold[2]
    pair_one = threshold_one.loc[
        (threshold_one["node_u"] == "1") & (threshold_one["node_v"] == "2")
    ].iloc[0]
    pair_two = threshold_two.loc[
        (threshold_two["node_u"] == "1") & (threshold_two["node_v"] == "2")
    ].iloc[0]
    assert int(pair_one["weight"]) == 3
    assert int(pair_one["directed_edge_count"]) == 2
    assert int(pair_two["weight"]) == 2
    assert int(pair_two["directed_edge_count"]) == 1
    assert int(result.sensitivity.loc[result.sensitivity["threshold"] == 2, "directed_edges_retained"].iloc[0]) == 2


def test_s2_keeps_fixed_node_domain_and_threshold_can_increase_isolates():
    result = compute_s2_weight_sensitivity(
        _edges(),
        _registry(),
        thresholds=[1, 2, 5, 10],
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    assert result.node_ids == ("1", "2", "3", "4")
    assert set(result.sensitivity["nodes"]) == {4}
    isolates = result.sensitivity.set_index("threshold")["isolates"]
    assert int(isolates.loc[2]) > int(isolates.loc[1])
    assert int(isolates.loc[10]) == 4


def test_s2_output_contract_is_complete_and_in_memory_only():
    result = compute_s2_weight_sensitivity(
        _edges(),
        _registry(),
        thresholds=[1, 2, 5, 10],
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    tables = build_future_s2_output_tables(result)
    assert set(tables) == set(S2_OUTPUT_CONTRACT)
    assert tuple(tables["edge_weight_sensitivity.csv"].columns) == S2_OUTPUT_CONTRACT["edge_weight_sensitivity.csv"]
    assert tuple(tables["threshold_2_undirected_edges.csv"].columns) == S2_OUTPUT_CONTRACT["threshold_2_undirected_edges.csv"]
    assert (paths.CORRECTED_OUTPUTS_ROOT / "S2_weight_sensitivity").exists() is False


@pytest.mark.parametrize(
    "thresholds",
    ([1, 1], [2, 1], [0, 1], [1, 2.5], [], [True, 2]),
)
def test_s2_threshold_configuration_is_strictly_validated(thresholds):
    with pytest.raises(S2ContractError):
        validate_s2_thresholds(thresholds)


def test_v2_sensitivity_parameters_must_match_corrected_p0_config():
    config = paths.load_config(paths.DEFAULT_CONFIG_PATH)
    bad_random_seed = dict(config)
    bad_random_seed["random_seed"] = 1
    with pytest.raises(paths.PathGuardError, match="random_seed"):
        paths.validate_scaffold_config(bad_random_seed)
    bad_brokerage = dict(config)
    bad_brokerage["brokerage_sample_size"] = 499
    with pytest.raises(paths.PathGuardError, match="brokerage_sample_size"):
        paths.validate_scaffold_config(bad_brokerage)
    bad_thresholds = dict(config)
    bad_thresholds["s2_directed_weight_thresholds"] = [1, 5, 2]
    with pytest.raises(paths.PathGuardError, match="strictly increasing"):
        paths.validate_scaffold_config(bad_thresholds)


def test_s2_input_contract_rejects_self_loops_and_weight_multiplicity_mismatch():
    self_loop = _edges().iloc[:1].copy()
    self_loop.loc[:, "target_project_id"] = "1"
    with pytest.raises(S2ContractError, match="self-loop"):
        validate_directed_cross_project_edges(self_loop)
    mismatch = _edges().iloc[:1].copy()
    mismatch.loc[:, "multiplicity"] = 3
    with pytest.raises(S2ContractError, match="equal"):
        validate_directed_cross_project_edges(mismatch)
    non_integral = _edges().iloc[:1].copy()
    non_integral.loc[:, "weight"] = 1.5
    with pytest.raises(S2ContractError, match="positive integral"):
        validate_directed_cross_project_edges(non_integral)


def test_s2_canonical_gate_rejects_historical_authority_without_reading_it():
    result = compute_s2_weight_sensitivity(
        _edges(),
        _registry(),
        thresholds=[1],
        random_seed=20260731,
        brokerage_sample_size=500,
    )
    with pytest.raises(S2ContractError, match="corrected P0 root"):
        from supplemental.reference_quotient_v2.scripts.s2_weight_sensitivity import assert_s2_threshold_one_matches_corrected_p0

        assert_s2_threshold_one_matches_corrected_p0(result, paths.HISTORICAL_P0_ROOT)


def test_s2_source_has_no_historical_numeric_or_v1_execution_authority():
    import supplemental.reference_quotient_v2.scripts.s2_weight_sensitivity as s2

    source = inspect.getsource(s2)
    assert "9557" not in source
    assert "6376" not in source
    assert "0.7973095950243088" not in source
    assert "reference_quotient_v1" not in source
    assert "undirected_edges_from_directed" not in source


def test_corrected_p0_sensitivity_preflight_is_headers_only_and_passes():
    result = preflight_corrected_p0_sensitivity_inputs()
    assert result["C3_7C_INPUT_PREFLIGHT"] == "PASS"
    assert result["headers_only"] is True
    assert result["corrected_data_s2_run"] is False
    assert result["corrected_data_s3_run"] is False
    assert result["network_corrected_data_run"] == 0
    assert result["s2_thresholds"] == [1, 2, 5, 10]
    assert result["random_seed"] == 20260731
    assert result["brokerage_sample_size"] == 500
    assert (paths.CORRECTED_OUTPUTS_ROOT / "S2_weight_sensitivity").exists() is False
