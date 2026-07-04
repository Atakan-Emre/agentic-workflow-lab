"""Read-only MCP-style tools for local project inspection (demo)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _resolve_safe(relative_path: str) -> Path:
    root = REPO_ROOT.resolve()
    candidate = (root / relative_path).resolve()

    if not candidate.is_relative_to(root):
        raise ValueError("Path escapes repository root")

    if not candidate.exists():
        raise FileNotFoundError(relative_path)

    return candidate


def read_project_file(relative_path: str, max_bytes: int = 100_000) -> dict:
    path = _resolve_safe(relative_path)
    if path.is_dir():
        raise IsADirectoryError(relative_path)

    data = path.read_bytes()[:max_bytes]
    return {
        "path": relative_path,
        "size": path.stat().st_size,
        "truncated": path.stat().st_size > max_bytes,
        "content": data.decode("utf-8", errors="replace"),
    }


def list_agent_manifests() -> dict:
    manifests_dir = REPO_ROOT / "agents" / "manifests"
    files = sorted(p.name for p in manifests_dir.glob("*.yaml"))
    return {"count": len(files), "manifests": files}


def read_policy(policy_name: str) -> dict:
    if not policy_name.endswith(".yaml"):
        policy_name = f"{policy_name}.yaml"
    path = _resolve_safe(str(Path("policies") / policy_name))
    return {
        "policy": policy_name,
        "content": path.read_text(encoding="utf-8"),
    }
