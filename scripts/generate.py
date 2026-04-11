#!/usr/bin/env python3
"""
generate.py — Regenerate all GENERATED: blocks in Markdown files from JSON data.

Reads JSON source-of-truth files and updates:
  - GENERATED: regions in characters/*.md
  - GENERATED: regions in overview/claude-expedition33.md
  - overview/party-summary.md            (fully generated)
  - overview/pictos-lumina-summary.md    (fully generated)
  - reference/pictos-lumina-catalogue.md (fully generated)

Usage (standalone):
    python3 scripts/generate.py [--repo-root .] [--no-interactive] [--dry-run]

Import and call from apply_changelist.py:
    import subprocess, sys
    subprocess.run([sys.executable, 'scripts/generate.py',
                    '--repo-root', repo_root, '--no-interactive'], check=True)
"""

import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CHARACTERS = ['Maelle', 'Verso', 'Sciel', 'Lune', 'Monoco']
MAIN_TEAM = {'Maelle', 'Verso', 'Sciel'}
RESERVE_TEAM = {'Lune', 'Monoco'}

GENERATED_RE = re.compile(
    r'<!-- GENERATED:START (\S+) -->\n(.*?)<!-- GENERATED:END -->',
    re.DOTALL
)

CATEGORY_NAMES = {
    "ap": "AP and Energy", "break": "Break", "burn": "Burn",
    "critical": "Critical Hit", "damage": "Damage Modifiers",
    "death": "Death Effects", "gradient": "Gradient Charge",
    "healing": "Healing", "mark": "Mark", "combat": "Combat Flow",
    "solo": "Solo and Last Stand", "survival": "Survival and Defence",
    "support": "Buffs and Support", "shots": "Free Aim and Shots",
    "misc": "Miscellaneous",
}

CATEGORY_ORDER = [
    "ap", "break", "burn", "critical", "damage", "death",
    "gradient", "healing", "mark", "combat", "solo", "survival",
    "support", "shots", "misc",
]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_data(repo_root):
    d = Path(repo_root) / 'data'
    return {
        'characters': load_json(d / 'characters.json'),
        'pictos_lumina': load_json(d / 'pictos-lumina.json'),
        'weapons': load_json(d / 'weapons.json'),
        'skills': load_json(d / 'skills.json'),
        'playthrough': load_json(d / 'playthrough.json'),
    }


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_pictos(data, interactive=True):
    """Cross-check characters.json pictos_equipped vs pictos-lumina.json equipped_by."""
    characters = data['characters']
    pictos_list = data['pictos_lumina']['pictos']

    # equipped_by from pictos-lumina.json
    equipped_by = {p['name']: p['equipped_by']
                   for p in pictos_list if p.get('equipped_by')}

    # pictos_equipped from characters.json
    pictos_equipped = {}
    for char_name, char in characters.items():
        for p in char.get('pictos_equipped', []):
            pictos_equipped[p] = char_name

    conflicts = []
    seen = set()

    for name, char_pl in equipped_by.items():
        seen.add(name)
        char_ch = pictos_equipped.get(name)
        if char_ch != char_pl:
            conflicts.append({'pictos': name,
                               'pictos_lumina_says': char_pl,
                               'characters_says': char_ch})

    for name, char_ch in pictos_equipped.items():
        if name not in seen:
            conflicts.append({'pictos': name,
                               'pictos_lumina_says': None,
                               'characters_says': char_ch})

    if not conflicts:
        return True

    print(f'\n{len(conflicts)} Pictos assignment conflict(s):')
    for c in conflicts:
        print(f'  {c["pictos"]}:')
        print(f'    pictos-lumina.json equipped_by  = {c["pictos_lumina_says"]}')
        print(f'    characters.json  pictos_equipped = {c["characters_says"]}')

    if not interactive:
        print('\nERROR: Resolve conflicts before running generate.py.')
        return False

    print('\n[1] Use pictos-lumina.json (equipped_by) as source of truth')
    print('[2] Use characters.json (pictos_equipped) as source of truth')
    print('[3] Abort')
    choice = input('Choice: ').strip()

    if choice == '3':
        return False

    if choice == '1':
        for c in conflicts:
            name, correct = c['pictos'], c['pictos_lumina_says']
            wrong = c['characters_says']
            if wrong and wrong in characters:
                eq = characters[wrong].get('pictos_equipped', [])
                if name in eq:
                    eq.remove(name)
            if correct and correct in characters:
                eq = characters[correct].setdefault('pictos_equipped', [])
                if name not in eq:
                    eq.append(name)
        print('  Applied: characters.json updated to match pictos-lumina.json')

    elif choice == '2':
        for c in conflicts:
            name, correct = c['pictos'], c['characters_says']
            for p in data['pictos_lumina']['pictos']:
                if p['name'] == name:
                    p['equipped_by'] = correct
                    break
        print('  Applied: pictos-lumina.json updated to match characters.json')

    return True


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def _cell(v):
    return str(v) if v is not None else '—'


