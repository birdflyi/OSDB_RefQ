# Chapter 5 RefQ Figure P00 — Current Authority and Maintenance Strategy Audit

## Decision

`CH5_REFQ_FIG_P00_CURRENT_AUTHORITY_AND_MAINTENANCE_STRATEGY_AUDIT_PASS_WITH_BOUNDED_REPAIR_RECOMMENDED`

This is a read-only authority and maintenance audit. It does not create the
future mapping register recommended below and does not modify any manuscript,
caption, figure, scientific output, or render.

## 1. Task and base authority

```text
TASK = CH5_REFQ_FIG_P00_CURRENT_AUTHORITY_AND_MAINTENANCE_STRATEGY_AUDIT
REPOSITORY = D:/github_repo/OSDB_RefQ
BRANCH = ch5-refq-repository-identity-correction-v1
TASK_BASE_REPOSITORY_HEAD = ae5ed9829aae4820ae8b27b8447139fc0dcbe039
REMOTE_HEAD_BEFORE = ae5ed9829aae4820ae8b27b8447139fc0dcbe039
ACCEPTED_MANUSCRIPT_REVISION = MS-R04
ACCEPTED_MANUSCRIPT_SHA256 = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
SCIENTIFIC_BASELINE = P0-v3
P0_V3_MANIFEST_SHA256 = be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776
```

The accepted MS-R04 snapshot and editable CURRENT were independently hashed;
both equal the required SHA. The snapshot is the manuscript authority. CURRENT
is only its matching editable alias.

## 2. Inspected paths and artifacts

- `versions/MS-R04_POST_OBSERVATION_FRAMING_F8071504.md` and
  `第5章-paper1_CURRENT.md` outside the repository; their SHA-256 values match
  MS-R04 above.
- `figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json`, the four main
  `main/figure*/source_manifest.json` files, and their SVG/PDF/PNG assets.
- `figures/ch5_refq/p0v3_final_v6_e01_eta_label/render_manifest_v6_e01_eta_label.json`,
  its Figure 4 source manifest, and corrected SVG/PDF/PNG assets.
- `figures/ch5_refq/phase2a_scaffold_manifest.json` and
  `figures/ch5_refq/phase2b_design_freeze_manifest.json` in the external
  manuscript figure directory.
- `docs/freeze/ch5_refq_p0v3_figure_rendering_final_acceptance.md`, the V6
  publication-label review, Figure 1–4 caption composition audit, final
  caption micro-polish record, MS-R04 promotion, manuscript version manifest,
  final Chinese semantic-source freeze, and the P0-v3 migration matrix.
- `docs/submission_suggestion/ch5_refq_sub_a02_jss_author_guideline_and_artifact_mapping_2026-09-22.md`
  and MS-R04 candidate/Final QA records.
- P0-v3 scientific manifest and the frozen Figure 4 effect-size result files,
  inspected only for authority/terminology lineage.

## 3. Current authority findings

The accepted V6 publication root is `figures/ch5_refq/p0v3_final_v6/`. Its
render manifest gives each main and supplementary item a separate directory
and records SHA-256 for SVG, PDF, and PNG. All 24 assets represented by the
eight V6 render sets (main Figures 1–4 and supplementary S1–S4) were checked
against the manifest; every digest matched.

MS-R04 promotion and the final Chinese semantic-source freeze specify the
current split authority:

```text
Figures 1–3 = figures/ch5_refq/p0v3_final_v6/
Figure 4    = figures/ch5_refq/p0v3_final_v6_e01_eta_label/
```

The E01 Figure 4 render manifest identifies V6 as its base and records a
terminology-only label delta. It reports no data, geometry, panel-structure,
or scale change and `scientific_recomputation = 0`. The three corrected asset
digests match the files on disk. Thus the authority is discoverable and
technically hash-closed across existing records, but the manuscript-to-panel-
to-file mapping is distributed among several documents rather than maintained
as one current MS-R04 mapping bridge.

### Figure 1–4 status table

