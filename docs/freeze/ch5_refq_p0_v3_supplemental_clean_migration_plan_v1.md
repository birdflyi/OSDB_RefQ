# Chapter 5 RefQ P0 v3 Supplemental Clean Migration Plan v1

Official P0 v3 is frozen in result commit
`2d284f4bc83c42ba6555a09a2e42693c5490b827`. The existing
`supplemental/reference_quotient_v2` codebase remains the single supplemental
implementation. Clean regeneration should use a new configured output root,
preferably `supplemental/reference_quotient_v2/outputs_p0v3/`, so current S1–S3
evidence remains immutable and no duplicate codebase is created.

| Stage | Current status | Clean decision | Reason |
|---|---|---|---|
| S1 | Accepted under v2 aggregate/P0 provenance | RERUN | Scientific computation does not consume community metadata, but a complete rerun avoids mixed receipts and gives S1–S6 one final supplemental implementation/runtime/provenance baseline |
| S2 | Accepted under corrected P0 v2 | RERUN_FOR_P0_V3_AUTHORITY | Clean package should bind v3 even if edge/scientific values are identical |
| S3 | Accepted under corrected P0 v2 | RERUN_REQUIRED | Community metadata and canonical parity authority changed to clean v3 |
| S4 | Blocked at v2 authority community-size closure | RUN_FROM_P0_V3 | Requires clean canonical community authority |
| S5 | Not run after S4 stop | RUN_FROM_P0_V3 | Bind canonical LCC/brokerage authority to v3 |
| S6 | Not run after S4 stop | RUN_FROM_P0_V3_AND_NEW_S4_S5 | Figure-ready source map must use clean v3 and new stability outputs |
| S7 | Not evaluated | DEFER | Separate authorization and final package boundary |

Recommended future order: freeze a supplemental-compatible runtime and final
supplemental implementation commit, then rerun S1, S2, S3, S4, S5, and S6 in
the new configured output root against official P0 v3. Do not use the P0
pandas-1.4.4 environment blindly: later supplemental serialization uses APIs
not supported by that pandas version. Do not overwrite current outputs.
Figures, manuscript edits, and S7 remain separate authorization boundaries.

This clean full rerun is preferred despite S1 runtime cost because final package
receipts must agree on the P0 v3 authority, supplemental implementation commit,
runtime, output root, and package manifest. No supplemental stage was executed
in the P0 recovery task.
