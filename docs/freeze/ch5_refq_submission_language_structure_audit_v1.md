# Chapter 5 RefQ — Submission-Oriented Language and Structure Audit V1

## Decision

CH5_REFQ_SUBMISSION_LANGUAGE_STRUCTURE_AUDIT_PASS_WITH_EDIT_PLAN

This is an audit-only record. The authoritative manuscript was read at the
frozen post-caption-polish SHA and was not edited. The proposed actions below
are bounded directions for later, human-reviewed batches; they are not executed
rewrites.

## 1. Starting identity and protected state

| Item | Value |
|---|---|
| Repository | D:/github_repo/OSDB_RefQ |
| Branch | ch5-refq-repository-identity-correction-v1 |
| repository_HEAD_before | 56aa72bf3f18f99078f1acdd0d07ea40d6387889 |
| remote_HEAD_before | 56aa72bf3f18f99078f1acdd0d07ea40d6387889 |
| Authoritative manuscript | C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md |
| Manuscript SHA before audit | 1EE57A3FCA1B8FDCC66B9FD2C45B9E6C696AE304F582FF64A82F235C64B9A7D7 |
| Manuscript SHA after audit | 1EE57A3FCA1B8FDCC66B9FD2C45B9E6C696AE304F582FF64A82F235C64B9A7D7 |
| Accepted captions | Frozen Figure 1–4 captions; no caption recommendations |
| Scientific/publication decisions | CH5_REFQ_THREE_WAY_RECONCILIATION_PASS; P0V3_FIGURE_RENDER_FINAL_ACCEPTED; CH5_REFQ_FINAL_FIGURE_CAPTION_COMPOSITION_PASS; CH5_REFQ_FINAL_CAPTION_EDITORIAL_POLISH_PASS |

Required frozen meanings were not reopened: the two evidence universes,
294 source-complete seeds versus source-incomplete expanded targets,
Q = M^T R_P M as the paper-defined first-order RefQ relation, the
direction-ignored first-order U(G_RefQ) view, the exclusion of second-order
projections from the main experiment, RQ2 typical/max separation and observed
concentration, RQ3 label-mode sensitivity with cross-mode robust feature count
zero, the cross-sectional 2023 project-age design, and the
formalization/reframing novelty boundary.

## 2. Audit methodology

The full 867-line authoritative Markdown manuscript was inspected section by
section. Repetition was judged by semantic function rather than string counts.
Local qualifiers were retained in the audit whenever removing them could blur
record versus entity units, source versus target observation, first-order versus
second-order construction, descriptive versus inferential evidence, or current
versus future-work scope.

Quantitative style diagnostics used this reproducible heuristic:

1. A paragraph is a contiguous non-empty prose block.
2. Headings, list items, Markdown table rows, fenced code, and display-math
   blocks are excluded from paragraph construction.
3. Sentences are split at Chinese terminal punctuation and at terminal
   English punctuation followed by whitespace and an uppercase letter or digit.
4. VERY_LONG_SENTENCE means more than 240 characters after the paragraph
   join; this threshold is diagnostic, not an editing rule.

Under that heuristic (including the four frozen caption blocks):

    TOTAL_PARAGRAPHS = 210
    TOTAL_SENTENCES = 580
    VERY_LONG_SENTENCE_COUNT = 32

For context, excluding the four caption blocks gives 206 paragraphs, 567
sentences, and 27 very-long sentences. The captions are protected and are not
editing targets in this audit.

Approximate manuscript-facing phrase counts (diagnostic only):

| Phrase | Count |
|---|---:|
| 本文不 | 11 |
| 不表示 | 13 |
| 不等同 | 8 |
| 不自动 | 5 |
| 仅 | 37 |
| 只 | 49 |
| 边界 | 50 |
| 口径 | 43 |
| 因此 | 38 |
| 需要强调 | 2 |
| 需要说明 | 1 |

