# Chapter 5 RefQ Submission Editing Batch C
# Methods Operational-Definition Reconciliation

## Decision

`CH5_REFQ_SUBMISSION_EDIT_BATCH_C_METHODS_PASS`

The authoritative external manuscript was edited only within the authorized
Methods regions. Its operational definitions now match the accepted P0-v3
implementation and frozen scientific outputs. Cross-section terminology remains
intentionally deferred to a later authorized pass.

## 1. Starting identities

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before | `493abf0505e21772e2fc529add2f19e3c3b96b0f` |
| Remote HEAD before | `493abf0505e21772e2fc529add2f19e3c3b96b0f` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Manuscript SHA before | `2ADF5AC63C1EC696EC2EC411444FC04B5588D3BC539CECD5A7C8F01976C9B2E1` |
| Manuscript SHA after | `BEB6E89127032EA93843AB2385573EE1306C087A06B182753A24AB9E74ED1761` |
| Primary audit authority | `docs/freeze/ch5_refq_submission_methods_fact_semantics_audit.md` |
| P0-v3 manifest SHA-256 | `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776` |
| Supplemental package manifest SHA-256 | `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd` |

The four pre-existing untracked V3/V4/V5/V6 ZIP archives were preserved and
were not staged.

## 2. Authority hierarchy

The edit used the following order: L0 accepted corrected P0-v3 and supplemental
scientific authorities; L1 current implementation/configuration/manifests/audits;
L2 repository-identity, source-admission and annotation governance; L3 Appendix A;
L4 current manuscript Methods; L5 historical prose. Historical wording was not
used to override the corrected implementation.

## 3. Methods correction matrix

| ID | Section | Old manuscript claim | Frozen operational authority | Treatment | Cross-section follow-up? |
|---|---|---|---|---|---|
| C01 | §3.1.1 | Domain, activity, diversity, license and observability appeared as one flat rule | Upstream curation is distinct from P0 gates; category/diversity are descriptive | Layered sample-construction prose | No |
| C02 | §3.1.1 | 294 admission was not decomposed | 301 activity candidates -> 294 when frozen 2023 evidence file exists | Added exact seven-exclusion gate | No |
| C03 | §3.1.1 | Annotation time was implicit | Event scope 2023; mapping snapshot 2024-10, post-scope curated snapshot | Added temporal and identity contract | No |
| C04 | §3.1.2 | "Collected GitHub logs" left historical source/API roles implicit | Persisted OpenDigger/GHArchive-derived events; API validation/enrichment | Added provenance role sentence | No |
| C05 | §3.1.2 | Records were said to be removed by event ID | Frozen P0 Reference dedup is `none`; upstream content normalization is separate | Removed unsupported active event-ID dedup claim | No |
| C06 | §§3.1.3/3.2.2 | GH_CoRE overview and extraction flow conflated duplicate controls | Upstream match/content controls differ from P0 retained-record policy | Separated overview and operational contract | No |
| C07 | §3.2.2 | Source admission was not stated as an exact rule | `relation_type == Reference` and `event_repo_id == frozen annotated seed github_repo_id` before membership | Added strict source-admission state | No |
| C08 | §3.2.3/§3.4.4 | Full denominator chain repeated at four levels | §3.2.3 is the single denominator/RQ mapping authority | Added authority sentence and removed §3.4.4 repetition | No |
| C09 | §3.3.1 | `external_reference_share` described external-resource share | `(total - self) / total`, complete non-self share | Renamed semantic term to Non-self Reference Share; field name retained | Yes, Results/labels |
| C10 | §3.3.1 | `non_project_reference_share` was not separately defined | `non_project_reference_records / total_reference_records` | Added separate subset definition | Yes, Results/labels |
| C11 | §3.3.1 | Active Issues/PRs implied all active issue/PR units | Unique `repo_id#issue_or_pr_number` keys from five admitted source-ID prefixes | Replaced with Reference-bearing Issue/PR Context Count | Yes, Results/table labels |
| C12 | §3.3.1 | `comment_per_issue` was comments per issue | Unique five-prefix source entities / unique issue/PR keys | Replaced legacy New Comment Rate semantics | Yes, Results/table labels |
| C13 | §3.3.1 | `comment_reference_density` was references/comments | Five-prefix admitted Reference rows / unique five-prefix source entities | Replaced denominator and label semantics | Yes, Results/table labels |
| C14 | §3.3.1 | Age formula and missingness were implicit | Frozen `repo_created_at`, 2023-12-31 UTC, `/365.25`; 291 complete, 3 missing, no imputation | Added exact formula and complete-case policy | No |
| C15 | §3.3.3 | FDR scope was underspecified and group threshold omitted | Minimum 5 nonmissing observations per category; at least 2 groups; BH across all computed feature tests within mode | Added eligibility and family definition | No |
| C16 | §3.3.2 | Fixed sample/seed did not expose weight settings | Weighted Louvain/modularity; unweighted clustering and betweenness | Added exact settings | No |
| C17 | §3.4.3 | Block sum did not state row-to-unit operationalization | One eligible retained Reference row contributes one ordered pair weight unit | Added bounded operational clause | No |