def md_table(headers, rows):
    """Build a Markdown pipe table."""
    col_w = [len(h) for h in headers]
    str_rows = []
    for row in rows:
        sr = [_cell(v) for v in row]
        str_rows.append(sr)
        for i, v in enumerate(sr):
            col_w[i] = max(col_w[i], len(v))

    def fmt(cells):
        return '| ' + ' | '.join(c.ljust(col_w[i]) for i, c in enumerate(cells)) + ' |'

    sep = '|' + '|'.join('-' * (w + 2) for w in col_w) + '|'
    lines = [fmt(headers), sep] + [fmt(r) for r in str_rows]
    return '\n'.join(lines) + '\n'


def pictos_lookup(pictos_lumina):
    return {p['name']: p for p in pictos_lumina.get('pictos', [])}


# ---------------------------------------------------------------------------
# Per-character GENERATED block generators
# ---------------------------------------------------------------------------

def gen_attributes(char_name, char):
    """Attributes table: Attribute | Value. Sorted by value descending, Level first."""
    level = char.get('level', '?')
    attrs = char.get('attributes', {})
    all_attrs = ['vitality', 'might', 'agility', 'defence', 'luck']
    sorted_attrs = sorted(all_attrs, key=lambda a: -attrs.get(a, 0))
    rows = [['Level', level]]
    for a in sorted_attrs:
        rows.append([a.capitalize(), attrs.get(a, 0)])
    return md_table(['Attribute', 'Value'], rows)

def gen_stats(char_name, char):
    """Stats table: Stat | Base | Modified."""
    base = char.get('stats_base') or {}
    mod = char.get('stats_modified') or {}
    note = mod.get('_note', '')

    stat_names = [('health', 'Health'), ('attack', 'Attack'), ('speed', 'Speed'),
                  ('defence', 'Defence'), ('crit', 'Crit')]

    rows = []
    for key, label in stat_names:
        b = base.get(key)
        m = mod.get(key)
        rows.append([label,
                      str(b) if b is not None else '*[unknown]*',
                      str(m) if m is not None else '*[unknown]*'])

    table = md_table(['Stat', 'Base', 'Modified'], rows)
    if note:
        return f'*{note}*\n\n' + table
    return table


def gen_pictos(char_name, char, plu):
    """Pictos table with stat bonuses and effects from pictos-lumina.json."""
    equipped = char.get('pictos_equipped', [])
    rows = []
    for i, name in enumerate(equipped, 1):
        p = plu.get(name, {})
        level = p.get('level', '?')
        effect = p.get('effect', '')
        stats = p.get('stats', {})
        stat_parts = []
        for k in ('health', 'speed', 'defence', 'crit'):
            if k in stats:
                stat_parts.append(f'{k.capitalize()} +{stats[k]}')
        stat_str = ', '.join(stat_parts) or '—'
        rows.append([i, name, level, stat_str, effect])
    return md_table(['Slot', 'Pictos', 'Level', 'Stat Bonus', 'Effect'], rows)


def gen_lp(char_name, char):
    """LP budget block."""
    total = char.get('lp_total', '?')
    used = char.get('lp_used', '?')
    spare = (total - used) if isinstance(total, int) and isinstance(used, int) else '?'
    return (f'- **Current capacity:** {total} LP\n'
            f'- **Used:** {used} LP\n'
            f'- **Spare:** {spare} LP\n')


