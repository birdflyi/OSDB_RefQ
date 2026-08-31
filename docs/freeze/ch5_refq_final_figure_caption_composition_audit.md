# Chapter 5 RefQ — Final Figure 1–4 Caption Composition Audit

## Decision

CH5_REFQ_FINAL_FIGURE_CAPTION_COMPOSITION_PASS

The four publication-facing captions below were composed from the accepted
V6 figures and frozen scientific authorities, then inserted into the sole
authoritative manuscript. No scientific value, body statement, table, figure
asset, or scientific output was changed.

## 1. Starting identity and scope

| Item | Value |
|---|---|
| Repository | D:/github_repo/OSDB_RefQ |
| Branch | ch5-refq-repository-identity-correction-v1 |
| repository_HEAD_before | fdf54c10173c42e01059981fb7229d99eb1a99cd |
| remote_HEAD_before | fdf54c10173c42e01059981fb7229d99eb1a99cd |
| Working tree before | Four pre-existing untracked V3/V4/V5/V6 ZIP archives only |
| Authoritative manuscript | C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md |
| Manuscript SHA before | 13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309 |
| Accepted figure root | figures/ch5_refq/p0v3_final_v6/ |
| Accepted figure decision | P0V3_FIGURE_RENDER_FINAL_ACCEPTED |

The manuscript is outside the repository. Its edit is therefore reported by
before/after SHA and is not represented as a tracked manuscript file in this
repository. Historical manuscript snapshots remain untouched.

## 2. Caption authority hierarchy

Caption composition followed this order:

1. accepted V6 rendered Figure 1–4 assets;
2. each V6 source_manifest.json;
3. docs/freeze/ch5_refq_p0v3_figure_rendering_final_acceptance.md;
4. corrected P0-v3 and corrected supplemental-v2 outputs;
5. the current authoritative manuscript;
6. docs/freeze/ch5_refq_three_way_reconciliation_audit.md;
7. figures/ch5_refq/p0v3_final_v6/captions_draft_v6.md only as a historical
   wording aid.

The V6 caption draft was not copied where it contained intermediate
presentation wording. In particular, its historical Figure 2 logarithmic-axis
sentence is not present in the manuscript-facing caption.

## 3. Final publication captions

### Figure 1 — RQ1

**图 1 Observable Reference evidence 与 project-mappable boundary。** (A) 294 个 analysis seed projects 的 Reference-record flow：从 3,748,078 条 scanned input records 经 source-admission，排除 120 条 out-of-seed records，保留 3,747,958 条 admitted source-observation records，并按 target membership 分为 1,586,047 条 project-mappable、1,686,729 条 non-project 和 475,182 条 unresolved records；(B) admitted-record universe 中八类 source event 的完整构成；(C) 各 event type 内 project-mappable、non-project 与 unresolved target 的比例。图中所有计数均为 Reference records；只有可唯一映射到项目的 project-mappable 子集进入 Project-level RefQN，外部或 non-project resource 不因此成为项目节点，图示也不等同于最终网络拓扑。

### Figure 2 — RQ2a/RQ2b

**图 2 Project-level RefQN 的 source/target role 视图（RQ2a/RQ2b）。** (A) 294 个 source-complete seed projects 的 out-degree CCDF，其中 out-degree 为每个 source project 指向的 unique target-project 数；(B) 同一 source 集合的 out-strength CCDF，其中 out-strength 为聚合的 cross-project RefQ weight；(C) observable targets 的 in-degree、in-strength 与 target coverage quantile profile，in-degree 为指向该 target 的 unique seed-source 数，in-strength 为其接收的聚合 cross-project RefQ weight，coverage 定义为 in-degree/294，Q1/Median/Q3/Max 标签分别为 in-degree 1/1/1/42、in-strength 1/2/5/3,430、coverage 0.34%/0.34%/0.34%/14.29%；(D) 以 138,974 条 cross-project weight 为分母的 target-weight Top-1、Top-10 与 Top-50 share（2.47%/16.00%/48.99%）。expanded targets 的 source behavior 未被完整观测，图中指标仅描述当前 seed-centered observed RefQN，不表示项目重要性或分布模型。

### Figure 3 — RQ2c