## 4. Seed-selection state

```text
upstream curated DBMS/repository and open-source eligibility
    -> repo_name non-null
    -> numeric i_pr_rec_cnt >= 10
       = 301 P0 candidate seeds
    -> expected frozen 2023 aggregate evidence CSV exists
       = 294 analysis seeds
```

```text
CANDIDATE_SEED_COUNT = 301
ANALYSIS_SEED_COUNT = 294
ACTIVITY_THRESHOLD = 10
ACTIVITY_FIELD = i_pr_rec_cnt
SEVEN_EXCLUSIONS_REASON = FROZEN_2023_EVIDENCE_UNAVAILABLE
SEED_SELECTION_LAYERING = PASS
```

dbdb.io/DB-Engines/category metadata and license eligibility remain upstream
curation inputs; technical diversity is descriptive sample coverage. P0 does not
re-execute those as additional gates.

## 5. Annotation time and repository identity

```text
EVENT_OBSERVATION_SCOPE = 2023
ANNOTATION_SNAPSHOT = 2024-10
ANNOTATION_ROLE = POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT
PROJECT_IDENTITY_UNIT = GITHUB_NUMERIC_REPOSITORY_ID
PRIMARY_REPOSITORY_AUTHORITY = frozen annotation github_repo_id
```

The manuscript now states that 2024-10 is neither a 2023-12 repository-state
snapshot nor an event-time identity replacement. `repo_name/full_name` remain
descriptive/retrieval metadata. Activity has two disambiguated roles: the
`i_pr_rec_cnt >= 10` P0 gate and a separate QC/anomaly signal that cannot override
curated numeric identity.

```text
ANNOTATION_TIME_ROLE = PASS
REPOSITORY_IDENTITY_AUTHORITY = PASS
ACTIVITY_ROLE_DISAMBIGUATED = PASS
```

## 6. Historical source and source-admission state

Historical facts are persisted OpenDigger/GHArchive-derived GitHub event records
for 2023. GitHub GraphQL/REST is limited to validation, enrichment, gap filling,
and entity/repository checking; it is not historical identity authority.

```text
HISTORICAL_EVENT_SOURCE = OPENDIGGER_GHARCHIVE_DERIVED_PERSISTED_EVENTS
GITHUB_API_ROLE = VALIDATION_ENRICHMENT
API_AS_HISTORICAL_IDENTITY_AUTHORITY = 0
```

The source-admission state is:

```text
relation_type == Reference
AND event_repo_id == frozen annotated seed github_repo_id
    -> source-observation view
    -> membership registry / profiles / edges
```

