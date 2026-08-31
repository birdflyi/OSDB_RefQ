# Chapter 5 RefQ — Framework Hierarchy Terminology Micro-Fix

## Decision

CH5_REFQ_FRAMEWORK_HIERARCHY_TERMINOLOGY_FIX_PASS

This is a single-fragment publication-wording correction after the accepted
CH5_REFQ_FRAMEWORK_DERIVED_HIERARCHY_REWRITE_PASS.  The manuscript remains
external to this repository.  No scientific result, hierarchy, RQ wording,
table, figure, code, output, or dissertation governance document was changed.

## 1. Starting identities

| Item | Value |
|---|---|
| Repository | D:/github_repo/OSDB_RefQ |
| Branch | ch5-refq-repository-identity-correction-v1 |
| repository_HEAD_before | 7640485ed00dcbd844a3313f57ac10bff99de1d8 |
| remote_HEAD_before | 7640485ed00dcbd844a3313f57ac10bff99de1d8 |
| Authoritative manuscript | C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md |
| Manuscript SHA before | 8ABC48751979461E2E8CC7389731FEB6BA5A6335CDF05706265BD1B4ED50248B |
| Read-only baseline copy | C:/Users/10651/AppData/Local/Temp/ch5_refq_hierarchy_terminology_micro_fix_baseline_20260831.md |
| Baseline-copy SHA | 8ABC48751979461E2E8CC7389731FEB6BA5A6335CDF05706265BD1B4ED50248B |
| Manuscript location in Git | External; not tracked by OSDB_RefQ |
| Prior accepted hierarchy record | docs/freeze/ch5_refq_framework_derived_hierarchy_rewrite.md |

The four pre-existing untracked rendering archives were preserved and not
staged:

~~~text
figures/ch5_refq/p0v3_final_v3.zip
figures/ch5_refq/p0v3_final_v4.zip
figures/ch5_refq/p0v3_final_v5.zip
figures/ch5_refq/p0v3_final_v6.zip
~~~

## 2. Authorized issue and exact correction

The standalone manuscript used the internal dissertation shorthand “严格商化”
in the core §1.3 construction sentence.  The underlying meaning is
quotient/coarse-graining under semantic membership, but the shorthand is not
preferred publication-facing terminology.  Existing publication terminology
already includes semantic membership quotient, quotient construction,
membership-induced graph coarsening, and block aggregation.

Exact before fragment:

~~~text
将其中满足项目映射条件的 evidence 严格商化为可解释的项目级结构关系
~~~

Exact after fragment:

~~~text
将其中满足项目映射条件的 evidence 通过基于语义归属的 quotient construction 提升为可解释的项目级结构关系
~~~

The replacement preserves the same semantic operation and makes the
semantic-membership constraint explicit.  It does not introduce
commercialization, generic projection, or a shared-reference projection.

The complete old fragment occurred once and the complete new fragment occurs
once.  UTF-8 byte lengths are 94 and 138 respectively.  Removing the old
fragment from the baseline and the new fragment from the edited manuscript
leaves an identical 121,044-byte remainder:

~~~text
OLD_FRAGMENT_OCCURRENCES_BEFORE = 1
OLD_FRAGMENT_OCCURRENCES_AFTER = 0
NEW_FRAGMENT_OCCURRENCES_BEFORE = 0
NEW_FRAGMENT_OCCURRENCES_AFTER = 1
OLD_FRAGMENT_UTF8_BYTES = 94
NEW_FRAGMENT_UTF8_BYTES = 138
UNCHANGED_REMAINDER_UTF8_BYTES = 121044
UNCHANGED_REMAINDER_SHA256_BEFORE = 1DAFC3D8F9B3E7014FDD0918BD431A9CB12BF8ECA165F92E38C679B378B12077
UNCHANGED_REMAINDER_SHA256_AFTER = 1DAFC3D8F9B3E7014FDD0918BD431A9CB12BF8ECA165F92E38C679B378B12077
~~~

## 3. Scope closure

Only the authorized terminology fragment in §1.3 differs:

~~~text
SECTION_1_3_TERMINOLOGY_FRAGMENT_CHANGED = 1
OTHER_SECTION_1_3_TEXT_CHANGED = 0
SECTION_1_4_CHANGED = 0
RESULTS_ROADMAP_CHANGED = 0
DISCUSSION_5_4_CHANGED = 0
CONCLUSION_CHANGED = 0
ABSTRACT_CHANGED = 0
RELATED_WORK_CHANGED = 0
METHODS_CHANGED = 0
RQ_TEXT_CHANGED = 0
FIGURE_CAPTION_CHANGED = 0
TABLE_CONTENT_CHANGED = 0
AUTHORIZED_MANUSCRIPT_FRAGMENT_CHANGE_COUNT = 1
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
~~~

