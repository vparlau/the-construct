# Start Here — How to Navigate the Catalog

**Who this is for:** Anyone who wants to quickly find and use a release‑ready prompt or template without touching any internal files.

**What this catalog is:** A simple library grouped by *domains* (topic areas). Each domain is a mini‑catalog with a short index and guide. You don’t need to read anything in `ops/` to use the catalog.

---

## Quick 30‑second tour

1. Open the **[Global Index](./INDEX.md)** — it lists all domains.
2. Click a domain’s **INDEX.md** — pick a prompt/template that matches your goal.
3. Open the file and follow its **front‑matter** (inputs, expected output, safety).
4. If you need help running it well, see the domain’s **USAGE-GUIDE.md**.

> The catalog keeps each domain self‑contained so you only see what matters. This is intentional and part of the repository’s design.

---

## Find by goal

- **Write something:** try the `writing/` domain.  
- **Summarize or extract:** look for artifacts tagged `summarization` or `extraction` in the domain index.  
- **Plan or ideate:** look for `planning` or `ideation`.  
- **Translate or rephrase:** look for `translation` or `rewriting`.

Inside each domain’s **INDEX.md**, you’ll see titles, versions, tags, and paths. Pick the one that matches your outcome and output format (Markdown or JSON).

---

## Find by output format

- Prefer **Markdown** (headings, lists)? Choose artifacts with `output_expectations.format: markdown`.
- Need **JSON** for tools? Choose artifacts with `format: json` and listed keys in `structure`.
- Just **plain text**? Look for `format: plain`.

You can check this in the file’s YAML front‑matter near the top.

---

## What you’ll see inside an artifact

At the top of each prompt/template is a small YAML block (the “front‑matter”). It tells you:

- **Inputs** — required fields and helpful defaults.  
- **Output expectations** — format and structure the artifact will produce.  
- **Constraints & Safety** — do/don’t rules and PII stance.  
- **Version & Status** — whether it’s draft, review, released, or deprecated.

You don’t need to edit this block; it’s there to guide you to provide the right inputs and expect the right output.

---

## Using an artifact (fast path)

1. **Open** the artifact from the domain’s `INDEX.md`.  
2. **Provide inputs** exactly as named in the `inputs.schema`.  
3. **Run** and ensure the output matches the format/structure stated.  
4. **Validate** with the quick checks below.

**Quick checks**
- Output matches **format** (Markdown/JSON/plain) and the listed **structure** (sections/keys).  
- The result answers your goal without fluff.  
- Any disclaimers or safety notes (if present) are included.

If you want deeper tips for great results, open the domain’s **USAGE-GUIDE.md**.

---

## Common “stuck” cases

- **Missing a required field?** Re‑check `inputs.schema` at the top; provide the exact field name.  
- **Output too long?** Trim your input or use a shorter “topic”/“goal” description.  
- **JSON not accepted?** Make sure there’s no extra text before or after the JSON object, and keys match the artifact’s `structure`.

---

## Where *not* to go (unless you’re curious)

- **`ops/`** contains internal rules, schemas, and checklists for maintainers and agents. You don’t need it to use the catalog day‑to‑day. The minimal domain layout and navigation are designed so you can ignore `ops/`

---

## Glossary

- **Domain:** A topic area (e.g., `writing/`) with its own index and guide.  
- **Artifact:** A single prompt or template you can run.  
- **Front‑matter:** The small YAML block at the top of an artifact describing inputs/outputs.

---

## Next steps

- Start at the **[Global Index](./INDEX.md)**.  
- Inside a domain, use its **INDEX.md** to pick an artifact, then read **front‑matter** and run.  
- If you want pro‑level results, see the repository‑wide **[USAGE-GUIDE.md](./USAGE-GUIDE.md)** and the domain’s `USAGE-GUIDE.md`.