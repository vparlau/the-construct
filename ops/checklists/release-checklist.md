# Release Checklist — Domain Changes

Run this sequence for every change that ships.

1) **Edit artifacts**
   - Update content and front‑matter (respect the schema).
   - Bump `version` per SemVer rules (MAJOR breaking, MINOR additive, PATCH fixes).

2) **Sync docs (domain)**
   - Update `INDEX.md` entry (title, type, version, path, status, tags).
   - If guidance changed, adjust `USAGE-GUIDE.md` and `README.md`.
   - Add or update “golden” examples if applicable.

3) **Record history**
   - Append domain `CHANGELOG.md` with date/version and concise bullets.

4) **Global summary**
   - Append root `CHANGELOG.md` referencing the domain log and files changed.

5) **Policy & taxonomy**
   - If behavior or tags changed, update `ops/AGENTS.md` or `ops/TAXONOMY.md`.

6) **(Optional) Machine index**
   - Regenerate `ops/catalogs/CATALOG.json` externally; set `generated: true` and update `last_updated`.

7) **Verify discoverability**
   - Confirm links work from root `INDEX.md` → domain `INDEX.md` → artifact.
