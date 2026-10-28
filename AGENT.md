# RJ Arts — Shopify theme agent brief

## Who
Shopify store **RJ Arts**. Custom storefront based on **Dawn**, matching the HTML in `/design`.

## Layout of this repo
- `design/` — source of truth for look & pages (static HTML).
- `theme_export/` — the actual Shopify theme (Liquid, assets, sections, snippets, templates, config, locales). This is what gets zipped and uploaded.
- Never mix design HTML into theme folders except as a reference.

## How the merchant works
- They paste CSS / Liquid / JS **manually** into the theme editor. Committing is not enough.
- Every change: write the **code in chat**, with:
  - exact file name (`assets/style.css`, `sections/main-product.liquid`, …)
  - **START line** and **END line** of the block to replace
  - what must survive above and below
- For a full Liquid file they prefer copy/paste of the whole file.
- For CSS they prefer step-by-step: “after this selector, add this block”.
- Do **not** create `snippets/custom-css.liquid` (or any extra snippet) just to hold handwritten CSS.
- Do **not** delete existing **ID-based** CSS rules. Add class / store-independent selectors **alongside**. They may run more than one store on similar code.
- Do **not** paste zip files as markdown download links. Use a GitHub **blob URL** on a fetchable branch.

## Theme zip
- Theme lives in `theme_export/`.
- Build: `(cd theme_export && zip -q -r ../rj-arts-theme.zip . -x '*.DS_Store')`
- Zip must contain **only** theme files (400-ish Dawn files). No `preview-*.html`, no `AGENT.md`, no `design/`, no `POLICY`.
- Before a new batch of work, use the **latest** zip / `theme_export` as the base.
- When merging a live Shopify export: **theirs wins** on shared files. Keep their handwritten rules verbatim; only **append** new blocks.

## Previews
- Static `preview-*.html` at repo root for the current change.
- Preview must load (no error page). No live-store / browser testing is available — do not ask the merchant to “check the live site”.
- Scope CSS tightly. Do not disturb collection cards / product grid when fixing something else.

## CSS numbers
- Merchant audits px. For any `clamp()` / font / spacing change, show computed px at **360 / 390 / 430 / 768 / 989**.
- Body text ≥ ~15px at 360px width.
- Accepted tighten band roughly −5% to −16% unless they ask otherwise.

## Implementation defaults
- Match `design/` visually (type, colour, spacing, components). Do not invent a second look.
- Dawn sections/snippets where they already fit; custom CSS in existing `assets/*.css` (append at end unless overriding a specific block).
- Mobile and desktop both. If a gesture is specified (swipe, hold-to-zoom), implement that — don’t substitute tap-only.
- Empty states: follow the design; if unspecified, text-only, no extra card/chrome.
- Global content bugs (e.g. `<br>` in policy HTML) must be fixed globally, not on one page.

## Do not
- Switch git branch away from the session branch.
- Rewrite the whole theme in one shot — page by page, matching `design/`.
- Ask the merchant to re-explain this file. Re-read it at the start of every task.
