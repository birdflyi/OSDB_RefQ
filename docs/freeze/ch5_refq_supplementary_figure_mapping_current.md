# Chapter 5 RefQ — Current Supplementary Figure Mapping

## Mapping identity

```text
MAPPING_BASE_MANUSCRIPT_REVISION = MS-R04
MAPPING_BASE_MANUSCRIPT_SHA = F80715045483F482D6640CF072FD61C58F7374182E1DF70D55B3EC500CF53549
MAPPING_SCIENTIFIC_BASELINE = P0-v3
MAPPING_CREATED_FROM = existing frozen assets and existing authority records
SCIENTIFIC_RECOMPUTATION = 0
FIGURE_RERENDER = 0
REGISTER_SCOPE = SUPPLEMENTARY_AND_ROBUSTNESS_ITEMS_ONLY
```

This register is independent of
`docs/freeze/ch5_refq_main_figure_text_mapping_current.md`; it contains no
main-paper Figures 1–4 records. The accepted V6 render manifest is
`figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json` (SHA-256
`469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da`). It
contains rendered supplementary S1–S4 under `supplementary/` and explicitly
records `supplementary_S5_rendered = NO`. S5 remains a reserve; this mapping
does not authorize creating it.

The shared P0-v3 baseline is recorded by
`outputs/reference_quotient_p0_corrected_v3/manifest.json` (SHA-256
`be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776`) and
`supplemental/reference_quotient_v2/outputs_p0v3/manifest.json` (SHA-256
`78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd`).

## Supplementary inventory

| SUPPLEMENT_ID | MAIN_OR_SUPPLEMENT | ROLE | STATUS | CURRENT_AUTHORITY_ROOT | MANUSCRIPT_OR_APPENDIX_REFERENCE | CURRENT_STATUS | MAINTENANCE_TRIGGER |
|---|---|---|---|---|---|---|---|
| Supplementary Figure S1 | SUPPLEMENTARY | Reference-record multiplicity sensitivity | RENDERED | `figures/ch5_refq/p0v3_final_v6/` | No direct S1 citation found in accepted MS-R04; planned supplementary item per final figure plan | MAPPED_HASH_VERIFIED | Change to supplementary S1 identity, status, asset, reference, or provenance |
| Supplementary Figure S2 | SUPPLEMENTARY | Louvain/community partition stability | RENDERED | `figures/ch5_refq/p0v3_final_v6/` | No direct S2 citation found in accepted MS-R04; planned supplementary item per final figure plan | MAPPED_HASH_VERIFIED | Change to supplementary S2 identity, status, asset, reference, or provenance |
| Supplementary Figure S3 | SUPPLEMENTARY | Structural brokerage-candidate stability | RENDERED | `figures/ch5_refq/p0v3_final_v6/` | No direct S3 citation found in accepted MS-R04; planned supplementary item per final figure plan | MAPPED_HASH_VERIFIED | Change to supplementary S3 identity, status, asset, reference, or provenance |
| Supplementary Figure S4 | SUPPLEMENTARY | Unit and weight-contract audit | RENDERED | `figures/ch5_refq/p0v3_final_v6/` | No direct S4 citation found in accepted MS-R04; planned supplementary item per final figure plan | MAPPED_HASH_VERIFIED | Change to supplementary S4 identity, status, asset, reference, or provenance |
| Supplementary Figure S5 | SUPPLEMENTARY | Fixed-object evidence-composition reviewer reserve | RESERVED_NOT_RENDERED | No rendered authority root | Reviewer-reserve item in final figure plan; not an accepted rendered figure or direct MS-R04 figure reference | RESERVE_ONLY_NO_ASSET | Explicit future reviewer need and separate authorization; never infer render authorization from reserve status |

All S1–S4 rendered files below were rehashed and matched against the V6
render manifest. Each row gives the exact paths relative to the V6 root.

### Supplementary Figure S1

