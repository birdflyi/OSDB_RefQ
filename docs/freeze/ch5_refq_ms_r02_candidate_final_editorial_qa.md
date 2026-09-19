# Chapter 5 RefQ MS-R02 Candidate Final Editorial QA

## Decision

`CH5_REFQ_MS_R02_CANDIDATE_FINAL_QA_PASS_WITH_BLOCKING_EDIT_LIST`

The MS-R02 candidate is scientifically and structurally coherent, but it is
not editorially complete under the stronger reviewer-facing standard. Eight
main-text phrases still read as repository freeze, authority, or admission
gate language. They are listed below as a bounded edit list. No manuscript,
accepted snapshot, sidecar, manifest, figure, table, or scientific output was
modified in this QA.

Promotion is therefore not authorized by this record.

## 1. Identity Closure

| Item | Result |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before QA | `5723c252cb173103bcd8aeb20d997bf13c65104b` |
| Remote HEAD before QA | `5723c252cb173103bcd8aeb20d997bf13c65104b` |
| Accepted source revision | `MS-R01` |
| CURRENT SHA-256 | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| MS-R01 snapshot SHA-256 | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| CURRENT equals MS-R01 snapshot | `YES` |
| Candidate | `working/MS-R02_CANDIDATE.md` |
| Candidate SHA before QA | `0E9CB83BC8D057EC982B1CAD2112259FD8912828AFB876949A08A0FD05EB3671` |
| Candidate state | `WORKING_CANDIDATE`; accepted revision remains `MS-R01` |
| Pre-existing untracked files | `p0v3_final_v3.zip`, `p0v3_final_v4.zip`, `p0v3_final_v5.zip`, `p0v3_final_v6.zip` |

The four ZIP files were not inspected as scientific inputs, modified, or
staged. The required repository identity matched the task authority before
the QA document was written.

## 2. Adjacent MS-R01 -> Candidate Diff

The comparison was made directly between:

* `versions/MS-R01_POST_G1_CF488538.md`
* `working/MS-R02_CANDIDATE.md`

The adjacent diff contains:

```text
CHANGED_HUNK_COUNT = 39
CHANGED_OLD_LINE_COUNT = 97
CHANGED_NEW_LINE_COUNT = 101
```

All changed regions map to the authorized canonical issue set. The Methods
reordering is treated as movement of the existing construction block, not as
scientific deletion or invention.

```text
UNMAPPED_CHANGED_REGION_COUNT = 0
UNAUTHORIZED_CHANGED_REGION_COUNT = 0
```

| Candidate region | Canonical issue(s) |
|---|---|
| Abstract result and contribution paragraphs | A-01, B-01, F-03 |
| Section 1.4 contribution paragraphs | A-01, B-01, B-02 |
| Section 3 introduction and block order | B-01, C-03 |
| Sections 3.1.1-3.1.3 | C-01, F-01 |
| Sections 3.2.2-3.2.3 | F-01 |
| Section 3.4.1 controlled terminology | B-02 |
| Sections 3.4.2-3.4.3 | E-01, F-05 |
| Section 4 opening | C-02 |
| Section 4.2 scale, Figure 2 order, and caption | C-04, D-01, F-03 |
| Section 4.2c prose and Figure 3 caption | F-02, F-03, F-05 |
| Section 4.3, Figure 4, Table 4.8, and statistical prose | D-02, E-01, F-02, F-03, F-05 |
| Sections 5.2 and 5.4 | B-01, F-04 |
| Section 6.2 | E-02 |
| Section 6.4 | E-01 |
| Section 9 | A-02, B-01, F-04, F-05 |
| Appendix A range and notation normalization | F-05 |
| Bibliography and versioned Figure 4 terminology | E-01 |

## 3. Independent Revalidation of the 17 Issues

The candidate was inspected directly rather than accepting the previous
candidate audit labels.

