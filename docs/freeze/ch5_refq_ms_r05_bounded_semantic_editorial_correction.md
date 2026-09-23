# Chapter 5 RefQ — MS-R05 Bounded Semantic Editorial Correction

## Decision

```text
TASK = CH5_REFQ_MS_R05_BOUNDED_SEMANTIC_EDITORIAL_CORRECTION
DECISION = CH5_REFQ_MS_R05_BOUNDED_SEMANTIC_EDITORIAL_CORRECTION_PASS
BASE_REVISION = MS-R04
BASE_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
NEW_REVISION = MS-R05
MS_R05_SHA = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
MS_R05_SNAPSHOT = versions/MS-R05_BOUNDED_SEMANTIC_EDITORIAL_30491279.md
SCIENTIFIC_BASELINE = P0-v3
SCIENTIFIC_RECOMPUTATION = 0
```

The repository base was `d2b0f12c6a9d8b2e10eaa9482a7386c860de4f63` on
`ch5-refq-repository-identity-correction-v1`, equal to the remote before this
task. The four pre-existing V3–V6 ZIP archives and both prompt files were
preserved untracked.

## Authorized source delta

Only the four STYLE-A02 trigger issues were applied, in seven source units:

```text
R02-001 = THREAT-U002
R02-054 = INTRO-U011
R02-043 = RES-RQ1-U002, RES-RQ1-U005, METH-U066
R02-050 = AVAIL-U004, APP-U001
```

The exact before/after source-unit text is registered in
`ch5_refq_ms_r05_bounded_semantic_editorial_delta.md`; the downstream English
traceability is registered in
`ch5_refq_ms_r05_source_unit_delta_bridge.csv`.

### Exact semantic changes

| Unit | Before | After |
|---|---|---|
| THREAT-U002 | Reference relations were described as approximating explicit knowledge pointers before excluding complete knowledge flow. | Reference evidence is explicitly observable-reference direction/context and is not a knowledge-flow measure. |
| INTRO-U011 | Expanded targets entered “主要因为” they were cited by seeds. | Expanded targets enter because they are cited by seed projects through admitted Reference records. |
| RES-RQ1-U002 | Figure 1B used “source event”. | Figure 1B uses “征引实体类型”. |
| RES-RQ1-U005 | Table 4.1 used an unlabeled source-category header. | Table 4.1 uses “征引实体类型（referencing entity types）”. |
| METH-U066 | The source category was “Referencing Entity” without schema clarification. | GH-CoRE `ObjEntity` and separate `src_entity_type`, `tar_entity_type`, and `event_type` fields are stated; source and target labels are canonicalized as referencing/referenced entity type. |
| AVAIL-U004 | Appendix provenance was both excluded from interpretation and described as supporting interpretation. | Appendix A supports reproduction, traceability, and verification of boundaries already stated in the main text, without adding interpretation. |
| APP-U001 | Appendix introduction broadly supported semantic interpretation. | Appendix A supports reproduction, traceability, and checking the main-text interpretation boundary only. |

No paragraph, heading, source-unit, RQ, contribution, table value, formula, or
figure asset was added, removed, reordered, or recomputed.

## GH-CoRE schema and Figure 1 field audit

```text
GH_CORE_MAIN_COMMIT = f4216351ffe62d71c571df08e80decc258d6125a
GH_CORE_ENTITY_MODEL_BLOB = 1c0604c8d062877889f662190ef03d39f961adaa
GH_CORE_RELATION_EXTRACTION_BLOB = b089c84a2214846e31b2722d1bb6f550d2ecf9ba
GH_CORE_MAIN_COMMIT_CHECK = PASS
GH_CORE_ENTITY_MODEL_BLOB_SHA_CHECK = PASS
GH_CORE_RELATION_EXTRACTION_BLOB_SHA_CHECK = PASS
GH_CORE_ENTITY_SCHEMA_VERIFIED = YES
GH_CORE_SRC_ENTITY_TYPE_COLUMN_VERIFIED = YES
GH_CORE_EVENT_TYPE_COLUMN_SEPARATE = YES
TABLE41_CATEGORY_SOURCE_FIELD = src_entity_type
FIGURE1B_CATEGORY_SOURCE_FIELD = src_entity_type
SOURCE_ENTITY_AND_EVENT_TYPE_DISTINCT_IN_GH_CORE = YES
```

The frozen schema evidence records `ObjEntity.E` entries including `Push` and
`Release`, dictionary-backed assignment through `set_val()`/`setattr`,
dependency completion through `apply_F()`, and the separate relation-output
columns. The P0-v3/S6 source is
`rq1_referencing_entity_distribution_plot.csv`, while the event distribution
is a separate `rq1_event_type_distribution_plot.csv`.

The Figure 1 SVG SHA remains
`63B5A581E65EF305EA7A3FEFD1E952E297A799E6F4D6FBB278DF6E05B6B74D24`.
The rendered asset contains no universal `source event type(s)` phrase;
therefore:

```text
FIGURE1_LABEL_PATCH_REQUIRED = NO
FIGURE1_CATEGORY_VALUES_CHANGED = NO
FIGURE1_PANEL_IDENTITY_CHANGED = NO
FIGURE1_RERENDER = NO
MAIN_FIGURE_MAPPING_TERMINOLOGY_ONLY_UPDATE = YES
```

