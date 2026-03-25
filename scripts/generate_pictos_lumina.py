#!/usr/bin/env python3
"""
generate_pictos_lumina.py
Reads pictos-lumina.json and generates two Markdown files:
  - pictos-lumina-summary.md  — loadouts, core sets, situational, candidates
  - pictos-lumina-catalogue.md — full alphabetical catalogue of all 194 Pictos

Usage:
    python3 generate_pictos_lumina.py [input.json] [output_dir]
Defaults:
    input:  overview/pictos-lumina.json
    output: overview/
"""

import json
import sys
from pathlib import Path


def load(path):
    with open(path) as f:
        return json.load(f)


def row(cells):
    return "| " + " | ".join(str(c) if c is not None else "—" for c in cells) + " |"


def header(cells):
    divider = "|" + "|".join("---" for _ in cells) + "|"
    return row(cells) + "\n" + divider


def pictos_detail(pictos_list, name):
    """Look up a Pictos by name and return a compact detail string."""
    for p in pictos_list:
        if p["name"] == name:
            parts = []
            if p.get("effect"):
                parts.append(p["effect"])
            if p.get("lp_cost") is not None:
                parts.append(f"{p['lp_cost']}LP")
            stats = p.get("stats", {})
            if stats:
                stat_parts = []
                for k in ("health", "speed", "defence", "crit"):
                    if k in stats:
                        label = k.capitalize()
                        if k == "crit":
                            label = "Crit"
                        stat_parts.append(f"{label} +{stats[k]}")
                if stat_parts:
                    parts.append(", ".join(stat_parts))
            return " — ".join(parts) if parts else ""
    return ""


def get_primary_cat(p):
    """Get primary category from a Pictos entry (handles both string and list)."""
    cat = p.get("category", "misc")
    return cat[0] if isinstance(cat, list) else cat


def get_all_cats(p):
    """Get all categories from a Pictos entry (handles both string and list)."""
    cat = p.get("category", ["misc"])
    return cat if isinstance(cat, list) else [cat]


def secondary_cats_label(p):
    """Return a label for secondary categories, or empty string if none."""
    cats = get_all_cats(p)
    if len(cats) <= 1:
        return ""
    return ", ".join(cats[1:])


