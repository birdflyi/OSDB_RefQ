# Chapter 5 RefQ MS-R02 L0 Submission Length and Information-Allocation Audit

## Decision

`CH5_REFQ_MS_R02_L0_LENGTH_AUDIT_PASS_READY_FOR_BOUNDED_CONDENSATION_PLAN`

MS-R02 is scientifically and editorially complete, but its current Abstract
is overloaded for journal-style submission and several main-text passages can
be made more information-efficient without scientific-semantic loss. This was
an audit-only task. No accepted manuscript, snapshot, sidecar, manifest,
figure, table, or scientific asset was modified.

## 1. Identity

| Item | Result |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before audit | `635aa4fc217ba22a00c62dff4813ffa27c980fdd` |
| Accepted manuscript revision | `MS-R02` |
| Scientific baseline | `P0-v3` |
| CURRENT SHA-256 | `B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC` |
| Immutable MS-R02 snapshot SHA-256 | `B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC` |
| CURRENT equals MS-R02 snapshot | `YES` |
| Stage | `EDITORIAL_COMPLETE_ACCEPTED` |

The four pre-existing untracked V3-V6 ZIP files were not modified or used as
audit inputs.

## 2. Current Abstract decomposition

The accepted Abstract contains five paragraphs and sixteen Chinese-sentence
units. The table decomposes it into twenty-one atomic information units. The
`BODY_STATUS` column records whether the body independently carries the unit;
the keep decision concerns only the future short Abstract.

| ID | Information unit | Current location | Keep in short Abstract | Body status | Body location | Rationale |
|---|---|---|---|---|---|---|
| A01 | Research motivation / construction gap | Paragraph 1 | YES | BODY_ALREADY_COVERS | §§1.1, 1.3 | Required opening problem; body provides full motivation and gap. |
| A02 | Reference Coupling prior-work statement | Paragraph 1 | NO | BODY_ALREADY_COVERS | §§1.2, 2.2 | Citation-bearing related-work detail belongs in Introduction/Related Work, not the short Abstract. |
| A03 | Observable versus quotient-eligible evidence distinction | Paragraph 2 | NO | BODY_ALREADY_COVERS | §§2.2, 3.2.3, 3.3 | Important distinction, but the short Abstract can express the elevation from fine-grained evidence to project relations without carrying the full two-universe terminology. |
| A04 | Artifact-to-project semantic membership | Paragraph 2 | YES | BODY_ALREADY_COVERS | §§1.3, 3.3.1-3.3.3 | Core construct-defining mechanism. |
| A05 | Membership-induced graph coarsening | Paragraph 2 | NO | BODY_ALREADY_COVERS | §§1.2, 2.3, 3.3.2-3.3.3 | The candidate retains the aggregation operation but removes the literature-heavy coarsening label. |
| A06 | RefQ / RefQN definition | Paragraph 2 | YES | BODY_ALREADY_COVERS | §§1.2, 3.3.3 | Essential construct identity. |
| A07 | Non-novelty of generic quotient/coarsening algorithm | Paragraph 2 | NO | BODY_ALREADY_COVERS | §§1.2, 2.5, 5.2 | Necessary novelty positioning in the body, but defensive and inefficient in the Abstract. |
| A08 | Non-dependency / non-task / non-causal boundary | Paragraph 2 | NO | BODY_ALREADY_COVERS | §§1.2, 3.3.3, 5, 6, 9 | Validity and interpretation boundaries remain explicit in the body. |
| A09 | 294 seed-project study design | Paragraph 3 | YES | BODY_ALREADY_COVERS | §§3.1, 3.3.4, 4 | Essential study-object denominator. |
| A10 | 3,748,078 scanned records | Paragraph 3 | NO | BODY_ALREADY_COVERS | §3.2.3; Figure 1 | Denominator-ledger detail, not required in a short Abstract. |
| A11 | 3,747,958 admitted records | Paragraph 3 | NO | BODY_ALREADY_COVERS | §§3.2.3, 4.1; Figure 1 | Fully reported in Methods and Results. |
| A12 | 1,586,047 quotient-eligible records | Paragraph 3 | NO | BODY_ALREADY_COVERS | §§3.2.3, 4.2; Tables 4.6b | Fully reported with its unit and role. |
| A13 | 6,506-node domain | Paragraph 3 | NO | BODY_ALREADY_COVERS | §4.2; Table 4.6b | Network-scale detail remains visible in Results. |
| A14 | 9,884 directed edges | Paragraph 3 | NO | BODY_ALREADY_COVERS | §4.2; Table 4.6b | Network-scale detail remains visible in Results. |
| A15 | 9,595 cross-project edges | Paragraph 3 | NO | BODY_ALREADY_COVERS | §4.2; Table 4.6b | Network-scale detail remains visible in Results. |
| A16 | RQ1 principal finding | Paragraph 4 | YES | BODY_ALREADY_COVERS | §4.1; §5.1; §9 | One compact empirical clause is needed in the Abstract. |
| A17 | RQ2a/RQ2b principal finding | Paragraph 4 | YES | BODY_ALREADY_COVERS | §§4.2a-4.2b; §5.1; §9 | Preserves source/target role asymmetry and heterogeneity. |
| A18 | RQ2c connectivity and Louvain sensitivity | Paragraph 4 | YES | BODY_ALREADY_COVERS | §4.2c; Figure 3; §5; §9 | Central structural result. |
| A19 | RQ3 label-mode-sensitive finding | Paragraph 4 | YES | BODY_ALREADY_COVERS | §4.3; §5; §9 | Central bounded comparison result. |
| A20 | Full scope/validity statement | Paragraph 4 | NO | BODY_ALREADY_COVERS | §3.3.4; §6; §9 | The short Abstract remains accurate without reproducing a validity paragraph. |
| A21 | Four-contribution enumeration | Paragraph 5 | NO | BODY_ALREADY_COVERS | §1.4; §§5.2-5.3; §9 | Replace enumeration with one positive contribution/implication sentence. |

