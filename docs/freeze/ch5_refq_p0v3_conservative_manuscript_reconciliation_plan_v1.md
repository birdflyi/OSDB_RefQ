# Chapter 5 RefQ P0-v3 Conservative Manuscript Reconciliation Plan v1

## Status and scope

Phase A composite numeric forensics v2 passed at `58e94c115de840736b05573c84366125eb50a578`. This Phase B audit is docs-only and read-only with respect to the three external manuscripts. It does not create the final reconciled manuscript, rerun science, render figures, or build the final numeric-authority audit.

`FORENSICS_V1_STATUS = SUPERSEDED_BY_V2_FOR_RECONCILIATION_CONTROL`

## Authority model

- BASE: 8/20 OLD manuscript, used for prose, narrative order, and presentation defaults.
- SCIENCE PATCH SOURCE: `outputs/reference_quotient_p0_corrected_v3/` plus `supplemental/reference_quotient_v2/outputs_p0v3/`.
- SEMANTIC/PROVENANCE PATCH REFERENCE: latest QA manuscript.
- OLD prose wins by default; OLD numeric values never inherit automatically.
- Current WiredTiger authority is project_id 2944302, `wiredtiger/wiredtiger`, with 15,332 total, 12,891 self, 19 external-project, 1,096 non-project, 1,326 unresolved, ratio `0.8407905035220454` and display 84.08%.
- Frozen L8 action is `KEEP_CURRENT_SCIENCE_USE_HUMAN_FROZEN_CONCISE_WORDING`: 经 source-admission 后保留 3,747,958 条 Reference records，其中 1,586,047 条具有可唯一映射到项目的 target endpoint，因而满足 quotient eligibility 并进入 Project-level RefQ aggregation。
- S4 must state that canonical 35 is one deterministic reference realization; the tested range is 32--37, 42/50 ARI values are below 0.9, minimum ARI is 0.6823671359861659 and minimum pairwise ARI is 0.6092441840471735.
- S5 may state minimum Spearman 0.9998339514284217, minimum top-50 overlap 0.82 and robustness_alert=FALSE, without causal brokerage language.

## Three-way evidence

The pinned manuscript hashes are OLD `4BA2DB1B45C97D0823C4909C705FC307AA3A992E4B2C2E59096FC630A871FD88`, MIGRATED_V1 `4BA0322DD577090FF7E063A7641AFBDED44150B42825EFB343BE265F141FA56C`, and QA `D353BB462BC3D4D0C07FA572AAF5B4DF64805B7E032C0A1587F641D0F3214831`. The line counts are 870, 820, and 824; byte counts are 119739, 112360, and 112891.

The diffs are:

- OLD -> MIGRATED_V1: 157 added / 207 deleted lines.
- MIGRATED_V1 -> QA: 27 added / 23 deleted lines.
- OLD -> QA: 169 added / 215 deleted lines.
- Changed heading: `社区协作特征 -> 协作特征`.
- Actual OLD->QA changed blocks: 30; unchanged controls: 10 (`N004,N005,N006,N009,N010,N015,N017,N020,N030,N038`).

The matrix file contains one exact row for every changed block. It records the primary and secondary classification, authority, value/semantic/schema flags, recommended action, and review requirement.

Primary class counts: `REQUIRED_NUMERIC_CORRECTION`=22, `REQUIRED_DATA_SCOPE_CORRECTION`=4, `REQUIRED_SEMANTIC_BOUNDARY_CORRECTION`=2, `EDITORIAL_CONDENSATION`=1, `REQUIRED_PROVENANCE_CORRECTION`=1.
Secondary class counts: `REQUIRED_DATA_SCOPE_CORRECTION`=9, `REQUIRED_NUMERIC_CORRECTION`=3, `PROSE_REWORDING_NOT_REQUIRED_BY_SCIENCE`=1, `REQUIRED_PROVENANCE_CORRECTION`=1, `NONE`=6, `TABLE_PRESENTATION_CHANGE`=2, `REQUIRED_ROBUSTNESS_EVIDENCE`=1, `REQUIRED_SEMANTIC_BOUNDARY_CORRECTION`=6, `EDITORIAL_CONDENSATION`=1.

## Section policy

- Abstract and methods: retain OLD explanatory prose where compatible, replace all counts with current P0-v3 and use the frozen L8 sentence.
- RQ1: retain valid descriptive interpretation and restore removed result-keypoint prose selectively after current row updates. Use compact Table 4.1/4.2 only if the human presentation decision accepts the reconstructible schema; current Other values are 260866 and 434337.
- RQ2a: preserve the source-role boundary. Table 4.6c requires a presentation decision because OLD means are not directly frozen and must not be recomputed.
- RQ2b: retain the old compact metric schema with corrected current values; target shares use 3,747,958 admitted records and current weight support.
- RQ2c: merge old explanatory prose with QA's corrected topology, S4 limitation, and algorithmic labels. No stable/true community claim and no causal brokerage claim.
- RQ3: preserve current corrected values and both label modes. Table 4.7 row selection and Table 4.8 display precision are presentation decisions; do not silently inherit QA expansion.
- Discussion, validity, and appendix: keep OLD boundary prose unless QA supplies a required provenance or semantic correction. The appendix must retain current package identity, expanded-target boundary, and no-second-order statement.
- Untouched-sections guard: Introduction literature positioning, Related Work, formal RefQ definition, Discussion framing, Threats, Data/code availability, and contribution claims receive `KEEP_OLD_EXACT` unless a mapped current-scope correction is required. No `POTENTIALLY_UNSUPPORTED_CHANGE` block was found.

## Required future patch classes

1. Current P0-v3 and supplemental numbers, including the full flow and graph anchors.
2. Data-scope semantics: scanned vs admitted vs quotient-eligible records; record vs entity vs edge-weight units.
3. WiredTiger corrected profile and historical mixed-authority note.
4. L8 frozen concise wording.
5. Provenance/runtime identity, including implementation/result commit distinction and pandas versions.
6. S4 limitation and S5 stability boundary.
7. Terminology corrections such as algorithmic communities and 协作特征.
8. Formatting corrections already validated by QA.

## Result-keypoint policy

There are five OLD `结果要点` blocks (lines 398, 422, 437, 491, 521). All five were removed in QA, but all remain scientifically supported after current-value updates. The result-keypoint register marks every block `VALID_AFTER_VALUE_UPDATE`, recommends selective restoration, and requires human review for duplication with adjacent prose/tables.

## Prohibitions

Do not automatically shorten prose, expand tables, redesign tables, rewrite style, restore old numbers, or create a final authority audit before the final reconciled manuscript exists. Do not edit OLD, MIGRATED_V1, or QA. Do not modify P0-v3, the 58-file supplemental package, manifests, receipts, historical S7, figures, or scientific code.

## Future controlled execution

1. Re-hash OLD and confirm the three pinned manuscript identities.
2. Bind each retained numeric block to one current frozen path and update values atomically.
3. Apply the human presentation decisions for Tables 4.1/4.2/4.6c/4.6d/4.6e/4.6f/4.7/4.8.
4. Restore only result-keypoint prose that survives duplication review.
5. Re-run manuscript-only QA and then create the final numeric-authority audit after the reconciled manuscript is frozen.

## Decision

`P0V3_FORENSICS_V2_AND_THREE_WAY_AUDIT_PASS_READY_FOR_HUMAN_RECONCILIATION_DECISION`

