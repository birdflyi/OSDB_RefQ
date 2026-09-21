# Chapter 5 RefQ — JSS Contribution Framing and Observation-Validity Audit

```text
TASK = CH5_REFQ_JSS_CONTRIBUTION_FRAMING_AND_OBSERVATION_VALIDITY_AUDIT
AUDIT_MODE = READ_ONLY_MANUSCRIPT_FRAMING_AUDIT
AUDIT_DATE = 2026-09-21
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
HEAD_BEFORE_AUDIT = 9ee95fbd8b2cadba3586ec2d7604265d13048eb2
```

This audit evaluates whether the accepted MS-R03 supports a JSS-facing
framing centred on traceable, observation-aware, project-level
operationalization and role-aware measurement. It does not edit the
manuscript, create MS-R04, alter scientific assets, or run an analysis.

## 1. Manuscript identity and protected state

| Item | Path / value | Result |
|---|---|---|
| Authoritative manuscript | `ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md` | MS-R03 |
| MS-R03 snapshot | `ch5_analysis_reference_coupling_for_osdbms/versions/MS-R03_POST_SUBMISSION_CONDENSED_E59F96FF.md` | immutable snapshot |
| CURRENT SHA-256 | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| snapshot SHA-256 | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| CURRENT equals snapshot | YES | PASS |
| repository HEAD | `9ee95fbd8b2cadba3586ec2d7604265d13048eb2` | PASS |
| remote HEAD before audit | `9ee95fbd8b2cadba3586ec2d7604265d13048eb2` | PASS |

The following framing authorities were read as strategy documents, not as
scientific-data authorities:

- `docs/strategy/ch5_refq_asset_and_publication_strategy_v1.0.md`
- `docs/submission_suggestion/ch5_refq_jss_elevated_framing_freeze_v1.0.md`
- `docs/submission_suggestion/ch5_refq_sub_a01_jss_vs_emse_target_venue_audit_2026-09-21.md`

The frozen paper centre is:

> a traceable and observation-aware operationalization of project-level
> explicit-reference structure.

The accepted manuscript’s evidence chain is `fine-grained Reference
evidence → endpoint eligibility → semantic membership → aggregation → RefQ /
RefQN → source-observation asymmetry → role-aware measurement → empirical
characterization → bounded interpretation`.

## 2. F1–F4 support matrix

| Claim | Status | MS-R03 evidence |
|---|---|---|
| F1 — RefQ transforms heterogeneous fine-grained Reference evidence into a reproducible project-level measurement object | `FULLY_SUPPORTED` | §1.2–§1.4 define RefQ/RefQN and contracts; §§3.2–3.3 define extraction, eligibility, membership, aggregation and observation boundary; §5.2 calls this a bounded formalization/reframing; §9 states the traceable construction. |
| F2 — source observation is asymmetric | `FULLY_SUPPORTED` | §3.3.4 defines 294 source-complete seeds and source-incomplete expanded targets; §§4.2a–4.2c use distinct role views; §§5.1/5.4 synthesize the asymmetry; §§6.3–6.4 and §9 retain the boundary. |
| F3 — role-aware measurement | `YES` | §§1.3–1.4 and 3.3.4 separate source, target and first-order undirected structural roles; §3.4 gives population/denominator semantics; §§4.2a–4.2c report separate metrics and §5.1 explains their different interpretations. |
| F4 — measurable but conditional interpretation | `FULLY_SUPPORTED` | §5.1/§5.4 and §9 jointly establish measurability, role dependence, observation bounds, metric dependence and label-mode sensitivity. |

### F2 lifecycle check

| Lifecycle stage | Status | Evidence |
|---|---|---|
| Defined in Methods | `DEFINED` | §§3.1.1, 3.3.4 and Appendix A.2 define the seed-centered observation contract. |
| Used in RQ design | `USED` | RQ2a source role, RQ2b target role and RQ2c first-order structural view are explicitly separated. |
| Respected in Results | `RESPECTED` | §§4.2a–4.2c use role-specific populations, denominators and interpretations; expanded-target out-degree is not interpreted as source activity. |
| Synthesized in Discussion | `SYNTHESIZED` | §§5.1, 5.2 and 5.4 make observation asymmetry an interpretation contract, not a reporting footnote. |
| Reflected in Threats | `REFLECTED` | §§6.1–6.4 constrain platform, source completeness, seed-centred boundary and metric interpretation. A more explicit consolidated validity paragraph remains advisable (see §8). |
| Answered in Conclusion | `ANSWERED` | §§9 and A.4 state what is measurable, under which boundaries, and what stronger semantics remain unsupported. |

