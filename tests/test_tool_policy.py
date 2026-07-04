"""Tests for tool policy validation."""

from scripts.validate_tool_policy import validate_tool_policy


def test_tool_policy_passes():
    errors, _warnings = validate_tool_policy()
    assert errors == []


def test_write_tools_require_approval():
    from scripts._utils import POLICIES_DIR, load_yaml

    data = load_yaml(POLICIES_DIR / "tool-policy.yaml")
    approval = set(data["approval_required_tools"])
    assert "write" in approval
    assert "shell" in approval
    assert data["defaults"]["external_write_allowed"] is False
