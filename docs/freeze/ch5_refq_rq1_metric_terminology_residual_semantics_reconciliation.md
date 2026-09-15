# Chapter 5 RefQ RQ1 Metric Terminology and Residual Semantics Reconciliation

## Decision

`CH5_REFQ_RQ1_METRIC_TERMINOLOGY_RESIDUAL_SEMANTICS_RECONCILIATION_PASS`

This is a bounded manuscript wording reconciliation. The external authoritative
manuscript was edited only in three authorized Results/semantic locations during
this pass. The R01-R03 Methods/Threats corrections were already present from
Batch C and were reverified here, not re-edited. No scientific pipeline, output,
manifest, receipt, figure asset, or table value was changed.

## 1. Starting identities and baseline drift

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before | `909bf6faaa0b0e7a78421e28ee93d6342f47ec5e` |
| Remote HEAD before | `909bf6faaa0b0e7a78421e28ee93d6342f47ec5e` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Task-stated expected SHA before | `BEB6E89127032EA93843AB2385573EE1306C087A06B182753A24AB9E74ED1761` |
| Observed practical SHA before | `0E39E2FF8D80DCD72E883F5A9141F4F003D5A3C2C6F2A28E46D2B0809D23F125` |
| SHA after authorized wording edits | `07F0C28A9F6A10679C2AFB3FC16836CE19FD65CCF9498ED35066F2A175C07255` |
| Primary authorities | `docs/freeze/ch5_refq_submission_methods_fact_semantics_audit.md`; `docs/freeze/ch5_refq_submission_edit_batch_c_methods.md` |

The task-stated `BEB6...` hash was not the byte state observed at the start of
this pass. The audit therefore records the actual observed `0E39...` hash as the
before baseline and does not claim that the expected baseline was reconstructed.
The manuscript has mixed newline encoding (`CRLF=832`, `LF=29`); no global
newline normalization was performed.

## 2. Governing metric definitions

| Field | Manuscript semantic contract |
|---|---|
| `external_reference_share` | Non-self Reference Share: `(total_reference_records - self_reference_records) / total_reference_records`, equivalently external-project + non-project + unresolved over total. It is not a non-project-only or external-URL-only share. |
| `non_project_reference_share` | Non-project target subset: `non_project_reference_records / total_reference_records`; distinct from complete non-self share. |
| `active_issue_pr_count` | Unique `repo_id#issue_or_pr_number` keys from admitted Reference-bearing source IDs with prefixes `I_`, `IC_`, `PR_`, `PRR_`, `PRRC_`. It is not all active repository Issues/PRs. |
| `comment_per_issue` | `comment_related_unique_source_count / active_issue_pr_count`; unique source entities per observed Reference-bearing Issue/PR context, not comment count or discussion depth. |
| `comment_reference_density` | `comment_body_ref_count / comment_related_unique_source_count`; Reference records per issue/PR-related source entity, not references per comment. |

## 3. Residual factual closure

The following Batch-C residual corrections were present before this pass and
were reverified without modification:

| ID | Surface | Before | After | Closure |
|---|---|---|---|---|
| R01 | §3.2.3 seed mapping row | Broad domain/activity/2023-log admission wording | Upstream DBMS/open-source curation, `repo_name` non-null, `i_pr_rec_cnt >= 10` activity candidate gate, and expected frozen 2023 evidence availability | `METHODS_MAPPING_SEED_ROW_LAYERED_ADMISSION = PASS` |
| R02 | §3.4.4 analysis-seed terminology | Wording implied the projects were obtained by actually crawling GitHub collaboration logs | Layered §3.1.1 admission plus 294 projects with frozen 2023 Reference evidence | `ANALYSIS_SEED_DEFINITION_LAYERED = PASS`; `LEGACY_ACTUAL_CRAWL_WORDING = 0` |
| R03 | §6.2 dedup wording | Event-level dedup-boundary wording | Upstream content/candidate-match duplicate controls distinguished from the P0 Reference-record multiplicity contract | `THREATS_EVENT_LEVEL_DEDUP_IMPLICATION = 0`; `P0_REFERENCE_DEDUP_NONE_SEMANTICS = PASS` |