```text
ROLE = Reference-record multiplicity sensitivity; thresholds 1, 2, 5, and 10
STATUS = RENDERED
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/supplementary/s1_multiplicity_sensitivity/source_manifest.json
SOURCE_MANIFEST_SHA256 = 8909abf67c4c372c1c4116e1860e26ec86548ee6251c19002db72bc8fdb3cd45
SCIENTIFIC_BASELINE_REFERENCE = supplemental/reference_quotient_v2/outputs_p0v3/S2_weight_sensitivity/; P0-v3 manifest
MANUSCRIPT_OR_APPENDIX_REFERENCE = no direct MS-R04 citation found; final figure plan inventory
MAINTENANCE_TRIGGER = only a change to supplementary S1 inventory, status, asset, or provenance
SVG_RELATIVE_PATH = supplementary/s1_multiplicity_sensitivity/supplementary_s1_multiplicity_sensitivity.svg
SVG_SHA256 = 8238af8d1303baac03ced9cecf5373ac9d92dd55610f528f52a3d3664ab5ce5e
PDF_RELATIVE_PATH = supplementary/s1_multiplicity_sensitivity/supplementary_s1_multiplicity_sensitivity.pdf
PDF_SHA256 = 568612462f7226c119af095123b5d0cafcc39b1c9969d552cf5b5d75f473cc56
PNG_RELATIVE_PATH = supplementary/s1_multiplicity_sensitivity/supplementary_s1_multiplicity_sensitivity.png
PNG_SHA256 = 928cdfa7d9e1d5a7cf6691a6cc9c98f7bb59cbd2d3dab8a9d9ea79a3498852aa
```

### Supplementary Figure S2

```text
ROLE = Louvain stability: 50 ARI values, community-count frequency, pairwise ARI distribution
STATUS = RENDERED
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/supplementary/s2_louvain_stability/source_manifest.json
SOURCE_MANIFEST_SHA256 = 84de9a327457220a78b6d327f09c9ea4a96c7d7e838061d7cf82cb85c51aa38c
SCIENTIFIC_BASELINE_REFERENCE = supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/; P0-v3 manifest
MANUSCRIPT_OR_APPENDIX_REFERENCE = no direct MS-R04 citation found; final figure plan inventory
MAINTENANCE_TRIGGER = only a change to supplementary S2 inventory, status, asset, or provenance
SVG_RELATIVE_PATH = supplementary/s2_louvain_stability/supplementary_s2_louvain_stability.svg
SVG_SHA256 = 82bb19482576b560ca40bd778cd6c04b33e2c07e20f4ccd7a4e6e0a1caaf26e0
PDF_RELATIVE_PATH = supplementary/s2_louvain_stability/supplementary_s2_louvain_stability.pdf
PDF_SHA256 = fbe0efe54f6b8fa2ad064997374fdb554bf40f9ff403bb7f470129b8b34b7552
PNG_RELATIVE_PATH = supplementary/s2_louvain_stability/supplementary_s2_louvain_stability.png
PNG_SHA256 = f3db529178117260e5b0fde4298db678a4046e1f2475d2878952991d725ce27e
```

### Supplementary Figure S3

```text
ROLE = Structural brokerage-candidate stability; ranking stability under declared settings
STATUS = RENDERED
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/supplementary/s3_brokerage_stability/source_manifest.json
SOURCE_MANIFEST_SHA256 = 243d32e566b75aa02678a37f22d8d2209e2513a04fb4598463e4e77aa0b47283
SCIENTIFIC_BASELINE_REFERENCE = supplemental/reference_quotient_v2/outputs_p0v3/S5_brokerage_stability/; P0-v3 manifest
MANUSCRIPT_OR_APPENDIX_REFERENCE = no direct MS-R04 citation found; final figure plan inventory
MAINTENANCE_TRIGGER = only a change to supplementary S3 inventory, status, asset, or provenance
SVG_RELATIVE_PATH = supplementary/s3_brokerage_stability/supplementary_s3_brokerage_stability.svg
SVG_SHA256 = bf56b9efb690681c8950f35f615b82f737f02756b54b4c09eedf822d7a4c4505
PDF_RELATIVE_PATH = supplementary/s3_brokerage_stability/supplementary_s3_brokerage_stability.pdf
PDF_SHA256 = 0694920c038e8321b12ee6dd67bf39b3c803b2077b51dd9ce1048116e7e68b15
PNG_RELATIVE_PATH = supplementary/s3_brokerage_stability/supplementary_s3_brokerage_stability.png
PNG_SHA256 = 1fd66d8fcb7e50978ce7fb5f38e1d3c7da03321195b649d20d4cf9f4bc30f892
```

### Supplementary Figure S4

