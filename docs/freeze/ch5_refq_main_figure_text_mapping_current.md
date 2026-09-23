# Chapter 5 RefQ — Current Main Figure–Text–Asset Mapping

## Mapping identity

```text
MAPPING_BASE_MANUSCRIPT_REVISION = MS-R05
MAPPING_BASE_MANUSCRIPT_SHA = 30491279BC31CC5012042F72E3BA8159DCF182CECEEB62EFF5C865C78B059B22
MAPPING_SCIENTIFIC_BASELINE = P0-v3
MAPPING_CREATED_FROM = existing frozen assets and existing authority records
SCIENTIFIC_RECOMPUTATION = 0
FIGURE_RERENDER = 0
REGISTER_SCOPE = MAIN_PAPER_FIGURES_1_TO_4_ONLY
```

The immutable manuscript snapshot is
`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/versions/MS-R05_BOUNDED_SEMANTIC_EDITORIAL_30491279.md`.
CURRENT was verified byte-identical at the same SHA. Caption text below is
copied from that snapshot. This register maps, but does not replace,
manuscript text.

The common P0-v3 scientific baseline is recorded by
`outputs/reference_quotient_p0_corrected_v3/manifest.json`
(SHA-256 `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`)
and the final supplemental manifest
(SHA-256 `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`).

## Current render authority

Figures 1–3 use `figures/ch5_refq/p0v3_final_v6/`. Figure 4 uses the
terminology-corrected derivative `figures/ch5_refq/p0v3_final_v6_e01_eta_label/`,
whose parent is V6. The original V6 manifest SHA-256 is
`469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da`;
the E01 manifest SHA-256 is
`8ae373659a94846ffe4b945969cd149701474fdf4c71eb4709276a9d43da3050`.

### Figure 1

```text
FIGURE_ID = Figure 1
MAIN_OR_SUPPLEMENT = MAIN
MANUSCRIPT_SECTION = §4.1
MANUSCRIPT_BODY_REFERENCE_ANCHORS = no separate prose cross-reference found; caption is the figure anchor (snapshot line 379)
MS_R05_CAPTION_ANCHOR = snapshot line 379
PANEL_COUNT = 3
PANEL_IDENTITIES = A, B, C
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
RENDER_MANIFEST_SHA256 = 469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/main/figure1_evidence_universe/source_manifest.json
SOURCE_MANIFEST_SHA256 = 540a608bf8d263032bbe15221f7bf0c0d380f7fcf6c05c312f012c94845b0be0
SCIENTIFIC_SEMANTIC_AUTHORITY = P0-v3; source manifest identifies corrected P0-v3 and supplemental P0-v3 S1/S6 inputs
SCIENTIFIC_BASELINE_REFERENCE = outputs/reference_quotient_p0_corrected_v3/manifest.json; supplemental/reference_quotient_v2/outputs_p0v3/
PARENT_RENDER_AUTHORITY = none recorded
CURRENT_STATUS = MAPPED_HASH_VERIFIED
KNOWN_PROVENANCE_DEBT = source manifest render lineage predates MS-R04; this register supplies the current text link
MAINTENANCE_TRIGGER = a change to Figure 1 identity/caption/body anchor, panel contract, asset, render authority, or source provenance
```

```text
SVG_RELATIVE_PATH = main/figure1_evidence_universe/figure1_evidence_universe.svg
SVG_SHA256 = 63b5a581e65ef305ea7a3fefd1e952e297a799e6f4d6fbb278df6e05b6b74d24
PDF_RELATIVE_PATH = main/figure1_evidence_universe/figure1_evidence_universe.pdf
PDF_SHA256 = 88de1c8c6bf62d8246492662f17a98a678bd2306aabccce465b6ffeab15f3229
PNG_RELATIVE_PATH = main/figure1_evidence_universe/figure1_evidence_universe.png
PNG_SHA256 = 1b30d76b37f171103b0d7f1e803cae1146b163b3e7dcdc1573cb1099c6c8ec5e
```

**CURRENT_CAPTION_TEXT**

