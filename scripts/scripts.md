# Pipeline Scripts

## apply_changelist.py

```python
#!/usr/bin/env python3
"""
Script 3: Apply a changelist of section replacements and insertions to repo files.

Usage:
    python scripts/apply_changelist.py <changelist> [options]

    <changelist>    Path to changelist file
    --repo-root     Root of the git repo (default: current directory)
    --dry-run       Show what would change without writing files

Changelist format:
    One or more entries. Each entry has a header block followed by CONTENT:.
    Everything after CONTENT: until the next FILE: line (or EOF) is the new
    section text, with trailing blank lines stripped.

    FILE: overview/maelle.md
    SECTION: ## Current Stats > ### Level and Attributes
    CONTENT:
    ### Level and Attributes

    | Attribute | Value |
    |-----------|-------|
    | Level     | 70    |

    FILE: overview/maelle.md
    SECTION: ## Open Questions > ### New Question
    AFTER: ### Which skill does Stendhal replace
    CONTENT:
    ### New Question

    Some new content here.

Header fields:
    FILE:     Repo-relative path to the target file (required)
    SECTION:  "## Parent > ### Child" identifier (required)
              For a ## -level change with no ### child: "## Section Name"
    AFTER:    ### heading to insert after (optional; only used when section
              does not yet exist — ignored for updates)
    CONTENT:  Marks the start of replacement text (required; must be last header field)

Behaviour:
    Update (### exists):    Replace the existing ### section with new content.
    Insert (### missing):   Insert after the last ### sibling in the ## parent,
                            or after the AFTER: sibling if specified.
    ## missing:             Fail loudly — structural changes require manual edit.
    ## -level entry:        Replace the entire ## section (no ### child specified).

    Note: the script operates at heading level only. Individual bullet points,
    table rows, or paragraphs within a section cannot be targeted directly —
    to update them, replace the entire ### section containing them.

Section boundaries:
    A ## section spans from its heading line to just before the next ## heading,
    or EOF. A ### section spans from its heading line to just before the next ###
    or ## heading, or EOF. Horizontal rules (--- or -----) are not used as
    boundaries and are stripped from files on load; --- separators are written
    between ## sections on output for readability.
"""

import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Separator normalisation
# ---------------------------------------------------------------------------

_SEPARATOR_RE = re.compile(r'^-{3,}\s*$')


def is_separator(line):
    """True if the line is a horizontal rule (--- or -----  etc.)."""
    return bool(_SEPARATOR_RE.match(line))


def strip_separators(lines):
    """
    Remove all horizontal-rule lines (--- / -----) from a line list.
    Returns a new list; does not modify in place.
    """
    return [line for line in lines if not is_separator(line)]


def normalise_blank_lines(lines):
    """
    Collapse runs of more than one blank line to a single blank line.
    Returns a new list.
    """
    result = []
    prev_blank = False
    for line in lines:
        blank = line.strip() == ''
        if blank and prev_blank:
            continue
        result.append(line)
        prev_blank = blank
    return result


def insert_h2_separators(lines):
    """
    Insert a '---\\n' line before every ## heading (except the very first line
    of the file), skipping any ## lines that appear inside fenced code blocks.

    Layout produced:

        <preceding content>

        ---

        ## Next Section
        ...

    The blank line BEFORE --- and the blank line AFTER --- come from the
    existing content or are added here; a run of blanks is collapsed to one.
    """
    result = []
    in_fence = False
    for i, line in enumerate(lines):
        # Track fenced code blocks (``` or ~~~, with optional language tag)
        if re.match(r'^(`{3,}|~{3,})', line):
            in_fence = not in_fence
        if i > 0 and not in_fence and re.match(r'^## ', line):
            # Ensure there's a blank line before the ---
            if result and result[-1].strip() != '':
                result.append('\n')
            result.append('---\n')
            # Ensure there's a blank line after the ---
            result.append('\n')
        result.append(line)
    return normalise_blank_lines(result)


def load_file(path):
    """Read a file, strip all horizontal rules, and return lines."""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return strip_separators(lines)


def save_file(path, lines):
    """Normalise blank lines, insert ## separators, and write the file."""
    lines = normalise_blank_lines(lines)
    lines = insert_h2_separators(lines)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(lines))


# ---------------------------------------------------------------------------
# Changelist parsing
# ---------------------------------------------------------------------------

def parse_changelist(text):
    """
    Parse changelist text into a list of entry dicts:
        {
            'file': str,
            'parent': str or None,   # e.g. '## Current Stats'
            'section': str,          # e.g. '### Level and Attributes'
            'after': str or None,    # e.g. '### Some Sibling'
            'content': str,          # replacement text (trailing blank lines stripped)
            'section_level': int,    # 2 for ##-level, 3 for ###-level
        }
    Raises ValueError on malformed entries.
    """
    entries = []

    # Split on FILE: boundaries (keep the FILE: line with its block)
    raw_blocks = re.split(r'(?m)^(?=FILE:)', text)

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue
        if not block.startswith('FILE:'):
            continue

        # Split header from content at CONTENT: marker
        content_match = re.search(r'(?m)^CONTENT:\s*\n', block)
        if not content_match:
            raise ValueError(f'Missing CONTENT: marker in block:\n{block[:200]}')

        header_text = block[:content_match.start()]
        content_text = block[content_match.end():]

        # Strip trailing blank lines from content, then add exactly one
        # trailing newline. The splice functions add blank line separators
        # around the content as needed.
        content_text = content_text.rstrip('\n') + '\n'

        # Parse header fields
        def get_field(name, required=True):
            m = re.search(rf'(?m)^{name}:\s*(.+)$', header_text)
            if m:
                return m.group(1).strip()
            if required:
                raise ValueError(f'Missing {name}: in block:\n{header_text}')
            return None

        file_path = get_field('FILE')
        section_str = get_field('SECTION')
        after_hint = get_field('AFTER', required=False)

        # Parse SECTION into parent + child
        if ' > ' in section_str:
            parts = section_str.split(' > ', 1)
            parent_heading = parts[0].strip()
            section_heading = parts[1].strip()
            section_level = 3
            if not parent_heading.startswith('## '):
                raise ValueError(f'Parent heading must start with "## ": {parent_heading}')
            if not section_heading.startswith('### '):
                raise ValueError(f'Child heading must start with "### ": {section_heading}')
        else:
            parent_heading = None
            section_heading = section_str.strip()
            section_level = 2
            if not section_heading.startswith('## '):
                raise ValueError(
                    f'Section heading must start with "## " or use "## > ###" format: '
                    f'{section_heading}'
                )

        entries.append({
            'file': file_path,
            'parent': parent_heading,
            'section': section_heading,
            'after': after_hint,
            'content': content_text,
            'section_level': section_level,
        })

    return entries


