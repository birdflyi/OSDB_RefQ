# Chapter 5 RefQ MS-R01 Editorial Audit Completion E0.1

## Decision

`CH5_REFQ_MS_R01_EDITORIAL_AUDIT_E0_1_PASS_READY_FOR_BOUNDED_EDIT`

E0.1 completes the reviewer-facing granularity missing from E0. It is a
read-only audit: no manuscript revision, scientific recomputation, display
render, or metadata rewrite was performed.

## 1. Identity and inherited authority

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before E0.1 | `11aed651943f9a2c233d8831d735bb3474576e6b` |
| Manuscript revision | `MS-R01` |
| CURRENT SHA-256 before/after | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Snapshot SHA-256 before/after | `CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE` |
| Previous authority | `ch5_refq_ms_r01_comprehensive_editorial_audit_e0.md` |

E0's scientific closure, 31/31 authority identification, citation-key and
bibliography closure, zero positive overclaim count, and immutability findings
are carried forward unchanged.

## 2. Canonical issue ledger

| ID | Dimension | Sections/occurrences | Problem | Reviewer effect | Minimal future action | Editorial severity | Scientific impact |
|---|---|---|---|---|---|---|---|
| A-01 | Chain/contribution | Abstract line 12; §1.4 lines 58-64 | C1/C2 and the four contribution labels are conceptually distinct but expressed as abstract internal taxonomy | Reader must translate labels into concrete research outputs | Retain four-part order; state each contribution first as a concrete action/output, then optionally retain the shorthand label | E1 | PRESENTATION_ONLY |
| A-02 | Chain/conclusion | §9 lines 737-743 | Conclusion closes contracts and boundaries more strongly than the memorable empirical answer | Main take-away is less visible than the qualification inventory | Add one concise evidence-led synthesis sentence and compress repeated boundary clauses | E1 | PRESENTATION_ONLY |
| B-01 | Terminology | Abstract; §§1-5; §9 | Dense Chinese-English noun stacks recur after concepts are already defined | Raises parsing cost and makes prose resemble specification language | Define canonical English terms once; reuse shorter Chinese or established acronym forms without global translation | E1 | PRESENTATION_ONLY |
| B-02 | Terminology | §§1.1-1.4, 3.3.1, 3.4.4, 4.1, 5.4 | `external`, `external-resource`, `external-project`, `non-self`, and `non-project` are correct but repeatedly juxtaposed | A reviewer can lose which complement/partition is meant | Add one compact controlled-terms statement and consistently reserve each term for its current denominator | E1 | INTERPRETATION_RISK |
| C-01 | Heading architecture | line 133 | `3.1.3` is Markdown level 3 while `3.1.1` and `3.1.2` are level 4 | Broken hierarchy in rendered navigation | Change only the Markdown heading level of `3.1.3` to match sibling subsections | E0 | NONE |
| C-02 | Rhetorical architecture | §4 opening, line 378 | One sentence carries the full RQ1/RQ2/RQ3 roadmap and all boundary qualifications | Reader must parse the complete results architecture before reaching evidence | Split into three ordered roadmap sentences keyed to RQ1, RQ2, and RQ3 | E1 | PRESENTATION_ONLY |
| C-03 | Methods architecture | §3.3 before §3.4 | Network metrics are introduced before the RefQN object and its formal construction are fully defined | Requires forward reconstruction of the analyzed object | Prefer §3.4 construction before network metrics, or add an explicit forward-definition bridge if reordering is undesirable | E1 | PRESENTATION_ONLY |
| C-04 | Heading architecture | §4.2.0 | `4.2.0` is an unconventional publication heading between §4.2 and §4.2a | Looks implementation-derived and interrupts hierarchy | Rename as an unnumbered/introductory scale paragraph or adopt a conventional subsection scheme | E1 | NONE |
| D-01 | Display integration | Figure 2, lines 501-503 | Figure 2 appears before the scale paragraph and before RQ2a/RQ2b result narration | Evidence is visible before its denominators and main claims are established in prose | Move after the RQ2a/RQ2b evidence or strengthen the lead-in and add an immediate interpretive sentence | E1 | PRESENTATION_ONLY |
| D-02 | Display integration | Figure 4 and §§4.3.1-4.3.3 | Caption already states nearly the full inferential result, then prose repeats it | Mild redundancy and slower Results progression | Keep caption self-contained but shorten repeated post-caption narration | E2 | NONE |
| E-01 | Literature/method semantics | §3.3.3 line 234; Figure 4; Table 4.8; §§4.3, 6.4 | Formula `max(0,(H-k+1)/(n-k))` is rank eta-squared (`eta-squared_H`) in authoritative implementations, not rank epsilon-squared | Current label is a factual method-name mismatch although frozen values are internally consistent | Rename the reported effect size consistently to rank eta-squared/`eta-squared_H`, retain the zero clamp as an implementation detail, and add a dedicated method source | E0 | FACTUAL_RISK |
| E-02 | Citation scope | §6.2 line 703 | GitHub Docs citations follow a sentence that also asserts possible false positives/negatives | Docs may appear to provide empirical extraction-error evidence | Attach Docs citations only to syntax/mechanics; present FP/FN risk as the study's rule-based extraction limitation | E1 | INTERPRETATION_RISK |
| F-01 | Methods style | §§3.1-3.4 (`P0`, `current analysis`, `frozen`, `gate`, configuration fields, mapping authority) | Reproducibility language sometimes reads as an audit/configuration record | Main Methods voice shifts from research design to workflow governance | Keep essential definitions, convert bare workflow labels to research prose, and move exact configuration identifiers to Appendix A where possible | E1 | PRESENTATION_ONLY |
| F-02 | Results style | lines 569, 649, 653 | Long sequences of full-precision statistics obscure the inferential point | Reader must extract the result from machine-level precision | Use publication precision in prose/tables and retain full precision in the reproducibility package | E1 | PRESENTATION_ONLY |
| F-03 | Line editing | Figure 2-4 captions; Abstract results/contribution prose | Captions and synthesis sentences contain multiple nested definitions, values, and guards | High working-memory burden despite correct content | Split into shorter declarative sentences without changing caption content or figure composition | E1 | PRESENTATION_ONLY |
| F-04 | Line editing | §§4-6 and §9 | Negative guards are sometimes repeated immediately after already bounded claims | Prose can feel defensive and the positive finding becomes less salient | Consolidate repeated guards at subsection exits while retaining every unique boundary | E2 | NONE |
| F-05 | Notation/style | `32--37`, slash spacing, mixed raw identifiers | Small typography and code-style residue remains in publication prose | Minor visual inconsistency | Normalize ranges, slash spacing, and identifier presentation in one mechanical pass | E2 | NONE |

Severity totals:

```text
E0_COUNT = 2
E1_COUNT = 12
E2_COUNT = 3
INFO_COUNT = 8
SCIENTIFIC_CONFLICT_COUNT = 0
```

The two E0 findings are bounded editorial/method-reporting defects. E-01 does
not invalidate the frozen statistic values: the implementation and reported
values agree with each other, but the effect-size name is wrong. No rerun is
required to repair the label and source.

## 3. Dimension A: problem-method-result-conclusion chains

