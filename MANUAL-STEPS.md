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

## 1. File list — jo pehle se paste ho chuki hain unhe SKIP karein

| # | File | Action | Lines | Status |
|---|------|--------|-------|--------|
| 1 | `config/settings_schema.json` | REPLACE | 1551 | ✅ pehle kar liya to skip |
| 2 | `config/settings_data.json` | REPLACE | 382 | **⬅ pending — Colours + banner isi se** |
| 3 | `assets/rj-arts.css` | **NAYI FILE** | 3204 | **⬅ is round me badli (footer CSS)** |
| 4 | `assets/rj-arts.js` | **NAYI FILE** | 211 | ✅ pichle round me kar liya to skip |
| 5 | `layout/theme.liquid` | REPLACE | 641 | ✅ pehle kar liya to skip |
| 6 | `sections/announcement-bar.liquid` | REPLACE | 180 | ✅ **skip — aapki set hai** |
| 7 | `sections/header.liquid` | REPLACE | 721 | ✅ pehle kar liya to skip |
| 8 | `snippets/header-mega-menu.liquid` | REPLACE | 134 | ✅ pehle kar liya to skip |
| 9 | `sections/header-group.json` | REPLACE | 145 | ✅ pehle kar liya to skip |
| 10 | `sections/rj-hero.liquid` | **NAYI FILE** | 411 | ✅ pehle kar liya to skip |
| 11 | `sections/rj-usp.liquid` | **NAYI FILE** | 145 | ✅ pehle kar liya to skip |
| 12 | `sections/rj-showroom.liquid` | **NAYI FILE** | 357 | ✅ pehle kar liya to skip |
| 13 | `sections/rj-categories.liquid` | **NAYI FILE** | 201 | ✅ pehle kar liya to skip |
| 14 | `sections/rj-band.liquid` | **NAYI FILE** | 188 | ✅ pehle kar liya to skip |
| 15 | `sections/rj-about.liquid` | **NAYI FILE** | 220 | ✅ pehle kar liya to skip |
| 16 | `sections/rj-best.liquid` | **NAYI FILE** | 239 | ✅ pehle kar liya to skip |
| 17 | `sections/rj-collections.liquid` | **NAYI FILE** | 212 | ✅ pehle kar liya to skip |
| 18 | `sections/rj-reviews.liquid` | **NAYI FILE** | 212 | ✅ pehle kar liya to skip |
| 19 | `sections/footer.liquid` | REPLACE (Dawn ki file) | 447 | **⬅ is round me badli (design footer isi me hai)** |
| 20 | `sections/footer-group.json` | REPLACE | 63 | **⬅ is round me badla** |
| 21 | `templates/index.json` | REPLACE | 413 | ✅ pichle round me kar liya to skip |

Dawn ki baaki **336 files untouched** hain — `assets/base.css`, `assets/global.js` bhi **100% stock** hain, unhe haath nahi lagana.

**Download:** `rj-arts-changes.zip` extract karein — folder structure theme jaisa hi hai, seedha path match karke paste karein.

---

## 2. Step-by-step

### Step 1 — `config/settings_schema.json` → REPLACE
Ye file "RJ Arts - brand tokens" panel add karti hai (accent colour, hairline, container width).
Full file `Ctrl+A` → paste → Save.

### Step 2 — `config/settings_data.json` → REPLACE
**Sabse important step.** Isme 5 colour schemes, page width, cart = drawer, RJ tokens — sab set hain.
`Ctrl+A` → `Ctrl+V` → Save.

> **Fonts ki keys is file me nahi hain** (jaan-boojh kar). `cormorant_garamond_n4` / `jost_n4` aapke store ke font library me valid nahi hain — isi wajah se `FileSaveError: … is not a valid font handle` aata tha aur ye file save hi nahi hoti thi. Type ab `theme.liquid` (Google Fonts) se aata hai, isliye design ke fonts milenge hi.

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

### Step 6 — `sections/announcement-bar.liquid` → REPLACE *(aapke yahan already set — SKIP)*
Design ki **chalti hui ticker** (marquee), brass highlights, 5 messages.

### Step 7 — `sections/header.liquid` → REPLACE
Header schema me mega-menu feature cards + `max_blocks: 9`.

> ⚠️ **Step 7 pehle, Step 9 baad me** — header-group.json me `mega_feature` blocks hain, schema pehle chahiye.

### Step 8 — `snippets/header-mega-menu.liquid` → REPLACE
Mega menu ke andar 2-column feature cards + hover zoom, aur **parent menu item ab asli link hai** (Bedroom par click karne se collection page khulti hai; caret/hover se panel khulta hai).

