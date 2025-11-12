# PPT Catalog Repository Context

## Purpose and Audience

The `ppt-catalog` repository is a curated library of "release-ready" AI prompts, templates, and supporting resources intended for reuse by friends, family, and trusted collaborators. The repository favours clarity and predictability over experimentation: each artifact should be production-ready, documented, and discoverable without requiring technical expertise or code execution.

## Structural Principles

- **Domain isolation:** Every AI domain lives inside its own top-level directory, forming a self-contained catalog with domain-specific documentation, governance rules, and change history.
- **Human-readable navigation:** Directory names, file names, and contents should read naturally, enabling non-technical users to scan and locate materials quickly.
- **Predictable updates:** Changes to content or structure must propagate through the relevant documentation files and be recorded in changelogs so that consumers can trust freshness and provenance.
- **Machine-friendly indexing:** Files such as `INDEX.md` and `AGENTS.md` should be authored to support LLM agents and automated tooling without sacrificing human readability.

## Root-Level Artifacts

| File | Role | When to Update |
| --- | --- | --- |
| `README.md` | Orientation guide that explains the repository purpose, layout, and discovery tips. | Update whenever structure, conventions, or onboarding guidance changes. |
| `AGENTS.md` | Operating envelope for AI agents (rules, constraints, behaviours). | Update when agent workflow, capabilities, or guardrails are adjusted. |
| `INDEX.md` | Cross-domain catalog and quick-search reference for users and tooling. | Update when domains, major artifacts, or key tags change. |
| `USAGE-GUIDE.md` | Step-by-step instructions for running prompts/templates and achieving optimal results. | Update whenever execution patterns, prerequisites, or best practices evolve. |
| `REPO-CONTEXT.md` | Canonical reference for repository architecture, governance, and content lifecycle (this file). | Update when governance rules, structural principles, or process guidelines change. |
| `LICENSE` | MIT licence covering all distributed assets. | Rarely; only if licence terms or contact details change. |
| `DISCLAIMER.md` | Liability disclaimer communicating usage expectations and limits. | Update if legal posture or messaging needs adjustment. |
| `CHANGELOG.md` | Repository-wide change log capturing high-level updates across domains. | Append entries whenever any root-level or domain-level change occurs. |

> If additional global guardrails are needed, consider adding:
> - `CONTRIBUTING.md` for collaboration etiquette and approval workflow.
> - `STYLE-GUIDE.md` to codify tone, formatting, and metadata standards across prompts.

## Domain Directory Blueprint

Each domain directory (for example `image-style-templates/`, `chat-assistant/`) mirrors a standard layout while preserving room for domain-specific assets:

```
domain-name/
  README.md
  AGENTS.md
  INDEX.md
  USAGE-GUIDE.md
  CHANGELOG.md
  prompts/
  templates/
  assets/
```

- `README.md`: Domain overview, scope, and quick-start guidance tailored to the domain’s users.
- `AGENTS.md`: Rules and operating modes for agents working exclusively within the domain catalog.
- `INDEX.md`: Structured listing of domain prompts/templates, tagged for topics, intended audiences, and expected outputs.
- `USAGE-GUIDE.md`: Detailed execution instructions, parameters, and optimisation tips specific to the domain artifacts.
- `CHANGELOG.md`: Domain-scoped patch notes containing append-only entries that reference corresponding updates in the root `CHANGELOG.md`.
- `prompts/`: Canonical prompt files, ideally organised by subtopic (e.g., `persona/`, `workflow/`).
- `templates/`: Ready-to-use template artifacts (e.g., Markdown, JSON, or plain text skeletons).
- `assets/`: Supporting files (images, datasets, reference PDFs) required by the prompts/templates; if unused, the directory may be omitted.

> Optional extras per domain:
> - `METADATA.json` (or `.yaml`) describing prompt IDs, tags, version numbers, and dependency hints for automated tooling.
> - `EXAMPLES.md` capturing sample outputs or case studies to inspire users.

## Content Authoring Guidelines

- Write prompts and templates in plain language with explicit instructions, placeholders, and usage notes.
- Keep metadata (title, tags, intended audience, version) close to each artifact to support indexing.
- Provide cross-links between related prompts or templates within `INDEX.md` and `USAGE-GUIDE.md`.
- Highlight required context (e.g., prerequisite datasets) and expected outcomes so users can assess suitability quickly.

## Update Workflow

1. **Plan change:** Identify the domain (or root) impacted and gather the files to edit.
2. **Edit content:** Modify prompts/templates and their companion documentation within the domain directory.
3. **Synchronise documentation:**
   - Refresh domain `README.md`, `INDEX.md`, and `USAGE-GUIDE.md` with the new or updated artifacts.
   - Update domain `AGENTS.md` if agent directives need revision.
4. **Record history:** Append a dated entry to the domain `CHANGELOG.md` describing the change and linking to relevant assets.
5. **Update global records:** Append a matching entry to root `CHANGELOG.md` summarising the change and referencing the domain’s log entry.
6. **Review global guides:** Adjust root-level `README.md`, `INDEX.md`, `USAGE-GUIDE.md`, or `AGENTS.md` if the change affects repository-wide guidance.
7. **Validate discoverability:** Confirm the new or updated artifacts appear in both domain and root indexes.

## Changelog Strategy

- **Root `CHANGELOG.md`:** Aggregates all notable updates across the repository, grouped by date. Each entry should reference the affected domain(s) and files, acting as a high-level newsfeed.
- **Domain `CHANGELOG.md`:** Contains detailed, domain-specific entries. When multiple domains change simultaneously, each domain log receives its own entry, preventing cross-contamination of histories.
- Entries should follow a consistent format (e.g., `<date> - <summary> - <files impacted>`), with optional links or references for deeper context.

## Search and Indexing Considerations

- Use consistent naming conventions (lowercase-with-hyphens) for directories and files.
- Employ descriptive headings and front matter to support full-text search and LLM parsing.
- Keep `INDEX.md` files structured (tables, bullet lists, or data blocks) so agents can interpret them reliably.
- When adding new assets, update backlinks in both root and domain indexes to preserve navigability.

## Governance and Access Expectations

- Repository maintainers should monitor changes for adherence to the structure and update protocol.
- Encourage contributors (friends and family) to review relevant `USAGE-GUIDE.md` sections before running prompts to set expectations.
- AI agents interacting with the repository must read `AGENTS.md` at the relevant scope (root or domain) to comply with constraints.

## Future Enhancements

- Introduce automation scripts (outside this no-code repository) to validate that required files exist in each domain.
- Consider tagging releases or snapshots when a collection of prompts is ready for distribution.
- Explore lightweight metadata standards (e.g., JSON Schema) to enable programmatic discovery or UI generation.


