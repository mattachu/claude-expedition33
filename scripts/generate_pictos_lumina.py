#!/usr/bin/env python3
"""
generate_pictos_lumina.py
Reads pictos-lumina.json and generates pictos-lumina.md.
Run from the overview/ directory, or pass paths as arguments.

Usage:
    python3 generate_pictos_lumina.py [input.json] [output.md]
Defaults:
    input:  overview/pictos-lumina.json
    output: overview/pictos-lumina.md
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

def generate(data):
    lines = []

    # ── Title ─────────────────────────────────────────────────────────────────
    lines += [
        "# Clair Obscur: Expedition 33 — Pictos and Lumina Reference",
        "",
        f"*Generated from `pictos-lumina.json` (commit `{data.get('_commit', 'unknown')}`).*",
        f"*{data.get('_notes', '')}*",
        "",
        "-----",
        "",
    ]

    # ── 1. Pictos Mechanics ────────────────────────────────────────────────────
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

    # ── 2. Lumina Mechanics ───────────────────────────────────────────────────
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

    # ── 3. Main Team Core Lumina Set ──────────────────────────────────────────
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
        header(["Lumina", "LP", "Notes"]),
    ]
    for e in main.get("entries", []):
        lines.append(row([e["name"], e["lp"], e.get("notes", "")]))
    lines += ["", "-----", ""]

    # ── 5. Reserve Team Core Lumina Set ───────────────────────────────────────
    reserve = data.get("core_lumina_suite", {}).get("reserve_team", {})
    lines += [
        "## 4. Reserve Team Core Lumina Set",
        "",
        f"**Total: {reserve.get('total_lp', '?')} LP** — applied to Lune, Monoco.",
        "",
        f"*{reserve.get('notes', '')}*",
        "",
        header(["Lumina", "LP"]),
    ]
    for e in reserve.get("entries", []):
        lines.append(row([e["name"], e["lp"]]))
    lines += ["", "-----", ""]

    # ── 6. Per-Character Loadouts ─────────────────────────────────────────────
    lines += ["## 5. Per-Character Loadouts", ""]
    for name, char in data.get("characters", {}).items():
        lines += [f"### {name}", ""]
        lines += [f"**Level:** {char.get('level', '?')} | **LP:** {char.get('lumina_lp_used', '?')}/{char.get('lumina_lp_total', '?')}"]
        if char.get("lumina_notes"):
            lines += [f"*{char['lumina_notes']}*"]
        lines += [""]

        # Pictos
        pictos = char.get("pictos", [])
        if pictos:
            lines += ["**Pictos:**", "", header(["Pictos", "Level"])]
            for p in pictos:
                lines.append(row([p["name"], p.get("level", "?")]))
            lines += [""]

        # Core adjustments note
        adj = char.get("lumina_core_adjustments")
        if adj:
            lines += [f"*Core adjustments: {adj}*", ""]

        # Extras
        extras = char.get("lumina_extras", [])
        if extras:
            lines += ["**Character-specific additions (on top of core):**", "", header(["Lumina", "LP", "Notes"])]
            for e in extras:
                lines.append(row([e["name"], e.get("lp", "?"), e.get("notes", "")]))
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

    # ── 7. Known Pictos Catalogue ─────────────────────────────────────────────
    lines += [
        "## 6. Known Pictos Catalogue",
        "",
        header(["Name", "Level", "Health", "Speed", "Defence", "Crit", "Other Stats", "Effect", "LP Cost", "Current Holder", "Notes"]),
    ]
    for p in sorted(data.get("pictos", []), key=lambda x: x["name"]):
        stats = p.get("stats", {})
        other = ", ".join(f"{k} +{v}" for k, v in stats.items() if k not in ("health", "speed", "defence", "crit"))
        lines.append(row([
            p["name"],
            p.get("level", "?"),
            stats.get("health", ""),
            stats.get("speed", ""),
            stats.get("defence", ""),
            stats.get("crit", ""),
            other,
            p.get("effect", ""),
            p.get("lp_cost", "?"),
            p.get("holder", ""),
            p.get("notes", ""),
        ]))
    lines += ["", "-----", ""]

    # ── 8. Situational Pictos ────────────────────────────────────────────────
    lines += ["## 7. Situational Lumina", "", "Add these as Lumina for specific boss fights — no need to change Pictos.", ""]
    sit = data.get("situational_lumina", [])
    if sit:
        lines += [header(["Lumina", "LP", "Notes"])]
        for s in sit:
            lines.append(row([s["name"], s.get("lp", "?"), s["notes"]]))
    lines += ["", "-----", ""]

    # ── 9. Candidates for Review ─────────────────────────────────────────────
    lines += ["## 8. Candidates for Future Review", "", header(["Lumina", "LP", "Notes"])]
    for c in data.get("candidates_for_review", []):
        lines.append(row([c["name"], c.get("lp", "?"), c.get("notes", "")]))
    lines += ["", "-----", ""]

    return "\n".join(lines)


if __name__ == "__main__":
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("overview/pictos-lumina.json")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("overview/pictos-lumina.md")

    data = load(input_path)
    md = generate(data)

    with open(output_path, "w") as f:
        f.write(md)

    print(f"Generated {output_path} ({len(md.splitlines())} lines)")
