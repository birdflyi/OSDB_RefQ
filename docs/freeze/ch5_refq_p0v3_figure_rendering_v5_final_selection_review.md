# Chapter 5 RefQ Figure Rendering V5 — final presentation selection review

## 1. Purpose and scope

V5 is a presentation-only final-selection package.  It creates the isolated
render root `figures/ch5_refq/p0v3_final_v5/` and selects the final Figure 2C
presentation: linear y-axes with raw-value labels on every quantile marker.
The frozen scientific inputs, computed results, manuscript, tables, V1/V2/V3/V4
roots, S7 artifacts, and scientific code are not modified.

## 2. Frozen starting state

- Repository: `D:/github_repo/OSDB_RefQ`
- Branch: `ch5-refq-repository-identity-correction-v1`
- `repository_HEAD_before = 6087b3b45de5d1a0496238a6c18bdd51ee4002cf`
- Local and remote starting HEAD were identical.
- Existing untracked `figures/ch5_refq/p0v3_final_v3.zip` and
  `figures/ch5_refq/p0v3_final_v4.zip` were preserved untouched.
- V4 root and V4 review remain immutable provenance.

Frozen authority hashes used by the V5 renderer:

```text
P0_manifest_SHA = be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776
supplemental_manifest_SHA = 78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd
S6_manifest_SHA = e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea
final_manuscript_SHA = 5C54BD725BECC7FF7253EC023E83258749B1868E14A70D34722ADCC1F421BC60
```

## 3. V4 outcome and final human selection

V4 established that a base-10 log rendering of Figure 2C was technically and
scientifically valid: its raw-value closure and deterministic SVG/PDF/PNG
checks passed, with no scientific values changed.  V4 is not a failed run and
is retained as presentation provenance.

Final human visual review selected the linear representation for publication
because the manuscript's actual claim concerns the magnitude separation
between typical and maximum target-side observations.  A linear axis preserves
that separation directly; deterministic raw-value labels prevent Q1, median,
and Q3 from being mistaken for zero or for missing values.  This does not add a
distributional, power-law, or fitted-tail claim.

V4 provenance is recorded in the V5 manifest and remains at
`figures/ch5_refq/p0v3_final_v4/` with decision
`P0V3_FIGURE_RENDER_V4_PASS_READY_FOR_FINAL_HUMAN_REVIEW`.

## 4. Exact V5 presentation changes

Only Figure 2C changed from V4:

- all three quantile inset y-axes are explicitly `LINEAR`;
- plotted y arrays are the original frozen values, with no log, ln, clipping,
  normalization, winsorization, or rescaling;
- each Q1, median, Q3, and maximum marker receives a deterministic numeric text
  label;
- integer metrics use integer labels (`1`, `2`, `5`, `42`, `3,430`);
- target coverage labels use the frozen fractional unit with compact numeric
  display formatting (`0.003401360544` and `0.1428571429`); the exact source
  values remain in the renderer contract and manifest;
- labels use inward edge offsets and deterministic vertical offsets only; marker
  coordinates are not jittered;
- the V4 connector style is preserved:
  `thin_alpha_0.55_markers_primary`.

Figure 2 A/B/D, Figures 1/3/4, and Supplementary S1–S4 remain semantically
unchanged.  S5 remains not rendered.  Captions are byte-identical to V4.

## 5. Frozen quantile and label closure

The source remains
`supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq2b_target_role_quantiles.csv`.

| metric | Q1 raw / rendered / label | median raw / rendered / label | Q3 raw / rendered / label | max raw / rendered / label |
|---|---|---|---|---|
| `in_degree` | 1 / 1 / `1` | 1 / 1 / `1` | 1 / 1 / `1` | 42 / 42 / `42` |
| `in_strength` | 1 / 1 / `1` | 2 / 2 / `2` | 5 / 5 / `5` | 3430 / 3430 / `3,430` |
| `target_coverage` | 0.0034013605442176 / 0.0034013605442176 / `0.003401360544` | 0.0034013605442176 / 0.0034013605442176 / `0.003401360544` | 0.0034013605442176 / 0.0034013605442176 / `0.003401360544` | 0.1428571428571428 / 0.1428571428571428 / `0.1428571429` |

The renderer compares every line and marker y-array to the frozen raw array,
compares every label's parsed numeric value to its marker value within the
documented display-format tolerance, and checks every label bounding box.  The
result is:

```text
F2C_IN_DEGREE_YSCALE = LINEAR
F2C_IN_STRENGTH_YSCALE = LINEAR
F2C_TARGET_COVERAGE_YSCALE = LINEAR
F2C_DATA_TRANSFORM = NONE
F2C_PLOTTED_VALUES_EQUAL_FROZEN_RAW_VALUES = PASS
F2C_RAW_VALUE_LABELS = ENABLED
F2C_RAW_VALUE_LABEL_CLOSURE = PASS
F2C_RAW_VALUE_LABEL_BBOX_CLOSURE = PASS
F2C_NO_LOG_TICK_FORMATTING = PASS
F2C_X_ORDER = Q1,Median,Q3,Max
RAW_QUANTILE_CLOSURE = PASS
RAW_VALUE_LABEL_CLOSURE = PASS
```

