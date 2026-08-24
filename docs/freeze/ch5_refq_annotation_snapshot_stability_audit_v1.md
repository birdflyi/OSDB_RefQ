# Chapter 5 RefQ Monthly Primary-Repository Annotation Stability Audit v1

## Final Status

ANNOTATION_SNAPSHOT_STABILITY_AUDIT = PASS_WITH_LIMITATIONS
snapshots_expected_range = 2024-01_to_2024-10
snapshots_found = 10
endpoint_january_file = dbfeatfusion_records_202401_automerged_manulabeled_with_repoid.csv
endpoint_october_file = dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv

january_dbms_count = 649
october_dbms_count = 690
union_dbms_count = 692
same_valid_repo_id_count = 576
blank_to_valid_repo_id_count = 0
valid_to_different_valid_id_count = 2
valid_to_blank_count = 0
row_added_count = 43
row_removed_count = 2
open_source_eligibility_change_count = 2
documented_change_reason_count = 1
unresolved_change_reason_count = 46
unexpected_valid_id_disappearance_count = 2
monthly_temporary_valid_to_blank_count = 0
monthly_multi_change_dbms_count = 1
fireproof_annotation_trajectory = MISSING_202401_TO_202403; 679889516_FROM_202404_THROUGH_202410
maintenance_hypothesis = SUPPORTED_WITH_EXCEPTIONS
scientific_decision = KEEP_2024_10_WITH_DOCUMENTED_LIMITATIONS
recommended_next_step = ANNOTATION_MAPPING_HUMAN_REVIEW_THEN_VERSIONED_REPOSITORY_IDENTITY_CORRECTION_PROTOCOL_DESIGN
scientific_code_modified = NO
scientific_data_modified = NO
scientific_outputs_modified = NO
P0_rerun = 0
S1_S7_rerun = 0
network_algorithms_rerun = 0
GH_CoRE_rerun = 0
documentation_commit = PENDING
push = PENDING

This is an annotation/provenance audit. It did not modify scientific code,
GH_CoRE, configuration, raw data, relation or aggregate artifacts, P0
outputs, manuscript, or repository identity rules. No scientific rerun was
performed.

## Scope And Provenance

The upstream repository is
https://github.com/birdflyi/od_label_issue_gen/tree/main/data/database_repo_label_dataframe.
The local read-only clone is D:\github_repo\od_label_issue_gen at HEAD
5f0d306c3263a699feb1039c5835a522dcf6de76 on branch main.
All ten expected monthly snapshots were found, each with a manually labeled
with_repoid file and an identifiable source commit and blob SHA.

| Month | Source commit | Blob SHA | File SHA-256 | Rows | Unique DBMS keys | Valid numeric IDs |
|---|---|---|---|---:|---:|---:|
| 202401 | 20a4783243f3 | ac27c109c8ac | a8146008e42c | 649 | 649 | 580 |
| 202402 | 06e2d954dbb7 | 4ca257b62eda | ae0790a924cc | 654 | 654 | 582 |
| 202403 | f5e8435db6b2 | b17ebb564aae | d17d7c4f5b55 | 658 | 658 | 586 |
| 202404 | dfbc6f5fa57c | 00e73e70c3ae | 1fb254b61bd5 | 668 | 668 | 596 |
| 202405 | c856d02ba459 | fe6756d5d85e | 710a051e7d16 | 677 | 677 | 603 |
| 202406 | 678d3397ac22 | fb48a5e88c6b | aa3ccfde95e1 | 682 | 682 | 608 |
| 202407 | bf36094b3504 | d0a762d1bc41 | ee27489c898e | 683 | 683 | 609 |
| 202408 | 01505a329a9d | fc49f4b37523 | d43c0c884111 | 685 | 685 | 611 |
| 202409 | 688c9e1f1477 | d6199175e08d | 191bcc838411 | 685 | 685 | 611 |
| 202410 | 834836201850 | 0fde579523ec | aecf9c168b93 | 690 | 690 | 616 |

The complete machine-readable provenance and monthly summary is in
docs/freeze/ch5_refq_annotation_snapshot_stability_audit_v1.csv.
The full DBMS-by-month trajectory is in
docs/freeze/ch5_refq_annotation_monthly_trajectory_202401_202410_v1.csv.

## Comparison Key

DBMS_urnform was used as the DBMS-level comparison key. It was non-null and
unique in every snapshot: all ten monthly files have zero duplicate keys and
zero blank keys. Row ordering was not used. X_DBMS_urnform,
Y_DBMS_urnform, and DBMS_common_name were retained only as supporting
descriptive fields. github_repo_link was not used as an identity key.

## January-to-October Endpoint Classification

