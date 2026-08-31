# Chapter 5 RefQ - Submission Editing Batch E: Discussion and Conclusion

## Decision

`CH5_REFQ_SUBMISSION_EDIT_BATCH_E_DISCUSSION_CONCLUSION_PASS`

This record documents the bounded, prose-only edit of the external
authoritative manuscript in §5.1-§5.4 and §9.  The edit interprets the frozen
results, positions the contribution relative to the already audited literature,
and compresses the conclusion.  No scientific output, code, table, caption,
figure, manifest, receipt, or experiment was changed.

## 1. Starting identity

| Item | Value |
|---|---|
| Repository | `D:/github_repo/OSDB_RefQ` |
| Branch | `ch5-refq-repository-identity-correction-v1` |
| `repository_HEAD_before` | `8a2d6456bf04f729b3efe3a6e5ee9426a2279e49` |
| `remote_HEAD_before` | `8a2d6456bf04f729b3efe3a6e5ee9426a2279e49` |
| Authoritative manuscript | `C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md` |
| Read-only baseline | `C:/Users/10651/AppData/Local/Temp/ch5_refq_batch_e_discussion_conclusion_baseline_20260831.md` |
| Manuscript SHA before | `34A8F0D63BA93C30361FA16529F0AD1C1970E18AA74FE8FB55EE1C42A94CEB16` |
| Baseline-copy SHA | `34A8F0D63BA93C30361FA16529F0AD1C1970E18AA74FE8FB55EE1C42A94CEB16` |
| Manuscript SHA after | `C729D739F00757840B8F456C18A88327946127CBEB5635DE2E08662B5D3C462C` |
| Manuscript Git status | External; not tracked by `OSDB_RefQ` |

The baseline was copied before any Batch E edit and marked read-only.  The
repository worktree at the start contained only these four pre-existing,
untracked rendering archives, all preserved and unstaged:

```text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
```

## 2. Authorized scope and frozen boundaries

Only the following manuscript regions were edited:

```text
§5.1  Reference Quotient 在开源 DBMS 生态中的解释意义
§5.2  与既有 OSS 引用网络研究的关系
§5.3  实践含义与使用边界
§5.4  RQ 归纳与解释边界
§9    结论
```

The following regions were byte-identical to the baseline:

```text
prefix through §4                         PASS (55,667 characters)
§6 Threats to Validity through §8        PASS (4,232 characters)
Appendix A and references suffix          PASS (12,203 characters)
```

Required scope status:

```text
DISCUSSION_CHANGED = 1
CONCLUSION_CHANGED = 1
ABSTRACT_CHANGED = 0
INTRODUCTION_CHANGED = 0
RELATED_WORK_CHANGED = 0
METHODS_CHANGED = 0
RESULTS_CHANGED = 0
THREATS_CHANGED = 0
AVAILABILITY_CHANGED = 0
APPENDIX_CHANGED = 0
RQ_TEXT_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
FIGURE_CAPTION_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
```

## 3. Section-role matrix

| Section | Required role | Closure |
|---|---|---|
| Results | Evidence authority: reports the frozen observations and statistical results | `PASS` |
| Discussion | Interpretation authority: explains construction, observation, and bounded meaning without re-inventorying Results | `PASS` |
| Conclusion | Compressed takeaway: construction -> supporting evidence -> semantic boundary -> future work | `PASS` |

The paper hierarchy remains:

```text
fine-grained Reference evidence
  -> endpoint eligibility + semantic membership
  -> quotient construction
  -> Project-level RefQ structural relation

RQ1       = evidence / construction-boundary support
RQ2a/b/c  = role-aware first-order structural center
RQ3       = bounded DBMS-domain evaluation
```

```text
RQ1_BOUNDARY_ROLE = PASS
RQ2ABC_STRUCTURAL_CENTER = PASS
RQ3_BOUNDED_EVALUATION = PASS
STRUCTURE_LAYER_DILUTION = NO
```

## 4. Issue table

