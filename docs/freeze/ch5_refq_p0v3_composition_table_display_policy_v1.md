# Chapter 5 RefQ Composition Table Display Policy v1

`policy name = COMPOSITION_DISPLAY_POLICY_V1`

`scope = Table 4.1 / Table 4.2 only`

This is a deterministic main-text presentation rule for descriptive composition tables whose mutually exclusive categories partition the same admitted-record universe. The complete frozen distributions remain the scientific authority.

## Rule

1. Sort frozen categories by count descending, with a stable lexical category-name tie-break.
2. Display categories individually until cumulative exact coverage reaches at least 95%.
3. A category with frozen share at least 5% must never be hidden in `Other`.
4. Aggregate every remaining tail row into one display-only `Other` row.
5. `Other` is the exact sum of the underlying frozen tail rows.
6. Compute each displayed share independently from its frozen count and denominator 3,747,958, then round to two decimal places.
7. Do not force component shares to sum to 100.00%; round-balancing is prohibited. The Total row remains 100.00%.

`coverage_threshold = 95%`

`coverage_threshold_semantics = PRESENTATION_ONLY`

`materiality_guard = 5%`

`5_percent_semantics = PRESENTATION_ONLY_NOT_STATISTICAL_SIGNIFICANCE`

The 5% guard is not alpha, a significance level, a p-value threshold, or an effect-size threshold. The 95% rule is only a cumulative main-text coverage criterion. Neither has inferential meaning and neither applies to Table 4.8 or any non-composition table.

For Table 4.1, the five individually displayed categories cover 95.619588053014% (`95.62%` displayed), and `Other=164,176` is the exact sum of PullRequestReview 72,597, PullRequestReviewComment 52,761 and CommitComment 38,818. For Table 4.2, the seven individually displayed categories cover 95.558167941049% (`95.56%` displayed), and `Other=166,478` is the exact sum of all twelve remaining frozen rows. `GitHub_Files_FileChanges=193,391` (5.16%) is therefore displayed individually under the materiality guard.

This policy changes presentation only. It does not change scientific values, the complete frozen distributions, Figure 1 policy, or any other manuscript table.
