# Chapter 5 RefQ Targeted Frozen-Annotation Provenance Repair v1

## Final Status

TARGETED_PROVENANCE_REPAIR = PASS_WITH_LIMITATIONS
scientific_decision = PROVENANCE_REPAIR_SUFFICIENT_WITH_DOCUMENTED_LIMITATIONS
documentation_commit = PENDING_FIRST_COMMIT
push = PENDING

This is a read-only provenance repair record. It documents the origin and
cross-artifact consistency that can be recovered for the frozen annotation
derivative. It does not correct the annotation file, rerun P0 or S1-S7, call
GH_CoRE or GitHub APIs, run network algorithms, or modify manuscript or frozen
scientific outputs.

## Frozen Controls

| control | result |
|---|---|
| scientific anchor | `chapter5-refq-freeze-v1.0` / `68d001551359d120bf2a06cc5e571742df7e7822` |
| repository state before repair | `OSDB_RefQ` `main` clean, `HEAD=origin/main=92df6a1827de2d6cc3d5bb5e709f7889b9b38e8f` |
| annotation rows / columns | 690 / 22 |
| upstream October rows / columns | 690 / 21 |
| activity materialization rows | 432 |
| activity IDs with multiple historical rows | 20 |
| annotation SHA-256 | `f35b2d646f84248ab6a32ae04dc2ef4df9e12d697f84a53d9abadd741e9c24a8` |
| upstream SHA-256 | `aecf9c168b93f84de5dbc83ba4b5dc1a4ed1a1dc419eae1fe0904eba96b83342` |
| raw annotation / activity mutation | NO |
| P0 rerun | 0 |
| S1-S7 rerun | 0 |
| GH_CoRE / network rerun | 0 |
| API calls | 0 |
| scientific output modification | NO |

The separate `OSDB_RefQ_source_data` clone contained pre-existing untracked
generated assets and was not modified or cleaned.

## Historical Materialization Correction

The earlier derivative audit's statement that the 2024-10 file was first
visible at `009bd98a` is corrected here. That commit contains the 2023-06
annotation file, not the 2024-10 file. The relevant path was added at
`2282800513c13be9d492327e5ced282094571233` with 616 valid numeric repository
IDs. The 32 blank-to-numeric IDs first appear in the 2024-10 path at
`5e84373acb3a38b24168d82d75d7a54d81f0e002`. Commit `720cb95a4731557d52674346f5d56a99a1bb8b56`
then adds `repo_created_at` and related materialization code. The frozen
source-data copy is present at `2944ab7ee828c1af427115d0808d4d62e5ac725e`.

This correction changes provenance documentation only. It does not alter the
historical input or any scientific result.

The earlier report's 20/21 column statement is also corrected: direct headers
are 21 upstream and 22 local, with `repo_created_at` as the local-only field.

## repo_created_at Chain

repo_created_at_original_run = NOT_RECOVERED
repo_created_at_frozen_value_chain = VERIFIED
repo_created_at_conflicting_seed_values = 0
repo_created_at_missing_seed_count = 3
missing_seed_timestamp_effect = EXPLICIT_MISSINGNESS

The 294 seed rows were joined across the annotation derivative, activity
materialization, and frozen seed manifest. Where activity contains multiple
rows for one numeric repository ID, the row matching the frozen
`repo_name_used` was selected; this preserves the canonical historical
repository-name observation instead of allowing a later-name row to overwrite
it. All 294 values agree exactly. The project profile stores only the derived
`project_age_years_at_2023_end`, so its original timestamp is recorded as
`NOT_AVAILABLE`, not reconstructed.

| repository ID | repository | seed order | frozen timestamp |
|---:|---|---:|---|
| 44781140 | greenplum-db/gpdb | 20 | (blank) |
| 65259211 | xap/xap | 126 | (blank) |
| 534109388 | EuclidOLAP/EuclidOLAP | 174 | (blank) |

The three missing seeds remain in the 294 seed domain. They produce explicit
missingness in age-only descriptive and age-association analyses; no value was
imputed and no analysis was recomputed here.

