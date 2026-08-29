# Chapter 5 RefQ P0-v3 Figure Rendering Review v1

Status: `READY_FOR_HUMAN_VISUAL_QA`  
Scope: deterministic presentation rendering only. No manuscript, scientific
output, historical figure, or scientific code was modified.

## Authority and immutability

- Repository branch: `ch5-refq-repository-identity-correction-v1`
- `repository_HEAD_before`: `fbb6114fd83c1fab503dadce470d9fa9ccee59f6`
- Composition audit label correction commit: `fbb6114fd83c1fab503dadce470d9fa9ccee59f6`
- Final composition manuscript SHA-256: `5C54BD725BECC7FF7253EC023E83258749B1868E14A70D34722ADCC1F421BC60` (116,819 bytes)
- P0-v3 manifest SHA-256: `BE802B9DF223C99BC2089A76AE9EC6E0B6047AB0C58237A5FC3050B51DCC9776`
- Supplemental v2 manifest SHA-256: `78D07FBDA2A045BA309A1CFCB23A68CA2BAFA910008B6483C0C4E0ACF9211BD`
- S6 figure-ready manifest SHA-256: `E9C192D140659B33C870A3B03E9583EC5C39AC0702ECC26F28C78E87648F4EEA`
- Composition display policy: `COMPOSITION_DISPLAY_POLICY_V1` (`c37638e4a1ae795b41e0b436a3c1802305ba6eadfc4ea8f77fbf07f20bce1165`)
- Figure plan SHA-256: `6d68c12dd785df653ff252ae5f79ae27cd1482d50deebafaacd96f2ccf175312`

The P0-v3 and supplemental scientific roots had no Git diff before or after
rendering. Historical figure assets were not overwritten. `Figure 0` was not
modified, and Supplementary S5 was not rendered.

## Render set and contracts

The rendered set is exactly Main Figures 1--4 and Supplementary S1--S4.
Inputs were frozen CSV/JSON files only. The renderer imports pandas, NumPy,
and Matplotlib; it does not import NetworkX, SciPy, statsmodels, sklearn, or
scientific stage code. Runtime: Python 3.9.13, pandas 1.5.3, NumPy 1.24.2,
Matplotlib 3.8.2, Windows-10-10.0.26200-SP0, Agg backend, `PYTHONHASHSEED=0`.

Figure contracts:

- Figure 1: Reference-record flow, all eight source-event rows, and event-type target-membership shares.
- Figure 2: Separate source degree/strength CCDFs, separate target quantile scales, and top-1/10/50 weight concentration.
- Figure 3: First-order undirected structure, observation-boundary sensitivity, and the seed-sensitive **algorithmic modular neighborhood view**.
- Figure 4: Frozen mean/median descriptive displays for both label modes and all 11 epsilon-squared/FDR rows; no uncertainty bars or new tests.
- S1: Thresholds 1, 2, 5, and 10 with retained edge/weight/LCC fields.
- S2: All 50 Louvain runs and pairwise ARI distribution.
- S3: Structural brokerage-candidate ranking diagnostics only.
- S4: Separate RECORD, REFERENCE_RECORD/aggregated weight, and EDGE_COUNT units.

## Determinism and output hashes

Attempt A and Attempt B were rendered to independent temporary roots. All 24
corresponding assets were byte-identical: SVG `PASS`, PDF `PASS`, PNG `PASS`.
The following are the official Attempt A hashes (paths are relative to
`figures/ch5_refq/p0v3_final/`):