```text
TOTAL_INFORMATION_UNITS = 21
KEEP_IN_SHORT_ABSTRACT_COUNT = 8
INFORMATION_UNITS_REMOVED = 13
```

## 3. Removed-information to body-location matrix

Every removed unit has an adequate body location. No information would vanish
from the manuscript if the proposed short Abstract replaced the current one.

| Removed units | Body coverage | Allocation action |
|---|---|---|
| A02 | §§1.2, 2.2 | NO BODY EDIT NEEDED |
| A03 | §§2.2, 3.2.3, 3.3 | NO BODY EDIT NEEDED |
| A05 | §§1.2, 2.3, 3.3 | NO BODY EDIT NEEDED |
| A07 | §§1.2, 2.5, 5.2 | NO BODY EDIT NEEDED |
| A08 | §§1.2, 3.3.3, 5, 6, 9 | NO BODY EDIT NEEDED |
| A10-A12 | §3.2.3; §§4.1-4.2; Figure 1; Table 4.6b | NO BODY EDIT NEEDED |
| A13-A15 | §4.2; Table 4.6b | NO BODY EDIT NEEDED |
| A20 | §3.3.4; §6; §9 | NO BODY EDIT NEEDED |
| A21 | §1.4; §§5.2-5.3; §9 | NO BODY EDIT NEEDED |

```text
BODY_ALREADY_COVERS_COUNT = 13
NEED_BODY_RELOCATION_COUNT = 0
ABSTRACT_ONLY_BUT_DISPENSABLE_COUNT = 0
```

## 4. Relocation-required findings

No removed Abstract information requires relocation. The body already carries
all thirteen removed units in logically appropriate locations. A future
condensation task should therefore change only the Abstract unless it is also
explicitly authorized to perform the separate main-text efficiency edits
listed below.

```text
ABSTRACT_BODY_RELOCATION_REQUIRED_COUNT = 0
```

## 5. Condensed Chinese Abstract assessment

Leading candidate:

