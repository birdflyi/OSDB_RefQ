# Chapter 5 RefQ Figure 4 Rank-Eta-Squared Provenance Closure

## 1. Task identity

```text
TASK = CH5_REFQ_FIGURE4_ETA_LABEL_PROVENANCE_CLOSURE
MODE = READ_ONLY_SCIENTIFIC_LINEAGE_VERIFICATION + DOCUMENTATION_ONLY_PROVENANCE_CLOSURE
TASK_BASE_REPOSITORY_HEAD = 0a9f06a7fd2f4f71ea37cb5c0c349c7f7d274fd3
BRANCH = ch5-refq-repository-identity-correction-v1
SCIENTIFIC_BASELINE = P0-v3
```

This record supersedes only the current-facing Figure 4 provenance status in
the main-figure mapping. It does not rewrite historical manifests, render
records, or audits.

## 2. Scientific and manuscript authority

The accepted immutable manuscript is MS-R04:

```text
MS_R04_SNAPSHOT = versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md
MS_R04_SNAPSHOT_SHA256 = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
CURRENT_SHA256 = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
CURRENT_EQUALS_SNAPSHOT = YES
P0_V3_MANIFEST = outputs/reference_quotient_p0_corrected_v3/manifest.json
P0_V3_MANIFEST_SHA256 = be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776
SUPPLEMENTAL_P0V3_MANIFEST_SHA256 = 78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd
```

The P0-v3 manifest records `script/ch5_reference_quotient/statistics.py` as an
implementation file with SHA-256
`db434b7d3e92b7567fd54bfa87aec79df390eb98774bd85ce990972be96fa116`; the
file at that path has the same hash. Its frozen output entry for
`rq3_kruskal_fdr_effect_sizes.csv` records SHA-256
`3ba3257c7a0060c95737d57065bea55e5e0d1d8e6a6b40493b6a24ad9b4c7363`, which
matches the file. No scientific function was executed.

## 3. Current Figure 4 authority

```text
CURRENT_FIGURE4_ASSET = figures/ch5_refq/p0v3_final_v6_e01_eta_label/
PARENT_RENDER = figures/ch5_refq/p0v3_final_v6/
FIGURE_ID = figure4_rq3_comparison
CURRENT_STATISTICAL_TERM = rank eta-squared
CURRENT_SYMBOL = η_H²
CURRENT_RENDERED_TERM = rank eta-squared
```

The accepted MS-R04 Methods defines the estimator in §3.3.3, and its Figure 4
caption uses the same term and symbol. The E01 SVG visibly carries the
`rank eta-squared` axis label. The V6 predecessor SVG carries
`epsilon-squared`.

## 4. Historical terminology lineage

The P0-v3 generated result schema and S6 figure-ready copy retain the field
name `epsilon_squared`. This is the historical schema identifier used by the
pipeline; the field name alone does not establish a separate estimator.
Historical V6 manifests, source manifests, and caption audits retain the
then-current `epsilon-squared` wording and their original asset hashes. They
remain valid historical records and are not edited by this closure.

## 5. Frozen implementation trace

```text
EFFECT_SIZE_IMPLEMENTATION_SOURCE = script/ch5_reference_quotient/statistics.py
FUNCTION = kruskal_fdr
FORMULA_LOCATION = lines 108-120
OUTPUT_GENERATION_CALL = script/ch5_reference_quotient/pipeline.py, lines 757-760
HISTORICAL_OUTPUT_FIELD_NAME = epsilon_squared
```

Within `kruskal_fdr`, the function sets `n` to the sum of retained group
observation counts and `k` to the number of eligible groups. It computes:

```text
epsilon_squared = max(0.0, float((statistic - k + 1) / (n - k))) if n > k else 0.0
```

Here `statistic` is the Kruskal-Wallis H statistic. The `n > k` branch is the
defined denominator guard; when it is false the implementation returns zero.
The frozen output and S6 figure-ready manifests tie the generated CSV and its
display copy to the P0-v3 result. The S6 transformation is declared
`stable_copy_for_plotting`, not a statistical recomputation.

## 6. Formula and field-name reconciliation

MS-R04 §3.3.3 defines rank eta-squared (`η_H²`) as `(H-k+1)/(n-k)` and states
that negative estimates are clamped to zero. The frozen implementation uses
that same expression and policy, with `0.0` as the explicit `n <= k` fallback.
Accordingly:

```text
FROZEN_ESTIMATOR = max(0, (H-k+1)/(n-k)) for n > k; 0 when n <= k
HISTORICAL_FIELD_ROLE = LEGACY_SCHEMA_IDENTIFIER_FOR_CURRENT_FROZEN_ESTIMATOR
```

No output column is renamed and no numeric value is recomputed in this audit.

## 7. V6 → E01 render lineage

The V6 and E01 renderer sources were compared without execution. In the
Figure 4 plotting code both read the same `epsilon_squared` column and use it
as the x-coordinate. The axis label changes from `epsilon-squared` to
`rank eta-squared`; the Figure 4 panel contract is updated to describe that
display terminology. The existing E01 render manifest records:

```text
terminology_delta = epsilon-squared -> rank eta-squared
figure4_semantic_label_changed = 1
figure4_data_changed = 0
figure4_geometry_changed = 0
figure4_panel_structure_changed = 0
figure4_scale_changed = 0
scientific_recomputation = 0
status = PASS
```

The E01 input hash for `rq3_kruskal_fdr_effect_sizes_plot.csv` matches the
existing file and both E01's source manifest and render manifest. This
documents identity of plotted stored values; no RQ3 rerun or renderer was
executed for this task.

## 8. Asset identity verification

The E01 render manifest SHA-256 is
`8ae373659a94846ffe4b945969cd149701474fdf4c71eb4709276a9d43da3050`; the E01
source manifest SHA-256 is
`c06767bb0c8200eef4648b03235d92c2e2dfd6d8364ed0167d9fff42e1f42059`. The
current assets were hashed read-only and match the manifest:

| Format | Relative path below current E01 root | Expected SHA-256 | Status |
|---|---|---|---|
| SVG | `main/figure4_rq3_comparison/figure4_rq3_comparison.svg` | `6ec08f8462bb13f46395678a5bfb1b5e753377399d5cfa612f85fd273b34e17a` | PASS |
| PDF | `main/figure4_rq3_comparison/figure4_rq3_comparison.pdf` | `daf4f9c486b19f229d0d13586cfceaba774bf7212466d7174877c57f07307c0c` | PASS |
| PNG | `main/figure4_rq3_comparison/figure4_rq3_comparison.png` | `6a279ae45570c06e745db65d3b14503b30f2ad98daac5c64dd8611a082fc44ea` | PASS |

## 9. Scientific no-change determination

```text
TEST_A_FORMULA_MATCH = YES
TEST_B_FIELD_IS_LEGACY_IDENTIFIER = YES
TEST_C_E01_VALUE_IDENTITY = YES
TEST_D_NO_SCIENTIFIC_OR_GEOMETRIC_CHANGE = YES
FIGURE4_SCIENTIFIC_MISMATCH = NO
SCIENTIFIC_RECOMPUTATION = 0
SCIENTIFIC_VALUE_CHANGE = 0
DATA_CHANGE = 0
GEOMETRY_CHANGE = 0
PANEL_STRUCTURE_CHANGE = 0
SCALE_CHANGE = 0
```

Tests A and B are supported by the manifest-bound implementation source and
the frozen output lineage. Test C is supported by the unchanged value-column
read and unchanged plotted coordinate in the V6/E01 source comparison, the
matching S6 input digest, and the terminology-only E01 manifest. Test D is
supported by that source comparison and E01 manifest. These are provenance
integrity checks, not new statistical results.

## 10. Historical-record preservation rule

Do not rename `epsilon_squared` in historical scientific outputs, S6 copies,
or source manifests. Do not rewrite V6 render manifests, V6 source manifests,
or historical caption/audit records to make their earlier terminology appear
current. This superseding record supplies the current estimator identity
without erasing historical evidence.

## 11. Current-facing terminology rule

For current manuscript and publication-facing Figure 4 references, use
`rank eta-squared` and `η_H²`. When tracing the frozen result schema or
pipeline, refer to `epsilon_squared` as the legacy schema field name for this
same estimator. Keep that distinction explicit; do not describe the field
name as evidence of a different effect-size computation.

## 12. Remaining figure-domain documentation debt

Figure 4's specific historical provenance debt is closed by this superseding
record. Three nonblocking figure-domain E2 documentation items remain from
the prior inventory:

1. superseded Phase 2-B historical design;
2. older scaffold-oriented migration matrix;
3. analysis-stage S1–S7 versus Supplementary Figure S1–S5 namespace ambiguity.

```text
FIGURE4_OPEN_PROVENANCE_DEBT = NO
OTHER_OPEN_FIGURE_DOCUMENTATION_DEBT_COUNT = 3
```

These historical documentation items do not indicate a current Figure 4
manuscript/render/implementation inconsistency.

## 13. No-change guards

```text
CURRENT_CHANGED = 0
MS_R04_SNAPSHOT_CHANGED = 0
MANUSCRIPT_TEXT_CHANGED = 0
CAPTION_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
SCIENTIFIC_VALUE_CHANGE_COUNT = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
SUPPLEMENTARY_MAPPING_CHANGED = 0
PREVIOUS_MAPPING_FREEZE_CHANGED = 0
FIG_P00_AUDIT_CHANGED = 0
HISTORICAL_V6_MANIFEST_CHANGED = 0
HISTORICAL_RESULT_SCHEMA_CHANGED = 0
OTHER_TRACKED_FILE_CHANGE_COUNT = 0
```

The four pre-existing untracked V3–V6 ZIP files were not staged or modified.

## 14. Final decision

```text
E0_COUNT = 0
E1_COUNT = 0
FIGURE4_SPECIFIC_OPEN_E2_COUNT = 0
OTHER_OPEN_FIGURE_DOCUMENTATION_DEBT_COUNT = 3
DECISION = CH5_REFQ_FIGURE4_ETA_LABEL_PROVENANCE_CLOSURE_PASS
```
