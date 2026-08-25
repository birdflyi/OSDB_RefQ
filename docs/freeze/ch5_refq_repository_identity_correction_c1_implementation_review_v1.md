# Chapter 5 RefQ C1 Repository-Identity Correction Implementation Review v1

## 1. Decision

```text
C1_REPOSITORY_IDENTITY_IMPLEMENTATION = PASS_READY_FOR_HUMAN_REVIEW
C1_decision = C1_IMPLEMENTATION_READY_FOR_HUMAN_REVIEW
recommended_next_step = HUMAN_REVIEW_BEFORE_C2
```

C1 implemented the opt-in repository-identity correction scaffolding and
synthetic contract tests. It did not regenerate real relation or aggregate
files, create a corrected P0 input, run P0, rerun S1-S7, call GitHub APIs, or
modify any frozen scientific asset.

## 2. Branch And Commit Provenance

| item | value |
|---|---|
| base branch | `main` |
| base commit | `dc88221ae6e0bb72f2c142b2811a4552c5ec2388` |
| C1 branch | `ch5-refq-repository-identity-correction-v1` |
| implementation commit | `bd9586696336d766e400fe6242267417ccbd60c9` |
| documentation commit | `5884363d1fa48fa87cde0ea9fe88d0c7790f96c9` (initial review; finalization recorded below) |
| historical tag | `chapter5-refq-freeze-v1.0` |
| historical scientific anchor | `68d001551359d120bf2a06cc5e571742df7e7822` |
| remote before C1 push | `git@github.com:birdflyi/OSDB_RefQ.git` |

The C1 implementation commit contains only four production files and one test
file. The documentation files in this review are committed separately.

## 3. Files Changed

Production files modified or added: **4**

- `script/build_dataset/repository_identity_provenance.py`
- `script/build_dataset/collaboration_relation_extraction.py`
- `script/build_dataset/granular_aggregation.py`
- `script/ch5_reference_quotient/source_observation.py`

Test files modified or added: **1**

- `tests/ch5_reference_quotient/test_repository_identity_correction.py`

The machine-readable impact table is
`ch5_refq_repository_identity_correction_c1_code_impact_v1.csv`.

## 4. Exact Implementation Architecture

The new v2 path is explicit and opt-in:

```text
raw event row
  -> GH_CoRE relation extraction
  -> preserve_event_repository_provenance=True
  -> attach_event_repository_provenance(event_id -> raw id)
  -> event_repo_id / event_repo_name / join status
  -> granu_agg_with_event_provenance
       source aggregate derives from event_repo_id
       expected seed ID is assertion context only
  -> build_refq_source_observation_view
       retain all rows for audit
       admit only event_repo_id == expected seed repo ID
  -> future C2 MembershipRegistry / profiles / quotient / edges
```

The historical v1 path remains:

```text
preserve_event_repository_provenance=False
  -> existing GH_CoRE relation schema
  -> existing granu_agg(row, repo_id=...)
  -> historical frozen artifacts remain readable and reproducible
```

No C1 code rewires the historical P0 pipeline. C2 must explicitly select the
new schema and source-observation view.

## 5. Relation Schema And Join Safety

The reusable adapter adds:

```text
event_repo_id
event_repo_name
event_repo_provenance_status
```

`event_repo_id` is canonicalized from the raw event `repo_id`; integral forms
such as `600271677.0` become `600271677`. Non-integral, negative, placeholder,
or ambiguous values do not fall back to filename or caller context.

The validator distinguishes:

```text
MATCHED_UNIQUE
RAW_REPO_ID_MISSING
RELATION_EVENT_UNMATCHED
RELATION_EVENT_MULTI_MATCH
REPO_ID_CONFLICT
```

Unmatched, multiply matched, and conflicting joins are blocking for future
corrected materialization. A partition column can be supplied when event IDs
are only unique within a source partition.

Old relation files can be passed through `adapt_legacy_relation_schema`, which
marks `event_repo_id` as unavailable with
`LEGACY_EVENT_REPOSITORY_UNAVAILABLE`. `require_corrected_relation_schema`
rejects that state for v2 input, so legacy readability is not confused with
corrected-run eligibility.

