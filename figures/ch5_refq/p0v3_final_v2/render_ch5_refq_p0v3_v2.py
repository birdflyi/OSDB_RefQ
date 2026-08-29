"""Deterministic presentation-only renderer for the frozen Chapter 5 RefQ set.

This module reads frozen CSV/JSON artifacts and formats them as figures.  It
does not import or execute any scientific analysis code.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("PYTHONHASHSEED", "0")

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams.update(
    {
        "svg.hashsalt": "ch5-refq-p0v3-final-v2",
        "svg.fonttype": "none",
        "font.family": "DejaVu Sans",
        "font.size": 8.5,
        "axes.titlesize": 10,
        "axes.labelsize": 8.5,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.5,
        "axes.linewidth": 0.6,
        "grid.linewidth": 0.35,
        "grid.alpha": 0.35,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    }
)
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd


P0_MANIFEST_SHA = "be802b9df223c99bc2089a76ae9ec6e0b6047ab0c58237a5fc3050b51dcc9776"
SUPP_MANIFEST_SHA = "78d07fbda2a045ba309a1cfcb23a68ca2baafa910008b6483c0c4e0acf9211bd"
S6_MANIFEST_SHA = "e9c192d140659b33c870a3b03e9583ec5c39ac0702ecc26f28c78e87648f4eea"
FINAL_MANUSCRIPT_SHA = "5c54bd725becc7ff7253ec023e83258749b1868e14a70d34722adcc1f421bc60"
FINAL_MANUSCRIPT = (
    Path(r"C:/Users/10651/Documents/trae_projects/thesis")
    / "ch5_analysis_reference_coupling_for_osdbms"
    / "第5章-paper1_content_v1.4.3.1_reference_quotient_citation_precision_clean_p0v3_reconciled_finalqa_composition.md"
)

BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
PURPLE = "#CC79A7"
GOLD = "#E69F00"
INK = "#222222"
MUTED = "#666666"
LIGHT = "#F2F2F2"
STATUS_COLORS = {"PROJECT_MAPPABLE": BLUE, "NON_PROJECT": ORANGE, "UNRESOLVED": "#999999"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def fmt_int(value) -> str:
    return f"{int(round(float(value))):,}"


def fmt_pct(value, digits=2) -> str:
    return f"{float(value) * 100:.{digits}f}%"


def add_panel_label(ax, label: str):
    ax.text(-0.04, 1.04, label, transform=ax.transAxes, fontsize=11, fontweight="bold", va="bottom", ha="right")


def clean_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(width=0.5, length=3)


def save_figure(fig, out_dir: Path, figure_id: str):
    out_dir.mkdir(parents=True, exist_ok=True)
    svg = out_dir / f"{figure_id}.svg"
    pdf = out_dir / f"{figure_id}.pdf"
    png = out_dir / f"{figure_id}.png"
    fig.savefig(svg, format="svg", metadata={"Date": None}, bbox_inches="tight", pad_inches=0.08)
    fig.savefig(
        pdf,
        format="pdf",
        metadata={"Creator": "ch5-refq-p0v3-final-v2", "Producer": "matplotlib", "CreationDate": None, "ModDate": None},
        bbox_inches="tight",
        pad_inches=0.08,
    )
    fig.savefig(png, format="png", dpi=300, metadata={"Software": "ch5-refq-p0v3-final-v2"}, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    return {"svg": sha256(svg), "pdf": sha256(pdf), "png": sha256(png)}


class FrozenInputs:
    def __init__(self, repo_root: Path):
        self.repo = repo_root
        self.p0 = repo_root / "outputs" / "reference_quotient_p0_corrected_v3"
        self.supp = repo_root / "supplemental" / "reference_quotient_v2" / "outputs_p0v3"
        self.s6 = self.supp / "S6_figure_ready"
        self.p0_manifest = self.p0 / "manifest.json"
        self.supp_manifest = self.supp / "manifest.json"
        self.s6_manifest = self.s6 / "figure_ready_manifest_v2.json"
        self.s6_entries = {e["output"]: e for e in read_json(self.s6_manifest)["entries"]}
        self.inputs = {}
        self.renderer_contracts = {}

    def register(self, path: Path, s6_name: str | None = None):
        path = path.resolve()
        expected = None
        if s6_name is not None:
            expected = self.s6_entries[s6_name]["output_sha256"]
            actual = sha256(path)
            if actual != expected:
                raise RuntimeError(f"S6 hash closure failure for {s6_name}: {actual} != {expected}")
        actual = sha256(path)
        if path.suffix.lower() == ".csv":
            frame = pd.read_csv(path)
            rows, columns = int(len(frame)), [str(c) for c in frame.columns]
        else:
            rows, columns = None, []
        key = str(path)
        self.inputs[key] = {"path": key, "sha256": actual, "row_count": rows, "columns": columns, "s6_expected_sha256": expected}
        return path

    def csv(self, rel: str, s6_name: str | None = None) -> pd.DataFrame:
        path = self.register(self.repo / rel, s6_name)
        return pd.read_csv(path)

    def json(self, rel: str, s6_name: str | None = None):
        path = self.register(self.repo / rel, s6_name)
        return read_json(path)


def render_figure1(fi: FrozenInputs, out_dir: Path):
    flow = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/evidence_universe_flow.csv")
    event = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq1_referencing_entity_distribution_plot.csv", "rq1_referencing_entity_distribution_plot.csv")
    membership = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/event_type_x_target_membership_status.csv")
    flow_map = dict(zip(flow["stage"], flow["count"]))
    scanned = flow_map["reference_records_before_source_admission"]
    out_of_seed = flow_map["out_of_seed_source_observation_reference_records"]
    admitted = flow_map["admitted_source_observation_reference_records"]
    status_keys = ["target_project_mappable_records", "target_non_project_records", "target_unresolved_records"]
    assert scanned - out_of_seed == admitted
    assert sum(flow_map[k] for k in status_keys) == admitted
    status = [
        ("PROJECT_MAPPABLE", flow_map["target_project_mappable_records"], BLUE),
        ("NON_PROJECT", flow_map["target_non_project_records"], ORANGE),
        ("UNRESOLVED", flow_map["target_unresolved_records"], "#999999"),
    ]
    # The edge list is the visual contract: out-of-seed is a sibling exclusion
    # branch, while admitted has exactly three mutually exclusive children.
    flow_edges = [
        ("scanned", "admitted"),
        ("scanned", "out_of_seed"),
        ("admitted", "project_mappable"),
        ("admitted", "non_project"),
        ("admitted", "unresolved"),
    ]
    assert ("out_of_seed", "admitted") not in flow_edges
    assert sum(edge[0] == "admitted" for edge in flow_edges) == 3
    fi.renderer_contracts.update(
        {
            "F1_source_admission_flow": "BRANCH_EXCLUSION",
            "F1_out_of_seed_exclusion_branch": "PASS",
            "F1_admitted_target_status_branch_count": 3,
            "F1_no_scanned_out_of_seed_admitted_serial_path": "PASS",
        }
    )
    fig = plt.figure(figsize=(7.1, 9.4), constrained_layout=True)
    gs = fig.add_gridspec(3, 1, height_ratios=[1.0, 0.95, 1.2], hspace=0.46)
    axa = fig.add_subplot(gs[0, :])
    add_panel_label(axa, "A")
    axa.axis("off")
    axa.set_title("Evidence-universe flow (Reference records)", loc="left", pad=3)
    # Source admission is drawn as a subtraction branch: the excluded records
    # leave the scanned universe, while the admitted parent fans out by target
    # status. No exclusion box is placed on the admitted path.
    boxes = [
        (0.04, 0.48, 0.22, 0.23, f"SCANNED\n{fmt_int(scanned)}"),
        (0.39, 0.48, 0.22, 0.23, f"ADMITTED\n{fmt_int(admitted)}"),
        (0.39, 0.79, 0.22, 0.14, f"EXCLUDED: OUT OF SEED\n{fmt_int(out_of_seed)}"),
    ]
    for x, y, w, h, txt in boxes:
        edge = ORANGE if "EXCLUDED" in txt else BLUE
        face = "#FCEFE8" if "EXCLUDED" in txt else "#EAF2F8"
        axa.add_patch(patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015", facecolor=face, edgecolor=edge, linewidth=0.8, transform=axa.transAxes))
        axa.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=8.3 if "EXCLUDED" in txt else 9, transform=axa.transAxes)
    axa.annotate("", (0.39, 0.595), (0.26, 0.595), xycoords=axa.transAxes, arrowprops={"arrowstyle": "->", "lw": 0.9, "color": MUTED})
    axa.text(0.325, 0.62, "source admission", ha="center", va="bottom", fontsize=7.0, color=MUTED, transform=axa.transAxes)
    axa.annotate("", (0.50, 0.79), (0.18, 0.71), xycoords=axa.transAxes, arrowprops={"arrowstyle": "->", "lw": 0.85, "color": ORANGE})
    axa.text(0.28, 0.76, "excluded branch", ha="center", va="bottom", fontsize=7.0, color=ORANGE, transform=axa.transAxes)
    total = admitted
    child_positions = [(0.74, 0.73), (0.74, 0.49), (0.74, 0.25)]
    for (name, count, color), (x, y) in zip(status, child_positions):
        axa.add_patch(patches.FancyBboxPatch((x, y), 0.23, 0.16, boxstyle="round,pad=0.012", facecolor=color, alpha=0.16, edgecolor=color, linewidth=0.7, transform=axa.transAxes))
        axa.text(x + 0.115, y + 0.08, f"{name}\n{fmt_int(count)} ({count / total:.2%})", ha="center", va="center", fontsize=7.3, transform=axa.transAxes)
        axa.annotate("", (x, y + 0.08), (0.61, 0.595), xycoords=axa.transAxes, arrowprops={"arrowstyle": "->", "lw": 0.75, "color": color})
    axa.text(0.04, 0.08, f"{fmt_int(scanned)} - {fmt_int(out_of_seed)} = {fmt_int(admitted)}", transform=axa.transAxes, fontsize=7.8, color=MUTED)
    axa.text(0.47, 0.08, f"{fmt_int(status[0][1])} + {fmt_int(status[1][1])} + {fmt_int(status[2][1])} = {fmt_int(admitted)}", transform=axa.transAxes, fontsize=7.8, color=MUTED)
    axa.text(0.04, 0.015, "All values are Reference records; quotient eligibility follows the project-mappable branch.", transform=axa.transAxes, fontsize=7.5, color=MUTED)

    axb = fig.add_subplot(gs[1, 0])
    add_panel_label(axb, "B")
    axb.set_title("Complete source-event composition", loc="left", pad=3)
    event = event.sort_values(["count", "referencing_entity_type"], ascending=[False, True]).reset_index(drop=True)
    labels = event["referencing_entity_type"].astype(str).tolist()
    y = np.arange(len(event))
    axb.barh(y, event["count"], color=BLUE, alpha=0.86)
    axb.set_yticks(y, labels)
    axb.invert_yaxis()
    axb.set_xlabel("Reference records")
    axb.xaxis.set_major_formatter(lambda x, pos: f"{x/1e6:.1f}M")
    for yi, (_, row) in enumerate(event.iterrows()):
        axb.text(row["count"] + event["count"].max() * 0.012, yi, f"{fmt_int(row['count'])} ({row['share']:.1%})", va="center", fontsize=6.8)
    clean_axes(axb)

    axc = fig.add_subplot(gs[2, 0])
    add_panel_label(axc, "C")
    axc.set_title("Target membership by event type", loc="left", pad=3)
    event_type_mapping = {
        "CommitComment": "CommitCommentEvent",
        "IssueComment": "IssueCommentEvent",
        "Push": "PushEvent",
        "PullRequest": "PullRequestEvent",
        "Issue": "IssuesEvent",
        "Release": "ReleaseEvent",
        "PullRequestReview": "PullRequestReviewEvent",
        "PullRequestReviewComment": "PullRequestReviewCommentEvent",
    }
    mapped_order = [event_type_mapping.get(label, label) for label in labels]
    membership_events = set(membership["event_type"].astype(str))
    order = [name for name in mapped_order if name in membership_events]
    order.extend(sorted(membership_events.difference(order)))
    fi.renderer_contracts.update(
        {
            "F1_panel_B_event_order": labels,
            "F1_panel_C_event_order": order,
            "F1_panel_B_C_event_order_aligned": order[: len(labels)] == [event_type_mapping.get(label, label) for label in labels if event_type_mapping.get(label, label) in membership_events],
            "F1_event_name_mapping": event_type_mapping,
        }
    )
    statuses = ["PROJECT_MAPPABLE", "NON_PROJECT", "UNRESOLVED"]
    for yi, et in enumerate(order):
        sub = membership[membership["event_type"] == et].set_index("target_membership_status")
        left = 0.0
        for st in statuses:
            val = float(sub.loc[st, "within_row_share"]) if st in sub.index else 0.0
            axc.barh(yi, val, left=left, color=STATUS_COLORS[st], label=st.replace("_", " ").title() if yi == 0 else None, height=0.72)
            left += val
    axc.set_yticks(np.arange(len(order)), [x.replace("Event", "") for x in order])
    axc.set_xlim(0, 1)
    axc.xaxis.set_major_formatter(lambda x, pos: f"{x:.0%}")
    axc.set_xlabel("Within-event-type share")
    axc.legend(frameon=False, fontsize=6.6, loc="lower right")
    axc.invert_yaxis()
    clean_axes(axc)
    fig.suptitle("Figure 1. Observable Reference evidence and its project-mappable boundary", fontsize=11, x=0.02, ha="left")
    hashes = save_figure(fig, out_dir, "figure1_evidence_universe")
    return hashes, fi.inputs


def render_figure2(fi: FrozenInputs, out_dir: Path):
    ccdf = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq2a_source_role_ecdf_ccdf.csv", "rq2a_source_role_ecdf_ccdf.csv")
    tq = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq2b_target_role_quantiles.csv", "rq2b_target_role_quantiles.csv")
    conc = fi.json("outputs/reference_quotient_p0_corrected_v3/rq2b_target_concentration.json")
    fig, axes = plt.subplots(2, 2, figsize=(7.1, 6.6), constrained_layout=True)
    ax = axes[0, 0]; add_panel_label(ax, "A"); ax.set_title("Source out-degree CCDF", loc="left", pad=3)
    panel_a_series = ["out_degree"]
    for metric, color, label in [("out_degree", BLUE, "out-degree")]:
        sub = ccdf[ccdf["metric"] == metric].sort_values("value")
        ax.plot(sub["value"], sub["ccdf"], color=color, lw=1.5, label=label)
    ax.set_xscale("symlog", linthresh=1); ax.set_yscale("log"); ax.set_xlabel("out-degree (count)"); ax.set_ylabel("CCDF"); ax.grid(True, which="both"); clean_axes(ax)
    ax = axes[0, 1]; add_panel_label(ax, "B"); ax.set_title("Source out-strength CCDF", loc="left", pad=3)
    panel_b_series = ["out_strength"]
    sub = ccdf[ccdf["metric"] == "out_strength"].sort_values("value")
    ax.plot(sub["value"], sub["ccdf"], color=ORANGE, lw=1.5)
    ax.set_xscale("symlog", linthresh=1); ax.set_yscale("log"); ax.set_xlabel("out-strength (aggregated Reference-record weight)"); ax.set_ylabel("CCDF"); ax.grid(True, which="both"); clean_axes(ax)
    ax = axes[1, 0]; add_panel_label(ax, "C"); ax.set_title("Target-role quantile profile (separate scales)", loc="left", pad=3); ax.axis("off")
    metrics = ["in_degree", "in_strength", "target_coverage"]
    qorder = ["q25", "median", "q75", "max"]
    metric_labels = {"in_degree": "in-degree", "in_strength": "in-strength", "target_coverage": "coverage (294 sources)"}
    for idx, metric in enumerate(metrics):
        sax = ax.inset_axes([0.16, 0.70 - idx * 0.32, 0.78, 0.22])
        sub = tq[tq["metric"] == metric].set_index("quantile")
        vals = [float(sub.loc[q, "value"]) for q in qorder]
        sax.plot(range(4), vals, marker="o", color=[BLUE, ORANGE, GREEN][idx], lw=1.1)
        sax.set_xticks(range(4), ["Q1", "Median", "Q3", "Max"]); sax.set_title(metric_labels[metric], fontsize=7.5, loc="left", pad=1); sax.grid(axis="y", alpha=0.25); clean_axes(sax)
        if idx < 2: sax.tick_params(axis="x", labelbottom=False)
        if metric == "target_coverage": sax.yaxis.set_major_formatter(lambda x, pos: f"{x:.0%}")
        elif metric == "in_strength": sax.ticklabel_format(axis="y", style="plain")
    ax = axes[1, 1]; add_panel_label(ax, "D"); ax.set_title("Target weight concentration", loc="left", pad=3)
    shares = [conc["top_1_weight_share"], conc["top_10_weight_share"], conc["top_50_weight_share"]]
    bars = ax.barh(["Top 1", "Top 10", "Top 50"], shares, color=[BLUE, ORANGE, GREEN], alpha=0.86)
    ax.set_xlim(0, 0.55); ax.xaxis.set_major_formatter(lambda x, pos: f"{x:.0%}"); ax.set_xlabel("Share of cross-project weight (n=138,974)")
    for b, v in zip(bars, shares): ax.text(v + 0.01, b.get_y() + b.get_height() / 2, fmt_pct(v), va="center", fontsize=8)
    ax.text(0.02, 0.05, "Top-1 support = 3,430 Reference records", transform=ax.transAxes, fontsize=7.2, color=MUTED); clean_axes(ax)
    rendered_a_series = [line.get_label() for line in axes[0, 0].lines if not line.get_label().startswith("_")]
    rendered_b_series = ["out_strength"] if len(axes[0, 1].lines) == 1 else []
    assert rendered_a_series == ["out-degree"]
    assert rendered_b_series == ["out_strength"]
    assert set(panel_a_series).isdisjoint(panel_b_series)
    fi.renderer_contracts.update(
        {
            "F2_PANEL_A_SERIES": panel_a_series,
            "F2_PANEL_B_SERIES": panel_b_series,
            "F2_SHARED_DEGREE_STRENGTH_AXIS": "NO",
            "F2_panel_A_renderer_labels": rendered_a_series,
            "F2_panel_B_line_count": len(axes[0, 1].lines),
        }
    )
    fig.suptitle("Figure 2. Asymmetric source and target views of observed Project-level RefQ", fontsize=11, x=0.02, ha="left")
    return save_figure(fig, out_dir, "figure2_source_target_roles"), fi.inputs


def render_figure3(fi: FrozenInputs, out_dir: Path):
    summary = fi.json("outputs/reference_quotient_p0_corrected_v3/rq2c_undirected_view_summary.json")
    structural = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/structural_summary.csv", "structural_summary.csv")
    sizes = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/community_size_distribution.csv", "community_size_distribution.csv")
    sensitivity = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S3_observation_sensitivity/observation_boundary_sensitivity.csv")
    runs = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/louvain_stability_plot.csv", "louvain_stability_plot.csv")
    stab = fi.json("supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_summary.json")
    fig = plt.figure(figsize=(7.1, 8.7), constrained_layout=True)
    gs = fig.add_gridspec(3, 1, height_ratios=[1.15, 1.05, 1.35], hspace=0.56)
    agrid = gs[0].subgridspec(1, 2, width_ratios=[0.48, 0.52], wspace=0.34)
    axa = fig.add_subplot(agrid[0]); add_panel_label(axa, "A"); axa.axis("off"); axa.set_title("Undirected structure", loc="left", pad=3)
    metric_lines = [
        f"nodes = {fmt_int(summary['nodes'])}", f"undirected edges = {fmt_int(summary['undirected_edges'])}", f"components = {summary['components']} | isolates = {summary['isolates']}",
        f"LCC = {fmt_int(summary['lcc_nodes'])} nodes, {fmt_int(summary['lcc_edges'])} edges", f"clustering = {summary['average_clustering_lcc']:.5f}", f"transitivity = {summary['transitivity_lcc']:.5f}",
        f"canonical communities = {summary['algorithmic_communities']}", f"modularity = {summary['modularity']:.6f}",
    ]
    axa.text(0.02, 0.94, "\n".join(metric_lines), va="top", family="DejaVu Sans Mono", fontsize=7.2, transform=axa.transAxes)
    axsize = fig.add_subplot(agrid[1]); ss = sizes.sort_values(["community_size", "community_id"], ascending=[False, True]); ysize = np.arange(len(ss))[::-1]
    axsize.barh(ysize, ss["community_size"], color=PURPLE, alpha=0.82); axsize.set_yticks([]); axsize.set_xlabel("community size"); axsize.set_title("35 sizes (descending)", loc="left", fontsize=8.5); clean_axes(axsize)
    axb = fig.add_subplot(gs[1]); add_panel_label(axb, "B"); axb.axis("off"); axb.set_title("Observation-boundary sensitivity (separate metric scales)", loc="left", pad=3)
    view_order = ["CANONICAL_SEED_CENTERED_OBSERVED", "SEED_ONLY_INDUCED", "MULTI_SEED_TARGET_VIEW"]
    metric_specs = [("lcc_coverage", "LCC coverage"), ("average_clustering_lcc", "average clustering (LCC)"), ("modularity", "modularity")]
    for idx, (col, label) in enumerate(metric_specs):
        sax = axb.inset_axes([0.05 + idx * 0.32, 0.16, 0.27, 0.69]); vals = [float(sensitivity[sensitivity["view"] == v].iloc[0][col]) for v in view_order]
        sax.bar(np.arange(3), vals, color=[BLUE, ORANGE, GREEN], alpha=0.84); sax.set_xticks(np.arange(3), ["can.", "seed", "multi"]); sax.set_title(label, fontsize=7.6, loc="left"); sax.grid(axis="y", alpha=0.25); sax.yaxis.set_major_formatter((lambda x, pos: f"{x:.0%}") if col == "lcc_coverage" else (lambda x, pos: f"{x:.3f}")); clean_axes(sax)
    axc = fig.add_subplot(gs[2]); add_panel_label(axc, "C"); axc.axis("off"); axc.set_title("Seed sensitivity of the algorithmic modular neighborhood view", loc="left", pad=3)
    c1 = axc.inset_axes([0.06, 0.38, 0.27, 0.48]); c2 = axc.inset_axes([0.38, 0.38, 0.27, 0.48]); c3 = axc.inset_axes([0.70, 0.38, 0.27, 0.48])
    runs = runs.sort_values("seed").reset_index(drop=True)
    canonical = int(stab["canonical_seed"])
    matches = np.flatnonzero(runs["seed"].to_numpy(dtype=int) == canonical)
    assert len(matches) == 1, f"canonical seed must resolve to exactly one display row: {canonical}"
    canonical_display_index = int(matches[0])
    canonical_row = runs.iloc[canonical_display_index]
    run_index = np.arange(len(runs))
    c1.plot(run_index, runs["community_count"], color=BLUE, lw=1.0); c1.scatter([canonical_display_index], [int(canonical_row["community_count"])], color=ORANGE, zorder=3); c1.set_ylabel("count"); c1.set_xlabel("run index"); c1.set_title("community count", fontsize=8); clean_axes(c1)
    c2.plot(run_index, runs["modularity"], color=GREEN, lw=1.0); c2.scatter([canonical_display_index], [float(canonical_row["modularity"])], color=ORANGE, zorder=3); c2.set_ylabel("modularity"); c2.set_xlabel("run index"); c2.set_title("modularity", fontsize=8); clean_axes(c2)
    c3.plot(run_index, runs["ari_to_canonical"], color=PURPLE, lw=1.0); c3.axhline(0.9, color=MUTED, ls="--", lw=0.7); c3.scatter([canonical_display_index], [float(canonical_row["ari_to_canonical"])], color=ORANGE, zorder=3); c3.set_ylabel("ARI"); c3.set_xlabel("run index"); c3.set_title("ARI to canonical", fontsize=8); clean_axes(c3)
    axc.text(0.06, 0.19, f"50 runs | community count 32--37 | 42/50 below ARI 0.9 | min ARI = {stab['ari_to_canonical_summary']['min']:.6f} | min pairwise ARI = {stab['pairwise_ari_summary']['min']:.6f}", transform=axc.transAxes, fontsize=7.4, color=MUTED)
    axc.text(0.06, 0.08, "Canonical seed 20260731 is a deterministic reference realization; no stable partition or consensus interpretation is implied.", transform=axc.transAxes, fontsize=7.2, color=MUTED)
    fi.renderer_contracts.update(
        {
            "F3_canonical_seed": canonical,
            "F3_canonical_display_index": canonical_display_index,
            "F3_canonical_highlight_resolved_by_seed": "YES",
        }
    )
    fig.suptitle("Figure 3. First-order undirected RefQ structure and seed-sensitive algorithmic modular neighborhood view", fontsize=10.5, x=0.02, ha="left")
    return save_figure(fig, out_dir, "figure3_undirected_structure"), fi.inputs


def render_figure4(fi: FrozenInputs, out_dir: Path):
    desc = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq3_subdomain_descriptive_comparison_plot.csv", "rq3_subdomain_descriptive_comparison_plot.csv")
    eff = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/rq3_kruskal_fdr_effect_sizes_plot.csv", "rq3_kruskal_fdr_effect_sizes_plot.csv")
    features = ["self_reference_ratio", "external_reference_share", "non_project_reference_share", "comment_reference_density"]
    feature_labels = {"self_reference_ratio": "self-reference ratio", "external_reference_share": "external-reference share", "non_project_reference_share": "non-project share", "comment_reference_density": "comment-reference density"}
    modes = ["include_mixed", "exclude_mixed_or_multilabel"]
    fig = plt.figure(figsize=(7.1, 11.2), constrained_layout=True)
    gs = fig.add_gridspec(2, 1, height_ratios=[2.7, 1.25], hspace=0.72)
    top = gs[0].subgridspec(2, 2, hspace=0.80, wspace=0.38)
    for i, feature in enumerate(features):
        ax = fig.add_subplot(top[i // 2, i % 2]); add_panel_label(ax, chr(ord("A") + i)); ax.set_title(feature_labels[feature], loc="left", pad=3)
        sub = desc[desc["feature"] == feature].copy(); cats = sorted(sub["category"].unique())
        ybase = np.arange(len(cats)); mode_offsets = {m: (-0.14 if m == modes[0] else 0.14) for m in modes}
        for mode, color in zip(modes, [BLUE, ORANGE]):
            msub = sub[sub["label_mode"] == mode].set_index("category")
            for metric, marker, dx in [("mean", "o", -0.035), ("median", "s", 0.035)]:
                vals = [float(msub.loc[c, metric]) if c in msub.index else np.nan for c in cats]
                vals = np.asarray(vals, dtype=float)
                display_vals = vals * 100 if feature != "comment_reference_density" else vals
                ax.scatter(display_vals, ybase + mode_offsets[mode] + dx, s=21, marker=marker, facecolor=color if metric == "mean" else "white", edgecolor=color, linewidth=0.8, label=("include mixed" if mode == modes[0] else "exclude mixed") + (" mean" if metric == "mean" else " median") if i == 0 else None)
        ax.set_yticks(ybase, cats); ax.tick_params(axis="y", labelsize=7.0); ax.set_xlabel("percent" if feature != "comment_reference_density" else "native density"); ax.grid(axis="x", alpha=0.25); clean_axes(ax)
        if feature != "comment_reference_density": ax.xaxis.set_major_formatter(lambda x, pos: f"{x:.0f}%")
    handles, labels = fig.axes[0].get_legend_handles_labels()
    fig.axes[0].legend_.remove() if fig.axes[0].legend_ is not None else None
    fig.legend(handles, labels, frameon=False, fontsize=6.5, ncol=4, loc="upper center", bbox_to_anchor=(0.5, 0.985))
    axb = fig.add_subplot(gs[1]); add_panel_label(axb, "E"); axb.set_title("FDR-bounded effect-size comparison", loc="left", pad=3)
    feature_order = list(dict.fromkeys(eff["feature"].tolist()))
    ypos = np.arange(len(feature_order));
    for mode, marker, color in [(modes[0], "o", BLUE), (modes[1], "^", ORANGE)]:
        sub = eff[eff["label_mode"] == mode].set_index("feature")
        for yi, feature in enumerate(feature_order):
            row = sub.loc[feature]; reject = bool(row["fdr_bh_reject_0_05"]); axb.scatter(float(row["epsilon_squared"]), yi + (-0.13 if mode == modes[0] else 0.13), marker=marker, s=30, facecolor=color if reject else "white", edgecolor=color, linewidth=0.9)
    axb.set_yticks(ypos, [feature_labels.get(x, x.replace("_", " ")) for x in feature_order]); axb.set_xlabel("epsilon-squared"); axb.set_xlim(left=-0.005); axb.grid(axis="x", alpha=0.25); clean_axes(axb)
    axb.text(0.99, 1.05, "filled = BH-FDR reject; open = not reject", transform=axb.transAxes, ha="right", fontsize=7.2, color=MUTED)
    fig.suptitle("Figure 4. Observed subdomain variation and FDR-bounded role/structure comparisons", fontsize=10.8, x=0.02, ha="left")
    return save_figure(fig, out_dir, "figure4_rq3_comparison"), fi.inputs


def render_s1(fi: FrozenInputs, out_dir: Path):
    df = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S2_weight_sensitivity/edge_weight_sensitivity.csv")
    df = df.sort_values("threshold")
    fig = plt.figure(figsize=(7.1, 7.3), constrained_layout=True)
    gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.35], hspace=0.55)
    top = gs[0].subgridspec(1, 2, wspace=0.32)
    ax = fig.add_subplot(top[0]); add_panel_label(ax, "A"); ax.set_title("Retained directed edges", loc="left", pad=3); ax.plot(df["threshold"], df["directed_edges_retained"], marker="o", color=BLUE, lw=1.4); ax.set_xlabel("multiplicity threshold"); ax.set_ylabel("directed edges retained"); ax.set_xticks(df["threshold"]); ax.grid(axis="y", alpha=0.25); clean_axes(ax)
    ax = fig.add_subplot(top[1]); add_panel_label(ax, "B"); ax.set_title("Weight share and LCC coverage", loc="left", pad=3); ax.plot(df["threshold"], df["directed_weight_share"], marker="o", color=ORANGE, label="weight share"); ax.plot(df["threshold"], df["lcc_coverage"], marker="s", color=GREEN, label="LCC coverage"); ax.set_ylim(0, 1.05); ax.set_xlabel("multiplicity threshold"); ax.set_ylabel("proportion"); ax.set_xticks(df["threshold"]); ax.yaxis.set_major_formatter(lambda x, pos: f"{x:.0%}"); ax.legend(frameon=False, fontsize=6.8); ax.grid(axis="y", alpha=0.25); clean_axes(ax)
    ax = fig.add_subplot(gs[1]); ax.axis("off"); add_panel_label(ax, "C"); ax.set_title("Exact frozen values", loc="left", pad=3)
    cols = ["threshold", "directed_edges_retained", "directed_weight_retained", "directed_weight_share", "lcc_nodes", "lcc_edges", "lcc_coverage", "algorithmic_communities", "modularity"]
    table = df[cols].copy(); table["directed_weight_share"] = table["directed_weight_share"].map(lambda x: f"{x:.6f}"); table["lcc_coverage"] = table["lcc_coverage"].map(lambda x: f"{x:.6f}"); table["modularity"] = table["modularity"].map(lambda x: f"{x:.6f}")
    header = "thr   edges   weight    share     LCC-nodes  LCC-edges  LCC-cov   comm  modularity"
    ax.text(0.02, 0.82, header, family="DejaVu Sans Mono", fontsize=7.0, weight="bold", transform=ax.transAxes)
    ax.plot([0.02, 0.98], [0.79, 0.79], color="#cccccc", lw=0.6, transform=ax.transAxes)
    for i, row in table.iterrows():
        line = f"{int(row['threshold']):>3} {int(row['directed_edges_retained']):>7} {int(row['directed_weight_retained']):>8} {row['directed_weight_share']:>8} {int(row['lcc_nodes']):>10} {int(row['lcc_edges']):>10} {row['lcc_coverage']:>8} {int(row['algorithmic_communities']):>5} {row['modularity']:>10}"
        ax.text(0.02, 0.70 - i * 0.13, line, family="DejaVu Sans Mono", fontsize=7.0, transform=ax.transAxes)
    ax.text(0.0, 0.02, "Threshold = retained Reference-record multiplicity for an ordered project pair; it is not event support, semantic strength, or an optimal threshold.", transform=ax.transAxes, fontsize=7.2, color=MUTED)
    fig.suptitle("Supplementary S1. Reference-record multiplicity sensitivity", fontsize=10.8, x=0.02, ha="left")
    return save_figure(fig, out_dir, "supplementary_s1_multiplicity_sensitivity"), fi.inputs


def render_s2(fi: FrozenInputs, out_dir: Path):
    runs = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/louvain_stability_plot.csv", "louvain_stability_plot.csv")
    pair = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_pairwise.csv")
    summary = fi.json("supplemental/reference_quotient_v2/outputs_p0v3/S4_community_stability/louvain_stability_summary.json")
    fig, axes = plt.subplots(1, 3, figsize=(7.1, 3.6), constrained_layout=True)
    ax = axes[0]; add_panel_label(ax, "A"); ax.set_title("All 50 ARI values", loc="left", pad=3); runs = runs.sort_values("seed"); ax.plot(np.arange(len(runs)), runs["ari_to_canonical"], marker="o", ms=2.8, color=PURPLE, lw=0.8); ax.axhline(0.9, color=MUTED, ls="--", lw=0.7); ax.set_xlabel("run (seed order)"); ax.set_ylabel("ARI to canonical"); ax.set_ylim(0.6, 1.02); clean_axes(ax)
    ax = axes[1]; add_panel_label(ax, "B"); ax.set_title("Community-count frequency", loc="left", pad=3); freq = runs["community_count"].value_counts().sort_index(); ax.bar(freq.index.astype(str), freq.values, color=BLUE, alpha=0.85); ax.set_xlabel("community count"); ax.set_ylabel("runs"); clean_axes(ax)
    ax = axes[2]; add_panel_label(ax, "C"); ax.set_title("Pairwise ARI distribution", loc="left", pad=3); ax.hist(pair["ari"], bins=10, color=ORANGE, alpha=0.82, edgecolor="white"); ax.axvline(summary["pairwise_ari_summary"]["min"], color=MUTED, ls="--", lw=0.8); ax.set_xlabel("pairwise ARI"); ax.set_ylabel("pairs"); clean_axes(ax)
    fig.text(0.02, -0.02, f"50 runs | community count 32--37 | min ARI = {summary['ari_to_canonical_summary']['min']:.6f} | min pairwise ARI = {summary['pairwise_ari_summary']['min']:.6f}. Community IDs have no substantive interpretation.", fontsize=7.3, color=MUTED)
    fig.suptitle("Supplementary S2. Louvain seed stability under the declared algorithmic view", fontsize=10.8, x=0.02, ha="left")
    return save_figure(fig, out_dir, "supplementary_s2_louvain_stability"), fi.inputs


def render_s3(fi: FrozenInputs, out_dir: Path):
    incl = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S5_brokerage_stability/brokerage_topk_inclusion_frequency.csv")
    runs = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S6_figure_ready/brokerage_stability_plot.csv", "brokerage_stability_plot.csv")
    summary = fi.json("supplemental/reference_quotient_v2/outputs_p0v3/S5_brokerage_stability/brokerage_stability_summary.json")
    fig = plt.figure(figsize=(7.1, 7.4), constrained_layout=True)
    gs = fig.add_gridspec(2, 1, height_ratios=[0.95, 1.25], hspace=0.58)
    top = gs[0].subgridspec(1, 2, wspace=0.32)
    frozen_spearman = runs["spearman_to_canonical"].to_numpy(dtype=float)
    assert np.all(np.isfinite(frozen_spearman))
    observed_min = float(np.min(frozen_spearman))
    observed_max = float(np.max(frozen_spearman))
    observed_range = observed_max - observed_min
    padding = 0.05 * observed_range if observed_range > 0 else 5e-5
    spearman_xmin = observed_min - padding
    spearman_min = float(summary["spearman_summary"]["min"])
    assert np.isclose(spearman_min, 0.9998339514284217, rtol=0.0, atol=1e-15)
    # Plot the frozen agreement values directly; the axis is presentation-only.
    ax = fig.add_subplot(top[0]); add_panel_label(ax, "A"); ax.set_title("Spearman agreement to canonical", loc="left", pad=3); ax.hist(frozen_spearman, bins=np.linspace(spearman_xmin, 1.0, 11), color=BLUE, alpha=0.85); ax.axvline(spearman_min, color=MUTED, ls="--", lw=0.8); ax.set_xlim(spearman_xmin, 1.0); ax.set_xticks(np.linspace(spearman_xmin, 1.0, 4)); ax.xaxis.set_major_formatter(lambda x, pos: f"{x:.5f}"); ax.tick_params(axis="x", labelrotation=20); ax.set_xlabel("Spearman rho"); ax.set_ylabel("runs"); clean_axes(ax)
    fi.renderer_contracts.update(
        {
            "S3_panel_A_metric": "spearman_to_canonical",
            "S3_panel_A_transform": "NONE",
            "S3_panel_A_minimum": spearman_min,
            "S3_panel_A_xlimit": [spearman_xmin, 1.0],
            "S3_panel_A_data_equals_frozen": "PASS",
        }
    )
    ax = fig.add_subplot(top[1]); add_panel_label(ax, "B"); ax.set_title("Top-50 overlap stability", loc="left", pad=3); ax.hist(runs["top50_overlap"], bins=np.linspace(0.8, 1.0, 11), color=GREEN, alpha=0.85); ax.axvline(summary["top50_overlap_summary"]["min"], color=MUTED, ls="--", lw=0.8); ax.set_xlabel("top-50 overlap"); ax.set_ylabel("runs"); clean_axes(ax)
    ax = fig.add_subplot(gs[1]); add_panel_label(ax, "C"); ax.set_title("Canonical top-50 inclusion frequency (k=250)", loc="left", pad=3)
    sub = incl[(incl["k"] == 250) & (incl["top_k"] == 50)].sort_values(["inclusion_frequency", "project_id"], ascending=[True, True]).tail(50)
    ax.barh(np.arange(len(sub)), sub["inclusion_frequency"], color=PURPLE, alpha=0.82); ax.set_yticks([]); ax.set_xlim(0, 1.05); ax.xaxis.set_major_formatter(lambda x, pos: f"{x:.0%}"); ax.set_xlabel("inclusion frequency across 20 runs"); clean_axes(ax)
    fig.text(0.02, 0.015, f"Minimum Spearman = {summary['spearman_summary']['min']} | minimum top-50 overlap = {summary['top50_overlap_summary']['min']:.2f} | robustness_alert = FALSE", fontsize=7.3, color=MUTED)
    fig.suptitle("Supplementary S3. Structural brokerage-candidate ranking stability", fontsize=10.8, x=0.02, ha="left")
    return save_figure(fig, out_dir, "supplementary_s3_brokerage_stability"), fi.inputs


def render_s4(fi: FrozenInputs, out_dir: Path):
    flow = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/evidence_universe_flow.csv")
    edge = fi.csv("supplemental/reference_quotient_v2/outputs_p0v3/S1_evidence_universe/edge_class_counts.csv")
    stage_labels = {
        "reference_records_before_source_admission": "before admission",
        "admitted_source_observation_reference_records": "admitted",
        "out_of_seed_source_observation_reference_records": "out of seed",
        "missing_event_repository_id_reference_records": "missing repo ID",
        "invalid_event_repository_id_reference_records": "invalid repo ID",
        "target_project_mappable_records": "target mappable",
        "target_non_project_records": "target non-project",
        "target_unresolved_records": "target unresolved",
        "target_ambiguous_records": "target ambiguous",
        "conflict_excluded_record_occurrences": "conflict excluded",
        "quotient_eligible_records": "quotient eligible",
        "self_loop_evidence_weight": "self-loop evidence",
        "cross_project_evidence_weight": "cross-project evidence",
        "self_loop_edge_count": "self-loop edges",
        "cross_project_directed_edge_count": "cross-project directed edges",
    }
    rows = []
    for _, r in flow.iterrows():
        measure = "-" if pd.isna(r["measure"]) else str(r["measure"])
        rows.append([stage_labels.get(r["stage"], str(r["stage"])), fmt_int(r["count"]), r["unit"], measure])
    for _, r in edge.iterrows():
        rows.append([str(r["edge_class"]).replace("_", " ").title(), fmt_int(r["count"]), r["unit"], "edge-class weight"])
    fig, ax = plt.subplots(figsize=(7.1, 7.0), constrained_layout=True); ax.axis("off"); add_panel_label(ax, "A"); ax.set_title("Unit-aware audit of frozen counts and weights", loc="left", pad=3)
    header = "stage / class               count        unit                measure"
    ax.text(0.02, 0.94, header, family="DejaVu Sans Mono", fontsize=6.8, weight="bold", transform=ax.transAxes)
    ax.plot([0.02, 0.98], [0.925, 0.925], color="#cccccc", lw=0.6, transform=ax.transAxes)
    for i, row in enumerate(rows):
        short_measure = {"AGGREGATED_EDGE_WEIGHT": "aggregated edge weight", "SELF_LOOP_EDGE_COUNT": "self-loop edge count", "CROSS_PROJECT_DIRECTED_EDGE_COUNT": "cross-project edge count", "edge-class weight": "edge-class weight"}.get(str(row[3]), str(row[3]))
        line = f"{str(row[0])[:27]:<27} {str(row[1]):>10}  {str(row[2]):<18} {short_measure[:27]}"
        ax.text(0.02, 0.885 - i * 0.045, line, family="DejaVu Sans Mono", fontsize=6.6, color=INK, transform=ax.transAxes)
    ax.text(0.0, 0.02, "RECORD counts, REFERENCE_RECORD/aggregated RefQ weights, and EDGE_COUNT values are separate contracts; no common quantitative axis is implied.", transform=ax.transAxes, fontsize=7.4, color=MUTED)
    fig.suptitle("Supplementary S4. Reference-record, aggregated-weight, and edge-count contract", fontsize=10.8, x=0.02, ha="left")
    return save_figure(fig, out_dir, "supplementary_s4_unit_contract"), fi.inputs


FIGURE_SPECS = {
    "figure1_evidence_universe": {"kind": "main", "render": render_figure1, "dir": "main/figure1_evidence_universe", "contract": "A flow; B complete eight-category source composition; C event-type target-membership shares.", "keys": ["3,748,078", "3,747,958", "1,586,047"]},
    "figure2_source_target_roles": {"kind": "main", "render": render_figure2, "dir": "main/figure2_source_target_roles", "contract": "Source degree/strength CCDF; target quantiles; top-1/10/50 concentration.", "keys": ["294", "2.47%", "16.00%", "48.99%"]},
    "figure3_undirected_structure": {"kind": "main", "render": render_figure3, "dir": "main/figure3_undirected_structure", "contract": "Structure summary; observation-boundary sensitivity; seed sensitivity.", "keys": ["35", "0.796922", "32--37", "42/50"]},
    "figure4_rq3_comparison": {"kind": "main", "render": render_figure4, "dir": "main/figure4_rq3_comparison", "contract": "Descriptive mean/median displays and epsilon-squared with explicit BH-FDR status.", "keys": ["include_mixed", "exclude_mixed_or_multilabel"]},
    "supplementary_s1_multiplicity_sensitivity": {"kind": "supplementary", "render": render_s1, "dir": "supplementary/s1_multiplicity_sensitivity", "contract": "Thresholds 1, 2, 5, 10; retained edge counts, weight share, and LCC coverage.", "keys": ["1", "2", "5", "10"]},
    "supplementary_s2_louvain_stability": {"kind": "supplementary", "render": render_s2, "dir": "supplementary/s2_louvain_stability", "contract": "All 50 ARI values, community-count frequency, pairwise ARI distribution.", "keys": ["0.682367", "0.609244"]},
    "supplementary_s3_brokerage_stability": {"kind": "supplementary", "render": render_s3, "dir": "supplementary/s3_brokerage_stability", "contract": "Spearman, top-50 overlap, and canonical top-50 inclusion frequency.", "keys": ["0.9998339514284217", "0.82", "FALSE"]},
    "supplementary_s4_unit_contract": {"kind": "supplementary", "render": render_s4, "dir": "supplementary/s4_unit_contract", "contract": "Unit-aware table separating RECORD, aggregated Reference-record weight, and EDGE_COUNT.", "keys": ["RECORD", "REFERENCE_RECORD", "EDGE_COUNT"]},
}


def make_source_manifest(fi: FrozenInputs, spec, out_dir: Path, output_hashes: dict, script_hash: str):
    manifest = {
        "figure_id": next(k for k, v in FIGURE_SPECS.items() if v is spec),
        "figure_plan_path": "docs/freeze/ch5_refq_p0v3_final_figure_plan_v1.md",
        "final_manuscript_sha256": FINAL_MANUSCRIPT_SHA,
        "composition_display_policy_path": "docs/freeze/ch5_refq_p0v3_composition_table_display_policy_v1.md",
        "authority_roots": {"corrected_p0_v3": "outputs/reference_quotient_p0_corrected_v3", "corrected_supplemental_v2": "supplemental/reference_quotient_v2/outputs_p0v3"},
        "input_files": sorted(fi.inputs),
        "input_sha256": {k: v["sha256"] for k, v in sorted(fi.inputs.items())},
        "input_row_counts": {k: v["row_count"] for k, v in sorted(fi.inputs.items())},
        "input_columns": {k: v["columns"] for k, v in sorted(fi.inputs.items())},
        "S6_manifest_closure": "PASS" if all(v["s6_expected_sha256"] is None or v["sha256"] == v["s6_expected_sha256"] for v in fi.inputs.values()) else "FAIL",
        "display_only_transformations": ["stable sorting for display", "formatting frozen values", "no scientific recomputation"],
        "panel_contract": spec["contract"],
        "renderer_contract_assertions": fi.renderer_contracts,
        "expected_key_values": spec["keys"],
        "render_runtime": runtime_info(),
        "render_script_sha256": script_hash,
        "svg_sha256": output_hashes["svg"], "pdf_sha256": output_hashes["pdf"], "png_sha256": output_hashes["png"], "status": "PASS",
    }
    with (out_dir / "source_manifest.json").open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=2, sort_keys=True); fh.write("\n")
    return sha256(out_dir / "source_manifest.json")


def runtime_info():
    return {"python": platform.python_version(), "pandas": pd.__version__, "numpy": np.__version__, "matplotlib": matplotlib.__version__, "platform": platform.platform(), "backend": matplotlib.get_backend(), "pythonhashseed": os.environ.get("PYTHONHASHSEED", "0")}


def make_contact_sheet(output_root: Path):
    figure_ids = list(FIGURE_SPECS)
    fig, axes = plt.subplots(4, 2, figsize=(11.0, 14.0), constrained_layout=True)
    for ax, figure_id in zip(np.asarray(axes).ravel(), figure_ids):
        png = output_root / FIGURE_SPECS[figure_id]["dir"] / f"{figure_id}.png"
        image = plt.imread(png)
        height, width = image.shape[:2]
        ax.imshow(image)
        ax.set_title(f"{figure_id}\n{width} x {height} px", fontsize=8, loc="left")
        ax.axis("off")
    contact_path = output_root / "human_qa_contact_sheet.png"
    fig.savefig(contact_path, format="png", dpi=200, metadata={"Software": "ch5-refq-p0v3-final-v2"}, bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    image = plt.imread(contact_path)
    return {"path": "human_qa_contact_sheet.png", "sha256": sha256(contact_path), "width": int(image.shape[1]), "height": int(image.shape[0])}


def render_all(output_root: Path):
    repo = Path(__file__).resolve().parents[3]
    output_root = output_root.resolve()
    if output_root.exists():
        script_path = Path(__file__).resolve()
        if output_root == script_path.parent:
            for child in output_root.iterdir():
                if child.resolve() != script_path:
                    if child.is_dir():
                        shutil.rmtree(child)
                    else:
                        child.unlink()
        else:
            shutil.rmtree(output_root)
    output_root.mkdir(parents=True)
    fi = FrozenInputs(repo)
    for manifest_path, expected in [(fi.p0_manifest, P0_MANIFEST_SHA), (fi.supp_manifest, SUPP_MANIFEST_SHA), (fi.s6_manifest, S6_MANIFEST_SHA)]:
        if sha256(manifest_path) != expected: raise RuntimeError(f"authority manifest hash mismatch: {manifest_path}")
    if not FINAL_MANUSCRIPT.exists() or sha256(FINAL_MANUSCRIPT) != FINAL_MANUSCRIPT_SHA: raise RuntimeError("final composition manuscript hash mismatch")
    plan = repo / "docs" / "freeze" / "ch5_refq_p0v3_final_figure_plan_v1.md"
    policy = repo / "docs" / "freeze" / "ch5_refq_p0v3_composition_table_display_policy_v1.md"
    script_hash = sha256(Path(__file__).resolve())
    outputs = {}
    source_manifest_hashes = {}
    renderer_contracts = {}
    for figure_id, spec in FIGURE_SPECS.items():
        fi.inputs = {}
        fi.renderer_contracts = {}
        fig_dir = output_root / spec["dir"]
        hashes, _ = spec["render"](fi, fig_dir)
        source_manifest_hashes[figure_id] = make_source_manifest(fi, spec, fig_dir, hashes, script_hash)
        outputs[figure_id] = {"relative_dir": spec["dir"], **hashes}
        renderer_contracts[figure_id] = fi.renderer_contracts.copy()
    determinism_status = os.environ.get("CH5_REFQ_DETERMINISM_CLOSURE", "PENDING")
    contact_sheet = make_contact_sheet(output_root)
    render_manifest = {
        "render_set_version": "ch5-refq-p0v3-final-v2", "parent_repository_HEAD": os.environ.get("CH5_REFQ_PARENT_HEAD", "654e5dde871a437ee949343651d6aa71932bcacc"),
        "final_manuscript_path": str(FINAL_MANUSCRIPT), "final_manuscript_SHA": FINAL_MANUSCRIPT_SHA,
        "composition_policy_path": str(policy.relative_to(repo)).replace("\\", "/"), "composition_policy_SHA": sha256(policy), "figure_plan_SHA": sha256(plan),
        "P0_manifest_SHA": P0_MANIFEST_SHA, "supplemental_manifest_SHA": SUPP_MANIFEST_SHA, "S6_manifest_SHA": S6_MANIFEST_SHA,
        "runtime": runtime_info(), "script_SHA": script_hash, "figures": outputs, "source_manifest_SHA": source_manifest_hashes,
        "renderer_contract_assertions": renderer_contracts, "contact_sheet": contact_sheet,
        "attempt_determinism": {"svg": determinism_status, "pdf": determinism_status, "png": determinism_status}, "historical_figure_immutability": "CHECKED_EXTERNALLY", "scientific_root_immutability": "CHECKED_EXTERNALLY", "v1_render_root": "figures/ch5_refq/p0v3_final", "supplementary_S5_rendered": "NO", "figure0_modified": "NO", "status": "READY_FOR_HUMAN_VISUAL_QA" if determinism_status == "PASS" else "RENDERED_ATTEMPT",
    }
    with (output_root / "render_manifest_v2.json").open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(render_manifest, fh, indent=2, sort_keys=True); fh.write("\n")
    return render_manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", required=True, type=Path)
    args = parser.parse_args()
    render_all(args.output_root)
    print(json.dumps({"status": "PASS", "output_root": str(args.output_root.resolve())}, sort_keys=True))


if __name__ == "__main__":
    main()
