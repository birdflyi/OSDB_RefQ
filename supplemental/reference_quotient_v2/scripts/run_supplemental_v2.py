"""Explicit one-stage C4 runner and read-only C3.7-F plan surface."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Optional, Sequence

from .historical_immutability import DEFAULT_BASELINE_PATH
from .orchestrator import OrchestrationError, run_stage
from .paths import DEFAULT_CONFIG_PATH


NOT_AUTHORIZED_IN_C37A = "NOT_AUTHORIZED_IN_C3_7A"
LEGACY_STAGES = ("S1", "S2", "S3", "S4", "S5", "S6", "S7")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Corrected supplemental v2 explicit C4 stage runner")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--baseline", default=str(DEFAULT_BASELINE_PATH))
    parser.add_argument("--validate-config", action="store_true")
    parser.add_argument("--preflight-scaffold", action="store_true")
    parser.add_argument("--show-plan", action="store_true")
    parser.add_argument("--run-stage", choices=("S1", "S2", "S3", "S4", "S5", "S6"))
    parser.add_argument("--authorization-phase")
    parser.add_argument("--expected-implementation-commit")
    parser.add_argument("--dry-run", action="store_true", help="authorize and preflight without loading scientific data")
    for stage in LEGACY_STAGES:
        parser.add_argument("--run-%s" % stage.lower(), action="store_true", help=argparse.SUPPRESS)
    return parser


def stage_requests(args: argparse.Namespace) -> list[str]:
    return [stage for stage in LEGACY_STAGES if getattr(args, "run_%s" % stage.lower())]


def show_plan() -> None:
    print("C3.7-F/C4 explicit stage plan")
    print("S1 -> S2 -> S3 -> S4 -> S5 -> S6")
    print("legacy shorthand: S1 -> S2 -> S3 -> S4/S5 -> S6")
    print("S7: outside DAG; future read-only overlap gate")
    print("scientific execution: NOT_AUTHORIZED_IN_C3_7A")
    print("production invocation requires exactly one --run-stage, matching --authorization-phase, and --expected-implementation-commit")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    legacy = [stage for stage in LEGACY_STAGES if getattr(args, "run_%s" % stage.lower())]
    if legacy:
        print("%s: %s" % (NOT_AUTHORIZED_IN_C37A, ", ".join(legacy)), file=sys.stderr)
        return 2
    if args.show_plan:
        show_plan()
    if args.run_stage:
        if not args.authorization_phase or not args.expected_implementation_commit:
            parser.error("--run-stage requires --authorization-phase and --expected-implementation-commit")
        try:
            result = run_stage(
                args.run_stage,
                authorization_phase=args.authorization_phase,
                expected_implementation_commit=args.expected_implementation_commit,
                config_path=args.config,
                baseline_path=args.baseline,
                dry_run=args.dry_run,
            )
        except OrchestrationError as exc:
            print("C4_STAGE_BLOCKED: %s" % exc, file=sys.stderr)
            return 2
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.validate_config or args.preflight_scaffold:
        from .manifest import validate_scaffold_provenance
        from .paths import load_config

        config = load_config(args.config)
        result = validate_scaffold_provenance(config)
        result["preflight_only"] = True
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.show_plan:
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
