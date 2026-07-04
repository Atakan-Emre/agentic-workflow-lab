"""Validate agent manifest YAML files against JSON Schema."""

from __future__ import annotations

import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts._utils import MANIFESTS_DIR, load_schema, load_yaml


def validate_manifests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    schema = load_schema("agent-manifest.schema.json")
    validator = Draft202012Validator(schema)

    manifest_files = sorted(MANIFESTS_DIR.glob("*.yaml"))
    if not manifest_files:
        errors.append("No agent manifests found in agents/manifests/")
        return errors, warnings

    names: set[str] = set()
    for path in manifest_files:
        data = load_yaml(path)
        for issue in validator.iter_errors(data):
            errors.append(f"{path.name}: {issue.message}")

        name = data.get("name")
        if name in names:
            errors.append(f"Duplicate manifest name: {name}")
        names.add(name)

        allowed = set(data.get("allowed_tools", []))
        blocked = set(data.get("blocked_tools", []))
        overlap = allowed & blocked
        if overlap:
            errors.append(f"{path.name}: tools in both allowed and blocked: {sorted(overlap)}")

    return errors, warnings


def main() -> int:
    errors, warnings = validate_manifests()
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Agent manifests validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
