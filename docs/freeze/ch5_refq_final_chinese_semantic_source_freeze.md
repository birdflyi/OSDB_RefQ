# Chapter 5 RefQ Final Chinese Semantic Source Freeze

## 1. Decision

`CH5_REFQ_FINAL_CHINESE_SEMANTIC_SOURCE_FREEZE_PASS`

This is a read-only final semantic-source freeze and translation-handoff
authority registration. It creates no manuscript revision and leaves the JSS
requirement debt recorded by SUB-A02 open.

## 2. Repository authority

```text
TASK = CH5_REFQ_FINAL_CHINESE_SEMANTIC_SOURCE_FREEZE
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
TASK_BASE_REPOSITORY_HEAD = fa5b5e785866fb86bfee2e9c8c5be2e78c999221
LOCAL_HEAD_BEFORE = fa5b5e785866fb86bfee2e9c8c5be2e78c999221
REMOTE_HEAD_BEFORE = fa5b5e785866fb86bfee2e9c8c5be2e78c999221
AHEAD_BEHIND_BEFORE = 0 / 0
```

Only this freeze document is authorized for repository creation. The four
pre-existing V3-V6 ZIP files remain untracked and untouched.

## 3. Accepted MS-R04 identity

```text
FINAL_CHINESE_SEMANTIC_SOURCE_REVISION = MS-R04
FINAL_CHINESE_SEMANTIC_SOURCE_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
FINAL_CHINESE_SEMANTIC_SOURCE_PATH = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md
FINAL_CHINESE_SEMANTIC_SOURCE_MUTABILITY = IMMUTABLE
AUTHORITATIVE_FOR_ENGLISH_TRANSLATION = YES
AUTHORITATIVE_FOR_JSS_SEMANTIC_CONTENT = YES

CURRENT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
MS_R04_SNAPSHOT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
CURRENT_EQUALS_MS_R04_SNAPSHOT = YES
MS_R04_SNAPSHOT_READ_ONLY = YES
```

The immutable snapshot, rather than the editable CURRENT alias, is the primary
translation source. No MS-R05, MS-R04.1, duplicate Chinese snapshot, or English
file is created.

## 4. Target venue authority

```text
TARGET_JOURNAL = Journal of Systems and Software
TARGET_TRACK = RESEARCH_PAPER
EDITORIAL_MANAGER_EXACT_ARTICLE_TYPE_LABEL = Research Paper
EDITORIAL_MANAGER_EXACT_ARTICLE_TYPE_LABEL_VERIFIED = YES
PRIMARY_TARGET_STATUS = FROZEN
SPECIAL_TRACK_SELECTED = NO
SPECIAL_ISSUE_SELECTED = NO
VSI_SELECTED = NO
```

The target decision remains
`CH5_REFQ_TARGET_VENUE_FREEZE_JSS_RESEARCH_PAPER_PASS`. It is not reopened.

## 5. SUB-A02 and MS-R05 gate

SUB-A02 remains the authority for JSS requirement debt:

```text
SUB_A02_DECISION = CH5_REFQ_SUB_A02_PASS_NO_MS_R05_REQUIRED
VERIFIED_JSS_REQUIREMENT_COUNT = 3
PARTIALLY_VERIFIED_JSS_REQUIREMENT_COUNT = 5
UNVERIFIED_JSS_REQUIREMENT_COUNT = 28
POTENTIAL_MS_R05_COUNT = 0
MS_R05_REQUIRED = NO
SEMANTIC_SOURCE_READY_FOR_ENGLISH_TRANSLATION = YES
PACKAGING_CAN_PROCEED_AFTER_TRANSLATION = YES
E0_COUNT = 0
E1_COUNT = 0
```

This means no verified current JSS rule requires another Chinese semantic-source
revision. It does not mean that all JSS Research Paper submission requirements
have been verified. The 28 unverified items remain downstream preparation debt.

## 6. Final Chinese semantic-source identity

The final Chinese semantic source is exactly the accepted MS-R04 snapshot:

```text
REVISION = MS-R04
SHA256 = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
SNAPSHOT = versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md
MUTABILITY = IMMUTABLE
CURRENT = editable alias only; same accepted bytes
```

Accepted lineage remains MS-R01, MS-R02, MS-R03, then MS-R04. No accepted
identity field, manifest entry, or sidecar is changed by this freeze.

## 7. Frozen paper centre

> RefQ provides a traceable and observation-aware operationalization of
> project-level explicit-reference structure.