### Step 9 — `sections/header-group.json` → REPLACE
5 announcement messages + 6 mega feature cards + header settings (logo middle-left, menu, sticky always).

### Step 10 — `sections/rj-hero.liquid` → **NAYI FILE**
Hero slider (3 slides, arrows, dots, auto-rotate). `sections` → New file → naam `rj-hero.liquid`.

### Step 11 — `sections/rj-usp.liquid` → **NAYI FILE**
Hero ke neeche 4-item USP strip. `sections` → New file → naam `rj-usp.liquid`.

### Step 12 — `sections/rj-showroom.liquid` → **NAYI FILE**
Homepage ka **The showroom edit** (pill tabs + horizontal product rail).
`sections` → New file → naam `rj-showroom.liquid` → paste → Save.

### Step 13 — `sections/rj-categories.liquid` → **NAYI FILE**
Homepage ke **Category tiles** (asymmetrical 1.4fr / 1fr grid, pehla tile 2 rows).
`sections` → New file → naam `rj-categories.liquid` → paste → Save.

### Step 14 — `sections/rj-band.liquid` → **NAYI FILE**
Feature band (photo + left copy). Isi ek file se **do** bands banenge —
"The Art of Rest" (560px) aur aage "Crafted Comfort" (520px).
`sections` → New file → naam `rj-band.liquid` → paste → Save.

### Step 16 — `sections/rj-best.liquid` → **NAYI FILE**
Best sellers 4-up grid. `sections` → New file → naam `rj-best.liquid` → paste → Save.

### Step 17 — `sections/rj-collections.liquid` → **NAYI FILE**
Collection carousel (arrows wali rail). File naam: `rj-collections.liquid`.

### Step 18 — `sections/rj-reviews.liquid` → **NAYI FILE**
Reviews rail (merchant ke apne review blocks, koi app nahi chahiye).
File naam: `rj-reviews.liquid`.

### Step 19 — `sections/footer.liquid` → **REPLACE (Dawn ki hi file)**
Group 3 ka footer: newsletter band (asli customer form), brand + 3 menus,
payment chips, bottom bar, ghost "RJ ARTS" wordmark.
**Nayi file nahi banani** — `sections/footer.liquid` (Dawn wali) kholiye,
`Ctrl+Home` → `Ctrl+A` → paste → `Ctrl+S`.
> Design footer isi ek file me hai, isliye theme me **ek hi footer** rahega —
> bilkul `header.liquid` ki tarah. Section type bhi Dawn ka hi (`footer`) hai.
> Agar pichle round me galti se `sections/rj-footer.liquid` bana li thi to
> **usse delete kar dein** (warna Add section list me do footer dikhenge).

### Step 20 — `sections/footer-group.json` → REPLACE
Footer ke 4 columns (brand + Shop + Company + Support).

### Step 15 — `sections/rj-about.liquid` → **NAYI FILE**
"Our Story" split section (4:5 photo + floating 25+ Years badge, 3 stats).
`sections` → New file → naam `rj-about.liquid` → paste → Save.

### Step 21 — `templates/index.json` → REPLACE
Homepage template — poore 10 sections (hero, USP, category tiles, showroom, Art of Rest band, About, best sellers, Crafted Comfort band, collection carousel, reviews).

> ⚠️ Steps 10–18 (saari custom sections) pehle hone chahiye, warna `Section type 'rj_best' / 'rj_collections' / 'rj_reviews' / 'rj-footer' does not exist` error aayega.

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
- **Typography panel chhod dein** — design ke fonts (Cormorant Garamond + Jost) theme se hi load hote hain.
  Customize me panel "Assistant" dikha sakta hai, par site par Cormorant + Jost render honge.
  Agar aap panel se koi font chunenge, wahi font use hone lagega (panel override kar deta hai).
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

### 3.7 Category tiles (homepage section)
Customize → **RJ Category tiles** → 3 blocks. Har block me **Collection** chunein
(Bedroom / Living / Dining) — title, link aur image apne aap bhar jayenge.
Design jaisa look chahiye to **Custom image** me `Images/Bed.png`, `Images/Living.jpg`,
`Images/Dining.png` upload karein. Sub-line text design se default aata hai.