| FIGURE_ID | MANUSCRIPT_SECTION | MANUSCRIPT_CAPTION_STATUS | CURRENT_AUTHORITY_ROOT | RENDERED_ASSET_STATUS | PANEL_STRUCTURE_STATUS | SCIENTIFIC_SEMANTIC_STATUS | PROVENANCE_STATUS | MAIN_OR_SUPPLEMENT | MAINTENANCE_RISK | RECOMMENDED_ACTION |
|---|---|---|---|---|---|---|---|---|---|---|
| Figure 1 | §4.1, caption at snapshot line 379 | Present; A evidence flow, B source event composition, C target membership composition | `figures/ch5_refq/p0v3_final_v6/` | SVG/PDF/PNG present; all three hashes match V6 manifest | A–C; matches current caption at the declared figure level | No mismatch found; record units, admission/membership boundary, and RefQN interpretation are bounded | V6 manifest/source manifest hash records; no one-document MS-R04 caption-to-file register | Main | E1 mapping debt; no E0 defect | Freeze current caption, panel identities, root, relative files, and hashes in main-figure mapping |
| Figure 2 | §4.2 RQ2a/RQ2b, caption at snapshot line 510 | Present; A/B source-role CCDFs, C target quantiles, D target-weight concentration | `figures/ch5_refq/p0v3_final_v6/` | SVG/PDF/PNG present; all three hashes match V6 manifest | A–D; matches the current caption; source/target role split is explicit | No mismatch found; 138,974 is described as cross-project RefQ total weight, not edge/record count | V6 manifest/source manifest and Figure 2 text-closure audit; mapping remains distributed | Main | E1 mapping debt; no E0 defect | Map A–D and the figure files/hashes together with the exact MS-R04 caption |
| Figure 3 | §4.2 RQ2c, caption at snapshot line 565 | Present; A structure/community-size summary, B observation-boundary views, C seed-run sensitivity | `figures/ch5_refq/p0v3_final_v6/` | SVG/PDF/PNG present; all three hashes match V6 manifest | A–C; current wording identifies the three views and algorithmic communities | No mismatch found; first-order direction-ignored view and algorithmic partition limits are explicit | V6 manifest/source manifest and caption audits; no consolidated current map | Main | E1 mapping debt; S-stage namespace contributes E2 tracking risk | Map panel names and exact assets; keep algorithmic labels distinct from analysis-stage identifiers |
| Figure 4 | §4.3 RQ3, caption at snapshot line 598 | Present; A–D category mean/median, E rank eta-squared and BH-FDR status | `figures/ch5_refq/p0v3_final_v6_e01_eta_label/` (V6 is its base) | Corrected SVG/PDF/PNG present; all three hashes match E01 manifest and MS-R04 promotion record | A–E; E01 asserts no panel-structure change; matches current caption | Current manuscript and E01 label use rank eta-squared (η_H²); P0 output field remains `epsilon_squared` for the same stated estimator. No value/formula change is evidenced | MS-R04 promotion records E01 hashes; earlier V6/caption-composition records still describe epsilon-squared and predecessor hashes | Main | E2 historical terminology/provenance debt; no current manuscript/render mismatch found | Treat E01 as current Figure 4 asset; annotate predecessor records as historical only in a separately authorized provenance-closure task |

The asset digests (SHA-256) for main figures are:

| Figure | SVG | PDF | PNG |
|---|---|---|---|
| 1 | `63b5a581e65ef305ea7a3fefd1e952e297a799e6f4d6fbb278df6e05b6b74d24` | `88de1c8c6bf62d8246492662f17a98a678bd2306aabccce465b6ffeab15f3229` | `1b30d76b37f171103b0d7f1e803cae1146b163b3e7dcdc1573cb1099c6c8ec5e` |
| 2 | `36f07513c7227261706966ba568475d68269ff8a03ad44b50f78daf06a7f956b` | `762136aae28f520532318308723aa343b5878565745143d59bd6ea904bf262b0` | `f2a86d2d8706415a7723892245eef31eb7c6b5b62a693b4142aed7f3cddf4311` |
| 3 | `b1bba74418b268985e90b7be0696d125fea02b1e6b9522fb8bb759eb0f57cb50` | `6ab0a57e25485a68ec343fc84b1b00c1851ebc21265bf6fe9b9e396c5ff6be7d` | `94d7952e6f00f74f11969c83652bd1379d426b734041f5a1890f0f982a22e22f` |
| 4, current E01 | `6ec08f8462bb13f46395678a5bfb1b5e753377399d5cfa612f85fd273b34e17a` | `daf4f9c486b19f229d0d13586cfceaba774bf7212466d7174877c57f07307c0c` | `6a279ae45570c06e745db65d3b14503b30f2ad98daac5c64dd8611a082fc44ea` |

