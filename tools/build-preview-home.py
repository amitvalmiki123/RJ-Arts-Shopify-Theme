#!/usr/bin/env python3
"""
Builds the static slice preview at the repo root from the theme's own CSS.

The preview is a hand-checked replica of the Liquid output for the current slice,
so it is always in sync with theme_export/assets/rj-arts.css.

Usage:  python3 tools/build-preview-home.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / "theme_export/assets/rj-arts.css").read_text()

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
<header class="rj-header-wrap header-wrapper color-scheme-1" data-rj-header>
  <div class="rj-wrap">
    <nav class="rj-nav" aria-label="Primary">
      <button class="rj-icon-btn rj-nav__burger" aria-label="Menu">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>

      <a href="#" class="rj-logo"><img src="Images/logo.svg" alt="RJ Arts" width="133" height="29"></a>

      <ul class="rj-nav__menu">
        <li class="rj-nav__item">
          <a href="#" class="rj-nav__link">Bedroom <i class="rj-chev" aria-hidden="true"></i></a>
          <div class="rj-mega">
            <div>
              <h4>Beds</h4>
              <ul>
                <li><a href="#">King Size Beds</a></li>
                <li><a href="#">Queen Size Beds</a></li>
                <li><a href="#">Single Beds</a></li>
                <li><a href="#">Double Beds</a></li>
                <li><a href="#">Beds with Storage</a></li>
              </ul>
            </div>
            <div>
              <h4>Bedroom Storage</h4>
              <ul>
                <li><a href="#">Chest of Drawers</a></li>
                <li><a href="#">Sideboard Cabinets</a></li>
                <li><a href="#">Bedside Tables</a></li>
                <li><a href="#">Wardrobes</a></li>
              </ul>
            </div>
            <div class="rj-mega__feature">
              <a class="rj-mega__card" href="#"><img src="Images/Bed.png" alt="Beds"><span>Sheesham Beds</span></a>
              <a class="rj-mega__card" href="#"><img src="Images/Bed2.png" alt="Heritage"><span>Brass Heritage</span></a>
            </div>
          </div>
        </li>

        <li class="rj-nav__item">
          <a href="#" class="rj-nav__link">Living <i class="rj-chev" aria-hidden="true"></i></a>
          <div class="rj-mega">
            <div>
              <h4>Seating</h4>
              <ul>
                <li><a href="#">1 Seater Sofa</a></li>
                <li><a href="#">2 Seater Sofa</a></li>
                <li><a href="#">3 Seater Sofa</a></li>
                <li><a href="#">Accent Chairs</a></li>
              </ul>
            </div>
            <div>
              <h4>Storage</h4>
              <ul>
                <li><a href="#">Book Shelves</a></li>
                <li><a href="#">Cabinets &amp; Sideboards</a></li>
                <li><a href="#">Bar Cabinets</a></li>
                <li><a href="#">Coffee Tables</a></li>
              </ul>
            </div>
            <div class="rj-mega__feature">
              <a class="rj-mega__card" href="#"><img src="Images/Living.jpg" alt="Living"><span>Bar Cabinets</span></a>
              <a class="rj-mega__card" href="#"><img src="Images/Sofa.png" alt="Sofa"><span>Signature Sofas</span></a>
            </div>
          </div>
        </li>

        <li class="rj-nav__item">
          <a href="#" class="rj-nav__link">Dining <i class="rj-chev" aria-hidden="true"></i></a>
          <div class="rj-mega">
            <div>
              <h4>Dining Sets</h4>
              <ul>
                <li><a href="#">2 Seat Dining</a></li>
                <li><a href="#">4 Seat Dining</a></li>
                <li><a href="#">6 Seat Dining</a></li>
                <li><a href="#">Dining Benches</a></li>
              </ul>
            </div>
            <div>
              <h4>Finishes</h4>
              <ul>
                <li><a href="#">Honey Finish</a></li>
                <li><a href="#">Walnut Finish</a></li>
                <li><a href="#">Natural Sheesham</a></li>
                <li><a href="#">Teak Finish</a></li>
              </ul>
            </div>
            <div class="rj-mega__feature">
              <a class="rj-mega__card" href="#"><img src="Images/Dining.png" alt="Dining"><span>6-Seater Sets</span></a>
              <a class="rj-mega__card" href="#"><img src="Images/Dining_image.webp" alt="Bench Dining"><span>Bench Dining</span></a>
            </div>
          </div>
        </li>

        <li class="rj-nav__item"><a href="#new" class="rj-nav__link">New Arrivals</a></li>
        <li class="rj-nav__item"><a href="#best" class="rj-nav__link">Best Sellers</a></li>
      </ul>

      <div class="rj-nav__actions">
        <button class="rj-icon-btn" aria-label="Search">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="16.5" y1="16.5" x2="21" y2="21"/></svg>
        </button>
        <a href="#" class="rj-icon-btn rj-icon-btn--account" aria-label="Account">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>
        </a>
        <a href="#" class="rj-icon-btn rj-icon-btn--cart" aria-label="Cart">
          <span class="rj-icon-btn__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><path d="M6 8h12l-1 12H7L6 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>
          </span>
          <div class="cart-count-bubble rj-cart-count"><span aria-hidden="true">0</span></div>
        </a>
      </div>
    </nav>
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
"""

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

  const header = document.querySelector('[data-rj-header]');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 30);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

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
/* preview-only: hamburger is hidden on desktop exactly like the Liquid header */
.rj-nav__burger {{ display: none; }}
@media (max-width: 768px) {{
  .rj-nav__burger {{ display: flex; }}
  .rj-nav__handle {{ display: none; }}
}}
@media (max-width: 768px) {{
  .rj-nav__menu {{ display: none; }}
}}
</style>
</head>
<body class="rj-theme">

<!-- ANNOUNCEMENT -->
<div class="rj-announce color-scheme-4" role="region" aria-label="Announcement">
  <div class="rj-announce__track" style="--rj-marquee-duration: 34s; font-size: 12px;">
    <span class="rj-announce__group">
      <i class="rj-announce__star" aria-hidden="true"></i><span><strong>10%</strong> off for registered members</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span>Over <strong>10,000</strong> happy customers</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span><strong>1,000+</strong> five-star reviews</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span><strong>0%</strong> finance available</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span>Free delivery on solid-wood beds</span>
    </span>
    <span class="rj-announce__group" aria-hidden="true">
      <i class="rj-announce__star" aria-hidden="true"></i><span><strong>10%</strong> off for registered members</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span>Over <strong>10,000</strong> happy customers</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span><strong>1,000+</strong> five-star reviews</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span><strong>0%</strong> finance available</span>
      <i class="rj-announce__star" aria-hidden="true"></i><span>Free delivery on solid-wood beds</span>
    </span>
  </div>
</div>

{NAV}
<main>
{HERO}
{USP}
</main>
{SCRIPT}
</body>
</html>
"""

(ROOT / "preview-home-01.html").write_text(html)
print("wrote preview-home-01.html", len(html), "bytes")
