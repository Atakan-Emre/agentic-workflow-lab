# Copilot instructions

GitHub Copilot consumes repository instructions from `.github/copilot-instructions.md` and path-specific files under `.github/instructions/`.

## Files

- `.github/copilot-instructions.md` — repo-wide standards, build/test commands, review expectations
- `.github/instructions/python.instructions.md` — Python modules
- `.github/instructions/docs.instructions.md` — documentation
- `.github/instructions/security.instructions.md` — security-sensitive edits
- `.github/instructions/tests.instructions.md` — pytest and validation tests

## Design goals

- Steer Copilot away from fake LLM runtime: runtime code
- Enforce validation before merge
- Keep code and docs aligned with policies and schemas

## Validation

```powershell
python scripts/scan_instruction_files.py
```

Ensures required instruction files exist and Claude/skills structure remains valid (shared scan).

## Tips

- Prefer linking to `AGENTS.md` instead of duplicating long policy text.
- Use path-scoped instruction files for detail; keep root Copilot file concise.