> **图 1 Observable Reference evidence 与 project-mappable boundary。** (A) 294 个 analysis seed projects 的 Reference-record flow：从 3,748,078 条 scanned input records 经 source-admission，排除 120 条 out-of-seed records，保留 3,747,958 条 admitted source-observation records，并按 target membership 分为 1,586,047 条 project-mappable、1,686,729 条 non-project 和 475,182 条 unresolved records；(B) admitted-record universe 中八类征引实体类型的完整构成；(C) 各 event type 内 project-mappable、non-project 与 unresolved target 的比例。图中所有计数均为 Reference records；只有可唯一映射到项目的 project-mappable 子集进入 Project-level RefQN，外部或 non-project resource 不因此成为项目节点，图示也不等同于最终网络拓扑。

| PANEL_ID | SHORT_SEMANTIC_ROLE | MS_R05_CAPTION_MATCH | RENDERED_ASSET_MATCH |
|---|---|---|---|
| A | Reference-record admission flow and target-membership partition | YES | YES |
| B | Complete source-side referencing-entity-type composition | YES | YES |
| C | Target-membership shares within event type | YES | YES |

### Figure 2

```text
FIGURE_ID = Figure 2
MAIN_OR_SUPPLEMENT = MAIN
MANUSCRIPT_SECTION = §4.2 RQ2a/RQ2b/RQ2c
MANUSCRIPT_BODY_REFERENCE_ANCHORS = §4.2 opening line 508; source interpretation line 514; target interpretation lines 540 and 542
MS_R05_CAPTION_ANCHOR = snapshot line 510
PANEL_COUNT = 4
PANEL_IDENTITIES = A, B, C, D
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
RENDER_MANIFEST_SHA256 = 469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/main/figure2_source_target_roles/source_manifest.json
SOURCE_MANIFEST_SHA256 = 441d02592d8d90574802ecf8a43b78ee2b0a35bb54f9028886054c02cfa4dbca
SCIENTIFIC_SEMANTIC_AUTHORITY = P0-v3; source/target roles and quantile/concentration definitions are drawn from frozen P0-v3 and supplemental P0-v3 S6 authorities
SCIENTIFIC_BASELINE_REFERENCE = outputs/reference_quotient_p0_corrected_v3/manifest.json; supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/
PARENT_RENDER_AUTHORITY = none recorded
CURRENT_STATUS = MAPPED_HASH_VERIFIED
KNOWN_PROVENANCE_DEBT = source manifest render lineage predates MS-R04; this register supplies the current text link
MAINTENANCE_TRIGGER = a change to Figure 2 identity/caption/body anchor, panel contract, asset, render authority, or source provenance
```

```text
SVG_RELATIVE_PATH = main/figure2_source_target_roles/figure2_source_target_roles.svg
SVG_SHA256 = 36f07513c7227261706966ba568475d68269ff8a03ad44b50f78daf06a7f956b
PDF_RELATIVE_PATH = main/figure2_source_target_roles/figure2_source_target_roles.pdf
PDF_SHA256 = 762136aae28f520532318308723aa343b5878565745143d59bd6ea904bf262b0
PNG_RELATIVE_PATH = main/figure2_source_target_roles/figure2_source_target_roles.png
PNG_SHA256 = f2a86d2d8706415a7723892245eef31eb7c6b5b62a693b4142aed7f3cddf4311
```

**CURRENT_CAPTION_TEXT**

> **图 2 Project-level RefQN 的 source/target role 视图（RQ2a/RQ2b）。** (A) 294 个 source-complete seed projects 的 out-degree CCDF；(B) 同一 source 集合的 out-strength CCDF。(C) observable targets 的 in-degree、in-strength 与 target coverage quantile profile；coverage 分母为 294 个 seed sources，Q1/Median/Q3/Max 标签分别为 1/1/1/42、1/2/5/3,430 和 0.34%/0.34%/0.34%/14.29%。(D) 以 cross-project RefQ total weight 138,974 为分母的 target-weight Top-1、Top-10 与 Top-50 share（2.47%/16.00%/48.99%）。这些指标描述当前 seed-centered observed RefQN，不表示项目重要性或分布模型。

