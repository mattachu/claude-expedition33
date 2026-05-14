<!-- SECTION -->
## Session Procedure File Scope — Single File, No Escalation Command

**Matt:** Yes, the procedure should detail everything about session procedure. It should be the full definitive reference. If that makes it too long for fetching at every `!wrap`, then we might need a separate file… 

I agree with your simple line for Section 11.

**Claude:** *[Turn 15. Last log: Turn 0.]*

I don't think we need to split it. The key point is that `reference/session-procedure.md` is only ever fetched by Sonnet, once per session. Sonnet has a large context window and fetching a 300-400 line file once at `!wrap` is negligible overhead. The length concern would only bite if Haiku had to fetch it — but under the new model Haiku never touches it.

So: one comprehensive file, Sonnet fetches it once. No split needed.

Ready to draft both documents now. To confirm the full scope:

**New Section 11 (concise):**
- Session start procedure (brief)
- !log (two steps only)
- !check definition
- !wrap trigger line
- One-liner for mid-session Sonnet escalation

**`reference/session-procedure.md` (comprehensive):**
- Session start detail
- !log, !check, !wrap command reference
- Mid-session escalation path
- Full end-of-session steps (11 steps with sub-steps, four-bin action categorisation, verbatim spot-check, part file logic, index format, changelist format with DATA:/FILE: blocks, jsDelivr URL construction)
- Compaction handling

Shall I draft Section 11 first for your approval, then the procedure file? Or both together?

---

**Matt:** Is it worth having a `!` command for Sonnet escalation? What circumstances did we say might trigger that?

**Claude:** *[Turn 16. Last log: Turn 0.]*

Good question — and I think the honest answer is we didn't define it precisely enough to justify a formal command.

The circumstances we vaguely gestured at were: Haiku visibly struggling, complex multi-step reasoning needed, or compaction occurring. But in all three cases, what actually happens is you start a new chat on Sonnet — there's nothing mechanical for Claude to do in response to a command. It's a human-side decision, not a Claude-side action.

The only case where a command would add value is if it triggered a **handoff summary** — Claude produces a compact state-of-session digest (decisions made, open questions, where we are) that you paste into the new Sonnet chat as context. That's genuinely useful and something Claude would need to actively produce.

So the question is: do you want a `!escalate` or `!handoff` command that produces that digest? Or is it simpler to just have a note in the procedure saying "if you need to switch to Sonnet mid-session, ask Claude for a session summary and paste it into the new chat with the LINKS file"?

The latter requires no formal command and adds no new mechanics to learn. I'd lean that way unless you find yourself escalating often enough that a dedicated command pays for itself.

---

**Matt:** Yeah, I think that last sentence is the key point. No need to add complication. I’m even wondering if we leave out the one-liner from section 11 about escalation: if I need to escalate, I can do so, and if it’s to do with a different problem, it might not definitely need the session procedure file.

**Claude:** *[Turn 17. Last log: Turn 0.]*

Agreed. Leave it out of Section 11 entirely. The procedure file can mention it briefly as a possibility — "if you switch to Sonnet mid-session, fetch this file for context" — but it doesn't need to be a formal part of the session lifecycle.

That makes Section 11 very clean:
- Session start
- !log
- !check
- !wrap

Nothing else. Ready to draft?

---

<!-- SECTION -->
## Drafting Section 11 — Iterative Refinement

**Matt:** Yes, draft section 11 now.

**Claude:** Let me read the current Section 11 first...

*[Turn 18. Last log: Turn 0.]*

Here's the draft:

```md
## Section 11: Session Procedure

*Full procedure in [`reference/session-procedure.md`](../reference/session-procedure.md) — fetched at `!wrap`.*

### Session Start

1. Read `LINKS.md` — extract all file URLs for use during session
2. Determine new chat number N: add 1 to "latest chat number" in `LINKS.md`
3. Fetch overview file
4. Review Section 9 open questions; flag any resolved items
5. Fetch `data/playthrough.json`
6. Create `/mnt/user-data/outputs/chatN.md` (empty transcript file)
7. Ask what the session is about — do not fetch character files until topic confirmed

### Turn Counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response.

### !log

1. Insert `<!-- SECTION -->` into `chatN.md`
2. Append all turns since last write — **verbatim**. Copy every turn exactly as it appears in context. Do not paraphrase, summarise, or compress any turn for any reason.

### ACTION Flags

When a decision, in-game action, data change, or open question arises, write `**ACTION:** <brief note>` as a standalone line in the response. The end-of-session pass collects and categorises these.

### !check

Critical review of Claude's most recent response. Does not trigger a log write.

### !wrap

Fetch `reference/session-procedure.md` and follow the end-of-session steps.
```

