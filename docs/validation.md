# Validation

Automated validation ensures the repository remains agent-ready and policy-compliant.

## Entry points

| Command | Purpose |
| --- | --- |
| `python scripts/validate_agentic_repo.py` | Full governance check |
| `python scripts/validate_agent_manifests.py` | Manifest schema validation |
| `python scripts/validate_tool_policy.py` | Tool policy rules |
| `python scripts/scan_instruction_files.py` | Instruction/subagent/skill structure |
| `python scripts/check_approval_gates.py` | Approval gate schemas |
| `agentic-lab-validate` | CLI alias (pyproject entry point) |
| `pytest -q` | Test suite |

## What `validate_agentic_repo.py` checks

1. Required instruction files exist (`AGENTS.md`, `CLAUDE.md`, Copilot instructions)
2. Claude subagent frontmatter and sections
3. Codex skill frontmatter and sections
4. Agent manifests match JSON Schema
5. Tool policy approval defaults and rules
6. Approval gates match JSON Schema
7. Risky keywords / forbidden command patterns (warnings)

## Schemas

- `schemas/agent-manifest.schema.json`
- `schemas/tool-policy.schema.json`
- `schemas/validation-result.schema.json`
- `schemas/approval-gate.schema.json`

## Adding new rules

Use the Codex skill `add-validator`:

1. Implement script logic
2. Wire into `validate_agentic_repo.py`
3. Add pytest coverage
4. Document here

## CI recommendation

Run at minimum:

```powershell
python scripts/validate_agentic_repo.py
pytest -q
```

on every pull request touching policies, manifests, scripts, or instructions.
