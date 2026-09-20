# Chapter 5 RefQ MS-R02 Candidate Final Editorial QA Rerun

## Decision

`CH5_REFQ_MS_R02_CANDIDATE_FINAL_QA_RERUN_PASS_READY_FOR_PROMOTION`

The post-F-01b MS-R02 working candidate passes the independent final editorial
QA rerun. All eight previously blocking workflow/governance-language regions
are closed, no new reviewer-facing workflow leak or scientific conflict was
introduced, and the previously closed A-E dimensions remain closed. This
record does not promote MS-R02 or modify any manuscript, accepted-authority,
figure, table, or scientific asset.

## 1. Repository and manuscript identity

| Item | Result |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before QA rerun | `42f0f805737e764dfc6f399e1bb464374da66d83` |
| Remote HEAD before QA rerun | `42f0f805737e764dfc6f399e1bb464374da66d83` |
| Accepted source revision | `MS-R01` |
| CURRENT SHA-256 | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| MS-R01 snapshot SHA-256 | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| CURRENT equals MS-R01 snapshot | `YES` |
| Candidate | `working/MS-R02_CANDIDATE.md` |
| Candidate SHA before QA rerun | `B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC` |
| Sidecar SHA-256 | `F6E76D4D9C496148B3FB78C897AC4A72A9467E8B8A404F188932FC8CBB3E0688` |
| Manuscript version manifest SHA-256 | `1CAEE8CF8D8A27451A76C9529BF449D4DB5107677C6A69BECF6ECCAA39B5B8D7` |

The four pre-existing untracked V3-V6 ZIP files remained untouched. The
candidate remains a working candidate; MS-R01 remains the accepted revision.

## 2. Candidate SHA and exact patch-scope closure

The current candidate SHA matches the required post-patch identity. Reversing
only the authorized F-01b substitutions in memory reconstructed the exact
pre-patch SHA:

```text
CANDIDATE_SHA_BEFORE = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
CANDIDATE_SHA_AFTER = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
F01B_PRE_PATCH_SHA_RECONSTRUCTED = 0E9CB83BC8D057EC982B1CAD2112259FD8912828AFB876949A08A0FD05EB3671
AUTHORIZED_F01B_PATCHES = 8
PATCHES_CLOSED = 8
UNAUTHORIZED_CHANGED_REGION_COUNT = 0
```

The eight resulting regions were independently inspected in the current file:

| Patch | Location | Verified publication-facing result | Status |
|---:|---|---|---|
| 1 | Section 3.1.1 | `既有 DBMS/repository annotation`; `实际样本纳入标准` | PASS |
| 2 | Section 3.1.1 | `2023 年证据可用性标准`; corresponding 2023 aggregate evidence CSV availability; 301 -> 294 and seven exclusions preserved | PASS |
| 3 | Section 3.2.2 | `event_repo_id` must equal the corresponding seed annotation's `github_repo_id`; admission still precedes membership/profile/edge aggregation | PASS |
| 4 | Section 3.3.3 | `在本文采用的 unit-weight 实现中`; one retained eligible row still contributes one weight unit | PASS |
| 5 | Section 4.2a | `seed-source quantiles 显示`; all out-degree/out-strength quantiles preserved | PASS |
| 6 | Section 4.3 | `include_mixed 口径下的 10 个 category rows` | PASS |
| 7 | Section 4.3.2 | higher precision is retained in the analysis-results file corresponding to Table 4.8 | PASS |
| 8 | Section 4.3.3 | higher precision is retained in the corresponding analysis-results file | PASS |

The numeric-token multiset comparison against the reconstructed pre-patch
candidate found only one additional occurrence of the already-established
contextual year `2023` in the authorized Patch 2 heading (`22 -> 23`
occurrences). No new value, result, denominator, or scientific claim was
introduced.

## 3. Blocked-literal closure

The main text before Appendix A contains zero occurrences of all eight blocked
literals:

```text
"实际 admission gate" = 0
"冻结证据可用性门槛" = 0
"冻结 aggregate evidence CSV" = 0
"frozen annotated seed github_repo_id" = 0
"在本文冻结实现中" = 0
"冻结 quantile authority" = 0
"当前 include_mixed 冻结输出" = 0
"冻结来源文件" = 0

BLOCKED_LITERAL_REMAINING_COUNT = 0
```

## 4. Full workflow-language rescan

The Abstract and Sections 1-9 were reread sequentially, and occurrences of
stage IDs, PASS/release terms, audit/authority/gate language, frozen/snapshot,
current-analysis, configuration/guard/workflow/manifest/package/provenance,
and write-back language were inspected in context.

