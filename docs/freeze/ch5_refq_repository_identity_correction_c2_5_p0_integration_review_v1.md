# C2.5 P0 v2 Source-Admission Integration Review

## Decision

`C2_5_P0_INTEGRATION_READY_FOR_HUMAN_REVIEW`

This patch wires the approved C2 source-observation contract into the
opt-in RefQ v2 pipeline. It does not authorize or execute corrected P0.

## Scope and provenance

- base C2 commit: `7e099098a6ac0a97ab5d98be35dfc740c6568996`
- semantic C1 implementation: `bd9586696336d766e400fe6242267417ccbd60c9`
- historical main: `dc88221ae6e0bb72f2c142b2811a4552c5ec2388`
- historical freeze: `chapter5-refq-freeze-v1.0` at `68d001551359d120bf2a06cc5e571742df7e7822`
- branch: `ch5-refq-repository-identity-correction-v1`

No candidate CSV, historical v1 configuration, manuscript, frozen P0 output,
S1-S7 output, or network result was modified.

## Why the amendment was needed

C2 materialized generic annotated aggregates containing event repository
provenance and source-admission fields, but the P0 pipeline still selected
Reference rows using only `relation_type`. Without this amendment, rejected
out-of-seed observations could enter `MembershipRegistry`, source profiles,
quotient eligibility, and edge construction.

## Exact integration

`_prepare_reference_evidence_chunk()` is the single selection boundary used by
both `_audit_memberships()` and `_scan_evidence()`. In strict v2 it requires:

```text
relation_type == Reference
source_admission_status == ADMITTED_SOURCE_OBSERVATION
event_repo_id == expected_source_context_repo_id
expected_source_context_repo_id == current seed repo_id
```

The helper validates the v2 schema, normalizes numeric repository IDs without
rewriting provenance, validates declared status against the observed event
repository, and returns only the admitted logical view. Rejected rows remain
in generic candidate input files. Any post-admission source membership mismatch
raises `SOURCE_SEED_MISMATCH_AFTER_ADMISSION`.

## v1/v2 separation

The strict path is enabled only when `identity_policy` is
`STRICT_REPOSITORY_IDENTITY`. Historical v1 has no such policy and retains its
relation-only Reference selection. No filename-based auto-detection was added.

## Configuration

`configs/ch5_reference_quotient_p0_v2.yaml` now defines executable
`input_paths.gh_core_ref_node_agg_dir` as the candidate root:

```text
D:/github_repo/OSDB_RefQ_source_data/data/github_osdb_data/repos_GH_CoRE_ref_node_agg_v2_identity_corrected
```

Strict config validation also requires the v2 schema and source-admission
contract, candidate/analysis seed counts `301/294`, and
`repo_created_at_refresh: false`. The historical v1 config still resolves the
historical aggregate root.

## Input-boundary counters

The read-only real-data preflight produced:

| counter | value |
|---|---:|
| input Reference rows before source admission | 3,748,078 |
| admitted Reference rows | 3,747,958 |
| out-of-seed Reference rows | 120 |
| missing event repository rows | 0 |
| invalid event repository rows | 0 |
| affected source seeds | 1 |
| source mismatch after admission | 0 |
| Fireproof admitted control | 58 |
| Fireproof out-of-seed control | 120 |

These are input-boundary counts only. No corrected membership, quotient edge,
RQ, or network total is inferred here. The C2 manifest field
`new_membership_conflicts=0` remains `CANDIDATE_PRECHECK_ONLY`; authoritative
membership conflicts require separately authorized C3 execution.

## Tests

The C2 baseline had 41 collected tests. This patch adds 12 regression tests,
for 53 passing tests in the repository venv. Coverage includes historical v1
filter behavior, strict schema blocking, filter-before-membership and
filter-before-profile/edge behavior, Fireproof-like rejected rows, admitted
rows, context/status assertions, v1/v2 config resolution, `repo_created_at`,
Titan handling, and read-only preflight output immutability.

## Restricted execution record

```text
real_P0_run = 0
network_algorithms_rerun = 0
S1_S7_rerun = 0
C2_data_regeneration = 0
candidate_data_modified = NO
historical_v1_artifacts_modified = NO
corrected_P0_output_created = NO
```

## C3 prerequisites

Human review must confirm this integration and separately authorize C3. C3
may execute the corrected P0 only into the new v2 output root, then compare
the resulting membership, quotient, statistical, and network outputs against
the historical freeze. This C2.5 patch does not authorize that execution.

## Final status

```text
C2_5_P0_V2_INTEGRATION = PASS_READY_FOR_HUMAN_REVIEW
v1_behavior_preserved = YES
v2_source_admission_before_membership = YES
v2_source_admission_before_scan = YES
v2_config_candidate_aggregate_resolved = YES
v2_missing_admission_schema_blocks = YES
membership_conflict_manifest_field = CANDIDATE_PRECHECK_ONLY
recommended_next_step = HUMAN_REVIEW_BEFORE_C3
```
