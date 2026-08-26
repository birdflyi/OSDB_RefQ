# Chapter 5 RefQ C3.7-E.1 package receipt / release closure review

## 1. Decision

```text
C3_7E1_PACKAGE_PROVENANCE_PASS_READY_FOR_C3_7F_REVIEW
```

This is a provenance/governance implementation result. It does not mean that a corrected supplemental scientific package was executed or released. No corrected-data S1-S6, S7 overlap, P0, GH-CoRE, event rejoin, network run, figure generation, or manuscript update occurred.

## 2. Baseline and confirmed prior gap

Required base commit and branch were confirmed before editing:

```text
base_commit = 0305324cda386dee8b8640c7ae942251a5bb86dd
branch = ch5-refq-repository-identity-correction-v1
```

The existing package builder accepted six receipts with `status = PASS` even when every receipt had `input_artifacts = []` and `output_artifacts = []`. Therefore:

```text
prior_G20_empty_receipt_gap = CONFIRMED
G20_RECEIPT_CLOSURE_DEFECT = CONFIRMED
classification = PROVENANCE_CONTRACT_DEFECT
scientific_logic_change_count = 0
```

The defect is now closed: a completed receipt must have a valid stage, all required receipt fields, non-empty input/output records, corrected input authority, and output hash closure against an existing stage tree.

## 3. Files changed

Allowed implementation/test surface only:

- `supplemental/reference_quotient_v2/scripts/stage_io.py`
- `supplemental/reference_quotient_v2/scripts/manifest.py`
- `supplemental/reference_quotient_v2/scripts/s6_figure_ready.py`
- `supplemental/reference_quotient_v2/tests/test_stage_io.py`
- `supplemental/reference_quotient_v2/tests/test_manifest_v2.py`
- `supplemental/reference_quotient_v2/tests/test_s6_figure_ready.py`
- this review document

No changes were made to frozen P0, corrected P0, historical supplemental, shared network/P0 code, source data, configuration authority, manuscript, main, or historical tag.

## 4. Strict receipt contract

The authoritative validator is `validate_stage_receipt()` in `stage_io.py`. Each completed S1-S6 receipt requires:

```text
stage
status
implementation_commit
input_artifacts
output_artifacts
parameters
runtime_versions
completed_at
```

The receipt stage is canonicalized and must equal the package manifest stage key. `PASS` alone is insufficient. A completed receipt must contain non-empty input and output lists. Every input record requires `path`, `sha256`, and `authority_class`; optional `root` and `version` are accepted only as a pair. Every output record requires `path`, `sha256`, `bytes`, and `row_count`.

Allowed input authority classes are stage-specific and include only:

```text
CORRECTED_AGGREGATE
CORRECTED_P0
CORRECTED_SUPPLEMENTAL_V2
```

Historical P0/v1/v1.1/v1.2 paths are rejected, as are malformed records, stage/path mismatches, invalid SHA values, and cross-root records.

## 5. Input/output hash closure

`validate_input_artifact_records()` resolves each recorded input path, requires the file to exist, rejects historical path fragments, checks declared root containment when present, and compares the recorded SHA-256 with the actual file.

`validate_output_artifact_records()` requires output files under the validated stage directory and checks file existence, SHA-256, byte count, and CSV row count. `stage_receipt.json` is explicitly excluded from the scientific output artifact list.

`validate_package_manifest()` invokes `validate_stage_receipt()` for every completed S1-S6 receipt. It therefore does not trust receipt mappings, and tampering with an output SHA, byte count, row count, input SHA, durable marker, or stage path fails closed.

## 6. Durable stage-completion marker

`write_stage_outputs()` now follows this order:

1. validate the explicit output root and receipt shape;
2. serialize scientific outputs;
3. create the new stage directory, refusing any existing stage directory;
4. write scientific output files;
5. validate output SHA/bytes/rows and input SHA closure;
6. write `stage_receipt.json` last;
7. validate that the durable marker matches the validated receipt.

The marker is not included in `output_artifacts`, and does not contain a self-hash. If execution stops before marker creation, the stage directory is partial and `validate_stage_receipt()` rejects it. There is no automatic cleanup or retry; an existing partial stage continues to block overwrite.

## 7. G19 package completion and release truth table

`validate_historical_write_audit()` requires:

```text
status = PASS
historical_roots_modified = False
no_overwrite = True
```

Missing, `NOT_EXECUTED`, `FAIL`, or malformed audit data cannot complete a package. Package completion now requires all six valid completed receipts, valid stage input/output closures, a valid S6 manifest closure, and G19 PASS.