| check | result |
|---|---:|
| seed rows inspected | 294 |
| all annotation/activity/manifest values equal | 294/294 |
| nonblank timestamp values | 291/294 |
| missing timestamp values | 3/294 |

## 32 Numeric Repository-ID Enrichments

The machine-readable row-level record is
`ch5_refq_enriched_repo_id_provenance_v1.csv`. All 32 IDs occur once in the
local 2024-10 derivative, with a nonblank repository link, and no duplicate
link-ID pair elsewhere in that derivative. No original API response, manual
correction record, or later 2024-11/2024-12 upstream match was recovered.

| classification | count |
|---|---:|
| fully traceable origin | 0 |
| multi-artifact consistent, origin unknown | 11 |
| single frozen materialization only | 21 |
| conflicting historical mapping | 0 |
| unresolved | 0 |
| in frozen 294 seeds | 0 |
| in frozen 301 candidates | 7 |
| frozen source evidence present | 0 |
| expanded target nodes | 2 |

The 11 cross-artifact-consistent names are: akumuli, atlas, datahike, dynomitedb, filodb, hadoop, kerf, littled, mldb, tieredmemdb, tile38. This is
consistency of the frozen materializations, not proof of the original API or
annotation-run origin.

Titan (`titan-nosql`, numeric ID `157514605`) is explicitly retained in the
single-materialization class: annotation says `meitu/titan` with timestamp
`2018-11-14T08:18:40Z`, while the activity artifact has blank `repo_name`,
`repo_name_used=distributedio/titan`, and blank `repo_created_at`. This is an
artifact-level mismatch requiring future identity review, but no competing
numeric repository ID was found and it is not classified as a conflicting
historical mapping.

The two expanded target nodes are Hadoop (`23418517`) and Titan (`157514605`).
Their current P0 target metadata has unavailable category labels; no current
P0 statistical result effect was found. None of the 32 IDs is a frozen 294
source seed or has frozen source evidence.

## Closed Differences And Fireproof Control

The 40 blank-to-`-` repository-ID values remain
`PLACEHOLDER_DIFF = REPRESENTATION_ONLY`: `-` is not admitted as a numeric
repository identity by the current code. The 39 `License_info` differences
remain `PROVENANCE_LIMITATION_NON_MATERIAL_TO_CURRENT_P0`; the
`open_source_license` value is unchanged for all 39 rows and active P0
metadata consumers do not use `License_info`.

`fireproof_annotation_derivative_issue = NO`. The approved Fireproof identity
mapping remains unchanged and was not reopened.

## Scientific Boundary

No repository identity correction is applied in this task. The frozen
annotation derivative remains the scientific input for the approved P0. The
repair establishes a documented provenance boundary, not a claim that all
historical enrichments are reproducible from original API responses.

recommended_next_step = VERSIONED_REPOSITORY_IDENTITY_CORRECTION_PROTOCOL_DESIGN

## Final Status Block

```text
TARGETED_PROVENANCE_REPAIR = PASS_WITH_LIMITATIONS
repo_created_at_original_run = NOT_RECOVERED
repo_created_at_frozen_value_chain = VERIFIED
repo_created_at_conflicting_seed_values = 0
repo_created_at_missing_seed_count = 3
missing_seed_timestamp_effect = EXPLICIT_MISSINGNESS
enriched_32_fully_traceable_origin = 0
enriched_32_multi_artifact_consistent_origin_unknown = 11
enriched_32_single_frozen_materialization_only = 21
enriched_32_conflicting_historical_mapping = 0
enriched_32_unresolved = 0
enriched_32_in_frozen_294 = 0
enriched_32_with_source_evidence = 0
placeholder_provenance_status = CLOSED_AS_REPRESENTATION_ONLY
license_info_provenance_status = CLOSED_NON_MATERIAL
materialization_manifest = CREATED
off_by_one_documentation_correction = RECORDED
fireproof_annotation_derivative_issue = NO
scientific_decision = PROVENANCE_REPAIR_SUFFICIENT_WITH_DOCUMENTED_LIMITATIONS
recommended_next_step = VERSIONED_REPOSITORY_IDENTITY_CORRECTION_PROTOCOL_DESIGN
commit = PENDING_FIRST_COMMIT
push = PENDING
```
