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
# GENERATED marker detection
# ---------------------------------------------------------------------------

_GENERATED_START_RE = re.compile(r'^<!-- GENERATED:START \S+ -->$')
_GENERATED_END_RE = re.compile(r'^<!-- GENERATED:END -->$')


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
            key = lines[i].split('GENERATED:START ')[1].split(' -->')[0].strip()
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

    Returns True if replacement should proceed, False to skip.

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
    added = new_keys - old_keys
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
    Apply a single changelist entry to a list of lines.
    Returns (new_lines, skipped) where skipped=True means the entry was
    skipped due to a GENERATED marker conflict.
    Raises ValueError on failure (loud failure mode).
    """
    section_level = entry['section_level']
    section_heading = entry['section']
    parent_heading = entry['parent']
    after_hint = entry['after']
    new_content_lines = entry['content'].splitlines(keepends=True)

    section_id = (f'{parent_heading} > {section_heading}'
                  if parent_heading else section_heading)

    if section_level == 2:
        note = None
        # Extract old section content for marker check
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
        # Extract old section content for marker check
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
    parser.add_argument('--no-interactive', action='store_true',
                        help='Abort (rather than prompt) on GENERATED marker conflicts')
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
                new_lines, skipped, note = apply_entry(lines, entry,
                                                       interactive=not args.no_interactive)
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
        print('\nRunning generate.py...')
        result = subprocess.run(
            [sys.executable,
             str(repo_root / 'scripts' / 'generate.py'),
             '--repo-root', str(repo_root),
             '--no-interactive'],
        )
        if result.returncode != 0:
            print('WARNING: generate.py reported errors — check output above.')
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
