# Chapter 5 RefQ Figure Render V4 — log-scale presentation review

## Scope and decision

This is a presentation-only V4 package.  It creates an isolated render root
at `figures/ch5_refq/p0v3_final_v4/` and changes only the Figure 2 Panel C
axis presentation.  No manuscript, scientific output, frozen input, V1/V2/V3
render root, S7 artifact, or scientific code was modified.

`HUMAN_VISUAL_QA = READY_FOR_FINAL_REVIEW`

The package is not called publication-ready; final human visual review remains
required.

## Baseline and immutable authorities

- Repository: `D:/github_repo/OSDB_RefQ`
- Branch: `ch5-refq-repository-identity-correction-v1`
- Repository HEAD before V4: `984b46c5f007c1c15cb4df51641d98ba05841532`
- V3 root: `figures/ch5_refq/p0v3_final_v3/` (unchanged)
- P0-v3 manifest SHA-256: `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
- Corrected supplemental v2 manifest SHA-256: `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`
- S6 figure-ready manifest SHA-256: `e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea`
- Figure-ready quantile CSV SHA-256: `1b2a1f58db6fa6f01394db6bd217e19ea3e39ad80bac62391c58870654e7b4ee`
- Reconciled manuscript SHA-256: `5C54BD725BECC7FF7253EC023E83258749B1868E14A70D34722ADCC1F421BC60`

The V3 render root and the scientific roots were checked with `git diff
--exit-code`; they remain byte-identical.  The existing untracked
`figures/ch5_refq/p0v3_final_v3.zip` was preserved.

## Why the Figure 2C linear scale was insufficient

The frozen target-role quantiles are strongly right-skewed.  In particular,
`in_strength` is 1, 2, 5, and 3,430 at Q1, median, Q3, and maximum.  On a
linear y-axis the first three order statistics collapse visually near zero,
so the discrete profile does not communicate their separation.  The same
issue is present, to a lesser degree, for the other target-role metrics.

## Frozen quantiles and display contract

The source is unchanged:
`supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq2b_target_role_quantiles.csv`.
The plotted x order is exactly `Q1, Median, Q3, Max` (the source rows are
`q25`, `median`, `q75`, `max`).

| metric | Q1 | median | Q3 | maximum |
|---|---:|---:|---:|---:|
| `in_degree` | 1 | 1 | 1 | 42 |
| `in_strength` | 1 | 2 | 5 | 3430 |
| `target_coverage` | 0.0034013605442176 | 0.0034013605442176 | 0.0034013605442176 | 0.1428571428571428 |

All twelve plotted values are finite and strictly positive.  Each of the three
inset y-axes uses `set_yscale("log", base=10)`.  The values passed to both the
connector line and the marker collection are the original frozen values;
there is no `log10`, `ln`, interpolation, smoothing, or fitting of the data.
Target coverage remains a fraction internally and is formatted as a
percentage on the tick labels.  Connector lines are a thin, alpha-0.55 guide;
markers are the primary visual elements.

The renderer records and asserts:

```text
F2C_INPUT_VALUES_STRICTLY_POSITIVE = YES
F2C_IN_DEGREE_YSCALE = log10
F2C_IN_STRENGTH_YSCALE = log10
F2C_TARGET_COVERAGE_YSCALE = log10
F2C_DATA_TRANSFORM = NONE
F2C_PLOTTED_VALUES_EQUAL_FROZEN_RAW_VALUES = PASS
F2C_X_ORDER = Q1,Median,Q3,Max
```

The Figure 2 A/B/D contracts are unchanged: A contains `out_degree` only, B
contains `out_strength` only, and D retains the frozen top-1/top-10/top-50
concentration display.

## V3 → V4 delta

| component | delta |
|---|---|
| Figure 2C | `CHANGED_AS_AUTHORIZED` — base-10 log y-axes and marker-primary guide lines |
| Figure 2A | `NO SEMANTIC CHANGE` |
| Figure 2B | `NO SEMANTIC CHANGE` |
| Figure 2D | `NO SEMANTIC CHANGE` |
| Figures 1, 3, and 4 | `NO SEMANTIC CHANGE` |
| Supplementary S1–S4 | `NO SEMANTIC CHANGE` |
| Supplementary S5 | `NOT RENDERED` |

The V4 SVG hash salt is `ch5-refq-p0v3-final-v4`; all eight figures were
rerendered from frozen inputs rather than copying V3 binaries.

## Determinism and asset closure

Independent Attempt A and Attempt B were rendered from the same V4 script and
environment.  All 24 publication assets are byte-identical (8 SVG, 8 PDF,
8 PNG).  Every publication PNG reports 300 DPI (`299.9994` DPI in the PNG
metadata, the normal libpng representation of 300 DPI).  The contact sheet is
not counted among the eight publication figures.

| figure | SVG SHA-256 | PDF SHA-256 | PNG SHA-256 |
|---|---|---|---|
| figure1_evidence_universe | `b9636375e057cfffd7d56cd42a0aa2ec53747798334fa92413d2e5dff81fd7b9` | `a6d291ad59cba122f51f3f80a65e275290c806f0a1161c9e5b20ee1e4ba019c1` | `28f151e3c94e791589f3deb17dcf247c1707726ca3c2c2f03a5ef69de1d47d94` |
| figure2_source_target_roles | `71f9cd900ccb91e755852598c6ae9a66c1b4401aa4e433cc0a72ad9c2872279b` | `4152523e5db599f68cd8eb34b39ee3e7ff34b0e3525f0776726e69743b3a91eb` | `d8f8f2094c2b9d78b21c48fb2180e305bdd492f96fa477ec8cfa69524174307b` |
| figure3_undirected_structure | `3e8e4b5f2738a54068c15fe38c59f826e457138ca958b14e068db2d7df3a6fb4` | `c314ba63daed153ecf07f7a78e62b42d31572f0705f785a50229daff4d085d9b` | `bf900762b20b56d9ab1ebf5d0be84052c08609d910377f2cd8e6d022ccd00cd9` |
| figure4_rq3_comparison | `5d36516cb8fbcfb5a5b21f309fbd25f3f128105cee50e8d74da0bbce11312420` | `cac857d9bd9822e35f4d5799a8da3a8943edd96b672824c76f517e6fc5c86291` | `f97c5b7a5b8674051fb97aae671c95bd23a63e5d5fad8907eae2d06d8222b37e` |
| supplementary_s1_multiplicity_sensitivity | `bcc9135936eaf1290f374ec1f7ec9df11b14f3aeb5c80a49e75d0ed16e69c5a9` | `345bc4172f163668969588827251d87a5acb4ac2fec679dc7d447d81a5c8f85b` | `4993ae98af84e06caa4ed2e9b1c4e5ed4ea5bbd9fd9c8458b05c715f39687fdd` |
| supplementary_s2_louvain_stability | `0eb31316459c6588bd95c6097f8b75d3bed2143f265a5f314db301515bc64448` | `d8e619e0bde8a8298203edc9da9e5cde0c026d57577ca0c800a2e154eff84755` | `745e02b109b0c43aad86ad9f9c90157b9207f017f9a942503658e0dc6910544a` |
| supplementary_s3_brokerage_stability | `5583e7156058d0d8179bcdf9ade83b0c6bedf3b5470ea0e469114fa0d12d1ce2` | `65657b355ee54aa946df4b93407e0792ac84a967c0155ab7e29ff79568aba393` | `cdcc945e80d06d0fc20f4d4558825589640ba71e9ccd11063c3241d23323a7a7` |
| supplementary_s4_unit_contract | `74ae6f91dc3c07c77811caf64b46552414d1dbff5db49e52fee5df57906f4f2a` | `558a9b6ba6878605fe0de70c31eac314830f863c7c86a22caaa7ef2b91af4ffb` | `922f8eb7f82afc6473673d4107da62d64b9a6f3c8f527854874b5e286b4fbec8` |

The table above is copied from `render_manifest_v4.json` and verified against
the files in the official V4 root.  The contact sheet hash is
`3075c15b9b917fc8f82fe17fd557a3cfc2aa8f6710f1ee8092230a8e7c09bbfb` with
dimensions 2001 × 2815 px.  The renderer script hash is
`e3c042ebafc589a64a136fe862350c263e6be67a0715bc02ecb352bade321286`.

## Scientific and repository immutability

```text
P0_RUN = 0
S1_RUN = 0
S2_RUN = 0
S3_RUN = 0
S4_RUN = 0
S5_RUN = 0
S6_RUN = 0
S7_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
scientific_logic_change_count = 0
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
SCIENTIFIC_RECOMPUTATION = 0
```

The V3 root, manuscript, P0-v3 outputs, corrected supplemental v2 outputs,
S7, historical figures, and scientific code all remain unchanged.  Only the
new V4 render root and this V4 review record are in scope for the presentation
closure.

## Final assessment

The V4 package satisfies the presentation-only Figure 2C log-axis contract,
preserves every frozen raw quantile, and passes independent byte-level
determinism checks.  No current scientific or manuscript defect was introduced.
Final human visual inspection is still required.

`decision = P0V3_FIGURE_RENDER_V4_PASS_READY_FOR_FINAL_HUMAN_REVIEW`