# ---------------------------------------------------------------------------
# Section finding and splicing
# ---------------------------------------------------------------------------

def find_heading_line(lines, heading, start=0, end=None):
    """
    Return the line index of an exact heading match within lines[start:end].
    Returns None if not found.
    Matches the heading text stripped of surrounding whitespace.
    """
    if end is None:
        end = len(lines)
    target = heading.strip()
    for i in range(start, end):
        if lines[i].strip() == target:
            return i
    return None


def find_section_end(lines, start, level):
    """
    Return the index of the first line that belongs to the NEXT section,
    starting from start+1.

    Rules (no separator logic — headings only):
      level=2: stop at the next ## heading (^## ) or EOF.
      level=3: stop at the next ### heading (^### ) or any ## heading
               (^## ), or EOF.

    Returns len(lines) if no stop line is found (section reaches EOF).
    """
    if level == 2:
        stop_re = re.compile(r'^## ')
    else:  # level == 3
        stop_re = re.compile(r'^#{2,3} ')

    for i in range(start + 1, len(lines)):
        if stop_re.match(lines[i]):
            return i
    return len(lines)


def apply_entry(lines, entry):
    """
    Apply a single changelist entry to a list of lines.
    Returns new list of lines.
    Raises ValueError on failure (loud failure mode).
    """
    section_level = entry['section_level']
    section_heading = entry['section']
    parent_heading = entry['parent']
    after_hint = entry['after']
    new_content_lines = entry['content'].splitlines(keepends=True)

    if section_level == 2:
        return _apply_h2_entry(lines, section_heading, new_content_lines)
    else:
        return _apply_h3_entry(lines, parent_heading, section_heading,
                               after_hint, new_content_lines)


def _apply_h2_entry(lines, section_heading, new_content_lines):
    """Replace an entire ## section."""
    h2_line = find_heading_line(lines, section_heading)
    if h2_line is None:
        raise ValueError(
            f'## section not found: "{section_heading}"\n'
            f'Structural changes require manual edit.'
        )

    section_end = find_section_end(lines, h2_line, level=2)

    prefix = lines[:h2_line]
    suffix = lines[section_end:]

    # Strip trailing blank lines from prefix to avoid accumulating blanks;
    # insert_h2_separators will add the correct spacing on write.
    while prefix and prefix[-1].strip() == '':
        prefix.pop()

    # Ensure exactly one blank line between new content and the next section
    # (if the suffix starts immediately with a ## heading or non-blank line).
    post_sep = ['\n'] if suffix and suffix[0].strip() != '' else []

    return prefix + new_content_lines + post_sep + suffix


def _apply_h3_entry(lines, parent_heading, section_heading, after_hint, new_content_lines):
    """Replace or insert a ### section within a ## parent."""

    # Find ## parent
    h2_line = find_heading_line(lines, parent_heading)
    if h2_line is None:
        raise ValueError(
            f'## parent not found: "{parent_heading}"\n'
            f'Structural changes require manual edit.'
        )

    # Find end of ## parent block
    h2_end = find_section_end(lines, h2_line, level=2)

    # Look for existing ### section within parent
    h3_line = find_heading_line(lines, section_heading, start=h2_line + 1, end=h2_end)

    if h3_line is not None:
        # UPDATE: replace existing ### section
        h3_end = find_section_end(lines, h3_line, level=3)
        prefix = lines[:h3_line]
        suffix = lines[h3_end:]

        # Preserve a blank line between new content and what follows, but
        # only if the suffix doesn't already start with one.
        post_sep = ['\n'] if suffix and suffix[0].strip() != '' else []

        return prefix + new_content_lines + post_sep + suffix

    else:
        # INSERT: section does not yet exist
        insert_pos = _find_insert_position(lines, h2_line, h2_end, after_hint)
        prefix = lines[:insert_pos]
        suffix = lines[insert_pos:]

        # Ensure a blank line before and after the inserted section
        pre_sep = ['\n'] if prefix and prefix[-1].strip() != '' else []
        post_sep = ['\n'] if suffix and suffix[0].strip() != '' else []

        return prefix + pre_sep + new_content_lines + post_sep + suffix


