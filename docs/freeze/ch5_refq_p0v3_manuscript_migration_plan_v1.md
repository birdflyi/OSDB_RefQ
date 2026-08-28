# Chapter 5 RefQ P0-v3 Manuscript Migration Plan v1

## Decision and authority

`P0V3_PRESENTATION_MIGRATION_PLAN_PASS_READY_FOR_EXECUTION`

This decision authorizes a later, separately controlled manuscript migration;
it does not modify the manuscript in this task. The target manuscript is
unambiguous by the external citation-precision report and its SHA-256, but it
has no Git commit provenance:

```text
MANUSCRIPT_SOURCE_PATH = C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean.md
MANUSCRIPT_SOURCE_SHA256 = 4BA2DB1B45C97D0823C4909C705FC307AA3A992E4B2C2E59096FC630A871FD88
MANUSCRIPT_SOURCE_COMMIT = UNVERSIONED_EXTERNAL_WORKSPACE
MANUSCRIPT_STATUS = DOCUMENTED_TARGET_SHA_PINNED_COMMIT_PROVENANCE_UNAVAILABLE
```

The source selection is recorded in
`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/docs/ch5_reference_quotient_v1_4_3_1_citation_precision_and_necessity_report_v1.0.md`.
Before any future edit, the operator must re-hash the file and refuse the
migration if the SHA differs. Other v0.7--v1.4.3 manuscript candidates remain
historical comparison artifacts and were not edited.

Numerical authority is strictly ordered as follows:

1. `outputs/reference_quotient_p0_corrected_v3/` (P0-v3, manifest SHA
   `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`, commit
   `2d284f4bc83c42ba6555a09a2e42693c5490b827`).
2. `supplemental/reference_quotient_v2/outputs_p0v3/` (package manifest SHA
   `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`,
   package commit `19e2f9a5d619de9620a6934f53321eb0704fe953`).
3. Historical S7 files only under the G09 fixed-object decision; they are not
   corrected top-N outputs.

Historical P0 and supplemental v1 values are comparison/audit evidence only.

## Frozen numeric replacements

The following values are the replacement anchors for all repeated manuscript
mentions. Exact table rows must be copied from the cited files rather than
retyped or recomputed.

| quantity | corrected value | frozen source |
|---|---:|---|
| seed projects | 294 | `outputs/reference_quotient_p0_corrected_v3/seed_observability_audit.json` |
| scanned input records | 3,748,078 | `outputs/reference_quotient_p0_corrected_v3/quotient_construction_audit.json` |
| admitted source-observation records | 3,747,958 | `outputs/reference_quotient_p0_corrected_v3/quotient_construction_audit.json`; `supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/evidence_universe_flow.csv` |
| out-of-seed records | 120 | same two sources |
| quotient-eligible records | 1,586,047 | same two sources |
| self-loop weight | 1,447,073 | same two sources |
| cross-project weight | 138,974 | same two sources |
| directed edges including self-loops | 9,884 | `outputs/reference_quotient_p0_corrected_v3/quotient_construction_audit.json` |
| self-loops | 289 | same source |
| directed cross-project edges | 9,595 | same source |
| project node domain | 6,506 | same source |
| P0 edge-observed nodes | 6,505 | same source |
| undirected edge-observed nodes | 6,476 | `outputs/reference_quotient_p0_corrected_v3/rq2c_undirected_view_summary.json` |
| undirected edges | 9,547 | same source |
| components / isolates | 55 / 30 | same source |
| LCC nodes / edges | 6,367 / 9,462 | same source |
| LCC directed sensitivity edges | 9,510 | same source |
| LCC coverage | 0.9786351060559484 | same source |
| average clustering / transitivity | 0.04225758251235413 / 0.008047960961122938 | same source |
| canonical communities / modularity | 35 / 0.7969220043681785 | same source and `S6_figure_ready/structural_summary.csv` |
| expanded target projects | 6,212 | `outputs/reference_quotient_p0_corrected_v3/seed_observability_audit.json` |
| observable target projects | 6,322 | `outputs/reference_quotient_p0_corrected_v3/rq2b_target_concentration.json` and `rq2b_target_role_metrics.csv` |
| seed-project targets | 110 | `outputs/reference_quotient_p0_corrected_v3/rq2b_target_role_metrics.csv` |
| source relation totals (seed-to-seed / seed-to-expanded) | 418 / 9,177; weights 7,630 / 131,344 | `outputs/reference_quotient_p0_corrected_v3/rq2a_source_role_metrics.csv` |

## Section-by-section actions

### Abstract (lines 1--14)

