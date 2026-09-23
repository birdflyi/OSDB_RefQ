# Chapter 5 RefQ English-Primary Style Reconstruction Route

## 1. Route identity

```text
TASK = CH5_REFQ_STYLE_ROUTE_A01_ENGLISH_PRIMARY_REGISTRATION
DECISION = CH5_REFQ_STYLE_ROUTE_A01_ENGLISH_PRIMARY_REGISTRATION_PASS
TASK_BASE_REPOSITORY_HEAD = 8085883b0720cc5e48ab14cdb25fdac0fd2dc991
BRANCH = ch5-refq-repository-identity-correction-v1
LANGUAGE_ROUTE = ENGLISH_PRIMARY_WITH_CHINESE_SEMANTIC_ANCHOR
```

This document registers workflow metadata only. It creates no manuscript
revision, English prose, blueprint, figure, or scientific result.

## 2. Scientific / semantic authority

```text
SCIENTIFIC_BASELINE = P0-v3
SCIENTIFIC_SEMANTIC_AUTHORITY = MS-R04
MS_R04_SHA256 = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
MS_R04_CURRENT_EQUALS_IMMUTABLE_SNAPSHOT = YES
```

The accepted Chinese MS-R04 snapshot remains the sole scientific and semantic
authority. No English draft, STYLE output, or translation becomes authoritative
by virtue of this route registration. The frozen paper centre is:

> RefQ provides a traceable and observation-aware operationalization of
> project-level explicit-reference structure.

The preserved chain is:

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

Interpretation remains role-dependent, observation-bounded, and
metric-dependent. RQ3 conclusions are additionally sensitive to label
operationalization. This registration imports no scientific claim.

## 3. STYLE-A00 acceptance

```text
STYLE_A00_SOURCE_DECISION = PASS_WITH_BOUNDED_CORPUS_GAPS
STYLE_A00_PROJECT_ACCEPTANCE = PASS_READY_FOR_STYLE_A00B
```

The accepted STYLE-A00 report documents four bounded, nonblocking corpus gaps:

1. limited direct corpus precedent for measurement-level Discussion;
2. no exact corpus template for the target Conclusion sequence;
3. no exact corpus precedent for source-complete / target-incomplete
   observation asymmetry;
4. only one direct JSS rhetoric reference in the corpus.

MS-R04 supplies scientific content and author decisions supply the selected
paper form; the corpus is presentation scaffolding only. These gaps do not
authorize scientific invention. The report records
`NO_SCIENTIFIC_CLAIM_IMPORTED = TRUE` and
`MANUSCRIPT_REWRITE_OCCURRED = NO`.

## 4. Language-route decision

```text
LANGUAGE_ROUTE = ENGLISH_PRIMARY_WITH_CHINESE_SEMANTIC_ANCHOR
OLD_PLANNED_ROUTE = MS-R04 -> Chinese STYLE-R01 -> English translation -> English candidate
OLD_PLANNED_ROUTE_STATUS = SUPERSEDED_FOR_ACTIVE_WORKFLOW
```

The active route uses a bilingual semantic / English-rhetoric blueprint and
direct English rhetorical reconstruction. This changes workflow order only;
MS-R04 remains the sole scientific and semantic authority until a separately
authorized manuscript revision is promoted.

## 5. Why English-primary

The route is selected because target peer review is conducted on English prose,
the rhetoric corpus is English, and claim strength, tense, voice, information
structure, qualification, and positioning can be evaluated directly at the
English sentence level. A polished Chinese STYLE intermediate would introduce
another cross-language transformation. Semantic control is retained through
explicit bilingual ledgers, source-unit traceability, and a later Codex
cross-language alignment audit. This is not permission for free translation.

## 6. Required STYLE-A00B artifacts

STYLE-A00B must produce all six artifacts:

```text
SOURCE_UNIT_MAP
CANONICAL_TERMINOLOGY_LEDGER
CLAIM_STRENGTH_LEDGER
SECTION_RECONSTRUCTION_BLUEPRINT
REDUNDANCY_BOUNDARY_MAP
RHETORICAL_CHANGE_RISK_MAP
```

They are mandatory because STYLE-A01-EN will create English prose directly
from the Chinese semantic authority. Missing any artifact blocks the
STYLE-A00B gate.

## 7. STYLE-A01-EN semantic-control model

