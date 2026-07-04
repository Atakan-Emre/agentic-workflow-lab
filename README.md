# Agentic Workflow Lab

A governance-first reference repository for making software projects ready for real AI coding agents such as Codex, GitHub Copilot, Claude Code, and Cursor.

It demonstrates how to combine `AGENTS.md`, Copilot instructions, Claude subagents, Codex skills, agent manifests, tool policies, validation scripts, CI checks, and MCP-style read-only tooling into a structured agent-ready workspace.

> **This repository does not simulate an agent.**
> **It prepares the repository so real coding agents can work safely and consistently.**

---

## What is this?

Agentic Workflow Lab is a **governance-first reference repo** for agent-ready software projects.

It shows how to prepare a codebase so real coding agents can operate with shared instructions, explicit contracts, enforceable policies, safety boundaries, and automated validation.

Agentic AI is not prompt engineering alone. Sustainable agentic development requires repo-level structure: instructions, capabilities, policies, contracts, validation, and observability.

---

## Why this repo exists

Real coding agents need more than prompts.

They need:

* Shared instructions through `AGENTS.md`, Copilot instructions, and Claude-specific guidance
* Reusable capabilities such as subagents, skills, and agent manifests
* Policy and approval gates for tool usage, security, shell execution, and external writes
* Machine-checkable schemas and validation scripts
* Automated tests and CI enforcement
* Optional read-only tool surfaces for safe project inspection

This repository encodes those layers as copyable patterns.

---

## What this repo is not

* Not a fake LLM provider or simulated agent runtime
* Not an OpenAI, Anthropic, or local LLM API integration sample
* Not a production MCP server
* Not a system that performs external writes without explicit approval policies
* Not a replacement for security review, code review, or production governance

---

## Design principles

This repository follows a few core principles:

* **Real agents, not simulated agents** — the repo is designed for actual coding agents and IDE assistants.
* **Instructions as contracts** — agent behavior should be guided by explicit repo-level instructions.
* **Policies before tools** — tool usage must be constrained by security and approval policies.
* **Validation is mandatory** — governance rules should be machine-checkable.
* **Read-only by default** — inspection is safe by default; write-capable actions require approval.
* **Portable patterns** — the structure should be reusable across different projects and agent ecosystems.
* **CI-enforced governance** — validation should run locally and in pull requests.
* **Security-first agent readiness** — external writes, shell execution, and destructive actions must be explicitly controlled.

---

## Supported coding-agent ecosystems

| Ecosystem          | Entry points in this repo                                                   |
| ------------------ | --------------------------------------------------------------------------- |
| **Codex**          | `AGENTS.md`, `.agents/skills/*/SKILL.md`, `agents/manifests/`               |
| **GitHub Copilot** | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` |
| **Claude Code**    | `CLAUDE.md`, `.claude/agents/*.md`                                          |
| **Cursor**         | `.cursor/rules/`, `AGENTS.md`, policies, validation scripts                 |

---

## How real coding agents use this repository

This repository is designed to be consumed by real AI coding agents and IDE assistants.

* **Codex** reads `AGENTS.md` and reusable skills under `.agents/skills/`.
* **GitHub Copilot** uses `.github/copilot-instructions.md` and path-specific instructions under `.github/instructions/`.
* **Claude Code** uses `CLAUDE.md` and specialized subagents under `.claude/agents/`.
* **Cursor** can use project rules under `.cursor/rules/` for local IDE guidance.

The repository does not provide a fake LLM runtime. Instead, it defines the instruction, policy, schema, validation, and safety layers that make real coding agents more consistent and governable.

---

## Architecture

```text
Instruction layer  -> AGENTS.md, CLAUDE.md, Copilot instructions, Cursor rules
Capability layer   -> Claude subagents, Codex skills, agent manifests
Policy layer       -> tool, approval, security policies + JSON schemas
Validation layer   -> Python validation scripts + pytest + CI
Tool layer (demo)  -> MCP-style read-only local inspection
```

See [docs/architecture.md](docs/architecture.md) for details.

---

## Instruction layer

The instruction layer defines how coding agents should understand and modify this repository.

* [`AGENTS.md`](AGENTS.md) — shared contract for all coding agents
* [`CLAUDE.md`](CLAUDE.md) — Claude Code-specific rules
* [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — Copilot repo-wide guidance
* [`.github/instructions/`](.github/instructions/) — path-scoped Copilot instruction files
* [`.cursor/rules/`](.cursor/rules/) — Cursor project rules

---

## Capability layer

The capability layer describes reusable agent behaviors and responsibilities.

* [`agents/manifests/`](agents/manifests/) — framework-independent agent manifests
* [`.claude/agents/`](.claude/agents/) — Claude Code subagents
* [`.agents/skills/`](.agents/skills/) — Codex skills

These files help real coding agents understand:

* What role an agent or skill is responsible for
* Which actions are allowed or forbidden
* Which contracts and policies must be respected
* Which validation checks should run after changes

---

## Policy & contract layer

The policy and contract layer makes agent behavior machine-checkable.

* [`policies/`](policies/) — YAML policies for tools, approval gates, and security
* [`schemas/`](schemas/) — JSON Schema contracts for manifests, policies, validation results, and approval gates

This layer is intentionally explicit. Agentic development should not rely only on natural language instructions; it should include structured policy and validation artifacts.

---

## Validation layer

The validation layer enforces the repository governance model.

* [`scripts/`](scripts/) — governance validation scripts
* [`tests/`](tests/) — pytest coverage for policies, instructions, manifests, and validators
* [`.github/workflows/ci.yml`](.github/workflows/ci.yml) — CI enforcement on pull requests and pushes to `main`

Validation runs both locally and in CI.

---

## MCP-style tool layer

[`mcp/`](mcp/) demonstrates read-only local inspection tools:

* `read_project_file`
* `list_agent_manifests`
* `read_policy`

The MCP-style layer is intentionally read-only and local-first. It demonstrates safe inspection patterns, not production tool execution.

See [mcp/README.md](mcp/README.md).

---

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

---

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

Expected result:

```text
PASSED
13 passed
```

---

## MCP demo commands

```powershell
python mcp/server.py list_agent_manifests
python mcp/server.py read_project_file --path AGENTS.md
python mcp/server.py read_policy --name tool-policy
```

---

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
├── .cursor/
│   └── rules/
├── .claude/
│   └── agents/
├── .agents/
│   └── skills/
├── agents/
│   └── manifests/
├── policies/
├── schemas/
├── scripts/
├── mcp/
├── docs/
└── tests/
```

---

## Security model

The repository uses a security-first agent-readiness model:

* Read-only tools are allowed by default
* Write-capable tools require approval
* Destructive actions are forbidden
* External writes are denied unless approval policy allows them
* Shell execution must be justified
* Remote script execution is forbidden
* Secrets must never be printed or committed
* MCP demo tools remain read-only
* CI runs validation and tests on pull requests and pushes to `main`

Details: [docs/security.md](docs/security.md)

---

## Governance model

This repository treats agentic development as a governed software workflow.

The core governance loop is:

```text
Instruction
  ↓
Capability
  ↓
Policy
  ↓
Validation
  ↓
CI enforcement
  ↓
Safe agent-assisted development
```

The goal is not to restrict agent productivity. The goal is to make agent-assisted development safer, more consistent, and easier to review.

---

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

Planned directions include:

* Expanded validation coverage
* More portable agent manifest examples
* Additional Cursor rule templates
* MCP-style read-only inspection improvements
* Scenario-based governance examples
* Optional approval workflow examples
* Agent-readiness checklist templates

---

## License

MIT — use as a template for your own agent-ready repositories.
