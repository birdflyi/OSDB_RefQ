# Chapter 5 RefQ C3 Correction Regeneration Planning Audit v1

审计日期：2026-08-25
Repository：`D:\github_repo\OSDB_RefQ`
Branch：`ch5-refq-repository-identity-correction-v1`
HEAD：`68054dceaebc14ecdf29ac9d0b209f28301fd7a4`

## 1. 目的与边界

本文件是 corrected P0 通过后的只读再生成依赖计划。它回答哪些现有
artifact 直接依赖 historical P0、哪些需要用 corrected P0 派生、哪些可在
不再生成的情况下保留，以及哪些正文/图表主张必须由人工复核。

本审计没有执行以下动作：

- 没有重跑 P0；
- 没有重跑 S1-S7；
- 没有重跑 GH-CoRE、network algorithms 或 raw external query；
- 没有渲染 Figure 1-4；
- 没有修改 historical freeze、任何 P0 或 supplemental output；
- 没有修改 manuscript、main branch 或 C4 artifact。

矩阵中的 `REGENERATE` 是未来获得授权后的动作，不是本次执行记录。
历史 artifact 仍然保留作为 v1 comparison baseline；它们不能在没有 corrected
派生结果的情况下被重新描述为 corrected-baseline evidence。

## 2. 已确认的输入状态

| 项目 | 当前证据 |
|---|---|
| historical P0 | `outputs/reference_quotient_p0_frozen/manifest.json`，status `PASS`，manifest SHA-256 `a3089fd8a6a58c0a15d2192a7b5f3388868ef0f1358c803be3aa4f27314c59f6` |
| corrected P0 | `outputs/reference_quotient_p0_corrected_v2/manifest.json`，status `PASS`，manifest SHA-256 `21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7` |
| P0 input scope | 两个 manifest 均记录 296 个 inputs、294 个 analysis seeds；两套 P0 均有 30 个 output files |
| correction scope | 10 个 directed edge pairs 删除，1 个 pair 的 weight 从 59 降为 2；所有变化均来自 Fireproof source `679889516` |
| RQ1 impact | `self_reference_ratio` 和 `external_reference_share` 的年龄关联 p-value 从 `0.070299` 变为 `0.043982`，跨过 nominal `p < 0.05` |
| RQ2 impact | RQ2a source top-50 50/50 且顺序不变；RQ2b target top-50 50/50 且顺序不变但数值份额变化；RQ2c communities `34 -> 35`，brokerage top-50 为 48/50 overlap |
| RQ3 impact | 数值 feature/effect-size 表发生 drift；uncorrected significance flips 为 0，FDR flips 为 0 |
| current decision | `C3_IMPACT_REQUIRES_EXPERIMENT_RERUN` |

## 3. 分类规则

`depends_on_P0?` 表示该 artifact 的当前内容或选择逻辑是否直接消费
P0 输出、P0 派生网络或固定于 P0 的对象集合。`affected?` 表示它是否会
因为 corrected P0 而改变数值、集合、解释资格或未来 corrected-baseline 用途。

| action | 含义 |
|---|---|
| `KEEP` | 当前 artifact 保持不变并作为历史归档或已验证稳定结果；不得覆盖或改写。 |
| `REGENERATE` | 未来从 corrected P0 v2 重新派生；应写入新的 versioned root，不得覆盖 v1。 |
| `REVIEW_ONLY` | 不需要在本计划中重新计算，但 corrected 表/图生成后必须人工复核措辞、数值、caption 或 section。 |

## 4. 再生成依赖矩阵

### 4.1 P0 与 S1-S7

