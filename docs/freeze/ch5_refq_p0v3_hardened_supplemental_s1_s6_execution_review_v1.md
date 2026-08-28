# Chapter 5 RefQ Hardened Supplemental S1-S6 Execution Review v1

## Decision

`P0V3_HARDENED_SUPPLEMENTAL_S1_S6_COMPLETE_WITH_ROBUSTNESS_ALERTS_READY_FOR_HUMAN_SCIENTIFIC_REVIEW`

Post-interruption Phase A integrity recheck passed. The deterministic
implementation authority remains `de9f03a1efb76f3abd2b7b6239f7748f40498d90`.
The only implementation change is deterministic graph representation/order;
scientific logic change count is zero. The audit transcription correction is
docs-only commit `e2d728c`, and the superseded S2 inventory is docs-only commit
`374d9c8`.

## Stage checkpoints

| Stage | Status | Commit | Key closure |
|---|---|---|---|
| S1 | KEEP_ACCEPTED | `5a670d5157c8a84d545795ef3e8114a5724523dd` | existing receipt and hashes retained; not rerun |
| S2 | PASS | `c879695` | one dry-run, one real run; thresholds 1/2/5/10; deterministic summaries exact |
| S3 | PASS | `1f99c7c` | three frozen views, canonical parity, receipt/hash closure |
| S4 | PASS WITH ROBUSTNESS ALERT | `bf7658a` | 50 seeds, 1,225 pairwise rows, minimum ARI 0.6823671359861659 |
| S5 | PASS | `ceef56c` | 60 runs, k 250/500/1000, inclusion closure; robustness alert false |
| S6 | PASS | `e13d915` | 23 output artifacts, structural summary and figure-ready manifest |

All stage receipts report `PASS`, use the clean supplemental runtime, and bind
to the hardened implementation SHA. The complete file-level output inventory is
frozen in `ch5_refq_p0v3_hardened_supplemental_output_hash_inventory_v1.csv`.

## Runtime and regression gates

The clean runtime is Python 3.9.13, pandas 1.5.3, NumPy 1.26.4, SciPy 1.13.1,
NetworkX 3.1, GH-CoRE 2.3.1, pytest 7.1.2. The accepted P0 runtime is identical
except pandas 1.4.4. Exact commands and collected/pass/fail/deselected/skipped
counts are frozen in `ch5_refq_p0v3_hardened_supplemental_runtime_gate_results_v1.csv`:

- supplemental suite 201/201 passed;
- shared Chapter 5 clean runtime 59 passed, 1 deselected (the pandas-1.4.4
  lock assertion), 0 failed;
- accepted P0 runtime 60/60 passed;
- targeted hardening suite 40/40 passed;
- compileall and `git diff --check` passed.

After outputs were intentionally materialized, a full supplemental rerun reported
196 passed and 5 failures, and the targeted rerun reported 37 passed and 3
failures. Every failure is an old fixture assertion that S3, S4, S5, or S6
output directories must not exist; it does not inspect scientific values or
receipt/hash closure. Excluding exactly those five stale absence assertions
returned 196/196 passed. No code or test patch was made after Phase A.

## Deterministic and scientific results

The fixed-seed matrix remains 320 rows (160 raw, 160 canonical), with 40 runs
per graph mode and threshold. Canonical summaries are threshold 1/2/5/10:
35/0.7969220043681785, 31/0.7970287474802773,
28/0.7962674935766076, and 21/0.7851714821417686. The raw threshold-5 maximum
is corrected to `0.7964351301769141` in the audit document.

S4's controlled seed sensitivity is a scientific interpretation item, not an
execution failure: ARI-to-canonical minimum is 0.6823671359861659 and pairwise
ARI minimum is 0.6092441840471735. S5 has Spearman minimum 0.9998339514284217,
top-50 overlap minimum 0.82, and no robustness alert. Human review must decide
how to interpret S4 variability before manuscript claims.

## Immutability, boundaries, and deferred work

Both historical comparators returned `HISTORICAL_IMMUTABILITY_MATCH`; official
P0-v3 (30 outputs), corrected aggregate (294 partitions), historical P0,
supplemental v1, old supplemental-v2 outputs, and accepted S1 remain unchanged.
The six-file pre-hardening S2 partial was hash-inventoried and removed; the
replacement S2 is the only accepted S2 authority.

P0, GH-CoRE, event rejoin, S7, figure rendering, and manuscript modification
were not executed. `S7=DEFER`, `G09=NOT_EXECUTED`, `G20=NOT_FINALIZED`,
`P0_RUN=0`, `GH_CORE_RUN=0`, `EVENT_REJOIN=0`, and `MANUSCRIPT_MODIFIED=NO`.

## Frozen authority summary

```text
C4_DETERMINISTIC_NETWORK_IMPLEMENTATION_COMMIT = de9f03a1efb76f3abd2b7b6239f7748f40498d90
AUDIT_DOC_CORRECTION_COMMIT = e2d728c
S1_RESULT_COMMIT = 5a670d5157c8a84d545795ef3e8114a5724523dd
S2_RESULT_COMMIT = c879695
S3_RESULT_COMMIT = 1f99c7c
S4_RESULT_COMMIT = bf7658a
S5_RESULT_COMMIT = ceef56c
S6_RESULT_COMMIT = e13d915
scientific_logic_change_count = 0
deterministic_execution_contract_change_count = 1
all_stage_receipts = PASS
all_output_hash_closures = PASS
G18 = PASS
G19 = PASS
G09 = NOT_EXECUTED
G20 = NOT_FINALIZED
```

No merge or tag was created. The branch is ready for human scientific review;
the S4 robustness alert must remain explicit in any subsequent interpretation.
