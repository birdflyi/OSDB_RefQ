# Chapter 5 RefQ 数据来源、Repository Identity、过滤边界与稳定性治理报告 v1.0

> **用途**：本报告用于两类场景：  
> 1. 作为后续 Codex / 人工审计、versioned correction、P0 重算和投稿前核查的上下文基线；  
> 2. 作为后续维护人员快速理解 Chapter 5 RefQ 数据来源、时间语义、repository identity、primary repository 标注、过滤位置、OpenDigger/GHArchive 历史属性、稳定性和已知缺陷的长期治理文档。
>
> **当前状态**：理论口径不变；`STRICT_REPOSITORY_IDENTITY` 已人工接受；Fireproof 的 source-observation 边界已解决；旧 P0 数值仍保留作 provenance anchor，但在 versioned correction 完成前不再作为最终投稿数值继续向正文/图表传播。

---

## 0. Executive Summary

当前 Chapter 5 RefQ 的数据与身份治理可以压缩为下面这条链：

```text
GHArchive / OpenDigger 历史 GitHub event facts
        ↓
保留 event-time numeric repo_id / event_time
        ↓
GH_CoRE relation extraction
        ↓
保留 fine-grained entity / target numeric identity
        ↓
通用 Relation asset：尽量保留，不因当前 RefQ 任务删除相关历史 repository facts
        ↓
RefQ observation view
        ↓
SOURCE admission:
event_repo_id == frozen annotated primary github_repo_id
        ↓
membership audit
        ↓
Q = M^T R_P M
        ↓
Project-level RefQ / RefQN
```

核心治理结论：

1. **GitHub numeric repository ID 是 repository identity authority。**
2. **DBMS → primary repository 的选择 authority 是冻结的人工维护月度标注快照，而不是 repo_name 或年度 event count。**
3. 当前 Chapter 5：
   - event observation scope = **2023**；
   - primary repository annotation snapshot = **2024-10**；
   - frozen annotation file = `dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv`。
4. 2024-10 是 **post-scope curated validation snapshot**：用于提高 DBMS→GitHub repository mapping 的正确性和完整性，而不是把 2024-10 的 GitHub 状态反写到 2023 event identity。
5. `repo_name/full_name` 是描述和检索元数据，不得作为稳定 identity key。
6. 历史/相关 repository：
   - 上游 raw/relation asset 中继续保留；
   - 如果不是该 DBMS 在冻结标注中的 primary repo，则不能作为该 seed 的 RefQ source observation；
   - 仍可作为合法的 expanded target。
7. event/activity count 只作为 **QC / anomaly trigger**，例如数量级差异可触发人工复核，但不得自动覆盖人工标注。
8. OpenDigger/GHArchive 保存并结构化 event-time repository attribute evidence；这些历史 snapshot 可以降低分析对“当前 GitHub 状态”和“实验即时执行”的依赖。
9. repository-level open-source eligibility 与 event-level payload 中的 `license` 是否为空是两个不同概念。当前样本资格已经由人工标注及 open-source-license 过滤规则决定，不应按每条 event 的 `license != null` 再过滤。
10. Fireproof 已确认是一个 **同名、不同 numeric repo ID、在 2023 年时间上连续出现** 的 observation-boundary defect：
    - `600271677`：历史 distinct repository；
    - `679889516`：冻结标注中的 Fireproof primary seed；
    - 120 条历史-ID Reference records 不属于 `679889516` 的 source observation。
11. 当前需要的是 **versioned correction**，不是改 RefQ 理论，也不是给 Fireproof 做 row-level 特判。

---

# 1. 研究对象与 RefQ 身份语义

## 1.1 Project-level RefQ 的项目节点

本研究的 Project-level RefQ 节点以 GitHub repository/project 为基本项目身份单位。

对于可映射为 repository 的 fine-grained entities，项目身份由 numeric repository ID 表示：

```text
R_<github_numeric_repo_id>
```

例如：

```text
R_679889516
R_600271677
```

即使两个 repository 在不同时间使用过相同的：

```text
owner/name
```

只要 numeric repository IDs 不同，就属于不同 repository identities。

因此：

```text
600271677 != 679889516
```

不会因为：

```text
fireproof-storage/fireproof
```

这个名称曾被二者先后使用而合并。

---

## 1.2 RefQ 理论层保持不变

当前 identity correction 不改变 RefQ 理论：

\[
Q=M^\top R_PM
\]

其中：

