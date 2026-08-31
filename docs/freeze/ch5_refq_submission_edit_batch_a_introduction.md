# Chapter 5 RefQ — Submission Editing Batch A: Introduction

## Decision

`CH5_REFQ_SUBMISSION_EDIT_BATCH_A_INTRODUCTION_PASS`

This record documents the bounded Batch-A edit of the external authoritative
manuscript.  Only Sections 1.1–1.4 were edited.  No scientific pipeline,
experiment, figure render, table, or repository scientific asset was run or
changed.

## 1. Starting identity and preserved state

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| `repository_HEAD_before` | `c864fa3adebc1843c68f53caf69cc7630d415369` |
| `remote_HEAD_before` | `c864fa3adebc1843c68f53caf69cc7630d415369` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Manuscript SHA before | `1EE57A3FCA1B8FDCC66B9FD2C45B9E6C696AE304F582FF64A82F235C64B9A7D7` |
| Manuscript SHA after | `8D2C8F0A8E3D57B98F388D1B84E7AEAC3192A6D16B79BB087F6202D53420CB9B` |
| `manuscript_files_changed` | `1` external authoritative Markdown file |

The four pre-existing untracked ZIP files were preserved without staging:

- `figures/ch5_refq/p0v3_final_v3.zip`
- `figures/ch5_refq/p0v3_final_v4.zip`
- `figures/ch5_refq/p0v3_final_v5.zip`
- `figures/ch5_refq/p0v3_final_v6.zip`

The repository itself had no tracked-file modification before this audit
record was created.

## 2. Batch-A scope and hard boundaries

Authorized manuscript scope:

- §1.1 开源 DBMS 生态中的可观测 Reference evidence
- §1.2 Reference Coupling、图粗化与 Reference Quotient
- §1.3 研究缺口与目标
- §1.4 研究问题与贡献

The abstract, Related Work (§2), Methods (§3), Results (§4), Discussion (§5),
Threats to Validity (§6), Data and Code Availability (§7), Supplementary
Material (§8), Conclusion (§9), Appendix, References, tables, equations
outside the Introduction, and all four figure captions were not edited.

The byte-level scope guard used the UTF-8 slice before `## 1 引言` plus the
slice from `## 2 相关工作` to EOF.  That non-Introduction concatenation was
`107746` bytes with SHA-256
`94e24308b387cf6f7da2777f905d2e3b8ab223253f6d106e9a319342cfdb4c27` both
before and after.  Thus the external manuscript change is confined to the
Introduction slice.

## 3. Protected scientific meanings

The following meanings were checked after editing and remained present:

| Closure | Status | Evidence retained |
|---|---|---|
| `REFERENCE_COUPLING_PRECEDENT` | `PASS` | Blincoe 2015/2019; cross-project references; directed project-level graph; project-pair count weight; ecosystem/community or dependency-oriented precedent |
| `IREL_PRECEDENT` | `PASS` | IREL URL/Num/SHA extraction and project identity/rename resolution |
| `GRAPH_QUOTIENT_BACKGROUND` | `PASS` | Loukas, Sánchez-García, Xiao; mapping/partition/coarsening vocabulary; no symmetry/spectral guarantees inherited |
| `REFQ_FORMALIZATION_REFRAMING` | `PASS` | RefQ/RefQN remains a paper-defined formalization/reframing of direct project-reference aggregation, not a new generic graph operator |
| `FIRST_ORDER_REFQ_BOUNDARY` | `PASS` | (Q=M^\top R_PM) remains the first-order RefQ relation |
| `SECOND_ORDER_PROJECTION_EXCLUDED` | `PASS` | (QQ^\top), (Q^\top Q), and (K=X\Phi X^\top) remain distinct and outside the core experiment |
| `TWO_UNIVERSE_BOUNDARY` | `PASS` | observable fine-grained Reference evidence universe remains separate from the quotient-eligible project-mappable subset |
| `SEED_CENTERED_OBSERVATION` | `PASS` | 294 source-side seed projects and source-incomplete expanded targets remain explicit |
| `WEAK_SEMANTIC_BOUNDARY` | `PASS` | RefQ is not package/code dependency, task resolution, technical adoption, causal influence, or complete knowledge flow |
| `DBMS_VERTICAL_SETTING` | `PASS` | Open-source DBMS vertical ecosystem and GitHub collaboration traces remain the empirical setting |

## 4. Exact bounded edits

Only the following Introduction fragments changed.  The edit types are
language or structure edits; no scientific value, population, metric, or
citation was changed.