**图 3 一阶无向 RefQ 结构与 algorithmic modular neighborhood view（RQ2c）。** (A) 将 9,595 条 directed cross-project RefQ edges 忽略方向并合并 reciprocal project pairs 后得到的 \(U(G_{\mathrm{RefQ}})\) 结构摘要及 35 个 community sizes；完整节点域为 6,506，含 9,547 条无向边，LCC 为 6,367 个节点和 9,462 条无向边，canonical Louvain partition 为 35 个 algorithmic communities（modularity=0.7969220043681785）；(B) canonical seed-centered observed、seed-only induced 与 multi-seed target 三种 observation-boundary views 在 LCC coverage、average clustering 和 modularity 上的并列比较，各指标使用独立刻度；(C) 50 次 seed runs 的 community count、modularity 与 ARI-to-canonical 敏感性，seed 20260731 作为确定性 reference realization。该图是一阶无向结构视图；community labels 是当前图与 modularity objective 下的算法分区，不表示稳定的真实社区或 DBMS taxonomy。

### Figure 4 — RQ3

**图 4 两种 label mode 下的 observed subdomain variation 与 FDR-bounded role/structure comparison（RQ3）。** (A–D) 按 category 展示 self-reference ratio、external-reference share、non-project share 与 comment-reference density 的 descriptive mean/median；filled circle/square 分别表示 include_mixed 的 mean/median，open circle/square 分别表示 exclude_mixed_or_multilabel 的 mean/median。(E) 展示各 feature 的 epsilon-squared，圆点与三角分别表示 include_mixed 与 exclude_mixed_or_multilabel，filled/open marker 分别表示 BH-FDR reject/not reject。include_mixed 下通过 FDR 的 feature 为 out_degree、out_strength、in_degree、in_strength、local_clustering 与 project_age_years_at_2023_end，exclude_mixed_or_multilabel 下无 feature 通过；因此不存在 cross-mode robust feature，结果应解释为 label-mode-sensitive，category labels 也不等同于算法社区或因果机制。

## 4. Caption scientific closure

| Figure | Panels verified | Scientific authority | Caption numeric closure | Semantic closure | Internal/provenance language | Status |
|---|---|---|---|---|---|---|
| 1 | A flow; B eight-category source composition; C event-type target membership | V6 Figure 1 source manifest; S1 evidence-universe flow and membership files | PASS (3,748,078 → 3,747,958; 1,586,047 + 1,686,729 + 475,182) | PASS (Reference-record units and quotient-eligibility boundary explicit) | None | PASS |
| 2 | A out-degree CCDF; B out-strength CCDF; C target quantiles; D concentration | V6 Figure 2 source manifest; S6 role files; P0 target concentration | PASS (quantile labels, 42/294 coverage, Top-1/10/50 shares and 138,974 denominator) | PASS (source-complete seeds separated from source-incomplete expanded targets) | None | PASS |
| 3 | A structure/community sizes; B observation-boundary metrics; C seed sensitivity | V6 Figure 3 source manifest; P0 RQ2c summary; S3/S4/S6 files | PASS (9,595/9,547; 6,506; 6,367/9,462; 35; modularity) | PASS (first-order undirected view and algorithmic partition limitation explicit) | None | PASS |
| 4 | A–D descriptive means/medians; E epsilon-squared and BH-FDR status | V6 Figure 4 source manifest; S6 RQ3 files | PASS (both label modes and six include-mixed FDR features; none in exclude mode) | PASS (label-mode-sensitive, descriptive-vs-inferential boundary explicit) | None | PASS |

## 5. Stale-provenance-language audit

The four manuscript-facing caption blocks contain zero occurrences of:

V3, V4, V5, V6, render, renderer, rendering, QA, manifest, source_manifest,
log-scale experiment, human visual review, raw-value label, connector alpha,
determinism, DPI, and SHA.

The immutable V6 draft remains historical provenance and retains its
intermediate logarithmic-axis sentence; that sentence was deliberately not
copied. It does not block the current caption closure.

## 6. Manuscript insertion locations

No image placeholders were present in the authoritative Markdown manuscript,
so the following publication caption blocks were inserted without fabricating
local image paths:

| Figure | Section / heading | Placement |
|---|---|---|
| 1 | §4.1.1 “引用类型分布特征与 Reference evidence composition” | Immediately after the opening admitted-record paragraph and before item 1 (current line 381) |
| 2 | §4.2 “Project-level RefQN 的角色化结构视图” | Immediately after the role-separation paragraph and before §4.2.0 (current line 505) |
| 3 | §4.2c “无向派生结构视图” | Immediately after the Louvain/sensitivity paragraph and before Table 4.6e (current line 573) |
| 4 | §4.3 “DBMS 子领域差异的局部性与非均质性” | Immediately after the section-opening methods paragraph and before §4.3.1 (current line 606) |