- \(R_P\)：project-mappable fine-grained Reference relation；
- \(M\)：artifact/entity → project membership；
- \(Q\)：Project-level Reference Quotient；
- membership 仍要求每个 quotient-eligible fine-grained identity 具有唯一 project membership。

因此 repository identity 修复属于：

```text
observation / provenance / upstream materialization correction
```

而不是：

```text
RefQ theory change
```

---

# 2. 数据源全景

## 2.1 DBMS repository 人工标注资产

当前 Chapter 5 使用的冻结标注文件：

- `data/github_osdb_data/dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv`
- GitHub：
  https://github.com/birdflyi/OSDB_RefQ/blob/main/data/github_osdb_data/dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv

该文件包含至少：

```text
DBMS identity / common name
category
github_repo_link
github_repo_id
open_source_license
License_info
repo_created_at
...
```

持续维护的上游月度标注资产：

- https://github.com/birdflyi/od_label_issue_gen/tree/main/data/database_repo_label_dataframe

`OSDB_RefQ` README 已明确指出该 upstream DBMS project list 持续按月更新，而 Chapter 5 P0 使用冻结输入：

- https://github.com/birdflyi/OSDB_RefQ/blob/main/README.md

---

## 2.2 当前 P0 冻结配置

配置：

- https://github.com/birdflyi/OSDB_RefQ/blob/main/configs/ch5_reference_quotient_p0.yaml

当前核心时间与输入：

```text
study_year = 2023

dbms_repos_key_features =
dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv

expected_candidate_seed_count = 301
expected_analysis_seed_count = 294
```

因此：

```text
event observation time
!=
annotation verification time
```

这是设计的一部分，不是误配。

---

## 2.3 GitHub 历史事件：GHArchive / OpenDigger

OpenDigger 数据源说明：

- https://open-digger.cn/docs/user-docs/data-sources/github#数据来源

其链接的 GHArchive：

- https://www.gharchive.org/

GHArchive 可直接下载小时级历史 event：

```bash
wget https://data.gharchive.org/2015-01-01-15.json.gz
gzip -d 2015-01-01-15.json.gz
head -30 2015-01-01-15.json
```

项目维护过程中确认：

- GHArchive 的 raw event JSON 中，不同 event type 的 `payload` schema 不同；
- 某些 event payload 会包含完整或较完整的 repository snapshot；
- OpenDigger 会进一步解析这些 payload 内部属性并结构化到可 SQL 查询的数据表中，从而便于本项目快速查询 repository metadata/history。

这意味着分析不必完全依赖实验执行当日 GitHub API 返回的“当前状态”。

---

## 2.4 GH_CoRE relation extraction

GH_CoRE 用于从已采集 GitHub 协作事件中识别 fine-grained relations / Reference evidence。

在当前已确认的 identity 机制中：

- target parsing 能利用 numeric repository identity；
- fine-grained Issue/PR/Commit identity 能包含 repository-scoped numeric identity；
- 但历史 relation serialization 没有把 source event 的 `repo_id/repo_name` 作为显式 relation columns 完整保留下来；
- downstream `granu_agg` 又使用 caller-supplied repo ID 聚合 source project，最终导致 Fireproof 的 source provenance 错配。

这属于 upstream provenance/materialization defect，不是 RefQ membership invariant 错误。

---

# 3. 时间模型：四类时间/状态必须分开

推荐长期采用下面四层时间语义。

## 3.1 Event fact time

由历史 event 自己携带：

```text
event_id
event_type
event_time / created_at
event.repo_id
event.repo.name
```

该层回答：

> 某个事件在什么时候发生、当时属于哪个 numeric repository identity？

这是历史 event identity 的最高 authority。

---

## 3.2 Event payload snapshot time

同一个 event 的 payload 可能携带 event-time repository / PR / fork 等对象快照。

例如上传的 GHArchive raw 样本中：

### PullRequestEvent

可出现：

```text
payload.pull_request.head.repo.license
payload.pull_request.base.repo.license
payload.pull_request.head.repo.description
payload.pull_request.base.repo.archived
...
```

样本中既出现：

```json
"license": null
```

也出现：

```json
"license": {
  "key": "mit",
  "name": "MIT License",
  "spdx_id": "MIT"
}
```

### ForkEvent

也可出现：

```text
payload.forkee.license
payload.forkee.description
payload.forkee.archived
...
```

因此正确认识是：

```text
event type
→ payload schema
→ available historical repository snapshot fields
```

而不是：