| ID | Section | Issue | Treatment | Semantic status | Risk |
|---|---|---|---|---|---|
| E01 | §5.1 | Results inventory was repeated instead of interpreted | Recast as evidence-boundary, role-aware structural meaning, and bounded heterogeneity | `PASS` | LOW |
| E02 | §5.2 | Related Work was reproduced as a literature mini-review | Compress precedents into a contribution-positioning paragraph | `PASS` | LOW |
| E03 | §5.2 | Unsupported DBMS-versus-general-OSS comparison | Replace with interpretation within the selected DBMS setting | `PASS` | LOW |
| E04 | §5.3 | Three paragraphs repeated the same practical boundary | Consolidate into candidate-level uses plus validation conditions | `PASS` | LOW |
| E05 | §5.4 | Internal phrase `当前 RQ1 artifacts` | Replace with §4.1 descriptive-statistics wording | `PASS` | LOW |
| E06 | §5.4 | Internal shorthand `50-seed sensitivity` | Replace with `50 次不同 random seed 的 Louvain 敏感性分析` | `PASS` | LOW |
| E07 | §5.4 | Exact directed/undirected edge and community counts repeated | State operator/view and denominator distinction conceptually | `PASS` | LOW |
| E08 | §9 | Novelty/contract inventory was overly dense | Retain formalization, explicit contracts, observation boundary, and non-new-algorithm boundary in compact form | `PASS` | LOW |
| E09 | §9 | Empirical summary repeated the Results inventory | Compress to RQ1 boundary, RQ2a-c structural center, and bounded RQ3 variation | `PASS` | LOW |
| E10 | §9 | Weak-semantic disclaimers were repeated | Keep one compact boundary paragraph | `PASS` | LOW |

No proposed edit required a HIGH-risk treatment.  No scientific claim was
recomputed or upgraded.

## 5. Edit records

### §5.1 Interpretation of empirical findings

The three former result-inventory paragraphs were replaced by three
interpretive paragraphs:

1. RQ1 is treated as an evidence-composition and construction-boundary
   argument.  The wording now says that eligibility and project-mapping
   boundaries must be made explicit before project topology is discussed, and
   that RefQ complements package-dependency or code-call views by preserving
   explicit collaboration references those relation types do not directly
   encode.
2. RQ2a/b/c are interpreted as distinct source-activity, target-coverage, and
   first-order structural-position questions.  Seed-centered source/target
   asymmetry is retained as an interpretation contract; central and brokerage
   positions remain network-position observations only.
3. RQ3 is summarized as local, metric-dependent, and label-mode-sensitive
   subdomain variation, without repeating the full FDR inventory.

```text
DISCUSSION_5_1_RESULT_REPETITION_REDUCED = PASS
DISCUSSION_5_1_INTERPRETIVE_ROLE = PASS
COMPLEMENT_NOT_SUPERIORITY = PASS
```

### §5.2 Contribution positioning and bounded setting

The literature enumeration was compressed to one contribution-positioning
paragraph.  It acknowledges that direct project-reference aggregation,
Reference extraction/identity handling, and quotient/coarsening vocabulary
already have precedents.  It then defines RefQ's bounded contribution as the
explicit integration of eligibility, semantic membership, aggregation,
observation, and interpretation contracts, without claiming a new generic
graph-coarsening algorithm or a replacement for Reference Coupling.

The next paragraph explains the analytical consequences: observable and
quotient-eligible evidence remain separately traceable; source and target
roles remain distinct; first-order structural views retain their own boundary;
and project-level relations can be traced back to fine-grained evidence.
The DBMS wording is explicitly within-setting: external specifications,
drivers, toolchains, test frameworks, and implementation experience provide
context for interpreting observed evidence.  “讨论驱动” is defined only as
concentration of observed evidence in discussion-related contexts; no culture,
causal exchange, or task-resolution mechanism is inferred.

The coarse-graining paragraph was retained: artifact semantics are compressed,
edge weight records evidence multiplicity rather than motivation or strength,
and membership-resolution errors can propagate to the quotient relation.

```text
DISCUSSION_5_2_RELATED_WORK_REPETITION_REDUCED = PASS
DISCUSSION_5_2_CONTRIBUTION_INTERPRETATION = PASS
COARSE_GRAINING_INFORMATION_LOSS_RETAINED = PASS
UNSUPPORTED_DBMS_VS_GENERAL_OSS_COMPARISON = 0
DBMS_AS_BOUNDED_SETTING = PASS
CROSS_DOMAIN_EMPIRICAL_CLAIM_ADDED = 0
DISCUSSION_DRIVEN_INTERPRETATION_BOUNDED = PASS
```