The linear geometry is visually obvious in the rendered Figure 2C PNG: typical
values occupy the low end while the maximum remains separated by its raw label.
The connector is visibly secondary and does not create interpolation or a fit.

## 6. Scientific freeze and pipeline non-execution

```text
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
SCIENTIFIC_RECOMPUTATION = 0
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
```

Only already frozen P0-v3/supplemental-v2 render inputs were read.  No
scientific pipeline, data derivation, event rejoin, GH-CoRE operation, or
manuscript edit was executed.

## 7. Deterministic rendering QA

Independent Attempt A and Attempt B renders were byte-identical for all 24
publication assets.  Publication PNG metadata reports 300 DPI (the normal
`299.9994` encoded value).  The contact sheet contains all eight figures and
is not counted as a publication figure.

```text
SVG_COUNT = 8
PDF_COUNT = 8
PNG_COUNT = 8
PNG_DPI = 300
SVG_DETERMINISM = PASS
PDF_DETERMINISM = PASS
PNG_DETERMINISM = PASS
AUTOMATED_RENDER_QA = PASS
SCIENTIFIC_FREEZE_QA = PASS
```

### V5 asset hashes

| figure | SVG SHA-256 | PDF SHA-256 | PNG SHA-256 |
|---|---|---|---|
| figure1_evidence_universe | `d4eaf81f91d80fd75d2343c8c2f53e9df1ca7267eba9d86af98506edbff37392` | `5ac3eecf4b17e07fed2a5982f3c49422f8597b739c68e13a0eb634401524e036` | `3b4b4d88332f3df1ecbd6c3a8f06c5737b5de0229b38b11c370e1dc4def60298` |
| figure2_source_target_roles | `d6d4fa71890891f1b0a2cb5cb9255feaa8ddeef10817d9fcf76560ffa57dc41c` | `47a6dc495ff5dd9a65d3fc2aa8c81a4c13ebd0bbf85737af28eaad988b4189c8` | `4e78df50dba13d40001fe80b1bf244603e233c190e3b48e8033ca3cbc7a63632` |
| figure3_undirected_structure | `caebb0d4fad48057456f0720bfbe6ee6b943dc1fbb55da0b79338e91c5865496` | `96cf6a0898aedb3f1d03cb572845da0f9bccb28fbc595de931396e26812dd0b3` | `b33a43def183abe8401278ce0d204f85c3e93a4a34325e9d4dd1b28bd570eea9` |
| figure4_rq3_comparison | `fee5af901d07a2b9f09a9c628bdda75e44e23651e1375c6fd8c0f3e7d25684fb` | `11619577ee51eaf8e0e9e07fa8be9d33ffef0e224cce14a7fad16829a7400c2b` | `e307d76dcff5e05502b4687c254baf3e74c5cfdcb5e4ef50299368eb357c66aa` |
| supplementary_s1_multiplicity_sensitivity | `e048d33189a1aed006d6abb3946af4b65e5cb8b8aa040d9201bfa078de07b17e` | `4604f7a651d647cd964c058dcc8c53e6a3b8cfd80200591f448da76350e50708` | `df0e39cffb3fbe1fb6749e9a51a9df23664c108d1e5602a4f5aebab90e3f69d6` |
| supplementary_s2_louvain_stability | `d95e71479643866e8f0fc5f7c05ececfcf01360a21c5310b7ac012f4f0181e18` | `5a5bccb253fbb8f6b65467df5571514953cbd9f62cb90894981754dc899d1b41` | `32073a81f4991eb77c8f833efa526183dc35cad6ff79efbf111c36d0b3ec923b` |
| supplementary_s3_brokerage_stability | `4653d3af485aca14dcbd5522d3f1ce575acccc3af5fc3156efa9e6fa1532cc67` | `2d63a3c8a106010672e73be5ee5800d5059092d00d6ca52c1bf1b864cfdb8e7e` | `58b7a676e2012d1f06a0288adc381dd21867b95ab6ede2e373884275678d5583` |
| supplementary_s4_unit_contract | `29dba46d9c03621570e96a8d8bf88c5f51af63256a85a6018132bf7c7b306430` | `d9094e43ef42aba392632925c39d8148f6e27d6f5d7e4cd94664e364fd4e9a1e` | `055eec6a4c0df116e658ba0b1cc1d3e1a02f72abb62c578ffdfae9d21da067d8` |

Additional package hashes:

```text
render_script_SHA = ed5bf4ae03d64e70e1256233e3e0363c97906605152bbc9bec9f2f2af6b4e14b
contact_sheet_SHA = 9cb41ae4ea66582b67e9b12fb1f69d215f5b292e2015e6fcb60ae53b76a28c3d
contact_sheet_dimensions = 2001 x 2815 px
```

## 8. Repository immutability and final status

The V4 root, V3 root, scientific roots, manuscript, tables, and pre-existing
zip files were checked as unchanged.  The only intended new repository content
is the V5 render root and this review document.

`HUMAN_VISUAL_QA = READY_FOR_FINAL_REVIEW`

This status is not an autonomous human approval.  It records that automated
render QA and renderer-level visual checks are complete and that final human
visual sign-off remains outstanding.

`decision = P0V3_FIGURE_RENDER_V5_PASS_READY_FOR_FINAL_HUMAN_VISUAL_QA`
