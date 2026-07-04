---
name: create-agent-manifest
description: Create a new framework-independent agent manifest under agents/manifests/.
---

## When to use

Use when adding a new agent role that real coding agents should follow, independent of Claude, Copilot, Codex, or Cursor specifics.

## Steps

1. Read `schemas/agent-manifest.schema.json` and an existing manifest as a template.
2. Choose a kebab-case `name` ending in `-agent` unless a shorter role name is already established.
3. Define `allowed_tools`, `blocked_tools`, contracts, handoffs, approval triggers, and `quality_gates`.
4. Ensure no tool appears in both allowed and blocked lists.
5. Add documentation references in `docs/agents-md.md` or `README.md` if the role is user-facing.
6. Run validation.

## Expected files

- `agents/manifests/<name>.yaml`
- Optional updates to `docs/architecture.md`

## Validation command

```powershell
python scripts/validate_agent_manifests.py
python scripts/validate_agentic_repo.py
```

## Anti-patterns

- Embedding LLM prompts inside manifests instead of contracts.
- Granting write tools without `approval_required_when` entries.
- Duplicating policy rules that belong in `policies/tool-policy.yaml`.
