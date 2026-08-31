# Chapter 5 RefQ — Thesis-Framework-to-Paper Research Hierarchy Reconciliation Audit

## Decision

`CH5_REFQ_THESIS_FRAMEWORK_RECONCILIATION_PASS_RECONSTRUCT_HIERARCHY`

This is an audit-only record.  No authoritative manuscript, scientific output,
figure, table, code, configuration, manifest, receipt, or experiment was
modified or run.  The audit finds that the current paper contains the right
construct and boundary semantics, but neither the pre-Batch-A nor the
Batch-A §1.3 opening expresses the dissertation-level hierarchy explicitly
enough.  A later, separately authorized framework-derived hierarchy rewrite is
recommended.  Batch-A's local language edits are retained pending that
rewrite; they are not reverted in this task.

## 1. Starting identity and comparison material

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| `repository_HEAD_before` | `4d813578f438c999df2fe8ef822bf5f4070e764c` |
| `remote_HEAD_before` | `4d813578f438c999df2fe8ef822bf5f4070e764c` |
| Current authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Current manuscript SHA | `8D2C8F0A8E3D57B98F388D1B84E7AEAC3192A6D16B79BB087F6202D53420CB9B` |
| Comparison manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa.md` |
| Comparison manuscript SHA | `3FF5CB4EDD5833F2C8D65BD255D5FAA5A694F509067923A2F0B674A233D9B337` |
| Pre-Batch-A manuscript snapshot | `C:/Users/10651/AppData/Local/Temp/ch5_refq_batch_a_baseline_20260831.md` |
| Pre-Batch-A snapshot SHA | `1EE57A3FCA1B8FDCC66B9FD2C45B9E6C696AE304F582FF64A82F235C64B9A7D7` |
| Batch-A audit record | `docs/freeze/ch5_refq_submission_edit_batch_a_introduction.md` |
| Framework memo consulted | `.../docs/第五章Reference_Quotient小论文重构与博士论文融合备忘录_v1.1_change_report.md` (SHA `14F3F084E32465E8DD01FFB43CEFFCDE3E548F1E8969BAF2B1C895CE693279F6`) |
| Cross-chapter boundary record consulted | `.../docs/ch5_research_boundary_lock_v1.0.md` (SHA `3835A3CB0FC9FBE11A2A3F9AF046079542B37ED84BEF8947040110DD526BE5E4`) |
| Framework-to-layer prompt consulted | `.../temp_solution_discussion/Prompt_B_latest_Reference_Quotient_v1.1.md` (SHA `7C5A557BF74871A899EF15D03C2984DC467BDC074D0DF11178C8E8733B60A1B3`) |
| Current repository construct authority | `D:/github_repo/OSDB_RefQ/README.md` (RefQ chain, (Q=M^\top R_PM), seed-centered boundary, and projection exclusions) |

The four pre-existing untracked rendering ZIPs remain untracked and were not
staged:

- `figures/ch5_refq/p0v3_final_v3.zip`
- `figures/ch5_refq/p0v3_final_v4.zip`
- `figures/ch5_refq/p0v3_final_v5.zip`
- `figures/ch5_refq/p0v3_final_v6.zip`

The pre-Batch-A snapshot is a temporary read-only comparison copy made during
the earlier authorized Batch-A work; it is used here only to recover the old
§1.3 wording and its recorded SHA.  The comparison manuscript is not treated
as a newer conceptual authority merely because it has a different filename.

## 2. Authority hierarchy

The permanent conflict-resolution order for Chapter 5 is:

```text
L0 — doctoral research scenario and chapter task allocation
L1 — cross-chapter construct / relation-asset hierarchy
L2 — Chapter-5 theoretical scope and semantic boundary
L3 — paper core research problem and contribution hierarchy
L4 — RQ organization
L5 — frozen empirical outputs and their admissible claims
L6 — figure/table composition and presentation
L7 — local manuscript wording and style
```

The order is substantive, not a preference for older text or smaller diffs.
L5 results constrain what the paper may claim, but L5 does not redefine the
higher-level research problem simply because an experiment already exists.  If
L0–L4 and L5 appear to conflict, the conflict must be surfaced in an audit and
resolved explicitly; it must not be hidden by local prose editing.  L6 can
change presentation of an already supported result, and L7 can improve
wording, but neither can promote an empirical detail into the governing
research problem.

The repository README corroborates the L1–L2 construct authority: RefQ is the
current principal construct; the evidence-preserving chain is fine-grained
Reference evidence → artifact-to-project membership → membership-induced graph
coarsening → Project-level RefQN; (Q=M^\top R_PM) is the defining relation;
second-order projections are excluded; and the network is seed-centered rather
than a complete ecosystem graph (README lines 3–64).

The current state at the start of this audit is therefore recorded as:

```text
BATCH_A_LANGUAGE_EDIT = PASS
THESIS_FRAMEWORK_RECONCILIATION = PENDING
```

## 3. Dissertation architecture and Chapter-5 allocation

The governing relation-asset architecture is:

```text
Chapter 4 — FACT LAYER
fine-grained REFERENCES / Reference evidence

