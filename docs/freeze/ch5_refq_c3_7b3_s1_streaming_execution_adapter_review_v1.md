# Chapter 5 RefQ C3.7-B3
# Corrected Supplemental v2 S1 两遍流式执行适配器审计 v1

审计日期：2026-08-26
仓库：`D:\github_repo\OSDB_RefQ`
分支：`ch5-refq-repository-identity-correction-v1`
基线提交：`909426b3c388761168de3a501951ad1d14a7428e`

本任务实现了 C3.7-B3 的 S1 两遍流式执行模型，但没有执行全量 corrected S1 科学运行。没有运行 P0、S2-S7、网络算法、event rejoin、figure 或 manuscript，也没有创建 `supplemental/reference_quotient_v2/outputs/`。

## 1. 基线与范围

基线门禁：

```text
branch = ch5-refq-repository-identity-correction-v1
HEAD = 909426b3c388761168de3a501951ad1d14a7428e
worktree = clean before implementation
baseline tests = 56 passed, 0 failed
```

允许修改的范围仅为：

```text
supplemental/reference_quotient_v2/，不含 outputs/
docs/freeze/ch5_refq_c3_7b3_*
```

受保护的 corrected P0、历史 P0、历史 supplemental、共享 P0 代码、repository identity helper、source data、历史 tag 和 manuscript 均未修改。

## 2. B2.1 conflict-excluded parity 修正

修正前 `supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py` 的 `build_evidence_universe_flow()` 直接用：

```text
src_membership_conflict OR tar_membership_conflict
```

这与历史 S1 的 occurrence 定义不完全一致。现已修正为：

```text
source project-mappable
AND target project-mappable
AND (source membership conflict OR target membership conflict)
```

该修正位于 [s1_evidence_universe.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s1_evidence_universe.py:327)。

新增测试覆盖三种边界：两端均 project-mappable 且 target conflict 时计数增加；source conflict 但 target 为 NON_PROJECT 时不计入；target conflict 但 source 不可映射时不计入。

这是 `IMPLEMENTATION_PARITY_DEFECT` 修正，不是科学逻辑变更。现有 corrected P0 membership audit 记录 membership conflict entities 为 0，因此 corrected baseline 的预期数值影响为 0。

## 3. 两遍流式架构

新增模块：[s1_streaming.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/scripts/s1_streaming.py)

数据流为：

```text
authorized partition paths
  -> bounded pd.read_csv chunk
  -> S1SourceObservationAdapter.validate_reference_chunk()
  -> admitted Reference rows only

Pass 1:
  -> canonical_project_entity_identity()
  -> unique_project_membership()
  -> shared MembershipRegistry (temporary SQLite)
  -> source boundary signature
  -> global conflict set

Pass 2:
  -> same adapter and same source-boundary validation
  -> one-chunk classify_evidence_records()
  -> Counter cross-tabs, target counts, edge classes and pair counters
  -> compact S1StreamingResult

compact result
  -> mandatory acceptance gate
  -> small in-memory future S1 tables
```

实现入口为 `run_s1_streaming()`，最终化入口为 `build_future_s1_streaming_output_tables()`。每个 chunk 都先经过 B1 source-observation adapter；没有重新实现 source-admission 规则，也没有 event rejoin。

第一遍只向临时 registry 写 admitted rows 的 source/target membership pairs；第二遍不保存完整 analytical records。最终结果只保留边界计数、membership summary、分类 Counter、六个 cross-tab Counter、edge class Counter，以及约 10k 规模的有向 pair weights/sets。

## 4. MembershipRegistry 与临时文件所有权

流式实现复用了未经修改的共享 `script/ch5_reference_quotient/membership.py:55` 中的 `MembershipRegistry`。registry 路径由调用方显式提供，并满足：

```text
必须是新路径
不得位于 supplemental/reference_quotient_v2/outputs/
由本次 run 创建
在 finally 中 close + unlink
```

合成测试验证了 registry 成功路径、异常路径和 output-root 路径拒绝后的清理行为。测试没有在 scientific output root 下创建任何目录或数据库。

## 5. 两遍输入稳定性

`S1BoundarySignature` 对每一遍保留并比较：

```text
partition identity/order
per-partition Reference rows before admission
per-partition admitted count
rejected status counts
total Reference rows
total admitted rows
unknown status count
source-admission contradiction count
```

第二遍与第一遍不一致时抛出：

```text
S1_TWO_PASS_INPUT_DRIFT
```

第一遍的 source-admission counters 才进入最终结果；第二遍只用于稳定性比较和 S1 analytical counter accumulation，不会重复计入最终 source status totals。测试已验证 partition order drift 会 fail closed，并且临时 registry 会被删除。

## 6. 语义与输出 parity

流式分类复用了 B2.1 的 `classify_evidence_records()`，因此保持：

```text
target_entity_type = fine-grained -> coarse -> UNKNOWN
global membership conflict exclusion
source-seed mismatch counting
one unit per eligible Reference occurrence
self-loop/cross-project classification
REFERENCE_RECORD != AGGREGATED_EDGE_WEIGHT != EDGE_COUNT
```

Counter finalization 产生与 `FUTURE_S1_OUTPUT_CONTRACT` 相同的八个 CSV table schema，并且不写文件：

