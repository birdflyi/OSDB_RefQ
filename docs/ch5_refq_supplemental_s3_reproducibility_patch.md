# RefQ Supplemental S3-Only Canonical Reproducibility Patch

## Decision

```text
S3_REPRODUCIBILITY_PATCH = PASS_READY_FOR_HUMAN_REVIEW
S2_STATUS = EXCLUDED_PENDING_WEIGHT_SEMANTICS_AUDIT
```

This patch corrects only the S3 observation-boundary sensitivity construction. It does not inspect or reinterpret S2 results, modify S2 outputs or wording, rerun edge-weight sensitivity, make claims about `w >= 2`, or perform a raw-data scan.

## Root Cause

The old S3 path reconstructed the undirected graph in supplemental code. It passed node domains through Python `set` objects and used a separate edge-to-undirected builder. This removed the deterministic node insertion order used by the canonical P0 path.

The canonical P0 implementation instead:

1. sorts/aggregates the directed rows through `directed_to_undirected_edges`;
2. builds the directed graph in the resulting deterministic row order;
3. converts it through the shared `DG2G` implementation;
4. inserts the full node registry in its CSV order before adding edges;
5. extracts the LCC and calls NetworkX Louvain with seed `20260731`.

For seeded Louvain, the same weighted edge set is not sufficient when graph node insertion order differs. The old S3 canonical row therefore produced 33 communities and modularity approximately `0.7962346034264995`, despite matching the non-stochastic structural metrics.

## Corrected Construction

The corrected S3 implementation reuses `script.ch5_reference_quotient.network_views.directed_to_undirected_edges` and `analyze_undirected_view`. It preserves:

- canonical node-registry order for `CANONICAL_SEED_CENTERED_OBSERVED`;
- seed-manifest order for `SEED_ONLY_INDUCED`;
- registry order restricted to seeds plus the fixed multi-seed target set for `MULTI_SEED_TARGET_VIEW`;
- first-order undirected view semantics;
- random seed `20260731`;
- canonical brokerage parameters only as part of the existing view analyzer.

The old S3 result remains at:

`supplemental/reference_quotient_v1/outputs/S3_observation_sensitivity/`

and is marked:

`SUPERSEDED_S3_NONCANONICAL_LOUVAIN_CONSTRUCTION_ORDER`

The corrected result is at:

`supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/outputs/S3_observation_sensitivity_corrected/`

## Canonical Row Recovery

| Metric | Old S3 canonical row | Corrected S3 canonical row |
|---|---:|---:|
| Nodes | 6,515 | 6,515 |
| Edge-observed nodes | 6,485 | 6,485 |
| Undirected edges | 9,557 | 9,557 |
| Components | 55 | 55 |
| Isolates | 30 | 30 |
| LCC nodes | 6,376 | 6,376 |
| LCC edges | 9,472 | 9,472 |
| LCC coverage | 0.9786646201074444 | 0.9786646201074444 |
| Average clustering | 0.0421978886450888 | 0.042197888645088825 |
| Transitivity | 0.0080461866658207 | 0.008046186665820756 |
| Community count | 33 | 34 |
| Modularity | 0.7962346034264995 | 0.7973095950243088 |
| Random seed | 20260731 | 20260731 |

Canonical recovery is exact for the required community count and modularity within `1e-12`. All non-stochastic structural metrics are unchanged.

## Corrected Restricted Views

| View | Nodes | Directed edges | Weight | Undirected edges | Components | Isolates | LCC nodes | LCC coverage | Clustering | Transitivity | Communities | Modularity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `CANONICAL_SEED_CENTERED_OBSERVED` | 6,515 | 9,605 | 139,044 | 9,557 | 55 | 30 | 6,376 | 0.9786646201074444 | 0.042197888645088825 | 0.008046186665820756 | 34 | 0.7973095950243088 |
| `SEED_ONLY_INDUCED` | 294 | 419 | 7,631 | 371 | 129 | 123 | 157 | 0.5340136054421769 | 0.17694197313661145 | 0.16256648936170212 | 13 | 0.7640545951865698 |
| `MULTI_SEED_TARGET_VIEW` | 1,299 | 4,349 | 69,670 | 4,310 | 63 | 62 | 1,237 | 0.9522709776751347 | 0.21972305939822673 | 0.03402921472618877 | 20 | 0.7764379829007504 |

The restricted-view changes are limited to the seeded algorithmic partition/modularity values and floating-point representations of deterministic metrics. Node, edge, weight, component, isolate and LCC counts are unchanged from the old S3 rows.

## Immutability and Execution Boundary

```text
raw_rescan_count = 0
canonical_p0_sha_drift = NO
S1_sha_drift = NO
S2_sha_drift = NO
S4_sha_drift = NO
S5_sha_drift = NO
S6_sha_drift = NO
S7_sha_drift = NO
existing_s3_sha_drift = NO
network_algorithms_rerun = 3 S3 views only
```

The patch reads existing canonical edge, node-registry and seed-manifest tables. It does not read frozen fine-grained input. The canonical P0 result remains the source of truth; corrected S3 is an additive supplemental result and does not replace P0 outputs.

## Tests

The S3-only test suite verifies:

- canonical nodes, edges, LCC, clustering, transitivity, community count and modularity;
- no drift in non-stochastic metrics between old and corrected S3 rows;
- all three corrected views and the exact 294-node seed-only domain;
- canonical, S1, S2, S4, S5, S6 and S7 immutability;
- zero raw scans and explicit S2 exclusion.

The S3 patch manifest records the generated output hashes and superseded old S3 path.

## Provenance

```text
canonical_parent_commit = 920286e134ca459c8e155942eabc6798ceab8b65
parent_supplemental_result_commit = ba72987adb2c2339bdf1f7a3b370278c88c29c3c
patch_implementation_commit = 9cb5dbd
```

No push was performed. The S2 weight semantics audit remains a separate pending task.
