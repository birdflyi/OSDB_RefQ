# Chapter 5 RefQ P0-v3 Figure Rendering V2 Review

Status: `PASS_READY_FOR_HUMAN_VISUAL_QA`

This is a deterministic presentation-only package. It is not publication-ready
and does not replace human visual inspection.

## Scope and supersession

V1 at `figures/ch5_refq/p0v3_final/` is retained as immutable historical
evidence and is superseded for publication use because its human visual-semantic
contract failed in three places: Figure 1 source-admission topology, Figure 2
degree/strength axis separation, and Supplementary S3 Panel A transform
semantics. Figure 3 also received renderer hardening so the canonical highlight
is resolved from the frozen seed rather than a sorted-row assumption.

V2 is isolated at `figures/ch5_refq/p0v3_final_v2/`. No V1 file was overwritten.
All eight figures were rendered again from frozen CSV/JSON inputs; unchanged
figures were not copied from V1.

## Frozen authority

- Repository branch: `ch5-refq-repository-identity-correction-v1`
- `repository_HEAD_before`: `654e5dde871a437ee949343651d6aa71932bcacc`
- Final composition manuscript SHA-256:
  `5c54bd725becc7ff7253ec023e83258749b1868e14a70d34722adcc1f421bc60`
- P0-v3 manifest SHA-256:
  `be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`
- Supplemental v2 manifest SHA-256:
  `78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`
- S6 figure-ready manifest SHA-256:
  `e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea`
- SVG hash salt: `ch5-refq-p0v3-final-v2`

## Visual contract corrections

### Figure 1

Panel A now draws `SCANNED 3,748,078` with an explicit sibling exclusion
branch `EXCLUDED: OUT OF SEED 120`, followed by `ADMITTED 3,747,958` and three
explicit target-status child branches: `PROJECT_MAPPABLE 1,586,047`,
`NON_PROJECT 1,686,729`, and `UNRESOLVED 475,182`. The renderer asserts
`3,748,078 - 120 = 3,747,958`, the three-way partition closure, no
`Scanned -> Out of seed -> Admitted` serial path, and exactly three admitted
children.

Panel B retains all eight source-event rows in count-descending order. Panel C
derives its event order from Panel B through the recorded mapping to `*Event`
names, rather than sorting event names independently.

### Figure 2

Panel A contains only `metric=out_degree`; Panel B contains only
`metric=out_strength`. The renderer-level assertions record:

```text
F2_PANEL_A_SERIES = ["out_degree"]
F2_PANEL_B_SERIES = ["out_strength"]
F2_SHARED_DEGREE_STRENGTH_AXIS = NO
```

Panel C uses `Q1 / Median / Q3 / Max`. No scientific values or distributions
were recomputed.

### Figure 3

After sorting only for display, the renderer matches
`runs["seed"] == summary["canonical_seed"]`, requires one match, and uses that
row for all three highlights. The frozen result is
`canonical_seed=20260731`, `canonical_display_index=0`,
`canonical_highlight_resolved_by_seed=YES`.

### Supplementary S3

Panel A plots the frozen `spearman_to_canonical` values directly. The transform
is `NONE`, the title is `Spearman agreement to canonical`, the x-axis is
`Spearman rho`, and the minimum marker is `0.9998339514284217`. The deterministic
presentation-only x-limit is `[0.9998256489998426, 1.0]`, derived from the
frozen observed values with fixed 5% padding. Panels B and C retain their V1
scientific logic.

## V2 asset hashes

The 24 publication assets are:

| figure | SVG SHA-256 | PDF SHA-256 | PNG SHA-256 |
|---|---|---|---|
| figure1_evidence_universe | `21c1a7185f2619af00a50f2c336674a62e5fbcef8bfc5841ce4dd06ec45ff865` | `9866472905cbb7939d7410f5d3bbae35044835687c7e557693eab65f8f8d0023` | `579d9ef550198b84d2085206addfb8542d2c6e79c8d800085103af6e3dbffc71` |
| figure2_source_target_roles | `4bd2e4a170695adab1ef13be15df0aa96fa02df77a4d156085858d8bba8f9614` | `d597452c3113b1c5e80f3668807a6f1f051f71b907d1b5356ec14642e55fcc62` | `ba13cd55ff51546d4d3b085918f2f745708321e0053e213f3736b7f8f1b8e4d4` |
| figure3_undirected_structure | `fc6e3446d0ed92b89597d619db2fdecb47971c014a063f513d72170a5dfb64c6` | `e41e82ce06dea186a7c505aac4e2ff23bfb64ec7e7529cf2a4be5f34408ecfff` | `2c19e26d13ea3cfd2bf9b859a670097b4512b44af71fce5b915a9e594986a4cb` |
| figure4_rq3_comparison | `5b23e1899da3deea30fe8c71501fea6dd3d42fd46cd3e0e448b125cab0a112fb` | `d462950aac299dd399f9cabf425c936a188bc21154030198ebd5ec3225b036cd` | `a652edf065875b23e212f729e5130a1e686837ea423fb61ee359e33b5c81dfbf` |
| supplementary_s1_multiplicity_sensitivity | `448fc341f3541c8bf9d163bdda3d62fae622074c3bf6935f484e05ba00fd54c2` | `71e8ac4c4093aefdcbe70bfe9b12ece67a8185930847fa19253be300d78bf48e` | `93ac7d857e4490b3655cf36f1c75d78a1e9845c3f679adfdc7bade9dea78c087` |
| supplementary_s2_louvain_stability | `8e85d0e0250c617a94406786a47a86ea0ac1ce58ed6ccf27d4ef5973e9c44e7a` | `e937ebca9fa8a0c0f839d07854028b6de358a43ebb87d4f4f3ed156e8a91eae1` | `de4e92ba886ae4ffcecc062f5c19e11c0151cd124a4126a961bbd449a835e537` |
| supplementary_s3_brokerage_stability | `313d52c73e095b12652d8635898cee937adcbf397ac66e37a949ac5778787fad` | `03c7ee1fe0f2ef06c0341dc634dcdbb67e1f8c6145361d925f73b00129ce8770` | `beaf1976798409b731639e27f5c496e121f4b23f3560eaf4b70be0f8742b74a6` |
| supplementary_s4_unit_contract | `3d6d234e4e6b4fc75bac7300561f677e3116e3a91d5fa3d43ce531f0a464cbe6` | `d764446e98771043e2ed933390220f777a798a7d6614ae1f86d931c7110c0201` | `e69e101797a9b3fc785555e835e8fbbbc00e69b78009cb5ea072fcd77fc4f397` |

