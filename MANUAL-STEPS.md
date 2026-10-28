# RJ Arts — Manual Setup (Dawn duplicate me 13 files paste karke)

Do zip hain, confusion na karein:

| Zip | Kaam |
|---|---|
| **`rj-arts-changes.zip`** | **Sirf 13 changed files** (204 KB) — ye guide isi ke liye hai. Copy-paste ke liye. |
| `rj-arts-theme.zip` | Poora theme (350 files) — sirf **Themes → Add theme → Upload zip** ke liye. |

> ⚠️ `rj-arts-changes.zip` ko theme upload **na** karein — usme Dawn ki zaroori files nahi hain.

**Total kaam: 4 nayi files + 9 replace. Koi file "patch" nahi karni — har file Ctrl+A → paste → Save.**

---

## 0. Taiyari (5 min)

1. Shopify admin → **Online Store → Themes**
2. Jis **Dawn 16.1.0** par kaam karna hai → `⋯` → **Duplicate**
3. Duplicate → `⋯` → **Edit code**
4. Ek baar duplicate ko **Customize → Save** karein (isse `config/settings_data.json` ban jata hai)
5. Explorer me folders: `assets / config / layout / locales / sections / snippets / templates`

**Rule:** har file paste ke baad **`Ctrl+S`**. Shopify wahin validate karta hai — error turant dikhega.

### ⚠️ Paste karne ka SAHI tarika (ye galti mat karein)

Shopify ka code editor **VS Code** jaisa hai. Agar aap pehle poora text **delete** karke phir paste karte hain, to editor samajhta hai ki aap file **delete** karna chahte hain — aur required files (jaise `config/settings_data.json`) par popup aata hai:

> `config/settings_data.json could not be deleted`

**Sahi tarika (ek hi action me replace):**

1. File kholein
2. Editor ke andar click karein → `Ctrl+Home` (cursor top par)
3. `Ctrl+A` (sab select hoga)
4. **Seedha `Ctrl+V`** — paste hi selection ko replace kar dega (beech me `Delete`/`Backspace` **na** dabayein)
5. `Ctrl+S`

File kabhi khaali save nahi hogi, isliye "could not be deleted" popup nahi aayega.

Agar galti ho jaye: page reload karein → file kholein → `Ctrl+Z` (undo) ya dobara paste → `Ctrl+S`.

---

## 1. 13 files — isi order me

| # | File | Action | Lines |
|---|------|--------|-------|
| 1 | `config/settings_schema.json` | REPLACE | 1551 |
| 2 | `config/settings_data.json` | REPLACE | 386 |
| 3 | `assets/rj-arts.css` | **NAYI FILE** | 1159 |
| 4 | `assets/rj-arts.js` | **NAYI FILE** | 64 |
| 5 | `layout/theme.liquid` | REPLACE | 513 |
| 6 | `sections/announcement-bar.liquid` | REPLACE | 180 |
| 7 | `sections/header.liquid` | REPLACE | 721 |
| 8 | `snippets/header-mega-menu.liquid` | REPLACE | 135 |
| 9 | `sections/header-group.json` | REPLACE | 145 |
| 10 | `sections/rj-hero.liquid` | **NAYI FILE** | 411 |
| 11 | `sections/rj-usp.liquid` | **NAYI FILE** | 145 |
| 12 | `sections/footer-group.json` | REPLACE | 61 |
| 13 | `templates/index.json` | REPLACE | 108 |

Dawn ki baaki **337 files untouched** hain — `assets/base.css`, `assets/global.js` bhi **100% stock** hain, unhe haath nahi lagana.

**Download:** `rj-arts-changes.zip` extract karein — folder structure theme jaisa hi hai, seedha path match karke paste karein.

---

## 2. Step-by-step

### Step 1 — `config/settings_schema.json` → REPLACE
Ye file "RJ Arts - brand tokens" panel add karti hai (accent colour, hairline, container width).
Full file `Ctrl+A` → paste → Save.

### Step 2 — `config/settings_data.json` → REPLACE
**Sabse important step.** Isme 5 colour schemes, fonts, page width, cart = drawer, RJ tokens — sab set hain.
`Ctrl+A` → paste → Save.

