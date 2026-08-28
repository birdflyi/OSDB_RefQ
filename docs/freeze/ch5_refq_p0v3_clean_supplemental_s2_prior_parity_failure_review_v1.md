# Chapter 5 RefQ P0 v3 Clean Supplemental S2 Prior-Parity Failure Review v1

## Decision

`P0V3_CLEAN_S2_FAIL_CLOSED`

The clean supplemental execution stopped at the S2 scientific differential
gate. S1 is durably accepted, S2 was executed exactly once and its partial
stage directory is preserved unchanged, and no S3-S6 or S7 execution followed.
The S2 stage receipt, output inventory, P0-v3 canonical threshold-1 gate, and
historical immutability checks pass. The blocker is the prompt-required prior
S2 scientific-identity comparison.

## Frozen authorities

- Branch: `ch5-refq-repository-identity-correction-v1`
- Official P0 v3 result commit:
  `2d284f4bc83c42ba6555a09a2e42693c5490b827`
- Official P0 v3 manifest SHA-256:
  `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
- Official P0 v3 config SHA-256:
  `43f97f9a2d177d325415bfbcc504f1779882cf83685b4fdebe505c8fed8e7cb0`
- Clean supplemental implementation commit:
  `e13eaf2b3bff040639e6256ea98aa1fa5bb0ef1f`
- Clean output root:
  `supplemental/reference_quotient_v2/outputs_p0v3`
- Prior accepted S2 result commit:
  `08a3c11a42a58958d0c60afe2f79a9d469c0ec5d`

## Runtime

The clean S1 and S2 receipts both record the accepted isolated supplemental
runtime:

- Python 3.9.13
- pandas 1.5.3
- NumPy 1.26.4
- SciPy 1.13.1
- NetworkX 3.1
- GH-CoRE 2.3.1
- Python executable:
  `D:/codex_envs/ch5_refq_supplemental_p0v3_runtime/Scripts/python.exe`

The prior accepted S2 receipt records Python 3.9.13, pandas 1.5.3, NumPy
1.24.2, SciPy 1.9.1, and NetworkX 3.2.1. This runtime difference explains the
observed Louvain sensitivity differences but does not satisfy the explicitly
required prior scientific-identity gate. No differential-policy relaxation,
runtime substitution, code patch, or retry was authorized.

## S1 durable checkpoint

S1 passed receipt, output-hash, P0-v3 provenance, prior-scientific-parity, and
immutability checks. All eight S1 CSV files are DataFrame-exact against the
prior accepted S1. The output-only commit is:

`5a670d5157c8a84d545795ef3e8114a5724523dd`

Frozen S1 counts are:

| Measure | Value |
|---|---:|
| Reference records before admission | 3,748,078 |
| Admitted source observations | 3,747,958 |
| Out-of-seed source observations | 120 |
| Missing / invalid event repository | 0 / 0 |
| Target project-mappable | 1,586,047 |
| Conflict excluded | 0 |
| Quotient eligible | 1,586,047 |
| Self-loop evidence weight | 1,447,073 |
| Cross-project evidence weight | 138,974 |
| Self-loop edge count | 289 |
| Cross-project directed edge count | 9,595 |

## S2 execution and closure

The S2 dry-run passed before the sole scientific execution:

- target S2 directory absent: PASS
- S1 durable upstream receipt: PASS
- official P0-v3 hash closure: PASS
- corrected aggregate 294/294 closure: PASS
- pre-run clean immutability comparison: `HISTORICAL_IMMUTABILITY_MATCH`

The sole S2 real run completed at `2026-08-28T13:29:46.716556+08:00`.
Its receipt status is PASS and records two official P0-v3 input artifacts,
five scientific output artifacts, implementation commit `e13eaf2...`, the
accepted runtime above, and `scientific_logic_change_count = 0`.

S2 canonical and inventory gates:

- thresholds: 1, 2, 5, 10
- threshold-before-undirected-collapse contract: PASS
- P0-v3 threshold-1 dynamic parity: PASS
- threshold-1 undirected edges: 9,547
- threshold-1 directed edges / weight: 9,595 / 138,974
- all four threshold edge tables versus prior S2: DataFrame-exact
- stage receipt contract: PASS
- receipt-declared output SHA closure: PASS
- post-run clean immutability comparison:
  `HISTORICAL_IMMUTABILITY_MATCH`

## Blocking prior-S2 differential

`edge_weight_sensitivity.csv` is not scientifically identical to the prior
accepted S2 summary. All non-community structural counts and measures are
unchanged, and threshold 1 is exact. The following Louvain fields differ:

| Threshold | Clean communities | Prior communities | Clean modularity | Prior modularity |
|---:|---:|---:|---:|---:|
| 1 | 35 | 35 | 0.7969220043681785 | 0.7969220043681785 |
| 2 | 30 | 31 | 0.7971408709601703 | 0.7971678810399976 |
| 5 | 25 | 26 | 0.7954773773187964 | 0.7955748244955425 |
| 10 | 19 | 19 | 0.7856263899246017 | 0.7850877914525455 |

Because the execution authorization states that unexplained or non-identical
S2 scientific sensitivity results are a blocker, the current stage cannot be
accepted as an output-only result checkpoint. The runtime cause is documented,
but accepting it would require a new human-authorized differential policy or a
new execution strategy; neither is inferred here.

## Preserved partial S2 inventory

The uncommitted partial directory is
`supplemental/reference_quotient_v2/outputs_p0v3/S2_weight_sensitivity/` and
must remain unchanged for diagnosis.

| File | Bytes | SHA-256 |
|---|---:|---|
| `edge_weight_sensitivity.csv` | 1,343 | `f0be076ad3a94ec98a6fabde0d813bdc16161303cf7f87ff86f29dc6a7eb087d` |
| `stage_receipt.json` | 2,963 | `1f2f5b4c5f566ed8ff30db82fbb45f903e55003e39c38420fbca4aea864083fa` |
| `threshold_1_undirected_edges.csv` | 217,657 | `30514267865f5baa3a50df6a3058e0b1ea5bddf83ef72b9884b302a156e06fc9` |
| `threshold_2_undirected_edges.csv` | 110,655 | `d105d96dad6e98bd4463595499838ba386bbf3d005f1845b6d9f4e93e2dc8bc7` |
| `threshold_5_undirected_edges.csv` | 53,825 | `514baffc1bafe744ce2700fcde43ef1fc6e5d1ca2e0877af6d83b9bcb2592d43` |
| `threshold_10_undirected_edges.csv` | 34,062 | `71c0975f8cdec8ff77f6dd02ed7a5cf29b6a2ee1b1c8f7e6161e9b1eea9db565` |

## Stop boundary and counters

```text
S1_run = PASS
S1_result_commit = 5a670d5157c8a84d545795ef3e8114a5724523dd
S1_prior_scientific_parity = PASS

S2_run = FAIL
S2_result_commit = NOT_COMMITTED
S2_p0v3_threshold1_parity = PASS
S2_prior_scientific_parity = FAIL

S3_run = NOT_RUN
S4_run = NOT_RUN
S5_run = NOT_RUN
S6_run = NOT_RUN
S7_run = 0

S1_SCIENTIFIC_RUN_THIS_TASK = 1
S2_SCIENTIFIC_RUN_THIS_TASK = 1
S3_SCIENTIFIC_RUN_THIS_TASK = 0
S4_SCIENTIFIC_RUN_THIS_TASK = 0
S5_SCIENTIFIC_RUN_THIS_TASK = 0
S6_SCIENTIFIC_RUN_THIS_TASK = 0

P0_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
scientific_logic_change_count = 0

G18_clean_execution_closure = FAIL
G19_clean_immutability_interval = PASS
G09_S7 = NOT_EXECUTED
G20_final_manifest = NOT_FINALIZED
push_status = NOT_PERFORMED
```

No S2 result commit, S3-S6 execution, S7 overlap gate, final release manifest,
figure rendering, manuscript update, merge, tag, or push was performed after
the blocking differential was identified.