| ID | Section | Before | After | Reason | Semantic risk |
|---|---|---|---|---|---|
| A1 | §1.1 | `explicit Reference evidence 和 project-level structural relation` | `显式 Reference evidence 和项目级结构关系` | Remove unnecessary code switching in the motivation sentence | LOW |
| A2 | §1.1 | `所有 Reference motives` | `所有 Reference 动机` | Publication-oriented local wording | LOW |
| A3 | §1.2 | `本文的增量不是否认这些已有操作，而是把 ... 这样可以在承认 project-level aggregation 先例的同时 ...` | `在承认这些先例的基础上，本文将 ... 该区分明确 ...` | Remove duplicated novelty transition while retaining Blincoe/IREL attribution and the two-universe contract | LOW–MEDIUM |
| A4 | §1.3 | `本文聚焦一个可实证检验的问题：...围绕这一问题，本文从...组织研究动机。` | `在上述概念定位基础上，本文将研究缺口具体化为三个方面：领域适用性、关系构造透明度和观测角色分离。` | Give §1.3 a direct gap bridge and avoid repeating the full positioning from §1.2 | LOW–MEDIUM |
| A5 | §1.3 | `因此，本文的 academic problem 不只是对记录进行 group-by...project-level relation` | `归结而言，本文关注的研究问题并非简单的记录分组统计...项目级关系` | Replace working-note phrasing with publication-oriented Chinese and retain the construction-contract list | LOW |
| A6 | §1.3 | `因此，本文的目标是...evidence layer...downstream analyses` | `基于这一研究问题，本文的目标是...提供证据层...这些分析` | Make the gap → problem → objective transition non-repetitive and reduce unnecessary English | MEDIUM |
| A7 | §1.4 | `针对上述问题...本文的核心目标是...围绕这一目标...` | `在上述研究目标下...通过 ... 构建 Project-level RefQN；围绕这一对象...` | Make the RQ lead-in concise without removing the 294-project sample or construction identity | LOW–MEDIUM |
| A8 | §1.4 | One 1,269-character sentence containing all four contributions | Four parallel `第一`/`第二`/`第三`/`第四` paragraphs plus the existing five-RQ summary | Improve submission readability while retaining exactly four contribution meanings | LOW–MEDIUM |
| A9 | §1.4 | `DBMS vertical ecosystem`; `sampling-induced misinterpretation`; `provenance`; `inference commitment`; `reusable interface` | `DBMS 垂直生态`; `抽样诱发误读`; `来源可追溯性`; `推断承诺`; `可复用接口` | Convert explanatory mixed-language fragments while retaining controlled technical terms | LOW |

The four contribution meanings remain, one each: explicit relation
formalization/construction contract; boundary-aware evidence instantiation;
observation-aware role-aware empirical characterization; and a traceable
weaker-semantic structural evidence layer.  No fifth contribution was added.

## 5. Introduction structure before and after

| Section | Before role | After role | Prose sentences before → after | Structural result |
|---|---|---|---:|---|
| §1.1 | Establish DBMS motivation and observable Reference evidence | Same motivation, with local wording simplified | 11 → 11 | Motivation remains distinct |
| §1.2 | Position Reference Coupling, quotient/coarsening, RefQ and projection boundary | Same conceptual-definition authority; duplicated transition compressed | 19 → 19 | Prior-work and mathematical boundary remain complete |
| §1.3 | Gap, working-note problem statement, and objective with repeated `因此` | Concise gap bridge → three gaps → formal problem → objective | 14 → 13 | `INTRO_GAP_OBJECTIVE_TRANSITION = PASS` |
| §1.4 | RQ lead-in plus one overloaded contribution paragraph | Concise lead-in → unchanged five RQs → four parallel contribution blocks | 8 → 6 | `CONTRIBUTION_COUNT = 4` |

The sentence diagnostic used the prior audit convention: contiguous prose
blocks; headings, Markdown list items, table rows, fenced code, and display
math excluded; sentences split at Chinese terminal punctuation (and eligible
English terminal punctuation); a trailing lead-in fragment ending in a colon
is not counted.  Results:

```text
INTRO_SENTENCE_COUNT_BEFORE = 52
INTRO_SENTENCE_COUNT_AFTER = 49
INTRO_VERY_LONG_SENTENCE_COUNT_BEFORE = 6
INTRO_VERY_LONG_SENTENCE_COUNT_AFTER = 6
INTRO_MAX_SENTENCE_LENGTH_BEFORE = 373
INTRO_MAX_SENTENCE_LENGTH_AFTER = 373
```

The unchanged long sentences are in the protected conceptual/gap material;
the former contribution sentence was separated into parallel blocks.  The
diagnostic is descriptive, not a target for mechanical sentence splitting.

