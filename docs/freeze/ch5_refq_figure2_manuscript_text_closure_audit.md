# Chapter 5 RefQ — Figure 2 Manuscript-Text Closure Audit

## Decision

`CH5_REFQ_FIGURE2_MANUSCRIPT_TEXT_CLOSURE_PASS_AFTER_EDIT`

The audit found no numeric or unit contradiction with the accepted Figure 2
render. Three descriptive phrases in the authoritative manuscript were
conservatively narrowed because a quantile/max contrast does not by itself
establish a formally right-skewed or long-tail distribution. No scientific
value, denominator, graph rule, or figure asset was changed.

## 1. Repository starting state

```text
repository = D:/github_repo/OSDB_RefQ
branch = ch5-refq-repository-identity-correction-v1
repository_HEAD_before = 91637b867ba8275a6917d3f5b65430426103bb3b
remote_HEAD_before = 91637b867ba8275a6917d3f5b65430426103bb3b
working_tree_before = four pre-existing untracked V3/V4/V5/V6 ZIP archives only
```

The ZIP archives were preserved and were not staged. No reset, clean, rerender,
pipeline execution, or scientific-output write was performed.

The authoritative manuscript is maintained outside this repository at:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md`

Its SHA-256 was `5C54BD725BECC7FF7253EC023E83258749B1868E14A70D34722ADCC1F421BC60`
before the edit and `13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309`
after the edit. Historical manuscript snapshots, including the OLD and QA
baselines, were not modified.

## 2. Authority inputs inspected

| Authority | Path | SHA-256 / decision |
|---|---|---|
| Accepted publication root | `figures/ch5_refq/p0v3_final_v6/` | immutable; `P0V3_FIGURE_RENDER_FINAL_ACCEPTED` |
| V6 manifest | `figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json` | `469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da` |
| Figure 2 V6 source manifest | `figures/ch5_refq/p0v3_final_v6/main/figure2_source_target_roles/source_manifest.json` | `441d02592d8d90574802ecf8a43b78ee2b0a35bb54f9028886054c02cfa4dbca` |
| Figure 2 SVG/PDF/PNG | `figures/ch5_refq/p0v3_final_v6/main/figure2_source_target_roles/` | `36f07513…f956b`, `762136aa…62b0`, `f2a86d2d…4311` |
| Target quantiles | `supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq2b_target_role_quantiles.csv` | `1b2a1f58db6fa6f01394db6bd217e19ea3e39ad80bac62391c58870654e7b4ee` |
| Target concentration | `outputs/reference_quotient_p0_corrected_v3/rq2b_target_concentration.json` | `1deed3aa5492d92ac4ce2f0d93ee7aa5e6897be10ccf528cb9b0c1f81f58a9b6` |
| Membership audit | `outputs/reference_quotient_p0_corrected_v3/membership_audit.json` | `4455a6af…b4259f`; `status=PASS` |
| Quotient audit | `outputs/reference_quotient_p0_corrected_v3/quotient_construction_audit.json` | `b54e21be…ee6b0`; `status=PASS` |
| Final acceptance record | `docs/freeze/ch5_refq_p0v3_figure_rendering_final_acceptance.md` | `P0V3_FIGURE_RENDER_FINAL_ACCEPTED` |

The V6 renderer contract records linear y-axes, `NONE` data transform,
`thin_alpha_0.55_markers_primary`, raw quantile coordinates, and the accepted
publication labels. These are presentation authorities, not new manuscript
statistics.

## 3. Files and passages inspected

Inspected:

1. The authoritative reconciled/composition manuscript named above, including
   the abstract, definitions in Sections 3.3–3.4, all of Section 4.2
   (RQ2a/RQ2b/RQ2c), Discussion, limitations, conclusion, and Appendix A.
2. `figures/ch5_refq/p0v3_final_v6/captions_draft_v6.md` and the immutable V3–V5
   caption drafts, solely to distinguish rendering provenance from manuscript
   prose.
3. `docs/freeze/ch5_refq_p0v3_final_figure_plan_v1.md`, the V6 source manifest,
   V6 render manifest, and the V6 acceptance/review records.
4. Frozen target quantile, concentration, membership, and quotient audit files.

The authoritative manuscript contains no inserted Figure 2 caption. The
caption drafts are explicitly rendering artifacts and are not manuscript text;
therefore no caption was added. The body passages under Sections 4.2a and
4.2b provide the reader-facing Figure 2 interpretation.

## 4. Internal audit table

| location | current wording before edit | issue type | evidence | recommended action | severity |
|---|---|---|---|---|---|
| Abstract, line 10 | “主动引用范围和聚合强度具有明显右偏” | `OVERCLAIM` | Abstract summarized a role contrast without a formal skewness/distribution fit | Describe typical/max separation and retained target concentration | P1 |
| Section 4.2a, line 518 | “分位数与极大值之间的明显差距显示……呈现较长的右尾” | `OVERCLAIM` | Frozen source quantiles support a contrast, not a fitted tail family | State that a small number of seed sources have values above the typical level; retain explicit no-fitting limitation | P1 |
| Discussion, line 655 | “source out-degree/out-strength 和 target weight 存在右偏与集中” | `OVERCLAIM` | Target concentration is frozen, but “right-skew” is stronger than the displayed quantile evidence | Separate quantile/max contrast from target-weight concentration | P1 |
| Section 4.2b, lines 544–561 | median/max, Top-k shares, denominator, and coverage | `NO_CHANGE_REQUIRED` | All values and metric definitions match frozen files | Leave unchanged | INFO |
| Sections 3.3–3.4 and 4.2.0 | source/target, record/weight/edge definitions | `NO_CHANGE_REQUIRED` | Explicit role and unit contract; no entity/edge conflation | Leave unchanged | INFO |
| V6 caption draft, line 27 | “Panel C uses base-10 logarithmic y-axes…” | `STALE_RENDER_LANGUAGE` | Conflicts with final V6 acceptance but file is an immutable rendering artifact, not manuscript prose | Do not edit historical render provenance; record as non-blocking | INFO |

## 5. Figure 2 caption and panel audit

There is no manuscript-embedded Figure 2 caption in the authoritative source.
The V6 draft caption was reviewed as a provenance artifact. It correctly names
the asymmetric source/target view, separates source out-degree/out-strength,
defines strength as aggregated Reference-record weight, uses 294 source
observations for target coverage, and identifies the 138,974 cross-project
weight denominator for concentration. Its log-axis sentence is historical
rendering provenance and is not copied into the manuscript; the accepted V6
publication root is linear for all Figure 2C axes.

The manuscript body closes the panel semantics as follows:

- RQ2a is source-side behavior of the 294 source-complete seed projects.
- RQ2b is target-side in-degree, in-strength, coverage, and concentration for
  observable targets; expanded targets are explicitly source-incomplete.
- RQ2c is a separate first-order undirected view and is not treated as a
  shared-reference projection.
- No line or marker is described as a fitted curve, interpolation, time path,
  or distributional model.

## 6. RQ2a audit

The frozen source quantiles are out-degree Q1/median/Q3/max = `3/11/39/352`
and out-strength Q1/median/Q3/max = `5/26.5/192.75/43,574`. The revised sentence
now says that the quantiles and maxima show a clear separation and that a small
number of seed sources have substantially higher observed range/weight. It
retains the explicit statement that no distribution fitting was executed and
does not introduce a tail-family claim.

The seed-to-seed and seed-to-expanded counts/weights remain unchanged and are
not affected by the wording edit.

## 7. RQ2b audit

The manuscript reports `6,322` observable targets (`110` seed targets and
`6,212` expanded targets), in-degree median/max `1/42`, in-strength median/max
`2/3,430`, and target-weight shares `2.47% / 16.00% / 48.99%` with denominator
`138,974`. It explicitly states that most observable targets have one seed
source and that a smaller set receives higher coverage or repeated weight.

Target coverage is defined with denominator `294`; maximum in-degree `42`
therefore gives `42/294 = 0.1428571428571428 = 14.29%`. The V6 quantile authority
has Q1/median/Q3 coverage all `0.0034013605442176 = 0.34%`; the manuscript does
not print those quartile labels, so no unsupported quartile value was added.

The Top-k values are independently frozen in
`rq2b_target_concentration.json`: exact shares are
`0.024680875559457166`, `0.15998676011340252`, and
`0.4899261732410379`, which round to `2.47%`, `16.00%`, and `48.99%`.
The manuscript's logic is descriptive concentration, not a causal or
distribution-family claim.

## 8. Numeric closure table

| quantity | manuscript | frozen authority | closure |
|---|---:|---:|---|
| in-degree median | 1 | 1 | PASS |
| in-degree maximum | 42 | 42 | PASS |
| in-strength median | 2 | 2 | PASS |
| in-strength maximum | 3,430 | 3,430 | PASS |
| target coverage Q1 | not printed | 0.0034013605442176 (0.34%) | NOT_APPLICABLE |
| target coverage median | not printed | 0.0034013605442176 (0.34%) | NOT_APPLICABLE |
| target coverage Q3 | not printed | 0.0034013605442176 (0.34%) | NOT_APPLICABLE |
| maximum target coverage | 14.29% from 42/294 | 0.1428571428571428 (14.29%) | PASS |
| Top-1 weight share | 2.47% | 2.4680875559457166% | PASS |
| Top-10 weight share | 16.00% | 15.998676011340252% | PASS |
| Top-50 weight share | 48.99% | 48.99261732410379% | PASS |
| concentration denominator | 138,974 | 138,974 | PASS |

## 9. Distributional-language audit

| occurrence | classification | rationale |
|---|---|---|
| Abstract pre-edit “明显右偏” (RQ2 summary) | `UNSUPPORTED_FOR_CURRENT_EVIDENCE` → corrected | Quantile/max contrast and concentration do not establish formal skewness; replaced with “典型值与极大值之间存在明显差距”. |
| Section 4.2a pre-edit “较长的右尾” | `UNSUPPORTED_FOR_CURRENT_EVIDENCE` → corrected | No fitted distribution or tail test; replaced with a bounded higher-than-typical observation statement. |
| Discussion pre-edit “右偏与集中” (RQ2a/RQ2b) | `SUPPORTED_BUT_NEEDS_QUALIFICATION` → corrected | Concentration is supported, but the right-skew label was too strong for Figure 2 evidence alone. |
| Section 4.1 active-issue “右偏分布” | `SUPPORTED`, `UNRELATED_TO_FIGURE2` | It is an RQ1 project-profile description with explicit mean/median/skewness/kurtosis values and no Figure 2 interpretation. |
| Section 4.1 discussion-depth “右偏” | `SUPPORTED`, `UNRELATED_TO_FIGURE2` | It reports frozen descriptive skewness/kurtosis for a different RQ1 metric. |
| “幂律/无标度结构” disclaimer in Section 4.2a | `SUPPORTED_BUT_NEEDS_QUALIFICATION` | Correctly states that no such claim is made; retained unchanged. |
| `power-law`, `heavy-tail`, `long-tail`, `scale-free`, `preferential attachment`, `hub` | none as Figure 2 claims | No unsupported positive occurrence remains in the authoritative manuscript. |

## 10. Stale rendering-language audit

The authoritative manuscript contains no `log10`, `log-scale`, `logarithmic`,
`raw-value label`, `V4`, `V5`, or `V6` rendering-process statement. It does not
describe transformed quantiles or internal QA. The historical V4–V6 caption
drafts and reviews contain intermediate log/linear wording, but those files are
immutable provenance and are not manuscript-facing text. No figure asset or
manifest was changed.

## 11. Exact manuscript edits

Only the authoritative external manuscript was edited, in three sentences:

1. **Abstract**
   - Before: `主动引用范围和聚合强度具有明显右偏`
   - After: `主动引用范围和聚合强度在典型值与极大值之间存在明显差距`
   - Reason: preserve the observed contrast without an unsupported formal skewness label.
2. **Section 4.2a RQ2a**
   - Before: `分位数与极大值之间的明显差距显示，主动引用范围和聚合强度呈现较长的右尾`
   - After: `分位数与极大值之间存在明显差距，表明少数 seed source 的主动引用范围和聚合强度显著高于典型值`
   - Reason: retain the quantile/max finding and explicit no-fitting boundary.
3. **Discussion Section 5.1**
   - Before: `source out-degree/out-strength 和 target weight 存在右偏与集中`
   - After: `source out-degree/out-strength 的典型值与极大值之间存在明显差距，target weight 集中于少数项目`
   - Reason: keep the independently supported concentration result while removing the overstrong distribution label.

No numeric token, table value, RQ definition, graph operator, source/target
membership rule, citation, figure reference, or historical manuscript snapshot
was changed.

## 12. Unchanged-but-reviewed passages

The following were reviewed and intentionally left unchanged: the Section 4.2b
target counts and medians/maxima; the `3,430/138,974 = 2.47%` rounding example;
the `42/294 = 14.29%` coverage explanation; source/target metric definitions;
the 9,595 directed versus 9,547 undirected edge distinction; the explicit
record/node/edge and weight/unit boundaries; the seed-centered observation
limitation; and the no-power-law/no-scale-free disclaimer.

## 13. Scientific guards and immutability

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
FIGURE_RERENDER = 0
figure_assets_changed = 0
scientific_assets_changed = 0
manuscript_files_changed = 1 (external authoritative source only)
```

The V6 root, V3/V4/V5 roots, all manifests, supplemental outputs, P0-v3
outputs, and historical receipts remain byte-identical. The repository working
tree retains the four pre-existing untracked ZIP archives.

## 14. Final assessment

```text
P0_ISSUES = 0
P1_ISSUES = 3 (all corrected in the authoritative manuscript)
P2_ISSUES = 0
INFO_ITEMS = 6
NUMERIC_MISMATCH = 0
METRIC_SEMANTIC_MISMATCH = 0
OVERCLAIM = 3 (corrected)
STALE_RENDER_LANGUAGE = 0 manuscript-facing; 1 immutable artifact note
RQ_TERMINOLOGY = 0
UNIT_MISMATCH = 0
FIGURE_CAPTION = 0 blocking; manuscript has no embedded caption
CROSS_REFERENCE = 0
reconciliation_readiness = READY
```

The Figure 2 manuscript text is closed against the accepted V6 scientific and
presentation authorities after the three bounded wording edits. The next
authorized activity may proceed to the planned conservative three-way
reconciliation audit; this task itself performed no reconciliation.

