# Chapter 5 RefQ Final Manuscript Editorial QA Review v1

Repository: `D:/github_repo/OSDB_RefQ`
Branch: `ch5-refq-repository-identity-correction-v1`
Repository HEAD before editorial QA: `55cfaec14e327db3b4a529871b3e57d59db81ddf`

## Scope and source identity

This task performed a narrow editorial and control-QA patch only. The accepted reconciled manuscript matched SHA-256 `2CFA7B6E72669352EEE24B9D7A79B49063A50A967CFF1C828CE910B12F9025C1` and 120,648 bytes before work. The new `finalqa` sibling began as an exact byte-copy with the same SHA and size. The reconciled source was not modified.

The final `finalqa` manuscript is:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa.md`

Final SHA-256: `3FF5CB4EDD5833F2C8D65BD255D5FAA5A694F509067923A2F0B674A233D9B337`
Final bytes: `116360`

Immutable source SHA-256 baselines: OLD `4BA2DB1B45C97D0823C4909C705FC307AA3A992E4B2C2E59096FC630A871FD88`; MIGRATED_V1 `4BA0322DD577090FF7E063A7641AFBDED44150B42825EFB343BE265F141FA56C`; QA `D353BB462BC3D4D0C07FA572AAF5B4DF64805B7E032C0A1587F641D0F3214831`; RECONCILED `2CFA7B6E72669352EEE24B9D7A79B49063A50A967CFF1C828CE910B12F9025C1`. All four source artifacts remained byte-identical.

## Control-document correction

The prior review stated that all five result-keypoint findings were retained semantically exactly once. That statement was too strong: the actual reconciled manuscript still contained five explicit `**结果要点**` blocks next to prose that already carried the same findings.

`PREVIOUS_RESULT_KEYPOINT_DEDUP_GATE = FALSE_POSITIVE`

This was an editorial/control-audit defect, not a scientific-result defect. The historical v1 disposition and review files remain immutable. The corrected v2 disposition records all five findings as `MERGED_INTO_RESULT_PROSE`, with every duplicate block removed and semantic retention passing.

## Applied narrow patch

- Removed the immediately duplicated standalone L8 sentence in section 3.1.1 while retaining the integrated frozen flow semantics.
- Merged RK001 and RK002 boundary language into the result prose and removed their explicit duplicate blocks.
- Removed the duplicate RK003 block because the adjacent self-reference prose already retains the distribution, corrected WiredTiger, SSDB, GreatSQL and H2 results.
- Merged RK004 complementarity and non-causal boundary into the section 4.1.2 result prose and removed the duplicate block.
- Removed the duplicate RK005 block because the adjacent prose already retains the cross-sectional design, weak magnitudes, complementary signs and non-causal interpretation.
- Replaced the unsupported RQ2a mean-dependent sentence with a quantile-to-maximum right-tail description; no mean was computed or inserted.
- Changed `表 4.6c（Block B）` to `表 4.6c（续）` without changing rows or values.
- Changed the Table 4.6f header from `Community` to `Louvain community label` without changing IDs or values.
- Replaced ambiguous future-work community wording with manual annotation of algorithmic communities and cross-year algorithmic-partition stability/evolution analysis.

## Result-keypoint closure

Explicit `**结果要点**` headings before: `5`
Explicit `**结果要点**` headings after: `0`
Local duplicate finding blocks after: `0`

RK001 through RK005 each retain their required scientific finding in normal result prose. The detailed location, exact excerpt, authority and disposition are recorded in `ch5_refq_p0v3_final_result_keypoint_disposition_v2.csv`.

## Table and numeric immutability

The actual `finalqa` manuscript contains 16 physical Markdown tables, all with internally consistent column widths. Fourteen are scientific-table blocks. The reconciled and `finalqa` table-data rows were compared directly: `SCIENTIFIC_TABLE_CELL_CHANGES = 0`. The only header change is the authorized Table 4.6f label; the only caption change is the authorized Table 4.6c continuation label.

An actual-manuscript numeric-token comparison found no values present in `finalqa` that were absent from the reconciled input. Removed occurrences are confined to the deleted duplicate L8 sentence and duplicate result-keypoint prose. No value substitution occurred.

`NEW_SCIENTIFIC_NUMERIC_VALUES = 0`
`CHANGED_SCIENTIFIC_NUMERIC_VALUES = 0`
`UNMAPPED_FINAL_SCIENTIFIC_NUMERIC_CLAIMS = 0`
`SCIENTIFIC_VALUE_VERIFICATION_FAILURES = 0`

WiredTiger remains 15,332 total and 12,891 self-reference records, displayed as 84.08%. The L8 flow remains `3,748,078 - 120 = 3,747,958`, with `1,586,047` quotient-eligible records. S4 remains `ACCEPT_WITH_LIMITATION`, S5 remains `robustness_alert=FALSE`, and S7 remains `KEPT_FIXED_OBJECT`.

## Community terminology rescan

Every occurrence of `社区`, `community` and `communities` was classified. Background occurrences refer to open-source community governance or cited ecosystem/community literature. Empirical analytic occurrences explicitly refer to Louvain or algorithmic communities, community IDs as algorithmic labels, or an algorithmic modular-neighborhood view. The Table 4.6f column now says `Louvain community label`. Future work now refers to manual thematic annotation of algorithmic communities and cross-year algorithmic-partition stability/evolution analysis. Bibliographic title occurrences are literature metadata.

`ANALYTIC_COMMUNITY_AMBIGUITIES = 0`

No statement equates a community with a DBMS technical subdomain, collaboration scale, stable true community or semantic natural community.

## Immutability and execution zeros

OLD, MIGRATED_V1, QA and RECONCILED manuscript hashes remained unchanged. P0-v3, the final supplemental package, manifests, receipts, historical S7, scientific code and all figure assets were read-only.

`P0_RUN=0`, `S1_RUN=0`, `S2_RUN=0`, `S3_RUN=0`, `S4_RUN=0`, `S5_RUN=0`, `S6_RUN=0`, `S7_RUN=0`, `GH_CORE_RUN=0`, `EVENT_REJOIN=0`, `FIGURES_GENERATED=0`, `scientific_logic_change_count=0`.

## Decision

`P0V3_FINAL_MANUSCRIPT_EDITORIAL_QA_PASS_READY_FOR_FIGURE_RENDERING`

`FINAL_MANUSCRIPT_EDITORIAL_QA_COMMIT = d4ad6b633c95eb2dcdea165c48ccc3cfd68d9a3f`
`push_status = PASS`
