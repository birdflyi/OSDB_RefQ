# Chapter 5 RefQ C3.5 Corrected Baseline Regeneration Implementation Audit v1

审计日期：2026-08-26
Repository：`D:\github_repo\OSDB_RefQ`
Branch：`ch5-refq-repository-identity-correction-v1`
HEAD：`68054dceaebc14ecdf29ac9d0b209f28301fd7a4`

## 1. 审计范围

本文件是 C3.5 corrected-baseline regeneration implementation audit。审计对象
是现有 S1-S6 生成代码、配置、authority manifest、deprecated artifact 引用
和测试入口，目标是判断它们能否从
`outputs/reference_quotient_p0_corrected_v2/` 安全生成新的 corrected
supplemental baseline。

本审计是只读的，没有执行：

- P0；
- S1-S7；
- network algorithms；
- figure generation 或 rendering；
- manuscript 修改；
- historical P0 或 historical supplemental output 修改。

### 1.1 结论摘要

现有 supplemental v1 pipeline **不能直接安全地从 corrected P0 v2 再生成
S1-S6**。P0 v2 的核心 CLI/config/output-root 机制可以支持 corrected output，
但 supplemental 代码仍然将 historical v1 作为 canonical source，并且其
S1 input scan 没有执行 corrected repository-identity source admission。

当前阻断项为：

1. `run_supplemental.py` 将 P0、manifest、配置、raw aggregate、输出 root 和
   immutability audit 固定到 v1；
2. 现有 S1 raw scan 读取 v1 `repos_GH_CoRE_ref_node_agg`，RAW_USECOLS 不含
   `event_repo_id`、`expected_source_context_repo_id` 或
   `source_admission_status`，因此不能复现 corrected Fireproof admission boundary；
3. 当前 branch/clean-worktree gates 要求已经不存在的 supplemental branch，且
   output writer 会删除固定的 v1 output root；
4. S2/S4/S1 tests 和运行状态检查写死 historical counts、34 communities 和
   historical modularity；
5. S3 的主 v1 implementation 仍使用已被 reproducibility audit supersede 的
   graph-construction path；v1.2 patch 的 canonical input 也仍固定为 historical
   P0；
6. S5 的主 writer 仍输出 deprecated `brokerage_topk_frequency.csv`，而现有
   authority 是 v1.1 completion 生成的
   `brokerage_topk_inclusion_frequency.csv`；
7. S6 的主 writer 仍输出 deprecated `structural_summary.json`，而现有
   authority 是 CSV structural summary 和 v1.1 figure-ready manifest；
8. v1.1 completion script 会重新读取 v1 S5/S6 outputs，不能作为 corrected
   S5/S6 authority generator 直接复用。

因此，C3.5 只产生 implementation patch requirements，不授权任何 regeneration。

## 2. Versioning 与不可变边界

### 2.1 当前与建议路径

| 用途 | 路径 | 状态 |
|---|---|---|
| historical P0 source | `outputs/reference_quotient_p0_frozen/` | 只读、不可覆盖 |
| corrected P0 source | `outputs/reference_quotient_p0_corrected_v2/` | 已有 `PASS`，本审计只读 |
| historical supplemental | `supplemental/reference_quotient_v1/outputs/` 及 v1.1/v1.2/v1.3 additive roots | 只读、保留 provenance |
| 当前代码默认 supplemental output | `supplemental/reference_quotient_v1/outputs/` | 不可用于 corrected run；存在 overwrite 风险 |
| 建议 corrected supplemental output | `supplemental/reference_quotient_v2/outputs/` | 建议的新 versioned root；本次未创建 |
| 建议 corrected supplemental config | `supplemental/reference_quotient_v2/configs/supplemental_v2_corrected.yaml` | 建议的新配置；本次未创建 |

建议的 corrected root 下应至少包含：

