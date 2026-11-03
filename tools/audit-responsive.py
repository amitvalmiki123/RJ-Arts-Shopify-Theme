#!/usr/bin/env python3
"""
Static responsive auditor — no browser needed.

Parses theme_export/assets/rj-arts.css, works out which rules win at a given
viewport width (cascade + simple specificity), and prints the effective value
of the properties that decide the About page's responsive layout.

Also flags body-copy selectors that end up under 15px on a 360px phone.

Usage:  python3 tools/audit-responsive.py
        python3 tools/audit-responsive.py 390
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "theme_export/assets/rj-arts.css").read_text()

WIDTHS = [1440, 1200, 1024, 990, 989, 768, 430, 390, 360]


# ---------------------------------------------------------------- parsing
def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def parse(css):
    """-> list of (selector, decls, media_list, order)"""
    rules = []
    order = [0]

    def walk(text, media):
        i = 0
        buf = ""
        while i < len(text):
            ch = text[i]
            if ch == "{":
                head = buf.strip()
                depth, j = 1, i + 1
                while j < len(text) and depth:
                    if text[j] == "{":
                        depth += 1
                    elif text[j] == "}":
                        depth -= 1
                    j += 1
                body = text[i + 1:j - 1]
                if head.startswith("@media"):
                    walk(body, media + [head[len("@media"):].strip()])
                elif head.startswith("@"):
                    pass  # @keyframes / @font-face / @supports — ignore
                else:
                    order[0] += 1
                    rules.append((head, parse_decls(body), media, order[0]))
                buf = ""
                i = j
            else:
                buf += ch
                i += 1

    walk(strip_comments(css), [])
    return rules


def parse_decls(body):
    out = {}
    for chunk in body.split(";"):
        if ":" not in chunk:
            continue
        prop, val = chunk.split(":", 1)
        prop = prop.strip().lower()
        if prop:
            out[prop] = val.strip()
    return out


HEIGHT = None  # set when auditing a short/landscape viewport


def media_matches(media, width):
    for m in media:
        if "hover: none" in m or "prefers-reduced-motion" in m:
            return False
        for cond in m.split(" and "):
            cond = cond.strip()
            mm = re.match(r"\(\s*(max|min)-width:\s*([\d.]+)px\s*\)", cond)
            if mm:
                kind, px = mm.group(1), float(mm.group(2))
                if kind == "max" and width > px:
                    return False
                if kind == "min" and width < px:
                    return False
                continue
            mh = re.match(r"\(\s*(max|min)-height:\s*([\d.]+)px\s*\)", cond)
            if mh:
                # height-only rules only apply when we are told the height
                if HEIGHT is None:
                    return False
                kind, px = mh.group(1), float(mh.group(2))
                if kind == "max" and HEIGHT > px:
                    return False
                if kind == "min" and HEIGHT < px:
                    return False
    return True


def split_selectors(sel):
    parts, depth, buf = [], 0, ""
    for ch in sel:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(buf.strip())
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf.strip())
    return parts


def specificity(sel):
    sel = re.sub(r"::?[a-z-]+(\([^)]*\))?", "", sel)  # drop pseudo
    ids = sel.count("#")
    classes = sel.count(".") + sel.count("[") + sel.count(":")
    types = len(re.findall(r'(^|[\s>+~])([a-z][a-z0-9]*)', sel))
    return (ids, classes, types)


RULES = parse(CSS)


def resolve(width, selector, prop):
    """Return (value, winning_selector) for the first matching selector exactly."""
    best = None
    for sel, decls, media, order in RULES:
        if prop not in decls:
            continue
        if not media_matches(media, width):
            continue
        for one in split_selectors(sel):
            if one != selector:
                continue
            key = (specificity(one), order)
            if best is None or key > best[0]:
                best = (key, decls[prop], one, media)
    return best


def applies(width, selector):
    """Does any rule with this selector match at this width (incl. partial)?"""
    hits = []
    for sel, decls, media, order in RULES:
        if not media_matches(media, width):
            continue
        for one in split_selectors(sel):
            if selector in one or one in selector:
                hits.append((one, media, order))
    return hits


CHECKS = [
    (".rj-ahero", "height"),
    (".rj-ahero", "min-height"),
    (".rj-ahero", "padding-block"),
    (".rj-ahero__title", "font-size"),
    (".rj-ahero__text", "font-size"),
    (".rj-split", "grid-template-columns"),
    (".rj-split__media", "aspect-ratio"),
    (".rj-astats__grid", "grid-template-columns"),
    (".rj-proc", "grid-template-columns"),
    (".rj-why__grid", "grid-template-columns"),
    (".rj-agal", "grid-template-columns"),
    (".rj-agal", "grid-auto-rows"),
    (".rj-atext", "font-size"),
    (".rj-cta__buttons", "flex-direction"),
]

BODY_COPY = [
    ".rj-atext",
    ".rj-wcard p",
    ".rj-pstep p",
    ".rj-wsband__inner p",
    ".rj-cta p",
    ".rj-ahero__text",
    ".rj-pstep h3",
    ".rj-wcard h3",
]


def fmt(v):
    return "-" if v is None else v[1]


def main():
    global HEIGHT
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for a in sys.argv[1:]:
        if a.startswith("--height="):
            HEIGHT = float(a.split("=", 1)[1])
    widths = [int(args[0])] if args else WIDTHS
    print("ABOUT PAGE — effective layout per viewport (static cascade check)")
    print("css:", CSS.count("\n") + 1, "lines ·", len(RULES), "rules\n")

    head = f"{'property':46}" + "".join(f"{w:>14}" for w in widths)
    print(head)
    print("-" * len(head))
    for sel, prop in CHECKS:
        row = f"{sel + ' ' + prop:46}"
        for w in widths:
            val = fmt(resolve(w, sel, prop))
            row += f"{val[:13]:>14}"
        print(row)

    print("\nBODY COPY (must stay >= 15px at 360):")
    problems = []
    for sel in BODY_COPY:
        val = fmt(resolve(360, sel, "font-size"))
        px = None
        m = re.match(r"([\d.]+)px", val or "")
        if m:
            px = float(m.group(1))
        elif val and "clamp" in val:
            nums = re.findall(r"([\d.]+)px", val)
            if nums:
                px = float(nums[0])
        flag = ""
        if px is not None and px < 15 and not sel.endswith(("h3", "__text")):
            flag = "  <-- FIX"
            problems.append(sel)
        print(f"  {sel:24} {val:42}{flag}")

    print("\nCOLLISION GUARD — product PDP gallery must keep its own grid:")
    gal = resolve(1440, ".rj-gal", "grid-template-columns")
    print("  .rj-gal (product):", gal[1] if gal else "MISSING")
    print("  .rj-agal (about) :", fmt(resolve(1440, ".rj-agal", "grid-template-columns")))

    print("\n", "FAIL" if problems else "All body-copy checks passed", problems or "")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
