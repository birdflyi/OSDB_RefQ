# Chapter 5 RefQ C3.7-D
# corrected supplemental v2 S4/S5 实现审查 v1

审查日期：2026-08-26
仓库：`D:\github_repo\OSDB_RefQ`
分支：`ch5-refq-repository-identity-correction-v1`
基线提交：`b690f4206536535cb6e99da22d44d9f800f0f15b`
实现提交：本文件随本轮唯一实现提交写入，最终提交号见交付状态。

## 1. 范围与授权

本轮仅实现 corrected supplemental v2 的 S4 Community Stability 和 S5
Brokerage Stability。实现包括配置、只读输入边界、共享 canonical-LCC helper、
纯内存计算 contract、合成网络测试和本审查文档。

本轮没有执行 corrected-data S4/S5，也没有执行 corrected-data S1/S2/S3、P0、
GH-CoRE、event rejoin、S6/S7、图表或正文更新。`supplemental/reference_quotient_v2/outputs/`
没有创建。

## 2. 变更文件

| 文件 | 分类 | 作用 |
|---|---|---|
| `supplemental/reference_quotient_v2/configs/supplemental_v2_corrected.yaml` | 修改 | 增加冻结的 S4/S5 生产配置 |
| `supplemental/reference_quotient_v2/scripts/paths.py` | 修改 | 严格校验 S4/S5 seed、k、top-k 和阈值 contract |
| `supplemental/reference_quotient_v2/scripts/s45_canonical_graph.py` | 新增 | corrected-P0 canonical graph/LCC authority 和 header-only preflight |
| `supplemental/reference_quotient_v2/scripts/s4_community_stability.py` | 新增 | 加权 Louvain、ARI、pairwise stability、summary 和动态 parity gate |
| `supplemental/reference_quotient_v2/scripts/s5_brokerage_stability.py` | 新增 | 无权近似 betweenness、全排名、Spearman、overlap、frequency closure 和动态 parity gate |
| `supplemental/reference_quotient_v2/tests/test_s4_community_stability.py` | 新增 | S4 合成网络与 contract 测试 |
| `supplemental/reference_quotient_v2/tests/test_s5_brokerage_stability.py` | 新增 | S5 合成网络与 contract 测试 |
| `docs/freeze/ch5_refq_c3_7d_s4_s5_implementation_review_v1.md` | 新增 | 本轮冻结审查记录 |

没有修改共享 `script/ch5_reference_quotient/network_views.py`、P0 代码、
repository identity helper、历史 supplemental、历史/校正 P0 输出、源数据、main
或历史 tag。

## 3. canonical graph authority

S4 和 S5 共同使用 `s45_canonical_graph.py` 中的
`canonical_lcc_from_edges()`，避免两个 stage 产生不同的 LCC：

```text
corrected P0 rq2c_undirected_view_edges.csv
        + corrected P0 reference_quotient_node_registry.csv
        -> registry 顺序添加节点
        -> canonical edge table 顺序添加边
        -> graph-derived 最大连通分量
        -> registry 顺序的 canonical LCC
```

shared helper 还验证：

```text
graph-derived canonical LCC project IDs
== corrected P0 rq2c_algorithmic_communities.csv project IDs
== corrected P0 rq2c_structural_brokerage_candidates.csv project IDs
```

corrected P0 的 `rq2c_undirected_view_lcc_edges.csv` 也被声明为 authority 并在
未来完整加载时与 graph-derived LCC 做闭合校验。preflight 只读取 CSV headers 和
summary JSON metadata，不构造 full graph。

## 4. S4 contract

生产配置被严格固定为：

```text
s4_louvain_seed_start = 20260731
s4_louvain_run_count = 50
s4_louvain_seed_end = 20260780
canonical_seed = 20260731
ARI alert threshold = 0.9
```

每次运行调用：

```python
networkx.community.louvain_communities(graph, weight="weight", seed=seed)
networkx.community.modularity(graph, communities, weight="weight")
```

社区标签通过 partition comparison 做 label-ID-invariant 处理。ARI 与历史 pair
count 数学定义保持一致；同一 partition 和整数标签置换均得到 `1.0`。future
contract 只在内存中形成：

```text
S4_community_stability/
  louvain_stability_runs.csv
  louvain_stability_pairwise.csv
  louvain_stability_summary.json
```

50 条 run rows 和 `50 choose 2 = 1225` 条 pairwise rows 的确定性顺序已测试。
summary 包含 min/q1/median/q3/max/mean、canonical seed metadata 和
`robustness_alert = min(ari_to_canonical) < configured threshold`。

`assert_s4_canonical_seed_matches_corrected_p0()` 已实现，但本轮没有调用；它是
后续授权阶段的动态 gate，不是本轮 corrected-data PASS。

## 5. S5 contract

生产配置被严格固定为：

