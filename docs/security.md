# Security model

Security in Agentic Workflow Lab is enforced through policies, validation, and agent instructions—not through a simulated runtime.

## Policies

| File | Focus |
| --- | --- |
| `policies/security-policy.yaml` | Secrets, shell, external access, agent constraints |
| `policies/tool-policy.yaml` | Tool allow/deny/approval matrix |
| `policies/approval-policy.yaml` | Human-in-the-loop gates |

## Core rules

1. **Read-only by default** for tools and external access.
2. **Writes require approval** unless explicitly documented otherwise.
3. **Destructive commands forbidden** (force push, hard reset, `rm -rf /`, remote pipe execution).
4. **Secrets never committed or printed**.
5. **No fake LLM / external API integration** in this reference repo.

## Shell execution

Shell commands must be justified. Validation commands (`pytest`, `validate_agentic_repo.py`) are allowlisted examples in `CLAUDE.md` and `security-policy.yaml`.

## Agent constraints

Agents must not:

- Exfiltrate repo contents to unapproved endpoints
- Disable validation or hooks
- Store API keys in tracked files

## Validation

```powershell
python scripts/validate_tool_policy.py
python scripts/check_approval_gates.py
python scripts/validate_agentic_repo.py
```

Scanners emit **warnings** for risky keywords and forbidden command patterns in tracked instruction files.

## Incident response

On suspected secret exposure: stop work, rotate credentials out of band, and document remediation without committing secret material.