```text
supplemental/reference_quotient_v2/outputs/
  S1_evidence_universe/
  S2_weight_sensitivity/
  S3_observation_sensitivity/
  S4_community_stability/
  S5_brokerage_stability/
  S6_figure_ready/
  manifest.json
```

S7 fixed-object composition 不属于本次 S1-S6 corrected regeneration；若继续
保留旧 S7，必须单独记录 fixed-object selection 未改变。

### 2.2 风险等级

- `CRITICAL`：当前代码会消费错误的 historical source、覆盖 historical root，或无法保证 corrected identity/authority；未 patch 前不得运行。
- `HIGH`：计算逻辑部分可复用，但历史 gate、硬编码 invariant、deprecated output 或依赖边界会使结果不能作为 corrected baseline。
- `MEDIUM`：核心逻辑可复用，但需要配置、manifest、命令入口或验证器适配。
- `LOW`：只需文档/metadata 适配；不代表可绕过上游 `CRITICAL/HIGH` blocker。

## 3. Implementation compatibility matrix

| artifact | current code path | historical dependency? | corrected compatibility? | required patch? | risk level |
|---|---|---:|---:|---|---|
| corrected P0 output-root mechanism | `configs/ch5_reference_quotient_p0_v2.yaml`；`script/ch5_reference_quotient/config.py:29-53`；`script/ch5_reference_quotient/pipeline.py:172-176` | NO（P0 v2 为 versioned candidate） | `YES` for P0 output-root resolution；`PARTIAL` for downstream consumers | supplemental must receive the v2 manifest/root explicitly and record corrected config/hash；不要让 supplemental 重新选择 v1 manifest | `MEDIUM` |
| P0 v2 identity contract | `configs/ch5_reference_quotient_p0_v2.yaml:24-44`；`script/ch5_reference_quotient/pipeline.py:43-158`；`script/ch5_reference_quotient/source_observation.py:18-52` | NO for candidate execution；metadata仍引用 historical seed boundary | `YES` for corrected P0 outputs；supplemental 当前未调用该 contract | S1 adapter must consume corrected provenance-enriched relation/aggregate or corrected P0-derived admitted records；must carry `event_repo_id`, expected source context and admission status into S1 evidence logic | `CRITICAL` |
| supplemental v1 global roots and constants | `supplemental/reference_quotient_v1/scripts/run_supplemental.py:34-39` | YES；`CANONICAL`、`P0_CONFIG`、`P0_MANIFEST` 和 `OUTPUT` 全部固定 v1 | `NO` | add explicit `p0_root`, `p0_manifest`, `p0_config`, `source_root` and `output_root` inputs；default must fail closed rather than point to frozen v1 | `CRITICAL` |
| supplemental branch/clean-worktree gate | `run_supplemental.py:60-70` | YES；要求 `ch5-refq-supplemental-evidence-v1` 和 v1 allowed dirty paths | `NO` on current correction branch | replace historical branch/merge-base gate with approved correction-branch policy and scoped output-root write allowlist；historical roots must be read-only | `HIGH` |
| S1 P0/seed/evidence loader | `run_supplemental.py:53-80` | YES；读取 historical `analysis_seed_manifest_294.csv` 和 v1 aggregate directory | `NO` for corrected source admission | load corrected manifest and corrected seed boundary from v2; resolve evidence path from v2 config, not `read_p0_config_paths()` hard-coded v1 path; validate manifest hash and 294 seeds | `CRITICAL` |
| S1 raw input columns and source admission | `run_supplemental.py:96-143`；`RAW_USECOLS` omits event repository provenance | YES；uses filename/seed context and v1 aggregate fields | `NO` | use corrected v2 relation/aggregate schema or a P0-consistent admitted-record adapter; require `event_repo_id == expected_source_context_repo_id` before membership/eligibility; reject source mismatch before S1 counts | `CRITICAL` |
| S1 fixed-object side effect | `run_supplemental.py:178-205` and `run_single_streaming_pass()` writes S7 files | YES；top source/target/edge sets read from historical P0 | `PARTIAL` | separate S1 from S7 execution; do not write S7 during S1-S6 run; if S7 is audited, read fixed selections from an immutable S7 record rather than reselecting from corrected top tables | `HIGH` |
| S1 flow and validation | `run_supplemental.py:263-301`；`validation["exact_p0_reconcile"]` | YES；expected counts are historical constants `3,748,078`, `1,586,117`, `1,447,073`, `139,044` | `NO` | derive expected values from corrected P0 manifest/output summaries or corrected S1 contract; preserve `REFERENCE_RECORD`/`AGGREGATED_EDGE_WEIGHT` and `EDGE_COUNT` labels; do not hard-code historical totals | `HIGH` |
| S2 threshold sensitivity | `run_supplemental.py:306-321` | YES for canonical comparison constants | `PARTIAL`；algorithm reads `weight` and can consume corrected edges after root patch | replace hard-coded threshold-1 values and modularity with corrected `rq2c_undirected_view_summary.json`; assert P0-specific `weight == evidence multiplicity` where applicable; keep threshold-before-undirected-collapse semantics | `HIGH` |
| S2 weight/multiplicity semantics | `run_supplemental.py:309-314`；`script/ch5_reference_quotient/edge_table.py:41-50`；`docs/ch5_refq_weight_multiplicity_contract_audit.md` | historical implementation assumes current P0 equality | `PARTIAL`；corrected P0 currently still uses `weight == multiplicity` | add explicit schema/semantic validation for corrected directed edges; never treat undirected `directed_edge_count` as Reference-record multiplicity; preserve `REFERENCE_RECORD_MULTIPLICITY` wording | `HIGH` |
| S3 main v1 view generator | `run_supplemental.py:324-345`；`common.undirected_edges_from_directed()` | YES；v1 output and historical canonical assumptions | `NO` as authoritative corrected S3 | replace with shared canonical `script.ch5_reference_quotient.network_views.directed_to_undirected_edges` plus `analyze_undirected_view`; preserve registry/seed insertion order and seed `20260731`; write new S3 root | `CRITICAL` |
| S3 reproducibility patch | `supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/patch_s3.py:12-18,75-130` | YES；`CANONICAL` and `OLD_S3` are historical; snapshot checks target v1 roots | `PARTIAL`；graph construction logic is compatible, path and comparison logic are not | parameterize corrected P0 root, corrected output root and corrected expected summary; compare against corrected P0 and retain historical comparison as metadata only; do not overwrite v1.2 outputs | `HIGH` |
| S4 community stability | `run_supplemental.py:366-400` | YES；reads historical RQ2c edge/registry and hard-codes 34 communities/modularity | `PARTIAL` after root patch | read corrected network edge/registry; compare canonical seed to corrected P0 structural summary; replace `34`/`0.7973095950243088` constants; preserve 50 Louvain seeds and partition-sensitive interpretation | `HIGH` |
| S5 brokerage stability graph | `run_supplemental.py:403-435` | YES; reads historical network and brokerage candidate table | `PARTIAL` after root patch | read corrected graph/registry/candidate table; compare `(k=500, seed=20260731)` to corrected candidate output; preserve unweighted approximate betweenness (`weight=None`) and canonical tie-break rules | `HIGH` |
| S5 brokerage frequency writer | `run_supplemental.py:436-449` | YES; emits v1 deprecated file semantics | `NO` as current authority | make `brokerage_topk_inclusion_frequency.csv` the only human-use frequency authority, derived from the corrected `brokerage_rank_stability.csv`; retain per-run table separately and label it non-authoritative | `HIGH` |
| S5 v1.1 frequency completion | `supplemental/reference_quotient_v1/v1_1_completion/run_completion.py:240-260` | YES；reads `V1/outputs/S5_brokerage_stability/brokerage_rank_stability.csv` | `NO` without path patch | parameterize input ranking and output root; never read historical S5 when creating corrected frequency; record source SHA and closure `run_count * top_k` | `HIGH` |
| S6 main figure-ready generator | `run_supplemental.py:451-494` | YES；all P0-derived entries use `CANONICAL` historical root | `NO` | parameterize corrected source root; require every source artifact to exist under corrected P0 or current corrected S4/S5 root; fail on cross-root mixing; write corrected source SHA for every entry | `CRITICAL` |
| S6 structural-summary authority | `run_supplemental.py:488` | YES；writes `structural_summary.json` | `NO` as current authority | emit `structural_summary.csv` directly; create a new corrected manifest such as `figure_ready_manifest_v2.json`; do not use deprecated JSON as source or authority | `HIGH` |
| S6 v1.1 format completion | `supplemental/reference_quotient_v1/v1_1_completion/run_completion.py:263-297` | YES；copies v1 deprecated JSON and v1 manifest | `NO` as corrected generator | replace copy-from-v1 behavior with corrected P0 structural summary derivation; keep deprecated JSON only in historical provenance; source manifest must point to corrected P0 and corrected S4/S5 | `HIGH` |
| S6 v1.1 figure-ready manifest | `supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/figure_ready_manifest_v1_1.json` | YES；manifest entries explicitly point to `outputs/reference_quotient_p0_frozen/...` | `NO` as corrected authority | generate a new manifest in the proposed v2 root with corrected source paths, corrected SHA-256 values, transformations and row counts; no in-place manifest edit | `CRITICAL` |
| supplemental v1 config | `supplemental/reference_quotient_v1/configs/supplemental_v1.yaml:1-14` | YES；`canonical_manifest` is historical and package root is v1 | `PARTIAL`；threshold/seed parameters are reusable | create v2 config containing corrected P0 manifest/root, corrected output root, corrected relation/source paths, weight contract and authority paths; keep v1 config immutable | `HIGH` |
| v1.3 S1 unit-label authority | `supplemental/reference_quotient_v1/v1_3_weight_multiplicity_contract_patch/contract_patch_manifest.json` | YES；values and old/new paths are v1 values | `PARTIAL` semantically, not numerically | create corrected S1 flow in new root with `REFERENCE_RECORD` + `AGGREGATED_EDGE_WEIGHT` and `EDGE_COUNT` labels; record corrected values and source hashes; do not reuse v1.3 CSV as corrected data | `HIGH` |
| supplemental package manifest/report generation | `run_supplemental.py:500-580` and `v1_1_completion/run_completion.py:290-435` | YES；package names, parent commits, canonical manifest and report wording are v1-specific | `NO` without versioned metadata patch | write a corrected manifest/report with v2 package identity, corrected P0 manifest/config hashes, output hashes, source roots, authority map and no-overwrite audit; historical reports remain unchanged | `HIGH` |
| historical freeze manifest | `supplemental/reference_quotient_v1/FINAL_FREEZE_MANIFEST.json` | YES by definition | `NO` for mutation; `YES` as immutable comparison record | no patch and no write; corrected package must have its own manifest and must not edit the final freeze manifest | `LOW` |
| S1-S6 tests | `supplemental/reference_quotient_v1/tests/test_supplemental.py`；`v1_1_completion/tests/test_completion.py`；`v1_2_s3_reproducibility_patch/tests/test_s3_patch.py` | YES；tests use v1 paths and historical constants | `NO` | parameterize P0/output roots; derive expected values from corrected manifest/summary; add identity-admission, authority-path, deprecated-artifact exclusion and historical-root immutability tests | `HIGH` |
| S1→S6 orchestration | `run_supplemental.py:641-660` | YES；single v1 main writes all stages to one fixed output root | `PARTIAL`；order is nominally S1→S2→S3→S4→S5→S6 | separate stage inputs/outputs and dependency gates; ensure S1 does not silently write S7; require S1 success before S2/S3, graph outputs before S4/S5, and corrected S4/S5 before S6 | `HIGH` |