### F4 component classification

| Component | Classification | Evidence |
|---|---|---|
| `MEASURABLE` | `DIRECTLY_SUPPORTED` | §1.4, §3.3 and §9 explicitly define and construct RefQ/RefQN. |
| `ROLE_DEPENDENT` | `DIRECTLY_SUPPORTED` | §3.3.4, §§4.2a–4.2c and §5.1 distinguish source, target and structural roles. |
| `OBSERVATION_BOUNDED` | `DIRECTLY_SUPPORTED` | §§3.3.4, 6.3 and A.2 identify the seed-centred boundary and incomplete expanded targets. |
| `METRIC_DEPENDENT` | `DIRECTLY_SUPPORTED` | §3.4 and §5.1/§5.4 state population, denominator and metric-specific interpretation limits. |
| `LABEL_OPERATIONALIZATION_SENSITIVE` | `DIRECTLY_SUPPORTED` | §§4.3, 5.1 and 5.4 report include-mixed versus exclude-mixed sensitivity and zero cross-mode robust features. |

## 3. Positive-but-objective reframing validation

| Candidate interpretation | Status | Frozen evidence |
|---|---|---|
| R1 — direct-reference structure exhibits modular organization, but one algorithmic partition is not a stable semantic taxonomy | `YES` | 35 canonical Louvain communities; sensitivity range 32–37; 42/50 ARI values below 0.9; minimum ARI 0.6823671359861659; minimum pairwise ARI 0.6092441840471735; §4.2c and A.4 explicitly reject a stable semantic/DBMS taxonomy. |
| R2 — subdomain effects are not invariant to label operationalization | `YES` | §4.3 compares `include_mixed` and `exclude_mixed_or_multilabel`; feature results are mode-sensitive and no feature passes FDR in both modes. |
| R3 — observation completeness determines admissible interpretation of node roles | `YES` | §§3.3.4, 4.2, 5.1, 6.3 and 9 state that expanded targets are not source-complete and that low target out-degree is not evidence of low source activity. |

## 4. Representative literature bridge

The bridge is intentionally complementary and critical, not adversarial:

```text
LITERATURE_POSITIONING = COMPLEMENTARY_CRITICAL
```

| Work | Verified bibliographic identity | Permitted use in the JSS framing | Boundary |
|---|---|---|---|
| Kalliamvakou et al. (2014), *The Promises and Perils of Mining GitHub*, DOI `10.1145/2597073.2597074` | Crossref: MSR 2014 proceedings article, published 2014-05-31 | Motivate explicit care with GitHub platform/data/sample interpretation and observable repository evidence. | Not evidence for RefQ-specific source asymmetry. |
| McClean, Greer & Jurek-Loughrey (2021), *Social network analysis of open source software: A review and categorisation*, DOI `10.1016/j.infsof.2020.106442` | Crossref: *Information and Software Technology* 130, 106442, published 2021-02 | Motivate variation in OSS network data sources and network constructions, and the dependence of structural interpretation on the analytical category. | Do not attribute RefQ-style role semantics to the review. |
| Blincoe et al. (2019), *Reference Coupling*, DOI `10.1016/j.infsof.2019.03.005` | Crossref: *Information and Software Technology* 110, 174–189, published 2019-06 | Preserve as a validated dependency-oriented project-reference precedent under its own sampling/relation scope. Use it to motivate a complementary question about broader heterogeneous Reference evidence and explicit observation contracts. | Do not claim that Reference Coupling is wrong; do not collapse its stronger semantics into current RefQ semantics. |

The current MS-R03 already cites McClean and Blincoe in the relevant
Related Work and framing passages. Kalliamvakou is not currently cited in
MS-R03; therefore the literature bridge is assessed as substantively
motivated but not fully source-closed in the manuscript itself. Direct
publisher pages were not relied on when blocked (ACM/ScienceDirect returned
HTTP 403/connection restrictions); DOI metadata was checked through
Crossref, and source-specific claims are kept at the narrow level above.

## 5. Related Work audit (§§2.2–2.5)

```text
RELATED_WORK_OBSERVATION_BRIDGE = WEAK
```

MS-R03 clearly covers repository/reference evidence, project-level relation
construction, endpoint eligibility, membership, aggregation and interpretation
boundaries (§§2.2 and 2.5). It also states that direct project-reference
aggregation does not automatically imply dependency semantics. However, it
does not yet provide a compact literature-backed bridge of the form:

```text
repository/network evidence value
→ data and network-boundary variation
→ observation-completeness implications
→ role/metric interpretation
→ broader-evidence, weaker-semantics RefQ contract
```

This is a framing/source gap, not a scientific conflict. It is the principal
reason a bounded MS-R04 semantic-source edit would be useful.

## 6. Introduction audit (§§1.2–1.4)

```text
INTRO_OBSERVATION_PROBLEM = EXPLICIT
```

§1.3 states that project-pair representation does not by itself express
source-observation completeness and that construction and observation
decisions must be made explicit. It further separates source role, target
role and the direction-ignored first-order view, explicitly warning against
reading expanded-target low out-degree as project behaviour. No introduction
repair is required for scientific correctness.

## 7. Discussion audit (§5)

```text
DISCUSSION_MEASUREMENT_VALIDITY_SYNTHESIS = SUFFICIENT
```

§5.1 makes source/target asymmetry an interpretation contract; §5.2 links
formalization to traceability and information loss; §5.3 bounds use to
candidate screening, structural inspection, manual-review prioritization and
follow-up analysis; §5.4 states that observation role, operator and
denominator cannot be mixed. This is a measurement-validity synthesis, not a
mere list of limitations.

## 8. Threats-to-Validity audit (§6)

```text
OBSERVATION_NETWORK_BOUNDARY_VALIDITY = WEAK
```

Current coverage is strong but distributed: §6.1 covers platform
observability and construct limits; §6.2 covers extraction/membership errors;
§6.3 covers GitHub/DBMS scope, seed-centred boundary and source-incomplete
expanded targets; §6.4 covers metric/statistical limits. The following are
not consolidated in one explicit validity statement:

- the target inclusion mechanism (targets enter because they are referenced
  by seed projects);
- metric populations and denominator contracts as a validity condition;
- missing expanded-target source behaviour is not observed zero;
- a direction-ignored first-order view does not restore missing source
  observations.

This is a bounded semantic-source gap, not a result defect.

## 9. Conclusion closure audit (§9)

| Closure question | Status | Evidence |
|---|---|---|
| What became measurable? | `SUPPORTED_AS_WRITTEN` | §9 first paragraph identifies traceable project-level RefQ from observable evidence and project-mappable subset. |
| What empirical knowledge was obtained? | `SUPPORTED_AS_WRITTEN` | §9 reports role asymmetry, broad first-order connectivity, Louvain seed sensitivity and label-mode-sensitive local subdomain differences. |
| Under what observation/metric conditions is it interpretable? | `SUPPORTED_BY_SYNTHESIS` | §9 and A.2/A.4 provide the seed-centred, role and statistical boundaries; a single concise condition sentence could make this closure more immediately visible. |
| What use is supported? | `SUPPORTED_AS_WRITTEN` | Candidate screening and structural inspection are explicitly bounded in §9 and §5.3. |
| What stronger claims require validation? | `SUPPORTED_AS_WRITTEN` | Dependency, task-resolution, causal-knowledge-flow and project-importance interpretations are explicitly excluded and require additional evidence. |

## 10. Platform-claim guard

| Claim | Audit result | Reason |
|---|---|---|
| `GENERAL_PLUG_AND_PLAY_PLATFORM_CLAIM` | `NOT_ALLOWED` | No cross-domain portability, plugin evaluation or general platform validation is reported. |
| `FULLY_AUTOMATED_RESEARCH_PLATFORM_CLAIM` | `NOT_ALLOWED` | The manuscript reports a staged empirical pipeline, not validated end-to-end automation. |
| `AI_AUTONOMOUS_RESEARCH_CLAIM` | `NOT_ALLOWED` | No AI orchestration experiment is part of MS-R03. |
| `CROSS_DOMAIN_GENERALITY_CLAIM` | `NOT_ALLOWED` | The study is bounded to GitHub DBMS projects and explicitly limits external validity. |
| `REUSABLE_ANALYTICAL_SUBSTRATE_CLAIM` | `ALLOWED_IF_TEXTUALLY_SUPPORTED` | The staged construction/measurement workflow, provenance and bounded follow-up analysis support this weaker claim; it must remain an implication, not a validated general platform contribution. |

## 11. Core academic sentences

