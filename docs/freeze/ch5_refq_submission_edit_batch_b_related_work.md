# Chapter 5 RefQ — Submission Editing Batch B: Related Work

## Decision

CH5_REFQ_SUBMISSION_EDIT_BATCH_B_RELATED_WORK_PASS

This record documents the bounded Related Work edit authorized after the
accepted hierarchy and terminology decisions.  Only §2.1–§2.5 of the
external authoritative manuscript were edited.  The edit clarifies empirical,
identity/extraction, mathematical, and DBMS-setting roles without redefining
the accepted RefQ hierarchy or adding a scientific claim.

## 1. Starting identity and preserved state

| Item | Value |
|---|---|
| Repository | D:/github_repo/OSDB_RefQ |
| Branch | ch5-refq-repository-identity-correction-v1 |
| repository_HEAD_before | b3dcd1264bd47ba6cac433b82a8ac2b08b43008c |
| remote_HEAD_before | b3dcd1264bd47ba6cac433b82a8ac2b08b43008c |
| Authoritative manuscript | C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md |
| Manuscript SHA before | 05232481C69BAAAE468F636D443D928D4162CE4864A72B796F2AC5603E5CC5B4 |
| Read-only baseline copy | C:/Users/10651/AppData/Local/Temp/ch5_refq_batch_b_related_work_baseline_20260831.md |
| Baseline-copy SHA | 05232481C69BAAAE468F636D443D928D4162CE4864A72B796F2AC5603E5CC5B4 |
| Manuscript location in Git | External; not tracked by OSDB_RefQ |

The four pre-existing untracked rendering archives were preserved and not
staged:

~~~text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
~~~

## 2. Governing hierarchy and Related Work responsibilities

The accepted paper chain remains:

~~~text
fine-grained Reference evidence
→ observable evidence is not identical to quotient-eligible evidence
→ endpoint eligibility + semantic membership
→ membership-induced quotient construction
→ Project-level RefQ / RefQN
→ seed-centered role separation
→ RQ2a/b/c structural characterization
→ RQ1 boundary support + RQ3 bounded comparison
~~~

Related Work now has the following reviewer-facing order:

~~~text
§2.1 ecosystem and socio-technical background
§2.2 direct-reference empirical precedent + extraction/identity precedent
§2.3 quotient/coarsening mathematical positioning + first-order boundary
§2.4 DBMS bounded empirical setting
§2.5 integrated implicit-to-explicit construction-contract gap
~~~

The section does not claim that RefQ invented project-pair aggregation,
direction, count weighting, a project-reference network, graph contraction,
or a generic graph algorithm.  RefQ remains a paper-defined, traceable,
first-order project-level relation under semantic membership and
seed-centered observation.

~~~text
SECTION_2_1_ROLE = ECOSYSTEM_SOCIO_TECHNICAL_BACKGROUND
SECTION_2_2_ROLE = DIRECT_REFERENCE_AND_EXTRACTION_IDENTITY_PRECEDENT
SECTION_2_3_ROLE = QUOTIENT_COARSENING_MATHEMATICAL_POSITIONING
SECTION_2_4_ROLE = DBMS_BOUNDED_EMPIRICAL_SETTING
SECTION_2_5_ROLE = INTEGRATED_IMPLICIT_TO_EXPLICIT_GAP_CLOSURE
~~~

## 3. Section-function matrix

