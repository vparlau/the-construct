# the-construct — Release‑Ready Prompt & Template Library

**Audience:** Non‑technical users (friends, family, collaborators) and agents.  
**Goal:** A no‑code, predictable catalog of prompts/templates organized by domain, with clear navigation and minimal surface area.

---

## How this repository is organized

- **Root (you are here):** User‑facing orientation and global guides.  
- **`ops/` (internal):** Agent rules, schemas, taxonomy, and checklists that keep the system deterministic and safe. See [`ops/AGENTS.md`](./ops/AGENTS.md) and the front‑matter schema in [`ops/schemas/frontmatter.schema.json`](./ops/schemas/frontmatter.schema.json).  
- **Domains:** Each domain is a self‑contained mini‑catalog (see layout below).

### Minimal domain layout
```
domain-name/
  README.md
  INDEX.md
  USAGE-GUIDE.md
  CHANGELOG.md
  prompts/
  templates/   # optional
  assets/      # optional
```
Domains inherit global agent behavior from `ops/AGENTS.md`. Add `domain/AGENTS.md` **only** when you need domain‑specific overrides.

---

## Quickstart

1) Open **[`INDEX.md`](./INDEX.md)** to find a domain.  
2) In the domain folder, open its **`INDEX.md`** and select an artifact.  
3) Read the artifact’s **YAML front‑matter** to understand inputs, constraints, and expected output.  
4) Follow the domain **`USAGE-GUIDE.md`** for best results.  
5) If something changed, the domain’s **`CHANGELOG.md`** records the history; root **`CHANGELOG.md`** summarizes major updates.

---

## Artifact anatomy (front‑matter)
Each prompt/template starts with YAML front‑matter that agents parse for determinism:
- `id`, `title`, `domain`, `type` (`prompt` | `template`), `version` (SemVer)  
- `release_status` (`draft` | `review` | `released` | `deprecated`)  
- `tags`, `owner`, `license`, optional `models`  
- `context_budget` (token hint)  
- `inputs.schema` (required fields/defaults)  
- `output_expectations` (format/structure/stop sequences)  
- `constraints`, `safety` (PII policy + redlines), `changelog_ref`

Schema reference: [`ops/schemas/frontmatter.schema.json`](./ops/schemas/frontmatter.schema.json)

---

## Update & release discipline (abridged)

1) Edit artifact → update domain **`INDEX.md`**.  
2) Append domain **`CHANGELOG.md`**.  
3) Append root **`CHANGELOG.md`** with a short summary and link to the domain entry.  
4) If rules/tags changed, update **`ops/`** docs; re‑generate any machine catalogs externally.

> This repo stays *no‑code*: validation and catalog generation, if used, run outside and simply read the Markdown/JSON in `ops/`.

---

## Legal & safety

- Licensed under **MIT** (see [`LICENSE`](./LICENSE)); no warranty (see [`DISCLAIMER.md`](./DISCLAIMER.md)).  
- Avoid personal data in examples; if present, redact. Respect each artifact’s `safety` policy.

---

## Learn more

- Architecture & operating contract: **`REPO-CONTEXT.md`** (root) and **`ops/REPO-CONTEXT.md`** (internal addendum).
- Agent behavior: **`ops/AGENTS.md`**.
- Tag vocabulary: **`ops/TAXONOMY.md`**.
