#!/usr/bin/env python3
"""
Builds the static slice preview at the repo root from the theme's own CSS.

The preview is a hand-checked replica of the Liquid output for the current slice,
so it is always in sync with theme_export/assets/rj-arts.css.

Usage:  python3 tools/build-preview-home.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
css = (
    (ROOT / "theme_export/assets/base.css").read_text()
    + "\n/* ---- rj-arts.css ---- */\n"
    + (ROOT / "theme_export/assets/rj-arts.css").read_text()
)  # Dawn base.css, then the RJ design system loaded after it

TOKENS = """
/* ---- static preview stand-ins for what layout/theme.liquid emits ---- */
:root {
  --color-background: 247, 244, 239;
  --color-foreground: 33, 28, 23;
  --font-heading-family: 'Cormorant Garamond';
  --font-body-family: 'Jost';
  --font-heading-scale: 1;
  --rj-set-panel: #efe9e1;
  --rj-set-hairline: #e2dbd0;
  --rj-set-muted: #8a8178;
  --rj-set-soft: #4a433b;
  --rj-set-accent: #a9865b;
  --rj-set-accent-deep: #8a6a43;
  --rj-set-sale: #9a5b46;
  --rj-set-container: 1850px;
  --rj-set-pad: 40px;
}
/* Dawn colour-scheme classes, preview stand-ins */
.color-scheme-1 { --color-background: 247, 244, 239; --color-foreground: 33, 28, 23; }
.color-scheme-4 { --color-background: 33, 28, 23; --color-foreground: 247, 244, 239; }
html { font-size: 62.5%; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { overflow-x: hidden; -webkit-font-smoothing: antialiased; }
img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
ul { list-style: none; }
button { font: inherit; }
.visually-hidden {
  position: absolute !important; width: 1px; height: 1px; overflow: hidden;
  clip: rect(0 0 0 0); white-space: nowrap;
}
"""

NAV = """
<div class="utility-bar color-scheme-4 gradient rj-announce-bar" style="--rj-marquee-duration: 34s;">
  <div class="rj-ticker" role="region" aria-label="Announcement">
    <div class="rj-ticker__group">
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg"><strong>10%</strong> off for registered members</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg">Over <strong>10,000</strong> happy customers</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg"><strong>1,000+</strong> five-star reviews</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg"><strong>0%</strong> finance available</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg">Free delivery on solid-wood beds</span>
    </div>
    <div class="rj-ticker__group" aria-hidden="true">
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg"><strong>10%</strong> off for registered members</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg">Over <strong>10,000</strong> happy customers</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg"><strong>1,000+</strong> five-star reviews</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg"><strong>0%</strong> finance available</span>
      <i class="rj-ticker__star" aria-hidden="true"></i><span class="rj-ticker__msg">Free delivery on solid-wood beds</span>
    </div>
  </div>
</div>

<header class="section-header">
  <div class="header-wrapper color-scheme-1 gradient">
    <header class="header header--middle-left header--has-menu page-width">
      <button class="header__icon header__icon--menu" aria-label="Menu">
        <span class="svg-wrapper"><svg viewBox="0 0 18 16" aria-hidden="true"><path fill="currentColor" d="M1 .5a.5.5 0 1 0 0 1h15.71a.5.5 0 0 0 0-1zM.5 8a.5.5 0 0 1 .5-.5h15.71a.5.5 0 0 1 0 1H1A.5.5 0 0 1 .5 8m0 7a.5.5 0 0 1 .5-.5h15.71a.5.5 0 0 1 0 1H1a.5.5 0 0 1-.5-.5"/></svg></span>
      </button>

      <h1 class="header__heading">
        <a href="#" class="header__heading-link link link--text">
          <span class="header__heading-logo-wrapper">
            <img class="header__heading-logo" src="Images/logo.png" alt="RJ Arts" width="133" height="29">
          </span>
        </a>
      </h1>

      <nav class="header__inline-menu">
        <ul class="list-menu list-menu--inline" role="list">
          <li>
            <header-menu>
              <details class="mega-menu">
                <summary class="header__menu-item list-menu__item link focus-inset">
                  <span>Bedroom</span>
                  <svg class="icon icon-caret" viewBox="0 0 10 6" aria-hidden="true"><path fill="currentColor" d="M9.354.646a.5.5 0 0 0-.708 0L5 4.293 1.354.646a.5.5 0 0 0-.708.708l4 4a.5.5 0 0 0 .708 0l4-4a.5.5 0 0 0 0-.708"/></svg>
                </summary>
                <div class="mega-menu__content mega-menu__content--with-feature color-scheme-3">
                  <ul class="mega-menu__list page-width" role="list">
                    <li>
                      <a href="#" class="mega-menu__link mega-menu__link--level-2 link">Beds</a>
                      <ul class="list-unstyled" role="list">
                        <li><a href="#" class="mega-menu__link link">King Size Beds</a></li>
                        <li><a href="#" class="mega-menu__link link">Queen Size Beds</a></li>
                        <li><a href="#" class="mega-menu__link link">Single Beds</a></li>
                        <li><a href="#" class="mega-menu__link link">Double Beds</a></li>
                        <li><a href="#" class="mega-menu__link link">Beds with Storage</a></li>
                      </ul>
                    </li>
                    <li>
                      <a href="#" class="mega-menu__link mega-menu__link--level-2 link">Bedroom Storage</a>
                      <ul class="list-unstyled" role="list">
                        <li><a href="#" class="mega-menu__link link">Chest of Drawers</a></li>
                        <li><a href="#" class="mega-menu__link link">Sideboard Cabinets</a></li>
                        <li><a href="#" class="mega-menu__link link">Bedside Tables</a></li>
                        <li><a href="#" class="mega-menu__link link">Wardrobes</a></li>
                      </ul>
                    </li>
                  </ul>
                  <div class="mega-menu__feature">
                    <a class="mega-menu__feature-card" href="#"><img src="Images/Bed.png" alt="Beds"><span>Sheesham Beds</span></a>
                    <a class="mega-menu__feature-card" href="#"><img src="Images/Bed2.png" alt="Heritage"><span>Brass Heritage</span></a>
                  </div>
                </div>
              </details>
            </header-menu>
          </li>
          <li>
            <header-menu>
              <details class="mega-menu">
                <summary class="header__menu-item list-menu__item link focus-inset">
                  <span>Living</span>
                  <svg class="icon icon-caret" viewBox="0 0 10 6" aria-hidden="true"><path fill="currentColor" d="M9.354.646a.5.5 0 0 0-.708 0L5 4.293 1.354.646a.5.5 0 0 0-.708.708l4 4a.5.5 0 0 0 .708 0l4-4a.5.5 0 0 0 0-.708"/></svg>
                </summary>
                <div class="mega-menu__content mega-menu__content--with-feature color-scheme-3">
                  <ul class="mega-menu__list page-width" role="list">
                    <li>
                      <a href="#" class="mega-menu__link mega-menu__link--level-2 link">Seating</a>
                      <ul class="list-unstyled" role="list">
                        <li><a href="#" class="mega-menu__link link">1 Seater Sofa</a></li>
                        <li><a href="#" class="mega-menu__link link">2 Seater Sofa</a></li>
                        <li><a href="#" class="mega-menu__link link">3 Seater Sofa</a></li>
                        <li><a href="#" class="mega-menu__link link">Accent Chairs</a></li>
                      </ul>
                    </li>
                    <li>
                      <a href="#" class="mega-menu__link mega-menu__link--level-2 link">Storage</a>
                      <ul class="list-unstyled" role="list">
                        <li><a href="#" class="mega-menu__link link">Book Shelves</a></li>
                        <li><a href="#" class="mega-menu__link link">Cabinets &amp; Sideboards</a></li>
                        <li><a href="#" class="mega-menu__link link">Bar Cabinets</a></li>
                        <li><a href="#" class="mega-menu__link link">Coffee Tables</a></li>
                      </ul>
                    </li>
                  </ul>
                  <div class="mega-menu__feature">
                    <a class="mega-menu__feature-card" href="#"><img src="Images/Living.jpg" alt="Bar Cabinets"><span>Bar Cabinets</span></a>
                    <a class="mega-menu__feature-card" href="#"><img src="Images/Sofa.png" alt="Signature Sofas"><span>Signature Sofas</span></a>
                  </div>
                </div>
              </details>
            </header-menu>
          </li>
          <li>
            <header-menu>
              <details class="mega-menu">
                <summary class="header__menu-item list-menu__item link focus-inset">
                  <span>Dining</span>
                  <svg class="icon icon-caret" viewBox="0 0 10 6" aria-hidden="true"><path fill="currentColor" d="M9.354.646a.5.5 0 0 0-.708 0L5 4.293 1.354.646a.5.5 0 0 0-.708.708l4 4a.5.5 0 0 0 .708 0l4-4a.5.5 0 0 0 0-.708"/></svg>
                </summary>
                <div class="mega-menu__content mega-menu__content--with-feature color-scheme-3">
                  <ul class="mega-menu__list page-width" role="list">
                    <li>
                      <a href="#" class="mega-menu__link mega-menu__link--level-2 link">Dining Sets</a>
                      <ul class="list-unstyled" role="list">
                        <li><a href="#" class="mega-menu__link link">2 Seat Dining</a></li>
                        <li><a href="#" class="mega-menu__link link">4 Seat Dining</a></li>
                        <li><a href="#" class="mega-menu__link link">6 Seat Dining</a></li>
                        <li><a href="#" class="mega-menu__link link">Dining Benches</a></li>
                      </ul>
                    </li>
                    <li>
                      <a href="#" class="mega-menu__link mega-menu__link--level-2 link">Finishes</a>
                      <ul class="list-unstyled" role="list">
                        <li><a href="#" class="mega-menu__link link">Honey Finish</a></li>
                        <li><a href="#" class="mega-menu__link link">Walnut Finish</a></li>
                        <li><a href="#" class="mega-menu__link link">Natural Sheesham</a></li>
                        <li><a href="#" class="mega-menu__link link">Teak Finish</a></li>
                      </ul>
                    </li>
                  </ul>
                  <div class="mega-menu__feature">
                    <a class="mega-menu__feature-card" href="#"><img src="Images/Dining.png" alt="6-Seater Sets"><span>6-Seater Sets</span></a>
                    <a class="mega-menu__feature-card" href="#"><img src="Images/Dining_image.webp" alt="Bench Dining"><span>Bench Dining</span></a>
                  </div>
                </div>
              </details>
            </header-menu>
          </li>
          <li><a href="#" class="header__menu-item list-menu__item link link--text"><span>New Arrivals</span></a></li>
          <li><a href="#" class="header__menu-item list-menu__item link link--text"><span>Best Sellers</span></a></li>
        </ul>
      </nav>

      <div class="header__icons">
        <a href="#" class="header__icon header__icon--search" aria-label="Search">
          <span class="svg-wrapper"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg></span>
        </a>
        <a href="#" class="header__icon header__icon--account" aria-label="Account">
          <span class="svg-wrapper"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg></span>
        </a>
        <a href="#" class="header__icon header__icon--cart" aria-label="Cart">
          <span class="svg-wrapper"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8h12l-1 12H7L6 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg></span>
          <div class="cart-count-bubble"><span aria-hidden="true">0</span></div>
        </a>
      </div>
    </header>
  </div>
</header>
"""

HERO = """
<rj-hero class="rj-hero" style="--rj-hero-height: 92vh; --rj-hero-min-height: 620px; --rj-hero-duration: 6s;"
  data-autoplay="true" data-speed="6">
  <div class="rj-hero__slide is-active" data-slide="0">
    <div class="rj-hero__bg"><img src="Images/Bed-Banner.png" alt="RJ Arts beds"></div>
    <div class="rj-wrap rj-hero__inner">
      <p class="rj-eyebrow rj-hero__eyebrow">Bedroom · Solid Sheesham</p>
      <h1 class="rj-hero__heading">Furniture that<br>outlives trends.</h1>
      <p class="rj-hero__text">Hand-finished solid-wood beds with cushioned headboards and clever storage — built to be handed down, backed by a 3-year warranty.</p>
      <div class="rj-hero__cta">
        <a href="#" class="rj-btn rj-btn--light">Shop Bedroom</a>
        <a href="#" class="rj-btn rj-btn--ghost">Explore Collections</a>
      </div>
    </div>
  </div>

  <div class="rj-hero__slide" data-slide="1" aria-hidden="true">
    <div class="rj-hero__bg"><img src="Images/Dining-Banner.png" alt="RJ Arts dining"></div>
    <div class="rj-wrap rj-hero__inner">
      <p class="rj-eyebrow rj-hero__eyebrow">Dining · Gather in Style</p>
      <h1 class="rj-hero__heading">Made for the<br>long dinners.</h1>
      <p class="rj-hero__text">Solid Sheesham dining sets in honey, walnut and natural finishes — from intimate 2-seaters to grand 6-seater tables with benches.</p>
      <div class="rj-hero__cta">
        <a href="#" class="rj-btn rj-btn--light">Shop Dining</a>
        <a href="#" class="rj-btn rj-btn--ghost">View Finishes</a>
      </div>
    </div>
  </div>

  <div class="rj-hero__slide" data-slide="2" aria-hidden="true">
    <div class="rj-hero__bg"><img src="Images/Sofa-Banner.png" alt="RJ Arts sofas"></div>
    <div class="rj-wrap rj-hero__inner">
      <p class="rj-eyebrow rj-hero__eyebrow">Living · Crafted Comfort</p>
      <h1 class="rj-hero__heading">Comfort, carved<br>from wood.</h1>
      <p class="rj-hero__text">Handcrafted sofas that blend timeless elegance with everyday comfort — a signature centrepiece for every living space.</p>
      <div class="rj-hero__cta">
        <a href="#" class="rj-btn rj-btn--light">Shop Living</a>
        <a href="#" class="rj-btn rj-btn--ghost">Explore Collections</a>
      </div>
    </div>
  </div>

  <div class="rj-hero__count"><b data-rj-hero-count>01</b> / 03</div>
  <div class="rj-hero__dots" data-rj-hero-dots>
    <button type="button" class="is-active" data-index="0" aria-label="Slide 1"></button>
    <button type="button" data-index="1" aria-label="Slide 2"></button>
    <button type="button" data-index="2" aria-label="Slide 3"></button>
  </div>
  <div class="rj-hero__arrows">
    <button type="button" data-dir="-1" aria-label="Previous slide"><svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="15 5 8 12 15 19"/></svg></button>
    <button type="button" data-dir="1" aria-label="Next slide"><svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="9 5 16 12 9 19"/></svg></button>
  </div>
</rj-hero>
"""

USP = """
<div class="rj-usp color-scheme-1 rj-usp--line" style="--rj-usp-pad: 30px;">
  <div class="rj-wrap">
    <div class="rj-usp__grid">
      <div class="rj-usp__item rj-reveal">
        <span class="rj-usp__icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M12 2l2.5 5 5.5.8-4 3.9.9 5.5L12 20l-4.9 2.6.9-5.5-4-3.9 5.5-.8z"/></svg></span>
        <div class="rj-usp__text"><b>1,000+ 5-Star Reviews</b><small>Loved by 10,000+ homes</small></div>
      </div>
      <div class="rj-usp__item rj-reveal d1">
        <span class="rj-usp__icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4"/><path d="M12 11v10"/></svg></span>
        <div class="rj-usp__text"><b>100% Solid Sheesham</b><small>Kiln-dried, hand-finished</small></div>
      </div>
      <div class="rj-usp__item rj-reveal d2">
        <span class="rj-usp__icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M4 12a8 8 0 0 1 16 0"/><path d="M12 4v4M12 12l3 2"/></svg></span>
        <div class="rj-usp__text"><b>3-Year Warranty</b><small>Built to be handed down</small></div>
      </div>
      <div class="rj-usp__item rj-reveal d3">
        <span class="rj-usp__icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M2 10h20"/></svg></span>
        <div class="rj-usp__text"><b>0% Finance Available</b><small>Easy EMI at checkout</small></div>
      </div>
    </div>
  </div>
</div>

<div class="rj-cats color-scheme-1" style="--rj-cats-pt: 96px; --rj-cats-pb: 96px;">
  <div class="rj-wrap">
    <div class="rj-cats__head rj-reveal">
      <div class="rj-cats__head-main">
        <span class="rj-eyebrow">Shop by Room</span>
        <h2 class="rj-cats__title">Three rooms,<br>one philosophy.</h2>
      </div>
      <p class="rj-cats__text">Every RJ Arts room is designed around solid wood &mdash; warm, tactile and made to last a lifetime, not a season.</p>
    </div>
    <div class="rj-cats__grid">
      <a class="rj-cat rj-reveal" href="#">
        <img class="rj-cat__img" src="Images/Bed.png" alt="Bedroom">
        <span class="rj-cat__body"><h3 class="rj-cat__title">Bedroom</h3><span class="rj-cat__sub">Beds, storage &amp; bedsides</span></span>
      </a>
      <a class="rj-cat rj-reveal d1" href="#">
        <img class="rj-cat__img" src="Images/Living.jpg" alt="Living Room">
        <span class="rj-cat__body"><h3 class="rj-cat__title">Living</h3><span class="rj-cat__sub">Sofas &amp; cabinets</span></span>
      </a>
      <a class="rj-cat rj-reveal d2" href="#">
        <img class="rj-cat__img" src="Images/Dining.png" alt="Dining Room">
        <span class="rj-cat__body"><h3 class="rj-cat__title">Dining</h3><span class="rj-cat__sub">Tables, sets &amp; benches</span></span>
      </a>
    </div>
  </div>
</div>

<div class="rj-show" id="new">
  <div class="rj-wrap">
    <div class="rj-show__head rj-reveal">
      <div>
        <span class="rj-eyebrow">Curated Selection</span>
        <h2 class="rj-show__title">The showroom edit.</h2>
      </div>
      <div style="display:flex;flex-direction:column;gap:20px;align-items:flex-end">
        <div class="rj-tabs" id="tabs">
          <button class="rj-tab is-active" data-tab="p-new">New Arrivals</button>
          <button class="rj-tab" data-tab="p-best">Best Sellers</button>
          <button class="rj-tab" data-tab="p-her">Heritage</button>
        </div>
        <div class="rj-railnav">
          <button data-dir="-1" aria-label="Previous"><svg viewBox="0 0 24 24"><polyline points="15 5 8 12 15 19"/></svg></button>
          <button data-dir="1" aria-label="Next"><svg viewBox="0 0 24 24"><polyline points="9 5 16 12 9 19"/></svg></button>
        </div>
      </div>
    </div>

    <!-- NEW ARRIVALS -->
    <div class="rj-panel is-active" id="p-new">
      <div class="rj-rail">
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">New</span><img src="Images/Bed2.png" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Jaipur Cane Box-Storage King Bed</h3><div class="rj-pcard__price"><span class="now">₹36,699</span><span class="was">₹67,899</span><span class="off">−46%</span></div><div class="rj-pcard__stars">★★★★★ <small>New</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/Bed_4.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Brass-Work Headboard King Bed</h3><div class="rj-pcard__price"><span class="now">₹35,522</span><span class="was">₹80,599</span><span class="off">−56%</span></div><div class="rj-pcard__stars">★★★★★ <small>New</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">New</span><img src="Images/Bed_Side_Table.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Sheesham Queen Bed · Honey Finish</h3><div class="rj-pcard__price"><span class="now">₹14,500</span></div><div class="rj-pcard__stars">★★★★★ <small>New</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/Dining_image.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Dining</span><h3 class="rj-pcard__title">Buck Dining Set · Walnut Finish</h3><div class="rj-pcard__price"><span class="now">₹41,595</span><span class="was">₹71,544</span><span class="off">−42%</span></div><div class="rj-pcard__stars">★★★★★ <small>New</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">New</span><img src="Images/Dining.png" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Dining</span><h3 class="rj-pcard__title">Solid Wood Dining Set with Bench</h3><div class="rj-pcard__price"><span class="now">₹45,522</span></div><div class="rj-pcard__stars">★★★★★ <small>New</small></div></div>
        </article>
      </div>
    </div>

    <!-- BEST SELLERS -->
    <div class="rj-panel" id="p-best" hidden>
      <div class="rj-rail">
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/Bed-Banner.png" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Platform Cot Bed · Cushioned Headboard</h3><div class="rj-pcard__price"><span class="now">₹15,566</span><span class="was">₹28,798</span><span class="off">−46%</span></div><div class="rj-pcard__stars">★★★★★ <small>19 reviews</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/Bed-2_4.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Wood Arch Bed · Without Storage</h3><div class="rj-pcard__price"><span class="now">₹15,998</span><span class="was">₹28,078</span><span class="off">−43%</span></div><div class="rj-pcard__stars">★★★★★ <small>16 reviews</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/BedRoom_a6f690c8-7f36-4dde-8366-7078a65d25fa.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Low-Height Double Bed · Rosewood</h3><div class="rj-pcard__price"><span class="now">₹15,823</span><span class="was">₹27,358</span><span class="off">−42%</span></div><div class="rj-pcard__stars">★★★★★ <small>19 reviews</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/Sofa-_4.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Living</span><h3 class="rj-pcard__title">Lurid Sheesham 3-Seater Sofa</h3><div class="rj-pcard__price"><span class="now">₹15,622</span></div><div class="rj-pcard__stars">★★★★★ <small>Best Seller</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag is-sale">Sale</span><img src="Images/Bed_4.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Double Bed · Without Storage</h3><div class="rj-pcard__price"><span class="now">₹21,100</span><span class="was">₹35,998</span><span class="off">−41%</span></div><div class="rj-pcard__stars">★★★★★ <small>15 reviews</small></div></div>
        </article>
      </div>
    </div>

    <!-- HERITAGE -->
    <div class="rj-panel" id="p-her" hidden>
      <div class="rj-rail">
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">Heritage</span><img src="Images/Sideboard_Cabinet_image.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Living</span><h3 class="rj-pcard__title">Regular Brass-Design Home Bar Cabinet</h3><div class="rj-pcard__price"><span class="now">₹41,595</span></div><div class="rj-pcard__stars">★★★★★ <small>Signature</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">Heritage</span><img src="Images/Bed_4.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Bedroom</span><h3 class="rj-pcard__title">Sevilla Half-Box & Trolley Storage Bed</h3><div class="rj-pcard__price"><span class="now">₹34,522</span><span class="was">₹80,599</span><span class="off">−57%</span></div><div class="rj-pcard__stars">★★★★★ <small>Signature</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">Heritage</span><img src="Images/Dining_Desktop_Banner.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Dining</span><h3 class="rj-pcard__title">Imperial 6-Seater Dining · Honey</h3><div class="rj-pcard__price"><span class="now">₹45,522</span></div><div class="rj-pcard__stars">★★★★★ <small>Signature</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">Heritage</span><img src="Images/Dining.png" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Dining</span><h3 class="rj-pcard__title">Natural Sheesham 6-Seater Set</h3><div class="rj-pcard__price"><span class="now">₹45,522</span></div><div class="rj-pcard__stars">★★★★★ <small>Signature</small></div></div>
        </article>
        <article class="rj-pcard">
          <div class="rj-pcard__media"><span class="rj-pcard__tag">Heritage</span><img src="Images/Dining_image.webp" alt=""><div class="rj-pcard__quick"><a class="rj-btn rj-btn--light" href="#">Quick View</a></div></div>
          <div class="rj-pcard__body"><span class="rj-pcard__cat">Dining</span><h3 class="rj-pcard__title">Buck Dining Set · Honey Finish</h3><div class="rj-pcard__price"><span class="now">₹41,595</span><span class="was">₹71,544</span><span class="off">−42%</span></div><div class="rj-pcard__stars">★★★★★ <small>Signature</small></div></div>
        </article>
      </div>
    </div>
  </div>
</div>
<div class="rj-bandwrap" style="--rj-band-pt: 0px; --rj-band-pb: 96px; --rj-band-min: 560px;">
  <div class="rj-wrap">
    <div class="rj-band rj-reveal">
      <div class="rj-band__bg"><img class="rj-band__img" src="Images/Bed2.png" alt="The Art of Rest"></div>
      <div class="rj-band__inner">
        <span class="rj-eyebrow rj-band__eyebrow">The Art of Rest</span>
        <h2 class="rj-band__title">Elevate every<br>moment of rest.</h2>
        <p class="rj-band__text">Beds that balance luxury and comfort — hand-finished solid Sheesham, engineered joinery, and headboards worth waking up to.</p>
        <a href="#" class="rj-btn rj-btn--light rj-band__cta">Shop Bedroom</a>
      </div>
    </div>
  </div>
</div>
<div class="rj-aboutsec" id="about" style="--rj-about-pt: 96px; --rj-about-pb: 96px;">
  <div class="rj-wrap">
    <div class="rj-about rj-reveal">
      <div class="rj-about__media">
        <img class="rj-about__img" src="Images/About/Our Story.png" alt="Inside the RJ Arts workshop">
        <div class="rj-about__badge"><b>25+ Years</b><small>of Woodcraft</small></div>
      </div>
      <div class="rj-about__body">
        <span class="rj-eyebrow">Our Story</span>
        <h2 class="rj-about__title">Craft that carries<br>a family's name.</h2>
        <div class="rj-about__text">
        <p>RJ Arts began in the workshops of Rajasthan, where solid Sheesham is still shaped the way it has been for generations — kiln-dried, hand-joined, and finished by artisans who take pride in every grain.</p>
        <p>Each bed, sofa and dining set is built to be lived with and handed down, not replaced. That belief in permanence is why over 10,000 homes have made RJ Arts a part of their everyday.</p>
        </div>
        <div class="rj-about__stats">
          <div class="rj-about__stat"><b>10,000+</b><small>Happy Homes</small></div>
          <div class="rj-about__stat"><b>830+</b><small>5-Star Reviews</small></div>
          <div class="rj-about__stat"><b>3 Years</b><small>Warranty</small></div>
        </div>
        <a href="#" class="rj-btn rj-btn--solid rj-about__cta">Read Our Story</a>
      </div>
    </div>
  </div>
</div>"""

SCRIPT = """
<script>
/* mirrors theme_export/assets/rj-hero.js + rj-arts.js for the static preview */
(function () {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.rj-reveal').forEach((el) => io.observe(el));

  const header = document.querySelector('.section-header .header-wrapper');
  const onScroll = () => header.classList.toggle('rj-scrolled', window.scrollY > 30);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });


  /* mirrors sections/rj-showroom.liquid + rj-arts.js <rj-showroom> */
  const show = document.querySelector('.rj-show');
  if (show) {
    const tabs = Array.from(show.querySelectorAll('.rj-tab'));
    const panels = Array.from(show.querySelectorAll('.rj-panel'));
    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const index = tabs.indexOf(tab);
        tabs.forEach((item, i) => item.classList.toggle('is-active', i === index));
        panels.forEach((panel, i) => {
          panel.classList.toggle('is-active', i === index);
          if (i === index) panel.removeAttribute('hidden');
          else panel.setAttribute('hidden', '');
        });
      });
    });
    show.querySelectorAll('[data-rj-rail-dir]').forEach((button) => {
      button.addEventListener('click', () => {
        const rail = show.querySelector('.rj-panel.is-active .rj-rail');
        if (!rail) return;
        const card = rail.querySelector('.rj-pcard');
        const step = card ? card.getBoundingClientRect().width + 22 : 320;
        rail.scrollBy({ left: step * parseInt(button.dataset.rjRailDir, 10), behavior: 'smooth' });
      });
    });
  }

  const hero = document.querySelector('rj-hero');
  const slides = [...hero.querySelectorAll('.rj-hero__slide')];
  const dots = [...hero.querySelectorAll('[data-rj-hero-dots] button')];
  const counter = hero.querySelector('[data-rj-hero-count]');
  const speed = 6000;
  let index = 0, timer;

  function go(next) {
    index = ((next % slides.length) + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      slide.classList.toggle('is-active', i === index);
      if (i === index) slide.removeAttribute('aria-hidden');
      else slide.setAttribute('aria-hidden', 'true');
    });
    dots.forEach((dot, i) => {
      const shouldBeActive = i === index;
      if (shouldBeActive && !dot.classList.contains('is-active')) {
        dot.classList.remove('is-active');
        void dot.offsetWidth;
      }
      dot.classList.toggle('is-active', shouldBeActive);
    });
    counter.textContent = String(index + 1).padStart(2, '0');
  }
  function start() { clearInterval(timer); timer = setInterval(() => go(index + 1), speed); }

  hero.querySelector('.rj-hero__arrows').addEventListener('click', (e) => {
    const b = e.target.closest('button[data-dir]');
    if (!b) return;
    go(index + Number(b.dataset.dir));
    start();
  });
  hero.querySelector('[data-rj-hero-dots]').addEventListener('click', (e) => {
    const b = e.target.closest('button');
    if (!b) return;
    go(Number(b.dataset.index));
    start();
  });

  let sx = 0, sy = 0, tracking = false;
  hero.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; sy = e.touches[0].clientY; tracking = true; }, { passive: true });
  hero.addEventListener('touchend', (e) => {
    if (!tracking) return;
    tracking = false;
    const dx = e.changedTouches[0].clientX - sx;
    const dy = e.changedTouches[0].clientY - sy;
    if (Math.abs(dx) < 45 || Math.abs(dx) < Math.abs(dy)) return;
    go(index + (dx < 0 ? 1 : -1));
    start();
  }, { passive: true });

  start();
})();
</script>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ Arts — Homepage slice 1 (announcement, header, hero)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
{TOKENS}
{css}
/* preview-only: Dawn hides the hamburger on desktop via component CSS */
/* design-exact icon row: one search trigger, no close glyph */
.header__icon--menu {{ display: none; }}
.header__icons .header__icon--search span.svg-wrapper {{ background-color: currentColor; }}
.header__icons .svg-wrapper > svg {{ display: none; }}
@media screen and (max-width: 989px) {{
  .header__icon--menu {{ display: flex; }}
  .header__inline-menu {{ display: none; }}
}}
.utility-bar__grid {{ display: block; }}
.page-width {{ margin-inline: auto; width: 100%; }}
/* ---- preview-only shim for Dawn base.css classes (real theme loads base.css) ---- */
.list-menu, .list-unstyled {{ list-style: none; margin: 0; padding: 0; }}
.list-menu--inline {{ display: inline-flex; flex-wrap: wrap; }}
.header__heading {{ margin: 0; line-height: 0; }}
.header__icon {{ position: relative; display: flex; align-items: center; justify-content: center; }}
.header__icon--cart {{ position: relative; }}
.mega-menu {{ position: static; }}
.mega-menu > summary {{ list-style: none; cursor: pointer; }}
.mega-menu > summary::-webkit-details-marker {{ display: none; }}
.mega-menu__content {{ position: absolute; left: 0; right: 0; top: 100%; z-index: 30; }}
.mega-menu__list {{ display: grid; grid-template-columns: repeat(3, 1fr); max-width: 1180px; margin-inline: auto; }}
.mega-menu:not([open]) .mega-menu__content {{ display: none; }}
.link {{ text-decoration: none; color: inherit; }}

