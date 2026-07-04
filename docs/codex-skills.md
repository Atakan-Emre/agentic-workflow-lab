# Codex skills

Codex skills live in `.agents/skills/<skill-name>/SKILL.md`.

## Frontmatter

Required:

- `name`
- `description`

## Body sections

- When to use
- Steps
- Expected files
- Validation command
- Anti-patterns

## Included skills

| Skill | Purpose |
| --- | --- |
| `create-agent-manifest` | Add framework-independent manifests |
| `add-validator` | Extend governance validators |
| `add-tool-policy` | Update tool policy rules |
| `run-governance-check` | Full validation suite |
| `write-architecture-doc` | Update architecture documentation |

## Skills vs manifests

- **Manifests** define agent roles and contracts (tools, handoffs, approvals).
- **Skills** define repeatable procedures for Codex to follow when performing repo maintenance tasks.

## Validation

```powershell
python scripts/scan_instruction_files.py
```