High counts do not by themselves justify deletion: many occurrences are
scientifically necessary local guards.

## 3. Section-by-section assessment

### Abstract

The abstract is information-dense (2,944 characters; 17 Chinese terminal
sentences under the diagnostic punctuation rule). It successfully exposes the
two-universe model, the source-admission flow, the Project-level RefQN scale,
the bounded RQ findings, and the four-part contribution. The main
submission-quality issue is density: implementation and boundary detail is
close to the level of a methods synopsis, while the empirical take-away is
compressed into long compound sentences. A later abstract batch may shorten
process nouns and retain only the minimum numeric chain and interpretation
limits. Frozen numbers and the formalization/reframing boundary must remain.

### Introduction

Sections 1.1–1.4 move from DBMS motivation to prior constructs, gap, RQs, and
contributions, but the same motivation and novelty disclaimer recurs in 1.2,
1.3, and 1.4. The adjacent transitions at lines 47 and 49 both begin with
“因此”; the first states that the problem is not merely group-by, and the
second states the paper goal. The meaning is coherent, but the transition can
be made more publication-like in a later batch.

The phrase “academic problem 不只是对记录进行 group-by” is conversational and
implementation-oriented. It is a P2 language/structure candidate; a later
direction is “研究问题不只是记录的简单分组统计”, while retaining the
construction-contract point. No edit is made here.

### Related Work

Sections 2.2–2.5 correctly separate direct project-reference precedent,
extraction/identity precedent, graph quotient/coarsening precedent, and
second-order projection boundaries. However, the direct-reference
formalization/reframing disclaimer and the two-universe distinction are
restated in 2.2, 2.3, and 2.5. A bounded consolidation can state each
attribution and novelty boundary fully once, then use short cross-references.
The bibliographic-coupling, QQ^T, Q^TQ, and K = X Phi X^T exclusions are
semantically important and should remain at least once in Related Work and
once at the relevant method/result boundary.

### Methods

The opening scope paragraphs (§3, lines 99–103), §3.1.1, the data-scope table
in §3.2.3, and §3.4.4 all restate the evidence universes, node/edge counts,
and observation boundary. This is understandable for navigability, but the
full numeric chain need not be repeated at every level. The method risk is
high because shortening the wrong occurrence could merge scanned records,
admitted records, quotient-eligible records, nodes, edges, or weights.

The seven-step GH_CoRE process in §3.1.3 overlaps the six-step extraction
pipeline in §3.2.2. A later batch should make §3.1.3 a short processing-chain
overview and leave operational matching/validation detail in §3.2.2.
Membership and quotient definitions in §3.4 are the full authority and should
not be replaced by a cross-reference alone.

### Results

Results remain evidence-first and preserve the required source/target and
record/weight/edge distinctions. The main style opportunities are
paragraphs that restate complete table content immediately after the table,
the five-RQ roadmap in line 374, and repeated RQ3 feature lists. Local
qualifiers about source incompleteness, cross-sectional age, and
descriptive-versus-FDR interpretation are necessary and should remain.

### Discussion

The four discussion subsections have distinguishable intended functions:
§5.1 interprets findings, §5.2 positions the contribution against prior work,
§5.3 gives practical implications, and §5.4 provides compact RQ synthesis and
boundaries. The main duplication is between §5.4 and §9, not a reason to
remove §5.4 automatically. A later batch should preserve §5.4 as the
structured synthesis and make the conclusion shorter and more take-away
oriented. §5.3 repeats “分析线索” and related boundary language across three
paragraphs and can be compressed while retaining its distinct audiences.

### Threats to Validity

Construct, Internal, External, Conclusion, and Reliability validity are all
present and should be preserved as five dimensions. The opening sentence at
line 695 (“以下讨论不削弱本文结果的经验价值……”) is understandable but
slightly reviewer-response-like; it can be made more direct later without
removing the scope limitation.

