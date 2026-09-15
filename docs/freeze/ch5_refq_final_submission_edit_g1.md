# Chapter 5 RefQ — Final Submission Bounded Edit G1

## Decision

`CH5_REFQ_FINAL_SUBMISSION_EDIT_G1_PASS`

G1 completed only the bounded publication-language edits authorized by the G0
issue table and the G1 task.  The authoritative manuscript is external to Git;
only this immutable audit record is committed to the repository.

## 1. Starting identities

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before | `2ea5507d3c4e4b14fb4a50e602a835e88de160b1` |
| Remote HEAD before | `2ea5507d3c4e4b14fb4a50e602a835e88de160b1` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Manuscript SHA-256 before | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` |
| Manuscript SHA-256 after | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Bytes before / after | 117,132 / 114,716 |
| Line count before / after | 861 / 861 |

Both identities matched the task before editing.  The four pre-existing
untracked V3–V6 ZIP archives were preserved and excluded from the commit.

## 2. G0 metadata notes

- `G0_METADATA_NOTE_1`: the phrase “10 category rows in the RQ2c category
  table” is interpreted as “10 category rows in RQ3 / Table 4.7.”  G1 does not
  change Table 4.7.
- `G0_METADATA_NOTE_2`: Methods/process-overview overlap remains P2-04.  G1 did
  not upgrade it to P1 or edit the unauthorized §3.1.2/§3.1.3 processing
  overview.

The historical G0 audit was not amended.

## 3. Exact changed-region ledger

The pre-edit text was reconstructed in memory from the following replacements;
its byte SHA-256 exactly reproduced the expected starting SHA
`8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18`.
Exactly 22 manuscript lines/paragraphs differ: 4, 6, 8, 10, 12, 45, 48, 115,
116, 119, 159, 161, 163, 548, 629, 677, 705, 729, 737, 739, 741, and 743.
Every region is mapped below; all other lines are byte-identical.

| Region | Location | Authority | Exact before fragment | Exact after fragment |
|---|---|---|---|---|
| G1-01 | Abstract ¶1 (line 4) | P1-01 / P2-A | `开源数据库管理系统（DBMS）生态具有长期维护... additional observable evidence` | `开源 DBMS 生态具有复杂的跨项目语境... 这些显式 Reference evidence 补充了包依赖和代码调用之外的项目关联` |
| G1-02 | Abstract ¶2 (line 6) | P1-01 / P2-A | `本文从可观测的细粒度 Reference evidence universe 出发... 本文将所得高层关系构念定义为 paper-specific...` | `本文将 observable fine-grained Reference evidence universe 与 quotient-eligible、project-mappable 子域分开... 所得构念定义为 paper-specific...` |
| G1-03 | Abstract ¶3 (line 8) | P1-01 / local split | full scale inventory through `6,505`, `289`, `9,547`, `6,367`, `9,462` | retained `294`, `3,748,078`, `3,747,958`, `1,586,047`, `6,506`, `9,884`, `9,595`; secondary scale list replaced by `无向派生视图用于结构分析` |
| G1-04 | Abstract ¶4 (line 10) | P1-01 / P2-A | `descriptive differences... 整体结果表现为 local and label-mode sensitive` | `在两种 label mode 下均无 FDR-supported group difference... 整体结果局部且 label-mode sensitive` |
| G1-05 | Abstract ¶5 (line 12) | P1-01 / local split | `本文的贡献包括：第一...第四...` | `本文贡献包括四点：第一...第四...` with the same four-part order and weaker-semantic boundary |
| G1-06 | §1.3 final paragraph (line 45) | P1-02 | long construction → DBMS instantiation → goal → interface explanation | concise DBMS empirical setting, explicit Project-level RefQN goal, and future-interface boundary |
| G1-07 | §1.4 opening (line 48) | P1-02 | repeated 294-seed/construction/RQ-roadmap paragraph | `围绕上述关系资产，本文提出以下研究问题：` |
| G1-08 | §3.1.1 item 1 (line 115) | P1-03 / P2-A | `当前 P0 不重新执行...` | `当前分析不重新执行...` |
| G1-09 | §3.1.1 item 2 (line 116) | P1-03 | `P0 活动候选门槛` | `活动候选门槛`; field `i_pr_rec_cnt >= 10` and 301 count unchanged |
| G1-10 | §3.1.1 snapshot paragraph (line 119) | P1-03 | `2024-10，属于 POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT... 实际 P0 gate` | `2024 年 10 月的后验整理 repository-mapping 标注快照... 实际活动候选门槛` |
| G1-11 | §3.2.2 opening (line 159) | P1-04 | `不等价于 P0 对保留 Reference rows 的 record-level deduplication` | `不等价于当前分析对保留 Reference rows 的 record-level deduplication` |
| G1-12 | §3.2.2 admission (line 161) | P1-04 | `当前 P0 首先保留 relation_type == Reference` | `当前分析首先保留 relation_type == Reference`; admission predicate and ordering unchanged |
| G1-13 | §3.2.2 multiplicity (line 163) | P1-04 | `P0 配置固定为 reference_dedup_rule = none... P0 不再应用...` | `当前分析不再对通过 source admission 的 Reference records 额外执行 record-level deduplication（配置项 reference_dedup_rule = none）...` |
| G1-14 | §4.2b paragraph 2 (line 548) | P1-05 | `这些 share 的分母是 138,974 的 cross-project weight；top-1 的 3,430/138,974...` | `上述 target-weight shares 均以 cross-project RefQ total weight 138,974 为分母；其中 3,430/138,974...` |
| G1-15 | §4.3.2 pre-Table 4.8 paragraph (line 629) | P1-06 | enumerated six include_mixed supported features | `include_mixed 下若干...通过 FDR...完整 feature-level results 见表 4.8。因此，不存在 cross-mode robust feature...` |
| G1-16 | §5.3 paragraph 1 (line 677) | P2-B | `candidate-level 的 screen、identify candidates、prioritize inspection 和 support follow-up analysis` | `仅处于候选层面，用于候选筛选、结构位置识别、人工复核优先级安排和后续分析支持` |
| G1-17 | §6.2 paragraph 2 (line 705) | P1-07 | `P0 Reference-record multiplicity 口径核查` | `当前分析的 Reference-record multiplicity 口径核查` |
| G1-18 | §7 paragraph 3 (line 729) | P1-07 | repeated full-code/public-release/final-package explanation | retained conditional code scope and final-package reconciliation once, with `现有 relation/data release 及其 DOI 不自动意味着上述完整代码已经公开` |
| G1-19 | §9 paragraph 1 (line 737) | P1-08 / local split | starts `本文构建并形式化了...` and places novelty boundary before construction | starts with the two-universe/contract construction; novelty boundary follows as a second sentence |
| G1-20 | §9 paragraph 2 (line 739) | P1-08 | `在这一关系资产上... 不支持把所有指标或所有子领域...` | `基于这一关系资产... 不支持把所有指标或子领域...` |
| G1-21 | §9 paragraph 3 (line 741) | P1-08 | enumerates five possible citation meanings | concise `不判定具体引用的任务语义`; all dependency/task/causality negative guards remain |
| G1-22 | §9 paragraph 4 (line 743) | P1-08 | extended limitation/future-work inventory | concise limitation and future-work paragraph retaining `QQ^T`, `Q^TQ`, and `K=XΦX^T` as future-only relations |

The ledger uses line identities from the stable 861-line manuscript.  No line
insertions/deletions occurred, which made a complete line-wise comparison
possible.

```text
UNMAPPED_CHANGED_REGION_COUNT = 0
UNAUTHORIZED_CHANGED_REGION_COUNT = 0
WHOLE_MANUSCRIPT_FREE_REWRITE = 0
P2_EXPANSION_BEYOND_LOCAL_P1_SURFACE = 0
```

## 4. Abstract compression and numeric deletion ledger

The Abstract was reduced from 2,779 to 2,426 characters under the same
line-preserving extraction, a reduction of 353 characters or 12.70%.  It still
contains all seven required functions: problem/gap; RefQ construction; 294-seed
setting; key scale evidence; RQ2 structure; RQ3 label-mode sensitivity; and the
four-part contribution plus weak-semantic boundary.

The minimum numeric anchors remain in the Abstract: 294, 3,748,078,
3,747,958, and 1,586,047.  The representative network anchors 6,506, 9,884,
and 9,595 also remain.

| Value removed only from Abstract | Remaining manuscript authority | Scientific meaning changed? |
|---:|---|---|
| 6,505 | §3.2.3, §4.2.0, Table 4.6b | No |
| 289 | §3.2.3, §4.2.0, Table 4.6b, Appendix A | No |
| 9,547 | §4.2.0, Table 4.6b, §4.2c, Table 4.6e, Figure 3 caption | No |
| 6,367 | §3.2.3, Table 4.6b, §4.2c, Table 4.6e, Figure 3 caption | No |
| 9,462 | §3.2.3, Table 4.6b, §4.2c, Table 4.6e, Figure 3 caption | No |

```text
ABSTRACT_NEW_SCIENTIFIC_VALUE_COUNT = 0
ABSTRACT_CHANGED_SCIENTIFIC_VALUE_COUNT = 0
ABSTRACT_REMOVED_UNIQUE_SCIENTIFIC_VALUE_COUNT = 0
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNIQUE_SCIENTIFIC_VALUE_LOSS_COUNT = 0
STATISTICAL_STATUS_CHANGE_COUNT = 0
```

## 5. P1 and selected-P2 closure

| Gate | Result | Evidence |
|---|---|---|
| `P1_01_ABSTRACT` | `PASS` | 12.70% bounded compression; seven functions preserved |
| `P1_02_INTRO` | `PASS` | §1.3 ends with paper goal; §1.4 enters the unchanged RQ list directly |
| `P1_03_METHODS_INTERNAL_LABEL` | `PASS` | §3.1.1 publication labels removed; snapshot time/role and numeric-ID authority unchanged |
| `P1_04_DEDUP_PUBLICATION_PROSE` | `PASS` | upstream duplicate control remains distinct from current-analysis record-level deduplication |
| `P1_05_RQ2B_DENOMINATOR` | `PASS` | denominator is explicitly cross-project RefQ total weight 138,974 |
| `P1_06_RESULTS_REDUNDANCY` | `PASS` | only §4.3.2 pre-table paragraph shortened; no broad Results compression |
| `P1_07_VALIDITY_AVAILABILITY` | `PASS` | one §6.2 label and one §7 paragraph edited; all release facts preserved |
| `P1_08_CONCLUSION` | `PASS` | §9 reduced 9.38%; structure-first contribution, RQ hierarchy, weak semantics, and future-only projection boundary remain |
| `P2_B_PRACTICAL_USE_VERBS` | `PASS` | only §5.3 candidate-level phrase translated |
| `P2_A_LOCAL_MIXED_LANGUAGE` | `PASS` | limited to already edited P1 paragraphs |
| `LOCAL_SENTENCE_SPLIT` | `PASS` | limited to Abstract and Conclusion authorized surfaces |

No §5.4 text was changed.  No optional broad P2-01/P2-04 rewrite was executed.

## 6. Internal-label before/after inventory

Counts below distinguish affected main-text lines from literal occurrences;
Appendix A is excluded from publication-language cleanup.

| Literal | Main-text before | Main-text after | Appendix status |
|---|---:|---:|---|
| `P0` | 9 lines / 11 literals | 2 lines / 3 literals | frozen (`P0-v3` provenance retained) |
| `P0-v3` | 0 | 0 | 7 literals retained |
| `POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT` | 1 | 0 | not present |
| `reference_dedup_rule` | 1 | 1 | exact field retained in main Methods as required |
| `S4` | 0 | 0 | retained |
| `S5` | 0 | 0 | retained |
| `S7` | 0 | 0 | retained |
| `robustness_alert` | 0 | 0 | retained |
| `RELEASE_READY` | 0 | 0 | retained |

The remaining main-text `P0` occurrences are confined to §3.1.2 and §3.1.3,
which G1 explicitly forbade editing.  They preserve the upstream-versus-current
analysis distinction and are therefore unavoidable within this task's scope.

```text
MAIN_TEXT_POST_SCOPE_INTERNAL_LABEL_COUNT = 0
ANNOTATION_TIME_ROLE_CHANGED = 0
REFERENCE_DEDUP_RULE_SEMANTICS_CHANGED = 0
UPSTREAM_VS_RECORD_DEDUP_DISTINCTION = PASS
```

## 7. Citation, RQ, contribution, and theory closure

```text
CITATION_TOKEN_COUNT_BEFORE = 68
CITATION_TOKEN_COUNT_AFTER = 68
UNIQUE_CITATION_KEY_COUNT_BEFORE = 31
UNIQUE_CITATION_KEY_COUNT_AFTER = 31
BIBLIOGRAPHY_ENTRY_COUNT_BEFORE = 31
BIBLIOGRAPHY_ENTRY_COUNT_AFTER = 31
CITATION_KEY_SET_CHANGED = 0
MISSING_BIBLIOGRAPHY_KEYS = 0
ORPHAN_BIBLIOGRAPHY_KEYS = 0