```text
所有 event 都有统一 repository metadata schema
```

这些 payload-derived fields 是：

> **historical snapshot evidence**

而不是完整、规则采样的 repository state history。

---

## 3.3 Repository annotation time

DBMS→primary repository mapping 的验证时间独立于 event time。

当前：

```text
annotation snapshot = 2024-10
```

该快照是实验执行前经过进一步人工维护后的 post-scope curated validation snapshot。

它回答：

> 在本次冻结研究设计中，哪个 GitHub numeric repository identity 被确认用于代表这个 DBMS？

它不回答：

> 2024-10 当时这个 repo 的事件是否应该写回 2023。

---

## 3.4 Analysis release time

一次科学分析还需要冻结：

```text
annotation snapshot
raw/event input snapshot
GH_CoRE relation extraction version
aggregation contract
RefQ code commit
analysis config
output manifest/checksum
```

后续月度标注变化不能静默修改已冻结 release。

---

# 4. 为什么使用 2024-10 标注快照

当前项目维护者给出的选择理由如下，应在后续稳定性 audit 中进一步机器化核验：

1. 相对于过早冻结在 2024-01，2024-10 的人工标注经过更充分的检查和补全；
2. 2024-10 相对于早期版本的大部分变化是：
   - 空 repository 标注被补全；
   - 不存在/无效 repository 被人工确认并修正；
   - 旧 repository ID 被检查出有问题后更新；
   - repository 删除、社区迁移、fork/upstream 关系改变后，对“哪个仓库代表 DBMS”的人工标注被纠正；
3. 已验证有效的 repository ID 不应因为普通月度维护而无原因消失；
4. 当前实验执行一次需要大量 GitHub API/entity validation 调用，因此在确定一个更高质量的人工标注快照并跑完整套 relation extraction 后，数据即冻结并上传，而不是每月随标注更新重跑科学结果；
5. 当前 relation/data release 已上传公共归档，后续应通过新 version 而不是覆盖旧 release。

公开数据入口在当前 README 中给出，包括 Zenodo：

- https://doi.org/10.5281/zenodo.18817348

因此 2024-10 应定义为：

```text
POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT
```

而不是：

```text
2023-12 instantaneous repository snapshot
```

---

# 5. Primary Repository Selection Contract

建议冻结如下。

```text
PRIMARY_REPOSITORY_ANNOTATION_CONTRACT

Repository identity:
GitHub numeric repository ID.

Primary-repository authority:
github_repo_id in the explicitly frozen monthly manually curated annotation snapshot.

Current Chapter 5:
event scope = 2023
annotation snapshot = 2024-10

repo_name/github_repo_link:
descriptive and retrieval metadata only.

activity/event count:
QC / anomaly-detection signal only.

later annotation:
new analysis version input, not retroactive mutation.
```

---

## 5.1 为什么不使用“年度事件最多的仓库自动成为主仓库”

年度 event count 与 repository representativeness 不是同一概念。

例如：

```text
旧仓库：
1-8 月很活跃，之后迁移

新仓库：
8-12 月成为真正上游，但全年 event 数较少
```

若按 annual event count 自动选择，会把已经发生迁移的旧 repository 重新选回来。

另一个更危险的场景：

```text
旧人工标注本身就是错误 repository
且这个无关 repository 恰好高活跃
```

若让事件量覆盖人工纠错，会把已纠正的错误再次放大。

因此项目接受这样的风险排序：

```text
错误分析一个高活跃但错误归属的 repository
>
少统计部分历史 related repository activity
```

---

## 5.2 10× 活动量规则的正确角色

可采用：

```text
max(activity_A, activity_B) / min(activity_A, activity_B) >= 10
```

作为：

```text
PRIMARY_REPO_ACTIVITY_ANOMALY = REVIEW
```

但不得：

```text
AUTO_OVERRIDE_PRIMARY_REPO
```

人工复核可检查：

- scope 后是否发生 repo recreate / migration；
- owner / organization transfer；
- archive / deletion；
- fork/upstream 角色改变；
- old annotation error；
- current primary repo 是否因为迁移较晚而历史活动较少。

---

# 6. Open-source eligibility 与历史 license evidence

## 6.1 Sample eligibility

当前 DBMS repository selection 本身已经有 open-source-license filtering rule。

Legacy selection code 中存在：

```python
ValidateFunc.check_open_source_license(
    nan_as_final_false=True,
    only_common_osl=True
)
```

因此：

```text
OPEN_SOURCE_ELIGIBILITY
```

