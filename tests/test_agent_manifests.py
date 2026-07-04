"""Tests for agent manifest validation."""

from scripts.validate_agent_manifests import validate_manifests


def test_all_manifests_are_valid():
    errors, _warnings = validate_manifests()
    assert errors == []


def test_expected_manifest_count():
    _errors, _warnings = validate_manifests()
    from scripts._utils import MANIFESTS_DIR

    assert len(list(MANIFESTS_DIR.glob("*.yaml"))) == 7