## 4. Hard-coded and deprecated reference inventory

### 4.1 Historical P0 paths

The following code/config paths directly hard-code or derive historical P0 paths:

- `run_supplemental.py:37-39`：`CANONICAL`、historical P0 config and manifest；
- `run_supplemental.py:75,197-199,309-310,327-329,369-370,406-412,457-488`：S1-S6 source tables all resolve through `CANONICAL`；
- `v1_1_completion/run_completion.py:19,21,61-65,100,149,293-297`：canonical seed/P0 and historical S2-S6 inputs；
- `v1_2_s3_reproducibility_patch/patch_s3.py:16,50-59,80-88`：historical P0 plus v1 supplemental snapshots；
- `supplemental_v1.yaml:3`：historical canonical manifest；
- `figure_ready_manifest.json` and `figure_ready_manifest_v1_1.json`：P0-derived source artifacts point to `outputs/reference_quotient_p0_frozen/...`；
- `tests/test_supplemental.py` and v1.1/S3 tests：historical output roots and historical structural constants。

### 4.2 Frozen supplemental paths

The current code also treats frozen supplemental files as active inputs rather than
immutable comparison records:

- v1.1 S5 frequency derives from `v1/outputs/S5_brokerage_stability/brokerage_rank_stability.csv`；
- v1.1 S6 format correction copies `v1/outputs/S6_figure_ready/structural_summary.json` and its v1 manifest；
- S6 plotting uses v1 S4/S5 stability tables when the output root is v1；
- v1.2 snapshots and compares v1 S1-S7 roots；
- v1.3 authority metadata points to v1 flow values and paths。

