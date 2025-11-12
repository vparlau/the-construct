# ops/ — Maintainers & Agents

This folder centralizes the *internal* operating contract for `the-construct`: agent rules, schemas, taxonomy, and release guardrails. Domains remain minimal and user-facing; `ops/` contains the machinery that keeps the catalog predictable and safe.

**Precedence**
1) Global rules in `ops/AGENTS.md`
2) Optional domain overrides in `domain/AGENTS.md` (may specialize, not weaken)
3) Artifact front‑matter in each prompt/template (must be respected by agents)

**What lives here**
- **AGENTS.md** — global agent contract (determinism, token/memory policy, safety, failure handling)
- **TAXONOMY.md** — canonical tags for consistent search and indexing
- **schemas/** — JSON Schemas for artifact front‑matter and optional domain manifests
- **catalogs/** — (optional) machine-generated index for tools; users can ignore
- **checklists/** — definition of done and release checklist (lightweight, enforceable)

**When to update**
- Behavior rules change → `AGENTS.md`
- Tagging vocabulary changes → `TAXONOMY.md`
- Metadata fields change → `schemas/…`
- Release process changes → `checklists/…`
- Machine index regenerated → `catalogs/`

See the repository’s context and domain blueprint for the minimal, user‑facing structure in `/REPO-CONTEXT.md`.
