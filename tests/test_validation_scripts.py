"""Integration tests for validation scripts."""

import subprocess
import sys
from pathlib import Path

from scripts.check_approval_gates import check_approval_gates
from scripts.validate_agentic_repo import main as validate_repo_main


REPO_ROOT = Path(__file__).resolve().parent.parent


def test_validate_agentic_repo_main_returns_zero():
    assert validate_repo_main() == 0


def test_approval_gates_pass():
    errors, _warnings = check_approval_gates()
    assert errors == []


def test_validate_agentic_repo_cli():
    result = subprocess.run(
        [sys.executable, "scripts/validate_agentic_repo.py"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "Repository validation PASSED" in result.stdout


def test_mcp_list_manifests_cli():
    result = subprocess.run(
        [sys.executable, "mcp/server.py", "list_agent_manifests"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "intake-agent.yaml" in result.stdout