def gen_lumina(char_name, char, pictos_lumina, plu):
    """Lumina loadout table."""
    is_main = char_name in MAIN_TEAM
    core_key = 'main_team' if is_main else 'reserve_team'
    core_entries = (pictos_lumina.get('core_lumina_suite', {})
                    .get(core_key, {}).get('entries', []))

    pictos_equipped = set(char.get('pictos_equipped', []))
    exclusion_names = {e['name'] for e in char.get('lumina_core_exclusions', [])}

    rows = []

    for entry in core_entries:
        name = entry['name']
        lp = entry.get('lp', '?')
        core_note = entry.get('notes', '')
        if name in pictos_equipped:
            rows.append([name, '—', f'FREE from {name} Pictos'])
        elif name in exclusion_names:
            continue  # omit non-functional exclusions
        else:
            # Filter notes prefixed with another character's name
            if core_note and ':' in core_note:
                prefix = core_note.split(':')[0].strip()
                if prefix in CHARACTERS and prefix != char_name:
                    core_note = ''
            rows.append([name, lp, core_note])

    # Character-specific extras
    for extra in char.get('lumina_extras', []):
        name = extra['name']
        note = extra.get('notes', extra.get('note', ''))
        if name in pictos_equipped:
            rows.append([name, '—', f'FREE from {name} Pictos'])
        else:
            lp = plu.get(name, {}).get('lp_cost', '?')
            rows.append([name, lp, note])

    rows.sort(key=lambda r: r[0])
    return md_table(['Lumina', 'LP', 'Notes'], rows)


# ---------------------------------------------------------------------------
# Skills tables — character-specific columns
# ---------------------------------------------------------------------------

def _ap_str(skill):
    """Return AP cost string, with optional adjusted cost in brackets.

    Uses the standardised `ap_adjusted` field (e.g. "2 in Virtuose",
    "5 at Rank B", "0 in Agile") if present.
    """
    ap = skill.get('ap')
    base = str(ap) if ap is not None else '—'
    adjusted = skill.get('ap_adjusted')
    return f'{base} ({adjusted})' if adjusted else base


def _maelle_extra(skill):
    return [skill.get('stance_change') or '—']


def _verso_extra(skill):
    rb = skill.get('rank_bonus')
    return [f'{rb["rank"]}: {rb["effect"]}' if rb else '—']


def _sciel_extra(skill):
    return [skill.get('charge') or '—']


def _lune_extra(skill):
    stains = skill.get('stains_generated') or []
    return [', '.join(stains) if stains else '—']


def _monoco_extra(skill):
    wheel = skill.get('wheel')
    mask = skill.get('mask') or '?'
    # Handle ap_on_mask for Abbest Wind (0 AP on Agile mask)
    ap_on_mask = skill.get('ap_on_mask', {})
    wheel_str = f'+{wheel}' if isinstance(wheel, int) else (str(wheel) if wheel else '?')
    return [wheel_str, mask]


SKILL_CONFIG = {
    'Maelle': {
        'headers': ['Skill', 'AP', 'Stance', 'Equipped', 'Notes'],
        'extra_fn': _maelle_extra,
    },
    'Verso': {
        'headers': ['Skill', 'AP', 'Rank Bonus', 'Equipped', 'Notes'],
        'extra_fn': _verso_extra,
    },
    'Sciel': {
        'headers': ['Skill', 'AP', 'Charge', 'Equipped', 'Notes'],
        'extra_fn': _sciel_extra,
    },
    'Lune': {
        'headers': ['Skill', 'AP', 'Stains Generated', 'Equipped', 'Notes'],
        'extra_fn': _lune_extra,
    },
    'Monoco': {
        'headers': ['Skill', 'AP', 'Wheel', 'Mask', 'Equipped', 'Notes'],
        'extra_fn': _monoco_extra,
    },
}


