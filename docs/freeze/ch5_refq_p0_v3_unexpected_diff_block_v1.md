# Chapter 5 RefQ P0 v3 Unexpected-Difference Block v1

## Decision

`P0_V3_BLOCKED_UNEXPECTED_SCIENTIFIC_DIFF`

The single authorized P0 v3 regeneration completed and its output root is
preserved at `outputs/reference_quotient_p0_corrected_v3/`. No supplemental
stage was executed. No result commit was created.

## Differential evidence

The accepted v2 and v3 manifests contain the same 296 input records with the
same paths, byte counts, and SHA-256 values. All graph, edge, node-registry,
partition, brokerage, role, profile, and feature artifacts are byte-identical
except `rq2c_algorithmic_communities.csv`, where the only changed column is
the corrected `community_size` metadata (6,367 rows).

Three statistical CSVs also differ in floating-point values:

| Artifact | Changed fields | Magnitude | Interpretation |
|---|---|---:|---|
| `rq1_descriptive_statistics.csv` | `std` (7 rows) | max 5.0931703299284e-11, about 7 ULP | runtime-dependent numeric drift |
| `rq1_project_age_cross_sectional_association.csv` | `p_value` (1 row) | 8.67361737988404e-19, 1 ULP | runtime-dependent numeric drift |
| `rq3_kruskal_fdr_effect_sizes.csv` | `p_value`, `fdr_bh_p_value` | max 2.220446049250313e-16, 2 ULP | runtime-dependent numeric drift |

The v2 runtime was pandas 1.4.4 / NumPy 1.26.4 / SciPy 1.13.1 / NetworkX
3.1 / GH-CoRE 2.3.1; the v3 runtime was pandas 1.5.3 / NumPy 1.24.2 / SciPy
1.9.1 / NetworkX 3.2.1 / GH-CoRE 2.3.0.0. Counts, test statistics,
categories, status flags, and rejection decisions remain unchanged, but the
task's strict gate permits no non-community statistical differences.

## Preserved state

- Implementation/config/audit commit: `25c6ef3f49af04e916f10e129d976ce7c2119fd8`
- P0 v3 run count: 1
- v3 manifest output files: 31; manifest SHA-256:
  `7c1f6da8ccc1df67ac6a5cdf94e477ceab034b0d82dfa278a3c4e4fca90462d2`
- v3 community closure: 6,367 rows, 35 communities, 0 mismatched rows
- v2 and historical roots: untouched
- Supplemental S1-S7: not executed

To reach a clean-pass decision, rerun under the frozen v2 runtime lock (or
explicitly revise the differential policy to accept documented ULP-bounded
runtime drift), then perform a new human-authorized review. Do not retry this
P0 run in place.
