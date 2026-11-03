#!/usr/bin/env python3
"""
Builds preview-about-01.html — a static replica of the Liquid output of
sections/rj-page-about.liquid, using the theme's real rj-arts.css + rj-arts.js.

Text and images are copied out of design/About.html so the preview and the
design can be compared side by side.

Usage:  python3 tools/build-preview-about.py
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

design = (ROOT / "design/About.html").read_text()

# ---------------------------------------------------------------- hero
hero_img = re.search(r'class="ahero__bg"><img src="([^"]+)"', design).group(1)
hero_h1 = re.search(r'ahero__inner"[^>]*>\s*<div class="crumb">.*?</div>\s*<h1>(.*?)</h1>', design, re.S).group(1)
hero_p = re.search(r'</h1>\s*<p>(.*?)</p>', design, re.S).group(1)

# ---------------------------------------------------------------- story
story_img = re.search(r'class="split__media">\s*<img src="([^"]+)"', design).group(1)
story_tag = re.search(r'class="tag"><b>(.*?)</b><small>(.*?)</small>', design)
story_body = re.search(
    r'<div class="split__body">(.*?)</div>\s*</div>\s*</div>\s*</section>', design, re.S
).group(1)
story_h2 = re.search(r'<h2 class="h-section">(.*?)</h2>', story_body, re.S).group(1)
story_paras = re.findall(r"<p>(.*?)</p>", story_body, re.S)
story_btn = re.search(r'class="btn btn--solid">(.*?)</a>', story_body).group(1)

# ---------------------------------------------------------------- stats
stats = re.findall(r'<div class="stat"><b>(.*?)</b><small>(.*?)</small></div>', design)

# ---------------------------------------------------------------- workshop
ws_img = re.search(r'class="wsband__bg"><img src="([^"]+)"', design).group(1)
ws_body = re.search(r'class="wsband__inner reveal">(.*?)</div>', design, re.S).group(1)
ws_h2 = re.search(r"<h2>(.*?)</h2>", ws_body, re.S).group(1)
ws_p = re.search(r"<p>(.*?)</p>", ws_body, re.S).group(1)

# ---------------------------------------------------------------- craft split
craft_body = re.search(
    r'<div class="split rev reveal"[^>]*>\s*<div class="split__body">(.*?)</div>', design, re.S
).group(1)
craft_h2 = re.search(r'<h2 class="h-section">(.*?)</h2>', craft_body, re.S).group(1)
craft_paras = re.findall(r"<p>(.*?)</p>", craft_body, re.S)
craft_img = re.search(r'class="split__media" style="aspect-ratio:1/1">\s*<img src="([^"]+)"', design).group(1)

# ---------------------------------------------------------------- process steps
steps = []
for m in re.finditer(
    r'<article class="pstep">\s*<div class="pstep__media"><img src="([^"]+)" alt="([^"]*)"></div>'
    r'\s*<div class="pstep__body"><div class="pstep__n">(.*?)</div><h3>(.*?)</h3><p>(.*?)</p></div>\s*</article>',
    design,
    re.S,
):
    steps.append(dict(img=m.group(1), num=m.group(3), title=m.group(4), text=m.group(5)))

# ---------------------------------------------------------------- why cards
# same icon order as templates/page.about.json / the section defaults
ICONS = {
    "wood": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4"/><path d="M12 11v10"/>',
    "check": '<path d="M20 6L9 17l-5-5"/>',
    "warranty": '<path d="M4 12a8 8 0 0 1 16 0"/><path d="M12 4v4M12 12l3 2"/>',
    "truck": '<rect x="1" y="3" width="15" height="13"/><path d="M16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
    "star": '<path d="M12 2l2.5 5 5.5.8-4 3.9.9 5.5L12 20l-4.9 2.6.9-5.5-4-3.9 5.5-.8z"/>',
    "chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
}
ICON_ORDER = ["wood", "check", "warranty", "truck", "star", "chat"]

whys = re.findall(r'<div class="wcard">.*?<h3>(.*?)</h3><p>(.*?)</p></div>', design, re.S)

# ---------------------------------------------------------------- CTA
cta_block = re.search(r'<section class="cta">(.*?)</section>', design, re.S).group(1)
cta_h2 = re.search(r"<h2>(.*?)</h2>", cta_block, re.S).group(1)
cta_p = re.search(r"<p>(.*?)</p>", cta_block, re.S).group(1)
cta_btns = re.findall(r'class="btn btn--light"[^>]*>(.*?)</a>', cta_block, re.S)

# ---------------------------------------------------------------- gallery
gallery = []
for m in re.finditer(
    r'<a(?: class="(big|wide)")? data-full="([^"]+)"><img src="([^"]+)" alt="([^"]*)"></a>', design
):
    gallery.append(dict(size=m.group(1) or "", full=m.group(2), img=m.group(3), alt=m.group(4)))

# ---------------------------------------------------------------- markup
STORY_PARAS = "\n            ".join(f"<p>{p}</p>" for p in story_paras)
CRAFT_PARAS = "\n            ".join(f"<p>{p}</p>" for p in craft_paras)

STATS = "\n        ".join(
    f'<div class="rj-astat"><b>{v}</b><small>{l}</small></div>' for v, l in stats
)

STEPS = ""
for s in steps:
    STEPS += f"""
        <article class="rj-pstep">
          <div class="rj-pstep__media"><img class="rj-pstep__img" src="{s['img']}" alt="" loading="lazy"></div>
          <div class="rj-pstep__body">
            <div class="rj-pstep__n">{s['num']}</div>
            <h3>{s['title']}</h3>
            <p>{s['text']}</p>
          </div>
        </article>"""

WHYS = ""
for i, (title, text) in enumerate(whys):
    key = ICON_ORDER[i] if i < len(ICON_ORDER) else "wood"
    WHYS += f"""
          <div class="rj-wcard">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[key]}</svg>
            <h3>{title}</h3>
            <p>{text}</p>
          </div>"""

GAL = ""
for g in gallery:
    cls = "rj-agal__item"
    if g["size"] == "big":
        cls += " is-big"
    elif g["size"] == "wide":
        cls += " is-wide"
    GAL += f"""
          <a class="{cls}" href="{g['full']}" data-rj-lightbox data-rj-lightbox-alt="{g['alt']}" aria-label="Open image: {g['alt']}">
            <img class="rj-agal__img" src="{g['img']}" alt="{g['alt']}" loading="lazy">
          </a>"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ Arts &mdash; About page (section preview)</title>
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
<div class="rj-about-page color-scheme-1 gradient" style="--rj-ahero-h: 74vh; --rj-wsband-h: 66vh;">

  <section class="rj-ahero">
    <div class="rj-ahero__bg"><img class="rj-ahero__img" src="{hero_img}" alt="Our story is carved in wood."></div>
    <div class="rj-wrap rj-ahero__inner">
      <nav class="rj-crumb rj-crumb--light" aria-label="Breadcrumb">
        <a href="THE-RJ-ARTS.html">Home</a><span>/</span><span>About Us</span>
      </nav>
      <h1 class="rj-ahero__title">{hero_h1}</h1>
      <div class="rj-ahero__text"><p>{hero_p}</p></div>
    </div>
  </section>

  <section class="rj-asec">
    <div class="rj-wrap">
      <div class="rj-split rj-reveal is-in">
        <div class="rj-split__media">
          <img class="rj-split__img" src="{story_img}" alt="Where furniture becomes heirloom." loading="lazy">
          <div class="rj-split__tag"><b>{story_tag1}</b><small>{story_tag2}</small></div>
        </div>
        <div class="rj-split__body">
          <span class="rj-eyebrow">Our Story</span>
          <h2 class="rj-ah2">{story_h2}</h2>
          <div class="rj-atext">
            {STORY_PARAS}
          </div>
          <a class="rj-btn rj-btn--solid rj-split__btn" href="THE-RJ-ARTS.html">{story_btn}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="rj-astats">
    <div class="rj-wrap">
      <div class="rj-astats__grid rj-reveal is-in">
        {STATS}
      </div>
    </div>
  </section>

  <section class="rj-wsband">
    <div class="rj-wsband__bg"><img class="rj-wsband__img" src="{ws_img}" alt="Handcrafted luxury, timeless living." loading="lazy"></div>
    <div class="rj-wsband__inner rj-reveal is-in">
      <span class="rj-eyebrow">Inside Our Workshop</span>
      <h2>{ws_h2}</h2>
      <p>{ws_p}</p>
    </div>
  </section>

  <section class="rj-asec">
    <div class="rj-wrap">
      <div class="rj-split rj-split--rev rj-reveal is-in">
        <div class="rj-split__body">
          <span class="rj-eyebrow">The Craft</span>
          <h2 class="rj-ah2">{craft_h2}</h2>
          <div class="rj-atext">
            {CRAFT_PARAS}
          </div>
        </div>
        <div class="rj-split__media rj-split__media--square">
          <img class="rj-split__img" src="{craft_img}" alt="The Craft" loading="lazy">
        </div>
      </div>

      <div class="rj-proc rj-reveal is-in">{STEPS}
      </div>
    </div>
  </section>

  <section class="rj-asec rj-why">
    <div class="rj-wrap">
      <div class="rj-asec__head rj-reveal is-in">
        <span class="rj-eyebrow">Why Choose Us</span>
        <h2 class="rj-ah2">A promise in every piece.</h2>
      </div>
      <div class="rj-why__grid rj-reveal is-in">{WHYS}
      </div>
    </div>
  </section>

  <section class="rj-cta">
    <div class="rj-wrap rj-reveal is-in">
      <span class="rj-eyebrow">Visit Us</span>
      <h2>{cta_h2}</h2>
      <p>{cta_p}</p>
      <div class="rj-cta__buttons">
        <a class="rj-btn rj-btn--light" href="THE-RJ-ARTS.html">{cta_btn1}</a>
        <a class="rj-btn rj-btn--ghost" href="https://wa.me/917014483250">{cta_btn2}</a>
      </div>
    </div>
  </section>

  <section class="rj-asec">
    <div class="rj-wrap">
      <div class="rj-asec__head rj-reveal is-in">
        <span class="rj-eyebrow">Our Spaces</span>
        <h2 class="rj-ah2">Step inside RJ Arts.</h2>
      </div>
      <div class="rj-agal rj-reveal is-in">{GAL}
      </div>
    </div>
  </section>

  <div class="rj-lb" data-rj-lightbox-modal hidden>
    <button type="button" class="rj-lb__close" data-rj-lightbox-close aria-label="Close">&times;</button>
    <img class="rj-lb__img" data-rj-lightbox-img src="" alt="">
  </div>
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
html = PAGE.format(
    TOKENS=TOKENS,
    css=css,
    NAV=NAV,
    FOOTER=FOOTER,
    hero_img=hero_img,
    hero_h1=hero_h1,
    hero_p=hero_p,
    story_img=story_img,
    story_tag1=story_tag.group(1),
    story_tag2=story_tag.group(2),
    story_h2=story_h2,
    STORY_PARAS=STORY_PARAS,
    story_btn=story_btn,
    STATS=STATS,
    ws_img=ws_img,
    ws_h2=ws_h2,
    ws_p=ws_p,
    craft_img=craft_img,
    craft_h2=craft_h2,
    CRAFT_PARAS=CRAFT_PARAS,
    STEPS=STEPS,
    WHYS=WHYS,
    cta_h2=cta_h2,
    cta_p=cta_p,
    cta_btn1=cta_btns[0],
    cta_btn2=cta_btns[1] if len(cta_btns) > 1 else "Chat on WhatsApp",
    GAL=GAL,
)
html = html.replace("<!--RJ_JS-->", js)
(ROOT / "preview-about-01.html").write_text(html)
print(
    "wrote preview-about-01.html",
    len(html),
    "bytes,",
    len(stats),
    "stats,",
    len(steps),
    "steps,",
    len(whys),
    "why cards,",
    len(gallery),
    "gallery items",
)
