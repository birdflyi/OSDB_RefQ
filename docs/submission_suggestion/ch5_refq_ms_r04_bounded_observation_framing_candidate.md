# Chapter 5 RefQ — MS-R04 Bounded Observation-Framing Candidate Audit

```text
TASK = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_REVISION
TASK_TYPE = BOUNDED_SEMANTIC_SOURCE_REVISION
BASE_REVISION = MS-R03
BASE_REPOSITORY_HEAD = 8055caf596621510176bccc34d81daa1594f7bdf
BRANCH = ch5-refq-repository-identity-correction-v1
```

This record documents a candidate only. MS-R04 was not promoted, CURRENT was
not replaced, and no accepted MS-R04 snapshot, sidecar, or manifest revision
was created.

## 1. Base authority and candidate identity

| Item | Value | Status |
|---|---|---|
| MS-R03 CURRENT | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_CURRENT.md` | protected |
| MS-R03 snapshot | `.../versions/MS-R03_POST_SUBMISSION_CONDENSED_E59F96FF.md` | protected |
| CURRENT SHA-256 before | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| MS-R03 snapshot SHA-256 before | `E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9` | PASS |
| Candidate | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/working/MS-R04_BOUNDED_OBSERVATION_FRAMING_CANDIDATE.md` | created outside repository |
| Candidate SHA-256 | `8F094C7187A9258F7053B5097862AE335C4183E07F731968D95C98202DA89E98` | recorded |
| Candidate base relation | full MS-R03 snapshot copied byte-for-byte before patching | PASS |

Repository preflight passed: local and remote HEAD were both
`8055caf596621510176bccc34d81daa1594f7bdf`. The four pre-existing V3–V6 ZIP
files remained untouched and untracked.

## 2. Authorized edit map

```text
MSR04_FRAME_A = APPLIED
MSR04_FRAME_D = APPLIED
MSR04_FRAME_E = NOT_APPLIED
```

### A — Related Work bridge

Location: after the existing §2.2 Reference Coupling paragraph and before the
IREL paragraph.

Before context (MS-R03):

> Reference Coupling 研究为利用 cross-reference 识别项目间关联提供了软件工程领域依据。Blincoe 2015/2019 的经验工作以 Issue/PR/Commit comments 中指向其他 repository 的 Issue/PR 或 Commit references 为核心，已经建立 directed project-level graph，并以 project-pair cross-reference count 作为 edge weight，进而开展 ecosystem/community 或 dependency-oriented analysis [@blincoe2015ecosystems; @blincoe2019referencecoupling]。这里的方向仅表示 cross-reference direction，并不自动表示真实 technical dependency direction。本文承认 project-level aggregation、direction 和 count-weighting 已有先例，不把这些操作单独作为 novelty；本文的 RefQ 是对该类 direct project-reference relation 的 formalization/reframing，而不是替代或重新发明 Reference Coupling。

After:

> Repository-derived relations and network representations have proved useful for empirical software engineering, while methodological work also shows that repository sampling, data semantics, and network construction condition what can be inferred from them [@kalliamvakou2014promises; @mcclean2021ossocialnetwork]. Reference Coupling demonstrates that stronger dependency-oriented semantics can be supported when the relation scope is specifically validated under its own sampling and relation definition [@blincoe2019referencecoupling]. RefQ addresses a complementary setting: it retains a broader heterogeneous universe of explicit Reference evidence and therefore makes endpoint eligibility, semantic membership, observation completeness, and metric interpretation explicit rather than assigning uniformly stronger semantics to every project-level edge.

The paragraph uses Kalliamvakou only for bounded GitHub mining/data
interpretation care, McClean for variation in OSS network data sources and
constructions, and Blincoe for its own validated dependency-oriented scope.
It does not characterize prior work as wrong or invalid.

### D — Observation / network-boundary validity

Location: §6.3 External Validity, after the existing statement of the
seed-centred boundary and before §6.4.

Before context (MS-R03):

> 同时，本文关注 DBMS 技术与维护语境，这一语境限制了结果向 Web 框架、机器学习库、移动应用或云原生基础设施项目的直接外推；是否存在系统性的跨领域差异仍需专门比较研究验证。当前 RefQN 是 seed-centered observed quotient network：294 个 seed projects 具有完整 source observation，而 expanded target nodes 不具有对称 source observation。因此，本文结果是开源 DBMS 场景内的有界经验发现，不是完整 GitHub ecosystem network 或所有 OSS 生态的普遍规律。

After:

> Observation / network-boundary validity. Expanded target projects enter RefQN because they are referenced by the 294 seed projects; they are not an independently source-sampled population. Under the current observation contract, the 294 seeds are source-complete, whereas expanded targets are source-incomplete, so missing or unobserved source behavior for an expanded target must not be interpreted as observed zero activity. Valid interpretation is therefore population-specific: RQ2a uses the source-complete seed population, RQ2b uses the observable target population, and RQ2c uses a first-order direction-ignored derived structural view. Ignoring direction does not restore missing source observations or transform the seed-centered network into a fully observed ecosystem graph; the research design defines the observation boundary, and that boundary defines the admissible metric interpretation.

This paragraph restates the existing estimand and population contracts. It does
not introduce a new dataset, metric, result, or scientific value.

### E — Conclusion

`MSR04_FRAME_E = NOT_APPLIED`.

§9 already states the traceable RefQ construction, seed-centred observation,
source/target role asymmetry, first-order undirected boundary, bounded uses and
stronger-semantic exclusions. A new sentence would be redundant after FRAME-D.

### BIB — required bibliography addition

Added exactly one entry and one citation key:

```text
`kalliamvakou2014promises` Kalliamvakou, E., Gousios, G., Blincoe, K., Singer, L., German, D. M., & Damian, D. (2014). The promises and perils of mining GitHub. Proceedings of the 11th Working Conference on Mining Software Repositories, 92-101. ACM. https://doi.org/10.1145/2597073.2597074
```

The metadata was checked through Crossref. No unrelated bibliography cleanup
was performed.

## 3. Complete diff audit

```text
CHANGED_HUNK_COUNT = 3
HUNK_A_COUNT = 1
HUNK_D_COUNT = 1
HUNK_BIB_COUNT = 1
HUNK_E_COUNT = 0
UNMAPPED_CHANGED_HUNKS = 0
UNAUTHORIZED_CHANGED_HUNKS = 0
BASE_LINES_NOT_FOUND_IN_CANDIDATE = 0
```

The candidate is the complete MS-R03 snapshot plus the three authorized
insertions above. No existing line was deleted or rewritten.

## 4. Citation audit

```text
CITATION_TOKEN_OCCURRENCES_BEFORE = 67
CITATION_TOKEN_OCCURRENCES_AFTER = 70
UNIQUE_CITATION_KEYS_BEFORE = 32
UNIQUE_CITATION_KEYS_AFTER = 33
BIBLIOGRAPHY_ENTRIES_BEFORE = 32
BIBLIOGRAPHY_ENTRIES_AFTER = 33
MISSING_CITATION_KEYS = 0
ORPHAN_BIBLIOGRAPHY_ENTRIES = 0
MALFORMED_CITATION_SYNTAX = 0
```

The sole new key is `kalliamvakou2014promises`. The two additional citation
groups and three additional key occurrences are all in FRAME-A; the new
bibliography entry is its required BIB companion.

## 5. Display and structure guards

```text
RQ_COUNT = 5
RQ_TEXT_CHANGED = 0
CONTRIBUTION_COUNT = 4
CONTRIBUTION_ORDER_CHANGED = 0
MAIN_TEXT_TABLE_BLOCK_COUNT_UNCHANGED = YES
FIGURE_CAPTION_COUNT_UNCHANGED = YES
TABLE_CONTENT_CHANGED = 0
TABLE_RELOCATION_COUNT = 0
FIGURE_CAPTION_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
```

Measured before/after counts: figure captions `4/4`, table headings `14/14`,
Markdown table rows `126/126`, contribution markers `4/4`, and RQ headings
`5/5`.

## 6. Scientific guards

```text
METHODS_SCIENTIFIC_SEMANTICS_CHANGED = 0
NEW_SCIENTIFIC_VALUE_COUNT = 0
CHANGED_SCIENTIFIC_VALUE_COUNT = 0
UNDERLYING_NUMERIC_VALUE_CHANGE_COUNT = 0
Q_FORMULA_CHANGED = 0
MEMBERSHIP_CONTRACT_CHANGED = 0
SOURCE_ADMISSION_SEMANTICS_CHANGED = 0
SELF_LOOP_POLICY_CHANGED = 0
FIRST_SECOND_ORDER_BOUNDARY_CHANGED = 0
STATISTICAL_TEST_CHANGED = 0
EFFECT_SIZE_LABEL_CHANGED = 0
FDR_FAMILY_CHANGED = 0
LABEL_MODE_CHANGED = 0
CROSS_MODE_RESULT_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
```

No sampling, population, observation window, formula, metric, result, table,
figure, caption, Appendix A value, DOI, or statistical procedure was changed.
The year and DOI in the new bibliography entry are bibliographic metadata,
not changed scientific values.

## 7. Framing closure

```text
RELATED_WORK_OBSERVATION_BRIDGE = SUFFICIENT
INTRO_OBSERVATION_PROBLEM = EXPLICIT
DISCUSSION_MEASUREMENT_VALIDITY_SYNTHESIS = SUFFICIENT
OBSERVATION_NETWORK_BOUNDARY_VALIDITY = SUFFICIENT
CONCLUSION_MEASUREMENT_CONDITION_CLOSURE = SUFFICIENT
LITERATURE_POSITIONING = COMPLEMENTARY_CRITICAL
ADVERSARIAL_PRIOR_WORK_CLAIM_COUNT = 0
```

The candidate preserves the frozen centre and meta-finding:

```text
traceable + observation-aware + project-level operationalization
explicit-reference structure is measurable, but interpretation is
role-dependent, observation-bounded, metric-dependent, and label-sensitive
for the RQ3 comparison
```

## 8. Core academic sentence support

```text
C1 = SUPPORTED
C2 = SUPPORTED
C3 = SUPPORTED
C4 = SUPPORTED
```

The support comes from the unchanged MS-R03 evidence and the two new
clarifying paragraphs; no stronger platform or causal claim was introduced.

## 9. Version protection and no-promotion record

```text
CURRENT_SHA_BEFORE = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
CURRENT_SHA_AFTER = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
MS_R03_SNAPSHOT_SHA_BEFORE = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
MS_R03_SNAPSHOT_SHA_AFTER = E59F96FF05279797BD047B127B537FEA2D1FB618478DBB5455C36EA2A83777F9
CURRENT_EQUALS_MS_R03_SNAPSHOT = YES
CURRENT_REPLACED = 0
MS_R03_SNAPSHOT_REPLACED = 0
SIDECAR_REVISION_CHANGED = 0
MANIFEST_ACCEPTED_REVISION_CHANGED = 0
MS_R04_PROMOTED = 0
```

The external working candidate is intentionally not committed. Only this
repository audit record is committed.

## 10. Decision and next task

```text
DECISION = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_CANDIDATE_PASS_READY_FOR_FINAL_QA
PROMOTION = NOT_PERFORMED
NEXT_TASK = CH5_REFQ_MS_R04_BOUNDED_OBSERVATION_FRAMING_FINAL_QA
```
