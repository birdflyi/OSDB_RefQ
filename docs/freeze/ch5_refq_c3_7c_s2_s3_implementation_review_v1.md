# Chapter 5 RefQ C3.7-C
# Corrected Supplemental v2 S2/S3 实现审计 v1

审计日期：2026-08-26
仓库：`D:\github_repo\OSDB_RefQ`
分支：`ch5-refq-repository-identity-correction-v1`
基线提交：`23b36a14273be7dd97520cbcbb54a9dae5e8852f`

本任务只实现 corrected supplemental v2 的 S2 weight sensitivity 和 S3 observation sensitivity。没有执行 corrected-data S2/S3，没有执行全量 S1，没有写 scientific output，也没有修改 P0、历史 artifacts、共享 P0/network 代码、figure 或 manuscript。

## 1. 基线与修改范围

基线门禁通过：

```text
branch = ch5-refq-repository-identity-correction-v1
HEAD = 23b36a14273be7dd97520cbcbb54a9dae5e8852f
worktree = clean before implementation
baseline tests = 64 passed, 0 failed
```

本提交修改/新增：

```text
supplemental/reference_quotient_v2/configs/supplemental_v2_corrected.yaml
supplemental/reference_quotient_v2/scripts/paths.py
supplemental/reference_quotient_v2/scripts/s2_weight_sensitivity.py
supplemental/reference_quotient_v2/scripts/s3_observation_sensitivity.py
supplemental/reference_quotient_v2/tests/test_s2_weight_sensitivity.py
supplemental/reference_quotient_v2/tests/test_s3_observation_sensitivity.py
docs/freeze/ch5_refq_c3_7c_s2_s3_implementation_review_v1.md
```

未修改：

```text
outputs/reference_quotient_p0_frozen/
outputs/reference_quotient_p0_corrected_v2/
supplemental/reference_quotient_v1/
script/ch5_reference_quotient/
script/build_dataset/repository_identity_provenance.py
configs/ch5_reference_quotient_p0_v2.yaml
source data
historical tag
manuscript
```

## 2. corrected-P0 输入 preflight

执行的是只读 metadata/header preflight，不是 S2/S3 scientific run。preflight 验证了：

```text
corrected P0 manifest status = PASS
corrected P0 manifest SHA-256 = 21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7
corrected P0 config SHA-256 = e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658
corrected P0 root = outputs/reference_quotient_p0_corrected_v2
S2 directed edge file exists and has required headers
node registry exists and has project_id
analysis seed manifest exists and has repo_id
canonical RQ2c edge/LCC/community/summary authorities exist
all inspected files resolve inside corrected P0 root
random_seed = 20260731
brokerage_sample_size = 500
```

结果：

```text
C3_7C_INPUT_PREFLIGHT = PASS
headers_only = true
corrected_data_S2_run = NO
corrected_data_S3_run = NO
network_corrected_data_run = 0
event_rejoin_performed = NO
```

S2/S3 的未来 load-contract 入口只从 corrected P0 root 读取 `reference_quotient_cross_project_edges.csv`、`reference_quotient_node_registry.csv` 和 `analysis_seed_manifest_294.csv`。历史 P0、历史 supplemental 和 v1.2 additive output 不属于 executable authority。

## 3. S2 实现

实现模块：[s2_weight_sensitivity.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s2_weight_sensitivity.py)

### 3.1 输入契约

directed cross-project edge 输入至少必须含有：

```text
source_project_id
target_project_id
weight
```

如果存在，还会校验：

```text
multiplicity
is_self_loop
```

当前 P0 operationalization 的约束为：

```text
source_project_id != target_project_id
weight 为 finite positive integral
weight == multiplicity（当 multiplicity 存在时）
is_self_loop == false（当字段存在时）
```

`weight == multiplicity` 仅表示当前 P0 的 Reference-record multiplicity operationalization，不被提升为一般图论不变量。node registry 的 `project_id` 必须非空、唯一，并按输入顺序完整保留。

### 3.2 阈值语义

v2 配置新增：

