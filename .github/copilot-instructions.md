# GitHub Copilot instructions

Repository-wide guidance for GitHub Copilot in **agentic-workflow-lab**.

## Mission

Help maintain an agent-ready reference repository. Copilot suggestions must align with existing governance layers and must not introduce simulated agent runtimes or external API clients.

## Build and setup

```powershell
pip install -e ".[dev]"
```

## Validation

Always prefer these commands over ad-hoc checks:

```powershell
python scripts/validate_agentic_repo.py
pytest -q
```

## Code standards

- Python 3.10+ with type hints where helpful.
- Keep modules small; shared validation logic lives in `scripts/_utils.py`.
- YAML and JSON must match schemas in `schemas/`.
- Markdown instruction files use clear headings and actionable lists.
- Match existing naming: kebab-case for manifests, snake_case for Python.

## Review standard

Before suggesting large changes, verify:

1. Architecture boundaries in `AGENTS.md` are respected.
2. Policies remain consistent across `policies/*.yaml`.
3. Manifests remain schema-valid.
4. No secrets or destructive command examples without explicit security context.

## Do not suggest

- Fake LLM providers or mock agent orchestrators.
- Real API keys, tokens, or `.env` commits.
- External write helpers without approval gates.
- Disabling validation scripts or tests.

## Preferred patterns

- Extend manifests and policies declaratively.
- Add validation coverage in `tests/` when changing governance logic.
- Document new agent surfaces in `docs/` and root `README.md`.

## File-specific instructions

See `.github/instructions/` for path-scoped rules:

- `python.instructions.md`
- `docs.instructions.md`
- `security.instructions.md`
- `tests.instructions.md`