| Classification | Main-text treatment |
|---|---|
| `NECESSARY_REPRODUCIBILITY_LANGUAGE` | Fixed project-activity statistics, the fixed 2023 event/evidence snapshot, posterior repository annotation date, exact retained field names, project-age source field, fixed display counts, and reproducibility/provenance statements |
| `NATURAL_RESEARCH_PROSE` | Package dependency as an explicitly excluded semantics; current-sample descriptions; observation, mapping, and evidence-boundary prose; data/code availability limitations |
| `INTERNAL_WORKFLOW_LEAK` | None |

Remaining uses of `冻结`, `frozen`, `snapshot`, or `provenance` identify a
fixed observation object, immutable raw field, display basis, or reproducible
data boundary. They do not instruct the reader about repository approval,
freeze gates, or internal acceptance workflow.

```text
INTERNAL_WORKFLOW_LEAK_COUNT = 0
NEW_WORKFLOW_LEAK_COUNT = 0
```

## 5. F-dimension final read-through

The complete main text was assessed for grammar, sentence architecture,
punctuation, mixed-language burden, technical-term density, paragraph and
transition coherence, specification/audit tone, nominalization, and reviewer
parsing cost.

The eight patches integrate grammatically into their paragraphs. The defined
English technical terms remain dense in places but are necessary to preserve
the paper's exact constructs and are introduced before reuse. Long sentences
retain identifiable subjects and claims. The revised Methods passages read as
research-method prose; Results, Discussion, validity, availability, and
Conclusion retain publication-facing interpretation rather than internal
workflow instructions. No grammatical defect, new ambiguity, unsupported
claim, or specification/audit-tone residue rises to E0 or E1.

```text
F_LANGUAGE_STYLE_AND_NOTATION = PASS
```

## 6. A-E regression closure

| Dimension | Regression result |
|---|---|
| A: problem-method-result-conclusion | Problem, method, empirical result, and bounded conclusion remain closed; RQ hierarchy and four-contribution logic are unchanged | PASS |
| B: terminology and experimental semantics | External/non-self/non-project, seed/expanded-target, RefQ/RefQN, and rank eta-squared meanings remain separated and consistent | PASS |
| C: rhetorical architecture | Heading hierarchy, Methods order, Results order, and all inspected internal references remain valid | PASS |
| D: figure/table/evidence architecture | Figures 1-4, Tables 4.1-4.8 including 4.6a-4.6f, lead-ins, interpretations, and claim/evidence roles remain intact | PASS |
| E: literature and citation verification | 69 citation tokens, 32 unique keys, and 32 bibliography entries close with no missing, orphan, or malformed citation | PASS |

```text
A_PROBLEM_METHOD_RESULT_CONCLUSION = PASS
B_TERMINOLOGY_AND_EXPERIMENTAL_SEMANTICS = PASS
C_RHETORICAL_ARCHITECTURE = PASS
D_FIGURE_TABLE_EVIDENCE_ARCHITECTURE = PASS
E_LITERATURE_AND_CITATION_VERIFICATION = PASS
F_LANGUAGE_STYLE_AND_NOTATION = PASS
```

## 7. RQ, contribution, and Methods architecture closure

The five RQ statements are byte-for-byte identical to MS-R01. Their hierarchy
remains RQ1 as evidence/boundary support, RQ2a/RQ2b/RQ2c as the structural
empirical center, and RQ3 as a bounded label-mode-sensitive comparison.

The four contributions retain their order and semantic roles: relation
construction/formalization; evidence and observation boundary; role-separated
empirical characterization; and a traceable weaker-semantic relation asset.

The Methods order remains:

```text
3.1 sample/data
3.2 extraction/admission/mapping
3.3 RefQ/RefQN construction
3.4 metrics/statistics

RQ_COUNT = 5
RQ_TEXT_CHANGED = 0
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0
CONTRIBUTION_SEMANTIC_ROLE_CHANGED = 0
BROKEN_INTERNAL_SECTION_REFERENCE_COUNT = 0
HEADING_HIERARCHY_ERROR_COUNT = 0
```

## 8. E-01 and corrected Figure 4 closure

The candidate uses `rank eta-squared` / `\eta_H^2` for
`(H-k+1)/(n-k)` with the implementation clamp
`max(0, (H - k + 1) / (n - k))`. No `epsilon-squared` label remains.
Kruskal and Wallis (1952) supports the test; Tomczak and Tomczak (2014)
supports the effect-size estimator/naming.

