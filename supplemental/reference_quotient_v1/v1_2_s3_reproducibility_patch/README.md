# S3-Only Canonical Reproducibility Patch

This additive patch corrects only the S3 observation-boundary sensitivity
construction. It does not inspect, rerun or modify S2, and it does not rerun
any raw scan or network sensitivity family other than the three S3 views.

The corrected implementation follows the canonical P0 path:

1. directed cross-project rows are passed through
   `script.ch5_reference_quotient.network_views.directed_to_undirected_edges`;
2. the full node registry is inserted in CSV order;
3. restricted view node domains use stable seed-manifest/registry order;
4. `analyze_undirected_view` is called with the same seed and canonical graph
   semantics.

The old S3 output remains in place as historical provenance and is marked
superseded by the patch manifest.
