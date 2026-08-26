# Chapter 5 RefQ C3.7-E 实现审查

## 1. 审查结论

本审查对应授权范围：只实现 corrected supplemental v2 的 S6 figure-ready 派生、版本化 manifest、通用 stage 输出序列化、SHA/字节数/行数闭包和测试。没有执行 corrected-data S1-S6/S7、P0、GH-CoRE、event rejoin、网络算法、绘图或稿件更新。

最终决策：

```text
C3_7E_S6_MANIFEST_IMPLEMENTATION_PASS_READY_FOR_HUMAN_REVIEW
```

该决策表示实现和只读前置检查已通过人工复核所需门禁，不表示 corrected supplemental scientific package 已生成或已达到 release-ready。真实 S1-S6 输出仍必须在单独授权下生成；S7 在本阶段保持 `NOT_EVALUATED`。

## 2. 基线与范围

| 项目 | 已核对结果 |
|---|---|
| repository | `D:\github_repo\OSDB_RefQ` |
| branch | `ch5-refq-repository-identity-correction-v1` |
| required base commit | `f3fe93c6e6ee544417b15dbf6eecb82ab79dd902` |
| base worktree | C3.7-E 修改前 clean |
| corrected P0 manifest SHA-256 | `21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7` |
| corrected P0 config SHA-256 | `e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658` |
| real v2 output root | 不存在，未创建 |

本轮修改仅在 `supplemental/reference_quotient_v2/` 和本审查文档内。以下保护路径无修改：

- `outputs/reference_quotient_p0_frozen/`
- `outputs/reference_quotient_p0_corrected_v2/`
- `supplemental/reference_quotient_v1/`
- `script/ch5_reference_quotient/`
- `script/build_dataset/repository_identity_provenance.py`
- `configs/ch5_reference_quotient_p0_v2.yaml`
- manuscript files

## 3. 历史 S6 派生面核对

历史主入口 `supplemental/reference_quotient_v1/scripts/run_supplemental.py` 的 `derive_figure_ready()` 明确产生 P0 stable-copy、profile/source/target quantiles、source ECDF/CCDF、edge-weight ECDF/CCDF、community size、structural summary、brokerage tables 和 S4/S5 stability plot tables。历史 v1.1 completion 的 `run_completion.py` 仅修正 structural summary 的扩展名和 figure-ready manifest 的完成格式，不能作为 corrected v2 的输入源。

### 3.1 corrected S6 的精确 20 项输出 inventory

| 输出 | v2 分类 | authoritative source |
|---|---|---|
| `rq1_referencing_entity_distribution_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq1_referenced_entity_distribution_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq1_event_type_distribution_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq1_project_age_cross_sectional_association_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq2a_source_role_metrics_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq2b_target_role_metrics_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq3_subdomain_descriptive_comparison_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq3_kruskal_fdr_effect_sizes_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq1_profile_quantiles.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq2a_source_role_quantiles.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq2a_source_role_ecdf_ccdf.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `rq2b_target_role_quantiles.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `edge_weight_ecdf_ccdf.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `edge_weight_quantiles.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `community_size_distribution.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `structural_summary.csv` | `RENAME_CORRECTED_AUTHORITY` | corrected P0 `rq2c_undirected_view_summary.json` |
| `brokerage_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `brokerage_top50_plot.csv` | `KEEP_SAME_DERIVATION` | corrected P0 |
| `louvain_stability_plot.csv` | `KEEP_SAME_DERIVATION` | corrected v2 S4 |
| `brokerage_stability_plot.csv` | `KEEP_SAME_DERIVATION` | corrected v2 S5 |

以下历史 artifacts 明确为 `DEPRECATED_DO_NOT_EMIT`，不会进入 corrected S6 scientific output set：

- `structural_summary.json`
- `figure_ready_manifest.json`
- `figure_ready_manifest_v1_1.json`