A few notes on choices made:

- Dropped the commit hash extraction step — all URLs come directly from LINKS.md now
- No session-state.json, no index file created at start
- ACTION flags get their own named subsection so they're easy to reference
- The verbatim instruction is terse but emphatic — the detail lives in the procedure file if needed

Happy with this, or any adjustments before we move to the procedure file?

---

**Matt:** Will the `!` commands be understood as commands from the context? I might move the ACTION flags section above the !log section to keep the commands together.

I spend most time fighting against logs that are not verbatim. I think we should keep the full verbatim instruction in this section.

**Claude:** *[Turn 19. Last log: Turn 0.]*

Good points, both. On the commands: they're defined in the overview which Haiku reads at session start, so they should be recognised. But it's worth adding a brief framing line to make explicit that these are commands Matt types — removes any ambiguity.

Revised draft:

```md
## Section 11: Session Procedure

*Full procedure in [`reference/session-procedure.md`](../reference/session-procedure.md) — fetched at `!wrap`.*

### Session Start

1. Read `LINKS.md` — extract all file URLs for use during session
2. Determine new chat number N: add 1 to "latest chat number" in `LINKS.md`
3. Fetch overview file
4. Review Section 9 open questions; flag any resolved items
5. Fetch `data/playthrough.json`
6. Create `/mnt/user-data/outputs/chatN.md` (empty transcript file)
7. Ask what the session is about — do not fetch character files until topic confirmed

### Turn Counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response.

### ACTION Flags

When a decision, in-game action, data change, or open question arises, write `**ACTION:** <brief note>` as a standalone line in the response. The end-of-session pass collects and categorises these.

### Commands

Matt types these commands to trigger specific actions:

**`!log`**
1. Insert `<!-- SECTION -->` into `chatN.md`
2. Append all turns since last write — **verbatim**. Copy every turn exactly as it appears in context — Matt's turns and Claude's turns alike, including all pasted content. Do not paraphrase, compress, summarise, or represent any turn, regardless of length or content. The pull to summarise long or repetitive content is strong — resist it explicitly. If in doubt, copy more rather than less.

   Bracket notation is for tool calls only: `[Fetched X]`, `[Created file Y]`. Never use brackets to summarise substantive response text.

   Insert a blank line between `**Matt:**` and any list item so Markdown renders correctly.

**`!check`** — critical review of Claude's most recent response. Does not trigger a log write.

**`!wrap`** — fetch `reference/session-procedure.md` and follow the end-of-session steps.
```

Changes from the previous draft: ACTION flags moved above the commands block; commands grouped under a single heading with an explicit framing line; verbatim instruction restored to near-full strength with the bracket notation rule included.

---

**Matt:** I’ve tweaked the structure to something a bit more logical to me, and adjusted some of the wording a little bit. Do you think this is better or worse for Haiku?

```md
## Section 11: Session Procedure

*Full procedure in [`reference/session-procedure.md`](../reference/session-procedure.md) — fetched at `!wrap`.*

### Session Start

1. Read `LINKS.md` — extract all file URLs for use during session
2. Determine new chat number N: add 1 to "latest chat number" in `LINKS.md`
3. Fetch `overview/claude-expedition33.md`
4. Review Section 9 open questions; flag any resolved items
5. Fetch `data/playthrough.json`
6. Create `/mnt/user-data/outputs/chatN.md` (empty transcript file)
7. Ask what the session is about — do not fetch character or reference files until topic confirmed

### Turn Counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response.

### ACTION Flags

When a decision, in-game action, data change, or open question arises, write `**ACTION:** <brief note>` as a standalone line in the response. The end-of-session pass collects and categorises these.

### Commands

Matt types these commands to trigger specific actions:

`!log` — log conversation to transcript, following logging process below

`!check` — critical review of Claude's most recent response. Does not trigger a log write.

`!wrap` — fetch `reference/session-procedure.md` and follow the end-of-session steps.

### Logging process

1. Append `<!-- SECTION -->` into `chatN.md` followed by a blank line
2. Append all turns since last write into `chatN.md` — **verbatim**. 

**Turn format:** Matt’s turn first, labelled `**Matt:**`, then a blank line, then Claude’s turn, labelled `**Claude:**`, then a blank line, then a horizontal rule `---`.

**Verbatim logging:** Copy every turn exactly as it appears in context — Matt's turns and Claude's turns alike, including all pasted content. Do not paraphrase, compress, summarise, or represent any turn, regardless of length or content. The pull to summarise long or repetitive content is strong — resist it explicitly. If in doubt, copy more rather than less.

**Bracket notation:** for tool calls only: `*[Fetched X]*`, `*[Created file Y]*`. Never use brackets to summarise substantive response text.

**Lists:** If Matt’s turn begins with a list, insert a blank line between `**Matt:**` and the first list item so Markdown renders correctly.
```

