"""Validate approval gates in approval-policy.yaml."""

from __future__ import annotations

import sys

from jsonschema import Draft202012Validator

from scripts._utils import POLICIES_DIR, load_schema, load_yaml


def check_approval_gates() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    path = POLICIES_DIR / "approval-policy.yaml"

    if not path.exists():
        errors.append("Missing policies/approval-policy.yaml")
        return errors, warnings

    data = load_yaml(path)
    gates = data.get("gates", [])
    if not gates:
        errors.append("approval-policy.yaml must define at least one gate")
        return errors, warnings

    schema = load_schema("approval-gate.schema.json")
    validator = Draft202012Validator(schema)

    gate_ids: set[str] = set()
    for gate in gates:
        for issue in validator.iter_errors(gate):
            errors.append(f"approval gate {gate.get('id', '<unknown>')}: {issue.message}")

        gate_id = gate.get("id")
        if gate_id in gate_ids:
            errors.append(f"Duplicate approval gate id: {gate_id}")
        gate_ids.add(gate_id)

    defaults = data.get("defaults", {})
    if defaults.get("deny_by_default") is not True:
        errors.append("approval-policy defaults.deny_by_default must be true")

    if defaults.get("allow_read_only_without_approval") is not True:
        errors.append("approval-policy defaults.allow_read_only_without_approval must be true")

    return errors, warnings


def main() -> int:
    errors, warnings = check_approval_gates()
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Approval gate validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