其中 corrected P0 的 `rq2c_undirected_view_summary.json` 是合法输入；被排除的是历史 S6 输出 `structural_summary.json`。corrected S6 的结构摘要权威是 `S6_figure_ready/structural_summary.csv`，由 corrected P0 JSON 转成一行 CSV，列名按 deterministic sorted order，未丢失标量字段。

## 4. corrected source map

### 4.1 corrected P0 authority

所有下列 source 必须来自 `outputs/reference_quotient_p0_corrected_v2/`，authority class 为 `CORRECTED_P0`，version 为 `corrected_p0_v2`：

```text
rq1_referencing_entity_distribution.csv
rq1_referenced_entity_distribution.csv
rq1_event_type_distribution.csv
rq1_project_age_cross_sectional_association.csv
rq1_project_reference_profiles.csv
rq2a_source_role_metrics.csv
rq2b_target_role_metrics.csv
rq3_subdomain_descriptive_comparison.csv
rq3_kruskal_fdr_effect_sizes.csv
reference_quotient_cross_project_edges.csv
rq2c_algorithmic_communities.csv
rq2c_undirected_view_summary.json
rq2c_structural_brokerage_candidates.csv
rq2c_structural_brokerage_top50.csv
```

### 4.2 corrected supplemental stage authority

这两个 source 只允许在未来 corrected v2 output root 下解析，authority class 为 `CORRECTED_SUPPLEMENTAL_V2`，version 为 `corrected_supplemental_v2`：

```text
supplemental/reference_quotient_v2/outputs/S4_community_stability/louvain_stability_runs.csv
supplemental/reference_quotient_v2/outputs/S5_brokerage_stability/brokerage_stability_runs.csv
```

S6 source map 要求 key 集合、路径、root、authority class 和 version 全部闭合。额外 source、key 与路径错配、历史 root、cross-root source 都 fail closed。没有从 v1、v1.1、v1.2 或历史输出进行 fallback discovery。

## 5. S6 transformation contract

实现文件：`supplemental/reference_quotient_v2/scripts/s6_figure_ready.py`。

1. **Stable copy**：读取 corrected P0 表并保持数据内容，只交给 deterministic CSV serializer。
2. **Quantiles**：对 numeric non-null values 保留 `min`、`q25`、`median`、`q75`、`max` 五个点，顺序和历史 `common.py` 一致。
3. **ECDF/CCDF**：先排序 numeric values；`cdf = rank / n`，`ccdf = (n - rank + 1) / n`，并保留历史逐观测行语义。
4. **Community size**：按 `community_id` 统计 `project_id` 行数，并在存在 `community_size` 时校验记录值与实际计数一致。
5. **Structural summary**：只读取 corrected P0 summary JSON 的 scalar object，转换为一行 `structural_summary.csv`。
6. **S4/S5 plot tables**：只从 corrected v2 的 S4/S5 run tables stable-copy，不在 S6 重新计算 network statistic。

`build_s6_figure_ready_bundle()` 是纯计算接口，不因 import 或构造 in-memory bundle 而写文件。真实 writer `serialize_s6_figure_ready_bundle()` 仅供未来执行使用；本轮只在 pytest temporary directory fixture 中调用。

## 6. figure-ready manifest v2

实现文件：`supplemental/reference_quotient_v2/scripts/s6_figure_ready.py`。

未来 manifest 路径为：

```text
supplemental/reference_quotient_v2/outputs/S6_figure_ready/figure_ready_manifest_v2.json
```

manifest schema 为 `figure_ready_manifest_v2`，每一个 20 项 scientific output entry 记录：

```text
output
output_sha256
output_bytes
row_count
transformation
source_artifacts[]
```

每一个 source record 记录：

```text
path
sha256
authority_class
root
version
```

manifest 还记录两个 machine-checkable `authority_roots`、deprecated output exclusion 和 `manifest_self_hash_not_embedded = true`。`validate_s6_manifest_sha_closure()` 对每一项校验 source SHA、output SHA、output bytes 和 serialized CSV row count，任一 mismatch 都 fail closed。manifest 本身不把自身 SHA 嵌入自身，避免循环闭包；写入后可以用 manifest 文件路径重新验证。

