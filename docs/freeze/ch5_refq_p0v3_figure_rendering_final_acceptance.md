# Chapter 5 RefQ Figure Rendering — Final Acceptance Record

## Acceptance decision

The externally reviewed V6 publication rendering is accepted as the final
publication representation for Chapter 5 RefQ.

```text
SCIENTIFIC_PRESENTATION_SELECTION = PASS
LINEAR_AXIS_SELECTION = FINAL
PUBLICATION_LABEL_QA = PASS
HUMAN_VISUAL_QA = PASS
decision = P0V3_FIGURE_RENDER_FINAL_ACCEPTED
```

This record is documentation-only.  It does not rerender figures, create a V7
root, modify V6 assets or manifests, alter scientific values, rerun a pipeline,
or modify the manuscript or tables.

## Accepted repository state

- Repository: `D:/github_repo/OSDB_RefQ`
- Branch: `ch5-refq-repository-identity-correction-v1`
- `repository_HEAD_before = c295e762865a5ad09fad3c4a7b99a43e58db0e01`
- Accepted publication render root:
  `figures/ch5_refq/p0v3_final_v6/`
- V6 manifest:
  `figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json`
- V6 QA review:
  `docs/freeze/ch5_refq_p0v3_figure_rendering_v6_publication_label_polish_review.md`

V3, V4, V5, and V6 roots and all prior provenance remain immutable.  The
pre-existing untracked ZIP files were preserved and were not included in this
acceptance change.

## Final externally accepted Figure 2C presentation

The external visual review accepted all three Figure 2C target-role quantile
panels with linear y-axes and the following publication labels:

- `in-degree`: `1 / 1 / 1 / 42`
- `in-strength`: `1 / 2 / 5 / 3,430`
- `target coverage`: `0.34% / 0.34% / 0.34% / 14.29%`

The final Panel C title is:

```text
Target-role quantile profile
```

The accepted connector and marker geometry are:

```text
thin_alpha_0.55_markers_primary
```

The current deterministic label offsets and marker coordinates were accepted.
The linear representation is retained because the manuscript's intended
observation is the pronounced separation between typical and maximum observed
target-side coverage/strength.  Numeric labels preserve the interpretation of
compressed lower quantiles without changing their geometry.  No distributional
fitting, power-law, or formally established tail-shape claim is introduced.

The underlying target-coverage marker coordinates remain the frozen fractions:

```text
Q1     = 0.0034013605442176
Median = 0.0034013605442176
Q3     = 0.0034013605442176
Max    = 0.1428571428571428
```

## Scientific and pipeline guards

The accepted V6 state retains the required zero-change and non-execution
guards:

```text
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
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
```

No scientific or rendered asset was changed by this acceptance record:

```text
rendered_asset_change_count = 0
scientific_asset_change_count = 0
```

## Acceptance provenance

V4's LOG10 rendering remains valid presentation provenance.  V5's human
selection of the linear representation remains the final scale decision.  V6
performed only publication-label/title polish.  This record adds the explicit
external acceptance without rewriting any V4, V5, or V6 provenance document.

## Final status

```text
AUTOMATED_RENDER_QA = PASS
SCIENTIFIC_FREEZE_QA = PASS
HUMAN_VISUAL_QA = PASS
P0V3_FIGURE_RENDER_FINAL_ACCEPTED
```