The three actual wording edits made in this pass were:

| Pass edit | Exact before fragment | Exact after fragment | Scope |
|---|---|---|---|
| §4.1.2 source-entity intensity | `讨论深度的项目间分化` and a statement that the metric supplemented discussion depth | The metric is explicitly bounded to observed Reference-bearing contexts and does not infer problem complexity, collaboration quality, or problem-resolution effects | Authorized Results prose only |
| §4.1.2 Reference-row density | `评论级 Reference density` and a statement that the metric supplemented `讨论深度` | The metric is explicitly stated to be Reference-record density and not a measure of discussion process or quality | Authorized Results prose only |
| §4.3.2 before Table 4.8 | No local sentence mapped the frozen field names to their manuscript semantics | `external_reference_share` is mapped to non-self Reference share and `comment_reference_density` to Reference rows per issue/PR-related source entity; field identifiers remain unchanged | Authorized Table 4.8 explanatory context only |

## 4. RQ1 terminology reconciliation matrix

| ID | Location | Legacy wording/semantic risk | Correct operational semantic | Treatment |
|---|---|---|---|---|
| T01 | §4.1.2 | Active Issues/PRs or generic collaboration scale | Reference-bearing Issue/PR context breadth | Kept/verified bounded wording |
| T02 | Table 4.3 | Active-issue label | Count of unique Reference-bearing Issue/PR contexts | Label verified; numeric cells unchanged |
| T03 | §4.1.2 | Comment-rate or discussion interpretation | Unique source-entity intensity per observed context | Definition and interpretation verified |
| T04 | Table 4.4 | New Comment Rate / discussion-depth reading | Unique source entities per Reference-bearing Issue/PR context | Label verified; numeric cells unchanged |
| T05 | §4.1.2 | References-per-comment reading | Reference-row density per issue/PR-related source entity | Definition and interpretation verified |
| T06 | Table 4.5 | New Reference Rate / comment-only denominator | Reference records per issue/PR-related source entity | Label verified; numeric cells unchanged |
| T07 | §4.1.2 synthesis | Collaboration scale/depth/density as constructs | Context breadth, source-entity intensity, and Reference-row density as distinct descriptive metrics | Construct-accurate synthesis verified |
| T08 | §4.1.3 and Table 4.6a | `external-reference share` ambiguity | Non-self Reference share (`external_reference_share`); field identifiers retained | Semantic gloss verified; identifiers unchanged |
| T09 | Figure 4 caption | Field-name semantic ambiguity | Non-self Reference share and Reference-row density per issue/PR-related source entity | Authorized caption semantic correction verified; no rerender |
| T10 | §4.3.1 | External-reference share as non-project share | Non-self Reference share | Prose verified |
| T11 | Table 4.7 | External-reference column label | Non-self Reference share median | Label verified; percentages unchanged |
| T12 | §4.3.2/Table 4.8 | Frozen field identifiers could be read as prose semantics | `external_reference_share` = non-self share; `comment_reference_density` = Reference rows per related source entity | Mapping sentence verified; identifiers unchanged |
| T13 | §5.4 | Discussion-level or external-resource interpretation | Non-self Reference share as observable evidence proportion | Discussion wording verified |

## 5. Occurrence and protected-identifier checks

The current manuscript contains zero occurrences of the following legacy
manuscript-facing metric terms: `external-reference share`, `新增议评率`,
`新增评引率`, `活跃议题`, `事件级去重边界控制`, and `实际爬取`.
The current manuscript also contains zero Results occurrences of `讨论深度`.
One explicit English `discussion depth` occurrence remains in the frozen §3.3.1
Methods definition as a negative semantic guard; it was intentionally not edited
because §3.3.1 is outside this pass's newly authorized edit surface.

The following implementation identifiers remain present and unchanged:

```text
active_issue_pr_count
comment_per_issue
comment_reference_density
external_reference_share
non_project_reference_share
```

`external_reference_share` and `comment_reference_density` remain as raw output
field identifiers in Table 4.6a and Table 4.8. This is required for
reproducibility and is not a semantic-label regression.