| Sentence | Result | Rationale |
|---|---|---|
| C1 — “RefQ provides a traceable and observation-aware operationalization of project-level explicit-reference structure.” | `SUPPORTED_AS_WRITTEN` | Directly follows §§1.3–1.4, 3.3 and 9. |
| C2 — “It separates evidence construction from role-specific structural measurement by making endpoint eligibility, semantic membership, observation completeness, and metric semantics explicit.” | `SUPPORTED_AS_WRITTEN` | Each contract and role distinction is explicit in §§3.2–3.4 and 4.2. |
| C3 — “The DBMS study shows substantial structural heterogeneity, while the interpretation of the resulting measurements depends on observation roles, algorithmic choices, and label operationalization.” | `SUPPORTED_AS_WRITTEN` | Supported by §§4.2c, 4.3, 5.1 and A.4. |
| C4 — “RefQ therefore provides a reproducible substrate for structural inspection, candidate screening, and follow-up empirical analysis rather than a ground-truth representation of dependency, task resolution, or causal knowledge flow.” | `SUPPORTED_AS_WRITTEN` | §5.3 and §9 support the bounded uses; §§5.2, 6.1 and 9 explicitly reject stronger semantics. |

## 12. MS-R04 gate and bounded edit plan

```text
MS_R04_REQUIRED = YES
```

The gate is triggered by semantic-source gaps in A (Related Work bridge) and
D (Observation / Network Boundary Validity), while B (Introduction), C
(Discussion) and most of E (Conclusion) already pass. This does not authorize
an MS-R04 edit in this task.

| EDIT_ID | SECTION | CURRENT_FUNCTION | TARGET_FUNCTION | MAXIMUM_SCOPE | SCIENTIFIC_CHANGE_ALLOWED |
|---|---|---|---|---|---|
| `MSR04-FRAME-A` | §2.2 or §2.5 Related Work | Describes direct references, Reference Coupling, extraction and quotient precedents | Add one narrow literature bridge connecting repository/network evidence and construction boundaries to observation-aware metric interpretation; position Kalliamvakou, McClean and Blincoe complementarily | One paragraph; no new construct, RQ, contribution, result or citation-derived claim beyond the bounded literature uses in §4 | `NO` |
| `MSR04-FRAME-D` | §6 Threats to Validity | Distributes platform, source-completeness, extraction and statistical limits across subsections | Add a concise “Observation / Network Boundary Validity” paragraph covering target inclusion, metric populations/denominators, missing source behaviour ≠ observed zero, and the fact that direction-ignored views do not restore missing observations | One paragraph or subsection; restate existing contracts only | `NO` |
| `MSR04-FRAME-E` | §9 Conclusion (optional) | States boundaries and uses, with conditions partly distributed to Appendix A | If desired, add one sentence making role/observation/metric conditions explicit at the point of conclusion; do not add a new result | One sentence only, and only if editorial review finds the existing synthesis insufficient | `NO` |

No new RQ, contribution count, table, figure, numeric value, statistical
result, analysis output or scientific interpretation is permitted under this
plan.

## 13. Severity classification

```text
E0_COUNT = 0
E1_COUNT = 2
E2_COUNT = 0
INFO_COUNT = 4
```

| Severity | Finding |
|---|---|
| E0 | No scientific conflict or unsupported current result was found. |
| E1 | Related Work lacks a complete observation/network-boundary literature bridge; Threats lacks a consolidated observation/network-boundary validity statement. Both should be fixed before a JSS-facing semantic-source translation. |
| E2 | No optional-polish issue was required to reach the gate decision. |
| INFO | MS-R03 already supports the operationalization, role-aware measurement, introduction problem, discussion synthesis and bounded conclusion; Kalliamvakou is not currently cited; the exact conclusion condition sentence is editorially optional. |

## 14. No-change guards

```text
CURRENT_CHANGED = 0
MS_R03_SNAPSHOT_CHANGED = 0
RQ_TEXT_CHANGED = 0
CONTRIBUTION_TEXT_CHANGED = 0
SCIENTIFIC_VALUE_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
FIGURE_RERENDER = 0
TABLE_RELOCATION = 0
NEW_MANUSCRIPT_CANDIDATE_CREATED = 0
NEW_ACCEPTED_REVISION_CREATED = 0
```

The only intended repository addition in this task is this audit document.
Pre-existing untracked strategy files, submission-suggestion files and V3–V6
figure ZIPs remain untouched and are not part of the audit commit.

## 15. Decision

```text
DECISION = CH5_REFQ_JSS_FRAMING_AUDIT_PASS_MS_R04_BOUNDED_EDIT_REQUIRED
```

The JSS framing is scientifically supportable. A future, separately
authorized MS-R04 should make the two bounded semantic-source bridges explicit
without changing the accepted MS-R03 science.
