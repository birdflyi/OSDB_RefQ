# Chapter 5 RefQ C4-S2/S3 Identifier-Representation Parity Hotfix v1

## Scope and provenance

This document records the separately authorized identifier-representation
hotfix based on `d3430ac2194ced80978c8591b4e2b2afa27c5028`. S1 remains closed
and untouched: implementation `fe327e17e0db66ca40bc97fc17309603bff2afc3`,
result `edb9441c7b276051224087fdf26d2e0cfcb78dba`.

No S1 rerun, P0 rerun, GH-CoRE rerun, event rejoin, S7, figure generation, or
manuscript update was performed.

## S2 attempt history and diagnosis

Attempt 1 stopped before canonical comparison with a pandas tuple-column
selector `KeyError` and created no S2 directory, receipt, or result commit.

Attempt 2 reached canonical comparison. The corrected-P0 authority and the
computed threshold-1 result each contained 9,547 rows. After converting
`node_u` and `node_v` to strings and applying the same ascending ordering, the
tables closed exactly: expected-only pairs 0, actual-only pairs 0, weight
mismatches 0, and directed-edge-count mismatches 0.

The failure was a representation defect: pandas inferred numeric-looking
authority IDs as integers, while computed IDs were strings, producing different
ordering and representation. Repository/project IDs are opaque; canonical
parity representation is string. Classification:
`NUMERIC_LOOKING_IDENTIFIER_DTYPE_AND_ORDERING_MISMATCH` /
`PARITY_COMPARATOR_REPRESENTATION_DEFECT`.

## S2 and S3 patch

S2 now normalizes both expected and actual undirected parity frames at the
comparison boundary. `node_u` and `node_v` must be non-missing, non-empty
strings; `weight` and `directed_edge_count` retain positive-integral
validation. Both frames are sorted by string `[node_u, node_v]` and compared
with exact four-column pandas semantics.

S3 now reads authority identifier columns with explicit `string` dtype and
applies the same boundary normalization to registry, edge, LCC, and community
parity frames. Community IDs and sizes remain integral numeric fields. View
generation, graph construction, thresholds, weights, directed edge counts,
community semantics, and tolerances are unchanged. The comparator still fails
closed for missing/extra rows, endpoint changes, weight changes,
directed-edge-count changes, and community changes.

## S4/S5 audit

`s45_canonical_graph.py` already explicitly reads `node_u`, `node_v`, and all
`project_id` fields as `string` for canonical edges, LCC edges, registry,
communities, and brokerage. No S4/S5 patch was required.

```text
S2_numeric_identifier_gap = CONFIRMED
S3_numeric_identifier_gap = CONFIRMED
S4_numeric_identifier_gap = REJECTED (already guarded)
S5_numeric_identifier_gap = REJECTED (already guarded)
```

## Production-representation tests

The C4 regression suite writes synthetic authority CSVs containing
numeric-looking IDs (`2`, `10`, `100`) without dtype metadata. Raw pandas reads
infer integer ID columns, while the actual S2 and S3 production parity
functions normalize both sides and pass. The tests mutate an S2 endpoint,
weight, directed-edge count, and remove a row; each mutation fails closed.
S3 mutation failure and the existing S4/S5 positive dynamic parity tests remain
covered.

## Regression and immutability

The full command `python -m pytest supplemental/reference_quotient_v2/tests -q`
must pass with zero failures. `python -m compileall supplemental/reference_quotient_v2`
and `git diff --check` are also required to pass before commit.

All nine S1 output files, including `stage_receipt.json`, remain byte/blob
identical to the `edb9441c7b276051224087fdf26d2e0cfcb78dba` result commit.
`scientific_logic_change_count = 0`.

## Commit boundary and execution status

The commit containing this document is the new
`C4_NETWORK_FROZEN_IMPLEMENTATION_COMMIT_V2` for S2-S6. It is distinct from
the S1 implementation baseline and must be used for all later corrected
network stages. No corrected S2-S6 scientific execution has occurred under
this V2 commit at document creation; stage execution remains pending the
post-commit S2 dry-run and sequential authorization gates.
