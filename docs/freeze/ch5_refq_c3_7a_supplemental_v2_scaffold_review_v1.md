# Chapter 5 RefQ C3.7-A
# Corrected Supplemental v2 Scaffold Review v1

审查日期：2026-08-26
Repository：`D:\github_repo\OSDB_RefQ`
Branch：`ch5-refq-repository-identity-correction-v1`

## 1. Scope and authorization

This review records the first implementation phase after C3.6-C. The phase was
limited to a corrected supplemental v2 scaffold, configuration provenance
checks, fail-closed path guards, manifest helpers, and non-scientific tests.

The following were not run or changed:

- P0;
- S1-S7;
- GH-CoRE or network algorithms;
- aggregate partition scans or scientific counters;
- figures or figure-ready data;
- manuscript files;
- historical P0, corrected P0, or supplemental v1 outputs.

`corrected_aggregate_is_S1_authority = YES`, `event_rejoin_required = NO`, and
`scientific_logic_change_count = 0` remain the frozen design facts. The v2
package is only a scaffold; no corrected supplemental result is produced.

## 2. Baseline and implementation scope

```text
base_commit = 3cd4c5397f33eb9a84c27da77e00fb286f509fcf
implementation_commit_candidate = RECORDED_IN_FINAL_STATUS
```

Created paths:

| path | classification | purpose |
|---|---|---|
| `supplemental/reference_quotient_v2/__init__.py` | scaffold | package marker |
| `supplemental/reference_quotient_v2/configs/supplemental_v2_corrected.yaml` | config | explicit corrected and comparison-only authorities |
| `supplemental/reference_quotient_v2/scripts/__init__.py` | scaffold | script package marker |
| `supplemental/reference_quotient_v2/scripts/paths.py` | implementation | normalized path, authority, and write-target guards |
| `supplemental/reference_quotient_v2/scripts/schema.py` | implementation | frozen status vocabulary and required-field definitions only |
| `supplemental/reference_quotient_v2/scripts/manifest.py` | implementation | read-only SHA/status/path provenance helpers |
| `supplemental/reference_quotient_v2/scripts/run_supplemental_v2.py` | implementation | non-executable plan, validation, and blocked-stage shell |
| `supplemental/reference_quotient_v2/tests/test_scaffold_and_paths.py` | test | scaffold and guard tests only |
| `docs/freeze/ch5_refq_c3_7a_supplemental_v2_scaffold_review_v1.md` | documentation | this review |

No v2 `outputs/` directory was created. No S1-S6 implementation modules were
created. In particular, no `s1_adapter.py`, `s1_evidence_universe.py`,
`s2_*.py` through `s6_*.py`, or S7 output path was added.

## 3. Configuration authority map

| config key | resolved authority | role |
|---|---|---|
| `corrected_p0_root` | `outputs/reference_quotient_p0_corrected_v2/` | executable corrected input |
| `corrected_p0_manifest` | corrected P0 `manifest.json` | executable corrected provenance |
| `corrected_p0_config` | `configs/ch5_reference_quotient_p0_v2.yaml` | executable corrected configuration |
| `corrected_aggregate_root` | `D:/github_repo/OSDB_RefQ_source_data/data/github_osdb_data/repos_GH_CoRE_ref_node_agg_v2_identity_corrected/` | executable corrected input |
| `corrected_output_root` | `supplemental/reference_quotient_v2/outputs/` | future write target only |
| `historical_p0_root.path` | `outputs/reference_quotient_p0_frozen/` | comparison-only historical input |
| `historical_supplemental_root.path` | `supplemental/reference_quotient_v1/` | comparison-only historical input |
| `historical_tag` | `chapter5-refq-freeze-v1.0` | immutable historical reference |

The corrected P0 manifest status was validated as `PASS`. Its legacy schema
label was accepted under the frozen C3 design. Its stale `entry_point` was
read only as metadata and was never used as an executable authority.

The corrected P0 config SHA validated to:

```text
e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658
```

The configuration preserves `random_seed = 20260731`, strict repository
identity, the no-event-rejoin boundary, the v2 S5 inclusion-frequency
authority, and the v2 S6 CSV structural-summary authority.

## 4. Path guard behavior

`paths.py` normalizes relative paths, Windows traversal, absolute paths, and
realpath aliases before authority comparisons. It enforces:

1. corrected P0 root resolves exactly to the approved corrected P0 root;
2. corrected P0 manifest is inside that root;
3. corrected P0 config resolves exactly to the approved v2 P0 config;
4. corrected aggregate root exists and matches the v2 aggregate configured by
   the corrected P0 config;
5. corrected output paths remain under `supplemental/reference_quotient_v2/outputs/`;
6. historical P0 and historical supplemental paths are comparison-only;
7. corrected P0, historical P0, historical supplemental, source-data roots, and
   discoverable manuscript roots cannot be write targets;
8. the historical aggregate root cannot be substituted for corrected aggregate
   authority.

`validate_write_target()` is intentionally stricter than ordinary read
resolution. It permits only a future v2 output descendant and rejects protected
roots after normalization. Validation does not create the output directory.

## 5. Scaffold behavior

The orchestrator exposes only:

```text
--validate-config
--preflight-scaffold
--show-plan
```

