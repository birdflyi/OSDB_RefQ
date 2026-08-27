# Chapter 5 RefQ P0 v3 Supplemental Clean Migration Plan v1

The existing `supplemental/reference_quotient_v2` implementation remains the
single implementation. Clean regeneration should use a new configured output
root, for example `supplemental/reference_quotient_v2/outputs_p0v3/`, so current
S1-S3 evidence remains immutable and no duplicate codebase is created.

| Stage | Current status | Clean decision | Reason |
|---|---|---|---|
| S1 | Accepted under v2 aggregate/P0 provenance | RERUN or retain only for a separate provenance package; prefer RERUN for one coherent final baseline | Scientific computation does not consume P0 community metadata, but final package cleanliness favors one implementation/provenance baseline |
| S2 | Accepted under corrected P0 v2 | RERUN_FOR_P0_V3_AUTHORITY | Clean package should bind v3 even if edge/scientific values are identical |
| S3 | Accepted under corrected P0 v2 | RERUN_REQUIRED | Community metadata and canonical parity authority changed to clean v3 |
| S4 | Blocked at v2 authority community-size closure | RUN_FROM_P0_V3 | Requires clean canonical community authority |
| S5 | Not run after S4 stop | RUN_FROM_P0_V3 | Bind canonical LCC/brokerage authority to v3 |
| S6 | Not run after S4 stop | RUN_FROM_P0_V3_AND_NEW_S4_S5 | Figure-ready source map must use clean v3 and new stability outputs |
| S7 | Not evaluated | DEFER | Separate authorization and final package boundary |

Recommended future order: finalize P0 v3, optionally rerun S1 for a single final
implementation baseline, then S2, S3, S4, S5, S6 in a new configured output
root. Do not overwrite current supplemental outputs. Figures, manuscript edits,
and S7 remain outside this migration task.

The recommendation balances scientific necessity (only S3-S6 depend on the
corrected community authority), provenance cleanliness (one coherent final
chain), runtime cost (S1 is expensive but deterministic and already accepted),
and package-manifest constraints (stage receipts must agree on authority roots
and implementation baseline).
