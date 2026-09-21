# Chapter 5 RefQ — MS-R04 Bounded Observation-Framing Final QA

```text
TASK = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_FINAL_QA
QA_MODE = READ_ONLY_FINAL_QA
QA_REPOSITORY_HEAD = 620a1e41feb4906595beb872b463f4ee865a574f
BRANCH = ch5-refq-repository-identity-correction-v1
BASE_ACCEPTED_REVISION = MS-R03
```

This QA evaluates the post-E01 MS-R04 candidate for promotion readiness. It
does not edit the candidate, CURRENT, the MS-R03 snapshot, or any scientific
asset, and it does not promote MS-R04.

## 1. Authority and identity

| Item | Value | Result |
|---|---|---|
| MS-R03 base SHA | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| CURRENT SHA | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| MS-R03 snapshot SHA | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| CURRENT equals snapshot | YES | PASS |
| Active MS-R04 candidate | `working/MS-R04_BOUNDED_OBSERVATION_FRAMING_CANDIDATE.md` | present |
| Active candidate SHA | `F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549` | PASS |
| Historical pre-E01 SHA | `8F094C7187A9258F7053B5097862AE335C4183E07F731968D95C98202DA89E98` | historical only |
| Candidate decision before QA | `CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_CANDIDATE_PASS_READY_FOR_FINAL_QA` | verified |
| E01 decision before QA | `CH5_REFQ_MS_R04_E01_LANGUAGE_NORMALIZATION_PASS_READY_FOR_FINAL_QA` | verified |

Required strategy, framing-freeze, prior audit, and candidate audit documents
were present and read for this QA.

## 2. Independent full-diff audit

The complete MS-R03 snapshot to active-candidate diff was independently
recomputed. The candidate contains only the two bounded framing paragraphs and
the one required Kalliamvakou bibliography entry.

```text
TOTAL_CHANGED_HUNK_COUNT = 3
FRAME_A_HUNKS = 1
FRAME_D_HUNKS = 1
BIB_HUNKS = 1
FRAME_E_HUNKS = 0
UNMAPPED_CHANGED_HUNKS = 0
UNAUTHORIZED_CHANGED_HUNKS = 0
```

No existing MS-R03 line was deleted or rewritten; the base file is a complete
linewise subsequence of the candidate.

## 3. FRAME-A semantic and citation QA

```text
FRAME_A_COMPLEMENTARY_POSITIONING = PASS
FRAME_A_OBSERVATION_BRIDGE = PASS
FRAME_A_STRONGER_SEMANTICS_CONDITION = PASS
FRAME_A_REFQ_DIFFERENTIATION = PASS
```

The Chinese paragraph establishes that repository/network evidence has
empirical value; repository sampling, data semantics and network construction
condition interpretation; stronger dependency-oriented semantics require a
specifically validated relation scope; Reference Coupling is a precedent under
its own scope; and RefQ retains a broader heterogeneous Reference evidence
universe with explicit endpoint eligibility, semantic membership, observation
completeness and metric interpretation.

```text
ADVERSARIAL_PRIOR_WORK_CLAIM_COUNT = 0
```

The forbidden readings “Reference Coupling is wrong”, “prior network research
is invalid”, “RefQ disproves Reference Coupling”, and equivalent claims were
absent.

### Citation-support alignment

```text
KALLIAMVAKOU_CLAIM_ALIGNMENT = PASS
MCCLEAN_CLAIM_ALIGNMENT = PASS
BLINCOE_CLAIM_ALIGNMENT = PASS
```

Kalliamvakou is used only for GitHub/repository mining sampling and data
interpretation care; McClean is used for variation in OSS network sources and
constructions; Blincoe is used for a validated dependency-oriented
Reference-Coupling precedent without adversarial criticism. DOI metadata for
the Kalliamvakou record was checked through Crossref.

## 4. FRAME-D observation-validity QA

```text
FRAME_D_TARGET_INCLUSION = PASS
FRAME_D_SOURCE_COMPLETENESS = PASS
FRAME_D_MISSING_NOT_ZERO = PASS
FRAME_D_ROLE_POPULATION_MAPPING = PASS
FRAME_D_DIRECTION_IGNORED_BOUNDARY = PASS
```

