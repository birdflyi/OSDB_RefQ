# Chapter 5 RefQ Submission Methods Fact and Semantics Audit

## Decision

`CH5_REFQ_SUBMISSION_METHODS_FACT_SEMANTICS_AUDIT_PASS_WITH_BOUNDED_CORRECTIONS`

The frozen P0-v3 and supplemental authorities support the reported scientific
outputs. The current Methods section nevertheless contains operational-definition,
deduplication-layer, terminology, and construct-strength discrepancies. They can
be corrected by a bounded Methods edit plus coordinated Results/table terminology
follow-up. No new experiment or scientific recomputation is required.

This is an audit-only record. The authoritative manuscript, scientific outputs,
figures, tables, and RQ text were not edited.

## 1. Starting identities

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| repository HEAD before audit | `878183fc34d5011f5cc1e47e640d499c6d59431a` |
| remote HEAD before audit | `878183fc34d5011f5cc1e47e640d499c6d59431a` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Manuscript SHA-256 before audit | `2ADF5AC63C1EC696EC2EC411444FC04B5588D3BC539CECD5A7C8F01976C9B2E1` |
| Accepted corrected P0 root | `outputs/reference_quotient_p0_corrected_v3/` |
| Accepted P0-v3 config | `configs/ch5_reference_quotient_p0_v3.yaml` |
| P0-v3 config SHA-256 | `43f97f9a2d177d325415bfbcc504f1779882cf83685b4fdebe505c8fed8e7cb0` |
| P0-v3 manifest SHA-256 | `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776` |
| Accepted supplemental root | `supplemental/reference_quotient_v2/outputs_p0v3/` |
| Supplemental package manifest SHA-256 | `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd` |

The four pre-existing untracked archives
`figures/ch5_refq/p0v3_final_v3.zip` through `p0v3_final_v6.zip` were preserved.

## 2. Authority hierarchy used

1. **L0:** accepted corrected scientific result/package authorities.
2. **L1:** accepted current implementation, configuration, manifest, and audits
   that generated or support the corrected baseline.
3. **L2:** repository-identity, source-admission, annotation-provenance, and
   filtering-stability governance records.
4. **L3:** Appendix A reproducibility authority.
5. **L4:** current manuscript Methods prose.
6. **L5:** historical manuscripts and working notes.

The current result authority is the corrected v3 configuration and output chain.
The unversioned historical `configs/ch5_reference_quotient_p0.yaml` confirms shared
metric settings such as `reference_dedup_rule: none`, but it does not supersede
the corrected strict repository-identity/source-admission contract in the v3
configuration.

## 3. M01 - candidate construction and analysis-seed admission

### 3.1 Implemented state machine

```text
upstream curated DBMS/repository annotation and open-source eligibility
    -> activity materialization row has non-null repo_name
    -> numeric i_pr_rec_cnt >= 10
       = 301 P0 candidate seeds
    -> expected frozen 2023 aggregate evidence CSV exists
       = 294 analysis seeds
```

The seven excluded candidates fail only the frozen-evidence-availability gate.
The implementation does not re-run a category, diversity, or license predicate
inside `build_seed_manifests()`.

| Item | Classification | Audit conclusion |
|---|---|---|
| Curated DBMS annotation | `UPSTREAM_DBMS_CANDIDATE_CURATION` | Defines the curated DBMS/repository universe and repository metadata upstream of P0. |
| dbdb.io / DB-Engines labels | `UPSTREAM_DBMS_CANDIDATE_CURATION` | Candidate-domain background; not a predicate re-executed by current P0. |
| `open_source_license` / license selection | `OPEN_SOURCE_ELIGIBILITY` | Part of the upstream annotation/selection contract; active P0 does not consume `License_info`. |
| `i_pr_rec_cnt >= 10` | `P0_ACTIVITY_GATE` | The exact active P0 candidate gate. |
| Frozen 2023 evidence file exists | `P0_FROZEN_EVIDENCE_AVAILABILITY_GATE` | The exact 301-to-294 admission gate. |
| Category labels | `DESCRIPTIVE_SAMPLE_COVERAGE` | Used descriptively and in RQ3 grouping; not an active P0 seed-selection predicate. |
| Technical diversity | `DESCRIPTIVE_SAMPLE_COVERAGE` | A sample-description goal, not an implemented gate. |
| General observability wording | `P0_FROZEN_EVIDENCE_AVAILABILITY_GATE` | Must be stated operationally as existence of the expected frozen 2023 evidence file. |