| Item | Motivation/gap | Method/definition | Evidence | Main result | Interpretation | Limitation | Conclusion closure | Status | Issue IDs |
|---|---|---|---|---|---|---|---|---|---|
| RQ1 | Observable references exceed dependency/code-call views | Admitted fine-grained Reference universe and project profiles | Fig. 1; Tables 4.1-4.6a | Discussion/event evidence, external-resource orientation, heterogeneous self/non-self composition | Evidence boundary supporting RefQ construction | Descriptive, seed/source-observed, no task/quality inference | §5.4 and §9 correctly subordinate RQ1 to construction support | CLOSED_BUT_VERBOSE | B-01, B-02 |
| RQ2a | Need source-complete active-reference characterization | Seed-only source role, out-degree/out-strength/concentration | Fig. 2A-B; Table 4.6c | Typical/max separation and seed-to-expanded dominance | Active range and repeated-reference strength are distinct | Only 294 seed sources complete; no power-law claim | §5.1/§5.4/§9 close source role | CLOSED | D-01 |
| RQ2b | Need target coverage/concentration characterization | Observable-target in-degree/in-strength and coverage | Fig. 2C-D; Table 4.6d | Most targets have low coverage; weight is concentrated | Target coverage is not global importance | Denominator is 294 seeds; target sources incomplete | §5.1/§5.4/§9 close target role | CLOSED | D-01 |
| RQ2c | Need first-order direction-ignored structural view | `U(G_RefQ)`, LCC, Louvain, approximate betweenness | Fig. 3; Tables 4.6e-4.6f | Large LCC, algorithmic partitions, bounded brokerage candidates | First-order modular-neighborhood and bridge-position evidence | Not projection, taxonomy, causal flow, or stable semantic community | Repeatedly and correctly closed in §§5 and 9 | CLOSED_BUT_VERBOSE | F-02, F-03, F-04 |
| RQ3 | Possible DBMS-category variation under uncertain labels | Two label modes, KW, multiplicity correction, bounded effect size | Fig. 4; Tables 4.7-4.8 | Composition unsupported; selected features only include-mixed; zero cross-mode robust features | Local, metric-dependent, label-sensitive variation | Cross-sectional, multi-label, minimum group size and FDR boundaries | Integrated in §5.1/§5.4 and §9 rather than appended | CLOSED | E-01, D-02 |
| C1 | Prior aggregation lacks explicit relation contract in this paper | Endpoint, membership, aggregation and interpretation formalization | §3.4 equations and boundary definitions | Paper-specific RefQ/RefQN contract | Concrete contribution is formalized construction semantics | Not a new quotient algorithm | Present in Abstract/§1.4/§9 but label is abstract | CLOSED_BUT_VERBOSE | A-01, B-01 |
| C2 | Observable evidence and edge-eligible evidence must not be conflated | Two-universe and source-observation boundary instantiation | Fig. 1; §3.2.3; §3.4.4 | Non-project/internal evidence retained while only eligible endpoints form RefQ | Boundary-aware empirical instantiation | DBMS/GitHub/2023 scope | Closed, but distinction from C1 requires careful reading | WEAK_TRANSITION | A-01, B-02 |
| C3 | Seed/target observation asymmetry requires role-aware analysis | RQ1 support plus RQ2a/b/c role separation and RQ3 sensitivity | Figs. 1-4; Tables 4.1-4.8 | Role-specific and boundary-aware characterization | Avoids sampling-induced source/target misreading | Expanded targets source-incomplete | Consistent across Abstract, Discussion and Conclusion | CLOSED_BUT_VERBOSE | A-01, B-01 |
| C4 | RefQ should support downstream work without stronger claims | Traceable weaker-semantic structural evidence layer | Provenance, membership and evidence-to-edge traceability | Reusable bounded relation asset | Candidate screening and future semantic validation interface | Not dependency/task/causal truth | Closed, but final concrete benefit is less memorable than label | UNDER_EXPLAINED | A-01, A-02 |

## 4. Dimension B: controlled terminology and semantic language

| Canonical concept | Preferred term | Current variants | Sections | Semantic conflict? | Reviewer burden? | Future action | Issue ID |
|---|---|---|---|---|---|---|---|
| Reference | `Reference` as relation/event family | reference,引用,Reference relation | all | No | Low | Keep capitalized construct; use Chinese explanation once | INFO |
| Reference evidence | Reference evidence | Reference facts, observable evidence | Abstract; §§1-6 | No | Medium | Define once, then shorten | B-01 |
| Fine-grained evidence | fine-grained Reference evidence | artifact-level evidence,底层 evidence | §§1-3 | No | Medium | `DEFINE_ONCE_THEN_REUSE` | B-01 |
| Reference relation | Reference relation | direct project-reference relation | §§1-3, 6 | No | Low | Keep distinction between record relation and aggregated RefQ | INFO |
| Reference Coupling | Reference Coupling | cross-reference coupling | §§1-2, 5 | No | Low | `KEEP_ENGLISH` as prior-work construct | INFO |
| Reference Quotient | Reference Quotient (`RefQ`) | semantic membership quotient, quotient relation | all | No | Medium | Define once; prefer `RefQ` after definition | B-01 |
| RefQN | Reference Quotient Network (`RefQN`) | RefQ network | all | No | Low | Prefer acronym after definition | INFO |
| Project-level RefQN | Project-level RefQN | project-level quotient network | §§1-5 | No | Medium | Keep when level matters; otherwise `RefQN` | B-01 |
| Observable universe | observable fine-grained Reference evidence universe | admitted universe, observable evidence universe | Abstract; §§1-5 | No | High | Define once; later use `observable evidence universe` | B-01 |
| Eligible subset | quotient-eligible project-mappable subset | eligible evidence, project-mappable records | Abstract; §§1-4 | No | High | Keep exact term at boundary definition; shorten later | B-01 |
| Endpoint eligibility | endpoint eligibility | quotient eligibility | §§1, 3 | No | Medium | Reserve endpoint eligibility for mapping condition; quotient eligibility for retained row | INFO |
| Project-mappable | project-mappable | project-mapped, mappable target | §§1, 3, 4 | No | Low | `DEFINE_ONCE_THEN_REUSE` | INFO |
| Semantic membership | semantic membership | project identity/membership | §§1-3, 5, 9 | No | Medium | State project ownership meaning once | B-01 |
| Membership mapping | artifact-to-project membership mapping | project mapping | §§1-3 | No | Medium | Prefer full term in Methods, `membership mapping` later | B-01 |
| Membership partition | membership partition | semantic partition, membership block | §§2-3 | No | Medium | Keep mathematical variants near equations only | B-01 |
| Membership-induced coarsening | membership-induced graph coarsening | quotient construction, block aggregation | §§1-3 | No | High | Use one process term per paragraph | B-01 |
| Quotient construction | quotient construction | block aggregation, compression | §§1-6 | No | Medium | Distinguish process from resulting relation | INFO |
| Analysis seed | analysis seed project | seed, seed DBMS project | all | No | Low | Prefer `analysis seed` after definition | INFO |
| Expanded target | expanded target project/node | referenced project, observable target | §§1, 3-5 | No | Medium | Reserve `observable target` for any target; `expanded target` for non-seed membership | B-02 |
| Observable target | observable target project | referenced project | §§3-4 | No | Medium | Add one explicit inclusion relation | B-02 |
| Source role | source role | source behavior/activity | §§1, 3-5 | No | Low | Keep role label; use behavior only for measured source-complete set | INFO |
| Target role | target role | target coverage/concentration | §§1, 3-5 | No | Low | Keep | INFO |
| Undirected view | first-order undirected structural view | direction-ignored view, `U(G_RefQ)` | §§1-5 | No | Medium | Prefer full phrase on first subsection use | B-01 |
| Self-reference | self-reference | internal reference | §§1, 3-5 | No | Medium | Use self-reference for mapped same-project records; internal evidence only as plain-language gloss | B-02 |
| Non-self share | non-self Reference share | `external_reference_share`, external share | §§3-5 | Potential naming risk only | High | Always pair field identifier with canonical semantic term | B-02 |
| Non-project share | non-project Reference share | external-resource share | §§1, 3-5 | No | High | Never abbreviate as external share | B-02 |
| External project | external-project Reference | cross-project, seed-to-expanded | §§1, 3-4 | No | High | Keep separate from non-project resource | B-02 |
| External resource | external non-project resource | external link/resource | §§1, 3-6 | No | High | Use full phrase when denominator matters | B-02 |
| Reference-bearing context | Reference-bearing Issue/PR context | active issue/PR | §§3-4 | Historical field risk controlled | Medium | Keep canonical prose term; raw field only in code font | INFO |
| Source entity | unique source entity | comment-related source | §§3-4 | No | Medium | Define covered entity prefixes once | B-01 |
| Reference-row density | Reference rows per issue/PR-related source entity | comment_reference_density, references per comment (negative only) | §§3-4 | No | Medium | Canonical prose first, identifier second | B-01 |
| Algorithmic community | algorithmic community/partition | community, modular neighborhood | §§3-6 | No | Medium | Retain `algorithmic`; use modular neighborhood as interpretation | INFO |
| Structural brokerage candidate | structural brokerage candidate | bridge-like position | §§3-5 | No | Medium | Define once; avoid standalone `broker` | B-01 |
| Cross-sectional | cross-sectional 2023 | age association | §§3-6 | No | Low | Keep | INFO |
| Label-mode sensitive | label-mode sensitive | mode-sensitive | §§3-6 | No | Low | Keep canonical hyphenation | F-05 |
| FDR-supported | FDR-supported | significant after FDR | §§3-6 | No | Low | Prefer canonical wording | INFO |
| Cross-mode robust | cross-mode robust | robust across modes | §§3-6 | No | Low | Keep and define once | INFO |

Mixed-language classification:

| Class | Examples | Treatment |
|---|---|---|
| KEEP_ENGLISH | Reference Coupling, RefQ, RefQN, Louvain, FDR, HHI, ARI | Established construct/acronym; retain |
| DEFINE_ONCE_THEN_REUSE | observable evidence universe, project-mappable, source/target role | Define once, then use a shorter canonical form |
| FIELD_IDENTIFIER | `external_reference_share`, `comment_reference_density`, `reference_dedup_rule` | Keep in code font only where reproducibility requires |
| REPLACE_WITH_NATURAL_CHINESE | long phrases such as `observation-aware role-aware empirical characterization` in running prose | Replace label-first prose with concrete Chinese action/result |
| INTERNAL_WORKFLOW_LEAK | bare P0, mapping authority, gate, frozen authority, configuration item | Move to Appendix or rephrase as method/snapshot definition |

