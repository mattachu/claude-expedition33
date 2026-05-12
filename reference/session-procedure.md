# Session Procedure

Full reference for the Clair Obscur: Expedition 33 AI session system.  
Fetched at `!wrap`. Also relevant when switching from a lighter to a more capable model mid-session for complex work.

---

## Session Start

Claude follows the condensed version in Section 7 of the overview file at session start. The steps here are for reference.

1. Read `LINKS.md` (pasted or uploaded by Matt) — extract all file URLs for use during session; note commit hash for reference
2. Determine new chat number N: add 1 to "latest chat number" in `LINKS.md`
3. Fetch `overview/claude-expedition33.md` using URL from `LINKS.md`
4. Review Section 6 open questions; flag any resolved items
5. Fetch `data/playthrough.json`
6. Create `/mnt/user-data/outputs/chatN.md` (empty transcript file with title heading only)
7. Ask what the session is about — do not fetch character or reference files unless topic requires them

---

## Turn Counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response. Track from context — no tool calls needed.

---

## Commands

`!log` — log conversation to transcript; follow Logging Process below  
`!check` — critical review of Claude's most recent response; does not trigger a log write  
`!wrap` — end-of-session; fetch this file and follow End-of-Session Steps below  

---

## ACTION Flags

When a decision, in-game action, data change, or open question arises, write `**ACTION:** <brief note>` as a standalone line in the response. These are collected and categorised by the end-of-session pass.

Examples:
- `**ACTION:** Expand Lune's Lumina pool by 24LP and add Cheater Lumina` (in-game action)
- `**ACTION:** Update progress log — Chromatic Clair Obscur defeated, set to true` (data file update)
- `**ACTION:** Add Frenzy to Pictos database` (data file addition)
- `**ACTION:** Update overview file with new session procedure` (text file change)

Flags are advisory — the end-of-session pass reconciles them against the full transcript before acting. A later exchange that modifies or retracts a flagged action takes precedence.

---

## Logging Process

Triggered by `!log`. Two steps only:

1. Append `<!-- SECTION -->` followed by a blank line to `chatN.md`
2. Append all turns since last write — **verbatim**

**Turn format:** Matt's turn first, labelled `**Matt:**`, then a blank line, then Claude's turn, labelled `**Claude:**`, then a blank line, then a horizontal rule `---`.

**Verbatim logging:** Copy every turn exactly as it appears in context — Matt's turns and Claude's turns alike, including all pasted content. Do not paraphrase, compress, summarise, or represent any turn, regardless of length or content. The pull to summarise long or repetitive content is strong — resist it explicitly. If in doubt, copy more rather than less.

**Bracket notation:** for tool calls only: `*[Fetched X]*`, `*[Created file Y]*`. Never use brackets to summarise substantive response text.

**Lists:** If Matt's turn begins with a list, insert a blank line between `**Matt:**` and the first list item so Markdown renders correctly.

---

## Mid-Session Escalation

If the current model is clearly struggling — complex multi-step reasoning, build optimisation across characters, or compaction — switch to a more capable model. Either switch in-chat or start a new chat and paste the LINKS file and ask for a session summary to reconstruct context. Fetch this file if the session procedure is relevant to the work continuing in the new model.

If compaction occurs and is noticed in the UI: move to `!wrap` and create new chat, rather than continuing.

---

## End-of-Session Steps

Triggered by `!wrap`. Fetch this file if not already in context. Then follow these steps in order, stopping for Matt's confirmation between each major step.

### Step 1 — Split transcript into sections and plan part grouping

Run from `/home/claude/` as working directory:

```bash
cp /mnt/user-data/outputs/chatN.md /home/claude/chatN.md
csplit /home/claude/chatN.md '/^<!-- SECTION -->$/' '{*}' --prefix=/home/claude/section --suffix-format='%02d.md'
```

`section00.md` is the transcript title header — skip it. Sections begin at `section01.md`.

Report section count, count lines in all sections, and propose part grouping targeting approximately 500–600 lines per part (e.g. "8 sections found. Part 1: sections 1–4 (487 lines), Part 2: sections 5–8 (521 lines)").

Stop and confirm grouping with Matt before continuing.

### Step 2 — Process sections one at a time

For each section from `section01.md` onward:

**a. Verbatim spot-check**  
Pick one Claude turn from the section at random. Compare against context memory of this chat. If it reads as a summary, paraphrase, or contains bracket notation representing substantive content, flag immediately and stop — do not proceed until Matt has reviewed. If clean, continue.

**b. Section title**  
Write a short descriptive title for this section (unique within the transcript; qualify if needed, e.g. "Verso Build — Pre-Sprong" / "Verso Build — Post-Sprong"). Insert it into the section file immediately after the `<!-- SECTION -->` marker:

```
<!-- SECTION -->
## Section Title
```

**c. Index entry**  
Record in memory for each section (accumulating for Step 4 assembly):
- Which part this section belongs to (Part 1, Part 2, etc.)
- Section title
- 2–3 short sentences covering the topic and key decisions. Do not list every item discussed.

