# Chapter 5 RefQ Versioned Repository-Identity Correction Protocol v1

## 1. Executive Decision

```text
VERSIONED_REPOSITORY_IDENTITY_CORRECTION_PROTOCOL = PASS_READY_FOR_HUMAN_REVIEW
protocol_decision = CORRECTION_PROTOCOL_READY_FOR_IMPLEMENTATION_REVIEW
```

This document is a design-only authorization protocol. It does not implement
the correction, regenerate relation or aggregate artifacts, rerun P0, rerun
S1-S7, call GitHub APIs, change the annotation derivative, or modify the
historical frozen package.

The protocol is ready for implementation review because the authoritative
event repository field, source-admission boundary, source aggregation rule,
regeneration DAG, versioning scheme, no-drift gates, stop conditions, and
human authorization gate are explicit. Numerical results are intentionally not
predicted or recomputed here.

## 2. Frozen Scientific Contract

The following remain unchanged:

| contract | frozen value |
|---|---|
| theory | `Q = M^T R_P M` |
| project identity unit | GitHub numeric repository ID |
| primary repository authority | frozen 2024-10 manually curated local enriched derivative |
| local annotation role | frozen enriched derivative |
| event scope | 2023 |
| annotation snapshot | 2024-10 |
| source admission | `event_repo_id == annotated_primary_github_repo_id` |
| membership | retained project-mappable endpoints require one unique `R_<repo_id>` membership |
| self-loop policy | preserve in directed RefQ; exclude from cross-project sensitivity view as already defined |
| edge weight | current unit operationalization: Reference-record multiplicity |
| seed boundary | 301 candidates, 294 analysis seeds |
| related repository policy | preserve distinct numeric identities; exclude as non-seed source; allow as expanded target |
| activity count | QC signal only, not identity authority |
| second-order projection | excluded |

The correction is an observation/provenance repair. It does not merge numeric
repository identities, redefine RefQ, alter membership semantics, or change
the statistical chain.

## 3. Defect Recap

The known Fireproof case has:

```text
annotated primary seed repository = 679889516 (fireproof-storage/fireproof)
historical distinct repository    = 600271677
raw events                        = 893
Reference-bearing events          = 91
candidate Reference records       = 120
project-mappable target records   = 74
non-project target records        = 46
```

The historical evidence file selected for the 679889516 seed contains events
whose raw event repository is 600271677. The old relation materialization
retains the fine-grained source identity but omits explicit event repository
provenance. The old `granu_agg(row, repo_id=...)` call then writes
`src_entity_id_agg = R_<caller repo_id>`, so filename/caller context can make a
600271677 event appear to have source aggregate `R_679889516`.

The corrected interpretation is:

```text
event_repo_id = 600271677
expected_seed_repo_id = 679889516
=> OUT_OF_SEED_SOURCE_OBSERVATION
=> exclude before MembershipRegistry, source profiles, quotient eligibility,
   source aggregation for the RefQ observation view, and edge construction
```

This does not claim that the Reference fact is false. It says that the record
cannot be assigned to the 679889516 seed-centered source observation under the
strict repository-identity contract.

The 600271677 identity may remain an expanded target when a valid source from
another seed references it.

## 4. Current Pipeline Dependency Map

The actual current path is:

```text
raw event CSV
  -> script/build_dataset/query_repos_event_log.py
  -> script/build_dataset/collaboration_relation_extraction.py
  -> GH_CoRe get_obj_collaboration_tuples_from_record
  -> GH_CoRe get_df_collaboration / save_GitHub_Collaboration_Network
  -> repos_GH_CoRe/<repo>_2023.csv
  -> script/build_dataset/granular_aggregation.py: granu_agg
     called from script/complex_network_analysis/Network_params_analysis.py
     with caller repo_id
  -> repos_GH_CoRE_ref_node_agg/<repo>_2023.csv
  -> script/ch5_reference_quotient/seed_selection.py
  -> RefQPipeline._audit_memberships
  -> RefQPipeline._scan_evidence
  -> edge_frame / quotient outputs / RQ1-RQ3
```