> Agar ye file explorer me na dikhe: Customize me koi chhota change karke **Save** dabayein, file khud ban jayegi, phir paste karein.

**Save ke baad check:** Customize → Theme settings → **Colours** me 5 schemes dikhni chahiye, aur upar ka "color schemes must be defined" banner **nahi**.

### Step 3 — `assets/rj-arts.css` → **NAYI FILE**
RJ ka poora design-system CSS (1159 lines).

1. `assets` folder par right-click → **New file** (ya `Ctrl+Shift+P` → `New File`)
2. Naam: `rj-arts.css`
3. Paste → Save

Pehli line: `/* ====...` `RJ ARTS — appended design-system block`

### Step 4 — `assets/rj-arts.js` → **NAYI FILE**
Scroll reveal + header "scrolled" state (64 lines).
`assets` → New file → naam `rj-arts.js` → paste → Save.

### Step 5 — `layout/theme.liquid` → REPLACE
Isme already sab patch hai: colour-scheme fallback, RJ tokens, `<body class="... rj-theme">`, `rj-arts.css` link (head ke end me) aur `rj-arts.js` script.
`Ctrl+A` → paste → Save.

> Ye file aapke Dawn 16.1.0 se hi bani hai (sirf 5 jagah RJ ka code add hai), isliye replace safe hai.

### Step 6 — `sections/announcement-bar.liquid` → REPLACE
Design ki **chalti hui ticker** (marquee), brass highlights, 5 messages.

### Step 7 — `sections/header.liquid` → REPLACE
Header schema me mega-menu feature cards + `max_blocks: 9`.

> ⚠️ **Step 7 pehle, Step 9 baad me** — header-group.json me `mega_feature` blocks hain, schema pehle chahiye.

### Step 8 — `snippets/header-mega-menu.liquid` → REPLACE
Mega menu ke andar 2-column feature cards + hover zoom.

### Step 9 — `sections/header-group.json` → REPLACE
5 announcement messages + 6 mega feature cards + header settings (logo middle-left, menu, sticky always).

### Step 10 — `sections/rj-hero.liquid` → **NAYI FILE**
Hero slider (3 slides, arrows, dots, auto-rotate). `sections` → New file → naam `rj-hero.liquid`.

### Step 11 — `sections/rj-usp.liquid` → **NAYI FILE**
Hero ke neeche 4-item USP strip. `sections` → New file → naam `rj-usp.liquid`.

### Step 12 — `sections/footer-group.json` → REPLACE
Footer ke 4 columns (brand + Shop + Company + Support).

### Step 13 — `templates/index.json` → REPLACE
Homepage template (abhi hero + USP; Group 2 ke baaki sections aage add honge).

> ⚠️ Steps 10–11 pehle hone chahiye, warna `Section type 'rj_hero' does not exist` error aayega.

---

## 3. Data jo manually set karna hai (code nahi)

Settings ka bada hissa Step 2 se aa jata hai. Ye cheezein editor me karni hain:

### 3.1 Logo
- Theme settings → **Logo** → `Images/logo.png` upload (1000×218)
- Logo width = 120 px (Step 2 se aayega, verify karein)
- Logo na daalein to header me text "RJ ARTS" dikhta hai

### 3.2 Colours (verify only)
| Scheme | Background | Text | Button | Button label |
|---|---|---|---|---|
| Scheme 1 cream | `#F7F4EF` | `#211C17` | `#211C17` | `#F7F4EF` |
| Scheme 2 cream 2 | `#EFE9E1` | `#211C17` | `#211C17` | `#EFE9E1` |
| Scheme 3 white | `#FFFFFF` | `#211C17` | `#211C17` | `#FFFFFF` |
| Scheme 4 ink | `#211C17` | `#F7F4EF` | `#F7F4EF` | `#211C17` |
| Scheme 5 brass | `#A9865B` | `#211C17` | `#211C17` | `#A9865B` |

Shadow = text colour. `secondary_button_label` = text colour.

### 3.3 Typography / Layout / Cart
- Heading = **Cormorant Garamond**, Body = **Jost** (scale 100 / 100)
- Page width = **1600**
- Cart type = **Drawer**
- Buttons radius = 2, border 1 · Spacing sections = 0 · Hover effects = None