def gen_skills(char_name, char, skills_data):
    """Skills table with character-specific columns."""
    cfg = SKILL_CONFIG[char_name]
    char_skills = {s['name']: s for s in skills_data.get(char_name, [])}

    equipped_set = set(char.get('skills_equipped', []))
    learned = char.get('skills_learned', [])

    # Equipped first, then unequipped
    ordered = [s for s in learned if s in equipped_set] + \
              [s for s in learned if s not in equipped_set]

    rows = []
    for name in ordered:
        skill = char_skills.get(name, {})
        ap = _ap_str(skill)
        extras = cfg['extra_fn'](skill)
        mark = '✅' if name in equipped_set else '❌'
        desc = skill.get('description', '')
        rows.append([name, ap] + extras + [mark, desc])

    equipped_names = ', '.join(s for s in learned if s in equipped_set)
    header_line = f'**Currently equipped ({len(equipped_set)}):** {equipped_names}\n\n'
    return header_line + md_table(cfg['headers'], rows)


def gen_gradients(char_name, char):
    """Gradient skills table."""
    rows = []
    for g in char.get('gradient_skills', []):
        rows.append([
            g.get('name', '?'),
            g.get('cost', '?'),
            '✅' if g.get('unlocked') else '❌',
            g.get('effect', ''),
        ])
    return md_table(['Gradient Skill', 'Gradient Cost', 'Acquired', 'Notes'], rows)


def gen_weapon(char_name, weapon_name, weapons_data):
    """Weapon stats block."""
    weapon = next(
        (w for w in weapons_data.get(char_name, []) if w['name'] == weapon_name),
        None
    )
    if not weapon:
        return f'*Weapon not found: {weapon_name}*\n'

    power = weapon.get('power')
    lines = [
        f'- **Name:** {weapon_name} ({weapon.get("level", "?")})',
        f'- **Power:** {power if power is not None else "*[unknown]*"}',
        f'- **Element:** {weapon.get("element") or "*[unknown]*"}',
        f'- **Scaling:** {weapon.get("scaling") or "*[unknown]*"}',
        '- **Effects:**',
    ]
    for eff in weapon.get('effects', []):
        desc = eff.get('description') or '*[unknown]*'
        lines.append(f'    - Level {eff["level"]}: {desc}')
    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# Overview GENERATED block generators
# ---------------------------------------------------------------------------

def gen_playthrough_summary(playthrough, characters):
    act = playthrough.get('act', '?')
    phase = playthrough.get('phase', '?')
    area = playthrough.get('current_area', '?')
    char_levels = [f'{n} L{characters[n]["level"]}'
                   for n in CHARACTERS if n in characters]
    return (
        '- **Platform:** Xbox Series X\n'
        '- **Current playthrough:** First playthrough\n'
        '- **Progress:**\n'
        f'  - Act {act}, Phase {phase}.\n'
        f'  - Characters: {", ".join(char_levels)}.\n'
        f'  - Current area: {area}.\n'
    )


def gen_party_list(playthrough):
    active = ', '.join(playthrough.get('active_party', []))
    reserve = ', '.join(playthrough.get('reserve_party', []))
    return f'- **Active:** {active}\n- **Reserve:** {reserve}\n'


def gen_inventory(playthrough):
    inv = playthrough.get('inventory', {})
    col = inv.get('colour_of_lumina', '?')
    rec = inv.get('recoats', '?')
    cats = (f'{inv.get("chroma_catalyst", "?")} standard, '
            f'{inv.get("chroma_catalyst_polished", "?")} polished, '
            f'{inv.get("chroma_catalyst_resplendent", "?")} resplendent, '
            f'{inv.get("chroma_catalyst_grandiose", "?")} grandiose, '
            f'{inv.get("chroma_catalyst_perfect", "?")} perfect')
    return (f'- Colour of Lumina: {col}\n'
            f'- Recoats: {rec}\n'
            f'- Chroma Catalysts: {cats}\n')


def gen_lp_summary(characters):
    lines = []
    for name in CHARACTERS:
        if name in characters:
            c = characters[name]
            lines.append(f'- {name}: {c.get("lp_used", "?")}/{c.get("lp_total", "?")}')
    return '\n'.join(lines) + '\n'


