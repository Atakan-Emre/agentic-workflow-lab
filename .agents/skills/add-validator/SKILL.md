---
name: add-validator
description: Add or extend Python validation scripts and pytest coverage for governance checks.
---

## When to use

Use when introducing a new repo rule that should be machine-enforced (manifest field, policy constraint, instruction section).

## Steps

1. Identify the rule and whether it is an error or warning.
2. Add reusable logic to `scripts/_utils.py` if shared.
3. Implement or extend a focused script under `scripts/`.
4. Wire the check into `scripts/validate_agentic_repo.py`.
5. Add pytest coverage under `tests/`.
6. Document the rule in `docs/validation.md`.

## Expected files

- `scripts/<validator>.py`
- `tests/test_validation_scripts.py` or focused test module
- Optional `docs/validation.md` update

## Validation command

```powershell
pytest tests/test_validation_scripts.py -q
python scripts/validate_agentic_repo.py
```

## Anti-patterns

- One-off shell grep instructions without a script.
- Validators that mutate the repository.
- Network calls inside validation logic.