def generate_summary(data):
    """Generate the summary Markdown (everything except the full catalogue)."""
    lines = []
    pictos = data.get("pictos", [])

    # ── Title ────────────────────────────────────────────────────────────
    lines += [
        "# Clair Obscur: Expedition 33 — Pictos and Lumina Summary",
        "",
        f"*Generated from `pictos-lumina.json` (commit `{data.get('_commit', 'unknown')}`).*",
        "",
        "See `pictos-lumina-catalogue.md` for the full list of all 194 Pictos.",
        "",
        "-----",
        "",
    ]

    # ── 1. Pictos Mechanics ──────────────────────────────────────────────
    lines += [
        "## 1. Pictos Mechanics",
        "",
        "Pictos are collectible items — one unique copy of each exists in the game. Finding a duplicate upgrades the existing copy. Each character has 3 Pictos slots. Equipping a Pictos applies both its **stat boosts** and its **effect**. After winning 4 battles with a Pictos equipped, it is learnt as a Lumina.",
        "",
        "Higher level Pictos give higher stat boosts. With all main attributes maxed at 99, Pictos stat boosts are the primary source of character growth.",
        "",
        "-----",
        "",
    ]

    # ── 2. Lumina Mechanics ──────────────────────────────────────────────
    lines += [
        "## 2. Lumina Mechanics",
        "",
        "Lumina are passive effects derived from Pictos. They apply the **effect only** — not the stat boosts. A character cannot equip the Lumina of a Pictos they already have equipped (the effect would be redundant and the game prevents it).",
        "",
        "Each character has a pool of Lumina Points (LP). LP = character level by default. Permanently increase LP by spending Colour of Lumina items (1 Colour = 1 LP).",
        "",
        "**In-game Lumina Sets:** The game allows saving up to 50 Lumina Sets per character. Sets apply a group of Lumina in one action. The recommended workflow is: apply core set first, then add character-specific extras on top.",
        "",
        "-----",
        "",
    ]

    # ── 3. Main Team Core Lumina Set ─────────────────────────────────────
    main = data.get("core_lumina_suite", {}).get("main_team", {})
    lines += [
        "## 3. Main Team Core Lumina Set",
        "",
        f"**Total: {main.get('total_lp', '?')} LP** — applied to Maelle, Verso, Sciel.",
        "",
        f"*{main.get('notes', '')}*",
        "",
        "*Note: any Lumina costs 0LP for a character who has that Pictos equipped. For example, Verso has Cheater as Pictos (0LP), Breaking Death as Pictos (0LP); Monoco has Energising Turn as Pictos (0LP).*",
        "",
        header(["Lumina", "LP", "Effect", "Notes"]),
    ]
    for e in main.get("entries", []):
        effect = ""
        for p in pictos:
            if p["name"] == e["name"]:
                effect = p.get("effect", "")
                break
        lines.append(row([e["name"], e["lp"], effect, e.get("notes", "")]))
    lines += ["", "-----", ""]

    # ── 4. Reserve Team Core Lumina Set ──────────────────────────────────
    reserve = data.get("core_lumina_suite", {}).get("reserve_team", {})
    lines += [
        "## 4. Reserve Team Core Lumina Set",
        "",
        f"**Total: {reserve.get('total_lp', '?')} LP** — applied to Lune, Monoco.",
        "",
        f"*{reserve.get('notes', '')}*",
        "",
        header(["Lumina", "LP", "Effect"]),
    ]
    for e in reserve.get("entries", []):
        effect = ""
        for p in pictos:
            if p["name"] == e["name"]:
                effect = p.get("effect", "")
                break
        lines.append(row([e["name"], e["lp"], effect]))
    lines += ["", "-----", ""]

    # ── 5. Per-Character Loadouts ────────────────────────────────────────
    lines += ["## 5. Per-Character Loadouts", ""]
    for name, char in data.get("characters", {}).items():
        lines += [f"### {name}", ""]
        lines += [f"**Level:** {char.get('level', '?')} | **LP:** {char.get('lumina_lp_used', '?')}/{char.get('lumina_lp_total', '?')}"]
        if char.get("lumina_notes"):
            lines += [f"*{char['lumina_notes']}*"]
        lines += [""]

        # Pictos with inline detail
        char_pictos = char.get("pictos", [])
        if char_pictos:
            lines += ["**Pictos:**", "", header(["Pictos", "Level", "Effect", "Stats"])]
            for cp in char_pictos:
                pname = cp["name"]
                # Find full details
                effect = ""
                stat_str = ""
                for p in pictos:
                    if p["name"] == pname:
                        effect = p.get("effect", "")
                        stats = p.get("stats", {})
                        if stats:
                            parts = []
                            for k in ("health", "speed", "defence", "crit"):
                                if k in stats:
                                    parts.append(f"{k.capitalize()} +{stats[k]}")
                            stat_str = ", ".join(parts)
                        break
                lines.append(row([pname, cp.get("level", "?"), effect, stat_str]))
            lines += [""]

        # Core adjustments note
        adj = char.get("lumina_core_adjustments")
        if adj:
            lines += [f"*Core adjustments: {adj}*", ""]

        # Extras
        extras = char.get("lumina_extras", [])
        if extras:
            lines += ["**Character-specific Lumina (on top of core):**", "", header(["Lumina", "LP", "Effect", "Notes"])]
            for e in extras:
                effect = ""
                for p in pictos:
                    if p["name"] == e["name"]:
                        effect = p.get("effect", "")
                        break
                lines.append(row([e["name"], e.get("lp", "?"), effect, e.get("notes", "")]))
            lines += [""]

        # Additions/removals this session
        adds = char.get("lumina_additions", [])
        rems = char.get("lumina_removals", [])
        if adds:
            lines += [f"*Added this session: {', '.join(e['name'] for e in adds)}*"]
        if rems:
            lines += [f"*Removed this session: {', '.join(e['name'] for e in rems)}*"]
        if adds or rems:
            lines += [""]
        lines += [""]

    lines += ["-----", ""]

    # ── 6. Situational Lumina ────────────────────────────────────────────
    lines += ["## 6. Situational Lumina", "", "Add these as Lumina for specific boss fights — no need to change Pictos.", ""]
    sit = data.get("situational_lumina", [])
    if sit:
        lines += [header(["Lumina", "LP", "Effect", "Notes"])]
        for s in sit:
            effect = ""
            for p in pictos:
                if p["name"] == s["name"]:
                    effect = p.get("effect", "")
                    break
            lines.append(row([s["name"], s.get("lp", "?"), effect, s["notes"]]))
    lines += ["", "-----", ""]

    # ── 7. Candidates for Review ─────────────────────────────────────────
    lines += ["## 7. Candidates for Future Review", ""]
    lines += [header(["Lumina", "LP", "Effect", "Notes"])]
    for c in data.get("candidates_for_review", []):
        effect = ""
        for p in pictos:
            if p["name"] == c["name"]:
                effect = p.get("effect", "")
                break
        lines.append(row([c["name"], c.get("lp", "?"), effect, c.get("notes", "")]))
    lines += ["", "-----", ""]

    return "\n".join(lines)