属于 DBMS/repository annotation + selection contract。

---

## 6.2 Event-level historical license

OpenDigger/GHArchive event payload 中的：

```text
repo.license
payload.pull_request.*.repo.license
payload.forkee.license
...
```

属于：

```text
HISTORICAL_LICENSE_EVIDENCE
```

它们可以用于：

- 历史状态验证；
- 许可证变化研究；
- repository metadata snapshot；
- 事后审计。

但不用于当前 RefQ 每条 record 的 source admission。

因此：

```text
event payload license = null
```

不意味着：

```text
repository is not open source
```

也不应产生：

```text
Reference record exclusion
```

---

## 6.3 推荐长期规则

```text
OPEN_SOURCE_SAMPLE_CONTRACT

1. Sample eligibility comes from the frozen curated DBMS repository annotation and license filter.
2. Event-level payload license is historical evidence, not a per-record eligibility gate.
3. Null event payload license does not override curated open-source eligibility.
4. Historical license snapshots may be used for provenance, validation, or separate temporal studies.
```

---

# 7. Preservation Contract 与 RefQ Participation Contract

这是当前维护最重要的架构区分。

## 7.1 Preservation Contract

上游尽量保留：

- raw events；
- event-time numeric repo ID；
- event payload attributes；
- fine-grained entity identities；
- relations；
- historical/related repositories；
- non-project targets；
- provenance。

即：

```text
不要因为当前 RefQ 只研究 primary seed repository，
就在通用数据层物理删除所有 related repository facts。
```

---

## 7.2 RefQ Participation Contract

只有进入 RefQ-specific observation view 时才施加严格分析边界。

对 seed \(s\)：

```text
SOURCE_OBSERVATION_ADMISSION:

event_repo_id == s.github_repo_id
```

并且该过滤必须发生在：

```text
MembershipRegistry
quotient eligibility
RQ1 seed profile
edge aggregation
```

之前。

---

## 7.3 为什么不能等到 edge build 后再过滤

如果 out-of-seed source rows 先进入：

```text
membership conflict detection
source profile
quotient counter
```

则它们可能：

- 制造分析域外的 false membership conflict；
- 污染 RQ1 denominator；
- 污染 self/external Reference composition；
- 改变 source role；
- 进入 quotient edge；
- 影响 topology/community/statistics。

因此：

> 数据可以保留到上游通用 relation asset，但不能保留到 RefQ membership/aggregation 计算内部再晚过滤。

---

# 8. Source / Target Asymmetry

对 historical/related repository 必须区分 source 和 target role。

假设：

```text
primary seed = 679889516
historical related repo = 600271677
```

### Source

如果 event：

```text
event_repo_id = 600271677
```

它不是 `679889516` seed 的 source observation。

因此：

```text
EXCLUDE_FROM_REFQ_SEED_SOURCE_VIEW
```

### Target

若一个合法 seed source：

```text
source = 679889516
```

显式 Reference 到：

```text
target = 600271677
```

则 target 仍然合法：

```text
ALLOW_AS_EXPANDED_TARGET
```

因此绝不能使用：

```text
“同一 DBMS 的非主仓库全部删除”
```

这种规则。

---

# 9. Fireproof Control Case

## 9.1 已确认事实

冻结 seed：

```text
repo_id = 679889516
repo_name = fireproof-storage/fireproof
```

同一 2023 observation file 中发现两个 numeric repo IDs：

### Historical repository

```text
repo_id = 600271677
repo_name = fireproof-storage/fireproof

raw events = 893
Reference-bearing events = 91
Reference records = 120

time range:
2023-03-06 18:20:42
→ 2023-08-17 21:10:24
```

### Frozen primary seed repository

```text
repo_id = 679889516
repo_name = fireproof-storage/fireproof

raw events = 437
Reference-bearing events = 41
Reference records = 58

time range:
2023-08-17 21:13:45
→ 2023-12-29 03:41:17
```

两个 numeric IDs distinct，名称相同。

---

## 9.2 Root cause

已确认链路：

```text
raw event repo_id = 600271677
        ↓
fine-grained source identity retains historical numeric identity
        ↓
relation schema omits explicit event_repo_id / event_repo_name
        ↓
evidence file / caller uses current same-name seed mapping
        ↓
caller repo_id = 679889516
        ↓
granu_agg assigns:
src_entity_id_agg = R_679889516
```

因此：

```text
SOURCE_AGG_MISMATCH
```

