# Session Procedure

Full reference for the Clair Obscur: Expedition 33 AI session system.  
Fetched at `!wrap`. Also relevant when switching from a lighter to a more capable model mid-session for complex work.

For system architecture and design rationale, see [`reference/session-design.md`](session-design.md)

---

## Session Start

Claude follows the condensed version in Section 7 of the overview file at session start. The steps here are for reference.

1. Read `LINKS.md` (pasted or uploaded by Matt) — extract all file URLs for use during session; note commit hash for reference
2. Determine new chat number N: add 1 to "latest chat number" in `LINKS.md`
3. Fetch `overview/claude-expedition33.md` using URL from `LINKS.md`
4. Review Section 6 open questions; flag any resolved items
5. Fetch `data/playthrough.json`
6. Create `/mnt/user-data/outputs/chatN.md` (transcript file, to be filled later) with title `# Clair Obscur: Expedition 33 — Chat N`
7. Ask what the session is about — do not fetch character or reference files unless topic requires them

---

## Turn Counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response. Track from context — no tool calls needed.

---

## Commands

`!log` — log conversation to transcript; follow Logging Process below  
`!check` — critical review of Claude's most recent response; does not trigger a log write  
`!close` — end-of-session for the current chat; follow Close Steps below  
`!wrap` — full end-of-session pass; run in a separate chat with the transcript uploaded; fetch this file and follow Wrap Steps below  

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

**Which turns to log:** Use the turn counter display (`*[Turn N. Last log: Turn L.]*`) to determine the range — log all turns from Last log + 1 to current turn. Do not view the transcript file to determine the last logged turn; the counter is the authoritative record.

**Appending to file:** Use bash `>>` redirection to append turns to the transcript file. No need to view the file before appending — just construct the content and redirect.

---

## Mid-Session Escalation

If the current model is clearly struggling — complex multi-step reasoning, build optimisation across characters, or compaction — switch to a more capable model. Either switch in-chat or start a new chat and paste the LINKS file and ask for a session summary to reconstruct context. Fetch this file if the session procedure is relevant to the work continuing in the new model.

If compaction occurs and is noticed in the UI: move to `!close` and create new chat, rather than continuing.

---

## Close Steps

Triggered by `!close` in the current session chat.

1. Complete transcript: run a final `!log` step
2. Verbatim check: sample 3–4 turns spread across the transcript file (beginning, middle, end) — read each from disk, compare against context, report pass/fail per sample
3. Output transcript: present `chatN.md` and stop

---

## Wrap Steps

These steps run in a separate chat after `!close` completes in the original session chat.  
Matt will upload `chatN.md` — do not read this full file, as it is long, and will consume too many tokens.  
Follow the steps below in order, stopping for Matt's confirmation between each major step.  
Don't write everything to the chat, process in files as described to reduce token usage.  

Throughout these steps, `N` is the chat number and `P` is the part number — replace both with actual values in all filenames, paths, URLs, and index content. Determine N from the uploaded filename before running any commands.

### Step 1 — Split transcript into sections and plan part grouping

Run from `/home/claude/` as working directory:

```bash
csplit /mnt/user-data/uploads/chatN.md '/^<!-- SECTION -->$/' '{*}' --prefix=/home/claude/section --suffix-format='%02d.md'
```

`section00.md` is the transcript title header — skip it. Sections begin at `section01.md`.

Report section count, count lines in all sections, and propose part grouping targeting approximately 500–600 lines per part (e.g. "8 sections found. Part 1: sections 1–4 (487 lines), Part 2: sections 5–8 (521 lines)").

Stop and confirm grouping with Matt before continuing.

### Step 2 — Process sections one at a time

Before reading any section files, first create the index file `/mnt/user-data/outputs/chatN-index.md`:

```md
# Clair Obscur: Expedition 33 — Chat N

Chat between Matt and Claude.

## Continuous Transcript

* [Formatted](chatN.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN.md)

## Part Files (Claude-readable)

(part list to be added later)

## Table of Contents
```

For each section from `section01.md` onward, follow the steps below. Read one section at a time. Do not read ahead. Read `sectionN.md`, complete all sub-steps (a, b, c) for that section, then read `section(N+1).md`. Do not batch reads across multiple sections.

**a. Part heading**
If the section opens a new part, append a part heading to the index file:
```md

### [Part P](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partP.md)

```

**b. Section title**
Write a short descriptive title for this section (unique within the transcript; qualify if needed, e.g. "Verso Build — Pre-Sprong" / "Verso Build — Post-Sprong"). Insert it into the section file immediately after the `<!-- SECTION -->` marker:
```md
<!-- SECTION -->
## Section Title
```

**c. Index entry**
Append the section title, section link and a section description to the index file. The description should be 2–3 concise sentences covering the topic and key decisions. Do not list every item discussed.
```md
- **[Section Title](chatN.md#section-title)** — description.
```

