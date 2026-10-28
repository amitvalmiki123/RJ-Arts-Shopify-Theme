# RJ Arts — Manual Setup Guide (Dawn duplicate me paste karke)

Ye guide us case ke liye hai jab aap **zip upload nahi** karna chahte, balki **Dawn ko duplicate** karke usme code **haath se paste** karna chahte hain.

Har step ke saath file ka GitHub link hai. Link khulein → top-right **`Copy raw file`** button dabayein → Shopify code editor me paste karein → **Save**.

> Total kaam: **4 nayi files** + **7 files replace** + **2 files me chhota patch**. Bas.
> (RJ ka poora CSS/JS alag files me hai — Dawn ki `base.css` / `global.js` ko chhuna nahi padta.)

---

## 0. Taiyari (5 minute)

1. Shopify admin → **Online Store → Themes**.
2. Jis **Dawn 16.1.0** theme par kaam karna hai (jo aapne download/upload kiya tha) uske `⋯` menu → **Duplicate**.
3. Duplicate theme ke `⋯` → **Edit code** khol lein. **Isi** duplicate me sab kaam hoga — apni live theme ko na chhuein.
4. Ek baar duplicate ko **Customize → Save** kar dein (isse `config/settings_data.json` ban jata hai).
5. Code editor me left side **Explorer** dikhega: `assets / config / layout / locales / sections / snippets / templates`.

**Tip:** har file paste karne ke baad `Ctrl+S` (Save) dabayein. Agar Liquid/JSON galat hoga to Shopify wahin error dikha dega — us step ko dobara karein.

---

## 1. Ek nazar me — kya kya badalna hai

| # | File | Kya karna hai | Kitni lines |
|---|------|---------------|-------------|
| 1 | `config/settings_schema.json` | ek group **add** (patch) | +81 |
| 2 | `config/settings_data.json` | **replace** pura file | 386 |
| 3 | `layout/theme.liquid` | **5 chhote patch** (3 block + 2 line) | +110 |
| 4 | `assets/rj-arts.css` | **nayi file** (RJ ka poora CSS) | 1159 |
| 5 | `assets/rj-arts.js` | **nayi file** (RJ ka poora JS) | 64 |
| 6 | `sections/announcement-bar.liquid` | **replace** | 180 |
| 7 | `sections/header.liquid` | **replace** | 721 |
| 8 | `snippets/header-mega-menu.liquid` | **replace** | 135 |
| 9 | `sections/header-group.json` | **replace** | 145 |
| 10 | `sections/rj-hero.liquid` | **nayi file** | 411 |
| 11 | `sections/rj-usp.liquid` | **nayi file** | 145 |
| 12 | `sections/footer-group.json` | **replace** | 61 |
| 13 | `templates/index.json` | **replace** | 108 |

Baaki 340+ Dawn files **bilkul chhoti nahi** — unhe haath nahi lagana.

> Sab links is branch ke hain:
> `https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/`
> (ya wahi file `rj-arts-theme.zip` ke andar bhi mil jayegi)

---

## 2. Step-by-step (isi order me karein — order matter karta hai)

### Step 1 — `config/settings_schema.json` (RJ brand tokens group add)

**Kyun:** Settings me "RJ Arts - brand tokens" panel aata hai (accent, hairline, container width, etc.).

1. `config/settings_schema.json` kholein.
2. File ke **bilkul end** me aakhri group ke baad ek comma lagayein aur closing `]` se pehle ye group paste karein.

Aakhri 3 lines aisi dikhni chahiye (pehle → baad me):

```json
// PEHLE
    }
  }
]
```

```json
// BAAD ME
    }
  },
  {  ← yahan snippet paste hoga
  }
]
```

**Paste karne ke liye:** [manual/snippet-3-settings-schema-rj-group.json](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/manual/snippet-3-settings-schema-rj-group.json) (81 lines)

**Save** → Customize → Theme settings me neeche **"RJ Arts - brand tokens"** panel dikhna chahiye.

---

### Step 2 — `config/settings_data.json` (pura replace)

**Kyun:** ye file theme ki saari settings rakhti hai — **5 colour schemes**, fonts, page width, cart = drawer, RJ tokens. **Yahi wo file hai jiske miss hone se "No color schemes defined" error aata hai.**

1. `config/settings_data.json` kholein (ek hi line me minified JSON dikhega).
2. `Ctrl+A` → delete → poora naya content paste karein.

**Paste:** [theme_export/config/settings_data.json](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/config/settings_data.json) (386 lines)

**Save** → Customize kholein → banner ("color schemes must be defined") **nahi** dikhna chahiye, aur Colours tab me 5 schemes dikhni chahiye.

> Agar aapki duplicate Dawn me file hi na dikhe (kabhi-kabhi explorer glitch karta hai): Customize me ek chhota change karke **Save** daba dein — file khud ban jayegi, phir paste karein.