For reproducibility, the >240-character locations were before: §1.2 L26
(260) and L28 (373), §1.3 L43 (364), and the three contribution clauses at
§1.4 L60 (349/305/276); after: §1.2 L26 (260) and L28 (373), §1.3 L43 (364),
and §1.4 L62 (349), L64 (290), and L66 (246).

## 6. RQ, citation, and numeric closure

The five RQ list items (`RQ1`, `RQ2a`, `RQ2b`, `RQ2c`, `RQ3`) are byte-identical
before and after.  Their semantic closures are:

```text
RQ1_SEMANTIC_CLOSURE = PASS
RQ2A_SEMANTIC_CLOSURE = PASS
RQ2B_SEMANTIC_CLOSURE = PASS
RQ2C_SEMANTIC_CLOSURE = PASS
RQ3_SEMANTIC_CLOSURE = PASS
```

Citation keys were compared as an occurrence multiset and as a unique set:

```text
CITATION_OCCURRENCES_BEFORE = 18
CITATION_OCCURRENCES_AFTER = 18
CITATION_UNIQUE_KEYS_BEFORE = 13
CITATION_UNIQUE_KEYS_AFTER = 13
CITATION_SET_CHANGED = 0
```

The Introduction numeric token multiset is unchanged.  The raw guard
tokenization used the alternation
`@[A-Za-z0-9_]+|(?<![A-Za-z0-9_])\d[\d,]*(?:\.\d+)?(?![A-Za-z0-9_])` on the
complete Introduction slice and gives 32 → 32 tokens (18 citation-key
occurrences plus 14 boundary numeric tokens, including heading/list labels).
After removing citation tokens, headings, and RQ labels, the guarded
scientific multiset is
`2015 × 2`, `2019 × 2`, and `294 × 5` both before and after.  Therefore:

```text
INTRO_NUMERIC_TOKEN_CHANGE_COUNT = 0
```

The RQ bullets, all sample counts, and all protected network quantities remain
unchanged.

## 7. Caption, table, and asset immutability

The four frozen caption blocks were extracted and compared byte-for-byte:

```text
FIGURE_CAPTION_COUNT = 4
FIGURE1_CAPTION_UNCHANGED = PASS
FIGURE2_SCIENTIFIC_CONTENT_UNCHANGED = PASS
FIGURE3_SCIENTIFIC_CONTENT_UNCHANGED = PASS
FIGURE4_CAPTION_UNCHANGED = PASS
FIGURE_CAPTION_EDIT_COUNT = 0
TABLE_CONTENT_CHANGED = 0
figure_assets_changed = 0
scientific_assets_changed = 0
```

No figure, supplemental output, manifest, receipt, scientific code, or ZIP
asset was opened for writing.  No experiment or render was run.

## 8. Scope and scientific guards

```text
INTRODUCTION_CHANGED = 1
NON_INTRODUCTION_PROSE_CHANGED = 0
ABSTRACT_CHANGED = 0
RELATED_WORK_CHANGED = 0
METHODS_CHANGED = 0
RESULTS_CHANGED = 0
DISCUSSION_CHANGED = 0
THREATS_CHANGED = 0
AVAILABILITY_CHANGED = 0
CONCLUSION_CHANGED = 0
APPENDIX_CHANGED = 0
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
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

The only durable, non-temporary write outside the repository was the
authorized edit to the external authoritative manuscript.  A temporary
read-only comparison snapshot was created under the local OS temporary
directory and is not a manuscript, scientific asset, or deliverable.  The
only repository artifact authorized by this batch is this freeze record.

## 9. Final closure

```text
INTRO_GAP_OBJECTIVE_TRANSITION = PASS
INTRO_NOVELTY_REDUNDANCY_REDUCED = PASS
NOVELTY_BOUNDARY_PRESERVED = PASS
CONTRIBUTION_COUNT = 4
CONTRIBUTION_SEMANTIC_CLOSURE = PASS
INTRO_UNNECESSARY_CODE_SWITCHING_REDUCED = PASS
RQ1_SEMANTIC_CLOSURE = PASS
RQ2A_SEMANTIC_CLOSURE = PASS
RQ2B_SEMANTIC_CLOSURE = PASS
RQ2C_SEMANTIC_CLOSURE = PASS
RQ3_SEMANTIC_CLOSURE = PASS
INTRO_NUMERIC_TOKEN_CHANGE_COUNT = 0
CITATION_SET_CHANGED = 0
```

No high-risk semantic edit was required.  The Introduction now has a clear
motivation → conceptual positioning → gap/problem/objective → RQ/contribution
sequence while preserving the accepted RefQ construction, observation, unit,
and weak-semantic boundaries.

Final decision:

`CH5_REFQ_SUBMISSION_EDIT_BATCH_A_INTRODUCTION_PASS`
