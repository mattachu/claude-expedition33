# Clair Obscur: Expedition 33 — Chat 13 — Part 6: Character Stats Screenshots

<!-- SECTION: Character Stats Screenshots -->
## Character Stats Screenshots

**Matt:** Sorry, I forgot to give you the character attributes and stats update. Can you pull out from the screenshot for each character: attribute points for each attribute (left hand side); base stats and modified stats (right hand side) — note, each stat is displayed as MODIFIED (BASE + MODIFIER), except when there is no modifier, and base and modified have the same value. I'll post the images one at a time so you know which is which.

**Claude:** *[Turn 79. Last log: Turn 78.]*

Ready — go ahead and post them one at a time.

---

**Matt:** *[Uploaded Maelle attributes screenshot]* Maelle

**Claude:** *[Turn 80. Last log: Turn 78.]*

**Maelle — Level 93**

Attributes: Vitality 0, Might 81, Agility 99, Defense 0, Luck 99.

Stats: Health 7823 (2232+5591), Attack Power 11156 (1368+9788), Speed 2208 (1228+980), Defense 182, Critical Rate 101% (41%+60%).

Ready for the next one.

---

**Matt:** *[Uploaded Verso attributes screenshot]* Verso

**Claude:** *[Turn 81. Last log: Turn 78.]*

**Verso — Level 93**

Attributes: Vitality 0, Might 81, Agility 99, Defense 0, Luck 99.

Stats: Health 6290 (2232+4058), Attack Power 10668 (1368+9300), Speed 2371 (1228+1143), Defense 182, Critical Rate 122% (41%+81%).

Ready for the next one.

---

**Matt:** *[Uploaded Sciel attributes screenshot]* Sciel

**Claude:** *[Turn 82. Last log: Turn 78.]*

**Sciel — Level 92**

Attributes: Vitality 0, Might 12, Agility 99, Defense 66, Luck 99.

Stats: Health 7172 (2202+4970), Attack Power 8771 (1226+7545), Speed 2519 (1221+1298), Defense 492, Critical Rate 102% (55%+47%).

Ready for the next one.

---

**Matt:** *[Uploaded Lune attributes screenshot]* Lune

**Claude:** *[Turn 83. Last log: Turn 78.]*

**Lune — Level 88**

Attributes: Vitality 99, Might 15, Agility 99, Defense 0, Luck 51.

Stats: Health 3469, Attack Power 10311 (1155+9156), Speed 2568 (1149+1419), Defense 182, Critical Rate 101% (29%+72%).

Ready for Monoco.

---

**Matt:** *[Uploaded Monoco attributes screenshot]* Monoco

**Claude:** *[Turn 84. Last log: Turn 78.]*

**Monoco — Level 88**

Attributes: Vitality 0, Might 0, Agility 99, Defense 99, Luck 66.

Stats: Health 4837 (2080+2757), Attack Power 10881 (1131+9750), Speed 2533 (1168+1365), Defense 2301 (729+1572), Critical Rate 99% (51%+48%).

All five done. A few quick observations before I produce the DATA blocks:

- **Maelle and Verso**: Might has increased from 75 → 81 from levelling.
- **Sciel**: Defence now 66 (was 63), Might 12 (was 9) — levelling has added points.
- **Lune**: Might now 15 (was 9), speed base 1149 (was 1134). Health base 3469 (was 3408).
- **Monoco**: Luck now 66 (was 63), crit rate 99% — very close to cap. Health base 2080 (was 2049).

Shall I produce the DATA blocks for all five characters now, or save them for the end-of-session changelist?

---

**Matt:** Let's go for end-of-session now anyway, so include the !log and DATA blocks in that process.

**Claude:** *[Turn 85. Last log: Turn 78.]*

**In-game actions before next session:**
- Reserve team Lumina review and upgrades (Chat 14 topic)

*[Checked /mnt/transcripts/ — empty]*

Writing the log now... Now producing the final end-of-session changelist... jsDelivr appears to be down temporarily. I'll write the final changelist from what I know, flagging where Section 10 format may need adjusting.

Things to flag on the final changelist:

1. **lp_total values** — calculated as pool-at-last-screenshot plus 2 per level gained since. Maelle/Verso: 269/249 + 2 = 271/251; Sciel: 220 + 2 = 222; Lune: 134 + 2 = 136; Monoco: 137 + 1 = 138. Verify these in-game before applying.

2. **Section 10** — I couldn't fetch the current file due to jsDelivr being down. The table format and the Chat 0–12 rows are written from memory. Verify the format matches the existing file before applying — the Chat 0–12 rows in particular may not be verbatim.

3. **historical-errors.md** — similarly not fetched. I've written a new section `## Recent Errors` which may not exist. Check the file format and add the entry in the correct location/number sequence.

4. **Section 7** — this supersedes the FILE block in changelist5. If changelist5 was already applied, this FILE block replaces it again with the additional Scaverim and Simon entries.

**Splitter command for this session:**
```
python3 scripts/split_transcript.py --sections-per-part 3 chat13.md
```

---