```text
CANDIDATE_SEED_COUNT = 301
ANALYSIS_SEED_COUNT = 294
ACTIVITY_THRESHOLD = 10
ACTIVITY_FIELD = i_pr_rec_cnt
ANALYSIS_SEED_ADMISSION_RULE = repo_name is non-null AND numeric i_pr_rec_cnt >= 10 AND expected frozen 2023 evidence CSV exists
```

Methods §§3 opening, 3.1.1, 3.2.3, and 3.4.4 currently flatten upstream
curation, license eligibility, activity gating, diversity description, and
frozen-evidence admission. Batch C should separate these layers.

## 4. M02 - annotation snapshot and repository identity

The governance authority establishes:

```text
EVENT_OBSERVATION_SCOPE = 2023
ANNOTATION_SNAPSHOT = 2024-10
ANNOTATION_ROLE = POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT
PROJECT_IDENTITY_UNIT = GITHUB_NUMERIC_REPOSITORY_ID
PRIMARY_REPOSITORY_AUTHORITY = github_repo_id in the frozen curated annotation
```

The 2024-10 file is not an event-time repository snapshot and does not claim to
represent GitHub state at 2023-12-31. `repo_name`/`full_name` are descriptive and
retrieval metadata. Activity has two context-specific roles that must not be
collapsed:

- `i_pr_rec_cnt >= 10` is the explicit P0 seed-activity gate.
- Activity differences used during repository-identity review are QC/anomaly
  signals only and cannot override the curated numeric repository identity.

```text
ANNOTATION_TIME_ROLE = PASS
REPOSITORY_IDENTITY_AUTHORITY = PASS
PRIMARY_REPOSITORY_AUTHORITY = PASS
```

The current Methods does not state the 2024-10 post-scope role explicitly; this
is a bounded provenance-definition omission.

## 5. M03 - source-admission semantics

### 5.1 Implemented state machine

```text
frozen aggregate row
    -> relation_type == Reference
    -> expected_source_context_repo_id equals current seed repo ID
    -> source_admission_status is recognized
    -> event_repo_id equals current seed's frozen annotated github_repo_id
       = ADMITTED_SOURCE_OBSERVATION
    -> membership audit / profile accumulation / quotient eligibility
```

The source-admission filter executes inside
`_prepare_reference_evidence_chunk()` before membership pairs are added to the
registry and before profiles or edge weights are accumulated.

| Counter | Frozen value |
|---|---:|
| Reference records before source admission | 3,748,078 |
| Admitted source-observation records | 3,747,958 |
| Out-of-seed source records | 120 |
| Missing event repository rows | 0 |
| Invalid event repository rows | 0 |

The 120 rejected records remain in the upstream corrected aggregate. They are
excluded only from the current seed's source-observation view. Target endpoints
are not required to be among the 294 seeds: uniquely project-mappable related
repositories remain eligible expanded targets.

```text
SOURCE_ADMISSION_RULE = event_repo_id == annotated/frozen seed github_repo_id
SOURCE_ADMISSION_RULE_STATUS = PASS
SOURCE_ADMISSION_BEFORE_MEMBERSHIP = PASS
OUT_OF_SEED_SOURCE_RECORDS = 120
TARGET_POLICY_KEEP_PROJECT_MAPPABLE = PASS
```

Future Methods location: state the exact rule once in §3.1.2 or §3.2.2, then
show its denominator effect in the primary §3.2.3 authority table.

## 6. M04 - deduplication layers