These references are valid historical provenance but invalid as corrected result
inputs unless the new manifest explicitly labels them as comparison-only.

### 4.3 Deprecated artifacts

The following must not become corrected human-use authority:

| artifact | existing status | corrected-run rule |
|---|---|---|
| `supplemental/reference_quotient_v1/outputs/S5_brokerage_stability/brokerage_topk_frequency.csv` | `DEPRECATED_SEMANTICS`；per-run membership rows | do not use as S5 inclusion frequency authority |
| `supplemental/reference_quotient_v1/outputs/S6_figure_ready/structural_summary.json` | `DEPRECATED_WRONG_EXTENSION`；CSV content under JSON extension | do not use as corrected S6 structural summary authority |
| `supplemental/reference_quotient_v1/outputs/S6_figure_ready/figure_ready_manifest.json` | historical source manifest | keep as archive; generate a new corrected manifest |
| `supplemental/reference_quotient_v1/outputs/S3_observation_sensitivity/` | superseded noncanonical Louvain construction | keep for provenance; corrected S3 must use the shared canonical view adapter |
| `supplemental/reference_quotient_v1/outputs/S1_evidence_universe/evidence_universe_flow.csv` | superseded unit-label presentation | keep for archive; corrected run must emit current corrected flow with explicit units |

## 5. S1-S6 dependency chain assessment

