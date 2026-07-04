"""Tests for MCP read-only path safety."""

from __future__ import annotations

import pytest

from mcp.tools.read_project_file import _resolve_safe, read_project_file


def test_resolve_safe_rejects_path_escape():
    with pytest.raises(ValueError, match="Path escapes repository root"):
        _resolve_safe("../AGENTS.md")


def test_read_project_file_reads_agents_md():
    result = read_project_file("AGENTS.md")
    assert result["path"] == "AGENTS.md"
    assert "content" in result
    assert "AGENTS.md" in result["content"] or "agent" in result["content"].lower()
