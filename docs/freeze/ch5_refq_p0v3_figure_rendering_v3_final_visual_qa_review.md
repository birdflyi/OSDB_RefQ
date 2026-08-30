# Chapter 5 RefQ P0-v3 Figure Rendering V3 — Final Visual QA Review

Status: `PASS_READY_FOR_FINAL_HUMAN_REVIEW`

This is the final presentation-only rendering package. It is not yet
publication-ready; the final human review gate remains open.

## Why V3 was needed

V1 and V2 remain immutable historical evidence. V3 addresses the remaining
human visual QA findings without changing scientific inputs, values, methods, or
manuscript content:

- Figure 4 A–D relied too heavily on color for label-mode interpretation and
  used excessive vertical whitespace.
- Figure 1 Panel A had avoidable crowding around source admission and the
  exclusion branch, and Panel C's legend obstructed the stacked bars.
- Figure 2's rendering caption repeated the strength-unit sentence.

The isolated output root is `figures/ch5_refq/p0v3_final_v3/`; V2 at
`figures/ch5_refq/p0v3_final_v2/` was not overwritten.

## Frozen authority and boundaries

- Repository branch: `ch5-refq-repository-identity-correction-v1`
- `repository_HEAD_before`: `c067750cadea3c18342fe2d97ebdb972b149d345`
- Final composition manuscript SHA-256:
  `5c54bd725becc7ff7253ec023e83258749b1868e14a70d34722adcc1f421bc60`
