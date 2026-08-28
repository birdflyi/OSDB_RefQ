# Chapter 5 RefQ P0-v3 Final Figure Plan v1

## Scope and decision

This is a read-only migration plan. No figure was rendered, no panel data was
rewritten, and no scientific stage was rerun. Existing Phase 2-A/2-B assets are
scaffolds only: all ten `source_manifest.json` files report
`final_render_ready=NO`, and the workspace contains zero PNG, SVG, or PDF
outputs.

The numerical authority is the corrected P0-v3 root and the frozen supplemental
v2 package:

| authority | path | identity |
|---|---|---|
| corrected P0-v3 | `outputs/reference_quotient_p0_corrected_v3/` | manifest SHA-256 `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`; commit `2d284f4bc83c42ba6555a09a2e42693c5490b827` |
| supplemental v2 | `supplemental/reference_quotient_v2/outputs_p0v3/` | package manifest SHA-256 `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`; package commit `19e2f9a5d619de9620a6934f53321eb0704fe953` |
| S6 figure-ready manifest | `supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/figure_ready_manifest_v2.json` | SHA-256 `e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea` |
| historical S7 reserve | `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/` | fixed-object G09 record in `docs/freeze/ch5_refq_p0v3_s7_fixed_object_overlap_runtime_gate_v1.md`; comparison-only |

The old figure manifests are derived from release commit
`68d001551359d120bf2a06cc5e571742df7e7822` and point to supplemental v1 or
historical P0. Their layout and deterministic display logic may be reused only
after replacing every source path.

## Main-paper figures

### Figure 1: Evidence universe and project-mappable boundary

- Research question: RQ1; distinguish observable Reference records from the
  quotient-eligible project-mappable subset.
- Frozen inputs:
  `supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/evidence_universe_flow.csv`,
  `S1_evidence_universe/event_type_x_quotient_eligibility.csv`,
  `S1_evidence_universe/event_type_x_target_membership_status.csv`,
  `S1_evidence_universe/source_entity_type_x_quotient_eligibility.csv`, and
  `S6_figure_ready/rq1_event_type_distribution_plot.csv`.
- Encoding: Panel A is a unit-labelled flow; Panel B is an event-type bar or
  dot display; Panel C is a target-membership/eligibility cross-tab. RECORD,
  REFERENCE_RECORD/aggregated weight, and EDGE_COUNT must never share an axis.
- Deterministic rules: preserve package row order only where declared; otherwise
  sort event/entity labels lexicographically after numeric counts are fixed;
  retain all categories or explicitly label a visual-only `Other` aggregation.
- Message boundary: observable evidence is not task resolution, dependency,
  semantic intent, or causal influence.
- Caption brief: “Observable Reference evidence and its project-mappable
  boundary under the corrected source-admission contract.” Draft wording is
  deferred to the rendering task.
- Placement: main paper.
- Action: `RENDER_FROM_FROZEN_AUTHORITY`.

### Figure 2: Source-role and target-role views

- Research questions: RQ2a and RQ2b; keep source-complete seed observations
  separate from expanded target coverage and concentration.
- Frozen inputs:
  `outputs/reference_quotient_p0_corrected_v3/rq2a_source_role_metrics.csv`,
  `supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq2a_source_role_ecdf_ccdf.csv`,
  `S6_figure_ready/rq2a_source_role_quantiles.csv`,
  `outputs/reference_quotient_p0_corrected_v3/rq2b_target_role_metrics.csv`,
  `S6_figure_ready/rq2b_target_role_quantiles.csv`, and
  `outputs/reference_quotient_p0_corrected_v3/rq2b_target_concentration.json`.
- Encoding: Panel A uses ECDF/CCDF or quantile displays for out-degree and
  out-strength; Panel B uses target in-degree/in-strength coverage and a
  cumulative top-1/top-10/top-50 weight-share inset.
- Deterministic rules: source rows are the 294 seed projects; target rows are
  the frozen observable-target table; sort by declared metric descending with
  project ID ascending as tie-break; do not rank targets as “important”.
- Message boundary: strength is aggregated Reference-record weight; coverage
  is coverage of the 294 observed seed sources, not ecosystem importance.
- Caption brief: “Asymmetric source and target views of the observed Project-level
  RefQN.”
- Placement: main paper.
- Action: `RENDER_FROM_FROZEN_AUTHORITY`.

### Figure 3: Undirected structure, observation boundary, and modular neighborhood

- Research questions: RQ2c, with S3 and S4 qualification.
- Frozen inputs:
  `outputs/reference_quotient_p0_corrected_v3/rq2c_undirected_view_summary.json`,
  `supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/structural_summary.csv`,
  `S6_figure_ready/community_size_distribution.csv`,
  `supplemental/reference_quotient_v2/outputs_p0v3/S3_observation_sensitivity/observation_boundary_sensitivity.csv`,
  `supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_runs.csv`, and
  `S4_community_stability/louvain_stability_summary.json`.
- Encoding: Panel A is a compact structural metric strip plus community-size
  distribution; Panel B is an aligned comparison of the three declared
  observation views; Panel C is a paired community-count/modularity display with
  ARI-to-canonical annotation.
- Deterministic rules: use the canonical seed `20260731` only as the declared
  reference realization; keep node/edge/weight units separate; never draw a
  full-node hairball; sort community sizes numerically for display.