### §5.3 Practical implications and limits

The three repetitive paragraphs were consolidated into two.  The first now
limits RefQ to candidate-level screening and follow-up: source-active
projects, target projects with broader coverage under seed-centered
observation, bridge-like structural candidates, qualitative/manual cases, and
organization of explicit Reference evidence.  It explicitly excludes project
quality ranking, governance judgments, and automatic maintenance decisions.

The second paragraph states the conditions for stronger downstream use:
Reference semantic classification, manual validation, longitudinal evidence
when time claims are made, and task/domain-specific validation.

```text
DISCUSSION_5_3_REDUNDANCY_REDUCED = PASS
PRACTICAL_USE_REMAINS_CANDIDATE_LEVEL = PASS
AUTOMATED_DECISION_CLAIM = 0
```

### §5.4 Compact RQ synthesis

The accepted hierarchy was retained.  `当前 RQ1 artifacts` was replaced by
`§4.1 的描述统计结果`.  The repeated `9,595`, `9,547`, and
`35-community` inventory was removed from Discussion; the text now states
that directed cross-project and direction-ignored views have different
operators, view provenance, and denominators.  The shorthand `50-seed
sensitivity` was replaced by `50 次不同 random seed 的 Louvain 敏感性分析`.
The Louvain result remains explicitly algorithmic and is not described as a
semantic community or causal mechanism.

```text
DISCUSSION_INTERNAL_TERM_RQ1_ARTIFACTS = 0
DISCUSSION_INTERNAL_TERM_50_SEED_SENSITIVITY = 0
DISCUSSION_5_4_RESULT_NUMBER_REPETITION_REDUCED = PASS
OPERATOR_VIEW_DISTINCTION = PASS
LOUVAIN_ALGORITHMIC_BOUNDARY = PASS
DISCUSSION_5_4_HIERARCHY = PASS
```

### §9 Structure-first conclusion

The conclusion now follows the required order:

1. RefQ is the constructed and formalized traceable project-level relation,
   with explicit semantic-membership, eligibility, aggregation, observation,
   and interpretation contracts; it is not a new generic graph algorithm.
2. RQ1 supplies evidence/construction-boundary support, RQ2a/b/c provide
   role-aware first-order structural characterization, and RQ3 provides
   bounded, label-mode-sensitive DBMS subdomain evidence.
3. A single compact paragraph states that RefQ is not dependency ground truth,
   task-resolution semantics, knowledge-flow causality, or an automatic
   downstream relation; stronger semantics require additional validation.
4. Longitudinal/multi-year evidence, semantic classification and manual
   interpretation, robustness/evolution work, and second-order relations
   remain future work.  `shared-reference projection`, `QQ^T`, `Q^TQ`, and
   `K=X Phi X^T` are explicitly not current experiments.

```text
CONCLUSION_STRUCTURE_FIRST = PASS
CONCLUSION_NOVELTY_BOUNDARY = PASS
CONCLUSION_CONTRACT_LIST_REDUNDANCY_REDUCED = PASS
CONCLUSION_RESULT_INVENTORY_REDUCED = PASS
CONCLUSION_WEAK_SEMANTIC_BOUNDARY = PASS
SECOND_ORDER_REMAINS_FUTURE_WORK = PASS
SECOND_ORDER_PROJECTION_RUN = 0
```

## 6. Results-Discussion-Conclusion functional matrix

| Finding | Results role | Discussion role | Conclusion role |
|---|---|---|---|
| Two-universe boundary | Full evidence and construction counts | Explain why eligibility and mapping boundaries are needed | One-line construction-boundary takeaway |
| Source/target asymmetry | Full role-specific values | Explain distinct observation roles and seed-centered limits | Compact role-aware support |
| Undirected first-order structure | Full operators and structural metrics | Explain view distinction and interpretation limits | Compact first-order structural support |
| RQ3 | Full FDR and label-mode evidence | Explain local, metric-dependent, label-sensitive variation | Bounded subdomain takeaway |
| RefQ contribution | Definition and method authority | Position explicit contracts relative to precedents | Final structure-first contribution |

