# Chapter 5 RefQ MS-R03 Venue-Independent Submission Condensation Candidate

## 1. Decision

```text
TASK = CH5_REFQ_MS_R03_VENUE_INDEPENDENT_SUBMISSION_CONDENSATION
DECISION = CH5_REFQ_MS_R03_SUBMISSION_CONDENSATION_CANDIDATE_PASS_READY_FOR_FINAL_QA
READY_FOR_FINAL_QA = YES
REDUCTION_TARGET_ENFORCED = NO
```

This record freezes the candidate-stage result only. It does not promote
MS-R03, replace the accepted `CURRENT`, or establish a new accepted manuscript
revision.

## 2. Source and candidate identity

```text
REPOSITORY_BRANCH = ch5-refq-repository-identity-correction-v1
REPOSITORY_HEAD_BEFORE = 6134a7cb875dc57e2fae3dd1c934023197a5265b

SOURCE_REVISION = MS-R02
SOURCE_PATH = versions/MS-R02_EDITORIAL_COMPLETE_B1494BA3.md
SOURCE_SHA = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC

CANDIDATE_REVISION = MS-R03_CANDIDATE
CANDIDATE_PATH = working/MS-R03_SUBMISSION_CONDENSATION_CANDIDATE.md
CANDIDATE_SHA = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
```

The source snapshot and candidate paths above are relative to the external
manuscript root:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/`

The candidate remains outside the Git repository under the established
manuscript-storage policy.

## 3. Candidate-first and protected-version gate

The pre-edit authority gate and the post-edit protection check both passed.

```text
CURRENT_SHA_BEFORE = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
CURRENT_SHA_AFTER  = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC

MS_R02_SNAPSHOT_SHA_BEFORE = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
MS_R02_SNAPSHOT_SHA_AFTER  = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC

SIDECAR_SHA_BEFORE = 16E02CD26445F416ED07BACE0568823A2EB5FE7310E362E143DAE0207A3F59A7
SIDECAR_SHA_AFTER  = 16E02CD26445F416ED07BACE0568823A2EB5FE7310E362E143DAE0207A3F59A7

MANIFEST_SHA_BEFORE = 639EEE81C15182D565D7207979EB6D9153C6B06F4094A4F780858EC3492FF9CB
MANIFEST_SHA_AFTER  = 639EEE81C15182D565D7207979EB6D9153C6B06F4094A4F780858EC3492FF9CB

ABS_R01_SHA_BEFORE = 68E85D74989880AC549B2A115FAC181BC46F40F5C0A50C4B664B639D86F534C9
ABS_R01_SHA_AFTER  = 68E85D74989880AC549B2A115FAC181BC46F40F5C0A50C4B664B639D86F534C9

