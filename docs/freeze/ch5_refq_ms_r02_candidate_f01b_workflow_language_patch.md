# Chapter 5 RefQ MS-R02 Candidate F-01b Workflow-Language Micro-Patch

## Decision

`CH5_REFQ_MS_R02_CANDIDATE_F01B_PATCH_PASS_READY_FOR_FINAL_QA_RERUN`

This record documents a strictly bounded eight-location wording patch to the
external MS-R02 working candidate. The patch removes the eight reviewer-facing
workflow/governance phrases identified by the preceding Final QA. It does not
promote MS-R02, replace CURRENT, create an accepted snapshot, or modify any
scientific or figure asset.

## 1. Identity and scope

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| Repository HEAD before patch record | `98182cadec3bf4628c24e158508e816e2a4990e9` |
| Task base revision | `MS-R02_CANDIDATE` |
| Candidate path | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/working/MS-R02_CANDIDATE.md` |
| Candidate SHA before | `0E9CB83BC8D057EC982B1CAD2112259FD8912828AFB876949A08A0FD05EB3671` |
| Candidate SHA after | `B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC` |
| Edit authority | Section 10 of `ch5_refq_ms_r02_candidate_final_editorial_qa.md` |
| Accepted manuscript revision | `MS-R01` |

The four pre-existing untracked V3-V6 ZIP files remained untouched.

## 2. Exact eight patches

### Patch 1 — Section 3.1.1 project annotation and admission wording

```text
OLD:
冻结的 DBMS/repository annotation

NEW:
既有 DBMS/repository annotation

OLD:
当前分析不重新执行一套领域、类别或许可证谓词，也不以这些描述性目标替代实际 admission gate

NEW:
本文不重新执行一套领域、类别或许可证谓词，也不以这些描述性目标替代实际样本纳入标准

STATUS = PASS
```

The dbdb.io, DB-Engines, and category-metadata citations are unchanged.

### Patch 2 — Section 3.1.1 evidence availability

```text
OLD:
3. **冻结证据可用性门槛**：对 301 个候选项目，仅当预期的 2023 年冻结 aggregate evidence CSV 存在时才纳入分析种子，最终得到 294 个 analysis seed projects。其余 7 个候选项目因冻结 2023 evidence file unavailable 而排除，不应解释为类别、开源资格或技术多样性排除。

NEW:
3. **2023 年证据可用性标准**：对 301 个候选项目，仅当对应的 2023 年 aggregate evidence CSV 可用时才纳入分析种子，最终得到 294 个 analysis seed projects。其余 7 个候选项目因缺少相应的 2023 年 evidence file 而排除，不应解释为类别、开源资格或技术多样性排除。

STATUS = PASS
```

The 301 -> 294 plus seven evidence-unavailable exclusions chain is unchanged.
The authorized heading repeats the already-existing year `2023`; this is not a
new scientific value.

### Patch 3 — Section 3.2.2 source-admission identity

```text
OLD:
`event_repo_id == frozen annotated seed github_repo_id`。其中 `event_repo_id` 表示该历史 event row 的 repository identity，冻结标注中的 `github_repo_id` 定义当前 seed 的 primary repository。

NEW:
`event_repo_id` 必须等于相应 seed 在项目标注中的 `github_repo_id`。其中，`event_repo_id` 表示该历史 event row 的 repository identity，项目标注中的 `github_repo_id` 定义当前 seed 的 primary repository。

STATUS = PASS
```

Source admission still occurs before membership-registry, profile, and edge
aggregation. Project-mappable targets still need not belong to the seed set.

### Patch 4 — Section 3.3.3 unit-weight wording

```text
OLD:
在本文冻结实现中

NEW:
在本文采用的 unit-weight 实现中

