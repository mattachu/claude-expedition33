# claude-expedition33

Tools and records for AI-assisted gameplay sessions for Clair Obscur: Expedition 33, using Claude.

## Contents

See [`repo-structure.md`](repo-structure.md) for repo structure.

### Overview and Character Files

Persistent context files loaded by Claude at the start of each session.

* [`overview/claude-expedition33.md`](overview/claude-expedition33.md) — Main overview file: playthrough status, party builds, progression plan, session procedure, and known AI failure modes
* [`overview/maelle.md`](overview/maelle.md) — Maelle character file
* [`overview/lune.md`](overview/lune.md) — Lune character file
* [`overview/sciel.md`](overview/sciel.md) — Sciel character file
* [`overview/verso.md`](overview/verso.md) — Verso character file
* [`overview/monoco.md`](overview/monoco.md) — Monoco character file
* [`overview/character-file-template.md`](overview/character-file-template.md) — Template for character files
* [`overview/historical-errors.md`](overview/historical-errors.md) — List of known AI errors from previous chats

### Chat Transcripts

Full records of gameplay planning sessions. Each chat has:

* A **continuous transcript** (`chatN.md`) — human-readable, with `##` section headings for navigation
* **Part files** (`chatN-partN.md`) — the same content split into smaller files for Claude to load selectively, reducing token consumption
* An **index file** (`chatN-index.md`) — table of contents with section descriptions and links into the continuous transcript

### Scripts

Python scripts for processing and managing session transcripts and repo files.

| Script                                                       | Description                                                                                                                                                                           |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`scripts/turn_index.py`](scripts/turn_index.py)             | JSON transcript → turn index. Manual use only; not part of the automated pipeline.                                                                                                    |
| [`scripts/transcript_to_md.py`](scripts/transcript_to_md.py) | JSON transcript → Markdown. Two modes: chunk mode (full session with chunk map) and timestamp mode (`--after-timestamp`, used after compaction to reconstruct post-compaction turns). |
| [`scripts/apply_changelist.py`](scripts/apply_changelist.py) | Applies a changelist of section replacements and insertions to overview and character files.                                                                                          |
| [`scripts/split_transcript.py`](scripts/split_transcript.py) | Splits a completed Markdown transcript into part files at `<!-- SECTION: -->` markers.                                                                                                |

## Pipeline Overview

Each session produces a running transcript and index, updated at regular **compound log steps**. At end of session, the transcript is split into part files, a changelist of section replacements is produced for any changed overview or character file sections, and the updater script applies those changes to the repo. User pushes changes to GitHub.

See [`scripts/pipeline.md`](scripts/pipeline.md) for a full description of the pipeline, including compound log mechanics, compaction handling, character file update approach, and changelist format.

## Session Startup

At the start of each session on any topic, Claude:

1. Asks for the startup file URL (`matteaston.net/claude`) and reads it
2. Asks what the session is about
3. Fetches the relevant overview file from the topic index in the startup file
4. Follows any further instructions in that overview file

For Expedition 33 game chats, the topic index leads to the overview and other files in this repo.