## 7. 通用 stage serialization

实现文件：`supplemental/reference_quotient_v2/scripts/stage_io.py`。

`write_stage_outputs()` 的行为：

- `pandas.DataFrame` 只写 deterministic CSV，`index=False`、LF line ending，并记录 row count。
- mapping 只写 deterministic UTF-8 JSON，sorted keys、固定 indentation 和末尾换行。
- stage 名称只接受 S1-S6，并映射到 `S1_evidence_universe` 至 `S6_figure_ready`。
- caller 必须明确提供 output root；历史 P0、corrected P0、历史 supplemental、source data 和 repository 内未声明 output root 均拒绝作为写目标。
- corrected v2 output parent 可以已经存在，但目标 stage directory 一旦存在就拒绝覆盖。
- 不调用 `shutil.rmtree`，不自动清理失败的 partial stage；失败后保留的 stage 需要人工审计。
- 返回 `StageReceipt`，其中包含 stage/status、implementation commit、input/output artifact records、parameters、runtime versions 和 completed timestamp。

`validate_output_artifact_records()` 对 output path 做 root containment 检查，并校验 SHA、字节数和 CSV 行数。malformed record、空记录集合、非法数值和类型错误统一转为 `StageIOError`。

## 8. corrected package manifest

实现文件：`supplemental/reference_quotient_v2/scripts/manifest.py`。

`build_corrected_package_manifest()` 只构造内存对象，不持久化真实 `supplemental/reference_quotient_v2/outputs/manifest.json`。schema 至少包括：

- package/schema version、package status、release status、implementation commit、branch；
- corrected P0 root、manifest/config paths 及 SHA；
- corrected aggregate root、strict identity policy 和 source admission rule；
- weight/multiplicity、random seed、S2 thresholds、S3 network authority；
- S4 seed contract、S5 k/seed/top-k contract 和 inclusion-frequency authority；
- S6 structural-summary authority 和 `figure_ready_manifest_v2.json` authority；
- S1-S6 stage receipts、runtime versions、historical comparison baseline；
- historical write audit/no-overwrite result；
- S7 enum status 和 `entry_point_used_as_authority = false`。

状态闭包为：

| 条件 | package status | release status |
|---|---|---|
| 任一 S1-S6 receipt 缺失或失败 | `STAGE_PACKAGE_INCOMPLETE` | `NOT_RELEASE_READY` |
| S1-S6 receipt 全部完成，S7=`NOT_EVALUATED` | `STAGE_PACKAGE_COMPLETE` | `NOT_RELEASE_READY` |
| S1-S6 receipt 全部完成，S7=`REGENERATE_REQUIRED` | `STAGE_PACKAGE_COMPLETE` | `NOT_RELEASE_READY` |
| S1-S6 receipt 全部完成，S7=`KEPT_FIXED_OBJECT` | `STAGE_PACKAGE_COMPLETE` | `RELEASE_READY` |

本轮没有读取或执行 S7 object/overlap gate，也没有给出 positive S7 result。

## 9. 只读 preflight 与验证结果

执行的 preflight 是 metadata/header/source-map 检查，不是 corrected P0 scientific table 的 S6 派生：

```text
C3_7E_INPUT_PREFLIGHT = PASS
headers_only = True
required_p0_source_count = 14
future_s4_s5_sources_resolved_under_v2 = True
historical_fallback_present = False
corrected_data_s6_run = False
network_corrected_data_run = 0
real_output_root_created = False
```

验证命令和结果：

```text
python -m pytest supplemental/reference_quotient_v2/tests -q
111 passed, 0 failed

scripts/*.py and tests/test_*.py py_compile
PASS

git diff --check
PASS
```

