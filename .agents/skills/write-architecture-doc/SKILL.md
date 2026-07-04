---
name: write-architecture-doc
description: Document architecture decisions and layer boundaries in docs/architecture.md.
---

## When to use

Use when adding a new governance layer, moving folders, or changing how agents consume instructions, policies, or tools.

## Steps

1. Read current `docs/architecture.md` and `AGENTS.md` boundaries table.
2. Describe the change, rationale, and affected agent ecosystems.
3. Update diagrams or tables showing instruction, capability, policy, validation, and tool layers.
4. Cross-link manifests, policies, and validation entry points.
5. Run instruction scan if headings or required docs changed.

## Expected files

- `docs/architecture.md`
- Optional updates to `README.md` folder structure section

## Validation command

```powershell
python scripts/scan_instruction_files.py
python scripts/validate_agentic_repo.py
```

## Anti-patterns

- Architecture docs that describe simulated agent runtimes.
- Stale folder trees contradicting the repository.
- Omitting security or approval implications of structural changes.
