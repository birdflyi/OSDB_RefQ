# Chapter 5 RefQ Supplemental Evidence Final Freeze Report

## Freeze status

```text
REFQ_SUPPLEMENTAL_FINAL_FREEZE = PASS_READY_TO_PUSH
canonical_parent_commit = 920286e134ca459c8e155942eabc6798ceab8b65
freeze_commit_sha_recorded_in_manifest = NO
push = NO
```

This freeze records the already completed supplemental evidence package. It
does not perform a scientific computation or replace any canonical P0 or
supplemental result.

## Scope and corrections

The package includes the S1-S7 supplemental evidence, the S2 observational
semantics audit, the corrected S3 reproducibility outputs, the v1.1 material
completion outputs, and the final human-decision summary.

The human-decision summary was corrected so that `1,447,073` and `139,044`
are identified as `REFERENCE_RECORD (aggregated edge weight)`, while the
distinct edge counts are `289` self-loop edges and `9,605` cross-project
directed edges. S6 is classified as:

```text
S6_class = FIGURE_READY_DERIVATION
S6_role = MAIN_TEXT_FIGURE_SUPPORT
historical_original_decision_label = MAIN_TEXT_RESULT_RECOMMENDED
```

The historical label refers to the use of selected derived data for main-text
figures; S6 is not classified as a new scientific result.

## Authoritative output map

```text
S1 = supplemental/reference_quotient_v1/outputs/S1_evidence_universe/
S2 = supplemental/reference_quotient_v1/outputs/S2_weight_sensitivity/
S3 authoritative = supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/outputs/S3_observation_sensitivity_corrected/
S3 superseded = supplemental/reference_quotient_v1/outputs/S3_observation_sensitivity/
S4 = supplemental/reference_quotient_v1/outputs/S4_community_stability/
S5 = supplemental/reference_quotient_v1/outputs/S5_brokerage_stability/
S6 = supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/
S7 = supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/
```

The old S3 remains in the tree for provenance and is explicitly superseded by
the corrected S3 result. No historical/superseded file was deleted.

## Provenance chain

```text
supplemental_v1_implementation_commit = 18717e7d8d269538872ab5a3bcb923234e52eecc
supplemental_v1_result_commit = ba72987adb2c2339bdf1f7a3b370278c88c29c3c
v1_1_completion_implementation_commit = d222654e2edfac07265f6a86f65c26c3d089d8e1
v1_1_completion_result_commit = d88c2f872f8fb2ec71261b7f1bdaa5423afff0e7
s3_patch_implementation_commit = 9cb5dbdd4ecebc93acfb892cf0c757de5d34b43e
s3_patch_result_commit = 3720b76e863261afd520113bf5ce5bfda46df4ea
```

The final freeze commit is intentionally not embedded in the manifest or
this report. Git records it after validation.

## Hash and immutability audit

The existing canonical immutability audit records:

```text
canonical P0 SHA drift = 0
canonical P0 input files = 296
canonical P0 non-manifest outputs = 30
canonical output bytes changed = 0
authoritative supplemental scientific outputs unchanged = YES
old S3 unchanged and superseded = YES
corrected S3 authoritative = YES
```

The freeze manifest points to the canonical P0 manifest, supplemental output
manifest, v1.1 completion manifest, S3 patch manifest, and their SHA-256
values. These existing manifests are the hash inventory for the scientific
outputs; the freeze manifest itself does not contain a self-referential commit
hash.

## Execution boundary

```text
raw_scan_count = 0
scientific_experiments_rerun = 0
network_algorithms_rerun = 0
P0_rerun = 0
S1-S7_rerun = 0
```

Only documentation, manifest, schema, and hash validation were performed for
this freeze. No source code, configuration, runtime lock, canonical P0
output, or supplemental scientific output was modified.

## Files created or tracked by this freeze

```text
supplemental/reference_quotient_v1/FINAL_FREEZE_MANIFEST.json
docs/ch5_refq_supplemental_final_freeze_report.md
docs/ch5_refq_s2_weight_observational_semantics_audit.md
docs/ch5_refq_final_supplemental_human_decision_summary_v2.md
```