```text
s5_brokerage_k = [250, 500, 1000]
s5_seed_start = 20260731
s5_run_count = 20
s5_seed_end = 20260750
s5_top_k = [10, 20, 50]
canonical setting = k=500, seed=20260731
Spearman alert threshold = 0.9
top50 overlap alert threshold = 0.8
```

每个 `(k, seed)` 明确调用：

```python
networkx.betweenness_centrality(
    graph,
    k=min(k, len(graph)),
    normalized=True,
    seed=seed,
    weight=None,
)
```

排名严格使用：

```text
score descending
undirected degree descending
project_id ascending
```

`brokerage_rank_stability.csv` 保留每个 `(k, seed)` 的完整 ordinal ranking；
`brokerage_topk_inclusion_frequency.csv` 只能由该完整 ranking 派生。实现对每个
`(k, top_k)` 检查：

```text
sum(inclusion_count) == run_count * top_k
```

future S5 contract 为：

```text
S5_brokerage_stability/
  brokerage_rank_stability.csv
  brokerage_stability_runs.csv
  brokerage_topk_inclusion_frequency.csv
  brokerage_stability_summary.json
```

旧的 per-run frequency authority 被排除，不会被 corrected v2 消费或生成。
`assert_s5_canonical_setting_matches_corrected_p0()` 已实现，但本轮没有调用。

Spearman 采用 complete node set 上的 ordinal rank correlation。由于 tie-break 后
rank 唯一，直接使用 centered ordinal ranks 的相关系数与 Spearman 定义等价，未增加
新的运行时依赖。

## 6. corrected-P0 input preflight

执行的是：

```text
C3_7D_INPUT_PREFLIGHT = PASS
headers_only = true
parity_gates_invoked = false
```

已确认：

```text
corrected P0 manifest status = PASS
corrected P0 manifest SHA-256 = 21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7
corrected P0 config SHA-256 = e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658
summary random_seed = 20260731
summary brokerage_sample_size = 500
S4 range = 20260731..20260780
S5 range = 20260731..20260750
S5 k = [250, 500, 1000]
S5 top_k = [10, 20, 50]
```

required authority headers 已检查：canonical edges、canonical LCC edges、node
registry、algorithmic communities 和 structural brokerage candidates。preflight
没有读完整 CSV rows，没有构造 corrected graph，也没有调用 Louvain、betweenness
或任何 corrected-P0 parity gate。

## 7. 测试与执行计数

命令：

```text
python -m pytest supplemental/reference_quotient_v2/tests -q
```

结果：

```text
96 passed, 0 failed
1 existing pandas deprecation warning
```

其中包括原有 S1-S3 测试回归，原有基线为 `84 passed`；C3.7-D 新增测试没有改变
S1/S2/S3 语义。

合成网络算法调用计数：

```text
S4_FIXTURE_LOUVAIN_RUNS = 8
S5_FIXTURE_BETWEENNESS_RUNS = 7
NETWORK_FIXTURE_TESTS > 0
NETWORK_CORRECTED_DATA_RUN = 0
```

S4 计数来自两次四 seed synthetic compute；S5 计数来自一次 canonical fixture
score 计算和一次两 k、三 seed synthetic compute。它们不是 corrected-data
scientific runs。

## 8. 保护边界与门禁状态

```text
P0_RUN = 0
S1_SCIENTIFIC_RUN = 0
S2_SCIENTIFIC_RUN = 0
S3_SCIENTIFIC_RUN = 0
S4_SCIENTIFIC_RUN = 0
S5_SCIENTIFIC_RUN = 0
S6_S7_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
supplemental_v2_outputs_root_created = NO
scientific_logic_change_count = 0
```

G01-G20 的 authoritative runtime status 仍为：

```text
DESIGN_ONLY_NOT_EXECUTED
```

特别是：

```text
G12 corrected canonical S4 comparison = NOT EXECUTED
G13 corrected brokerage authority = NOT EXECUTED
G14 deprecated authority = IMPLEMENTATION CONTRACT TEST ONLY
```

工作树差异仅落在允许的 `supplemental/reference_quotient_v2/` 和本审查文档；main
branch、`chapter5-refq-freeze-v1.0` tag、历史 P0、corrected P0、C4、figure 和
manuscript 均未修改。

## 9. 已知限制与下一授权边界

1. 本轮证明了实现 contract、路径边界、算法参数、确定性排序和 synthetic
   closure；没有证明 corrected-data S4/S5 的数值 parity。
2. 动态 parity gate 必须在未来获授权的 corrected-data execution 中调用；本轮
   不应把它们标记为 PASS。
3. S6/S7、figure-ready、figure render 和 manuscript claim 更新留待后续明确授权。
4. `C3.7E_authorized = NO`，`C4_authorized = NO`。

推荐下一阶段：`C3.7E`。

## 10. 决策

```text
C3_7D_S4_S5_IMPLEMENTATION_PASS_READY_FOR_HUMAN_REVIEW
```
