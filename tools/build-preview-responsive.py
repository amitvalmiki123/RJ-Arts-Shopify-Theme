#!/usr/bin/env python3
"""
Builds preview-about-responsive.html — the About page shown side by side at the
widths we audit (360 / 390 / 430 / 768 / 989 / 1024 / 1440).

Each column is a real iframe pointing at preview-about-01.html, so the CSS
breakpoints are exercised exactly like a device would.

Usage:  python3 tools/build-preview-responsive.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEVICES = [
    ("360", "360 px", "small phone"),
    ("390", "390 px", "iPhone 14"),
    ("430", "430 px", "phone XL"),
    ("768", "768 px", "tablet portrait"),
    ("989", "989 px", "Dawn tablet breakpoint"),
    ("1024", "1024 px", "tablet landscape"),
    ("1440", "1440 px", "desktop"),
]

COLUMNS = ""
for slug, label, note in DEVICES:
    width = int(slug)
    COLUMNS += f"""
    <section class="col">
      <header class="col__head">
        <b>{label}</b>
        <span>{note}</span>
        <a href="preview-about-01.html" target="_blank" rel="noopener">open raw</a>
      </header>
      <div class="frame" style="width: {width}px">
        <iframe src="preview-about-01.html" title="About page at {slug}px" width="{width}" height="1400" loading="lazy"></iframe>
      </div>
    </section>"""

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RJ Arts — About page responsive check</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 28px 24px 60px;
    background: #211c17;
    color: #f7f4ef;
    font-family: Jost, system-ui, sans-serif;
  }}
  h1 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 400;
    font-size: 30px;
    margin: 0 0 6px;
    color: #fff;
  }}
  .sub {{
    font-size: 13px;
    letter-spacing: 0.08em;
    color: #a9865b;
    text-transform: uppercase;
    margin-bottom: 26px;
  }}
  .row {{
    display: flex;
    gap: 26px;
    align-items: flex-start;
    overflow-x: auto;
    padding-bottom: 24px;
  }}
  .col {{ flex: 0 0 auto; }}
  .col__head {{
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin-bottom: 10px;
    font-size: 12px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #cfc6b8;
  }}
  .col__head b {{ color: #fff; }}
  .col__head span {{ color: #8a8178; text-transform: none; letter-spacing: 0; }}
  .col__head a {{ margin-left: auto; color: #a9865b; text-decoration: none; }}
  .col__head a:hover {{ text-decoration: underline; }}
  .frame {{
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 30px 60px -30px rgba(0, 0, 0, 0.8);
  }}
  iframe {{ display: block; border: 0; }}
</style>
</head>
<body>
  <h1>About page — responsive check</h1>
  <p class="sub">360 · 390 · 430 · 768 · 989 · 1024 · 1440 — real iframes, real CSS</p>
  <div class="row">{COLUMNS}
  </div>
</body>
</html>
"""

out = ROOT / "preview-about-responsive.html"
out.write_text(PAGE)
print("wrote preview-about-responsive.html", len(PAGE), "bytes,", len(DEVICES), "widths")
