# Chapter 5 RefQ Fixed-Seed Louvain Reproducibility Audit v1

## Decision

`P0V3_DETERMINISTIC_HARDENING_PASS_READY_FOR_S2_S6_REGENERATION`

This audit found and corrected an ordering defect at the shared network
analysis boundary. The prior `analyze_undirected_view()` built an LCC with
`graph.subgraph(component).copy()` and only canonicalized community labels
after Louvain. The LCC node and neighbor insertion order therefore depended on
the iteration order of a set returned by `connected_components()`. Fixed
Louvain seeds did not define that representation order.

The in-memory canonical graph diagnostic removed the variation across all
authorized hash seeds and fresh processes while preserving official P0-v3
canonical community and brokerage authority. The production patch is
output-neutral for P0-v3 and is ready for a future clean S2-S6 regeneration.
No S1/S2 stage rerun, S3-S6 stage, P0, GH-CoRE, event rejoin, S7, figure, or
manuscript execution occurred in this task.

## Authorities and preserved evidence

- Repository: `D:/github_repo/OSDB_RefQ`
- Branch: `ch5-refq-repository-identity-correction-v1`
- Audit starting HEAD: `12a59ce292e313f3d860f03a85117e6df8699b56`
- Official P0-v3 result commit:
  `2d284f4bc83c42ba6555a09a2e42693c5490b827`
