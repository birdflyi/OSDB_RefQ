# Chapter 5 RefQ P0 v3 Clean Supplemental Runtime Lock

Status: accepted for clean supplemental S1-S6 execution.

Frozen implementation commit: `e13eaf2b3bff040639e6256ea98aa1fa5bb0ef1f`.

## Runtime identity

- Environment: `D:/codex_envs/ch5_refq_supplemental_p0v3_runtime`
- Python executable: `D:/codex_envs/ch5_refq_supplemental_p0v3_runtime/Scripts/python.exe`
- Python: 3.9.13 (MSC v.1916 64 bit, AMD64)
- Platform: Windows-10-10.0.26200-SP0
- pandas: 1.5.3
- NumPy: 1.26.4
- SciPy: 1.13.1
- NetworkX: 3.1
- GH-CoRE: 2.3.1
- pytest: 7.1.2

The environment was created outside the repository from the accepted P0
Python 3.9.13 interpreter. The primary creation command was:

```text
D:/codex_envs/ch5_refq_p0_v2_runtime/Scripts/python.exe -m venv D:/codex_envs/ch5_refq_supplemental_p0v3_runtime
```

Scientific packages were installed at the versions above. GH-CoRE 2.3.1 was
installed with `--no-deps` because its distribution metadata declares
`pandas~=1.4.4`; all its accepted P0-runtime dependencies were then installed
at the accepted versions. This is a known metadata incompatibility, not a code
or scientific patch.

## Regression closure

- Supplemental suite in selected runtime: 199 collected, 199 passed, 0 failed.
- Shared Chapter 5 suite in selected runtime: 55 collected, 54 passed,
  1 deselected (`test_p0_runtime_lock_matches_current_environment`).
- Shared Chapter 5 suite in the accepted P0 runtime: 55 collected, 55 passed,
  0 failed.
- `compileall` for `script/ch5_reference_quotient` and
  `supplemental/reference_quotient_v2`: PASS.
- `git diff --check`: PASS.

The single selected-runtime deselection asserts the P0 execution environment's
pandas 1.4.4 lock and is therefore intentionally evaluated in the accepted P0
runtime. All shared scientific/configuration tests pass in the selected runtime.

## Dynamic P0 v3 parity gates

- S2 threshold-1 parity: PASS; 9,547 undirected edges.
- S3 canonical observation parity: PASS.
- S4 canonical partition/modularity parity: PASS; canonical communities 35;
  canonical modularity 0.7969220043681785.
- S5 canonical k=500/seed=20260731 brokerage parity: PASS.

The runtime-gate production-parameter probe found `S4 robustness_alert=true`
(minimum ARI to canonical 0.6823671359861659). This does not invalidate the
runtime or canonical parity, but the authorized clean execution must stop for
human review after a durable S4 stage if the same alert is reproduced.

## BLAS/LAPACK metadata

- NumPy BLAS: OpenBLAS64 0.3.23.dev, 64-bit integer build, dynamic architecture.
- NumPy LAPACK: internal NumPy 1.26.4 wheel authority.
- SciPy BLAS/LAPACK: OpenBLAS 0.3.27, dynamic architecture, Windows x86_64.

## Known limitations

- pandas 1.5.3 emits NumPy 1.25+ deprecation warnings; no test or parity failure
  results from these warnings.
- The selected runtime is supplemental-only. P0 regeneration remains locked to
  the separate pandas 1.4.4 P0 runtime.
- No global/base environment was modified.