**Claude:** *[Turn 20. Last log: Turn 0.]*

Better, for two reasons:

**Separation of commands from logging process** is the main improvement. Commands are now a scannable quick-reference; the logging procedure is a standalone section. Haiku can find `!log → "logging process below"` without wading through the procedure every time it reads the commands block.

**Explicit turn format** removes a source of ambiguity. The previous version implied the format from examples in the pipeline doc; now it's stated directly where Haiku will actually encounter it.

One small thing to flag: step 3 says "Fetch `overview/claude-expedition33.md`" — strictly speaking Haiku needs to fetch the URL from LINKS.md, not construct the path directly. In practice it'll do the right thing since step 1 extracts all URLs, but it could be made explicit: "Fetch `overview/claude-expedition33.md` using URL from LINKS.md." Minor, but worth tightening since it's a procedure file.

One question on the bracket notation: you've changed from `[Fetched X]` to `*[Fetched X]*` (italicised). Is that intentional — matching the style of the turn counter — or incidental?

Otherwise I'd approve this version as-is and move on to drafting `reference/session-procedure.md`.

---

<!-- SECTION -->
## Testing csplit and Fixing the Section Marker Edge Case

**Matt:** Agree with clarify the URL source. The reason I changed it was that one time I said “fetch the overview file” and Haiku fetched all the files in the overview folder. 

I like the tool calls in italics. Not a big deal either way.

**Claude:** *[Turn 21. Last log: Turn 0.]*

Good — the URL clarification makes sense given that history. I'll phrase it as "using the URL from LINKS.md."

Ready to draft `reference/session-procedure.md`. Before I write: one structural question raised by the new end-of-session model.

Under the new design, Sonnet creates part files directly by writing them out — it has the transcript in context and can use file tools. That makes `split_transcript.py` redundant. Do you want to:

**a)** Remove any mention of the splitter script from the procedure (Sonnet creates part files directly), or  
**b)** Keep an option to run the script as an alternative, in case Sonnet struggles with a very long transcript?

Option (b) adds a fallback but complicates the procedure. My instinct is (a) — Sonnet is well-suited to this and the script was only needed because Haiku couldn't reliably do it. But it's your call since you maintain the scripts.

Similarly: `generate.py` is still needed (regenerates GENERATED marker blocks from JSON after data changes). That stays referenced in the procedure. And the updater script Matt runs manually — that also stays. Just the splitter that becomes redundant.

---

**Matt:** It’s not correct that the splitter “script was only needed because Haiku couldn’t reliably do it.” At the time of writing, I was using Sonnet. The aim was to split the file using a script to avoid having to read the full transcript. In that mode, the transcript and index were built through the session, and the end-of-session run only needed to produce the part files, so a script was more efficient. 

In the new system, we are splitting and reading first, so it’s a different scenario. I think it’s worth keeping (briefly) in the file that the script exists and what it does, but it won’t be used in the new workflow. 

Is it worth specifying in the procedure how the transcript will be split into sections? I assume it’s a `sed` command? Or should we leave it to Sonnet to decide each time?

The updater script and generator script will still be used, that part is unchanged.

**Claude:** *[Turn 22. Last log: Turn 0.]*

Apologies for the mischaracterisation of the splitter — that was sloppy reasoning on my part.

On splitting into sections: worth specifying. Leaving it to Sonnet each time creates variance and occasional errors. A `sed` command is the right tool:

```bash
sed -n '/<!-- SECTION -->/,/<!-- SECTION -->/p' chatN.md
```

