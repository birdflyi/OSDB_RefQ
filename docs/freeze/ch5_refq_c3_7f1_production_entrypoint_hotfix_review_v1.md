# Chapter 5 RefQ C3.7-F.1 Production Entrypoint Hotfix Review v1

## Decision

`C3_7F1_HOTFIX_PASS_READY_FOR_C4_BATCH_S1_S6`

Phase A repaired one production-entrypoint integration defect. No corrected
scientific stage was executed during Phase A.

## Prior Failure and Root Cause

The prior authorized C4-S1 dry-run stopped before scientific execution with
`KeyError: 'S1_evidence_universe'` in `authorize_stage()`.

The defect was confirmed in the frozen pre-hotfix implementation commit
`e4159f1183463085c68cf1cca5549c083404d16b`: `authorize_stage()` canonicalized
short `S1` to `S1_evidence_universe`, while `STAGE_PHASES` was keyed by short
stage identifiers. This is a `PRODUCTION_ENTRYPOINT_INTEGRATION_DEFECT`, not a
scientific logic, data, fireproof, or supplemental semantic defect.

The existing C3.7-F fixture pipeline used
`execute_stage_control_plane()` and did not exercise production
`authorize_stage()`/`run_stage()`. The missed production-entrypoint coverage is
therefore confirmed.

## Phase A Baseline

```text
branch = ch5-refq-repository-identity-correction-v1
head_before = e4159f1183463085c68cf1cca5549c083404d16b
worktree_before = clean
real_v2_output_root_before = ABSENT
baseline_tests = 175 passed / 0 failed
corrected_p0_manifest_sha256 = 21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7
corrected_p0_config_sha256 = e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658
historical_tag = chapter5-refq-freeze-v1.0
historical_tag_commit = 68d001551359d120bf2a06cc5e571742df7e7822
```

## Exact Hotfix

`STAGE_PHASES` is now derived directly from `STAGE_DIRECTORY_NAMES.items()`:

```text
S1_evidence_universe -> C4-S1
S2_weight_sensitivity -> C4-S2
S3_observation_sensitivity -> C4-S3
S4_community_stability -> C4-S4
S5_brokerage_stability -> C4-S5
S6_figure_ready -> C4-S6
```

No scientific stage computation, authority, configuration, input/output
contract, receipt, hash, or historical immutability semantics changed.

## Coverage Added

Production authorization tests cover all S1-S6 short names, all canonical
directory names, exact phase acceptance, wrong-phase rejection as
`OrchestrationError`, unknown-stage rejection, and phase-map closure. A direct
`run_stage("S1", ..., dry_run=True)` test reaches production preflight and
confirms no scientific execution.

The same-class mapping audit closed successfully:

```text
phase_keys == STAGE_DIRECTORY_NAMES.values() = PASS
dependency_keys == STAGE_DIRECTORY_NAMES.values() = PASS
canonical short/value closure = PASS
stage_output_inventory closure = PASS
```

## Verification

```text
F1_tests_collected = 189
F1_tests_passed = 189
F1_tests_failed = 0
compileall = PASS
git diff --check = PASS
scientific_logic_change_count = 0
P0_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
S1-S6 scientific runs = 0
S7_OVERLAP_RUN = 0
real_v2_output_root = ABSENT
```

The historical C3.7-F review document was not modified. No protected path,
corrected P0, source data, manuscript, figure, tag, or shared network code was
modified.

## Hotfix Commit

```text
prior_implementation_commit = e4159f1183463085c68cf1cca5549c083404d16b
C4_FROZEN_IMPLEMENTATION_COMMIT = resolve after commit
```

The hotfix commit becomes the frozen implementation baseline for the
conditionally authorized C4-BATCH-S1-S6 phase. All C4 invocations must use its
full SHA via `--expected-implementation-commit`.

## Phase B Boundary

Phase B may begin only after this hotfix commit is created, pushed, and the
worktree is clean. C4 remains one-stage-at-a-time, with dry-run, execution,
receipt validation, historical pre/post comparison, and a local output-only
checkpoint after every stage. S7, final `outputs/manifest.json`, figures, and
manuscript changes remain unauthorized.
