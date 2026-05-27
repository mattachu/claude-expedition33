#!/usr/bin/env python3
"""Generate LINKS.md with raw.githubusercontent.com URLs pinned to the given commit hash."""

import re
import sys
from pathlib import Path

REPO = "mattachu/claude-expedition33"
HASH = sys.argv[1][:8]
BASE = f"https://raw.githubusercontent.com/{REPO}/{HASH}"

# Repo root is the parent of the scripts/ directory
REPO_ROOT = Path(__file__).resolve().parent.parent

STATIC_FILES = [
    # Overview
    "overview/claude-expedition33.md",
    "overview/party-summary.md",
    "overview/progress.md",
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
    "reference/session-procedure.md",
    "reference/session-design.md",
    "reference/historical-errors.md",
    # Scripts
    "scripts/scripts.md",
    # Chats
    "chats/chat-index.md",
    # Root
    "README.md",
]

def find_chat_indexes():
    """Scan chats/ for chatN folders that contain a chatN-index.md file."""
    chats_dir = REPO_ROOT / "chats"
    if not chats_dir.is_dir():
        return []
    entries = []
    for folder in sorted(chats_dir.iterdir()):
        m = re.fullmatch(r'chat(\d+)', folder.name)
        if m and folder.is_dir():
            index_path = f"chats/{folder.name}/{folder.name}-index.md"
            if (REPO_ROOT / index_path).exists():
                entries.append((int(m.group(1)), index_path))
    return [path for _, path in sorted(entries)]

chat_indexes = find_chat_indexes()
last_chat_num = len(chat_indexes) - 1 if chat_indexes else -1

FILES = STATIC_FILES[:-1] + chat_indexes + STATIC_FILES[-1:]  # insert before root files

lines = [
    "# Session Links",
    "",
    f"*Commit: `{HASH}`*  ",
    f"*Latest chat: {last_chat_num}*  ",
    "",
    "Paste this file's content at session start. "
    "Claude fetches files from these URLs on demand.",
    "",
]
for path in FILES:
    lines.append(f"- `{path}`: {BASE}/{path}")

with open("LINKS.md", "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"Generated LINKS.md with hash {HASH} ({len(chat_indexes)} chat indexes found)")