Internal-validity process controls overlap with §3.1.3/§3.2.2, while
Reliability overlaps with §7 and Appendix A. The overlap is a consolidation
opportunity, not a scientific defect.

### Data/Code Availability

The section is factual about data sensitivity but not yet submission-final in
readiness. It moves among “正在整理”, “拟整理”, “将在投稿前统一确认”,
“最终归档……将在……提供”, and “仍建议提供”. These are different author
action states and should be harmonized in a later human-reviewed statement.
No archive URL or release commitment should be invented.

### Conclusion

The conclusion gives a clear RQ1–RQ3 take-away, restates the
formalization/reframing contribution, preserves the weak-semantic boundary,
and explicitly keeps second-order projections as future work. It substantially
duplicates §5.4 and repeats some Introduction/§5.2 positioning. A later
conclusion batch should retain the final contribution and future-work
boundary, but reduce repeated metric inventories and disclaimers.

## 4. Results–Discussion–Conclusion matrix

| Finding | Abstract | Results | §5.1 | §5.4 | §9 conclusion | Assessment |
|---|---|---|---|---|---|---|
| RQ1 Reference composition | APPROPRIATELY_SUMMARIZES | Full evidence and tables | ADDS_INTERPRETATION | APPROPRIATELY_SUMMARIZES | REPEATS_RESULTS with final scope | Keep local evidence limits; shorten conclusion inventory |
| RQ2a source-role contrast | APPROPRIATELY_SUMMARIZES | Full quantiles, partitions, examples | ADDS_INTERPRETATION | APPROPRIATELY_SUMMARIZES | REPEATS_RESULTS | Keep source-complete seed qualifier |
| RQ2b target concentration | APPROPRIATELY_SUMMARIZES | Full target counts, shares, denominator | ADDS_INTERPRETATION | APPROPRIATELY_SUMMARIZES | REPEATS_RESULTS | Keep denominator and coverage semantics |
| RQ2c algorithmic structure | APPROPRIATELY_SUMMARIZES | Full undirected/LCC/Louvain evidence | ADDS_INTERPRETATION | APPROPRIATELY_SUMMARIZES | REPEATS_RESULTS | Keep algorithmic/non-semantic boundary |
| RQ3 label-mode sensitivity | APPROPRIATELY_SUMMARIZES | Full descriptive and FDR results | ADDS_INTERPRETATION | APPROPRIATELY_SUMMARIZES | REPEATS_RESULTS | Keep cross-mode robust count zero |
| Methodological contribution | APPROPRIATELY_SUMMARIZES | Construction contract in Methods | ADDS_INTERPRETATION | APPROPRIATELY_SUMMARIZES | REPEATS_RESULTS and Introduction positioning | Keep formalization/reframing boundary; consolidate wording |

§5.4 has a valid compact-synthesis role. The strongest duplication is the
combination of §5.4 bullets with the first two conclusion paragraphs, not a
need to delete either section wholesale.

## 5. Mixed-language taxonomy

