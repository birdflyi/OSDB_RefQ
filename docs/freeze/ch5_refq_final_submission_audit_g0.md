# Chapter 5 RefQ — Final Submission Audit G0

## Decision

`CH5_REFQ_FINAL_SUBMISSION_AUDIT_G0_PASS_WITH_BOUNDED_EDIT_PLAN`

G0 is a read-only submission-readiness audit.  No manuscript, figure,
scientific output, manifest, receipt, or scientific code was changed.  The
audit found no P0 factual or scientific blocker.  It found a bounded set of
P1/P2 publication-language and structure improvements for a later,
human-reviewed G1 editing batch.

## 1. Starting identity and protected state

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| `repository_HEAD_before` | `695b7c4e18351066c2917d359b115d00573c2657` |
| `remote_HEAD_before` | `695b7c4e18351066c2917d359b115d00573c2657` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Manuscript SHA-256 before | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` |
| Manuscript SHA-256 after | `8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18` |
| Manuscript bytes / encoding | 117,132 bytes; UTF-8, LF-only, no BOM, final LF present |
| `MANUSCRIPT_CHANGED` | `0` |

The four pre-existing untracked archives remain outside the commit and were
not inspected or altered:

```text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
```

All previously frozen P0-v3 and supplemental artifacts, figures, manifests,
receipts, historical S7 object, and scientific code are treated as immutable.

## 2. Audit scope and method

The audit read the authoritative post-reconciliation manuscript section by
section and compared its claims with the repository's frozen P0-v3 and
supplemental `outputs_p0v3` contracts.  It checked terminology, section
structure, numeric identities, table/figure references, citation closure,
negative interpretation guards, and occurrences of internal workflow labels.

The governing hierarchy was respected throughout: doctoral framework, then
paper problem/contribution hierarchy, then RQs, frozen scientific outputs,
presentation, and only then local style.  No style recommendation weakens an
accepted scientific contract or introduces a new RQ, experiment, contribution,
or theoretical construct.

No P0, S1–S7, GH-CoRE, event-rejoin, second-order projection, statistical
recomputation, network rebuild, or figure rendering command was run.  Simple
arithmetic checks on already frozen values were allowed.

Readability counts below use a diagnostic heuristic: headings, list items,
tables, fenced code, and display math are excluded; sentence boundaries use
Chinese terminal punctuation and terminal English punctuation followed by
whitespace and an uppercase letter or digit; `VERY_LONG_SENTENCE` is more than
240 characters.  These counts identify editing surfaces only and are not
scientific measurements.

## 3. Scientific and numeric closure

The following frozen contracts remain explicit and internally coherent:

- observable fine-grained Reference evidence universe is distinct from the
  quotient-eligible, project-mappable subset;
- 294 source-complete analysis seeds are distinct from source-incomplete
  expanded target nodes;
- strict source admission, unique semantic membership, and
  `Q = M^T R_P M` define the first-order RefQ construction;
- each retained eligible Reference record contributes one weight unit;
- general RefQ preserves self-loops, while the cross-project view excludes
  them;
- `U(G_RefQ)` is a direction-ignored first-order view, not `QQ^T`, `Q^TQ`, or
  a shared-reference projection;
- RQ1 is evidence/boundary support, RQ2a/b/c are empirical structural
  characterizations, and RQ3 is bounded and label-mode sensitive.

Arithmetic closure of the frozen chains:

| Closure | Result |
|---|---|
| `3,748,078 - 120 = 3,747,958` | `PASS` |
| `1,586,047 + 1,686,729 + 475,182 = 3,747,958` | `PASS` |
| `1,447,073 + 138,974 = 1,586,047` | `PASS` |
| `9,884 - 289 = 9,595` | `PASS` |
| `418 + 9,177 = 9,595` | `PASS` |
| `7,630 + 131,344 = 138,974` | `PASS` |
| `6,505 + 1 = 6,506` | `PASS` |
| `6,476 + 30 = 6,506` | `PASS` |

Frozen profile and graph anchors cross-check as follows:

```text
candidate seeds = 301; analysis seeds = 294; activity gate = i_pr_rec_cnt >= 10
scanned records = 3,748,078; out-of-seed = 120; admitted = 3,747,958
project-mappable = 1,586,047; non-project = 1,686,729; unresolved = 475,182
ambiguous = 0; quotient-eligible = 1,586,047
self-loop weight = 1,447,073; cross-project weight = 138,974
directed edges (with self-loops) = 9,884; self-loops = 289; cross-project edges = 9,595
node domain = 6,506; edge-observed nodes = 6,505; zero-edge nodes = 1
undirected edges = 9,547; LCC = 6,367 nodes / 9,462 edges; components = 55; isolates = 30
canonical Louvain communities = 35; sensitivity = 32--37; ARI < 0.9 = 42/50
betweenness sample = 500; random seed = 20260731
```

The manuscript also consistently reports the complete-case age sample of 291
out of 294 seeds (3 missing, no imputation) and the 10 category rows in the
RQ2c category table.  These are distinct from the activity gate value 10 and
from graph edge/self-loop counts.

The WiredTiger row in `outputs/reference_quotient_p0_corrected_v3/
rq1_project_reference_profiles.csv` is the current authority:

```text
project_id = 2944302
total_reference_records = 15332
self_reference_records = 12891
external_project_reference_records = 19
non_project_reference_records = 1096
unresolved_target_reference_records = 1326
self_reference_ratio = 0.8407905035220454 (84.08% at two decimals)
```

The row closes exactly: `12,891 + 19 + 1,096 + 1,326 = 15,332` and
`12,891 / 15,332 = 0.8407905035220454`.  No manuscript claim was found that
contradicts these current values.

## 4. Internal-workflow label inventory

Exact repository/manuscript search counts (including Appendix A where present)
were:

| Literal / family | Count | Location and disposition |
|---|---:|---|
| `P0` | 17 | Methods operational labels and Appendix provenance; retain the underlying admission/multiplicity fact, translate publication-facing prose in G1 |
| `P0-v3` | 7 | Appendix A reproducibility identity; `KEEP_REPRODUCIBILITY_TERM` |
| `POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT` | 1 | §3.1.1; factual mapping snapshot, define or move exact identifier to Appendix in G1 |
| `reference_dedup_rule` | 1 | §3.2.2; exact multiplicity contract, retain identifier and explain in prose |
| `S4` | 1 | Appendix A status; reproducibility identifier |
| `S5` | 1 | Appendix A status; reproducibility identifier |
| `S7` | 1 | Appendix A fixed-object status; reproducibility identifier |
| `PASS` | 2 | Appendix audit statuses; field identifiers, not workflow instructions |
| `RELEASE_READY` | 1 | Appendix package status; factual provenance, not a new release promise |
| `robustness_alert` | 1 | Appendix reliability field; retain exact field and explain `FALSE` |
| `candidate gate` / `frozen evidence` / `frozen annotation` / `pipeline status` / `working note` | 0 | No bare publication-facing literal; the `i_pr_rec_cnt >= 10` gate and frozen-file facts are expressed as operational semantics |
| `stage` | 1 | Appendix package status; `KEEP_REPRODUCIBILITY_TERM` |
| `audit` | 4 | Appendix audit/provenance descriptions; `KEEP_REPRODUCIBILITY_TERM` |
| `guard` | 0 | No literal guard label; scope limits are expressed as ordinary scientific prose |
| `current corrected` | 0 | No stale correction label |

The labels in Appendix A are appropriate reproducibility metadata.  The few
Methods labels are not scientific errors, but are publication-voice candidates
for G1.  They must not be silently deleted because they encode real source
admission, deduplication, or mapping contracts.

## 5. Terminology and mixed-language assessment

Controlled technical vocabulary to retain and define once includes `Reference`,
`RefQ`/`RefQN`, `source`/`target`, `in-degree`/`out-degree`,
`in-strength`/`out-strength`, `FDR`, `Louvain`, `graph coarsening`, `quotient`,
`membership`, `project-mappable`, `GH_CoRE`, and `NetworkX`.  Field identifiers
such as `active_issue_pr_count`, `comment_per_issue`,
`comment_reference_density`, `external_reference_share`,
`non_project_reference_share`, `reference_dedup_rule`, and `i_pr_rec_cnt` must
remain exact when cited for reproducibility, with a Chinese semantic gloss.

Bounded language candidates (not G0 edits) are:

- translate explanatory phrases such as `additional observable evidence`,
  `paper-specific`, `bounded methodological contribution`, and `role-aware
  empirical characterization` after first definition;
- replace conversational `academic problem 不只是对记录进行 group-by` with
  formal Chinese while preserving the construction contract;
- standardize `source behavior` versus `source-role` and the hyphenation of
  `comment reference density`;
- make the §4.2b denominator sentence publication-like (the denominator is
  the cross-project RefQ total weight 138,974).
- render `current unit-weight operationalization`, `descriptive sample
  coverage`, and candidate-level `screen/identify/prioritize` as natural
  Chinese explanatory prose while retaining their exact metric semantics.

These are readability/terminology issues only.  No semantic boundary or metric
definition is changed by the proposed wording.

### Terminology consistency matrix

| Controlled concept | Current use | G0 classification | Guard for G1 |
|---|---|---|---|
| Reference Quotient / `RefQ` | construct and relation | `DEFINE_ONCE_THEN_KEEP` | Do not replace with a stronger semantic label |
| Reference Quotient Network / `RefQN` / Project-level RefQN | network representation | `DEFINE_ONCE_THEN_KEEP` | Preserve Project-level scope |
| Reference evidence / fine-grained Reference evidence | observation universe | `KEEP_TECHNICAL_TERM` | Keep record-unit meaning explicit |
| source role / source-role; target role / target-role | role-specific metrics | `DEFINE_ONCE_THEN_KEEP` | Hyphenation may be standardized locally |
| first-order structural view | `U(G_RefQ)` result | `KEEP_TECHNICAL_TERM` | Do not conflate with second-order projection |
| algorithmic community / modular neighborhood | Louvain output | `KEEP_TECHNICAL_TERM` | Never rewrite as semantic DBMS community |
| structural brokerage candidate | bounded graph position | `DEFINE_ONCE_THEN_KEEP` | Do not call it a knowledge broker |
| `active_issue_pr_count`, `comment_per_issue`, `i_pr_rec_cnt`, `reference_dedup_rule` | implementation fields/contracts | `FIELD_IDENTIFIER_DO_NOT_RENAME` | Add prose gloss; retain exact field in reproducibility context |

## 6. Abstract-only compression categories

The Abstract satisfies all seven required content functions.  The residual
issues are classified as follows:

| Category | Finding | Bounded action |
|---|---|---|
| `ABSTRACT_REDUNDANT_PROCESS_DETAIL` | GH-CoRE processing and boundary clauses approach Methods-level detail | Remove only repeated process nouns in the Abstract |
| `ABSTRACT_EXCESSIVE_NUMERIC_DETAIL` | The 3,748,078 → 3,747,958 → 1,586,047 chain is useful, but graph counts can be compacted | Keep source-admission and eligibility scale; compress secondary count listing |
| `ABSTRACT_MIXED_LANGUAGE_ISSUES` | English technical vocabulary is valid, but explanatory phrases are dense | Translate explanatory phrases after first definition; retain protected technical terms |
| `ABSTRACT_OVERLONG_SENTENCES` | Diagnostic maximum is ~754 characters; two sentences exceed 240 characters | Split or shorten locally; target approximately 10–20% compression |

No Abstract number, RQ, contribution, or weak-semantic guard is proposed for
deletion.

## 6. Section-by-section submission assessment

| Section | Diagnostic profile (paragraphs / sentences / >240 chars / max chars) | Assessment |
|---|---|---|
| Abstract | 6 / 18 / 2 / ~754 | Complete and accurate but dense; bounded 10–20% compression candidate |
| §1 Introduction | 21 / 55 / 7 / ~373 | Motivation, gap, RQs, and contributions are complete; motivation/novelty lead-in repeats |
| §2 Related Work | 15 / 50 / 6 / ~452 | Correctly separates direct-reference, identity, quotient/coarsening, and projection precedent; boundary reminders can be consolidated |
| §3 Methods | 72 / 113 / 16 / ~2,111 | Operationally complete; process overview and operational matching detail overlap; preserve record/entity/edge/weight and source/target distinctions |
| §4 Results | 81 / 118 / 20 / ~1,395 | Evidence-first and numerically closed; table restatement and RQ3 feature-list repetition are presentation candidates |
| §5 Discussion | 12 / 33 / 2 / ~295 | §5.4 provides valid structured RQ synthesis; shorten repetition with §9 only in G1 |
| §6 Validity | 10 / 30 / 1 / ~246 | Five validity dimensions and limits are present; reliability overlaps §7/Appendix but is factually sound |
| §7 Availability | 3 / 7 / 0 / ~163 | Conditional archive/release wording is accurate but should be harmonized before submission |
| §8 Supplement | 1 / 2 / 0 / ~181 | Correctly distinguishes provenance appendix from availability promise |
| §9 Conclusion | 4 / 9 / 1 / ~351 | Clear RQ1–RQ3 take-away and future-work boundary; repeats §5.4 and some positioning |
| Appendix A | reproducibility record (heuristic sentence count is not meaningful for lists) | Appropriate identity, audit, and semantic-boundary metadata |

Figure 1–4 captions occur once each and are already frozen.  Table 4.1–4.8
references are present and their reported partitions remain closed.  Heading
hierarchy §1–§9, Appendix A, and References is complete; existing §4.2.0 is
preserved and must not be renumbered as part of G1.

## 6B. Figure, table, heading, and equation closure

`Figure 1`–`Figure 4` each have one caption; captions already use the accepted
RefQ unit and algorithmic-community terminology.  `Table 4.1`–`Table 4.8`,
including the `4.6a`–`4.6f` sub-tables, are referenced in sequence and retain
their frozen values.  RQ1, RQ2a, RQ2b, RQ2c, and RQ3 labels are used
consistently across the Abstract, Results, Discussion, Conclusion, and
Appendix mapping.  The formal relation `Q = M^T R_P M` and the explicit
second-order exclusions are not contradicted by later prose.  No broken figure,
table, heading, equation, or Appendix reference was found.  This is a closure
check only; no asset was edited.

## 6C. Availability-state closure

The manuscript distinguishes the existing public relation/data release and
Zenodo DOI `10.5281/zenodo.18817348` from the internal supplemental package
marked `STAGE_PACKAGE_COMPLETE / RELEASE_READY`.  It also states that final
submission replication-package scope/version still requires reconciliation,
that raw GitHub user content is not unconditionally redistributed, and that a
full GH-CoRE code release is not implied by the DOI.  This state is factual and
non-blocking; G1 may harmonize wording but must not invent a release promise.

## 7. Results–discussion–conclusion consistency

The manuscript consistently assigns RQ1 to evidence composition and
construction boundary, RQ2a/b/c to source role, target coverage/concentration,
and first-order undirected structure, and RQ3 to bounded subdomain comparison.
The same qualifiers recur where interpretation could otherwise be overstated:
seed-centered observation, source-incomplete expanded targets,
descriptive/non-FDR-supported differences, cross-sectional 2023 project age,
and algorithmic (not semantic) Louvain communities.  Repetition is a bounded
editorial issue, not a contradiction.

## 8. Citation and reference closure

The manuscript contains 68 citation tokens, 31 unique citation keys, and 31
bibliography entries.  There are zero missing bibliography entries and zero
orphan bibliography entries.  Citation/reference closure is therefore
`PASS`.

## 9. Overclaim and negative-guard closure

No unsupported positive claim of power law, scale-free behavior, heavy tail,
dependency ground truth, task resolution, knowledge-flow causality, project
importance, collaboration quality, problem complexity, stable/semantic
communities, or a complete GitHub/OSS ecosystem was found.  These expressions
occur only in explicit negative or scope-limiting guards.  Therefore:

```text
OVERCLAIM = 0
NEGATIVE_GUARD = PRESENT
```

The linear Figure 2C presentation and algorithmic-community wording remain
consistent with the accepted visual contract; no figure re-rendering is
needed.

## 10. Compact issue inventory

Severity counts use one primary category per bounded issue:

```text
P0_COUNT   = 0
P1_COUNT   = 8
P2_COUNT   = 18
INFO_COUNT = 5
```

| ID | Section | Issue | Evidence | Recommended bounded action | Severity |
|---|---|---|---|---|---|
| P1-01 | Abstract | Density and mixed explanatory English | 6 paragraphs; 2 sentences >240 chars; max ~754 | Abstract-only 10–20% compression preserving seven content functions | P1 |
| P1-02 | §1.3–§1.4 | Motivation/gap/novelty lead-in repeats | same positioning job appears in adjacent subsections | Merge one lead-in; preserve RQs and hierarchy | P1 |
| P1-03 | §3.1.1 | Internal `P0`/snapshot labels are publication-facing | `P0`, `P0 gate`, `POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT` | Convert one paragraph to publication prose; keep exact ID in Appendix if needed | P1 |
| P1-04 | §3.2.2 | `reference_dedup_rule = none` is opaque without gloss | exact multiplicity contract is shown as a field assignment | Keep field identifier and add natural-language contract | P1 |
| P1-05 | §4.2b | Weight denominator sentence is awkward | `138,974` is correctly a cross-project total weight | Replace one sentence with publication wording; do not change value | P1 |
| P1-06 | §4 | Table narration/RQ3 feature lists repeat complete outputs | results restate frozen rows and feature names | Compress local prose; preserve all table values and statistical status | P1 |
| P1-07 | §6.2 and §6.5–§7 | Internal label and availability states need publication harmonization | `P0 Reference-record` and conditional release wording | Edit one sentence plus availability paragraphs; no new promise | P1 |
| P1-08 | §5.4/§9 | Structured synthesis and conclusion partly repeat | both summarize RQ1–RQ3 and novelty boundary | Keep §5.4; shorten §9 to final take-away | P1 |
| P2-01 | §§1–2 | Local boundary reminders are stylistically repetitive | two-universe/first-vs-second-order wording recurs | Consolidate only true redundancy; keep local qualifiers | P2 |
| P2-02 | §§1–6 | Mixed explanatory English and long sentences | technical vocabulary is valid, prose density varies | Local language polish, no terminology erasure | P2 |
| P2-03 | §5.3 | Candidate-level practical verbs are code-switching heavy | `screen/identify/prioritize` sequence | Translate one sentence | P2 |
| P2-04 | §§3–4 | Process overview and operational detail overlap | GH-CoRE and matching descriptions recur | Shorten overview, retain operational authority | P2 |
| P2-05 | §9 | Repeated result inventory | conclusion repeats some §5.4 metrics | Remove only duplicate inventory, keep take-away | P2 |

The five P2 rows above group 18 local style instances; they are not 18
separate edit requests.  INFO items are intentionally retained technical and
Appendix terms, accepted figure/table structure, and necessary local guards.

P1 issues are submission-facing but non-scientific: abstract density;
repeated motivation/novelty lead-in in §1.3–§1.4; internal workflow labels in
§3.1.1/§3.2.2 and one §6.2 phrase; Methods process-overview duplication;
Results table/feature-list repetition; §6.5/§7 availability-state
harmonization; and the awkward §4.2b weight-denominator sentence.  P2 issues
are local style, sentence-length, mixed-language, and bounded repetition
opportunities (18 total), while INFO items record protected technical terms,
intentional Appendix metadata, and accepted figure/table structure.  None
changes a number, population, operator, or interpretation boundary.

## 11. Minimal G1 edit plan

Any later G1 batch should be human-reviewed and limited to these surfaces:

1. Compress the Abstract by approximately 10–20%, retaining the problem/gap,
   RefQ construction, 294 seeds and the key evidence-flow numbers, RQ2
   typical/max separation, RQ3 label-mode sensitivity, four-part contribution,
   and weak-semantic boundary.
2. Consolidate duplicate motivation and novelty lead-ins in §§1.3–1.4 without
   changing the RQ or contribution hierarchy.
3. Keep §3.2.3 as numeric authority; shorten §3.1.1 to a process overview and
   retain operational matching/validation detail in §3.2.2.  Translate internal
   labels to publication prose while preserving exact field names in Appendix A.
4. Reduce repeated complete table prose and RQ3 feature lists in §4; retain
   label-mode-sensitive and cross-mode robust-feature-zero conclusions.
5. Keep §5.4 as structured RQ synthesis and compress §9 to a concise final
   take-away; retain all negative semantic guards and second-order future-work
   boundary.
6. Harmonize conditional availability/reproducibility wording in §§6.5–§8;
   do not invent an archive URL, release date, or code-publication promise.
7. Preserve all Figure 1–4 captions, tables, equations, references, and
   Appendix reproducibility identifiers during any subsequent edit.

## 12. Immutability and guard record

```text
MANUSCRIPT_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
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
OVERCLAIM = 0
```

Only this G0 document is authorized for the current commit.  The four V3–V6
ZIPs remain untracked and unstaged by design.

## 13. Final status

```text
repository_HEAD_before = 695b7c4e18351066c2917d359b115d00573c2657
manuscript_SHA_before = 8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18
manuscript_SHA_after  = 8BF9F6225FF160CFE661D30C9D2A7F9A1656A4BE34A0F244F70072957F526B18
P0_COUNT = 0
P1_COUNT = 8
P2_COUNT = 18
INFO_COUNT = 5
numeric_scientific_blockers = 0
citation_reference_closure = PASS
overclaim_closure = PASS
reconciliation_readiness = READY_WITH_BOUNDED_G1_EDIT_PLAN
```

The exact final decision for this audit is:

`CH5_REFQ_FINAL_SUBMISSION_AUDIT_G0_PASS_WITH_BOUNDED_EDIT_PLAN`