Actually the cleaner approach is to split on the markers and write each section to a numbered temp file:

```bash
csplit chatN.md '/<!-- SECTION -->/' '{*}'
```

This produces `xx00`, `xx01`, etc. — one file per section. Sonnet can then read each in sequence. Worth specifying this in the procedure as the canonical method, with the output files going to `/home/claude/` as working files.

However — one thing to verify before I bake this into the procedure: does `csplit` behave consistently on the Ubuntu environment? The split marker `<!-- SECTION -->` appears at the start of each section, so `xx00` will be empty (content before the first marker) and sections start from `xx01`. Worth noting that in the procedure.

Should I draft the procedure now with this specified, or do you want to test the `csplit` command first to confirm the behaviour? Given we're planning to test `!wrap` at the end of this session, testing now might save a rewrite.

---

**Matt:** Ok, here is the transcript of this chat so far. We can use this for testing. Before testing the splitter command, would we test verbatim checking on random turns in the whole transcript or is it better to do that as part of the per-section read?

**Claude:** Per-section — for the same reason we're splitting in the first place. Reading the whole transcript to do verbatim checks upfront defeats the purpose. The check belongs inside the per-section loop: read section, spot-check one turn, then proceed with title/index/actions for that section before moving to the next.

Let me test the `csplit` command on your uploaded transcript now...

Works cleanly. 25 sections (01–25) plus a 2-line header in `section00.md`. Each section file starts with `<!-- SECTION -->` followed by the turns. `section00.md` is just the transcript title — skipped in processing.

So the procedure for `!wrap` would specify:

```bash
csplit chatN.md '/<!-- SECTION -->/' '{*}' --prefix=section --suffix-format='%02d.md'
```

Run in `/home/claude/` as working directory. Skip `section00.md`. Process `section01.md` onward.

Line counts look very manageable — most sections are 5–95 lines, which is trivial for Sonnet to read. The verbatim spot-check then happens naturally: Sonnet reads a section file, picks one turn, compares against its context memory of this chat, flags if it looks summarised.

One thing confirmed by the test: the `<!-- SECTION -->` marker lands at the very top of each section file, which is clean for the second pass to insert a section title directly below it.

Ready to draft `reference/session-procedure.md` now? I have everything I need: the split command confirmed, the four-bin action categorisation, the discrete sequential steps, the changelist format, and the note about the splitter script existing but not used in this workflow.

---

**Matt:** Ah, an interesting edge case in this particular chat. As we are discussing the session procedure, the code `<!-- SECTION -->` has been written multiple times in your and my turns. It appears on 25 lines. Only 8 of those 25 are actually section markers! This would not come up very often in other chats. Maybe split on `^<!-- SECTION -->$` instead?

**Claude:** Good catch. Let me test the anchored pattern:9 files — 8 actual sections plus the header. Same 795 total lines, now correctly split. Let me verify the sections look right... Clean — 8 sections matching Matt's 8 actual log writes. Section boundaries look correct throughout. `^<!-- SECTION -->$` is the right pattern.

Updated command for the procedure:

```bash
csplit chatN.md '/^<!-- SECTION -->$/' '{*}' --prefix=section --suffix-format='%02d.md'
```

Section sizes range from 54 to 177 lines — all very comfortable for Sonnet. `section00.md` is the header, skip it; sections `01` onward are processed in sequence.

Ready to draft `reference/session-procedure.md` now. Shall I go ahead?

---

**Matt:** !log

**Claude:** *[Started writing log from scratch]*

---

<!-- SECTION -->
## Drafting session-procedure.md — First Pass and Decision to Split Files

**Matt:** I stopped you there. You had started logging from scratch. I wasn’t sure what would happen when I called !log, as we’re in the middle of adjusting the logging system. Don’t worry about it, I’ll keep doing the manual log.

Let’s go for drafting the session procedure file.

**Claude:** *[Turn 24. Last log: Turn 0.]**[Turn 25. Last log: Turn 0.]*

A few things I want to flag about choices made:

**Step 3 report cadence** — I've written "report section title and action count to Matt after each section." In a long session that could be verbose. If you'd prefer a silent run with a summary at the end, easy to change.

**Step 2 confirmation** — I've included a stop for Matt to confirm the part grouping before proceeding. You may prefer to skip this and let Sonnet determine grouping automatically.