---

### Step 3 — `layout/theme.liquid` (5 chhote patch — pura file replace NA karein)

Isme sirf 5 jagah change hai: 3 blocks + 2 single lines. Link: [theme_export/layout/theme.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/layout/theme.liquid)

#### Patch 3a — colour-scheme fallback (safety net)

`theme.liquid` me kareeb **line 119** — dawn ka scheme loop aise khatam hota hai:

```liquid
      }
      {% endfor %}          ← iske THIK BAAD paste karein

      {{ scheme_classes | prepend: 'body' }} {
```

`{% endfor %}` ke baad (blank line se pehle) ye block paste karein:

**Paste:** [manual/snippet-1-color-scheme-fallback.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/manual/snippet-1-color-scheme-fallback.liquid) (89 lines)

**Kaam kya karta hai:** agar kabhi theme ki settings me colour schemes na hon, to theme khud design ke 5 colours print kar deti hai → site kabhi "white/bina colour" nahi dikhegi.

#### Patch 3b — RJ design tokens

`theme.liquid` me ye line dhundein (kareeb line 371 — `Ctrl+F` me search karein):

```liquid
    {{ 'base.css' | asset_url | stylesheet_tag }}
```

Iske **thik neeche** ye block paste karein:

**Paste:** [manual/snippet-2-rj-tokens.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/manual/snippet-2-rj-tokens.liquid) (14 lines)

#### Patch 3c — body class

Line ~432 par (ya `Ctrl+F` → `<body class`):

```liquid
<body class="gradient{% if ... %}">          ← PEHLE
<body class="gradient rj-theme{% if ... %}">  ← BAAD ME
```

Bas `rj-theme` word add karna hai (RJ ka poora CSS isi class ke andar band hai, isliye Dawn ka baaki design kharab nahi hota).

#### Patch 3d — RJ CSS load karna

`theme.liquid` ke **`<head>` ke sabse end** me, `</head>` se thik pehle ye 2 lines daalein:

```liquid
    {%- comment -%} RJ ARTS — design system (keep last in <head> so it wins the cascade) {%- endcomment -%}
    {{ 'rj-arts.css' | asset_url | stylesheet_tag }}

  </head>
```

(`</head>` pehle se hai — uske thik upar 2 lines add karni hain. Ye `<head>` ka last stylesheet hona chahiye taki Dawn ke baad load ho.)

#### Patch 3e — RJ JS load karna

`theme.liquid` me ye line dhundein (kareeb line 54):

```liquid
    <script src="{{ 'global.js' | asset_url }}" defer="defer"></script>
```

Iske **thik neeche**:

```liquid
    <script src="{{ 'rj-arts.js' | asset_url }}" defer="defer"></script>
```

**Save.**

---

### Step 4 — `assets/rj-arts.css` (**nayi file**)

**Kyun:** RJ Arts ka poora design-system CSS (1159 lines) — tokens, header, ticker, hero, USP, buttons, mobile. Dawn ki `base.css` ko **bilkul chhedna nahi** hai.

1. Explorer me **`assets`** folder par right-click → **New file** (ya `Ctrl+Shift+P` → `New File`)
2. Naam: `rj-arts.css`
3. Paste karein → Save.

**Paste:** [theme_export/assets/rj-arts.css](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/assets/rj-arts.css) (1159 lines, 27 KB)

Pehli line yahi honi chahiye:

```css
/* ==========================================================================
   RJ ARTS — appended design-system block (do not reformat)
```

**Save** → preview kholein: header/nav ab Cormorant + Jost me dikhna chahiye.

---

### Step 5 — `assets/rj-arts.js` (**nayi file**)

**Kyun:** scroll-reveal animation + header ka "scrolled" state (border/shadow jab page scroll ho).

Wahi tarika: `assets` folder → New file → naam `rj-arts.js` → paste → Save.

**Paste:** [theme_export/assets/rj-arts.js](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/assets/rj-arts.js) (64 lines)

Pehli line:

```js
/* ==========================================================================
   RJ ARTS — appended helpers (scroll reveal + header scrolled state)
```

**Save.**

---

### Step 6 — `sections/announcement-bar.liquid` (replace)

**Kyun:** design ka **chalti hui ticker** (marquee) announcement bar, brass highlights ke saath.

`Ctrl+A` → paste → Save.
**Paste:** [theme_export/sections/announcement-bar.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/sections/announcement-bar.liquid) (180 lines)

---

### Step 7 — `sections/header.liquid` (replace)

**Kyun:** header ke schema me mega-menu feature cards (image + label) wala block type add hota hai (`max_blocks: 9`).

`Ctrl+A` → paste → Save.
**Paste:** [theme_export/sections/header.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/sections/header.liquid) (721 lines)

