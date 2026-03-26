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

## List of part files

The files for each chunk are on Github and can be accessed through jsDelivr:

1. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part1.md
2. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part2.md
3. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part3.md
4. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part4.md
5. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part5.md
6. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part6.md
7. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part7.md
8. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part8.md
9. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part9.md
10. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part10.md
11. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part11.md
12. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part12.md
13. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part13.md
14. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part14.md
15. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part15.md
16. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part16.md
17. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part17.md
18. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part18.md
19. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part19.md
20. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part20.md
21. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part21.md
22. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part22.md
23. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part23.md
24. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part24.md
25. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part25.md
26. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part26.md
27. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part27.md
28. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part28.md
29. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part29.md
30. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part30.md
31. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part31.md
32. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part32.md
33. https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@bd8d2870/chats/chat0/chat0-part33.md
