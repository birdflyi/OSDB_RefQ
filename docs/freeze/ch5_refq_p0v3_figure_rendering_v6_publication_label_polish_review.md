# Chapter 5 RefQ Figure Rendering V6 — publication-label polish review

## 1. Purpose

V6 is a presentation-only micro-polish of the isolated Figure 2C render.  The
V5 publication-scale decision is final: all three Figure 2C y-axes remain
linear.  V6 changes only publication text formatting for target coverage and
removes internal QA scale wording from the Panel C title.

No scientific computation, data derivation, manuscript edit, table edit, or
figure logic outside the authorized text changes was performed.

## 2. Frozen starting state

- Repository: `D:/github_repo/OSDB_RefQ`
- Branch: `ch5-refq-repository-identity-correction-v1`
- `repository_HEAD_before = 649ff466f8dc2be434bee677158817b799dbfc25`
- Local and remote starting HEAD were identical.
- V3, V4, and V5 roots remain immutable.
- Existing untracked `figures/ch5_refq/p0v3_final_v3.zip` and
  `figures/ch5_refq/p0v3_final_v4.zip` were preserved untouched.

Frozen authority hashes used by the renderer:

```text
P0_manifest_SHA = be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776
supplemental_manifest_SHA = 78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd
S6_manifest_SHA = e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea
final_manuscript_SHA = 5C54BD725BECC7FF7253EC023E83258749B1868E14A70D34722ADCC1F421BC60
```

## 3. V4 and V5 provenance

V4 demonstrated that the Figure 2C base-10 logarithmic presentation was a
valid display alternative, with raw-value and deterministic-render QA passing
and no scientific values changed.  V4 remains valid immutable provenance; it
was not scientifically wrong.

V5 finalized the linear representation for publication after human visual
selection because the manuscript's intended observation is the magnitude
separation between typical and maximum target-side values.  V5 added raw-value
labels while preserving all marker coordinates and frozen values.  V6 does not
reopen that scale selection.

## 4. Authorized V6 changes

### Target coverage labels

The marker coordinates remain the original frozen fractions:

```text
Q1     = 0.0034013605442176
Median = 0.0034013605442176
Q3     = 0.0034013605442176
Max    = 0.1428571428571428
```

Only the publication label strings changed to match the percentage-formatted
y-axis:

```text
Q1     -> 0.34%
Median -> 0.34%
Q3     -> 0.34%
Max    -> 14.29%
```

This is display formatting, not a data transformation, rescaling, or
recomputation.  The renderer compares the V6 marker arrays to the V5 arrays
and validates each percentage label against the underlying fraction.

### Panel C title

```text
before: Target-role quantile profile (linear y-scales)
after:  Target-role quantile profile
```

No axis scale changed.  The title now uses publication wording while scale
selection remains recorded in V4/V5/V6 provenance.

All other Figure 2C labels, Figure 2 A/B/D, Figures 1/3/4, Supplementary
S1–S4, captions, and scientific inputs are frozen.

## 5. Renderer-level closure

```text
F2C_AXIS_SCALE = LINEAR
F2C_IN_DEGREE_YSCALE = LINEAR
F2C_IN_STRENGTH_YSCALE = LINEAR
F2C_TARGET_COVERAGE_YSCALE = LINEAR
F2C_DATA_TRANSFORM = NONE
F2C_X_ORDER = Q1,Median,Q3,Max
F2C_CONNECTOR_STYLE = thin_alpha_0.55_markers_primary
F2C_TARGET_COVERAGE_RAW_VALUES_UNCHANGED = PASS
F2C_TARGET_COVERAGE_MARKER_COORDINATES_UNCHANGED = PASS
F2C_TARGET_COVERAGE_LABEL_UNIT = PERCENT
F2C_TARGET_COVERAGE_LABEL_FORMAT = TWO_DECIMAL_PERCENT
F2C_TARGET_COVERAGE_LABEL_CLOSURE = PASS
F2C_RAW_VALUE_LABEL_CLOSURE = PASS
F2C_RAW_VALUE_LABEL_BBOX_CLOSURE = PASS
F2C_NO_LOG_TICK_FORMATTING = PASS
V5_V6_F2C_MARKER_COORDINATE_CLOSURE = PASS
V5_V6_IN_DEGREE_LABEL_CLOSURE = PASS
V5_V6_IN_STRENGTH_LABEL_CLOSURE = PASS
RAW_QUANTILE_CLOSURE = PASS
RAW_VALUE_LABEL_CLOSURE = PASS
```

The V5 and V6 source-manifest input SHA maps are identical for all eight
figures.  The only Figure 2C source-manifest presentation differences are the
shorter Panel C title and two-decimal percentage coverage labels.

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