Chapter 5 — STRUCTURE LAYER
artifact-to-project membership
→ membership-induced graph coarsening
→ Reference Quotient
→ Project-level RefQN
→ PROJECT_REFERENCES_PROJECT materialization

Chapter 6 — TASK LAYER
strict Issue–PR RESOLVES candidate

Chapter 7 — ACCESS LAYER
controlled relation access / query
```

In standalone-paper language, Chapter 5's governing question is:

> 如何将可追溯的细粒度 Reference evidence 通过实体归属关系严格商化
> （quotient/coarse-graining）为可解释的项目级结构关系？

The paper must remain self-contained: it should not tell a reader that
“Chapter 4 does X” or “Chapter 6 does Y.”  It can, however, express the
resulting chain directly as fine-grained evidence → eligibility and semantic
membership → project-level structural relation → role/structure
characterization.  The current manuscript does contain this self-contained
chain in the abstract (lines 3–12), §1.2, §3.4, §5.1–§5.2, and §9.

The accepted cross-paper relation is complementary, not causal:

```text
project–project, weak-semantic structure/context relation asset (RefQ)
        ≠
PR–Issue, strict task-outcome relation asset (RESOLVES candidate)
```

No RefQ edge is evidence that knowledge was absorbed or that an Issue was
resolved.  The current manuscript repeatedly preserves this distinction (for
example §§1.2, 3.4.3, 5.1–5.2, 9, and Appendix A).

The consulted framework-to-layer prompt freezes the same sequence as “事实可
追溯 → 关系商化与结构可解释 → 任务结果可判定 → 分层关系可受控访问”
(lines 1118–1151), and explicitly states that the Chapter-5 and Chapter-6
assets differ in granularity and evidence strength rather than forming an
automatic causal pipeline (lines 1155–1181).  These statements are treated as
L0–L2 governance evidence, not as manuscript prose to be copied literally.

Historical dissertation drafts and legacy Chapter-5 prose were not allowed to
override the current RefQ theory and boundary records.  Where an older draft
uses stronger dependency, knowledge-transfer, or access-layer language, it is
treated as historical context requiring separate governance review, not as a
current authority for this paper.

## 4. Explicit §1.3/L39 comparison

### 4.1 Pre-Batch-A formulation

The pre-Batch-A snapshot (§1.3 opening, line 39) says in substance:

> 本文聚焦一个可实证检验的问题：细粒度 GitHub Reference evidence 如何在
> artifact-to-project membership 约束下被严格构造为项目级 RefQ relation，
> 以及这一 Project-level RefQN 在开源 DBMS 技术场景中呈现何种可观察模式
> 和解释边界。围绕这一问题，本文从领域适用性、关系构造透明度和观测角色
> 分离三个方面组织研究动机。

This version has an important advantage: it opens with the project-level
construction problem and then names the DBMS observations.  Its defect is that
the final sentence still presents domain applicability, construction
transparency, and observation-role separation as three parallel “motivation”
axes.  It does not identify construction as the core, observation as a
methodological constraint, and DBMS as the empirical instantiation.

### 4.2 Batch-A formulation

The current Batch-A wording (§1.3, line 39) is:

> 在上述概念定位基础上，本文将研究缺口具体化为三个方面：领域适用性、
> 关系构造透明度和观测角色分离。

This wording improved local flow and allowed the later gap → problem →
objective sequence, but it makes the flattening more explicit: the three items
are grammatically co-equal before the core construction problem appears at line
47.  Domain applicability is an empirical setting/evaluation layer, not a
peer-level replacement for the Chapter-5 structure-layer problem.  Observation
role separation is a constraint on interpretation of the seed-centered
experiment, not a separate construct of the same level as quotient
construction.

### 4.3 Judgment and selected option

| Option | Judgment | Reason |
|---|---|---|
| `KEEP_OLD` | Reject | Better opening emphasis, but still leaves the three axes co-equal and does not state the method-constraint tier. |
| `KEEP_BATCH_A` | Reject | Cleaner wording, but explicitly flattens the hierarchy and delays the core problem. |
| `HYBRID_REFRAME` | Useful implementation tactic | A future sentence can retain the old core opening and Batch-A's concise transitions, but the conceptual source of authority must be the thesis hierarchy. |
| `RECONSTRUCT_FROM_THESIS_FRAMEWORK` | **Selected** | Neither version explicitly separates core construction, observation constraint, and empirical instantiation. |

`L39_SELECTED_OPTION = RECONSTRUCT_FROM_THESIS_FRAMEWORK`.

The selected option is a conceptual recommendation only.  It does not
authorize an edit in this task.

## 5. Preferred core hierarchy

### 5.1 Core academic problem

```text
CORE_ACADEMIC_PROBLEM =
如何将可追溯的细粒度 Reference facts/evidence，在明确的 endpoint
eligibility、semantic membership、aggregation semantics、self-loop /
non-project policy、observation completeness 与 interpretation boundaries
下，严格商化（quotient/coarse-grain）为可解释的 project-level structural
relation / RefQ。
```

This is the Chapter-5 structure-layer question.  It determines what counts as
an admissible project-level edge and how that edge can be interpreted; it is
not merely a choice of grouping records.

### 5.2 Methodological / observational constraint

```text
METHOD_CONSTRAINT =
由于 source observation 以 seed-centered set 为边界，必须分离 source role、
target role 与 direction-ignored first-order structural views，并显式说明
expanded targets 的 source-incomplete 状态，以避免 sampling-induced
misinterpretation。
```

Observation completeness belongs in the construction-and-observation contract,
but its role in the hierarchy is subordinate to the core construct: it governs
how the resulting relation may be measured and read.

### 5.3 Empirical instantiation / evaluation

```text
EMPIRICAL_INSTANTIATION =
在 open-source DBMS vertical setting 中，刻画上述 relation asset 的
observable evidence composition、source/target role patterns、undirected
structural views，以及 bounded subdomain differences。
```

The DBMS setting is meaningful and scientifically necessary for this paper, but
it instantiates and evaluates the structure-layer relation; it does not define
the higher-level construct.

### 5.4 Recommended self-contained bridge (future wording only)

The following is a framework-derived wording direction, not an edit performed
here:

> 在上述概念定位基础上，本文首先关注一个核心构造问题：如何在明确
> endpoint eligibility、semantic membership、aggregation 与解释边界的
> construction contract 下，将可追溯的细粒度 Reference evidence 严格商化
> 为可解释的项目级结构关系。由于观测以 seed-centered source set 为边界，
> 还需分离 source role、target role 和 direction-ignored structural views；
> 在此基础上，本文以开源 DBMS 垂直生态作为经验实例，刻画该 relation
> asset 的 evidence composition 与结构模式。

This bridge is self-contained and does not mention dissertation chapter
numbers.  It preserves the current contract vocabulary and does not add a new
scientific claim.

## 6. Gap hierarchy audit

The three current §1.3 items should be reclassified as follows:

| Current item | Correct hierarchical role | Assessment | Later action |
|---|---|---|---|
| 领域适用性 | Empirical instantiation / evaluation context | Valid motivation, but not a co-equal core gap | Keep as why DBMS is a useful bounded setting; move after the core construct in the bridge. |
| 关系构造透明度 | Core academic problem / construction contract | Governing gap | Make endpoint eligibility, semantic membership, aggregation, self-loop/non-project policy, and interpretation explicit as the central gap. |
| 观测角色分离 | Methodological / observational constraint | Necessary constraint on the core relation's interpretation | Present after the core construct; retain source/target/view separation and expanded-target asymmetry. |

The two-universe model is not “just more entity types.”  It changes which
questions are answerable: the observable universe supports independent RQ1
composition findings, while only the quotient-eligible project-mappable subset
can form RefQ edges.  This is both a boundary-support contribution and an
independent empirical layer; it remains subordinate to, and constitutive of,
the core construction contract.

## 7. RQ hierarchy audit (no RQ wording edit)

The five frozen RQ formulations are retained byte-for-byte.  Their functional
hierarchy is not five co-equal contributions:

| RQ | Functional role | Relation to Chapter-5 structure task | Current evidence |
|---|---|---|---|
| RQ1 | Input evidence-universe and construct-boundary characterization | Supports the boundary of structural construction; does not redefine Chapter 5 as the FACT layer | §4.1 uses admitted source-observation records and retains non-project/internal evidence separately. |
| RQ2a | Core source-role structural characterization | Central empirical characterization of Project-level RefQN | §4.2a and Figure 2 source-role outputs. |
| RQ2b | Core target-role structural characterization | Central empirical characterization of Project-level RefQN | §4.2b target coverage/concentration outputs. |
| RQ2c | Core direction-ignored first-order structural characterization | Central empirical characterization of the derived undirected view | §4.2c, (U(G_{\mathrm{RefQ}})), LCC, and algorithmic modular view. |
| RQ3 | Bounded vertical-domain comparison | Evaluation/characterization of the relation asset in DBMS subdomains, not construct definition | §4.3 reports descriptive and label-mode-sensitive comparisons. |

The current RQ list is acceptable as a standalone list.  The later hierarchy
correction should be made in the lead-in, Results roadmap (§4, line 384),
§5.4 synthesis, and §9 conclusion rather than by changing the five question
texts.

## 8. Contribution hierarchy audit

The current four contributions should remain exactly four, but their relation
is hierarchical rather than merely parallel:

| Current contribution | Recommended role | Closure |
|---|---|---|
| 1. explicit relation formalization / construction contract | **Core methodological / construct contribution**: semantic membership quotient, endpoint eligibility, aggregation, and interpretation contract | Present in abstract, §1.4, §2.5, §3.4, §5.2, §9 |
| 2. boundary-aware evidence instantiation | **Boundary support**: two evidence universes, non-project/self-loop policy, membership resolution, and observation boundary; independently supports RQ1 | Present and explicitly not reduced to “more entity types” |
| 3. observation-aware role-aware empirical characterization | **Empirical validation**: RQ2a/b/c structural center, with RQ1/RQ3 contextual support | Present; later prose should name RQ2a/b/c as the center explicitly |
| 4. traceable weaker-semantic structural evidence layer | **Relation-asset positioning/interface**: provenance, weaker semantics, and future stronger-semantic validation boundary | Present; does not claim access-layer implementation or causal/task meaning |

This hierarchy does not increase novelty.  It makes the already accepted
semantics legible: contribution 1 defines the object, contribution 2 defines
its admissible evidence boundary, contribution 3 characterizes the resulting
object, and contribution 4 states how it may be reused without semantic
overreach.

## 9. Fact / structure / task / access leakage audit

| Leakage class | Finding | Evidence and interpretation |
|---|---|---|
| `FACT_LAYER_LEAKAGE` | `NO_MATERIAL_LEAKAGE` (watch only) | RQ1 and §4.1 characterize fine-grained evidence, but §3 and §3.4 explicitly distinguish it from the project-level quotient input; non-project evidence is retained for RQ1 and excluded from RefQN. A later hierarchy rewrite should call RQ1 a boundary/input characterization, not the Chapter-5 core. |
| `STRUCTURE_LAYER_DILUTION` | `PRESENT_BOUNDED` | §1.3 L39 names domain applicability, construction transparency, and observation-role separation as three co-equal gaps; §4 L384, §5.4 L697–701, and §9 L753 present RQ1/RQ2/RQ3 in broadly parallel narrative order. The construct and methods sections nevertheless preserve the structure layer, so this is dilution rather than loss. |
| `TASK_LAYER_LEAKAGE` | `NO` | §§1.2, 3.4.3, 5.1–5.2, 9, and Appendix A state that RefQ is not task resolution, knowledge transfer, dependency ground truth, causal influence, or `RESOLVES`. |
| `ACCESS_LAYER_LEAKAGE` | `NO` | No controlled query/access implementation is claimed as a Chapter-5 contribution; “interface” language is limited to a reusable evidence/relation boundary. No literal Chapter 7 dependency appears in the manuscript. |

No literal “Chapter 4/Chapter 6/in the dissertation framework” dependency was
found in the standalone manuscript.  The recommended correction therefore
adds hierarchy without importing dissertation chapter names into paper prose.

## 10. Whole-manuscript alignment matrix

| Location | Current implied core problem | Dissertation-layer alignment | Issue | Recommended hierarchy |
|---|---|---|---|---|
| Abstract, §§1–12 | Observable evidence is separated from eligible evidence, then aggregated to RefQ and empirically analyzed | Mostly aligned with STRUCTURE layer; DBMS is the setting | Opening/result inventory gives domain, evidence, structure, and RQ3 similar surface weight | Lead conceptually with evidence → eligibility/membership → RefQ; present DBMS as instantiation and RQ2 as structural center |
| §1.1 L19–23 | Why explicit Reference evidence is meaningful in DBMS ecosystems | Aligned as empirical motivation/context | Domain motivation is appropriately prominent within this subsection, but must not become the paper's core problem | Retain as motivation subordinate to construction question |
| §1.2 L26–36 | Prior direct-reference network, quotient vocabulary, RefQ first-order definition, two universes | Strong STRUCTURE-layer conceptual positioning | No material hierarchy defect; this is the conceptual authority | Keep full definitions here |
| §1.3 L39–49 | Three named gaps, followed by construction problem and DBMS objective | Partially aligned | L39 flattens core, method constraint, and empirical context | Reconstruct L39 bridge from thesis framework; keep Batch-A language cleanup around it |
| §1.4 L52–70 | RQs and four contributions presented after a concise DBMS lead-in | Partially aligned but semantically complete | Contribution hierarchy is implicit; final “five questions” sentence sounds flat | Add a hierarchy cue in a later authorized edit; do not alter RQ wording or count |
| §2.5 L105 | RefQ as the bounded increment over empirical and mathematical precedents | Strong STRUCTURE-layer alignment | Task-level analyses are correctly future/interface only | Keep as related-work closure |
| §3 opening L109–113 | Data sources, extraction, RefQN construction, metrics, and four numeric scopes | Mostly aligned; facts are inputs to structure construction | Data/scanning appears before the construction contract and can foreground FACT layer | In a later methods pass, introduce the construction objective before the scope inventory; no current edit |
| §3.4 L250–380 | Explicit project-mappable subset, total single-valued membership, block aggregation, (Q=M^\top R_PM), observation boundary | Strong STRUCTURE-layer authority | No material issue | Treat as the full construction authority |
| Results roadmap §4 L384 | Five RQs listed in sequence with RQ1, RQ2a/b/c, and RQ3 | Partially aligned | RQ1 and RQ3 can appear co-equal with the structure center despite local qualifiers | Label RQ1 as boundary/input, RQ2a/b/c as core structure, RQ3 as bounded evaluation in a future narrative edit |
| §5.1 L671–675 | Empirical meaning is organizing evidence into a bounded project relation | Strong alignment | RQ1 opens the discussion, which can slightly foreground facts | Lead with RefQ construction, then use RQ1 as boundary evidence |
| §5.2 L679–685 | Bounded formalization/reframing of direct project-reference aggregation | Strongest STRUCTURE-layer alignment | No material issue; explicit construction contract and weak semantics are clear | Preserve as contribution-positioning authority |
| §5.4 L697–701 | Parallel RQ synthesis and DBMS applicability | Partially aligned | Summary order and “适用性” wording may dilute the structure-layer center | Reorder synthesis emphasis: construct → RQ2 structural characterization → RQ1 boundary → RQ3 domain comparison |
| §9 L753–759 | Result inventory followed by formalization value and limitations | Mostly aligned, with bounded dilution | Conclusion starts with parallel RQ results before naming the governing structure problem | Open with the evidence-to-RefQ construction, then summarize RQ2 center and RQ1/RQ3 support; retain all limits |
| Appendix A / §6 | Reproducibility identity and semantic limits | Supports all layers without reallocating tasks | No material leakage | Keep as provenance and validity boundary |

## 11. Experiment-adjustability assessment

The research framework, not the current output layout, defines the problem.  The
frozen outputs already support all three tiers:

- RQ1 artifacts support the observable-versus-quotient-eligible boundary and
  independent evidence-composition findings.
- RQ2a, RQ2b, and RQ2c outputs support the core source-role, target-role, and
  first-order undirected structural characterization.
- RQ3 outputs support bounded DBMS subdomain evaluation, including its
  descriptive and label-mode-sensitive limits.

Therefore:

```text
EXPERIMENT_REFRAMING_NEEDED = YES
NEW_EXPERIMENT_NEEDED = NO
```

“Reframing” here means changing the explanatory hierarchy and roadmap, not
recomputing statistics or relabeling frozen outputs.  No existing output needs
to be discarded.  A future author may choose a low-cost narrative
reorganization; an additional scientific run is not justified by this audit.
If a later claim requires a new construct validation that the frozen outputs
cannot support, that would be a separately surfaced L0–L5 conflict, not an
implicit expansion of this task.

## 12. Preferred final Chapter-5 story

```text
Fine-grained Reference facts provide explicit, traceable evidence
        ↓