- P0-v3 manifest SHA-256:
  `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
- Supplemental v2 manifest SHA-256:
  `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`
- S6 figure-ready manifest SHA-256:
  `e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea`
- V3 SVG hash salt: `ch5-refq-p0v3-final-v3`

Only pandas, NumPy, Matplotlib, and the standard library were used for
presentation rendering. No P0, S1–S7, GH-CoRE, event rejoin, Louvain,
brokerage, FDR, or other scientific rerun was performed.

## Figure 1 cleanup

Panel A retains the V2 branch semantics and frozen counts:
`SCANNED 3,748,078` → `ADMITTED 3,747,958`, with sibling exclusion branch
`EXCLUDED: OUT OF SEED 120` and exactly three admitted children:
`PROJECT_MAPPABLE 1,586,047`, `NON_PROJECT 1,686,729`, and `UNRESOLVED 475,182`.
The source-admission label, exclusion annotation, and boxes were spaced to
reduce crowding. Panel C's legend is outside/below the stacked bars and no
longer obscures them. No count or branch relationship changed.

## Figure 2 caption correction

The V3 caption contains exactly one occurrence of “Strength is aggregated
Reference-record weight”. The V2 visual contract is unchanged: Panel A is
`out_degree` only and Panel B is `out_strength` only.

## Figure 4 encoding and layout correction

Panels A–D now use a grayscale-safe grammar:

- mean = circle; median = square;
- `include_mixed` = filled marker;
- `exclude_mixed_or_multilabel` = open marker.

Color remains only a secondary aid. The A–D legend explicitly names all four
combinations. Panel E preserves its separate significance grammar: filled means
BH-FDR reject and open means not reject; its dedicated legend is titled
`E significance fill grammar`. The A–D block and Panel E were vertically
recomposed to reduce whitespace while retaining all five panels, categories,
labels, and frozen values.

The renderer records and asserts:

```text
F4_AD_grayscale_safe = PASS
F4_AD_statistic_encoding = mean=circle; median=square
F4_AD_label_mode_encoding = include_mixed=filled; exclude_mixed_or_multilabel=open
F4_E_FDR_fill_grammar = filled=BH-FDR reject; open=not reject
F4_layout_tightened = YES
```

## Exact V3 asset hashes

The 24 publication assets in `figures/ch5_refq/p0v3_final_v3/` are:

| figure | SVG SHA-256 | PDF SHA-256 | PNG SHA-256 |
|---|---|---|---|
| figure1_evidence_universe | `a77350aa5fd09c7897491a26183388d0187b22bbd6355ddb2ba2b74c4c178ab6` | `9dd8d429283eb03c10182d572e260727a8f56ffc0ad3ebe2318336e8e35d6dfd` | `13d2423791d109a2a5655d424864a6ccec7240939a210508bdc2030254e4771a` |
| figure2_source_target_roles | `35af180690ed229d3fc63b6f091aa1602c34541db3b41e7380a8eb756fcd3199` | `261708722490064e22659fe869daa02ac5fc911e880b743e4638bc6e8f00ddeb` | `14a0990435a2ef91fc76ea492aab771415939e546c4d4651423a1cbe8dc2cc55` |
| figure3_undirected_structure | `2b34188b9d05715bf4c8d09060a88aa8a702315512cd2fd02b9756e77448e289` | `6c957f33bb70357c18f39b884c38a860df0dd7d38acf018dbd076ca7fae85243` | `c4ec4025570a026822a8ae344111bd6fa7a457e2b941f5d002704302a47edd01` |
| figure4_rq3_comparison | `2136f0c2374f583f30850f226e9275218e05758171022c7c7c0e12661f64185e` | `3a63af15206d1762a483e26dc30fa6feda2424a1abf9b9b64cd44b78ddfb9dd4` | `7eb4e5caddf61c4154a857babe83b4dc79a90d22078bcac855566dad95d735ac` |
| supplementary_s1_multiplicity_sensitivity | `5ce498f22c8535c89de09a2964e2807f88c69fc8f720a0f6d74d93fb55097551` | `1b84352baf76675477e0c98bbb81f6463dffa5eee061c8907a753cd626949926` | `0336ff517b6fde8142c3a32336d893d350f12697f295d02598a46ba3df6540b0` |
| supplementary_s2_louvain_stability | `9eb4e8de2828d699d45332f002bf04bf6c8ba729811c530cd7bb5808433bbf80` | `1bb34b793879294d276372d6589539e4285665d18c8b8e30fcd6ecf9dfa38b55` | `e3d75b853c3d972da2e7daafd06a1767669cb6b7b6ce5855d62ebb79368fac46` |
| supplementary_s3_brokerage_stability | `471e7e8041b61750db107d5c7e1202f75628b35d2275008f294ccd1b2d19ed18` | `cb414153cdb97a0c2e295f21093882bd776b7277dfda21a381d2bee81b48c420` | `4b7716da007431e76f8e67e8910514c15ee8f589a41c15bb52d4c2bd4450afa0` |
| supplementary_s4_unit_contract | `b3af4539074a0279420bf9e76e58be3093ac4e33268369aabe7b08bbb7cfba4f` | `66d0861c5c691f313522ff37bcf75cb63279af6a546c238f0f249428d84930b9` | `a29724f2b81cde7663f48edef4b2d014b14c57f2b6dc9a4296d7e4a76c353565` |

Additional V3 package hashes:

| file | SHA-256 |
|---|---|
| `render_ch5_refq_p0v3_v3.py` | `31a0b5a1e3a1be049835fa787e8fa119bfc1db3e836ba26df4f7e23b02f0f856` |
| `captions_draft_v3.md` | `9ffb58a4913d1ab2eb9eb851d87f70db412ac0d5a789a547000404b0ca9c5554` |
| `render_manifest_v3.json` | `fd88594a233aa09cc743232bfa773b4c2b38a45f81d53c7467d98165a33d5462` |
| `human_qa_contact_sheet.png` | `131d0469590ace778348fe96ce45c9ab5feaa642e47fbeca86ab077468152381` |

The eight source-manifest hashes are recorded in `render_manifest_v3.json`.

## Deterministic A/B closure and machine QA

Attempt A and Attempt B were rendered to independent temporary roots with
identical runtime (`Python 3.9.13`, pandas `1.5.3`, NumPy `1.24.2`, Matplotlib
`3.8.2`, Agg backend, `PYTHONHASHSEED=0`). All 24 corresponding SVG/PDF/PNG
assets and both manifests were byte-identical:

```text
deterministic_svg = PASS
deterministic_pdf = PASS
deterministic_png = PASS
```

The official root contains 8 SVG, 8 PDF, and 8 PNG publication assets plus the
presentation-only contact sheet. Publication PNGs are non-empty and 300 DPI;
SVGs are non-empty, finite, and contain the required panel labels and contract
text. S5 remains not rendered. No duplicate panel labels or stale V1/V2 output
root was introduced.

## Scientific, manuscript, and V2 immutability

All plotted values are identical to the V2 frozen authorities:

```text
NEW_SCIENTIFIC_VALUES = 0
CHANGED_SCIENTIFIC_VALUES = 0
scientific_logic_change_count = 0
manuscript_unchanged = YES
scientific_outputs_modified = NO
V2_root_unchanged = YES
```

Execution counters are all zero:

```text
P0_RUN = 0
S1_RUN = 0
S2_RUN = 0
S3_RUN = 0
S4_RUN = 0
S5_RUN = 0
S6_RUN = 0
S7_RUN = 0
GH_CORE_RUN = 0
EVENT_REJOIN = 0
```

## Human gate and provenance

Contact sheet: `figures/ch5_refq/p0v3_final_v3/human_qa_contact_sheet.png`.

`HUMAN_VISUAL_QA = READY_FOR_FINAL_REVIEW`. This status requests the final
human visual review; it must not be described as publication-ready yet.

`FIGURE_RENDER_V3_COMMIT_A = 23a60fd` (`fig(ch5): finalize p0v3 visual presentation`)

Commit A was pushed to `origin/ch5-refq-repository-identity-correction-v1`.
The docs-only closure commit records this predecessor and push status without
self-referencing its own SHA.

## Decision

`P0V3_FIGURE_RENDER_V3_PASS_READY_FOR_FINAL_HUMAN_REVIEW`
