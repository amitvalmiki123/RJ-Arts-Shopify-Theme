#!/usr/bin/env python3
"""
Builds preview-collection-01.html — a static replica of the Liquid output of
sections/rj-collection.liquid, using the theme's real rj-arts.css.

Content (products, badges, counts) is copied out of design/collection.html so
the preview and the design can be compared side by side.

Usage:  python3 tools/build-preview-collection.py
"""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# reuse the tokens + header + footer from the home preview builder
spec = importlib.util.spec_from_file_location("home", ROOT / "tools/build-preview-home.py")
home = importlib.util.module_from_spec(spec)
spec.loader.exec_module(home)

css = home.css
TOKENS = home.TOKENS
NAV = home.NAV

usp = home.USP
FOOTER = usp[usp.index('<footer class="rj-footer"'): usp.index("</footer>") + len("</footer>")]

design = (ROOT / "design/collection.html").read_text()

# ---------------------------------------------------------------- cards
cards = []
for block in re.findall(r'<article class="pcard reveal">(.*?)</article>', design, re.S):
    tag = re.search(r'class="pcard__tag">(.*?)<', block).group(1)
    img = re.search(r'<img src="([^"]+)"', block).group(1)
    cat = re.search(r'class="pcard__cat">(.*?)<', block).group(1)
    title = re.search(r'class="pcard__title"><a [^>]*>(.*?)</a>', block).group(1)
    now = re.search(r'class="now">(.*?)<', block).group(1)
    was = re.search(r'class="was">(.*?)<', block)
    stars = re.search(r'<small>(.*?)</small>', block).group(1)
    cards.append(
        dict(tag=tag, img=img, cat=cat, title=title, now=now,
             was=was.group(1) if was else "", stars=stars)
    )

CARD = """
        <article class="rj-pcard rj-pcard--grid rj-reveal is-in">
          <a class="rj-pcard__media rj-pcard__media--link" href="product.html">
            <span class="rj-pcard__tag{tag_class}">{tag}</span>
            <img class="rj-pcard__img" src="{img}" alt="" loading="lazy">
          </a>
          <a class="rj-pcard__wish rj-card-wish" href="#hero-wishlist" aria-label="Add {title} to wishlist">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.5s-7.5-4.6-7.5-9.7A4.3 4.3 0 0 1 12 7.9a4.3 4.3 0 0 1 7.5 2.9c0 5.1-7.5 9.7-7.5 9.7z"/></svg>
          </a>
          <div class="rj-pcard__quick"><button type="button" class="rj-btn rj-btn--light" data-rj-qv-open="{pid}" aria-haspopup="dialog">Quick View</button></div>
          <div class="rj-pcard__body">
            <span class="rj-pcard__cat">{cat}</span>
            <h3 class="rj-pcard__title"><a href="product.html">{title}</a></h3>
            <div class="rj-pcard__price"><span class="now">{now}</span>{was}</div>
            <div class="rj-pcard__stars"><span aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span><small>{stars}</small></div>
          </div>
        </article>"""

GRID = ""
cards_done = []
QV = ""
for c in cards:
    GRID += CARD.format(
        pid=str(1000 + len(cards_done)),
        tag=c["tag"],
        tag_class="" if c["tag"].lower() == "new" else " is-sale",
        img=c["img"],
        cat=c["cat"],
        title=c["title"],
        now=c["now"],
        was=f'<span class="was">{c["was"]}</span>' if c["was"] else "",
        stars=c["stars"],
    )
    pid = str(1000 + len(cards_done))
    cards_done.append(c)
    thumbs = "".join(
        f'<button type="button" class="rj-qv__thumb{" is-active" if i == 0 else ""}" data-rj-qv-thumb data-full="{src}">'
        f'<img class="rj-qv__thumb-img" src="{src}" alt="" loading="lazy"></button>'
        for i, src in enumerate([c["img"], cards[(len(cards_done)) % len(cards)]["img"], cards[(len(cards_done) + 1) % len(cards)]["img"]])
    )
    was_html = f'<span class="was" data-rj-qv-was>{c["was"]}</span>' if c["was"] else '<span class="was" data-rj-qv-was hidden></span>'
    QV += f"""
  <template data-rj-qv-template="{pid}">
    <div class="rj-qv__grid">
      <div class="rj-qv__media">
        <div class="rj-qv__stage"><img class="rj-qv__img" data-rj-qv-stage src="{c['img']}" alt="{c['title']}"></div>
        <div class="rj-qv__thumbs">{thumbs}</div>
      </div>
      <div class="rj-qv__info">
        <span class="rj-qv__cat">{c['cat']}</span>
        <h2 class="rj-qv__title">{c['title']}</h2>
        <div class="rj-qv__price"><span class="now" data-rj-qv-price>{c['now']}</span>{was_html}</div>
        <div class="rj-qv__desc">Solid Sheesham, hand-finished by RJ Arts artisans in Jaipur. Kiln-dried timber, hand-joined frames and a natural polish that deepens with age.</div>
        <product-form class="rj-pform rj-qv__form" data-section-id="qv-{pid}">
          <form class="rj-qv__form-el" data-type="add-to-cart-form" onsubmit="return false">
            <input type="hidden" name="id" class="product-variant-id" value="{pid}">
            <label class="rj-qv__label" for="RjQvVariant-{pid}">Options</label>
            <div class="rj-qv__selectwrap">
              <select id="RjQvVariant-{pid}" class="rj-qv__select" data-rj-qv-variant>
                <option value="{pid}" data-price="{c['now']}" data-compare="{c['was']}" data-available="true" data-image="{c['img']}" selected>King — {c['now']}</option>
                <option value="{pid}2" data-price="{c['now']}" data-compare="{c['was']}" data-available="true" data-image="{c['img']}">Queen — {c['now']}</option>
              </select>
            </div>
            <div class="rj-buyrow rj-qv__buyrow">
              <div class="rj-qty">
                <button type="button" data-rj-qty="-1" aria-label="Decrease">&minus;</button>
                <input type="number" class="rj-qty__input" name="quantity" value="1" min="1" step="1" data-rj-qty-input aria-label="Quantity">
                <button type="button" data-rj-qty="1" aria-label="Increase">+</button>
              </div>
              <button type="submit" name="add" class="rj-btn rj-btn--solid rj-add"><span data-rj-qv-add-text>Add to Cart</span></button>
            </div>
          </form>
        </product-form>
        <div class="rj-qv__links">
          <a class="rj-qv__details" href="product.html">View full details <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg></a>
          <a class="rj-wishline rj-card-wish" href="#hero-wishlist"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.5s-7.5-4.6-7.5-9.7A4.3 4.3 0 0 1 12 7.9a4.3 4.3 0 0 1 7.5 2.9c0 5.1-7.5 9.7-7.5 9.7z"/></svg> Add to Wishlist</a>
        </div>
      </div>
    </div>
  </template>"""

