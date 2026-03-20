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

Section boundaries:
    A ### section spans from its heading line to just before the next ### or ##
    heading, or EOF. Trailing blank lines between sections are preserved as-is
    in the surrounding file; the replacement content's own trailing blank lines
    are stripped to avoid accumulation.
"""

import re
import sys
from pathlib import Path


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

        # Split header from content at CONTENT: marker
        content_match = re.search(r'(?m)^CONTENT:\s*\n', block)
        if not content_match:
            raise ValueError(f'Missing CONTENT: marker in block:\n{block[:200]}')

        header_text = block[:content_match.start()]
        content_text = block[content_match.end():]

        # Strip trailing blank lines from content, then add exactly one trailing newline.
        # The splice functions add a blank line separator before the suffix if needed.
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
                raise ValueError(f'Section heading must start with "## " or use "## > ###" format: {section_heading}')

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


def find_section_end(lines, start, stop_patterns):
    """
    Find the line index where a section ends, starting from `start+1`.
    A section ends at the first line matching any stop_pattern, or at a
    '-----' separator line (which marks the end of a ## block), or EOF.
    Returns the index of the first line that does NOT belong to this section.
    """
    for i in range(start + 1, len(lines)):
        # ----- separator marks the end of a ## section block
        if lines[i].strip() == '-----':
            return i
        for pattern in stop_patterns:
            if re.match(pattern, lines[i]):
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
        raise ValueError(f'## section not found: "{section_heading}"\n'
                         f'Structural changes require manual edit.')

    section_end = find_section_end(lines, h2_line, [r'^## '])

    # Preserve blank lines before the section
    prefix = lines[:h2_line]

    # section_end points at the ----- separator.
    # The replacement content already includes its own -----  so skip the
    # original separator, but preserve the blank lines that follow it.
    suffix_start = section_end
    if suffix_start < len(lines) and lines[suffix_start].strip() == '-----':
        suffix_start += 1  # skip the original ----- (replacement has its own)
    # suffix starts at the blank lines (or next ## heading) after the separator
    suffix = lines[suffix_start:]

    return prefix + new_content_lines + suffix


def _apply_h3_entry(lines, parent_heading, section_heading, after_hint, new_content_lines):
    """Replace or insert a ### section within a ## parent."""

    # Find ## parent
    h2_line = find_heading_line(lines, parent_heading)
    if h2_line is None:
        raise ValueError(f'## parent not found: "{parent_heading}"\n'
                         f'Structural changes require manual edit.')

    # Find end of ## parent block
    h2_end = find_section_end(lines, h2_line, [r'^## '])

    # Look for existing ### section within parent
    h3_line = find_heading_line(lines, section_heading, start=h2_line + 1, end=h2_end)

    if h3_line is not None:
        # UPDATE: replace existing section
        h3_end = find_section_end(lines, h3_line, [r'^### ', r'^## '])
        prefix = lines[:h3_line]
        suffix = lines[h3_end:]
        # Ensure a blank line between new content and what follows
        separator = ['\n'] if suffix and suffix[0].strip() != '' else []
        return prefix + new_content_lines + separator + suffix

    else:
        # INSERT: section does not yet exist
        insert_after_line = _find_insert_position(lines, h2_line, h2_end, after_hint, section_heading)
        prefix = lines[:insert_after_line]
        suffix = lines[insert_after_line:]
        # Ensure a blank line before and after the inserted section
        pre_sep = ['\n'] if prefix and prefix[-1].strip() != '' else []
        post_sep = ['\n'] if suffix and suffix[0].strip() != '' else []
        return prefix + pre_sep + new_content_lines + post_sep + suffix


def _find_insert_position(lines, h2_start, h2_end, after_hint, new_heading):
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
        return find_section_end(lines, after_line, [r'^### ', r'^## '])

    # Find last ### sibling
    last_h3_line = None
    for i in range(h2_start + 1, h2_end):
        if re.match(r'^### ', lines[i]):
            last_h3_line = i

    if last_h3_line is not None:
        return find_section_end(lines, last_h3_line, [r'^### ', r'^## '])

    # No ### siblings — insert at end of ## parent block
    # Back up over trailing blank lines to keep formatting clean
    pos = h2_end
    while pos > h2_start + 1 and not lines[pos - 1].strip():
        pos -= 1
    return pos


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
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
        with open(target_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for entry in file_entries:
            section_id = (f'{entry["parent"]} > {entry["section"]}'
                          if entry['parent'] else entry['section'])
            try:
                new_lines = apply_entry(lines, entry)
                action = 'UPDATE' if _section_exists(lines, entry) else 'INSERT'
                print(f'  {action}: {section_id}')
                lines = new_lines
            except ValueError as e:
                print(f'  ERROR ({section_id}): {e}')
                any_error = True
                # Loud failure: stop processing this file
                break

        if not any_error:
            new_content = ''.join(lines)
            if args.dry_run:
                print(f'  [dry-run] Would write {len(new_content):,} bytes to {target_path}')
            else:
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
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
    h2_end = find_section_end(lines, h2_line, [r'^## '])
    return find_heading_line(lines, entry['section'], h2_line + 1, h2_end) is not None


if __name__ == '__main__':
    main()
