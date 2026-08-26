# Chapter 5 RefQ C3.7-B2.1
# S1 语义一致性与全量执行就绪性修正审计 v1

审计日期：2026-08-26
仓库：`D:\github_repo\OSDB_RefQ`
分支：`ch5-refq-repository-identity-correction-v1`
基线提交：`139125fb5066c34c7c0a88588575f6ad8bb7e40e`

本审计只处理 C3.7-B2.1 明确授权的 S1 窄修正。没有运行 P0、全量 S1 科学计算、S2-S7、网络算法、图形或稿件更新，也没有创建 `supplemental/reference_quotient_v2/outputs/`。

## 1. 执行边界

| 项目 | 状态 |
|---|---|
| 基线 v2 测试 | PASS，45/45 |
| 修正后 v2 测试 | PASS，56/56 |
| corrected aggregate 全量列级剖析 | 已执行，只用于 source-admission 和实体类型计数 |
| 全量 S1 科学计算 | NO |
| S1 publication output | NO |
| P0 rerun | 0 |
| S2-S7 | 0 |
| network algorithms | 0 |
| figure/manuscript | 0 / NO |
| v2 outputs root | 未创建 |
| event rejoin | NO |

剖析读取了 corrected aggregate 的 294 个授权分区，使用 source-boundary 所需字段以及 `tar_entity_type`、`tar_entity_type_fine_grained`。它没有调用 `compute_evidence_universe()` 处理全量数据，也没有写入科学结果。

## 2. Target entity type 语义一致性

### 2.1 直接比对结果

历史 supplemental v1 的实现位置为 `supplemental/reference_quotient_v1/scripts/run_supplemental.py:226` 和 `:229`，使用：

```python
frame["target_fine_type"].fillna(frame["target_entity_type"])
```

当前 P0 authority 的实现位置为 `script/ch5_reference_quotient/pipeline.py:365`，使用：

```python
chunk["tar_entity_type_fine_grained"].fillna(chunk["tar_entity_type"]).fillna("UNKNOWN")
```

修正前 v2 S1 的位置 `supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py:233` 只使用了：

```python
result["tar_entity_type_fine_grained"].map(_text)
```

因此修正前属于 `IMPLEMENTATION_PARITY_DEFECT`，不是 `SCIENTIFIC_LOGIC_CHANGE`。当前 v2 已在同一位置恢复 fine-grained -> coarse -> `UNKNOWN` 的回退顺序；source entity-type 规则没有改变。

### 2.2 corrected aggregate 真实数据剖析

| 指标 | 数值 |
|---|---:|
| Reference rows before source admission | 3,748,078 |
| admitted Reference rows | 3,747,958 |
| `tar_entity_type_fine_grained` non-null | 3,747,958 |
| fine-grained missing | 0 |
| fine-grained missing + coarse present | 0 |
| fine-grained missing + coarse missing | 0 |
| coarse fallback category distribution | 空 |
| source-admission rejected rows | 120 |

所有 admitted 行的 fine-grained 类型均非空，故本次 corrected aggregate 中旧 B2 实现实际误分类的行数为 0。但回退规则仍是授权历史行为，不能因为本数据集没有触发回退就保留错误实现。

source-admission 状态计数为：

```text
ADMITTED_SOURCE_OBSERVATION = 3,747,958
OUT_OF_SEED_SOURCE_OBSERVATION = 120
MISSING_EVENT_REPOSITORY_ID = 0
INVALID_EVENT_REPOSITORY_ID = 0
```

观察到的 aggregate schema version 全部为：

```text
reference_aggregate_schema_v2_event_repository_provenance
```

## 3. 修正内容

### 3.1 类型回退

文件：[s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py:233)

现在的规则是：

```text
fine-grained 非空 -> fine-grained
否则 coarse tar_entity_type 非空 -> coarse
否则 UNKNOWN
```

该值同时进入两个 target entity type cross-tab，因此 cross-tab 与单行分类使用同一语义。

测试位置：[test_s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/tests/test_s1_evidence_universe.py:110)

覆盖了 fine-grained present、fine-grained missing + coarse present、两者均缺失，以及 fallback 进入 cross-tab 输出。

### 3.2 source-admission before-count 闭合

文件：[s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py:148)

`admitted_records_from_chunks()` 现在即使没有 admitted rows，也返回：

```text
source_admission_before_count = sum(source_admission_status_counts.values())
```

因此 admitted-only、mixed、rejected-only、missing-only、invalid-only、empty/no-Reference 都满足通用闭合。对于 rejected-only，admitted 为 0 但 before-count 保留 rejected Reference rows 数量；对于真正空输入，两个值都为 0。

测试位置：[test_s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/tests/test_s1_evidence_universe.py:220)

### 3.3 source-seed mismatch fail-closed

文件：[s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py:384)

新增 `assert_s1_runtime_acceptance(result)`，要求以下检查全部通过：

```text
source_admission_closes
admitted_count_matches_status
target_membership_split_closes
source_mismatch_after_admission_is_zero
edge_weight_closes
```

`build_future_s1_output_tables()` 在构造任何未来 S1 表之前调用该 gate。因此正常的 future table acceptance path 遇到 source-seed mismatch 会拒绝，而不会仅保留诊断字段后继续接受结果。

测试夹具满足：

```text
event_repo_id = expected_source_context_repo_id = authoritative seed = 101
src_entity_id_agg = R_202
```