The paragraph explicitly states that expanded targets enter because they are
referenced by the 294 seeds, are not independently source-sampled, and are
source-incomplete while seeds are source-complete. It explicitly rejects the
interpretation of missing/unobserved expanded-target source behavior as
observed zero activity. It maps RQ2a to source-complete seeds, RQ2b to
observable targets, and RQ2c to the first-order direction-ignored structural
view. It also states that ignoring direction cannot restore missing source
observations or create a fully observed ecosystem graph.

## 5. Manuscript-wide observation-role consistency

```text
INTRO_OBSERVATION_PROBLEM = EXPLICIT
METHODS_OBSERVATION_CONTRACT = CONSISTENT
RQ2A_SOURCE_ROLE = CONSISTENT
RQ2B_TARGET_ROLE = CONSISTENT
RQ2C_STRUCTURAL_VIEW = CONSISTENT
RESULTS_ROLE_INTERPRETATION = CONSISTENT
DISCUSSION_MEASUREMENT_VALIDITY_SYNTHESIS = SUFFICIENT
THREATS_OBSERVATION_NETWORK_BOUNDARY = SUFFICIENT
CONCLUSION_MEASUREMENT_CONDITION_CLOSURE = SUFFICIENT
APPENDIX_OBSERVATION_BOUNDARY = CONSISTENT
MISSING_SOURCE_BEHAVIOR_AS_ZERO_COUNT = 0
```

The same contract is preserved in §1.3, §§3.3.4/3.4, §§4.2a–4.2c, §§5.1/5.4,
§6.3, §9 and Appendix A. No expanded-target unobserved source behavior is
treated as zero anywhere in the candidate.

## 6. Elevated framing and core sentences

```text
OPERATIONALIZATION = SUPPORTED
TRACEABILITY = SUPPORTED
OBSERVATION_AWARENESS = SUPPORTED
ROLE_DEPENDENCE = SUPPORTED
OBSERVATION_BOUNDING = SUPPORTED
METRIC_DEPENDENCE = SUPPORTED
LABEL_OPERATIONALIZATION_SENSITIVITY = SUPPORTED

C1 = SUPPORTED
C2 = SUPPORTED
C3 = SUPPORTED
C4 = SUPPORTED
```

The candidate retains the frozen paper centre and meta-finding: explicit-
reference structure is measurable, but interpretation is role-dependent,
observation-bounded and metric-dependent, with additional label-
operationalization sensitivity for RQ3.

## 7. Scientific invariance audit

```text
SCIENTIFIC_BASELINE = P0-v3
RQ_COUNT = 5
RQ_TEXT_CHANGED = 0
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0
CONTRIBUTION_TEXT_CHANGED = 0
TITLE_CHANGED = 0
ABSTRACT_CHANGED = 0
KEYWORDS_CHANGED = 0
METHODS_SCIENTIFIC_SEMANTICS_CHANGED = 0
RESULTS_CHANGED = 0
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0
Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
DEDUP_RULE_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_SECOND_ORDER_BOUNDARY_CHANGED = 0
STATISTICAL_TEST_CHANGED = 0
EFFECT_SIZE_DEFINITION_CHANGED = 0
FDR_FAMILY_CHANGED = 0
LABEL_MODE_CHANGED = 0
CROSS_MODE_RESULT_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
```

## 8. Frozen numeric-anchor guard

The following anchors were spot-checked against the candidate and the MS-R03
base. All present anchors are unchanged. `1,447,073` is not printed in either
manuscript version, so it has no manuscript mutation; its frozen authority is
external to this semantic-source QA.