</style>
</head>
<body class="rj-theme">

{NAV}
<main>
{HERO}
{USP}
</main>
{SCRIPT}
</body>
</html>
"""

HEADER_ONLY_SCRIPT = """
<script>
  const header = document.querySelector('.section-header .header-wrapper');
  const onScroll = () => header.classList.toggle('rj-scrolled', window.scrollY > 30);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  document.querySelectorAll('.mega-menu').forEach((d) => {
    d.addEventListener('mouseenter', () => d.setAttribute('open', ''));
    d.addEventListener('mouseleave', () => d.removeAttribute('open'));
  });
</script>
"""

header_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ Arts — Header group (announcement + header)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
{TOKENS}
{css}
.header__icon--menu {{ display: none; }}
@media screen and (max-width: 989px) {{
  .header__icon--menu {{ display: flex; }}
  .header__inline-menu {{ display: none; }}
}}
.page-width {{ margin-inline: auto; width: 100%; }}
.list-menu, .list-unstyled {{ list-style: none; margin: 0; padding: 0; }}
.list-menu--inline {{ display: inline-flex; flex-wrap: wrap; }}
.header__heading {{ margin: 0; line-height: 0; }}
.header__icon {{ position: relative; display: flex; align-items: center; justify-content: center; }}
.mega-menu {{ position: static; }}
.mega-menu > summary {{ list-style: none; cursor: pointer; }}
.mega-menu > summary::-webkit-details-marker {{ display: none; }}
.mega-menu__content {{ position: absolute; left: 0; right: 0; top: 100%; z-index: 30; }}
.mega-menu__list {{ display: grid; grid-template-columns: repeat(2, 1fr); }}
.mega-menu:not([open]) .mega-menu__content {{ display: none; }}
.link {{ text-decoration: none; color: inherit; }}
body {{ min-height: 200vh; }}
</style>
</head>
<body class="rj-theme">
{NAV}
{HEADER_ONLY_SCRIPT}
</body>
</html>
"""

(ROOT / "preview-header-group.html").write_text(header_page)
(ROOT / "preview-home-01.html").write_text(html)
print("wrote preview-home-01.html", len(html), "bytes")