| PANEL_ID | SHORT_SEMANTIC_ROLE | MS_R05_CAPTION_MATCH | RENDERED_ASSET_MATCH |
|---|---|---|---|
| A | Source-role out-degree CCDF | YES | YES |
| B | Source-role out-strength CCDF | YES | YES |
| C | Observable-target in-degree, in-strength, and coverage quantiles | YES | YES |
| D | Target-weight Top-1/10/50 concentration | YES | YES |

### Figure 3

```text
FIGURE_ID = Figure 3
MAIN_OR_SUPPLEMENT = MAIN
MANUSCRIPT_SECTION = §4.2 RQ2c
MANUSCRIPT_BODY_REFERENCE_ANCHORS = no separate prose cross-reference found; caption is the figure anchor (snapshot line 565)
MS_R05_CAPTION_ANCHOR = snapshot line 565
PANEL_COUNT = 3
PANEL_IDENTITIES = A, B, C
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
RENDER_MANIFEST_SHA256 = 469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/main/figure3_undirected_structure/source_manifest.json
SOURCE_MANIFEST_SHA256 = 0d429da458042135777a17c1b449ded48b52106a51effcded6f93b7844fa46a2
SCIENTIFIC_SEMANTIC_AUTHORITY = P0-v3; first-order direction-ignored summary, observation-boundary sensitivity, and seed sensitivity use frozen P0-v3/S3/S4/S6 inputs
SCIENTIFIC_BASELINE_REFERENCE = outputs/reference_quotient_p0_corrected_v3/manifest.json; supplemental/reference_quotient_v2/outputs_p0v3/
PARENT_RENDER_AUTHORITY = none recorded
CURRENT_STATUS = MAPPED_HASH_VERIFIED
KNOWN_PROVENANCE_DEBT = source manifest render lineage predates MS-R04; this register supplies the current text link
MAINTENANCE_TRIGGER = a change to Figure 3 identity/caption/body anchor, panel contract, asset, render authority, or source provenance
```

```text
SVG_RELATIVE_PATH = main/figure3_undirected_structure/figure3_undirected_structure.svg
SVG_SHA256 = b1bba74418b268985e90b7be0696d125fea02b1e6b9522fb8bb759eb0f57cb50
PDF_RELATIVE_PATH = main/figure3_undirected_structure/figure3_undirected_structure.pdf
PDF_SHA256 = 6ab0a57e25485a68ec343fc84b1b00c1851ebc21265bf6fe9b9e396c5ff6be7d
PNG_RELATIVE_PATH = main/figure3_undirected_structure/figure3_undirected_structure.png
PNG_SHA256 = 94d7952e6f00f74f11969c83652bd1379d426b734041f5a1890f0f982a22e22f
```

**CURRENT_CAPTION_TEXT**

> **图 3 一阶无向 RefQ 结构与 algorithmic modular neighborhood view（RQ2c）。** (A) \(U(G_{\mathrm{RefQ}})\) 的结构摘要及 35 个 algorithmic communities 的规模分布。(B) canonical seed-centered observed view、seed-only induced view 与 multi-seed target view 的 LCC coverage、average clustering 和 modularity 比较，各指标使用独立刻度。(C) 50 次 seed runs 的 community count、modularity 与 ARI-to-canonical 敏感性；seed 20260731 为 deterministic reference realization。该图是一阶无向结构视图，community labels 不表示稳定的真实社区或 DBMS taxonomy。

| PANEL_ID | SHORT_SEMANTIC_ROLE | MS_R05_CAPTION_MATCH | RENDERED_ASSET_MATCH |
|---|---|---|---|
| A | Undirected structural summary and algorithmic community-size distribution | YES | YES |
| B | Metrics across the three declared observation-boundary views | YES | YES |
| C | Fifty-seed community-count, modularity, and ARI sensitivity | YES | YES |

### Figure 4