The current main-figure mapping was updated only for the MS-R05 manuscript
pointer and Figure 1 source-side terminology. Asset roots, hashes, panels,
numeric content, and scientific provenance are unchanged.

## Structural and scientific guards

```text
SOURCE_UNIT_PARTITION_CHANGED = NO
SOURCE_UNIT_COUNT = 222
HEADING_COUNT_CHANGE = 0
PARAGRAPH_COUNT_CHANGE = 0
RQ_COUNT_CHANGE = 0
CONTRIBUTION_COUNT_CHANGE = 0
CITATION_KEY_CHANGE = 0
FORMULA_COUNT_CHANGE = 0
FORMULA_BYTE_CHANGE = 0
TABLE_NUMERIC_VALUE_CHANGE = 0
SCIENTIFIC_NUMERIC_TOKEN_CHANGE = 0
FIGURE_CAPTION_NUMERIC_CHANGE = 0
UNMAPPED_CHANGED_HUNK_COUNT = 0
UNAUTHORIZED_CHANGED_HUNK_COUNT = 0
CHANGED_HUNK_COUNT = 8
```

The eight textual hunks map exactly to the seven allowlisted source units
(METH-U066 has two label lines). Citation keys remain 33/33; display-math
delimiters remain 12/12; all numeric-token multisets and table numeric-token
multisets are byte-equivalent as sets and counts.

## Semantic closure

```text
KNOWLEDGE_FLOW_POSITIVE_PROXY_RESIDUE_COUNT = 0
KNOWLEDGE_FLOW_AS_MEASURE_OF_REFQ = NO
EXPLICIT_REFERENCE_STRUCTURE_CENTRE_PRESERVED = YES
EXPANDED_TARGET_ALTERNATE_ENTRY_PATH_IMPLIED = NO
SOURCE_CATEGORY_UNIVERSAL_LABEL_CONFLICT_COUNT = 0
REFERENCE_ENTITY_TYPE_AMBIGUOUS_LABEL_COUNT = 0
REFERENCING_ENTITY_TYPE_CANONICAL_LABEL_PRESENT = YES
REFERENCING_ENTITY_AS_SCHEMA_TERM_EXPLAINED = YES
SOURCE_EVENT_TYPE_AS_UNIVERSAL_CLASS_LABEL = 0
APPENDIX_ROLE_INTERNAL_CONTRADICTION = 0
SOURCE_COMPLETE_SEED_STATUS_CHANGED = NO
SOURCE_INCOMPLETE_EXPANDED_TARGET_STATUS_CHANGED = NO
DIRECTION_IGNORED_VIEW_SEMANTICS_CHANGED = NO
EXPANDED_TARGET_ENTRY_RULE = referenced by admitted seed-source Reference records and uniquely project-mappable
ALTERNATE_ENTRY_PATH = NONE
```

The two remaining knowledge-flow/transfer occurrences are explicit negative
boundaries, not positive measurement claims. Appendix A has the same bounded
role in §8 and its introduction: reproduction, traceability, and verification
of already stated interpretation boundaries, with no new empirical
interpretation.

## No-change and version protection

```text
MS_R04_SNAPSHOT_CHANGED = 0
P0_V3_SCIENTIFIC_OUTPUT_CHANGED = 0
SCIENTIFIC_VALUE_CHANGE_COUNT = 0
CITATION_KEY_CHANGE_COUNT = 0
FORMULA_CHANGE_COUNT = 0
FIGURE_ASSETS_CHANGED = 0
SUPPLEMENTARY_FIGURE_MAPPING_CHANGED = 0
MAIN_FIGURE_MAPPING_SCIENTIFIC_CONTENT_CHANGED = 0
STYLE_R01_EN_CHANGED = 0
STYLE_A00B_CHANGED = 0
STYLE_R02_CHANGED = 0
STYLE_A02_CHANGED = 0
JSS_PACKAGING_CHANGE = 0
```

The MS-R04 snapshot remains SHA
`F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549`. CURRENT
and the new MS-R05 snapshot are byte-identical at
`30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22`.
CURRENT, the MS-R04 snapshot, and historical STYLE-A00/A00B/A01/R01/R02/A02
artifacts were not overwritten.

## Promotion records

```text
PROMOTION_DOCUMENT = docs/freeze/ch5_refq_ms_r05_bounded_semantic_editorial_correction.md
DELTA_DOCUMENT = docs/freeze/ch5_refq_ms_r05_bounded_semantic_editorial_delta.md
DELTA_BRIDGE = docs/freeze/ch5_refq_ms_r05_source_unit_delta_bridge.csv
POST_MS_R05_ROUTE = docs/strategy/ch5_refq_post_ms_r05_english_correction_route.md
MANUSCRIPT_VERSION_MANIFEST_UPDATED = YES
```

MS-R05 supersedes MS-R04 as the current Chinese semantic authority for the
post-STYLE-A02 source correction. MS-R04 remains immutable historical lineage.
The next task is the separate English correction; it has not been started:

```text
NEXT_TASK = CH5_REFQ_STYLE_R03_BOUNDED_ENGLISH_CORRECTION
```