`RESULT_DISCUSSION_CONCLUSION_ROLE_SEPARATION = PASS`

## 7. Removed numeric-occurrence ledger

Numeric deletion was limited to duplicate Discussion prose.  The complete
scientific values remain in Results, tables, captions, or the reproducibility
appendix.  The target-region numeric-token diagnostic found four removed
occurrences and no added numeric token:

| Value/token | Old location | Treatment and reason | Remaining authoritative location |
|---|---|---|---|
| `9,595` | §5.4 repeated directed-edge sentence | Removed duplicate inventory; directed cross-project edge count remains in §3/§4 and Figure 3 caption | Results §3.4/§4.2 and frozen Figure 3 caption |
| `9,547` | §5.4 repeated undirected-edge sentence | Removed duplicate inventory; undirected edge count remains in structural Results | Results §3.4/§4.2 and frozen Figure 3 caption |
| `35` in `35-community` | §5.4 repeated community label | Replaced by conceptual `canonical Louvain realization`; community count remains authoritative elsewhere | Results §4.2c, Figure 3 caption, Appendix A |
| `4.6` in `表 4.1 至表 4.6a` | §5.4 table-reference tail | Removed redundant table-range pointer while retaining the §4.1 authority reference | Frozen Results tables |

`50` was not lost: the old hyphenated shorthand and the new publication-facing
phrase both denote the accepted 50-run sensitivity analysis.  `2023` was
retained because the project-age statement must remain explicitly
cross-sectional.  No unique scientific value was removed.

```text
NEW_SCIENTIFIC_VALUE_COUNT = 0
SCIENTIFIC_VALUE_CHANGE_COUNT = 0
UNIQUE_SCIENTIFIC_VALUE_LOSS_COUNT = 0
DUPLICATE_NUMERIC_OCCURRENCES_REMOVED = 4
```

## 8. Citation closure

The Discussion/Conclusion target contains five citation blocks before and
after the edit, representing six citation-key occurrences.  The six-key set is
unchanged:

```text
@blincoe2015ecosystems
@blincoe2019referencecoupling
@liu2022irel
@loukas2019graphreduction
@sanchezgarcia2020quotientnetwork
@xiao2008networkquotients
```

```text
CITATION_BLOCKS_BEFORE = 5
CITATION_BLOCKS_AFTER = 5
CITATION_KEY_OCCURRENCES_BEFORE = 6
CITATION_KEY_OCCURRENCES_AFTER = 6
UNIQUE_CITATION_KEYS_BEFORE = 6 (target scope; 31 globally)
UNIQUE_CITATION_KEYS_AFTER = 6 (target scope; 31 globally)
UNIQUE_CITATION_KEY_SET_CHANGED = 0
```

No new literature was added.  The precedent citations remain represented in
Related Work and the compact §5.2 contribution paragraph.

## 9. Interpretation and cross-layer guards

The following are zero affirmative overclaims in §5 and §9.  Negative boundary
statements (for example, “not dependency ground truth”) are retained as
guards, not counted as claims:

```text
POWER_LAW_CLAIM = 0
SCALE_FREE_CLAIM = 0
HEAVY_TAIL_CLAIM = 0
LONGITUDINAL_AGE_CLAIM = 0
SEMANTIC_COMMUNITY_CLAIM = 0
PROJECT_IMPORTANCE_OVERCLAIM = 0
GOVERNANCE_EFFECTIVENESS_CLAIM = 0
KNOWLEDGE_FLOW_CAUSAL_CLAIM = 0
TASK_RESOLUTION_OVERCLAIM = 0
DEPENDENCY_OVERCLAIM = 0
CAUSAL_OVERCLAIM = 0
```

```text
FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
```

`COMPLEMENT_NOT_SUPERIORITY = PASS` and
`DBMS_AS_BOUNDED_SETTING = PASS` remain in force.  Practical implications are
candidate/evidence-support uses only; RefQ is not turned into an access-layer
system or an automated decision rule.

## 10. Internal-language audit