def _find_insert_position(lines, h2_start, h2_end, after_hint):
    """
    Determine the line index after which the new ### section should be inserted.

    Priority:
    1. If AFTER: hint given, insert after that ### sibling's section end.
    2. Otherwise, insert after the last ### sibling's section end.
    3. If no ### siblings exist, insert at end of ## parent block.
    """
    if after_hint:
        after_line = find_heading_line(lines, after_hint, start=h2_start + 1, end=h2_end)
        if after_line is None:
            raise ValueError(f'AFTER: sibling not found: "{after_hint}"')
        return find_section_end(lines, after_line, level=3)

    # Find last ### sibling
    last_h3_line = None
    for i in range(h2_start + 1, h2_end):
        if re.match(r'^### ', lines[i]):
            last_h3_line = i

    if last_h3_line is not None:
        return find_section_end(lines, last_h3_line, level=3)

    # No ### siblings — insert at end of ## parent block, before trailing blanks
    pos = h2_end
    while pos > h2_start + 1 and not lines[pos - 1].strip():
        pos -= 1
    return pos


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('changelist', help='Path to changelist file')
    parser.add_argument('--repo-root', default='.', help='Root of git repo (default: .)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would change without writing files')
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    changelist_path = Path(args.changelist)

    print(f'Reading changelist: {changelist_path}')
    with open(changelist_path, 'r', encoding='utf-8') as f:
        changelist_text = f.read()

    try:
        entries = parse_changelist(changelist_text)
    except ValueError as e:
        print(f'ERROR parsing changelist: {e}')
        sys.exit(1)

    print(f'  {len(entries)} entries parsed')

    # Group by file to avoid re-reading/re-writing the same file per entry
    from collections import defaultdict
    entries_by_file = defaultdict(list)
    for entry in entries:
        entries_by_file[entry['file']].append(entry)

    any_error = False

    for rel_path, file_entries in entries_by_file.items():
        target_path = repo_root / rel_path

        if not target_path.exists():
            print(f'ERROR: File not found: {target_path}')
            any_error = True
            continue

        print(f'\nProcessing: {rel_path}')

        # Load with separator stripping — normalises files regardless of
        # whether they previously used ---, -----, or no separators.
        lines = load_file(target_path)

        for entry in file_entries:
            section_id = (f'{entry["parent"]} > {entry["section"]}'
                          if entry['parent'] else entry['section'])
            try:
                exists = _section_exists(lines, entry)
                new_lines = apply_entry(lines, entry)
                action = 'UPDATE' if exists else 'INSERT'
                print(f'  {action}: {section_id}')
                lines = new_lines
            except ValueError as e:
                print(f'  ERROR ({section_id}): {e}')
                any_error = True
                # Loud failure: stop processing this file
                break

        if not any_error:
            if args.dry_run:
                import difflib
                original_lines = []
                with open(target_path, 'r', encoding='utf-8') as f:
                    original_lines = f.readlines()
                normalised = normalise_blank_lines(lines)
                normalised = insert_h2_separators(normalised)
                diff = list(difflib.unified_diff(
                    original_lines,
                    normalised,
                    fromfile=f'a/{rel_path}',
                    tofile=f'b/{rel_path}',
                ))
                if diff:
                    print(f'  [dry-run] diff for {rel_path}:')
                    print(''.join(diff), end='')
                else:
                    print(f'  [dry-run] No changes to {rel_path}')
            else:
                save_file(target_path, lines)
                print(f'  Written: {target_path}')

    if any_error:
        print('\nCompleted with errors — some entries were not applied.')
        sys.exit(1)
    else:
        print('\nDone.')


def _section_exists(lines, entry):
    """Check whether the target section already exists (for action labelling)."""
    if entry['section_level'] == 2:
        return find_heading_line(lines, entry['section']) is not None
    h2_line = find_heading_line(lines, entry['parent'])
    if h2_line is None:
        return False
    h2_end = find_section_end(lines, h2_line, level=2)
    return find_heading_line(lines, entry['section'], h2_line + 1, h2_end) is not None


if __name__ == '__main__':
    main()

```

## generate_links.py

```python
#!/usr/bin/env python3
"""Generate LINKS.md with jsDelivr URLs pinned to the given commit hash."""

import sys

REPO = "mattachu/claude-expedition33"
HASH = sys.argv[1][:8]
BASE = f"https://cdn.jsdelivr.net/gh/{REPO}@{HASH}"

FILES = [
    # Overview
    "overview/claude-expedition33.md",
    "overview/party-summary.md",
    "overview/pictos-lumina-summary.md",
    # Data
    "data/playthrough.json",
    "data/characters.json",
    "data/skills.json",
    "data/weapons.json",
    "data/pictos-lumina.json",
    # Characters
    "characters/maelle.md",
    "characters/verso.md",
    "characters/sciel.md",
    "characters/lune.md",
    "characters/monoco.md",
    # Reference
    "reference/mechanics.md",
    "reference/pictos-lumina-catalogue.md",
    "reference/historical-errors.md",
    # Scripts
    "scripts/scripts.md",
    # Chat indexes
    "chats/chat0/chat0-index.md",
    "chats/chat1/chat1-index.md",
    "chats/chat2/chat2-index.md",
    "chats/chat3/chat3-index.md",
    "chats/chat4/chat4-index.md",
    "chats/chat5/chat5-index.md",
    "chats/chat6/chat6-index.md",
    "chats/chat7/chat7-index.md",
    "chats/chat8/chat8-index.md",
    # Root
    "repo-structure.md",
    "README.md",
]

lines = [
    "# Session Links",
    "",
    f"*Commit: `{HASH}`*",
    "",
    "Paste this file's content at session start. "
    "Claude fetches files from these URLs on demand.",
    "",
]
for path in FILES:
    lines.append(f"- `{path}`: {BASE}/{path}")

with open("LINKS.md", "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated LINKS.md with hash {HASH}")