- Official P0-v3 manifest SHA-256:
  `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
- Official P0-v3 config SHA-256:
  `43f97f9a2d177d325415bfbcc504f1779882cf83685b4fdebe505c8fed8e7cb0`
- Frozen clean supplemental implementation before this hardening:
  `e13eaf2b3bff040639e6256ea98aa1fa5bb0ef1f`
- Accepted clean S1 output commit:
  `5a670d5157c8a84d545795ef3e8114a5724523dd`
- Existing uncommitted S2 partial remains untouched at:
  `supplemental/reference_quotient_v2/outputs_p0v3/S2_weight_sensitivity/`

The S2 six-file inventory was revalidated byte-for-byte against the prior
failure-review inventory. S1 and S2 receipts remained valid, and the clean
immutability baseline remained `HISTORICAL_IMMUTABILITY_MATCH` for historical
P0, P0-v2, P0-v3, supplemental v1, old supplemental-v2 outputs, and the
corrected aggregate.

## Production ordering path

Before hardening, the shared sequence was:

1. Convert input node IDs to strings and insert the configured node domain.
2. Insert undirected edge rows in input table order.
3. Enumerate `nx.connected_components(graph)`.
4. Select the largest component and call `graph.subgraph(lcc_nodes).copy()`.
5. Call `nx.community.louvain_communities(lcc, weight="weight", seed=...)`.
6. Sort the returned communities only after Louvain by size and minimum node to
   assign canonical labels.

Steps 3–4 exposed set iteration order to Louvain. The new shared helper
`canonicalize_undirected_graph_order()` rebuilds a simple undirected graph with
sorted string node IDs and lexicographically sorted normalized edge endpoints
before all order-sensitive network analysis. LCC selection now has a
deterministic size/minimum-node tie-break. Weights and all scientific
parameters are unchanged.

## Raw fixed-seed matrix

The harness launched fresh Python 3.9.13 processes with `PYTHONHASHSEED` set
before interpreter startup. For every threshold, it ran 20 processes at seed
0 and 5 processes each at seeds 1, 2, 42, and 20260731 (40 runs per graph
mode, 160 raw and 160 canonical runs). The diagnostic used only the existing
S2 threshold edge tables and official P0-v3 node registry; it never called a
stage writer.

Raw graph results:

| Threshold | Runs | Raw LCC node/edge/adjacency orders | Partition digests | Community counts | Modularity values |
|---:|---:|---:|---:|---:|---:|
| 1 | 40 | 1 / 1 / 1 | 1 | 35 | 0.7969220043681785 |
| 2 | 40 | 5 / 5 / 5 | 5 | 30, 31, 32, 33 | 0.7966022539777434 … 0.7970506377080826 |
| 5 | 40 | 5 / 5 / 5 | 5 | 25, 26 | 0.7955541407309554 … 0.7964351301769141 |
| 10 | 40 | 5 / 5 / 5 | 5 | 20, 21, 22 | 0.7846128064957263 … 0.7858423086877339 |

Full graph node and edge order fingerprints were stable (one each); the
variation began at raw LCC node/edge/adjacency order. Within each fixed hash
seed, repeated fresh processes were stable, confirming that the earlier
same-runtime variation was a diagnostic-methodology gap rather than unexplained
randomness.

## Canonical graph matrix

After in-memory canonical rebuilding, every threshold had exactly one analysis
graph node order, edge order, adjacency order, partition digest, community
count, and modularity across all 160 fresh processes and all five hash seeds:

| Threshold | Unique partition | Communities | Modularity |
|---:|---:|---:|---:|
| 1 | 1 | 35 | 0.7969220043681785 |
| 2 | 1 | 31 | 0.7970287474802773 |
| 5 | 1 | 28 | 0.7962674935766076 |
| 10 | 1 | 21 | 0.7851714821417686 |

The complete row-level matrix, including all graph-order and partition
fingerprints, is frozen in
`ch5_refq_fixed_seed_louvain_reproducibility_matrix_v1.csv`.

## P0-v3 authority impact gates

Using the canonical threshold-1 graph and clean NetworkX 3.1 runtime:

- canonical LCC: 6,367 nodes and 9,462 edges;
- canonical community count: 35;
- project-to-community mapping versus official P0-v3: 6,367/6,367 exact;
- modularity: `0.7969220043681785`, within absolute tolerance `1e-12`;
- community-size closure: every recorded size equals actual group cardinality;
- brokerage k=500, seed=20260731: every score within `1e-12` of official P0-v3;
- brokerage top-50 order: exact.

Therefore:

```text
P0V3_CANONICAL_PARTITION_PARITY = PASS
P0V3_CANONICAL_MODULARITY_PARITY = PASS
P0V3_CANONICAL_BROKERAGE_PARITY = PASS
P0_V4_REQUIRED = NO
DETERMINISTIC_HARDENING_OUTPUT_NEUTRAL_FOR_P0V3 = YES
```

The prior S4 robustness probe (`minimum ARI ≈ 0.6823671359861659`) is not a
scientifically interpretable final result yet. S4 must be regenerated after
this hardening so that its across-seed variation is not confounded by graph
iteration order.

## Implementation and regression scope

The shared helper is used by `network_views.analyze_undirected_view`, the
corrected P0 S4/S5 canonical-LCC loader, and S4/S5 computation entry points.
Regression coverage proves shuffled node/edge insertion invariance, fresh
hash-seed process repeatability, four frozen threshold deterministic summaries,
P0-v3 partition/modularity/brokerage parity, community-size closure, and
S4/S5 order invariance.

The hardening changes deterministic execution behavior only:

```text
scientific_logic_change_count = 0
deterministic_execution_contract_change_count = 1
```

Regression evidence:

- supplemental suite: `201 passed / 0 failed` under
  `D:/codex_envs/ch5_refq_supplemental_p0v3_runtime`;
- shared Chapter 5 under supplemental runtime: `56 passed / 0 failed` when
  excluding the pandas-1.4.4 P0 runtime-lock assertion;
- shared Chapter 5 under accepted P0 runtime
  `D:/codex_envs/ch5_refq_p0_v2_runtime`: `60 passed / 0 failed`;
- targeted deterministic/hardening suite: `40 passed / 0 failed`;
- `compileall`: PASS;
- `git diff --check`: PASS.

The three legacy test assumptions that the clean output root must not exist
were updated to assert byte immutability/no-write behavior, because this task
must preserve the authorized partial S2 directory. No scientific output was
rewritten.

## Future execution disposition

The existing S2 partial was generated before deterministic hardening and remains
`SUPERSEDED_UNCONTROLLED_ORDER_EXECUTION`; it is not committed or deleted in
this task. Future authorized work must:

```text
S1 = KEEP_ACCEPTED
S2 = RERUN_REQUIRED
S3 = RERUN/RUN_REQUIRED
S4 = RUN_REQUIRED
S5 = RUN_REQUIRED
S6 = RUN_AFTER_S4_S5
S7 = DEFER
```

No S1/S2 rerun, no S2 acceptance commit, no downstream stage, no P0-v4
regeneration, no figures/manuscript update, and no push occurred here.