The filter executes before membership and profile/edge accumulation. The frozen
flow is 3,748,078 scanned Reference records minus 120 out-of-seed source records
equals 3,747,958 admitted records. Out-of-seed rows remain upstream historical
facts; project-mappable targets need not be among the 294 seeds.

```text
SOURCE_ADMISSION_RULE = PASS
SOURCE_ADMISSION_BEFORE_MEMBERSHIP = PASS
TARGET_NEED_NOT_BE_SEED = PASS
OUT_OF_SEED_SOURCE_RECORDS = 120
METHODS_OPERATIONAL_CHAIN = PASS
```

## 7. Dedup-layer reconciliation

| Layer | Accepted status after edit |
|---|---|
| Upstream event/content materialization | GH_CoRE `dedup_content()` normalizes redundant content fields; this is not a general Reference-row deletion rule. |
| GH_CoRE extraction | Duplicate candidate matches may be suppressed during matching/cache processing; this is extraction-level control. |
| Optional helper | `deduplicate_references(rule="event_source_target")` exists but is not called by P0. |
| Current P0 retained Reference policy | `reference_dedup_rule = none`; admitted rows retain frozen multiplicity. |

```text
UPSTREAM_DUPLICATE_CONTROL_DISTINGUISHED = PASS
REFERENCE_RECORD_DEDUP_RULE = none
P0_RECORD_DEDUP_EXECUTED = NO
DEDUP_LAYER_CONTRADICTION_AFTER = NO
```

## 8. Denominator authority and mapping table

`§3.2.3` is now explicitly the primary denominator/RQ mapping authority. Its
numeric cells were not changed. The table retains the accepted values for the
294 seeds, scanned/admitted records, 1,586,047 quotient-eligible records,
6,506-node domain, 6,505 edge-observed nodes, 9,884 directed edges, 289
self-loops, 9,595 cross-project directed edges, 6,367 LCC nodes, and 9,462 LCC
undirected edges.

```text
METHODS_OPENING_ROLE = ROADMAP
METHODS_OPENING_FULL_DENOMINATOR_CHAIN = 0
PRIMARY_DENOMINATOR_AUTHORITY = §3.2.3
METHODS_MAPPING_TABLE_NUMERIC_CHANGE_COUNT = 0
METHODS_MAPPING_TABLE_NONNUMERIC_EDIT_ALLOWED = YES
METHODS_DENOMINATOR_REDUNDANCY = HIGH (before); consolidated (after)
SECTION_3_4_4_FULL_DENOMINATOR_REPETITION = 0
```

## 9. Exact RQ1 operational definitions

| Field | Exact operational definition recorded in Methods |
|---|---|
| `self_reference_ratio` | `self_reference_records / total_reference_records`; self rows have project-mappable source and target mapping to the same project. |
| `external_reference_share` | `(total_reference_records - self_reference_records) / total_reference_records`; complete non-self share equal to external-project + non-project + unresolved over total. |
| `non_project_reference_share` | `non_project_reference_records / total_reference_records`; non-project target subset, not synonymous with non-self share. |
| `active_issue_pr_count` | Unique `repo_id#issue_or_pr_number` keys parsed from admitted Reference-bearing source IDs with prefixes `I_`, `IC_`, `PR_`, `PRR_`, `PRRC_`. |
| `comment_related_unique_source_count` | Unique admitted source entity IDs with those five prefixes; includes Issue, IssueComment, PullRequest, PullRequestReview, and PullRequestReviewComment identities. |
| `comment_body_ref_count` | Admitted Reference rows whose source entity ID has one of those five prefixes. |
| `comment_per_issue` | `comment_related_unique_source_count / active_issue_pr_count`; unique source entities per Reference-bearing Issue/PR context. |
| `comment_reference_density` | `comment_body_ref_count / comment_related_unique_source_count`; Reference rows per issue/PR-related source entity. |
| `project_age_years_at_2023_end` | `(2023-12-31 UTC - frozen repo_created_at).days / 365.25`; 291 nonmissing seeds, 3 missing, no imputation, complete-case age analyses. |

