"""Demo read-only MCP-style server for agentic-workflow-lab.

This is NOT a production MCP server. It demonstrates how a read-only tool
layer can expose local repository inspection to coding agents without granting
write or external network capabilities.
"""

from __future__ import annotations

import argparse
import json
from typing import Any, Callable

from mcp.tools.read_project_file import list_agent_manifests, read_policy, read_project_file

ToolHandler = Callable[..., dict[str, Any]]

TOOLS: dict[str, ToolHandler] = {
    "read_project_file": lambda args: read_project_file(args["path"]),
    "list_agent_manifests": lambda _args: list_agent_manifests(),
    "read_policy": lambda args: read_policy(args["name"]),
}


def dispatch(tool: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
    if tool not in TOOLS:
        raise KeyError(f"Unknown tool: {tool}")
    return TOOLS[tool](arguments or {})


def main() -> int:
    parser = argparse.ArgumentParser(description="Demo read-only MCP-style tool dispatcher")
    parser.add_argument("tool", choices=sorted(TOOLS))
    parser.add_argument("--path", help="Relative path for read_project_file")
    parser.add_argument("--name", help="Policy name for read_policy")
    args = parser.parse_args()

    payload: dict[str, Any] = {}
    if args.path:
        payload["path"] = args.path
    if args.name:
        payload["name"] = args.name

    result = dispatch(args.tool, payload)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