## 5. Dimension C: heading and subsection architecture

| Section | Heading | Main purpose | Entry logic | Internal progression | Exit logic | Overlap | Heading/content fit | Status | Issue IDs |
|---|---|---|---|---|---|---|---|---|---|
| Abstract | 摘要 | Standalone problem-method-data-result-contribution summary | Direct | Logical but dense | Contributions/boundary close | Some contribution repetition with §1.4 | Fit | NEEDS_TRANSITION | A-01, B-01, F-03 |
| §1.1 | 可观测 Reference evidence | Domain motivation | Natural | Ecosystem -> DBMS -> evidence | Leads to construct | Low | Fit | PASS | - |
| §1.2 | Reference Coupling、图粗化与 RefQ | Prior construct and mathematical positioning | Natural | empirical precedent -> quotient language -> boundaries | Leads to gap | Moderate repetition with §2 | Fit | PASS | B-01 |
| §1.3 | 研究缺口与目标 | Explicit construction/observation gap | Strong | relation gap -> prior limits -> observation -> objective | Leads to RQs | Low | Fit | PASS | - |
| §1.4 | 研究问题与贡献 | Five RQs and four contributions | Strong | RQs -> C1-C4 -> synthesis | Closes introduction | Labels abstract | Fit | NEEDS_BOUNDARY_CLARIFICATION | A-01 |
| §2.1 | 软件生态与社会技术证据 | Broad background | Natural | ecosystem -> triad -> premises | Leads to references | Low | Fit | PASS | - |
| §2.2 | Cross-project References | Platform/link studies and coupling | Natural | mechanics -> coupling -> IREL -> two universes | Leads to math | Low | Fit | PASS | - |
| §2.3 | Graph coarsening/quotients | Mathematical precedent | Natural | definitions -> paper adaptation -> projections | Leads to DBMS context | Low | Fit | PASS | B-01 |
| §2.4 | DBMS domain | Domain motivation for heterogeneity | Natural | domain features -> possible categories -> bounded close | Leads to gap | Low | Fit | PASS | - |
| §2.5 | 研究缺口收束 | Synthesize exact gap | Strong | three precedents -> missing contract | Explicit Methods handoff | Some repetition with §1.3 | Fit | PASS | B-01 |
| §3 intro | 研究方法 | Method roadmap | Natural | two roadmap paragraphs | Sample section | Slight duplication | Fit | PASS | C-03 |
| §3.1 | 数据来源与样本筛选 | Sample and source facts | Natural | selection -> data -> pipeline | Extraction | Low | Fit | PASS | - |
| §3.1.1 | 目标项目选择与数据口径 | Three-level selection contract | Natural | candidate -> evidence availability -> identity | Defines 294 seeds | Low | Fit | PASS | F-01 |
| §3.1.2 | 数据获取与清洗 | Historical events and preprocessing | Natural | sources -> fields -> normalization | GH_CoRE | Low | Fit | PASS | F-01 |
| §3.1.3 | GH_CoRE 处理链 | Pipeline/provenance | Natural content | six steps -> credibility boundary | Extraction rules | Low | Content fits, Markdown level does not | HEADING_MISMATCH | C-01, F-01 |
| §3.2 | 引用关系抽取与实体校验 | Rules, admission, mapping | Natural | rules -> flow -> denominator map | Metrics | Low | Fit | PASS | - |
| §3.2.1 | 跨项目引用识别规则 | Recognition grammar | Natural | precedent -> seven rules | Extraction flow | Low | Fit | PASS | E-02 |
| §3.2.2 | 引用抽取流程 | Admission and multiplicity | Natural | extraction controls -> admission -> no dedup | Denominator table | Low | Fit | PASS | F-01 |
| §3.2.3 | 数据来源/口径/RQ | Denominator authority | Strong | flow equation -> mapping table | Metrics | Low | Fit | PASS | F-01 |
| §3.3 | 度量与统计 | Operational metrics/tests | Requires RefQN forward reference | descriptive -> network -> inference | Then construction definition | Moderate | Fit, order weak | NEEDS_REORDERING | C-03 |
| §3.3.1 | 描述性指标 | RQ1 operational definitions | Natural | entity -> context -> composition/age | Network metrics | Low | Fit | PASS | B-02 |
| §3.3.2 | 网络拓扑指标 | RQ2 metrics/settings | Object not yet formally defined | source -> target -> undirected | Statistics | Low | Fit | NEEDS_TRANSITION | C-03 |
| §3.3.3 | 统计分析 | Descriptive/age/KW/FDR boundaries | Natural | tests -> correction -> interpretation | RefQ construction | Low | Formula label defect | NEEDS_BOUNDARY_CLARIFICATION | E-01 |
| §3.4 | RefQN 构建 | Formal object construction | Arrives after its metrics | entity domain -> partition -> equation -> boundary | Results | Low | Fit | NEEDS_REORDERING | C-03 |
| §3.4.1 | 细粒度图与可映射子域 | Define domain | Natural | entity table -> graph -> eligible subset | Partition | Low | Fit | PASS | - |
| §3.4.2 | Membership partition | Define equivalence blocks | Natural | equivalence -> blocks -> literature boundary | RefQ equation | Low | Fit | PASS | B-01 |
| §3.4.3 | RefQ formalization | Define q, M, Q and semantics | Natural | scalar -> matrix -> graph -> exclusions | Observation boundary | Some repeated second-order guard | Fit | PASS | F-04 |
| §3.4.4 | RefQN observation boundary | Seed/target vocabulary and loops | Natural | set -> terms -> loops -> close | Results | Low | Fit | PASS | B-02 |
| §4 intro | 结果 | Evidence hierarchy roadmap | Correct hierarchy | One overloaded sentence | RQ1 | None | Fit | NEEDS_TRANSITION | C-02 |
| §4.1 | RQ1 | Evidence composition/support | Natural | types -> contexts -> age | RQ2 | Low | Fit | PASS | - |
| §4.1.1 | 类型与构成 | Global distributions/self share | Natural | Fig.1 -> Tables 4.1/4.2 -> self ratio | Context metrics | Low | Fit | PASS | F-04 |
| §4.1.2 | Context/intensity/density | Three operational metrics | Natural | Tables 4.3-4.5 -> synthesis | Age | Low | Fit | PASS | B-01 |
| §4.1.3 | 年龄横截面关联 | Weak associations and limit | Natural | result -> table -> boundary | RQ2 | Low | Fit | PASS | - |
| §4.2 | RQ2 role views | Separate source/target/undirected roles | Strong | Figure before denominators/results | Scale/RQ2a | Low | Fit | NEEDS_REORDERING | D-01 |
| §4.2.0 | Scale 与视图边界 | Denominator preface | Natural content | scale -> table | RQ2a | None | Unconventional number | HEADING_MISMATCH | C-04 |
| §4.2a | RQ2a | Source role | Natural | quantiles -> partitions -> top sources | RQ2b | Low | Fit | PASS | - |
| §4.2b | RQ2b | Target role | Natural | targets -> concentration -> coverage | RQ2c | Low | Fit | PASS | - |
| §4.2c | RQ2c | First-order undirected structure | Natural | topology -> Louvain -> brokerage/stability | RQ3 | Low | Fit | PASS | F-02, F-03 |
| §4.3 | RQ3 | Label-mode-sensitive comparison | Natural | Figure -> composition -> role/structure -> age | Discussion | Some caption repetition | Fit | PASS | D-02, E-01 |
| §4.3.1 | Composition | Negative FDR result | Natural | descriptive table -> boundary | Network features | Low | Fit | PASS | - |
| §4.3.2 | RefQ/local metrics | Mode-sensitive features | Natural | summary -> semantic mapping -> table/example | Age | Low | Fit | PASS | E-01, F-02 |
| §4.3.3 | Age/boundary | Age sensitivity and RQ3 close | Natural | result -> integrated conclusion | Discussion | Low | Fit | PASS | E-01, F-02 |
| §5.1 | RefQ meaning | Interpret RQ hierarchy | Natural | RQ1 -> RQ2 -> RQ3 | Prior work | Low | Fit | PASS | - |
| §5.2 | Prior OSS relation | Position contribution/loss | Natural | novelty boundary -> value -> information loss | Practice | Low | Fit | PASS | B-01, F-04 |
| §5.3 | Practice | Candidate uses and validation needs | Natural | uses -> required evidence | RQ synthesis | Low | Fit | PASS | - |
| §5.4 | RQ synthesis | Explicit RQ closure | Natural | RQ1 -> RQ2 -> RQ3 -> hierarchy | Threats | Some repetition | Fit | PASS | F-04 |
| §6 intro | Validity | Threat roadmap | Natural | Five categories | Construct | None | Fit | PASS | - |
| §6.1 | Construct | Evidence/construct limits | Natural | coverage -> semantic ambiguity | Internal | Low | Fit | PASS | - |
| §6.2 | Internal | Extraction/mapping/aggregation risk | Natural | threats -> mitigations | External | Low | Fit | PASS | E-02 |
| §6.3 | External | Population/platform limits | Natural | platform -> domain/observation | Conclusion validity | Low | Fit | PASS | - |
| §6.4 | Conclusion validity | Statistical limits | Natural | methods -> bounded inference | Reliability | Low | Effect-size name wrong | NEEDS_BOUNDARY_CLARIFICATION | E-01 |
| §6.5 | Reliability | Reproduction meaning | Natural | identity -> external mutability | Availability | Low | Fit | PASS | - |
| §7 | 数据与代码可用性 | Release scope | Natural | existing release -> permissible archive -> code status | Supplement | Some governance prose | Fit | PASS | F-01 |
| §8 | 补充材料说明 | Appendix authority boundary | Natural | one bounded paragraph | Conclusion | None | Fit | PASS | - |
| §9 | 结论 | Formal/empirical/boundary/future close | Natural | construction -> RQs -> nonclaims -> future | End | Boundary inventory dominates | Fit | NEEDS_TRANSITION | A-02, B-01, F-04 |