def gen_party_table(characters, plu, weapons_data):
    rows = []
    for name in CHARACTERS:
        if name not in characters:
            continue
        char = characters[name]
        wname = char.get('weapon_equipped', '?')
        wlevel = next((w.get('level', '?')
                       for w in weapons_data.get(name, [])
                       if w['name'] == wname), '?')
        rows.append([
            name,
            char.get('level', '?'),
            char.get('role', '?'),
            f'{wname} ({wlevel})',
            ', '.join(char.get('pictos_equipped', [])),
            f'{char.get("lp_used", "?")}/{char.get("lp_total", "?")}',
        ])
    return md_table(['Character', 'Level', 'Role', 'Weapon', 'Pictos', 'LP'], rows)


def gen_core_lumina(pictos_lumina, team):
    """Inline summary for overview Section 5."""
    core = pictos_lumina.get('core_lumina_suite', {}).get(f'{team}_team', {})
    total_lp = core.get('total_lp', '?')
    entries = core.get('entries', [])
    notes_items = [f'{e["name"]} ({e["notes"]})' for e in entries if e.get('notes')]
    names = ', '.join(e['name'] for e in entries)
    line = f'**{total_lp}LP** {names}.'
    if notes_items:
        line += f' Note: {"; ".join(notes_items)}.'
    return line + '\n'


def gen_lumina_core_table(pictos_lumina, team, plu):
    """Full table for pictos-lumina-summary.md."""
    core = pictos_lumina.get('core_lumina_suite', {}).get(f'{team}_team', {})
    total_lp = core.get('total_lp', '?')
    entries = core.get('entries', [])
    char_labels = 'Maelle, Verso, Sciel' if team == 'main' else 'Lune, Monoco'

    notes = core.get('notes', '')
    header = f'**Total: {total_lp} LP** — applied to {char_labels}.\n'
    if notes:
        header += f'\n*{notes}*\n'

    if team == 'main':
        rows = [[e['name'], e.get('lp', '?'),
                 plu.get(e['name'], {}).get('effect', ''),
                 e.get('notes', '')] for e in entries]
        table = md_table(['Lumina', 'LP', 'Effect', 'Notes'], rows)
    else:
        rows = [[e['name'], e.get('lp', '?'),
                 plu.get(e['name'], {}).get('effect', '')] for e in entries]
        table = md_table(['Lumina', 'LP', 'Effect'], rows)

    return header + '\n' + table


def gen_lumina_situational(pictos_lumina, plu):
    """Situational Lumina table for pictos-lumina-summary.md."""
    sit = pictos_lumina.get('situational_lumina', [])
    rows = [[s['name'], s.get('lp', '?'),
             plu.get(s['name'], {}).get('effect', ''),
             s.get('notes', '')] for s in sit]
    return md_table(['Lumina', 'LP', 'Effect', 'Notes'], rows)


def gen_lumina_future(pictos_lumina, plu):
    """Candidates for future review table for pictos-lumina-summary.md."""
    cands = pictos_lumina.get('candidates_for_review', [])
    rows = [[c['name'], c.get('lp', '?'),
             plu.get(c['name'], {}).get('effect', ''),
             c.get('notes', '')] for c in cands]
    return md_table(['Lumina', 'LP', 'Effect', 'Notes'], rows)


def gen_phase_checklist(playthrough):
    # Support both old and new key names
    checklist = (playthrough.get('current_phase_checklist')
                 or playthrough.get('phase_3_checklist', {}))

    labels = {
        'the_reacher': ('The Reacher (Maelle solo) → Lithum weapon, Maelle Level 7, '
                        'Gustave resurrection path'),
        'chromatic_braseleur': 'Chromatic Braseleur (inside The Reacher) — complete (easy)',
        'serpenphare': 'Serpenphare (SE Boat Graveyard)',
        'flying_manor': ('Flying Manor (if too difficult at current level, use Endless Tower '
                         'floors 1–20 first) → Clea\'s Life Pictos, Perfect Chroma Catalyst'),
        'renoir': ('**Renoir (final boss)** — enter Lumière → fight at end of dungeon. '
                   '*[Choose Maelle → "A Life to Paint" → Gustave returns]*. '
                   'Self-nerf: enter with Gaulteram/Medalum, calibrate on earlier fights, '
                   'add back before final save point.'),
    }

    lines = []
    for key, done in checklist.items():
        label = labels.get(key, key.replace('_', ' ').title())
        lines.append(f'- {"✅" if done else "⬜"} {label}')
    return '\n'.join(lines) + '\n'


