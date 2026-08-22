# Chapter 5 RefQ Weight / Multiplicity Contract Clarification Patch

## Status

```text
REFQ_WEIGHT_MULTIPLICITY_CONTRACT_PATCH = PASS_READY_TO_PUSH
parent_freeze_commit = 82e992aadd6c8e63ca699d766148d11f35ef7d0a
scientific_numbers_changed = NO
raw_scan_count = 0
scientific_experiments_rerun = 0
network_algorithms_rerun = 0
push = NO
```

This v1.3 patch is a pre-push contract/schema clarification. It does not
rerun P0 or any supplemental scientific analysis and does not change the
canonical RefQ theory, RQs, numeric outputs, or frozen input interpretation.

## Exact field contract

For a canonical directed RefQ edge:

```text
multiplicity = number of retained eligible fine-grained Reference records
               aggregated into the ordered project pair

weight = analytical numeric edge weight consumed by downstream network analyses

current P0: weight := multiplicity
```

Therefore, under the current unit-weight operationalization:

```text
weight == multiplicity == aggregated retained eligible Reference-record count
```

This equality is a current operationalization, not a theoretical invariant of
`Q = M^T R_P M` and not a generic `MDG2DG`/`DG2G` graph API invariant. The
shared graph converter can carry distinct `weight` and graph-instance
`multiplicity` values.

For the first-order RefQ undirected view:

```text
undirected weight = sum of directed analytical edge weights
directed_edge_count = number of directed edge-table rows collapsed into the
                      unordered pair
```

`directed_edge_count` is not a Reference-record count and does not propagate
the input RefQ evidence-multiplicity field.

## S1 flow correction

The historical flow remains unchanged:

```text
old status = SUPERSEDED_UNIT_LABEL_ONLY
old path = supplemental/reference_quotient_v1/outputs/S1_evidence_universe/evidence_universe_flow.csv
old sha256 = c9951e5d61c0e16b3c10d18329f1ac95219c7cb49c05a11ab9891eeffa00dc48
```

The additive human-use copy is authoritative for the corrected unit labels:

```text
corrected status = AUTHORITATIVE_UNIT_LABEL_CORRECTED
corrected path = supplemental/reference_quotient_v1/v1_3_weight_multiplicity_contract_patch/outputs/S1_evidence_universe/evidence_universe_flow_corrected.csv
corrected sha256 = 1404ed2cfb2fc4e0f6001c03ac307e52af2e40be5c3a15eaa09107b4cc7bd2b8
```

The corrected flow preserves the existing record counts and makes the two
record-weight rows explicit:

| stage | count | unit | measure |
|---|---:|---|---|
| `self_loop_evidence_weight` | 1,447,073 | `REFERENCE_RECORD` | `AGGREGATED_EDGE_WEIGHT` |
| `cross_project_evidence_weight` | 139,044 | `REFERENCE_RECORD` | `AGGREGATED_EDGE_WEIGHT` |
| `self_loop_edge_count` | 289 | `EDGE_COUNT` | `SELF_LOOP_EDGE_COUNT` |
| `cross_project_directed_edge_count` | 9,605 | `EDGE_COUNT` | `CROSS_PROJECT_DIRECTED_EDGE_COUNT` |

The 289 and 9,605 values are structural edge counts and remain separate from
the 1,447,073 and 139,044 aggregated Reference-record weights.

## Producer label fix

`supplemental/reference_quotient_v1/scripts/run_supplemental.py` now emits the
record-weight rows with:

```text
unit = REFERENCE_RECORD
measure = AGGREGATED_EDGE_WEIGHT
```

The first seven flow rows retain their original numeric values and `RECORD`
unit labels. No count arithmetic, membership logic, edge construction,
threshold, or scientific result was changed. The producer change is classified
as:

```text
SCHEMA_LABEL_BUGFIX
```

## Tests

The lightweight contract tests cover:

1. RefQ `edge_frame` current unit mode sets `weight == multiplicity`.
2. Generic `MDG2DG`/`DG2G` can preserve distinct `weight` and graph-instance
   `multiplicity`, so the equality is not enforced generically.
3. `A -> B` weight 37 plus `B -> A` weight 8 produces undirected weight 45
   and `directed_edge_count` 2.
4. The corrected S1 flow uses `REFERENCE_RECORD` for 1,447,073 and 139,044,
   and `EDGE_COUNT` for 289 and 9,605.

No test invokes the P0 runner or reruns S1-S7.

The executed RefQ unit/API suite completed with:

```text
tests_passed = 22
tests_failed = 0
```

## Validation and immutability

The generic edge validator was not changed to require
`weight == multiplicity`. Any future P0-specific equality assertion is scoped
to `CURRENT_REFQ_UNIT_WEIGHT_MODE`; transformed analytical weights are not
implemented in this patch.

Existing hash inventories were rechecked after the patch:

```text
P0 non-manifest outputs = 30/30 hash matches
supplemental main outputs = 49/49 hash matches
v1.1 completion outputs = 9/9 hash matches
corrected S3 outputs = 10/10 hash matches
canonical P0 scientific outputs drift = 0
S2-S7 scientific numeric outputs drift = 0
corrected S3 remains authoritative = YES
old S1 flow remains unchanged = YES
corrected S1 original rows field-equivalent = YES
```

The only changes in this commit are documentation, contract tests, the stale
producer label fix, the additive corrected S1 flow, and contract/freeze
metadata. The v1.3 manifest is:

```text
supplemental/reference_quotient_v1/v1_3_weight_multiplicity_contract_patch/contract_patch_manifest.json
```

The final freeze manifest now points human use to the corrected S1 flow while
retaining the historical artifact for provenance.

## No-computation declaration

```text
raw_scan_count = 0
scientific_experiments_rerun = 0
network_algorithms_rerun = 0
P0_rerun = 0
S1-S7_rerun = 0
commit_before_this_patch = 82e992aadd6c8e63ca699d766148d11f35ef7d0a
```
