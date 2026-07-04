# Documentation instructions

Apply when editing `docs/`, `README.md`, and instruction markdown files.

## Style

- Clear headings, short paragraphs, actionable command blocks.
- Use PowerShell examples on Windows (`AGENTS.md` quickstart).
- Cross-link related docs and policy files.

## Required messaging

Every top-level doc should reinforce:

> This repository does not simulate an agent. It prepares the repository so real coding agents can work safely and consistently.

## Do not

- Document fake runtime setup or API key configuration.
- Add broken command examples; verify against `pyproject.toml` and scripts.

## Validation

After structural doc changes, run:

```powershell
python scripts/scan_instruction_files.py
```