## 6. Source Admission And Aggregation

`admit_source_record` returns one of:

```text
ADMITTED_SOURCE_OBSERVATION
OUT_OF_SEED_SOURCE_OBSERVATION
MISSING_EVENT_REPOSITORY_ID
INVALID_EVENT_REPOSITORY_ID
```

`build_refq_source_observation_view` retains rejected rows in its annotated
frame and returns only admitted direct Reference rows in the logical view.
Therefore an out-of-seed row does not enter the future membership registry,
source profile denominator, quotient eligibility, or edge construction.

`granu_agg_with_event_provenance` derives a non-Actor source aggregate as:

```text
src_entity_id_agg = R_<event_repo_id>
```

The caller/seed ID is stored as
`expected_source_context_repo_id` and cannot overwrite the event identity.
Target aggregation is delegated to the existing parser and is not materially
changed.

## 7. Required Synthetic Contract Tests

The C1 test file covers T1-T14 from the prompt. In particular:

| case | result |
|---|---|
| expected seed `679889516`, event repo `600271677` | `OUT_OF_SEED_SOURCE_OBSERVATION` |
| expected seed `679889516`, event repo `679889516` | `ADMITTED_SOURCE_OBSERVATION` |
| valid source targeting repo `600271677` | target remains `R_600271677` expanded-project eligible |
| missing event repository | no filename or caller fallback |
| ambiguous raw-event join | blocking failure |
| existing relation/raw ID conflict | blocking failure |
| old relation schema | explicit unavailable state; rejected for v2 |
| seed boundary | existing 301/294 contract remains unchanged |
| `repo_created_at` | passed through unchanged; no refresh path |
| Titan-like numeric identity | handled generically; no production special case |

## 8. Test Execution

Executed with the locked project runtime:

```text
venv\Scripts\python.exe -m pytest -q
60 passed, 13 warnings
```

The warnings are existing pandas/NumPy deprecation warnings. `py_compile` for
all four modified production modules and `git diff --check` also passed.

The system `python` outside the locked venv reports NumPy 1.24.2, pandas 1.5.3,
SciPy 1.9.1, and NetworkX 3.2.1; its runtime-lock test fails as expected. It
was not used for the C1 acceptance result. No package installation or runtime
lock modification was performed.

## 9. Real-Data Read-Only Probes

These probes inspected existing source-data and frozen relation files only;
they did not write candidate files or establish C2 gates.

| probe | observed result |
|---|---|
| Fireproof raw rows | 1,330 rows; all 1,330 have non-null `repo_id` and `repo_name` |
| raw repository composition | `600271677`: 893 rows; `679889516`: 437 rows |
| raw event identity | 1,330 unique raw event IDs; no duplicates in the inspected file |
| current aggregate schema | no `event_repo_id`, `event_repo_name`, or `source_admission_status` columns |
| Fireproof Reference rows in current aggregate | 178 rows |
| current Reference rows joined to raw event repo | 178/178 matched uniquely by event ID |
| joined historical-source Reference rows | 120 records across 91 events for repo `600271677` |
| joined frozen-seed Reference rows | 58 records across 41 events for repo `679889516` |

The probes support the C1 architecture and the known Fireproof diagnosis. They
are not a candidate regenerated relation/aggregate diff and therefore remain
`DEFERRED_TO_C2` for acceptance-gate purposes.

## 10. C1 Gates