| Section | Function before | Function after | Redundancy reduced | Semantic change |
|---|---|---|---|---|
| §2.1 | Broad ecosystem and socio-technical background, with mixed-language labels and a slightly early RefQ capability claim | Same background; terminology is publication-facing and DBMS is framed as a bounded setting | Removes unnecessary code switching and weakens premature novelty emphasis | No |
| §2.2 | Platform links, direct-reference precedent, IREL, and two-universe model | Primary authority for Blincoe precedent, IREL extraction/identity distinction, and the two-universe boundary | Keeps the full precedent statement here and avoids repeating it as a long disclaimer later | No |
| §2.3 | Quotient/coarsening background, formula, guarantees, and projection boundary in dense paragraphs | Primary mathematical authority with clearer normalized/unnormalized and first-/second-order transitions | Splits dense sentences without deleting necessary boundaries | No |
| §2.4 | DBMS motivation and RQ3 setting with mixed English phrases and a repeated capability framing | Bounded vertical empirical setting and testable RQ3 motivation | Removes repeated gap language and translates non-technical working-note phrases | No |
| §2.5 | Long recap of empirical and mathematical precedents plus formalization claim | Short decisive synthesis and implicit-to-explicit contract closure | Consolidates precedent descriptions and avoids repeating §2.2/§2.3 detail | No |

## 4. Exact bounded edits

### 4.1 §2.1

The analytical framing paragraph was changed only in terminology:

~~~text
Before:
在本文的 analytical framing 中，社会关系用于指代开发者互动和社区协作，技术关系用于指代依赖、调用、构件和代码演化，任务关系用于组织 Issue、PR、Commit 和评论等问题处理上下文；这一三分结构是本文的分析组织方式，而不是上述文献共同给出的标准 taxonomy。开源 DBMS 生态中的协作证据可能跨越这些视角：开发者在问题讨论中引用其他项目的实现或缺陷报告，维护者在 PR 审查中链接历史提交和外部文档，用户在 Issue 中提供跨版本适配经验或兼容性证据。因此，包依赖或代码调用关系之外的 explicit Reference evidence 值得单独观察。

After:
在本文的分析框架中，社会关系用于指代开发者互动和社区协作，技术关系用于指代依赖、调用、构件和代码演化，任务关系用于组织 Issue、PR、Commit 和评论等问题处理上下文；这一三分结构是本文的分析组织方式，而不是上述文献共同提出的标准分类体系。开源 DBMS 生态中的协作证据可能跨越这些视角：开发者在问题讨论中引用其他项目的实现或缺陷报告，维护者在 PR 审查中链接历史提交和外部文档，用户在 Issue 中提供跨版本适配经验或兼容性证据。因此，包依赖或代码调用关系之外的显式 Reference evidence 值得单独观察。
~~~

The closing paragraph was made contextual rather than a second novelty
statement:

~~~text
Before:
现有软件生态研究为本文提供了两个基础前提。其一，生态层面的结构分析需要明确场景边界，避免将所有开源项目视为同质样本。其二，项目间关系解释需要通过可追溯的协作事实进行表示，否则难以支持跨项目比较。本文将开源 DBMS 作为垂直软件生态场景，正是为了在明确场景约束的前提下考察 RefQ 的构造与解释能力。

After:
现有软件生态研究为本文提供了两个背景前提。其一，生态层面的结构分析需要明确场景边界，避免将所有开源项目视为同质样本。其二，项目间关系解释需要通过可追溯的协作事实进行表示。本文将开源 DBMS 作为受约束的经验场景，以便在明确场景边界的前提下观察 Reference evidence 与项目级结构关系；具体的 RefQ 构造和解释规则在后文说明。
~~~

### 4.2 §2.2

The platform/link-context wording was translated without removing any
platform or empirical precedent:

~~~text
empirical link contexts → 链接场景
link context → 链接场景
Reference taxonomy → Reference 分类体系
explicit Reference evidence → 显式 Reference evidence
~~~

The Blincoe paragraph now states what was established, then the direction
boundary, then the conservative novelty position:

~~~text
Reference Coupling 研究为利用 cross-reference 识别项目间关联提供了软件工程领域依据。Blincoe 2015/2019 的经验工作以 Issue/PR/Commit comments 中指向其他 repository 的 Issue/PR 或 Commit references 为核心，已经建立 directed project-level graph，并以 project-pair cross-reference count 作为 edge weight，进而开展 ecosystem/community 或 dependency-oriented analysis [@blincoe2015ecosystems; @blincoe2019referencecoupling]。这里的方向仅表示 cross-reference direction，并不自动表示真实 technical dependency direction。本文承认 project-level aggregation、direction 和 count-weighting 已有先例，不把这些操作单独作为 novelty；本文的 RefQ 是对该类 direct project-reference relation 的 formalization/reframing，而不是替代或重新发明 Reference Coupling。
~~~

