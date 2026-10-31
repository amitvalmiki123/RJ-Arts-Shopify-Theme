#!/usr/bin/env python3
"""
Builds preview-product-01.html — a static replica of the Liquid output of
sections/rj-product.liquid, using the theme's real rj-arts.css + rj-arts.js.

Sample product data (title, prices, gallery) is copied from design/product.html
so the preview can be compared with the design. Reviews / trust bar stay empty,
exactly like a live store without Judge.me installed.

Usage:  python3 tools/build-preview-product.py
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("home", ROOT / "tools/build-preview-home.py")
home = importlib.util.module_from_spec(spec)
spec.loader.exec_module(home)

css = home.css
TOKENS = home.TOKENS
NAV = home.NAV

usp = home.USP
FOOTER = usp[usp.index('<footer class="rj-footer"'): usp.index("</footer>") + len("</footer>")]

THUMBS = [
    "81dP0WMJ1zL._SL1500.jpg",
    "61V6A_vqILL._SL1500.jpg",
    "617kVRk4kgL._SL1500.jpg",
    "619Po-ovFZL._SL1500.jpg",
    "51sAvLWD43L._SL1500.jpg",
    "51szxPQ3ERL._SL1500.jpg",
]
CDN = "https://cdn.shopify.com/s/files/1/0675/3042/4451/files/"

THUMB_HTML = ""
for index, image in enumerate(THUMBS):
    THUMB_HTML += f"""
              <button type="button" class="rj-thumb{' is-active' if index == 0 else ''}" data-rj-thumb data-media-id="{index}" data-full="{CDN}{image}?width=1400" aria-label="Image {index + 1}">
                <img class="rj-thumb__img" src="{CDN}{image}?width=200" alt="" loading="lazy">
              </button>"""

RELATED = [
    ("Rjart_Sheesham_Regular_Brass_Design_Home_Bar_Cabinet.png", "Storage", "Sheesham Bedside Table", "₹8,499", "₹13,998", True),
    ("81Qr_Z7CWZL._SL1500.jpg", "Storage", "Chest of Drawers · Sheesham", "₹19,999", "₹32,000", True),
    ("Rjart_Nirvana_Sheesham_Single_Seater_Sofa.png", "Living", "Nirvana Accent Chair", "₹15,622", "", False),
    ("71pdtMlrqpL._SL1500.jpg", "Bedroom", "Sideboard Cabinet", "₹24,499", "₹39,000", True),
]
RELATED_HTML = ""
for image, cat, title, now, was, has_was in RELATED:
    src = image if image.startswith("http") else "https://therjart.com/cdn/shop/files/" + image
    if not image.startswith("http") and image.endswith((".jpg", ".png")):
        src = "https://therjart.com/cdn/shop/files/" + image
    if image.startswith("81") or image.startswith("71"):
        src = CDN + image + "?width=700"
    RELATED_HTML += f"""
            <article class="rj-pcard rj-pcard--grid rj-reveal is-in">
              <a class="rj-pcard__media rj-pcard__media--link" href="#">
                <img class="rj-pcard__img" src="{src}" alt="" loading="lazy">
              </a>
              <div class="rj-pcard__body">
                <span class="rj-pcard__cat">{cat}</span>
                <h3 class="rj-pcard__title"><a href="#">{title}</a></h3>
                <div class="rj-pcard__price"><span class="now">{now}</span>{f'<span class="was">{was}</span>' if has_was else ''}</div>
              </div>
            </article>"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ Arts &mdash; Product page (section preview)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
{TOKENS}
{css}
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
.rj-add {{ border: 1px solid var(--rj-ink); background: var(--rj-ink); color: var(--rj-cream); }}
</style>
</head>
<body class="rj-theme">

