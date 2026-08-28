# Chapter 5 RefQ Post-S1-S6 Governance / Test-Harness QA Closure v1

## Decision

`P0V3_S4_ACCEPTED_WITH_LIMITATION_AND_S7_KEEP_GATE_PASS_READY_FOR_FINAL_PACKAGE_FREEZE`

This QA task made no scientific rerun and no scientific implementation change.
The production output tree, six stage receipts, P0-v3, corrected aggregate, and
historical assets remain byte-identical.

## Initial provenance and structural findings

The accepted S1 receipt correctly records execution implementation
`e13eaf2b3bff040639e6256ea98aa1fa5bb0ef1f`; S1 was retained and was not rerun
after graph-order hardening. S2-S6 receipts correctly record
`de9f03a1efb76f3abd2b7b6239f7748f40498d90`. The output inventory now records
these stage-specific receipt implementation commits (57 rows); paths, bytes,
SHA-256 values, and receipt status were not changed.

S6 inspection confirms 8 stable-copy tables + 12 derived tables = 20
scientific tables, plus one `figure_ready_manifest_v2.json` and one
`stage_receipt.json`: 22 stage files total. The prior ambiguous “23 output
artifacts” wording was corrected.

The runtime-gate CSV now has exactly 10 columns on every row. Python's
`csv.DictReader` and pandas both parse it with the same header, no unnamed
columns, and no shifted status/notes fields. PRE_EXECUTION_REGRESSION and
POST_OUTPUT_FINAL_REGRESSION rows are retained separately.

## Stale post-output tests

Before this task, materialized legitimate S3-S6 directories caused five tests
to fail because they asserted that production stage directories must not exist:

| Test path | Test function | Old assumption | Replacement fixture strategy |
|---|---|---|---|
| `supplemental/reference_quotient_v2/tests/test_s3_observation_sensitivity.py` | `test_s3_output_contract_contains_summary_and_three_view_tables` | in-memory table construction implies the real S3 directory is absent | snapshot the legitimate S3 directory before/after and assert byte identity |
| `supplemental/reference_quotient_v2/tests/test_s4_community_stability.py` | `test_s4_uses_weighted_louvain_and_builds_deterministic_tables` | synthetic in-memory S4 computation requires no production S4 directory | snapshot the legitimate S4 directory before/after and assert byte identity |
| `supplemental/reference_quotient_v2/tests/test_s5_brokerage_stability.py` | `test_s5_calls_unweighted_normalized_betweenness_and_closes_frequency` | synthetic in-memory S5 computation requires no production S5 directory | snapshot the legitimate S5 directory before/after and assert byte identity |
| `supplemental/reference_quotient_v2/tests/test_s5_brokerage_stability.py` | `test_corrected_p0_s45_preflight_is_metadata_header_only_and_passes` | metadata-only preflight requires the real S5 directory to be absent | snapshot the legitimate S5 directory before/after and assert byte identity |
| `supplemental/reference_quotient_v2/tests/test_s6_figure_ready.py` | `test_s6_corrected_p0_preflight_is_header_only_and_contracts_are_v2` | metadata-only S6 preflight requires the real S6 directory to be absent | snapshot the legitimate S6 directory before/after and assert byte identity |

The old assertions were valid only while the output root was a pre-execution
empty target. They coupled synthetic/preflight tests to global repository phase
state. The replacement tests preserve the relevant no-write/no-overwrite
property while allowing finalized outputs to exist. Existing tmp_path fixture
tests continue to exercise wrong-root rejection, write-once guards, and
isolated absent targets. Production write guards were not weakened.

Test-only files changed:

- `supplemental/reference_quotient_v2/tests/test_s3_observation_sensitivity.py`
- `supplemental/reference_quotient_v2/tests/test_s4_community_stability.py`
- `supplemental/reference_quotient_v2/tests/test_s5_brokerage_stability.py`
- `supplemental/reference_quotient_v2/tests/test_s6_figure_ready.py`

## Regression closure

The pre-fix post-output result was 196 passed / 5 failed for the full
supplemental suite and 37 passed / 3 failed for the targeted suite. After the
test-only fixture isolation, the clean supplemental runtime reports 201
collected / 201 passed / 0 failed; the targeted deterministic/hardening suite
reports 40 passed / 0 failed. Shared Chapter 5 reports 60 collected / 59
passed / 1 deselected / 0 failed (only the pandas-1.4.4 lock assertion is
deselected), and accepted P0 runtime reports 60 collected / 60 passed / 0
failed. Compileall and `git diff --check` pass.

## Scientific immutability and authority

All 57 output inventory entries still match disk exactly; all six stage receipts
remain byte-identical to their accepted output commits. P0-v3 hash closure is
PASS for 30 outputs, corrected aggregate closure is PASS for 294 partitions,
and historical comparison remains `HISTORICAL_IMMUTABILITY_MATCH`.

S1 remains `KEEP_ACCEPTED`. S2 and S3 remain PASS. S4 remains PASS with
robustness alert (minimum ARI-to-canonical `0.6823671359861659`, pairwise
minimum `0.6092441840471735`; scientific interpretation required). S5 remains
PASS with robustness alert FALSE. S6 remains PASS. The scientific network
implementation authority remains `de9f03a1efb76f3abd2b7b6239f7748f40498d90`;
`scientific_logic_change_count=0` and
`deterministic_execution_contract_change_count=1`.

No S1-S6 stage was rerun in this task. P0, GH-CoRE, event rejoin, S7, figure
rendering, manuscript modification, merge, and tag creation remain out of
scope.

```text
G18 = PASS
G19 = PASS
S4_SCIENTIFIC_REVIEW = ACCEPT_WITH_LIMITATION
S7 = KEPT_FIXED_OBJECT
G09 = PASS
G20 = NOT_FINALIZED
P0_RUN = 0
S1_RUN = 0
S2_RUN = 0
S3_RUN = 0
S4_RUN = 0
S5_RUN = 0
S6_RUN = 0
S7_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
```

## Post-QA scientific interpretation and G09 closure

The human S4 review is frozen as `S4_SCIENTIFIC_REVIEW =
ACCEPT_WITH_LIMITATION`. The canonical 35-community partition is retained as
one deterministic reference realization and is described only as an
algorithmic modular neighborhood view; the seed-sensitivity alert is not a
reason to rerun S4.

A separate read-only G09 audit established
`S7 = KEPT_FIXED_OBJECT` and `G09 = PASS`: fixed source/target/edge sizes are
50/50/100, affected sizes are 1/11/11, and all three exact numeric-ID
intersections are empty. S7 writes, reselection, and raw scientific rerun are
all zero. The audit and complete membership table are frozen in
`ch5_refq_p0v3_s7_fixed_object_overlap_runtime_gate_v1.md` and
`ch5_refq_p0v3_s7_fixed_object_overlap_sets_v1.csv`.

This addendum changes no S1-S6 output, receipt, implementation, or test
record. G20 remains `NOT_FINALIZED`; figures, manuscript edits, merge, and
final tagging remain outside this authorization.
