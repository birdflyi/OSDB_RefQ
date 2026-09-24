# Figure 3 Observation-View Definition Provenance Closure

```text
TASK = CH5_REFQ_STYLE_R04_POST_A03_BOUNDED_CORRECTION
TRIGGER = STYLE-A03 / R02-009
SCIENTIFIC_BASELINE = P0-v3
CURRENT_V2_IMPLEMENTATION = supplemental/reference_quotient_v2/scripts/s3_observation_sensitivity.py
CURRENT_S3_OUTPUT = supplemental/reference_quotient_v2/outputs_p0v3/S3_observation_sensitivity/observation_boundary_sensitivity.csv
FIGURE3_SOURCE_MANIFEST = figures/ch5_refq/p0v3_final_v6/main/figure3_undirected_structure/source_manifest.json
VIEW_DEFINITION_STATUS = PROVENANCE_CLOSED
SCIENTIFIC_RECOMPUTATION = 0
FIGURE_RERENDER = 0
FIGURE_ASSET_CHANGE = 0
MS_R06_REQUIRED = NO
HISTORICAL_V1_EVIDENCE_ROLE = CORROBORATIVE_ONLY
```

## Authority and verification

The current v2 `build_s3_view_inputs` implementation was checked directly. It
validates the directed cross-project edge table, the complete node registry,
and the 294-seed manifest; derives the three observation-boundary sensitivity
views from those inputs; and applies the first-order direction-ignored
structural analysis to those views. The P0-v3 S3 output records the three view
summaries. The Figure 3 source manifest lists
`observation_boundary_sensitivity.csv` as an input with columns for view,
directed/undirected edges and weights, operator order, node domains, and the
structural summaries.

The current implementation and v2 tests—not a reconstruction from the view
names—are the semantic authority for the definitions below. Historical
reference_quotient_v1/v1.2 implementation/report material agrees and is
corroborative only.

## Exact view definitions

### `CANONICAL_SEED_CENTERED_OBSERVED`

- Directed view: the validated directed cross-project RefQ edge table.
- Node domain: the complete declared RefQN node registry.
- Role: the canonical seed-centered observed view used as the primary
  first-order direction-ignored structural view.

### `SEED_ONLY_INDUCED`

- Directed edge set: cross-project RefQ edges for which both
  `source_project_id` and `target_project_id` belong to the 294-project seed
  set.
- Node domain: all 294 seed projects from the seed manifest, including
  zero-edge isolates.
- This is a first-order induced sensitivity view; it is not a separately
  sampled population or a shared-reference projection.

### `MULTI_SEED_TARGET_VIEW`

- Multi-seed target set: `target_project_id` values referenced by at least two
  distinct `source_project_id` values in the directed cross-project RefQ edge
  table.
- Directed edge set: cross-project RefQ edges whose target belongs to that
  multi-seed target set.
- Node domain: the union of the seed set and the multi-seed target set.
- Node order: inherited from the validated node registry.
- This is a first-order observation-boundary sensitivity view; it is not an
  independently source-sampled target population or a shared-reference
  projection.

## Interpretation boundary

The views differ in the selected first-order edge and node domains; they do
not define new causal models or new scientific results. The seed-only view's
node domain is the complete seed population. The multi-seed target criterion
identifies targets by the number of distinct observed seed sources that point
to them; it does not make expanded targets source-complete. The direction-
ignored analyses remain derived from first-order RefQ edges and do not restore
missing source observations. Neither sensitivity view is a complete ecosystem
graph or a population independently sampled from all OSS projects.

## Scope guards

```text
QQT_OR_QTQ_USED_TO_DEFINE_THESE_VIEWS = NO
KXPHIXT_USED_TO_DEFINE_THESE_VIEWS = NO
SHARED_REFERENCE_PROJECTION = NO
EXPANDED_TARGET_SOURCE_COMPLETE = NO
INDEPENDENT_TARGET_SAMPLING = NO
FIGURE_ASSET_CHANGED = 0
```

This closure registers the existing P0-v3 view construction for text and
mapping traceability. It does not alter P0-v3, S3 outputs, any figure asset, or
the Chinese MS-R05 caption.
