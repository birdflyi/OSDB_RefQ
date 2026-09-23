# CH5_REFQ_STYLE_A02 Cross-Language Semantic Alignment Audit

## Decision

**CH5_REFQ_STYLE_A02_PASS_MS_R05_REQUIRED_BEFORE_ENGLISH_CORRECTION**

The 222 source units are traceably represented in STYLE-R01-EN and the 67 STYLE-R02 issues are independently adjudicated. The English candidate is not promoted or edited. Four source-level corrections are required before final English correction: R02-001 (knowledge-flow residue), R02-043 (source-event versus referencing-entity classification terminology), R02-050 (appendix interpretive-role inconsistency), and R02-054 (source-internal mainly-because inconsistency).

## Base and authority checks

- Repository branch: `ch5-refq-repository-identity-correction-v1`
- Required/base/local/remote HEAD: `90f740113a50a1cf5506bea1e701fbf4f52f279f`
- AHEAD_BEHIND: `0 / 0`
- MS-R04 SHA-256: `F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549` - PASS
- STYLE-R01-EN SHA-256: `5D5225F720E4B57D0162AD9EBC7394100EDD48E3B987D24CBABA574F961934B9` - PASS
- STYLE-R02 review / ledger / section status hashes: all match the frozen controls - PASS
- A01 source coverage / traceability / change log / self-audit hashes: all match the frozen manifest - PASS
- Pre-existing untracked V3-V6 ZIPs preserved; no asset operation performed.

## Coverage and invariants

- Source-unit alignment: **222 / 222**
- Target blocks: 211
- Explicit change-register coverage: 36 / 36
- R3 executed by A01: 0
- R02 issue adjudication: **67 / 67**
- RQ count: 5
- Contribution count: 4
- Citation-key set: 33 / 33
- Formula count: 12 / 12
- Scientific value change: 0
- Scientific recomputation: 0
- Figure assets/mapping/rerender: 0 / 0 / 0

## P0 adjudication

### R02-001 - knowledge-flow residue

- A1: **YES**. MS-R04 positively leaves "Reference relations approximate explicit knowledge pointers" while negating only complete/causal variants.
- A2: **NO**. That affirmative residue is not compatible with the frozen paper centre when read as a measure of knowledge flow.
- A3: **YES, with author interpretation**. English can state the measured construct directly without adding a result.
- A4: **YES**. The Chinese semantic authority needs a bounded source correction; do not edit it in STYLE-A02.
- Classification: `SOURCE_LEVEL_SEMANTIC_DEBT`; MS_R05_REQUIRED_FOR_THIS_ISSUE=YES.

### R02-005 - external / non-self / largely

- B1: `GitHub_Service_External_Links` is a legitimate category label and should be retained.
- B2: metric prose must use `non-self`, not generic `external`.
- B3: `largely` is unsupported by the frozen denominator (largest category 43.47%; non-project records below a majority) and must be removed or replaced by "largest category/orientation".
- Classification: primary `ENGLISH_SEMANTIC_DRIFT_FROM_MS_R04`, with terminology/control-layer secondary; no MS-R05 required for this item.

### R02-013 - affect / causality

The English causal reading is stronger than the bounded comparison design. Treat as English semantic disambiguation: compare composition/role/local-structure metrics across DBMS subdomains; do not claim causal effects. MS_R05_REQUIRED_FOR_THIS_ISSUE=NO.

### R02-054 - mainly because

- D1: **NO**. Under the frozen construction, expanded targets enter only when admitted seed-source Reference records point to uniquely project-mappable non-seed targets.
- D2: **YES**. "Mainly" implies an alternate path not present in the formal contract.
- D3: **YES**. English "because" is the faithful formal realization, but the Chinese source inconsistency must first be logged for MS-R05.
- Classification: `SOURCE_INTERNAL_INCONSISTENCY`; MS_R05_REQUIRED_FOR_THIS_ISSUE=YES.

### R02-043 - Figure 1B versus Table 4.1 classification name

The current main-figure mapping confirms Figure 1B as the complete source-event composition. The parallel table/prose wording calls these categories referencing entity types, although Push and Release are event types rather than entities. This is a source-level terminology inconsistency, not an asset mismatch. MS-R05 should use one accurate classification name while preserving every category and value; no scientific rerun is required.

### R02-050 - Appendix interpretation role