> 开源软件项目中的显式引用记录了包依赖和代码调用之外的跨项目关联，但将细粒度协作引用提升为可解释、可追溯的项目级关系，需要明确项目归属、聚合和观测语义。本文提出 Reference Quotient（RefQ），基于工件到项目的语义归属，将细粒度有向 Reference 关系聚合为加权有向的项目级 Reference Quotient Network（RefQN）。以 294 个开源 DBMS 项目为征引侧种子，本文分析引用证据构成、项目级征引与被引角色、一阶无向结构特征及子领域差异。结果表明，IssueComment 是主要征引载体，外部链接是主要被引对象；不同项目的主动引用范围和被引覆盖呈明显异质性，RefQN 的一阶无向视图广泛连通，但 Louvain 划分对随机种子敏感；子领域差异主要出现在部分网络角色和局部结构指标中，并随标签处理口径变化。RefQ 为开源软件生态中的显式引用关系提供了可追溯的项目级表示，并支持角色化结构分析及对底层协作证据的追溯。

| Diagnostic | Current accepted Abstract | Condensed candidate |
|---|---:|---:|
| Chinese-character count | 555 | 298 |
| Total non-whitespace character count | 2,039 | 418 |
| Paragraph count | 5 | 1 |
| Sentence count | 16 | 5 |

The candidate follows the desired five-function order: problem/gap; construct
and approach; study object/design; principal findings; positive contribution.
It contains no citation, denominator ledger, contribution enumeration,
reproducibility record, or explicit novelty-defense/validity paragraph. No
clear content-allocation defect requires refining the supplied candidate at
this stage.

## 6. English translation and versioning policy

The manuscript should not maintain an authoritative English Abstract during
ordinary Chinese revisions. English translation is deferred until the Chinese
submission Abstract is accepted.

```text
ENGLISH_ABSTRACT_STATUS = TERMINOLOGY_ALIGNMENT_REFERENCE_ONLY
AUTHORITATIVE_FOR_SUBMISSION = NO
FINAL_TRANSLATION_REQUIRED = YES
FINAL_TRANSLATION_TRIGGER = accepted Chinese submission abstract
```

Stable construct names may be aligned now, but sentence-level English wording
must be freshly translated and copyedited later. In particular, no literal
English rendering of `较弱语义` or `弱语义关系` is frozen by this audit.
The provisional alignment paragraph contains 163 English words, within the
working 160-200-word range; it remains non-authoritative.

## 7. Bilingual alignment-file identity

The independent alignment record is outside repository manuscript history:

```text
ALIGNMENT_FILE = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/abstract/ch5_refq_abstract_bilingual_alignment_ABS-R01.md
ABSTRACT_ALIGNMENT_REVISION = ABS-R01
SOURCE_MANUSCRIPT_REVISION = MS-R02
SOURCE_MANUSCRIPT_SHA = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
CHINESE_ABSTRACT_STATUS = SUBMISSION_CONDENSATION_CANDIDATE
ENGLISH_ABSTRACT_STATUS = TERMINOLOGY_ALIGNMENT_REFERENCE_ONLY
AUTHORITATIVE_FOR_SUBMISSION = NO
```

It preserves the current Abstract for comparison, the condensed Chinese
candidate, a non-authoritative provisional English paragraph, terminology
alignment, and an explicit deferred-translation notice.

## 8. Whole-manuscript quantitative length profile

Measurement method:

* Chinese characters: Unicode CJK unified ideographs.
* English token-like units: bounded strings beginning with an ASCII letter and
  continuing with letters, digits, underscore, or hyphen.
* Non-whitespace characters: all characters after removing whitespace.
* Prose paragraphs: blank-line-delimited blocks excluding headings, Markdown
  tables, lists, code/equation blocks, and bibliography entries.
* Table blocks: Markdown header rows followed by separator rows.
* Abstract excludes its heading and keyword line; section headings are excluded
  from their section bodies. Character metrics include tables and equations.

