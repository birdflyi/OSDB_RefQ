# Chapter 5 RefQ - Submission Editing Batch D: Results

## Decision

`CH5_REFQ_SUBMISSION_EDIT_BATCH_D_RESULTS_PASS`

This record documents the bounded Results prose edit performed after the
accepted hierarchy, terminology, and Related Work decisions.  The external
authoritative manuscript was edited only in the permitted prose locations in
§4.1, §4.2, and §4.3.  No experiment, scientific pipeline, renderer, table,
caption, or scientific asset was run or changed.

## 1. Starting identity and preserved state

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| `repository_HEAD_before` | `1079ba2956b041f96ba6b4f0bb30141830b6c6c3` |
| `remote_HEAD_before` | `1079ba2956b041f96ba6b4f0bb30141830b6c6c3` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Manuscript SHA before | `53F30E4406BD0195AD097A1C425F3B5EC8A19048B5C1BADC429F6B673425901B` |
| Read-only baseline copy | `C:/Users/10651/AppData/Local/Temp/ch5_refq_batch_d_results_baseline_20260831.md` |
| Baseline-copy SHA | `53F30E4406BD0195AD097A1C425F3B5EC8A19048B5C1BADC429F6B673425901B` |
| Manuscript SHA after | `34A8F0D63BA93C30361FA16529F0AD1C1970E18AA74FE8FB55EE1C42A94CEB16` |
| Manuscript location in Git | External; not tracked by `OSDB_RefQ` |
| Initial repository worktree | Four pre-existing untracked V3/V4/V5/V6 ZIP archives only |

The preserved untracked archives were not staged or modified:

```text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
```

The expected starting manuscript SHA matched before the first edit.  The
after SHA above records the intentional external manuscript change and must
not be treated as a repository-tracked manuscript commit.

## 2. Governing hierarchy and authorized scope

The frozen Results hierarchy remains:

```text
RQ1 = evidence-universe / construction-boundary support
RQ2a/RQ2b/RQ2c = core Project-level RefQN structural characterization
RQ3 = bounded DBMS-domain comparison
```

The Results roadmap immediately after `## 4 结果` was not edited.  Changes
were limited to prose after that roadmap and before `## 5 讨论`, specifically
the local prose blocks in §4.1.2, §4.1.3, §4.2c, and the §4.3 lead-in.

```text
RESULTS_PROSE_CHANGED = 1
RESULTS_ROADMAP_CHANGED = 0
RQ1_BOUNDARY_ROLE = PASS
RQ2ABC_STRUCTURAL_CENTER = PASS
RQ3_BOUNDED_EVALUATION = PASS
RQ1_ENTITY_COUNTS_CHANGED = 0
SELF_REFERENCE_VALUES_CHANGED = 0
```

## 3. Before/after issue table

| ID | Subsection | Before issue | After treatment | Scientific status changed? | Risk |
|---|---|---|---|---:|---|
| D01 | §4.1.2 | Table 4.3 interpretation was repeated in three adjacent prose blocks | Consolidated into one right-skew / typical-versus-large-project paragraph retaining CockroachDB `22,349`, with explicit descriptive-only boundaries | No | LOW |
| D02 | §4.1.3 | Cross-sectional limitation was stated three times | Kept the 2023 single-window opening, retained the four Spearman results, and reduced the closing boundary to one sentence | No | LOW |
| D03 | §4.2c | Internal `S4 sensitivity` stage label | Replaced with `50 次不同 random seed 的 Louvain 敏感性分析` | No | LOW |
| D04 | §4.2c | Working-note phrase `当前 corrected top-five` | Replaced with `按 approximate betweenness 排序，前五位分别为` | No | LOW |
| D05 | §4.2c | Internal `S5` stage label | Replaced with an approximate-betweenness sampling-stability description | No | LOW |
| D06 | §4.2c | Raw `robustness_alert=FALSE` field | Replaced with publication-facing no-alert / high-ranking-stability wording | No | LOW |
| D07 | §4.3 opening | Three raw CSV filenames | Replaced with the scientific comparison description for both label modes | No | LOW |
| D08 | §4.3 opening | Raw `test_status` and `reject flag` fields | Replaced with Kruskal-Wallis, effect-size, and Benjamini-Hochberg FDR wording | No | LOW |

No candidate edit required a HIGH-risk treatment.

## 4. §4.1 edits