| Candidate | Locations | Classification | Direction |
|---|---|---|---|
| Reference, RefQ/RefQN, source/target, in-degree/out-degree, in-strength/out-strength, FDR, Louvain | Throughout | KEEP_TECHNICAL_TERM | Define once and retain as controlled technical vocabulary |
| graph coarsening, quotient, membership, project-mappable | §§1–4 | KEEP_TECHNICAL_TERM | Keep because they name the formal construction; define once, standardize hyphenation |
| additional observable evidence | Abstract line 4 | CAN_TRANSLATE_TO_CHINESE | Prefer a concise Chinese equivalent after first definition |
| academic problem; group-by | §1.3 line 47 | WORKING-NOTE_STYLE | Translate to formal Chinese wording in BATCH_A |
| bounded methodological contribution | §2.5 and §5.2 | DEFINE_ONCE_THEN_STANDARDIZE | Retain the bounded contribution, but use one consistent Chinese/English form |
| local and label-mode sensitive | Abstract, §5, §9 | DEFINE_ONCE_THEN_STANDARDIZE | Retain label-mode sensitive as the controlled result label; avoid unnecessary variants |
| reusable interface; inference commitment | §§1.4, 2.3, 5.2 | CAN_TRANSLATE_TO_CHINESE | Translate explanatory prose while retaining the technical contract |
| testable motivation; abstraction goals | §§2.4–2.5 | CAN_TRANSLATE_TO_CHINESE | Replace working-note metaphors with publication-oriented Chinese |
| source behavior versus source-role | §§1–4 | INCONSISTENT_VARIANT only if conflated | Keep both when behavior is broad and role is metric-specific; standardize local definitions |
| comment reference density versus comment-reference density | §§3–4 | INCONSISTENT_VARIANT | Choose one hyphenation in a later terminology pass |
| current corrected top-five; robustness_alert=FALSE | §4.2c lines 588–600 | WORKING-NOTE_STYLE | Use publication-neutral result wording without internal correction labels |

Mathematical notation and graph-theoretic terms should not be translated merely
for cosmetic uniformity.

## 6. Proposed consolidation map

| Concept | Full-definition authority | Repeated locations | Local qualifier still required? | Recommended strategy |
|---|---|---|---|---|
| Two evidence universes | §3.4.1, lines 241–285 | Abstract; §§1.2–1.4; §2.2; §3.0/3.2.3; §4.1; §5; Appendix A | Yes, at RQ1 and RefQ transitions | KEEP_FULL_ONCE_SHORTEN_ELSEWHERE |
| Seed-centered observation asymmetry | §3.4.4, lines 358–370 | §§1.2–1.4; §3.1.1; §4.2; §5; §6; Appendix A | Yes, in RQ2 target interpretation | KEEP_FULL_ONCE_SHORTEN_ELSEWHERE |
| First-order RefQ versus projections | §2.3, lines 81–85 and §3.4.3 | §4.2c; §5.4; §9; Appendix A | Yes, at undirected-view and future-work boundaries | KEEP_FULL_ONCE_SHORTEN_ELSEWHERE |
| Not dependency/task/cause ground truth | §3.4.3, lines 313–319 | Abstract; RQ1; RQ2; §5; §6; §9 | Yes, where a stronger reading is likely | KEEP_LOCAL_ONE_CLAUSE_BOUNDARY |
| Formalization/reframing novelty | §2.5 line 95 and §5.2 | Abstract; §§1.2–1.4; §2.2–2.5; §5.2; §9 | Yes, in contribution and conclusion | KEEP_FULL_ONCE_SHORTEN_ELSEWHERE |
| RQ3 label-mode sensitivity | §3.3.3 and §4.3 | Abstract; §4.3; §5.1; §5.4; §9 | Yes, around inferential results | KEEP_FULL_ONCE_SHORTEN_ELSEWHERE |
| Louvain algorithmic partition limitation | §3.3.2 and §4.2c | §4.2c; §5.1; §5.4; §6; Appendix A | Yes, whenever communities are named | KEEP_LOCAL_ONE_CLAUSE_BOUNDARY |

## 7. No-edit issue table

Severity counts are based on the primary category assigned in this table:
P0 = 0, P1 = 7, P2 = 18, INFO = 5.

