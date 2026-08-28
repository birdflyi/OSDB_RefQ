# Chapter 5 RefQ P0 v3 Clean Regeneration Review v1

## Decision

`P0_V3_RUNTIME_LOCKED_CLEAN_PASS_READY_FOR_SUPPLEMENTAL_MIGRATION`

Attempt 1 is `REJECTED_RUNTIME_MISMATCH`. Attempt 2 is
`ACCEPTED_RUNTIME_LOCKED_V3`.

## Authority and provenance

- shared implementation commit:
  `25c6ef3f49af04e916f10e129d976ce7c2119fd8`
- attempt-1 blocker commit:
  `b9c6d6616dffb2cd368eba30382bf786c1f8db83`
- attempt-2 result commit:
  `2d284f4bc83c42ba6555a09a2e42693c5490b827`
- v3 config SHA-256:
  `43f97f9a2d177d325415bfbcc504f1779882cf83685b4fdebe505c8fed8e7cb0`
- v3 manifest SHA-256:
  `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
- manifest status: PASS; inputs: 296; output records: 30; files including
  manifest: 31
- corrected aggregate closure: 294/294 PASS

The attempt-2 manifest records Python 3.9.13, pandas 1.4.4, NumPy 1.26.4,
SciPy 1.13.1, NetworkX 3.1, and GH-CoRE 2.3.1. No GH-CoRE run, event rejoin,
aggregate regeneration, or external retrieval occurred.

## Scientific acceptance

- seed count: 294
- reference records before admission: 3,748,078
- admitted source observations: 3,747,958
- out-of-seed source observations: 120
- missing/invalid event-repository observations: 0/0
- source mismatch after admission: 0
- source-seed membership mismatch: 0
- quotient-eligible records: 1,586,047
- self-loop weight: 1,447,073
- cross-project weight: 138,974
- community rows/count: 6,367 / 35
- community-size mismatch rows: 0
- project-to-community mapping versus v2: exact
- modularity: `0.7969220043681785`, exact v2 output parity
- edges, LCC, brokerage, RQ1, RQ2a, RQ2b, and RQ3: byte-identical to v2

The only scientific-file difference is the expected correction of
`community_size` in `rq2c_algorithmic_communities.csv`. All 6,367 rows now
equal their community's actual cardinality. The global size multiset remains
unchanged.

## Strict differential and closure

Of 30 scientific outputs, 29 are byte-identical and one is classified
`EXPECTED_COMMUNITY_SIZE_CORRECTION`. The three prior runtime-drift files are
now byte-identical. The v3 manifest validates every output path, SHA-256, and
byte count with zero mismatches.

Pre/post tree hashes were unchanged for corrected P0 v2, historical P0,
supplemental v1, and the existing supplemental v2 S1–S3 outputs. Corrected
aggregate hashes remained 294/294. Thus v2, historical, aggregate, and
supplemental immutability all PASS.

## Limitations and next boundary

Historical OS/BLAS metadata was not recorded. The full later supplemental
implementation is not compatible with pandas 1.4.4 serialization APIs, so the
future clean S1–S6 migration must freeze one supplemental-compatible runtime
and implementation baseline while consuming official P0 v3. No supplemental
stage, figure, or manuscript update was executed in this task.