| gate class | status | reason |
|---|---|---|
| branch/worktree and historical anchor | PASS | C1 started from the clean approved `dc88221` main and the anchor remains an ancestor |
| implementation contract tests | PASS | 60 tests passed in the locked venv |
| relation schema helper | PASS | fields, normalization, statuses, legacy rejection implemented and tested |
| source admission helper | PASS | explicit statuses and retained rejected rows implemented and tested |
| event-derived source aggregation | PASS | caller context cannot overwrite event identity; tested |
| target semantics | PASS | existing target parser reused; expanded-target test passes |
| raw-event read-only assumption probe | PASS_PARTIAL | inspected Fireproof evidence confirms fields and joins; full C2 input gate not run |
| relation/aggregate regenerated artifact gates | DEFERRED_TO_C2 | C1 is forbidden to write those artifacts |
| Fireproof 120-row candidate scope gate | DEFERRED_TO_C2 | confirmed by read-only existing-file probe, not candidate regeneration |
| 293-seed no-drift gate | DEFERRED_TO_C2 | requires corrected relation/aggregate candidates |
| corrected P0 gate | DEFERRED_TO_C2 | C3 authorization explicitly NO |
| S1-S7 rerun decisions | DEFERRED_TO_C2/C4 | depend on corrected P0 hashes |

The protocol acceptance-table typo `PO_CANDIDATE_RUN_GATE` is recorded as
`DOCUMENTATION_TYPO_NON_BLOCKING`; historical protocol files were not edited.

## 11. Historical Freeze, Titan, And Timestamp Controls

The following were verified:

```text
chapter5-refq-freeze-v1.0 unchanged
68d001551359d120bf2a06cc5e571742df7e7822 unchanged
historical P0 config unchanged
historical P0 output root unchanged
historical relation/aggregate directories unchanged
Titan-specific production strings introduced = 0
repo_created_at production changes introduced = 0
```

No current GitHub API was called. No timestamp was refreshed or inferred. The
Titan case remains a generic future identity-review case and is not included
in the correction logic.

## 12. Known Limitations And C2 Prerequisites

C1 does not prove the full 294-file relation/raw join integrity, unchanged
relation-row content for 293 seeds, exact corrected Fireproof quotient deltas,
or old/new P0 scientific equivalence. Those require C2 candidate regeneration.

Before C2, human review must confirm:

1. the relation adapter is applied to every relation partition with the
   correct event partition key;
2. C2 uses the new relation schema and rejects legacy v1 files;
3. source admission occurs before MembershipRegistry and profile/quotient
   calculations;
4. all candidate gates in the approved protocol pass, including the 293-seed
   no-drift gate;
5. C2 does not write the historical v1 relation, aggregate, or P0 roots.

No C2, C3, supplemental rerun, manuscript update, or corrected scientific tag
is authorized by this report.

## 13. Final Status Block

```text
C1_REPOSITORY_IDENTITY_IMPLEMENTATION = PASS_READY_FOR_HUMAN_REVIEW
branch = ch5-refq-repository-identity-correction-v1
base_commit = dc88221ae6e0bb72f2c142b2811a4552c5ec2388
implementation_commit = bd9586696336d766e400fe6242267417ccbd60c9
production_files_modified = 4
test_files_modified_or_added = 1
relation_event_repo_fields_implemented = YES
event_repo_join_validator_implemented = YES
source_admission_implemented = YES
source_aggregation_uses_event_repo_id = YES
caller_context_can_overwrite_event_repo_id = NO
target_semantics_changed = NO
seed_selection_semantics_changed = NO
repo_created_at_semantics_changed = NO
Titan_semantics_changed = NO
historical_v1_artifacts_modified = NO
tests_total = 60
tests_passed = 60
tests_failed = 0
Fireproof_600_source_rejection_test = PASS
Fireproof_679_source_admission_test = PASS
expanded_target_600_test = PASS
legacy_schema_behavior_test = PASS
C1_real_data_gates = DEFERRED_TO_C2
protocol_documentation_typo = RECORDED_NON_BLOCKING
C1_decision = C1_IMPLEMENTATION_READY_FOR_HUMAN_REVIEW
recommended_next_step = HUMAN_REVIEW_BEFORE_C2
P0_rerun = 0
S1_S7_rerun = 0
GH_CoRE_scientific_regeneration = 0
aggregate_scientific_regeneration = 0
network_algorithms_rerun = 0
documentation_commit = 5884363d1fa48fa87cde0ea9fe88d0c7790f96c9
documentation_metadata_finalization_commit = PENDING
push = correction branch after finalization
```

This branch must be reviewed before any C2 candidate regeneration is
authorized. It must not be merged into `main` as a corrected scientific
baseline at this stage.