```text
WRONG_EFFECT_SIZE_LABEL_COUNT = 0
EFFECT_SIZE_VALUE_CHANGE_COUNT = 0
FIGURE4_DATA_CHANGED = 0
FIGURE4_PANEL_STRUCTURE_CHANGED = 0
FIGURE4_SCALE_CHANGED = 0
FIGURE4_GEOMETRY_CHANGED = 0
FIGURE4_SEMANTIC_LABEL_CHANGED = 1
FIGURE_RERENDER = 0
```

The semantic-label value is relative to historical V6 and records the already
accepted E-01 terminology correction; it is not a change made in this QA.

| Corrected Figure 4 asset | SHA-256 |
|---|---|
| `figures/ch5_refq/p0v3_final_v6_e01_eta_label/main/figure4_rq3_comparison/figure4_rq3_comparison.svg` | `6EC08F8462BB13F46395678A5BFB1B5E753377399D5CFA612F85FD273B34E17A` |
| `figures/ch5_refq/p0v3_final_v6_e01_eta_label/main/figure4_rq3_comparison/figure4_rq3_comparison.pdf` | `DAF4F9C486B19F229D0D13586CFCEABA774BF7212466D7174877C57F07307C0C` |
| `figures/ch5_refq/p0v3_final_v6_e01_eta_label/main/figure4_rq3_comparison/figure4_rq3_comparison.png` | `6A279AE45570C06E745DB65D3B14503B30F2AD98DAAC5C64DD8611A082FC44EA` |

## 9. Citation closure

```text
CITATION_TOKEN_COUNT = 69
UNIQUE_CITATION_KEY_COUNT = 32
BIBLIOGRAPHY_ENTRY_COUNT = 32
MISSING_CITATION_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
```

The dedicated effect-size source remains present. GitHub Docs remain scoped to
platform syntax/mechanics rather than empirical false-positive/false-negative
evidence.

## 10. Display and evidence closure

The candidate contains Figures 1-4 and Tables 4.1-4.8, including Tables
4.6a-4.6f. The Table 4.6c continuation remains part of Table 4.6c. Figure and
table units continue to distinguish records, entities, directed and undirected
edges, and aggregated weight.

```text
FIGURE_CAPTION_COUNT = 4
MISSING_REQUIRED_DISPLAY_COUNT = 0
ORPHAN_DISPLAY_COUNT = 0
DISPLAY_WITHOUT_LEAD_IN_COUNT = 0
DISPLAY_WITHOUT_INTERPRETATION_COUNT = 0
UNSUPPORTED_MATERIAL_CLAIM_COUNT = 0
```

## 11. Scientific-value and semantic guards

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0

RQ_TEXT_CHANGED = 0
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0

Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_SECOND_ORDER_BOUNDARY_CHANGED = 0

STATISTICAL_TEST_CHANGED = 0
EFFECT_SIZE_VALUE_CHANGE_COUNT = 0
FDR_FAMILY_CHANGED = 0
LABEL_MODE_CHANGED = 0
CROSS_MODE_RESULT_CHANGED = 0
SCIENTIFIC_CONFLICT_COUNT = 0
```

## 12. Scientific execution and asset guards

```text
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
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
```

## 13. No-edit and accepted-authority guards

```text
CANDIDATE_SHA_BEFORE = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
CANDIDATE_SHA_AFTER = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
CANDIDATE_CHANGED = 0

CURRENT_CHANGED = 0
MS_R01_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_ACCEPTED_REVISION_CREATED = 0
```

No `versions/MS-R02_*` accepted snapshot was created. CURRENT and its sidecar
still identify MS-R01. Promotion is explicitly outside this transaction.

## 14. Severity and editorial-completion gate

The six informational observations retained by this rerun are nonblocking:
the candidate remains a working revision; promotion is a separate transaction;
the four pre-existing ZIP files remain untracked; the repeated `2023` token is
contextual rather than a new result; remaining fixed-snapshot terminology is
necessary reproducibility language; and the Figure 4 semantic-label delta is
the already accepted E-01 correction. They require no manuscript edit.

```text
E0_COUNT = 0
E1_COUNT = 0
E2_COUNT = 0
INFO_COUNT = 6
SCIENTIFIC_CONFLICT_COUNT = 0

EDITORIAL_COMPLETE = YES
READY_FOR_PROMOTION = YES
```

## 15. Promotion recommendation and Git scope

MS-R02 is eligible for a separately authorized promotion transaction. This QA
does not execute that promotion.

```text
AUDIT_PATH = docs/freeze/ch5_refq_ms_r02_candidate_final_editorial_qa_rerun.md
COMMIT_SCOPE = this audit document only
READY_FOR_PROMOTION = YES
PROMOTION_EXECUTED = NO
```

Final decision:

`CH5_REFQ_MS_R02_CANDIDATE_FINAL_QA_RERUN_PASS_READY_FOR_PROMOTION`