```text
ROLE = Unit audit separating records, aggregated Reference-record weight, and edge count
STATUS = RENDERED
CURRENT_AUTHORITY_ROOT = figures/ch5_refq/p0v3_final_v6/
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
SOURCE_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/supplementary/s4_unit_contract/source_manifest.json
SOURCE_MANIFEST_SHA256 = dc6f9f1dbdbb38205114fd964c71d9db1000f4f93757d9f16a55f6abf3f763d3
SCIENTIFIC_BASELINE_REFERENCE = supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/; P0-v3 manifest
MANUSCRIPT_OR_APPENDIX_REFERENCE = no direct MS-R04 citation found; final figure plan inventory
MAINTENANCE_TRIGGER = only a change to supplementary S4 inventory, status, asset, or provenance
SVG_RELATIVE_PATH = supplementary/s4_unit_contract/supplementary_s4_unit_contract.svg
SVG_SHA256 = b458c0c2410ec01bbdd2bfabf306a34b239e3f7af90a865f3d62555783f3c0da
PDF_RELATIVE_PATH = supplementary/s4_unit_contract/supplementary_s4_unit_contract.pdf
PDF_SHA256 = 11cdadd6dd5097f1a1ca1e40ec5dddc06194c59d37cd4c74b5af3c164624c143
PNG_RELATIVE_PATH = supplementary/s4_unit_contract/supplementary_s4_unit_contract.png
PNG_SHA256 = a7d92310c8e360ecee1f29690ecc88a3fb5289f1b1dfdbe69fd70c87a769b55a
```

### Supplementary Figure S5 reserve

```text
SUPPLEMENT_ID = Supplementary Figure S5
ROLE = fixed-object evidence composition reviewer reserve
STATUS = RESERVED_NOT_RENDERED
CURRENT_AUTHORITY_ROOT = none; no accepted rendered file in V6
RENDER_MANIFEST_PATH = figures/ch5_refq/p0v3_final_v6/render_manifest_v6.json
RENDER_MANIFEST_SHA256 = 469a7eb68bd31b5ec1578ecaf1eaabc41fecf7cdff5b4bbfa499e9e5676fa8da
SOURCE_MANIFEST_PATH = none in current accepted render root
SCIENTIFIC_BASELINE_REFERENCE = historical S7 fixed-object sources only if separately authorized; no current rendered result
MANUSCRIPT_OR_APPENDIX_REFERENCE = reviewer reserve in docs/freeze/ch5_refq_p0v3_final_figure_plan_v1.md; no direct MS-R04 figure reference found
CURRENT_STATUS = RESERVE_ONLY; NOT_RENDERED; NOT_AN_AUTHORITY_FOR_A_RENDERED_FIGURE
MAINTENANCE_TRIGGER = separate explicit decision and authorization to render or remove reserve status
```

## Namespace and maintenance rules

```text
ANALYSIS_STAGE_NAMESPACE = S1, S2, S3, S4, S5, S6, S7
SUPPLEMENTARY_FIGURE_NAMESPACE = Supplementary Figure S1; Supplementary Figure S2; Supplementary Figure S3; Supplementary Figure S4; Supplementary Figure S5
NAMESPACES_INTERCHANGEABLE = NO
```

In prose, use `analysis stage S5` / `the S5 robustness analysis` for a
scientific pipeline stage and `Supplementary Figure S5` for a figure item. Do
not rename assets to resolve this ambiguity.

```text
MAIN_MAPPING_UPDATE_TRIGGER = changes to main Figures 1–4 manuscript identity, caption/body reference, asset, panel structure, or render/provenance authority only
SUPPLEMENTARY_MAPPING_UPDATE_TRIGGER = changes to supplementary inventory, render status, asset, reference, or provenance only
SHARED_BASELINE_CHANGE_REQUIRES_BOTH = only when it materially changes both mapping identities
MAIN_ONLY_CHANGE_REQUIRES_SUPPLEMENTARY_REWRITE = NO
SUPPLEMENTARY_ONLY_CHANGE_REQUIRES_MAIN_REWRITE = NO
FIGURE0_STATUS = no Figure 0 asset found in the current repository render tree; prior migration record calls it internal/non-paper
```

### Inventory closure

```text
SUPPLEMENTARY_INVENTORY_RESOLVED = YES
S1_STATUS_RESOLVED = YES
S2_STATUS_RESOLVED = YES
S3_STATUS_RESOLVED = YES
S4_STATUS_RESOLVED = YES
S5_STATUS_RESOLVED = YES
MAIN_SUPPLEMENT_NAMESPACE_SEPARATED = YES
E0_COUNT = 0
E1_COUNT = 0
E2_COUNT = 4
INFO_COUNT = 2
```

The E2 findings are inherited documentation/provenance items only: historical
Phase 2-B design, pre-E01 Figure 4 terminology/hashes, the older scaffold-based
migration matrix, and S-stage naming ambiguity. None changes the current
supplementary inventory or main-figure mapping.