```text
STYLE_A01_EN_ROLE = ENGLISH_RHETORICAL_CANDIDATE
STYLE_A01_EN_SCIENTIFIC_AUTHORITY = NO
STYLE_A01_EN_SEMANTIC_AUTHORITY = NO
```

Every meaningful English unit must trace to one or more `SOURCE_UNIT_MAP` IDs
from MS-R04. The later audit compares each MS-R04 source unit with its
STYLE-R01-EN English unit rather than relying only on whole-document
similarity. Claim strength, qualifications, observation roles, relation
semantics, RQ/contribution meanings, empirical findings, and validity
boundaries remain governed by MS-R04.

## 8. EN-R01 role

```text
EN_R01_ROLE = STRUCTURAL_TRANSLATION_BASELINE_ONLY
EN_R01_PROSE_AUTHORITY = NO
EN_R01_SEMANTIC_AUTHORITY = NO
EN_R01_TERMINOLOGY_AUTHORITY = NO
EN_R01_NUMERIC_AUTHORITY = NO
EN_R01_FORMULA_AUTHORITY = NO
EN_R01_FIGURE_REFERENCE_AUTHORITY = NO
EN_R01_PROMOTION_ELIGIBLE = NO
```

EN-R01 may be used only for section-presence, heading-hierarchy,
rough-block-coverage, table-block-count, and citation-key-set comparisons.
Scientific, numeric, formula, figure, and terminology checks must use MS-R04
and current authority records directly.

## 9. Discussion route

```text
DISCUSSION_ROUTE = MEASUREMENT_AND_INTERPRETATION_PRIMARY
STAKEHOLDER_IMPLICATION_EXPANSION = NO
```

The Discussion is driven by the paper's existing contribution and evidence.
Style references may improve readability, paragraph architecture, transition
efficiency, qualification, information order, and presentation maturity only.
They may not change scientific facts, the bottom-level logic chain,
observation or relation semantics, RQ or contribution semantics, empirical
findings, or validity boundaries. Preserve only bounded use cases already in
MS-R04; do not invent recommendations for developers, maintainers, vendors,
educators, platform teams, or other stakeholders.

## 10. Current figure authority

```text
MAIN_MAPPING = docs/freeze/ch5_refq_main_figure_text_mapping_current.md
MAIN_MAPPING_CLOSED = YES
SUPPLEMENTARY_MAPPING = docs/freeze/ch5_refq_supplementary_figure_mapping_current.md
SUPPLEMENTARY_INVENTORY_RESOLVED = YES
MAIN_SUPPLEMENT_NAMESPACE_SEPARATED = YES
FIGURE4_PROVENANCE_CLOSURE = docs/freeze/ch5_refq_figure4_eta_label_provenance_closure.md
FIGURE4_PROVENANCE_CLOSURE_PENDING = NO
FIGURE4_SCIENTIFIC_MISMATCH = NO
CURRENT_FIGURE_SCIENTIFIC_BLOCKER_COUNT = 0
CURRENT_FIGURE_MAPPING_BLOCKER_COUNT = 0
OTHER_OPEN_FIGURE_DOCUMENTATION_DEBT_COUNT = 3
```

Figures 1–3 use `figures/ch5_refq/p0v3_final_v6/`; Figure 4 uses
`figures/ch5_refq/p0v3_final_v6_e01_eta_label/`. Current Figure 4 terminology
is rank eta-squared (`η_H²`). The historical `epsilon_squared` field is a
legacy schema identifier for the same frozen estimator. This issue is closed
and is not reopened absent a new scientific inconsistency. The three remaining
figure-documentation items are historical/nonblocking debt.

## 11. Main/supplement maintenance separation

```text
MAIN_FIGURE_TEXT_AUTHORITY = docs/freeze/ch5_refq_main_figure_text_mapping_current.md
SUPPLEMENTARY_FIGURE_TEXT_AUTHORITY = docs/freeze/ch5_refq_supplementary_figure_mapping_current.md
MAIN_ONLY_CHANGE_REQUIRES_SUPPLEMENTARY_REWRITE = NO
SUPPLEMENTARY_ONLY_CHANGE_REQUIRES_MAIN_REWRITE = NO
```