Not every observable reference can become a project-level relation
        ↓
Explicit endpoint eligibility + semantic membership are required
        ↓
Membership-induced block aggregation constructs Project-level RefQ
        ↓
Seed-centered observation requires source/target/view separation
        ↓
The resulting relation asset is empirically characterized in DBMS
        ↓
It remains weaker-semantic than strict task relations
```

```text
PREFERRED_CHAPTER5_STORY = ACCEPT_WITH_REVISION
```

The chain is substantively present in the current abstract, §1.2, §3.4,
§5.1–§5.2, and §9.  Revision is needed only to make the hierarchy explicit in
the §1.3 bridge and the later RQ roadmap/synthesis.  The story is not rejected:
it is the most faithful self-contained expression of the dissertation
structure-layer allocation.

## 13. Exact locations requiring later revision

No edits are authorized in this audit.  The following are bounded future
targets, in priority order:

1. **§1.3 L39** — replace the three-co-equal-gap bridge with a core
   construction problem, followed by the observation constraint and DBMS
   empirical instantiation.
2. **§1.3 L41–45** — retain the DBMS motivation, endpoint/membership gap, and
   source/target asymmetry, but label their tiers rather than presenting them
   as parallel top-level gaps.
3. **§1.4 L52** — add a self-contained hierarchy cue before the unchanged five
   RQs; do not edit RQ1/RQ2a/RQ2b/RQ2c/RQ3 wording in this audit.
4. **§1.4 L60–70** — retain four contributions and their semantics, while
   making contribution 1 core, 2 boundary support, 3 empirical validation,
   and 4 relation-asset/interface positioning.
5. **§4 L384** — revise only the narrative roadmap labels/order if authorized;
   frozen result numbers and views remain unchanged.
6. **§5.4 L697–701** — make RQ2a/b/c the structural center, with RQ1 as
   boundary evidence and RQ3 as bounded domain comparison.
7. **§9 L753–759** — open the conclusion with the evidence-to-RefQ
   construction and then summarize empirical tiers; retain all weak-semantic
   and second-order exclusions.

§1.2 L26–36, §2.5 L105, and §3.4 L250–380 are already suitable authority
anchors and should not be weakened during the future revision.

## 14. Batch-A disposition

```text
BATCH_A_STATUS = REVISE
```

The local Batch-A language edits are retained: they removed working-note
phrasing, reduced repeated transitions, preserved citations/numbers, and made
the contribution paragraph readable.  They should not be partially or fully
reverted.  The only required follow-up is a separately authorized,
framework-derived hierarchy correction, principally at §1.3 L39 and the
downstream roadmap/synthesis locations listed above.

This disposition explains why the final decision is not
`...KEEP_BATCH_A`: the current Batch-A opening is not yet the final authority
for the paper's research hierarchy.  It also explains why the decision is not
`...RESTORE_PRE_BATCH_A`: the old wording has the same unresolved flattening,
and restoring it would lose the accepted local language improvements.

## 15. Future conflict-resolution governance rule

For any future manuscript conflict, apply the following procedure:

1. Identify the conflict at the highest applicable level L0–L7.
2. State the governing dissertation scenario and chapter/task allocation
   before comparing prose variants.
3. Check cross-chapter relation-asset semantics and the Chapter-5 weak,
   project-level boundary.
4. Define the paper core problem and contribution hierarchy before choosing RQ
   order or experiment emphasis.
5. Use RQs and frozen outputs to test admissible claims, not to redefine the
   problem.  Record any L0–L4 versus L5 conflict explicitly.
6. Treat figures/tables as presentation of supported evidence and local style
   as the final tie-breaker only after the higher levels close.
7. If the conflict cannot be resolved without changing a higher-level
   authority, stop and mark the issue blocked rather than silently editing the
   manuscript.

This rule applies equally to future caption, result, discussion, conclusion,
and cross-chapter wording decisions.  A local fluency improvement or smaller
diff cannot override the relation-asset architecture.

## 16. No-edit and scientific guards

The audit performed read-only text inspection and hash/status checks only.

```text
manuscript_files_changed = 0
scientific_assets_changed = 0
figure_assets_changed = 0
tables_changed = 0
figures_rendered = 0
scientific_recomputation = 0
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
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
```

During this task the authoritative manuscript SHA remained
`8D2C8F0A8E3D57B98F388D1B84E7AEAC3192A6D16B79BB087F6202D53420CB9B`.  Before
the audit record was created, the repository had no tracked-file diff and the
four V3–V6 ZIPs were the only pre-existing untracked files.  Only this new
freeze document is authorized for the repository commit.

## 17. Final status fields

```text
L39_SELECTED_OPTION = RECONSTRUCT_FROM_THESIS_FRAMEWORK
CORE_HIERARCHY_CLOSURE = PASS
RQ_HIERARCHY_CLOSURE = PASS_WITH_NARRATIVE_REFRAME_REQUIRED
CONTRIBUTION_HIERARCHY_CLOSURE = PASS_WITH_NARRATIVE_REFRAME_REQUIRED
SELF_CONTAINED_PAPER_CHAIN = PASS
FACT_LAYER_LEAKAGE = NO (bounded RQ1 input/boundary support)
STRUCTURE_LAYER_DILUTION = YES (bounded presentation dilution)
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
PREFERRED_CHAPTER5_STORY = ACCEPT_WITH_REVISION
EXPERIMENT_REFRAMING_NEEDED = YES
NEW_EXPERIMENT_NEEDED = NO
BATCH_A_LANGUAGE_EDIT = PASS
BATCH_A_STATUS = REVISE
```

Final decision:

`CH5_REFQ_THESIS_FRAMEWORK_RECONCILIATION_PASS_RECONSTRUCT_HIERARCHY`
