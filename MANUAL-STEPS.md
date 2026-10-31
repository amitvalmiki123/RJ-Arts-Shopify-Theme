# RJ Arts — Manual Setup (Dawn duplicate me files paste karke)

Do zip hain, confusion na karein:

| Zip | Kaam |
|---|---|
| **`rj-arts-changes.zip`** | **Sirf changed files** — ye guide isi ke liye hai. Copy-paste ke liye. |
| `rj-arts-theme.zip` | Poora theme — sirf **Themes → Add theme → Upload zip** ke liye. |

> ⚠️ `rj-arts-changes.zip` ko theme upload **na** karein — usme Dawn ki zaroori files nahi hain.

**Total kaam: 13 nayi files + 12 replace. Koi file "patch" nahi karni — har file Ctrl+A → paste → Save.**

**Is round me (Product page) 4 files:** `assets/rj-arts.css`, `assets/rj-arts.js`,
`sections/rj-product.liquid` (**nayi**), `templates/product.json`. Baaki sab ✅ skip.

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
| 3 | `assets/rj-arts.css` | **NAYI FILE** | 4961 | **⬅ is round me badli (Product page CSS)** |
| 4 | `assets/rj-arts.js` | **NAYI FILE** | 510 | **⬅ is round me badla (variant + sticky bar JS)** |
| 5 | `layout/theme.liquid` | REPLACE | 641 | ✅ pehle kar liya to skip |
| 6 | `sections/announcement-bar.liquid` | REPLACE | 180 | ✅ **skip — aapki set hai** |
| 7 | `sections/header.liquid` | REPLACE | 820 | ✅ pichle round me kar liya to skip |
| 8 | `sections/header-group.json` | REPLACE | 150 | ✅ pichle round me kar liya to skip |
| 9 | `snippets/header-mega-menu.liquid` | REPLACE | 134 | ✅ pehle kar liya to skip |
| 10 | `sections/rj-hero.liquid` | **NAYI FILE** | 411 | ✅ pehle kar liya to skip |
| 11 | `sections/rj-usp.liquid` | **NAYI FILE** | 145 | ✅ pehle kar liya to skip |
| 12 | `sections/rj-showroom.liquid` | **NAYI FILE** | 352 | ✅ pichle round me kar liya to skip |
| 13 | `sections/rj-categories.liquid` | **NAYI FILE** | 201 | ✅ pehle kar liya to skip |
| 14 | `sections/rj-band.liquid` | **NAYI FILE** | 188 | ✅ pehle kar liya to skip |
| 15 | `sections/rj-about.liquid` | **NAYI FILE** | 220 | ✅ pehle kar liya to skip |
| 16 | `sections/rj-best.liquid` | **NAYI FILE** | 234 | ✅ pichle round me kar liya to skip |
| 17 | `sections/rj-collections.liquid` | **NAYI FILE** | 219 | ✅ pehle kar liya to skip *(homepage carousel)* |
| 18 | `sections/rj-reviews.liquid` | **NAYI FILE** | 276 | ✅ pichle round me kar liya to skip |
| 19 | `sections/footer.liquid` | REPLACE (Dawn ki file) | 447 | ✅ pichle round me kar liya to skip |
| 20 | `sections/footer-group.json` | REPLACE | 63 | ✅ pichle round me kar liya to skip |
| 21 | `templates/index.json` | REPLACE | 418 | ✅ pichle round me kar liya to skip |
| 22 | `sections/rj-collection.liquid` | **NAYI FILE** | 556 | ✅ pichle round me kar liya to skip |
| 23 | `templates/collection.json` | REPLACE | 35 | ✅ pichle round me kar liya to skip |
| 24 | `sections/rj-product.liquid` | **NAYI FILE** | 726 | **⬅ is round me bani (Product page)** |
| 25 | `templates/product.json` | REPLACE | 104 | **⬅ is round me badla (product template)** |

Dawn ki baaki **336 files untouched** hain — `assets/base.css`, `assets/global.js` bhi **100% stock** hain, unhe haath nahi lagana.

> ⚠️ **Do sections ke naam me sirf ek `s` ka farq hai — ye duplicate NAHI hain:**
>
> | File | Kahan use hota hai | Theme editor me naam | Template |
> |---|---|---|---|
> | `rj-collections.liquid` (**plural**) | Homepage ka "The Collections" carousel | **RJ Collection carousel** | `templates/index.json` |
> | `rj-collection.liquid` (**singular**) | Collection page (hero, filter, grid) | **RJ Collection page** | `templates/collection.json` |
>
> Dono alag files hain — **koi ek bhi delete na karein**. Naya file banate waqt naam
> exactly copy karein (extra `s` ya kam `s` → `Section type ... does not exist` error).

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