| Layer | Actual operation | Enabled for current authority? | Authority | Current edge-weight effect |
|---|---|---|---|---|
| A. Upstream event/content materialization | The tracked wrapper calls GH_CoRE `dedup_content()` before relation extraction. The recoverable implementation masks redundant content fields for selected event classes; it does not establish a general event-ID row deletion rule. Corrected relation generation also preserves original relation multiplicity while adding repository-provenance fields. | YES, upstream frozen preprocessing/materialization | Source repository commit `2944ab7...`; versioned identity protocol/dependency matrix; frozen input hashes | Defines the text/event materialization presented to extraction, but is not a P0 Reference-record dedup. |
| B. GH_CoRE extraction duplicate boundary | Candidate recognition suppresses duplicate matches flagged by the extractor and caches repeated object lookups. These controls are extraction/matching controls, not proof of a general `event_id + source + target` row collapse. | PARTIAL/UPSTREAM | GH_CoRE relation wrapper and frozen materialized relation outputs | Can suppress duplicate pattern matches upstream; it does not authorize a new P0 dedup. |
| C. Optional retained-Reference helper | `deduplicate_references(rule="event_source_target")` exists, but current P0 does not call it. | NO | `script/ch5_reference_quotient/reference_filtering.py` | Zero effect on accepted P0-v3. |
| D. Current P0 retained records | Configuration validation requires `reference_dedup_rule: none`; admitted rows are counted as retained rows without a dedup call. | YES | v3 config, `config.py`, `pipeline.py`, quotient audit | Each retained quotient-eligible Reference row adds exactly one unit to its ordered project-pair weight. |

The §3.1.2 statement that Issue/PR/Commit records and repository descriptions
are removed "by event ID" is not supported by the current frozen operational
contract. The §3.2.2 optional event-level relation-dedup description is distinct
from upstream content cleanup and was not enabled for accepted P0-v3. Treating
both sentences as one active rule would be incorrect.

```text
REFERENCE_RECORD_DEDUP_RULE = none
ONE_RETAINED_REFERENCE_RECORD_ONE_WEIGHT_UNIT = PASS
DEDUP_LAYER_CONTRADICTION = YES
```

The contradiction is in the prose model of the layers, not in the frozen
scientific output.

## 7. M05 - RQ1 metric-definition matrix

| Manuscript term | Output field | Exact numerator | Exact denominator | Population | Current Methods correct? |
|---|---|---|---|---|---|
| Self-reference ratio | `self_reference_ratio` | `self_reference_records`: admitted rows whose source and target are both project-mappable and map to the same project | `total_reference_records`: all admitted Reference rows for the seed | Per-seed admitted source-observation records | YES |
| External-reference share | `external_reference_share` | `total_reference_records - self_reference_records` | `total_reference_records` | Per-seed admitted source-observation records | NO: it is the complete non-self share, not only external-resource/non-project URLs. |
| Non-project reference share | `non_project_reference_share` | `non_project_reference_records` | `total_reference_records` | Per-seed admitted source-observation records | Not explicitly and distinctly defined in §3.3.1; the implementation is verified. |
| Active Issues/PRs | `active_issue_pr_count` | Count of unique `repo_id#issue_or_pr_number` keys parsed from admitted Reference-bearing source IDs with prefixes `I_`, `IC_`, `PR_`, `PRR_`, `PRRC_` | Not applicable | Per-seed admitted Reference-bearing issue/PR-related source context | NO: not all active repository Issues/PRs, and not selected by a comment-or-code-commit predicate. |
| Comment-related unique source count | `comment_related_unique_source_count` | Count of unique admitted source entity IDs beginning with `I_`, `IC_`, `PR_`, `PRR_`, or `PRRC_` | Not applicable | Per-seed admitted Reference-bearing source entities | NO if called "comment count"; the set includes Issue, IssueComment, PR, PRReview, and PRReviewComment identities. |
| Comment-body reference count | `comment_body_ref_count` | Count of admitted Reference rows whose source entity ID begins with one of the five prefixes | Not applicable | Per-seed admitted issue/PR-related Reference rows | The output is verified, but the name is broader than comments only. |
| Comment per issue | `comment_per_issue` | `comment_related_unique_source_count` | `active_issue_pr_count` | Same admitted Reference-bearing source context | NO: legacy "New Comment Rate" is not literal comments per issue. |
| Comment reference density | `comment_reference_density` | `comment_body_ref_count` | `comment_related_unique_source_count` | Same admitted Reference-bearing source context | NO: it is Reference rows per unique issue/PR-related source entity, not references divided by comment count. |
| Project age at 2023 end | `project_age_years_at_2023_end` | `(2023-12-31 UTC - repo_created_at).days` | `365.25` | Seeds with nonmissing frozen `repo_created_at` | YES as a formula; provenance/missingness should be stated. |

### 7.1 Share identities

The exact profile partition is:

```text
total_reference_records
  = self_reference_records
  + external_project_reference_records
  + non_project_reference_records
  + unresolved_target_reference_records
```

Therefore:

```text
external_reference_share
  = (external_project + non_project + unresolved) / total
  = 1 - self_reference_ratio

non_project_reference_share
  = non_project / total
```

`external_reference_share` and `non_project_reference_share` are not synonyms.

```text
EXTERNAL_REFERENCE_SHARE_DEFINITION = VERIFIED
CURRENT_METHODS_EXTERNAL_REFERENCE_DEFINITION = INCORRECT
NON_PROJECT_REFERENCE_SHARE_DEFINITION = VERIFIED
```

### 7.2 Collaboration-feature identities

```text
ACTIVE_ISSUE_PR_COUNT_OPERATIONAL_DEFINITION = unique issue/PR keys occurring in admitted Reference-bearing source entity IDs with prefixes I_, IC_, PR_, PRR_, PRRC_
CURRENT_METHODS_ACTIVE_ISSUE_DEFINITION = INCORRECT

COMMENT_PER_ISSUE_OPERATIONAL_DEFINITION = unique admitted issue/PR-related source entity IDs / unique admitted Reference-bearing issue/PR keys
LEGACY_LABEL_NEW_COMMENT_RATE_SEMANTICALLY_EXACT = NO

COMMENT_REFERENCE_DENSITY_OPERATIONAL_DEFINITION = admitted Reference rows from issue/PR-related source entities / unique admitted issue/PR-related source entity IDs
CURRENT_METHODS_COMMENT_REFERENCE_DENSITY = INCORRECT
CROSS_SECTION_TERMINOLOGY_CORRECTION_NEEDED = YES
```

## 8. M06 - construct-strength audit for RQ1 metrics

| Current phrase | Classification | Reason |
|---|---|---|
| "外部资源偏好" | `TOO_STRONG` | The target-type distribution observes referenced objects; it does not identify a developer preference construct. |
| `active_issue_pr_count` "反映协作规模" | `AMBIGUOUS` | It measures breadth/count of admitted Reference-bearing issue/PR keys, not all collaboration activity. |
| `active_issue_pr_count` "反映问题复杂度" | `TOO_STRONG` | No complexity construct is operationalized or validated. |
| `comment_per_issue` "讨论参与密度" | `AMBIGUOUS` | The numerator mixes five issue/PR-related source entity classes and is conditioned on Reference-bearing records. |
| `comment_per_issue` "讨论深度" | `TOO_STRONG` | Entity counts per issue/PR key do not establish depth or quality. |
| `comment_reference_density` as Reference intensity in the defined source context | `SUPPORTED` after exact denominator naming | It is a count ratio, provided it is not called references per comment. |

Conservative future constructs are: observed Reference-bearing issue/PR context
breadth, unique source-entity intensity per issue/PR key, and Reference-row
density per unique issue/PR-related source entity.

## 9. M07 - historical evidence source and GitHub API role

The frozen source wrapper queries persisted `opensource.events` records for
`platform='GitHub'` and a 2023 `created_at` window. Governance identifies these
persisted historical events as OpenDigger/GHArchive-derived historical facts.
Current GitHub API calls are used for object validation, entity enrichment, gap
filling, and current-state annotation checking. They are not the sole historical
event or repository-identity authority.

The current Methods line "data come from collected GitHub collaboration logs,
with GitHub API used for supplementary validation" does not make the API the
primary source, but it should name the persisted OpenDigger/GHArchive source to
remove ambiguity.

```text
HISTORICAL_EVENT_SOURCE_ROLE = VERIFIED: persisted OpenDigger/GHArchive GitHub event records materialized through the upstream source repository
GITHUB_API_ROLE = VALIDATION_ENRICHMENT
CURRENT_API_WORDING = NEEDS_REVISION
```

## 10. M08 - GH_CoRE processing-chain classification