Update the main mapping only for changes to main Figures 1–4 identity, caption
or body reference, asset, panel structure, or render/provenance authority.
Update the supplementary mapping only for supplementary inventory, render
status, asset, reference, or provenance changes. Analysis stages S1–S7 and
Supplementary Figures S1–S5 remain distinct namespaces. The historical
`phase2b_design_freeze_manifest.json` is a superseded design reference, not
current render, panel, or text-mapping authority.

## 12. Remaining nonblocking figure debt

The three open documentation-only items are the superseded Phase 2-B design,
the older scaffold-oriented migration matrix, and S-stage versus
Supplementary Figure namespace ambiguity. They do not block STYLE-A00B,
STYLE-A01-EN, or submission preparation unless a new current inconsistency is
discovered. No separate `FIG-A00` gate remains open. STYLE-A00B must consume
the current main and supplementary mapping registers; it may not redesign
figures.

## 13. Active workflow gates

Before STYLE-A00B:

```text
STYLE_A00_PROJECT_ACCEPTANCE = PASS_READY_FOR_STYLE_A00B
LANGUAGE_ROUTE = ENGLISH_PRIMARY_WITH_CHINESE_SEMANTIC_ANCHOR
MAIN_MAPPING_CLOSED = YES
FIGURE4_PROVENANCE_CLOSURE_PENDING = NO
GATE = PASS
```

Before STYLE-A01-EN:

```text
ROUTE_A01 = PASS
STYLE_A00B = PASS
AUTHOR_DECISIONS_FROM_STYLE_A00B = RESOLVED_IF_BLOCKING_QUESTIONS_EXIST
STYLE_A01_EN_GATE = PENDING_STYLE_A00B
```

If STYLE-A00B produces blocking author questions, resolve them before
STYLE-A01-EN. No separate figure gate is open.

## 14. Full next-stage workflow

```text
MS-R04
-> STYLE-A00 accepted rhetoric corpus model
-> ROUTE-A01 active route registration
-> STYLE-A00B (Opus 5 High): bilingual semantic / English-rhetoric reconstruction blueprint
-> author decisions, if required
-> STYLE-A01-EN (Opus 5 High): direct English rhetorical reconstruction
-> STYLE-R02: independent Opus review in a fresh conversation
-> STYLE-A02: Codex cross-language semantic alignment audit
-> bounded correction, if required
-> EN-R02 accepted English candidate lineage
-> JSS packaging / unresolved verified-guideline debt
```

Figure mapping is a supporting authority for this route, not a separate open
blocker. Journal-specific packaging remains separate; SUB-A02 records
unverified JSS requirements and no verified requirement currently mandates an
MS-R05 semantic revision.

## 15. No-change guards

This route registration authorizes only the creation of this workflow document.
The following are required unchanged:

```text
CURRENT_CHANGED = 0
MS_R04_SNAPSHOT_CHANGED = 0
MANUSCRIPT_VERSION_MANIFEST_CHANGED = 0
SIDECAR_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
MAIN_FIGURE_MAPPING_CHANGED = 0
SUPPLEMENTARY_MAPPING_CHANGED = 0
FIGURE4_PROVENANCE_CLOSURE_CHANGED = 0
EN_R01_CHANGED = 0
MANUSCRIPT_TEXT_CHANGED = 0
```

No MS-R04 edit, MS-R05 creation, manuscript snapshot or CURRENT promotion,
figure edit/rerender, scientific recomputation, or historical audit/freeze
rewrite is authorized. Existing untracked V3–V6 ZIP files are preserved and
must not be staged.

## 16. Final route decision

```text
STYLE_A00_PROJECT_ACCEPTANCE = PASS_READY_FOR_STYLE_A00B
LANGUAGE_ROUTE = ENGLISH_PRIMARY_WITH_CHINESE_SEMANTIC_ANCHOR
SCIENTIFIC_SEMANTIC_AUTHORITY = MS-R04
ROUTE_A01 = PASS
STYLE_A00B_GATE = PASS
STYLE_A01_EN_GATE = PENDING_STYLE_A00B
NEXT_TASK = CH5_REFQ_STYLE_A00B_ENGLISH_RECONSTRUCTION_BLUEPRINT
DECISION = CH5_REFQ_STYLE_ROUTE_A01_ENGLISH_PRIMARY_REGISTRATION_PASS
```

This is workflow registration only. No manuscript or scientific authority is
promoted.
