# Chapter 5 RefQ — Final Caption Editorial Micro-Polish

## Decision

CH5_REFQ_FINAL_CAPTION_EDITORIAL_POLISH_PASS

This record closes three narrowly authorized editorial corrections in the
already accepted Figure 2 and Figure 3 captions. Scientific caption content,
Figure 1, Figure 4, manuscript body prose, tables, equations, references,
appendix content, figure assets, and scientific outputs remain unchanged.

## 1. Starting identity

| Item | Value |
|---|---|
| Repository | D:/github_repo/OSDB_RefQ |
| Branch | ch5-refq-repository-identity-correction-v1 |
| repository_HEAD_before | b24c71ac73b4da9b07ab6e84d9b046ba6ea8c3f8 |
| remote_HEAD_before | b24c71ac73b4da9b07ab6e84d9b046ba6ea8c3f8 |
| Working tree before | Four pre-existing untracked V3/V4/V5/V6 ZIP archives only |
| Authoritative manuscript | C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md |
| Manuscript SHA before | 4CD0D743ED6B17D0DE7FB4D566296CC97664271F56014C19F2FEA0B34EF890DD |
| Manuscript SHA after | 1EE57A3FCA1B8FDCC66B9FD2C45B9E6C696AE304F582FF64A82F235C64B9A7D7 |

The manuscript is external to the repository. Its edit is recorded by exact
before/after SHA rather than represented as a Git-tracked manuscript change.

## 2. Exact authorized changes

### 2.1 Figure 2 weight-unit wording

Before:

    以 138,974 条 cross-project weight 为分母的 target-weight Top-1、Top-10 与 Top-50 share

After:

    以 cross-project RefQ total weight 138,974 为分母的 target-weight Top-1、Top-10 与 Top-50 share

This removes the record/edge classifier from an aggregated RefQ weight
denominator. The denominator and all Top-k shares are unchanged.

### 2.2 Figure 3 community-size wording

Before:

    结构摘要及 35 个 community sizes

After:

    结构摘要及 35 个 algorithmic communities 的规模分布

This identifies the display as the size distribution of the 35 algorithmic
communities. It does not change the community count, method, or semantic
limitation.

### 2.3 Figure 3 view-name grammar

Before:

    canonical seed-centered observed、seed-only induced 与 multi-seed target 三种 observation-boundary views

After:

    canonical seed-centered observed view、seed-only induced view 与 multi-seed target view 三种 observation-boundary views

This makes all three declared view names grammatically complete without
redefining any observation boundary.

## 3. Exact-difference verification

The preceding accepted caption-composition record was used as the line-level
baseline. Verification established:

- Figure 1 caption: byte-for-byte unchanged.
- Figure 4 caption: byte-for-byte unchanged.
- Figure 2 caption: exactly one authorized fragment replacement.
- Figure 3 caption: exactly two authorized fragment replacements.
- Numeric tokens in Figure 2 and Figure 3 captions: unchanged.

Applying the inverse of the three replacements in memory reconstructs the
exact pre-edit manuscript SHA:

    4CD0D743ED6B17D0DE7FB4D566296CC97664271F56014C19F2FEA0B34EF890DD

This proves that no other manuscript byte changed.

## 4. Caption closure

    FIGURE_CAPTION_COUNT = 4
    FIGURE1_CAPTION_UNCHANGED = PASS
    FIGURE2_SCIENTIFIC_CONTENT_UNCHANGED = PASS
    FIGURE3_SCIENTIFIC_CONTENT_UNCHANGED = PASS
    FIGURE4_CAPTION_UNCHANGED = PASS
    FIGURE2_WEIGHT_UNIT_WORDING_CLOSURE = PASS
    FIGURE3_COMMUNITY_SIZE_WORDING_CLOSURE = PASS
    FIGURE3_VIEW_NAME_SEMANTIC_CLOSURE = PASS
    NUMERIC_TOKEN_CHANGE_COUNT = 0

## 5. Scope and scientific immutability

    body_prose_changed = 0
    table_content_changed = 0
    figure_assets_changed = 0
    scientific_assets_changed = 0

Repository comparison for figures/ch5_refq/p0v3_final_v6, outputs, and
supplemental was empty. The four pre-existing V3/V4/V5/V6 ZIP archives remained
untracked and were not staged.

## 6. Scientific and execution guards

    NEW_SCIENTIFIC_VALUES = 0
    CHANGED_SCIENTIFIC_VALUES = 0
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

The final caption authority therefore retains the accepted scientific content
while resolving the three authorized editorial ambiguities.