CURRENT_CHANGED = 0
MS_R02_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_ACCEPTED_REVISION_CREATED = 0
```

The standalone ABS-R01 English paragraph remains a terminology-alignment
reference only. It was neither rewritten nor mechanically synchronized.

## 4. Abstract before and after

### 4.1 MS-R02 Abstract before

> 开源 DBMS 生态具有复杂的跨项目语境，许多项目间关联难以仅通过包依赖或代码调用观察。Reference Coupling 研究表明，GitHub cross-project references 可形成有向、按引用次数加权的项目级网络并用于软件生态分析 [@blincoe2015ecosystems; @blincoe2019referencecoupling]。这些显式 Reference evidence 补充了包依赖和代码调用之外的项目关联；从细粒度 evidence 到项目级关系仍需明确 membership semantics、endpoint eligibility、聚合与观测边界。
>
> 本文将 observable fine-grained Reference evidence universe 与 quotient-eligible、project-mappable 子域分开；后者通过 artifact-to-project membership mapping 形成 partition，并以 membership-induced graph coarsening 将工件级有向关系聚合为 weighted directed quotient graph。所得构念定义为 paper-specific Reference Quotient（RefQ），网络表示为 Reference Quotient Network（RefQN）。本文不提出新的 quotient-graph 或 graph-coarsening algorithm，而在开源 DBMS 场景中对项目级 Reference aggregation 进行语义形式化、边界化实例化与实证分析。RefQ 是可追溯的一阶项目级结构关系，不等同于 package/code dependency、task resolution 或 causal influence。
>
> 本文以 GitHub 平台 294 个开源 DBMS 项目作为征引侧种子样本，基于 GH_CoRE 处理链抽取并校验协作引用关系。观测窗口扫描 3,748,078 条输入 Reference records，经 source-admission 后保留 3,747,958 条 admitted source-observation records；其中 1,586,047 条具有可唯一映射到项目的 target endpoint，满足 quotient eligibility 并进入 Project-level RefQ aggregation。Project-level RefQN 的完整节点域为 6,506 个项目，形成 9,884 条含自环的有向 RefQ edges，其中 9,595 条为跨项目边；无向派生视图用于结构分析。
>
> 结果显示，IssueComment 是主要征引载体，GitHub external links 是主要被引对象，项目内部与外部 evidence 并存。Project-level RefQN 的 source/target role 在典型值与极大值之间存在明显差距，target-side weight 集中于少数项目；一阶无向视图广泛连通，但 Louvain algorithmic partition 对 random seed 敏感。RQ3 中 Reference composition 在两种 label mode 下均无 FDR-supported group difference；部分 RefQ role、local-structure 与 project-age features 仅在 include_mixed 下达到阈值。因此，子领域结果是局部且 label-mode sensitive 的。上述发现限于 GitHub 可观测 Reference evidence、GH_CoRE 抽取规则和 seed-centered observed RefQN 边界。
>
> 本文贡献包括四点：第一，明确规定细粒度 Reference evidence 如何经 endpoint eligibility、semantic membership、block aggregation、方向与 self-loop policy 构造成可追溯的 RefQ/RefQN；第二，在 DBMS 垂直生态中实例化 observable Reference evidence 与 quotient-eligible project-mappable subset 的证据边界，分别保留 non-project evidence、source observation boundary 与 expanded-target asymmetry；第三，在不对称观测下分别刻画 source role、target role 与一阶无向结构视图，并以 RQ1 支撑边界、以受限 RQ3 比较检验局部且 label-mode-sensitive 的差异；第四，将 RefQ 定位为可追溯、较弱语义的项目级 structural evidence layer，用于 candidate screening、structural inspection，并为需要更强语义验证的后续关系分析提供接口。

### 4.2 MS-R03 candidate Abstract after

> 开源软件项目中的显式引用记录了包依赖和代码调用之外的跨项目关联，但将细粒度协作引用提升为可解释、可追溯的项目级关系，需要明确项目归属、聚合和观测语义。本文提出 Reference Quotient（RefQ），基于工件到项目的语义归属，将细粒度有向 Reference 关系聚合为加权有向的项目级 Reference Quotient Network（RefQN）。以 294 个开源 DBMS 项目为征引侧种子，本文分析引用证据构成、项目级征引与被引角色、一阶无向结构特征及子领域差异。结果表明，IssueComment 是主要征引载体，外部链接是主要被引对象；不同项目的主动引用范围和被引覆盖呈明显异质性，RefQN 的一阶无向视图广泛连通，但 Louvain 划分对随机种子敏感；子领域差异主要出现在部分网络角色和局部结构指标中，并随标签处理口径变化。RefQ 为开源软件生态中的显式引用提供了可追溯的项目级结构表示，可用于刻画跨项目引用角色及其网络组织特征。

```text
ABSTRACT_CHINESE_CHARS_BEFORE = 555
ABSTRACT_CHINESE_CHARS_AFTER = 297
ABSTRACT_REDUCTION_PERCENT = 46.49
ABSTRACT_BODY_RELOCATION_COUNT = 0
ABSTRACT_CITATION_TOKEN_COUNT_AFTER = 0
```

## 5. Authorized changed-region map

The MS-R02-to-candidate line diff contains 21 non-equal hunks. Every hunk maps
to one of the five authorized groups.

| Group | Authorized region | Hunk count | Result | Condensation performed |
|---|---|---:|---|---|
| A | Abstract | 1 | PASS | Replaced the five-paragraph Abstract with the frozen short Chinese Abstract. |
| B | §1.2 | 2 | PASS | Consolidated RefQ positioning, non-novelty, stronger-semantics boundaries, and the second-order exclusion without removing the formulas or citation roles. |
| C | §2.5 | 1 | PASS | Preserved the four required precedent/gap functions while shortening the repeated inventory. |
| D | §§4.1-4.3 | 14 | PASS | Removed exact display-value repetition while retaining interpretation, representative values, denominators, and unit boundaries. |
| E | §5.4 / §9 | 3 | PASS | Replaced duplicate RQ ledgers with distinct Discussion synthesis and concise Conclusion findings. |

```text
UNMAPPED_CHANGED_REGION_COUNT = 0
UNAUTHORIZED_CHANGED_REGION_COUNT = 0
```

The following non-authorized regions were compared as exact text blocks and
remained identical: §§1.1, 1.3, 1.4, 2.1-2.4, all of §3, §§5.1-5.3, §§6-8,
Appendix A, and References. Heading hierarchy is unchanged. Table 4.6c remains
two display blocks and was not merged or moved.

## 6. Removed repetition and retained evidence locations

| Condensed statement class | Candidate treatment | Retained evidence / function location |
|---|---|---|
| Abstract prior-work citations and literature detail | Removed from Abstract | §§1.2, 2.2 and 2.5 retain Reference Coupling, IREL and quotient/coarsening precedent with citations. |
| Abstract denominator and network-scale ledger | Removed from Abstract | §3.2.3, Figure 1, and Table 4.6b retain the scanned/admitted/eligible and node/edge/weight contracts. |
| Abstract four-contribution enumeration | Replaced by one bounded implication sentence | §1.4 retains all four contributions in the accepted order and wording. |
| Abstract dependency/task/causal and validity caveats | Removed from Abstract | §§1.2, 3.3.3-3.3.4, 5, 6 and 9 retain the stronger-semantics and observation-boundary guards. |
| Repeated §1.2 non-novelty and stronger-semantics wording | Consolidated | The RefQ positioning paragraph retains direct-aggregation precedent, non-operator novelty, direction, membership, weight and semantic limits. |
| Repeated §1.2 second-order exclusion | Consolidated | The unchanged formula paragraph retains `Q=M^\top R_PM`, `QQ^\top`, `Q^\top Q`, `K=X\Phi X^\top`, and the first-/second-order operator distinction. |
| Full §2.5 gap/contribution inventory | Condensed | §§1.3-1.4 retain the detailed gap and contributions; §3 operationalizes the construction-and-observation contract. |
| Table 4.1 full percentage list | Removed from prose | Table 4.1 remains byte-identical; the 3,747,958-record denominator and interpretation remain in prose. |
| Table 4.2 full percentage list | Removed from prose | Table 4.2 remains byte-identical; target-type interpretation and semantic limits remain. |
| Tables 4.3-4.5 complete descriptive-statistic lists | Removed from prose | Tables 4.3-4.5 remain byte-identical; distributional interpretation, unit semantics and bounded examples remain. |
| Table 4.6a full coefficient/p-value list | Removed from prose | Table 4.6a remains byte-identical; `n=291`, complementary-share sign relation and weak-association interpretation remain. |
| Table 4.6b complete node/edge/weight ledger | Removed from prose | Table 4.6b remains byte-identical; cross-project weight denominator 138,974 and the directed/undirected edge-count distinction remain. |
| Figure 2 / Table 4.6c complete source quantiles | Removed from prose | Figure 2 and both Table 4.6c blocks remain byte-identical; the typical-versus-maximum interpretation and no-distribution-fit caveat remain. |
| Table 4.6c relation-partition exact totals | Removed from prose | The Table 4.6c continuation remains byte-identical; seed-to-expanded dominance and source-incomplete semantics remain. |
| Figure 2 / Table 4.6d complete target quantiles and top-k list | Removed from prose | Figure 2 and Table 4.6d remain byte-identical; denominator 138,974 and the 3,430 / 2.47% top-1 example remain. |
| Table 4.6e complete structure-value list | Removed from prose | Table 4.6e remains byte-identical; 97.86% LCC coverage and the first-order-not-projection boundary remain. |
| Table 4.6f five exact ranking values | Removed from prose | Table 4.6f remains byte-identical; representative top projects, sampling method and non-importance caveat remain. |
| Table 4.8 full inferential-matrix preview | Replaced by display lead-in | Table 4.8 remains byte-identical; the following paragraphs retain representative cross-mode interpretation. |
| §5.4 full RQ-by-RQ ledger | Condensed to two Discussion-level paragraphs | §4 retains result detail; §5.4 retains the evidence-boundary / structural-center / bounded-comparison hierarchy. |
| §9 repeated RQ ledger | Removed | §9 retains construct/method summary, principal findings, positive bounded use, limitations and future work. |

No removed scientific value was deleted from its authoritative table, figure
caption, formula, or other required evidence location.

## 7. Length diagnostics

Measurement follows the L0 method: CJK characters are Unicode CJK unified
ideographs; English token-like units begin with an ASCII letter and continue
with letters, digits, underscore or hyphen; non-whitespace characters remove
all whitespace. Abstract excludes its heading and keyword line. Section
headings are excluded from section bodies. The whole-main-text row concatenates
the Abstract and §§1-9 and excludes Appendix A and References.

| Scope | CJK before | CJK after | CJK reduction | English token-like before | English token-like after | Non-whitespace before | Non-whitespace after | Non-whitespace reduction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Abstract | 555 | 297 | 46.49% | 156 | 13 | 2,039 | 417 | 79.55% |
| §1 | 2,035 | 1,950 | 4.18% | 465 | 453 | 6,497 | 6,300 | 3.03% |
| §2 | 1,802 | 1,804 | -0.11% | 440 | 433 | 6,266 | 6,179 | 1.39% |
| §4 | 3,599 | 3,424 | 4.86% | 1,090 | 1,028 | 16,520 | 15,375 | 6.93% |
| §5 | 1,079 | 953 | 11.68% | 207 | 172 | 3,097 | 2,601 | 16.02% |
| §9 | 244 | 221 | 9.43% | 67 | 58 | 794 | 715 | 9.95% |
| Main text excluding Appendix/References | 15,510 | 14,845 | 4.29% | 4,184 | 3,916 | 57,813 | 54,187 | 6.27% |

```text
MAIN_TEXT_REDUCTION_PERCENT = 6.27
MAIN_TEXT_REDUCTION_METRIC = NON_WHITESPACE_CHARACTERS
REDUCTION_TARGET_ENFORCED = NO
```

The small CJK increase in §2 reflects a shorter mixed Chinese/English synthesis
with fewer English token-like units and fewer total non-whitespace characters;
it is not a failed target because no fixed reduction percentage was imposed.

## 8. Citation closure

```text
CITATION_TOKEN_COUNT_BEFORE = 69
CITATION_TOKEN_COUNT_AFTER = 67

