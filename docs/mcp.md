# MCP-style tool layer

The `mcp/` directory demonstrates a **read-only**, **local** tool surface for coding agents.

## Important

This is a **demo**, not a production MCP server. It does not:

- Implement full MCP wire protocol
- Perform writes or external API calls
- Host or simulate an LLM/agent runtime

## Tools

| Tool | Description |
| --- | --- |
| `read_project_file` | Read a file under repository root |
| `list_agent_manifests` | List YAML files in `agents/manifests/` |
| `read_policy` | Read a policy from `policies/` |

## CLI usage

```powershell
python mcp/server.py list_agent_manifests
python mcp/server.py read_project_file --path AGENTS.md
python mcp/server.py read_policy --name security-policy
```

## Policy alignment

`policies/tool-policy.yaml` allows read-only inspection tools by default and requires approval for write-capable tools.

## Production evolution

A production server would add authentication, audit logging, schema-validated tool inputs, and approval enforcement at dispatch time.

See [mcp/README.md](../mcp/README.md).