The translation must distinguish observable fine-grained Reference evidence
from the project-level RefQ relation, and must distinguish a project-level
structural relation from dependency, task-resolution, and causal knowledge-flow
ground truth. RefQ is not elevated to any of those stronger semantics.

## 8. Frozen methodological chain

```text
fine-grained explicit Reference evidence
-> endpoint eligibility
-> semantic membership
-> aggregation
-> RefQ / RefQN
-> asymmetric source observation
-> role-aware measurement
-> empirical characterization
-> bounded interpretation
```

English translation may improve sentence cohesion and terminology, but may not
change this logical order or its semantic dependence.

## 9. Frozen observation contract

```text
294 analysis seeds = source-complete under the current observation contract
expanded targets = source-incomplete
```

Expanded targets enter because seed projects reference them; they are not an
independently source-sampled project population. Missing or unobserved
expanded-target source behavior is not observed zero activity.

```text
RQ2a = source-complete seed population
RQ2b = observable target population
RQ2c = first-order direction-ignored derived structural view
```

Ignoring direction does not restore missing source observations. The
seed-centered RefQN is not a fully observed OSS ecosystem graph.

## 10. Frozen RQs

```text
RQ_COUNT = 5
RQ_TEXT_CHANGED = 0
```

The translation must preserve the five semantic functions `RQ1`, `RQ2a`,
`RQ2b`, `RQ2c`, and `RQ3`. RQ2a/RQ2b/RQ2c must not be merged, and no new RQ
may be introduced.

## 11. Frozen contribution structure

```text
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0
```

The accepted hierarchy is:

1. RefQ/project-level operationalization and construction contract;
2. endpoint, membership, and observation-boundary support;
3. observation-aware empirical structural characterization;
4. reusable weak-semantic relation asset and interface positioning.

The five venue-fit dimensions in the target-freeze document are not five
manuscript contributions. No platform, plug-and-play, AI, cross-domain, or
generic graph-algorithm contribution may be added.

## 12. Frozen first-order boundary

The core contribution is first-order RefQ/RefQN relation analysis. The current
scope excludes:

```text
QQ^T
Q^TQ
K = X Phi X^T
shared-reference projection
shared-neighbor projection
second-order similarity networks
```

These remain future-work interfaces, not current results or contributions.

## 13. Frozen empirical interpretation

Louvain sensitivity is a positive-but-bounded finding: structural modularity is
present, but one partition is not a stable semantic taxonomy. The RQ3
cross-mode robust feature count is:

```text
RQ3_CROSS_MODE_ROBUST_FEATURE_COUNT = 0
```

This means subdomain effects are not invariant to label operationalization. It
must not be rewritten as either a universal failure or a universal effect.

## 14. Scientific, citation, and display state

```text
SCIENTIFIC_BASELINE = P0-v3
301 candidate projects
294 analysis seeds
3,748,078 scanned
3,747,958 admitted
120 out-of-seed
1,586,047 quotient-eligible weight
138,974 cross-project weight
6,506 node domain
9,884 directed edges including loops
289 self-loops
9,595 directed cross-project edges
9,547 first-order undirected edges
6,367 LCC nodes
9,462 LCC undirected edges
35 canonical Louvain communities
MODULARITY = 0.7969220043681785
RQ3_CROSS_MODE_ROBUST_FEATURE_COUNT = 0

CITATION_TOKEN_COUNT = 70
UNIQUE_CITATION_KEY_COUNT = 33
BIBLIOGRAPHY_ENTRY_COUNT = 33
MAIN_TEXT_TABLE_BLOCK_COUNT = 14
FIGURE_CAPTION_COUNT = 4
FIGURES_1_3_AUTHORITY = figures/ch5_refq/p0v3_final_v6
FIGURE_4_AUTHORITY = figures/ch5_refq/p0v3_final_v6_e01_eta_label
```

These are identity and prior-QA anchors only. No scientific code is rerun and
no value is recomputed. The external frozen `1,447,073` self-loop evidence
weight need not be printed in the manuscript.

## 15. Data, code, and availability boundary

```text
ZENODO_DOI = 10.5281/zenodo.18817348
```

The existing public relation/data release is distinct from the final-submission
replication package, and neither is a blanket full GH_CoRE code release.
Future JSS-facing availability wording may improve clarity but must preserve
the same factual scope, platform/rights caveats, and release/version boundary.

## 16. Paper A versus future-paper boundary

```text
PAPER_A = current RefQ/JSS manuscript
PAPER_B = future contract-based reproducible Reference-analysis workbench
PAPER_C = future cross-ecosystem RefQ transportability/generalization
PAPER_D = future agentic empirical-SE workflow
```

