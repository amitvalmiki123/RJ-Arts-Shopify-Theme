#!/usr/bin/env python3
"""Build products/rj-arts-products.csv from the design HTML.

Source of truth: design/THE-RJ-ARTS.html, design/collection.html, design/product.html
Output:          products/rj-arts-products.csv  (Shopify product import format)
                 products/_extracted.json      (raw scrape, for reference)

Usage:
    python3 tools/build-product-csv.py
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = [
    "design/THE-RJ-ARTS.html",
    "design/collection.html",
    "design/product.html",
]

TYPE_MAP = {
    "Bedroom": "Bedroom",
    "Living": "Living",
    "Dining": "Dining",
    "Lounge": "Living",
    "Crafted": "Living",
    "Single": "Bedroom",
    "Storage": "Bedroom",
}

# same product, different wording in the design
MERGE = {
    "platform cot bed · upholstered headboard": "platform cot bed · cushioned headboard",
    "wood arch bed · sheesham": "wood arch bed · without storage",
    "brass-design home bar cabinet": "regular brass-design home bar cabinet",
}

BEDROOM_STORAGE = {
    "sevilla half-box storage bed",
    "sheesham bedside table",
    "chest of drawers · sheesham",
    "sideboard cabinet",
}

BODY = {
    "Bedroom": """<p><strong>{title}</strong> — solid sheesham wood, handcrafted in Jaipur by RJ Arts.</p>
<ul>
  <li>Solid sheesham (Indian rosewood) frame and legs</li>
  <li>Hand-finished, matte protective lacquer</li>
  <li>Zero-cost EMI available at checkout</li>
  <li>3-year structural warranty</li>
</ul>
<p><strong>Care:</strong> wipe with a dry cloth, avoid direct sunlight and standing water.</p>""",
    "Living": """<p><strong>{title}</strong> — solid sheesham wood with high-density foam, handcrafted in Jaipur by RJ Arts.</p>
<ul>
  <li>Solid sheesham frame, mortise-and-tenon joinery</li>
  <li>High-density foam with fabric upholstery</li>
  <li>Zero-cost EMI available at checkout</li>
  <li>3-year structural warranty</li>
</ul>
<p><strong>Care:</strong> vacuum weekly, blot spills immediately, keep out of direct sunlight.</p>""",
    "Dining": """<p><strong>{title}</strong> — solid sheesham wood, handcrafted in Jaipur by RJ Arts.</p>
<ul>
  <li>Solid sheesham table top and legs, kiln-dried</li>
  <li>Hand-finished, matte protective lacquer</li>
  <li>Zero-cost EMI available at checkout</li>
  <li>3-year structural warranty</li>
