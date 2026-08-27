# Chapter 5 RefQ C4-S2 Dynamic Parity-Gate Hotfix Review v1

## Scope and authorization

This review records the authorized C4-S2 parity-gate hotfix and the
proactive S2-S5 positive-path audit.  No S1 rerun was performed.  No P0,
GH-CoRE, event rejoin, S7, figure generation, or manuscript update was
performed.

The accepted S1 implementation baseline remains
`fe327e17e0db66ca40bc97fc17309603bff2afc3`; the accepted S1 result baseline
remains `edb9441c7b276051224087fdf26d2e0cfcb78dba`.

## First S2 attempt

The first corrected S2 scientific attempt was recorded as attempt 1.  It
computed the corrected network in memory but stopped before the canonical
parity comparison completed.  The exception was:

```text
KeyError: ('node_u', 'node_v', 'weight', 'directed_edge_count')
```

The failure occurred in `assert_s2_threshold_one_matches_corrected_p0()`.
No S2 stage directory, receipt, scientific output, or result commit was
created.  This was not a canonical parity mismatch.

## Root cause and patch

`S2_UNDIRECTED_EDGE_COLUMNS` is intentionally a tuple containing the four
frozen columns `node_u`, `node_v`, `weight`, and `directed_edge_count`.  The
parity gate used `frame[S2_UNDIRECTED_EDGE_COLUMNS]`.  Pandas interprets a
tuple in `DataFrame.__getitem__` as one column key, producing the observed
`KeyError` instead of selecting four columns.  A micro reproduction with
`DataFrame(columns=["a", "b"])[("a", "b")]` shows the same behavior.

The minimal patch converts the frozen tuple to a list and selects explicitly
with `.loc[:, columns]` for both expected and actual edge tables.  Column
names, values, sorting, threshold semantics, tolerances, and pandas assertion
semantics are unchanged.

Classification: `PANDAS_TUPLE_COLUMN_SELECTOR_IN_PARITY_GATE`, an
`INTEGRATION_COMPARISON_GATE_DEFECT`; not a scientific-logic, corrected-P0, or
network-semantics defect.

## Same-class selector audit

The S2-S6 supplemental-v2 scripts were audited for tuple constants used as
`DataFrame[TUPLE_CONSTANT]`.  The S2 parity gate was the only unsafe occurrence
and was patched.  S3 uses `.loc[:, columns]` for parity tables; S4 and S5 use
explicit columns/row predicates; S6 uses keyed manifest assignment.  No other
mechanical selector patch was required.

## Positive dynamic parity-path audit

Temporary synthetic corrected-P0 authority fixtures were used with explicit
test-only root/authority monkeypatches.  Production root guards remained
active, and each test executed the real comparison body after authority
loading/column selection.

| Gate | Positive path | Mutated authority failure |
|---|---|---|
| S2 | PASS: threshold-1 edges and summary close | PASS: changed weight and missing edge fail closed |
| S3 | PASS: node order, edges, LCC edges, communities, summary close | PASS: changed edge fails closed |
| S4 | PASS: canonical seed, label-invariant partition, count, modularity close | PASS: mutated partition fails closed |
| S5 | PASS: canonical k/seed, project set, scores, ranking tie-break close | PASS: mutated score fails closed |

## Regression and immutability

The full supplemental-v2 regression command completed with `195 passed, 0
failed` (one pre-existing pandas deprecation warning).  `python -m compileall
supplemental/reference_quotient_v2` and `git diff --check` passed.

All nine files under `supplemental/reference_quotient_v2/outputs/S1_evidence_universe`
were compared with the `edb9441c7b276051224087fdf26d2e0cfcb78dba` blobs and
matched exactly, including `stage_receipt.json`.  No S1 output, receipt, or
result commit was modified.

## Provenance and boundary

The new implementation hotfix commit is the frozen C4 network implementation
baseline for S2-S6 (`C4_NETWORK_FROZEN_IMPLEMENTATION_COMMIT`, recorded by the
commit that contains this review).  It is distinct from the S1 implementation
baseline above.  `scientific_logic_change_count = 0`.

At this checkpoint no corrected S2-S6 scientific execution has been resumed;
therefore S2-S6 result commits, stage receipts, output hashes, G18/G19 closure,
and final C4 batch status remain `NOT_RUN` pending the separately authorized
dry-run and sequential execution.