> ⚠️ **Step 7 pehle, Step 9 baad me.** Header-group.json me `mega_feature` blocks hain — agar schema pehle nahi hai to JSON save par error aayega.

---

### Step 8 — `snippets/header-mega-menu.liquid` (replace)

**Kyun:** mega menu ke andar 2-column feature cards + hover zoom.

`Ctrl+A` → paste → Save.
**Paste:** [theme_export/snippets/header-mega-menu.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/snippets/header-mega-menu.liquid) (135 lines)

---

### Step 9 — `sections/header-group.json` (replace)

**Kyun:** announcement bar ke 5 messages + 6 mega feature cards + header settings (logo middle-left, menu, sticky always, scheme-1, padding 0).

`Ctrl+A` → paste → Save.
**Paste:** [theme_export/sections/header-group.json](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/sections/header-group.json) (145 lines)

**Save ke baad** Customize → Header section me: 5 announcement blocks aur 6 feature cards dikhne chahiye.

---

### Step 10 — `sections/rj-hero.liquid` (**nayi file**)

**Kyun:** homepage ka hero slider (3 slides, arrows, dots, auto-rotate). Ye koi Dawn file nahi — nayi section hai.

1. Explorer me **`sections`** folder par right-click → **New file**
   (ya `Ctrl+Shift+P` → `New File`)
2. Naam: `rj-hero.liquid`
3. Paste karein → Save.

**Paste:** [theme_export/sections/rj-hero.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/sections/rj-hero.liquid) (411 lines)

---

### Step 11 — `sections/rj-usp.liquid` (**nayi file**)

**Kyun:** hero ke neeche 4-item USP strip (1,000+ reviews / solid sheesham / 3-year warranty / 0% finance).

Wahi tarika: `sections` folder → New file → naam `rj-usp.liquid` → paste → Save.

**Paste:** [theme_export/sections/rj-usp.liquid](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/sections/rj-usp.liquid) (145 lines)

---

### Step 12 — `sections/footer-group.json` (replace)

**Kyun:** footer me 4 columns (brand + Shop + Company + Support) set ho jate hain.

`Ctrl+A` → paste → Save.
**Paste:** [theme_export/sections/footer-group.json](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/sections/footer-group.json) (61 lines)

---

### Step 13 — `templates/index.json` (replace)

**Kyun:** homepage ka template — abhi hero + USP hi hai (Group 2 ke baaki sections next turns me add honge).