| Section | Chinese chars | English token-like | Non-whitespace chars | Prose paragraphs | Table blocks | Figure captions |
|---|---:|---:|---:|---:|---:|---:|
| Abstract | 555 | 156 | 2,039 | 5 | 0 | 0 |
| §1 | 2,035 | 465 | 6,497 | 16 | 0 | 0 |
| §2 | 1,802 | 440 | 6,266 | 10 | 0 | 0 |
| §3 | 4,688 | 1,529 | 18,900 | 34 | 2 | 0 |
| §4 | 3,599 | 1,090 | 16,520 | 57 | 14 | 4 |
| §5 | 1,079 | 207 | 3,097 | 12 | 0 | 0 |
| §6 | 1,136 | 167 | 2,757 | 10 | 0 | 0 |
| §7 | 298 | 48 | 704 | 3 | 0 | 0 |
| §8 | 74 | 17 | 239 | 1 | 0 | 0 |
| §9 | 244 | 67 | 794 | 4 | 0 | 0 |
| Appendix A | 29 | 483 | 4,202 | 8 | 0 | 0 |
| References | 17 | 808 | 6,774 | 1 | 0 | 0 |

Section 4's fourteen Markdown table blocks include the separate continuation
block for Table 4.6c; it is not a fourteenth semantic numbered table.

## 9. Section-by-section allocation recommendations

| Surface | Primary classification | Recommendation and unique-function guard |
|---|---|---|
| Abstract | CONDENSE_IN_PLACE | Use the five-function candidate; do not relocate the thirteen removed units because the body already covers them. |
| §1.1 | KEEP_MAIN_TEXT | Provides domain motivation not duplicated elsewhere in the same form. |
| §1.2 | CONDENSE_IN_PLACE | Retain RefQ/Reference Coupling/quotient positioning, but consolidate repeated non-novelty and stronger-semantics boundaries. |
| §1.3 | KEEP_MAIN_TEXT | Preserve construction problem and asymmetric observation boundary; only remove wording duplicated verbatim by §1.2 or §1.4. |
| §1.4 | KEEP_MAIN_TEXT | Five RQs and four contributions are structurally necessary; shorten labels only if their semantic roles remain intact. |
| §§2.1-2.4 | KEEP_MAIN_TEXT | Prior-work strands perform distinct support roles; use sentence-level compression rather than removal. |
| §2.5 | CONDENSE_IN_PLACE | Preserve the related-work synthesis, but reduce overlap with the gap and contribution statements in §§1.3-1.4. |
| §§3.1-3.2.2 | KEEP_MAIN_TEXT | Sample identity and source admission are required for interpretation. |
| §3.2.3 | MOVE_TO_APPENDIX | Keep the scanned/admitted/eligible flow and essential denominator map in the main text; move broader data-source, provenance, and artifact-to-RQ inventory detail to Appendix A. |
| §3.3 | KEEP_MAIN_TEXT | This is the construct-defining formal core and should not be shortened by removing membership, endpoint, direction, weight, self-loop, or observation semantics. |
| §3.4 | KEEP_MAIN_TEXT | Metrics and statistical contracts are needed to interpret all RQs; only normalize repeated definitions. |
| §4.1 | CONDENSE_IN_PLACE | Tables and captions carry exact values; prose should interpret leading patterns rather than restate every displayed percentage. |
| §4.2 | CONDENSE_IN_PLACE | Keep denominator scale and RQ2 role findings; remove repeated quantile/top-k lists when already present in Figure 2 and Tables 4.6c-d. |
| Table 4.6c + continuation | MERGE_WITH_ADJACENT_CONTENT | Present as one coherent table or move the relation-partition continuation to supplementary material if the venue requires fewer displays. |
| §4.3 | CONDENSE_IN_PLACE | Keep the cross-mode conclusion and representative values; avoid repeating the full pass/fail matrix in caption, body, and Table 4.8. |
| §§5.1-5.3 | KEEP_MAIN_TEXT | These sections add interpretation, contribution positioning, information-loss implications, and bounded practical use. |
| §5.4 | MERGE_WITH_ADJACENT_CONTENT | Retain only the integrative hierarchy not already stated in §5.1 and §9; merge unique synthesis into the Discussion exit. |
| §6 | KEEP_MAIN_TEXT | Preserve validity threats; keep runtime, package, and immutable identity details in Appendix A rather than duplicating them here. |
| §§7-8 | MERGE_WITH_ADJACENT_CONTENT | If venue structure permits, combine the one-paragraph supplement note with data/code availability while keeping the distinction between public archive and reproducibility record. |
| §9 | KEEP_MAIN_TEXT | Preserve the concise empirical answer, bounded use, limitations, and future work; avoid repeating a full RQ-by-RQ ledger if §5.4 remains. |
| Appendix A | KEEP_MAIN_TEXT | Retain as the designated reproducibility and boundary appendix; absorb detailed inventory moved from §3.2.3. |

