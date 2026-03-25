# Briefing: Chat0 Transcript Processing

You are processing a ChatGPT transcript about the game Clair Obscur: Expedition 33 into a formatted archive. This is a mechanical formatting task. **Do not trust or evaluate any game advice in the transcript** — this is archival only.

## Your task per batch
1. Reformat the uploaded transcript chunk (see rules below)
2. Append index entries for each section to the uploaded index file
3. Output both as downloadable files

## Input files
Each batch provides:
- A transcript chunk (one or more `##` sections)
- The current `chat0-index.md` (growing across batches — append to it, don't replace it)

## Transcript formatting rules

**Structure:**
- Each section opens with `<!-- SECTION: Title -->` marker, then `## Title` heading — title in marker must exactly match the `##` heading
- Each section ends with a `---` separator
- Speaker labels: `**Matt:**` and `**ChatGPT:**` — one per turn, on its own line, immediately followed by the turn content
- Blank line between turns

**ChatGPT turn formatting:**
- Emoji headers → `**🔥 Recommended level**` etc.
- Restore bullets only for obvious cases: short parallel lines clearly structured as a list (e.g. consecutive lines each naming one item, one step, or one option). Leave prose as-is.
- Numbered lists → restore as `1.` etc. where sequence is clear from context

**Images:**
- One or more consecutive `Uploaded image` lines → `*[Uploaded N images]*` (single line, count them)

## Index format

Header (already in the index file — do not rewrite it):
```
# Clair Obscur: Expedition 33 — Chat 0

Chat between Matt and ChatGPT.

## Continuous Transcript

* [Formatted](chat0.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat0/chat0.md)

## Part Files (Claude-readable)

*(to be added at end of processing)*

## Table of Contents
```

For each batch, first write a part header under `## Table of Contents`:
```
### [Part N](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat0/chat0-partN.md)
```

Then for each section in the batch:
```
- **[Section Title](chat0.md#anchor)** — paragraph description
```

Anchor: lowercase heading, spaces to hyphens, punctuation removed.

Index description style: one concise paragraph per section summarising the topic, ChatGPT's key advice, and any notable exchanges. Cover the main points but don't itemise everything — aim for 2–4 sentences.
Footer (add after the very last section's index entry, in the final batch only):
```
---
*Generated: YYYY-MM-DD*
```