# ---------------------------------------------------------------------------
# Build generators dict
# ---------------------------------------------------------------------------

def build_generators(data):
    characters = data['characters']
    pictos_lumina = data['pictos_lumina']
    weapons = data['weapons']
    skills = data['skills']
    playthrough = data['playthrough']
    plu = pictos_lookup(pictos_lumina)

    gens = {}

    for name in CHARACTERS:
        if name not in characters:
            continue
        char = characters[name]
        gens[f'characters:{name}:attributes'] = gen_attributes(name, char)
        gens[f'characters:{name}:stats']      = gen_stats(name, char)
        gens[f'characters:{name}:Pictos']     = gen_pictos(name, char, plu)
        gens[f'characters:{name}:LP']         = gen_lp(name, char)
        gens[f'characters:{name}:Lumina']     = gen_lumina(name, char, pictos_lumina, plu)
        gens[f'characters:{name}:skills']     = gen_skills(name, char, skills)
        gens[f'characters:{name}:gradients']  = gen_gradients(name, char)
        for w in weapons.get(name, []):
            gens[f'weapons:{name}:{w["name"]}'] = gen_weapon(name, w['name'], weapons)

    gens['playthrough:summary']             = gen_playthrough_summary(playthrough, characters)
    gens['playthrough:party']               = gen_party_list(playthrough)
    gens['playthrough:inventory']           = gen_inventory(playthrough)
    gens['characters:summary:LP']           = gen_lp_summary(characters)
    gens['characters:summary:party']        = gen_party_table(characters, plu, weapons)
    gens['pictos:core:main']                = gen_core_lumina(pictos_lumina, 'main')
    gens['pictos:core:reserve']             = gen_core_lumina(pictos_lumina, 'reserve')
    gens['lumina:core:main']               = gen_lumina_core_table(pictos_lumina, 'main', plu)
    gens['lumina:core:reserve']            = gen_lumina_core_table(pictos_lumina, 'reserve', plu)
    gens['lumina:situational']             = gen_lumina_situational(pictos_lumina, plu)
    gens['lumina:future']                  = gen_lumina_future(pictos_lumina, plu)
    gens['playthrough:current_phase_checklist'] = gen_phase_checklist(playthrough)
    gens['playthrough:phase_3_checklist']   = gen_phase_checklist(playthrough)  # compat

    return gens


# ---------------------------------------------------------------------------
# File updater (GENERATED blocks)
# ---------------------------------------------------------------------------

def update_file(filepath, generators, dry_run=False):
    """Replace GENERATED blocks in one file. Returns True if changed."""
    path = Path(filepath)
    if not path.exists():
        return False

    content = path.read_text(encoding='utf-8')
    if 'GENERATED:START' not in content:
        return False

    changed = False

    def replace(m):
        nonlocal changed
        key = m.group(1)
        old = m.group(2)
        if key not in generators:
            print(f'  WARNING: no generator for key {key!r} in {path.name}')
            return m.group(0)
        new = generators[key]
        if not new.endswith('\n'):
            new += '\n'
        if new != old:
            changed = True
        return f'<!-- GENERATED:START {key} -->\n{new}<!-- GENERATED:END -->'

    new_content = GENERATED_RE.sub(replace, content)

    if changed:
        if dry_run:
            print(f'  [dry-run] would update: {path}')
        else:
            path.write_text(new_content, encoding='utf-8')
            print(f'  Updated: {path}')
    else:
        print(f'  Unchanged: {path}')

    return changed


# ---------------------------------------------------------------------------
# Fully generated files
# ---------------------------------------------------------------------------

