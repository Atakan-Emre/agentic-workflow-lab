# Test instructions

Apply when editing `tests/` or validation behavior in `scripts/`.

## Framework

- Use `pytest`.
- Tests must run offline with no external services.
- Prefer testing validators against the real repo fixtures.

## Coverage expectations

When changing:

    logic, update tests for:

- manifest schema validation
- tool policy approval rules
- instruction file structure
- approval gate schema compliance
- top-level `validate_agentic_repo.py` integration

## Commands

```powershell
pytest -q
pytest tests/test_validation_scripts.py -q
```

## Do not

- Mock LLM responses.
- Require API keys or network access in tests.