| ID | Section / location | Current fragment or pattern | Category | Diagnosis | Preserve semantics | Proposed later action | Severity |
|---|---|---|---|---|---|---|---|
| C01 | §§1.2–1.4, lines 26–60 | Motivation, gap, and novelty boundary recur | STRUCTURE | Introduction has overlapping positioning jobs | Keep direct-reference precedent and bounded novelty | Consolidate full gap in §1.3; shorten §1.4 lead-in | P1 |
| C02 | §3 opening/§3.1.1/§3.2.3/§3.4.4 | Same universe and node/edge counts restated | METHOD_REPETITION | Numeric scope is repeated at four levels | Keep scanned/admitted/eligible/node/edge distinctions | Full chain once; later cross-reference with local unit clause | P1 |
| C03 | §§3.1.3 and 3.2.2 | Seven-step and six-step processing descriptions overlap | METHOD_REPETITION | Overview and operational pipeline are not clearly separated | Keep GH_CoRE, validation, de-duplication, and membership controls | Make §3.1.3 overview; retain detail in §3.2.2 | P1 |
| C04 | §5.4 and §9, lines 685–749 | RQ synthesis appears in both sections | RESULT_DISCUSSION_DUPLICATION | Conclusion inventories §5.4 findings | Keep §5.4 as compact synthesis and §9 as final take-away | Cross-reference §5.4 and shorten conclusion | P1 |
| C05 | §6.5 and §7, lines 721–735 | “仍需整理/建议/拟/将在确认” | AVAILABILITY_WORDING | Readiness and author action states are mixed | Keep conditional privacy/licensing boundary | Human-review one factual staged availability statement | P1 |
| C06 | §1.4 line 60 | Four contributions in one 1,269-character sentence | SENTENCE_COMPLEXITY | Many conceptual units and semicolons | Preserve all four contribution boundaries | Split by contribution or use shorter parallel sentences | P1 |
| C07 | §5.2/§9, lines 669 and 745 | Long contribution/positioning sentences | SENTENCE_COMPLEXITY | Attribution, novelty, construction, and implication are nested | Preserve formalization/reframing and weak semantics | Separate prior-work positioning from current contract | P1 |
| C08 | Abstract/§2.2/§3/§4 | Two-universe distinction repeated | REDUNDANCY | Full definition and local reminders are not differentiated | Keep transition qualifiers | Full definition once; one-clause reminders elsewhere | P2 |
| C09 | Abstract, §4, §5, §6, §9 | Not dependency/task/cause disclaimers recur | REDUNDANCY | Necessary guards have high surface density | Keep when metric could be overread | Remove only true adjacent duplicates | P2 |
| C10 | §§1.2, 2.2–2.5, 5.2, 9 | Formalization/reframing disclaimer repeated | REDUNDANCY | Same novelty boundary appears in several roles | Keep attribution and no-new-algorithm claim | Full statement in Introduction/Related Work; compact later | P2 |
| C11 | Abstract, §3.3, §4.3, §5, §9 | RQ3 feature list and sensitivity conclusion repeated | REDUNDANCY | Full list appears more often than needed | Keep six include-mixed features and zero cross-mode robust features | Full list in Results; concise Abstract/Conclusion | P2 |
| C12 | §1.3 line 47 | “academic problem”; “group-by” | MIXED_LANGUAGE | Conversational/implementation-oriented phrasing | Keep the research-problem meaning | Translate to formal Chinese wording | P2 |
| C13 | §2.5 line 95 | “abstraction goals”, “empirical and mathematical precedents” | MIXED_LANGUAGE | English metaphor adds little precision | Keep precedent distinction | Define once or use Chinese equivalent | P2 |
| C14 | §2.4 line 90 | “testable motivation”, “bounded comparison” | MIXED_LANGUAGE | Working-note flavor | Keep bounded RQ3 motivation | Use publication-oriented wording | P2 |
| C15 | §3 line 99 and §3.1.3 | GH_CoRE expansion and naming vary | MIXED_LANGUAGE | Expansion appears once with formatting inconsistency | Keep GH_CoRE identity | Standardize expansion and spacing once | P2 |
| C16 | §3.1.1 line 114 | Sample, flow, topology, and upstream scope in one sentence | SENTENCE_COMPLEXITY | 538-character numeric chain is hard to scan | Keep all denominator and node distinctions | Split sample/flow from topology | P2 |
| C17 | §3.1.3 line 141 | Process, credibility, controls, and Appendix pointer in one paragraph | SENTENCE_COMPLEXITY | Multiple epistemic layers are nested | Keep controls and non-classifier statement | Separate process description from validity note | P2 |
| C18 | §3.4.1–3.4.2 lines 285/302 | Membership definition, exclusions, and graph-coarsening caveats | SENTENCE_COMPLEXITY | Long nested exception structure | Keep total/single-valued mapping and projection limits | Split definition from exclusion consequences | P2 |
| C19 | §4 opening line 374 | Five-RQ roadmap in one semicolon-heavy sentence | SENTENCE_COMPLEXITY | Orientation sentence carries too many roles | Keep RQ role separation | Use two or three roadmap sentences | P2 |
| C20 | §6 opening line 695 | “以下讨论不削弱本文结果的经验价值……” | DEFENSIVE_PROSE | Slightly reviewer-response-like | Keep validity scope | Use direct validity-section transition | P2 |
| C21 | §§6.2/6.5 lines 707/721 | “需要说明” and advice-like package language | DEFENSIVE_PROSE | Reads partly as audit/reviewer response | Keep process-vs-model distinction and reproducibility need | Reframe as factual method/author action statements | P2 |
| C22 | §5.3 lines 679–683 | Three paragraphs repeat “分析线索” and boundaries | RESULT_DISCUSSION_DUPLICATION | Practical implications are partially redundant | Keep distinct maintainer/tool/researcher uses | Merge repeated closing qualifier | P2 |
| C23 | §6.5 line 723 and Appendix A line 739 | Reproducibility metadata list repeated | VALIDITY_REPETITION | Reliability and appendix point to same inventory | Keep reliability rationale | Cross-reference Appendix A rather than relist | P2 |
| C24 | §7 lines 723 and 735 | Protocol/data-script recommendation repeated | AVAILABILITY_WORDING | Same conditional recommendation appears twice | Keep privacy and access conditions | Consolidate in availability statement | P2 |
| C25 | §4.2c lines 588–600 | “当前 corrected top-five”, robustness flag | WORKING_NOTE_STYLE | Internal artifact wording in Results | Keep candidate-position weak semantics | Use publication-neutral result label | P2 |
| C26 | §4.1.2 lines 433–447 | Explicit skewness/kurtosis for RQ1 metric | NO_CHANGE_REQUIRED | Distributional claim is supported locally | Preserve RQ1 descriptive result | No edit recommended | INFO |
| C27 | §4.2a line 522 | No-fitting/no-power-law qualifier | NO_CHANGE_REQUIRED | Correctly bounds RQ2 interpretation | Preserve typical/max-only semantics | No edit recommended | INFO |
| C28 | §4.3 lines 631–655 | Label-mode sensitivity and no cross-mode robust feature | NO_CHANGE_REQUIRED | Central frozen statistical boundary | Preserve exactly | No edit recommended | INFO |
| C29 | §6 lines 693–723 | Five validity dimensions | NO_CHANGE_REQUIRED | Functional validity structure is complete | Preserve all five dimensions | Consolidate only duplicated details | INFO |
| C30 | Figure captions lines 381/505/573/606 | Accepted final captions | NO_CHANGE_REQUIRED | Captions are frozen publication authority | Preserve all figure semantics | FIGURE_CAPTION_EDIT_RECOMMENDATIONS = 0 | INFO |

