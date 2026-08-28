# Chapter 5 RefQ P0 v3 Clean Supplemental Migration Review

Status: implementation review before clean scientific execution.

This migration keeps the single `supplemental/reference_quotient_v2` scientific
implementation and changes only its executable provenance boundary. Production
authority is the official P0 v3 result (`2d284f4bc83c42ba6555a09a2e42693c5490b827`),
with manifest SHA `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
and config SHA `43f97f9a2d177d325415bfbcc504f1779882cf83685b4fdebe505c8fed8e7cb0`.
The corrected aggregate inventory remains fixed at 294 seed-linked partitions.

The clean execution output root is
`supplemental/reference_quotient_v2/outputs_p0v3/`. The historical supplemental
`outputs/` root and P0 v2 root remain explicit comparison-only authorities and
are protected from writes. The clean root must be absent before S1 and each
stage directory is write-once.

Runtime selection is isolated from the P0 v3 runtime because supplemental CSV
serialization requires a pandas release compatible with the existing stage I/O.
The selected runtime must retain Python 3.9.13, NumPy 1.26.4, SciPy 1.13.1,
NetworkX 3.1, and GH-CoRE 2.3.1 while using supplemental-compatible pandas.
No global environment is changed and no scientific implementation is forked.

The migration includes hard P0 v3 manifest/config hash closure, aggregate
partition closure, P0 v2 substitution rejection, clean output-root guards,
write-once stage guards, v3 stage receipt provenance, and dynamic S2-S5 parity
paths. Scientific semantics are unchanged: `scientific_logic_change_count=0`.

Pre-execution closure is PASS: P0 v3 manifest/output closure is exact, all 294
aggregate partitions close against the accepted manifest, the supplemental
suite passes 199/199, the selected runtime passes 54 shared scientific tests
with the P0-runtime-lock assertion deselected, and the accepted P0 runtime
passes the full 55/55 shared suite. S2, S3, S4, and S5 canonical P0 v3 parity
gates pass. The runtime-gate S4 probe reports a robustness alert; clean execution
must therefore stop after durable S4 if the production result reproduces it.

The immutability baseline in
`ch5_refq_p0v3_clean_supplemental_immutability_baseline_v1.json` records the
historical P0, P0 v2, official P0 v3, supplemental v1, old supplemental v2
outputs, and corrected aggregate assets before any clean stage execution.
