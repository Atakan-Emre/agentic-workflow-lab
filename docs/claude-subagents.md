# Claude subagents

Claude Code subagents live in `.claude/agents/*.md` with YAML frontmatter.

## Frontmatter contract

Required keys:

- `name`
- `description`
- `tools` (list)

## Body sections

Each subagent must include:

- Role
- Responsibilities
- Allowed actions
- Forbidden actions
- Quality checklist
- Handoff rules

Validated by `scripts/scan_instruction_files.py`.

## Included subagents

| File | Purpose |
| --- | --- |
| `planner.md` | Implementation planning |
| `security-reviewer.md` | Security and policy review |
| `validator.md` | Run governance validation |
| `docs-writer.md` | Documentation maintenance |
| `repo-reviewer.md` | Repo structure / governance review |

## When to use subagents

Use for parallel review, multi-file governance checks, or security validation. Avoid subagents for trivial single-file edits.

## Mapping to manifests

Subagents are Claude-specific views of roles also described in `agents/manifests/`. Keep handoff targets and forbidden actions aligned with manifest contracts.