Once all sections are processed, replace the `(part list to be added later)` placeholder in the index file with the actual part list, using `sed`. Follow the Part Files list format in the Index File Format section below. For example:

```bash
sed -i 's/(part list to be added later)/* Part 1 — Opening Title: [Raw](https:\/\/cdn.jsdelivr.net\/gh\/mattachu\/claude-expedition33@main\/chats\/chatN\/chatN-part1.md)\n* Part 2 — Closing Title: [Raw](https:\/\/cdn.jsdelivr.net\/gh\/mattachu\/claude-expedition33@main\/chats\/chatN\/chatN-part2.md)/' /mnt/user-data/outputs/chatN-index.md
```

Or write the part list to a temporary file and use `sed -i` with a file reference if the substitution string is unwieldy.

Confirm with Matt when all sections are processed.

### Step 3 — Pull and present raw actions

Use `awk` to pull all ACTION flags from the section files, grouped by section title:

```bash
awk '/^## /{section=$0; found=0} /^\*\*ACTION:/{if(!found){print section; found=1} print}' /home/claude/section*.md
```

Present the output to Matt and stop. Matt reviews and flags any actions to drop or modify before continuing.

### Step 4 — Generate action list and changelist

Sort confirmed actions into bins:

- **In-game actions** — things Matt needs to do in the game before the next session
- **Data changes** — updates to JSON data files (→ `DATA:` blocks in changelist)
- **File changes** — updates to Markdown files (→ `FILE:` blocks in changelist)
- **Open questions** — items to add to Section 6 of the overview

Work through the action bins and generate `chatN-changelist.txt`. Fetch each file that has confirmed changes before writing its block.

- **Data changes** → `DATA:` blocks (one per field change)
- **File changes** → `FILE:` blocks (one per section replacement)
- **Open questions** → `FILE:` block targeting Section 6 of the overview
- Processing order: `DATA:` blocks first, then `FILE:` blocks, then `APPEND:` blocks

Also include:
- New row appended to `chats/chat-index.md` → `APPEND:` block (fetch existing file to match table row style — concise prose covering topics, decisions, infrastructure changes; do not generate mechanically from action list)
- Any updates to Section 6 open questions (even if not specifically flagged) → `FILE:` block
- Any new entries for `reference/historical-errors.md` → `APPEND:` block if significant errors were made this session

See Changelist Format below for block syntax.

Present the in-game actions checklist and the changelist file to Matt. Matt runs `scripts/apply_changelist.py` on the changelist, makes any manual changes, and pushes all files to GitHub.

### Step 5 — Complete transcript

For each part, concatenate its section files into a part file. For example:

```bash
cat /home/claude/section01.md /home/claude/section02.md /home/claude/section03.md /home/claude/section04.md > /mnt/user-data/outputs/chatN-part1.md
cat /home/claude/section05.md /home/claude/section06.md > /mnt/user-data/outputs/chatN-part2.md
```

Log the end-of-session chat itself as the final section. Append directly into the last part file (already written above — do not re-concatenate):

1. Append `<!-- SECTION -->` and `## Session Wrap` followed by a blank line into the last part file `/mnt/user-data/outputs/chatN-partP.md`
2. Append all turns from this end-of-session chat — verbatim, following the standard logging process
3. Update the chat index to add the Session Wrap entry

Then combine into the final transcript. `section00.md` contains the transcript title header, which is excluded from part files, but must be included once at the top of the full transcript. For example:

```bash
cat /home/claude/section00.md /mnt/user-data/outputs/chatN-part1.md /mnt/user-data/outputs/chatN-part2.md > /mnt/user-data/outputs/chatN.md
```

Present the completed transcript, part files, and chat index to Matt.

---

## Changelist Format

Three block types: `DATA:` (JSON field updates), `FILE:` (Markdown section replacements), and `APPEND:` (raw append to end of file).
Processing order: DATA → FILE → APPEND → `generate.py`.

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

**Array element type:** When using `ADD` to append to an array field, the `VALUE` must match the type of the existing elements. If the array contains objects (e.g. `lumina_extras`, which holds `{"name": "...", "notes": "..."}` entries), use `VALUE: {"name": "..."}` — not a plain string. A plain string `ADD` will succeed without error but will corrupt the data and cause `generate.py` to fail with `TypeError: string indices must be integers`.

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

### APPEND: blocks

Append content verbatim to the end of a file:

```
APPEND: chats/chat-index.md
CONTENT:
| Chat 23 | [Formatted](...) / [Raw](...) | [chat23.md](...) | Summary text. |
```

- No section targeting — content is appended directly after the last line of the file
- No reformatting — separator stripping, blank-line normalisation, and `##` separator insertion are not applied
- Intended for flat-structure files where `FILE:` section targeting is not applicable: `chats/chat-index.md` (table rows) and `reference/historical-errors.md` (numbered list items)
- The script ensures the file ends with exactly one newline before appending

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