**`scripts/pipeline.md`** — listed in the scripts table as "superseded by this file." Once you're happy with this document, the old pipeline.md can be deleted or archived. I haven't written a FILE: block for that in the changelist yet — that's for you to decide.

**One gap I noticed while writing:** Step 8 (append !wrap session to transcript) creates a chicken-and-egg situation — to log the !wrap session verbatim, Sonnet would need to write out its own responses from the current chat, which it has in context. That should work fine in practice, but worth flagging as slightly unusual.

What would you like to review or adjust?

---

**Matt:** Ok, I’ve made some changes to that file. I don’t want to assume the Haiku/Sonnet division — some chats may be different. So I’ve tried to generalise a little. Also made some tweaks to the procedure.

Also, if this file is to completely replace `scripts/pipeline.md`, there is an awful amount of detail lost. Here are the headings of the existing file:

```md
# Session Pipeline — Detailed Description
## Core Principle
## File Architecture
### Folder structure
### LINKS.md
### Data files (JSON source of truth)
### Generated files
### Boundary markers
### Changelist format
## Role
### Transcript file
### Index file
### Section markers
### Part files
### Session state file
## Session Start Procedure
## Compound Log Step
## Compaction Detection and Response
## End-of-Session Procedure
## Character File Update Approach
## Changelist Format
### DATA: blocks
### FILE: blocks
### Child
## Scripts
## Key Constraints
## Future Enhancements
```

We’ve lost everything before Session Start Procedure and everything after Changelist Format. The DATA and FILE block descriptions have also been hugely cut down. I think maybe you developed this session-procedure file from the existing overview section 11. Perhaps we need two separate files, one for session-procedure and one for session-design or something?

**Claude:** *[Turn 26. Last log: Turn 0.]*

You're right, and the diagnosis is accurate — I drafted session-procedure.md from Section 11 of the overview rather than from pipeline.md, so the design rationale and architectural detail were left behind.

Two files is the right answer:

**`reference/session-procedure.md`** — operational, fetched at `!wrap`. Covers: commands, ACTION flags, logging process, mid-session escalation, end-of-session steps, changelist format (concise), index format, scripts table, compaction handling. What Sonnet needs to *do* things.

**`reference/session-design.md`** — reference, fetched when needed. Covers: core principle, file architecture, folder structure, LINKS.md, data files, generated files, boundary markers, role descriptions (transcript/index/sections/parts), character file update approach, detailed changelist format with edge cases, key constraints, future enhancements. What anyone needs to *understand* the system.

The DATA:/FILE: block specs are a borderline case — they appear in both. I'd keep the concise version in session-procedure.md (enough for Sonnet to write a changelist) and the full spec with edge cases in session-design.md.

The session-design.md content is largely already written in pipeline.md — it's mostly a rename with minor updates to reflect the new workflow. Whereas session-procedure.md is new content.

Shall I draft session-design.md now by pulling the relevant sections from pipeline.md, or do you want to review and finalise session-procedure.md first?

---

<!-- SECTION -->
## Reviewing and Finalising session-procedure.md — Step Structure and Index Design

**Matt:** Let’s review and finalise session-procedure first. What do you think of my changes?

**Claude:** *[Turn 27. Last log: Turn 0.]*

The changes are good overall. Specific observations:

**Strong improvements:**
- Removing the Haiku/Sonnet assumption throughout — more durable as the model landscape changes
- jsDelivr URLs added to the part headers in Step 2c — I'd left those as placeholders
- Open questions explicitly mapped to a `FILE:` block in Step 5 — cleaner than my vague "any updates to Section 9"
- `chats/chat-index.md` rather than "Section 10 of the overview" — correct, since that was moved in chat 16
- Step 8 including "update the chat index" — I'd missed that the index needs updating after the wrap section is added

**One error to fix:**
Step numbering jumps from Step 6 to Step 8 — Step 7 is missing. My Step 7 (present to Matt) became your Step 6, but the wrap step kept its old number rather than renumbering to 7.

**Two cross-reference errors:**
- "Index File Format" section says "See Step 5 above" — should now be "See Step 4"
- Scripts table entry for `pipeline.md` says "Superseded by this file" — since we're now splitting into two files (session-procedure + session-design), it should say "Superseded by `reference/session-procedure.md` and `reference/session-design.md`"