| artifact | current_source | depends_on_P0? | affected? | action |
|---|---|---:|---:|---|
| historical P0 frozen package | `outputs/reference_quotient_p0_frozen/` 及 `chapter5-refq-freeze-v1.0` | NO（基准本体） | NO（作为 v1 archive） | `KEEP` |
| corrected P0 candidate package | `outputs/reference_quotient_p0_corrected_v2/` | NO（候选 P0 本体） | NO（已有 `PASS`，本计划不重跑） | `KEEP` |
| S1 evidence-universe tables | `supplemental/reference_quotient_v1/outputs/S1_evidence_universe/` 及 `v1_1_completion/outputs/S1_evidence_universe/` | YES | YES；retained Reference universe、edge-class counts 和 P0 reconciliation 随 corrected P0 改变 | `REGENERATE` |
| S2 weight/multiplicity sensitivity | `supplemental/reference_quotient_v1/outputs/S2_weight_sensitivity/` | YES | YES；RefQ edge weights/multiplicity 改变，包含 `59 -> 2` 的 directed pair | `REGENERATE` |
| S3 observation-boundary sensitivity | `supplemental/reference_quotient_v1/outputs/S3_observation_sensitivity/` 及 `v1_2_s3_reproducibility_patch/outputs/S3_observation_sensitivity_corrected/` | YES | YES；canonical network、nodes、edges、components 和 community summary 的输入图改变 | `REGENERATE` |
| S4 community stability | `supplemental/reference_quotient_v1/outputs/S4_community_stability/` | YES | YES；Louvain stability runs 依赖 corrected graph，现有 34-community baseline 不能直接作为 corrected result | `REGENERATE` |
| S5 brokerage stability | `supplemental/reference_quotient_v1/outputs/S5_brokerage_stability/` | YES | YES；brokerage values 与 top-50 membership 已改变 | `REGENERATE` |
| S6 figure-ready derivations | `supplemental/reference_quotient_v1/outputs/S6_figure_ready/` 及 `v1_1_completion/outputs/S6_figure_ready/` | YES | YES；`figure_ready_manifest_v1_1.json` 明确引用 historical P0 source files | `REGENERATE` |
| S7 fixed top-evidence composition | `supplemental/reference_quotient_v1/outputs/S7_top_evidence_composition/` 及 `v1_1_completion/outputs/S7_top_evidence_composition/` | YES | NO（当前固定 source/target/edge sets 与 affected Fireproof objects 零 overlap） | `KEEP` |
| S7 fixed-object definition and selection record | S7 fixed top source/target/edge definitions及现有 provenance records | YES | YES（仅需确认定义仍固定；若未来重新选择对象则不再适用） | `REVIEW_ONLY` |
| historical supplemental freeze manifest and archive | `supplemental/reference_quotient_v1/FINAL_FREEZE_MANIFEST.json`、`outputs/manifest.json` | YES | NO（作为历史 supplemental archive）；不能冒充 corrected baseline | `KEEP` |
| supplemental decision/freeze prose | `docs/ch5_refq_final_supplemental_human_decision_summary_v2.md`、`docs/ch5_refq_supplemental_final_freeze_report.md` | YES | YES（正文数字和 corrected applicability 仍指向 historical P0） | `REVIEW_ONLY` |

### 4.2 RQ1/RQ2/RQ3 P0 表

| artifact | current_source | depends_on_P0? | affected? | action |
|---|---|---:|---:|---|
| RQ1 descriptive statistics | `outputs/reference_quotient_p0_frozen/rq1_descriptive_statistics.csv` | YES | YES；总量、分布和 profile-derived summary 发生 drift | `REGENERATE` |
| RQ1 event/entity distribution tables | `rq1_event_type_distribution.csv`、`rq1_referenced_entity_distribution.csv`、`rq1_referencing_entity_distribution.csv` | YES | YES；8 个 event-type counts 及 entity distributions 改变 | `REGENERATE` |
| RQ1 project reference profiles | `rq1_project_reference_profiles.csv` | YES | YES；294 行中 Fireproof 行改变，且该表支撑后续 profile statistics | `REGENERATE` |
| RQ1 project-age association | `rq1_project_age_cross_sectional_association.csv` | YES | YES；两项 p-value 穿过 nominal threshold | `REGENERATE` |
| RQ2a complete source-role metrics | `rq2a_source_role_metrics.csv` | YES | YES；Fireproof source row 的 degree/strength 等数值改变 | `REGENERATE` |
| RQ2a source-role top-50 table | `rq2a_source_role_top50.csv` | YES | NO；当前文件 hash unchanged，集合和顺序均 50/50 unchanged | `KEEP` |
| RQ2b target category breakdown | `rq2b_target_category_type_breakdown.csv` | YES | YES；target rows/weights 的类别汇总改变 | `REGENERATE` |
| RQ2b target concentration | `rq2b_target_concentration.json` | YES | YES；top-1/top-10/top-50 shares 及 denominator 改变 | `REGENERATE` |
| RQ2b complete target-role metrics | `rq2b_target_role_metrics.csv` | YES | YES；10 个 target rows 删除，common rows 的 cumulative share 也改变 | `REGENERATE` |
| RQ2b target-role top-50 table | `rq2b_target_role_top50.csv` | YES | YES；集合/顺序虽稳定，但 `cumulative_weight_share` 等数值字段改变 | `REGENERATE` |
| RQ2c directed/undirected edge tables | `reference_quotient_cross_project_edges.csv`、`rq2c_undirected_view_edges.csv`、`rq2c_undirected_view_lcc_edges.csv` | YES | YES；10 个 cross-project pairs 删除，1 个 pair 减权，LCC edge set 改变 | `REGENERATE` |
| RQ2c community table | `rq2c_algorithmic_communities.csv` | YES | YES；algorithmic community count `34 -> 35` | `REGENERATE` |
| RQ2c structural summary | `rq2c_undirected_view_summary.json` | YES | YES；nodes, edges, weights, communities, modularity 和结构统计改变 | `REGENERATE` |
| RQ2c brokerage candidate table | `rq2c_structural_brokerage_candidates.csv` | YES | YES；network-derived betweenness values 改变 | `REGENERATE` |
| RQ2c brokerage top-50 table | `rq2c_structural_brokerage_top50.csv` | YES | YES；移除 `105944401`、`724712`，加入 `341631350`、`99919302` | `REGENERATE` |
| RQ3 seed role-aware features | `rq3_seed_role_aware_features.csv` | YES | YES；Fireproof fields 及 228 个 network-observed rows 的 betweenness 改变 | `REGENERATE` |
| RQ3 subdomain descriptive comparison | `rq3_subdomain_descriptive_comparison.csv` | YES | YES；mean/median/std 派生值发生改变 | `REGENERATE` |
| RQ3 Kruskal/FDR/effect-size table | `rq3_kruskal_fdr_effect_sizes.csv` | YES | YES；p-values/effect sizes 数值改变，虽无 significance/FDR decision flip | `REGENERATE` |