### 5.1 Intended chain

```text
corrected P0 v2 manifest/root
  -> corrected source-admitted evidence boundary
  -> S1 evidence universe and edge-class tables
  -> S2 weight/multiplicity sensitivity
  -> S3 corrected observation views
  -> corrected graph input
  -> S4 community stability + S5 brokerage stability
  -> S6 figure-ready derivations and source manifest
```

The current `main()` call order is superficially
`S1 -> S2 -> S3 -> S4 -> S5 -> S6`, but this is not yet a safe dependency chain:

- S1 reads historical raw aggregate files and writes S7 as a side effect;
- S2/S3/S4/S5 read the global hard-coded `CANONICAL`, not the output of a corrected
  input contract;
- S3's main v1 path does not use the authoritative corrected construction order;
- S5 emits a deprecated frequency file;
- S6 can mix P0 files with same-run S4/S5 tables and has a fallback from
  `CANONICAL` to `output`, which can hide a missing source;
- the manifest records historical source hashes and does not prove all source roots
  are corrected.

### 5.2 Required dependency gates before any future run

1. **Corrected source gate**：v2 P0 manifest `PASS`、config SHA、30 output hashes and
   corrected input references are recorded; historical P0 manifest is comparison-only。
2. **Identity gate**：every S1 retained source record satisfies the v2
   `event_repo_id == annotated_primary_github_repo_id` rule; the Fireproof mismatch
   cannot re-enter through filename or caller context。