### Step 3 — `assets/rj-arts.css` → **NAYI FILE** *(is round me badli)*
RJ ka poora design-system CSS (1159 lines).

1. `assets` folder par right-click → **New file** (ya `Ctrl+Shift+P` → `New File`)
2. Naam: `rj-arts.css`
3. Paste → Save

Pehli line: `/* ====...` `RJ ARTS — appended design-system block`

### Step 4 — `assets/rj-arts.js` → **NAYI FILE** *(is round me badla)*
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

### Step 17 — `sections/rj-collections.liquid` → **NAYI FILE** *(plural — homepage carousel)*
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

### Step 22 — `sections/rj-collection.liquid` → **NAYI FILE** *(singular — collection page)*

> ⚠️ Ye **`rj-collection.liquid`** hai (bina `s` ke). Step 17 wali
> **`rj-collections.liquid`** (plural) homepage ka carousel hai — usse replace mat karein.

Collection page ka poora layout ek hi section me: hero (breadcrumb + title +
description + 16% opacity image), sticky toolbar (Filter pill + live count +
sort), active-filter chips, 4-up product grid (wishlist heart + tag + price +
stars), "Load More" bar aur **left filter drawer**.

`sections` → **New file** → naam `rj-collection.liquid` → paste → `Ctrl+S`.

Kya asli data se aata hai (hardcoded nahi):
- Title / description / image → collection settings se
- Products, prices, compare-at price, badges (-46% / New) → products se
- Count ("48 products") → `collection.products_count`
- Filters + counts → **Search & Discovery** app ke filters se
- Sort dropdown → store ki `sort_options` (Featured / Price / Best selling / Newest)
- Stars → Judge.me ka `judgeme.badge` metafield (app na ho to stars row chhup
  jata hai — jhoothe 5 stars nahi dikhte). Design jaisa 5-star fallback chahiye
  to section setting **"Stars fallback text"** me `Verified` likh dein.

> ⚠️ Collection page par Dawn ke `main-collection-banner` + `main-collection-product-grid`
> hat jayenge — ye jaan-boojh kar hai, design ek hi section maangta hai.

### Step 23 — `templates/collection.json` → REPLACE

Sirf 35 lines. `templates` → `collection.json` → `Ctrl+A` → paste → `Ctrl+S`.

Iske baad **Customize → Collection page** kholein aur **RJ Collection** section
verify karein (Filter, Sort by, Load More labels wahin se badal sakte hain).

### Step 25 — `sections/rj-product.liquid` → **NAYI FILE** ⬅ is round

Product page ka poora layout ek section me: breadcrumb, gallery (88px thumbs +
square stage + "Save 46%" badge), SKU + stock, title, price, **size/variant
buttons**, dispatch line, qty stepper + Add to Cart (+ Shop Pay/UPC dynamic
checkout), wishlist line, 3 policy tiles, accordion (Details = product
description), "Complete the Set" aur **Customer Reviews (Judge.me widget)**,
plus neeche **sticky add bar**.

`sections` → **New file** → naam `rj-product.liquid` → paste → `Ctrl+S`.

Kya asli data se aata hai (hardcoded nahi):
- Title, price, compare-at ("Save 46%"), SKU, stock, images, variants → product se
- Size buttons → product options (har option ka apna group ban jata hai)
- Details tab → **product description**
- Reviews + rating + trust bar → **Judge.me** (`judgeme.widget` / `judgeme.badge`),
  app na ho to sirf editor me hint dikhta hai
- Related products → Shopify recommendations, fallback = section ki collection
- Add to Cart → Dawn ka `product-form` (AJAX + cart drawer), koi custom JS nahi

> ⚠️ Is section ke naam `rj-product.liquid` hai — Step 17/22 wali collection
> files se alag hai.

### Step 26 — `templates/product.json` → REPLACE ⬅ is round

104 lines. `templates` → `product.json` → `Ctrl+A` → paste → `Ctrl+S`.

Ise paste karne ke baad product page par Dawn ka purana `main-product` (vendor,
title, price, variant picker, buy buttons...) **hat jayega** — sab kuch naye
**RJ Product** section se aata hai. Blocks pehle se bhare hain: 3 policy tiles +
4 accordion tabs (Delivery / Return & Cancellation / Care Instructions /
Quality Promise).

### Editable check — kya hardcoded hai aur kya nahi

**Theme editor me sab kuch badal sakte hain** — Collection section me 35 settings:

| Setting | Kya karta hai | Default |
|---|---|---|
| Colour scheme | section ka background/text | scheme-1 cream |
| Hero image + **opacity** | collection image override, 0–60% | collection image, 16% |
| Description override | hero paragraph | collection description |
| Home label / Parent label / Parent link | breadcrumb | Home |
| **Sticky toolbar offset** | header ki height ke hisaab se 0–140px | 82px |
| Products per page | 8–48 (4 ke steps) | 16 |
| **Columns** desktop / mobile | 2–5 / 1–2 | 4 / 2 |
| Show filter drawer | ON/OFF | ON |
| Filter / Count / Sort / Clear all labels | toolbar + chips text | Filter, products, Sort by, Clear all |
| Apply / Clear / Show results | drawer ke buttons | Apply, Clear, Show results |
| **New tag** + **New badge** | kaunsa product tag "New" badge banaye, badge ka text | `New Arrivals` / `New` |
| Stars fallback text | khali = sirf Judge.me stars; bhara = 5★ + text | khali |
| Card button label | hover button | View Product |
| Wishlist page URL | heart ka fallback link | `/pages/wishlist` |
| Empty state | collection khaali ho to | Hinglish line |
| Showing / Load more label | pagination text | Showing / Load More |
| Currency symbol fallback | store ka symbol na mile to | ₹ |

**Jo Shopify khud deta hai (editable par section settings me nahi):** products,
prices, compare-at price, discount %, `products_count`, filters + counts
(Search & Discovery), sort options, pagination numbers, Judge.me stars.

**Jo jaan-boojh kar hardcoded hai (badalne ki zaroorat nahi):**
- Screen-reader labels (`Breadcrumb`, `Close`, `Remove <filter>`, `Add … to wishlist`) — visible text nahi hai
- `−46%` ka minus sign, `1–16 / 48` ka separator, `×` close glyph — typography ka hissa
- Grid/hero spacing — design tokens (`rj-arts.css`)

**Is round me fake data hataya:** `rj-best` aur `rj-showroom` ke placeholder cards
pehle `Bedroom` / `Example best seller` / `₹0` / 5 stars dikhate the — ab sirf
placeholder image + **"Placeholder card note"** setting ka text. Reviews section
ka editor hint bhi ab setting hai (**Editor hint when Judge.me is empty**).

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
Collection na chuni ho to section khaali placeholder cards dikhata hai — koi
fake product/price nahi, sirf ek note: **"Placeholder card note"** setting ka
text (default `Choose a collection for this tab.`).

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

### 3.16 Collection page — 5 cheezein (zaroori)

1. **Collections banayein** — Products → Collections → Create collection
   (Bedroom / Living Room / Dining / New Arrivals / Best Sellers).
   Handle wahi rakhein jo menu me link kiya hai.
2. **Collection image** — har collection me 1 wide image (2000px+). Hero me
   16% opacity par background ki tarah dikhti hai; na daalein to plain cream
   hero rahega (layout nahi tootega).
3. **Description** — collection description hi hero ka paragraph banta hai.
4. **Filters** — Shopify admin → **Apps → Search & Discovery → Filters** →
   Add filter: `Availability`, `Price`, `Product type`, `Vendor`,
   `Size` (variant option), `Finish` (variant option / metafield).
   Finish ko **Swatch** presentation de dein, to drawer me colour dots aayenge.
   Filter add na karein to Filter button + drawer chhup jayenge (page normal chalega).
5. **Sort options** — store ki default list hi use hoti hai; kuch karne ki zaroorat nahi.

### 3.17 Product page — 5 cheezein (zaroori)

1. **Products me images** — pehli image stage par aati hai, baaki thumbnails.
   6–8 square images best lagti hain.
2. **Variants** — Size/Storage options ho to buttons khud ban jate hain; har
   variant ka price/SKU/image badalte hi update ho jata hai.
3. **Compare-at price** — daal dein to "Save 46%" badge aur cut price dikhta hai;
   na ho to badge chhup jata hai.
4. **Dimension (optional)** — Settings → Custom data → Products → metafield
   definition banayein: namespace `custom`, key `dimension`, type **Single line
   text** (e.g. `2.11L x 1.89W x 0.91H Meters`). Product me value bharne par
   stage ke neeche line aati hai; na bharein to line dikhti hi nahi.
5. **Judge.me** — install ke baad reviews + rating + trust bar khud aate hain.
   Tab tak section editor me hint dikhata hai (live site par kuch nahi).