### 4.3 Figure 1-4 及 panel data

下列是 panel data 的未来再生成计划，不是本次 figure render 授权。所有
`S6` panel data 都必须把 source artifact 从 `outputs/reference_quotient_p0_frozen/`
切换到 `outputs/reference_quotient_p0_corrected_v2/`，并重新写入新的
corrected S6 versioned root。

| artifact | current_source | depends_on_P0? | affected? | action |
|---|---|---:|---:|---|
| Figure 1 panel data：evidence-universe flow、RQ1 composition、event/entity distributions | S6 `rq1_event_type_distribution_plot.csv`、`rq1_referenced_entity_distribution_plot.csv`、`rq1_referencing_entity_distribution_plot.csv`、以及 RQ1 flow tables | YES | YES；record/entity/event totals 和 age-association panel source 改变 | `REGENERATE` |
| Figure 1 panel data：RQ1 profiles/age association | S6 `rq1_profile_quantiles.csv`、`rq1_project_age_cross_sectional_association_plot.csv` | YES | YES；profile-derived quantiles 与 nominal p-value panel 改变 | `REGENERATE` |
| Figure 2 panel data：RQ2a source role | S6 `rq2a_source_role_metrics_plot.csv`、`rq2a_source_role_quantiles.csv`、`rq2a_source_role_ecdf_ccdf.csv` | YES | YES；complete source-role distribution 有 Fireproof drift；top-50 identity claim需复核 | `REGENERATE` |
| Figure 2 panel data：RQ2b target role/concentration | S6 `rq2b_target_role_metrics_plot.csv`、`rq2b_target_role_quantiles.csv` 及 concentration source | YES | YES；target denominator、observable rows 和 cumulative shares 改变 | `REGENERATE` |
| Figure 3 panel data：network/edge/community structure | S6 `edge_weight_ecdf_ccdf.csv`、`edge_weight_quantiles.csv`、`community_size_distribution.csv`、`structural_summary.csv` | YES | YES；network size、edge mass、community count 和 modularity source 改变 | `REGENERATE` |
| Figure 3 panel data：brokerage and robustness | S6 `brokerage_plot.csv`、`brokerage_top50_plot.csv`、`louvain_stability_plot.csv`、`brokerage_stability_plot.csv` | YES | YES；brokerage top-50 membership 改变；community/brokerage interpretation 也需复核 | `REGENERATE` |
| Figure 4 panel data：RQ3 descriptive/effect-size/FDR | S6 `rq3_subdomain_descriptive_comparison_plot.csv`、`rq3_kruskal_fdr_effect_sizes_plot.csv` | YES | YES；数值表改变，significance/FDR decision 目前保持不变 | `REGENERATE` |
| Figure 1 final rendered artifact | repository 中未发现可作为 corrected final 的 Figure 1 render；当前来源应为 corrected S6 panel data | YES | YES | `REGENERATE` |
| Figure 2 final rendered artifact | repository 中未发现可作为 corrected final 的 Figure 2 render；当前来源应为 corrected S6 panel data | YES | YES | `REGENERATE` |
| Figure 3 final rendered artifact | repository 中未发现可作为 corrected final 的 Figure 3 render；当前来源应为 corrected S6 panel data 和解释复核 | YES | YES | `REGENERATE` |
| Figure 4 final rendered artifact | repository 中未发现可作为 corrected final 的 Figure 4 render；当前来源应为 corrected S6 panel data | YES | YES | `REGENERATE` |

