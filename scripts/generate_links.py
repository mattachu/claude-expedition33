#!/usr/bin/env python3
"""Generate LINKS.md with jsDelivr URLs pinned to the given commit hash."""

import sys

REPO = "mattachu/claude-expedition33"
HASH = sys.argv[1]
BASE = f"https://cdn.jsdelivr.net/gh/{REPO}@{HASH}"

FILES = [
    # Overview
    "overview/claude-expedition33.md",
    "overview/party-summary.md",
    "overview/pictos-lumina-summary.md",
    "overview/historical-errors.md",
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
