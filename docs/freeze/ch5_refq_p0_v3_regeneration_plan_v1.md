# Chapter 5 RefQ Corrected P0 v3 Regeneration Plan v1

1. Freeze the shared `network_views.py` metadata alignment fix and direct
   regression tests. Do not alter identity, membership, quotient, graph, seed,
   Louvain, brokerage, or threshold semantics.
2. Use `configs/ch5_reference_quotient_p0_v3.yaml`, derived from the accepted
   v2 config. The only operational changes are clean versioned output identity
   (`frozen_output_root`) and run provenance (`run_id_prefix`). Scientific
   settings and all accepted input roots remain unchanged.
3. Require a clean worktree, v2 manifest/hash closure, accepted aggregate
   294/294 closure, and historical immutability before execution.
4. Run exactly one P0 v3 execution with the existing P0 CLI semantics:
   `python -m script.ch5_reference_quotient.cli --config configs/ch5_reference_quotient_p0_v3.yaml --workspace-root . --execute`.
   This is a regeneration from frozen corrected aggregate inputs; do not run
   GH-CoRE, event rejoin, or external retrieval.
5. Validate all v3 counts, partition closure, community-size closure, modularity,
   and v2/v3 scientific differential gates. Preserve any partial root on failure;
   do not delete or retry it.
6. Commit v3 outputs only after all gates pass. Then create the docs-only review
   and supplemental migration plan. Do not run supplemental S1-S7 in this task.

The intended v2-to-v3 scientific difference is limited to corrected
`community_size` label association plus versioned provenance/manifest/config
metadata. Any graph, partition, brokerage, RQ1, RQ2a, RQ2b, or RQ3 difference is
an unexpected scientific diff and blocks acceptance.