| Structural category | DBMS count |
|---|---:|
| SAME_VALID_REPO_ID | 576 |
| SAME_BLANK_REPO_ID | 69 |
| BLANK_TO_VALID_REPO_ID | 0 |
| VALID_ID_TO_DIFFERENT_VALID_ID | 2 |
| VALID_TO_BLANK | 0 |
| VALID_TO_PLACEHOLDER | 0 |
| PLACEHOLDER_TO_VALID_REPO_ID | 0 |
| ROW_ADDED_BY_202410 | 43 |
| ROW_REMOVED_BY_202410 | 2 |
| OTHER | 0 |

The 43 October-added DBMS keys contain 38 valid numeric repository IDs and 5
blank repository IDs. There were no January blank-to-valid endpoint changes:
the one monthly blank-to-valid transition occurred for chdb after that key
appeared in the monthly history. Thus, the data support a small amount of
blank completion, but most growth from 649 to 690 keys is row addition rather
than filling a January blank cell.

## Monthly Trajectory

All months from 2024-01 through 2024-10 are available; no continuity month is
missing. Observed transition signals are:

row appeared = 43
row disappeared = 2
blank -> valid = 1
valid -> different valid = 2
temporary valid -> blank with later recovery = 0
valid ID disappearance without later recovery = 2
DBMS with more than one ID/state change = 1

The only multi-change DBMS is chdb, whose trajectory includes
MISSING -> BLANK_REPO_ID -> 606433492 and then remains stable. The two
valid-ID disappearances without later recovery are CeresDB
(496505424, present in January and absent from February onward) and
HEAVY.AI (90541149, present through July and absent from August onward).
The two valid-ID replacements are LonaDB (646427433 -> 750864017) and
Solr (341374920 -> 50229487). Snapshot fields and generic monthly commit
messages do not prove whether these represent correction, migration,
fork/upstream selection, or another reason.

## Changed-ID Case Table

| DBMS key | DBMS | Endpoint class | January ID | October ID | Monthly ID trajectory | Reason |
|---|---|---|---:|---:|---|---|
| ceresdb | CeresDB | ROW_REMOVED_BY_202410 | 496505424 | - | 496505424 -> MISSING -> MISSING -> MISSING -> MISSING -> MISSING -> MISSING -> MISSING -> MISSING -> MISSING | UNRESOLVED_REASON |
| heavyai | HEAVY.AI | ROW_REMOVED_BY_202410 | 90541149 | - | 90541149 -> 90541149 -> 90541149 -> 90541149 -> 90541149 -> 90541149 -> 90541149 -> MISSING -> MISSING -> MISSING | UNRESOLVED_REASON |
| lonadb | LonaDB | VALID_ID_TO_DIFFERENT_VALID_ID | 646427433 | 750864017 | 646427433 -> 646427433 -> 750864017 -> 750864017 -> 750864017 -> 750864017 -> 750864017 -> 750864017 -> 750864017 -> 750864017 | UNRESOLVED_REASON |
| solr | Solr | VALID_ID_TO_DIFFERENT_VALID_ID | 341374920 | 50229487 | 341374920 -> 341374920 -> 341374920 -> 341374920 -> 341374920 -> 341374920 -> 341374920 -> 50229487 -> 50229487 -> 50229487 | UNRESOLVED_REASON |

The 43 row additions and their endpoint fields are retained in
docs/freeze/ch5_refq_annotation_snapshot_change_cases_v1.csv; no causal
reason was assigned to them merely because they appeared in October.
BLANK_COMPLETION is assigned only to the directly observed monthly
blank-to-valid transition. The remaining 46
changed cases have UNRESOLVED_REASON.

## Open-Source Eligibility

Eligibility was evaluated only from the annotation-level open_source_license
field. Event payload license values were not inspected and were not used as a
record-level filter.

The January-to-October common-key comparison finds
2 annotation-level eligibility-state changes:

| DBMS key | DBMS | January value | October value | Classification |
|---|---|---|---|---|
| altibase | Altibase | Y | N | BECAME_INELIGIBLE |
| memgraph | Memgraph | Y#dbdbio>|<dbengines#N | Y | BECAME_ELIGIBLE |

Altibase is a clear BECAME_INELIGIBLE transition (Y -> N). Memgraph changes
from a composite label string to Y; because the January composite value
encodes more than one source label, it is reported as a field change but not
treated as a fully proven eligibility correction.

## Fireproof Control Row

The monthly annotation history contains no Fireproof row from January through
March. It first appears in April with curated primary repository ID
679889516, and that ID/link/license remains unchanged through October. No
monthly annotation snapshot in this audit contains 600271677 for Fireproof.