| stage | current code path | current identity field | event_repo_id survives? | repo_name used? | caller repo_id used? | source admission | target effect |
|---|---|---|---|---|---|---|---|
| raw event retrieval | `script/build_dataset/query_repos_event_log.py:22-40`; GH_CoRE query helper | raw `repo_id`, `repo_name` | YES in raw event | used to choose files/query scope | indirectly used to form requested names | filename-level only | target payload is retained |
| raw/dedup materialization | `collaboration_relation_extraction_service` and `process_body_content` | raw `repo_id`, `repo_name` | YES in raw/dedup CSV | used for file selection | not an event-level authority | no explicit row admission | none |
| relation extraction | `collaboration_relation_extraction.py:96-128` | `event_id`, fine-grained entity and target properties | NO explicit relation column | file name is retained externally | not in relation row | no row-level source check | target parsed by GH_CoRE |
| fine-grained aggregation | `granular_aggregation.py:19-40` | target `repo_id` from `tar_entity_objnt_prop_dict`; source caller arg | NO | caller/file context supplies source | YES; writes `R_<repo_id>` | no event identity check | target numeric identity retained when parsed |
| aggregate caller | `Network_params_analysis.py:515-524` | `repo_key_id_dict` from activity `repo_id` | NO | maps repo name to file and ID | YES | filename-level | target aggregation applied |
| seed boundary | `seed_selection.py:27-73` | activity `repo_id`, `repo_name`, evidence file | not applicable | used to find evidence filename | activity ID identifies candidate | activity/evidence availability | establishes 294 source seeds |
| membership audit | `pipeline.py:_audit_memberships` | `src/tar_entity_id_agg` | NO | no | inherited aggregate | after current faulty aggregation | both endpoints enter registry |
| RefQ scan | `pipeline.py:_scan_evidence` | `src/tar_entity_id_agg` and entity IDs | NO | evidence filename in provenance sample | expected seed used only for mismatch assertion | too late for source provenance defect | target projects can expand |
| edge construction | `edge_table.py:edge_frame`; `pipeline.py:_write_quotient_outputs` | project IDs from aggregate membership | NO | no | inherited from aggregate | only aggregate eligibility | expanded target nodes allowed |
| RQ outputs | `pipeline.py:_write_rq1_outputs`, `_write_role_outputs`, `_write_rq3_outputs` | seed IDs and derived project metrics | NO | seed names descriptive | seed IDs define output rows | consumes prior stages | target category metadata may be joined |

The two current defects are therefore coupled: relation serialization loses
the event-level identity, and aggregation trusts caller context. The candidate
protocol fixes both without changing target parsing or the quotient formula.

## 5. Corrected Relation Schema

The minimum generic relation schema addition is:

| field | type/encoding | nullability | authority and source |
|---|---|---|---|
| `event_repo_id` | canonical decimal numeric ID serialized as string in CSV; `Int64`/string in data frames | nullable only if raw `repo_id` is absent; source admission blocks such rows | exact `raw_event.repo_id` |
| `event_repo_name` | UTF-8 string | nullable if raw `repo_name` is absent | exact `raw_event.repo_name`, descriptive only |

The relation row already contains `event_id`; its source raw event has `id`.
The corrected materializer must join `relation.event_id == raw_event.id`
within the declared 2023 raw snapshot and propagate the two fields from the
matched raw row. A relation record may fan out from one event, so many relation
rows may join one raw event, but every relation row must have exactly one raw
match.

Required invariants:

```text
if raw_event.repo_id exists:
    relation.event_repo_id == raw_event.repo_id
if raw_event.repo_name exists:
    relation.event_repo_name == raw_event.repo_name
relation.event_repo_id is never derived from filename, repo_name lookup,
annotation, or caller seed ID
```

