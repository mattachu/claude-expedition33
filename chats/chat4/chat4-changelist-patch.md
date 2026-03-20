FILE: overview/claude-expedition33.md
SECTION: ## Section 4: Game Mechanics
CONTENT:
## Section 4: Game Mechanics

### Gradient Skills

Each character has three Gradient Skills, costing 1, 2, and 3 Gradient Charges (GC) respectively. Gradient charges build by spending AP on skills. Gradient Skills are powerful abilities with effects ranging from damage to healing to revival — not all are attacks, hence "Gradient Skills" rather than "Gradient Attacks."

Individual character Gradient Skills are listed in each character file. Details for most characters are not yet confirmed in transcript — placeholders are in place.

### Break Mechanics

There are two distinct types of Break skills:
- **Break bar filling skills** (labelled "High Break damage"): Deal high damage to the break bar to fill it up over multiple hits. Example: Stalact Punches.
- **Break trigger skills** (labelled "Can Break"): Land the final hit that actually triggers the Break when the bar is full. Example: Moissonneuse Vendange, Mayhem.

A team typically needs both types — a filler to build the bar and a trigger to fire it. Some gradient skills combine both (e.g. Monoco's Break Point fills and triggers simultaneously).

### Pictos

Each Pictos item exists as a single copy in the game. Only one character can equip a given Pictos at a time. If another character wants the Lumina effect associated with a Pictos, they must equip it via Lumina at the listed LP cost — they cannot share the Pictos itself.

### Attribute System

Characters gain 3 attribute points per level up. Points are held in reserve and can be spent at any Flag. Points committed to an attribute are permanent unless a Recoat is used (resets all attributes and skill points to zero, returning all spent points). Attributes cap at 99 — points cannot be spent on an attribute already at 99.

### Reserve Party

If the main party (Verso/Maelle/Sciel) is fully wiped in a battle, the player can continue the battle using the reserve party (Lune and Monoco). This is most relevant for hard bosses. Lune and Monoco should not be stripped of all useful Pictos/Lumina — but main party optimisation takes priority for the vast majority of battles.

-----


FILE: overview/claude-expedition33.md
SECTION: ## Section 13: Session Procedure
CONTENT:
## Section 13: Session Procedure

*Full design rationale: [Formatted](../scripts/pipeline.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/scripts/pipeline.md)*

### Session Start

1. Fetch overview file (jsDelivr raw; use commit hash if provided)
2. Determine chat number N: count Claude chats in Section 12 + 1
3. Ask what the session is about — do not fetch character files until topic confirmed
4. Create in `/mnt/user-data/outputs/`:
   - `chatN.md` — empty transcript file
   - `chatN-index.md` — index file with header (see Index File format below)
   - `session-state.json` — `{"chat": "chatN", "last_write_timestamp": null, "modified_sections": []}`
5. Check `/mnt/transcripts/` — flag if any files present (unexpected at session start)
6. Confirm to user: chat number, files created, ready

### !log Command

Matt types `!log` at any natural pause to trigger the compound log step. Claude does not self-trigger log writes. `!check` does not trigger a log write — it often fires mid-topic and would create misleading section boundaries.

### Compound Log Step

Triggered by `!log` and always at end of session.

1. Write `<!-- SECTION: Title -->` and `## Title` heading to `chatN.md` — title must be unique within transcript; qualify if needed (e.g. "Verso Build — Pre-Sprong" / "Verso Build — Post-Sprong")
2. Check `/mnt/transcripts/` — if compaction found since last check, notify Matt immediately (memory of earlier conversation may be incomplete; Matt may want to re-paste context or ask Claude to fetch files); note internally
3. If compaction noted: run converter script (`transcript_to_md.py --after-timestamp <last_write_timestamp>`), append reconstructed turns to `chatN.md`, insert compaction markers in transcript and index, update `last_write_timestamp` to `start_timestamp` of last reconstructed turn, sourced from JSON output
4. Append turns since last write to `chatN.md` — **verbatim**. Copy every turn exactly as it appears in context — Matt's turns and Claude's turns alike, including all pasted content. Do not paraphrase, compress, or represent. This applies even when there are many turns, when content is long, or when the transcript would read more cleanly if summarised. The pull to summarise in these cases is strong — resist it explicitly. If in doubt, copy more rather than less.
5. Append to `chatN-index.md` under `## Table of Contents`: if this is the first section in a new part (every 2 sections), first write part header `### [Part N](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md)`; then append section entry `- **[Section Title](chatN.md#anchor)** — paragraph description`
6. Update `session-state.json`: for each file section discussed since the last log write, append an entry to `modified_sections` if not already present. Set `last_write_timestamp` only if compaction recovery was run in step 3 — otherwise leave as null.

### End of Session

1. Run compound log step — transcript and index now complete
2. Insert any remaining part headers in `chatN-index.md` by counting sections (2 sections per part)
3. Run splitter (`split_transcript.py --sections-per-part 2`) on `chatN.md`
4. Edit `chatN-index.md` directly to add Part Files list under `## Part Files (Claude-readable)`
5. Produce `chatN-changelist.md` covering:
   - Changelist entries for all sections in `modified_sections`
   - New Chat N row for Section 12 of overview (generate summary at this point)
   - **Write the changelist once at end of session only** — do not write changelist entries incrementally during the session. The `modified_sections` list in session state is the tracking mechanism throughout.
6. Matt pushes to GitHub

### Index File

Header (written at session start, replacing N with actual chat number):

```
# Clair Obscur: Expedition 33 — Chat N

Chat between Matt and Claude.

## Continuous Transcript

* [Formatted](chatN.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN.md)

## Part Files (Claude-readable)

*(to be added at end of session)*

## Table of Contents
```

At each compound log step: if this is the first section in a new part, first write a part header under `## Table of Contents`:

```
### [Part N](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md)
```

Then append the section entry:

```
- **[Section Title](chatN.md#section-title-anchor)** — paragraph description
```

Part number for section S: ⌈S/2⌉. Part file link: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md`

Anchor derived from `## Title` heading: lowercase, spaces to hyphens, punctuation removed.

End-of-session additions to `chatN-index.md` (done as part of end-of-session step 4):

Part Files list (one entry per part, under `## Part Files (Claude-readable)`):

```
* Part N — Descriptive Title: [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md)
```

Footer (after last ToC entry):

```
---
*Generated: YYYY-MM-DD*
```

### Changelist Format

```