Primary-category counts:

| Category | Count |
|---|---:|
| STRUCTURE | 1 |
| METHOD_REPETITION | 2 |
| RESULT_DISCUSSION_DUPLICATION | 2 |
| AVAILABILITY_WORDING | 2 |
| SENTENCE_COMPLEXITY | 6 |
| REDUNDANCY | 4 |
| MIXED_LANGUAGE | 4 |
| DEFENSIVE_PROSE | 2 |
| VALIDITY_REPETITION | 1 |
| WORKING_NOTE_STYLE | 1 |
| NO_CHANGE_REQUIRED | 5 |
| Total | 30 |

## 8. Highest-priority findings

1. C02: repeated numeric universe definitions in Methods; high semantic risk.
2. C03: overlapping GH_CoRE and extraction pipelines; high semantic risk.
3. C04: §5.4 and §9 repeat the same RQ synthesis.
4. C05: Data/Code Availability has mixed readiness and author-action states.
5. C01: Introduction repeats motivation and novelty positioning.
6. C06: the contribution sentence is 1,269 characters with multiple clauses.
7. C07: §5.2/§9 contribution positioning is structurally dense.
8. C11: RQ3 feature lists are repeated across abstract, results, discussion, and
   conclusion.
9. C22: §5.3 repeats practical-implication framing across adjacent paragraphs.
10. C23/C24: Reliability, Appendix A, and Availability repeat the same
    reproducibility inventory and advice.