The join must normalize numeric CSV representations such as `123.0` to the
canonical string `123`, but must fail on non-integral or conflicting values.
If event IDs are not unique within the declared raw snapshot, the candidate
materializer must use `(source_event_file, event_id)` and record that schema
fact; silently choosing one match is forbidden. A missing or multiply matched
join is a blocking gate.

`event_repo_name` is provenance metadata and must never be used as an identity
key. The old relation schema remains readable only through an explicit legacy
adapter that marks `event_repo_id` as unavailable; it is not eligible for a
corrected P0 run.

The RefQ source-observation view may add these context/status fields without
polluting the generic relation asset:

```text
expected_source_context_repo_id
expected_source_context_repo_name
source_admission_status
source_provenance_mismatch
```

The expected context is an assertion and audit field. It cannot overwrite
`event_repo_id`.

## 6. RefQ Source Observation View

Define an explicit logical or materialized view named
`REFQ_SOURCE_OBSERVATION_VIEW`.

For seed `s`, a Reference record is admissible when:

```text
record.relation_type == Reference
record.event_repo_id == s.github_repo_id
record.event_time is within the declared study scope
all existing direct-Reference eligibility rules hold
```

Rows failing only the source identity condition are retained in the generic
relation/provenance layer and classified as:

```text
OUT_OF_SEED_SOURCE_OBSERVATION
```

They do not enter the MembershipRegistry, source profile denominator, RQ1
seed-source counts, quotient eligibility, source project aggregation, or
network edge construction for that seed. They are not physically deleted from
generic relation assets.

Filtering must happen after event provenance enrichment and before
`_audit_memberships`/`_scan_evidence` semantics. The corrected pipeline must
also retain `expected_source_context_repo_id` so it can assert:

```text
admitted row: event_repo_id == expected_source_context_repo_id
```

and report a mismatch count of zero after admission.

## 7. Source Aggregation Contract

The corrected aggregation contract is:

```text
non-Actor source:
    src_entity_id_agg = R_<event_repo_id>
    src_entity_type_agg = Repo

Actor source:
    source artifact identity remains the Actor identity
    source admission still uses event_repo_id
```

Target aggregation remains based on `tar_entity_objnt_prop_dict` and its
numeric `repo_id`/`actor_id`, with the existing fine-grained type logic. The
caller-supplied `repo_id` is renamed conceptually to
`expected_source_context_repo_id` and is used only for assertion and audit.

For every admitted non-Actor row:

```text
event_repo_id == expected_source_context_repo_id
unique_project_membership(src_entity_id_agg) == expected_source_context_repo_id
```

If the first assertion fails, classify and filter the row before membership;
do not repair it by replacing `event_repo_id` with the expected seed ID. If the
second assertion fails after admission, stop with
`SOURCE_SEED_MISMATCH_AFTER_ADMISSION`.

This preserves row-level provenance over caller context and prevents numeric
repository identities from being collapsed because their names look related.

## 8. Target Asymmetry

Target project-mappability remains determined by the existing target
fine-grained identity and aggregate rules. A target does not need to be one of
the 294 seeds. A valid source may reference a related or historical repository
as an expanded target.

Therefore repository `600271677` may remain an `expanded_target_project` when
it is reached from an admissible source of another seed. It is not converted
to `679889516`, and it is not excluded merely because it is not a primary DBMS
seed. The post-correction target gate compares target identity, target type,
and target parsing for all unaffected rows and checks that expanded-target
policy remains enabled.

## 9. Regeneration Boundary

```text
raw external re-query       = NOT REQUIRED
raw event rematerialization = NOT REQUIRED
relation regeneration       = REQUIRED
relation schema migration   = REQUIRED
aggregate regeneration      = REQUIRED
RefQ P0 rerun               = REQUIRED only after candidate gates PASS
S1-S7 rerun                 = CONDITIONAL per dependency gate
```

The existing raw CSVs already contain authoritative event `repo_id` and
`repo_name`; the defect is introduced when those fields are not propagated
into relation rows and when caller context is used during aggregation. A raw
external query would introduce an unauthorized current-state dependency and
is not part of this correction.

