---
name: run-governance-check
description: Run the full agentic repository governance validation suite.
---

## When to use

Use before PR submission, after changing policies/manifests/instructions, or when verifying agent-ready status.

## Steps

1. Ensure dev dependencies are installed: `pip install -e ".[dev]"`.
2. Run `python scripts/validate_agentic_repo.py`.
3. Run `pytest -q`.
4. Review warnings for risky keywords or forbidden command patterns.
5. Record pass/fail summary in PR or handoff note.

## Expected files

- No file changes required when passing.
- Remediation targets listed in validator output on failure.

## Validation command

```powershell
python scripts/validate_agentic_repo.py
pytest -q
agentic-lab-validate
```

## Anti-patterns

- Skipping validation because edits "look small".
- Treating warnings as pass when they indicate secrets or forbidden commands in tracked files.
- Running destructive git commands to "fix" validation failures.