The source says the appendix is not a basis for interpreting the main results, yet also says it supports semantic interpretation. Reconcile these as documentation of boundaries already stated in the main text, without adding empirical interpretation. Because both source statements are frozen and map faithfully to the candidate, record this source inconsistency for MS-R05. No result should be added.

## Additional semantic-risk adjudications

- R02-007: terminology normalization is required to distinguish the node-set term "expanded project node" from the non-seed term "expanded target".
- R02-008: add the already-frozen seed-centered qualifier to RQ2c result wording; no new science.
- R02-009: figure 3B definitions/cross-reference are documentation/placement debt; current figure mapping remains authoritative.
- R02-020: `controlling for` suggests covariate adjustment; replace in English with "accounting for" or an equivalent population/label-condition phrase.
- R02-021: clarify extraction-level controls versus the explicit absence of record-level deduplication.
- R02-022: dangling "disambiguation rule defined here" is a documentation/source traceability gap.
- R02-043: the source must first select one accurate classification name for the same frozen category/value distribution; do not alter categories or values.
- R02-050: reconcile appendix language as boundary documentation that adds no new interpretation.
- R02-053: qualify the OSS-wide framing as an instance instantiated for open-source DBMS projects.
- R02-066: synthesis blocks are traceable and require no change.

## Cross-language conclusion

Alignment is faithful at the source-unit level: restructuring is bounded and does not change numbers, citations, formulas, observation roles, or figures. Faithful translation does not cure source correctness: R02-001, R02-043, R02-050, and R02-054 require bounded source clarification before final English correction. Literature positioning remains complementary-critical; no adversarial prior-work claim was introduced.

## MS-R05 gate

`MS_R05_REQUIRED = YES`

`MS_R05_TRIGGER_ISSUES = R02-001, R02-043, R02-050, R02-054`

`MS_R05_MINIMAL_SOURCE_SCOPE = one bounded construct-validity correction, one source-category naming correction, one appendix-role clarification, and one admission-path wording correction; no scientific recomputation.`

`MS_R05_EXPECTED_CHANGE_CLASS = R3 semantic editorial correction`

The four source corrections must be completed and re-audited before any final English correction is promoted. STYLE-A02 does not create MS-R05.

## Counts

- Primary classes: SOURCE_LEVEL_SEMANTIC_DEBT=1; ENGLISH_ONLY_RHETORIC=28; ENGLISH_SEMANTIC_DRIFT_FROM_MS_R04=5; ENGLISH_TERMINOLOGY_NORMALIZATION=13; TRACEABILITY_OR_DOCUMENTATION_ONLY=2; CONTROL_LAYER_DRIFT_FROM_A00B=1; PACKAGING_ONLY=5; SOURCE_INTERNAL_INCONSISTENCY=3; NO_CHANGE=9
- Planned English-layer corrections after source closure: 47 English-only/drift/terminology/control-layer items, plus 2 documentation/traceability placements
- Planned source corrections: 4 (R02-001, R02-043, R02-050, R02-054; source-level semantic debt=1, source-internal inconsistency=3)
- Packaging-only items: 5
- No-change items: 9
- Semantic drift from MS-R04 (primary): 5
- Source-level semantic debt (primary): 1
- Source-internal inconsistency (primary): 3

## Required guards

```text
MS_R04_CHANGED = 0
CURRENT_CHANGED = 0
STYLE_R01_EN_CHANGED = 0
STYLE_A00/A00B/A01/R02_ARTIFACT_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_MAPPING_CHANGED = 0
FIGURE_RERENDER = 0
SCIENTIFIC_RECOMPUTATION = 0
EN_R02_CREATED = 0
MS_R05_CREATED = 0
JSS_PACKAGING_CHANGE = 0
```

## Outputs

- `docs/submission_suggestion/ch5_refq_style_a02_cross_language_semantic_alignment_audit.md`
- `docs/submission_suggestion/ch5_refq_style_a02_r02_issue_adjudication.csv`
- `docs/submission_suggestion/ch5_refq_style_a02_source_unit_alignment.csv`
- `docs/submission_suggestion/ch5_refq_style_a02_bounded_correction_plan.md`

This audit is documentation-only. Promotion did not occur. Because MS_R05 is required, the next task is `CH5_REFQ_MS_R05_BOUNDED_SEMANTIC_EDITORIAL_CORRECTION`.