def generate_catalogue(data):
    """Generate the full catalogue Markdown."""
    lines = []
    pictos = data.get("pictos", [])

    lines += [
        "# Clair Obscur: Expedition 33 — Pictos Catalogue",
        "",
        f"*Generated from `pictos-lumina.json` (commit `{data.get('_commit', 'unknown')}`).*",
        "",
        f"**{len(pictos)} Pictos total.** {len([p for p in pictos if p.get('obtained')])} obtained.",
        "",
        "-----",
        "",
    ]

    # Group by PRIMARY category
    categories = {}
    for p in pictos:
        primary = get_primary_cat(p)
        categories.setdefault(primary, []).append(p)

    CATEGORY_NAMES = {
        "ap": "AP and Energy",
        "break": "Break",
        "burn": "Burn",
        "critical": "Critical Hit",
        "damage": "Damage Modifiers",
        "death": "Death Effects",
        "gradient": "Gradient Charge",
        "healing": "Healing",
        "mark": "Mark",
        "combat": "Combat Flow",
        "solo": "Solo and Last Stand",
        "survival": "Survival and Defence",
        "support": "Buffs and Support",
        "shots": "Free Aim and Shots",
        "misc": "Miscellaneous",
    }

    CATEGORY_ORDER = [
        "ap", "break", "burn", "critical", "damage", "death",
        "gradient", "healing", "mark", "combat", "solo", "survival",
        "support", "shots", "misc",
    ]

    for cat in CATEGORY_ORDER:
        entries = categories.get(cat, [])
        if not entries:
            continue

        cat_name = CATEGORY_NAMES.get(cat, cat.title())
        obtained_count = len([p for p in entries if p.get("obtained")])

        lines += [
            f"## {cat_name} ({len(entries)} Pictos, {obtained_count} obtained)",
            "",
            header(["", "Name", "Effect", "LP", "Equipped By", "Also in"]),
        ]

        for p in sorted(entries, key=lambda x: x["name"]):
            obtained_mark = "✓" if p.get("obtained") else ""
            equipped = p.get("equipped_by") or ""
            also_in = secondary_cats_label(p)
            lines.append(row([
                obtained_mark,
                p["name"],
                p.get("effect", ""),
                p.get("lp_cost", "?"),
                equipped,
                also_in,
            ]))

        lines += ["", "-----", ""]

    return "\n".join(lines)


if __name__ == "__main__":
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("overview/pictos-lumina.json")
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("overview")

    data = load(input_path)

    summary = generate_summary(data)
    catalogue = generate_catalogue(data)

    summary_path = output_dir / "pictos-lumina-summary.md"
    catalogue_path = output_dir / "pictos-lumina-catalogue.md"

    with open(summary_path, "w") as f:
        f.write(summary)
    with open(catalogue_path, "w") as f:
        f.write(catalogue)

    print(f"Generated {summary_path} ({len(summary.splitlines())} lines)")
    print(f"Generated {catalogue_path} ({len(catalogue.splitlines())} lines)")