```text
FIGURE_ID = Figure 4
MAIN_OR_SUPPLEMENT = MAIN
MANUSCRIPT_SECTION = §4.3 RQ3
MANUSCRIPT_BODY_REFERENCE_ANCHORS = no separate prose cross-reference found; caption and §4.3 RQ3 results anchor (snapshot line 598)
MS_R05_CAPTION_ANCHOR = snapshot line 598
PANEL_COUNT = 5
PANEL_IDENTITIES = A, B, C, D, E
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6_e01_eta_label/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6_e01_eta_label/render_manifest_v6_e01_eta_label.json
RENDER_MANIFEST_SHA256 = 8ae373659a94846ffe4b945969cd149701474fdf4c71eb4709276a9d43da3050
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6_e01_eta_label/main/figure4_rq3_comparison/source_manifest.json
SOURCE_MANIFEST_SHA256 = c06767bb0c8200eef4648b03235d92c2e2dfd6d8364ed0167d9fff42e1f42059
SCIENTIFIC_SEMANTIC_AUTHORITY = P0-v3 RQ3 descriptive comparison and Kruskal-Wallis/BH-FDR outputs; no new analysis
SCIENTIFIC_BASELINE_REFERENCE = outputs/reference_quotient_p0_corrected_v3/manifest.json; supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/
PARENT_RENDER_AUTHORITY = figures/ch5_refq/p0v3_final_v6/main/figure4_rq3_comparison/
E01_DELTA = terminology-only display-label correction
SCIENTIFIC_RECOMPUTATION = 0
DATA_CHANGE = 0
GEOMETRY_CHANGE = 0
PANEL_STRUCTURE_CHANGE = 0
SCALE_CHANGE = 0
CURRENT_STATUS = MAPPED_HASH_VERIFIED_PROVENANCE_CLOSED
FIGURE4_HISTORICAL_PROVENANCE_DEBT = CLOSED_BY_SUPERSEDING_PROVENANCE_RECORD
FIGURE4_PROVENANCE_CLOSURE_PENDING = NO
FIGURE4_PROVENANCE_CLOSURE_DOCUMENT = docs/freeze/ch5_refq_figure4_eta_label_provenance_closure.md
KNOWN_PROVENANCE_DEBT = predecessor V6 terminology and hashes remain preserved as historical provenance; current estimator identity is closed by the superseding record
MAINTENANCE_TRIGGER = a change to Figure 4 identity/caption/body anchor, panel contract, asset, render authority, or source provenance
```

```text
SVG_RELATIVE_PATH = main/figure4_rq3_comparison/figure4_rq3_comparison.svg
SVG_SHA256 = 6ec08f8462bb13f46395678a5bfb1b5e753377399d5cfa612f85fd273b34e17a
PDF_RELATIVE_PATH = main/figure4_rq3_comparison/figure4_rq3_comparison.pdf
PDF_SHA256 = daf4f9c486b19f229d0d13586cfceaba774bf7212466d7174877c57f07307c0c
PNG_RELATIVE_PATH = main/figure4_rq3_comparison/figure4_rq3_comparison.png
PNG_SHA256 = 6a279ae45570c06e745db65d3b14503b30f2ad98daac5c64dd8611a082fc44ea
```

**CURRENT_CAPTION_TEXT**

> **图 4 两种 label mode 下的 observed subdomain variation 与 FDR-bounded role/structure comparison（RQ3）。** (A–D) 展示四项 Reference composition 指标的 category-level mean/median；circle/square 区分 mean/median，filled/open 区分 include_mixed 与 exclude_mixed_or_multilabel。(E) 展示 rank eta-squared（\(\eta_H^2\)）及 BH-FDR status；圆点与三角区分两种 label mode，filled/open marker 表示 reject/not reject。正文与表 4.8 解释 mode-sensitive inferential result；category labels 不等同于算法社区或因果机制。

| PANEL_ID | SHORT_SEMANTIC_ROLE | MS_R05_CAPTION_MATCH | RENDERED_ASSET_MATCH |
|---|---|---|---|
| A | Reference-composition category mean/median, first feature | YES | YES |
| B | Reference-composition category mean/median, second feature | YES | YES |
| C | Reference-composition category mean/median, third feature | YES | YES |
| D | Reference-composition category mean/median, fourth feature | YES | YES |
| E | Rank eta-squared with BH-FDR status by label mode | YES | YES |