The IREL paragraph keeps URL/Num/SHA extraction, identity and rename
resolution, same-project deletion, and the different RefQ self-loop rule.  It
now explicitly states that IREL also does not define the observation contract:

~~~text
本文因此把 IREL 视为 reference extraction/identity-resolution precedent，而不是本文 quotient 或 self-loop contract 的来源，也不定义本文的 observation contract。
~~~

The two-universe paragraph remains the complete §2 boundary authority; only
the connective wording changed from “贡献” to “作用”.

### 4.3 §2.3

The mathematical paragraph was split to make the following order explicit:

1. Loukas, Sánchez-García, and Xiao provide coarsening/quotient vocabulary.
2. Normalized quotient and unnormalized compression are distinct.
3. The paper uses an unnormalized Reference block-sum formalization.
4. Contraction, membership-induced graph coarsening, and the weighted directed
   quotient network name different levels of the construction.

The preserved formula and qualification are:

~~~text
Sánchez-García 区分 normalized quotient \(Q(A)=\Lambda^{-1}S^\top A S\) 与 unnormalized compression \(B=S^\top A S\)。本文只把 characteristic-matrix aggregation 视为数学先例，并根据 Reference evidence multiplicity 采用 structurally analogous 的 unnormalized Reference block-sum formalization \(Q=M^\top R_PM\)；这里的 \(Q\) 是本文定义的 RefQ 矩阵，不将其与文献中的 normalized quotient definition 写成完全相同。
~~~

The non-inheritance boundary remains explicit:

~~~text
本文的 partition 来源是 artifact-to-project semantic membership，而不是 symmetry、automorphism、equitable partition 或 spectral optimization；本文也不继承 quotient literature 的 spectral preservation、lossless-compression 或 Loukas locality guarantees。
~~~

The Kessler and projection paragraph now says directly that the paper does
not construct the second-order projections \(QQ^\top\), \(Q^\top Q\), or
\(K=X\Phi X^\top\).  The first-order direct RefQ distinction, shared-neighbor,
shared-reference, and co-citation exclusions remain.

### 4.4 §2.4

Mixed-language phrases were made publication-facing:

~~~text
DBMS extensibility/adoption → DBMS 可扩展性/采用情境
Reference contexts → 引用场景
testable motivation → 可检验动机
RefQ differences → RefQ 差异
bounded comparison → 受约束比较
entity types → 实体类型
~~~

The DBMS references, multi-database-model motivation, source/schema evolution,
and the statement that prior studies do not already prove RefQ differences
remain.  The final paragraph now closes the setting without redefining the
core gap:

~~~text
因此，开源 DBMS 在本文中仅作为受约束的经验场景：其协作数据和技术语境足以支持对 Project-level RefQN 结构线索及解释边界的观察。
~~~

### 4.5 §2.5

The former recap:

~~~text
综上，已有研究建立了重要的 empirical and mathematical precedents，但它们服务于不同的 abstraction goals。经验先例方面，Blincoe 2015/2019 关注 cross-reference 驱动的 directed/count-weighted project-level ecosystem analysis，IREL 关注 project-reference identification 与 identity resolution [@blincoe2015ecosystems; @blincoe2019referencecoupling; @liu2022irel]。数学先例方面，Loukas、Sánchez-García 和 Xiao 分别提供 graph coarsening/contraction、quotient-network aggregation 与 network-quotient background [@loukas2019graphreduction] [@sanchezgarcia2020quotientnetwork] [@xiao2008networkquotients]。本文的增量不是声称这些先例不存在，而是把 heterogeneous fine-grained Reference evidence 提升为 semantic membership partition 下的 traceable project-level RefQ，并同时报告 observation and interpretation boundaries。后续更强语义的 task-level relation analyses 仅作为关系资产接口与未来扩展方向，不构成本文的核心贡献。
~~~