### D01 - active-issue distribution

The three repeated blocks after Table 4.3 were replaced by this single
paragraph:

```text
表 4.3 显示，活跃议题数明显右偏且峰度较高：中位数 85.50 远低于均值 739.92，CockroachDB 的 22,349 为当前项目级 profile 中的观测最大值，说明少数高活跃项目显著抬高整体协作规模，而多数项目处于较低活跃区间。该结果仅描述当前项目级分布，不表示已经识别核心—边缘结构，也不支持生命周期或特定分布模型解释。
```

The table remains the authority for every complete statistic, including Q1,
Q3, skewness, and kurtosis.  The consolidated prose retains right skew,
typical-versus-large-project contrast, the CockroachDB maximum, and the
non-core-periphery/non-distribution-model/lifecycle boundaries.

```text
ACTIVE_ISSUE_REDUNDANCY_REDUCED = PASS
RQ1_RIGHT_SKEW_SUPPORTED = PASS
CORE_PERIPHERY_CLAIM_ADDED = 0
DISTRIBUTION_MODEL_CLAIM_ADDED = 0
```

The New Comment Rate and Comment Reference Density blocks were byte-identical
to baseline.  AlaSQL and pubkey/rxdb values remain in the latter block, and
the distinction between discussion intensity and comment Reference density
was not collapsed.  No quality, resolution, or causal claim was added.

### D02 - project-age boundary

The opening remains the single-window 2023 cross-sectional definition.  The
four frozen Spearman results remain unchanged; only the repeated ending was
shortened to:

```text
这些关联只支持项目间横截面差异，不能解释为同一项目的时间演化或因果效应。
```

The separate opening repetition was removed, while the numbered local
boundary label and Table 4.6a were retained.

```text
PROJECT_AGE_CROSS_SECTIONAL_BOUNDARY = PASS
PROJECT_AGE_REDUNDANCY_REDUCED = PASS
LONGITUDINAL_CLAIM = 0
CAUSAL_AGE_CLAIM = 0
```

## 5. §4.2 edits

The source/target observation asymmetry, all §4.2.0 denominators, and the
RQ2a/RQ2b blocks were unchanged:

```text
SOURCE_TARGET_OBSERVATION_ASYMMETRY = PASS
EXPANDED_TARGET_SOURCE_COMPLETE_CLAIM = 0
TABLE_4_6B_VALUES_CHANGED = 0
```

### D03 - Louvain sensitivity wording

`S4 sensitivity` was replaced by:

```text
50 次不同 random seed 的 Louvain 敏感性分析
```

The canonical 35-community realization, 32--37 sensitivity range, 42/50
ARI-to-canonical result, minimum ARI `0.6823671359861659`, minimum pairwise
ARI `0.6092441840471735`, and algorithmic modular neighborhood boundary all
remain unchanged.

### D04 - brokerage ranking wording

The working-note phrase was replaced by:

```text
按 approximate betweenness 排序，前五位分别为
```

All five project identities, order, and values remain unchanged.  The metric
continues to be described as a fixed-500-node unweighted
approximate-betweenness sample and only a bridge-like position in the current
LCC.

### D05/D06 - sampling stability wording

The internal stage/field sentence was replaced by:

```text
对 approximate-betweenness 抽样设置的稳定性分析为 brokerage ranking 提供辅助证据：minimum Spearman 为 0.9998339514284217，minimum top-50 overlap 为 0.82；在已测试的 sampling settings 下未触发预设稳健性告警，排名整体保持较高稳定性。这不改变候选位置的弱语义边界。
```

This preserves the minimum Spearman, minimum top-50 overlap, and the weak
semantic interpretation without exposing an internal output field.

## 6. §4.3 edits

The new scientific lead-in is:

```text
本节在 include_mixed 与 exclude_mixed_or_multilabel 两种标签口径下，比较 Reference composition、RefQ role/local-structure features 和 project age。前者允许多标签项目进入多个 category group，后者仅保留单一标签项目。组间检验采用 Kruskal-Wallis，并报告效应量与 Benjamini-Hochberg FDR 校正结果。
```

This retains the two label modes and the fact that `include_mixed` permits a
multi-label project to enter multiple category groups.  The complete list of
six FDR-supported include-mixed features remains once in the principal
§4.3.2 result sentence and in the frozen Figure 4 caption/Table 4.8 context;
the adjacent summary uses the shorter selected-feature wording already
present.  Reference-composition FDR status, exclude-mode none status, and
cross-mode robust-feature count remain unchanged.

