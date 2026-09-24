# Chapter 5 RefQ — STYLE-A03 EN-R02 Post-Edit Semantic Re-Audit

## Decision

```text
TASK = CH5_REFQ_STYLE_A03_EN_R02_POST_EDIT_SEMANTIC_REAUDIT
DECISION = CH5_REFQ_STYLE_A03_PASS_WITH_BOUNDED_CORRECTION_REQUIRED
E0 = 0
E1 = 1
E2 = 10
INFO = 59
```

The EN-R02 candidate has no identified scientific-value, formula, population,
causal, or claim-strength drift. One bounded traceability clarification remains:
the candidate names the seed-only induced and multi-seed target views but does
not define their edge and node sets, although current P0-v3 authority now
provides those definitions. Do not promote EN-R02 until that clarification is
made and re-audited. No scientific recomputation, figure rerender, or MS-R06 is
needed for this correction.

## Repository and manuscript identity

```text
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
TASK_BASE_HEAD = 0689a80be4112300632943914df46fe6033c6a6e
UPSTREAM_HEAD = 0689a80be4112300632943914df46fe6033c6a6e
AHEAD_BEHIND_BEFORE_AUDIT = 0 / 0

MS_R05 = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R05_BOUNDED_SEMANTIC_EDITORIAL_30491279.md
MS_R05_SHA256 = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
EN_R02 = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/temp_solution_discussion/chatgpt-claude/EN-R02_REFQ_JSS_BOUNDED_CORRECTION_CANDIDATE.md
EN_R02_SHA256 = F3D42BAF2034631CD5D2909A0DC2D43428742302BA605BBF489FBD5A6C00DB77
```

Both manuscript hashes match the task authority. The repository was clean of
tracked modifications at preflight. Four pre-existing untracked V3–V6 ZIPs
were preserved unchanged; they are not audit outputs.

Before the audit, the two untracked files below were identified as task prompts
(not freeze/audit deliverables) and moved from `docs/submission_suggestion/` to
`temp_solution_discussion/`. No tracked file was moved or edited, and the move
does not rewrite repository history or alter a remote commit.

| Prompt moved | SHA-256 before and after | Result |
|---|---|---|
| `MS_R05_Bounded_Semantic_Editorial_Correction_Prompt_v1.0.md` | `30593DA9D9687014ADFC88C89AD9FE212BDE92E07DFBF0108F8F8F15E240C834` | byte-identical |
| `MS_R05_Bounded_Semantic_Editorial_Correction_Prompt_v1.1_GHCoRE_Entity_Schema.md` | `3D5963E1CDD59A9ED195A09FC77B3644A994412F2E0E551A9E31B4B18442A898` | byte-identical |

## Inputs and traceability

All required local inputs were present. The task-specified SHA-256 checks
matched for MS-R05, EN-R02, and the five STYLE-R03 sidecars:

| Input | SHA-256 |
|---|---|
| `STYLE-R03_INPUT_OUTPUT_MANIFEST.md` | `52E9E339CE5A5A87A20C82172442A1C8A12C8789336245B7CD9A2D548E1105CA` |
| `STYLE-R03_SOURCE_UNIT_COVERAGE.csv` | `848189A5C9BC5ED92D4196A541039A8D75D569D35726349A1D1323E933893894` |
| `STYLE-R03_TARGET_BLOCK_DELTA.csv` | `24707626DD1049A9CE4779218706D364BE296F76762BE8F7B1D196CE2471BCF6` |
| `STYLE-R03_R02_EXECUTION_LOG.csv` | `1DD637D254F86005075B9C581FFFB4F19FC4B3405297D5E5A3A948BDC8959793` |
| `STYLE-R03_SELF_AUDIT.md` | `B6159C30DA9E98ECAFF8677B4DC4E743CA53F0EC6A8A8E87CBB119672D39D3C0` |

Historical/control inputs were cross-checked against the current R05 freeze,
delta bridge, manuscript manifest, current main/supplementary figure mappings,
Figure 4 eta-label provenance, post-R05 English route, and all four STYLE-A02
audit/plan artifacts. The A02 source-unit alignment and issue log were used as
traceability aids, not accepted as proof of the EN-R02 realization.

## Structural and scientific invariants

Independent checks on the actual MS-R05 and EN-R02 files give:

```text
SOURCE_UNIT_COUNT = 222
SOURCE_UNIT_COVERED = 222
SOURCE_UNIT_UNACCOUNTED = 0
MS_R05_DELTA_UNITS = 7
MS_R05_UNCHANGED_UNITS = 215
MS_R05_DELTA_PROPAGATED = 7 / 7

RQ_COUNT = 5
RQ_ORDER = RQ1 / RQ2a / RQ2b / RQ2c / RQ3
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = NO
CITATION_TOKEN_OCCURRENCES = 70 (STYLE-R01-EN: 70)
UNIQUE_CITATION_KEYS = 33
CITATION_KEY_SET_MATCH = YES
DISPLAY_FORMULA_COUNT = 12
DISPLAY_FORMULA_ID_SET_MATCH = YES
TABLE_NUMERIC_TOKEN_MULTISET_MATCH = YES (265 tokens each)
FIGURE_CAPTION_NUMERIC_MULTISET_MATCH = YES (37 tokens each)
SCIENTIFIC_VALUE_CHANGED = 0
TABLE_VALUE_CHANGED = 0
FIGURE_CAPTION_NUMERIC_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = NO
FIGURE_RERENDER = NO
```

All 118 STYLE-R03 changed-block rows have a corresponding candidate target (the
heading and Table 4.7 title were normalized to their actual, unmarked/marked
candidate locations). No changed block is unaccounted for. See the complete
row-level disposition in `ch5_refq_style_a03_en_r02_changed_block_audit.csv`.

The seven MS-R05 delta units were individually checked against the frozen
source bridge and EN-R02:

| Unit | Result |
|---|---|
| `THREAT-U002` | `THREAT-P002` preserves observable explicit-reference direction/context, project-association evidence, and the explicit non-measurement boundary for knowledge-flow processes. |
| `INTRO-U011` | `INTRO-P010` states expanded targets enter because seed projects reference them through admitted Reference records; no alternate admission path or “mainly” residue. |
| `RES-RQ1-U002` | Figure 1B uses referencing-entity types; Figure 1C remains grouped within event type. |
| `RES-RQ1-U005` | Table 4.1 and its result label use canonical “referencing entity type(s)” terminology; category is aligned without changing values. |
| `METH-U066` | `METH-P047` distinguishes the GH-CoRE schema abstraction and `src_entity_type`, `tar_entity_type`, and `event_type`; source-side metrics use `src_entity_type`. |
| `AVAIL-U004` | Appendix role is reproduction, traceability, and verification of boundaries already stated, not new interpretation. |
| `APP-U001` | Appendix introduction preserves the same bounded role and no longer claims a broader interpretive authority. |

## Changed-block and R02 issue adjudication

The changed-block ledger contains 118 rows: 109 MS-R05-unchanged-source rows
and 9 rows containing the seven MS-R05 delta units (some blocks include more
than one unit). Each row records source unit(s), source proposition, EN-R02
realization, qualifier/population/denominator/claim-strength checks, dependency
check, disposition, and whether correction remains.

The R02 ledger was joined against all 67 A02 issue rows and all 67 STYLE-R03
execution-log rows. Every issue is accounted for. Actual target IDs and the
STYLE-R03 realization notes were checked against EN-R02; no over-execution was
identified. Primary R03 status counts match the supplied execution log:

```text
SOURCE_DELTA_PROPAGATED = 4
ENGLISH_EDIT_EXECUTED = 32
TERMINOLOGY_EDIT_EXECUTED = 11
DOCUMENTATION_PLACEMENT_EXECUTED = 1
AUTHOR_DECISION_EXECUTED = 3
PACKAGING_DEFERRED = 5
NO_CHANGE_CONFIRMED = 10
DEFERRED_NEEDS_SOURCE_DEFINITION = 1
R02_ISSUE_LOG_COUNT = 67
UNACCOUNTED_R02_ISSUES = 0
```

The full issue-by-issue A02/R03/A03 comparison is in
`ch5_refq_style_a03_en_r02_issue_adjudication.csv`. Its 70 rows comprise the
67 R02 issues plus three separately registered packaging/provenance items.

## R02-009 — current-authority adjudication

```text
R02_009_AUTHORITY_STATUS = CURRENT_P0V3_AUTHORITY_CONFIRMS_DEFINITION
R02_009_CORRECTION_REQUIRED = YES (bounded wording/mapping clarification)
```

The current `supplemental/reference_quotient_v2/scripts/s3_observation_sensitivity.py`
uses the P0-v3 cross-project edge table, complete node registry, and 294-seed
manifest. Its `build_s3_view_inputs` implementation defines:

- `SEED_ONLY_INDUCED`: directed cross-project edges for which both source and
  target are seed projects; node domain is the complete seed manifest, so all
  294 seeds remain, including isolates.
- `MULTI_SEED_TARGET_VIEW`: first form the target set whose `target_project_id`
  is referenced by at least two distinct `source_project_id` values in the
  directed cross-project edge table; retain cross-project edges whose target
  is in that set; use the union of seed nodes and multi-seed targets as the
  node domain.

The v2 unit tests verify these view edge sets and deterministic node domains.
The P0-v3 S3 stage receipt and `observation_boundary_sensitivity.csv` show the
views are generated under the corrected P0-v3 authority; the Figure 3 source
manifest identifies that exact output as an input. Historical v1/v1.2 S3 code
and its execution report agree but are corroborative only; they are not the
basis of this decision.