## 6. Table, caption, and scientific closure

```text
TABLE_4_3_NUMERIC_CHANGE_COUNT = 0
TABLE_4_4_NUMERIC_CHANGE_COUNT = 0
TABLE_4_5_NUMERIC_CHANGE_COUNT = 0
TABLE_4_6A_FIELD_IDENTIFIERS_CHANGED = 0
TABLE_4_7_NUMERIC_CHANGE_COUNT = 0
TABLE_4_8_FIELD_IDENTIFIER_CHANGE_COUNT = 0
TABLE_NUMERIC_CHANGE_COUNT = 0
AUTHORIZED_TABLE_LABEL_CHANGE_COUNT > 0
UNAUTHORIZED_TABLE_CHANGE_COUNT = 0
FIGURE_4_CAPTION_CHANGED = 1
OTHER_FIGURE_CAPTION_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNIQUE_SCIENTIFIC_VALUE_LOSS_COUNT = 0
STATISTICAL_STATUS_CHANGE_COUNT = 0
```

Protected values include all Table 4.3–4.8 numeric cells, p-values, effect
sizes, RQ3 FDR statuses, and the existing figure metrics. No numeric scientific
value was added, removed, or recomputed.

## 7. Semantic, interpretation, and layer guards

```text
NON_SELF_SHARE_SEMANTICS = PASS
NON_PROJECT_SHARE_SEPARATE = PASS
ACTIVE_ISSUE_PR_OPERATIONAL_DEFINITION = PASS
COMMENT_PER_ISSUE_OPERATIONAL_DEFINITION = PASS
COMMENT_REFERENCE_DENSITY_OPERATIONAL_DEFINITION = PASS
RESULTS_RQ1_CONTEXT_POPULATION = PASS
PROBLEM_COMPLEXITY_CLAIM = 0
DISCUSSION_DEPTH_CLAIM = 0
DISCUSSION_QUALITY_CLAIM = 0
GENERIC_COLLABORATION_SCALE_CLAIM = 0
EXTERNAL_REFERENCE_SHARE_AS_NON_PROJECT = 0
NON_SELF_AND_NON_PROJECT_CONFLATION = 0
DEPENDENCY_OVERCLAIM = 0
TASK_RESOLUTION_OVERCLAIM = 0
CAUSAL_OVERCLAIM = 0
FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
GLOBAL_EXTERNAL_REFERENCE_REPLACEMENT = 0
```

The zero-valued `DISCUSSION_DEPTH_CLAIM` refers to manuscript claims, not the
single §3.3.1 negative definition that explicitly rejects that interpretation.

## 8. Exact scope and execution guards

```text
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
ABSTRACT_CHANGED = 0
INTRODUCTION_CHANGED = 0
RELATED_WORK_CHANGED = 0
CONCLUSION_CHANGED = 0
AVAILABILITY_CHANGED = 0
APPENDIX_CHANGED = 0
RQ_TEXT_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0

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

The repository worktree contained no tracked scientific or figure changes. The
four pre-existing untracked V3/V4/V5/V6 ZIP archives were preserved and not
staged.

## 9. Authority and reproducibility anchors

The audit relied on the accepted Methods authorities and read-only frozen output
anchors. Representative P0-v3 hashes observed during QA were:

```text
outputs/reference_quotient_p0_corrected_v3/manifest.json
SHA256 = BE802B9DF223C99BC2089A76AE9EC6E0B6047AB0C58237A5FC3050B51DCC9776

supplemental/reference_quotient_v2/outputs_p0v3/
file_count = 58
```

No output or manifest was rewritten. The current manuscript remains external to
the repository; this file records its hashes rather than treating it as
Git-tracked.

## 10. Final disposition

All authorized residual and cross-section terminology checks close without a
scientific change. The remaining §3.3.1 negative `discussion depth` phrase is a
protected Methods guard and is explicitly classified as out of scope, not as an
unresolved Results defect.

`CH5_REFQ_RQ1_METRIC_TERMINOLOGY_RESIDUAL_SEMANTICS_RECONCILIATION_PASS`
