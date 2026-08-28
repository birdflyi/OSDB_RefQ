# Chapter 5 RefQ Deterministic Graph-Order Hardening Review v1

## Scope and authorization

This review implements the conditional Phase E authorization from the
fixed-seed Louvain audit. It changes one shared graph-representation boundary
and does not run any scientific supplemental stage. S1 remains the accepted
checkpoint; the preserved S2 directory is not accepted or committed and must be
regenerated under this implementation.

```text
scientific_logic_change_count = 0
deterministic_execution_contract_change_count = 1
P0_V4_REQUIRED = NO
```

## Root cause

`network_views.analyze_undirected_view()` previously selected the LCC from
`connected_components()` and passed `graph.subgraph(lcc_nodes).copy()` directly
to NetworkX. A component is a set, so the copied graph's node and adjacency
insertion order depended on the interpreter's hash seed. Community labels were
sorted only after Louvain; that post-processing could not repair the order
already consumed by the stochastic algorithm. NetworkX's fixed `seed` controls
the shuffle RNG, but does not define this initial graph representation.

The raw diagnostic confirmed the causal boundary: full graph node/edge order
fingerprints were stable, while raw LCC node, edge, and adjacency fingerprints
varied across hash seeds. For thresholds 2, 5, and 10, five distinct raw LCC
orders produced five partition digests. Repeated processes at one fixed hash
seed were stable, which also explains why an earlier audit that omitted
pre-start `PYTHONHASHSEED` control gave misleading same-runtime variation.

## Hardening implementation

`canonicalize_undirected_graph_order()` now rebuilds a simple undirected graph
with:

1. sorted string node IDs;
2. normalized `(min(node_u, node_v), max(node_u, node_v), weight)` edge records;
3. lexicographic edge insertion;
4. preserved node and edge attributes.

LCC selection uses a deterministic `(-component_size, minimum_string_node)` tie
break. The helper is consumed by the shared production network view, the
corrected P0 S4/S5 canonical-LCC authority, and S4/S5 stochastic computation
entry points. No weight, threshold, random seed, resolution, modularity,
brokerage, or community-labeling rule changed.

## Impact gates

The canonical graph matrix ran 160 fresh processes across
`PYTHONHASHSEED=0,1,2,42,20260731` for each of four frozen S2 threshold edge
tables. Each threshold produced exactly one analysis graph order, adjacency
order, partition digest, community count, and modularity.

Official P0-v3 threshold-1 impact is neutral:

- LCC: 6,367 nodes / 9,462 edges;
- community partition: exact 6,367/6,367 project mapping;
- communities: 35;
- modularity: `0.7969220043681785` (absolute tolerance `1e-12`);
- community-size closure: PASS;
- brokerage k=500, seed=20260731: all scores within `1e-12`;
- brokerage top-50: exact.

The deterministic candidate threshold summaries under NetworkX 3.1 are:

| Threshold | Communities | Modularity |
|---:|---:|---:|
| 1 | 35 | 0.7969220043681785 |
| 2 | 31 | 0.7970287474802773 |
| 5 | 28 | 0.7962674935766076 |
| 10 | 21 | 0.7851714821417686 |

These are diagnostic candidate authority values only. They are not written into
the preserved S2 output. A future authorization must rerun S2 once and create
its output-only checkpoint under the hardened implementation.

## Regression closure

- deterministic/hardening targeted tests: `40 passed / 0 failed`;
- supplemental suite under clean runtime: `201 passed / 0 failed`;
- shared Chapter 5 under clean supplemental runtime: `56 passed / 0 failed`
  excluding the P0 pandas-1.4.4 lock assertion;
- shared Chapter 5 under accepted P0 runtime: `60 passed / 0 failed`;
- compileall: PASS;
- `git diff --check`: PASS.

The runtime-lock test was executed in
`D:/codex_envs/ch5_refq_p0_v2_runtime` (pandas 1.4.4). The supplemental tests
were executed in `D:/codex_envs/ch5_refq_supplemental_p0v3_runtime` (pandas
1.5.3). No scientific output writer, P0 regeneration, or downstream stage was
invoked.

## Future disposition

```text
S1 = KEEP_ACCEPTED
S2 = RERUN_REQUIRED
S3 = RERUN/RUN_REQUIRED
S4 = RUN_REQUIRED
S5 = RUN_REQUIRED
S6 = RUN_AFTER_S4_S5
S7 = DEFER
```

The previous S4 robustness probe is not yet scientifically interpretable and
must be regenerated after graph-order hardening. The existing S2 partial remains
preserved as `SUPERSEDED_UNCONTROLLED_ORDER_EXECUTION`; it is not deleted,
rewritten, or committed here.