```text
NON_SELF_SHARE_SEMANTICS = PASS
EXTERNAL_REFERENCE_SHARE_AS_NON_PROJECT = 0
NON_PROJECT_SHARE_SEPARATE = PASS
ACTIVE_ISSUE_PR_OPERATIONAL_DEFINITION = PASS
COMMENT_PER_ISSUE_OPERATIONAL_DEFINITION = PASS
COMMENT_REFERENCE_DENSITY_OPERATIONAL_DEFINITION = PASS
COMMENT_COUNT_DENOMINATOR_MISLABEL = 0
PROJECT_AGE_FORMULA = PASS
PROJECT_AGE_COMPLETE_CASE_POLICY = PASS
PROJECT_AGE_IMPUTATION = NO
```

## 10. Network and RQ3 closure

```text
LOUVAIN_WEIGHTED = PASS
MODULARITY_WEIGHTED = PASS
LOCAL_CLUSTERING_UNWEIGHTED = PASS
BETWEENNESS_UNWEIGHTED = PASS
BETWEENNESS_SAMPLE_SIZE = 500
NETWORK_RANDOM_SEED = 20260731
NETWORK_WEIGHT_SEMANTICS = PASS

RQ3_MIN_GROUP_SIZE = 5
RQ3_MIN_ELIGIBLE_GROUP_COUNT = 2
RQ3_FDR_FAMILY = all computed feature-level Kruskal-Wallis tests within each label mode
RQ3_LABEL_MODE_SEMANTICS = PASS
STATISTICAL_RESULT_STATUS_CHANGED = 0
```

The manuscript now states `include_mixed` (multi-label projects may be repeated
across represented categories) and `exclude_mixed_or_multilabel` (exactly one
label only). FDR is applied once across all computed feature-level tests within
each mode, not separately per feature.

## 11. RefQ construction and protected theory

The protected definitions `V_P`, `pi: V_P -> P`, unique-existence membership,
membership blocks `B_p`, row-sum-one matrix `M`, `Q = M^T R_P M`, first-order
versus second-order operators, general self-loop preservation, and
seed-centered observation boundary were not weakened or rewritten.

```text
MEMBERSHIP_CONTRACT = PASS
QUOTIENT_ELIGIBILITY_CONTRACT = PASS
ONE_ELIGIBLE_ROW_ONE_WEIGHT_UNIT = PASS
EDGE_WEIGHT_THEORY_OVERCLAIM = 0
SELF_LOOP_GENERAL_VS_VIEW_POLICY = PASS
FIRST_ORDER_REFQ = PASS
SECOND_ORDER_EXCLUSION = PASS
PROTECTED_REFQ_THEORY_CHANGED = 0
```

The new §3.4.3 clause records only the current operationalization: each retained
quotient-eligible fine-grained Reference row contributes one unit to its ordered
source-project/target-project pair. In the undirected view, `directed_edge_count`
remains the number of directed project-pair rows represented by a merged pair,
not the underlying Reference-record count.

## 12. Authorized numeric-fact ledger

The following Methods facts were added or made explicit. They are provenance or
method settings, not new scientific results; no frozen result/table value was
changed.

