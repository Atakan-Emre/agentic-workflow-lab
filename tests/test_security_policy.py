"""Tests for security policy presence and constraints."""

from scripts._utils import POLICIES_DIR, load_yaml


def test_security_policy_exists():
    path = POLICIES_DIR / "security-policy.yaml"
    assert path.exists()


def test_security_policy_forbids_secret_commits():
    data = load_yaml(POLICIES_DIR / "security-policy.yaml")
    never_commit = data["secrets"]["never_commit"]
    assert ".env" in never_commit
    assert "credentials.json" in never_commit


def test_security_policy_requires_shell_justification():
    data = load_yaml(POLICIES_DIR / "security-policy.yaml")
    assert data["shell"]["require_justification"] is True