3. **S1 contract gate**：flow, cross-tabs, eligible totals, units and edge-weight
   closure are generated from corrected inputs and do not use historical constants。
4. **S2/S3 graph gate**：S2 thresholds operate on directed `weight` before collapse;
   S3 uses the shared canonical conversion and deterministic node insertion order。
5. **S4/S5 authority gate**：S4 uses corrected graph and dynamic corrected canonical
   summary；S5 uses corrected brokerage candidates and its inclusion-frequency table
   is derived from the corrected ranking runs。
6. **S6 source gate**：every figure-ready entry has a corrected source path and SHA;
   no v1 frozen path, deprecated JSON summary or deprecated S5 frequency file appears
   as an authority source。
7. **No-overwrite gate**：all writes target the proposed v2 supplemental root; the
   historical P0 root and all v1 supplemental roots have zero bytes changed。

## 6. Existing audit lessons carried forward

### 6.1 Weight and multiplicity

The current operationalization uses one unit per retained eligible Reference record
on the directed RefQ edge, so current corrected P0 is expected to satisfy
`weight == multiplicity`. This is a P0-specific equality, not a universal graph
invariant. S2 must threshold directed analytical `weight` before undirected collapse.
After collapse, `directed_edge_count` counts directed edge-table rows and must not be
reported as Reference-record multiplicity.

### 6.2 S5 brokerage inclusion frequency

The authoritative human-use S5 frequency artifact is the aggregated
`brokerage_topk_inclusion_frequency.csv`, with `run_count`, `inclusion_count` and
`inclusion_frequency`, and closure against `run_count * top_k`. The old
`brokerage_topk_frequency.csv` is per-run membership and is deprecated. A corrected
run must derive the authoritative table from the corrected S5 ranking output, not
from historical v1 ranking rows.

### 6.3 S6 figure-ready authority

S6 is a derivation layer. Its manifest must record each source artifact, source
SHA-256, transformation and row count. The corrected authority must be a new
manifest whose P0-derived entries point to
`outputs/reference_quotient_p0_corrected_v2/`, whose S4/S5 entries point to the new
corrected supplemental root, and whose structural summary is CSV. Existing v1/v1.1
manifests remain historical records.

### 6.4 Repository identity provenance

The corrected P0 source-admission rule is not present in the current supplemental
raw scan. The scan's input schema omits the event repository identity fields and
uses the seed filename/aggregate context. This is the highest-risk scientific
compatibility issue: path parameterization alone would still allow the historical
Fireproof source contamination to re-enter S1 and all downstream supplements.

## 7. Required implementation patch set

Before any authorized corrected S1-S6 generation, the implementation needs at least:

1. Add explicit source/output configuration or CLI arguments for corrected P0 root,
   corrected P0 manifest/config, corrected relation/aggregate inputs and a new
   supplemental output root; remove historical defaults from executable paths。
2. Add strict root separation: v1 roots are read-only comparison inputs, never write
   targets; reject output roots equal to any historical root。
3. Replace the S1 v1 raw scan input boundary with the corrected provenance-enriched
   relation/aggregate boundary or a dedicated adapter that enforces source admission
   before membership and quotient eligibility。