11. C12: “academic problem/group-by” is not final publication language.
12. C25: “corrected top-five” is an internal artifact label in Results.

No P0 issue was found. None of these findings authorizes a scientific
reinterpretation or a manuscript edit in this task.

## 9. Recommended later editing batches

| Batch | Issue count | Highest severity | Semantic risk | Execution recommendation |
|---|---:|---|---|---|
| BATCH_A_INTRODUCTION | 4 | P1 | MEDIUM | Human review; consolidate gap/novelty and formalize academic-problem wording |
| BATCH_B_RELATED_WORK | 2 | P2 | MEDIUM | Human review; preserve attribution and projection exclusions |
| BATCH_C_METHODS | 5 | P1 | HIGH | Human review only; use a numeric/unit checklist before and after |
| BATCH_D_RESULTS | 4 | P2 | MEDIUM | Human review; preserve source/target and descriptive boundaries |
| BATCH_E_DISCUSSION_CONCLUSION | 4 | P1 | HIGH | Human review; retain §5.4 function and conclusion take-away |
| BATCH_F_VALIDITY_AVAILABILITY | 5 | P1 | HIGH | Human review; unify author-action states without inventing commitments |
| BATCH_G_TERMINOLOGY_LANGUAGE | 1 primary issue plus cross-batch terminology checks | P2 | LOW–MEDIUM | Human review; automatic global replacement is not authorized |

Batch counts cover candidate P1/P2 rows by primary section; INFO rows are
protected and are not editing targets. Batches must be executed separately,
with a manuscript SHA and scientific-token comparison after each batch.

## 10. Protected scientific and publication boundaries

- Observable fine-grained Reference evidence and quotient-eligible
  project-mappable records are different universes.
- The 294 seed projects are source-complete observations; expanded targets are
  not source-complete.
- RefQ is the paper-defined first-order relation Q = M^T R_P M and a
  formalization/reframing of direct project-reference aggregation, not a new
  generic graph algorithm.
- U(G_RefQ) is a direction-ignored first-order view, not bibliographic
  coupling, co-citation, shared-neighbor, QQ^T, Q^TQ, or K = X Phi X^T.
- RQ1 skewness wording is supported only where the explicit descriptive
  statistics are reported.
- RQ2 supports typical/max separation and observed concentration, not a fitted
  tail family or causal mechanism.
- RQ3 is label-mode sensitive; no feature is robust across both label modes.
- Project age is a cross-sectional 2023 attribute.
- Louvain communities are algorithmic partitions under the declared graph and
  modularity objective, not semantic DBMS taxonomy.
- The four final Figure 1–4 captions are frozen:
  FIGURE_CAPTION_EDIT_RECOMMENDATIONS = 0.

## 11. Guards

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
    manuscript_files_changed = 0
    figure_assets_changed = 0
    scientific_assets_changed = 0

No tests, experiment, scientific pipeline, figure rendering, or manuscript
write was performed. The only new repository artifact from this task is this
audit document.