```text
RQ3_ANALYSIS_SEMANTICS_PRESERVED = PASS
RQ3_REFERENCE_COMPOSITION_FDR_STATUS = PASS
RQ3_INCLUDE_MIXED_STATUS = PASS
RQ3_EXCLUDE_STATUS = PASS
RQ3_CROSS_MODE_ROBUST_FEATURE_COUNT = 0
RQ3_LABEL_MODE_SENSITIVE = PASS
```

## 7. Removed duplicate numeric-occurrence ledger

The whole-manuscript numeric-token diagnostic changed from 1,157 to 1,150
occurrences.  Eight occurrences were removed because they duplicated values
still present in Table 4.3 or an existing frozen Results authority.  One
occurrence of the already-existing value `50` was added while spelling out
the accepted 50-run sensitivity analysis.  No scientific value was created,
recomputed, or changed.

| Value | Old location | Removal/rewrite reason | Remaining authoritative location |
|---|---|---|---|
| `85.50` | §4.1.2 old prose lines 451 and 453 | One repeated prose occurrence removed | Table 4.3 and consolidated paragraph |
| `739.92` | §4.1.2 old prose lines 451 and 453 | One repeated prose occurrence removed | Table 4.3 and consolidated paragraph |
| `22,349` | §4.1.2 old prose lines 451 and 453 | One repeated prose occurrence removed | Table 4.3 and consolidated paragraph |
| `15.00` | §4.1.2 old prose line 453 | Table-cell quantile need not be restated | Table 4.3 |
| `566.00` | §4.1.2 old prose line 453 | Table-cell quantile need not be restated | Table 4.3 |
| `6.25` | §4.1.2 old prose line 453 | Table-cell skewness need not be restated | Table 4.3 |
| `51.99` | §4.1.2 old prose line 453 | Table-cell kurtosis need not be restated | Table 4.3 |
| `294` | §4.3 old opening line 612 | Internal replacement-count detail removed from publication lead-in | RQ1/§4.2 seed-project statements and frozen tables/captions |

The added `50` is a restatement of an existing sensitivity-run value already
present in `42/50` and the frozen Figure 3 caption, not a new scientific
value.  Therefore:

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
SCIENTIFIC_VALUE_CHANGE_COUNT = 0
UNIQUE_SCIENTIFIC_VALUE_LOSS_COUNT = 0
DUPLICATE_NUMERIC_OCCURRENCES_REMOVED = 8
```

## 8. Table, caption, heading, and byte identity

The following before/after comparisons were made against the read-only
baseline copy:

```text
RESULTS_ROADMAP_CHANGED = 0
TABLE_4_1_CHANGED = 0
TABLE_4_2_CHANGED = 0
TABLE_4_3_CHANGED = 0
TABLE_4_4_CHANGED = 0
TABLE_4_5_CHANGED = 0
TABLE_4_6A_CHANGED = 0
TABLE_4_6B_CHANGED = 0
TABLE_4_6C_CHANGED = 0
TABLE_4_6D_CHANGED = 0
TABLE_4_6E_CHANGED = 0
TABLE_4_6F_CHANGED = 0
TABLE_4_7_CHANGED = 0
TABLE_4_8_CHANGED = 0
RESULTS_TABLE_CHANGE_COUNT = 0
TABLE_CHANGE_COUNT = 0
FIGURE_CAPTION_COUNT = 4
FIGURE_CAPTION_EDIT_COUNT = 0
FIGURE_CAPTION_CHANGED = 0
RESULTS_FIGURE_CAPTION_CHANGE_COUNT = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
RQ_HEADING_CHANGED = 0
RESULTS_HEADING_CHANGE_COUNT = 0
```

The manuscript contains four figure-caption blocks, 126 Markdown table rows,
65 Markdown headings, and 13 equation/display-math markers both before and
after; each extracted frozen array is byte-identical.  The Results roadmap
prefix and the complete suffix from `## 5 讨论` onward are byte-identical.
The unchanged local slices include §4.1.1, the New Comment Rate block, the
Comment Reference Density block, §4.2.0, §4.2a, §4.2b, and §4.3.1.

```text
NON_RESULTS_PROSE_CHANGED = 0
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
```