| Manuscript stage | Classification | Audit finding |
|---|---|---|
| Data input / time alignment | `CURRENT_IMPLEMENTED_OR_FROZEN` | The wrapper queries persisted GitHub events for the 2023 interval and the frozen P0 consumes the resulting 2023 evidence files. |
| Text normalization | `UPSTREAM_HISTORICAL_PROCESS` | Code/inline-code/quote masking and content-field redundancy handling are recoverable. The manuscript's specific SVN/debug-log examples are not established as a complete frozen contract and should not be presented as exhaustive facts. |
| Candidate-reference recognition | `UPSTREAM_HISTORICAL_PROCESS` | Regex/rule families recognize Issue/PR, SHA, file, GitHub-service, and external links. |
| Reachability/object validation | `UPSTREAM_HISTORICAL_PROCESS` | DB/API-backed object lookup and validation support entity resolution; API is validation/enrichment, not event-source authority. |
| Attribute completion/entity typing | `UPSTREAM_HISTORICAL_PROCESS` plus `CURRENT_IMPLEMENTED_OR_FROZEN` | GH_CoRE enriches fine-grained objects; the current corrected adapter/materialization preserves event repository provenance and P0 applies membership classification. |
| Duplicate-boundary handling | `OPTIONAL_NOT_ENABLED` for P0 event/source/target dedup; `UPSTREAM_HISTORICAL_PROCESS` for duplicate-match suppression | The manuscript must state which control it means. A general active event-ID relation collapse is unsupported. |
| Standardized relation output | `CURRENT_IMPLEMENTED_OR_FROZEN` | Frozen relation records retain fine-grained IDs/types, relation type/label, event identity/time, match fields, and corrected repository provenance. |
| Project-level construction preparation | `CURRENT_IMPLEMENTED_OR_FROZEN` | Corrected aggregate fields, source admission, unique membership, and quotient eligibility prepare the project-level construction. |

The seven-step overview in §3.1.3 and six-step extraction description in §3.2.2
currently overlap and assign different semantics to deduplication. Batch C should
retain one overview and one operational description with explicit layer names.

## 11. M09 - membership and quotient eligibility

The accepted construction order is:

```text
observable frozen Reference evidence
    -> strict source admission
    -> endpoint project-mappability classification
    -> globally unique membership registry
    -> exclude conflicting/unresolved/non-project endpoints from Q
    -> quotient-eligible retained records
    -> Q = M^T R_P M
```

Frozen checks:

| Contract | Result |
|---|---|
| Retained entity has exactly one project membership | PASS |
| Maximum memberships per retained entity | 1 |
| Membership conflict entities | 0 |
| Unique project-mappable entities | 1,142,161 |
| Quotient-eligible Reference records | 1,586,047 |
| Non-project targets excluded from Q but retained in RQ1 | PASS |
| General Q preserves self-loops | PASS |
| Cross-project RQ2 views exclude self-loops | PASS |

```text
MEMBERSHIP_CONTRACT = PASS
QUOTIENT_ELIGIBILITY_CONTRACT = PASS
SELF_LOOP_GENERAL_VS_VIEW_POLICY = PASS
```

The protected `V_P`, `pi`, unique-existence invariant, membership blocks,
row-sum-one condition, and seed-centered observation boundary agree with the
current implementation and must remain.

## 12. M10 - edge weight and multiplicity

Current operationalization:

```text
one retained quotient-eligible fine-grained Reference row
    -> one unit added to the ordered (source_project, target_project) pair
    -> directed edge weight is the sum of those units
```

The complete directed RefQ table has weight 1,586,047 over 9,884 ordered
project-pair rows, including 289 self-loops. The cross-project table has weight
138,974 over 9,595 directed rows.

In the undirected derived view, reciprocal directed rows are merged and their
weights are summed. `directed_edge_count`/`multiplicity` there means the number
of directed project-pair rows represented by an undirected pair (normally one
or two), not the number of underlying Reference records.

```text
EDGE_WEIGHT_OPERATIONALIZATION = VERIFIED
WEIGHT_MULTIPLICITY_THEORY_OVERCLAIM = 0
```

The row-to-unit equality is an operational property of the accepted unit-weight
implementation, not a universal theorem of quotient networks.

## 13. M11 - first-order and second-order boundary

The current theory is coherent with the accepted implementation:

- `Q = M^T R_P M` is the first-order directed RefQ block-sum.
- `QQ^T` is a shared-target second-order relation.
- `Q^T Q` is a shared-source second-order relation.
- `K = X Phi X^T` is a shared-reference projection family.
- `second_order_projection_executed = false`.

```text
FIRST_ORDER_REFQ = PASS
SECOND_ORDER_EXCLUSION = PASS
UNIVERSAL_NUMERIC_INEQUALITY_CLAIM = 0
```

The current Methods correctly says semantic/operator identity is distinct even
if matrices could coincide in a degenerate numeric case. No weakening of this
protected theory is recommended.

