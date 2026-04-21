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

```

## generate.py

```python
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
    chroma = inv.get('chroma', '?')
    return (f'- Colour of Lumina: {col}\n'
            f'- Recoats: {rec}\n'
            f'- Chroma Catalysts: {cats}\n'
            f'- Chroma: {chroma}\n')


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
    checklist = playthrough.get('current_phase_checklist', [])

    lines = []

    def render_item(item, indent=0):
        prefix = '  ' * indent

        # Group (has children)
        if 'items' in item:
            children = item.get('items', [])

            total = len(children)
            done_count = sum(1 for c in children if c.get('done', False))
            done = (total > 0 and done_count == total)

            # Parent line with progress
            lines.append(
                f'{prefix}- {"✅" if done else "⬜"} {item.get("label", item.get("id", ""))} ({done_count}/{total})'
            )

            # Render children
            for child in children:
                render_item(child, indent + 1)

        # Leaf item
        else:
            done = item.get('done', False)
            lines.append(
                f'{prefix}- {"✅" if done else "⬜"} {item.get("label", item.get("id", ""))}'
            )

    for item in checklist:
        render_item(item)

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

    lines += ['# Inventory', '']
    lines.append(gen_inventory(playthrough))

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
            ('|  | Name | Effect | LP | Stat boosts | Equipped By | Also in |\n'
             '|--|------|--------|----|-------------|-------------|---------|'),
        ]
        for p in sorted(entries, key=lambda x: x['name']):
            stats = ', '.join(f'{key.capitalize()}: {value}'
                              for key, value in p.get('stats', {}).items())
            lines.append(
                f'| {"✓" if p.get("obtained") else ""} '
                f'| {p["name"]} '
                f'| {p.get("effect", "")} '
                f'| {p.get("lp_cost", "?")} '
                f'| {stats} '
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
    "data/schema.md",
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
    "scripts/pipeline.md",
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
    "chats/chat9/chat9-index.md",
    "chats/chat10/chat10-index.md",
    "chats/chat11/chat11-index.md",
    "chats/chat12/chat12-index.md",
    # Root
    "repo-structure.md",
    "README.md",
]

lines = [
    "# Session Links",
    "",
    f"*Commit: `{HASH}`*"
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

