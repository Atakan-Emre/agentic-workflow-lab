# AGENTS.md guide

`AGENTS.md` is the shared operating contract for all coding agents in a repository.

## Purpose

- Single entry point for setup, test, and validation commands
- Architecture boundaries and security rules
- Allowed/forbidden actions and external write policy
- PR checklist and routing hints

## Why root-level

Codex, Cursor, Copilot, and Claude-compatible tools increasingly look for repo-root agent instructions. Keeping shared rules in `AGENTS.md` avoids ecosystem-specific drift.

## Relationship to other files

| File | Scope |
| --- | --- |
| `AGENTS.md` | All agents |
| `CLAUDE.md` | Claude Code specifics |
| `.github/copilot-instructions.md` | Copilot specifics |
| `agents/manifests/` | Structured role contracts |

## Maintenance

Update `AGENTS.md` when:

- Validation commands change
- Folder structure changes
- Security or approval rules change
- New agent roles are introduced

Run `python scripts/scan_instruction_files.py` after edits.

## Template message

Include clearly:

> This repository does not simulate an agent. It prepares the repository so real coding agents can work safely and consistently.