Stock text, SKU label, "Ships in", button labels, accordion tabs, related
heading, sticky bar — sab **RJ Product** section ke settings/blocks se editable.

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
| 7g | Header: search ke right wishlist (heart) icon, click → Wishlist Hero | Header right |
| 7h | Judge.me install ke baad reviews app se aate hain | Sabse neeche |
| 7i | Footer form submit → Customers me subscriber | Footer + admin |
| 8c | Collection page: hero + breadcrumb + description, image 16% opacity | Kisi collection par jayein |
| 8d | Toolbar chipka rehta hai (scroll par header ke neeche) | Collection page scroll |
| 8e | Filter pill → left drawer khulta hai, groups expand/collapse | Collection page |
| 8f | Filter lagane par chip + count badalte hain, "Clear all" sab hata deta hai | Collection page |
| 8g | Sort badalne par order badalta hai (URL me `sort_by`) | Collection page |
| 8h | Card hover: heart + View Product, tag -46% / New | Collection page |
| 8i | "Load More" 16 products ke baad dikhta hai | Collection page bottom |
| 8j | Mobile 360/390: 2-column grid, drawer full-height | Devtools |
| 9a | Product page: thumbs click par stage image badalti hai | Kisi product par |
| 9b | Size button badalne par price/SKU/image/URL (`?variant=`) badalta hai | Product page |
| 9c | Qty +/− chalta hai, Add to Cart cart drawer kholta hai | Product page |
| 9d | Save % badge sirf compare-at price hone par | Product page |
| 9e | Accordion: Details = product description, baaki tabs blocks | Product page |
| 9f | Scroll down par sticky add bar neeche aata hai | Product page |
| 9g | Complete the Set me 4 products (recommendations/collection se) | Product page |
| 9h | Reviews section Judge.me widget dikhata hai (install ke baad) | Product page bottom |
| 9i | Mobile 360/390: gallery single column, thumbs neeche scroll | Devtools |
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
| Wishlist icon par click se kuch nahi hota | app ka Launch Point “As a menu item” nahi hai | Wishlist Hero → Customize Appearance → Launch Point Type |
| Wishlist icon 404 par ja raha | link mode + galat URL | Header → Wishlist app = **Wishlist Hero**, ya URL theek karein |
| Do wishlist icon dikh rahe | app ne apna icon inject kiya | Section 6.3 — ek ko OFF karein (CSS duplicate already hide karta hai) |
| Wishlist count badge nahi aa raha | app count class nahi mili | Header → “Extra CSS classes” me app ki class dalein (e.g. `ssw-wishlist`) |
| Judge.me reviews nahi dikh rahe | app install nahi / carousel off | Section 6.2 steps 1–3 |
| Reviews section purane 4 cards dikha raha | Judge.me carousel khaali | App me reviews publish karein — fallback isi liye hai |
| Newsletter submit par kuch nahi hota | form ka `action` block | `footer.liquid` dobara paste karein (asli customer form hai) |
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

## 6. Apps & integrations (real-time data)

### 6.1 Newsletter → Customers (already wired)
Footer ka form **asli Shopify customer form** hai (`{% form 'customer' %}`,
`contact[tags] = newsletter`). Submit hote hi:
- **Customers** me subscriber ban jata hai (tag `newsletter`),
- success message wahin dikhta hai,
- email marketing consent store ki settings par depend karta hai
  (Settings → Customer accounts / Notifications → **double opt-in** ON ho to
  customer ko confirm email jaata hai, confirm ke baad hi marketing list me).
Agar submit par kuch na ho to check: form ka `<input name="contact[email]">`,
hidden `contact[tags]`, aur button `name="commit"` — teeno footer.liquid me hain.

### 6.2 Judge.me reviews (homepage rail)
1. Shopify App Store se **Judge.me Product Reviews** install karein (free plan kaafi hai).
2. Judge.me app → **Settings → Widgets** me **Reviews Carousel / Featured reviews**
   enable karein (yahi homepage rail ka source hai).
3. Theme editor → **RJ Reviews rail** → **Reviews source** = **Judge.me — Reviews Carousel**.
   (Default isi par set hai.)
4. Judge.me ki apni script/theme integration zaroori nahi — hum official liquid
   snippet use karte hain (`shop.metafields.judgeme.featured_carousel`).
5. App me reviews aane ke baad section apne aap unhe dikhayega. Jab tak reviews
   na hon, section **manual blocks** par fallback karta hai (khaali nahi dikhega),
   aur editor me ek hint dikhta hai.
6. "Read all reviews" link → `all_reviews_url` (design: `/pages/reviews`). Chahein
   to Judge.me ka All-reviews page bana kar wahan point karein.

> Product page ka review widget alag hota hai — wo Group 4 (product template) me
> lagega, tab Judge.me ka Review Widget snippet wahan add hoga.

