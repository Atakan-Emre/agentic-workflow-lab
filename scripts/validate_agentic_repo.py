"""Top-level repository validation for agent-ready governance."""

from __future__ import annotations

import sys
from datetime import datetime, timezone

from scripts._utils import REPO_ROOT
from scripts.check_approval_gates import check_approval_gates
from scripts.scan_instruction_files import scan_instruction_files
from scripts.validate_agent_manifests import validate_manifests
from scripts.validate_tool_policy import validate_tool_policy


def main() -> int:
    print(f"Validating agentic repository: {REPO_ROOT}")
    print("=" * 60)

    all_errors: list[str] = []
    all_warnings: list[str] = []

    checks = [
        ("Required instruction files", scan_instruction_files),
        ("Agent manifests", validate_manifests),
        ("Tool policy", validate_tool_policy),
        ("Approval gates", check_approval_gates),
    ]

    passed = 0
    for name, fn in checks:
        errors, warnings = fn()
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        status = "PASS" if not errors else "FAIL"
        print(f"[{status}] {name}")
        if errors:
            for error in errors:
                print(f"  ERROR: {error}")
        passed += 0 if errors else 1

    print("=" * 60)
    if all_warnings:
        print(f"Warnings ({len(all_warnings)}):")
        for warning in all_warnings:
            print(f"  WARNING: {warning}")

    timestamp = datetime.now(timezone.utc).isoformat()
    print(f"Validation completed at {timestamp}")
    print(f"Checks passed: {passed}/{len(checks)}")

    if all_errors:
        print("Repository validation FAILED.")
        return 1

    print("Repository validation PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