# ---------------------------------------------------------------- filters
CHECK = """
                  <a class="rj-fopt" href="#">
                    <span class="rj-fopt__box{checked}"></span>
                    {label}
                    <span class="rj-fopt__count">{count}</span>
                  </a>"""


def opts(rows):
    out = ""
    for label, count, checked in rows:
        out += CHECK.format(label=label, count=count, checked=" is-checked" if checked else "")
    return out


SWATCHES = """
                <div class="rj-swatches">
                  <a class="rj-sw is-active" href="#" title="Honey (12)" aria-label="Honey"><span class="rj-sw__fill" style="background: rgb(202, 160, 106)"></span></a>
                  <a class="rj-sw" href="#" title="Walnut (9)" aria-label="Walnut"><span class="rj-sw__fill" style="background: rgb(107, 74, 46)"></span></a>
                  <a class="rj-sw" href="#" title="Natural (7)" aria-label="Natural"><span class="rj-sw__fill" style="background: rgb(156, 107, 67)"></span></a>
                  <a class="rj-sw" href="#" title="Teak (4)" aria-label="Teak"><span class="rj-sw__fill" style="background: rgb(74, 53, 32)"></span></a>
                </div>"""

DRAWER_GROUP = """
          <div class="rj-fgroup{open}" data-rj-fgroup>
            <button type="button" class="rj-fgroup__h" aria-expanded="{aria}">
              {label}
              <span class="rj-fgroup__pm" aria-hidden="true"></span>
            </button>
            <div class="rj-fgroup__c">{content}</div>
          </div>"""


def group(label, content, is_open):
    return DRAWER_GROUP.format(label=label, content=content,
                               open=" is-open" if is_open else "",
                               aria="true" if is_open else "false")


PRICE_FORM = """
                  <form class="rj-priceform" method="get" action="#">
                    <label><span>&#8377;</span><input type="number" placeholder="0" min="0"></label>
                    <span class="rj-priceform__dash">&ndash;</span>
                    <label><span>&#8377;</span><input type="number" placeholder="50,000" min="0"></label>
                    <button type="submit" class="rj-btn">Apply</button>
                  </form>"""

GROUPS = (
    group("Size", opts([("King Size", 18, True), ("Queen Size", 15, False),
                        ("Double", 9, False), ("Single", 6, False)]), True)
    + group("Finish", SWATCHES, True)
    + group("Storage", opts([("With Storage", 22, False), ("Without Storage", 26, False)]), False)
    + group("Price", PRICE_FORM, False)
    + group("Availability", opts([("In Stock", 44, False), ("On Sale", 31, False)]), False)
)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ Arts &mdash; Collection page (section preview)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
{TOKENS}
{css}
.color-scheme-3 {{ --color-background: 255, 255, 255; --color-foreground: 33, 28, 23; }}
.page-width {{ margin-inline: auto; width: 100%; }}
.list-menu, .list-unstyled {{ list-style: none; margin: 0; padding: 0; }}
.list-menu--inline {{ display: inline-flex; flex-wrap: wrap; }}
.header__heading {{ margin: 0; line-height: 0; }}
.header__icon {{ position: relative; display: flex; align-items: center; justify-content: center; }}
.header__icon--menu {{ display: none; }}
@media screen and (max-width: 989px) {{
  .header__icon--menu {{ display: flex; }}
  .header__inline-menu {{ display: none; }}
}}
.mega-menu {{ position: static; }}
.mega-menu > summary {{ list-style: none; cursor: pointer; }}
.mega-menu > summary::-webkit-details-marker {{ display: none; }}
.mega-menu__content {{ position: absolute; left: 0; right: 0; top: 100%; z-index: 30; }}
.mega-menu__list {{ display: grid; grid-template-columns: repeat(2, 1fr); }}
.mega-menu:not([open]) .mega-menu__content {{ display: none; }}
.link {{ text-decoration: none; color: inherit; }}
main {{ display: block; }}
</style>
</head>
<body class="rj-theme">

