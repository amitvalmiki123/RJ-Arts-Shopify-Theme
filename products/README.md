# RJ Arts — Product CSV (import ke liye)

`rj-arts-products.csv` — design files se nikale gaye **26 products**, Shopify ke official product-import format me.

| File | Kya hai |
|---|---|
| `rj-arts-products.csv` | Shopify me import karne wali file (26 products) |
| `_extracted.json` | design HTML se nikala gaya raw data (reference) |

## Kahan se aaya

Source: `design/THE-RJ-ARTS.html` (25 cards), `design/collection.html` (9 cards), `design/product.html` (4 related cards) → duplicate hata ke **26 unique products**.

Duplicate merge (ek hi product, do naam):
- `Platform Cot Bed · Upholstered Headboard` + `Platform Cot Bed · Cushioned Headboard` → ek product
- `Wood Arch Bed · Sheesham` + `Wood Arch Bed · Without Storage` → ek
- `Brass-Design Home Bar Cabinet` + `Regular Brass-Design Home Bar Cabinet` → ek

## Import kaise karein

1. Shopify admin → **Products** → **Import**
2. `rj-arts-products.csv` upload karein
3. Preview me 26 rows dikhengi → **Import products**
4. 2–5 minute lagenge (images Shopify apne CDN par copy karta hai)

Import ke baad check:
- 26 products, 3 types (Bedroom 14 / Dining 6 / Living 6)
- 14 products par **compare-at price** (sale badge dikhega)
- Sab par image (URL se aayegi — design ki original RJ Arts CDN images)
- Prices design se liye gaye hain, import ke baad ek baar verify kar lein

Tags design ke **exact blocks** se liye gaye hain (guess nahi):

| Tag | Kitne products | Source |
|---|---|---|
| New Arrivals | 5 | homepage tab 1 (`#p-new`) |
| Best Sellers | 6 | tab 2 (`#p-best`) + Best-sellers grid |
| Heritage | 5 | tab 3 (`#p-her`) |
| Sale | 14 | jinke compare-at price hai |
| Bedroom / Living / Dining | 14 / 6 / 6 | product card category |

## Collections (import ke baad, 2 minute)

CSV collections nahi bana sakta, lekin har product par **Tags** hain — automatic collections bana lein:

**Products → Collections → Create collection → condition: Product tag equals …**

| Collection | Condition | Homepage me kahan use hoga |
|---|---|---|
| Bedroom | tag = `Bedroom` | Category tiles, mega menu |
| Living | tag = `Living` | Category tiles, mega menu |
| Dining | tag = `Dining` | Category tiles, mega menu |
| New Arrivals | tag = `New Arrivals` | Tabbed slider (tab 1) |
| Best Sellers | tag = `Best Sellers` | Tabbed slider (tab 2), Best sellers grid |
| Heritage | tag = `Heritage` | Tabbed slider (tab 3) |
| Sale | tag = `Sale` | Best sellers / badges |
| Sevilla, Crew, Simons, Scott, Arvyn, Bar | tag = same | Collection carousel (#9) |

> Sab collections ko **automatic** rakhein (condition based) — naye products apne aap add ho jayenge.

## CSV columns

Shopify standard:

```
Handle, Title, Body (HTML), Vendor, Product Category, Type, Tags, Published,
Option1 Name, Option1 Value, Variant SKU, Variant Grams, Variant Inventory Tracker,
Variant Inventory Qty, Variant Inventory Policy, Variant Fulfillment Service,
Variant Price, Variant Compare At Price, Variant Requires Shipping, Variant Taxable,
Variant Barcode, Image Src, Image Position, Image Alt Text, Gift Card,
SEO Title, SEO Description, Status
```

Details:
- **SKU**: `RJ-BED-001`, `RJ-LIV-001`, `RJ-DIN-001` …
- **Vendor**: RJ Arts · **Type**: Bedroom / Living / Dining · **Status**: active
- **Option1 = Title / Default Title** (single variant per product)
- **Body (HTML)**: category ke hisaab se description template (solid sheesham, 3-year warranty, care line) — apne hisaab se edit kar sakte hain
- **Inventory**: policy `deny`, tracker khaali (stock baad me daal dein)

## Kya baad me khud bharna hoga

| Cheez | Kyun |
|---|---|
| Stock quantity | design me nahi thi |
| Weight (grams) | shipping rates ke liye |
| HSN / GST | India ke liye |
| Barcode | — |
| Product Category (Shopify taxonomy) | optional, SEO ke liye accha |

## Dobara generate karna ho

```bash
python3 tools/build-product-csv.py      # (design HTML badle to)
```
