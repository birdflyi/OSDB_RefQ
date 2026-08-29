# Chapter 5 RefQ Composition Table Presentation Correction Review v1

Repository: `D:/github_repo/OSDB_RefQ`
Branch: `ch5-refq-repository-identity-correction-v1`
Repository HEAD before this task: `3621bdacac255ccc82ab57fca298e822a20923f2`

## Source and output identity

The input FINALQA manuscript was verified byte-identically before copying:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa.md`

`FINALQA_SHA = 3FF5CB4EDD5833F2C8D65BD255D5FAA5A694F509067923A2F0B674A233D9B337`

`FINALQA_BYTES = 116360`

The new external composition sibling began as an exact byte-copy with `COMPOSITION_INITIAL_SHA = 3FF5CB4EDD5833F2C8D65BD255D5FAA5A694F509067923A2F0B674A233D9B337`. It is:

`C:/Users/10651/Documents/trae_projects/thesis/ch5_analysis_reference_coupling_for_osdbms/第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md`

`COMPOSITION_FINAL_SHA = 5C54BD725BECC7FF7253EC023E83258749B1868E14A70D34722ADCC1F421BC60`

`COMPOSITION_FINAL_BYTES = 116819`

The input FINALQA, OLD, MIGRATED_V1, QA, RECONCILED manuscript, P0-v3, supplemental package, manifests, receipts, historical S7, scientific code and figure assets remained unchanged.

## Why the display policy changed

The previous fixed Top-4/Top-5 compact display hid material composition categories in `Other`. In particular, `GitHub_Files_FileChanges = 193,391 = 5.16%` was hidden in Table 4.2. This was a presentation defect, not a scientific-value defect. `COMPOSITION_DISPLAY_POLICY_V1` now sorts the complete frozen distribution by count descending, displays categories through at least 95% cumulative coverage, and prevents any individual category with share at least 5% from entering `Other`. Remaining tail rows are aggregated exactly for display only.

The 5% threshold is `PRESENTATION_ONLY_NOT_STATISTICAL_SIGNIFICANCE`: it is not alpha, a p-value threshold, a significance level or an effect-size threshold. The 95% threshold is also only a main-text cumulative-coverage criterion. The full frozen distributions remain the scientific authority. Shares are independently rounded to two decimals and no round-balancing is performed.

## Table 4.1 closure

Individually displayed categories are IssueComment, Push, PullRequest, Issue and Release. Their exact cumulative coverage is `95.619588053014%`, displayed as `95.62%`. `Other = 164,176 = 72,597 + 52,761 + 38,818`, covering PullRequestReview, PullRequestReviewComment and CommitComment. Its independently rounded share is `4.38%`. Total remains `3,747,958` and `100.00%`.

## Table 4.2 closure

Individually displayed categories are GitHub_Service_External_Links, PullRequest, Actor, Issue, Commit, GitHub_Files_FileChanges and Repo. Their exact cumulative coverage is `95.558167941049%`, displayed as `95.56%`. `GitHub_Files_FileChanges = 193,391` and `5.16%` is visible individually under the materiality guard. `Other = 166,478` is the exact sum of all twelve remaining frozen rows, with independently rounded share `4.44%`. The displayed component shares sum to `99.99%`; this is permitted independent rounding and was not corrected artificially. Total remains `3,747,958` and `100.00%`.

## Scope and immutability checks

The manuscript still contains 16 physical Markdown tables, all with valid column widths. Table 4.1 now has 7 data rows including Total; Table 4.2 now has 9 data rows including Total. Direct table comparison reports `tables_outside_4_1_4_2_changed = 0`; no scientific data cell outside the authorized composition rows changed. Table 4.8 remains exactly as FINALQA, and the 5% rule was not applied to any inferential table.

The actual manuscript numeric audit maps all current scientific numeric claims. `UNMAPPED_SCIENTIFIC_NUMERIC_CLAIMS = 0` and `SCIENTIFIC_VALUE_VERIFICATION_FAILURES = 0`. Newly visible Release, GitHub_Files_FileChanges and Repo values are existing frozen rows; only Other values are deterministic display sums.

All five result-keypoint findings remain semantically retained. Explicit `**结果要点**` headings remain `0`. RK001 and RK002 excerpts change only because their immediately adjacent composition prose now reflects the policy-driven rows; RK003, RK004 and RK005 remain textually unchanged. The detailed check is recorded in `ch5_refq_p0v3_compositionfix_result_keypoint_check_v1.csv`.

Figure 1 policy is unchanged: future Figure 1 Panel B uses all eight frozen source-event rows. No figure was rendered.

Execution counts are all zero: `P0_RUN=0`, `S1_RUN=0`, `S2_RUN=0`, `S3_RUN=0`, `S4_RUN=0`, `S5_RUN=0`, `S6_RUN=0`, `S7_RUN=0`, `GH_CORE_RUN=0`, `EVENT_REJOIN=0`, `FIGURES_GENERATED=0`, `scientific_logic_change_count=0`.

`COMPOSITION_PRESENTATION_COMMIT_A` and `COMPOSITION_PRESENTATION_CLOSURE_COMMIT_B` are recorded after the two docs-only commits.

## Decision

`P0V3_COMPOSITION_PRESENTATION_PASS_READY_FOR_FIGURE_RENDERING`
