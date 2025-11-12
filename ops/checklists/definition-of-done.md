# Definition of Done — Artifacts

Apply this checklist before marking a prompt/template as **released**.

## Metadata & Structure
- [ ] YAML front‑matter present and valid against `ops/schemas/frontmatter.schema.json`
- [ ] `id`, `domain`, `type`, `version` (SemVer), `release_status` set
- [ ] `inputs.schema` declares all required parameters and defaults
- [ ] `output_expectations.format` and `structure` specified

## Quality & Safety
- [ ] Instructions are explicit, concise, and unambiguous
- [ ] Failure modes called out (assumptions and limits)
- [ ] Safety: `pii` policy set; redlines appropriate; disclaimers added if needed
- [ ] At least one “golden” example available (inline or in `examples/`)

## Discoverability
- [ ] Domain `INDEX.md` updated (table row or bullet with link)
- [ ] Tags follow `ops/TAXONOMY.md` and avoid synonyms

## History & Governance
- [ ] Domain `CHANGELOG.md` appended (date, version, summary)
- [ ] Root `CHANGELOG.md` appended with a short summary and link to the domain log
