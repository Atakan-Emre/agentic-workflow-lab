# Roadmap

Planned evolution for Agentic Workflow Lab as a reference template.

## v0.1 (current)

- [x] Instruction layer (`AGENTS.md`, Claude, Copilot, Cursor rules)
- [x] Claude subagents and Codex skills
- [x] Framework-independent manifests
- [x] JSON Schemas and YAML policies
- [x] Python validators and pytest suite
- [x] Read-only MCP-style demo tools
- [x] GitHub Actions CI (validate + pytest on PR/push to main)

## v0.2

- [ ] Example `validation-result.json` emitter from scripts
- [ ] Policy precedence documentation and tests
- [ ] Contract tests between manifests and subagents/skills

## v0.3

- [ ] Production-oriented MCP server sketch (stdio, auth, audit log)
- [ ] Approval gate integration examples (PR labels / CODEOWNERS mapping)
- [ ] Observability hooks (structured JSON logs from validators)

## v0.4

- [ ] Multi-repo policy pack sharing pattern
- [ ] Contract tests between manifests and subagents/skills
- [ ] Sample consumer repo showing copy-and-adapt workflow

## Non-goals

- Fake LLM providers or agent simulators
- Storing or requesting real vendor API keys
- External write demos without approval gates