### 6.3 Wishlist — Wishlist Hero (installed)
App: **Wishlist Hero (Revamp)**. Header icon already in code hai (search ke right),
**mode = Wishlist Hero** set hai — yaani app install karte hi icon click par
wishlist khulni chahiye.

**App me yeh 3 setting check karein:**
1. Wishlist Hero admin → **Customize Appearance** →
   **Launch Point Type = “As a menu item”** → Save.
   (Floating button wahin se off/on hota hai. Agar floating button rakhein to
   icon ke saath dono dikhenge — chaho to floating off kar dein.)
2. **Wishlist page / popup**: app jis page/popup par le jata hai wahi rakhein.
   Agar app khud ka page use karta hai (e.g. `/pages/wishlist` ya `/apps/wishlist`),
   to theme me `Pages → Wishlist` page banane ki zaroorat nahi — app ka URL chalega.
3. **Collections / product cards par heart** (optional): app ke App Embeds me
   “Collections Icon” ON karein — hamare product cards par heart aa jayenge.

**Theme side (already done):**
| Setting (Header → RJ wishlist icon) | Value |
|---|---|
| Show wishlist icon | ON |
| Wishlist app | **Wishlist Hero (#hero-wishlist)** |
| Wishlist page URL | `/pages/wishlist` (sirf link mode ke liye) |
| Extra CSS classes | khaali |

- Icon `href="#hero-wishlist"` par jata hai — yeh Wishlist Hero ka documented
  static launch point hai; unka script click pakad kar wishlist kholta hai.
- Count badge: `<span class="wishlist-hero-header-count">` — app jab count deta
  hai tab dikhta hai, 0 par chhupa rehta hai.

**Duplicate icon ho to:** agar app ne apna icon header me inject kar diya
(`a.wishlist-hero-header-icon` do baar), CSS pehle se hi hamare icon row ka
duplicate hide karta hai. Phir bhi do dikhe to:
- Header → RJ wishlist icon → **Show wishlist icon = OFF** (app ka apna chale), ya
- App ka auto-inject band karein.

**Zaroori warning:** Wishlist Hero install par kai baar theme files me apna code
khud daal deta hai (`header.liquid`, `theme.liquid`). Hum `header.liquid` paste
karte hain, isliye:
1. Paste se pehle **app ka snippet/insert note kar lein** (Edit code me grep:
   `wishlisthero`, `wlh-`, `hero-wishlist`).
2. Paste ke baad check karein icon ek hi hai; agar app ka code hat gaya ho to
   app se **Reinstall theme integration** dobara chala lein — hamara icon phir
   bhi kaam karega (sirf app ka extra code wapas aayega).

**Product page heart** Group 4 (product template) me lagega:
`{% render 'wishlisthero-collection-product' with product: product, buttonMode:'default', buttonClass:'wishlisthero-quick-view' %}`
(ya app ka product-page button auto hi aa jata hai).

---

## 7. Appendix — sirf patch karna ho (optional)

Agar poora `layout/theme.liquid` replace nahi karna chahte, to `manual/` folder me chhote snippets hain:

- `manual/snippet-1-color-scheme-fallback.liquid` (102 lines) → `{% endfor %}` ke baad
- `manual/snippet-2-rj-tokens.liquid` (14 lines) → `{{ 'base.css' ... }}` ke neeche
- body class: `gradient` → `gradient rj-theme`
- `{{ 'rj-arts.css' | asset_url | stylesheet_tag }}` → `</head>` se pehle
- `<script src="{{ 'rj-arts.js' | asset_url }}" defer>` → `global.js` script ke neeche

`config/settings_schema.json` ke liye: `manual/snippet-3-settings-schema-rj-group.json` (81 lines) → aakhri group ke baad comma + `]` se pehle.

---

## 8. Aage

Group 1 (header) ✅ · Group 2 (**10/10** homepage sections) ✅ · Group 3 (footer) ✅ ·
**Group 4 (Collection page) ✅** · **Group 5 (Product page) ✅** · Integrations code ready (app install aapke baad).

Ab bacha:
1. `config/settings_data.json` (Colours panel) — Colours + banner, ek hi baar me
2. ~~Product page~~ ✅ ho gaya (Judge.me widget + wishlist button slot ready)
3. **About page** (design/`About.html`)
4. Content entry: collections, menus, images, products

App install (Judge.me, Wishlist Hero) aap identity verify karne ke baad karenge —
tab tak code graceful fallback par chalta hai (reviews = blocks, wishlist heart =
`#hero-wishlist` / `/pages/wishlist`).
