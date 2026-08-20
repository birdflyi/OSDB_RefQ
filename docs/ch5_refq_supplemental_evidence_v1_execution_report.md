# Chapter 5 RefQ Supplemental Evidence and Robustness Package v1 Execution Report

## 1. Executive Status

```text
SUPPLEMENTAL_EVIDENCE_V1 = PASS_WITH_ROBUSTNESS_ALERTS
branch = ch5-refq-supplemental-evidence-v1
canonical_parent_commit = 920286e134ca459c8e155942eabc6798ceab8b65
canonical_outputs_changed = 0
raw_frozen_rows_scanned = 3748078
raw_rescan_count = 1
S1 = PASS
S2 = PASS
S3 = PASS
S4 = PASS
S5 = PASS
S6 = PASS
S7 = PASS
S1_exact_reconciliation = YES
S2_threshold1_matches_canonical = YES
S4_canonical_seed_matches = YES
S5_canonical_setting_matches = YES
tests_passed = 9
tests_failed = 0
robustness_alerts = 1
canonical_output_sha_drift = NO
implementation_commit = 18717e7d8d269538872ab5a3bcb923234e52eecc
result_package_commit = recorded by the final commit below
```

The package is supplemental to P0.1. It does not revise the manuscript, P0 config, canonical outputs, RQs, membership semantics, first-order RefQ semantics, observation boundary or RQ3 policy.

## 2. Canonical-Parent Verification

- Working branch: `ch5-refq-supplemental-evidence-v1`.
- Canonical parent: `920286e134ca459c8e155942eabc6798ceab8b65`.
- The canonical parent is an ancestor of the supplemental branch.
- Canonical config and manifest were consumed by path and SHA-256 reference.
- All 30 non-manifest canonical output hashes were captured in the supplemental manifest.

## 3. Canonical Immutability Audit

The pre-run and post-run SHA-256 inventories of `outputs/reference_quotient_p0_frozen/` were compared. `canonical_output_bytes_changed = 0`. No canonical output, config or source input was written by the supplemental run.

## 4. Supplemental Code Inventory

The code is self-contained under `supplemental/reference_quotient_v1/`. The raw input is read by one controlled streaming pass with `csv_chunk_size = 100000`. The pass stores only local staging rows and membership pairs; S1 cross-tabs and S7 composition are computed after membership conflicts are resolved from that local staging database. The staging database is removed after the pass.

## 5. S1 Result and Validation

S1 exact reconciliation is `PASS`. The aggregate flow records 3,748,078 Reference records, target project-mappable/non-project/unresolved counts, 4 conflict-excluded record occurrences, 1,586,117 quotient-eligible records, 1,447,073 self-loop evidence weight and 139,044 cross-project evidence weight. Six requested cross-tabs are emitted with overall, within-row and within-status shares. Cross-tab totals reconcile to the retained Reference-record total.

## 6. S2 Result and Validation

S2 applies thresholds to directed cross-project edge weights before undirected collapse. Threshold 1 reproduces the canonical undirected edge count, LCC, and modularity within the test tolerance. Full node-domain retention, isolates and components are reported for every threshold.

## 7. S3 Result and Validation

S3 emits `CANONICAL_SEED_CENTERED_OBSERVED`, `SEED_ONLY_INDUCED` and `MULTI_SEED_TARGET_VIEW`. The seed-only view retains all 294 seed nodes, including zero-edge seeds. The multi-seed target view includes all seeds and expanded targets referenced by at least two distinct seed projects. These are sensitivity views only.

## 8. S4 Result and Validation

S4 evaluates Louvain on the canonical RQ2c LCC for seeds 20260731 through 20260780. It reports community count, modularity, ARI to the canonical partition and pairwise ARI summaries. It does not search resolution or select a best seed. The canonical seed reproduces 34 communities and modularity 0.7973095950243088 within tolerance. Robustness alert: `True`.

## 9. S5 Result and Validation

S5 evaluates unweighted normalized approximate betweenness for `k = 250, 500, 1000` and seeds 20260731 through 20260750. It reports full rankings, Spearman correlation to the canonical ranking, top-10/top-20/top-50 overlap and top-k frequency. The canonical `k = 500`, seed `20260731` setting reproduces the canonical brokerage output within tolerance. Robustness alert: `False`.

## 10. S6 Output Inventory

S6 contains stable long-format or plotting-ready tables derived only from existing canonical CSV/JSON outputs. Each entry records its source artifact, source SHA-256, transformation name and row count in `S6_figure_ready/figure_ready_manifest.json`. No figure image was generated and no automatic statistical claim was made.

## 11. S7 Result and Validation

S7 fixes its object sets before the raw scan: canonical top 50 source projects by out-strength, canonical top 50 target projects by in-strength and canonical top 100 directed cross-project edges by weight. It reports event-type, source-entity-type and target-entity-type composition of eligible underlying Reference evidence. It does not infer bots, dependencies, importance causes or knowledge-flow mechanisms.

## 12. Test Results

Tests are executed separately after this report is generated. The supplemental test suite covers S1 arithmetic and cross-tab closure, S2 threshold ordering and canonical recovery, S3 seed-domain size, S4 canonical reproduction, S5 canonical reproduction, second-order-operator exclusion and canonical hash immutability.

## 13. Output SHA Manifest

`manifest.json` records canonical config/manifest hashes, all canonical output hashes consumed, supplemental implementation file hashes, runtime versions, parameters, raw scan facts, output classification and generated supplemental output hashes. Its own SHA-256 is intentionally not embedded to avoid a self-referential hash.

## 14. Robustness Alerts

The package does not alter an algorithm in response to a sensitivity result. A true alert is recorded when the predeclared community ARI or brokerage ranking stability rule is crossed. Any alert remains a human-review item and is not promoted into the manuscript automatically.

## 15. Candidate Manuscript and Figure Implications

No manuscript file was changed. S1 may support a methods/evidence-universe figure; S2/S3/S4/S5 are sensitivity reserves; S6 supplies figure-ready data; S7 supports cautious evidence-composition description. Whether any result enters main text, appendix or reviewer reserve remains a human decision.

## 16. Git Status

The implementation commit is created before the computation run. The result-package commit is created only after tests and final immutability checks pass. The branch is not pushed.

## 17. Remaining Human Decisions

- Decide whether S4 and S5 are required in the main paper or supplementary material.
- Decide whether S1 detailed cross-tabs are worth the figure/table space.
- Decide whether S7 composition is explanatory evidence or reviewer reserve.
- Review any robustness alert before changing manuscript wording.