STATUS = PASS
```

One quotient-eligible retained Reference record still contributes one RefQ
weight unit.

### Patch 5 — Section 4.2a quantile wording

```text
OLD:
冻结 quantile authority 给出 seed source out-degree 的 Q1/median/Q3/max 为 3/11/39/352，out-strength 的 Q1/median/Q3/max 为 5/26.5/192.75/43,574。

NEW:
seed-source quantiles 显示，out-degree 的 Q1/median/Q3/max 为 3/11/39/352，out-strength 的 Q1/median/Q3/max 为 5/26.5/192.75/43,574。

STATUS = PASS
```

All quantile values are unchanged.

### Patch 6 — Section 4.3 Table 4.7 wording

```text
OLD:
表 4.7 完整呈现当前 include_mixed 冻结输出中的 10 个 category rows。

NEW:
表 4.7 完整呈现 include_mixed 口径下的 10 个 category rows。

STATUS = PASS
```

The subsequent metadata/community and interpretation boundaries are unchanged.

### Patch 7 — Section 4.3.2 precision-source wording

```text
OLD:
完整精度保留于表 4.8 的冻结来源文件

NEW:
更高精度的数值保留于表 4.8 对应的分析结果文件

STATUS = PASS
```

No reported out-degree statistic or interpretation changed.

### Patch 8 — Section 4.3.3 precision-source wording

```text
OLD:
完整精度保留于冻结来源文件

NEW:
更高精度的数值保留于相应分析结果文件

STATUS = PASS
```

No project-age statistic or interpretation changed.

## 3. Exact diff and candidate identity guard

Before applying the patch, the exact authorized transformations were performed
in memory against the baseline bytes. The predicted post-patch SHA was:

```text
EXPECTED_CANDIDATE_SHA_AFTER = B1494BA3133713CAA34D3A62D99DF94878028560CD065FBCC01F0E5A897479AC
```

The actual file has exactly that SHA. Reversing only the authorized
transformations in memory reconstructs the required baseline SHA:

```text
RECONSTRUCTED_CANDIDATE_SHA_BEFORE = 0E9CB83BC8D057EC982B1CAD2112259FD8912828AFB876949A08A0FD05EB3671
```

Line-by-line comparison of the reconstructed baseline and patched candidate
identified only lines 115, 117, 161, 265, 522, 627, 651, and 655.

```text
AUTHORIZED_PATCH_REGION_COUNT = 8
CHANGED_REGION_COUNT = 8
UNMAPPED_CHANGED_REGION_COUNT = 0
UNAUTHORIZED_CHANGED_REGION_COUNT = 0
ENCODING_CHANGED = 0
LINE_ENDING_CHANGED = 0
```

The file remains UTF-8 without BOM, with LF line endings.

## 4. Residual literal scan

The main text before Appendix A contains zero occurrences of every blocked
literal:

```text
"实际 admission gate" = 0
"冻结证据可用性门槛" = 0
"冻结 aggregate evidence CSV" = 0
"frozen annotated seed github_repo_id" = 0
"在本文冻结实现中" = 0
"冻结 quantile authority" = 0
"当前 include_mixed 冻结输出" = 0
"冻结来源文件" = 0