并不是 P0 membership detector 产生了错误。

---

## 9.3 Impact audit

Repository Identity Provenance Impact Audit v1.1：

```text
JOIN_INTEGRITY = PASS

code_defect_scope = PIPELINE_WIDE_CODE_PATH
observed_data_impact_scope = LOCALIZED_SINGLE_SEED

affected_seed_files = 1
multi_repo_files = 1

affected_raw_events = 893
affected_reference_bearing_events = 91
affected_reference_records = 120
source_agg_mismatch_reference_records = 120

project-mappable targets = 74
non-project targets = 46
target_numeric_conflicts = 0
```

294/294 observation files通过 event_id provenance gate。

---

## 9.4 最终 identity/observation decision

人工接受：

```text
STRICT_REPOSITORY_IDENTITY
```

因此：

```text
600271677:
historical distinct repository
outside frozen 679889516 seed source unit

679889516:
frozen Fireproof primary seed
```

seed count：

```text
294 unchanged
```

不引入：

```text
project lineage identity layer
```

也不把 historical repo 加成第 295 个 seed。

---

# 10. 为什么不能直接把 120 条 source aggregate 改成 R_600271677

当前 P0 有 source-seed invariant：

```text
expected_source = seed.repo_id
```

并要求所有 project-mappable source membership 与该 seed 一致。

若直接：

```text
R_679889516
→
R_600271677
```

却仍然把这 120 条保留在 seed `679889516` 的 RefQ source view 中，会产生：

```text
source_project = 600271677
expected_source = 679889516
source_seed_membership_mismatch = TRUE
```

因此真正的 correction semantics 是：

```text
恢复 event_repo_id
        ↓
判断它不属于该 seed source observation
        ↓
OUT_OF_SEED_SOURCE_OBSERVATION
        ↓
RefQ view 中排除
```

而不是：

```text
换 ID 后继续算
```

---

# 11. Recommended Correction Boundary

当前建议：

```text
EVENT_REPOSITORY_FILTER
+
RELATION_SCHEMA_PLUS_AGGREGATE
```

具体含义：

1. 上游 raw event 保持不变；
2. relation layer 必须显式携带，或通过可验证 join 获得：
   - `event_repo_id`
   - 可选 `event_repo_name`；
3. source aggregation 使用 row-level event repository identity；
4. caller-supplied repo ID 只能作为 expected/context/assertion，不得覆盖 event provenance；
5. RefQ observation view 增加一般规则：
   ```text
   event_repo_id == annotated_seed.github_repo_id
   ```
6. 293 个 unaffected seeds 不应产生 unrelated drift；
7. Fireproof 120 条历史 source Reference records 应在 RefQ source admission 阶段被排除；
8. 不对 Fireproof 做硬编码 ID 特判。

---

# 12. 当前冻结与 correction release 的关系

历史 release：

```text
chapter5-refq-freeze-v1.0
HEAD historical canonical freeze:
68d001551359d120bf2a06cc5e571742df7e7822
```

应继续保留作为 provenance anchor。

但当前科学状态应理解为：

```text
OLD_FREEZE =
PROVENANCE_ANCHOR

OLD_NUMERICAL_BASELINE =
SCIENTIFICALLY_SUPERSEDED_PENDING_VERSIONED_CORRECTION
```

禁止：

- 删除旧 tag；
- 覆盖旧 outputs；
- silent patch frozen CSV；
- 把旧数值继续传播成最终投稿 baseline。

未来 corrected release 应使用：

```text
new branch / version / tag
new manifest
new checksums
old-new diff report
```

---

# 13. 当前已经完成的主要审计

## 13.1 Corrected-Baseline Semantic Reuse Audit v2

正确 stable pre-refactor commit：

```text
4bc2a7e3aa8526d167001cdb6e98e59930238602
```

first RefQ refactor：

```text
0049034231794bc39becb08846a5efcf2beda45e
```

current freeze：

```text
68d001551359d120bf2a06cc5e571742df7e7822
```

结果：

```text
CORRECTED_BASELINE_REUSE_AUDIT =
PASS_READY_FOR_HUMAN_REVIEW

POST_REFACTOR_REGRESSION = 0

Fireproof =
PRE_EXISTING_BASELINE_DEFECT
```

说明当前问题不是最近 RefQ refactor 新引入的大范围回归。

---

## 13.2 Repository Identity Provenance Impact Audit v1.1

结果：

