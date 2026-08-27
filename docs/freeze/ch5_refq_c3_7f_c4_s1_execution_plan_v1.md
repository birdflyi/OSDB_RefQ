# Chapter 5 RefQ C4-S1 Execution Plan v1

This document freezes the future invocation contract only. C3.7-F does not authorize execution.

## Preconditions

- Branch: `ch5-refq-repository-identity-correction-v1`.
- Worktree: clean, or explicitly reviewed known state with no implementation changes.
- Implementation commit: the final C3.7-F commit recorded in the review receipt.
- Corrected P0 manifest SHA: `21699353d5dc9476547ee7f56881ba0a1ccc842a6d3c95adad9a28dedfd656d7`.
- Corrected P0 config SHA: `e19c0937e0d6f72fa84ad135b55a4056357d132d3a3df4ae5455bda7bc3de658`.
- Corrected aggregate: 294/294 files must match the accepted corrected-P0 provenance records.
- Historical baseline: `docs/freeze/ch5_refq_c3_7f_historical_immutability_baseline_v1.json` must compare as `HISTORICAL_IMMUTABILITY_MATCH` before execution.
- Target `supplemental/reference_quotient_v2/outputs/S1_evidence_universe/` must be absent.

## Exact Invocation

```text
python -m supplemental.reference_quotient_v2.scripts.run_supplemental_v2 \
  --run-stage S1 \
  --authorization-phase C4-S1 \
  --expected-implementation-commit <FINAL_C3_7F_COMMIT_SHA> \
  --baseline docs/freeze/ch5_refq_c3_7f_historical_immutability_baseline_v1.json
```

Exactly one stage is permitted. There is no `--run-all`, retry, cleanup, overwrite, downstream continuation, or S7 path.

## Expected Authorities

S1 loads the corrected aggregate authority recorded by the corrected P0 seed manifest, all 294 partition files, and only optional corrected P0 metadata/seed records needed by the implementation. It must not event-rejoin, discover historical v1 files, or infer identity from repository names.

## Output and Gates

The runner must pass corrected aggregate schema/294 hash closure, status-aware admission, before/admitted/rejected reconciliation, admitted contradiction zero, source-seed mismatch zero, membership/evidence/eligible/unit closures, two-pass input-drift equality, and the exact eight-CSV S1 output contract. It writes `S1_evidence_universe/stage_receipt.json` last and validates the receipt afterward.

## Stop Conditions

Stop closed on any input hash mismatch, missing/extra partition, unknown or contradictory admission status, input drift, failed acceptance gate, existing target directory, incomplete output set, receipt mismatch, historical pre/post mismatch, branch/worktree mismatch, or implementation-commit mismatch. Never restore or overwrite a partial stage.

## Evidence For Human Review

Return the exact implementation commit, command, corrected P0 and 294-partition closure summaries, pre/post historical comparison, stage receipt path and SHA records, all S1 gate results, output inventory, runtime versions, and counters proving `P0_RUN=0`, `S1_SCIENTIFIC_RUN=1` for that future invocation, with no downstream stage executed.

`C4_S1_AUTHORIZED_BY_C3_7F = NO`.