EN-R02 currently says that Figure 3B compares the three named observation-
boundary views and glosses “seed,” but does not provide the two view
definitions. Add a concise, traceable definition in the manuscript/mapping
closure. This is a documentation-level view-definition clarification, not a
new result or a view change. It requires no S3 rerun, figure rerender, or
MS-R06. A03 does not execute the correction.

## MS-R05 promotion provenance metadata

```text
RECORDED_PROMOTION_SHA = 837f617e9d05fd3c933a8fd7f56a7e5e08bc7d0d
RECORDED_PROMOTION_SHA_VALID = NO
ACTUAL_PROMOTION_SHA = 837f61791adbe96a9565a2cc4fe1a6e377fa5662
ACTUAL_COMMIT_MESSAGE = docs(ch5): promote bounded semantic source MS-R05
PROMOTION_COMMIT_METADATA_REPAIR_REQUIRED = YES
```

Git confirms the recorded SHA is absent and the actual commit exists with the
expected message and the six-file MS-R05 promotion change set. This is E2
provenance metadata debt only; it does not change manuscript identity or the
validated MS-R05 SHA. A03 does not repair it.

## Claim-strength audit

```text
CLAIM_STRENGTHENING = NO
CAUSAL_DRIFT = NO
KNOWLEDGE_FLOW_MEASURE_CLAIM = NO
DEPENDENCY_GROUND_TRUTH_CLAIM = NO
PROJECT_IMPORTANCE_CLAIM = NO
SEMANTIC_COMMUNITY_DRIFT = NO
UNQUALIFIED_OSS_GENERALIZATION = NO
```

Knowledge-flow terms occur only as explicit limits/negations or in the
description of prior work; there is no positive RefQ measurement or proxy
claim. `RES-RQ1-P005` restricts the metric to Reference-evidence composition
and says it does not measure stronger constructs such as knowledge processes,
organizational properties, or capabilities. Prior-work dependency/community
descriptions remain attributed to their own cited scope.

## Observation-semantics audit

```text
OBSERVATION_SEMANTIC_DRIFT = NO
MISSING_AS_ZERO_DRIFT = NO
SOURCE_TARGET_POPULATION_CONFLATION = NO
DIRECTION_IGNORED_RESTORES_OBSERVATION_DRIFT = NO
```

Across Abstract, Introduction, Methods, Results, Discussion, Threats, and
Conclusion, the 294 seeds remain source-complete and expanded targets remain
source-incomplete. Expanded targets enter because seeds reference them; their
unobserved source behavior is not treated as zero. RQ2a uses source-complete
seeds, RQ2b the observable target population, and RQ2c the first-order
direction-ignored view. The text explicitly states that ignoring direction
does not restore missing source observations or yield a fully observed
ecosystem network. This is population-specific interpretation, not a dataset
defect apology.

## Figure, table, and formula audit

```text
FIGURE1B = referencing-entity-type composition (source side)
FIGURE1C = target-membership shares within event type
FIGURE2 = source/target roles under seed-centered observation
FIGURE3 = first-order direction-ignored structure + observation-boundary and random-seed sensitivity
FIGURE4 = rank eta-squared (η_H²) + BH-FDR
FORMULA_SEMANTIC_CHANGE = 0
FIGURE_ASSET_CHANGE = 0
```

Current figure mappings and Figure 4 provenance support these interpretations.
All 12 formula IDs match STYLE-R01-EN, and the numeric multisets in table
blocks and figure captions are unchanged. The appendix and formula text do
not introduce new semantics for (Q=M^\top R_PM), first-/second-order
operators, or (K=X\Phi X^\top).

## Deferred packaging and provenance debt

The following are not EN-R02 semantic blockers and remain for a distinct JSS
packaging task:

- R02-017, R02-024, R02-025, R02-026, and R02-041;
- R02-065 bibliography ordering/key formatting;
- the “no preset robustness alert” wording (author/packaging review);
- verification of applicable JSS requirements;
- anonymization and package declarations;
- MS-R05 promotion SHA metadata repair.

These are classified as E2. Do not expand this semantic audit into venue
formatting or package declarations.

## Outputs and next task

Only the three authorized A03 audit artifacts were added to the repository:

```text
docs/submission_suggestion/ch5_refq_style_a03_en_r02_post_edit_semantic_reaudit.md
docs/submission_suggestion/ch5_refq_style_a03_en_r02_issue_adjudication.csv
docs/submission_suggestion/ch5_refq_style_a03_en_r02_changed_block_audit.csv
```

EN-R02, MS-R05, figures, and scientific outputs were not edited. The branch
must be committed and pushed with only these three audit artifacts staged;
the four pre-existing ZIPs must remain untracked and untouched.

```text
NEXT_TASK = CH5_REFQ_STYLE_R04_POST_A03_BOUNDED_CORRECTION
```