Any `--run-s1` through `--run-s7` request exits with
`NOT_AUTHORIZED_IN_C3_7A` before opening a write target or importing scientific
modules. The displayed structural plan is:

```text
S1 -> S2 -> S3 -> S4/S5 -> S6
S7 outside DAG; future read-only overlap gate
```

`schema.py` defines exactly the four frozen source-admission statuses and the
five required corrected aggregate provenance field names. It does not process
rows, calculate counters, or iterate through the 294 aggregate partitions.

`manifest.py` provides SHA-256, manifest status/path/config closure, and future
manifest enum definitions. It does not persist a scientific manifest.

## 6. Tests

Command executed:

```text
venv\Scripts\python.exe -m pytest supplemental\reference_quotient_v2\tests\test_scaffold_and_paths.py -q
```

```text
tests_collected = 20
tests_passed = 20
tests_failed = 0
```

The tests cover configuration loading, corrected and historical authority
resolution, corrected-only write roots, protected-root rejection, historical
aggregate rejection, stale entry-point isolation, PASS status and config SHA
validation, exact status vocabulary, blocked S1/S7 requests, no output-root
creation, Windows traversal protection, required field definitions, and
non-executable plan display.

The read-only command also returned:

```text
status = SCAFFOLD_VALID
corrected_p0_manifest_status = PASS
entry_point_used_as_authority = false
```

No networkx, numpy, pandas, scipy, GH-CoRE, or stage module was imported by the
new scaffold.

## 7. Immutability and contamination postcheck

The following read-only reference values were recorded or rechecked:

| protected item | postcheck evidence |
|---|---|
| historical P0 manifest | SHA-256 `a3089fd8a6a58c0a15d2192a7b5f3388868ef0f1358c803be3aa4f27314c59f6` |
| corrected P0 manifest | SHA-256 `21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7` |
| corrected P0 v2 config | SHA-256 `e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658` |
| historical supplemental v1 | Git tree `74ddfa6feb36239d34d5f6ffc1d2041f4cda772c` at base |
| shared P0 implementation | Git tree `c0d97752939a82ad6c63023831c31f82004186c0` at base |
| identity provenance implementation | Git blob `ea7c7aeaf3e9a5871d401e4b776a74ecf0953514` at base |
| historical tag | `chapter5-refq-freeze-v1.0` -> `68d001551359d120bf2a06cc5e571742df7e7822` |
| source-data repository | manifest-recorded commit `2944ab7ee828c1af427115d0808d4d62e5ac725e`; no source-data hash scan performed |

At postcheck, the only dirty path was the new
`supplemental/reference_quotient_v2/` package. The forbidden scientific modules
and `supplemental/reference_quotient_v2/outputs/` were absent. No v1 file,
shared P0 code, source-data file, manuscript, figure, or historical artifact
was modified.

## 8. Scientific execution counters

```text
P0_RUN = 0
S1_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
SUPPLEMENTAL_V2_OUTPUTS_CREATED = 0
```

The authoritative C3 gate CSV remains unchanged and all G01-G20 statuses
remain `DESIGN_ONLY_NOT_EXECUTED`. Scaffold test PASS is not a runtime gate
PASS:

```text
DESIGN TEST PASS != G01-G20 RUNTIME PASS
```

## 9. Limitations and next boundary

This phase does not prove the later S1 admission behavior, scientific counts,
weight semantics, graph construction, S4/S5 algorithms, S6 source closure, or
S7 zero-overlap runtime result. Those remain future implementation and runtime
acceptance work.

The exact next authorized boundary is:

```text
C3.7-B = NOT_AUTHORIZED
C3.7-A scaffold = READY_FOR_HUMAN_REVIEW
```

The current human checkpoint authorizes only the C3.7-A scaffold. A separately
reviewed authorization is required before implementing the S1 adapter or any
later phase. Scientific regeneration, P0 rerun, S1-S7 execution, C4, figure
rendering, manuscript modification, merge to main, and new final tags remain
forbidden.

## 10. Final status

```text
COMMAND_EXECUTION_AVAILABLE = YES
base_commit = 3cd4c5397f33eb9a84c27da77e00fb286f509fcf
implementation_commit = RECORDED_IN_FINAL_STATUS
push_status = RECORDED_IN_FINAL_STATUS

v2_package_created = YES
v2_config_created = YES
path_guards_created = YES
orchestrator_scaffold_created = YES
manifest_scaffold_created = YES

S1_adapter_implemented = NO
S1_scientific_logic_implemented = NO
S2_S6_scientific_logic_implemented = NO

corrected_aggregate_is_S1_authority = YES
event_rejoin_required = NO
historical_v1_executable_authority = NO
historical_v1_write_target = NO
supplemental_v2_outputs_root_created = NO

tests_collected = 20
tests_passed = 20
tests_failed = 0
G01_G20_runtime_status = DESIGN_ONLY_NOT_EXECUTED

P0_RUN = 0
S1_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
MAIN_MERGED = NO
FINAL_TAG_CREATED = NO

C3_7B_authorized = NO
C4_authorized = NO
decision = C3_7A_SCAFFOLD_PASS_READY_FOR_HUMAN_REVIEW
```