Claims from Papers B, C, or D must not be imported into the English
translation of Paper A.

## 17. JSS requirement debt

```text
JSS_REQUIREMENTS_FULLY_VERIFIED = NO
JSS_GUIDE_DETAIL_CLOSURE_COMPLETE = NO
UNVERIFIED_JSS_REQUIREMENT_COUNT = 28
JSS_REQUIREMENT_DEBT_AUTHORITY = docs/submission_suggestion/ch5_refq_sub_a02_jss_author_guideline_and_artifact_mapping_2026-09-22.md
```

SUB-A02's 28 unverified items remain downstream submission-preparation debt.
This freeze does not claim that JSS requirements are fully closed.

## 18. Future-requirement reopening policy

If a future authoritative JSS source verifies a hard requirement that requires
semantic content absent from MS-R04, cannot be solved by English translation,
and cannot be solved by packaging or submission metadata, do not modify this
frozen snapshot. Open an explicitly authorized MS-R05 from:

```text
PARENT_REVISION = MS-R04
PARENT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
```

This possibility does not prevent the current translation handoff.

## 19. English translation invariant contract

The English translation may restructure sentences locally for idiomatic
academic English, choose conventional software-engineering terminology,
normalize tense/voice, improve cohesion, adapt section-local rhetoric for JSS,
and create a fresh English Abstract from the Chinese source.

It must not add scientific facts, delete qualifications, strengthen causality
or dependency semantics, turn observation absence into zero, universalize DBMS
findings, suppress negative/non-robust findings, change RQs or contribution
count, change metric definitions or numerical results, change citations without
authorization, import platform/AI claims, or silently implement an unverified
JSS requirement. Translation is semantic preservation, not manuscript redesign.

## 20. English Abstract policy

```text
FINAL_ENGLISH_ABSTRACT_PENDING = YES
CHINESE_ABSTRACT_IS_SEMANTIC_AUTHORITY = YES
LEGACY_ENGLISH_ABSTRACT_SUBMISSION_AUTHORITY = NO
```

The next English workflow must generate a fresh authoritative English Abstract
from the immutable MS-R04 Chinese source. No English Abstract is created here.

## 21. Next-task handoff

```text
SOURCE_REVISION = MS-R04
SOURCE_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
SOURCE_SNAPSHOT = versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md
AUTHORITATIVE_CHINESE_SOURCE = YES
NEXT_TASK = CH5_REFQ_LANG_A01_AUTHORITATIVE_ENGLISH_TRANSLATION
```

The next English manuscript must be a separate candidate lineage and must not
overwrite CURRENT or the immutable Chinese snapshot.

## 22. No-change guards

```text
CURRENT_CHANGED = 0
MS_R04_SNAPSHOT_CHANGED = 0
MS_R03_SNAPSHOT_CHANGED = 0
MS_R02_SNAPSHOT_CHANGED = 0
MS_R01_SNAPSHOT_CHANGED = 0
CANDIDATE_CHANGED = 0
SIDECAR_CHANGED = 0
MANUSCRIPT_VERSION_MANIFEST_CHANGED = 0
TARGET_VENUE_FREEZE_DOCUMENT_CHANGED = 0
SUB_A02_DOCUMENT_CHANGED = 0
MANUSCRIPT_TEXT_CHANGED = 0
TITLE_CHANGED = 0
ABSTRACT_CHANGED = 0
KEYWORDS_CHANGED = 0
RQ_TEXT_CHANGED = 0
CONTRIBUTION_TEXT_CHANGED = 0
SCIENTIFIC_VALUE_CHANGED = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0
CITATION_STATE_CHANGED = 0
BIBLIOGRAPHY_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
TABLE_RELOCATION_COUNT = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
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
OTHER_TRACKED_FILE_CHANGE_COUNT = 0
```

## 23. Final freeze decision

```text
FINAL_FREEZE_CREATES_NEW_MS_REVISION = NO
MS_R05_CREATED = NO
MS_R05_REQUIRED = NO
JSS_REQUIREMENTS_FULLY_VERIFIED = NO
SEMANTIC_SOURCE_READY_FOR_ENGLISH_TRANSLATION = YES
FINAL_ENGLISH_ABSTRACT_PENDING = YES
E0_COUNT = 0
E1_COUNT = 0
E2_COUNT = 4
INFO_COUNT = 1
DECISION = CH5_REFQ_FINAL_CHINESE_SEMANTIC_SOURCE_FREEZE_PASS
```

