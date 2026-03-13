# claude-expedition33

Tools and records for AI-assisted gameplay sessions for Clair Obscur: Expedition 33, using Claude.

## Contents

See [`repo-structure.md`](repo-structure.md) for repo structure.

### Overview and Character Files

Persistent context files loaded by Claude at the start of each session.

* [`overview/claude-expedition33.md`](overview/claude-expedition33.md) — Main overview file: playthrough status, party builds, progression plan, session procedure, and known AI error log
* [`overview/character-file-template.md`](overview/character-file-template.md) — Template for character files
* [`overview/maelle.md`](overview/maelle.md) — Maelle character file
* [`overview/lune.md`](overview/lune.md) — Lune character file
* [`overview/sciel.md`](overview/sciel.md) — Sciel character file
* [`overview/verso.md`](overview/verso.md) — Verso character file
* [`overview/monoco.md`](overview/monoco.md) — Monoco character file

### Chat Transcripts

Full records of gameplay planning sessions. Each chat has:

* A **continuous transcript** (`chatN.md`) — human-readable, with `##` section headings for navigation
* **Part files** (`chatN-partN.md`) — the same content split into smaller files for Claude to load selectively, reducing token consumption
* An **index file** (`chatN-index.md`) — table of contents with section descriptions and links into the continuous transcript

| Chat   | Index                                        | Transcript                       | Summary                                                                                                                                      |
|--------|----------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Chat 0 | _None_                                       | [chat0.md](chats/chat0/chat0.md) | Prior (abandoned) conversation with ChatGPT; not yet indexed                                                                                 |
| Chat 1 | [chat1-index.md](chats/chat1/chat1-index.md) | [chat1.md](chats/chat1/chat1.md) | Initial build analysis across all five characters; Monoco stat respec; Lune weapon comparison; Sciel and Verso builds; full progression plan |
| Chat 2 | [chat2-index.md](chats/chat2/chat2-index.md) | [chat2.md](chats/chat2/chat2.md) | Endgame skill research; character stat update via voice; chromatic progress; compaction mechanics; session procedure design                  |

### Scripts

Python scripts for processing and managing session transcripts and repo files.

| Script                                                       | Description                                                                                                                                                                           |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`scripts/turn_index.py`](scripts/turn_index.py)             | JSON transcript → turn index. Manual use only; not part of the automated pipeline.                                                                                                    |
| [`scripts/transcript_to_md.py`](scripts/transcript_to_md.py) | JSON transcript → Markdown. Two modes: chunk mode (full session with chunk map) and timestamp mode (`--after-timestamp`, used after compaction to reconstruct post-compaction turns). |
| [`scripts/apply_changelist.py`](scripts/apply_changelist.py) | Applies a changelist of section replacements and insertions to overview and character files.                                                                                          |
| [`scripts/split_transcript.py`](scripts/split_transcript.py) | Splits a completed Markdown transcript into part files at `<!-- SECTION: -->` markers.                                                                                                |

## Pipeline Overview

Each session produces a running transcript and index, updated at regular **compound log steps**. At end of session, the transcript is split into part files, a changelist of section replacements is produced for any changed overview or character file sections, and Script 3 applies those changes to the repo. You push.

See [`scripts/pipeline.md`](scripts/pipeline.md) for a full description of the pipeline, including compound log mechanics, compaction handling, character file update approach, and changelist format.

## Session Startup

At the start of each session, Claude:

1. Asks for the startup file URL (`matteaston.net/claude`) and reads it
2. Asks what the session is about
3. Fetches the relevant overview file from the topic index in the startup file
4. Follows any further instructions in that overview file
