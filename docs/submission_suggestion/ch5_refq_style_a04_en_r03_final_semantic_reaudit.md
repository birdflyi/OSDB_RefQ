# STYLE-A04 Final Semantic Re-audit: EN-R03 against MS-R05

```text
TASK = CH5_REFQ_STYLE_A04_EN_R03_FINAL_SEMANTIC_REAUDIT
DECISION = CH5_REFQ_STYLE_A04_PASS_WITH_METADATA_REPAIR_ONLY
REPOSITORY_BASE_HEAD = ca4a0c131019bfdb9693f7b47f0c8a9d074256df
BASE_COMMIT_MESSAGE = docs(ch5): close Figure 3 view definitions
REMOTE_SYNC_AT_PREFLIGHT = 0 / 0
SOURCE_OF_SCIENCE = MS-R05
SCIENTIFIC_BASELINE = P0-v3
```

## Identity and source integrity

| Artifact | Required SHA-256 | Result |
|---|---|---|
| MS-R05 immutable snapshot | `30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22` | PASS |
| EN-R02 historical candidate | `F3D42BAF2034631CD5D2909A0DC2D43428742302BA605BBF489FBD5A6C00DB77` | PASS |
| EN-R03 audit target | `B61683132DCAD3B6BB4D5ACCA4B49AE4FCAB0CC0B9A2D57FFCC06CF359AFBFE4` | PASS |
| STYLE-R04 manifest | `207BB9210E8F3948F7BE7DE1C8E69591A5AD54A93A47B8520F415E68FF6405C2` | PASS; contains truncated source-manifest SHA (E2 below) |
| STYLE-R04 source-unit coverage | `C931DBC8FBD7CFA65358BE347857C37F6633D10FE5BF2F8790B13BFD1084953D` | PASS; 222 rows |
| STYLE-R04 changed-block delta | `B28552A90F4E1D320D14E74AF9B6FD0247EBEAC0D4F9F8A1FA7AAD723BF64628` | PASS; 2 rows; independently compared with candidate diff |
| STYLE-R04 self-audit | `321C63AE832ADC1BFD3E6781CF63A91BB3F2E90CA09AC51C4C37CB5315F97C0F` | PASS; corroborative only |
| Figure 3 view-definition closure | `509B81E5EE5156FDF235CCB208CD4F3784D50838927B82545D8817FBEAB61965` | PASS |
| Current main figure mapping | `B5D19396C3553BB08702254A2FCF2832AFE865C8DAF384D76B98B117CC4D5611` | PASS |

All listed manuscript and external STYLE-R04 artifacts were read-only. The A03 accepted base records E0=0, E1=1, E2=10, INFO=59, with R02-009 as its sole E1. Its accepted identity/hashes and the A03 report, issue adjudication, and changed-block audit were checked; the A03 decision is `CH5_REFQ_STYLE_A03_PASS_WITH_BOUNDED_CORRECTION_REQUIRED`.

## Independent EN-R02 → EN-R03 delta adjudication

The candidate text was independently compared; the delta sidecar was not treated as sole proof. The only substantive manuscript blocks changed are `RES-RQ2C-P001` and `RES-RQ2C-FIG001`. The only other change is the top candidate-role/provenance comment. No other substantive block changed.

`RES-RQ2C-P001` defines the seed-only induced view as cross-project RefQ edges whose source and target are both in the 294-seed set, retaining all 294 seeds in the node domain; this includes isolates because the node domain is the complete seed manifest, not only edge-observed seeds. It defines the multi-seed target set by at least two distinct source project IDs in the directed cross-project RefQ edge table, retains edges to those targets, and uses seed set ∪ multi-seed targets for nodes. It then explicitly preserves the first-order—not second-order—boundary and places source-incomplete expanded-target interpretation under §6.3.

`RES-RQ2C-FIG001` leaves panel A and panel C wording intact. Panel B now states the canonical view, the seed-to-seed edge restriction over all 294 seed nodes, and the ≥2-distinct-seed-source target criterion over seed ∪ those targets. It retains each metric's own scale. The existing 35-community result, 50 random-seed runs, seed 20260731, and algorithmic/non-taxonomic community boundary remain unchanged. Added 294 and 2 are view-definition identifiers already fixed by the seed manifest and S3 construction; no reported result value was changed.

The directed implementation `build_s3_view_inputs` in `supplemental/reference_quotient_v2/scripts/s3_observation_sensitivity.py`, existing P0-v3 `observation_boundary_sensitivity.csv`, Figure 3 source manifest, provenance closure, and current Figure 3 mapping agree. Both sensitivity views are first-order observation-boundary views—not shared-reference projections, QQᵀ/QᵀQ or K=XΦXᵀ projections, independent target samples, or source-complete expanded-target populations. The seed-only node domain contains all 294 seeds including isolates. Missing expanded-target source activity is not interpreted as zero, and ignoring direction does not restore observations or yield a complete ecosystem graph.

The Figure 3 mapping includes `VIEW_DEFINITION_PROVENANCE` and `VIEW_DEFINITION_STATUS = PROVENANCE_CLOSED`; its panel-B role records the exact view criteria. Comparing the mapping against its pre-R04 parent shows changes only in the Figure 3 section. Figure 1, Figure 2, Figure 4, asset paths, Figure 3 panel count/identity, and hashes are unchanged.

