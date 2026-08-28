# Chapter 5 RefQ P0-v3 Hardened S4 Scientific Interpretation v1

## Scope and authority

This document freezes the human scientific interpretation of the accepted
corrected supplemental S4 output. It is a descriptive read of the existing
artifacts; Louvain was not rerun, no consensus partition was constructed, no
seed was selected as a “best” seed, and no resolution sweep was performed.

Input artifacts (all already accepted and immutable for this review):

- `supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_runs.csv`
- `supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_pairwise.csv`
- `supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_summary.json`
- canonical comparison: `outputs/reference_quotient_p0_corrected_v3/rq2c_undirected_view_summary.json`

The SHA-256 values used for the read-only review are:

| artifact | SHA-256 |
|---|---|
| `louvain_stability_runs.csv` | `913266c48ba0dab8a08b0013c557c350c0f6493c0ee5e993141a8329e85b9d8c` |
| `louvain_stability_pairwise.csv` | `240852543183948b6107c9fd00a51de48f2dbb03f813083e30e0ca43d521cc69` |
| `louvain_stability_summary.json` | `37594b91e0c25cbfc5b31b0c9036f4e0bdddc324e724e5a2ca4398cf7e307421` |

## Descriptive recomputation

The values below were recomputed from the two frozen CSV tables. Quantiles use
the pandas/numpy linear interpolation convention (the default `quantile`
method); means are arithmetic means. The canonical row is identified by
`is_canonical_seed=True`.

### Run-level table

| quantity | value |
|---|---:|
| run count | 50 |
| seed range | 20260731..20260780 |
| canonical seed | 20260731 |
| canonical communities | 35 |
| canonical modularity | 0.7969220043681785 |
| canonical seed matches corrected P0-v3 | TRUE |
| community-count minimum | 32 |
| community-count maximum | 37 |

Exact community-count frequency:

| community_count | run_count | share |
|---:|---:|---:|
| 32 | 3 | 0.06 |
| 33 | 8 | 0.16 |
| 34 | 17 | 0.34 |
| 35 | 13 | 0.26 |
| 36 | 5 | 0.10 |
| 37 | 4 | 0.08 |

ARI to the canonical partition:

| statistic | value |
|---|---:|
| minimum | 0.6823671359861659 |
| Q1 | 0.8015113273472703 |
| median | 0.8428021239753398 |
| Q3 | 0.8829726199240396 |
| mean | 0.8349375327028501 |
| maximum | 1.0 |

The threshold counts were independently derived from the 50 frozen
`ari_to_canonical` values:

| condition | count | share |
|---|---:|---:|
| ARI < 0.9 | 42 | 0.84 |
| ARI >= 0.9 | 8 | 0.16 |

### Pairwise table

The pairwise table contains 1,225 rows, equal to the 50-run unordered pair
count, 50 × 49 / 2.

| statistic | pairwise ARI |
|---|---:|
| minimum | 0.6092441840471735 |
| Q1 | 0.7906438122735062 |
| median | 0.8552010290058881 |
| Q3 | 0.899869642409877 |
| mean | 0.844734724518271 |
| maximum | 0.9909005516367752 |

## Human scientific decision

`S4_SCIENTIFIC_REVIEW = ACCEPT_WITH_LIMITATION`

The canonical seed remains one deterministic reference realization and exactly
matches the accepted corrected P0-v3 canonical summary. Across the tested
seeds, the community count is broadly similar, while exact membership is
materially seed-sensitive (42/50 runs have ARI below 0.9 and the minimum
pairwise ARI is 0.6092441840471735).

Accordingly, S4 results are interpreted as an **algorithmic modular
neighborhood view** of the canonical undirected RefQ view. The canonical
35-community partition is retained as a deterministic reference realization,
not as a unique or true partition.

Allowed interpretation:

- Louvain yields an algorithmic modular partition of the canonical undirected
  RefQ view.
- Community count is broadly similar across runs but exact membership is
  seed-sensitive.
- The canonical 35-community partition is retained as a deterministic
  reference realization.
- Community membership is an algorithmic neighborhood view, and the stability
  experiment is evidence that exact membership should not be overinterpreted.

Disallowed interpretation:

- “stable 35 communities” or a unique stable community structure;
- a natural technical-domain taxonomy;
- community = DBMS subdomain;
- community membership as proof of knowledge diffusion, cohesion, integration,
  or organizational openness;
- a causal or organizational conclusion; or
- high modularity alone as proof of a unique true partition.

The S4 robustness alert is therefore a scientific limitation/interpretation
result, not a computational or reproducibility failure. Brokerage stability is
separate: S5's accepted results show substantially stronger ranking stability
under the tested settings, and S4 seed sensitivity must not be used to infer
unstable brokerage.

## S5 contrast (read-only)

The accepted S5 summary records:

- `canonical_setting_matches_p0 = TRUE`;
- minimum Spearman correlation `0.9998339514284217`;
- minimum top-50 overlap `0.82`; and
- `robustness_alert = FALSE`.

This contrast supports the bounded statement that brokerage ranking stability
is substantially stronger than exact Louvain membership stability under the
tested settings. It does not support a causal claim.

## Execution boundary

`S4_SCIENTIFIC_RUN = 0` for this review. No S1-S6 stage was rerun, no output or
receipt was rewritten, and no consensus clustering or resolution tuning was
introduced. Figures, manuscript edits, S7 scientific execution, G20, and final
release remain outside this decision.