```yaml
s2_directed_weight_thresholds: [1, 2, 5, 10]
brokerage_sample_size: 500
```

阈值列表强制为正整数、唯一、严格递增，并保持授权的 `1, 2, 5, 10`。每个阈值先执行：

```text
retain directed edge row iff weight >= threshold
```

然后才调用共享 `directed_to_undirected_edges()`。因此 threshold `2` 表示 directed project-pair row 的 analytical weight 至少为 2，不能先合并 opposite directed rows 后按 summed undirected weight threshold。

每个 threshold 都传入同一个完整 node registry。阈值升高时 edge-observed nodes、components、LCC coverage 和 isolates 可以变化，但 node domain 不缩小。

### 3.3 共享 network authority

S2 使用未经修改的：

```text
script/ch5_reference_quotient/network_views.py:directed_to_undirected_edges
script/ch5_reference_quotient/network_views.py:analyze_undirected_view
```

没有使用历史 `common.py`、历史 `undirected_edges_from_directed()` 或历史 `structural_summary()`，也没有重新实现 DG2G 或 Louvain。对“无边但有 isolates”的 NetworkX 退化输入，v2 只增加了边界 fallback；非空边网络仍全部经过共享 authority。

### 3.4 S2 future output contract

`build_future_s2_output_tables()` 只返回内存对象，不写文件。contract 包含：

```text
edge_weight_sensitivity.csv
threshold_1_undirected_edges.csv
threshold_2_undirected_edges.csv
threshold_5_undirected_edges.csv
threshold_10_undirected_edges.csv
```

敏感性表保留 threshold、directed edge/weight retained、weight share、undirected edge count 以及共享 `analyze_undirected_view()` 的 canonical structural fields。没有写入或硬编码历史数值 `9557`、`6376`、`9472` 或旧 modularity。

## 4. S3 实现

实现模块：[s3_observation_sensitivity.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s3_observation_sensitivity.py)

S3 使用同一 corrected-P0 directed cross-project edge、完整 node registry 和 294-seed manifest，定义且只定义以下三个 first-order view：

| view | directed edges | node domain | node order |
|---|---|---|---|
| `CANONICAL_SEED_CENTERED_OBSERVED` | 全部 corrected cross-project RefQ edges | 完整 corrected P0 node registry | registry order |
| `SEED_ONLY_INDUCED` | source 和 target 都在 seed set | 全部 analysis seeds，包括 isolates | seed manifest order |
| `MULTI_SEED_TARGET_VIEW` | target 在 multi-seed target set | seeds UNION multi-seed targets | registry order 过滤后的顺序 |

multi-seed target 的定义是：在 corrected directed edge table 中，具有至少两个不同 `source_project_id` 的 `target_project_id`。没有引入 shared-target projection、二阶耦合或 `X*X^T`。

每个 view 都执行：

```text
directed view
  -> shared directed_to_undirected_edges()
  -> shared analyze_undirected_view()
```

node IDs 在传入 network authority 前已物化为有序 tuple，不使用无序 Python set 作为 node domain。所有 view 都传入配置的 `random_seed = 20260731` 和 `brokerage_sample_size = 500`；weighted Louvain 与 unweighted approximate brokerage 均由共享 authority 执行。

### 4.1 S3 future output contract

`build_future_s3_output_tables()` 只生成内存 DataFrame，不写文件。输出 contract 包含：

```text
observation_boundary_sensitivity.csv
canonical_seed_centered_observed_undirected_edges.csv
canonical_seed_centered_observed_lcc_edges.csv
canonical_seed_centered_observed_communities.csv
seed_only_induced_undirected_edges.csv
seed_only_induced_lcc_edges.csv
seed_only_induced_communities.csv
multi_seed_target_view_undirected_edges.csv
multi_seed_target_view_lcc_edges.csv
multi_seed_target_view_communities.csv
```

## 5. 动态 parity gate

实现了但没有调用 corrected-data parity gate：

```text
assert_s2_threshold_one_matches_corrected_p0()
assert_s3_canonical_view_matches_corrected_p0()
```

