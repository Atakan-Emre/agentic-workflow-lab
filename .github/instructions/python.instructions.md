# Python instructions

Apply when editing `*.py` files, especially under `scripts/`, `mcp/`, and `tests/`.

## Conventions

- Use `from __future__ import annotations` in new modules.
- Return structured `(errors, warnings)` tuples from validators.
- Exit non-zero from CLI `main()` on validation failure.
- Keep repo root resolution in `scripts/_utils.py`.

## Dependencies

Runtime: `pyyaml`, `jsonschema`. Dev: `pytest`, optional `ruff`.

## Do not

- Add LLM SDK dependencies.
- Add network calls in validation scripts.
- Write files from MCP demo tools (read-only v1).

## Required checks after edits

```powershell
python scripts/validate_agentic_repo.py
pytest -q
```