Actual image path and page-layout embedding remains a downstream Word/LaTeX
composition operation; the inserted blocks are the prose-authority captions.

## 7. Exact manuscript diff

The external manuscript changed only by four additions. No existing sentence,
table row, heading, citation, or equation was replaced or deleted. The exact
added lines are the four caption blocks in Section 3 of this record, beginning
with “图 1”, “图 2”, “图 3”, and “图 4” respectively.

Measured scope:

    manuscript_files_changed = 1
    body_prose_changed = 0
    table_content_changed = 0
    caption_blocks_added = 4

Removing the four added caption blocks in memory reconstructs the exact
pre-edit SHA 13C36E377AA4EA329CF96825F09D93466925D86FCEC15636D53E7ABDBE080309,
confirming that no other manuscript content changed. The manuscript SHA after
insertion is:

4CD0D743ED6B17D0DE7FB4D566296CC97664271F56014C19F2FEA0B34EF890DD

## 8. Figure and scientific immutability verification

The accepted V6 root contained 36 files before and after composition. The
publication asset hashes remained:

| Asset | SHA-256 |
|---|---|
| Figure 1 SVG | 63b5a581e65ef305ea7a3fefd1e952e297a799e6f4d6fbb278df6e05b6b74d24 |
| Figure 1 PDF | 88de1c8c6bf62d8246492662f17a98a678bd2306aabccce465b6ffeab15f3229 |
| Figure 1 PNG | 1b30d76b37f171103b0d7f1e803cae1146b163b3e7dcdc1573cb1099c6c8ec5e |
| Figure 2 SVG | 36f07513c7227261706966ba568475d68269ff8a03ad44b50f78daf06a7f956b |
| Figure 2 PDF | 762136aae28f520532318308723aa343b5878565745143d59bd6ea904bf262b0 |
| Figure 2 PNG | f2a86d2d8706415a7723892245eef31eb7c6b5b62a693b4142aed7f3cddf4311 |
| Figure 3 SVG | b1bba74418b268985e90b7be0696d125fea02b1e6b9522fb8bb759eb0f57cb50 |
| Figure 3 PDF | 6ab0a57e25485a68ec343fc84b1b00c1851ebc21265bf6fe9b9e396c5ff6be7d |
| Figure 3 PNG | 94d7952e6f00f74f11969c83652bd1379d426b734041f5a1890f0f982a22e22f |
| Figure 4 SVG | 2a4a486ce9aff1cb7da19c07776495db9574d73f8967f1ef27657fedbc047695 |
| Figure 4 PDF | 212d30c35bf3bfc625cbfc5be0f008d789df000cbde23442951d9792eafcf42e |
| Figure 4 PNG | 4d92b97743dd2671f1711a6c025b372dea7d754d55ca0286ceccda5909d14503 |
| V6 render manifest | 469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da |

git diff -- figures/ch5_refq/p0v3_final_v6 outputs supplemental was empty.
The four pre-existing V3/V4/V5/V6 ZIP archives remained untracked and were not
staged.

## 9. Scientific and execution guards

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
    SECOND_ORDER_PROJECTION_RUN = 0
    FIGURE_RERENDER = 0
    figure_assets_changed = 0
    scientific_assets_changed = 0

## 10. Final composition status

    FIGURE1_CAPTION_CLOSURE = PASS
    FIGURE2_CAPTION_CLOSURE = PASS
    FIGURE3_CAPTION_CLOSURE = PASS
    FIGURE4_CAPTION_CLOSURE = PASS
    FIGURE_CAPTION_COUNT = 4
    DUPLICATE_FIGURE_CAPTION_COUNT = 0
    MISSING_FINAL_CAPTION_COUNT = 0
    STALE_RENDER_LANGUAGE_COUNT = 0
    BROKEN_CAPTION_NUMBERING_COUNT = 0
    manuscript_files_changed = 1
    body_prose_changed = 0
    table_content_changed = 0
    figure_assets_changed = 0
    scientific_assets_changed = 0

The accepted Figure 1–4 figures now have one corresponding final caption each,
mapped to RQ1, RQ2a/RQ2b, RQ2c, and RQ3 respectively. The composition task is
closed with no scientific or presentation-authority change.