## 14. M12 - denominator authority

The full scanned/admitted/eligible/node/edge/LCC chain is repeated in the §3
opening, §3.1.1, §3.2.3, and §3.4.4. All repetitions are currently numerically
consistent, but maintaining four full authorities is high-risk because record,
entity, node, edge, and weight units can drift independently.

```text
METHODS_DENOMINATOR_REDUNDANCY = HIGH
RECOMMENDED_PRIMARY_DENOMINATOR_AUTHORITY = §3.2.3
```

Recommended future allocation:

- §3 opening: short roadmap without the full numeric chain.
- §3.1: sample and input construction, including 301-to-294 admission.
- §3.2.3: the single compact denominator/RQ mapping authority.
- §3.4.4: observation and graph-view semantics, with only locally necessary
  unit clauses.

## 15. M13 - project-age provenance

`project_age_years_at_2023_end` is computed as:

```text
(Timestamp("2023-12-31", UTC) - parsed frozen repo_created_at).days / 365.25
```

The accepted v3 config sets `repo_created_at_refresh: false`. The frozen
annotation derivative, activity materialization, and seed manifest agree for
all 294 seed rows. There are 291 nonmissing timestamps and three explicit
missing values (`greenplum-db/gpdb`, `xap/xap`, and `EuclidOLAP/EuclidOLAP`).
No imputation is performed; downstream age analyses use complete cases.

```text
PROJECT_AGE_DEFINITION = VERIFIED
PROJECT_AGE_MISSINGNESS_POLICY = VERIFIED
```

The historical origin of every timestamp is not reconstructed from original
API responses, but the frozen multi-artifact consistency and explicit
missingness are sufficient for the current accepted analysis.

## 16. M14 - RQ3 statistics

For each label mode, the implementation expands/filters labels first, then for
each feature retains only category groups with at least five nonmissing values.
A Kruskal-Wallis test is computed only when at least two eligible groups remain.
Epsilon-squared is:

```text
max(0, (H - k + 1) / (n - k))
```

BH-FDR is applied once across all computed feature-level Kruskal p-values within
that label mode. In the accepted output there are 11 tested features in each
mode.

`include_mixed` splits the category field and duplicates a multi-label project
into every represented category. `exclude_mixed_or_multilabel` retains only
projects with exactly one category label.

```text
RQ3_MIN_GROUP_SIZE = 5
RQ3_FDR_FAMILY_DEFINITION = all computed feature-level Kruskal-Wallis tests within each label mode
RQ3_LABEL_MODE_SEMANTICS = PASS
```

Current §3.3.3 states within-mode FDR and the two label modes correctly, but
omits the minimum group size and does not name the exact computed-test family.

## 17. M15 - approximate betweenness and Louvain

| Setting | Frozen operational value | Future placement |
|---|---|---|
| Graph/view | LCC of the first-order undirected `U(G_RefQ)` view | Methods |
| Louvain | `nx.community.louvain_communities(lcc, weight="weight", seed=20260731)` | Methods |
| Modularity | Weighted by `weight` | Methods |
| Local clustering | Unweighted (`weight=None`) | Methods |
| Approximate betweenness | `nx.betweenness_centrality(lcc, k=500, normalized=True, seed=20260731, weight=None)` | Methods |
| Random seed | `20260731` | Methods and Appendix reproducibility identity |
| Brokerage sample size | `500` | Methods |
| NetworkX | `3.1` | Appendix/reproducibility metadata; optional concise Methods note |
| Sampling-sensitivity outcomes | Supplemental S5/frozen Results authority | Results/supplement, not the base method definition |

Current Methods mentions the fixed sample and seed, but should state that
betweenness and clustering are unweighted while Louvain/modularity use edge
weight.

## 18. M16 - Methods claim-strength results

Positive overclaim search found no assertion that RefQ is dependency ground
truth, task resolution, causal knowledge transfer, project importance, or a
complete GitHub/OSS ecosystem. The explicit negative boundary statements in
§§3.4.1, 3.4.3, and 3.4.4 are correct and protected.

The bounded construct-strength problems are the three RQ1 labels discussed in
M06: external-resource "preference", problem "complexity", and discussion
"depth". They are interpretation/terminology problems, not evidence that the
frozen numerical outputs are invalid.