| Month | Repository state | Numeric ID | Link | Open-source license |
|---|---|---:|---|---|
| 202401 | MISSING | - | - | - |
| 202402 | MISSING | - | - | - |
| 202403 | MISSING | - | - | - |
| 202404 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |
| 202405 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |
| 202406 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |
| 202407 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |
| 202408 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |
| 202409 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |
| 202410 | VALID_NUMERIC_REPO_ID | 679889516 | fireproof-storage/fireproof | Y |

This is consistent with the already approved STRICT_REPOSITORY_IDENTITY
decision. It does not establish repository lineage and does not override the
historical event evidence showing 600271677 in the 2023 observation file.

## Upstream Snapshot Versus Frozen RefQ Copy

The upstream October blob is 0fde579523ec017b61c93f06c2d9eb94cd7832a2 with SHA-256
aecf9c168b93f84de5dbc83ba4b5dc1a4ed1a1dc419eae1fe0904eba96b83342. The current tracked RefQ annotation is
D:\github_repo\OSDB_RefQ\data\github_osdb_data\dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv with SHA-256 f35b2d646f84248ab6a32ae04dc2ef4df9e12d697f84a53d9abadd741e9c24a8.
The same local file hash is present in OSDB_RefQ_source_data.

The current RefQ copy has 21 columns versus 20 upstream columns, with an additional repo_created_at column. Across the 690 common DBMS keys, 591 rows are equal on common columns and 99 rows differ. Field-level differences are 72 in github_repo_id (32 upstream blanks enriched to numeric IDs and 40 upstream blanks represented as placeholder values locally) and 39 in License_info. The local copy has 648 valid numeric IDs, 2 blank IDs, and 40 placeholder/invalid-format IDs.

The local RefQ file is therefore an enriched derivative/materialization of
the upstream October key set, not a byte-identical copy of the upstream
monthly blob. The additional repo_created_at field and the local ID/license
enrichment may be intentional, but this audit found no per-field provenance
document that maps those 99 row changes to specific upstream maintenance
reasons. This is a limitation for release provenance and should be resolved
before a versioned repository-identity correction. It does not by itself
invalidate the monthly upstream trajectory.

## Maintenance Hypothesis

Evidence supporting the hypothesis:

- 576 of 580 January valid numeric repository IDs were preserved unchanged
  through October (99.31%).
- There were no temporary valid-to-blank transitions with later recovery.
- The monthly valid-ID count increased from 580 to 616.
- The October-added rows include 38 valid numeric IDs, and one directly
  observed blank-to-valid completion occurred during the monthly trajectory.
- Fireproof's curated primary annotation is stable from April through October.

Evidence requiring limitations:

- The January-to-October comparison contains zero blank-to-valid changes among
  keys already present in January; most growth is new DBMS rows, not completion
  of January blank cells.
- Two valid IDs disappear without later recovery and two valid IDs change to
  different valid IDs; no case-specific reason is proven by the available
  history.
- The local frozen annotation differs from the upstream October blob in 99
  rows on common columns and has an extra field.
- Monthly commit messages are generic data-update messages, not case-level
  correction records.

Therefore the maintenance hypothesis is SUPPORTED_WITH_EXCEPTIONS, not a
claim that all October mappings are objectively true or that every change was
documented. There is no direct evidence in this audit that October was
produced by activity-based post-hoc reselection; activity counts were not used
to choose or override repository IDs.

## Reviewer-Safe Interpretation And Next Step

The 2024-10 file is defensible as the frozen manually curated post-scope
repository-mapping snapshot used for this study, with explicit limitations:
valid January identities are mostly preserved, the mapping becomes more
complete at the DBMS-key level, and Fireproof's curated identity is stable
once introduced. The audit does not establish that every changed or removed
mapping is correct, and it does not convert annotation history into repository
lineage.

Before any scientific correction, perform human review of the two valid-ID
disappearances, the two valid-ID replacements, and the 99-row difference
between the upstream October blob and the locally frozen enriched derivative.
After that review, design the versioned repository-identity correction
protocol. Do not use activity counts to auto-select a primary repository.

## Controls

scientific_code_modified = NO
scientific_data_modified = NO
scientific_outputs_modified = NO
P0_rerun = 0
S1_S7_rerun = 0
network_algorithms_rerun = 0
GH_CoRE_rerun = 0

## Output Files

- docs/freeze/ch5_refq_annotation_snapshot_stability_audit_v1.md
- docs/freeze/ch5_refq_annotation_snapshot_stability_audit_v1.csv
- docs/freeze/ch5_refq_annotation_snapshot_change_cases_v1.csv
- docs/freeze/ch5_refq_annotation_monthly_trajectory_202401_202410_v1.csv