## 4. `phase2b_design_freeze_manifest.json` role

**Classification: historical design freeze / superseded design reference; not
current rendered authority and not the MS-R04 figure-text mapping authority.**

Evidence: the manifest identifies itself as Phase 2-B design, says
`rendering_authorized = NO` and `render_ready = NO`, and points at earlier
supplemental-v1 or historical inputs. Its figure contracts do not match the
current render/caption structure: for example, its Figure 2 contract covers
only A/B while V6/MS-R04 has A–D; its Figure 4 uses a two-panel
epsilon-squared design, while the current figure has A–E and the E01 rank
eta-squared label. These are superseded editorial/panel and provenance
differences, not evidence of scientific mismatch in the accepted P0-v3 assets.
Do not use Phase 2-B to select current asset files or panel descriptions.

## 5. Main-paper and supplementary separation

V6 separates main items under `main/figure1...figure4...` and supplements
under `supplementary/s1...s4...`; the manifest also says supplementary S5 was
not rendered. Figure 0 is internal and not a paper figure. This is a clear
asset-directory separation, but manuscript-figure-to-file mapping should be
maintained as two independent registers so a main-figure change does not force
an unrelated supplement mapping update:

1. Main-paper Figures 1–4, keyed to the accepted manuscript revision and
   caption/panel identities.
2. Supplementary/robustness S1–S5 (including explicit reserve/not-rendered
   status), keyed to supplementary item identities and render roots.

There is a naming collision risk between analysis stages S1–S7 and
Supplementary Figures S1–S5. They are different namespaces. Use explicit
labels such as `analysis stage S4` and `Supplementary Figure S2`; never infer
one from the other. The separate registers should preserve that distinction.

## 6. Figure 4 effect-size terminology

| Layer | Observed authority |
|---|---|
| Accepted MS-R04 Methods and Figure 4 caption | `rank eta-squared` and `η_H²`; caption at line 598, operational definition at line 364 |
| Current Figure 4 rendered label | V6-E01 changes the display term from `epsilon-squared` to `rank eta-squared`; corrected SVG/PDF/PNG hashes are recorded above |
| Scientific baseline | P0-v3 manifest SHA is frozen; result files retain an `epsilon_squared` column and the manuscript gives the Kruskal–Wallis estimator `(H-k+1)/(n-k)` with truncation at zero |
| Prior rendering/audit records | V6 source manifest and caption-composition audit still describe `epsilon-squared` and the pre-E01 hashes |

**Status: current-facing terminology is aligned; provenance closure is partial.**
The manuscript and E01 label now agree, and E01 records a label-only delta
with no data, geometry, panel, scale, or scientific recomputation change. The
frozen result schema and predecessor records retain `epsilon_squared`. This
is a terminology/provenance distinction, not evidence of changed estimator or
scientific values. A future mapping/provenance record must name E01 as the
current Figure 4 asset and retain V6 as its immutable base; do not edit
historical V6 records in this audit.

## 7. Mapping-gap diagnosis and severity register

The mapping gap is **not** that current roots, asset hashes, or manuscript
captions are unknowable: they are recoverable from the MS-R04 promotion,
V6/E01 manifests, source manifests, and manuscript. The gap is the lack of one
revision-keyed bridge that joins exact MS-R04 caption and body reference →
panel contract → current asset path/format/hash → source manifest/scientific
baseline, while keeping main and supplementary maps separate. The existing
SUB-A02 map records roots but not this per-panel/hash bridge. Source manifests
also predate MS-R04 and name an earlier manuscript SHA, so they cannot alone
establish MS-R04 text-to-asset identity.