```text
PASS_READY_FOR_HUMAN_REVIEW
JOIN_INTEGRITY = PASS
observed_data_impact_scope = LOCALIZED_SINGLE_SEED
```

确认 294-file boundary，定位 Fireproof 影响为 1 seed / 120 Reference records。

---

## 13.3 Fireproof Seed Identity Boundary Decision Audit v1

结果：

```text
PASS_READY_FOR_HUMAN_DECISION

recommended_policy =
STRICT_REPOSITORY_IDENTITY
```

人工已接受该 policy。

---

# 14. OpenDigger / GHArchive 对稳定性的意义

## 14.1 历史事实不会完全依赖当前 GitHub 状态

由于历史 event 已持久化：

```text
repo rename
repo transfer
repo archive
repo deletion
visibility change
license change
```

不会自动重写已经保存的：

```text
event_repo_id
event_time
event payload snapshot
```

因此分析可以在 scope 结束后较长时间执行，而不必把“当前 GitHub API 返回什么”当作唯一 historical truth。

---

## 14.2 当前 GitHub API 的正确定位

GitHub API 更适合：

```text
validation
entity enrichment
gap filling
current-state annotation checking
```

而不是：

```text
sole historical identity authority
```

特别是：

```text
historical repo_id
```

优先服从 historical event identity。

---

## 14.3 结果稳定性的真正来源

推荐表述：

> 当前设计降低的是对分析执行时点和实时 GitHub repository state 的依赖。

稳定性来自：

```text
historical event archive
+
numeric identity
+
frozen curated mapping snapshot
+
frozen GH_CoRE relation extraction
+
versioned analysis contract
```

而不是声称：

```text
历史 repository state 完整无缺
```

---

# 15. Annotation History 的用途与边界

月度 annotation history 可以用于：

```text
annotation provenance
mapping correction audit
blank completion audit
repository-ID change audit
open-source eligibility change audit
```

但：

```text
ANNOTATION_HISTORY != REPOSITORY_LINEAGE
```

例如：

```text
2024-01: repo_id = A
2024-10: repo_id = B
```

只能直接证明：

```text
annotation changed A → B
```

不能自动证明：

```text
A and B are the same repository/project identity
```

变更原因需人工分类：

```text
BLANK_TO_VALID
INVALID_TO_CORRECTED
VALID_ID_TO_DIFFERENT_VALID_ID
VALID_ID_TO_BLANK
REMOVED_NON_OPEN_SOURCE
REPO_MIGRATION
FORK_TO_UPSTREAM_CORRECTION
OTHER
```

---

# 16. 推荐的 2024-01 → 2024-10 Annotation Stability Audit

该 audit 当前为推荐 QC，不是理论 blocker。

目标：

验证“为什么选择 2024-10”能够形成 reviewer-proof provenance evidence。

重点统计：

```text
SAME_REPO_ID
BLANK_TO_VALID_REPO_ID
INVALID_TO_CORRECTED_REPO_ID
VALID_ID_TO_DIFFERENT_VALID_ID
VALID_ID_TO_BLANK
REMOVED_NON_OPEN_SOURCE
OTHER
```

重点检查：

```text
unexpected VALID_ID_TO_BLANK
```

是否为 0。

对于：

```text
VALID_ID_TO_DIFFERENT_VALID_ID
```

要求人工原因分类，不允许自动使用 event count 决定谁正确。

---

# 17. Codex 后续任务必须遵守的 Authority Hierarchy

建议 Codex 在任何 identity/source filtering correction 中使用：

```text
1. historical event numeric repo_id
   → event repository identity

2. frozen curated annotation github_repo_id
   → which repository represents the DBMS in this experiment

3. OpenDigger/GHArchive event-time payload attributes
   → historical repository attribute evidence

4. repo_name/full_name
   → descriptive/retrieval metadata

5. activity/event count
   → QC signal only
```

不得反向使用低 authority 覆盖高 authority。

---

# 18. Codex Correction Review Checklist

执行任何 versioned correction 前至少核对：