### 4.4 Main text claims 与 manuscript sections

仓库中没有发现独立的 `manuscript/`、Chapter 5 LaTeX 或 Word source；以下
section 名称按现有 RQ/figure 组织作依赖定位，不代表本次修改 manuscript。

| artifact | current_source | depends_on_P0? | affected? | action |
|---|---|---:|---:|---|
| RQ1 evidence-universe counts and composition claims | manuscript source 未在仓库中发现；现有 wording 记录见 `docs/ch5_refq_final_supplemental_human_decision_summary_v2.md` | YES | YES；observed/eligible/non-project/unresolved counts 改变 | `REVIEW_ONLY` |
| RQ1 project-age association claim | 同上；对应 `rq1_project_age_cross_sectional_association.csv` | YES | YES；self-reference/external-share p-value 由 `0.070299` 变为 `0.043982` | `REVIEW_ONLY` |
| RQ2a source-role distribution claim | 同上；对应 `rq2a_source_role_metrics.csv` | YES | YES；complete table 的 Fireproof row 改变 | `REVIEW_ONLY` |
| RQ2a source top-50 set/order claim | 同上；对应 hash-unchanged `rq2a_source_role_top50.csv` | YES | NO；50/50 overlap、顺序不变 | `KEEP` |
| RQ2b target concentration numeric claim | 同上；对应 `rq2b_target_concentration.json` 和 target-role tables | YES | YES；top-1/top-10/top-50 shares 改变 | `REVIEW_ONLY` |
| RQ2b target top-50 membership/order claim | 同上；集合和顺序稳定，但表内 share 数值改变 | YES | NO（若只宣称集合/顺序）；若报告 exact shares则受影响 | `REVIEW_ONLY` |
| RQ2c community-count/partition claim | 同上；对应 community table and structural summary | YES | YES；community count `34 -> 35` | `REVIEW_ONLY` |
| RQ2c brokerage candidate/top-50 claim | 同上；对应 brokerage candidate/top-50 tables | YES | YES；top-50 发生 2 removed / 2 added | `REVIEW_ONLY` |
| RQ3 exact effect-size/p-value claims | 同上；对应 RQ3 tables | YES | YES；numeric drift | `REVIEW_ONLY` |
| RQ3 significance/FDR conclusion | 同上；对应 `rq3_kruskal_fdr_effect_sizes.csv` | YES | NO；当前无 uncorrected 或 FDR decision flip，但需以 corrected table复核 | `KEEP` |
| P0 source-admission/identity-boundary wording | protocol `docs/freeze/ch5_refq_versioned_repository_identity_correction_protocol_v1.md` 与 future manuscript methods | YES | YES；Fireproof source observation boundary 已修正 | `REVIEW_ONLY` |
| Figure captions, in-text figure references, and result cross-references | manuscript source 未在仓库中发现；figure mapping 见 decision summary | YES | YES；Figures 1-4 的 panel values/interpretation 需同步 | `REVIEW_ONLY` |
| Chapter 5 evidence-universe/RQ1 methods and results section | manuscript source 未在仓库中发现 | YES | YES | `REVIEW_ONLY` |
| Chapter 5 RQ2a/RQ2b role and concentration sections | manuscript source 未在仓库中发现 | YES | YES（RQ2a headline ranking较稳定，complete metrics仍需复核） | `REVIEW_ONLY` |
| Chapter 5 RQ2c network/community/brokerage section | manuscript source 未在仓库中发现 | YES | YES | `REVIEW_ONLY` |
| Chapter 5 RQ3 statistical comparison section | manuscript source 未在仓库中发现 | YES | YES（数值需更新；结论目前稳定） | `REVIEW_ONLY` |
| Supplementary methods/results references to S1-S6 | `docs/ch5_refq_supplemental_final_freeze_report.md` 及 `docs/ch5_refq_final_supplemental_human_decision_summary_v2.md` | YES | YES；现有 prose 以 historical supplemental results 为依据 | `REVIEW_ONLY` |

## 5. 直接依赖 historical P0 的结论

### 5.1 直接依赖且需要再生成

以下 artifact 的当前 source 明确引用或等价消费
`outputs/reference_quotient_p0_frozen/`：