Only frozen render inputs and the immutable V5 Figure 2 source manifest were
read.  No scientific pipeline or event operation was run.

## 7. Deterministic publication rendering

Independent Attempt A and Attempt B renders were byte-identical for all 24
publication assets.  Each publication PNG reports 300 DPI (encoded as the
normal `299.9994` DPI value).  The contact sheet is separate and is not counted
among the eight publication figures.

```text
SVG_COUNT = 8
PDF_COUNT = 8
PNG_COUNT = 8
SVG_DETERMINISM = PASS
PDF_DETERMINISM = PASS
PNG_DETERMINISM = PASS
AUTOMATED_RENDER_QA = PASS
SCIENTIFIC_FREEZE_QA = PASS
```

### V6 asset hashes

| figure | SVG SHA-256 | PDF SHA-256 | PNG SHA-256 |
|---|---|---|---|
| figure1_evidence_universe | `63b5a581e65ef305ea7a3fefd1e952e297a799e6f4d6fbb278df6e05b6b74d24` | `88de1c8c6bf62d8246492662f17a98a678bd2306aabccce465b6ffeab15f3229` | `1b30d76b37f171103b0d7f1e803cae1146b163b3e7dcdc1573cb1099c6c8ec5e` |
| figure2_source_target_roles | `36f07513c7227261706966ba568475d68269ff8a03ad44b50f78daf06a7f956b` | `762136aae28f520532318308723aa343b5878565745143d59bd6ea904bf262b0` | `f2a86d2d8706415a7723892245eef31eb7c6b5b62a693b4142aed7f3cddf4311` |
| figure3_undirected_structure | `b1bba74418b268985e90b7be0696d125fea02b1e6b9522fb8bb759eb0f57cb50` | `6ab0a57e25485a68ec343fc84b1b00c1851ebc21265bf6fe9b9e396c5ff6be7d` | `94d7952e6f00f74f11969c83652bd1379d426b734041f5a1890f0f982a22e22f` |
| figure4_rq3_comparison | `2a4a486ce9aff1cb7da19c07776495db9574d73f8967f1ef27657fedbc047695` | `212d30c35bf3bfc625cbfc5be0f008d789df000cbde23442951d9792eafcf42e` | `4d92b97743dd2671f1711a6c025b372dea7d754d55ca0286ceccda5909d14503` |
| supplementary_s1_multiplicity_sensitivity | `8238af8d1303baac03ced9cecf5373ac9d92dd55610f528f52a3d3664ab5ce5e` | `568612462f7226c119af095123b5d0cafcc39b1c9969d552cf5b5d75f473cc56` | `928cdfa7d9e1d5a7cf6691a6cc9c98f7bb59cbd2d3dab8a9d9ea79a3498852aa` |
| supplementary_s2_louvain_stability | `82bb19482576b560ca40bd778cd6c04b33e2c07e20f4ccd7a4e6e0a1caaf26e0` | `fbe0efe54f6b8fa2ad064997374fdb554bf40f9ff403bb7f470129b8b34b7552` | `f3db529178117260e5b0fde4298db678a4046e1f2475d2878952991d725ce27e` |
| supplementary_s3_brokerage_stability | `bf56b9efb690681c8950f35f615b82f737f02756b54b4c09eedf822d7a4c4505` | `0694920c038e8321b12ee6dd67bf39b3c803b2077b51dd9ce1048116e7e68b15` | `1fd66d8fcb7e50978ce7fb5f38e1d3c7da03321195b649d20d4cf9f4bc30f892` |
| supplementary_s4_unit_contract | `b458c0c2410ec01bbdd2bfabf306a34b239e3f7af90a865f3d62555783f3c0da` | `11cdadd6dd5097f1a1ca1e40ec5dddc06194c59d37cd4c74b5af3c164624c143` | `a7d92310c8e360ecee1f29690ecc88a3fb5289f1b1dfdbe69fd70c87a769b55a` |

```text
render_script_SHA = d50b26e179146c9617fb0e876566c6b66d5a26e20e2f27117feb79238ed712d4
contact_sheet_SHA = 05ce61a87bd310d5485c0bc5860f2c1df9d4b86a11d36ceebd18b729743d8ec3
contact_sheet_dimensions = 2001 x 2815 px
```

## 8. Final status

V6 changes only display-level labeling and title text.  The raw target
coverage fractions and all marker coordinates remain frozen.  V4 log-scale and
V5 linear-selection artifacts remain immutable provenance.

`HUMAN_VISUAL_QA = READY_FOR_FINAL_REVIEW`

This is not autonomous final human acceptance.

`decision = P0V3_FIGURE_RENDER_V6_PASS_READY_FOR_FINAL_HUMAN_VISUAL_QA`
