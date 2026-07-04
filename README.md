# Agentic Workflow Lab

A reference repository for building AI-coding-agent-ready software projects with AGENTS.md, Copilot instructions, Claude subagents, Codex skills, tool policies, validation scripts and MCP-style tool integration.

> **This repository does not simulate an agent.**  
> **It prepares the repository so real coding agents can work safely and consistently.**

## What is this?

Agentic Workflow Lab is a **governance-first reference repo**. It shows how to prepare a codebase so Codex, GitHub Copilot, Claude Code, and Cursor can operate with shared instructions, explicit contracts, enforceable policies, and automated validation.

Agentic AI is not prompt engineering alone. Sustainable agentic development requires repo-level structure.

## Why this repo exists

Real coding agents need:

- Shared instructions (`AGENTS.md`, Copilot, Claude-specific guides)
- Capability definitions (subagents, skills, manifests)
- Policy and approval gates (tool, security, external write rules)
- Validation scripts and tests (machine-enforceable governance)
- Optional read-only tool surfaces (MCP-style inspection)

This repository encodes those layers as copyable patterns.

## What this repo is not

- Not a fake LLM provider or simulated agent runtime
- Not an OpenAI/Anthropic API integration sample
- Not a production MCP server
- Not a system that performs external writes by default

## Supported agent ecosystems

| Ecosystem | Entry points in this repo |
| --- | --- |
| **Codex** | `.agents/skills/*/SKILL.md`, `agents/manifests/`, `AGENTS.md` |
| **GitHub Copilot** | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` |
| **Claude Code** | `CLAUDE.md`, `.claude/agents/*.md` |
| **Cursor** | `AGENTS.md`, optional `.cursor/rules/` (local IDE), policies, validation scripts |

## How real coding agents use this repository

This repository is designed to be consumed by real AI coding agents and IDE assistants.

- **Codex** reads `AGENTS.md` and reusable skills under `.agents/skills/`.
- **GitHub Copilot** uses `.github/copilot-instructions.md` and path-specific instructions under `.github/instructions/`.
- **Claude Code** uses `CLAUDE.md` and specialized subagents under `.claude/agents/`.
- **Cursor** can use optional project rules under `.cursor/rules/` (local IDE only; not Cloud Agents)

The repository does not provide a fake LLM runtime. Instead, it defines the instruction, policy, schema, validation and safety layers that make real coding agents more consistent and governable.

## Architecture

```text
Instruction layer  -> AGENTS.md, CLAUDE.md, Copilot instructions
Capability layer   -> Claude subagents, Codex skills, agent manifests
Policy layer       -> tool, approval, security policies + JSON schemas
Validation layer   -> Python scripts + pytest
Tool layer (demo)  -> mcp/ read-only local inspection
```

See [docs/architecture.md](docs/architecture.md) for details.

## Instruction layer

- [`AGENTS.md`](AGENTS.md) — shared contract for all agents
- [`CLAUDE.md`](CLAUDE.md) — Claude Code-specific rules
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — Copilot repo-wide guidance
- [`.github/instructions/`](.github/instructions/) — path-scoped instruction files

## Capability layer

- [`agents/manifests/`](agents/manifests/) — framework-independent agent manifests
- [`.claude/agents/`](.claude/agents/) — Claude Code subagents
- [`.agents/skills/`](.agents/skills/) — Codex skills

## Policy & contract layer

- [`policies/`](policies/) — YAML policies
- [`schemas/`](schemas/) — JSON Schema contracts

## Validation layer

- [`scripts/`](scripts/) — governance validators
- [`tests/`](tests/) — pytest coverage
- [`.github/workflows/ci.yml`](.github/workflows/ci.yml) — CI enforcement on PRs and pushes to `main`

## MCP-style tool layer

[`mcp/`](mcp/) demonstrates read-only local tools (`read_project_file`, `list_agent_manifests`, `read_policy`). See [mcp/README.md](mcp/README.md).

## Quickstart

```powershell
git clone <your-fork-url> agentic-workflow-lab
cd agentic-workflow-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python scripts/validate_agentic_repo.py
pytest -q
```

## Validation commands

```powershell
python scripts/validate_agentic_repo.py
python scripts/validate_agent_manifests.py
python scripts/validate_tool_policy.py
python scripts/scan_instruction_files.py
python scripts/check_approval_gates.py
agentic-lab-validate
pytest -q
```

## Folder structure

```text
agentic-workflow-lab/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── pyproject.toml
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   └── workflows/
│       └── ci.yml
├── .cursor/rules/
├── .claude/agents/
├── .agents/skills/
├── agents/manifests/
├── policies/
├── schemas/
├── scripts/
├── mcp/
├── docs/
└── tests/
```

## Security model

- Read-only tools allowed by default (`policies/tool-policy.yaml`)
- Write-capable tools require approval
- Destructive actions forbidden
- External writes denied unless approval policy allows
- Shell execution must be justified
- Secrets must never be printed or committed

Details: [docs/security.md](docs/security.md)

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## License

MIT — use as a template for your own agent-ready repositories.