```text
evidence_universe_flow.csv
event_type_x_target_membership_status.csv
source_entity_type_x_target_membership_status.csv
target_entity_type_x_target_membership_status.csv
event_type_x_quotient_eligibility.csv
source_entity_type_x_quotient_eligibility.csv
target_entity_type_x_quotient_eligibility.csv
edge_class_counts.csv
```

target membership base counts 用于保持 flow split closure；conflict-excluded occurrence 使用修正后的两端 project-mappable 条件。重复 directed pair 累加 Reference-record weight，但只产生一条 `EDGE_COUNT` pair identity；self-loop 和 cross-project pair 分开维护。

## 7. 强制 acceptance gate

`assert_s1_streaming_runtime_acceptance()` 在未来表构造前 fail closed，至少检查：

```text
source admission closure
pass 1/pass 2 input equality
unknown status = 0
source-admission contradiction = 0
admitted count matches ADMITTED status
target membership split closure
source-seed mismatch = 0
eligible Reference closure
self weight + cross weight = eligible Reference count
edge class count closure
unit distinctions
output contract completeness
```

source-seed mismatch 仍然沿用 B2.1 mandatory gate。合成测试验证了：event identity 与 seed context 正确，但 source aggregate 映射到其他 project 时，mismatch 被计数，compact result 可以保留诊断信息，但 acceptance 和 future table construction 都拒绝。

## 8. Parity 测试

最重要的测试在 [test_s1_streaming.py](D:/github_repo/OSDB_RefQ/supplemental/reference_quotient_v2/tests/test_s1_streaming.py) 中：同一组合成分区同时执行：

```text
A. B2.1 in-memory compute_evidence_universe()
B. C3.7-B3 run_s1_streaming()
```

逐项比较并通过：

```text
source admission counters
membership summary
membership conflict count
target membership counts
conflict-excluded occurrence count
quotient-eligible count
self/cross evidence weights
directed edge counts
all six cross-tab cell counts and shares
edge-class counts
future output table schemas/content
```

跨分区测试让同一个 canonical entity 在两个分区映射到不同项目。第一遍 registry 发现 global conflict，第二遍把冲突应用到两个分区的 occurrence；结果与 in-memory B2 完全一致，证明冲突规则不是 chunk-local。

此外覆盖了 admitted-only、rejected-only、empty/no-Reference、out-of-seed audit-only、target fallback、mismatch fail-closed、重复 pair、self-loop、cross-project、input drift、registry 清理、无 S7 surface、无历史 authority 和 output-root 不创建。

本次没有执行 bounded real-data parity check，理由是该项在 B3 中为 optional；此前 B2.1 已完成全量 source-boundary/profile 证据，本轮只使用合成临时分区验证执行模型。

## 9. 内存模型

新的模型峰值近似取决于：

```text
一个或两个 bounded chunks
small category/cross-tab counters
directed project-pair counters/sets
global conflict set
disk-backed MembershipRegistry
```

它不再随 `3,747,958` 条 admitted Reference rows 保留完整 DataFrame。Counter 会随 category 和 edge cardinality 增长，因此不是字面上的 constant memory；但不会产生 B2.1 的全量 `pd.concat`、完整 classified DataFrame 和全量 row-level output table 内存峰值。

## 10. 测试结果与保护边界

测试命令：

```text
venv\Scripts\python.exe -m pytest supplemental/reference_quotient_v2/tests -q
```

最终结果：

```text
tests_collected = 64
tests_passed = 64
tests_failed = 0
```

测试输出只有既有 pandas dependency deprecation warnings。

状态：

```text
COMMAND_EXECUTION_AVAILABLE = YES
streaming_adapter_implemented = YES
two_pass_membership_model = YES
shared_MembershipRegistry_reused = YES
full_records_dataframe_retained = NO
conflict_excluded_occurrence_parity = PASS
streaming_vs_in_memory_fixture_parity = PASS
cross_partition_global_conflict_parity = PASS
two_pass_input_drift_guard = PASS
target_entity_type_fallback_parity = PASS
source_seed_mismatch_runtime_gate = PASS
bounded_real_data_parity_run = NO
full_data_S1_run = NO
supplemental_v2_outputs_root_created = NO
```

保护与执行计数：

```text
P0_RUN = 0
S1_SCIENTIFIC_RUN = 0
S2_S7_RUN = 0
NETWORK_ALGORITHMS_RUN = 0
FIGURES_GENERATED = 0
MANUSCRIPT_MODIFIED = NO
HISTORICAL_OUTPUTS_MODIFIED = NO
CORRECTED_P0_MODIFIED = NO
SHARED_P0_CODE_MODIFIED = NO
G01_G20_authoritative_runtime_status = DESIGN_ONLY_NOT_EXECUTED
scientific_logic_change_count = 0
C3_7C_authorized = NO
C4_authorized = NO
```

## 11. 最终决定

```text
C3_7B3_STREAMING_PASS_READY_FOR_HUMAN_REVIEW
```

实现门、语义 parity、跨分区冲突测试、输入漂移保护和完整 v2 测试均通过。下一步仅可在单独授权后进入 `C3.7C`；本提交本身不授权全量 S1 科学运行。

recommended_next_phase = C3.7C
implementation_commit = PENDING_SINGLE_C3_7B3_COMMIT
push_status = PENDING
