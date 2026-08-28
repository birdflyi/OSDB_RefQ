# Chapter 5 RefQ P0 v3 Runtime Lock v1

## Accepted runtime authority

Attempt 2 used an isolated environment outside the repository:
`D:/codex_envs/ch5_refq_p0_v2_runtime`. The exact scientific package versions
match the accepted P0 v2 manifest and runtime lock:

- Python 3.9.13 (MSC v.1916, 64-bit)
- pandas 1.4.4
- NumPy 1.26.4
- SciPy 1.13.1
- NetworkX 3.1
- GH-CoRE 2.3.1
- pytest 7.1.2

The observed platform was Windows `10.0.26200`, x86-64. NumPy reported
OpenBLAS64 0.3.23.dev; SciPy reported OpenBLAS 0.3.27. The historical v2
manifest did not record OS or BLAS build metadata, so historical OS/BLAS parity
is `NOT_HISTORICALLY_RECORDED`; only package-version parity can be asserted.

## Attempts

Attempt 1 used pandas 1.5.3, NumPy 1.24.2, SciPy 1.9.1, NetworkX 3.2.1,
GH-CoRE 2.3.0.0, and Python 3.9.13. It was rejected because three statistical
artifacts differed from v2 at 1–7 ULP despite unchanged scientific decisions.
Its 31-file, 3,029,426-byte inventory is frozen in
`ch5_refq_p0_v3_attempt1_runtime_mismatch_hash_inventory_v1.csv`. Recursive
deletion was blocked by the execution safety layer, so the intact 31-file root
was moved to the recoverable external archive
`D:/codex_recovery_archive/OSDB_RefQ_reference_quotient_p0_corrected_v3_attempt1_b9c6d66`.

Attempt 2 command:

```text
D:/codex_envs/ch5_refq_p0_v2_runtime/Scripts/python.exe -m script.ch5_reference_quotient.cli --config configs/ch5_reference_quotient_p0_v3.yaml --workspace-root . --execute
```

It ran from `2026-08-28 10:53:03` to `11:00:55` local time (approximately
7 minutes 52 seconds). The manifest records implementation repository HEAD
`44e6c39783c16832cfab15b13ed0b76042ac522b`; the scientific implementation
remains the unchanged implementation commit
`25c6ef3f49af04e916f10e129d976ce7c2119fd8`, with only later docs commits.

## Pre-run verification

- corrected P0 v2 manifest/config closure: PASS
- corrected aggregate: 294/294 PASS
- RefQ/P0 tests under locked runtime: 55 passed, 0 failed
- directly affected compatible supplemental S2–S5 scientific tests: 33 passed,
  0 failed, 3 deselected
- compileall and `git diff --check`: PASS

The complete supplemental test suite is not compatible with pandas 1.4.4:
post-P0 supplemental serialization code uses the newer `lineterminator`
argument. That incompatible surface produced 38 failures and is not part of
the P0 scientific execution. No source patch or policy relaxation was made.

## Strict differential result

Twenty-nine non-community scientific artifacts are byte-identical to v2.
`rq2c_algorithmic_communities.csv` differs only in `community_size` for 6,367
rows; `project_id` and `community_id` are identical. All three former runtime
blockers are now byte-identical. No ULP, rounding, `isclose`, or formatting
exception was used.

Remaining reproducibility limitation: historical OS/BLAS metadata is absent,
and the full later supplemental implementation requires its own explicitly
frozen compatible runtime before future S1–S6 execution.