```

## generate_pictos_lumina.py

```python
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
        f"*Generated from `pictos-lumina.json`.*",
        "",
        "See [`pictos-lumina-catalogue.md`](pictos-lumina-catalogue.md) for the full list of all 194 Pictos.",
        "",
        "---",
        "",
    ]

    # ── 1. Pictos Mechanics ──────────────────────────────────────────────
    lines += [
        "## 1. Pictos Mechanics",
        "",
        "Pictos are collectible items giving stat boosts and effects. Each character has 3 Pictos slots. Equipping a Pictos applies both its **stat boosts** and its **effect**. After winning 4 battles with a Pictos equipped, it is learnt as a Lumina.",
        "",
        "Higher level Pictos give higher stat boosts. Pictos stat boosts cover Health, Defence, Speed, and Crit only — they do not boost Attack. Attack scaling comes from base stats, weapons, attributes, and Lumina. With attributes maxed at 99, Pictos stat boosts are the primary source of character growth.",
        "",
        "Each Pictos exists as a single unique copy — only one character can equip it at a time. Any other character wanting the same Lumina effect must pay the full LP cost. Finding a duplicate of an already-owned Pictos upgrades the existing copy (increases level and stat boosts) rather than adding a second copy.",
        "",
        "Extra-turn effects (e.g. Quick Break's \"play again on Break\") do not stack — if a character is already on a bonus turn, any further extra-turn trigger is nullified. Quick Break is therefore a pure stat stick for any Cheater user.",
        "",
        "---",
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
        "Passive Lumina effects that trigger \"on turn start\" (e.g. Recovery: 10% health regen) fire on bonus turns granted by Cheater or Intervention, not only on normal turns.",
        "",
        "For status immunity, add the relevant Lumina (e.g. Anti-Blight, 10LP) rather than swapping Pictos. The Pictos stays on its holder for the stat boosts; Lumina is the situational layer.",
        "",
        "**In-game Lumina Sets:** The game allows saving up to 50 Lumina Sets per character. Sets apply a group of Lumina in one action. The recommended workflow is: apply core set first, then add character-specific extras on top.",
        "",
        "---",
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
    lines += ["", "---", ""]

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
    lines += ["", "---", ""]

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

    lines += ["---", ""]

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
    lines += ["", "---", ""]

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
    lines += ["", "---", ""]

    return "\n".join(lines)


def generate_catalogue(data):
    """Generate the full catalogue Markdown."""
    lines = []
    pictos = data.get("pictos", [])

    lines += [
        "# Clair Obscur: Expedition 33 — Pictos Catalogue",
        "",
        f"*Generated from `pictos-lumina.json`.*",
        "",
        "See [`pictos-lumina-summary.md`](pictos-lumina-summary.md) for the Pictos and Lumina currently in use.",
        "",
        f"**{len(pictos)} Pictos total.** {len([p for p in pictos if p.get('obtained')])} obtained.",
        "",
        "---",
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

        lines += ["", "---", ""]

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

```

## generate_scripts_md.py

```python
#!/usr/bin/env python3
"""Generate scripts/scripts.md — a readable listing of all pipeline scripts."""

import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPTS_DIR, "scripts.md")

def main():
    py_files = sorted(
        f for f in os.listdir(SCRIPTS_DIR) if f.endswith(".py")
    )

    lines = ["# Pipeline Scripts\n", "\n"]
    for filename in py_files:
        filepath = os.path.join(SCRIPTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        lines.append(f"## {filename}\n\n")
        lines.append(f"```python\n{content}\n```\n\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Written: {OUTPUT_FILE} ({len(py_files)} scripts)")

if __name__ == "__main__":
    main()

```

## split_transcript.py

```python
#!/usr/bin/env python3
"""
Script 4: Split a completed Markdown transcript into part files.

Usage:
    python scripts/split_transcript.py <transcript> [options]

    <transcript>          Path to full Markdown transcript file
    --sections-per-part   Number of index sections per part file (default: 4)
    --output-dir          Directory for output part files (default: /mnt/user-data/outputs/)
    --chat-name           Display name override, e.g. "Chat 5"; auto-detected from filename if not set

Section markers:
    The transcript must contain markers of the form:
        <!-- SECTION: Title -->
    inserted by Claude during the compound log step, immediately before the first turn
    of each new topic section, following a --- separator.

Split behaviour:
    - One part file per every N section markers (configurable, default 4)
    - The --- separator preceding a section marker stays at the bottom of the
      previous part; the marker and its content open the new part
    - Part files are named <chat_base>-part1.md, <chat_base>-part2.md, etc.
    - Each part file has a header: # <chat_display_name> — Part N: <first_section_title>
"""

import re
import sys
from pathlib import Path
from datetime import date


DEFAULT_OUTPUT_DIR = '/mnt/user-data/outputs/'
DEFAULT_SECTIONS_PER_PART = 4

SECTION_MARKER_RE = re.compile(r'^<!-- SECTION: (.+) -->$')


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def find_section_positions(lines):
    """
    Scan lines for section markers.
    Returns list of (line_index, title) for each marker found.
    """
    positions = []
    for i, line in enumerate(lines):
        m = SECTION_MARKER_RE.match(line.rstrip())
        if m:
            positions.append((i, m.group(1)))
    return positions


def split_into_parts(lines, section_positions, sections_per_part):
    """
    Split lines into parts at every Nth section marker.

    Each part starts at the line of its first section marker.
    The content before the first section marker (e.g. any file-level header)
    is prepended to part 1.

    Returns list of (start_line_index, [section_titles]) tuples,
    where start_line_index is the line where this part's content begins.
    """
    if not section_positions:
        return []

    # Group section positions into chunks of sections_per_part
    part_starts = []
    for i in range(0, len(section_positions), sections_per_part):
        group = section_positions[i:i + sections_per_part]
        start_line = group[0][0]
        titles = [t for _, t in group]
        part_starts.append((start_line, titles))

    return part_starts


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def generate_part_content(lines, part_start, next_part_start, preamble_lines,
                           part_num, chat_display_name, first_title, is_first_part):
    """
    Build the content for a single part file.

    Preamble (content before first section marker) is included in part 1 only.
    Header line is prepended.
    """
    output_lines = []

    # Part header
    output_lines.append(f'# {chat_display_name} — Part {part_num}: {first_title}')
    output_lines.append('')

    # Preamble in part 1 only (skip if empty/whitespace)
    if is_first_part and preamble_lines:
        preamble = '\n'.join(preamble_lines).strip()
        if preamble:
            output_lines.append(preamble)
            output_lines.append('')

    # Body: lines from part_start up to (but not including) next_part_start
    body_lines = lines[part_start:next_part_start]

    # Strip leading blank lines from body (the header provides the gap)
    while body_lines and not body_lines[0].strip():
        body_lines = body_lines[1:]

    # Strip trailing blank lines
    while body_lines and not body_lines[-1].strip():
        body_lines = body_lines[:-1]

    output_lines.extend(body_lines)
    output_lines.append('')  # final newline

    return '\n'.join(output_lines) + '\n'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('transcript', help='Path to full Markdown transcript file')
    parser.add_argument('--sections-per-part', type=int, default=DEFAULT_SECTIONS_PER_PART,
                        help=f'Index sections per part file (default: {DEFAULT_SECTIONS_PER_PART})')
    parser.add_argument('--output-dir', default=DEFAULT_OUTPUT_DIR,
                        help=f'Output directory (default: {DEFAULT_OUTPUT_DIR})')
    parser.add_argument('--chat-name', default=None,
                        help='Display name override, e.g. "Chat 5"')
    args = parser.parse_args()

    transcript_path = Path(args.transcript)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Infer base name and display name from transcript filename
    # e.g. chat5-transcript.md -> chat5, Chat 5
    stem = transcript_path.stem
    chat_name_base = re.sub(r'[-_]transcript$', '', stem, flags=re.IGNORECASE)

    if args.chat_name:
        chat_short_name = args.chat_name
    else:
        auto_match = re.match(r'chat(\d+)', chat_name_base, re.IGNORECASE)
        if auto_match:
            chat_short_name = f'Chat {auto_match.group(1)}'
            print(f'Auto-detected chat name: {chat_short_name}')
        else:
            chat_short_name = chat_name_base
            print(f'WARNING: Could not auto-detect chat name from filename, using: {chat_short_name}')

    chat_display_name = f'Clair Obscur: Expedition 33 — {chat_short_name}'

    # Read transcript
    print(f'Reading transcript: {transcript_path}')
    with open(transcript_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    print(f'  {len(lines)} lines read')

    # Find section markers
    section_positions = find_section_positions(lines)
    print(f'  {len(section_positions)} section markers found')

    if not section_positions:
        print('ERROR: No section markers found. Transcript must contain <!-- SECTION: Title --> markers.')
        sys.exit(1)

    # Preamble: lines before first section marker
    first_marker_line = section_positions[0][0]
    preamble_lines = lines[:first_marker_line]

    # Group into parts
    parts = split_into_parts(lines, section_positions, args.sections_per_part)
    print(f'  {len(parts)} parts ({args.sections_per_part} sections per part)')

    # Write part files
    output_files = []
    for part_num, (start_line, titles) in enumerate(parts, start=1):
        # Determine end of this part's content
        if part_num < len(parts):
            next_start_line = parts[part_num][0]  # parts is 0-indexed here; part_num is 1-indexed
        else:
            next_start_line = len(lines)

        first_title = titles[0]
        is_first_part = (part_num == 1)

        part_content = generate_part_content(
            lines, start_line, next_start_line, preamble_lines,
            part_num, chat_display_name, first_title, is_first_part
        )

        part_filename = output_dir / f'{chat_name_base}-part{part_num}.md'
        with open(part_filename, 'w', encoding='utf-8') as f:
            f.write(part_content)

        section_summary = ', '.join(f'"{t}"' for t in titles)
        size = len(part_content)
        print(f'  Part {part_num}: sections {section_summary} ({size:,} bytes) → {part_filename}')
        output_files.append(part_filename)

    print('\nDone.')
    for f in output_files:
        print(f'  {f}')


if __name__ == '__main__':
    main()

```

## transcript_to_md.py

```python
#!/usr/bin/env python3
"""
Script 2: Convert raw JSON transcript to Markdown.

Two modes:

  CHUNK MODE (original):
    python scripts/transcript_to_md.py <raw_json> <chunk_map> [options]

    Converts the full transcript using a chunk map into part files + skeleton index.
    <raw_json>    Path to raw transcript JSON (e.g. chats/chat2/chat2-raw.json)
    <chunk_map>   Path to chunk map JSON (e.g. chats/chat2/chat2-chunk-map.json)
    --repo-root   Root of the git repo (default: current directory)
    --output-dir  Directory for output files (default: /mnt/user-data/outputs/)
    --push        Commit and push after writing files (uses --repo-root)
    --chat-name   Display name override (e.g. "Chat 2"); auto-detected if not set

  TIMESTAMP MODE (new):
    python scripts/transcript_to_md.py <raw_json> --after-timestamp <ISO> [options]

    Extracts and converts only turns after the given timestamp. Used after compaction
    to reconstruct the portion of the transcript not yet written to the running file.
    <raw_json>         Path to raw transcript JSON
    --after-timestamp  ISO 8601 timestamp (e.g. 2026-03-08T21:45:23.000000Z)
    --append-to        Append output to this file; prints to stdout if omitted

Block rendering rules (both modes):
    - text blocks: rendered as-is (whitespace-only blocks skipped)
    - thinking blocks: omitted
    - tool_use blocks: rendered as italics using 'message' field if present
    - tool_result blocks: rendered using 'message' field if present; otherwise omitted
"""

import json
import re
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone
from datetime import date


DEFAULT_OUTPUT_DIR = '/mnt/user-data/outputs/'


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_blocks(raw):
    """
    Parse H:/A: block format into list of (turn_number, speaker, blocks, first_timestamp) tuples.
    Each block is a dict with at minimum a 'type' field.
    first_timestamp is a datetime parsed from the first block's start_timestamp, or None.
    """
    sections = re.split(r'={20,}', raw)
    turns = []
    turn_number = 0

    for section in sections:
        section = section.strip()
        if not section:
            continue

        if re.match(r'(?i)^(human|h)\s*:', section):
            speaker = 'H'
        elif re.match(r'(?i)^(assistant|a)\s*:', section):
            speaker = 'A'
        else:
            continue

        # Extract JSON content array
        content_match = re.search(r'Content\s*:\s*(\[.*)', section, re.DOTALL)
        if content_match:
            try:
                blocks = json.loads(content_match.group(1))
            except json.JSONDecodeError as e:
                print(f'WARNING: JSON parse error in turn {turn_number + 1}: {e}', file=sys.stderr)
                blocks = []
        else:
            blocks = []

        # Extract first timestamp
        first_timestamp = None
        for block in blocks:
            if isinstance(block, dict) and block.get('start_timestamp'):
                first_timestamp = parse_iso_timestamp(block['start_timestamp'])
                break

        turn_number += 1
        turns.append((turn_number, speaker, blocks, first_timestamp))

    return turns


def parse_iso_timestamp(ts_str):
    """Parse ISO 8601 timestamp string to timezone-aware datetime. Handles Z suffix."""
    if ts_str.endswith('Z'):
        ts_str = ts_str[:-1] + '+00:00'
    try:
        return datetime.fromisoformat(ts_str)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Block rendering
# ---------------------------------------------------------------------------

def render_blocks(speaker, blocks):
    """
    Convert a list of content blocks into Markdown text.
    Returns None if there is no renderable content.
    """
    parts = []

    for block in blocks:
        if not isinstance(block, dict):
            continue

        block_type = block.get('type', '')

        if block_type == 'text':
            text = block.get('text', '').strip()
            if text:
                parts.append(text)

        elif block_type == 'thinking':
            pass  # omit

        elif block_type == 'tool_use':
            message = (block.get('message') or '').strip()
            if message:
                parts.append(f'*{message}*')

        elif block_type == 'tool_result':
            message = (block.get('message') or '').strip()
            if message:
                parts.append(f'*{message}*')

        # All other block types: omit

    if not parts:
        return None

    return '\n\n'.join(parts)


# ---------------------------------------------------------------------------
# Markdown generation — chunk mode
# ---------------------------------------------------------------------------

def format_speaker(speaker):
    return '**Matt:**' if speaker == 'H' else '**Claude:**'


def generate_part_md(part_info, turns_in_part, chat_name):
    """Generate full Markdown content for a single part file."""
    part_num = part_info['part']
    title = part_info['title']

    lines = [
        f'# {chat_name} — Part {part_num}: {title}',
        '',
    ]

    for turn_num, speaker, blocks, _ts in turns_in_part:
        rendered = render_blocks(speaker, blocks)
        if rendered is None:
            continue

        lines.append(f'{format_speaker(speaker)} {rendered}')
        lines.append('')
        lines.append('---')
        lines.append('')

    # Remove trailing separator if present
    while lines and lines[-1] in ('', '---'):
        lines.pop()

    return '\n'.join(lines) + '\n'


def generate_index_md(chat_name, chat_dir_name, parts_info, repo_url):
    """Generate skeleton index file with part links and blank section descriptions."""
    lines = [
        f'# {chat_name}',
        '',
        f'Chat between Matt and Claude.',
        '',
        '## Part Files',
        '',
    ]

    for part in parts_info:
        part_num = part['part']
        title = part['title']
        filename = f'{chat_dir_name}-part{part_num}.md'
        raw_url = f'{repo_url}/raw/main/chats/{chat_dir_name}/{filename}'
        formatted_url = f'{repo_url}/blob/main/chats/{chat_dir_name}/{filename}'
        lines.append(f'* Part {part_num} — {title}: [Formatted]({formatted_url}) / [Raw]({raw_url})')

    lines.append('')
    lines.append('## Table of Contents')
    lines.append('')

    for part in parts_info:
        part_num = part['part']
        title = part['title']
        filename = f'{chat_dir_name}-part{part_num}.md'
        formatted_url = f'{repo_url}/blob/main/chats/{chat_dir_name}/{filename}'
        lines.append(f'### [Part {part_num}: {title}]({formatted_url})')
        lines.append('')
        lines.append('*[Section descriptions to be added]*')
        lines.append('')

    lines.append('---')
    lines.append(f'*Generated: {date.today().isoformat()}*')

    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# Markdown generation — timestamp mode
# ---------------------------------------------------------------------------

def generate_timestamp_md(turns_after):
    """
    Generate Markdown for turns after a given timestamp.
    Format matches the running transcript: **Speaker:** content, separated by ---.
    Returns empty string if no renderable turns.
    """
    lines = []

    for turn_num, speaker, blocks, _ts in turns_after:
        rendered = render_blocks(speaker, blocks)
        if rendered is None:
            continue

        if lines:
            lines.append('')
            lines.append('---')
            lines.append('')

        lines.append(f'{format_speaker(speaker)} {rendered}')

    if not lines:
        return ''

    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# Git operations
# ---------------------------------------------------------------------------

def git_run(args, cwd):
    """Run a git command, print output, raise on failure."""
    result = subprocess.run(
        ['git'] + args,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    if result.returncode != 0:
        raise RuntimeError(f'git {" ".join(args)} failed with code {result.returncode}')


def commit_and_push(repo_root, files, chat_name):
    """Stage specified files, commit, and push."""
    print('\nCommitting and pushing...')
    for f in files:
        git_run(['add', str(f)], cwd=repo_root)
    git_run(['commit', '-m', f'Add {chat_name} Markdown transcript files'], cwd=repo_root)
    git_run(['push'], cwd=repo_root)
    print('Done.')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('raw_json', help='Path to raw transcript JSON')
    parser.add_argument('chunk_map', nargs='?', default=None,
                        help='Path to chunk map JSON (chunk mode only)')

    # Chunk mode options
    parser.add_argument('--repo-root', default='.',
                        help='Root of git repo (default: .)')
    parser.add_argument('--output-dir', default=DEFAULT_OUTPUT_DIR,
                        help=f'Output directory for part/index files (default: {DEFAULT_OUTPUT_DIR})')
    parser.add_argument('--push', action='store_true',
                        help='Commit and push after writing files (chunk mode only)')
    parser.add_argument('--chat-name', default=None,
                        help='Display name override, e.g. "Chat 2"')

    # Timestamp mode options
    parser.add_argument('--after-timestamp', default=None, metavar='ISO',
                        help='Timestamp mode: extract turns after this ISO 8601 timestamp')
    parser.add_argument('--append-to', default=None, metavar='FILE',
                        help='Timestamp mode: append output to this file (default: stdout)')

    args = parser.parse_args()

    # -----------------------------------------------------------------------
    # Mode determination
    # -----------------------------------------------------------------------
    if args.after_timestamp is not None:
        run_timestamp_mode(args)
    elif args.chunk_map is not None:
        run_chunk_mode(args)
    else:
        parser.error('chunk_map is required unless --after-timestamp is specified')


def run_timestamp_mode(args):
    raw_json_path = Path(args.raw_json)

    # Parse anchor timestamp
    anchor = parse_iso_timestamp(args.after_timestamp)
    if anchor is None:
        print(f'ERROR: Could not parse timestamp: {args.after_timestamp}', file=sys.stderr)
        sys.exit(1)

    print(f'Reading transcript: {raw_json_path}', file=sys.stderr)
    with open(raw_json_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    print('Parsing transcript...', file=sys.stderr)
    turns = parse_blocks(raw)
    print(f'  {len(turns)} turns parsed', file=sys.stderr)

    # Filter to turns strictly after anchor.
    # Contract: each turn is identified by the start_timestamp of its FIRST content block.
    # The session state's last_write_timestamp must record that same field for the last
    # turn written — any other timestamp risks missing a turn or duplicating one.
    turns_after = [t for t in turns if t[3] is not None and t[3] > anchor]
    print(f'  {len(turns_after)} turns after {args.after_timestamp}', file=sys.stderr)

    if not turns_after:
        print('  No turns to output.', file=sys.stderr)
        return

    md = generate_timestamp_md(turns_after)

    if args.append_to:
        out_path = Path(args.append_to)
        with open(out_path, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write(md)
        print(f'  Appended to {out_path}', file=sys.stderr)
    else:
        sys.stdout.write(md)


def run_chunk_mode(args):
    repo_root = Path(args.repo_root).resolve()
    raw_json_path = Path(args.raw_json)
    chunk_map_path = Path(args.chunk_map)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Infer chat directory name and base name from raw JSON path
    chat_dir = raw_json_path.parent
    chat_name_base = raw_json_path.stem.replace('-raw', '')  # e.g. 'chat2'

    # Determine display name
    if args.chat_name:
        chat_short_name = args.chat_name
    else:
        auto_match = re.match(r'chat(\d+)', chat_name_base, re.IGNORECASE)
        if auto_match:
            chat_short_name = f'Chat {auto_match.group(1)}'
            print(f'Auto-detected chat name: {chat_short_name}')
        else:
            chat_short_name = chat_name_base
            print(f'WARNING: Could not auto-detect chat name from filename, using: {chat_short_name}')

    chat_display_name = f'Clair Obscur: Expedition 33 — {chat_short_name}'

    # GitHub repo URL — infer from git remote
    try:
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            cwd=repo_root, capture_output=True, text=True
        )
        remote_url = result.stdout.strip()
        if remote_url.startswith('git@github.com:'):
            remote_url = remote_url.replace('git@github.com:', 'https://github.com/')
            remote_url = remote_url.rstrip('.git')
        elif remote_url.endswith('.git'):
            remote_url = remote_url[:-4]
    except Exception:
        remote_url = 'https://github.com/mattachu/claude-expedition33'
        print(f'WARNING: Could not infer repo URL, using default: {remote_url}')

    # Load inputs
    print(f'Reading transcript: {raw_json_path}')
    with open(raw_json_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    print(f'Reading chunk map: {chunk_map_path}')
    with open(chunk_map_path, 'r', encoding='utf-8') as f:
        chunk_map = json.load(f)

    # Parse transcript
    print('Parsing transcript...')
    turns = parse_blocks(raw)
    print(f'  {len(turns)} turns parsed')

    # Build turn lookup by turn number
    turn_lookup = {t[0]: t for t in turns}

    # Generate part files
    output_files = []

    for part_info in chunk_map:
        part_num = part_info['part']
        start = part_info['start_turn']
        end = part_info['end_turn']
        title = part_info['title']

        turns_in_part = [turn_lookup[i] for i in range(start, end + 1) if i in turn_lookup]

        md_content = generate_part_md(part_info, turns_in_part, chat_display_name)

        part_filename = output_dir / f'{chat_name_base}-part{part_num}.md'
        with open(part_filename, 'w', encoding='utf-8') as f:
            f.write(md_content)

        size = len(md_content)
        print(f'  Part {part_num}: {title} (turns {start}–{end}, {size:,} bytes) → {part_filename}')
        output_files.append(part_filename)

    # Generate index file
    index_content = generate_index_md(
        chat_display_name,
        chat_name_base,
        chunk_map,
        remote_url
    )
    index_filename = output_dir / f'{chat_name_base}-index.md'
    with open(index_filename, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f'  Index skeleton → {index_filename}')
    output_files.append(index_filename)

    # Optionally commit and push
    if args.push:
        commit_and_push(repo_root, output_files, chat_name_base)
    else:
        print('\nFiles written. Run with --push to commit and push.')
        for f in output_files:
            print(f'  {f}')


if __name__ == '__main__':
    main()

```

## turn_index.py

```python
#!/usr/bin/env python3
"""
Script 1: Generate turn index from Claude.ai transcript.

Usage:
    python script1_turn_index.py <transcript_file> [output_file]

Input:  Raw transcript file exported from Claude.ai (JSON or block format)
Output: Lightweight turn index text file for pasting to Claude to get chunk map

The output format is:
    TURN INDEX
    ============================================================
      1  H  Hi Claude…
      2  A  Hi Matt! To get started properly…
      3  H  matteaston.net/claude…
    ...
    Total turns: N
"""

import json
import sys
import re
from pathlib import Path


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------

def extract_preview(content_blocks, max_words=20):
    """Get first N words from the first non-empty text block."""
    if isinstance(content_blocks, str):
        words = content_blocks.split()
        preview = ' '.join(words[:max_words])
        return preview + ('…' if len(words) > max_words else '')

    for block in content_blocks:
        if not isinstance(block, dict):
            continue
        if block.get('type') == 'text':
            text = block.get('text', '').strip()
            if text:
                words = text.split()
                preview = ' '.join(words[:max_words])
                return preview + ('…' if len(words) > max_words else '')
        # Some formats nest content differently
        if block.get('type') == 'thinking':
            # Use summary if available, otherwise skip
            summaries = block.get('summaries', [])
            if summaries and isinstance(summaries[0], dict):
                return '[thinking: ' + summaries[0].get('summary', '') + ']'

    return '[no text content]'


# ---------------------------------------------------------------------------
# Format parsers
# ---------------------------------------------------------------------------

def try_pure_json(raw):
    """
    Try to parse as a pure JSON object.
    Handles several possible top-level shapes:
      - List of turn objects with 'role' field
      - Dict with a 'messages' or 'turns' key
    Returns list of (speaker, content_blocks) or None if unrecognised.
    """
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None

    # Shape 1: top-level list of turns
    if isinstance(data, list) and data and isinstance(data[0], dict):
        if 'role' in data[0] or 'type' in data[0]:
            turns = []
            for item in data:
                role = item.get('role', '')
                speaker = 'H' if role in ('human', 'user') else 'A'
                content = item.get('content', item.get('text', ''))
                turns.append((speaker, content))
            return turns if turns else None

    # Shape 2: dict with messages key
    if isinstance(data, dict):
        for key in ('messages', 'turns', 'conversation'):
            if key in data and isinstance(data[key], list):
                return try_pure_json(json.dumps(data[key]))

    return None


def try_block_format(raw):
    """
    Parse the H:/A: block format produced by Claude.ai transcript exports.

    Each block looks like:
        Human:
        Content:
        [
          { "type": "text", "text": "..." },
          ...
        ]
        ================================================================================

    or the same with 'A:' / 'Assistant:'.
    """
    blocks = re.split(r'={20,}', raw)
    turns = []

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Identify speaker
        if re.match(r'(?i)^(human|h)\s*:', block):
            speaker = 'H'
        elif re.match(r'(?i)^(assistant|a)\s*:', block):
            speaker = 'A'
        else:
            continue

        # Extract JSON content array
        content_match = re.search(r'Content\s*:\s*(\[.*)', block, re.DOTALL)
        if content_match:
            try:
                content = json.loads(content_match.group(1))
                preview = extract_preview(content)
            except json.JSONDecodeError:
                # Try to find just the first text value
                text_match = re.search(r'"text"\s*:\s*"([^"]{0,200})', block)
                preview = text_match.group(1) + '…' if text_match else '[parse error]'
        else:
            # No Content: block — try to find any text directly
            text_match = re.search(r'"text"\s*:\s*"([^"]{0,200})', block)
            preview = text_match.group(1) + '…' if text_match else '[no content found]'

        turns.append((speaker, preview))

    return turns if turns else None


# ---------------------------------------------------------------------------
# Main parse dispatcher
# ---------------------------------------------------------------------------

def parse_transcript(filepath):
    """Try each parser in order, return list of (speaker, preview) tuples."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    print(f'File size: {len(raw):,} bytes')

    # Try pure JSON first
    turns = try_pure_json(raw)
    if turns:
        print('Parsed as: pure JSON format')
        return turns

    # Try block format
    turns = try_block_format(raw)
    if turns:
        print('Parsed as: H:/A: block format')
        return turns

    # Failed
    print('ERROR: Could not parse file. First 500 chars for diagnosis:')
    print(raw[:500])
    return None


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_index(turns, output_path):
    lines = [
        'TURN INDEX',
        '=' * 60,
        '',
    ]

    for i, (speaker, preview) in enumerate(turns, 1):
        # Clean up whitespace and newlines in preview
        preview_clean = re.sub(r'\s+', ' ', preview).strip()
        lines.append(f'{i:3}  {speaker}  {preview_clean}')

    lines.append('')
    lines.append(f'Total turns: {len(turns)}')

    output = '\n'.join(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'\nTurn index written to: {output_path}')
    print(f'Total turns: {len(turns)}')
    print(f'Output size: {len(output):,} bytes')
    print('\nFirst 10 turns:')
    for line in lines[3:13]:
        print(' ', line)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f'ERROR: File not found: {input_path}')
        sys.exit(1)

    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix('.index.txt')

    turns = parse_transcript(input_path)
    if not turns:
        print('\nERROR: No turns extracted. Paste error output + first 500 chars of file to Claude.')
        sys.exit(1)

    write_index(turns, output_path)

```