RQ_TEXT_CHANGED = 0
RQ_COUNT_CHANGED = 0
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0
CONTRIBUTION_HIERARCHY_CHANGED = 0

Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_ORDER_SECOND_ORDER_BOUNDARY_CHANGED = 0
SECTION_5_4_ROLE_CHANGED = 0
CONCLUSION_STRUCTURE_FIRST = PASS
SECOND_ORDER_REMAINS_FUTURE_ONLY = PASS
```

Repeated numeric anchors remain internally present, including 301, 294, the
activity gate 10, 3,748,078, 120, 3,747,958, 1,586,047, 6,506, 6,505, 9,884,
289, 9,595, 138,974, 9,547, 6,367, 9,462, 291, 35, 32--37, 42/50, both frozen
ARI minima, 500, and 20260731.  No new calculation was performed.

## 8. Figure, table, Appendix, availability, and layer guards

The exact 22-line diff excludes every table row, caption, equation, explicit RQ
item, reference entry, and Appendix A line.  Figure captions remain four; the
explicit RQ list remains five items; the four ordered contribution paragraphs
remain unchanged.

```text
TABLE_CONTENT_CHANGED = 0
TABLE_LABEL_CHANGED = 0
TABLE_NUMERIC_CHANGE_COUNT = 0
FIGURE_CAPTION_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
RQ2B_NUMERIC_CHANGE_COUNT = 0
RQ2B_DENOMINATOR_SEMANTICS = PASS
RESULTS_BROAD_COMPRESSION = 0
STATISTICAL_STATUS_CHANGED = 0
APPENDIX_CHANGED = 0
APPENDIX_PROVENANCE_IDENTIFIER_CHANGE_COUNT = 0
AVAILABILITY_FACT_CHANGE_COUNT = 0
PUBLIC_RELEASE_PROMISE_ADDED = 0
DOI_CHANGED = 0
FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
```

Appendix A's post-heading byte hash remains
`CC63D59F1250318DAF5040251D571CE35C74131A06EA0F1FC312EA04137CA1DB`.
Its `P0-v3`, `S4`, `S5`, `S7`, `PASS`, `RELEASE_READY`, and
`robustness_alert` provenance identifiers are unchanged.

## 9. Encoding and readability closure

```text
UTF8_AFTER = PASS
CRLF_BEFORE = 0
CRLF_AFTER = 0
LF_BEFORE = 861
LF_AFTER = 861
CR_ONLY_BEFORE = 0
CR_ONLY_AFTER = 0
BOM_BEFORE = False
BOM_AFTER = False
FINAL_LF_BEFORE = True
FINAL_LF_AFTER = True
```

Under the G0 diagnostic heuristic, the Abstract changed from 18 to 15
sentences, retained two very-long sentences, and reduced its maximum sentence
length from approximately 754 to 730 characters.  The main-text
very-long-sentence count changed from 55 to 54; this limited change is expected
because G1 was not a whole-manuscript sentence-length sweep.  The Conclusion
remains nine sentences, with one very-long sentence; its maximum fell from
approximately 351 to 274 characters.

```text
ABSTRACT_COMPRESSION_PERCENT = 12.70
MAIN_TEXT_VERY_LONG_SENTENCE_BEFORE = 55
MAIN_TEXT_VERY_LONG_SENTENCE_AFTER = 54
```

## 10. Scientific execution and overclaim guards

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
```

No positive power-law, scale-free, heavy-tail, dependency-ground-truth,
task-resolution, causal-knowledge-flow, project-importance,
collaboration-quality, problem-complexity, stable-semantic-community,
complete-GitHub-ecosystem, or longitudinal-evolution claim was added.  Existing
negative guards remain.

## 11. Final status

```text
repository_HEAD_before = 2ea5507d3c4e4b14fb4a50e602a835e88de160b1
manuscript_SHA_before = 8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18
manuscript_SHA_after = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
P1_CLOSURE = PASS
SCIENTIFIC_CLOSURE = PASS
SCOPE_CLOSURE = PASS
ENCODING_CLOSURE = PASS
```

The exact final decision is:

`CH5_REFQ_FINAL_SUBMISSION_EDIT_G1_PASS`