### 3.8 Showroom edit — collections (zaroori)
Customize → **RJ Showroom edit** → 3 tabs. Har tab me **Collection** chunein:
`New Arrivals` collection → tab 1, `Best Sellers` → tab 2, `Heritage` → tab 3.
Collection na chuni ho to section dummy cards dikhata hai (₹0, "Example
solid-wood product") — yeh sirf placeholder hai.

- Card **badge** product tag se aata hai: `Sale` (compare-at price > price),
  warna `New Arrivals` tag → "New", `Heritage` tag → "Heritage".
- Stars ke neeche wala text (`New` / `Best Seller` / `Signature`) tab setting
  se aata hai — asli review count ke liye reviews app chahiye.
- "Quick View" button product page kholta hai (hover par slide-up). Sach ka
  modal quick-view ke liye app lagana padega.

### 3.9 Feature band — image (zaroori)
Customize → **RJ Feature band** → **Background image** me `Images/Bed2.png`
upload karein (Art of Rest). Design me subject right-of-centre hai — left side
par dark gradient aata hai, isliye photo me furniture right me rakhein.
Button label `Shop Bedroom` → link `/collections/bedroom` (collection ban jaye
ke baad). Aage "Crafted Comfort" band isi section se banega — image
`Images/Sofa_Desktop_Banner.webp`, height 520.

### 3.10 About story — image (zaroori)
Customize → **RJ About story** → **Workshop / story image** me
`Images/About/Our Story.png` upload karein (portrait 4:5). Badge text
(`25+ Years` / `of Woodcraft`) aur 3 stats blocks wahin se edit hote hain.
Button `Read Our Story` → `pages/about-us` (page banane ke baad).

### 3.11 Best sellers — collection (zaroori)
Customize → **RJ Best sellers** → **Collection** = `best-sellers`. 4 products
dikhenge (slider se 2–8). Badge: discount % (compare-at se) ya `Best Sellers`
tag hone par "Best Seller".

### 3.12 Collection carousel — collection cards
Customize → **RJ Collection carousel** → har card me **Collection** chunein
(Sevilla / Crew / Simons / Scott / Arvyn / Bar jaisi series-auto collections).
"Small image tag" aur "Category line" design ke text hain — apne hisaab se badal
sakte hain. Card na chunein to placeholder dikhega.

### 3.13 Reviews rail — apne reviews
Customize → **RJ Reviews rail** → 4 review blocks pehle se bhare hain (design ke
text). Apne asli reviews paste karein: text, naam, product line, stars. Reviews
app baad me lag sakta hai — CSS same rahega.

### 3.14 Footer — 4 cheezein (zaroori)
1. **Menus** (Settings → Navigation): `Company` aur `Support` menus banayein —
   footer-group dono ko `footer` menu par point karta hai, ya Customize me
   **RJ Footer** ke har column me alag menu chunein.
2. **Social links**: Customize → RJ Footer → Instagram / Facebook / Pinterest /
   YouTube URLs. Khaali chhodein to icon dikhega hi nahi.
3. **Payment chips**: store me payment method active ho to asli icons aate hain;
   warna `UPI, Visa, Mastercard, EMI` text chips dikhte hain.
4. **Logo**: Theme settings ka logo hi invert hokar white dikhta hai
   (RJ Footer me chaho to alag logo bhi laga sakte hain).

### 3.15 Mega feature cards (6)
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
| 5a | Showroom: 3 pill tabs switch, arrows rail scroll karte hain | Hero ke neeche |
| 6 | Hero: 3 slides, arrows, dots, auto-rotate | Homepage |
| 7 | USP: 4 items, brass icons | Hero ke neeche |
| 7a | Art of Rest band: photo + gold eyebrow + white button | Showroom ke neeche |
| 7b | About: 4:5 photo + 25+ Years badge + 3 brass stats | Band ke neeche |
| 7c | Best sellers: 4 cards, −46% jaise rust badges | About ke neeche |
| 7d | Crafted Comfort band (sofa photo, 520px) | Best sellers ke neeche |
| 7e | Collection carousel: arrows rail scroll karte hain | Band ke neeche |
| 7f | Reviews: white section, cream cards, brass initials | Sabse neeche |
| 8 | Footer: brand + Shop + Company + Support | Page bottom |
| 8a | Footer newsletter band + brass Subscribe button | Footer top |
| 8b | Payment chips + ghost "RJ ARTS" wordmark | Footer bottom |
| 9 | Mobile 390px: hamburger drawer, hero 1 column | Devtools |

---

## 5. Troubleshooting

| Error / symptom | Karan | Fix |
|---|---|---|
| `FileSaveError: 'cormorant_garamond_n4' is not a valid font handle` | purani `settings_data.json` (jisme font keys thi) paste ho gayi | naya `rj-arts-changes.zip` se `settings_data.json` dobara paste karein |
| `color schemes must be defined…` | Step 2 nahi hua / cache | `settings_data.json` paste → Save → editor reload |
| `Block type 'mega_feature' does not exist` | Step 7 se pehle Step 9 | `header.liquid` paste, phir `header-group.json` |
| `Section type 'rj_hero' does not exist` | Steps 10–11 pending | rj-hero + rj-usp banao, phir `index.json` |
| `config/settings_data.json` folder me hi nahi dikh raha | upload/paste ke waqt file theme me nahi gayi | Section 5.1 dekhein |
| Colours panel khaali + banner | `settings_data.json` missing | Section 5.1 → Step 2 |
| Hero me description aur buttons ke beech gap nahi | purani `rj-arts.css` (reset rule) | Step 3 dobara paste (2281 lines) |
| Showroom aur band ek dusre se chipke hain | purani `rj-arts.css` | Step 3 dobara paste |
| Band ka button khaali/white box dikh raha | purani `rj-arts.css` + purani `rj-band.liquid` | Steps 3 + 14 |
| Design jaisa styling nahi aa raha | `rj-arts.css` ya uski link missing | Step 3 + Step 5 |
| Scroll par header border/shadow nahi | `rj-arts.js` ya link missing | Step 4 + Step 5 |
| Mega menu hover par kuch nahi | Menu me children nahi | Section 3.4 |
| Kuch bhi bigad jaye | — | Duplicate delete → naya duplicate → 14 steps (30 min). Live theme safe. |

---

### 5.1 `config/settings_data.json` missing / `could not be deleted`

Editor banner `The configuration file config/settings_data.json needs to be added…`
aur **Theme settings → Colours = "No color schemes defined"** ka matlab: theme me
yeh file nahi hai (ya khaali hai). Check: **Edit code → config** — wahan sirf
`settings_schema.json` dikhe.

Fix (is order me try karein):

1. **Edit code → config → `settings_schema.json` ke saath jo bhi file hai** dekhein.
   Agar `settings_data.json` hai → Step 2 ke content se **Replace** karein
   (`Ctrl+Home` → `Ctrl+A` → paste → `Ctrl+S`).
2. Agar file hai hi nahi → **config** folder ke aage `...` (ya sidebar me `+`)
   → **New file** → naam exactly `settings_data.json` → Step 2 ka content paste → Save.
3. New file ka option na mile → **Customize** me koi bhi chhota change karein
   (e.g. logo width slider hilaayein) → **Save**. Iske baad Shopify file khud
   bana deta hai, phir Step 2 ka content paste karein.
4. Phir bhi na ho → theme **delete** karke `rj-arts-theme.zip` dobara upload karein
   (fresh slot me) aur `config` check karein.

> Note: ab tak ke zips me `config/settings_data.json` **zip ke andar maujood hai**
> (verify: `unzip -l rj-arts-theme.zip | grep config` → 12 KB). Isliye agar wo
> theme me nahi pahuncha to problem upload/paste side ki hai, file ki nahi.
>
> Safety net: `theme.liquid` me fallback hai — schemes missing ho to bhi
> storefront cream/ink + Cormorant/Jost me dikhega, sirf **Colours panel** aur
> banner baaki rahega.

---

## 6. Appendix — sirf patch karna ho (optional)

Agar poora `layout/theme.liquid` replace nahi karna chahte, to `manual/` folder me chhote snippets hain:

- `manual/snippet-1-color-scheme-fallback.liquid` (102 lines) → `{% endfor %}` ke baad
- `manual/snippet-2-rj-tokens.liquid` (14 lines) → `{{ 'base.css' ... }}` ke neeche
- body class: `gradient` → `gradient rj-theme`
- `{{ 'rj-arts.css' | asset_url | stylesheet_tag }}` → `</head>` se pehle
- `<script src="{{ 'rj-arts.js' | asset_url }}" defer>` → `global.js` script ke neeche

`config/settings_schema.json` ke liye: `manual/snippet-3-settings-schema-rj-group.json` (81 lines) → aakhri group ke baad comma + `]` se pehle.

---

## 7. Aage

Group 1 (header) ✅ · Group 2 (**10/10** homepage sections) ✅ · Group 3 (footer) ✅ — teeno groups poore. Ab bacha: Colours/settings_data, template pages (collection, product, about), aur content entry.

Group 2 ✅ **poora ho gaya** (10/10 sections). Ab sirf **Group 3 — Footer** bacha hai (newsletter band, brand, 3 menus, contact, socials, payment chips, ghost wordmark).