| Issue | Independent result |
|---|---|
| A-01 | PASS: contributions lead with concrete construction, boundary, empirical, and relation-asset outputs while retaining the four-part order. |
| A-02 | PASS: Section 9 gives an evidence-led empirical synthesis before limitations and future work. |
| B-01 | PASS: recurring noun stacks are reduced after first definition; remaining technical English is tied to defined constructs. |
| B-02 | PASS: external, non-self, non-project, project-mappable, and expanded-target meanings are separated in Section 3.4.1 and aligned prose. |
| C-01 | PASS: `3.1.3` is a level-4 sibling of `3.1.1` and `3.1.2`. |
| C-02 | PASS: the Results opening separates RQ1, RQ2a/b/c, and RQ3 roles. |
| C-03 | PASS: Methods order is sample/data -> extraction/admission/mapping -> RefQ/RefQN construction -> metrics/statistics. |
| C-04 | PASS: the former `4.2.0` heading is removed and its scale material is retained in Section 4.2. |
| D-01 | PASS: Figure 2 follows scale and denominator context and has a lead-in and interpretation. |
| D-02 | PASS: Figure 4 caption now describes panel encoding while body/Table 4.8 carry inferential interpretation. |
| E-01 | PASS: the formula is identified as rank eta-squared, with a separate Tomczak source and unchanged values. |
| E-02 | PASS: GitHub Docs are limited to platform syntax/mechanics; extraction error is stated as this study's limitation. |
| F-01 | PASS_WITH_EDITS: most Methods workflow voice was removed, but eight reviewer-facing freeze/authority phrases remain; see Section 10. |
| F-02 | PASS: publication precision is used in running prose while exact values remain recoverable from tables and frozen sources. |
| F-03 | PASS: Abstract and Figure 2-4 descriptions are shorter and less repetitive. |
| F-04 | PASS: repeated negative guards are consolidated without removing a scientific boundary. |
| F-05 | PASS: ARI/HHI/FDR notation, range punctuation, and statistical display formatting are normalized. |

## 4. A-F Closure

```text
A_PROBLEM_METHOD_RESULT_CONCLUSION = PASS
B_TERMINOLOGY_AND_EXPERIMENTAL_SEMANTICS = PASS
C_RHETORICAL_ARCHITECTURE = PASS
D_FIGURE_TABLE_EVIDENCE_ARCHITECTURE = PASS
E_LITERATURE_AND_CITATION_VERIFICATION = PASS
F_LANGUAGE_STYLE_AND_NOTATION = PASS_WITH_EDITS
```

The candidate is readable as a research paper in all six dimensions, but the
F dimension cannot be closed as `PASS` while the residual workflow phrases
remain in the main text.

## 5. Scientific-Value Preservation

The candidate was compared with MS-R01 for the frozen constructs, equations,
RQ text, and reported values. The following guards pass:

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0

RQ_TEXT_CHANGED = 0
RQ_COUNT_CHANGED = 0
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0

Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_SECOND_ORDER_BOUNDARY_CHANGED = 0