## 9. Statistical-status closure

| Status surface | Before | After | Closure |
|---|---|---|---|
| RQ1 descriptive distribution | Right-skew/high-kurtosis descriptive profile only | Same | PASS |
| Project-age design | 2023 single-window cross-sectional association | Same | PASS |
| RQ2a distribution-model status | No fitted power-law/scale-free claim | Same | PASS |
| RQ2b concentration status | Descriptive target-side concentration under frozen denominator | Same | PASS |
| RQ2c community sensitivity | 35 canonical realization; 32--37 range and ARI limitations | Same | PASS |
| RQ2c brokerage robustness | Minimum Spearman `0.9998339514284217`, top-50 overlap `0.82`, bounded stability | Same | PASS |
| RQ3 FDR status | Composition none; six include-mixed features; exclude none | Same | PASS |
| RQ3 label-mode sensitivity | No cross-mode robust feature | Same | PASS |

```text
STATISTICAL_STATUS_CHANGE_COUNT = 0
```

## 10. Interpretation and internal-language guards

```text
DEPENDENCY_OVERCLAIM = 0
TASK_RESOLUTION_OVERCLAIM = 0
CAUSAL_OVERCLAIM = 0
PROJECT_IMPORTANCE_OVERCLAIM = 0
POWER_LAW_CLAIM = 0
SCALE_FREE_CLAIM = 0
HEAVY_TAIL_CLAIM = 0
LONG_TAIL_CLAIM = 0
SEMANTIC_COMMUNITY_CLAIM = 0
LONGITUDINAL_AGE_CLAIM = 0
```

The following internal workflow terms were counted within the §4 Results
slice only (Appendix A and other reproducibility records were not targets):

| Term | Count after |
|---|---:|
| `S4` | 0 |
| `S5` | 0 |
| `corrected` | 0 |
| `robustness_alert=` | 0 |
| `rq3_seed_role_aware_features.csv` | 0 |
| `rq3_subdomain_descriptive_comparison.csv` | 0 |
| `rq3_kruskal_fdr_effect_sizes.csv` | 0 |
| `test_status` | 0 |
| `reject flag` | 0 |
| `n_with_replacement` | 0 |

## 11. Results readability diagnostics

The diagnostic uses the established convention: contiguous non-empty prose
blocks; headings, list items, Markdown table rows, fenced code, display math,
and figure-caption lines are excluded; sentences are split at Chinese
terminal punctuation and eligible terminal English punctuation; the
very-long threshold is `>240` characters.  The frozen Results roadmap is
included in the §4 diagnostic slice.

```text
RESULTS_PROSE_SENTENCE_COUNT_BEFORE = 117
RESULTS_PROSE_SENTENCE_COUNT_AFTER = 105
RESULTS_VERY_LONG_SENTENCE_COUNT_BEFORE = 3
RESULTS_VERY_LONG_SENTENCE_COUNT_AFTER = 3
RESULTS_MAX_SENTENCE_LENGTH_BEFORE = 575
RESULTS_MAX_SENTENCE_LENGTH_AFTER = 575
```

The unchanged maximum is in protected, information-dense Results material;
the reduction is from local redundancy removal rather than mechanical
sentence splitting.

## 12. Scientific execution guards

No tests or scientific commands were run for this bounded prose task.

```text
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
SECOND_ORDER_PROJECTION_RUN = 0
FIGURE_RERENDER = 0
figure_assets_changed = 0
scientific_assets_changed = 0
```

## 13. Final manuscript and repository checks

```text
body_prose_changed = 1 (Results prose only)
table_content_changed = 0
figure_assets_changed = 0
scientific_assets_changed = 0
```

The repository worktree still contains only this new freeze record plus the
four preserved untracked rendering archives before the documentation commit.
The manuscript remains external and is not staged.

```text
MANUSCRIPT_SHA_BEFORE = 53F30E4406BD0195AD097A1C425F3B5EC8A19048B5C1BADC429F6B673425901B
MANUSCRIPT_SHA_AFTER = 34A8F0D63BA93C30361FA16529F0AD1C1970E18AA74FE8FB55EE1C42A94CEB16
```

The documentation-only commit and push are recorded in the final repository
check performed after this file is staged.

```text
CH5_REFQ_SUBMISSION_EDIT_BATCH_D_RESULTS_PASS
```
