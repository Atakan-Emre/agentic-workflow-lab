"""Tests for instruction file scanning."""

from scripts.scan_instruction_files import scan_instruction_files


def test_instruction_files_pass():
    errors, _warnings = scan_instruction_files()
    assert errors == []


def test_required_root_instruction_files_exist():
    from scripts._utils import REPO_ROOT

    assert (REPO_ROOT / "AGENTS.md").exists()
    assert (REPO_ROOT / "CLAUDE.md").exists()
    assert (REPO_ROOT / ".github" / "copilot-instructions.md").exists()