S2 gate 动态读取 corrected P0 的 `rq2c_undirected_view_edges.csv` 和 `rq2c_undirected_view_summary.json`，比较 threshold 1 的 canonical edge table 和 structural metrics。S3 gate 动态读取 corrected P0 的 canonical undirected edges、LCC edges、algorithmic communities、node registry 和 summary，比较 node domain/order、edges、LCC、community membership 及 summary metrics。

浮点比较只使用明确的绝对容差 `1e-12`；没有硬编码 community count `34` 或 `35`、modularity、LCC 或 edge 数值。gate 的存在不代表本轮 runtime gate 已 PASS，因为本轮禁止在 corrected data 上调用 compute 或 parity gate。

## 6. 合成网络测试

S2 测试覆盖：

```text
directed threshold before undirected collapse
opposite directed edge weight summation
directed_edge_count != Reference-record multiplicity
threshold 2 semantics
fixed node domain and increased isolates
self-loop rejection
weight/multiplicity equality
strict threshold validation
dynamic random_seed/brokerage config validation
no historical numeric constants
no output root creation
```

S3 测试覆盖：

```text
three exact view names
canonical all-edge definition
seed-only induced edge definition and all-seed node domain
multi-seed target >= 2 unique source projects
filtered registry node order for multi-target view
shared network authority identity
deterministic node insertion and repeated output
random seed and brokerage sample propagation
all future output schemas
no historical/v1.2 authority
no output root creation
```

`NETWORK_FIXTURE_TESTS = 7`，这些测试中的 network algorithm 调用全部只作用于小型合成图；`NETWORK_CORRECTED_DATA_RUN = 0`。

## 7. 测试结果与执行隔离

测试命令：

```text
venv\Scripts\python.exe -m pytest supplemental/reference_quotient_v2/tests -q
```

结果：

```text
tests_collected = 84
tests_passed = 84
tests_failed = 0
S1_regression = PASS
```

其中 baseline 为 64/64；本轮新增 S2/S3 测试后完整 v2 suite 为 84/84。测试只有既有 pandas dependency deprecation warnings，没有 failure。

工作树中不存在：

```text
supplemental/reference_quotient_v2/outputs/
```

本轮没有调用 `load_corrected_p0_s2_inputs()` 或 `load_corrected_p0_s3_inputs()`，也没有调用两个 corrected-data parity gate；它们仅作为未来 C3.7D/C4 的 load/validate contract 实现。

## 8. 已知限制与下一边界

1. 本轮 preflight 是 corrected P0 manifest/config/header 只读检查，不是 corrected edge table 的行级计算。
2. 本轮没有生成 S2 threshold 数值、S3 observation 数值、Louvain community 结果或 brokerage 结果。
3. B3 的两遍输入漂移保护是逻辑 boundary signature，不是逐 pass 的 cryptographic content lock；未来 C3.7-F/C4-S1 仍需在科学运行前完成 294/294 corrected aggregate candidate hash closure。
4. 空边但有 isolates 的共享 NetworkX 退化异常由 v2 wrapper 处理；非空边网络仍直接经过共享 `network_views.py` authority，未修改共享代码。

执行计数：

```text
corrected_data_S2_run = NO
corrected_data_S3_run = NO
full_data_S1_run = NO
P0_RUN = 0
S1_SCIENTIFIC_RUN = 0
S2_SCIENTIFIC_RUN = 0
S3_SCIENTIFIC_RUN = 0
S4_S7_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
G01_G20_authoritative_runtime_status = DESIGN_ONLY_NOT_EXECUTED
scientific_logic_change_count = 0
C3_7D_authorized = NO
C4_authorized = NO
```

## 9. 最终决定

```text
C3_7C_S2_S3_IMPLEMENTATION_PASS_READY_FOR_HUMAN_REVIEW
```

实现、配置校验、只读 preflight、合成 network tests、S1 regression 和保护边界均通过。推荐下一阶段为 `C3.7D`；本任务不授权 corrected-data S2/S3 scientific execution。

recommended_next_phase = C3.7D
implementation_commit = PENDING_SINGLE_C3_7C_COMMIT
push_status = PENDING
