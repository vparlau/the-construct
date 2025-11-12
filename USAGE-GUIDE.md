# Usage Guide (Repository‑Wide)

This guide explains how to run prompts/templates consistently for high‑quality results across all domains.

---

## 1) Find and select an artifact
1. Open the root **`INDEX.md`** → choose a domain → open the domain’s **`INDEX.md`**.
2. Skim titles and tags; pick an artifact that matches your goal and output format.

## 2) Read the front‑matter
At the top of each artifact:
- **Inputs (`inputs.schema`)** — required fields and defaults.
- **Output expectations** — format and structure to produce (markdown/json/plain).
- **Constraints** — do/don’t rules.
- **Safety** — PII policy and redlines.

## 3) Prepare your inputs
- Provide all **required** fields; use the declared names exactly.
- Keep inputs concise and factual; link any long context rather than pasting it inline.
- If examples exist, clone their structure.

## 4) Run with discipline
- Respect the **format** and **structure** requested; don’t add commentary.
- If the artifact expects JSON, return **only** one valid JSON object.
- If you hit token limits, summarize secondary details first; keep essentials and any “golden” example intact.

## 5) Validate the output
Use this quick checklist:
- Matches the declared **format/structure**.
- Answers the task completely and concisely.
- Respects **constraints** and **safety**.
- Any assumptions are listed briefly at the end.

## 6) Troubleshooting
- **Missing input?** Provide the specific field listed in `inputs.schema`.
- **Ambiguity?** Re‑read the artifact’s instructions; if still unclear, propose two interpretations and choose the safer one.
- **Unexpected verbosity?** Tighten inputs and remove non‑essential context.
- **JSON not accepted?** Ensure there’s no extra text before/after the object and keys match the expected schema.

---

## Conventions (important)
- Lowercase‑hyphen names for files and folders.
- Keep domain folders minimal and user‑facing.
- Avoid personal data in examples; redact when in doubt.