## 6. Dimension C2: paragraph-purpose audit

Audit unit: every blank-line-delimited non-list prose block in Abstract and
§§1-9, including figure captions and the Methods mapping-table lead. Markdown
headings, table cells, displayed equations, and enumerated list items are
audited in the heading, display, terminology, method, and notation matrices.

| Paragraph locator | Dominant role | One-sentence gist | Problem? | Issue ID |
|---|---|---|---|---|
| L4 | BACKGROUND | Positions Reference evidence beyond dependencies and identifies the aggregation gap | No | - |
| L6 | DEFINITION | Defines the two universes and paper-specific RefQ/RefQN | Dense terminology | B-01 |
| L8 | METHOD | Summarizes sample, record flow and network scale | No | - |
| L10 | RESULT | Summarizes RQ1-RQ3 results and scope | Dense synthesis | B-01, F-03 |
| L12 | CONCLUSION | States four contributions in one taxonomy-heavy sentence | Multiple competing main points | A-01, F-03 |
| L14 | DEFINITION | Lists keywords | No | - |
| L19 | MOTIVATION | Establishes DBMS as a bounded vertical setting | No | - |
| L21 | BACKGROUND | Connects ecosystem and DBMS literature to the study setting | No | - |
| L23 | MOTIVATION | Grounds DBMS technical context and observable traces | Mild noun-stack load | B-01 |
| L26 | COMPARISON | Positions RefQ against Reference Coupling precedent | No | - |
| L28 | BACKGROUND | Introduces graph-coarsening and quotient foundations | Dense terminology | B-01 |
| L30 | DEFINITION | Defines Project-level RefQN and semantic nonclaims | Dense terminology | B-01 |
| L32 | BOUNDARY | Separates first-order Q from second-order operators | No | - |
| L34 | BOUNDARY | Excludes projection relations from the study | No | - |
| L36 | GAP | Introduces the two-universe distinction as the paper's focus | Dense terminology | B-01 |
| L39 | GAP | States the project-level construction problem | Long specification-style list | B-01 |
| L41 | GAP | Narrows the gap relative to prior project-reference work | Dense contract list | B-01 |
| L43 | BOUNDARY | States source/target observation asymmetry | No | - |
| L45 | MOTIVATION | Converts construction and observation boundaries into study objectives | No | - |
| L48 | TRANSITION | Introduces RQs | No | - |
| L56 | TRANSITION | Introduces contribution list | No | - |
| L58 | CONCLUSION | States C1 formalization contribution | Abstract label obscures concrete output | A-01 |
| L60 | BOUNDARY | States C2 evidence-boundary contribution | C1/C2 distinction requires reconstruction | A-01, B-02 |
| L62 | CONCLUSION | States C3 role-aware empirical contribution | English noun stack | A-01, B-01 |
| L64 | IMPLICATION | States C4 reusable weaker-semantic layer | Label more memorable than concrete deliverable | A-01 |
| L66 | CONCLUSION | Synthesizes contribution hierarchy | No | - |
| L71 | BACKGROUND | Reviews ecosystem interaction research | No | - |
| L73 | BACKGROUND | Reviews socio-technical networks and defines the paper's triad | Dense but bounded | B-01 |
| L75 | TRANSITION | Derives two premises and hands off to RefQ | No | - |
| L78 | BACKGROUND | Reviews platform mechanisms and link-context studies | Citation scope clear | - |
| L80 | COMPARISON | Positions Reference Coupling precedent and novelty boundary | No | - |
| L82 | COMPARISON | Positions IREL and distinguishes self-loop policy | No | - |
| L84 | DEFINITION | Defines the two evidence layers | Dense terminology | B-01 |
| L87 | BACKGROUND | Reviews coarsening and quotient language | No | - |
| L89 | DEFINITION | Relates normalized and unnormalized quotient forms | Dense notation/code-switching | B-01, F-05 |
| L91 | COMPARISON | Assigns separate roles to coupling and quotient literatures | No | - |
| L93 | BOUNDARY | Separates RefQ from second-order projections | No | - |
| L96 | MOTIVATION | Establishes DBMS domain characteristics | No | - |
| L98 | MOTIVATION | Motivates possible subdomain variation without asserting it | No | - |
| L100 | CONCLUSION | Closes DBMS as bounded setting | No | - |
| L103 | GAP | Synthesizes exact formalization gap | Specification-style density | B-01 |
| L107 | METHOD | Introduces Methods components and GH_CoRE | Dense roadmap | B-01, C-03 |
| L109 | TRANSITION | Orders method stages and denominator authority | Slight roadmap duplication | C-03 |
| L113 | METHOD | Introduces three-level sample construction | No | - |
| L119 | BOUNDARY | Defines event window and repository identity rules | Audit-record tone | F-01 |
| L121 | BOUNDARY | Defines source observation set and defers denominators | No | - |
| L124 | METHOD | States event sources, API role and fields | No | - |
| L130 | METHOD | Describes preprocessing, time alignment and P0 boundary | Workflow terminology leak | F-01 |
| L134 | METHOD | Defines GH_CoRE inputs and outputs | No | - |
| L143 | BOUNDARY | Limits pipeline credibility and P0 dedup implication | Workflow terminology leak | F-01 |
| L148 | METHOD | States extraction precedent and recognition rules | Docs scope clear here | - |
| L159 | METHOD | Separates extraction controls from analysis deduplication | No | - |
| L161 | METHOD | Defines strict source admission and ordering | Configuration/audit tone | F-01 |
| L163 | METHOD | Defines no-dedup setting and unit weight | Configuration identifier dominates prose | F-01 |
| L166 | BOUNDARY | Introduces the denominator/RQ mapping authority | Internal authority language | F-01 |
| L168 | METHOD | States record-flow equation and eligibility step | No | - |
| L170 | TRANSITION | Labels the mapping table | No | - |
| L185 | METHOD | Introduces three-dimensional descriptive metrics | No | - |
| L204 | METHOD | Introduces role-separated network metrics | Object is defined later | C-03 |
| L224 | BOUNDARY | Separates labels from algorithmic communities | No | - |
| L228 | METHOD | Introduces statistical methods | Object-order issue inherited | C-03 |
| L243 | DEFINITION | Introduces entity/mappability table | No | - |
| L258 | DEFINITION | Defines fine-grained Reference graph | No | - |
| L264 | BOUNDARY | Defines graph elements and seed-centered limitation | No | - |
| L266 | DEFINITION | Introduces project-mappable set | No | - |
| L272 | DEFINITION | Introduces membership mapping | No | - |
| L278 | DEFINITION | States total/single-valued mapping requirement | No | - |
| L287 | BOUNDARY | Explains eligible entities and non-project exclusions | Long but coherent | B-01 |
| L290 | DEFINITION | Introduces induced equivalence relation | No | - |
| L298 | DEFINITION | Introduces membership blocks | No | - |
| L304 | COMPARISON | Relates semantic blocks to Loukas while limiting inheritance | Dense qualification | B-01 |
| L306 | DEFINITION | Introduces scalar RefQ weight | No | - |
| L315 | DEFINITION | Defines directed project relation | No | - |
| L321 | DEFINITION | States relation semantics and nonclaims | No | - |
| L323 | METHOD | States frozen unit-weight implementation | Audit/implementation tone | F-01 |
| L325 | DEFINITION | Defines `R_P` and membership matrix `M` | No | - |
| L335 | DEFINITION | States one-hot membership condition | No | - |
| L344 | COMPARISON | Positions unnormalized block sum against quotient precedent | Dense transition into equation | B-01 |
| L352 | DEFINITION | Introduces RefQN graph tuple | No | - |
| L358 | BOUNDARY | Restates first/second-order distinction | Repeated guard | F-04 |
| L360 | BOUNDARY | Excludes K projection | Repeated guard | F-04 |
| L363 | BOUNDARY | Defines seed-centered network | No | - |
| L365 | DEFINITION | Introduces controlled observation terms | No | - |
| L372 | BOUNDARY | Defines self-loop semantics and view choice | No | - |
| L374 | BOUNDARY | Closes observation and denominator boundaries | Internal authority wording | F-01 |
| L378 | TRANSITION | Gives complete Results roadmap | Run-on/competing main points | C-02 |
| L383 | RESULT | Introduces RQ1 universe and dimensions | No | - |
| L385 | RESULT | Figure 1 caption reports flow and eligibility boundary | Dense caption | F-03 |
| L389 | INTERPRETATION | Motivates source-entity distribution | No | - |
| L391 | METHOD | Defines compact-table display rule | No | - |
| L405 | RESULT | Interprets source distribution | Repeated guard, acceptable | F-04 |
| L409 | INTERPRETATION | Motivates target-entity distribution | No | - |
| L425 | RESULT | Interprets target distribution | Repeated guard | F-04 |
| L429 | RESULT | Reports self-reference distribution | No | - |
| L431 | RESULT | Gives project examples | No | - |
| L433 | CONCLUSION | Synthesizes RQ1 evidence composition | No | - |
| L435 | METHOD | Defines three context/intensity/density metrics | English noun-stack load | B-01 |
| L439 | DEFINITION | Defines context breadth | No | - |
| L447 | RESULT | Interprets Table 4.3 | No | - |
| L451 | DEFINITION | Defines source-entity intensity | No | - |
| L459 | RESULT | Interprets Table 4.4 | Repeated boundary | F-04 |
| L463 | DEFINITION | Defines row density | No | - |
| L471 | RESULT | Interprets Table 4.5 and RQ3 relation | No | - |
| L475 | CONCLUSION | Synthesizes three metric units | No | - |
| L479 | METHOD | Defines cross-sectional age associations | No | - |
| L483 | RESULT | Reports correlations and weak effects | No | - |
| L496 | LIMITATION | Blocks longitudinal/causal reading | No | - |
| L501 | BOUNDARY | Separates RQ2 roles | Figure lead-in exists but is general | D-01 |
| L503 | RESULT | Figure 2 caption defines roles, denominators and shares | Caption overload and early placement | D-01, F-03 |
| L507 | RESULT | Reports network scale and view denominators | No | - |
| L520 | RESULT | Reports source quantiles and non-power-law boundary | Full precision limited | - |
| L522 | RESULT | Reports seed-to-seed/expanded partitions | No | - |
| L542 | RESULT | Reports top source projects and interpretation | No | - |
| L546 | RESULT | Reports target population and quantiles | No | - |
| L548 | RESULT | Reports target weight concentration | No | - |
| L563 | LIMITATION | Defines coverage denominator and non-importance | No | - |
| L567 | RESULT | Reports undirected topology and first-order status | No | - |
| L569 | RESULT | Reports Louvain and sensitivity with machine precision | Number dumping | F-02 |
| L571 | RESULT | Figure 3 caption integrates structure/views/sensitivity | Caption overload | F-03 |
| L586 | RESULT | Reports brokerage candidates | No | - |
| L598 | BOUNDARY | Reports ranking stability without semantic upgrade | No | - |
| L602 | METHOD | Introduces RQ3 label modes and tests | No | - |
| L604 | RESULT | Figure 4 caption gives descriptive and inferential outcome | Caption/prose redundancy and wrong effect-size label | D-02, E-01, F-03 |
| L608 | RESULT | Reports composition differences as unsupported | No | - |
| L625 | LIMITATION | Limits category interpretation | No | - |
| L629 | RESULT | States label-mode-sensitive result | No | - |
| L631 | DEFINITION | Maps raw identifiers to prose meanings | No | - |
| L649 | RESULT | Gives out-degree test values at full precision | Number dumping and wrong effect-size label | E-01, F-02 |
| L653 | RESULT | Gives age test values at full precision | Number dumping and wrong effect-size label | E-01, F-02 |
| L655 | CONCLUSION | Closes RQ3 | Wrong effect-size label inherited only indirectly | E-01 |
| L661 | INTERPRETATION | Explains RefQ empirical meaning and RQ1 support role | No | - |
| L663 | INTERPRETATION | Explains role asymmetry and bounded position | No | - |
| L665 | INTERPRETATION | Integrates RQ3 as local/label-sensitive | No | - |
| L669 | COMPARISON | Positions contribution against precedents | Dense citation/contract prose | B-01 |
| L671 | INTERPRETATION | Explains traceability and bounded domain interpretation | Repeated guards | F-04 |
| L673 | LIMITATION | Explains coarse-graining loss | No | - |
| L677 | IMPLICATION | Gives candidate practical uses | No | - |
| L679 | LIMITATION | States evidence needed for stronger use | No | - |
| L683 | CONCLUSION | Synthesizes RQ1 | No | - |
| L685 | CONCLUSION | Synthesizes RQ2 | Dense guard sequence | F-04 |
| L687 | CONCLUSION | Synthesizes RQ3 | No | - |
| L689 | CONCLUSION | Reasserts RQ/contribution hierarchy | No | - |
| L693 | TRANSITION | Introduces validity categories | No | - |
| L697 | LIMITATION | States construct coverage limits | No | - |
| L699 | LIMITATION | States semantic ambiguity | No | - |
| L703 | LIMITATION | Lists extraction/mapping/aggregation threats | Citation scope ambiguity | E-02 |
| L705 | LIMITATION | Lists mitigations and residual error | Audit-style density | F-01 |
| L709 | LIMITATION | States platform/population limits | No | - |
| L711 | LIMITATION | States domain and observation limits | No | - |
| L715 | LIMITATION | States statistical conclusion limits | Wrong effect-size label | E-01 |
| L719 | METHOD | Defines reproducibility requirements | No | - |
| L721 | LIMITATION | Limits byte-identical future reconstruction | No | - |
| L725 | METHOD | Describes existing release and version reconciliation | Governance tone but necessary | F-01 |
| L727 | BOUNDARY | Defines potentially publishable artifacts | No | - |
| L729 | LIMITATION | Clarifies code/release status | No | - |
| L733 | BOUNDARY | Defines Appendix A authority | No | - |
| L737 | CONCLUSION | Restates formal contribution and non-novelty | Technical inventory dominates | A-02, B-01 |
| L739 | CONCLUSION | Summarizes RQ hierarchy and bounded variation | No | - |
| L741 | BOUNDARY | Restates stronger-semantic nonclaims | Repeated guard | A-02, F-04 |
| L743 | LIMITATION | States limitations and future work | Dense notation/term inventory | A-02, B-01, F-05 |