```text
DEPENDENCY_OVERCLAIM = 0
TASK_OVERCLAIM = 0
CAUSAL_OVERCLAIM = 0
COMPLETE_ECOSYSTEM_CLAIM = 0
```

## 19. M17 - Methods versus implementation/provenance conflicts

| Methods claim | Current manuscript | Current implementation/provenance | Conflict? | Required future treatment |
|---|---|---|---|---|
| Seed activity threshold | 2023 has at least 10 Issue/PR records | Numeric `i_pr_rec_cnt >= 10` after non-null `repo_name` | PARTIAL | Name the exact field; do not substitute a prose event definition unless its materialization contract is established. |
| 301-to-294 admission | Final 294 after broad criteria | 301 activity candidates; 294 after frozen evidence-file availability | YES/OMISSION | Separate upstream eligibility, P0 activity gate, and evidence availability gate. |
| 2024-10 annotation role | Not stated | Post-scope curated repository-mapping snapshot | YES/OMISSION | State event scope versus annotation verification time. |
| Source admission | Named with counts but rule omitted | `event_repo_id == frozen annotated seed github_repo_id`, before membership | YES/OMISSION | State exact rule and target-expansion distinction. |
| Event/reference dedup | Event-ID deletion plus optional relation dedup narrative | Upstream content/match controls are distinct; current P0 Reference dedup is `none` | YES | Replace with a three-layer description; do not imply enabled event/source/target collapse. |
| `external_reference_share` | External-resource share | Complete non-self admitted Reference share | YES | Correct formula and semantics; coordinate Results/RQ terminology. |
| `non_project_reference_share` | Not separately operationalized in metric list | `non_project_reference_records / total_reference_records` | YES/OMISSION | Define separately from non-self share. |
| `active_issue_pr_count` | Active Issues/PRs with comment or commit | Unique issue/PR keys among admitted Reference-bearing source IDs | YES | Replace operational definition and weaken construct label. |
| `comment_per_issue` | Comments / active issues | Unique five-prefix source IDs / unique issue/PR keys | YES | Replace formula/label; coordinate table and Results terminology. |
| `comment_reference_density` | References / comments | Five-prefix admitted Reference rows / unique five-prefix source IDs | YES | Replace denominator/label; coordinate table and Results terminology. |
| Project age | Age at 2023 end | Day difference / 365.25; 291 complete cases; no imputation | PARTIAL | Add frozen field provenance and missingness. |
| Edge weight | Multiplicity/block sum | One eligible Reference row contributes one unit to ordered pair weight | NO, precision needed | State unit-weight operationalization and distinguish undirected `directed_edge_count`. |
| Self-loop | General Q preserves; cross-project view may remove | Exactly matches config/audit | NO | Preserve. |
| RQ3 minimum group size | Omitted | Five nonmissing observations per category/feature | YES/OMISSION | Add threshold and at-least-two-groups condition. |
| RQ3 FDR family | Within each label mode | All computed feature-level Kruskal tests within each mode | PARTIAL | Name exact family. |
| Network settings | Fixed `k=500` and seed | Unweighted normalized betweenness; unweighted clustering; weighted Louvain/modularity | PARTIAL | State weight semantics; keep NetworkX 3.1 in reproducibility metadata. |

## 20. Scientific-impact classification

| Discrepancy | Classification | Scientific impact |
|---|---|---|
| Flattened seed-selection criteria | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | No sample change; clarify how the accepted 294 were admitted. |
| Annotation time/identity omission | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | No identity change; clarify frozen mapping authority. |
| Source-admission rule omission | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | No record change; document the accepted 120-row exclusion rule. |
| Dedup-layer conflict | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | No dedup or rerun; correct the description of existing frozen layers. |
| External/non-project share conflation | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION`, `TYPE_C_CROSS_SECTION_TERMINOLOGY_CORRECTION`, `TYPE_D_REPORTED_RESULT_INTERPRETATION_IMPACT` | Numbers remain valid; Methods, Results, RQ synthesis, and labels must describe non-self versus non-project correctly. |
| Active issue/comment metrics | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION`, `TYPE_C_CROSS_SECTION_TERMINOLOGY_CORRECTION`, `TYPE_D_REPORTED_RESULT_INTERPRETATION_IMPACT` | Frozen fields remain valid; legacy labels and depth/complexity interpretations require coordinated correction. |
| Project-age provenance/missingness | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | Accepted complete-case results remain valid. |
| RQ3 threshold/FDR-family omissions | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | Frozen tests remain valid; report the executed family. |
| Network weight-setting omissions | `TYPE_B_OPERATIONAL_DEFINITION_CORRECTION` | Frozen graph metrics remain valid; state weighted/unweighted settings. |
| Denominator repetition | `TYPE_A_LANGUAGE_ONLY` | Consolidation reduces future drift risk. |
| Preference/complexity/depth wording | `TYPE_A_LANGUAGE_ONLY`, `TYPE_D_REPORTED_RESULT_INTERPRETATION_IMPACT` | Weaken constructs; do not change values. |

