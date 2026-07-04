# CLAUDE.md

Claude Code operating guide for **agentic-workflow-lab**.

## Read first

1. `AGENTS.md` — shared contract for all agents.
2. `policies/security-policy.yaml` — non-negotiable security constraints.
3. `policies/tool-policy.yaml` — tool allow/deny/approval matrix.

## Working style

- Prefer reading manifests and policies before editing.
- Keep diffs minimal and focused.
- Run `python scripts/validate_agentic_repo.py` before finishing substantive changes.
- Do not create fake LLM providers or simulated runtimes.

## When to use subagents

| Situation | Subagent |
| --- | --- |
| Multi-step feature planning | `planner` |
| Security-sensitive changes | `security-reviewer` |
| Pre-PR validation | `validator` |
| Documentation updates | `docs-writer` |
| Repo structure / governance review | `repo-reviewer` |

Use subagents for parallelizable review work. Do not spawn subagents for trivial one-file edits.

## Files requiring extra care

| Path | Why |
| --- | --- |
| `policies/` | Changes affect all agents |
| `schemas/` | Contract breakage impacts validation |
| `agents/manifests/` | Defines agent capabilities |
| `scripts/validate_*.py` | Governance enforcement |
| `.github/instructions/security.instructions.md` | Security guidance |
| `mcp/server.py` | Must remain read-only in v1 |

## Tool safety

- Treat read-only inspection as default.
- Any write, shell, commit, or push requires explicit user approval when policy demands it.
- Never run remote piped scripts.
- Never expose or commit secrets.

## Shell command rules

Allowed without escalation when validating this repo:

```powershell
pip install -e ".[dev]"
python scripts/validate_agentic_repo.py
pytest -q
git status
git diff
```

Requires justification and often approval:

- Network installs outside the project venv.
- Git write operations (`commit`, `push`).
- Commands touching paths outside the repository root.

Forbidden:

- `git push --force`
- `git reset --hard`
- `curl ... | bash` / `wget ... | sh`
- `Invoke-Expression` on remote content

## Handoff format

When handing off to another subagent or manifest role, include:

1. Goal and scope
2. Files touched or to inspect
3. Validation commands run and results
4. Open risks or approval needs

## Quality bar

A task is not done until validation passes and policy constraints are documented in the PR or handoff note.
