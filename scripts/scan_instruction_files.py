"""Scan instruction files for required structure and frontmatter."""

from __future__ import annotations

import sys

from scripts._utils import (
    GOVERNANCE_VALIDATION_COMMANDS,
    REPO_ROOT,
    extract_markdown_section,
    load_known_policy_tools,
    parse_markdown_frontmatter,
    required_sections_present,
    scan_text_for_risks,
)


def validate_claude_subagents() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    agents_dir = REPO_ROOT / ".claude" / "agents"

    required_frontmatter = {"name", "description", "tools"}
    required_body_sections = [
        "## Role",
        "## Responsibilities",
        "## Allowed actions",
        "## Forbidden actions",
        "## Quality checklist",
        "## Handoff rules",
    ]
    known_policy_tools = load_known_policy_tools()

    for path in sorted(agents_dir.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        frontmatter, body = parse_markdown_frontmatter(content)
        missing_fm = required_frontmatter - set(frontmatter)
        if missing_fm:
            errors.append(f"{path.name}: missing frontmatter keys: {sorted(missing_fm)}")

        if "tools" in frontmatter and not isinstance(frontmatter["tools"], list):
            errors.append(f"{path.name}: tools frontmatter must be a list")

        missing_sections = required_sections_present(body, required_body_sections)
        if missing_sections:
            errors.append(f"{path.name}: missing sections: {missing_sections}")

        rel_path = str(path.relative_to(REPO_ROOT))
        for tool in frontmatter.get("tools", []):
            if isinstance(tool, str) and tool not in known_policy_tools:
                warnings.append(
                    f"{rel_path}: tool '{tool}' is not declared in tool-policy.yaml"
                )

        warnings.extend(scan_text_for_risks(content, rel_path))

    return errors, warnings


def validate_skills() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skills_root = REPO_ROOT / ".agents" / "skills"

    required_frontmatter = {"name", "description"}
    required_body_sections = [
        "## When to use",
        "## Steps",
        "## Expected files",
        "## Validation command",
        "## Anti-patterns",
    ]

    for skill_dir in sorted(skills_root.iterdir()):
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"Missing SKILL.md in {skill_dir.name}")
            continue

        content = skill_path.read_text(encoding="utf-8")
        frontmatter, body = parse_markdown_frontmatter(content)
        missing_fm = required_frontmatter - set(frontmatter)
        if missing_fm:
            errors.append(f"{skill_path}: missing frontmatter keys: {sorted(missing_fm)}")

        missing_sections = required_sections_present(body, required_body_sections)
        if missing_sections:
            errors.append(f"{skill_path}: missing sections: {missing_sections}")

        validation_section = extract_markdown_section(body, "Validation command")
        if validation_section and not any(
            cmd in validation_section for cmd in GOVERNANCE_VALIDATION_COMMANDS
        ):
            warnings.append(
                f"{skill_path.relative_to(REPO_ROOT)}: Validation command section "
                "does not reference a governance/test command"
            )

        warnings.extend(scan_text_for_risks(content, str(skill_path.relative_to(REPO_ROOT))))

    return errors, warnings


def scan_instruction_files() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    required_files = [
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "CLAUDE.md",
        REPO_ROOT / ".github" / "copilot-instructions.md",
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f"Missing required instruction file: {path.relative_to(REPO_ROOT)}")

    github_instructions = REPO_ROOT / ".github" / "instructions"
    expected_instruction_files = [
        "python.instructions.md",
        "docs.instructions.md",
        "security.instructions.md",
        "tests.instructions.md",
    ]
    for filename in expected_instruction_files:
        path = github_instructions / filename
        if not path.exists():
            errors.append(f"Missing GitHub instruction file: {path.relative_to(REPO_ROOT)}")

    subagent_errors, subagent_warnings = validate_claude_subagents()
    skill_errors, skill_warnings = validate_skills()

    errors.extend(subagent_errors)
    errors.extend(skill_errors)
    warnings.extend(subagent_warnings)
    warnings.extend(skill_warnings)

    scanned_paths = {
        *(p.resolve() for p in (REPO_ROOT / ".claude" / "agents").glob("*.md")),
        *(p.resolve() for p in (REPO_ROOT / ".agents" / "skills").glob("*/SKILL.md")),
    }
    for path in REPO_ROOT.rglob("*.md"):
        if ".git" in path.parts or path.resolve() in scanned_paths:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        warnings.extend(scan_text_for_risks(text, str(path.relative_to(REPO_ROOT))))

    return errors, list(dict.fromkeys(warnings))


def main() -> int:
    errors, warnings = scan_instruction_files()
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Instruction file scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
