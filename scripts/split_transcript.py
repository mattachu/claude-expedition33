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