{NAV}
<main>
<div class="rj-product color-scheme-1 gradient" data-rj-product data-label-add="Add to Cart" data-label-sold-out="Sold out" data-label-in-stock="In Stock">

  <div class="rj-wrap">

    <nav class="rj-crumb rj-crumb--pdp" aria-label="Breadcrumb">
      <a href="THE-RJ-ARTS.html">Home</a><span>/</span><a href="collection.html">Beds &amp; Bedroom</a><span>/</span><span>Platform Cot Bed</span>
    </nav>

    <div class="rj-pdp">

      <div class="rj-gal">
        <div class="rj-thumbs">{THUMBS}</div>
        <div class="rj-stage">
          <span class="rj-stage__badge" data-rj-badge>Save 46%</span>
          <img class="rj-stage__img" data-rj-stage src="{CDN}81dP0WMJ1zL._SL1500.jpg?width=1400" alt="Platform Cot Bed">
          <span class="rj-stage__zoom">Hover to zoom</span>
        </div>
      </div>

      <div class="rj-pinfo">

        <div class="rj-skurow">
          <span class="rj-sku">SKU: <span data-rj-sku>RJWBK001</span></span>
          <span class="rj-stock" data-rj-stock><i aria-hidden="true"></i><span data-rj-stock-text>In Stock</span></span>
        </div>

        <h1 class="rj-pinfo__title">Wood Bed For Bedroom | Platform Cot Bed With Upholstered Cushioned Headboard | Sheesham Solid Wood</h1>

        <div class="rj-price">
          <span class="rj-price__now" data-rj-price>₹15,566</span>
          <span class="rj-price__was" data-rj-was>₹28,798</span>
        </div>

        <div class="rj-options" data-rj-options>
          <div class="rj-opt" data-rj-opt-group="1">
            <div class="rj-opt__label">Size: <span data-rj-opt-name="1">King</span></div>
            <div class="rj-sizes">
              <button type="button" class="rj-size is-active" data-rj-opt-value="King" data-option-position="1" aria-pressed="true"><b>King</b></button>
              <button type="button" class="rj-size" data-rj-opt-value="Queen" data-option-position="1" aria-pressed="false"><b>Queen</b></button>
            </div>
          </div>
        </div>

        <div class="rj-metaline">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="5" width="14" height="11" rx="1"/><path d="M15 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.2"/><circle cx="18.5" cy="18.5" r="2.2"/></svg>
          Ships in: <b>7-10 Days</b>
        </div>

        <div class="rj-divider"></div>

        <product-form class="rj-pform" data-section-id="preview">
          <div class="product-form__error-message-wrapper rj-pform__error" role="alert" hidden>
            <span class="product-form__error-message rj-pform__error-text"></span>
          </div>
          <form class="rj-pform__form" data-type="add-to-cart-form" onsubmit="return false">
            <div class="rj-buyrow">
              <div class="rj-qty">
                <button type="button" data-rj-qty="-1" aria-label="Decrease">&minus;</button>
                <input type="number" class="rj-qty__input" name="quantity" value="1" min="1" step="1" data-rj-qty-input aria-label="Quantity">
                <button type="button" data-rj-qty="1" aria-label="Increase">+</button>
              </div>
              <button type="submit" name="add" class="rj-btn rj-btn--solid rj-add" data-rj-add>
                <span data-rj-add-text>Add to Cart</span>
              </button>
            </div>
          </form>
        </product-form>

        <a class="rj-wishline rj-card-wish" href="#hero-wishlist">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.5s-7.5-4.6-7.5-9.7A4.3 4.3 0 0 1 12 7.9a4.3 4.3 0 0 1 7.5 2.9c0 5.1-7.5 9.7-7.5 9.7z"/></svg>
          Add to Wishlist
        </a>

        <div class="rj-usprow">
          <div class="rj-uspi"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="15" height="12" rx="1"/><path d="M16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg><b>Free Shipping</b></div>
          <div class="rj-uspi"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg><b>Secure Payments</b></div>
          <div class="rj-uspi"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4"/><path d="M8 15l-2-2 2-2"/><path d="M6 13h5"/></svg><b>7-Days Returns</b></div>
        </div>

        <div class="rj-acc">
          <div class="rj-acc__item is-open" data-rj-acc>
            <button type="button" class="rj-acc__head" aria-expanded="true">Details <span class="rj-acc__pm" aria-hidden="true"></span></button>
            <div class="rj-acc__body"><div class="rj-acc__inner rte">
              <ul>
                <li>Product Dimensions (in inch): Length 83 × Width 74.5 × Height 36 | Recommended Mattress (in inch): 78 × 72, mattress not included, thickness up to 6 in.</li>
                <li>Premium Sheesham wood construction — made from high-quality solid Sheesham for exceptional durability and a natural, timeless finish.</li>
                <li>Comfortable upholstered headboard — a cushioned headboard for added comfort and style, ideal for leaning back while reading or relaxing.</li>
                <li>DIY assembly required — easy-to-follow instructions included, with a 12 mm MDF mattress base ensuring solid support and stability.</li>
                <li>Spacious King size — generously sized at 6.5 × 6 ft for a restful sleep experience in any bedroom.</li>
              </ul>
            </div></div>
          </div>
          <div class="rj-acc__item" data-rj-acc>
            <button type="button" class="rj-acc__head" aria-expanded="false">Delivery <span class="rj-acc__pm" aria-hidden="true"></span></button>
            <div class="rj-acc__body"><div class="rj-acc__inner rte"><p>Your order will be delivered within 7–10 days.</p></div></div>
          </div>
          <div class="rj-acc__item" data-rj-acc>
            <button type="button" class="rj-acc__head" aria-expanded="false">Return &amp; Cancellation <span class="rj-acc__pm" aria-hidden="true"></span></button>
            <div class="rj-acc__body"><div class="rj-acc__inner rte">
              <p><strong>Returns</strong></p>
              <p>We take great care to ensure your order is delivered safely. In the unlikely event you receive a damaged or defective product:</p>
              <ul><li>Inform the delivery personnel immediately.</li><li>Report the issue to our Customer Support team right away.</li></ul>
              <p>All complaints are reviewed within 72 hours. If confirmed, we will arrange a replacement, return, or other suitable resolution.</p>
              <p><strong>Cancellations</strong></p>
              <p>Orders may be cancelled within 24 hours of placement.</p>
            </div></div>
          </div>
          <div class="rj-acc__item" data-rj-acc>
            <button type="button" class="rj-acc__head" aria-expanded="false">Care Instructions <span class="rj-acc__pm" aria-hidden="true"></span></button>
            <div class="rj-acc__body"><div class="rj-acc__inner rte">
              <p><strong>Cleaning</strong></p>
              <ul><li>Wipe dust with a soft cotton cloth.</li><li>Use a slightly moistened cloth, avoiding excess water.</li><li>Clean only with water — avoid chemicals or harsh cleaners.</li></ul>
              <p><strong>Surface Care</strong></p>
              <ul><li>Use coasters or mats for hot, cold, or wet items to protect the polish.</li><li>Wipe spills immediately with a soft, dry cloth to prevent stains.</li></ul>
            </div></div>
          </div>
          <div class="rj-acc__item" data-rj-acc>
            <button type="button" class="rj-acc__head" aria-expanded="false">Quality Promise &amp; Disclaimer <span class="rj-acc__pm" aria-hidden="true"></span></button>
            <div class="rj-acc__body"><div class="rj-acc__inner rte">
              <p><strong>Quality Promise</strong></p>
              <ul><li>All wooden products undergo a 3-step treatment for protection against termites, borers, and pests.</li><li>Every product is tested through a 3-stage quality check with over 50+ checkpoints before dispatch.</li></ul>
              <p><strong>Disclaimer</strong></p>
              <ul><li>Accessories shown in images are for display purposes only and are not included, unless specified.</li><li>Natural wood grains may vary slightly from piece to piece.</li></ul>
            </div></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <section class="rj-relsec">
    <div class="rj-wrap">
      <div class="rj-relsec__head rj-reveal is-in">
        <span class="rj-eyebrow">Complete the Set</span>
        <h2 class="rj-relsec__title">Pairs beautifully with</h2>
      </div>
      <div class="rj-cgrid rj-cgrid--related">{RELATED}</div>
    </div>
  </section>

  <section class="rj-prev" id="RjReviews">
    <div class="rj-wrap">
      <h2 class="rj-prev__title">Customer Reviews</h2>
      <p class="rj-prev__note">Judge.me review widget yahan aayega — app install hone ke baad reviews khud dikhenge (live site par ye note nahi dikhta).</p>
    </div>
  </section>

  <div class="rj-stickybar is-shown" data-rj-sticky>
    <div class="rj-wrap rj-stickybar__in">
      <div class="rj-stickybar__left">
        <img class="rj-stickybar__img" src="{CDN}81dP0WMJ1zL._SL1500.jpg?width=150" alt="">
        <div>
          <b>Platform Cot Bed</b>
          <span class="rj-stickybar__price"><span data-rj-sticky-price>₹15,566</span><s data-rj-sticky-was>₹28,798</s></span>
        </div>
      </div>
      <div class="rj-stickybar__right">
        <button type="button" class="rj-btn rj-btn--solid rj-stickybar__add" data-rj-sticky-add>Add to Cart</button>
      </div>
    </div>
  </div>
</div>
</main>

{FOOTER}

<script type="application/json" data-rj-variants>
[
  {{"id": 1, "options": ["King"], "available": true, "price": "₹15,566", "compare": "₹28,798", "discount": 46, "sku": "RJWBK001", "media_id": 0, "image": "{CDN}81dP0WMJ1zL._SL1500.jpg?width=1400"}},
  {{"id": 2, "options": ["Queen"], "available": true, "price": "₹15,956", "compare": "₹27,898", "discount": 43, "sku": "RJWQB002", "media_id": 1, "image": "{CDN}61V6A_vqILL._SL1500.jpg?width=1400"}}
]
</script>

<script>
/* real theme JS (assets/rj-arts.js) */
<!--RJ_JS-->
</script>
</body>
</html>
"""

html = PAGE.format(
    TOKENS=TOKENS,
    css=css,
    NAV=NAV,
    FOOTER=FOOTER,
    THUMBS=THUMB_HTML,
    RELATED=RELATED_HTML,
    CDN=CDN,
)
js = (ROOT / "theme_export/assets/rj-arts.js").read_text()
html = html.replace("<!--RJ_JS-->", js)
(ROOT / "preview-product-01.html").write_text(html)
print("wrote preview-product-01.html", len(html), "bytes")