| Value | Added/clarified location | Authority | Scientific output changed? |
|---|---|---|---|
| 301 | §3.1.1 activity candidate gate | `seed_selection.py`, v3 config | NO |
| 10 | §3.1.1 `i_pr_rec_cnt` threshold | v3 config | NO |
| 7 | §3.1.1 unavailable-evidence exclusions | candidate audit | NO |
| 2023 | §§3.1.1-3.1.2/3.1.3 scope | v3 config and frozen event inputs | NO |
| 2024-10 | §3.1.1 annotation snapshot | provenance governance | NO |
| 3,748,078 | §3.2.3 source-admission arithmetic | observation audit | NO |
| 120 | §3.2.3 out-of-seed subtraction | observation audit | NO |
| 3,747,958 | §3.2.3 admitted total | observation audit | NO |
| 291 | §3.3.1 age complete cases | age provenance/output | NO |
| 3 | §3.3.1 age missingness | age provenance/output | NO |
| 365.25 | §3.3.1 age conversion denominator | pipeline implementation | NO |
| 5 | §3.3.3 minimum nonmissing group size | v3 config/statistics implementation | NO |
| 500 | §3.3.2 betweenness sample size | v3 config/network implementation | NO |
| 20260731 | §3.3.2 network/Louvain seed | v3 config/network implementation | NO |

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNIQUE_REPORTED_RESULT_VALUE_LOSS_COUNT = 0
AUTHORIZED_METHODS_FACT_ADDITION_COUNT = 14
```

The only globally disappearing numeric tokens were legacy `2.0` (an old license
example) and `100%` (a removed generic percentage transform). No unique Results,
table, figure, or scientific-authority value disappeared.

## 13. Cross-section terminology occurrence inventory (deferred)

The following occurrences remain outside the authorized Methods scope. They were
inventoried but not edited. Line numbers refer to the post-Methods-edit external
manuscript.

| Occurrence(s) | Current term/context | Required later classification |
|---|---|---|
| 479, 483, 604 (Figure 4 caption), 608, 612, 681 | `external-reference share` | `RENAME_TO_NON_SELF_SHARE`; caption occurrence is protected and requires a separate caption-authorized decision |
| 490, 636 | `external_reference_share` field rows | Keep field identifier, label/define as `RENAME_TO_NON_SELF_SHARE` |
| 50, 380, 383, 427, 433 | Broad `外部 Reference` evidence/orientation wording | `CORRECT_AS_IS` where it denotes broad evidence; use `RENAME_TO_NON_SELF_SHARE` where paired directly with self-reference ratio |
| 435, 437, 439, 441, 445, 447, 459, 475 | `活跃议题` / active-issue prose and table labels | `RENAME_REFERENCE_BEARING_CONTEXT_COUNT` |
| 435, 449, 451, 453, 457, 459 | `新增议评率` and its legacy formula/heading | `RENAME_SOURCE_ENTITIES_PER_CONTEXT` |
| 435, 461, 463, 465, 469, 471 | `新增评引率` and its legacy formula/heading | `RENAME_REFERENCE_ROWS_PER_SOURCE_ENTITY` |
| 434, 479, 483, 471 | `comment reference density` / 评论引用密度 | `RENAME_REFERENCE_ROWS_PER_SOURCE_ENTITY` while preserving field identifier |
| 449, 459, 471, 475 | `讨论深度` interpretation | `WEAKEN_INTERPRETATION` |
| none outside §3 | `New Comment Rate`, `New Reference Rate`, `问题复杂度`, `外部资源偏好` | No remaining literal occurrence outside Methods; verify in next pass |

```text
CROSS_SECTION_TERMINOLOGY_FOLLOWUP_REQUIRED = YES
```

No Results paragraph, table, Discussion/Conclusion prose, figure caption, or
RQ wording was changed in Batch C.

## 14. Citation closure

No literature search was performed and no citation key was added or removed.

```text
CITATION_COUNT_BEFORE = 68
CITATION_COUNT_AFTER = 68
UNIQUE_CITATION_KEY_COUNT_BEFORE = 31
UNIQUE_CITATION_KEY_COUNT_AFTER = 31
UNIQUE_CITATION_KEY_SET_CHANGED = 0
CITATION_KEY_SET_CHANGED = 0
```

## 15. Readability diagnostics

The established diagnostic excludes headings, lists, tables, fenced code, and
display math; `VERY_LONG` means more than 240 characters after sentence joining.

| Diagnostic | Before | After |
|---|---:|---:|
| Methods paragraph count | 41 | 44 |
| Methods sentence count | 86 | 89 |
| Methods very-long sentence count (>240 chars) | 5 | 3 |
| Methods maximum sentence length | 285 | 285 |

The change adds explicit operational clauses while reducing the number of very
long Methods sentences and establishing one denominator authority, one chain
overview, and one metric-definition authority.

## 16. Semantic, overclaim, and layer guards

```text
SEED_SELECTION_LAYERING = PASS
ANNOTATION_TIME_ROLE = PASS
REPOSITORY_IDENTITY_AUTHORITY = PASS
SOURCE_ADMISSION_RULE = PASS
SOURCE_ADMISSION_BEFORE_MEMBERSHIP = PASS
DEDUP_LAYER_CONTRADICTION_AFTER = NO
REFERENCE_RECORD_DEDUP_RULE = none
NON_SELF_SHARE_SEMANTICS = PASS
NON_PROJECT_SHARE_SEPARATE = PASS
ACTIVE_ISSUE_PR_OPERATIONAL_DEFINITION = PASS
COMMENT_PER_ISSUE_OPERATIONAL_DEFINITION = PASS
COMMENT_REFERENCE_DENSITY_OPERATIONAL_DEFINITION = PASS
PROJECT_AGE_COMPLETE_CASE_POLICY = PASS
RQ3_FDR_FAMILY = PASS
NETWORK_WEIGHT_SEMANTICS = PASS
MEMBERSHIP_CONTRACT = PASS
QUOTIENT_ELIGIBILITY_CONTRACT = PASS
SELF_LOOP_GENERAL_VS_VIEW_POLICY = PASS
FIRST_ORDER_REFQ = PASS
SECOND_ORDER_EXCLUSION = PASS

