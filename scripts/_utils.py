"""Shared helpers for agentic-workflow-lab validation scripts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "schemas"
POLICIES_DIR = REPO_ROOT / "policies"
MANIFESTS_DIR = REPO_ROOT / "agents" / "manifests"

RISKY_KEYWORDS = [
    "api_key",
    "api-key",
    "password",
    "secret",
    "token",
    "private_key",
    "BEGIN RSA PRIVATE KEY",
    "sk-",
    "ghp_",
]

FORBIDDEN_COMMAND_PATTERNS = [
    re.compile(r"git\s+push\s+--force", re.I),
    re.compile(r"git\s+reset\s+--hard", re.I),
    re.compile(r"curl\s+.*\|\s*bash", re.I),
    re.compile(r"wget\s+.*\|\s*sh", re.I),
    re.compile(r"Invoke-Expression", re.I),
    re.compile(r"\biex\s*\(", re.I),
    re.compile(r"rm\s+-rf\s+/", re.I),
]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_schema(name: str) -> dict[str, Any]:
    return load_json(SCHEMAS_DIR / name)


def parse_markdown_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    if not content.startswith("---"):
        return {}, content

    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)
    if not isinstance(frontmatter, dict):
        return {}, content
    return frontmatter, body


def scan_text_for_risks(text: str, source: str) -> list[str]:
    warnings: list[str] = []
    lowered = text.lower()

    for keyword in RISKY_KEYWORDS:
        if keyword.lower() in lowered:
            warnings.append(f"{source}: risky keyword detected: {keyword}")

    for pattern in FORBIDDEN_COMMAND_PATTERNS:
        if pattern.search(text):
            warnings.append(f"{source}: forbidden command pattern: {pattern.pattern}")

    return warnings


def required_sections_present(body: str, sections: list[str]) -> list[str]:
    missing: list[str] = []
    for section in sections:
        if section not in body:
            missing.append(section)
    return missing


def load_known_policy_tools() -> set[str]:
    data = load_yaml(POLICIES_DIR / "tool-policy.yaml")
    known: set[str] = set()
    for rule in data.get("rules", []):
        known.update(rule.get("tools") or [])
    known.update(data.get("approval_required_tools", []))
    return known


def extract_markdown_section(body: str, heading: str) -> str:
    marker = f"## {heading}"
    start = body.find(marker)
    if start == -1:
        return ""

    content_start = start + len(marker)
    next_heading = body.find("\n## ", content_start)
    if next_heading == -1:
        return body[content_start:].strip()
    return body[content_start:next_heading].strip()


GOVERNANCE_VALIDATION_COMMANDS = (
    "python scripts/validate_agentic_repo.py",
    "pytest -q",
    "agentic-lab-validate",
    "ruff check .",
)