| ID | Severity | Finding | Immediate effect |
|---|---|---|---|
| E1-01 | E1 | No single current MS-R04 Figure 1–4 caption/panel/file/hash mapping register; authority is distributed across promotion, render manifests, source manifests, caption audits, and SUB-A02. | Create and verify the current mapping before English reconstruction or submission packaging. No present scientific contradiction was found. |
| E2-01 | E2 | Phase 2-B manifest is explicitly non-render-ready and carries superseded panels/inputs. | Historical design/provenance debt only; do not treat as current. |
| E2-02 | E2 | Older caption-composition audit and V6 Figure 4 source manifest retain epsilon-squared wording and pre-E01 Figure 4 hashes. | Historical record is stale relative to MS-R04/E01; current manuscript and selected E01 render agree. |
| E2-03 | E2 | P0-v3 migration matrix describes older scaffold paths and source replacement actions, rather than the current rendered authority roots. | Useful migration history, not a current figure map. |
| E2-04 | E2 | `S1`–`S7` analysis-stage names can be confused with supplementary Figure S1–S5 labels. | Namespace/documentation debt; two explicit mapping registers and qualified names prevent confusion. |
| INFO-01 | INFO | The V6 final acceptance record accepts the publication presentation; MS-R04 promotion and semantic-source freeze separately identify V6-E01 as Figure 4 authority. | Split lineage is documented across records, but should be made visible in the future current map. |
| INFO-02 | INFO | Render assets and manifests distinguish internal Figure 0, main Figures 1–4, rendered Supplementary S1–S4, and unrendered S5 reserve. | Context only; preserve existing separation. |

```text
E0_COUNT = 0
E1_COUNT = 1
E2_COUNT = 4
INFO_COUNT = 2
```

## 8. Maintenance strategy and sequencing

**Yes: create the current mapping documentation before any caption/prose
repair or English reconstruction.** The audit finds no current manuscript vs
selected-render scientific mismatch requiring immediate text or figure
repair. The next authorized maintenance task should create a revision-keyed
mapping freeze with separate main and supplementary registers. For each main
figure it should record MS-R04 SHA, section/body reference, exact caption, A–E
panel identity, authority root, SVG/PDF/PNG relative paths and SHA-256, source
manifest SHA, P0-v3 authority, and status. The supplementary register should
record S1–S4 roots/hashes and S5 as reserve/not-rendered, and explicitly
separate Supplementary Figure IDs from S1–S7 analysis stages.

Recommended ordering:

1. **First, freeze the two current mappings** from already-existing manifests
   and audits; do not render or recompute.
2. **Then close Figure 4 lineage debt** in a separately authorized
   documentation-only task: designate E01 as current Figure 4, record its
   parent V6 and label-only delta, and mark older caption/source records as
   historical rather than current. Do not rewrite immutable historical files.
3. **Only after mapping review**, conduct any explicitly authorized bounded
   caption/prose repair if an actual mismatch is found, then do English
   reconstruction/submission packaging against the frozen mapping.

The main and supplementary registers can be prepared in parallel once their
separate authority inventories are fixed. Any edit to current manuscript text,
caption, or an asset must be serial after the mapping is accepted, followed by
its own scoped QA. English reconstruction and final packaging are downstream
of both mapping and any authorized repair. Current blockers: none for scientific
correctness; E1 mapping is a gate before reconstruction/packaging. Phase 2-B,
old-matrix, namespace, and predecessor Figure 4 provenance items are E2
documentation debt, not present scientific blockers.

## 9. No-change guards

This task performed reads, hashing, and authority comparison only.

```text
CURRENT_CHANGED = 0
MS_R04_SNAPSHOT_CHANGED = 0
MANUSCRIPT_VERSION_MANIFEST_CHANGED = 0
SIDECAR_CHANGED = 0
SCIENTIFIC_RECOMPUTATION = 0
SCIENTIFIC_ASSETS_CHANGED = 0
FIGURE_ASSETS_CHANGED = 0
FIGURE_RERENDER = 0
MANUSCRIPT_TEXT_CHANGED = 0
FORMAL_MAPPING_DOCUMENT_CREATED = 0
```

Only this audit document is authorized for repository change. The four
pre-existing untracked V3–V6 ZIP archives were preserved and not staged.