No discrepancy reaches `TYPE_E_SCIENTIFIC_RECOMPUTATION_REQUIRED`.

```text
NEW_EXPERIMENT_NEEDED = NO
SCIENTIFIC_RECOMPUTATION_NEEDED = NO
RESULTS_TEXT_FOLLOWUP_NEEDED = YES
TABLE_LABEL_FOLLOWUP_NEEDED = YES
```

## 21. Recommended bounded edit surfaces

### 21.1 Methods Batch C surfaces

1. §3 opening: retain a short roadmap; remove the full repeated denominator
   chain.
2. §3.1.1: distinguish upstream DBMS/open-source curation, the exact
   `i_pr_rec_cnt` gate, and frozen-evidence availability.
3. §3.1.2: name persisted OpenDigger/GHArchive historical events, keep GitHub API
   as validation/enrichment, and replace the unsupported event-ID dedup claim.
4. §3.1.3/§3.2.2: separate chain overview from operational extraction and label
   upstream duplicate-match control versus disabled P0 dedup.
5. §3.2.3: make this the primary denominator/RQ mapping authority and state the
   source-admission rule.
6. §3.3.1: replace all RQ1 formulas and construct labels with the exact profile
   field definitions.
7. §3.3.2: specify unweighted clustering/betweenness and weighted Louvain.
8. §3.3.3: add minimum group size five, the at-least-two-groups condition, and
   the exact within-mode BH-FDR family.
9. §3.4: preserve the complete protected quotient theory; add only the exact
   unit-weight operational clause where needed.

### 21.2 Cross-section follow-up surfaces

After Methods Batch C, a separate authorized pass must align:

- §4.1.2 headings and prose for active issue/PR count, `comment_per_issue`, and
  `comment_reference_density`;
- Tables 4.3-4.5 labels;
- statements in §4.1.3, RQ3, Discussion §5.4, and Conclusion that use
  `external_reference_share` as though it meant non-project/external-resource
  share;
- any caption or table label that literalizes the legacy "new comment/new
  reference" terms.

Scientific values, table cells, p-values, effect sizes, and graph metrics are
not authorized to change in that terminology follow-up.

## 22. Protected theory and construction diagram

```text
persisted 2023 OpenDigger/GHArchive GitHub events
    -> upstream GH_CoRE text/pattern/object processing
    -> frozen fine-grained Reference relations
    -> corrected repository-provenance adapter/materialization
    -> relation_type == Reference
    -> strict source admission
    -> unique endpoint membership (V_P, pi, M row-sum = 1)
    -> quotient-eligible record set
    -> Q = M^T R_P M, one eligible row = one weight unit
    -> general directed Q preserves self-loops
    -> RQ2 cross-project view removes self-loops
    -> U(G_RefQ) ignores direction and merges reciprocal directed rows
    -> weighted Louvain / unweighted clustering and approximate betweenness on LCC
```

No recommendation weakens or removes `V_P`, `pi`, the unique-existence
invariant, membership blocks, `M` row-sum, `Q=M^T R_P M`, the first/second-order
distinction, the self-loop general/view distinction, or the seed-centered
observation boundary.

## 23. No-edit and scientific-execution guards

```text
MANUSCRIPT_CHANGED = 0
METHODS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
TABLES_CHANGED = 0
RQ_TEXT_CHANGED = 0

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

## 24. Final disposition

The current Methods is not submission-final because it does not consistently
describe the exact operational definitions that generated the accepted
results. The discrepancies are bounded and repairable without changing the
sample, evidence, graph, statistics, figures, or reported numeric values.

`CH5_REFQ_SUBMISSION_METHODS_FACT_SEMANTICS_AUDIT_PASS_WITH_BOUNDED_CORRECTIONS`