`Ctrl+A` → paste → Save.
**Paste:** [theme_export/templates/index.json](https://github.com/amitvalmiki123/RJ-Arts-Shopify-Theme/blob/arena/b22b7858-rj-arts-shopify-theme/theme_export/templates/index.json) (108 lines)

> ⚠️ Steps 10–11 pehle hone chahiye, warna Shopify `rj_hero` / `rj_usp` section na milne par error dega.

---

## 3. Data jo manually set karna hai (code nahi, editor me)

Code paste karne ke baad **Customize** me ye cheezein set karni hain. Settings ka **bada hissa Step 2 ki JSON se already aa jayega** — neeche sirf wahi hai jo JSON me nahi aa sakta (images, menus) + verify list.

### 3.1 Logo
- **Theme settings → Logo** → `Images/logo.png` upload karein (1000×218 px).
  Zip/repo me: `Images/logo.png`
- **Logo width** = `120 px` (JSON se aa jayega, check kar lein).
- Logo na daalne par header me text "RJ ARTS" dikhta hai (fallback).

### 3.2 Colours (verify — Step 2 ke baad apne aap set honge)
Theme settings → **Colours** → 5 schemes:

| Scheme | Background | Text | Button | Button label | Shadow |
|--------|-----------|------|--------|--------------|--------|
| Scheme 1 (cream) | `#F7F4EF` | `#211C17` | `#211C17` | `#F7F4EF` | `#211C17` |
| Scheme 2 (cream 2) | `#EFE9E1` | `#211C17` | `#211C17` | `#EFE9E1` | `#211C17` |
| Scheme 3 (white) | `#FFFFFF` | `#211C17` | `#211C17` | `#FFFFFF` | `#211C17` |
| Scheme 4 (ink) | `#211C17` | `#F7F4EF` | `#F7F4EF` | `#211C17` | `#211C17` |
| Scheme 5 (brass) | `#A9865B` | `#211C17` | `#211C17` | `#A9865B` | `#211C17` |

`secondary_button_label` = text colour (har scheme me).

### 3.3 Typography
- Heading = **Cormorant Garamond** (weight 400)
- Body = **Jost** (weight 400)
- Heading scale = 100, Body scale = 100

### 3.4 Layout / Buttons / Cart
- Page width = **1600 px**
- Buttons → corner radius = **2**, border thickness = **1**
- Cart type = **Drawer**
- Animations → hover effects = **None**, reveal on scroll = **On**
- Spacing → sections = **0**

### 3.5 Navigation (zaroori — mega menu isi par depend karta hai)
**Online Store → Navigation → Main menu** me ye structure banayein:

```
Bedroom      → children: King Size Beds, Bedroom Storage, Bedside Tables
Living       → children: Sofas, Coffee Tables, Living Storage
Dining       → children: Dining Tables, Dining Chairs, Sideboards
New Arrivals (no children)
Best Sellers (no children)
```

⚠️ **Children links ke bina mega panel kabhi nahi khulega.** Header ka hover-menu sirf tab kaam karta hai jab parent ke andar kam se kam 1 link ho.

### 3.6 Hero slider (rj-hero section)
Customize → **Hero slider** → 3 slides. Har slide me:
- Image (desktop) + Image (mobile)
- Eyebrow (e.g. `LIVING · CRAFTED COMFORT`)
- Heading (e.g. `Comfort, carved from wood.`)
- Text + 2 buttons (label + link)

Images: `Images/` folder se (`Bed_Desktop_Banner.webp`, `Dining_Desktop_Banner.webp`, `Living_Room_Img.webp` etc.).

### 3.7 USP strip (rj-usp section)
Customize → **USP strip** → 4 blocks: icon + heading + subtext.
Default copy: `1,000+ 5-Star Reviews` / `100% Solid Sheesham` / `3-Year Warranty` / `0% Finance Available`.

### 3.8 Mega feature cards (6)
Customize → **Header** section → `mega_feature` blocks (6). Har block me:
- **Parent link** = menu ka **exact** naam (`Bedroom` / `Living` / `Dining`) — spelling/space same hona chahiye
- Image (3:4 ratio best), Label, Link

Labels/aapke paas images: `Images/Bed.png`, `Bed2.png`, `Living.jpg`, `Dining.png` etc.

---

## 4. Final check (5 minute)

| # | Check | Kahan |
|---|-------|-------|
| 1 | Colours tab me 5 schemes | Customize → Theme settings → Colours |
| 2 | "color schemes must be defined" banner **gaya** | Customize ke top par |
| 3 | Ticker **dark ink** background, cream text, chal raha hai | Homepage top |
| 4 | Header **cream** (#F7F4EF), nav 13px uppercase letter-spaced | Homepage |
| 5 | Icons: 1 magnifier + account + bag (bag ke saath 17px count circle) | Header right |
| 6 | Hover `Bedroom` → mega panel khulta hai + 2 image cards | Homepage |
| 7 | Hero slider: 3 slides, arrows + dots, auto-rotate | Homepage |
| 8 | USP strip: 4 items, brass icons | Hero ke neeche |
| 9 | Footer: brand + Shop + Company + Support columns | Page bottom |
| 10 | Mobile 390px: hamburger drawer, ticker, hero 1 column | Devtools |

---

## 5. Agar kuch galat ho

| Error / symptom | Karan | Fix |
|---|---|---|
| `To preview your changes, color schemes must be defined…` | Step 2 paste nahi hua, ya editor cache | `settings_data.json` dobara paste → Save → Customize reload |
| `Scheme "mega_feature" does not exist` (ya header-group save error) | Step 7 se pehle Step 9 kar diya | `header.liquid` paste karein, phir `header-group.json` |
| `Section type 'rj_hero' does not exist` | Steps 10–11 pending | `rj-hero.liquid` + `rj-usp.liquid` banao, phir `index.json` paste |
| Header ke saare colours white/grey, design jaisa nahi | `rj-arts.css` file nahi bani ya theme.liquid me link nahi laga | Step 3d + Step 4 check karein |
| Scroll karne par header border/shadow nahi aata | `rj-arts.js` link missing | Step 3e + Step 5 |
| Fonts default lag rahe hain | Step 2 nahi hua | settings_data paste → Customize me Typography check |
| Mega menu hover par kuch nahi khulta | Menu me children nahi hain | Section 3.5 follow karein |
| Kabhi bhi kuch bigad jaye | — | Duplicate theme delete karein → naya duplicate → 13 steps dobara (25 min) |

---

## 6. Aage ka kaam

Ye setup = **Group 1 (header)** complete + homepage ke pehle 2 sections (hero, USP).

Group 2 ke baaki sections (design order me) ek-ek karke aayenge:
3. Category tiles → 4. The showroom edit (tabbed slider) → 5. The Art of Rest → 6. About → 7. Best sellers grid → 8. Crafted Comfort → 9. Collection carousel → 10. Reviews rail
Fir **Group 3 — Footer**.

Har section ke liye 2-3 file steps milenge: nayi `sections/rj-*.liquid` + `templates/index.json` me ek block + (agar CSS ho to) base.css ke end me ek block.
