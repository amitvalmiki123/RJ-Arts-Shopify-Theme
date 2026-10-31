#!/usr/bin/env python3
"""
Validates the theme's Liquid section schemas against Shopify's hard limits,
because a bad schema only shows up as a FileSaveError in the theme editor.

Checks
  1. schema block is valid JSON
  2. range: (max - min) / step + 1 <= 101   (Shopify: "Range settings must have
     at most 101 steps") and the default sits on a valid step
  3. select: default is one of the option values
  4. ids are unique inside each settings array and inside each block
  5. max_blocks <= 50
  6. section/block type names and ids are sane (lowercase, a-z0-9_-)

Usage:  python3 tools/validate-schemas.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "theme_export"

MAX_RANGE_STEPS = 101
ID_RE = re.compile(r"^[a-z0-9_-]+$")

problems = []


def check_id_setting(section, where, item):
    setting_id = item.get("id")
    if setting_id is None:
        return
    if not ID_RE.match(setting_id):
        problems.append(f"{section} [{where}] id '{setting_id}' should be lowercase a-z0-9_-")

    kind = item.get("type")
    if kind == "range":
        low = item.get("min", 0)
        high = item.get("max", 100)
        step = item.get("step", 1)
        steps = (high - low) / step + 1
        if steps > MAX_RANGE_STEPS:
            problems.append(
                f"{section} [{where}] range '{setting_id}' has {int(steps)} steps "
                f"(max {MAX_RANGE_STEPS}) - increase step or lower max"
            )
        default = item.get("default")
        if default is not None and (default < low or default > high or (default - low) % step != 0):
            problems.append(f"{section} [{where}] range '{setting_id}' default {default} is off-grid")

    if kind == "select" and item.get("default") is not None:
        values = [option["value"] for option in item.get("options", [])]
        if item["default"] not in values:
            problems.append(f"{section} [{where}] select '{setting_id}' default not in options")


def check_list(section, where, items):
    seen = set()
    for item in items:
        setting_id = item.get("id")
        if setting_id:
            if setting_id in seen:
                problems.append(f"{section} [{where}] duplicate id '{setting_id}'")
            seen.add(setting_id)
        check_id_setting(section, where, item)


for path in sorted((THEME / "sections").glob("*.liquid")):
    text = path.read_text()
    match = re.search(r"{% schema %}(.*?){% endschema %}", text, re.S)
    if not match:
        continue
    try:
        schema = json.loads(match.group(1))
    except json.JSONDecodeError as error:
        problems.append(f"{path.name} schema is not valid JSON: {error}")
        continue

    check_list(path.name, "settings", schema.get("settings", []))

    for block in schema.get("blocks", []):
        check_list(path.name, f"block:{block.get('type')}", block.get("settings", []))

    if schema.get("max_blocks", 0) > 50:
        problems.append(f"{path.name} max_blocks {schema['max_blocks']} exceeds 50")

# ---- templates: har section type ka file hona chahiye (warna "Section type does not exist")
section_files = {path.stem for path in (THEME / "sections").glob("*.liquid")}
section_blocks = {}
for path in sorted((THEME / "sections").glob("*.liquid")):
    match = re.search(r"{% schema %}(.*?){% endschema %}", path.read_text(), re.S)
    if not match:
        continue
    try:
        schema = json.loads(match.group(1))
    except json.JSONDecodeError:
        continue
    section_blocks[path.stem] = {block.get("type") for block in schema.get("blocks", [])}

for path in sorted((THEME / "templates").glob("*.json")):
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as error:
        problems.append(f"templates/{path.name} is not valid JSON: {error}")
        continue
    for instance, payload in data.get("sections", {}).items():
        section_type = payload.get("type")
        if not section_type:
            continue
        if section_type.startswith("@") or section_type.startswith("shopify://"):
            continue
        if section_type not in section_files:
            problems.append(
                f"templates/{path.name} '{instance}' uses missing section '{section_type}.liquid'"
            )
            continue
        allowed = section_blocks.get(section_type, set())
        for block_instance, block in payload.get("blocks", {}).items():
            block_type = block.get("type")
            if block_type and allowed and block_type not in allowed:
                problems.append(
                    f"templates/{path.name} '{instance}' block '{block_instance}' "
                    f"has unknown type '{block_type}'"
                )

if problems:
    print(f"{len(problems)} problem(s):")
    for problem in problems:
        print("  -", problem)
    sys.exit(1)

print("All section schemas OK")
