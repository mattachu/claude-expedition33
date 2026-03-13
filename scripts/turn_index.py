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