</ul>
<p><strong>Care:</strong> use coasters, wipe with a dry cloth, avoid direct sunlight.</p>""",
}

HEADER = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags", "Published",
    "Option1 Name", "Option1 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker",
    "Variant Inventory Qty", "Variant Inventory Policy", "Variant Fulfillment Service",
    "Variant Price", "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable",
    "Variant Barcode", "Image Src", "Image Position", "Image Alt Text", "Gift Card",
    "SEO Title", "SEO Description", "Status",
]

PREFIX = {"Bedroom": "BED", "Living": "LIV", "Dining": "DIN"}


def strip_tags(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()


def grab(pattern: str, block: str) -> str:
    m = re.search(pattern, block, re.S)
    return m.group(1).strip() if m else ""


def cards(path: str) -> list[str]:
    html = (ROOT / path).read_text(encoding="utf-8")
    return re.findall(r'<article class="pcard.*?</article>', html, re.S)


def money(value: str) -> str:
    if not value:
        return ""
    cleaned = value.replace("₹", "").replace(",", "").strip()
    return cleaned if cleaned.isdigit() else ""


def slug(title: str) -> str:
    text = unicodedata.normalize("NFKD", title).replace("·", " ").replace("&", " and ")
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return re.sub(r"-+", "-", text)


def norm_title(text: str) -> str:
    key = re.sub(r"\s+", " ", text).strip().lower()
    return MERGE.get(key, key)


def section_tags() -> dict[str, set[str]]:
    """Tag products by the homepage block they appear in, exactly like the design.

    p-new panel -> New Arrivals, p-best panel + best-sellers grid -> Best Sellers,
    p-her panel -> Heritage.
    """
    html = (ROOT / "design/THE-RJ-ARTS.html").read_text(encoding="utf-8")

    def titles(segment: str) -> list[str]:
        found = re.findall(r'class="pcard__title">(.*?)</h3>', segment, re.S)
        return [norm_title(strip_tags(t)) for t in found]

    def between(start: str, end: str) -> str:
        i = html.index(start)
        j = html.index(end, i + len(start))
        return html[i:j]

    mapping: dict[str, set[str]] = {}

    def add(names: list[str], tag: str) -> None:
        for name in names:
            mapping.setdefault(name, set()).add(tag)

    add(titles(between('id="p-new"', 'id="p-best"')), "New Arrivals")
    add(titles(between('id="p-best"', 'id="p-her"')), "Best Sellers")
    add(titles(between('id="p-her"', "<!-- ===== FEATURE BAND — THE ART OF REST")), "Heritage")
    add(titles(between("BEST SELLERS — ASYMMETRICAL GRID", "CRAFTED COMFORT")), "Best Sellers")

    return mapping


def badge_tags(raw_tags: list[str]) -> set[str]:
    out: set[str] = set()
    for tag in raw_tags:
        low = tag.lower()
        if low == "new":
            out.add("New Arrivals")
        elif low == "heritage":
            out.add("Heritage")
        elif low == "best seller":
            out.add("Best Sellers")
        elif low == "sale" or low.startswith("−") or low.startswith("-"):
            out.add("Sale")
        elif low:
            out.add(tag)
    return out


def scrape() -> list[dict]:
    seen: dict[str, dict] = {}
    order: list[str] = []

    for path in SOURCES:
        for block in cards(path):
            title = strip_tags(grab(r'class="pcard__title">(.*?)</h3>', block))
            if not title:
                continue
            key = re.sub(r"\s+", " ", title).lower()
            key = MERGE.get(key, key)
            record = {
                "title": title,
                "cat": strip_tags(grab(r'class="pcard__cat">(.*?)</span>', block)),
                "price": money(strip_tags(grab(r'class="now">(.*?)</span>', block))),
                "compare": money(strip_tags(grab(r'class="was">(.*?)</span>', block))),
                "img": grab(r'<img src="([^"]+)"', block),
                "raw_tags": [],
            }
            tag = strip_tags(grab(r'class="pcard__tag[^"]*">(.*?)</span>', block))
            if key in seen:
                target = seen[key]
                if tag and tag not in target["raw_tags"]:
                    target["raw_tags"].append(tag)
                if not target["compare"] and record["compare"]:
                    target["compare"] = record["compare"]
                if not target["img"] and record["img"]:
                    target["img"] = record["img"]
                continue
            if tag:
                record["raw_tags"].append(tag)
            seen[key] = record
            order.append(key)

    return [seen[key] for key in order]


def build(products: list[dict]) -> list[dict]:
    rows, used, counters = [], set(), Counter()
    by_section = section_tags()

    for product in products:
        title = product["title"]
        key = re.sub(r"\s+", " ", title).lower()
        key = MERGE.get(key, key)

        if key in BEDROOM_STORAGE:
            ptype = "Bedroom"
        else:
            ptype = TYPE_MAP.get(product["cat"].title(), "Bedroom")

        handle = slug(title)
        if handle in used:
            continue
        used.add(handle)

        counters[ptype] += 1
        price, compare = product["price"], product["compare"]
        if compare and int(compare) <= int(price):
            compare = ""

        tags = badge_tags(product["raw_tags"])
        tags |= by_section.get(key, set())
        tags.add(ptype)
        # a compare-at price is what makes Shopify show the sale badge,
        # so keep the "Sale" tag in sync with it
        tags.add("Sale") if compare else tags.discard("Sale")

        rows.append({
            "Handle": handle,
            "Title": title,
            "Body (HTML)": BODY[ptype].format(title=title),
            "Vendor": "RJ Arts",
            "Product Category": "",
            "Type": ptype,
            "Tags": ", ".join(sorted(tags)),
            "Published": "TRUE",
            "Option1 Name": "Title",
            "Option1 Value": "Default Title",
            "Variant SKU": f"RJ-{PREFIX[ptype]}-{counters[ptype]:03d}",
            "Variant Grams": "",
            "Variant Inventory Tracker": "",
            "Variant Inventory Qty": "",
            "Variant Inventory Policy": "deny",
            "Variant Fulfillment Service": "manual",
            "Variant Price": price,
            "Variant Compare At Price": compare,
            "Variant Requires Shipping": "TRUE",
            "Variant Taxable": "TRUE",
            "Variant Barcode": "",
            "Image Src": product["img"],
            "Image Position": 1,
            "Image Alt Text": title,
            "Gift Card": "FALSE",
            "SEO Title": f"{title} | RJ Arts",
            "SEO Description": (
                f"Buy {title} online — solid sheesham wood, handcrafted in Jaipur "
                "by RJ Arts. Free delivery on solid-wood beds, 0% EMI available."
            ),
            "Status": "active",
        })

    return rows


def main() -> None:
    products = scrape()
    out_dir = ROOT / "products"
    out_dir.mkdir(exist_ok=True)

    (out_dir / "_extracted.json").write_text(
        json.dumps(products, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    rows = build(products)
    with (out_dir / "rj-arts-products.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)

    print(f"scraped {len(products)} card rows -> {len(rows)} unique products")
    print("by type:", dict(Counter(r["Type"] for r in rows)))
    print("with compare-at:", sum(1 for r in rows if r["Variant Compare At Price"]))
    print("with image:", sum(1 for r in rows if r["Image Src"]))
    print("written:", out_dir / "rj-arts-products.csv")


if __name__ == "__main__":
    main()
