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
The transcript is split into part files at end of session by Script 4, at every 4th section marker (configurable). Part files are for Claude to read — loading only the relevant part keeps token consumption low. The boundary points are irrelevant to Matt.

### Session state file
Persisted to `/mnt/user-data/outputs/session-state.json` throughout the session. Survives compaction.

```json
{
  "last_write_timestamp": "2026-03-08T21:45:23.000000Z",
  "turns_since_last_write": 3,
  "modified_sections": [
    {"file": "overview/maelle.md", "parent": "## Current Stats", "section": "### Level and Attributes"}
  ]
}
```

**`last_write_timestamp`:** Must be the `start_timestamp` of the first content block of the last turn written to the transcript. Script 2 uses this as an anchor — any other timestamp risks missing or duplicating turns.

**`modified_sections`:** A to-do list for end-of-session changelist generation, not a record of completed work. Sections are added as changes are made during the session.

---

## Compound Log Step

Triggered every 10 turns when the topic has shifted since the last write, and always at end of session. `!check` does not trigger it.

1. Append turns since last write to the transcript, preceded by a section marker
2. Append a completed section entry to the index file
3. Update session state — new timestamp, reset turn counter, add any changed `###` sections to `modified_sections`
4. Check for compaction (see below)

---

## Compaction Detection and Response

At every compound log step, check `/mnt/transcripts/` for files.

**If compaction detected:**

1. Read session state — find `last_write_timestamp`
2. Run Script 2 with `--after-timestamp` on the JSON transcript to extract turns after the last write
3. Append reconstructed content to the running transcript file
4. Insert a compaction marker in the transcript:
   ```
   ---
   *[Compaction occurred here — pre-compaction content reconstructed from transcript JSON]*
   ---
   ```
5. Insert a compaction marker in the index (inline note, not a full section entry)
6. Reset session state — update timestamp to last reconstructed turn, reset counter
7. Do not write an index section entry — that waits for the next genuine topic shift
8. Continue session as normal

**Note:** Script 1 is not needed in this flow. Timestamps in the JSON are used directly as anchors.

---

## End-of-Session Procedure

Identical whether or not compaction occurred.

1. Final compound log step — transcript and index are now complete
2. Script 4 splits the transcript into part files (every 4 sections by default)
3. Produce changelist entries for all sections in the `modified_sections` to-do list
4. You push to GitHub

---

## Character File Update Approach

The compound log step only tracks changes in `modified_sections` — it never produces changelist entries directly. Entries are always produced at end of session.

**Minor changes** (stats, notes, small tweaks): only overview `###` sections are tracked. At end of session, Claude infers which character files are affected, fetches those sections, and produces changelist entries for both overview and character files. This step can happen in a new chat if needed.

**Major changes** (structural overhaul): the character file is loaded mid-session. Both overview and character file `###` sections are tracked in `modified_sections`. At end of session, both files are already in context — Claude produces changelist entries directly without re-fetching.

**Decision rule:** if a change can't be fully specified in the overview note, load the character file mid-session.

---

## Changelist Format

Section replacement at `###` level. Script 3 (`apply_changelist.py`) locates and replaces each section in the target file.

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
- Failure mode: loud — no silent corruption
- **Maintenance discipline:** `###` heading text must be unique within its `##` parent. Renaming a heading requires a direct file edit, not a changelist entry.

---

## Scripts

| Script | File | Description |
|--------|------|-------------|
| Script 1 | `turn_index.py` | JSON transcript → turn index. Manual use only; not part of the automated pipeline. |
| Script 2 | `transcript_to_md.py` | JSON transcript → Markdown. Chunk mode (full session with chunk map) or timestamp mode (`--after-timestamp`) for post-compaction reconstruction. |
| Script 3 | `apply_changelist.py` | Applies a changelist of section replacements and insertions to repo files. |
| Script 4 | `split_transcript.py` | Splits a completed Markdown transcript into part files at `<!-- SECTION: -->` markers. |

---

## Key Constraints

- Claude cannot intercept its own output stream — transcripts are written explicitly at each compound log step
- SSH key is not accessible to Claude — `git push` is always done by Matt
- Compaction is detectable by checking `/mnt/transcripts/` for files
- Timestamps used as anchors are more robust than turn counting
- `###` heading uniqueness within a `##` parent must be maintained
- Session state must survive compaction — written to file, not held in memory
- Part file split is mechanical (every 4 sections) — configurable in Script 4
- Compaction markers are inserted in both transcript and index for traceability
