# Security instructions

Apply when editing `policies/`, `schemas/`, security docs, or CI workflows.

## Non-negotiables

- Secrets must never be committed or printed.
- External writes denied unless approval policy allows.
- Destructive commands forbidden (see `policies/tool-policy.yaml`).
- MCP demo layer stays read-only in v1.

## Sensitive paths

- `policies/security-policy.yaml`
- `policies/tool-policy.yaml`
- `policies/approval-policy.yaml`
- `.github/instructions/security.instructions.md`

## Review checklist

- [ ] Least privilege preserved
- [ ] Approval gates updated when new write tools added
- [ ] Forbidden patterns list covers new risky commands
- [ ] Validation scripts enforce changes

## Incident handling

If a secret appears in the working tree, stop and rotate credentials out of band. Do not commit remediation artifacts containing the secret.