**One question:**
Step 8 now says "Append `<!-- SECTION -->` and a section header" — should that section header be titled something specific (e.g. "Session Wrap"), or determined by Sonnet based on content?

---

**Matt:** Might as well call it Session Wrap. No real need for flexibility there.

Some follow-ups:

1. The procedure talks about constructing the index in memory and then writing to file in one go. Is that definitely the right way?
2. If building the index file this way is indeed best, should we stick with your simpler notation in step 2c and add the links as part of step 4? Maybe that’s what you intended.
3. Are you happy with the combining of steps 1 and 2 from your original procedure, or are they better separate?
4. Where did the Scripts Reference section come from? I don’t see that in Section 11 of the overview.
5. Is it worth moving the index file format from step 4 into the index file format section and referencing it from step 4, or does that risk poor logic?

**Claude:** *[Turn 28. Last log: Turn 0.]*

Working through each:

**1. Index in memory then single write:** Probably right for most sessions. The risk is a very long session with many sections where accumulated index content becomes unwieldy in context. But in practice the index entries are short (2–3 sentences each) and even a 20-section chat produces maybe 100 lines of index content — well within context limits. Single write also means the file is either complete or absent, no partial states.

**2. Simpler notation in step 2c, links in step 4:** Yes — and I think that's cleaner regardless. Step 2c should stay focused on content (title + description), not URL construction. The jsDelivr links are a formatting concern that belongs in step 4 when you're assembling the file. I'd simplify 2c back to: record title and description, note which part it belongs to. Step 4 constructs the full markdown with links.

**3. Combining steps 1 and 2:** The merge works structurally, but there are actually two confirmation beats in that combined step — one after counting sections, one after proposing part groupings. That's slightly awkward for a single step. Worth either splitting back into two steps or making the two confirmation beats explicit within the combined step.

**4. Scripts Reference:** You're right that it didn't come from Section 11 — I carried it over from pipeline.md when drafting. It belongs in session-design.md rather than here. The only script directly relevant to the procedure is `apply_changelist.py` and `generate.py`, which can be mentioned inline in Step 5 without a full table.

**5. Index format into reference section:** Yes, do it. Step 4 becomes a brief instruction with "following the Index File Format section below." Keeps the step scannable and the template findable as a standalone reference. No logic risk — anyone running step 4 will naturally look up the format section.

---

**Matt:** With 1 and 2, I’m a bit worried about corruption between steps. If you’re confident that building the index in memory in simpler format is ok, then let’s go for it. If you’re rewriting in step 4 anyway, where is best to split into parts: 2c or 4?

With 3, the reason I combined the steps was to remove the first confirmation beat. I think you could output the number of sections but go straight into grouping. After the section lengths are enumerated and part groups are set seems a more sensible place to pause for confirmation.

Happy with 4 and 5.

**Claude:** *[Turn 29. Last log: Turn 0.]*

**1 & 2 — Index building and part split location:**

Confident enough in memory — the conversion from simple notation to full markdown in step 4 is mechanical (lowercase title for anchor, fill in URL template) and less error-prone than constructing URLs mid-section while simultaneously doing spot checks and action categorisation. So: simple notation in 2c, full markdown assembly in step 4.

On where to split into parts: step 2c is the right place to *record* which part each section belongs to (just a label — "Part 1", "Part 2"), since that's determined by the grouping decided at the end of step 1. Step 4 then uses those labels when assembling. The actual file split happens in step 3. So the decision is made in step 1, recorded in 2c, enacted in step 3, reflected in step 4. Clean separation.

**3 — Single confirmation beat:**

Agree with your reasoning. The revised step 1 becomes:

> Run csplit. Report section count. Count lines in all sections and propose part grouping. Stop and confirm with Matt before continuing.

No pause after the section count alone — it's not actionable. The grouping proposal is the natural confirmation point.

Shall I now produce a clean revised version of session-procedure.md incorporating all agreed changes? To summarise what's being fixed:

- Step numbering (Step 8 → Step 7)
- Two cross-reference errors
- Step 8 title fixed to "Session Wrap"
- Steps 1 & 2 merged per your version, with single confirmation beat
- Step 2c simplified (simple notation, part label only)
- Step 4 handles full markdown with links; references Index File Format section
- Scripts Reference section removed; inline mentions only in Step 5
- Index File Format section becomes standalone reference

---