is replaced by the concise synthesis:

~~~text
综上，相关工作提供三类基础：Blincoe 2015/2019 建立了直接 cross-project Reference 的 directed、count-weighted project-level network 经验先例，IREL 提供 Reference extraction 与 project-identity/rename-resolution 先例；graph coarsening、contraction 与 quotient-network 文献提供 many-to-one mapping、partition 和 block aggregation 的数学词汇 [@blincoe2015ecosystems; @blincoe2019referencecoupling; @liu2022irel; @loukas2019graphreduction; @sanchezgarcia2020quotientnetwork; @xiao2008networkquotients]。这些先例分别处理经验网络、身份识别或数学聚合；本文关注的 implicit-to-explicit formalization gap，是将 heterogeneous fine-grained Reference evidence 的 endpoint eligibility、semantic membership、aggregation、non-project/self-loop policy、seed-centered source-observation completeness 与 interpretation boundaries 组织为统一、可追溯的 first-order project-level RefQ construction-and-observation contract。该定位不否认既有 project-level edges；second-order/shared-reference/task-level relations 不属于本文核心。
~~~

This is an implicit-to-explicit formalization gap, not a claim that prior work
did nothing and not a generic-algorithm novelty claim.

## 5. Precedent and boundary closure

~~~text
DIRECT_REFERENCE_PRECEDENT = PASS
EXTRACTION_IDENTITY_PRECEDENT = PASS
MATHEMATICAL_PRECEDENT = PASS
FIRST_ORDER_BOUNDARY = PASS
EXPLICIT_CONTRACT_GAP = PASS

BLINCOE_ATTRIBUTION = PASS
IREL_ATTRIBUTION = PASS
QUOTIENT_LITERATURE_ATTRIBUTION = PASS
KESSLER_BOUNDARY = PASS

IMPLICIT_TO_EXPLICIT_GAP = PASS
PRIOR_WORK_ERASURE = 0
NOVELTY_STRENGTHENING = 0
~~~

The §2 citation multiset is unchanged: 28 occurrences over 22 unique keys.
The full-manuscript multiset is also unchanged: 68 occurrences over 31 unique
keys.  The ten authorities that occur only in Related Work remain present,
including the social-technical, platform-link, discussion-link, code-review,
ecosystem, and Kessler citations.

~~~text
CITATION_OCCURRENCES_BEFORE = 28
CITATION_OCCURRENCES_AFTER = 28
CITATION_UNIQUE_KEYS_BEFORE = 22
CITATION_UNIQUE_KEYS_AFTER = 22
CITATION_SET_CHANGED = 0
~~~

## 6. Redundancy and mixed-language audit

Diagnostic counts within the §2 slice:

| Concept or phrase | Before | After | Classification after |
|---|---:|---:|---|
| formalization/reframing | 1 | 1 | RELATED_WORK_AUTHORITY (§2.2 full statement) |
| directed project-level graph | 1 | 1 | RELATED_WORK_AUTHORITY (§2.2) |
| project-level aggregation | 1 | 1 | RELATED_WORK_AUTHORITY (§2.2) |
| two-universe | 1 | 1 | NECESSARY_LOCAL_BOUNDARY (§2.2) |
| explicit second-order wording | 0 | 1 | NECESSARY_LOCAL_BOUNDARY (§2.5 compact closure; full formulas remain §2.3) |
| QQ superscript projection expression | 1 | 1 | NECESSARY_LOCAL_BOUNDARY (§2.3) |
| empirical and mathematical precedents | 1 | 0 | TRUE_DUPLICATE removed |
| abstraction goals | 1 | 0 | TRUE_DUPLICATE / working-note wording removed |
| testable motivation | 1 | 0 | TRUE_DUPLICATE / working-note wording removed |
| bounded comparison | 1 | 0 | TRUE_DUPLICATE / mixed-language wording removed |

