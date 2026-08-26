"""Fail-closed C3.7-A orchestration shell.

Only configuration validation, scaffold preflight, and plan display are
available. Scientific stage flags are intentionally blocked before any output
path is opened or any scientific module is imported.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional, Sequence

from .manifest import validate_scaffold_provenance
from .paths import DEFAULT_CONFIG_PATH, load_config, validate_scaffold_config


NOT_AUTHORIZED_IN_C37A = "NOT_AUTHORIZED_IN_C3_7A"
STAGES = ("S1", "S2", "S3", "S4", "S5", "S6", "S7")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Corrected supplemental v2 C3.7-A scaffold")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="scaffold YAML path")
    parser.add_argument("--validate-config", action="store_true", help="validate corrected authority paths and manifest")
    parser.add_argument("--preflight-scaffold", action="store_true", help="run read-only scaffold preflight")
    parser.add_argument("--show-plan", action="store_true", help="show the non-executable stage plan")
    for stage in STAGES:
        parser.add_argument("--run-%s" % stage.lower(), action="store_true", help=argparse.SUPPRESS)
    return parser


def stage_requests(args: argparse.Namespace) -> list[str]:
    return [stage for stage in STAGES if getattr(args, "run_%s" % stage.lower())]


def show_plan() -> None:
    print("C3.7-A scaffold plan")
    print("S1 -> S2 -> S3 -> S4/S5 -> S6")
    print("S7: outside DAG; future read-only overlap gate")
    print("scientific execution: NOT_AUTHORIZED_IN_C3_7A")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    requested = stage_requests(args)
    if requested:
        print("%s: %s" % (NOT_AUTHORIZED_IN_C37A, ", ".join(requested)), file=sys.stderr)
        return 2
    if not (args.validate_config or args.preflight_scaffold or args.show_plan):
        parser.print_help()
        return 0
    if args.show_plan:
        show_plan()
    if args.validate_config or args.preflight_scaffold:
        config = load_config(args.config)
        result = validate_scaffold_provenance(config)
        result["preflight_only"] = True
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