## 7. Dimension C3: narrative transitions

| Transition | Assessment | Reason / future action |
|---|---|---|
| §1.1 -> §1.2 | NATURAL | Domain evidence motivates prior construct/formal language |
| §1.2 -> §1.3 | NATURAL | Positioning leads directly to missing contract |
| §1.3 -> §1.4 | NATURAL | Gap and objective lead to RQs/contributions |
| §1 -> §2 | ACCEPTABLE | Introduction closes hierarchy; Related Work restarts precedent detail |
| §2 -> §3 | NATURAL | §2.5 explicitly hands off the formalization gap |
| §3.1 -> §3.2 | NATURAL | Sample/source facts precede extraction/admission |
| §3.2 -> §3.3 | ACCEPTABLE | Denominators precede metrics |
| §3.3 -> §3.4 | MISSING_LOGICAL_BRIDGE | Metrics refer to RefQN before formal construction; C-03 |
| RQ1 -> RQ2 | NATURAL | Evidence boundary precedes project-level structure |
| RQ2a -> RQ2b | NATURAL | Source role contrasts with target role |
| RQ2b -> RQ2c | NATURAL | Directed roles lead to direction-ignored structure |
| RQ2c -> RQ3 | NATURAL | Structure leads to bounded category comparison |
| §4 -> §5 | NATURAL | Results close with RQ3 synthesis; Discussion interprets hierarchy |
| §5 -> §6 | ACCEPTABLE | Interpretation is followed by explicit validity limits |
| §6 -> §7 | NATURAL | Reliability leads to availability/reproduction scope |
| §7 -> §8 | NATURAL | Release scope leads to supplement authority |
| §8 -> §9 | ACCEPTABLE | Short provenance note precedes conclusion; no decorative bridge needed |

## 8. Dimension D: figure/table/claim evidence architecture