### 3.4 Navigation → Main menu  ⭐ zaroori
```
Bedroom      → King Size Beds, Bedroom Storage, Bedside Tables
Living       → Sofas, Coffee Tables, Living Storage
Dining       → Dining Tables, Dining Chairs, Sideboards
New Arrivals (no children)
Best Sellers (no children)
```
**Children links ke bina mega panel kabhi nahi khulega.**

### 3.5 Hero slider (3 slides)
Image desktop + mobile, eyebrow, heading, text, 2 buttons.
Images: `Images/` folder (`Bed_Desktop_Banner.webp`, `Dining_Desktop_Banner.webp`, `Living_Room_Img.webp`…)

### 3.6 USP strip (4 items)
`1,000+ 5-Star Reviews` · `100% Solid Sheesham` · `3-Year Warranty` · `0% Finance Available`
(icon + heading + subtext per block)

### 3.7 Mega feature cards (6)
Header section → `mega_feature` blocks. Har block me:
- **Parent link** = menu naam **exactly** (`Bedroom` / `Living` / `Dining`)
- Image (3:4), Label, Link

---

## 4. Final check

| # | Check | Kahan |
|---|-------|-------|
| 1 | 5 colour schemes, banner gaya | Theme settings → Colours |
| 2 | Ticker dark ink + cream, chal raha hai | Homepage top |
| 3 | Header cream, nav 13px uppercase | Homepage |
| 4 | Icons: 1 magnifier + account + bag (+count) | Header right |
| 5 | Hover Bedroom → mega panel + 2 image cards | Homepage |
| 6 | Hero: 3 slides, arrows, dots, auto-rotate | Homepage |
| 7 | USP: 4 items, brass icons | Hero ke neeche |
| 8 | Footer: brand + Shop + Company + Support | Page bottom |
| 9 | Mobile 390px: hamburger drawer, hero 1 column | Devtools |

---

## 5. Troubleshooting

| Error / symptom | Karan | Fix |
|---|---|---|
| `color schemes must be defined…` | Step 2 nahi hua / cache | `settings_data.json` paste → Save → editor reload |
| `Block type 'mega_feature' does not exist` | Step 7 se pehle Step 9 | `header.liquid` paste, phir `header-group.json` |
| `Section type 'rj_hero' does not exist` | Steps 10–11 pending | rj-hero + rj-usp banao, phir `index.json` |
| Design jaisa styling nahi aa raha | `rj-arts.css` ya uski link missing | Step 3 + Step 5 |
| Scroll par header border/shadow nahi | `rj-arts.js` ya link missing | Step 4 + Step 5 |
| Mega menu hover par kuch nahi | Menu me children nahi | Section 3.4 |
| Kuch bhi bigad jaye | — | Duplicate delete → naya duplicate → 13 steps (25 min). Live theme safe. |

---

## 6. Appendix — sirf patch karna ho (optional)

Agar poora `layout/theme.liquid` replace nahi karna chahte, to `manual/` folder me chhote snippets hain:

- `manual/snippet-1-color-scheme-fallback.liquid` (89 lines) → `{% endfor %}` ke baad
- `manual/snippet-2-rj-tokens.liquid` (14 lines) → `{{ 'base.css' ... }}` ke neeche
- body class: `gradient` → `gradient rj-theme`
- `{{ 'rj-arts.css' | asset_url | stylesheet_tag }}` → `</head>` se pehle
- `<script src="{{ 'rj-arts.js' | asset_url }}" defer>` → `global.js` script ke neeche

`config/settings_schema.json` ke liye: `manual/snippet-3-settings-schema-rj-group.json` (81 lines) → aakhri group ke baad comma + `]` se pehle.

---

## 7. Aage

Group 1 (header) ✅ + homepage ke section 1–2 (hero, USP) ✅.

Group 2 me aage: **3** Category tiles → **4** Showroom edit → **5** Art of Rest → **6** About → **7** Best sellers grid → **8** Crafted Comfort → **9** Collection carousel → **10** Reviews. Fir **Group 3 — Footer**.
