# Chapter 5 RefQ Supplemental Evidence v1.1 Material Completion Report

## 1. Scope

This additive patch completes materials needed by the human-decision audit. It does not modify the manuscript, P0 configuration, canonical outputs, RefQ algorithms, S2/S3/S4/S5 results, thresholds, seeds, `k` values, time window or seed set. The prior v1 files remain in place and are not overwritten.

## 2. Parent Verification

```text
branch = ch5-refq-supplemental-evidence-v1
parent_supplemental_result_commit = ba72987adb2c2339bdf1f7a3b370278c88c29c3c
canonical_parent_commit = 920286e134ca459c8e155942eabc6798ceab8b65
v1_implementation_commit = 18717e7d8d269538872ab5a3bcb923234e52eecc
current_completion_implementation_commit = d222654e2edfac07265f6a86f65c26c3d089d8e1
completion_result_commit = d88c2f872f8fb2ec71261b7f1bdaa5423afff0e7
```

The v1 execution report is intentionally unchanged. Its historical bookkeeping remains: `result_package_commit = recorded by the final commit below`, even though the actual v1 result commit is `ba72987adb2c2339bdf1f7a3b370278c88c29c3c`. Its Section 12 wording that tests were executed separately after report generation is also retained as a historical wording inconsistency. The v1 report records 9 passed and 0 failed tests.

## 3. One-Extra-Scan Audit

Exactly one additional controlled streaming pass was used with the canonical 294-seed manifest, frozen 2023 evidence files, `relation_type = Reference`, the canonical identity/membership/conflict rules and `csv_chunk_size = 100000`. The pass scanned `3,748,078` Reference rows. Cumulative supplemental raw scan count is `2`: v1 = 1 and v1.1 completion = 1. This is not raw-data recollection and not a P0 rerun.

## 4. S1 Eligible-Edge-Class Completion

New files:

- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S1_evidence_universe/event_type_x_eligible_edge_class.csv`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S1_evidence_universe/source_entity_type_x_eligible_edge_class.csv`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S1_evidence_universe/target_entity_type_x_eligible_edge_class.csv`

These tables include only quotient-eligible Reference records and explicitly label their unit as `REFERENCE_RECORD`. The exact closure is:

| eligible edge class | records |
|---|---:|
| SELF_LOOP | 1,447,073 |
| CROSS_PROJECT | 139,044 |
| TOTAL | 1,586,117 |

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
S1 edge-class exact reconciliation = PASS
S1 SELF_LOOP exact = PASS
S1 CROSS_PROJECT exact = PASS
S7 top-source closure = PASS
S5 inclusion-frequency closure = PASS
S6 structural CSV content identity = PASS
canonical output SHA drift = NO
existing S2/S3/S4/S5 output SHA drift = NO
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

The completion report and manifest were recorded in local result commit `d88c2f872f8fb2ec71261b7f1bdaa5423afff0e7`. This bookkeeping update is a local follow-up to record that exact SHA. No push is performed.
