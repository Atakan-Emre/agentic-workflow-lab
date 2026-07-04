# Architecture

Agentic Workflow Lab organizes agent governance into explicit layers so real coding agents can operate consistently without embedding runtime logic in the repository.

## Design principle

**Prepare the repo; do not simulate the agent.**

The repository supplies instructions, contracts, policies, validation, and optional read-only tools. The agent runtime lives in Codex, Copilot, Claude Code, or Cursor.

## Layers

### 1. Instruction layer

Human- and agent-readable rules:

- `AGENTS.md` — universal contract
- `CLAUDE.md` — Claude-specific execution guidance
- `.github/copilot-instructions.md` and `.github/instructions/` — Copilot path rules

### 2. Capability layer

Role definitions and reusable workflows:

- `agents/manifests/*.yaml` — framework-independent manifests
- `.claude/agents/*.md` — Claude subagents
- `.agents/skills/*/SKILL.md` — Codex skills

Manifests express **contracts** (tools, handoffs, approvals). Skills and subagents express **how** an ecosystem should apply those contracts.

### 3. Policy and contract layer

Machine-readable constraints:

- `policies/tool-policy.yaml`
- `policies/approval-policy.yaml`
- `policies/security-policy.yaml`
- `schemas/*.json`

Schemas make governance evolvable: add a field, update validators, extend tests.

### 4. Validation layer

Enforcement via Python scripts and pytest:

- Schema validation for manifests and policies
- Instruction structure checks
- Risky keyword / forbidden command warnings
- Top-level `validate_agentic_repo.py` orchestration

### 5. MCP-style tool layer (demo)

`mcp/` exposes read-only local inspection. It illustrates how tool dispatch can be constrained without granting write or network access.

## Data flow

```text
User request
    -> intake-agent manifest
    -> context-agent (read files/policies)
    -> planner-agent (plan + validation steps)
    -> tool-agent (approved writes/commands)
    -> verifier-agent (scripts + pytest)
    -> security-agent (policy review)
    -> supervisor-agent (routing/approvals)
```

## Boundaries

| Concern | Belongs in | Does not belong in |
| --- | --- | --- |
| Tool allow/deny | `policies/tool-policy.yaml` | Ad hoc prompt text |
| Agent role contracts | `agents/manifests/` | Python business logic |
| Claude behavior | `.claude/agents/` | Manifest YAML |
| Enforcement | `scripts/`, `tests/` | README only |

## Extension guidelines

When adding a new agent capability:

1. Update or add a manifest.
2. Mirror ecosystem-specific guidance (Claude subagent / Codex skill).
3. Adjust policies if tools change.
4. Extend validators and tests.
5. Document in README and relevant doc page.