STATISTICAL_TEST_CHANGED = 0
FDR_FAMILY_CHANGED = 0
LABEL_MODE_CHANGED = 0
CROSS_MODE_RESULT_CHANGED = 0
SCIENTIFIC_CONFLICT_COUNT = 0
```

The five RQs remain byte-for-byte identical to MS-R01. Their hierarchy remains
RQ1 as evidence/boundary support, RQ2a/RQ2b/RQ2c as the structural empirical
center, and RQ3 as a bounded label-mode-sensitive comparison. The four
contributions retain their order and semantic roles.

Presentation-only transforms are limited to rounded display values, including
the modularity and ARI values in Section 4.2c and the statistical values in
Sections 4.3.2-4.3.3. The corresponding exact values remain present in the
tables or frozen source outputs.

## 6. Methods and Internal References

The final Methods sequence is:

```text
3.1 sample/data
3.2 extraction/admission/mapping
3.3 RefQ/RefQN construction
3.4 metrics/statistical analysis
```

The section headings are hierarchical, and the inspected `§3.1.1`, `§3.2.3`,
`§3.3.3`, `§4.1`, `§4.2a`, and `§4.2b` references resolve to existing
sections.

```text
BROKEN_INTERNAL_SECTION_REFERENCE_COUNT = 0
HEADING_HIERARCHY_ERROR_COUNT = 0
```

The unit-weight cross-reference now points to `§3.3.3`; the first-order versus
second-order boundary remains explicit.

## 7. E-01 and Figure 4 Closure

The candidate consistently uses rank eta-squared / `eta_H^2` for:

* the estimator `(H-k+1)/(n-k)` with implementation `max(0, ...)`;
* the Methods definition;
* the Figure 4 caption;
* Table 4.8;
* Sections 4.3 and 6.4; and
* the bibliography/source attribution.

`Kruskal & Wallis (1952)` is used for the Kruskal-Wallis test. `Tomczak &
Tomczak (2014)` is used for the effect-size estimator/naming. The candidate
contains no remaining epsilon-squared label.

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

Corrected Figure 4 root:
`figures/ch5_refq/p0v3_final_v6_e01_eta_label/`

| Asset | SHA-256 |
|---|---|
| `main/figure4_rq3_comparison/figure4_rq3_comparison.svg` | `6EC08F8462BB13F46395678A5BFB1B5E753377399D5CFA612F85FD273B34E17A` |
| `main/figure4_rq3_comparison/figure4_rq3_comparison.pdf` | `DAF4F9C486B19F229D0D13586CFCEABA774BF7212466D7174877C57F07307C0C` |
| `main/figure4_rq3_comparison/figure4_rq3_comparison.png` | `6A279AE45570C06E745DB65D3B14503B30F2AD98DAAC5C64DD8611A082FC44EA` |

The corrected render differs from historical V6 only in the Figure 4 effect
size label. Historical V6 assets remain present and were not overwritten.

## 8. Citation Closure

```text
CITATION_TOKEN_COUNT = 69
UNIQUE_CITATION_KEY_COUNT = 32
BIBLIOGRAPHY_ENTRY_COUNT = 32
MISSING_CITATION_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
```

The Tomczak entry is present and is assigned the estimator/naming role. GitHub
Docs are not used as empirical false-positive/false-negative evidence.

## 9. Display and Evidence Closure

The candidate contains four semantic figure captions and all required tables:
Figures 1-4; Tables 4.1-4.5, 4.6a-4.6f, 4.7, and 4.8. The Table 4.6c
continuation is retained as part of that display, not counted as a new table.

Figure 2 follows the Project-level RefQN scale and denominator context. Figure
4 separates panel encoding from the inferential explanation in the body and
Table 4.8. Figure/table units distinguish records, entities, directed edges,
undirected edges, and aggregated weight.

```text
FIGURE_CAPTION_COUNT = 4
MISSING_REQUIRED_DISPLAY_COUNT = 0
ORPHAN_DISPLAY_COUNT = 0
DISPLAY_WITHOUT_LEAD_IN_COUNT = 0
DISPLAY_WITHOUT_INTERPRETATION_COUNT = 0
UNSUPPORTED_MATERIAL_CLAIM_COUNT = 0
```

## 10. Residual Internal-Workflow-Language Audit

The independent scan covered the main text before Appendix A. Established
reproducibility terms such as event snapshots, repository identity, runtime
settings, and provenance were not automatically treated as defects. The
following eight distinct phrases were judged to be reviewer-facing internal
workflow/governance language that can be replaced without losing scientific
precision:

| Location | Current phrase or construction | Classification | Smallest future edit |
|---|---|---|---|
| §3.1.1, line 115 | `冻结的 DBMS/repository annotation` and `实际 admission gate` | E1 INTERNAL_WORKFLOW_LEAK | Describe the project annotation and the study's inclusion criterion directly; remove `admission gate`. |
| §3.1.1, line 117 | `冻结证据可用性门槛` and `冻结 aggregate evidence CSV` | E1 INTERNAL_WORKFLOW_LEAK | State the 2023 evidence-file availability criterion without presenting it as a repository freeze gate. |
| §3.2.2, line 161 | `frozen annotated seed github_repo_id` | E1 INTERNAL_WORKFLOW_LEAK | Say `the annotated seed repository ID` in the main text; retain the exact field identity in Appendix A. |
| §3.3.3, line 265 | `在本文冻结实现中` | E1 INTERNAL_WORKFLOW_LEAK | Replace with `在本文采用的 unit-weight 实现中`. |
| §4.2a, line 522 | `冻结 quantile authority` | E1 INTERNAL_WORKFLOW_LEAK | Replace with `the seed-source quantiles` or `the reported seed-source quantiles`. |
| §4.3, line 627 | `当前 include_mixed 冻结输出` | E1 INTERNAL_WORKFLOW_LEAK | Replace with `the complete include_mixed output`. |
| §4.3.2, line 651 | `表 4.8 的冻结来源文件` | E1 INTERNAL_WORKFLOW_LEAK | Refer to the exact values in Table 4.8 or its associated data source without `frozen source`. |
| §4.3.3, line 655 | `完整精度保留于冻结来源文件` | E1 INTERNAL_WORKFLOW_LEAK | Use the same publication-facing reference to Table 4.8/source data. |

Other occurrences of snapshot, runtime, provenance, package, or field-name
language were classified as necessary reproducibility language or natural
research prose because they define the observation window, preserve exact
field semantics, or explain data/code availability. They do not add to the
eight blocking occurrences above.

```text
INTERNAL_WORKFLOW_LANGUAGE_OCCURRENCE_COUNT = 8
INTERNAL_WORKFLOW_LEAK_COUNT = 8
```

## 11. Mixed-Language, Paragraph, and Readability Review

The Abstract and Sections 1-9 were read sequentially. Technical English is
dense in several sentences, but the central constructs are defined before
reuse and established terms such as Reference, RefQ, RefQN, Louvain, FDR,
HHI, and ARI are appropriate. The candidate has no new grammatical defect,
abrupt rhetorical jump, duplicate display role, or unsupported positive
claim that rises to E0.

The only blocking readability issue is the workflow-language set in Section
10. Remaining long sentences and mixed-language noun phrases are optional
polish after that bounded edit list, not separate blockers.

## 12. Severity Ledger

```text
E0_COUNT = 0
E1_COUNT = 8
E2_COUNT = 0
INFO_COUNT = 6
SCIENTIFIC_CONFLICT_COUNT = 0
EDITORIAL_COMPLETE = NO
```

The eight E1 items are all presentation-only and have unambiguous minimal
replacements. They do not block the scientific baseline, but they do block
the stronger `EDITORIAL_COMPLETE = YES` status.

## 13. No-Edit Guards

```text
CANDIDATE_SHA_BEFORE = 0E9CB83BC8D057EC982B1CAD2112259FD8912828AFB876949A08A0FD05EB3671
CANDIDATE_SHA_AFTER = 0E9CB83BC8D057EC982B1CAD2112259FD8912828AFB876949A08A0FD05EB3671
CANDIDATE_CHANGED = 0

CURRENT_CHANGED = 0
MS_R01_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_ACCEPTED_REVISION_CREATED = 0
```

The accepted CURRENT, MS-R01 snapshot, manuscript sidecar, and manuscript
version manifest were not edited. The candidate remains a working candidate;
no `versions/MS-R02_*` file was created and CURRENT was not replaced.

## 14. Scientific Execution Guards

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

## 15. Recommendation

```text
READY_FOR_PROMOTION = NO
```

Before promotion, apply only the eight wording substitutions in Section 10,
then repeat the candidate SHA, scope, citation, display, and scientific guard
cycle. Do not reopen the scientific baseline, Figure 4 composition, or the
MS-R01 authority.

## 16. Audit / Git

```text
AUDIT_PATH = docs/freeze/ch5_refq_ms_r02_candidate_final_editorial_qa.md
COMMIT_SCOPE = audit document only
```

This document is the only file authorized for the QA commit. The repository
HEAD and push result are filled in after the documentation-only commit and
remote verification.

Final decision before promotion remains:

`CH5_REFQ_MS_R02_CANDIDATE_FINAL_QA_PASS_WITH_BLOCKING_EDIT_LIST`
