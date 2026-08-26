# Chapter 5 RefQ C3.7-B2
# Corrected S1 Evidence-Universe Implementation Review v1

审查日期：2026-08-26

Repository：`D:\github_repo\OSDB_RefQ`

Branch：`ch5-refq-repository-identity-correction-v1`

## 1. 授权和基线

本 C3.7-B2 实现完整 S1 evidence-universe 的计算逻辑，但不执行全量 corrected
S1 dataset。不创建 `supplemental/reference_quotient_v2/outputs/`，不生成 publication
tables，不运行 P0、S2-S7、network algorithms、figures 或 manuscript 操作。

```text
base_commit = 7b883f424135c773a0a74159fd4147dd7aa9073c
HEAD_before = 7b883f424135c773a0a74159fd4147dd7aa9073c
implementation_commit = PENDING_SINGLE_C3_7B2_COMMIT
```

开始修改前，既有 v2 baseline 已通过：

```text
tests_collected = 33
tests_passed = 33
tests_failed = 0
```

## 2. 实现范围

| path | classification | purpose |
|---|---|---|
| `supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py` | created | admitted-only membership、evidence classification、cross-tab、unit reconciliation 和 in-memory future output construction |
| `supplemental/reference_quotient_v2/tests/test_s1_evidence_universe.py` | created | deterministic unit/integration fixtures |
| `docs/freeze/ch5_refq_c3_7b2_s1_output_contract_v1.csv` | created | future S1 output schema contract; no result files |
| this review | created | implementation, authority, test and scope review |

`s1_evidence_universe.py` 没有 CLI、`read_csv`、`to_csv`、SQLite、output-root path、
historical v1 path、historical numeric total或 S7 选择/写入接口。它只接收
`ValidatedReferenceChunk`，并在所有 analytical entry point 重新验证：

```text
relation_type = Reference
source_admission_status = ADMITTED_SOURCE_OBSERVATION
source_provenance_mismatch = False
event_repo_id = expected_source_context_repo_id = authoritative_seed_project
```

因此 rejected audit rows 只能停留在 C3.7-B provenance counters；它们不能进入
membership、cross-tab、target eligibility、quotient eligibility、edge class 或分母。

## 3. Historical Semantic Mapping

| historical S1 behavior | B2 classification | corrected B2 realization |
|---|---|---|
| `Reference` relation filter | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | B1 validated `admitted_rows` already filters Reference；B2 validates it again |
| `R_<repo_id>` project parsing and unique membership | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | imports shared `unique_project_membership()` |
| canonical entity identity with project-node fallback | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | imports shared `canonical_project_entity_identity()` |
| global entity-to-project conflict exclusion | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | derives global admitted-only pair set and excludes every conflicting endpoint occurrence from quotient eligibility |
| project-mappable, non-project, unresolved and ambiguous target statuses | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | imports shared `classify_membership()` and retains explicit corrected labels |
| self/internal and cross-project Reference classes | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | eligible rows use equal/unequal source-target project IDs |
| event/entity type cross-tabs and shares | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | in-memory `cross_tab()` preserves Reference-record counting/share definitions |
| source/target/edge composition | `REUSE_UNCHANGED_SCIENTIFIC_SEMANTIC` | generic in-memory `composition_table()` has no top-object selection |
| historical aggregate paths and `RAW_USECOLS` | `REPLACE_HISTORICAL_PATH_OR_CONSTANT` | no aggregate path or reader exists in the module; B1 adapter is the sole input boundary |
| historical total-number assertions | `REPLACE_HISTORICAL_PATH_OR_CONSTANT` | `reconcile_evidence_universe()` checks generic closures only |
| S7 top-object selection, S7 writes and overlap side effect | `REMOVE_S7_SIDE_EFFECT` | absent; S7 remains outside the S1-S6 DAG |
| historical `EDGE` label for evidence weights | `DEPRECATED_PRESENTATION_ONLY` | uses v1.3 `REFERENCE_RECORD` + `AGGREGATED_EDGE_WEIGHT`; structural rows use `EDGE_COUNT` |

No shared P0 code was modified. Shared membership functions are reused; the B2
implementation uses an in-memory pair set rather than the shared disk-backed
`MembershipRegistry`, because B2 is required to remain pure and must not create a
staging database or output root. The membership rule, conflict policy and canonical
identity semantics are unchanged.

## 4. Corrected S1 Classifications and Units

The module computes the following admitted-only classifications:

```text
REFERENCE_RECORD
PROJECT_MAPPABLE | NON_PROJECT | UNRESOLVED | AMBIGUOUS | CONFLICT_EXCLUDED
QUOTIENT_ELIGIBLE | NOT_QUOTIENT_ELIGIBLE
SELF_INTERNAL_PROJECT_REFERENCE | CROSS_PROJECT_REFERENCE | NOT_QUOTIENT_ELIGIBLE_REFERENCE
```