4. Split S1 from S7 side effects and keep S7 fixed-object selection outside the
   corrected S1-S6 generation chain。
5. Replace hard-coded historical numeric checks with manifest-/corrected-summary-
   driven checks while retaining the semantic invariants for units, weights,
   multiplicity, seed counts and random seeds。
6. Make S3 use the shared canonical network-view construction and preserve the
   corrected deterministic node order；adapt v1.2 comparison logic to compare corrected
   outputs without writing v1.2 historical outputs。
7. Make S5 inclusion-frequency output authoritative and derived from corrected S5
   ranking runs；retain unweighted brokerage semantics and tie-breaking rules。
8. Make S6 emit CSV structural summary and a corrected figure-ready manifest with
   corrected source hashes；remove fallback behavior that silently mixes roots。
9. Parameterize tests and add checks for identity admission, corrected source hashes,
   deprecated-artifact exclusion, S1-S6 dependency order and historical-root
   immutability。
10. Generate a new corrected supplemental manifest/report that records implementation
    commit, corrected P0 manifest/config hashes, corrected source/output roots,
    authority map, runtime metadata and no-overwrite audit。

## 8. Final status

```text
C3_5_REGENERATION_STATUS = REGENERATION_NOT_SAFE_WITH_CURRENT_PIPELINE
REQUIRED_PRECONDITION = IMPLEMENTATION_PATCH_AND_READ_ONLY_VALIDATION
CORRECTED_P0_SOURCE = outputs/reference_quotient_p0_corrected_v2/
PROPOSED_CORRECTED_SUPPLEMENTAL_ROOT = supplemental/reference_quotient_v2/outputs/
P0_RERUN_THIS_AUDIT = 0
S1_S7_RERUN_THIS_AUDIT = 0
NETWORK_ALGORITHMS_RUN_THIS_AUDIT = 0
FIGURES_GENERATED_THIS_AUDIT = 0
MANUSCRIPT_MODIFIED_THIS_AUDIT = NO
HISTORICAL_OUTPUTS_MODIFIED_THIS_AUDIT = NO
```

No S1-S6 regeneration is authorized by this audit. The approved regeneration plan
can proceed only after the `CRITICAL` and `HIGH` implementation patches above are
reviewed and a separate execution authorization is recorded.

## 9. Evidence sources

- `docs/freeze/ch5_refq_c3_correction_regeneration_plan_v1.md`
- `docs/freeze/ch5_refq_c3_scientific_impact_review_v1.md`
- `docs/freeze/ch5_refq_versioned_repository_identity_correction_protocol_v1.md`
- `docs/freeze/ch5_refq_versioned_repository_identity_correction_dependency_matrix_v1.csv`
- `outputs/reference_quotient_p0_corrected_v2/manifest.json`
- `configs/ch5_reference_quotient_p0_v2.yaml`
- `script/ch5_reference_quotient/config.py`
- `script/ch5_reference_quotient/pipeline.py`
- `script/ch5_reference_quotient/source_observation.py`
- `script/ch5_reference_quotient/network_views.py`
- `supplemental/reference_quotient_v1/scripts/run_supplemental.py`
- `supplemental/reference_quotient_v1/configs/supplemental_v1.yaml`
- `supplemental/reference_quotient_v1/v1_1_completion/run_completion.py`
- `supplemental/reference_quotient_v1/v1_2_s3_reproducibility_patch/patch_s3.py`
- `supplemental/reference_quotient_v1/v1_1_completion/outputs/S6_figure_ready/figure_ready_manifest_v1_1.json`
- `docs/ch5_refq_weight_multiplicity_contract_audit.md`
- `docs/ch5_refq_weight_multiplicity_contract_patch_report.md`
- `docs/ch5_refq_supplemental_s3_reproducibility_patch.md`
- `docs/ch5_refq_supplemental_evidence_v1_1_material_completion_report.md`
- `docs/ch5_refq_supplemental_final_freeze_report.md`