| Display | RQ | Exact evidence role | Main claim supported | Pre-display lead-in | Post-display interpretation | Redundant prose? | Type suitable? | Missing information? | Status | Issue IDs |
|---|---|---|---|---|---|---|---|---|---|---|
| Figure 1 | RQ1 | Record flow, target partition, event composition | Observable universe differs from eligible subset | Strong | Tables 4.1/4.2 and text interpret | No | Yes | No | PASS | - |
| Figure 2 | RQ2a/b | Source CCDFs, target quantiles, target-weight shares | Role distributions and target concentration | General boundary lead only | Interpretation is separated into later subsections | Some | Yes | No | UNDER_INTEGRATED | D-01, F-03 |
| Figure 3 | RQ2c | First-order undirected scale, view sensitivity, Louvain sensitivity | Structure is large-LCC but partition is algorithmic/sensitive | Strong | Brokerage and stability follow | Mild | Yes | No | PASS | F-03 |
| Figure 4 | RQ3 | Two-mode descriptive and FDR/effect-size comparison | No cross-mode robust feature | Strong | Subsections repeat caption outcome | Yes | Yes | Effect-size label needs repair | OVER_NARRATED | D-02, E-01, F-03 |
| Table 4.1 | RQ1 | Source entity distribution | IssueComment dominates observed sources | Strong | Direct interpretation | No | Yes | No | PASS | - |
| Table 4.2 | RQ1 | Target entity distribution | External links dominate observed targets | Strong | Direct interpretation | No | Yes | No | PASS | - |
| Table 4.3 | RQ1 | Context breadth distribution | Strong right skew/heterogeneity | Strong | Direct interpretation | No | Yes | No | PASS | - |
| Table 4.4 | RQ1 | Unique source entities/context | Right-skewed source-entity intensity | Strong | Direct interpretation | No | Yes | No | PASS | - |
| Table 4.5 | RQ1 | Reference rows/source entity | Right-skewed row density | Strong | Direct interpretation/RQ3 boundary | No | Yes | No | PASS | - |
| Table 4.6a | RQ1 | Cross-sectional age correlations | Associations are weak and non-longitudinal | Strong | Explicit boundary | No | Yes | No | PASS | - |
| Table 4.6b | RQ2 | Directed/undirected denominator map | Edge/weight/view counts must not be mixed | Strong | Used by all RQ2 text | No | Yes | No | PASS | C-04 |
| Table 4.6c | RQ2a | Source quantiles/concentration and relation partitions | Source range/strength differ; expanded targets dominate | Strong | Top-source interpretation | No | Yes | No | PASS | - |
| Table 4.6d | RQ2b | Target counts/quantiles/concentration | Most targets low coverage; weight concentrated | Strong | Coverage denominator interpretation | No | Yes | No | PASS | - |
| Table 4.6e | RQ2c | Undirected/LCC/Louvain summary | First-order structural scale and modularity | Strong | Brokerage follows | No | Yes | No | PASS | F-02 |
| Table 4.6f | RQ2c | Top brokerage candidates | Candidate bridge positions | Strong | Stability qualification | No | Yes | No | PASS | - |
| Table 4.7 | RQ3 | Include-mixed category composition | Descriptive ranges do not survive FDR | Strong | Direct boundary | No | Yes | No | PASS | - |
| Table 4.8 | RQ3 | Two-mode FDR/effect-size matrix | Selected features are mode-sensitive; none robust | Strong | Example and age result follow | Mild | Yes | Effect-size label needs repair | MISSING_REQUIRED_INFORMATION | E-01, D-02 |

Evidence summary:

```text
UNSUPPORTED_MATERIAL_CLAIM_COUNT = 0
MISSING_REQUIRED_DISPLAY_COUNT = 0
ORPHAN_DISPLAY_COUNT = 0
DISPLAY_WITHOUT_LEAD_IN_COUNT = 0
DISPLAY_WITHOUT_INTERPRETATION_COUNT = 0
```

## 9. Dimension D2: material claim-to-evidence coverage

| Claim locator | Material claim | Evidence source | Direct/derived | RQ | Evidence sufficient? | Interpretation bounded? | Issue ID |
|---|---|---|---|---|---|---|---|
| §4.1.1 L383-405 | 3,747,958 admitted records and source composition | Fig. 1; Table 4.1 | Direct | RQ1 | Yes | Yes | - |
| §4.1.1 L409-425 | Target composition led by external links | Fig. 1; Table 4.2 | Direct | RQ1 | Yes | Yes | - |
| §4.1.1 L429-433 | Self-reference distribution and examples | Frozen project profiles | Direct | RQ1 | Yes | Yes | - |
| §4.1.2 L439-447 | Context breadth is right-skewed | Table 4.3 | Direct | RQ1 | Yes | Yes | - |
| §4.1.2 L451-459 | Source-entity intensity is right-skewed | Table 4.4 | Direct | RQ1 | Yes | Yes | - |
| §4.1.2 L463-475 | Reference-row density is heterogeneous | Table 4.5 | Direct | RQ1 | Yes | Yes | - |
| §4.1.3 L483-496 | Age associations are weak/cross-sectional | Table 4.6a | Direct | RQ1 | Yes | Yes | - |
| §4.2.0 L507 | RefQN scale and denominators | Table 4.6b | Direct | RQ2 | Yes | Yes | C-04 |
| §4.2a L520 | Source quantile/max separation | Fig. 2A-B; Table 4.6c | Direct | RQ2a | Yes | Yes | D-01 |
| §4.2a L522 | Seed-to-expanded relations dominate | Table 4.6c continuation | Direct | RQ2a | Yes | Yes | - |
| §4.2a L542 | Top out-strength projects | Frozen source-role rows | Direct | RQ2a | Yes | Yes | - |
| §4.2b L546 | Target population and in-role quantiles | Fig. 2C; Table 4.6d | Direct | RQ2b | Yes | Yes | D-01 |
| §4.2b L548 | Top-k target weight concentration | Fig. 2D; Table 4.6d | Direct | RQ2b | Yes | Yes | - |
| §4.2b L563 | Maximum coverage is 42/294 | Fig. 2C; Table 4.6d | Derived from direct fields | RQ2b | Yes | Yes | - |
| §4.2c L567 | First-order undirected topology/LCC scale | Fig. 3A; Table 4.6e | Direct | RQ2c | Yes | Yes | - |
| §4.2c L569 | Louvain partition and sensitivity | Fig. 3A/C; supplemental sensitivity | Direct | RQ2c | Yes | Yes | F-02 |
| §4.2c L586 | Brokerage candidate ranking | Table 4.6f | Direct | RQ2c | Yes | Yes | - |
| §4.2c L598 | Brokerage ranking stability | Supplemental sensitivity output | Direct | RQ2c | Yes | Yes | - |
| §4.3.1 L608-625 | Composition differences are descriptive, not FDR-supported | Fig. 4A-D; Table 4.7/4.8 | Direct | RQ3 | Yes | Yes | E-01 |
| §4.3.2 L629-649 | Selected role/structure features pass only include-mixed | Fig. 4E; Table 4.8 | Direct | RQ3 | Yes | Yes | E-01, F-02 |
| §4.3.3 L653-655 | Age difference is label-mode sensitive; no robust feature | Fig. 4E; Table 4.8 | Direct | RQ3 | Yes | Yes | E-01, F-02 |
| §5.1 L661 | RQ1 is evidence-boundary support, not topology itself | Fig. 1; §§3.2-3.4; Tables 4.1-4.6a | Derived synthesis | RQ1 | Yes | Yes | - |
| §5.1 L663 | Source/target/undirected roles are non-interchangeable | Fig. 2/3; Tables 4.6b-f | Derived synthesis | RQ2 | Yes | Yes | - |
| §5.1 L665 | RQ3 is local/metric/mode-sensitive | Fig. 4; Tables 4.7-4.8 | Direct synthesis | RQ3 | Yes | Yes | - |
| §5.2 L669-673 | Contribution is bounded formalization with coarse-graining loss | Methods + prior-work contrast + provenance | Derived | C1-C4 | Yes | Yes | B-01 |
| §5.3 L677-679 | RefQ supports candidate screening, not automated decisions | RQ2 structure + semantic boundary | Derived implication | RQ2 | Yes | Yes | - |
| §5.4 L683-689 | RQ hierarchy and conclusions | All Results displays | Derived synthesis | all | Yes | Yes | F-04 |

## 10. Dimension E: literature-support completion

### E-LIT-01: effect-size formula

Exact manuscript location: §3.3.3 line 234:

```text
max(0, (H - k + 1) / (n - k))
```

Focused verification found that the official `effectsize` documentation and
implementation distinguish:

```text
rank epsilon-squared: H / ((n^2 - 1) / (n + 1)) = H / (n - 1)
rank eta-squared:     max(0, (H - k + 1) / (n - k))
```

The package documentation cites Tomczak and Tomczak (2014), *The need to
report effect size estimates revisited*, for rank-based ANOVA effect sizes.
Kruskal and Wallis (1952) supports the test, not this later effect-size naming
and estimator choice.

Focused sources checked on 2026-09-17:

* `https://easystats.github.io/effectsize/reference/rank_epsilon_squared.html`
* `https://github.com/easystats/effectsize/blob/main/R/rank_ANOVA.R`

Closure:

```text
E-LIT-01 = DEFECT_CONFIRMED_BOUNDED_LABEL_AND_CITATION_REPAIR
DEDICATED_SOURCE_REQUIRED = YES
SCIENTIFIC_RECOMPUTATION_REQUIRED = NO
```

Smallest future action: consistently rename the current values to rank
eta-squared (`eta-squared_H`) in Methods, Figure 4 caption/labels, Table 4.8,
Results and validity prose; explain `max(0, ...)` as the implementation's
non-negative clamp; add a dedicated effect-size source. Do not change the
frozen numeric values.

### E-LIT-02: GitHub Docs limitation

The citations in §2.2 line 78 and §3.2.1 line 148 clearly support GitHub link
syntax/mechanics. In §6.2 line 703, their placement after the FP/FN-risk clause
can imply empirical support that the Docs do not provide.

Closure:

```text
E-LIT-02 = WORDING_SCOPE_REPAIR_REQUIRED
```

Smallest future action: cite GitHub Docs only in the syntax/mechanics sentence;
state that rule-based extraction may miss variants or admit ambiguous matches
as the study's own internal-validity limitation.

### Citation placement across citation-bearing paragraphs

| Locators | Placement class | Note | Issue ID |
|---|---|---|---|
| L4, L21, L23, L26, L28, L36, L71, L73, L78, L80, L82, L87, L93, L96, L98, L115, L148, L221, L236, L304, L344 | CLEAR_SCOPE | Citation immediately follows the supported precedent/mechanism | - |
| L41, L103, L669 | CLEAR_SCOPE | Grouped sources support prior-work synthesis; novelty/gap remains author synthesis | - |
| L234 | MULTI_CLAIM_SCOPE_AMBIGUOUS | Kruskal citation is adjacent to test and effect-size formula, but supports only the test | E-01 |
| L703 | MULTI_CLAIM_SCOPE_AMBIGUOUS | Docs support mechanics, not empirical FP/FN rates | E-02 |

## 11. Dimension F: candidate line-edit ledger

| ID | Section | Current function | Problem type | Why it increases reviewer parsing cost | Minimal edit strategy | Severity |
|---|---|---|---|---|---|---|
| A-01 | Abstract/§1.4 | Four contributions | AI_LIKE_NOMINALIZATION | Abstract labels precede concrete deliverables | Lead with action/output; keep shorthand second | E1 |
| B-01 | Abstract L6/L10; §§1-5 | Define/summarize construct | ENGLISH_NOUN_STACK | Multiple modifiers switch language inside one clause | Define once and shorten later occurrences | E1 |
| C-02 | §4 L378 | Results roadmap | RUN_ON | Three RQ layers and all qualifiers compete | Split into three RQ-ordered sentences | E1 |
| F-03 | Abstract L10/L12 | Results/contributions | NESTED_QUALIFIERS | Main result is separated from predicate by boundaries | Split result and scope/contribution clauses | E1 |
| F-01 | §3.1.1 L119 | Identity/window definition | SPECIFICATION_STYLE | Snapshot/gate vocabulary resembles audit record | State research date/identity choice first; move governance detail to Appendix | E1 |
| F-01 | §3.1.2 L130 | Preprocessing boundary | EXPERIMENT_LOG_STYLE | `P0` and write-back language assumes internal workflow knowledge | Replace with analysis-stage wording; retain P0 only in Appendix | E1 |
| F-01 | §3.2.2 L161-L163 | Admission/dedup definition | SPECIFICATION_STYLE | Raw predicates/config fields dominate method explanation | Give prose rule first, identifier second or Appendix | E1 |
| F-01 | §3.2.3 L166 | Denominator map | EXPERIMENT_LOG_STYLE | `only authority` reads as governance instruction | Say the table summarizes denominators used in Results | E1 |
| B-01 | §3.4.2 L304 | Literature boundary | NESTED_QUALIFIERS | One sentence carries precedent, exclusions and exact definition | Split precedent from paper-specific rule | E1 |
| B-01 | §3.4.3 L344/L358 | Matrix definition/boundary | ENGLISH_NOUN_STACK | English technical modifiers obscure the equation's simple role | State unnormalized block sum plainly, then contrast source | E1 |
| D-01 | §4.2 L501-L503 | Figure 2 introduction | ABRUPT_TRANSITION | Figure precedes scale and main RQ claims | Reposition or add denominator/result lead-in | E1 |
| F-03 | Figures 2-4 captions | Self-contained captions | PUNCTUATION_OVERLOAD | Multiple panels, definitions, numbers and guards occupy one sentence | Use one sentence per panel group plus one boundary sentence | E1 |
| F-02 | §4.2c L569 | Louvain sensitivity | TERM_DENSITY_LOW_INFORMATION | Exact decimals obscure instability conclusion | Round in prose; retain exact values in table/package | E1 |
| F-02 | §4.3 L649/L653 | Statistical examples | NUMBER_DUMPING | Full raw/FDR/effect-size precision hides mode comparison | Report publication precision and point to complete table | E1 |
| D-02 | §4.3 | Caption and subsection narration | DUPLICATE_FUNCTION | Caption and body repeat the same pass/fail list | Let caption identify panels; body interpret the result | E2 |
| F-04 | §§4-6 | Boundary statements | REPEATED_NEGATIVE_GUARD | Repeated disclaimers dilute positive finding | Consolidate only duplicate guards at subsection exits | E2 |
| E-02 | §6.2 L703 | Extraction threat | AMBIGUOUS_REFERENCE | Docs appear to evidence FP/FN behavior | Separate mechanics citation from author limitation | E1 |
| A-02 | §9 | Final answer | TERM_DENSITY_LOW_INFORMATION | Technical contracts dominate the concluding message | Add concise empirical takeaway; compress repeated exclusions | E1 |
| F-05 | §§4-9 | Typography | SYMBOL_NOTATION | Double hyphens/slashes/raw identifiers look mechanically exported | One mechanical typography pass | E2 |

## 12. Special F audit: Abstract sentence units

The semicolon-linked contribution sentence is audited as four clause units
because each functions as a separate contribution claim.

| Sentence/unit | Function | Information conveyed | Terminology load | Readability | Action | Issue ID |
|---|---|---|---|---|---|---|
| S1 L4.1 | Problem | DBMS cross-project relations exceed dependencies/calls | Low | Clear | Keep | - |
| S2 L4.2 | Background | Reference Coupling supports project networks | Medium | Clear | Keep | - |
| S3 L4.3 | Gap | Fine-grained-to-project aggregation needs explicit semantics/boundaries | Medium | Clear | Keep | - |
| S4 L6.1 | Method concept | Separates observable and eligible universes | High | Dense | Rephrase | B-01 |
| S5 L6.2 | Definition | Names RefQ/RefQN | Medium | Clear | Keep | - |
| S6 L6.3 | Novelty boundary | No new generic quotient algorithm | Medium | Clear | Keep | - |
| S7 L6.4 | Semantic boundary | First-order traceable relation, not stronger semantics | Medium | Clear | Keep | - |
| S8 L8.1 | Data/method | 294 seeds and GH_CoRE | Medium | Clear | Keep | - |
| S9 L8.2 | Data | Record flow and eligibility | High | Clear because arithmetic is linear | Keep | - |
| S10 L8.3 | Network scale | Nodes/edges and undirected view | Medium | Clear | Keep | - |
| S11 L10.1 | RQ1 result | Discussion/external-resource evidence composition | Medium | Clear | Keep | - |
| S12 L10.2 | RQ2 result | Typical/max separation and target concentration | High | Dense | Split/rephrase | F-03 |
| S13 L10.3 | RQ3 result | No composition support; mode-sensitive selected features | High | Dense | Split/rephrase after E-01 rename | E-01, F-03 |
| S14 L10.4 | Boundary | Scope limited to observed GitHub evidence | Medium | Clear | Keep | - |
| S15a L12 | C1 | Formal construction contract | Very high | Abstract label dominates | Rephrase | A-01 |
| S15b L12 | C2 | Boundary-aware evidence instantiation | Very high | C1/C2 distinction not immediate | Rephrase | A-01 |
| S15c L12 | C3 | Role-aware empirical characterization | Very high | Noun stack | Rephrase | A-01 |
| S15d L12 | C4 | Reusable weaker-semantic layer | High | Concrete utility arrives late | Rephrase | A-01 |

Abstract coverage is otherwise complete:

```text
PROBLEM_VISIBILITY = PASS
METHOD_VISIBILITY = PASS
DATA_VISIBILITY = PASS
MAIN_FINDINGS_VISIBILITY = PASS_WITH_EDITS
CONTRIBUTION_VISIBILITY = PASS_WITH_EDITS
BOUNDARY_VISIBILITY = PASS
STANDALONE_COMPREHENSIBILITY = PASS_WITH_EDITS
```