{NAV}
<main>
<div class="rj-col color-scheme-1 gradient">

  <section class="rj-chero">
    <div class="rj-chero__bg"><img class="rj-chero__img" src="Images/Bed.png" alt="RJ Arts beds"></div>
    <div class="rj-wrap rj-chero__in">
      <nav class="rj-crumb" aria-label="Breadcrumb">
        <a href="THE-RJ-ARTS.html">Home</a><span>/</span><span>Beds &amp; Bedroom</span>
      </nav>
      <h1 class="rj-chero__title">Beds &amp; Bedroom</h1>
      <div class="rj-chero__desc"><p>Solid Sheesham beds &mdash; hand-finished, storage-smart and built to be handed down. From low-profile platforms to brass-work heritage headboards.</p></div>
    </div>
  </section>

  <div class="rj-toolbar">
    <div class="rj-wrap rj-toolbar__in">
      <div class="rj-toolbar__left">
        <button type="button" class="rj-filterbtn" data-rj-open-filter>
          <svg viewBox="0 0 24 24" aria-hidden="true"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/><circle cx="9" cy="7" r="2"/><circle cx="15" cy="12" r="2"/><circle cx="8" cy="17" r="2"/></svg>
          Filter (2)
        </button>
        <span class="rj-tbcount"><b>48</b> products</span>
      </div>
      <div class="rj-toolbar__right">
        <label for="RjSort">Sort by</label>
        <div class="rj-select">
          <select id="RjSort" data-rj-sort>
            <option value="manual">Featured</option>
            <option value="price-ascending">Price, low to high</option>
            <option value="price-descending">Price, high to low</option>
            <option value="best-selling">Best selling</option>
            <option value="created-descending">Date, new to old</option>
          </select>
        </div>
      </div>
    </div>
  </div>

  <div class="rj-wrap">
    <div class="rj-chips">
      <span class="rj-chip">King Size<a href="#" aria-label="Remove King Size">&times;</a></span>
      <span class="rj-chip">Honey Finish<a href="#" aria-label="Remove Honey Finish">&times;</a></span>
      <a class="rj-chips__clear" href="#">Clear all</a>
    </div>
  </div>

  <div class="rj-wrap">
    <div class="rj-cgrid">{GRID}</div>
    {QV}

    <div class="rj-loadmore">
      <small>Showing 1&ndash;16 / 48</small>
      <div class="rj-loadmore__bar"><i style="width: 33%"></i></div>
      <a class="rj-btn rj-btn--solid" href="#">Load More</a>
    </div>
  </div>

  <div class="rj-qv" data-rj-qv hidden>
    <div class="rj-qv__overlay" data-rj-qv-close></div>
    <div class="rj-qv__dialog" role="dialog" aria-modal="true" aria-label="Quick view">
      <button type="button" class="rj-qv__x" data-rj-qv-close aria-label="Close"><span aria-hidden="true">&times;</span></button>
      <div class="rj-qv__content" data-rj-qv-content></div>
    </div>
  </div>

  <div class="rj-foverlay" data-rj-filter-overlay hidden></div>
  <aside class="rj-fdrawer" data-rj-filter-drawer aria-labelledby="RjFilterTitle" hidden>
    <div class="rj-fdrawer__head">
      <h3 id="RjFilterTitle">Filter</h3>
      <button type="button" data-rj-close-filter aria-label="Close">&times;</button>
    </div>
    <div class="rj-fdrawer__body">{GROUPS}</div>
    <div class="rj-fdrawer__foot">
      <a class="rj-btn" href="#">Clear</a>
      <button type="button" class="rj-btn rj-btn--solid" data-rj-close-filter>Show results</button>
    </div>
  </aside>
</div>
</main>

{FOOTER}

<script>
<!--RJ_JS-->
</script>
</body>
</html>
"""

js = (ROOT / "theme_export/assets/rj-arts.js").read_text()
html = PAGE.format(TOKENS=TOKENS, css=css, NAV=NAV, FOOTER=FOOTER, GRID=GRID, QV=QV, GROUPS=GROUPS)
html = html.replace("<!--RJ_JS-->", js)
(ROOT / "preview-collection-01.html").write_text(html)
print("wrote preview-collection-01.html", len(html), "bytes,", len(cards), "cards")