```text
301 candidate projects = UNCHANGED
294 analysis seeds = UNCHANGED
3,748,078 scanned = UNCHANGED
3,747,958 admitted = UNCHANGED
120 out-of-seed = UNCHANGED
1,586,047 quotient-eligible/weight = UNCHANGED
1,447,073 self-loop weight = ABSENT_IN_BOTH_MANUSCRIPT_VERSIONS
138,974 cross-project weight = UNCHANGED
6,506 node domain = UNCHANGED
9,884 directed edges including loops = UNCHANGED
289 self-loops = UNCHANGED
9,595 directed cross-project edges = UNCHANGED
9,547 undirected first-order edges = UNCHANGED
6,367 LCC nodes = UNCHANGED
9,462 LCC undirected edges = UNCHANGED
35 canonical Louvain communities = UNCHANGED
0.7969220043681785 modularity = UNCHANGED
RQ3 cross-mode robust features = 0 / UNCHANGED

FROZEN_NUMERIC_ANCHORS = PASS
```

## 9. Citation and bibliography QA

```text
CITATION_TOKEN_OCCURRENCES = 67 -> 70
UNIQUE_CITATION_KEYS = 32 -> 33
BIBLIOGRAPHY_ENTRIES = 32 -> 33
SOLE_NEW_KEY = kalliamvakou2014promises
MISSING_CITATION_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
UNEXPLAINED_CITATION_DELTA = 0
UNEXPLAINED_BIBLIOGRAPHY_DELTA = 0
CITATION_AUDIT = PASS
```

The delta is fully explained by FRAME-A and its required Kalliamvakou entry.

## 10. Language and editorial coherence

```text
FRAME_A_PARAGRAPH_LEVEL_LANGUAGE = CHINESE
FRAME_D_PARAGRAPH_LEVEL_LANGUAGE = CHINESE
FULL_ENGLISH_PARAGRAPH_INSERTION_COUNT = 0
LANGUAGE_COHERENCE = PASS
LOCAL_REDUNDANCY = ACCEPTABLE
```

English technical terms remain where they preserve established manuscript
precision. The two paragraphs match the surrounding Chinese semantic-source
style, contain no adversarial rhetorical shift, and introduce neither a new
RQ nor a new contribution.

## 11. FRAME-E gate

```text
FRAME_E_REQUIRED = NO
```

§9 already closes what became measurable, the observed structural findings,
observation/metric boundaries, supported uses, and unsupported stronger
semantics. No conclusion edit is required.

## 12. Platform, display, availability and provenance guards

```text
GENERAL_PLUG_AND_PLAY_PLATFORM_CLAIM_COUNT = 0
FULLY_AUTOMATED_RESEARCH_PLATFORM_CLAIM_COUNT = 0
AI_AUTONOMOUS_RESEARCH_CLAIM_COUNT = 0
CROSS_DOMAIN_VALIDATED_FRAMEWORK_CLAIM_COUNT = 0
RESEARCH_EFFICIENCY_IMPROVEMENT_CLAIM_COUNT = 0

MAIN_TEXT_TABLE_BLOCK_COUNT_UNCHANGED = YES
TABLE_CONTENT_CHANGED = 0
TABLE_RELOCATION_COUNT = 0
FIGURE_CAPTION_COUNT_UNCHANGED = YES
FIGURE_CAPTION_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0

AVAILABILITY_SCOPE_UNCHANGED = PASS
ZENODO_DOI_UNCHANGED = PASS
ZENODO_DOI = 10.5281/zenodo.18817348
```

The candidate preserves the distinction between the existing public
relation/data release and the final-submission replication package, and does
not strengthen claims about full GH_CoRE code release.

## 13. Severity and promotion readiness

```text
E0_COUNT = 0
E1_COUNT = 0
E2_COUNT = 0
INFO_COUNT = 1
PROMOTION_READY = YES
```

The sole INFO item is that `1,447,073` is an external frozen authority value
not printed in either manuscript version. No blocking semantic, scientific or
editorial finding remains.

## 14. No-change guards

```text
CANDIDATE_CHANGED_BY_QA = 0
CURRENT_CHANGED = 0
MS_R03_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_ACCEPTED_SNAPSHOT_CREATED = 0
MS_R04_PROMOTED = 0
SCIENTIFIC_RECOMPUTATION = 0
```

## 15. Decision and handoff

```text
DECISION = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_FINAL_QA_PASS_READY_FOR_PROMOTION
NEXT_TASK = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_PROMOTION
```

Promotion was not started in this QA task.