def generate_party_summary(data, out_path, dry_run=False):
    """Generate overview/party-summary.md."""
    characters = data['characters']
    pictos_lumina = data['pictos_lumina']
    weapons = data['weapons']
    playthrough = data['playthrough']
    plu = pictos_lookup(pictos_lumina)

    active = playthrough.get('active_party', [])
    reserve = playthrough.get('reserve_party', [])

    lines = [
        '# Party Summary',
        '',
        '*Generated from JSON data files. Do not edit manually.*',
        '',
        '---',
        '',
        '## Active Party',
        '',
    ]

    for name in active:
        if name not in characters:
            continue
        char = characters[name]
        wname = char.get('weapon_equipped', '?')
        wlevel = next((w.get('level', '?')
                       for w in weapons.get(name, [])
                       if w['name'] == wname), '?')

        mod = char.get('stats_modified') or {}
        base = char.get('stats_base') or {}

        lines += [
            f'### {name}',
            '',
            (f'**Level:** {char.get("level", "?")} | '
             f'**Role:** {char.get("role", "?")} | '
             f'**Weapon:** {wname} ({wlevel})'),
            '',
            md_table(
                ['Stat', 'Base', 'Modified'],
                [['Health',  base.get('health',  '*[unknown]*'), mod.get('health',  '*[unknown]*')],
                 ['Attack',  base.get('attack',  '*[unknown]*'), mod.get('attack',  '*[unknown]*')],
                 ['Speed',   base.get('speed',   '*[unknown]*'), mod.get('speed',   '*[unknown]*')],
                 ['Defence', base.get('defence', '*[unknown]*'), mod.get('defence', '*[unknown]*')],
                 ['Crit',    base.get('crit',    '*[unknown]*'), mod.get('crit',    '*[unknown]*')]],
            ),
            '',
        ]

        pictos_rows = []
        for pname in char.get('pictos_equipped', []):
            p = plu.get(pname, {})
            stats = p.get('stats', {})
            stat_parts = [f'{k.capitalize()} +{v}' for k, v in stats.items()]
            pictos_rows.append([pname, p.get('level', '?'), ', '.join(stat_parts) or '—'])
        if pictos_rows:
            lines.append(md_table(['Pictos', 'Level', 'Stats'], pictos_rows))
            lines.append('')

        # Lumina loadout
        lumina_table = gen_lumina(name, char, pictos_lumina, plu)
        lines.append('**Lumina loadout:**')
        lines.append('')
        lines.append(lumina_table)

        used = char.get('lp_used', '?')
        total = char.get('lp_total', '?')
        lines += [f'**LP:** {used}/{total}', '', '---', '']

    lines += ['## Reserve Party', '']

    for name in reserve:
        if name not in characters:
            continue
        char = characters[name]
        wname = char.get('weapon_equipped', '?')
        wlevel = next((w.get('level', '?')
                       for w in weapons.get(name, [])
                       if w['name'] == wname), '?')

        mod = char.get('stats_modified') or {}
        base = char.get('stats_base') or {}

        lines += [
            f'### {name}',
            '',
            (f'**Level:** {char.get("level", "?")} | '
             f'**Role:** {char.get("role", "?")} | '
             f'**Weapon:** {wname} ({wlevel})'),
            '',
            md_table(
                ['Stat', 'Base', 'Modified'],
                [['Health',  base.get('health',  '*[unknown]*'), mod.get('health',  '*[unknown]*')],
                 ['Attack',  base.get('attack',  '*[unknown]*'), mod.get('attack',  '*[unknown]*')],
                 ['Speed',   base.get('speed',   '*[unknown]*'), mod.get('speed',   '*[unknown]*')],
                 ['Defence', base.get('defence', '*[unknown]*'), mod.get('defence', '*[unknown]*')],
                 ['Crit',    base.get('crit',    '*[unknown]*'), mod.get('crit',    '*[unknown]*')]],
            ),
            '',
        ]

        pictos_rows = []
        for pname in char.get('pictos_equipped', []):
            p = plu.get(pname, {})
            stats = p.get('stats', {})
            stat_parts = [f'{k.capitalize()} +{v}' for k, v in stats.items()]
            pictos_rows.append([pname, p.get('level', '?'), ', '.join(stat_parts) or '—'])
        if pictos_rows:
            lines.append(md_table(['Pictos', 'Level', 'Stats'], pictos_rows))
            lines.append('')

        lumina_table = gen_lumina(name, char, pictos_lumina, plu)
        lines.append('**Lumina loadout:**')
        lines.append('')
        lines.append(lumina_table)

        used = char.get('lp_used', '?')
        total = char.get('lp_total', '?')
        lines += [f'**LP:** {used}/{total}', '', '---', '']

    content = '\n'.join(lines)
    _write_file(Path(out_path), content, dry_run)


