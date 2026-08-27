# Chapter 5 RefQ C4-S1 Failed-Run PD.NA Identity Diagnosis v1

## Preserved Failure Scene

The first real C4-S1 run used frozen implementation commit
`85083edd9d30280fcd030a5316cdff52846c577c` and produced a durable PASS receipt
and eight CSV outputs under `supplemental/reference_quotient_v2/outputs/S1_evidence_universe/`.
The scene was preserved unchanged until this audit. Its complete SHA/byte/row
inventory is frozen in `ch5_refq_c4_s1_failed_run_hash_inventory_v1.csv`.

## Numeric Diagnosis

```text
reference_records_before_source_admission = 3,748,078
admitted_source_observation = 3,747,958
target_project_mappable_records = 1,586,047
target_non_project_records = 1,686,729
target_unresolved_records = 475,182
target_ambiguous_records = 0
conflict_excluded_record_occurrences = 273,283
quotient_eligible_records = 1,312,764
self_loop_evidence_weight = 1,205,913
cross_project_evidence_weight = 106,851
self_loop_edge_count = 284
cross_project_directed_edge_count = 7,474
```

The expected corrected authority is eligible `1,586,047`, self weight
`1,447,073`, and cross weight `138,974`. Therefore:

```text
eligible_delta = 273,283
self_delta = 241,160
cross_delta = 32,123
self_delta + cross_delta = eligible_delta
conflict_excluded_record_occurrences = eligible_delta
```

The arithmetic and conflict-exclusion closure are exact.

## H1-H5 Confirmation

Historical v1 normalizes missing raw entity values using `pd.isna(value)` to
`None` before canonical membership identity. Corrected v2 reads production
partitions with `dtype="string"`, so empty entity cells become `pd.NA`. The
shared `normalized_entity_identity()` handles `None`, empty text, and `"nan"`,
but not `pd.NA`/`"<NA>"`; consequently `canonical_project_entity_identity(pd.NA,
"R_101")` returns `"<NA>"` instead of `"R_101"`.

The direct micro-reproduction was:

```text
normalized_entity_identity(pd.NA) = '<NA>'
canonical_project_entity_identity(pd.NA, 'R_101') = '<NA>'
canonical_project_entity_identity(None, 'R_101') = 'R_101'
```

## Full-Data Conflict Audit

The read-only scan covered all 294 admitted partitions and 3,747,958 admitted
records. It found 273,283 admitted records with a missing target raw entity
identity, split into self-project pairs `241,160` and cross-project pairs
`32,123`. Under current v2 representation, the only conflict identity was
`"<NA>"`; there were no additional conflict identities. All 273,283 records
were attributable to that identity.

```text
membership_conflict_entity_count = 1
conflicting_identities = ["<NA>"]
false_conflict_record_occurrences = 273,283
false_conflict_self_occurrences = 241,160
false_conflict_cross_occurrences = 32,123
additional_real_conflict_entities = NONE
```

## Root Cause and Compatibility Scope

`C4_S1_ROOT_CAUSE = PANDAS_NULL_IDENTITY_REPRESENTATION_COMPATIBILITY`.
Classification: `INTEGRATION_COMPATIBILITY_DEFECT`. The fix is supplemental-S1
only: pandas-missing scalar values are converted to `None` before calling the
unchanged shared canonical helper. The same helper is used by both streaming
membership-registry construction and evidence classification.

No shared membership code, Fireproof identity semantics, corrected aggregate,
corrected P0, eligibility definition, or S2-S6 semantics changed. The existing
non-missing real-conflict fixture remains enforced by tests.

## Test Coverage and Recovery

The former 175-test suite did not exercise production `authorize_stage()` or
`run_stage()` and therefore missed the phase-map defect. F.1 added that coverage.
The compatibility tests cover actual empty CSV cells under StringDtype,
`None`/NaN/`pd.NA` parity for source and target, and false-global-conflict
prevention.

The invalid S1 scene was audited before deletion. It is explicitly removed only
after this document and hash inventory matched the preserved files. The rerun
uses a new implementation commit and is a second S1 scientific execution; the
first invalid run remains disclosed.

## Immutability

The failed run had historical before/after
`HISTORICAL_IMMUTABILITY_MATCH`. No historical root, tag, manuscript, figure,
source data, corrected P0, or shared P0 code was modified.
