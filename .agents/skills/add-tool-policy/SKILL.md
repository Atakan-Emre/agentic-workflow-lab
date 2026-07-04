---
name: add-tool-policy
description: Extend tool-policy.yaml and schemas with new allow, deny, or approval rules.
---

## When to use

Use when a coding agent gains access to a new tool class (write, shell, external API) and the repository must express governance explicitly.

## Steps

1. Read `policies/tool-policy.yaml` and `schemas/tool-policy.schema.json`.
2. Decide effect: `allow`, `deny`, or `require_approval`.
3. Add rule with stable `id`, description, tools, and conditions.
4. Update `approval_required_tools` when writes are involved.
5. Mirror critical constraints in `policies/security-policy.yaml` if needed.
6. Extend `tests/test_tool_policy.py` for new rules.

## Expected files

- `policies/tool-policy.yaml`
- Optional `policies/approval-policy.yaml`
- `tests/test_tool_policy.py`

## Validation command

```powershell
python scripts/validate_tool_policy.py
python scripts/check_approval_gates.py
python scripts/validate_agentic_repo.py
```

## Anti-patterns

- Allow-by-default for write-capable tools.
- Policy rules without schema validation.
- Duplicating the same tool in conflicting effects without documented precedence.