BLOCKED_LITERAL_REMAINING_COUNT = 0
```

## 5. Workflow-language rescan

All remaining main-text occurrences of freeze/snapshot/provenance/package or
similar terms were reviewed in context rather than globally replaced.

* `NECESSARY_REPRODUCIBILITY_LANGUAGE`: fixed observation snapshots and
  activity fields; historical event identity/provenance; exact retained field
  names; project-age source field; table-display policy; Appendix A and
  data/code availability provenance.
* `NATURAL_RESEARCH_PROSE`: package dependency as an excluded interpretation;
  current analysis sample descriptions; relation semantics and observation
  boundaries.
* `INTERNAL_WORKFLOW_LEAK`: none after the eight authorized patches.

Existing wording such as the frozen activity-statistics description, frozen
2023 evidence snapshot, and frozen output field names is retained because it
identifies a fixed data snapshot or an immutable raw field rather than a
repository approval process. No new blocking phrase was found outside the
authorized regions.

```text
INTERNAL_WORKFLOW_LEAK_COUNT = 0
NEW_UNAUTHORIZED_WORKFLOW_LEAK_COUNT = 0
```

## 6. Frozen scientific guards

The candidate still contains five byte-identical RQ statements and four
contributions in their original order. The RefQ formula, membership contract,
source-admission ordering, self-loop policy, first-/second-order boundary,
statistical tests, effect-size terminology and values, FDR family, label modes,
and cross-mode conclusion are unchanged.

The numeric-token comparison differs only by one additional occurrence of the
already-present contextual year `2023` in the authorized Patch 2 heading. No
new numeric value, result, denominator, or scientific claim was introduced.

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0

RQ_TEXT_CHANGED = 0
RQ_COUNT_CHANGED = 0
RQ_COUNT = 5

CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0

Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_SECOND_ORDER_BOUNDARY_CHANGED = 0

STATISTICAL_TEST_CHANGED = 0
EFFECT_SIZE_LABEL_CHANGED = 0
EFFECT_SIZE_VALUE_CHANGE_COUNT = 0
FDR_FAMILY_CHANGED = 0
LABEL_MODE_CHANGED = 0
CROSS_MODE_RESULT_CHANGED = 0
```

The already-corrected `rank eta-squared` terminology remains present and no
`epsilon-squared` label was reintroduced.

## 7. Citation and display guards

```text
CITATION_TOKEN_COUNT = 69
UNIQUE_CITATION_KEY_COUNT = 32
BIBLIOGRAPHY_ENTRY_COUNT = 32
MISSING_CITATION_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0

FIGURE_CAPTION_COUNT = 4
MISSING_REQUIRED_DISPLAY_COUNT = 0
ORPHAN_DISPLAY_COUNT = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
```

Corrected Figure 4 hashes remain:

```text
SVG = 6EC08F8462BB13F46395678A5BFB1B5E753377399D5CFA612F85FD273B34E17A
PDF = DAF4F9C486B19F229D0D13586CFCEABA774BF7212466D7174877C57F07307C0C
PNG = 6A279AE45570C06E745DB65D3B14503B30F2AD98DAAC5C64DD8611A082FC44EA
```

## 8. Accepted-authority protection

```text
CURRENT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
MS_R01_SNAPSHOT_SHA = CF4885382474A04A2A8476C3F29460AABFF049C8BD3224F5727CD67A0C134DEE
SIDECAR_SHA = F6E76D4D9C496148B3FB78C897AC4A72A9467E8B8A404F188932FC8CBB3E0688
MANIFEST_SHA = 1CAEE8CF8D8A27451A76C9529BF449D4DB5107677C6A69BECF6ECCAA39B5B8D7

CURRENT_CHANGED = 0
MS_R01_SNAPSHOT_CHANGED = 0
SIDECAR_CHANGED = 0
MANIFEST_CHANGED = 0
NEW_ACCEPTED_REVISION_CREATED = 0
```

MS-R01 remains the accepted manuscript revision. No `versions/MS-R02_*` file
was created and CURRENT was not replaced.

## 9. Scientific execution guards

```text
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
```

## 10. Readiness and Git scope

The eight authorized F-01b issues are closed without scope expansion. The
candidate is ready for a separately authorized repeat Final QA, but is not
promoted by this patch.

```text
READY_FOR_FINAL_QA_RERUN = YES
READY_FOR_PROMOTION = NOT_EVALUATED_IN_THIS_TASK
AUDIT_PATH = docs/freeze/ch5_refq_ms_r02_candidate_f01b_workflow_language_patch.md
COMMIT_SCOPE = audit document only
```

Final decision:

`CH5_REFQ_MS_R02_CANDIDATE_F01B_PATCH_PASS_READY_FOR_FINAL_QA_RERUN`