## 10. Figure and table placement recommendations

1. Keep Figures 1-4 in the main text because each maps directly to an RQ and
   no figure is merely decorative.
2. Keep Table 4.6b in the main text as the essential edge/node/weight
   denominator map; its units prevent interpretation errors.
3. Merge the two Table 4.6c blocks. If display limits are strict, retain source
   quantiles in the main text and move the relation-partition continuation to
   supplementary material.
4. Keep Table 4.8 in the main text because it directly supports the bounded
   RQ3 inferential conclusion.
5. Treat Table 4.6f's project-level brokerage list as a supplementary-relocation
   candidate; retain the bounded top-line interpretation in the main text.
6. Treat Table 4.7's complete ten-category descriptive rows as a
   supplementary-relocation candidate if the journal limits tables; retain
   representative ranges and the no-FDR-support conclusion in the main text.
7. In §§4.1-4.3, assign exact values primarily to tables/captions and use body
   prose for interpretation. Do not repeat complete row inventories in prose.

```text
SUPPLEMENT_RELOCATION_CANDIDATE_COUNT = 2
```

The conditional Table 4.6c continuation option is classified as a merge first,
not included in the two stronger supplementary candidates.

## 11. Estimated reduction ranges

The proposed Abstract reduces the Han-character count from 555 to 298, a
46.3% reduction, while total non-whitespace characters fall from 2,039 to 418
because citations, dense English taxonomy, and denominator details are
removed. The useful planning range is therefore expressed against Chinese
content rather than the mixed-language raw-character total.

```text
ABSTRACT_REDUCTION_RANGE = approximately 45%-55% by Chinese-character count
MAIN_TEXT_REDUCTION_RANGE = approximately 7%-12% excluding Abstract
SUPPLEMENT_RELOCATION_CANDIDATE_COUNT = 2
```

The main-text range is conditional on consolidating duplication and making the
two table relocations; it is not an acceptance threshold or a required quota.

## 12. Required audit decisions

```text
ABSTRACT_CURRENT_OVERLOADED = YES
ABSTRACT_CONDENSATION_RECOMMENDED = YES
ABSTRACT_BODY_RELOCATION_REQUIRED_COUNT = 0
WHOLE_MANUSCRIPT_CONDENSATION_RECOMMENDED = YES
SCIENTIFIC_RECOMPUTATION_REQUIRED = NO
```

The recommendation is based on information allocation, not a claim about a
specific journal's word limit.

## 13. Scientific and version guards

```text
CURRENT_CHANGED = 0
MS_R02_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_ACCEPTED_REVISION_CREATED = 0

NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0
RQ_TEXT_CHANGED = 0
CONTRIBUTION_ORDER_CHANGED = 0

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

The external ABS-R01 alignment record is non-authoritative and does not count
as a manuscript revision.

## 14. Recommendation for the next manuscript revision

Define a bounded future revision only after the target journal's structural
and length rules are known. The lowest-risk first edit is Abstract-only:
replace the current five-paragraph Abstract with the audited Chinese candidate,
with no body relocation. A separate, explicitly authorized efficiency pass may
then address §1.2/§2.5 overlap, §3.2.3 detail allocation, Results display/prose
duplication, the Table 4.6c merge, conditional Table 4.6f/Table 4.7 relocation,
and §5.4/§9 synthesis overlap. Do not combine that future edit with scientific
recomputation or final English translation.

Final decision:

`CH5_REFQ_MS_R02_L0_LENGTH_AUDIT_PASS_READY_FOR_BOUNDED_CONDENSATION_PLAN`
