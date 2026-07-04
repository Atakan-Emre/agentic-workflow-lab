# MCP-style read-only tool layer (demo)

This folder contains a **demonstration** read-only tool layer inspired by MCP (Model Context Protocol). It is **not** a production MCP server and does not connect to external systems.

## Purpose

Show how coding agents can inspect a repository through a constrained tool surface:

- Read project files
- List agent manifests
- Read policy YAML

## Design constraints (v1)

- **Read-only**: no writes, deletes, shell execution, or external API calls.
- **Local only**: operates on the repository checkout.
- **No LLM runtime**: this layer does not simulate or host agents.

## Tools

| Tool | Module | Description |
| --- | --- | --- |
| `read_project_file` | `mcp/tools/read_project_file.py` | Read a file under repo root |
| `list_agent_manifests` | `mcp/tools/list_agent_manifests.py` | List YAML manifests |
| `read_policy` | `mcp/tools/read_policy.py` | Read a file from `policies/` |

## CLI demo

```powershell
python mcp/server.py list_agent_manifests
python mcp/server.py read_project_file --path AGENTS.md
python mcp/server.py read_policy --name tool-policy
```

## Production path

A production MCP server would:

1. Implement the MCP wire protocol (stdio/SHTTP).
2. Enforce `policies/tool-policy.yaml` at dispatch time.
3. Emit structured audit logs for observability.
4. Keep write tools behind approval gates.

This demo intentionally stops at local read-only inspection.
