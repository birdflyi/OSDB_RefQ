# Chapter 5 RefQ C2 Candidate Materialization Review

## Decision

`C2_CANDIDATE_INPUT_READY_FOR_HUMAN_REVIEW`

This phase created offline candidate relation and aggregate inputs only. It
did not authorize or run C3/P0, construct quotient edges, calculate network
metrics, rerun S1-S7, call GitHub APIs, rerun GH_CoRE semantic extraction, or
query external raw data.

## Provenance

- correction branch: `ch5-refq-repository-identity-correction-v1`
- C2 start tip: `a75523cfad76aa507672cd2f0138cfcdfb1a86c0`
- semantic C1 implementation commit: `bd9586696336d766e400fe6242267417ccbd60c9`
- historical main baseline: `dc88221ae6e0bb72f2c142b2811a4552c5ec2388`
- historical freeze: `chapter5-refq-freeze-v1.0` at `68d001551359d120bf2a06cc5e571742df7e7822`
- source-data snapshot: `ch5-direct-reference-coupling-prep` at `2944ab7ee828c1af427115d0808d4d62e5ac725e`

The C1 documents retain the distinction between the semantic implementation
commit and the documentation-finalized branch tip; this report does not
rewrite that historical record.

## Historical input hash gate

The historical frozen P0 manifest declares 296 input files. A read-only
comparison of every declared file against its recorded SHA-256 produced:

```text
historical_p0_input_hashes = 296/296 MATCH
missing = 0
mismatch = 0
```

The candidate manifest retains the complete historical input-file hash list.

## Offline migration

For each of 294 analysis-seed filenames, frozen raw event rows from
`repos_dedup_content` were joined to frozen v1 relation rows from
`repos_GH_CoRE` by `event_id`. The candidate relation adds only
`event_repo_id`, `event_repo_name`, `event_repo_provenance_status`, and the
declared v2 schema field. Existing relation facts, parsed target fields,
event IDs, and row order were retained.

The candidate aggregate is a `GENERIC_ANNOTATED_AGGREGATE`. It starts from
the frozen v1 Reference aggregate, attaches raw event provenance and source
admission status, and derives non-Actor `src_entity_id_agg` from
`event_repo_id`. Existing target aggregate fields are retained and checked.
The logical admitted Reference view is the subset with
`source_admission_status == ADMITTED_SOURCE_OBSERVATION`; rejected rows remain
in the generic candidate artifact for auditability.

No semantic GH_CoRE extraction or external/API lookup was used.

## Candidate inventory

| item | value |
|---|---:|
| raw partitions | 294 |
| v1 relation partitions | 294 |
| v2 relation partitions | 294 |
| v1 aggregate partitions | 294 |
| v2 aggregate partitions | 294 |
| candidate seeds | 301 |
| analysis seeds | 294 |
| relation rows | 12,518,072 |
| Reference rows | 3,748,078 |
| aggregate rows | 3,748,078 |

Candidate data roots, kept outside this code repository, are:

- `D:\github_repo\OSDB_RefQ_source_data\data\github_osdb_data\repos_GH_CoRE_v2_identity_corrected`
- `D:\github_repo\OSDB_RefQ_source_data\data\github_osdb_data\repos_GH_CoRE_ref_node_agg_v2_identity_corrected`

`CANDIDATE_DATA_PUSH = DEFERRED`; no large candidate CSV is committed here.

## Full event join gate

```text
MATCHED_UNIQUE = 12,518,072
RAW_REPO_ID_MISSING = 0
RELATION_EVENT_UNMATCHED = 0
RELATION_EVENT_MULTI_MATCH = 0
REPO_ID_CONFLICT = 0
```

All 294 relation partitions passed the row-keyed no-drift check after
excluding only the approved provenance/schema fields. Relation row counts,
Reference counts, relation types, fine-grained endpoints, target properties,
and event IDs remained unchanged.

## Source admission and Fireproof control

The full relation candidate contains 3,017
out-of-seed rows across all relation types. The required Reference-specific
control is:

- expected seed `679889516`, event repository `600271677`: **120 Reference records across 91 events**, all rejected as `OUT_OF_SEED_SOURCE_OBSERVATION`;
- event repository `679889516`: **58 Reference records across 41 events**, admitted;
- affected source seeds: **1**;
- unaffected source seeds: **293**;
- admitted-view source mismatch: **0**.

These are candidate-input/source-observation results only, not corrected P0
metrics.

## Aggregate and target gates

- 293 unaffected aggregate partitions: all historical aggregate columns are content-equivalent (`PASS`);
- affected Fireproof aggregate source-identity changes: **120 rows**, exactly the rejected historical-source Reference rows;
- target aggregate identity drift: **0**;
- relation-type drift: **0**;
- Reference multiplicity drift: **0**;
- source aggregate contract failures: **0**;
- annotation drift: **NONE**;
- repo_created_at refresh: **0**;
- Titan unintended change: **NO**.

The 120 changed source aggregate labels are intentionally retained in the
generic annotated candidate for provenance. They are not admitted to the
future corrected RefQ input view.

## Acceptance gates

The machine-readable result is in
`ch5_refq_repository_identity_correction_c2_acceptance_gate_results_v1.csv`.
G01-G25 passed. G26-G28 are explicitly deferred to C3 because P0,
membership/quotient/network computation, and supplemental dependency
decisions are outside C2 authorization.

## Candidate manifest

`ch5_refq_repository_identity_correction_candidate_manifest_v1.json` has
status `CANDIDATE`, records raw/v1/candidate per-file SHA-256 values, records
the annotation and seed-manifest hashes, contains no corrected P0 metrics,
and leaves S1-S7 decisions as `PENDING`.

## Limitations and C3 prerequisites

This report does not claim that corrected membership conflicts, RefQ edges,
P0 statistics, or network outputs have been recomputed. C3 requires a new
human authorization, a v2 candidate configuration review, execution into a
new output root only, and then an old/new scientific comparison before any
manuscript or supplemental decision.

## Final status

```text
C2_REPOSITORY_IDENTITY_CANDIDATE = PASS_READY_FOR_HUMAN_REVIEW
C1_implementation_commit = bd9586696336d766e400fe6242267417ccbd60c9
C2_start_tip = a75523cfad76aa507672cd2f0138cfcdfb1a86c0
GH_CoRE_semantic_reextraction = 0
GitHub_API_calls = 0
raw_external_requery = 0
full_event_join = PASS
relation_unaffected_no_drift = PASS
aggregate_unaffected_no_drift = PASS
affected_source_seed_count = 1
unaffected_source_seed_count = 293
fireproof_out_of_seed_reference_rows = 120
fireproof_out_of_seed_reference_events = 91
fireproof_admitted_reference_rows = 58
fireproof_admitted_reference_events = 41
source_seed_mismatch_after_admission = 0
unexpected_target_identity_drift = 0
new_target_numeric_conflicts = 0
annotation_drift = NONE
repo_created_at_drift = NONE
Titan_unintended_change = NO
candidate_manifest = CREATED
candidate_config = CREATED
acceptance_gates_passed = 25
acceptance_gates_failed = 0
acceptance_gates_deferred_to_C3 = 3
P0_rerun = 0
network_algorithms_rerun = 0
S1_S7_rerun = 0
C2_decision = C2_CANDIDATE_INPUT_READY_FOR_HUMAN_REVIEW
recommended_next_step = HUMAN_REVIEW_BEFORE_C3
```