- [ ] 不修改 RefQ 理论；
- [ ] 不修改 unique membership invariant；
- [ ] 不按 `repo_name` 合并不同 numeric repo IDs；
- [ ] relation schema 明确保留 `event_repo_id`；
- [ ] `event_repo_id` 不可被 caller current ID 覆盖；
- [ ] source admission 在 MembershipRegistry 之前；
- [ ] source admission = `event_repo_id == annotated_primary_repo_id`；
- [ ] target 不要求属于 294 seed；
- [ ] related/historical repo 可以作为 expanded target；
- [ ] out-of-seed source records 在上游资产中保留；
- [ ] Fireproof 不做 ID hard-code；
- [ ] 293 unaffected seed 无 unrelated drift；
- [ ] old frozen tag/output 不覆盖；
- [ ] corrected candidate input 先做 diff gate；
- [ ] P0 只在 input correction review PASS 后重算；
- [ ] S1-S7 是否重算由 corrected P0 output drift 再决定；
- [ ] manuscript/figures 在 corrected baseline 冻结前继续 HOLD。

---

# 19. 建议的 Candidate-Input Diff Gate

versioned correction 生成 candidate upstream artifacts 后，在 P0 前应先确认：

```text
affected seed files = expected localized scope

Fireproof out-of-seed historical source records removed from RefQ source view = 120

event_repo_id preserved

target extraction semantics unchanged

no target numeric-ID conflicts

293 unaffected seeds:
no unrelated semantic/content drift
```

不要提前假定：

```text
quotient_eligible_records -= 120
```

因为 120 是受影响 Reference-record source observation 数，不等于 quotient-eligible edge weight 的最终变化。

---

# 20. 当前 Decision Ledger

```text
REFQ_THEORY =
FROZEN_UNCHANGED

PROJECT_IDENTITY_UNIT =
GITHUB_NUMERIC_REPOSITORY_ID

PRIMARY_REPOSITORY_AUTHORITY =
FROZEN_MANUALLY_CURATED_MONTHLY_ANNOTATION_SNAPSHOT

CURRENT_EVENT_SCOPE =
2023

CURRENT_ANNOTATION_SNAPSHOT =
2024-10

CURRENT_ANNOTATION_FILE =
dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv

ANNOTATION_ROLE =
POST_SCOPE_CURATED_REPOSITORY_MAPPING_SNAPSHOT

ACTIVITY_COUNT_ROLE =
QC_SIGNAL_ONLY

10X_ACTIVITY_DIFFERENCE =
OPTIONAL_MANUAL_REVIEW_TRIGGER
NOT_SELECTION_RULE

REFQ_SOURCE_OBSERVATION =
PRIMARY_ANNOTATED_REPO_ID_ONLY

SOURCE_ADMISSION =
event_repo_id == annotated github_repo_id

FILTER_BOUNDARY =
REFQ_OBSERVATION_VIEW
BEFORE_MEMBERSHIP_AND_QUOTIENT

TARGET_POLICY =
KEEP_ALL_PROJECT_MAPPABLE_TARGETS

RELATED_REPOSITORY_POLICY =
PRESERVE_UPSTREAM
DO_NOT_COLLAPSE_IDENTITY
EXCLUDE_AS_SOURCE_IF_NOT_SEED
ALLOW_AS_EXPANDED_TARGET

OPEN_SOURCE_ELIGIBILITY =
CURATED_ANNOTATION / LICENSE FILTER

EVENT_PAYLOAD_LICENSE =
HISTORICAL_ATTRIBUTE_EVIDENCE
NOT RECORD-LEVEL ADMISSION RULE

MONTHLY_ANNOTATION_HISTORY =
PROVENANCE
NOT LINEAGE

FIREPROOF_POLICY =
STRICT_REPOSITORY_IDENTITY

FIREPROOF_HISTORICAL_REPO =
600271677

FIREPROOF_PRIMARY_SEED =
679889516

FIREPROOF_OUT_OF_SEED_REFERENCE_RECORDS =
120

CURRENT_P0_NUMERICAL_BASELINE =
PROVENANCE_ANCHOR
SCIENTIFICALLY_SUPERSEDED_PENDING_CORRECTION

CORRECTION_IMPLEMENTATION =
NOT_YET_COMPLETED

PHASE2B_1 =
HOLD

PHASE2C =
HOLD
```

---

# 21. 关键链接

## OSDB_RefQ

Repository：

https://github.com/birdflyi/OSDB_RefQ

README：

https://github.com/birdflyi/OSDB_RefQ/blob/main/README.md

P0 config：

https://github.com/birdflyi/OSDB_RefQ/blob/main/configs/ch5_reference_quotient_p0.yaml

2024-10 frozen DBMS repository annotation：

https://github.com/birdflyi/OSDB_RefQ/blob/main/data/github_osdb_data/dbfeatfusion_records_202410_automerged_manulabeled_with_repoid.csv

Zenodo data release：