**d. Categorise ACTION flags**  
Scan the section for `**ACTION:**` flags. Reconcile against context — if a later exchange in the section modifies or retracts a flag, adjust accordingly. Add confirmed actions to the appropriate bin:

- **In-game actions** — things Matt needs to do in the game before the next session
- **Data changes** — updates to JSON data files (→ `DATA:` blocks in changelist)
- **File changes** — updates to Markdown files (→ `FILE:` blocks in changelist)
- **Open questions** — items to add to Section 6 of the overview

Report section title and action count to Matt after each section. Continue to next section.

Confirm with Matt when all sections are processed.

### Step 3 — Combine into part files

For each part, concatenate its section files:

```bash
cat /home/claude/section01.md /home/claude/section02.md /home/claude/section03.md /home/claude/section04.md > /mnt/user-data/outputs/chatN-part1.md
```

Repeat for each part.

### Step 4 — Create index file

Write `/mnt/user-data/outputs/chatN-index.md` using the index entries built in Step 2, following the Index File Format section below. Construct jsDelivr URLs and section anchors at this point.

### Step 5 — Generate changelist

Work through the action bins and generate change blocks for `chatN-changelist.md`. Fetch each file that has confirmed changes before writing its block.

- **Data changes** → `DATA:` blocks (one per field change)
- **File changes** → `FILE:` blocks (one per section replacement)
- **Open questions** → `FILE:` block targeting Section 6 of the overview
- Processing order: `DATA:` blocks first, then `FILE:` blocks

Also include:
- New row appended to `chats/chat-index.md` (fetch existing file to match style — concise prose covering topics, decisions, infrastructure changes; do not generate mechanically from action list)
- Any updates to Section 6 open questions (even if not specifically flagged)
- Any new entries for `reference/historical-errors.md` if significant errors were made this session

See Changelist Format below for block syntax.

### Step 6 — Present to Matt

**In-game actions checklist** (from in-game actions bin):

```
## In-Game Actions

- [ ] Action 1
- [ ] Action 2
```

**Changelist** — present file for Matt to review. Matt runs `scripts/apply_changelist.py` on the changelist, makes any manual changes, and pushes all files to GitHub.

### Step 7 — Append wrap session to transcript

Log the `!wrap` session itself as the final section of `chatN.md`:

1. Append `<!-- SECTION -->` and `## Session Wrap` followed by a blank line
2. Append all turns from `!wrap` onward — verbatim, following the standard logging process
3. Update the chat index to add the Session Wrap entry

Present the completed transcript, part files, and chat index to Matt.

---

## Changelist Format

Two block types: `DATA:` (JSON field updates) and `FILE:` (Markdown section replacements).  
Processing order: DATA → FILE → `generate.py`.

### DATA: blocks

Update any field in any JSON data file:

```
DATA: data/characters.json
PATH: Maelle.level
OP: SET
VALUE: 87
```

- `PATH:` — dot-notation: `Maelle.level`, `pictos[name=Clea's Life].obtained`, `arr[2]`
- `OP:` — `SET` (create or update), `ADD` (append to array), `REMOVE` (delete key, array item, or filtered object)
- `VALUE:` — any JSON value; must be last field; omit for `REMOVE` without value

### FILE: blocks

Replace or insert a Markdown section:

```
FILE: path/to/file.md
SECTION: ## Parent > ### Child
AFTER: ### Sibling
CONTENT:
### Child
...full replacement content...

```

- `SECTION:` — path to the target heading; use `## Parent > ### Child` for nested sections
- `AFTER:` — for insertions only; omit for replacements
- `###` heading must be unique within its `##` parent; renames require direct edit
- Separators (`---`) between `##` sections are inserted automatically by the updater script — do not include them in `CONTENT:` or between FILE blocks
- Failure mode: loud

---

## Index File Format

```markdown
# Clair Obscur: Expedition 33 — Chat N

Chat between Matt and Claude.

## Continuous Transcript

* [Formatted](chatN.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN.md)

## Part Files (Claude-readable)

* Part 1 — Descriptive Title: [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-part1.md)
* Part 2 — Descriptive Title: [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-part2.md)

## Table of Contents

### [Part 1](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-part1.md)

- **[Section Title](chatN.md#section-title)** — description.
- **[Section Title](chatN.md#section-title)** — description.

### [Part 2](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-part2.md)

- **[Section Title](chatN.md#section-title)** — description.

*Generated: YYYY-MM-DD*
```

Key notes:
- jsDelivr URLs use `@main` (not a pinned hash) — these are valid after pushing
- Section anchors: lowercase title, spaces to hyphens, punctuation removed
- Part descriptive titles: short evocative label for the part's content as a whole
- Section descriptions: 2–3 sentences, topic and key decisions only

---

## Compaction Handling

If compaction is noticed during a session (earlier context is unavailable), Matt will trigger `!wrap` immediately. The end-of-session pass works from the transcript file rather than context memory, so compaction does not prevent a clean wrap. Section files that were written before compaction are already on disk; Claude reads them directly.

If the transcript file itself is incomplete due to compaction (turns missing before the last `!log`), note the gap in the index entry for the affected section and flag for Matt to review.
