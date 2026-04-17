#!/usr/bin/env python3
"""
Script 3: Apply a changelist of section replacements and insertions to repo files.

Usage:
    python scripts/apply_changelist.py <changelist> [options]

    <changelist>    Path to changelist file
    --repo-root     Root of the git repo (default: current directory)
    --dry-run       Show what would change without writing files

Changelist format:
    One or more entries. Each entry is either a DATA: block (JSON update) or a
    FILE: block (Markdown section replacement/insertion).

    DATA: data/characters.json
    PATH: Maelle.level
    OP: SET
    VALUE: 87

    DATA: data/pictos-lumina.json
    PATH: pictos[name=Clea's Life].obtained
    OP: SET
    VALUE: true

    DATA: data/characters.json
    PATH: Maelle.lumina_extras
    OP: ADD
    VALUE: {"name": "Full Strength", "notes": "25% damage at full HP"}

    DATA: data/characters.json
    PATH: Maelle.lumina_extras[name=Full Strength]
    OP: REMOVE

    DATA: data/characters.json
    PATH: Maelle.skills_learned
    OP: REMOVE
    VALUE: "Gommage"

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

DATA: block fields:
    DATA:     Repo-relative path to the target JSON file (required)
    PATH:     Dot-notation path to the target field (required; see below)
    OP:       SET, ADD, or REMOVE (required)
    VALUE:    JSON value — must be last field; omit for REMOVE without value (optional)

PATH syntax:
    foo.bar                     Key 'bar' inside key 'foo'
    foo[name=Bar].baz           Item in 'foo' array where name == "Bar", then key 'baz'
    foo[2]                      Item at index 2 in 'foo' array
    Filter values are always compared as plain strings.

OP semantics:
    SET     Create or update the value at PATH (set-or-create; no failure if key absent).
    ADD     Append VALUE to the array at PATH.
    REMOVE  Three sub-cases:
              Path ends with [filter] or [index] → remove that item from the array.
              Path ends with a key + VALUE given  → remove VALUE from the array at that key.
              Path ends with a key + no VALUE     → delete that key from its parent dict.

Processing order:
    DATA blocks are applied first (updating JSON), then FILE blocks update Markdown
    sections, then generate.py runs to refresh GENERATED markers from the updated JSON.

FILE: block fields:
    FILE:     Repo-relative path to the target file (required)
    SECTION:  "## Parent > ### Child" identifier (required)
              For a ## -level change with no ### child: "## Section Name"
    AFTER:    ### heading to insert after (optional; only used when section
              does not yet exist — ignored for updates)
    CONTENT:  Marks the start of replacement text (required; must be last header field)

FILE: behaviour:
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

import json
import re
import sys
from pathlib import Path
import subprocess


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
# DATA: block — path parsing
# ---------------------------------------------------------------------------

def parse_path(path_str):
    """
    Tokenise a dot-notation path string into a list of step tuples.

    Returns list of:
        ('key',    fieldname)         dict key access
        ('index',  N)                 array index (integer)
        ('filter', filter_key, fval)  array item where filter_key == fval (string compare)

    Examples:
        'Maelle.level'
            -> [('key', 'Maelle'), ('key', 'level')]

        'pictos[name=Clea\\'s Life].obtained'
            -> [('key', 'pictos'), ('filter', 'name', "Clea's Life"), ('key', 'obtained')]

        'pictos_equipped[1]'
            -> [('key', 'pictos_equipped'), ('index', 1)]
    """
    steps = []
    i = 0
    current_key = []

    while i < len(path_str):
        c = path_str[i]

        if c == '.':
            if current_key:
                steps.append(('key', ''.join(current_key)))
                current_key = []
            # Silently swallow the dot; a leading dot is an error caught below
            i += 1

        elif c == '[':
            if current_key:
                steps.append(('key', ''.join(current_key)))
                current_key = []
            # Find the matching closing bracket
            j = path_str.find(']', i + 1)
            if j == -1:
                raise ValueError(f'Unmatched "[" in path: {path_str!r}')
            inner = path_str[i + 1:j]
            if '=' in inner:
                filter_key, filter_val = inner.split('=', 1)
                steps.append(('filter', filter_key.strip(), filter_val.strip()))
            else:
                try:
                    steps.append(('index', int(inner.strip())))
                except ValueError:
                    raise ValueError(
                        f'Invalid array indexer [{inner!r}] in path {path_str!r} — '
                        f'must be an integer or key=value filter'
                    )
            i = j + 1
            # Swallow a following dot (e.g. foo[0].bar)
            if i < len(path_str) and path_str[i] == '.':
                i += 1

        else:
            current_key.append(c)
            i += 1

    if current_key:
        steps.append(('key', ''.join(current_key)))

    if not steps:
        raise ValueError(f'Empty path: {path_str!r}')

    return steps


# ---------------------------------------------------------------------------
# DATA: block — JSON operations
# ---------------------------------------------------------------------------

def _navigate(data, steps, create_dicts=False):
    """
    Traverse data following steps (all but caller's last step).
    Returns the container at the end of the traversal.
    Raises ValueError on missing keys, type mismatches, or unmatched filters.
    If create_dicts is True, missing dict keys are auto-vivified as empty dicts
    (used for SET to support creating new nested fields).
    """
    current = data
    for step in steps:
        stype = step[0]

        if stype == 'key':
            key = step[1]
            if not isinstance(current, dict):
                raise ValueError(
                    f'Expected dict at key "{key}", '
                    f'found {type(current).__name__}'
                )
            if key not in current:
                if create_dicts:
                    current[key] = {}
                else:
                    raise ValueError(f'Key not found: "{key}"')
            current = current[key]

        elif stype == 'index':
            idx = step[1]
            if not isinstance(current, list):
                raise ValueError(
                    f'Expected list for index [{idx}], '
                    f'found {type(current).__name__}'
                )
            try:
                current = current[idx]
            except IndexError:
                raise ValueError(
                    f'Index [{idx}] out of range '
                    f'(list length {len(current)})'
                )

        elif stype == 'filter':
            _, fkey, fval = step
            if not isinstance(current, list):
                raise ValueError(
                    f'Expected list for filter [{fkey}={fval!r}], '
                    f'found {type(current).__name__}'
                )
            matches = [
                item for item in current
                if isinstance(item, dict) and str(item.get(fkey, '')) == fval
            ]
            if not matches:
                raise ValueError(f'No item where {fkey}={fval!r}')
            if len(matches) > 1:
                raise ValueError(f'Multiple items where {fkey}={fval!r} — path is ambiguous')
            current = matches[0]

    return current


def apply_data_op(data, path_str, op, value, has_value):
    """
    Apply one DATA: block operation to a parsed JSON structure (mutates in place).

    Parameters
    ----------
    data      : dict/list — top-level JSON object (mutated in place)
    path_str  : str       — dot-notation path string
    op        : str       — 'SET', 'ADD', or 'REMOVE'
    value     : any       — parsed JSON value; meaningful only when has_value is True
    has_value : bool      — True if a VALUE: field was present (even if value is None/null)

    Raises ValueError on any path or type error.
    """
    steps = parse_path(path_str)
    op = op.upper()

    # Navigate to the parent of the target (all steps except last)
    parent_steps = steps[:-1]
    last = steps[-1]
    last_type = last[0]

    # ------------------------------------------------------------------ SET
    if op == 'SET':
        parent = _navigate(data, parent_steps, create_dicts=True)

        if last_type == 'key':
            if not isinstance(parent, dict):
                raise ValueError(
                    f'SET: parent of "{last[1]}" must be a dict, '
                    f'found {type(parent).__name__}'
                )
            parent[last[1]] = value

        elif last_type == 'index':
            if not isinstance(parent, list):
                raise ValueError(
                    f'SET: parent of [{last[1]}] must be a list, '
                    f'found {type(parent).__name__}'
                )
            try:
                parent[last[1]] = value
            except IndexError:
                raise ValueError(
                    f'SET: index [{last[1]}] out of range '
                    f'(list length {len(parent)})'
                )

        elif last_type == 'filter':
            _, fkey, fval = last
            if not isinstance(parent, list):
                raise ValueError(
                    f'SET: parent of [{fkey}={fval!r}] must be a list, '
                    f'found {type(parent).__name__}'
                )
            indices = [
                i for i, item in enumerate(parent)
                if isinstance(item, dict) and str(item.get(fkey, '')) == fval
            ]
            if not indices:
                raise ValueError(f'SET: no item where {fkey}={fval!r}')
            parent[indices[0]] = value

    # ------------------------------------------------------------------ ADD
    elif op == 'ADD':
        if not has_value:
            raise ValueError('ADD requires a VALUE: field')

        parent = _navigate(data, parent_steps, create_dicts=False)

        if last_type == 'key':
            key = last[1]
            if not isinstance(parent, dict):
                raise ValueError(
                    f'ADD: parent of "{key}" must be a dict, '
                    f'found {type(parent).__name__}'
                )
            if key not in parent:
                raise ValueError(f'ADD: key not found: "{key}"')
            target = parent[key]

        elif last_type == 'index':
            if not isinstance(parent, list):
                raise ValueError(
                    f'ADD: parent of [{last[1]}] must be a list, '
                    f'found {type(parent).__name__}'
                )
            target = parent[last[1]]

        elif last_type == 'filter':
            _, fkey, fval = last
            if not isinstance(parent, list):
                raise ValueError(
                    f'ADD: parent of [{fkey}={fval!r}] must be a list, '
                    f'found {type(parent).__name__}'
                )
            matches = [
                item for item in parent
                if isinstance(item, dict) and str(item.get(fkey, '')) == fval
            ]
            if not matches:
                raise ValueError(f'ADD: no item where {fkey}={fval!r}')
            target = matches[0]

        if not isinstance(target, list):
            raise ValueError(
                f'ADD: target at "{path_str}" must be a list, '
                f'found {type(target).__name__}'
            )
        target.append(value)

    # --------------------------------------------------------------- REMOVE
    elif op == 'REMOVE':
        parent = _navigate(data, parent_steps, create_dicts=False)

        if last_type == 'key':
            key = last[1]
            if not isinstance(parent, dict):
                raise ValueError(
                    f'REMOVE: parent of "{key}" must be a dict, '
                    f'found {type(parent).__name__}'
                )
            if key not in parent:
                raise ValueError(f'REMOVE: key not found: "{key}"')

            if has_value:
                # Remove a specific value from the array at this key
                arr = parent[key]
                if not isinstance(arr, list):
                    raise ValueError(
                        f'REMOVE with VALUE: "{key}" must be a list, '
                        f'found {type(arr).__name__}'
                    )
                try:
                    arr.remove(value)
                except ValueError:
                    raise ValueError(
                        f'REMOVE: {value!r} not found in list at "{key}"'
                    )
            else:
                # Delete the key entirely
                del parent[key]

        elif last_type == 'index':
            idx = last[1]
            if not isinstance(parent, list):
                raise ValueError(
                    f'REMOVE: parent of [{idx}] must be a list, '
                    f'found {type(parent).__name__}'
                )
            try:
                del parent[idx]
            except IndexError:
                raise ValueError(
                    f'REMOVE: index [{idx}] out of range '
                    f'(list length {len(parent)})'
                )

        elif last_type == 'filter':
            _, fkey, fval = last
            if not isinstance(parent, list):
                raise ValueError(
                    f'REMOVE: parent of [{fkey}={fval!r}] must be a list, '
                    f'found {type(parent).__name__}'
                )
            indices = [
                i for i, item in enumerate(parent)
                if isinstance(item, dict) and str(item.get(fkey, '')) == fval
            ]
            if not indices:
                raise ValueError(f'REMOVE: no item where {fkey}={fval!r}')
            del parent[indices[0]]

    else:
        raise ValueError(
            f'Unknown operation: {op!r} — must be SET, ADD, or REMOVE'
        )


# ---------------------------------------------------------------------------
# Changelist parsing
# ---------------------------------------------------------------------------

def parse_changelist(text):
    """
    Parse changelist text into a list of entry dicts.

    Each entry has a 'type' field: 'data' or 'file'.

    DATA entries:
        {
            'type':      'data',
            'file':      str,    # repo-relative JSON path
            'path':      str,    # dot-notation path
            'op':        str,    # 'SET', 'ADD', or 'REMOVE'
            'value':     any,    # parsed JSON value, or None if no VALUE: field
            'has_value': bool,   # True if VALUE: field was present
        }

    FILE entries:
        {
            'type':          'file',
            'file':          str,
            'parent':        str or None,
            'section':       str,
            'after':         str or None,
            'content':       str,
            'section_level': int,   # 2 for ##, 3 for ###
        }

    Raises ValueError on malformed entries.
    """
    entries = []

    # Split on DATA: or FILE: boundaries (keep the marker with its block)
    raw_blocks = re.split(r'(?m)^(?=(?:DATA:|FILE:))', text)

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        if block.startswith('DATA:'):
            entries.append(_parse_data_block(block))
        elif block.startswith('FILE:'):
            entries.append(_parse_file_block(block))
        # Anything else (preamble text etc.) is silently ignored

    return entries


def _parse_data_block(block):
    """Parse one DATA: block. Returns a data entry dict."""

    # VALUE: must be the last field — split the block there.
    # Everything before VALUE: is the header; everything after is the value text.
    value_split = re.split(r'(?m)^VALUE:', block, maxsplit=1)
    if len(value_split) == 2:
        header_text = value_split[0]
        value_raw = value_split[1].strip()
        if not value_raw:
            raise ValueError(
                f'VALUE: field is present but empty in DATA block:\n{block[:200]}'
            )
        try:
            value = json.loads(value_raw)
        except json.JSONDecodeError as e:
            raise ValueError(
                f'VALUE: is not valid JSON in DATA block '
                f'({e}):\n{value_raw[:200]}'
            )
        has_value = True
    else:
        header_text = block
        value = None
        has_value = False

    def get_field(name, required=True):
        m = re.search(rf'(?m)^{name}:\s*(.+)$', header_text)
        if m:
            return m.group(1).strip()
        if required:
            raise ValueError(
                f'Missing {name}: in DATA block:\n{header_text[:200]}'
            )
        return None

    file_path = get_field('DATA')
    path_str  = get_field('PATH')
    op        = get_field('OP').upper()

    if op not in ('SET', 'ADD', 'REMOVE'):
        raise ValueError(
            f'Invalid OP: {op!r} — must be SET, ADD, or REMOVE'
        )
    if op in ('SET', 'ADD') and not has_value:
        raise ValueError(f'OP: {op} requires a VALUE: field')

    return {
        'type':      'data',
        'file':      file_path,
        'path':      path_str,
        'op':        op,
        'value':     value,
        'has_value': has_value,
    }


def _parse_file_block(block):
    """Parse one FILE: block. Returns a file entry dict. (Extracted from parse_changelist.)"""

    # Split header from content at CONTENT: marker
    content_match = re.search(r'(?m)^CONTENT:\s*\n', block)
    if not content_match:
        raise ValueError(f'Missing CONTENT: marker in block:\n{block[:200]}')

    header_text  = block[:content_match.start()]
    content_text = block[content_match.end():]

    # Strip trailing blank lines from content, then add exactly one trailing newline.
    content_text = content_text.rstrip('\n') + '\n'

    def get_field(name, required=True):
        m = re.search(rf'(?m)^{name}:\s*(.+)$', header_text)
        if m:
            return m.group(1).strip()
        if required:
            raise ValueError(f'Missing {name}: in FILE block:\n{header_text}')
        return None

    file_path    = get_field('FILE')
    section_str  = get_field('SECTION')
    after_hint   = get_field('AFTER', required=False)

    # Parse SECTION into parent + child
    if ' > ' in section_str:
        parts = section_str.split(' > ', 1)
        parent_heading  = parts[0].strip()
        section_heading = parts[1].strip()
        section_level   = 3
        if not parent_heading.startswith('## '):
            raise ValueError(
                f'Parent heading must start with "## ": {parent_heading}'
            )
        if not section_heading.startswith('### '):
            raise ValueError(
                f'Child heading must start with "### ": {section_heading}'
            )
    else:
        parent_heading  = None
        section_heading = section_str.strip()
        section_level   = 2
        if not section_heading.startswith('## '):
            raise ValueError(
                f'Section heading must start with "## " or use "## > ###" format: '
                f'{section_heading}'
            )

    return {
        'type':          'file',
        'file':          file_path,
        'parent':        parent_heading,
        'section':       section_heading,
        'after':         after_hint,
        'content':       content_text,
        'section_level': section_level,
    }


# ---------------------------------------------------------------------------
# GENERATED marker detection
# ---------------------------------------------------------------------------

_GENERATED_START_RE = re.compile(r'^<!-- GENERATED:START \S+ -->$')
_GENERATED_END_RE   = re.compile(r'^<!-- GENERATED:END -->$')


def find_generated_markers(lines):
    """
    Return a list of (key, start_line, end_line) tuples for all GENERATED blocks
    found in lines. Returns an empty list if none found.
    """
    markers = []
    i = 0
    while i < len(lines):
        m = _GENERATED_START_RE.match(lines[i].rstrip())
        if m:
            key   = lines[i].split('GENERATED:START ')[1].split(' -->')[0].strip()
            start = i
            for j in range(i + 1, len(lines)):
                if _GENERATED_END_RE.match(lines[j].rstrip()):
                    markers.append((key, start, j))
                    i = j
                    break
        i += 1
    return markers


def check_generated_overlap(old_lines, new_content_lines, section_id,
                             interactive=True):
    """
    Check whether old section content contains GENERATED markers and whether
    the new content changes them.

    Returns (proceed: bool, note: str or None).

    - No markers in old or new: proceed silently.
    - Same marker keys in old and new: proceed with a NOTE (generate.py will
      refill the markers after the changelist is applied).
    - Marker keys differ (added/removed/renamed): warn and require confirmation
      if interactive, abort if not.
    """
    old_markers = find_generated_markers(old_lines)
    new_markers = find_generated_markers(new_content_lines)

    if not old_markers and not new_markers:
        return True, None

    old_keys = {key for key, _, _ in old_markers}
    new_keys = {key for key, _, _ in new_markers}

    if old_keys == new_keys:
        note = None
        if old_keys:
            note = (f'NOTE: section contains GENERATED markers '
                    f'({", ".join(sorted(old_keys))}) — '
                    f'generate.py will refill them after this changelist.')
        return True, note

    # Keys differ — warn.
    added   = new_keys - old_keys
    removed = old_keys - new_keys
    print(f'\n  WARNING: GENERATED markers will change in {section_id}:')
    if added:
        print(f'    Added:   {", ".join(sorted(added))}')
    if removed:
        print(f'    Removed: {", ".join(sorted(removed))}')

    if not interactive:
        print('  Aborting — run interactively to confirm marker changes.')
        return False, None

    answer = input('  Proceed with this change? [y/N] ').strip().lower()
    return answer == 'y', None


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


def apply_entry(lines, entry, interactive=True):
    """
    Apply a single FILE: changelist entry to a list of lines.
    Returns (new_lines, skipped, note) where skipped=True means the entry was
    skipped due to a GENERATED marker conflict.
    Raises ValueError on failure (loud failure mode).
    """
    section_level   = entry['section_level']
    section_heading = entry['section']
    parent_heading  = entry['parent']
    after_hint      = entry['after']
    new_content_lines = entry['content'].splitlines(keepends=True)

    section_id = (f'{parent_heading} > {section_heading}'
                  if parent_heading else section_heading)

    if section_level == 2:
        note = None
        h2_line = find_heading_line(lines, section_heading)
        if h2_line is not None:
            h2_end = find_section_end(lines, h2_line, level=2)
            old_section_lines = lines[h2_line:h2_end]
            proceed, note = check_generated_overlap(old_section_lines,
                                                    new_content_lines,
                                                    section_id, interactive)
            if not proceed:
                return lines, True, None
        return _apply_h2_entry(lines, section_heading, new_content_lines), False, note
    else:
        note = None
        h2_line = find_heading_line(lines, parent_heading)
        if h2_line is not None:
            h2_end = find_section_end(lines, h2_line, level=2)
            h3_line = find_heading_line(lines, section_heading,
                                        start=h2_line + 1, end=h2_end)
            if h3_line is not None:
                h3_end = find_section_end(lines, h3_line, level=3)
                old_section_lines = lines[h3_line:h3_end]
                proceed, note = check_generated_overlap(old_section_lines,
                                                        new_content_lines,
                                                        section_id, interactive)
                if not proceed:
                    return lines, True, None
        return _apply_h3_entry(lines, parent_heading, section_heading,
                               after_hint, new_content_lines), False, note


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

    while prefix and prefix[-1].strip() == '':
        prefix.pop()

    post_sep = ['\n'] if suffix and suffix[0].strip() != '' else []

    return prefix + new_content_lines + post_sep + suffix


def _apply_h3_entry(lines, parent_heading, section_heading, after_hint, new_content_lines):
    """Replace or insert a ### section within a ## parent."""

    h2_line = find_heading_line(lines, parent_heading)
    if h2_line is None:
        raise ValueError(
            f'## parent not found: "{parent_heading}"\n'
            f'Structural changes require manual edit.'
        )

    h2_end = find_section_end(lines, h2_line, level=2)
    h3_line = find_heading_line(lines, section_heading, start=h2_line + 1, end=h2_end)

    if h3_line is not None:
        # UPDATE: replace existing ### section
        h3_end = find_section_end(lines, h3_line, level=3)
        prefix = lines[:h3_line]
        suffix = lines[h3_end:]
        post_sep = ['\n'] if suffix and suffix[0].strip() != '' else []
        return prefix + new_content_lines + post_sep + suffix

    else:
        # INSERT: section does not yet exist
        insert_pos = _find_insert_position(lines, h2_line, h2_end, after_hint)
        prefix  = lines[:insert_pos]
        suffix  = lines[insert_pos:]
        pre_sep  = ['\n'] if prefix and prefix[-1].strip() != '' else []
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

    last_h3_line = None
    for i in range(h2_start + 1, h2_end):
        if re.match(r'^### ', lines[i]):
            last_h3_line = i

    if last_h3_line is not None:
        return find_section_end(lines, last_h3_line, level=3)

    pos = h2_end
    while pos > h2_start + 1 and not lines[pos - 1].strip():
        pos -= 1
    return pos


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse
    from collections import defaultdict

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('changelist', help='Path to changelist file')
    parser.add_argument('--repo-root', default='.', help='Root of git repo (default: .)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would change without writing files')
    parser.add_argument('--no-interactive', action='store_true',
                        help='Abort (rather than prompt) on GENERATED marker conflicts')
    args = parser.parse_args()

    repo_root      = Path(args.repo_root).resolve()
    changelist_path = Path(args.changelist)

    print(f'Reading changelist: {changelist_path}')
    with open(changelist_path, 'r', encoding='utf-8') as f:
        changelist_text = f.read()

    try:
        entries = parse_changelist(changelist_text)
    except ValueError as e:
        print(f'ERROR parsing changelist: {e}')
        sys.exit(1)

    data_entries = [e for e in entries if e['type'] == 'data']
    file_entries = [e for e in entries if e['type'] == 'file']
    print(f'  {len(data_entries)} DATA entries, {len(file_entries)} FILE entries parsed')

    any_error = False

    # ----------------------------------------------------------------
    # Phase 1: DATA entries — update JSON files
    # ----------------------------------------------------------------
    if data_entries:
        print('\nPhase 1: Applying DATA entries...')

        data_by_file = defaultdict(list)
        for entry in data_entries:
            data_by_file[entry['file']].append(entry)

        for rel_path, file_data_entries in data_by_file.items():
            target_path = repo_root / rel_path

            if not target_path.exists():
                print(f'ERROR: File not found: {target_path}')
                any_error = True
                continue

            print(f'\n  JSON: {rel_path}')

            try:
                with open(target_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
            except json.JSONDecodeError as e:
                print(f'  ERROR: Could not parse JSON: {e}')
                any_error = True
                continue

            file_ok = True
            for entry in file_data_entries:
                desc = f'{entry["op"]} {entry["path"]}'
                try:
                    apply_data_op(
                        json_data,
                        entry['path'],
                        entry['op'],
                        entry['value'],
                        entry['has_value'],
                    )
                    print(f'  OK:    {desc}')
                except ValueError as e:
                    print(f'  ERROR ({desc}): {e}')
                    any_error = True
                    file_ok = False
                    break

            if file_ok:
                if args.dry_run:
                    print(f'  [dry-run] would write: {target_path}')
                else:
                    with open(target_path, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, indent=2, ensure_ascii=False)
                        f.write('\n')
                    print(f'  Written: {target_path}')

    if any_error:
        print('\nCompleted with errors in DATA phase — skipping FILE phase and generate.py.')
        sys.exit(1)

    # ----------------------------------------------------------------
    # Phase 2: FILE entries — update Markdown sections
    # ----------------------------------------------------------------
    if file_entries:
        print('\nPhase 2: Applying FILE entries...')

        entries_by_file = defaultdict(list)
        for entry in file_entries:
            entries_by_file[entry['file']].append(entry)

        for rel_path, md_entries in entries_by_file.items():
            target_path = repo_root / rel_path

            if not target_path.exists():
                print(f'ERROR: File not found: {target_path}')
                any_error = True
                continue

            print(f'\nProcessing: {rel_path}')

            lines = load_file(target_path)

            for entry in md_entries:
                section_id = (f'{entry["parent"]} > {entry["section"]}'
                              if entry['parent'] else entry['section'])
                try:
                    exists = _section_exists(lines, entry)
                    new_lines, skipped, note = apply_entry(
                        lines, entry,
                        interactive=not args.no_interactive,
                    )
                    if skipped:
                        print(f'  SKIPPED: {section_id}')
                    else:
                        action = 'UPDATE' if exists else 'INSERT'
                        print(f'  {action}: {section_id}')
                        if note:
                            print(f'  {note}')
                        lines = new_lines
                except ValueError as e:
                    print(f'  ERROR ({section_id}): {e}')
                    any_error = True
                    break

            if not any_error:
                if args.dry_run:
                    import difflib
                    with open(target_path, 'r', encoding='utf-8') as f:
                        original_lines = f.readlines()
                    normalised = normalise_blank_lines(lines)
                    normalised = insert_h2_separators(normalised)
                    diff = list(difflib.unified_diff(
                        original_lines, normalised,
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

    # ----------------------------------------------------------------
    # Phase 3: generate.py — refresh GENERATED blocks from updated JSON
    # ----------------------------------------------------------------
    if not any_error:
        print('\nRunning generate.py...')
        generate_args = [
            sys.executable,
            str(repo_root / 'scripts' / 'generate.py'),
            '--repo-root', str(repo_root),
            '--no-interactive',
        ]
        if args.dry_run:
            generate_args.append('--dry-run')

        result = subprocess.run(generate_args)
        if result.returncode != 0:
            print('WARNING: generate.py reported errors — check output above.')
            any_error = True

    if any_error:
        print('\nCompleted with errors.')
        sys.exit(1)
    else:
        print('\nDone.')


def _section_exists(lines, entry):
    """Check whether the target FILE: section already exists (for action labelling)."""
    if entry['section_level'] == 2:
        return find_heading_line(lines, entry['section']) is not None
    h2_line = find_heading_line(lines, entry['parent'])
    if h2_line is None:
        return False
    h2_end = find_section_end(lines, h2_line, level=2)
    return find_heading_line(lines, entry['section'], h2_line + 1, h2_end) is not None


if __name__ == '__main__':
    main()