## 13. Special F audit: contribution prose

| Contribution label | Classification | Concrete contribution currently present? | Future treatment | Issue ID |
|---|---|---|---|---|
| explicit relation formalization / construction contract | Conceptually necessary label plus internal taxonomy | Yes: endpoint/membership/aggregation/interpretation contract | State concrete formalization first; label optional | A-01 |
| boundary-aware evidence instantiation | Conceptually necessary but close to C1 in wording | Yes: two universes, non-project/self-loop/source-target boundaries | Emphasize empirical instantiation and denominator boundary to distinguish from C1 | A-01 |
| observation-aware role-aware empirical characterization | Useful shorthand with AI-like nominalization | Yes: RQ2a/b/c roles plus RQ1/RQ3 placement | Replace stacked label with plain-language action | A-01 |
| traceable weaker-semantic structural evidence layer | Conceptually necessary positioning but noun-heavy | Yes: traceable relation asset for bounded screening/future validation | Lead with reuse/traceability outcome, then weaker-semantic qualification | A-01, A-02 |

## 14. Special F audit: Methods publication prose

| Expression | Occurrences/surface | Classification | Future action | Issue ID |
|---|---|---|---|---|
| `P0` | lines 130, 143 | MOVE_TO_APPENDIX_CANDIDATE | Replace in main text with `current analysis stage`; retain exact stage ID in Appendix A | F-01 |
| `current analysis` | sample/admission/dedup/statistics prose | REPHRASE_FOR_PUBLICATION | Use `本文分析` or direct active statement | F-01 |
| `frozen` | evidence files, annotation, implementation/results | KEEP_FOR_REPRODUCIBILITY selectively | Keep only when snapshot immutability matters; otherwise state date/version | F-01 |
| `gate` / 门槛 | §3.1.1 | REPHRASE_FOR_PUBLICATION | Use inclusion criterion/availability criterion | F-01 |
| configuration item / raw predicate | §3.2.2 | MOVE_TO_APPENDIX_CANDIDATE | Prose rule in main text; exact key/value in Appendix | F-01 |
| mapping/denominator authority | §3.2.3 | REPHRASE_FOR_PUBLICATION | Use `summary of denominators used in Results` | F-01 |
| unit-weight operationalization | §§3.2.2, 3.4.3 | KEEP_FOR_REPRODUCIBILITY | Keep once in natural prose; Appendix may retain exact configuration | F-01 |

## 15. Special F audit: Results, Discussion, and Conclusion

Results are evidence-complete and do not contain unsupported material claims.
The main editorial costs are Figure 2 integration, Figure 4/caption repetition,
machine-level decimal precision, and repeated negative guards. Discussion adds
interpretation rather than merely copying tables: it explains role asymmetry,
formalization value, information loss, and bounded practical use. Conclusion
preserves the central problem but should make the empirical answer more
memorable before repeating nonclaims and future operators.

## 16. Symbol and notation matrix

| Symbol | First definition | Meaning | Later uses consistent? | Formatting issue? | Issue ID |
|---|---|---|---|---|---|
| `Q` | L32; formal L348 | RefQ project-level weighted adjacency | Yes | None | - |
| `R_P` | L325 | Project-mappable fine-grained Reference adjacency | Yes | Subscript typography consistent | - |
| `M` | L325 | One-hot artifact-to-project membership matrix | Yes | None | - |
| `pi` (`\pi`) | L272-275 | Membership mapping from `V_P` to projects | Yes | None | - |
| `V_P` | L266-269 | Project-mappable entity set | Yes | None | - |
| `G_R^obs` | L260-264 | Seed-centered observed fine-grained graph | Yes | Superscript consistent | - |
| `G_P^obs` | L287 | Induced project-mappable endpoint subgraph | Yes, limited use | Define as displayed equation if reused more | INFO |
| `G_RefQ` | L355 | Project-level RefQN graph tuple | Yes | None | - |
| `U(G_RefQ)` | L219; results L567 | Direction-ignored first-order RefQ view | Yes | None | - |
| `q_ab` | L306-313 | Aggregated directed weight from project a to b | Yes | None | - |
| `QQ^T` | L32 | Shared-target second-order relation | Yes | Transpose typography `\top` consistent | - |
| `Q^TQ` | L32 | Shared-source second-order relation | Yes | Transpose typography consistent | - |
| `K=X Phi X^T` | L32/L360 | Shared-reference projection | Yes | `Phi` defined only as generic operator; acceptable because excluded | INFO |
| `H` | L234 | Kruskal-Wallis statistic | Yes | Effect-size label attached to derived formula is wrong | E-01 |
| `k` | L234 | Number of eligible groups | Yes | None | - |
| `n` | L234 | Total eligible observations | Yes | Also table sample-size column; context clear | - |
| epsilon-squared | L234 | Currently named effect size | No: formula is rank eta-squared | Rename consistently and cite | E-01 |
| `rho` | L483 | Spearman coefficient | Yes | None | - |
| `p` | L483 | p-value; also project metavariable in formal section | Context separates uses | Italic/math p in prose could be standardized | F-05 |
| FDR p | L236; Table 4.8 | BH-adjusted p-value | Yes | Prefer consistent `FDR-adjusted p` | F-05 |
| ARI | L569 | Adjusted Rand Index to canonical/pairwise partitions | Yes | Define expansion on first use | F-05 |
| HHI | L210/Table 4.6c | Source target-weight concentration | Yes | Define expansion on first use | F-05 |

Equation punctuation and transpose formatting are otherwise consistent.
Percent signs and numeric ranges are semantically correct; `32--37` should be
normalized to an en dash in publication output. Chinese/English parentheses
are understandable but can be mechanically normalized with F-05.

## 17. Accepted INFO controls

1. RQ1 is explicitly a support/evidence-boundary RQ rather than a co-equal
   structural contribution.
2. RQ2c remains explicitly first-order in Methods, Results, captions,
   Discussion, validity, and Conclusion.
3. RQ3's negative and label-sensitive result is integrated throughout.
4. Every material empirical claim has visible evidence.
5. No display is orphaned or lacks interpretation.
6. External/non-self/non-project meanings are scientifically closed despite
   editorial burden.
7. The principal matrix symbols and transpose notation are consistent.
8. Positive overclaim count remains zero.

## 18. Future bounded edit groups

| Edit group | Issue IDs | Exact surfaces | Scientific values touched? | Figures/tables touched? | References touched? | Risk |
|---|---|---|---|---|---|---|
| EDIT-GROUP-1 Abstract / Introduction narrative | A-01, B-01, B-02 | Abstract L6/L10/L12; §1.4 contribution paragraphs; controlled external-family terms | No | No | No | Medium: preserve hierarchy/semantics |
| EDIT-GROUP-2 Methods architecture, publication prose and citation repair | C-01, C-03, E-01, E-02, F-01 | Heading 3.1.3; §3.3/§3.4 order/bridge; L234; L703; workflow terms | No numeric change | Table 4.8 and Figure 4 labels/caption terminology only for E-01 | Yes: add effect-size source; reposition Docs scope | High: global effect-size label consistency |
| EDIT-GROUP-3 Results and display integration | C-02, C-04, D-01, D-02, F-02, F-03, F-05 | §4 roadmap; §4.2.0; Figures 2-4 placement/captions; precision/typography | Display precision only, no value change | Text/caption/table headings only; no rerender unless separately authorized | No | Medium |
| EDIT-GROUP-4 Discussion / Conclusion convergence | A-02, F-04 | §§5.2, 5.4, 6 and 9 repeated guards/final synthesis | No | No | No | Low |

## 19. Mandatory closure statuses

```text
A_PROBLEM_METHOD_RESULT_CONCLUSION = PASS_WITH_EDITS
B_TERMINOLOGY_AND_EXPERIMENTAL_SEMANTICS = PASS_WITH_EDITS
C_RHETORICAL_ARCHITECTURE = PASS_WITH_EDITS
D_FIGURE_TABLE_EVIDENCE_ARCHITECTURE = PASS_WITH_EDITS
E_LITERATURE_AND_CITATION_VERIFICATION = PASS_WITH_EDITS
F_LANGUAGE_STYLE_AND_NOTATION = PASS_WITH_EDITS

EDITORIAL_COMPLETE = NO
READY_FOR_BOUNDED_EDITORIAL_CONVERGENCE = YES
```

## 20. No-edit and execution guards

```text
MANUSCRIPT_REVISION = MS-R01
MANUSCRIPT_SHA_BEFORE = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
MANUSCRIPT_SHA_AFTER = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
MANUSCRIPT_CHANGED = 0
CURRENT_CHANGED = 0
SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_MANUSCRIPT_REVISION_CREATED = 0

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

Final decision:

`CH5_REFQ_MS_R01_EDITORIAL_AUDIT_E0_1_PASS_READY_FOR_BOUNDED_EDIT`