Additional V2 package hashes:

| file | SHA-256 |
|---|---|
| `render_ch5_refq_p0v3_v2.py` | `50b81ac6fd146fc5510a45b7921a99fea726aaee45f7985d92a5f0c22302d02a` |
| `captions_draft_v2.md` | `177d57f66a5f43c1efacbcd41564dcdf8c28265cd9fe0c0c5496c8601b17b18b` |
| `render_manifest_v2.json` | `5c6e86df27eaf1fd98d938e07c8cade472b3d71a39cd740814f8ebaaf8e225f9` |
| `human_qa_contact_sheet.png` | `c53890fa7dfad2e9f8c148e3aaa1d126275ef089e36ba5bc946ba5b97b8419a1` |

The eight source-manifest SHA-256 values are recorded in `render_manifest_v2.json`:

```text
figure1_evidence_universe = 3b33a48804d6fee71958bc1d172bcc92cef58d02a2bb0c322c7c0ede59efa848
figure2_source_target_roles = 7f8c880f28a607a1705d2449ae89165bf9f93bfc28e8312f9314fc4922321d65
figure3_undirected_structure = 985b345395222ec2ab7fcf2837e7e68d32de486c4e0b828331bf9d990a09fd05
figure4_rq3_comparison = 4c682b29b2a7f0b12d171212803431c81dbf177878c524602835fc165a2fc73f
supplementary_s1_multiplicity_sensitivity = 5ab767c13cc79380fdca49ddf9b56d64f331b95d057a49176b3c7ee029da957c
supplementary_s2_louvain_stability = ec0e641e0221fc163d99ab0e040a023be08fddb9a9091a867b9838d7c206b0ef
supplementary_s3_brokerage_stability = 1e40d27e35d599a543042c1ef681cacb74408ae32e461c9a8842ce685ad38863
supplementary_s4_unit_contract = f112ce4ec01a5ac64e46629b42d5f733ea4e4700a97fa1210cd851274c635276
```

## Determinism and machine QA

Attempt A and Attempt B used independent temporary roots with identical
environment (`Python 3.9.13`, pandas `1.5.3`, NumPy `1.24.2`, Matplotlib
`3.8.2`, Agg backend, `PYTHONHASHSEED=0`). All 24 corresponding SVG/PDF/PNG
assets and both render manifests were byte-identical. Publication PNGs are
non-empty, non-zero, and 300 DPI; SVGs are non-empty, finite, and contain the
required contract labels. The contact sheet is presentation-only and is not
counted among the eight publication figures.

Scientific execution counters are all zero: `P0_RUN=0`, `S1_RUN=0`,
`S2_RUN=0`, `S3_RUN=0`, `S4_RUN=0`, `S5_RUN=0`, `S6_RUN=0`, `S7_RUN=0`,
`GH_CORE_RUN=0`, and `EVENT_REJOIN=0`.

## Immutability

The final composition manuscript, P0-v3 outputs, supplemental v2 outputs and
manifests, S7, scientific code, historical figures, and V1 render root were
unchanged. `manuscript_modified=NO`, `scientific_outputs_modified=NO`,
`figures_generated=8 publication figures plus one contact sheet`, and
`scientific_logic_change_count=0`.

## Human gate and provenance

`HUMAN_VISUAL_QA = PENDING`. The contact sheet is provided for human review of
font size, density, panel balance, and cross-figure consistency. This package
must not be described as publication-ready until that gate passes.

`FIGURE_RENDER_V2_COMMIT_A = 31929c645b25f5a986a408cd1b6f9f0bdc2dcc73`

Commit A was pushed to `origin/ch5-refq-repository-identity-correction-v1`.
The docs-only closure commit records this predecessor and the successful push;
it intentionally does not self-reference its own SHA.

## Decision

`P0V3_FIGURE_RENDER_V2_PASS_READY_FOR_HUMAN_VISUAL_QA`
