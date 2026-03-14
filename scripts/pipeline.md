# Session Pipeline — Detailed Description

This document describes the full pipeline for Claude-assisted Expedition 33 gameplay sessions: how transcripts are produced, how context is managed across compaction, and how overview and character files are kept up to date.

---

## Core Principle

Claude does all content generation. Scripts handle mechanical file operations. You only push.

---

## File Architecture

### Transcript file
A single Markdown file written incrementally during the session. Format:

```
**Matt:** ...

---

**Claude:** ...

---
```

Tool calls are italicised inline. The same format is used regardless of whether compaction has occurred. This is the human-readable record of the full session.

### Index file
A single Markdown file written incrementally, one entry per completed topic section. Used by Matt for navigation (jump links into the transcript) and by Claude to identify which part file to fetch when looking something up mid-session.

### Section markers
Claude inserts a marker in the transcript at the start of each new topic section during the compound log step:

```
<!-- SECTION: Section Title -->
```

Placement: immediately after the `---` separator that closes the previous section, before the first speaker line of the new section. These are HTML comments — invisible when rendered, unambiguous to parse.

### Part files
The transcript is split into part files at end of session by the splitter script, at every 4th section marker (configurable). Part files are for Claude to read — loading only the relevant part keeps token consumption low. The boundary points are irrelevant to Matt.

### Session state file
Persisted to `/mnt/user-data/outputs/session-state.json` throughout the session. Survives compaction.

```json
{
  "last_write_timestamp": "2026-03-08T21:45:23.000000Z",
  "modified_sections": [
    {"file": "overview/maelle.md", "parent": "## Current Stats", "section": "### Level and Attributes"}
  ]
}
```

**`last_write_timestamp`:** Must be the `start_timestamp` of the first content block of the last turn written to the transcript. The converter script uses this as an anchor — any other timestamp risks missing or duplicating turns.

**`modified_sections`:** A to-do list for end-of-session changelist generation, not a record of completed work. Sections are added as changes are made during the session.

---

## Session Start Procedure

1. Fetch overview file (jsDelivr raw; use commit hash if provided)
2. Determine chat number N: count Claude chats in Section 12 of overview + 1
3. Ask what the session is about — do not fetch character files until topic confirmed
4. Create in `/mnt/user-data/outputs/`:
   - `chatN.md` — empty transcript file
   - `chatN-index.md` — index file with header (see Index File section in Section 13 of overview)
   - `session-state.json` — initial state: `{"chat": "chatN", "last_write_timestamp": null, "modified_sections": []}`
5. Check `/mnt/transcripts/` — flag if any files present (unexpected at session start)
6. Confirm to user: state chat number, confirm files created, confirm ready

---

## Compound Log Step

Triggered by the 10-turn topic shift check, and always at end of session.

1. Write `<!-- SECTION: Title -->` and `## Title` heading to `chatN.md` — title must be unique within transcript (anchor uniqueness requirement); qualify if needed
2. If compaction noted (from 10-turn check): run converter (`transcript_to_md.py --after-timestamp <last_write_timestamp>`), append reconstructed turns to `chatN.md`, insert compaction markers in transcript and index, update `last_write_timestamp` to last reconstructed turn
3. Append turns since `last_write_timestamp` to `chatN.md`
4. Append section entry to `chatN-index.md`
5. Update `session-state.json`: set `last_write_timestamp` to `start_timestamp` of first content block of last turn written in step 3; append changed `###` sections to `modified_sections`

**10-turn check** (every 10 turns):
1. Check `/mnt/transcripts/` — if compaction found, notify Matt immediately; note internally
2. Check for topic shift — if shifted, run compound log step
3. Reset counter

Topic shift is operationalised as: would the new section marker have a different title than the last section written? If yes, the topic has shifted.

---

## Compaction Detection and Response

Compaction is detected at every 10-turn check by inspecting `/mnt/transcripts/`. If detected, Matt is notified immediately — memory of earlier conversation may be incomplete and Matt may want to re-paste context or ask Claude to fetch files. Compaction is noted internally but no file operations are run until the next compound log step.