The candidate regeneration should use new versioned paths, for example:

```text
data/github_osdb_data/repos_GH_CoRE_v2_identity_corrected/
data/github_osdb_data/repos_GH_CoRE_ref_node_agg_v2_identity_corrected/
```

All 294 relation/aggregate partitions need candidate regeneration because the
schema and provenance columns change. The expected *semantic* source impact is
localized to one seed, Fireproof 679889516; this distinction is required in
the manifest and no-drift report.

The historical `repos_GH_CoRE` and `repos_GH_CoRE_ref_node_agg` paths remain
unchanged and are used as the v1 comparison baseline.

## 10. Unaffected-Seed No-Drift Policy

The no-drift gate compares corrected candidate artifacts to the historical
baseline in layers:

| layer | required comparison |
|---|---|
| raw events | `BYTE_IDENTICAL_REQUIRED` |
| seed manifest and annotation metadata | `BYTE_IDENTICAL_REQUIRED` |
| relation rows for 293 unaffected seeds, excluding newly added provenance columns | `CONTENT_EQUIVALENT_REQUIRED` |
| relation `event_id`, relation type, source/target entity IDs and target parsed properties | `CONTENT_EQUIVALENT_REQUIRED` |
| aggregate rows for 293 unaffected seeds, excluding new provenance/status columns | `CONTENT_EQUIVALENT_REQUIRED` |
| target project identity and fine-grained target type | `CONTENT_EQUIVALENT_REQUIRED` |
| serialization order | `SEMANTIC_EQUIVALENT_ALLOWED` if row-keyed content is equal |
| annotation category metadata | `BYTE_IDENTICAL_REQUIRED` |
| activity and seed boundary | `BYTE_IDENTICAL_REQUIRED` |

The row-keyed relation comparison must require zero unexpected row loss or
addition, zero repo-ID drift, zero target parsing drift, zero Reference-type
drift, and zero category metadata drift. A changed serialization order is not
scientific drift when a canonical row-keyed comparison proves content
equivalence.

The only expected semantic source difference is the Fireproof mismatch scope.
Any change outside that scope is `UNEXPECTED_GLOBAL_CHANGE` until manually
explained and approved.

## 11. Candidate-Input Diff Gate

No corrected P0 execution is authorized until the candidate input report proves:

```text
affected_seed_files = 1
Fireproof event_repo_id=600271677 candidate rows = 120
unaffected_seed_files = 293
analysis_seed_count = 294
candidate_seed_count = 301
raw-event join integrity = PASS
event_repo_id field invariant = PASS
source provenance mismatch after admission = 0
source_seed_membership_mismatch after admission = 0
target numeric conflicts = 0 new conflicts
unexpected relation-type drift = 0
unrelated Reference-record count drift = 0
seed-set drift = 0
```

The known Fireproof composition of 74 project-mappable target records and 46
non-project target records is a diagnostic control only. The corrected run
must establish exact quotient eligibility and edge deltas; no corrected totals
are manually precomputed from 120.

## 12. Membership Invariants

The existing unique membership semantics remain in force:

```text
forall retained v in V_P, exists! p in P : pi(v) = p
```

After source observation filtering, every retained seed-source row must satisfy:

```text
source_project_membership == expected_seed_repo_id
source_seed_membership_mismatch == 0
```

The old mismatch counter remains a post-admission assertion. It must not be
used to justify collapsing `600271677` into `679889516` or any other numeric
identity. New membership conflicts or ambiguous target assignments are
blocking conditions.

## 13. Version, Config, and Tag Strategy

The historical version is immutable. Use the following names only after a
separate implementation authorization:

```text
correction branch:  ch5-refq-repository-identity-correction-v1
data_version:       refq_p0_2023_seed_observation_v2_strict_identity
run_id_prefix:      ch5_refq_correction_v2
config:             configs/ch5_reference_quotient_p0_v2.yaml
candidate output:   outputs/reference_quotient_p0_corrected_v2
candidate relation: data/.../repos_GH_CoRE_v2_identity_corrected
candidate aggregate:data/.../repos_GH_CoRE_ref_node_agg_v2_identity_corrected
final tag:          chapter5-refq-corrected-v2.0
```

The names make the correction version explicit, retain the v1 historical
baseline, and prevent output-directory collision. The old
`configs/ch5_reference_quotient_p0.yaml`, v1 data version, v1 output root,
freeze tag, and freeze commit must not be edited.

The v2 config must record `study_year=2023`, the frozen annotation SHA, raw
snapshot provenance, relation schema version, strict source-admission rule,
membership rule, self-loop and weight rules, random seed `20260731`, expected
seed counts 301/294, correction protocol version, and the v1 baseline tag and
commit.

## 14. Manifest Schema

The optional JSON schema companion
`ch5_refq_versioned_repository_identity_correction_manifest_schema_v1.json`
defines the required corrected manifest fields:

1. implementation commit and config hash;
2. frozen annotation, raw event, relation, aggregate, and seed-manifest hashes;
3. correction protocol and relation schema versions;
4. source admission rule and excluded out-of-seed rows by seed/event repo;
5. unaffected-seed no-drift results;
6. historical baseline tag/commit;
7. corrected output checksums and P0 metrics;
8. S1-S7 rerun decisions.

The manifest must report provenance and results separately. It must never use a
new corrected result as an oracle before old/new comparison is complete.

## 15. Scientific Old/New Comparison Plan

After candidate P0 execution, compare old v1 and corrected v2 for:

```text
fine Reference record counts
project-mappable Reference count
quotient-eligible count
directed RefQ edges including self-loops
self-loop edge count and aggregated weight
cross-project edge count and weight
undirected edge count
node domain and edge-observed nodes
components, LCC size, isolates, clustering, transitivity
Louvain community count and modularity
RQ1 source profiles
RQ2a source metrics
RQ2b target metrics
RQ2c topology
RQ3 sample sizes and effects
```

Each difference must be labeled:

```text
EXPECTED_LOCAL_CHANGE
UNEXPECTED_GLOBAL_CHANGE
PROVENANCE_ONLY_CHANGE
```

The expected local-change hypothesis is limited to records whose source
observation was incorrectly associated with Fireproof 679889516. This protocol
does not assert the sign or magnitude of any corrected metric delta.

## 16. S1-S7 Dependency and Rerun Matrix

| supplement | corrected dependency | default decision before candidate diff | final rule |
|---|---|---|---|
| S1 evidence universe | retained Reference records and source admission | `PENDING` | `RERUN_REQUIRED` if its input hash or retained-record universe changes; otherwise `DOCUMENTATION_ONLY` |
| S2 weight/multiplicity semantics | RefQ edges and multiplicity fields | `PENDING` | `RERUN_REQUIRED` if corrected edge/multiplicity inputs change; otherwise `NO_RERUN_REQUIRED` |
| S3 observation-boundary sensitivity | RefQ network views and canonical construction order | `PENDING` | `RERUN_REQUIRED` if corrected network input changes; otherwise `NO_RERUN_REQUIRED` |
| S4 role/target evidence | target and role outputs | `PENDING` | `RERUN_REQUIRED` if target or role artifacts change; otherwise `NO_RERUN_REQUIRED` |
| S5/S6 structural robustness | network outputs and sampled structural views | `PENDING` | `RERUN_REQUIRED` if their graph inputs change; otherwise `NO_RERUN_REQUIRED` |
| S7 additional validation | validation and provenance boundaries | `PENDING` | `RERUN_REQUIRED` if its audited input changes; otherwise `DOCUMENTATION_ONLY` |

No S1-S7 result is overwritten. Historical supplemental artifacts remain
available for comparison, and corrected supplemental outputs require their own
versioned roots if rerun is authorized.

