# AGENTS — Global Operating Contract

**Scope:** Applies to all LLM agents interacting with this repository.
**Precedence:** Global (this file) → Domain overrides (`domain/AGENTS.md`, if present) → Artifact front‑matter. On conflicts, the stricter rule wins. Global safety cannot be relaxed.

---

## A. Determinism & Output Guarantees
1. **Front‑matter first.** Parse YAML front‑matter to learn inputs, constraints, and `output_expectations`. Do not proceed without it.
2. **Honor the format.**
   - If `output_expectations.format: json`, emit a single valid JSON object **and nothing else**.
   - If `markdown`, produce the specified sections/headings in the given order.
   - If `plain`, emit plain text with no extra scaffolding.
3. **Stop sequences.** If `stop_sequences` are provided, terminate exactly at the first match.
4. **No surprise content.** Do not add sections, commentary, or metadata that are not specified by the artifact.

## B. Context, Tokens & Memory
1. **Budget hint:** Respect `context_budget` (tokens).
2. **80% threshold:** Summarize prior turns into a compact state (≤15% of budget), retaining any “pinned” details indicated by the artifact or domain policy.
3. **90% threshold:** Drop non-essential examples; keep exactly one “golden” example.
4. **Hard cap:** If still over budget, request the minimal missing input or propose a compact plan before proceeding.

## C. Inputs & Validation
1. **Requireds:** Validate against `inputs.schema`. For missing required fields, ask **one** targeted question to obtain the value.
2. **Defaults:** Apply `default` where provided; otherwise omit rather than guessing.
3. **Strict binding:** Map variables **exactly** as named. No hidden assumptions or renaming.

## D. Safety & PII
1. **PII policy:** Respect `safety.pii` (`reject`, `redact`, or `allow`). Default is `reject`.
2. **Redlines:** Enforce `safety.redlines` (e.g., “no medical advice”). Decline or reframe accordingly.
3. **Disclaimers:** If present in `safety.disclaimers`, include verbatim at the end of the output.
4. **Repo discipline:** Do **not** write to or restructure the repository. Propose changes as plain text with explicit paths.

## E. Cross‑Domain Isolation
Stay within the active domain unless an artifact explicitly authorizes cross‑domain linkage. Never import prompts/templates from other domains implicitly.

## F. Quality Gates (Definition of Done for outputs)
- Inputs validated; front‑matter followed.
- Output matches specified format/structure; no extraneous text.
- Language is concise and unambiguous.
- If sources/examples were used, cite or link as instructed by the artifact.
- Add a brief **“Assumptions & Limits”** section if any uncertainty remains.

## G. Failure Handling
- **Missing input:** Ask one precise question, then proceed.
- **Ambiguity:** Offer two concise interpretations; choose the most conservative and state why.
- **Conflicting rules:** Apply the stricter rule, note the conflict in one sentence.

_This contract complements the repository’s architecture and update workflow defined in `/REPO-CONTEXT.md`._