DISSERTATION_FRAMEWORK_SHORTHAND_CHANGED = 0 means that no dissertation
framework or governance document was edited.  The ambiguous shorthand was
removed only from the standalone manuscript:

~~~text
DISSERTATION_FRAMEWORK_SHORTHAND_CHANGED = 0
MANUSCRIPT_AMBIGUOUS_SHANGHUA_OCCURRENCES = 0
MANUSCRIPT_COMMERCIALIZATION_OCCURRENCES = 0
MANUSCRIPT_PROJECT_COMMERCIALIZATION_OCCURRENCES = 0
~~~

The six pre-existing occurrences of “shared-reference projection” and all
other technical terminology remain unchanged; the replacement adds none.

## 4. Semantic hierarchy closure

The accepted hierarchy is preserved:

~~~text
fine-grained Reference evidence
→ endpoint eligibility + semantic membership
→ quotient construction / membership-induced aggregation
→ Project-level RefQ / RefQN
→ seed-centered role separation
→ structural characterization
~~~

~~~text
CORE_ACADEMIC_PROBLEM = PASS
QUOTIENT_CONSTRUCTION_MEANING = PASS
SEMANTIC_MEMBERSHIP_MEANING = PASS
PROJECT_LEVEL_STRUCTURAL_RELATION = PASS

RQ1_BOUNDARY_ROLE = PASS
RQ2ABC_STRUCTURAL_CENTER = PASS
RQ3_BOUNDED_EVALUATION = PASS

FACT_LAYER_LEAKAGE = NO
STRUCTURE_LAYER_DILUTION = NO
TASK_LAYER_LEAKAGE = NO
ACCESS_LAYER_LEAKAGE = NO
~~~

No wording change reopens §1.3 hierarchy, §1.4 RQ hierarchy, contribution
hierarchy, the Results roadmap, §5.4 synthesis, or the Conclusion hierarchy.

## 5. Numeric, citation, and protected-content guards

The before/after full-manuscript checks use the same UTF-8 text and the
following numeric-token expression:

~~~text
NUMERIC_TOKEN_REGEX = (?<![A-Za-z0-9_])\d[\d,]*(?:\.\d+)?(?![A-Za-z0-9_])
~~~

~~~text
MANUSCRIPT_SHA_BEFORE = 8ABC48751979461E2E8CC7389731FEB6BA5A6335CDF05706265BD1B4ED50248B
MANUSCRIPT_SHA_AFTER = 05232481C69BAAAE468F636D443D928D4162CE4864A72B796F2AC5603E5CC5B4
NUMERIC_TOKEN_COUNT_BEFORE = 991
NUMERIC_TOKEN_COUNT_AFTER = 991
NUMERIC_TOKEN_CHANGE_COUNT = 0
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
CITATION_SET_CHANGED = 0
CITATION_OCCURRENCES_BEFORE = 68
CITATION_OCCURRENCES_AFTER = 68
RQ_TEXT_CHANGED = 0
RQ_COUNT_BEFORE = 5
RQ_COUNT_AFTER = 5
FIGURE_CAPTION_CHANGED = 0
FIGURE_CAPTION_COUNT_BEFORE = 4
FIGURE_CAPTION_COUNT_AFTER = 4
TABLE_CONTENT_CHANGED = 0
TABLE_ROW_COUNT_BEFORE = 126
TABLE_ROW_COUNT_AFTER = 126
~~~

All non-§1.3 top-level sections have identical UTF-8 slices.  The only
top-level mismatch is the expected §1 引言 slice containing the authorized
fragment:

~~~text
NON_1_3_TOP_LEVEL_SECTION_MISMATCH_COUNT = 0
ABSTRACT_CHANGED = 0
RELATED_WORK_CHANGED = 0
METHODS_CHANGED = 0
RESULT_VALUES_CHANGED = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
~~~

## 6. Scientific and execution guards

~~~text
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
tables_changed = 0
figure_caption_changed = 0
~~~

No experiment, pipeline, rendering command, scientific recomputation, or
repository output regeneration was performed.

## 7. Final status

~~~text
manuscript_files_changed = 1
SECTION_1_3_TERMINOLOGY_FRAGMENT_CHANGED = 1
OTHER_SECTION_1_3_TEXT_CHANGED = 0
UNAUTHORIZED_MANUSCRIPT_REGION_CHANGE_COUNT = 0
MANUSCRIPT_SHA_AFTER = 05232481C69BAAAE468F636D443D928D4162CE4864A72B796F2AC5603E5CC5B4

repository_HEAD_before = 7640485ed00dcbd844a3313f57ac10bff99de1d8
commit_message = docs(ch5): polish quotient terminology in hierarchy wording
commit_hash = reported from final repository HEAD after this docs-only commit
push_status = reported after remote verification
~~~

Only this audit document is authorized for the repository commit.