| condition | package status | release status |
|---|---|---|
| fake/invalid/missing S1-S6 receipt | `STAGE_PACKAGE_INCOMPLETE` | `NOT_RELEASE_READY` |
| valid S1-S6 + G19 missing/NOT_EXECUTED/FAIL | `STAGE_PACKAGE_INCOMPLETE` | `NOT_RELEASE_READY` |
| valid S1-S6 + G19 PASS + S7 `NOT_EVALUATED` | `STAGE_PACKAGE_COMPLETE` | `NOT_RELEASE_READY` |
| valid S1-S6 + G19 PASS + S7 `REGENERATE_REQUIRED` | `STAGE_PACKAGE_COMPLETE` | `NOT_RELEASE_READY` |
| valid S1-S6 + G19 PASS + S7 `KEPT_FIXED_OBJECT` | `STAGE_PACKAGE_COMPLETE` | `RELEASE_READY` |

The package builder constructs only an in-memory manifest. It does not create the real v2 output root.

## 8. S6 manifest authority

`s6_figure_ready_manifest_authority` now records an object:

```text
path
sha256
```

Final package validation checks the recorded SHA, requires the `figure_ready_manifest_v2` schema, and invokes `validate_s6_manifest_sha_closure()`. The S6 manifest still does not embed its own SHA, so no circular self-hash is introduced. A missing or tampered S6 manifest prevents package completion.

## 9. Production output-root policy

The default `write_stage_outputs()` policy now accepts only the exact configured production root:

```text
supplemental/reference_quotient_v2/outputs/
```

An external temporary root is accepted only when the caller explicitly passes `allow_external_test_root=True`, and it must be outside the repository. Historical P0, corrected P0, historical supplemental, source-data, and undeclared repository roots remain blocked. The parent production output root may exist; only the target stage directory must be absent.

All E.1 tests use temporary roots with explicit opt-in. The real production root remained absent.

## 10. Tests and execution counters

Verification:

```text
python -m pytest supplemental/reference_quotient_v2/tests -q
126 passed, 0 failed

scripts/*.py and tests/test_*.py py_compile
PASS

git diff --check
PASS
```

Coverage includes empty/malformed receipts, stage mismatch, missing fields, input/output SHA closure, historical authority rejection, bytes/row-count closure, durable marker ordering and tamper rejection, partial-stage no-retry, G19 status truth, S6 manifest path/SHA closure, production-root rejection, explicit test-root opt-in, and S7 release distinctions.

```text
real_v2_output_root_created = NO
corrected_data_S1_S6_run = NO
S7_overlap_run = NO
P0_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
NETWORK_CORRECTED_DATA_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
G01_G20_authoritative_runtime_status = DESIGN_ONLY_NOT_EXECUTED
scientific_logic_change_count = 0
```

## 11. Limitations and next boundary

The tests use synthetic/temp-directory artifacts. No real corrected S1-S6 stage receipt, real S6 output tree, or real G19 before/after scientific SHA inventory was created or audited in this phase. Accordingly, the implementation prechecks are PASS, while authoritative G01-G20 runtime status remains `DESIGN_ONLY_NOT_EXECUTED`.

The next authorization boundary is C3.7-F. This patch does not authorize corrected-data S1-S6, S7, figures, manuscript updates, P0, GH-CoRE, or event rejoin.

## 12. Final status

```text
base_commit = 0305324cda386dee8b8640c7ae942251a5bb86dd
implementation_commit = THIS_COMMIT (resolve with git log; self-hash is not embedded)
push_status = PASS
prior_G20_empty_receipt_gap = CONFIRMED
strict_stage_receipt_validation = PASS
stage_receipt_durable_completion_marker = YES
empty_input_receipt_rejected = YES
empty_output_receipt_rejected = YES
stage_output_hash_closure = PASS
stage_input_hash_closure = PASS
historical_write_audit_required_for_package_completion = YES
G19_NOT_EXECUTED_can_complete_package = NO
S6_manifest_path_and_sha_authority = PASS
arbitrary_external_output_root_allowed_by_default = NO
explicit_test_root_opt_in = YES
tests_collected = 126
tests_passed = 126
tests_failed = 0
real_v2_output_root_created = NO
corrected_data_S1_S6_run = NO
S7_overlap_run = NO
G01_G20_authoritative_runtime_status = DESIGN_ONLY_NOT_EXECUTED
scientific_logic_change_count = 0
C3_7F_authorized = NO
recommended_next_phase = C3_7F
decision = C3_7E1_PACKAGE_PROVENANCE_PASS_READY_FOR_C3_7F_REVIEW
```