At the compound log step, if compaction was noted:

1. Run converter (`transcript_to_md.py --after-timestamp <last_write_timestamp>`) on the JSON transcript
2. Append reconstructed pre-compaction turns to `chatN.md`
3. Insert compaction markers:
   - Transcript: `*[Compaction occurred here — pre-compaction content reconstructed from transcript JSON]*`
   - Index: inline note, not a full section entry
4. Update `last_write_timestamp` to last reconstructed turn — step 3 of the compound log step then appends only post-compaction turns, eliminating any overlap

**Multiple compaction events:** behaviour of `/mnt/transcripts/` (overwrite vs. append) is not empirically verified. Flag as risk if multiple compactions occur in a session.

---

## End-of-Session Procedure

Identical whether or not compaction occurred.

1. Final compound log step — transcript and index are now complete
2. Splitter script splits `chatN.md` into part files (every 4 sections by default)
3. Edit `chatN-index.md` directly to add Part Files list under `## Part Files (Claude-readable)`
4. Produce a single `chatN-changelist.md` covering:
   - Changelist entries for all sections in `modified_sections`
   - New Chat N row for Section 12 of overview (generate summary at this point)
5. Matt pushes to GitHub

---

## Character File Update Approach

The compound log step only tracks changes in `modified_sections` — it never produces changelist entries directly. Entries are always produced at end of session.

**Minor changes** (stats, notes, small tweaks): only overview `###` sections are tracked. At end of session, Claude infers which character files are affected, fetches those sections, and produces changelist entries for both overview and character files. This step can happen in a new chat if needed.

**Major changes** (structural overhaul): the character file is loaded mid-session. Both overview and character file `###` sections are tracked in `modified_sections`. At end of session, both files are already in context — Claude produces changelist entries directly without re-fetching.

**Decision rule:** if a change can't be fully specified in the overview note, load the character file mid-session.

---

## Changelist Format

Section replacement at `###` level. Updater script (`apply_changelist.py`) locates and replaces each section in the target file.

```
FILE: overview/maelle.md
SECTION: ## Parent > ### Child
AFTER: ### Sibling (optional — only for inserts, specifies insertion point)
CONTENT:
### Child
...full replacement content...

```

- `SECTION` uses `## Parent > ### Child` for `###`-level; `## Section` for `##`-level
- `AFTER` is omitted for replacements; only used for new section inserts
- `CONTENT` is the complete replacement text including the heading line
- For `##`-level replacements, include the trailing `-----` separator as the last line of the `CONTENT` block — the separator is consumed by the replacement and will be lost if omitted
- Failure mode: loud — no silent corruption
- **Maintenance discipline:** `###` heading text must be unique within its `##` parent. Renaming a heading requires a direct file edit, not a changelist entry.

---

## Scripts

|Script      | File                  | Description                                                                                                                                      |
|------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Turn index | `turn_index.py`       | JSON transcript → turn index. Manual use only; not part of the automated pipeline.                                                               |
| Converter  | `transcript_to_md.py` | JSON transcript → Markdown. Chunk mode (full session with chunk map) or timestamp mode (`--after-timestamp`) for post-compaction reconstruction. |
| Splitter   | `split_transcript.py` | Splits a completed Markdown transcript into part files at `<!-- SECTION: -->` markers.                                                           |
| Updater    | `apply_changelist.py` | Applies a changelist of section replacements and insertions to repo files.                                                                       |

---

## Key Constraints

- Claude cannot intercept its own output stream — transcripts are written explicitly at each compound log step
- SSH key is not accessible to Claude — `git push` is always done by Matt
- Compaction is detectable by checking `/mnt/transcripts/` for files
- Timestamps used as anchors are more robust than turn counting
- `###` heading uniqueness within a `##` parent must be maintained
- Session state must survive compaction — written to file, not held in memory
- Part file split is mechanical (every 4 sections) — configurable in Splitter script
- Compaction markers are inserted in both transcript and index for traceability