source admission 本身有效，但 `source_seed_membership_mismatch` 为 true；runtime acceptance 和 future table construction 均抛出 `S1EvidenceUniverseContractError`。测试位置：[test_s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/tests/test_s1_evidence_universe.py:262)。

这仍然是边界/契约修正，不改变 RefQ 的 membership、eligibility、edge 或权重科学规则。

## 4. 输出契约复核

`docs/freeze/ch5_refq_c3_7b2_s1_output_contract_v1.csv` 中 target entity type 相关表仍使用 `target_entity_type` 作为维度，列结构不需要改变。修正后的模块保证该维度按 fine-grained -> coarse -> `UNKNOWN` 生成，并在两个 target entity type cross-tab 中复用。

没有增加 publication output，也没有改变历史 v1 或 corrected P0 输出。

## 5. 全量执行就绪性与内存边界

### 5.1 有界样本测量

使用 corrected aggregate 的单个分区、100,000 行 admitted bounded sample，测量了当前 v2 内存 DataFrame 模型：

| 对象 | 样本内存 |
|---|---:|
| source/admitted DataFrame | 119,238,880 bytes，约 113.7 MiB |
| classified DataFrame | 191,483,503 bytes，约 182.6 MiB |
| source + classified 同时保留 | 310,722,383 bytes，约 296.3 MiB |
| corrected aggregate admitted rows | 3,747,958 |
| 线性放大倍数 | 37.48 |
| source DataFrame 线性估算 | 约 4.16 GiB |
| classified DataFrame 线性估算 | 约 6.68 GiB |
| source + classified 线性下界 | 约 10.85 GiB，约 11.65 GB decimal |
| 当前机器物理内存 | 约 29.73 GiB |

上述 10.85 GiB 只是 source 与 classified 两个稳定对象的线性下界，不包括：

```text
admitted_frames 列表和 pd.concat 的同时保留
require_admitted_reference_records() 的复制
classify_evidence_records() 的复制和派生列
pairs / by_entity / per-entity set membership 临时对象
groupby、drop_duplicates、cross-tab 和布尔 mask 临时对象
Python、pandas、NumPy 运行时开销
```

corrected P0 的现有 membership audit 记录了 `1,142,161` 个 unique project-mappable entities、0 个 conflict entities、最大 membership 数为 1。当前 B2 的内存实现还会在冲突扫描期间保留 Python pair set 和 entity-to-project set 映射；该结构的确切峰值依赖 CPython allocator，但至少属于数百 MiB 级别的额外结构，不能从 10.85 GiB 下界中忽略。

当前模型还会保留全量 admitted chunks，随后执行全量 `pd.concat`，并在分类和 cross-tab 入口重复复制 DataFrame。以约 29.73 GiB 的机器内存没有足够的可验证安全余量，因此不能把当前 in-memory 模型判定为合理的全量执行方案。

### 5.2 决策

```text
S1_FULL_DATA_EXECUTION_MODEL = STREAMING_REQUIRED
```

本任务没有实现 streaming rewrite。建议后续单独授权：

```text
C3.7-B3 S1 STREAMING EXECUTION ADAPTER
```

设计要求：

1. 第一遍按 corrected source-boundary 分块验证并累计状态计数，同时建立可复用的 `MembershipRegistry` 或等价磁盘辅助索引，完成全局 membership conflict detection。
2. 第二遍重新分块验证 admitted Reference rows，使用已冻结的 membership/conflict 结果进行分类。
3. 所有 universe、target/source entity type cross-tab、eligibility、edge class 和 directed project-pair counters 增量累计。
4. 保留 source-seed mismatch、before-count、admitted-count、target split 和 edge-weight 的同一 acceptance gate。
5. 不保留全量 3.7M 行 DataFrame，不做 event rejoin，不修改 P0 代码，不写入历史根目录。

该设计保持 B2 的 Reference-record multiplicity、global conflict exclusion、self-loop 和 cross-project directed edge 语义，不引入科学逻辑变化。

## 6. 测试与结果

测试命令：

```text
venv\Scripts\python.exe -m pytest supplemental/reference_quotient_v2/tests -q
```

结果：

```text
tests_collected = 56
tests_passed = 56
tests_failed = 0
```

测试包含原有 C3.7-A/B/B2 回归，以及本次新增的 target fallback、各 source-admission status before-count closure、rejected-only boundary、empty/no-chunks boundary 和 source-seed mismatch mandatory rejection。

测试只有 pandas dependency deprecation warnings，没有 failure。

## 7. 科学与保护边界

```text
scientific_logic_change_count = 0
full_data_S1_run = NO
S1_SCIENTIFIC_RUN = 0
S2_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
supplemental_v2_outputs_root_created = NO
event_rejoin_performed = NO
C3_7C_authorized = NO
```

本任务只改变：

```text
supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py
supplemental/reference_quotient_v2/tests/test_s1_evidence_universe.py
docs/freeze/ch5_refq_c3_7b21_s1_semantic_parity_execution_readiness_review_v1.md
```

## 8. 最终决定

```text
C3_7B21_PASS_REQUIRES_S1_STREAMING_PHASE
```

含义：语义 parity、计数闭合和 mismatch fail-closed 修正已通过测试并具备继续设计的条件；但当前全量 in-memory 执行模型不应直接用于 3,747,958 条 admitted Reference rows。下一授权边界应为 `C3.7-B3 S1 STREAMING EXECUTION ADAPTER`，而不是 C3.7-C 科学运行。

implementation_commit = PENDING_SINGLE_C3_7B21_COMMIT
push_status = PENDING