UNIQUE_CITATION_KEY_COUNT_BEFORE = 32
UNIQUE_CITATION_KEY_COUNT_AFTER = 32

BIBLIOGRAPHY_ENTRY_COUNT_BEFORE = 32
BIBLIOGRAPHY_ENTRY_COUNT_AFTER = 32

MISSING_CITATION_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
```

The only removed citation tokens are `blincoe2015ecosystems` and
`blincoe2019referencecoupling` from the old Abstract. Both keys remain cited in
the body and both bibliography entries remain required. No body citation token
was removed.

## 9. Display closure

All fourteen main-text Markdown table blocks, including the separate Table
4.6c continuation block, are exact text matches to MS-R02. All four figure
captions are exact text matches to MS-R02. Figures 1-4 and Tables 4.1-4.8,
including Tables 4.6a-4.6f, remain in the main text.

```text
FIGURE_CAPTION_COUNT = 4
MISSING_REQUIRED_DISPLAY_COUNT = 0
ORPHAN_DISPLAY_COUNT = 0
DISPLAY_WITHOUT_LEAD_IN_COUNT = 0
DISPLAY_WITHOUT_INTERPRETATION_COUNT = 0
UNSUPPORTED_MATERIAL_CLAIM_COUNT = 0

TABLE_4_6C_MOVED = 0
TABLE_4_6F_MOVED = 0
TABLE_4_7_MOVED = 0
FIGURE_ASSET_CHANGE_COUNT = 0
FIGURE_RERENDER = 0
```

## 10. Scientific and semantic guards

The five RQ lines and the complete §1.4 contribution block are exact text
matches to MS-R02. All of §3, all Markdown table blocks, all figure captions,
and the inferential result paragraphs following Table 4.8 are exact matches.
The candidate changes presentation density only.

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0

RQ_COUNT = 5
RQ_TEXT_CHANGED = 0

CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0
CONTRIBUTION_SEMANTIC_ROLE_CHANGED = 0

Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_SECOND_ORDER_BOUNDARY_CHANGED = 0

STATISTICAL_TEST_CHANGED = 0
EFFECT_SIZE_LABEL_CHANGED = 0
EFFECT_SIZE_VALUE_CHANGE_COUNT = 0
FDR_FAMILY_CHANGED = 0
LABEL_MODE_CHANGED = 0
CROSS_MODE_RESULT_CHANGED = 0

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
```

## 11. Readiness

The candidate meets the venue-independent objective: the overloaded Abstract
is replaced, demonstrated repetition is reduced, and each unique scientific,
semantic and rhetorical function remains in the manuscript. No venue-specific
display relocation, appendix restructuring, English-Abstract maintenance, or
accepted-version promotion was performed.

```text
AUTHORIZED_EDIT_GROUP_A = PASS
AUTHORIZED_EDIT_GROUP_B = PASS
AUTHORIZED_EDIT_GROUP_C = PASS
AUTHORIZED_EDIT_GROUP_D = PASS
AUTHORIZED_EDIT_GROUP_E = PASS

READY_FOR_FINAL_QA = YES
DECISION = CH5_REFQ_MS_R03_SUBMISSION_CONDENSATION_CANDIDATE_PASS_READY_FOR_FINAL_QA
```