The audit was run only over the §5 and §9 slices.  Appendix A was intentionally
excluded, as required by the task specification.

| Term | Before | After |
|---|---:|---:|
| `artifacts` / `RQ1 artifacts` | 1 | 0 |
| `50-seed sensitivity` | 1 | 0 |
| `current corrected` | 0 | 0 |
| `S4` | 0 | 0 |
| `S5` | 0 | 0 |
| `robustness_alert` | 0 | 0 |
| `output authority` | 0 | 0 |
| `current output` | 0 | 0 |
| `test_status` | 0 | 0 |
| `reject flag` | 0 | 0 |

`DISCUSSION_INTERNAL_LANGUAGE_COUNT = 0`

## 11. Readability diagnostics

The established heuristic splits on Chinese or English terminal punctuation,
includes the terminal punctuation in sentence length, and uses `>240`
characters for the very-long threshold.  Headings, table rows, and code were
excluded from this prose diagnostic.

```text
DISCUSSION_CONCLUSION_SENTENCE_COUNT_BEFORE = 56
DISCUSSION_CONCLUSION_SENTENCE_COUNT_AFTER = 42
VERY_LONG_SENTENCE_COUNT_BEFORE = 6
VERY_LONG_SENTENCE_COUNT_AFTER = 3
MAX_SENTENCE_LENGTH_BEFORE = 430
MAX_SENTENCE_LENGTH_AFTER = 351
```

The remaining long sentences are information-dense contribution or boundary
sentences; no mechanical sentence splitting was applied.

## 12. Exact scope and immutability checks

The following read-only comparisons were made against the baseline copy:

```text
NON_DISCUSSION_CONCLUSION_PROSE_CHANGED = 0
TABLE_CHANGE_COUNT = 0
FIGURE_CAPTION_COUNT_BEFORE = 4
FIGURE_CAPTION_COUNT_AFTER = 4
FIGURE_CAPTION_EDIT_COUNT = 0
RQ_TEXT_CHANGED = 0
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
```

Additional structural counts remained unchanged:

```text
MARKDOWN_TABLE_ROWS_BEFORE = 126
MARKDOWN_TABLE_ROWS_AFTER = 126
MARKDOWN_HEADINGS_BEFORE = 65
MARKDOWN_HEADINGS_AFTER = 65
DISPLAY_MATH_OPEN_MARKERS_BEFORE = 12
DISPLAY_MATH_OPEN_MARKERS_AFTER = 12
```

Protected-slice hashes (prefix, §6-§8, and Appendix A/reference suffix) were
identical before and after.  The four rendering ZIPs were not staged, opened,
rewritten, or compared as new scientific outputs.

## 13. Scientific execution guards

This was a documentation/manuscript wording task.  No test suite, scientific
pipeline, renderer, data rebuild, or network operation was run.

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
figure_assets_changed = 0
scientific_assets_changed = 0
```

## 14. Final recommendation

All current Discussion and Conclusion composite prose claims close under the
frozen hierarchy and semantic boundaries.  The current QA manuscript has no
arithmetic or population calculation to repair, and the historical Results
authority remains unchanged.  The package is therefore ready for the next
separately authorized manuscript or submission audit; this Batch E record does
not authorize any further manuscript edit.

```text
reconciliation_readiness = READY
```

## 15. Final status

```text
repository_HEAD_before = 8a2d6456bf04f729b3efe3a6e5ee9426a2279e49
manuscript_SHA_before = 34A8F0D63BA93C30361FA16529F0AD1C1970E18AA74FE8FB55EE1C42A94CEB16
manuscript_SHA_after = C729D739F00757840B8F456C18A88327946127CBEB5635DE2E08662B5D3C462C
DISCUSSION_CHANGED = 1
CONCLUSION_CHANGED = 1
NON_DISCUSSION_CONCLUSION_PROSE_CHANGED = 0
TABLE_CHANGE_COUNT = 0
FIGURE_CAPTION_EDIT_COUNT = 0
RQ_TEXT_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
```

The manuscript remains external and is not included in the repository commit.

```text
CH5_REFQ_SUBMISSION_EDIT_BATCH_E_DISCUSSION_CONCLUSION_PASS
```