- S4 limitation: the canonical 35-community partition is one deterministic
  reference realization. Across 50 controlled seeds, community count is 32--37,
  42/50 ARI-to-canonical values are below 0.9, minimum ARI is
  `0.6823671359861659`, and minimum pairwise ARI is `0.6092441840471735`.
  Use the phrase **algorithmic modular neighborhood view**; do not imply stable
  true communities, a DBMS-subdomain taxonomy, or consensus clustering.
- Caption brief: “First-order undirected RefQ structure and the seed-sensitive
  algorithmic modular neighborhood view.”
- Placement: main paper, with the full run-level ARI table in Supplementary S2.
- Action: `RENDER_FROM_FROZEN_AUTHORITY`.

### Figure 4: RQ3 descriptive and FDR-bounded comparison

- Research question: RQ3; compare label-mode-sensitive descriptive and executed
  inferential fields without adding a new test.
- Frozen inputs:
  `outputs/reference_quotient_p0_corrected_v3/rq3_subdomain_descriptive_comparison.csv`,
  `outputs/reference_quotient_p0_corrected_v3/rq3_kruskal_fdr_effect_sizes.csv`,
  `supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq3_subdomain_descriptive_comparison_plot.csv`, and
  `S6_figure_ready/rq3_kruskal_fdr_effect_sizes_plot.csv`.
- Encoding: Panel A is a faceted dot-and-interval display of descriptive
  medians/means by category and label mode; Panel B is an epsilon-squared dot
  plot with BH-FDR status markers. Descriptive and inferential layers must be
  visually distinct.
- Deterministic rules: retain both `include_mixed` and
  `exclude_mixed_or_multilabel`; sort features by the frozen file order or a
  declared stable feature order; show `fdr_bh_reject_0_05` explicitly.
- Message boundary: results are local and label-mode sensitive; category labels
  are metadata and do not equal algorithmic communities or causal mechanisms.
- Caption brief: “Observed subdomain variation and FDR-bounded role/structure
  comparisons under the two declared label modes.”
- Placement: main paper.
- Action: `RENDER_FROM_FROZEN_AUTHORITY`.

## Supplementary figures and tables

### Supplementary S1: Reference-record multiplicity sensitivity

Use `supplemental/reference_quotient_v2/outputs_p0v3/S2_weight_sensitivity/edge_weight_sensitivity.csv`.
Render a two-panel threshold display and an exact table of thresholds 1, 2, 5,
and 10. The threshold is retained Reference-record multiplicity for an ordered
project pair, not independent-event support, semantic strength, or a selected
“optimal” threshold. Action: `RENDER_FROM_FROZEN_AUTHORITY`.

### Supplementary S2: Louvain stability

Use the frozen S4 run, pairwise, and summary files. Show all 50 runs or a
deterministic subset labelled as such, with ARI and pairwise-ARI distributions.
The panel must carry the S4 limitation and must not assign substantive meaning
to community IDs. Action: `RENDER_FROM_FROZEN_AUTHORITY`.

### Supplementary S3: Structural brokerage-candidate stability

Use the frozen S5 inclusion-frequency, run, and summary files. Report the
minimum Spearman `0.9998339514284217`, minimum top-50 overlap `0.82`, and
`robustness_alert=FALSE` only as ranking-stability evidence under the declared
settings. Do not call candidates influential, important, causal, or knowledge
brokers. Action: `RENDER_FROM_FROZEN_AUTHORITY`.

### Supplementary S4: Unit and weight-contract audit

Use the frozen S1 flow and edge-class files. Present a compact unit-aware table
that separates RECORD, REFERENCE_RECORD/aggregated weight, and EDGE_COUNT. This
is an audit table, not a semantic target classification. Action:
`RENDER_FROM_FROZEN_AUTHORITY`.

### Supplementary S5: Fixed-object evidence composition reserve

Use only the three historical S7 composition files listed in the G09 review.
This is a reviewer-reserve table for fixed source-top-50, target-top-50, and
directed-edge-top-100 objects. Do not reselect corrected top-N objects, claim
the corrected ranking is identical, or describe the table as a regenerated S7
result. Action: `MANUAL_DECISION` pending reviewer need; no render is implied.

## Internal Figure 0

Keep `figure0_internal_measurement_ontology` for internal unit-contract
maintenance only. It has no publication output target and must not be cited as
an empirical figure. Action: `KEEP`.

## Global rendering contract

1. Before rendering, verify the P0-v3 manifest SHA and supplemental package
   manifest SHA recorded above, then verify every panel source against the S6
   figure-ready manifest where applicable.
2. Rendering is a deterministic copy/format operation. It must not run P0,
   S1--S7, GH-CoRE, event rejoin, network recomputation, statistical tests,
   consensus clustering, resolution sweeps, or new thresholds.
3. Use stable numeric sorting and explicit tie-breaks; preserve declared units,
   view operators, seed ranges, and label modes.
4. Use a color-blind-safe role-based palette, with labels or marker shapes
   carrying all essential distinctions. Colors must not encode significance or
   semantic classes by themselves.
5. No full-node network layout, project-value ranking, dependency claim,
   knowledge-flow mechanism, task-resolution claim, or causal interpretation is
   allowed in any caption or axis label.
6. Generated outputs, if separately authorized later, must be written outside
   the frozen scientific roots and recorded with hashes and a render receipt.

## Final proposed set

Main paper: Figures 1--4. Supplement: S1--S4, with S5 held as reviewer reserve.
Figure 0 remains internal. This is the minimum sufficient set supported by the
frozen results; no decorative or redundant plot is proposed.
