# Chapter 5 RefQ JSS Submission Derivative Preparation Audit

## Identity and scope

```text
TASK = CH5_REFQ_JSS_PACKAGING_REQUIREMENT_VERIFICATION_AND_SUBMISSION_DERIVATIVE_PREP
MODE = CURRENT_JSS_REQUIREMENT_VERIFICATION + SUBMISSION_DERIVATIVE_PREPARATION + NO_SCIENTIFIC_EDIT
TASK_BASE_REPOSITORY_HEAD = 4c62effcd693026acbd37d7a99992ddbe1559a9f
CURRENT_CHINESE_SEMANTIC_AUTHORITY = MS-R05
MS_R05_SHA = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
CURRENT_ENGLISH_SEMANTIC_AUTHORITY = EN-R03
EN_R03_SHA = B61683132DCAD3B6BB4D5ACCA4B49AE4FCAB0CC0B9A2D57FFCC06CF359AFBFE4
```

The external working directory is:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/submission/jss/EN-R03_P0/`

It contains the source-level derivative and packaging records. External files
are intentionally not committed to GitHub because author metadata and
submission materials are private working data.

## Derivative construction

`JSS_MAIN_MANUSCRIPT_DERIVATIVE.md` was generated from the exact EN-R03 bytes.
The only transformations were:

1. removal of 213 internal HTML process comments (`src`, `src-caption`,
   `src-table`, revision/task and promotion metadata comments); and
2. one reader-facing wording normalization: “no preset robustness alert was
   triggered” → “the prespecified robustness criteria were not triggered”.

The second change preserves the tested-criteria meaning and does not add a
robustness claim. No scientific sentence, numeric value, table value, formula,
citation key, figure caption, observation boundary or claim strength changed.

```text
JSS_MAIN_MANUSCRIPT_DERIVATIVE_SHA256 = D75409CFE976EB04DA7B192DCD9C064B559A56D7699B03512A65E27ADC08A080
PROCESS_COMMENT_REMOVAL_COUNT = 213
SEMANTIC_RISK_CHANGE_COUNT = 0
```

`JSS_HIGHLIGHTS.txt` contains four manuscript-grounded bullets, each at most
85 characters. The current Guide verifies that Highlights are mandatory.
The Guide also verifies that a Graphical Abstract is mandatory. No graphical
abstract is generated or rendered here; `JSS_GRAPHICAL_ABSTRACT_PLAN.md`
records the required size/format and leaves its production to author-approved
packaging work.

## Frozen asset handling

`JSS_FIGURE_UPLOAD_MANIFEST.csv` records SHA-256 values for the accepted V6
Figures 1–3 and the V6-E01 terminology-corrected Figure 4. The manifest does
not convert, copy, edit, or rerender any figure. `JSS_SUPPLEMENTARY_MATERIAL_PLAN.md`
classifies Appendix A, the four frozen supplementary families, repository
artifacts, and the existing relation/data DOI without moving files.

## Scientific and semantic guards

```text
MS_R05_SHA_CHECK = PASS
EN_R03_SHA_CHECK = PASS
EN_R03_CHANGED = NO (immutable source preserved)
SEMANTIC_GATE = PASS
SCIENTIFIC_VALUE_CHANGE = 0
TABLE_VALUE_CHANGE = 0
FORMULA_COUNT = 12 (preserved)
FORMULA_SEMANTIC_CHANGE = 0
CITATION_KEY_COUNT = 33 (preserved)
CITATION_KEY_SET_CHANGE = 0
CLAIM_STRENGTHENING = 0
OBSERVATION_SEMANTIC_DRIFT = 0
SOURCE_COMPLETE_SEEDS_PRESERVED = YES
SOURCE_INCOMPLETE_EXPANDED_TARGETS_PRESERVED = YES
MISSING_AS_ZERO_DRIFT = 0
FIRST_SECOND_ORDER_DRIFT = 0
KNOWLEDGE_FLOW_MEASURE_CLAIM = 0
DEPENDENCY_GROUND_TRUTH_CLAIM = 0
PROJECT_IMPORTANCE_CLAIM = 0
CAUSAL_DRIFT = 0
UNQUALIFIED_OSS_GENERALIZATION = 0
FIGURE_ASSET_CHANGE = 0
SCIENTIFIC_RECOMPUTATION = 0
```

The single-anonymized review model is verified by the current Guide. Therefore
no double-anonymization was applied, and repository/Zenodo provenance wording
was not blindly removed. No author metadata, funding, conflict, CRediT or AI
statement was fabricated.

## Packaging gates

```text
PACKAGING_CONTENT_GATE = PASS_WITH_AUTHOR_INPUT
UPLOAD_READINESS = NOT_READY_AUTHOR_INPUT
UNRESOLVED_CURRENT_JSS_HARD_REQUIREMENT_COUNT = 0
AUTHOR_INPUT_REQUIRED_COUNT = 12
GRAPHICAL_ABSTRACT = required by verified Guide; not created
TABLE_RENUMBERING_PERFORMED = NO
BIBLIOGRAPHY_RESTYLE_PERFORMED = NO
ANONYMIZATION_PERFORMED = NO
```

The derivative is packaging-ready in content and semantics, but it is not an
upload-ready package until the authors provide identity/declaration facts and a
graphical abstract, and the live system resolves its article-type, ORCID,
reviewer and cover-letter fields.

## Decision and next task

```text
DECISION = CH5_REFQ_JSS_PACKAGING_PREP_PASS_READY_FOR_AUTHOR_METADATA_AND_FINAL_UPLOAD_CHECK
NEXT_TASK = CH5_REFQ_JSS_AUTHOR_METADATA_AND_DECLARATION_COMPLETION
```

The decision does not authorize Editorial Manager submission and does not
promote the derivative to semantic authority.