## 17. Titan Separation Rule

The known Titan case is:

```text
titan-nosql
numeric ID = 157514605
annotation link = meitu/titan
activity repo_name_used = distributedio/titan
```

It is not one of the frozen 294 source seeds and is not part of the Fireproof
correction. It remains a `KNOWN_FUTURE_IDENTITY_REVIEW_CASE`. The candidate
implementation must include a no-touch assertion for Titan; any incidental
change is a blocking drift.

## 18. repo_created_at Freeze Rule

The corrected run reuses the frozen annotation/materialized timestamp values.
It must not call GitHub APIs, refresh current repository state, infer missing
timestamps, or rebuild `repo_created_at`. The prior provenance decision remains:

```text
repo_created_at_original_run = NOT_RECOVERED
repo_created_at_frozen_value_chain = VERIFIED
repo_created_at_conflicting_seed_values = 0
repo_created_at_missing_seed_count = 3
missing_timestamp_effect = EXPLICIT_MISSINGNESS
```

This identity correction is independent of timestamp provenance.

## 19. Stop Conditions

Execution must stop before P0 if any condition occurs:

| condition | evidence required to clear |
|---|---|
| `EVENT_REPO_JOIN_INTEGRITY_FAIL` | complete join audit with zero unmatched/multiply matched rows or approved composite-key explanation |
| `UNEXPECTED_MULTI_SEED_IMPACT` | row-keyed 293-seed no-drift report and human explanation |
| `UNEXPECTED_SEED_SET_CHANGE` | identical candidate/analysis seed manifests and hashes |
| `UNEXPECTED_ANNOTATION_DRIFT` | annotation SHA and field-level diff showing no change |
| `UNEXPECTED_TARGET_ID_DRIFT` | target identity/type diff with approved explanation |
| `NEW_MEMBERSHIP_CONFLICT` | registry report proving no new conflict or a separate approved membership decision |
| `SOURCE_SEED_MISMATCH_AFTER_ADMISSION` | retained-row assertion showing zero mismatch |
| `UNEXPECTED_RELATION_RECORD_DRIFT` | row-keyed relation diff and approved scope explanation |
| `RAW_INPUT_HASH_MISMATCH` | corrected raw snapshot provenance and explicit human approval; otherwise stop |
| `CONFIG_PROVENANCE_MISMATCH` | v2 config hash and baseline fields reviewed |
| `UNAUTHORIZED_FILE_CHANGE` | clean worktree and allowed-path diff |

No failure is cleared by changing a seed ID, collapsing numeric identities,
rounding results, or requerying current GitHub state.

## 20. Phased Future Execution Plan

| phase | scope | required approval before next phase |
|---|---|---|
| C1 | implementation patch, schema adapter, tests; no scientific regeneration | human review of code and tests |
| C2 | candidate relation/aggregate regeneration, join audit, candidate-input diff gate; no P0 | explicit C2 PASS and human authorization |
| C3 | corrected P0 in v2 output root and old/new comparison | scientific diff review |
| C4 | evaluate and run only required S1-S7 supplements | supplemental decision approval |
| C5 | freeze corrected config, manifest, outputs, and tag | corrected scientific freeze approval |
| C6 | update manuscript and figures after corrected baseline freeze | manuscript/figure release approval |

Phase 2B.1 and Phase 2C remain HOLD until C5 is complete. No implementation
phase is authorized by this design document alone.

## 21. Test Plan

No tests are executed in this design task. The future C1/C2 test suite must
include:

1. same `repo_name` with different numeric IDs remains distinct;
2. `event_repo_id` survives relation serialization;
3. source aggregate derives from `event_repo_id`;
4. caller seed ID cannot overwrite row provenance;
5. out-of-seed source rows filter before membership;
6. historical related repository remains an expanded target when valid;
7. Fireproof 600271677 source row is rejected for seed 679889516;
8. Fireproof 679889516 source row is admitted;
9. 293 unaffected seeds have no semantic drift;
10. `source_seed_membership_mismatch` is zero after admission;
11. analysis seed count remains 294;
12. `repo_created_at` is not refreshed;
13. Titan is unchanged by the correction.