| figure | SVG | PDF | PNG |
|---|---|---|---|
| figure1_evidence_universe | `38dbaab3bde0c58f9b4270f7afcf41d132307e3c123f54f79b93a5c34b6d5952` | `3d7d01cc1ca3353d507db1fe1830407cd717ad99196cd101784c7f4bff99f609` | `2a0470d5f83923d3110b86af028103595cd76086169461f3594ce8914710e873` |
| figure2_source_target_roles | `029795e9344422817eab16bc6dd66e81d606ec742f51cea049d8cd0ca8991015` | `db722092f1047f9f84fd9e56bf9508ad89ca31f6c04deb6ef38f48981a35d947` | `d64782c115714ddbf655d1f31dfdbeac416905ec1cce07f0189f4f54b813561a` |
| figure3_undirected_structure | `47e01cc1c7e36196a3dc1fb62ccb0c1573c78ec263c85edc12992b2e179df339` | `12eb15d43fd03eed6a20cfd02d0527727cd7e4c2d512e12e7d00bc452f67653f` | `940ffa15f494f098098effaca5d20541684c2910afca062470c7344286ed34ae` |
| figure4_rq3_comparison | `e997272d1af4882d1bf136c59b187999e90655fbc587c77704565db112026ecf` | `3b8ab590531ed75585a0c32a413f031ab27c12e052d44e82691f51ccb3037eda` | `fb9f289d484b9cb85bc8d9d5af9793e7223a1e14625c06f3f7f45031be1d8eac` |
| supplementary_s1_multiplicity_sensitivity | `de59c20e0ce17c9850a31861882c1497f18cb35e43ed9fe02379fb817a1c9ed6` | `9bd60f42244e1abe20c002109131c6afcadf64c295f477080f40bb325e6dadbd` | `e9ceb1b09178f8f0a5751745e5a919d432d4a729342b785333c20085dda752f5` |
| supplementary_s2_louvain_stability | `e362f3ff8d9f8289a50f607c535a452f69f999db317034bb05269cec1e476ed4` | `b645d85b49eda49244656f733f29562de08e0b3b9c1e65a053cd6a2a86365bef` | `a692d10f9f96c44d1b15932284c32e714c30d0fff478f0faab5d7686ab362e8b` |
| supplementary_s3_brokerage_stability | `060416a09a06b875d72504813685aa5433cfd5d097b8385594f74218d226e911` | `5f1e7654f416f5e5be33757e32976ab08fe55bff020ca245506ba079a5561081` | `52d8b4177034ef954cee53dbad6771f16008127e4695c90f647ff47a2526c159` |
| supplementary_s4_unit_contract | `84108c313f8c938c53e50ccacaad7e8c4f16259f7efa59b77eb68441cc53e3c5` | `c13a5990ab6b12682d1e5c8c2ae596c0b67c5e421cb6bbaaa4f237637e464506` | `29c3a836e02ea622670b046d3d57a40f55d625e4f03b9cdb063ef14f8c0d71d1` |

The eight per-figure source manifests are present and report `status=PASS`
and `S6_manifest_closure=PASS`. The renderer SHA-256 recorded in those
manifests is `b9e3a51f6e5adeceeefd2f518af8c1e137eee18992cf26ff60858210462ef669`.

## Key-value and machine QA

Frozen key values were asserted during rendering, including 3,748,078 scanned
records, 3,747,958 admitted records, 1,586,047 quotient-eligible records,
138,974 cross-project weight, 6,506 nodes, 9,547 undirected edges, 35
canonical algorithmic communities, and modularity 0.7969220043681785. Figure
2 displays 294 source projects and 2.47%, 16.00%, and 48.99% concentration.
S2 displays minimum ARI 0.6823671359861659 and minimum pairwise ARI
0.6092441840471735. S3 displays minimum Spearman 0.9998339514284217 and
minimum top-50 overlap 0.82.

Machine QA results:

- SVG/PDF/PNG counts: 8 / 8 / 8; all files non-empty.
- PNG dimensions non-zero and embedded DPI is 300 for all eight PNGs.
- SVG text contains no NaN or Inf and required value/label checks pass.
- Caption semantic boundary issues: `0`.
- No `reference_quotient_v1` or historical figure path appears in the new render root.
- Scientific roots unchanged; manuscript unchanged; scientific logic changes: `0`.
- `P0_RUN=S1_RUN=S2_RUN=S3_RUN=S4_RUN=S5_RUN=S6_RUN=S7_RUN=0`;
  `GH_CORE_RUN=0`; `EVENT_REJOIN=0`.

## Human gate and decision

Human visual inspection is the next gate and remains pending. This package is
not publication-ready and does not claim publication acceptance.

`HUMAN_VISUAL_QA = PENDING`  
`SUPPLEMENTARY_S5_RENDERED = NO`  
`FIGURE0_MODIFIED = NO`  
`decision = P0V3_FIGURE_RENDER_PASS_READY_FOR_HUMAN_VISUAL_QA`

`FIGURE_RENDER_COMMIT_A = 71ae8f3ccb78831d443547a412a44d1d3a728d6c`  
`push_status = PASS`  
`FIGURE_RENDER_CLOSURE_COMMIT_B = PENDING`

No manuscript or scientific-output commit is included.