`NUMERIC_UPDATE`: line 8 repeats the core counts. Replace the old node, edge,
weight, and LCC values with the frozen anchors above. Keep the 294-seed,
seed-centered and weaker-semantic framing. Do not add a claim of stable
communities or causal influence.

`SEMANTIC_UPDATE`: retain RefQ as a paper-specific construct and Reference
Coupling as prior work. The existing negative-boundary wording is acceptable.

### Sections 1--2: introduction and related work (lines 16--95)

`UNCHANGED` for literature positioning and RQ structure. Occurrences of 294 in
lines 30, 45, 52, 55, and 60 remain correct after authority verification.
`SEMANTIC_UPDATE` only where the migration adds the phrase “algorithmic
modular neighborhood view” to community references. Preserve the explicit
statement that project-level aggregation, direction, and count weighting are
not claimed as novel. No generic RQ2 wording remains; use RQ2a/RQ2b/RQ2c.

### Section 3: methods (lines 97--369)

`NUMERIC_UPDATE`: replace the repeated boundary summary in lines 101--113 and
369 with the corrected anchors. Add the explicit 120 out-of-seed record count
only if the final methods layout has a source-admission flow; otherwise keep it
in the data-availability/boundary note.

`UNCHANGED`: the 294 seed sample, 2023 observation window, active-unit
threshold of 10, and the `Q=M^T R_P M` construction remain unchanged. These
are contract/configuration facts, not regenerated statistics.

`SEMANTIC_UPDATE`: preserve the two-universe distinction, unique membership,
self-loop policy, non-project boundary, and seed-centered observation. The
unidirectional source observation must not be generalized to expanded targets.

### Section 4.1: RQ1 fine-grained evidence (lines 375--525)

`NUMERIC_UPDATE`: migrate every result paragraph and table from the following
frozen files:

- `rq1_referencing_entity_distribution.csv` for Table 4.1. The current file
  has the complete event-type rows; the old five-row `Other` aggregation must
  not be silently retained.
- `rq1_referenced_entity_distribution.csv` for Table 4.2. Use the complete
  fine-grained target-entity rows rather than the old six-row aggregation.
- `rq1_descriptive_statistics.csv` for Tables 4.3--4.5 and the self-reference
  profile paragraph. This updates the 41.68/39.37/25.63/58.45 self-reference
  summary and the active-issue, comment-per-issue, and comment-density rows.
- `rq1_project_age_cross_sectional_association.csv` for Table 4.6a and lines
  507--525. The corrected correlations are -0.11817282564989658,
  0.11817282564989658, 0.15735877529004005, and 0.1417469559448153, with the
  four p-values in that file.

`SEMANTIC_UPDATE`: keep all RQ1 claims descriptive. Do not turn non-project
share, comment density, or age association into openness, knowledge, or causal
claims. The corrected profile confirms the named examples but changes
WiredTiger to 15,332 total records, 12,891 self records, and self-reference
ratio `0.8407905035220454`; SSDB, GreatSQL, H2, AlaSQL, and pubkey/rxdb remain
file-backed. Use the corrected rows and remove the old 100,190/84,239 counts.

### Section 4.2: RQ2a/RQ2b/RQ2c (lines 528--613)

`NUMERIC_UPDATE`: replace Tables 4.6b--4.6f and their surrounding paragraphs.

- Table 4.6b uses `quotient_construction_audit.json` and
  `rq2c_undirected_view_summary.json`; all old 1,586,117, 139,044, 6,485,
  9,520, 6,376, and 34/0.797309595 values are stale.
- Table 4.6c uses `rq2a_source_role_metrics.csv` and the S6 quantile file.
  Preserve the 294-source denominator and replace relation totals with 418 and
  9,177 (weights 7,630 and 131,344).
- Table 4.6d uses `rq2b_target_role_metrics.csv` and
  `rq2b_target_concentration.json`: 6,322 observable targets, 110 seed targets,
  and 6,212 expanded targets. The corrected metadata-unavailable target count
  is 6,191. Concentration shares must be read from the JSON.
- Table 4.6e uses the corrected undirected summary and S4 limitation. The
  canonical result is 35 communities and modularity
  `0.7969220043681785`.
- Table 4.6f uses the complete corrected
  `rq2c_structural_brokerage_top50.csv`; the old top-five values, order, and
  community IDs must be replaced together.

`SEMANTIC_UPDATE`: community membership is an algorithmic modular neighborhood
view. Brokerage is a bridge-like structural candidate under an unweighted
approximate-betweenness sample, never project importance, influence, or
knowledge flow. Keep directed and undirected edge counts separate.

### Section 4.3: RQ3 (lines 615--664)

`NUMERIC_UPDATE`: migrate Table 4.7 and Table 4.8, the descriptive example in
line 621, the out-degree comparison in line 658, and the project-age comparison
in line 662 from:

- `outputs/reference_quotient_p0_corrected_v3/rq3_subdomain_descriptive_comparison.csv`
- `outputs/reference_quotient_p0_corrected_v3/rq3_kruskal_fdr_effect_sizes.csv`
- `outputs/reference_quotient_p0_corrected_v3/rq3_seed_role_aware_features.csv`

Use both `include_mixed` and `exclude_mixed_or_multilabel` rows exactly as
stored. The corrected effect file includes 10 groups for include-mixed and
updated n-with-replacement and FDR values; do not preserve the old rounded
table values.

`SEMANTIC_UPDATE`: category labels are metadata, not RQ2c communities. Report
descriptive differences, executed Kruskal-Wallis/FDR fields, and label-mode
sensitivity without claiming a universal subdomain effect, mechanism, or
causality.

### Section 5: discussion (lines 666--698)

`NUMERIC_UPDATE`: line 697's 9,605 and 9,557 must use the corrected values;
other numeric statements repeated from Section 4 must be synchronized with the
same authority files. Do not introduce a new result in discussion.

`SEMANTIC_UPDATE`: retain the bounded formalization/reframing contribution and
the distinction from Reference Coupling. Add the corrected S4 wording wherever
the canonical partition is summarized. Keep brokerage as structural position
description only.

### Sections 6--9 (lines 702--758)

`UNCHANGED` for validity, data availability, and conclusion structure, subject
to propagation of corrected values and the S4/S5 boundary language. Line 726's
fixed 500-node approximate-betweenness setting remains correct and maps to
`rq2c_undirected_view_summary.json` and the S5 contract. Do not imply that
unobserved channels or expanded-target source behavior were measured.

No current main-text S7 quantitative claim was found. If a reviewer asks for
S7 composition, add it only as a fixed-object reserve note under G09; do not
reselect corrected top-50/top-100 objects or claim an S7 rerun.

### Appendix A (lines 761--803)

`STRUCTURAL_UPDATE` is required. Replace the historical reproducibility block
with the corrected package identity:

- branch `ch5-refq-repository-identity-correction-v1`;
- P0-v3 root `outputs/reference_quotient_p0_corrected_v3` and its manifest/config
  hashes;
- supplemental root `supplemental/reference_quotient_v2/outputs_p0v3` and
  package manifest SHA `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`;
- accepted runtime Python 3.9.13, pandas 1.5.3, NumPy 1.26.4, SciPy 1.13.1,
  NetworkX 3.1, GH-CoRE 2.3.1;
- package status `STAGE_PACKAGE_COMPLETE` / `RELEASE_READY`, S7
  `KEPT_FIXED_OBJECT`, and S4 `ACCEPT_WITH_LIMITATION`.

Replace line 783's old 1,586,117 quotient-eligible value with 1,586,047 and
retain the corrected edge/weight fields. Replace line 785's old 6,221 expanded
target count with 6,212; retain 262 positive-out-degree seeds and 32 zero-out-
degree seeds if the corrected audit is cited. The Appendix must state that
expanded targets are not source-complete and that no second-order projection
was executed.

## S4, S5, and S7 wording gates

- S4: no occurrence currently overclaims a stable or true partition, but the
  single “34 communities” claim and Table 4.6e require numeric and semantic
  replacement. Add the frozen 50-run range 32--37, 42/50 ARI below 0.9,
  minimum ARI `0.6823671359861659`, and minimum pairwise ARI
  `0.6092441840471735` when discussing stability.
- S5: current brokerage language is non-causal and therefore semantically
  acceptable; replace stale top-five values/IDs and, if stability is discussed,
  use minimum Spearman `0.9998339514284217`, minimum top-50 overlap `0.82`, and
  `robustness_alert=FALSE` from the frozen S5 summary.
- S7: no current quantitative claim is present. Any future insertion must cite
  G09 and say `KEPT_FIXED_OBJECT`; it must not say corrected top-N was
  reselected, rankings are identical, or S7 was regenerated.

## Execution protocol after this plan

1. Re-hash the external manuscript and verify the path/SHA above.
2. Verify the P0-v3 and supplemental package manifest hashes.
3. Apply the numeric and semantic updates in one controlled manuscript change;
   keep an old-to-new diff for every line/table listed above.
4. Rebuild figures only from the separate figure plan and frozen sources; never
   compute new science during rendering.
5. Validate that every manuscript quantitative claim still maps to exactly one
   frozen path, then record the new manuscript SHA and an external-workspace
   provenance note.

No part of this plan authorizes P0/S1--S7 reruns, output rewrites, figure
generation, or manuscript edits in the current task.