## 22. Implementation Authorization Gate

Before C1, a human must explicitly authorize all of the following:

```text
AUTHORIZE_C1_IMPLEMENTATION = YES
AUTHORIZE_C2_CANDIDATE_REGENERATION = NO until C1 tests PASS
AUTHORIZE_C3_P0_EXECUTION = NO in this protocol
AUTHORIZE_SUPPLEMENTAL_RERUN = NO until corrected P0 diff
AUTHORIZE_MANUSCRIPT_UPDATE = NO until corrected freeze
```

The implementation branch must be separate from `main`, the v1 config and
outputs must remain untouched, and candidate artifacts must use new versioned
paths. A failed gate automatically revokes authorization for all later phases.

## 23. Limitations

This design does not inspect or recalculate the exact corrected quotient delta.
It does not prove that all 120 Fireproof historical-ID records were previously
quotient-eligible; the known 74/46 target composition is retained only as a
candidate audit control. It also does not resolve unrelated future identity
cases such as Titan. The protocol relies on the existing raw event snapshot;
if raw event hashes or event join integrity fail, implementation must stop
until a separately authorized source-data decision is made.

## 24. Final Status

```text
VERSIONED_REPOSITORY_IDENTITY_CORRECTION_PROTOCOL = PASS_READY_FOR_HUMAN_REVIEW
recommended_correction_boundary = EVENT_REPOSITORY_PROVENANCE_FIELD + SOURCE_ADMISSION_FILTER + RELATION_SCHEMA + AGGREGATE_REGENERATION; then candidate P0 and conditional supplements
raw_external_requery_required = NO
relation_schema_change_required = YES
aggregate_regeneration_required = YES
P0_rerun_required_after_candidate_gate = YES
analysis_seed_count_expected = 294
expected_affected_source_seeds = 1
expected_unaffected_source_seeds = 293
source_admission_rule = event_repo_id == annotated_primary_github_repo_id, before MembershipRegistry and quotient eligibility
target_policy = project-mappable targets remain eligible as expanded targets even when not one of 294 seeds
membership_invariant = retained source_project_membership == expected_seed_repo_id and source_seed_membership_mismatch == 0
historical_freeze_preserved = YES
recommended_branch = ch5-refq-repository-identity-correction-v1
recommended_data_version = refq_p0_2023_seed_observation_v2_strict_identity
recommended_config = configs/ch5_reference_quotient_p0_v2.yaml
recommended_output_root = outputs/reference_quotient_p0_corrected_v2
recommended_final_tag = chapter5-refq-corrected-v2.0
candidate_input_gate_defined = YES
unaffected_seed_no_drift_gate_defined = YES
scientific_diff_plan_defined = YES
supplemental_rerun_gate_defined = YES
stop_conditions_defined = YES
test_plan_defined = YES
protocol_decision = CORRECTION_PROTOCOL_READY_FOR_IMPLEMENTATION_REVIEW
recommended_next_step = obtain explicit human authorization for C1 implementation-only phase
scientific_code_modified = NO
scientific_data_modified = NO
scientific_outputs_modified = NO
P0_rerun = 0
S1_S7_rerun = 0
GH_CoRE_rerun = 0
network_algorithms_rerun = 0
documentation_commit = 17ba6771809c34bf057b3d8264738e4010f9b9d6 (initial design commit)
metadata_finalization_commit = 132c649b7f0d0310d2c552d6cd3e06fa95525417
push = origin/main after final documentation commit
remote_head_before_push = c8f25a70cf5d04ecce48fb95fd0f1f003a8525a7
```

The historical tag `chapter5-refq-freeze-v1.0` and commit
`68d001551359d120bf2a06cc5e571742df7e7822` are not rewritten or deleted.