EXTERNAL_RESOURCE_PREFERENCE_CONSTRUCT = 0
PROBLEM_COMPLEXITY_CLAIM = 0
DISCUSSION_DEPTH_CLAIM = 0
DEPENDENCY_OVERCLAIM = 0
TASK_RESOLUTION_OVERCLAIM = 0
CAUSAL_KNOWLEDGE_FLOW_CLAIM = 0
PROJECT_IMPORTANCE_OVERCLAIM = 0
COMPLETE_ECOSYSTEM_CLAIM = 0

FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
```

## 17. Exact scope and scientific-execution guards

The external manuscript comparison showed exact byte identity outside §3 and
exact identity for protected §3.2.1, §3.4.1, and §3.4.2 regions. The §3.2.3
mapping table's numeric content is byte-identical.

```text
METHODS_CHANGED = 1
NON_METHODS_PROSE_CHANGED = 0
ABSTRACT_CHANGED = 0
INTRODUCTION_CHANGED = 0
RELATED_WORK_CHANGED = 0
RESULTS_CHANGED = 0
DISCUSSION_CHANGED = 0
THREATS_CHANGED = 0
AVAILABILITY_CHANGED = 0
CONCLUSION_CHANGED = 0
APPENDIX_CHANGED = 0
RQ_TEXT_CHANGED = 0
RESULTS_TABLE_CHANGED = 0
RESULTS_TABLE_CHANGE_COUNT = 0
FIGURE_CAPTION_CHANGED = 0
FIGURE_CAPTION_EDIT_COUNT = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0

SCIENTIFIC_RECOMPUTATION = 0
P0_RUN = 0
S1_RUN = 0
S2_RUN = 0
S3_RUN = 0
S4_RUN = 0
S5_RUN = 0
S6_RUN = 0
S7_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
SECOND_ORDER_PROJECTION_RUN = 0
FIGURE_RERENDER = 0
```

## 18. Final disposition

Batch C corrected the Methods operational definitions without touching frozen
scientific values or any non-Methods manuscript surface. A separate
cross-section terminology reconciliation remains required and is explicitly
not part of this commit.

`CH5_REFQ_SUBMISSION_EDIT_BATCH_C_METHODS_PASS`