测试覆盖 temporary-directory S6 bundle、20 项 inventory、stable copy、quantile、ECDF/CCDF、community-size consistency、summary JSON 到 CSV、deprecated exclusion、v2 S4/S5 source、历史 root rejection、source/output SHA closure、no-overwrite、stage receipt、package status/S7 distinction 和 malformed-record fail-closed 行为。没有测试或创建真实 corrected supplemental output root。

## 10. 修改面与科学执行计数器

本轮实现文件：

- `supplemental/reference_quotient_v2/scripts/s6_figure_ready.py`，新增；
- `supplemental/reference_quotient_v2/scripts/stage_io.py`，新增；
- `supplemental/reference_quotient_v2/scripts/manifest.py`，扩展 package manifest builder/validator；
- `supplemental/reference_quotient_v2/tests/test_s6_figure_ready.py`，新增；
- `supplemental/reference_quotient_v2/tests/test_stage_io.py`，新增；
- `supplemental/reference_quotient_v2/tests/test_manifest_v2.py`，新增；
- 本文件。

计数器：

```text
P0_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
corrected_data_S1_run = NO
corrected_data_S2_run = NO
corrected_data_S3_run = NO
corrected_data_S4_run = NO
corrected_data_S5_run = NO
corrected_data_S6_run = NO
NETWORK_CORRECTED_DATA_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
scientific_logic_change_count = 0
G01_G20_authoritative_runtime_status = DESIGN_ONLY_NOT_EXECUTED
```

测试通过只说明实现契约、synthetic derivation 和边界校验可运行，不等同于 S1-S6 corrected-data scientific execution 已发生。

## 11. 已知限制与下一授权边界

1. corrected v2 的真实 `outputs/` 仍不存在，因此本轮不能证明真实 S4/S5 run table 的内容闭包，也不能提供真实 S6 output hashes。
2. S6 writer 和 package manifest builder 已实现，但没有在真实 output root 调用；真实 stage receipt、figure-ready manifest 和 package manifest 需留待授权执行阶段。
3. `S6` 只消费已生成的 corrected P0、S4、S5 artifact，不修复或重新计算上游科学逻辑。S1-S5 的运行时结果仍需分别通过其既定 gate。
4. `S7_status` 仅保留 schema/enum 语义，当前默认 `NOT_EVALUATED`，因此本审查不能宣告 release-ready。
5. 下一边界为 C3.7-F。除非取得新的明确授权，不得据此运行 corrected-data S1-S6、S7、figure render、manuscript update、P0 或 GH-CoRE。

## 12. 审查状态字段

```text
base_commit = f3fe93c6e6ee544417b15dbf6eecb82ab79dd902
S1_S5_regression = PASS (111-test implementation suite)
S6_implemented = YES
S6_exact_historical_derivation_inventory_verified = YES
S6_corrected_P0_only_source_contract = PASS
S6_v2_S4_S5_only_source_contract = PASS
S6_historical_fallback_present = NO
S6_structural_summary_authority = structural_summary.csv
deprecated_structural_summary_json_excluded = YES
S6_figure_ready_manifest_authority = figure_ready_manifest_v2.json
S6_source_SHA_closure_contract = PASS
S6_output_SHA_closure_contract = PASS
stage_serializer_implemented = YES
stage_no_overwrite_contract = PASS
existing_parent_output_root_allowed = YES
existing_same_stage_root_rejected = YES
package_manifest_builder_implemented = YES
package_manifest_schema_complete = PASS
S7_status_default = NOT_EVALUATED
C3_7E_INPUT_PREFLIGHT = PASS
G15_IMPLEMENTATION_PRECHECK = PASS
G16_IMPLEMENTATION_PRECHECK = PASS
G17_IMPLEMENTATION_PRECHECK = PASS
G20_IMPLEMENTATION_PRECHECK = PASS
supplemental_v2_outputs_root_created = NO
C3_7F_authorized = NO
recommended_next_phase = C3_7F
decision = C3_7E_S6_MANIFEST_IMPLEMENTATION_PASS_READY_FOR_HUMAN_REVIEW
```