Figure 4 terminology lineage is closed by
`docs/freeze/ch5_refq_figure4_eta_label_provenance_closure.md`. MS-R04 and E01
use `rank eta-squared` / `η_H²`; the frozen `epsilon_squared` result field is
the legacy schema identifier for the same estimator, `(H-k+1)/(n-k)` with
negative estimates truncated at zero. E01 changes only the displayed label.
The historical V6 terminology and hashes remain preserved in their original
records; they are not current-facing authorities.

```text
FIGURE4_HISTORICAL_PROVENANCE_DEBT = CLOSED_BY_SUPERSEDING_PROVENANCE_RECORD
FIGURE4_PROVENANCE_CLOSURE_PENDING = NO
FIGURE4_PROVENANCE_CLOSURE_DOCUMENT = docs/freeze/ch5_refq_figure4_eta_label_provenance_closure.md
CURRENT_STATUS = MAPPED_HASH_VERIFIED_PROVENANCE_CLOSED
FIGURE4_SCIENTIFIC_MISMATCH = NO
```

## Current mapping closure

```text
FIGURE1_MANUSCRIPT_REFERENCE_RESOLVED = YES
FIGURE1_CAPTION_RESOLVED = YES
FIGURE1_PANEL_STRUCTURE_RESOLVED = YES
FIGURE1_CURRENT_AUTHORITY_ROOT_RESOLVED = YES
FIGURE1_ASSET_HASHES_VERIFIED = YES
FIGURE1_RENDER_MANIFEST_RESOLVED = YES
FIGURE1_SOURCE_MANIFEST_RESOLVED = YES
FIGURE1_SCIENTIFIC_BASELINE_RESOLVED = YES

FIGURE2_MANUSCRIPT_REFERENCE_RESOLVED = YES
FIGURE2_CAPTION_RESOLVED = YES
FIGURE2_PANEL_STRUCTURE_RESOLVED = YES
FIGURE2_CURRENT_AUTHORITY_ROOT_RESOLVED = YES
FIGURE2_ASSET_HASHES_VERIFIED = YES
FIGURE2_RENDER_MANIFEST_RESOLVED = YES
FIGURE2_SOURCE_MANIFEST_RESOLVED = YES
FIGURE2_SCIENTIFIC_BASELINE_RESOLVED = YES

FIGURE3_MANUSCRIPT_REFERENCE_RESOLVED = YES
FIGURE3_CAPTION_RESOLVED = YES
FIGURE3_PANEL_STRUCTURE_RESOLVED = YES
FIGURE3_CURRENT_AUTHORITY_ROOT_RESOLVED = YES
FIGURE3_ASSET_HASHES_VERIFIED = YES
FIGURE3_RENDER_MANIFEST_RESOLVED = YES
FIGURE3_SOURCE_MANIFEST_RESOLVED = YES
FIGURE3_SCIENTIFIC_BASELINE_RESOLVED = YES

FIGURE4_MANUSCRIPT_REFERENCE_RESOLVED = YES
FIGURE4_CAPTION_RESOLVED = YES
FIGURE4_PANEL_STRUCTURE_RESOLVED = YES
FIGURE4_CURRENT_AUTHORITY_ROOT_RESOLVED = YES
FIGURE4_ASSET_HASHES_VERIFIED = YES
FIGURE4_RENDER_MANIFEST_RESOLVED = YES
FIGURE4_SOURCE_MANIFEST_RESOLVED = YES
FIGURE4_SCIENTIFIC_BASELINE_RESOLVED = YES

MAIN_MAPPING_CLOSED = YES
E0_COUNT = 0
E1_COUNT = 0
E2_COUNT = 3
INFO_COUNT = 2
```

The remaining E2 items carried forward from FIG-P00 are historical Phase 2-B
design status, the older migration matrix's scaffold-oriented role, and
analysis-stage/supplementary-figure namespace ambiguity. Figure 4's specific
provenance debt is closed by the superseding record above. These remaining
items do not indicate current manuscript-to-render scientific mismatch.
