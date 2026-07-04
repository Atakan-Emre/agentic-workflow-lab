"""Validate tool policy against schema and governance rules."""

from __future__ import annotations

import sys

from jsonschema import Draft202012Validator

from scripts._utils import POLICIES_DIR, load_schema, load_yaml


def validate_tool_policy() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    path = POLICIES_DIR / "tool-policy.yaml"

    if not path.exists():
        errors.append("Missing policies/tool-policy.yaml")
        return errors, warnings

    data = load_yaml(path)
    schema = load_schema("tool-policy.schema.json")
    validator = Draft202012Validator(schema)

    for issue in validator.iter_errors(data):
        errors.append(f"tool-policy.yaml: {issue.message}")

    defaults = data.get("defaults", {})
    if defaults.get("read_only_allowed") is not True:
        errors.append("defaults.read_only_allowed must be true")

    if defaults.get("write_requires_approval") is not True:
        errors.append("defaults.write_requires_approval must be true")

    if defaults.get("external_write_allowed") is not False:
        errors.append("defaults.external_write_allowed must be false")

    approval_tools = set(data.get("approval_required_tools", []))
    write_like = {"write", "edit", "delete_file", "shell", "git_commit", "git_push"}
    if not write_like.issubset(approval_tools):
        missing = sorted(write_like - approval_tools)
        errors.append(f"approval_required_tools missing write-capable tools: {missing}")

    deny_rules = [rule for rule in data.get("rules", []) if rule.get("effect") == "deny"]
    if not deny_rules:
        errors.append("At least one deny rule is required")

    forbidden_patterns = data.get("forbidden_patterns", [])
    if not forbidden_patterns:
        errors.append("forbidden_patterns must not be empty")

    return errors, warnings


def main() -> int:
    errors, warnings = validate_tool_policy()
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Tool policy validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