The formalization/reframing statement is retained once in §2.2, while §2.5
uses the distinct implicit-to-explicit gap formulation.  Repeated technical
terms in §2.3 and §2.5 are local authority/boundary reminders rather than
duplicate claims.  No identical paragraph occurs twice after the edit:

~~~text
TRUE_DUPLICATE_AFTER = 0
NECESSARY_LOCAL_BOUNDARY = retained
RELATED_WORK_AUTHORITY = retained
~~~

## 7. Byte, citation, numeric, and scope guards

The §2 slice is delimited from the heading ## 2 相关工作 through the byte
before ## 3 研究方法.  Its before/after sizes are 10,712 and 10,794 UTF-8
bytes.  The prefix before §2 and suffix from §3 onward are byte-identical:

~~~text
RELATED_WORK_CHANGED = 1
RELATED_WORK_BYTES_BEFORE = 10712
RELATED_WORK_BYTES_AFTER = 10794
NON_RELATED_WORK_PROSE_CHANGED = 0
NON_RELATED_WORK_REMAINDER_UTF8_BYTES = 110470
NON_RELATED_WORK_REMAINDER_SHA256_BEFORE = 8476732620834415ED7493C2B9997EFB2D5C240762AE9D01ED255783B1D8A798
NON_RELATED_WORK_REMAINDER_SHA256_AFTER = 8476732620834415ED7493C2B9997EFB2D5C240762AE9D01ED255783B1D8A798
~~~

All five authorized subsection slices changed and no other heading slice
changed.  The complete manuscript checks are:

~~~text
ABSTRACT_CHANGED = 0
INTRODUCTION_CHANGED = 0
METHODS_CHANGED = 0
RESULTS_CHANGED = 0
DISCUSSION_CHANGED = 0
THREATS_CHANGED = 0
AVAILABILITY_CHANGED = 0
CONCLUSION_CHANGED = 0
APPENDIX_CHANGED = 0
RQ_TEXT_CHANGED = 0
FIGURE_CAPTION_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
~~~

The complete manuscript numeric-token multiset remains 991 before and after.
The citation multiset remains 68 occurrences over 31 unique keys.  The five
RQ lines, four figure captions, and 126 table rows are byte-identical.

## 8. Layer and semantic guards

~~~text
FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO

TWO_UNIVERSE_BOUNDARY = PASS
IREL_SELF_LOOP_DISTINCTION = PASS
NORMALIZED_UNNORMALIZED_DISTINCTION = PASS
REFQ_BLOCK_SUM_FORMALIZATION = PASS
SPECTRAL_EQUITABLE_SYMMETRY_GUARANTEES_NOT_INHERITED = PASS
LOUKAS_LOCALITY_NOT_INHERITED = PASS
SECOND_ORDER_PROJECTION_EXCLUDED = PASS
DBMS_AS_BOUNDED_SETTING = PASS
RQ3_AS_TESTABLE_COMPARISON = PASS
~~~

No task-level semantics, controlled-access functionality, causal knowledge
flow, or dependency ground truth is attributed to RefQ.

## 9. Scientific execution guards

~~~text
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
~~~

No scientific pipeline, output regeneration, figure rendering, or new
literature search was performed.

## 10. Final status

~~~text
repository_HEAD_before = b3dcd1264bd47ba6cac433b82a8ac2b08b43008c
remote_HEAD_before = b3dcd1264bd47ba6cac433b82a8ac2b08b43008c
manuscript_SHA_before = 05232481C69BAAAE468F636D443D928D4162CE4864A72B796F2AC5603E5CC5B4
manuscript_SHA_after = 53F30E4406BD0195AD097A1C425F3B5EC8A19048B5C1BADC429F6B673425901B
audit_record = docs/freeze/ch5_refq_submission_edit_batch_b_related_work.md
commit_message = docs(ch5): record related work submission edit
commit_hash = reported from final repository HEAD after this docs-only commit
push_status = reported after remote verification
~~~

Final decision:

CH5_REFQ_SUBMISSION_EDIT_BATCH_B_RELATED_WORK_PASS