### Delta and manuscript invariants

```text
SUBSTANTIVE_CHANGED_BLOCKS = RES-RQ2C-P001; RES-RQ2C-FIG001
SUBSTANTIVE_CHANGED_BLOCK_COUNT = 2
OTHER_SUBSTANTIVE_CHANGED_BLOCK_COUNT = 0
SOURCE_UNIT_COUNT = 222
SOURCE_UNIT_COVERED = 222
SOURCE_UNIT_UNACCOUNTED = 0
ONLY_CHANGED_SOURCE_UNITS = RES-RQ2C-U001; RES-RQ2C-U003
RQ_COUNT = 5
RQ_ORDER = RQ1 / RQ2a / RQ2b / RQ2c / RQ3
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = NO
UNIQUE_CITATION_KEYS = 33
CITATION_KEY_SET_MATCH_MS_R05_AND_EN_R02 = YES (A03-accepted base plus exact EN-R02→EN-R03 delta)
DISPLAY_FORMULA_COUNT = 12
DISPLAY_FORMULA_BYTE_CHANGE_FROM_EN_R02 = 0
SCIENTIFIC_VALUE_CHANGED_FROM_EN_R02 = 0
TABLE_VALUE_CHANGED = 0
FIGURE_CAPTION_NUMERIC_RESULT_CHANGED = 0
FIGURE_ASSET_CHANGE = 0
SCIENTIFIC_RECOMPUTATION = 0
FIGURE_RERENDER = 0
```

Claim-strength and observation review of the two changed blocks found no stronger construct, causal drift, knowledge-flow measurement claim, dependency-ground-truth claim, project-importance claim, semantic-community drift, or unqualified OSS generalization. Seeds remain the source-complete population; expanded targets remain source-incomplete. There is no source/target population conflation, missing-as-zero drift, independent-target-sample claim, target-source-completeness claim, direction-ignored observation-restoration claim, or complete-ecosystem-graph claim.

```text
CLAIM_STRENGTHENING = 0
CAUSAL_DRIFT = 0
KNOWLEDGE_FLOW_MEASURE_CLAIM = 0
DEPENDENCY_GROUND_TRUTH_CLAIM = 0
PROJECT_IMPORTANCE_CLAIM = 0
SEMANTIC_COMMUNITY_DRIFT = 0
UNQUALIFIED_OSS_GENERALIZATION = 0
MISSING_AS_ZERO_DRIFT = 0
SOURCE_TARGET_POPULATION_CONFLATION = 0
MULTI_SEED_TARGET_INDEPENDENT_SAMPLE_CLAIM = 0
MULTI_SEED_TARGET_SOURCE_COMPLETE_CLAIM = 0
DIRECTION_IGNORED_RESTORES_OBSERVATION_DRIFT = 0
COMPLETE_ECOSYSTEM_GRAPH_CLAIM = 0
SEED_ONLY_VIEW_FIRST_ORDER = YES
MULTI_SEED_TARGET_VIEW_FIRST_ORDER = YES
SEED_ONLY_VIEW_SHARED_REFERENCE = NO
MULTI_SEED_TARGET_VIEW_SHARED_REFERENCE = NO
QQT_QTQ_VIEW_DEFINITION = NO
KXPHIXT_VIEW_DEFINITION = NO
```

## E2 provenance and deferred packaging debt

The actual Figure 3 source-manifest SHA-256 is `0D429DA458042135777A17C1B449DED48B52106A51EFFCDED6F93B7844FA46A2`, verified from the repository file and current mapping. The STYLE-R04 external manifest instead records `0D429DA458042135777A17C1B44946A2`, which is not a full SHA-256 and does not match. This is E2 sidecar metadata debt only; it is not a discrepancy in the actual Figure 3 authority and does not indicate scientific drift.

A03's promotion metadata debt was independently checked: recorded SHA `837f617e9d05fd3c933a8fd7f56a7e5e08bc7d0d` is not a Git object, while actual commit `837f61791adbe96a9565a2cc4fe1a6e377fa5662` exists with message `docs(ch5): promote bounded semantic source MS-R05`. This remains E2 provenance debt. Neither discrepancy is repaired here.

Packaging items R02-017, R02-024, R02-025, R02-026, R02-041, and R02-065, together with JSS formatting, anonymization, declarations, archive/code-release status, final Zenodo/package correspondence, and the “no preset robustness alert” wording, remain deferred and are not semantic blockers.

```text
E0 = 0
E1 = 0
E2 = 11 (10 accepted A03 E2 items carried forward, including the MS-R05 promotion SHA and packaging debt; plus 1 STYLE-R04 manifest SHA defect)
INFO = 0
SEMANTIC_PROMOTION_READY = YES
EN_R03_PROMOTION_PERFORMED = NO
METADATA_REPAIRED = NO
MS_R06_CREATED = NO
```

## Recommendation

The English candidate is semantically ready, and R02-009 is closed in the manuscript, mapping, and provenance record. Complete the separate `CH5_REFQ_EN_R03_PROMOTION_AND_PROVENANCE_METADATA_CLOSURE` task next: repair and verify both metadata records, then handle EN-R03 promotion under that task's authority. This audit neither promotes EN-R03 nor performs packaging work.
