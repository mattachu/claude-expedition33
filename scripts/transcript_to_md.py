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