The quotient-eligible condition is unchanged:

```text
source project mappable
AND target project mappable
AND neither canonical endpoint has a global membership conflict
```

The current RefQ unit contract remains explicit:

```text
REFERENCE_RECORD != AGGREGATED_EDGE_WEIGHT != EDGE_COUNT

current directed analytical weight
  = retained eligible Reference-record multiplicity
  = current P0 operationalization only

directed_edge_count
  = number of directed project-pair rows
  != Reference-record multiplicity
```

`build_evidence_universe_flow()` uses `RECORD` for universe counts,
`REFERENCE_RECORD` plus `AGGREGATED_EDGE_WEIGHT` for self/cross eligible evidence
weights, and `EDGE_COUNT` for unique directed project-pair counts. No historical
value is a generic requirement.

## 5. Future Output Contract

The future output location is documented only, not created:

```text
supplemental/reference_quotient_v2/outputs/S1_evidence_universe/
```

The filename/schema contract is [ch5_refq_c3_7b2_s1_output_contract_v1.csv](D:/github_repo/OSDB_RefQ/docs/freeze/ch5_refq_c3_7b2_s1_output_contract_v1.csv).
`FUTURE_S1_OUTPUT_CONTRACT` in the module enforces the same table columns before a
future authorized writer can consume them. Current execution status for every listed
artifact is `CONTRACT_ONLY_NOT_WRITTEN`.

## 6. Validation Helpers

`reconcile_evidence_universe()` prepares future runtime reconciliation without
performing it on all 294 partitions. It separately reports:

1. Source admission: before-admission count, admitted count, per-status closure.
2. Target/evidence universe: project-mappable, non-project, unresolved, ambiguous
   and conflict-excluded accounting.
3. Units: eligible Reference-record total, self/cross evidence-weight closure, and
   separate structural edge counts.
4. Source-observation consistency: `source_mismatch_after_admission` and its
   required zero condition.

These generic checks intentionally do not use `3,748,078`, `1,586,117`,
`1,447,073` or `139,044` as module validity constants. Corrected-baseline fixtures
remain comparison metadata for a later explicitly authorized runtime gate.

## 7. Tests and Isolation

The deterministic fixture includes an admitted self/internal Reference, admitted
cross-project Reference, admitted non-project Reference, admitted unresolved
Reference, an ambiguous target fixture, a target membership-conflict fixture, and a
Fireproof-like out-of-seed source row.

Coverage includes:

- B1 admitted rows accepted; rejected source row has zero S1 analytical contribution.
- self/internal, cross-project, non-project, unresolved, ambiguous and
  quotient-eligibility classification.
- global target conflict exclusion from the quotient universe.
- event-type and entity-type Reference-record cross-tabs; edge-class counts and
  explicit unit distinction.
- generic reconciliation without historical numeric constants.
- no S7 selection/artifact surface, no v2 outputs root and no historical reader API.
- empty Reference partition contributes zero rather than failing the analytical API.
- full C3.7-A and C3.7-B regressions through the complete v2 test suite.

```text
tests_collected = 45
tests_passed = 45
tests_failed = 0
C3_7A_regression = PASS (20 tests)
C3_7B_adapter_regression = PASS (13 tests)
C3_7B2_evidence_universe = PASS (12 tests)
```

The suite emitted 20 pandas dependency deprecation warnings only; it reported no
test failure. No full-data S1 execution is part of this task.

## 8. Immutability and Execution Counters

```text
full_data_S1_run = NO
P0_RUN = 0
S1_BOUNDARY_PREFLIGHT = 0
S1_SCIENTIFIC_RUN = 0
S2_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
supplemental_v2_outputs_root_created = NO
```

The B2 implementation is limited to `supplemental/reference_quotient_v2/` excluding
`outputs/`, plus `docs/freeze/ch5_refq_c3_7b2_*`. G01-G20 remain
`DESIGN_ONLY_NOT_EXECUTED`; synthetic tests do not change any runtime-gate status.

## 9. Limitation and Next Boundary

This implementation proves code readiness and fixture behavior only. It does not
produce corrected S1 values, prove full-data target/evidence reconciliation, run S2-S7
or establish S7 zero-overlap. Those require separate authorization.

```text
C3_7C_authorized = NO
C4_authorized = NO
next_authorization_boundary = human review followed by separately authorized runtime or C3.7-C work
```

## 10. Decision

```text
C3_7B2_S1_IMPLEMENTATION_PASS_READY_FOR_HUMAN_REVIEW
```
