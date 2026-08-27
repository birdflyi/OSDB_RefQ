# Chapter 5 RefQ Corrected P0 v3 Community Metadata Impact Audit v1

## Baseline

Audit started at HEAD `0c73d5f6e95c1fa8227b11aec8c8f1643476e662`, on branch
`ch5-refq-repository-identity-correction-v1`, with a clean worktree. The
accepted corrected-P0 v2 manifest SHA is
`21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7`; the v2
config SHA is `e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658`.
The v2 manifest validates, and the accepted corrected aggregate hash closure is
294/294.

Corrected P0 v2 and historical outputs are frozen and will not be modified.

## Shared root cause

`script/ch5_reference_quotient/network_views.py` obtains raw Louvain
communities, assigns IDs from a sorted canonical community list, but computes
`community_size` by indexing the pre-sort `communities` list. This is a shared
canonical-label/index alignment defect:

```text
SHARED_COMMUNITY_SIZE_INDEXING_DEFECT = CONFIRMED
classification = REDUNDANT_COMMUNITY_METADATA_LABEL_ALIGNMENT_DEFECT
```

The defect affects only the redundant label-to-size association.

## Corrected-P0 v2 evidence

The v2 community table has 6,367 rows and 35 communities. Every community ID
has a recorded size that differs from its actual row cardinality, yet the
recorded size multiset equals the actual size multiset exactly. Thus the defect
is a permutation of sizes across canonical labels, not a changed partition.
The partition is unique and complete over the 6,367-node canonical LCC.

The frozen v2 graph reconstructed from canonical edges has 6,367 nodes and
9,462 LCC edges. Modularity recomputed from that graph and the existing
project-to-community mapping is `0.7969220043681784`, versus recorded
`0.7969220043681785` (absolute difference approximately `1.1e-16`, within
`1e-12`).

Brokerage calculation consumes graph structure and numeric network parameters,
not `community_size`. Graph metrics and directed/undirected RefQ edge tables
are produced before and independently of this redundant field. Therefore:

```text
project_to_community_partition_integrity = PASS
partition_coverage = PASS
canonical_modularity_recomputed_parity = PASS
graph_structure_integrity = PASS
brokerage_scientific_integrity = PASS
community_size scientific dependency = NONE
SCIENTIFIC_PARTITION_CHANGE_REQUIRED = NO
SCIENTIFIC_GRAPH_CHANGE_REQUIRED = NO
REDUNDANT_METADATA_FIX_REQUIRED = YES
```

## Historical impact

The frozen historical P0 community table and the historical supplemental v1
S3 community tables show the same class of label-to-size mismatch. Their size
multisets/distributions remain invariant under the permutation. Historical
assets are immutable; corrected-vs-historical comparisons must distinguish
per-community label association from the global community-size distribution.

## Repository-wide consumer audit

The accompanying CSV enumerates executable producers and consumers. No
scientific P0 graph, partition, brokerage, RQ1, RQ2a, RQ2b, or RQ3 computation
consumes recorded `community_size`. Supplemental S6 derives a display/distribution
artifact and the S45 loader validates closure; both should use clean v3 authority
for future regeneration. `unexpected_scientific_consumers = 0`.

## Decision

The audit passes the clean-asset gate. The shared producer will be corrected,
tested, and frozen in a new implementation commit. A versioned P0 v3 config and
output root will then be used for exactly one regeneration from the same accepted
294-partition aggregate authority. Supplemental stages are not executed in this
task; a separate migration plan will specify which stages must be rerun under
v3 provenance.