def generate_pictos_catalogue(pictos_lumina, out_path, dry_run=False):
    """Generate reference/pictos-lumina-catalogue.md."""
    pictos = pictos_lumina.get('pictos', [])

    def get_cats(p):
        cat = p.get('category', ['misc'])
        return cat if isinstance(cat, list) else [cat]

    def primary_cat(p):
        return get_cats(p)[0]

    def secondary_cats(p):
        cats = get_cats(p)
        return ', '.join(cats[1:]) if len(cats) > 1 else ''

    by_cat = {}
    for p in pictos:
        by_cat.setdefault(primary_cat(p), []).append(p)

    obtained_total = sum(1 for p in pictos if p.get('obtained'))

    lines = [
        '# Clair Obscur: Expedition 33 — Pictos Catalogue',
        '',
        '*Generated from `data/pictos-lumina.json`.*',
        '',
        ('See [`overview/pictos-lumina-summary.md`](../overview/pictos-lumina-summary.md) '
         'for Pictos and Lumina currently in use.'),
        '',
        f'**{len(pictos)} Pictos total.** {obtained_total} obtained.',
        '',
        '---',
        '',
    ]

    for cat in CATEGORY_ORDER:
        entries = by_cat.get(cat, [])
        if not entries:
            continue
        obtained = sum(1 for p in entries if p.get('obtained'))
        cat_name = CATEGORY_NAMES.get(cat, cat.title())
        lines += [
            f'## {cat_name} ({len(entries)} Pictos, {obtained} obtained)',
            '',
            ('|  | Name | Effect | LP | Equipped By | Also in |\n'
             '|--|------|--------|----|-------------|---------|'),
        ]
        for p in sorted(entries, key=lambda x: x['name']):
            lines.append(
                f'| {"✓" if p.get("obtained") else ""} '
                f'| {p["name"]} '
                f'| {p.get("effect", "")} '
                f'| {p.get("lp_cost", "?")} '
                f'| {p.get("equipped_by") or ""} '
                f'| {secondary_cats(p)} |'
            )
        lines += ['', '---', '']

    _write_file(Path(out_path), '\n'.join(lines), dry_run)


def _write_file(path, content, dry_run):
    if dry_run:
        print(f'  [dry-run] would write: {path}')
    else:
        path.write_text(content, encoding='utf-8')
        print(f'  Written: {path}')


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def run_generate(repo_root='.', interactive=True, dry_run=False):
    """Entry point callable from CLI or apply_changelist.py."""
    repo = Path(repo_root).resolve()

    print('Loading data files...')
    try:
        data = load_data(repo)
    except FileNotFoundError as e:
        print(f'ERROR: {e}')
        return False

    print('Validating Pictos assignments...')
    if not validate_pictos(data, interactive=interactive):
        return False

    print(f'Building generators...')
    generators = build_generators(data)
    print(f'  {len(generators)} keys ready')

    # Update character files
    print('\nCharacter files:')
    for name in CHARACTERS:
        update_file(repo / 'characters' / f'{name.lower()}.md', generators, dry_run)

    # Update overview
    print('\nOverview file:')
    update_file(repo / 'overview' / 'claude-expedition33.md', generators, dry_run)

    # Update Pictos/Lumina summary
    print('\nPictos/Lumina summary:')
    update_file(repo / 'overview' / 'pictos-lumina-summary.md', generators, dry_run)

    # Fully generated files
    print('\nGenerating party-summary.md...')
    generate_party_summary(data, repo / 'overview' / 'party-summary.md', dry_run)

    print('Generating pictos-lumina-catalogue.md...')
    generate_pictos_catalogue(
        data['pictos_lumina'],
        repo / 'reference' / 'pictos-lumina-catalogue.md',
        dry_run,
    )

    print('\nDone.')
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--repo-root', default='.',
                        help='Root of git repo (default: current directory)')
    parser.add_argument('--no-interactive', action='store_true',
                        help='Error on conflicts instead of prompting (for CI use)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would change without writing files')
    args = parser.parse_args()

    success = run_generate(
        repo_root=args.repo_root,
        interactive=not args.no_interactive,
        dry_run=args.dry_run,
    )
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