- S1-S6 的现有 output roots；
- RQ1 全部 P0 表；
- RQ2a complete metrics、RQ2b 全部 numeric tables、RQ2c 全部 network/structure/brokerage tables；
- RQ3 全部 feature、descriptive 和 statistical tables；
- S6 manifest 中列出的所有 P0-derived figure-ready tables；
- Figures 1-4 的 panel data。

这些 artifact 应从已通过的
`outputs/reference_quotient_p0_corrected_v2/` 派生，并使用新的 versioned
输出根。不得通过覆盖 historical v1 文件来完成更新。

### 5.2 不需要再生成但仍需保存

- historical P0 30-file package及其 manifest；
- historical supplemental S1-S7 archive；
- corrected P0 v2 package本身；
- RQ2a `source_role_top50.csv`，因为其当前内容 hash unchanged；
- S7 fixed-object composition，因为受影响 source/target/edge 与固定对象零 overlap；
- 仅陈述 RQ2a top-50 集合/顺序稳定的 claim；
- 仅陈述 RQ3 无 significance/FDR decision flip 的 claim，前提是 corrected table 已通过复核。

`KEEP` 不表示这些历史文件已经变成 corrected v2 文件；它表示它们应保持
不变，或其稳定性已经由现有 comparison evidence 证明。

## 6. 建议的未来执行顺序

1. 保持 historical P0、historical supplemental outputs、historical tag 和 manuscript 不变。
2. 使用现有 `outputs/reference_quotient_p0_corrected_v2/` 作为 corrected P0 source；本计划不重跑 P0。
3. 在新的 versioned supplemental root 中先派生 S1，再按 corrected network/role/graph dependencies 生成 S2、S3、S4、S5。
4. 在 S1-S5 依赖通过后生成 corrected S6 figure-ready tables和manifest；S6 manifest 必须记录 corrected P0 source hashes。
5. 保留 S7 当前 fixed-object composition；仅复核 fixed-object definition。若 fixed top objects 改变，S7 从 `KEEP` 转为 `REGENERATE`。
6. 以 corrected tables 为唯一新数值来源，执行正文 claims、section、caption 和 cross-reference 的 `REVIEW_ONLY` 人工复核。
7. corrected supplemental freeze 和 manuscript review 完成后，另行授权 Figure 1-4 panel render；本审计不渲染图。

## 7. 需要避免的错误依赖

- 不得把 historical S1-S6 的数字直接用于 corrected-baseline manuscript claims。
- 不得因为 RQ2a/RQ2b top-50 集合稳定，就保留包含旧 denominator 或 cumulative share 的完整表。
- 不得把 RQ2c community count `34` 或旧 brokerage top-50 当作 corrected result。
- 不得把 RQ3 “无显著性翻转”误写成“所有 RQ3 数值未变化”。
- 不得覆盖 `outputs/reference_quotient_p0_frozen/`、historical supplemental roots 或 historical tag。
- 不得在本计划阶段运行 C4、S1-S7、figure rendering 或 manuscript update。

## 8. 最终计划判断

当前 corrected P0 已通过，但 historical P0 直接派生的 S1-S6、RQ numeric
tables 和 Figure 1-4 panel data 不能全部视为 corrected-baseline artifacts。
S7 和少数稳定 claim 可以保留，但 RQ1 的 nominal significance crossing、
RQ2c 的 community/brokerage 变化以及所有 stale numeric tables 需要进入
后续授权流程。

```text
PLAN_DECISION = C3_IMPACT_REQUIRES_EXPERIMENT_RERUN
P0_RERUN_THIS_TASK = 0
S1_S7_RERUN_THIS_TASK = 0
FIGURE_RENDER_THIS_TASK = 0
MANUSCRIPT_MODIFIED_THIS_TASK = NO
HISTORICAL_FREEZE_MODIFIED_THIS_TASK = NO
```

## 9. 证据来源

- `outputs/reference_quotient_p0_frozen/manifest.json`
- `outputs/reference_quotient_p0_corrected_v2/manifest.json`
- `docs/freeze/ch5_refq_c3_scientific_impact_review_v1.md`
- `docs/freeze/ch5_refq_c3_execution_provenance_reconstruction_audit_v1.md`
- `docs/freeze/ch5_refq_versioned_repository_identity_correction_protocol_v1.md`
- `docs/freeze/ch5_refq_versioned_repository_identity_correction_dependency_matrix_v1.csv`
- `docs/ch5_refq_final_supplemental_human_decision_summary_v2.md`
- `docs/ch5_refq_supplemental_final_freeze_report.md`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/figure_ready_manifest_v1_1.json`
- `supplemental/reference_quotient_v1/v1_1_completion_manifest.json`