https://doi.org/10.5281/zenodo.18817348

---

## Monthly DBMS repository annotation upstream

https://github.com/birdflyi/od_label_issue_gen/tree/main/data/database_repo_label_dataframe

---

## OpenDigger / GHArchive

OpenDigger GitHub data source documentation：

https://open-digger.cn/docs/user-docs/data-sources/github#数据来源

GHArchive：

https://www.gharchive.org/

GHArchive example download：

```bash
wget https://data.gharchive.org/2015-01-01-15.json.gz
```

---

# 22. GHArchive Payload Mini Samples

以下只保留结构样例，不复制完整 event JSON。

## 22.1 PullRequestEvent repository license

```json
{
  "type": "PullRequestEvent",
  "payload": {
    "pull_request": {
      "base": {
        "repo": {
          "id": 132188670,
          "full_name": "jkuhlmann/cgltf",
          "license": {
            "key": "mit",
            "name": "MIT License",
            "spdx_id": "MIT"
          }
        }
      }
    }
  }
}
```

同一种 event schema 的其他样本也可能出现：

```json
"license": null
```

因此 payload license availability 不能作为 open-source sample eligibility gate。

---

## 22.2 ForkEvent repository license

```json
{
  "type": "ForkEvent",
  "payload": {
    "forkee": {
      "id": 237828381,
      "full_name": "mafertoken/assets",
      "license": {
        "key": "mit",
        "name": "MIT License",
        "spdx_id": "MIT"
      }
    }
  }
}
```

这说明 repository attribute availability 与 event payload schema 有关。

---

# 23. 维护者快速判断规则

以后遇到 repository identity / event filtering 问题，按下面顺序判断：

```text
Q1. 这是哪个 event？
→ 看 event_id / event_time

Q2. event 当时属于哪个 repository？
→ 看 numeric event_repo_id

Q3. 当前冻结研究中哪个 repository 代表这个 DBMS？
→ 看 frozen annotation snapshot 的 github_repo_id

Q4. 两个 repo_name 相同但 ID 不同怎么办？
→ 保持 distinct identities

Q5. historical/related repo 数据要删吗？
→ 上游不删

Q6. 它能作为当前 seed source 吗？
→ 只有 event_repo_id == annotated seed repo_id 才能

Q7. 它能作为 target 吗？
→ project-mappable 时可以作为 expanded target

Q8. event count 很高能覆盖人工标注吗？
→ 不能，只触发 review

Q9. event payload license=null 怎么办？
→ 不影响 curated open-source eligibility

Q10. 后续月度 annotation 改了怎么办？
→ 新 analysis version；不 silent mutate 旧 release
```

---

# 24. 仍待完成事项

按优先级：

```text
P0-A
2024-01 → 2024-10 annotation stability audit
（推荐 QC，非理论 blocker）

P0-B
Versioned repository-identity correction protocol design

P0-C
Candidate relation / aggregate / RefQ observation-view correction

P0-D
Candidate-input old/new diff gate

P0-E
Corrected P0 rerun

P0-F
Determine required supplemental S1-S7 reruns

P0-G
Corrected manuscript / figures / Phase2B.1 / Phase2C
```

其中 P0-B～P0-E 是当前科学 correction 主链。

---

# 25. Report Provenance / Evidence Status

本报告综合以下已完成审计和已核查资产：

- Corrected-Baseline Semantic Reuse Audit v2；
- Repository Identity Provenance Impact Audit v1.1；
- Fireproof Seed Identity and Observation Boundary Decision Audit v1；
- current `OSDB_RefQ` README；
- current P0 config；
- frozen 2024-10 DBMS repository annotation；
- `od_label_issue_gen` monthly annotation upstream；
- GHArchive raw JSON sample；
- 当前项目维护者关于 OpenDigger relational schema / annotation-maintenance process 的说明。

其中：

- Fireproof numeric impact 已经机器审计；
- `STRICT_REPOSITORY_IDENTITY` 已人工接受；
- 2024-01 → 2024-10 annotation change taxonomy 目前仍建议通过独立 audit 做机器化确认；
- 不应把尚未执行的 annotation-stability audit 写成已完成事实。

---

# 26. 一句话总原则

> **历史事实尽量完整保留；numeric repo ID 负责身份；冻结人工标注负责选择 DBMS 的 primary repository；OpenDigger/GHArchive 提供时间化历史证据；RefQ 只在 observation-view 入口过滤 source participation，并保持 target expansion 与上游事实资产完整性。**
