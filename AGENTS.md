# AGENTS.md

Shared operating contract for AI coding agents working in **agentic-workflow-lab**.

> **This repository does not simulate an agent.**  
> It prepares the repository so real coding agents can work safely and consistently.

## Project purpose

This is a reference repository demonstrating repo-level agentic governance: instructions, manifests, policies, validation, and read-only tool layers. Do not add fake LLM providers, simulated agent runtimes, or external API integrations.

## Cursor Cloud Agents

This repository is a **local governance template**. Do **not** connect it to Cursor Cloud Agents environment setup, and do **not** trigger `@cursor` on GitHub issues or PRs by default. Contributors should use their own local IDE agents; this repo only supplies instructions and policies.

## Setup commands

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Test commands

```powershell
python scripts/validate_agentic_repo.py
pytest -q
agentic-lab-validate
```

## Architecture boundaries

| Layer | Location | Responsibility |
| --- | --- | --- |
| Instruction | `AGENTS.md`, `CLAUDE.md`, `.github/`, `.cursor/rules/` | Agent behavior and standards |
| Capability | `.claude/agents/`, `.agents/skills/` | Subagents and skills |
| Contract | `agents/manifests/`, `schemas/` | Agent roles and schemas |
| Policy | `policies/` | Tool, approval, and security rules |
| Validation | `scripts/`, `tests/` | Automated governance checks |
| Tool demo | `mcp/` | Read-only local inspection (not production MCP) |

Do not collapse these layers. Policies belong in `policies/`, not embedded ad hoc in scripts.

## Security rules

- Never commit secrets, tokens, keys, or `.env` files.
- Never print secrets in logs, diffs, or command output.
- Remote script execution (`curl | bash`, `wget | sh`, `iex`) is forbidden.
- Destructive git operations (`push --force`, `reset --hard`) are forbidden.
- External writes require explicit human approval per `policies/approval-policy.yaml`.

## Allowed actions

- Read repository files and policies.
- Run validation scripts and pytest.
- Edit source, docs, policies, manifests, and tests when tasked.
- Use read-only MCP demo tools under `mcp/`.
- Create or update agent manifests, skills, and instruction files following schemas.

## Forbidden actions

- Adding FakeLLMProvider or simulated agent runtime code.
- Integrating real LLM APIs or requesting API keys in repo files.
- Calling external APIs that mutate remote state without approval.
- Disabling validation, hooks, or policy checks.
- Force push, hard reset, or deleting unrelated user data.

## External write policy

External writes are **denied by default**. Allowed only when:

1. `policies/approval-policy.yaml` gate is satisfied, and
2. `policies/tool-policy.yaml` explicitly permits the tool/action, and
3. A human approver is recorded in the workflow log.

## Validation requirements

Before opening or merging a PR:

1. `python scripts/validate_agentic_repo.py` must pass.
2. `pytest -q` must pass.
3. CI workflow (`.github/workflows/ci.yml`) must pass on GitHub.
4. Changed manifests must validate against `schemas/agent-manifest.schema.json`.
5. Changed policies must validate against their schemas.
6. Instruction files must retain required sections and frontmatter.

## PR checklist

- [ ] Scope matches request; no unrelated refactors.
- [ ] Validation scripts pass locally.
- [ ] Tests added or updated for behavioral changes.
- [ ] Policies and manifests updated when agent capabilities change.
- [ ] No secrets, tokens, or credentials in diff.
- [ ] README or docs updated when structure or commands change.
- [ ] Security-sensitive edits reviewed against `policies/security-policy.yaml`.

## Agent routing hints

- Planning and decomposition → `planner-agent` manifest / `.claude/agents/planner.md`
- Security review → `security-agent` / `.claude/agents/security-reviewer.md`
- Validation → `verifier-agent` / `.claude/agents/validator.md`
- Docs → `.claude/agents/docs-writer.md`
- Repo structure review → `.claude/agents/repo-reviewer.md`

## Observability

Record handoffs, approvals, and validation results in PR descriptions or workflow notes. Prefer machine-checkable outputs aligned with `schemas/validation-result.schema.json`.
