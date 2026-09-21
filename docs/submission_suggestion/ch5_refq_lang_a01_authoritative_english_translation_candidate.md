# Chapter 5 RefQ LANG-A01 Authoritative English Translation Candidate

## Decision

`CH5_REFQ_LANG_A01_AUTHORITATIVE_ENGLISH_TRANSLATION_CANDIDATE_PASS_READY_FOR_LANG_A02`

This record documents a complete English translation candidate. It does not
promote an accepted English manuscript and does not replace the Chinese
CURRENT or MS-R04 snapshot.

## Authority and identity

| Item | Result |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Base repository HEAD | `6ab22dc317a83638385fef4842bfbe9b5d2cc8e1` |
| Remote branch HEAD before commit | `6ab22dc317a83638385fef4842bfbe9b5d2cc8e1` |
| Frozen Chinese source | `versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md` (external) |
| Chinese source SHA-256 | `F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549` |
| External CURRENT SHA-256 | `F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549` |
| English candidate identity | `EN-R01` |
| English candidate path | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/working/EN-R01_JSS_RESEARCH_PAPER_TRANSLATION_CANDIDATE.md` |
| English candidate SHA-256 | `9927C3FD73796A5B7D24E6B70957E923008921845A6BD0551934C0091720DBF2` |
| English candidate repository status | External working candidate; not promoted and not tracked |

The Chinese CURRENT and MS-R04 snapshot were read-only throughout this task.
No `CURRENT_EN`, `MS-R05`, `MS-R04-English`, or accepted English identity was
created.

## Target and requirement-debt boundary

The frozen target is the *Journal of Systems and Software*, Research Paper
track. The JSS target freeze and SUB-A02 mapping remain authoritative. The
translation candidate does not implement the outstanding JSS requirement debt:
word-limit adaptation, keyword reduction, review anonymization, template
conversion, reference-style conversion, title-page material, highlights,
graphical abstract, declarations, CRediT, cover letter, or submission
packaging. The frozen state remains `JSS_REQUIREMENTS_FULLY_VERIFIED = NO`
with `UNVERIFIED_JSS_REQUIREMENT_COUNT = 28`.

## Translation strategy

The complete 857-line Chinese source was translated into a separate EN-R01
working file. Markdown headings, tables, captions, code spans, citation
blocks, formulas, URLs, and numeric strings were protected during machine
translation and restored in place. The title, abstract, keywords, five RQs,
four contributions, the observation-boundary paragraph in §6.3, and the
conclusion were then checked against the frozen semantic source and corrected
to the accepted terminology. This is a translation candidate, not native
English editorial completion; sentence-level fluency and idiomatic technical
wording are explicit LANG-A02 review items.

## Title, abstract, and keywords

The title maps the frozen Chinese title to:

> From Artifact-Level References to Project-Level Reference Quotient Networks:
> An Empirical Study of the Open-Source DBMS Ecosystem

The candidate abstract preserves the paper centre, 294 source-complete seeds,
evidence composition, source/target roles, first-order direction-ignored
structure, Louvain seed sensitivity, and label-sensitive subdomain results.
It contains no citation tokens. Candidate abstract length is 160 English words;
the Chinese source abstract contains 297 Chinese characters.

The seven frozen keyword concepts are preserved as:

`open-source software ecosystem; open-source DBMS; explicit Reference evidence; Reference Quotient; Reference Quotient Network; graph coarsening; GitHub`

## Research-question parity

| Frozen RQ | English candidate mapping | Parity |
|---|---|---|
| RQ1 | Collaboration contexts, target object types, and internal/external Reference differentiation | Supported |
| RQ2a | Seed source activity range and aggregated strength; seed-to-seed versus seed-to-expanded relations | Supported |
| RQ2b | Multi-seed target coverage and concentration of aggregated strength | Supported |
| RQ2c | First-order direction-ignored connectivity, local clustering, modular neighborhood, and bridge-like structure | Supported |
| RQ3 | Label-controlled, multiple-testing-controlled, observation-bounded DBMS subdomain differences | Supported |

`RQ_COUNT = 5`; no RQ was added, removed, merged, or scientifically
redefined.

## Contribution parity

`CONTRIBUTION_COUNT = 4`; contribution order and semantic roles are preserved:

1. RefQ/RefQN construction contract with endpoint eligibility, membership,
   aggregation, and interpretation boundaries.
2. DBMS instantiation with the two evidence universes, non-project evidence,
   self-loops, membership resolution, and source/target asymmetry.
3. Role-aware source, target, and first-order structural measurement under
   asymmetric observation.
4. RefQ as a traceable, weak-semantic relation asset for screening and
   inspection, not dependency ground truth or causal knowledge flow.

## Section and display completeness

| Check | Chinese source | EN-R01 | Result |
|---|---:|---:|---|
| Source lines / candidate lines | 857 | 857 | PASS |
| Main-text table blocks | 14 | 14 | PASS |
| Figure captions | 4 | 4 | PASS |
| Heading count | 64 | 64 | PASS |
| References section | Present | Present | PASS |
| Appendix A | Present | Present | PASS |

All manuscript sections are represented: Title, Abstract, Introduction,
Related Work, Methods, Results, Discussion, Threats to Validity, Data and
Code Availability, Supplementary Material, Conclusion, Appendix A, and
References.

## Observation-contract parity

The candidate explicitly preserves the following frozen contract:

- 294 analysis seeds are source-complete under the current observation
  contract.
- Expanded targets enter because seed projects reference them and are
  source-incomplete, not independently source-sampled.
- Missing or unobserved expanded-target source behavior is not observed zero
  activity.
- RQ2a uses the source-complete seed population; RQ2b uses the observable
  target population; RQ2c uses the first-order direction-ignored structural
  view.
- Ignoring direction does not restore missing source observations or create a
  fully observed ecosystem graph.

## Numeric and formula audit

The protected frozen anchor set is present in EN-R01, including 301 candidate
projects, 294 seeds, 3,748,078 scanned records, 3,747,958 admitted records,
120 out-of-seed records, 1,586,047 quotient-eligible records, 1,686,729
non-project records, 475,182 unresolved records, 138,974 cross-project weight,
6,506 nodes, 9,884 directed edges, 289 self-loops, 9,595 directed
cross-project edges, 9,547 first-order undirected edges, 6,367 LCC nodes,
9,462 LCC edges, 35 canonical communities, 0.7969220043681785 modularity,
and the frozen RQ3 values and percentages. Core expressions including
`Q=M^T R_P M`, `QQ^T`, `Q^TQ`, `K=X Phi X^T`, and `eta_H^2` remain present.

The translation changes language surrounding numeric strings but introduces no
new scientific value. A strict token-by-token punctuation audit is deferred
to LANG-A02 because some numbers adjacent to translated words lose a spacing
boundary; the value strings and scientific anchors remain unchanged.

## Tables, figures, citations, and bibliography

- Table block count: unchanged at 14.
- Figure caption count: unchanged at 4.
- Figure assets: not read or modified.
- Citation groups: 38 before and 38 after.
- Citation-token occurrences: 70 before and 70 after.
- Unique citation keys: 33 before and 33 after.
- Bibliography entries: 33 before and 33 after.
- Abstract citation count: 0 before and 0 after.
- Missing citation keys: 0.
- Orphan bibliography entries: 0.
- Malformed citation syntax: 0 detected.

## Related Work positioning

The candidate retains complementary-critical positioning. Kalliamvakou et al.
is used for repository-data and interpretation pitfalls; McClean et al. is used
for variation in OSS SNA data sources and network construction; and Blincoe et
al. is retained as a dependency-oriented Reference Coupling precedent under
its own validated scope. None is attributed with RefQ role semantics. The
candidate contains no adversarial claim that prior work is wrong, subjective,
or invalid.

## RQ2 and RQ3 interpretation guards

RQ2 remains role-aware and observation-bounded: source activity, target
coverage, and the first-order structural view are not interchangeable, and
expanded-target low out-degree is not interpreted as project behavior. RQ3
retains the frozen result that `include_mixed` has selected features while
`exclude_mixed_or_multilabel` has none; no feature is robust across both label
modes. The candidate does not say that no subdomain differences exist and does
not convert Louvain communities into semantic DBMS communities.

## Threats and availability scope

The §6.3 observation/network-boundary paragraph is explicitly consolidated in
English. It defines the estimand boundary rather than apologizing for the
dataset. Data and Code Availability remains limited to the frozen public
archive scope and does not claim that a DOI automatically makes the full code
or all source content public.

## Paper A/B/C/D boundary

The candidate preserves the existing four-part paper decomposition used by the
Chinese source: (A) evidence composition and RQ1, (B) source/target role
measurements in RQ2a/RQ2b, (C) first-order structural inspection in RQ2c, and
(D) bounded DBMS subdomain comparison in RQ3. No new paper, contribution, or
platform claim was introduced.

## Residual CJK and claim-strength audit

Residual CJK code-point count in EN-R01: `0` across 857 lines. Technical
identifiers, repository names, citation keys, formulas, and URLs are retained
where translation would damage provenance. No unauthorized claims of
dependency ground truth, task resolution, causal knowledge flow, complete OSS
ecosystem coverage, a platform, AI autonomy, or research-efficiency gains were
introduced.

## Semantic parity matrix

| Frozen semantic requirement | EN-R01 status |
|---|---|
| RefQ is a traceable, observation-aware operationalization of project-level explicit-reference structure | Supported |
| Evidence construction is separated from role-specific structural measurement | Supported |
| Interpretation is role-dependent, observation-bounded, metric-dependent, and label-sensitive | Supported |
| RefQ is not dependency ground truth, task-resolution truth, causal knowledge flow, or project importance | Supported |
| Source-complete seeds versus source-incomplete expanded targets | Supported |
| Direction-ignored view is first-order and does not restore missing observations | Supported |

`PARITY_REVIEW_ITEMS = 9` (native wording, spacing around protected tokens,
caption idiom, table-label idiom, formula delimiter placement, and six
section-level fluency clusters). `BLOCKING_SEMANTIC_CONFLICTS = 0`.

## LANG-A02 review items

LANG-A02 must perform native English semantic parity and editorial QA,
including sentence fluency, terminology consistency, table/caption grammar,
formula delimiter placement, numeric-token boundary normalization, and a
line-level comparison against the frozen Chinese source. LANG-A02 must not
change scientific values, RQ semantics, observation contracts, or the JSS
requirement-debt boundary.

## No-change guards

```text
CHINESE_CURRENT_MODIFIED = NO
MS_R04_SNAPSHOT_MODIFIED = NO
SCIENTIFIC_VALUES_CREATED = 0
SCIENTIFIC_VALUES_CHANGED = 0
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
NETWORK_RECOMPUTATION = 0
FIGURE_RERENDER = 0
FIGURE_ASSETS_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
```

## Repository scope and handoff

The only intended tracked addition is this audit document. The four existing
untracked V3-V6 ZIP files remain untouched. The external EN-R01 working file
is intentionally not committed as an accepted manuscript or repository
version.

Next task:

`CH5_REFQ_LANG_A02_ENGLISH_SEMANTIC_PARITY_AND_NATIVE_QA`

## Final decision

`CH5_REFQ_LANG_A01_AUTHORITATIVE_ENGLISH_TRANSLATION_CANDIDATE_PASS_READY_FOR_LANG_A02`
