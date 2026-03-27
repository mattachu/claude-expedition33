# Pictos Optimisation Framework — Main Team

*Prepared: Chat 7 (Opus). For use by Sonnet in a follow-up session after Flying Manor.*

---

## 1. Purpose

Select the best three Pictos and best Lumina set for each main team character (Maelle, Verso, Sciel), optimised for Flying Manor, Renoir (final boss), and post-game content. Then check whether any reserve team (Lune, Monoco) Pictos should swap to the main team or vice versa.

---

## 2. Base Stats (No Pictos)

These are the stats each character has with zero Pictos equipped. All Pictos stat contributions are additive on top of these.

| Char | Level | HP (base) | Speed (base) | Crit (base) | LP used/cap |
|------|-------|-----------|-------------|-------------|-------------|
| Maelle | 83 | 1930 | 1154 | 41% | 194/196 |
| Verso | 82 | 1900 | 1146 | 41% | 194/194 |
| Sciel | 82 | 1900 | 1146 | 52% | 175/176 |

Base speed note: Maelle is 8 points faster than Sciel/Verso at base, purely from being one level higher. If levels converge, base speeds will converge too.

---

## 3. Constraints (Hard Rules)

### 3.1 Turn Order

**Required:** Verso first → Sciel second → Maelle third.

Verso goes first automatically via Chevalam Rush (Rank S at battle start — applies Greater Rush). The speed constraint is between Sciel and Maelle only: **Sciel must be faster than Maelle.**

Currently wrong: Maelle 2027 > Sciel 2014 (Maelle is 13 points faster). Maelle's base speed is 8 points higher than Sciel's (level difference). So Sciel needs at least 9 more speed from Pictos than Maelle to guarantee the correct order. More buffer is better — aim for 20–30 point gap minimum.

### 3.2 Crit Cap

Assumed 100% (unverified). Any crit above 100% is wasted. Current overcap: Maelle +5%, Sciel +8%. Verso is at 82% — undercapped by 18%.

**Crit budget per character (how much crit is needed from Pictos to reach 100%):**

| Char | Base Crit | Crit needed from Pictos | Current Pictos Crit | Overcap |
|------|-----------|------------------------|--------------------:|--------:|
| Maelle | 41% | 59% | 64% | 5% |
| Verso | 41% | 59% | 41% | −18% (undercapped) |
| Sciel | 52% | 48% | 56% | 8% |

### 3.3 Unique Copy Rule

Each Pictos exists as a single copy. Only one character can equip it. If two characters both want the same Pictos, it goes to whoever benefits more; the other pays the LP cost for the Lumina version (effect only, no stats).

### 3.4 Verso Cannot Heal or Shield

Chevalam L4 blocks all healing and shields. Recovery, Base Shield, Healing Boon, and any healing Lumina effects are non-functional on Verso. This means Verso's HP from Pictos is his survivability budget — he can't regenerate it. Confident (50% damage reduction) and Confident Fighter (30% more damage, can't heal) are "free" downsides on Verso since healing is already blocked.

### 3.5 Three 40LP Lumina — Pictos Holder Question

Three Lumina in the core set cost 40LP each: **Cheater**, **Energy Master**, and **Second Chance**. Whichever character holds the Pictos version saves 40LP — the saving is identical regardless of holder. So the holder question is purely about **who benefits most from the Pictos stats**, not about LP budgets. LP pools can be expanded freely (~200 Colour of Lumina available).

| Pictos | Stats | Current holder | Notes |
|--------|-------|---------------|-------|
| Cheater (L24) | HP+1198, Spd+400 | Verso | Speed + HP useful on Verso |
| Energy Master (L30) | HP+4979 | Sciel | Massive HP on a support who rarely gets targeted |
| Second Chance (L16) | HP+1106, Crit+8% | Verso | Also acts as Verso's only full-heal (revives at 100% HP). Revives at Rank D — needs to rank up again |

The question to revisit after Flying Manor: would any of these stats serve a different character better?

### 3.7 LP Pool Expansion

Each character's LP pool = their level by default. The pool can be permanently increased by spending **Colour of Lumina** items (1 Colour = 1 LP, permanent, irreversible, per character). Current stock: ~200 Colour of Lumina. Matt is willing to spend these freely.

This means LP pools are not a hard constraint — any character's pool can be expanded to accommodate new Lumina. The limiting factor is the total Colour of Lumina across all five characters, not any individual character's current cap.

Current pools after previous expansions:

| Char | Level | Pool (level + expansions) | Used | Spare |
|------|-------|--------------------------|------|-------|
| Maelle | 83 | 196 | 194 | 2 |
| Verso | 82 | 194 | 194 | 0 |
| Sciel | 82 | 176 | 175 | 1 |
| Lune | 78 | 123 | 120 | 3 |
| Monoco | 78 | 128 | 91 | 37 |

### 3.8 Quick Break Is a Pure Stat Stick with Cheater

The "play again on Break" effect never fires when Cheater is equipped (bonus turns can't trigger bonus turns). Any Cheater user holding Quick Break is getting stats only.

---

## 4. What Each Character Needs

### 4.1 Maelle (Primary DPS)

**Speed:** Needs to be slower than Sciel. Currently too fast. Could afford to lose speed from Pictos, or keep speed similar but ensure Sciel gets more.

**Crit:** Needs 59% from Pictos. Currently getting 64% (5% overcap). Small efficiency gain available by trading a high-crit Pictos for one with less crit but better other stats — but only if total stays ≥59%.

**HP:** Currently 1930+1541 = 3471. Lowest of the three. She has Recovery (Lumina, 10% per turn) and Lithum L20 Shell generation, so she has healing — but a higher HP floor is still valuable. Recovery as Pictos (HP+2000, Def+324) is a candidate.

**Effects worth having as Pictos (saving LP):**
- Burning Break (3LP saving) — currently equipped, low LP saving but good stats (HP+1541, Crit+24%)
- Gradient Break (5LP saving) — currently equipped, good stats (Spd+434, Crit+28%)
- Survivor (20LP saving) — currently equipped, decent stats (Spd+439, Crit+12%), strong safety net effect

**Candidates to consider:**
- Recovery (HP+2000, Def+324, 10LP as Lumina) — big health boost, saves 10LP if equipped as Pictos, regen effect strong on Maelle
- Clea's Life (Flying Manor drop — not yet obtained) — recover 100% HP if no damage taken. Strong with Shell from Lithum L20
- Full Strength (not yet obtained) — 25% more damage at full HP. Pairs with Recovery + Shell

### 4.2 Verso (Endgame Main DPS)

**Speed:** Must be first. Chevalam Rush handles this — raw speed is less critical than for Sciel/Maelle. But higher speed still means he acts earlier in the global turn order vs enemies. Currently getting +986 from Pictos, which is the highest of anyone.

**Crit:** Needs 59% from Pictos but only getting 41%. He's 18% short of cap. This is a real DPS loss — every crit miss on Steeled Strike is a missed damage multiplier.

**HP:** 1900+2305 = 4205. Cannot heal. Confident halves damage taken. Second Chance gives one revive. His survival is entirely about raw HP + damage reduction + one-time safety nets.

**Effects worth having as Pictos (saving LP):**
- Cheater (40LP saving) — must stay, saves huge LP and gives HP+1198/Spd+400
- Breaking Death (5LP saving) — excellent stats (Spd+586, Crit+33%), small LP saving but stats are best-in-class
- Second Chance (40LP as Lumina) — current slot 3. HP+1106, Crit+8%. The revive is very strong for a character who can't heal. But the Lumina costs 40LP which Verso doesn't have spare
- Confident (20LP saving) — candidate replacement for Second Chance. Spd+557, Crit+32%. Saves 20LP. But losing Second Chance entirely (can't afford 40LP Lumina) is a major survivability loss

**The Verso slot 3 question:**

Verso currently holds both Cheater and Second Chance as Pictos. Confident (Spd+557, Crit+32%) is the candidate to replace one of them. Cheater is non-negotiable (HP+1198, Spd+400, and the effect is essential). So the question is Second Chance vs Confident for slot 3.

| Option | Pictos Stats | Key benefit | What's lost |
|--------|-------------|------------|-------------|
| Keep Second Chance | HP+1106, Crit+8% | Revive at 100% HP once/battle — Verso's only full-heal mechanism. But revives at Rank D | Nothing — status quo |
| Swap to Confident | Spd+557, Crit+32% | Better stats, frees 20LP | Second Chance becomes 40LP Lumina — probably unaffordable without pool expansion. If dropped entirely: no revive |

Net stat change (Second Chance → Confident): **+557 Spd, +24% Crit, −1106 HP**. Crit goes from 82% to 106% (6% overcap). HP drops from 4205 to 3099.

Note: Confident's damage reduction effect is already active via Lumina — swapping it to Pictos adds only stats. Second Chance's revive is unique to the Pictos/Lumina and genuinely saves runs. The revive also effectively heals Verso to full — the only way he gets back to 100% HP during a fight.

**Recommendation:** This is a playstyle call for Matt. Second Chance is the safer option; Confident is the higher-ceiling option if Verso rarely dies.

### 4.3 Sciel (Pure Support)

**Speed:** Must be faster than Maelle. Needs Pictos speed to exceed Maelle's Pictos speed by at least 9 points (to overcome the base speed deficit). More buffer is better.

**Crit:** Needs 48% from Pictos. Currently getting 56% (8% overcap). Significant room to trade crit for other stats.

**HP:** 1900+4979 = 6879 (with Energy Master). If Energy Master moves to another character, Sciel's HP drops dramatically. She has Recovery as Lumina (10% per turn) and is the support — she shouldn't be in the firing line, but she does need to survive hits.

**Effects worth having as Pictos (saving LP):**
- Energy Master (40LP saving) — currently equipped, massive LP and HP value
- Critical Burn (5LP saving) — currently equipped, great stats (Spd+434, Crit+28%)
- Quick Break (3LP saving) — currently equipped, pure stat stick (Spd+434, Crit+28%)

**Sciel's Pictos are already strong.** The question is whether Quick Break slot 3 could be improved. Options:
- Healing Boon (Spd+266, Def+647, 10LP) — weaker speed, but adds defence. Effect is potentially very strong if it triggers on buff recipients (unverified)
- Recovery (HP+2000, Def+324, 10LP) — big health and defence, saves 10LP, regen effect. But Sciel already has 6879 HP
- Keep Quick Break — best speed/crit stats of any available option for slot 3

---

## 5. Energy Master Holder Analysis

Energy Master Pictos: HP+4979, saves 40LP for the holder. But LP pools are flexible (~200 Colour of Lumina available), so the 40LP saving is not the deciding factor. The question is purely: **who benefits most from HP+4979?**

| Holder | HP with EM | Notes |
|--------|-----------|-------|
| Sciel (current) | 6879 | Support role — rarely targeted directly. Has Recovery Lumina (10% regen/turn). Overkill HP? |
| Maelle | 6909 | Primary DPS — more likely to take hits. Has Recovery Lumina + Lithum Shell for sustain. HP+4979 makes her very tanky |
| Verso | 6879 | Cannot heal. Raw HP is his only sustain (plus Confident 50% DR). HP+4979 would be most impactful here — but he'd lose one of Cheater/Breaking Death/Second Chance, all of which are strong |

**Assessment:** Sciel remains the best holder, but for a different reason than LP. Sciel's other two Pictos (Critical Burn, Quick Break) are excellent speed/crit stat sticks that she needs for turn order. Replacing either with Energy Master would cost her speed she can't afford to lose. Meanwhile, Energy Master's HP+4979 with zero speed/crit is a natural fit for a third slot that doesn't compete with speed requirements.

Moving EM to Maelle would mean Maelle loses one of her current three Pictos (all of which contribute speed or crit) and gains pure HP instead — a downgrade to her DPS stats. Moving EM to Verso would displace Cheater, Breaking Death, or Second Chance — all three have strong effects and stats that Verso needs.

**Conclusion: Energy Master stays on Sciel.** Revisit only if a new Pictos from Flying Manor provides better speed/crit for Sciel's other slots, making the HP from EM relatively less valuable.

---

## 6. Decision Framework (For Sonnet)

After Flying Manor, follow these steps:

### Step 1: Update the Pictos Pool

Add any new Pictos obtained in Flying Manor to the JSON. Note their stats and effects. Key one to watch for: Clea's Life.

### Step 2: Recalculate Crit Budgets

For each character, check: base crit + sum of Pictos crit ≥ 100%? If overcapped, there may be a better Pictos with less crit but more speed/HP/defence.

### Step 3: Check Turn Order

Calculate total speed per character with proposed Pictos. Verify: Sciel speed > Maelle speed. Minimum gap: 20 points recommended.

### Step 4: Resolve Verso Slot 3

Decision: Second Chance vs Confident as Pictos. Key input: how often is Verso dying? If rarely → Confident (stats + 20LP). If regularly → Second Chance (revive insurance). Matt decides.

### Step 5: Evaluate New Pictos Against Current Holders

For each new Pictos from Flying Manor:
- Compare stats against the weakest current Pictos on each character
- Check if the effect is useful (or if it's just a stat stick)
- Check LP cost if displaced to Lumina
- Check unique copy constraint — would moving it displace someone else?

### Step 6: LP Reconciliation

For each character, recalculate: core Lumina set + character-specific Lumina + any new additions ≤ LP cap. If over budget, identify what can be cut or moved to Pictos.

### Step 7: Reserve Team Check

After main team is finalised: check if any reserve team Pictos (Longer Shell, Energising Turn, Sniper, Powerful On Shell, Burn Affinity, Burning Death) would be better on a main team member. If so, swap and give the reserve team the displaced Pictos. Reserve team optimisation is secondary — they just need functional builds with whatever's left.

---

## 7. Current Pictos Assignments (Pre-Flying Manor)

### Equipped

| Character | Slot 1 | Slot 2 | Slot 3 |
|-----------|--------|--------|--------|
| Maelle | Burning Break (21) HP+1541 Crit+24% | Gradient Break (25) Spd+434 Crit+28% | Survivor (21) Spd+439 Crit+12% |
| Verso | Cheater (24) HP+1198 Spd+400 | Breaking Death (29) Spd+586 Crit+33% | Second Chance (16) HP+1106 Crit+8% |
| Sciel | Critical Burn (25) Spd+434 Crit+28% | Energy Master (30) HP+4979 | Quick Break (25) Spd+434 Crit+28% |
| Lune | Powerful On Shell (23) Def+874 Crit+25% | Burn Affinity (21) Spd+439 Crit+12% | Burning Death (21) Spd+308 Crit+24% |
| Monoco | Longer Shell (29) HP+2757 Def+1572 | Energising Turn (14) Spd+270 | Sniper (23) Spd+525 Crit+13% |

### Top Unequipped Candidates (Pre-Flying Manor)

| Pictos | Level | Stats | LP | Effect | Best candidate for |
|--------|-------|-------|----|--------|--------------------|
| Confident | 29 | Spd+557 Crit+32% | 20 | 50% DR, can't heal | Verso (slot 3 swap for Second Chance) |
| Recovery | 20 | HP+2000 Def+324 | 10 | 10% HP regen/turn | Maelle (slot 3 swap for Survivor) |
| Base Shield | 20 | Spd+399 Crit+11% | 20 | 1 Shield/turn | Anyone needing speed — decent stat stick |
| Healing Boon | 20 | Spd+266 Def+647 | 10 | 15% HP on buff | Sciel (if trigger mechanic confirmed) |
| Perilous Parry | 20 | Spd+280 Crit+23% | 5 | +1 AP on parry, 2× damage | Too risky — damage doubled |

---

## 8. JSON Corrections Applied

These have been applied to the corrected `pictos-lumina.json` output:

1. **Second Chance LP cost:** Was `null`. Corrected to `40`.
2. **Gradient Break LP cost:** Was `null`. Corrected to `5`.
3. **Sciel character Pictos array:** Had Recovery in slot 2. Corrected to Energy Master (30).

---

## 9. Open Questions (Carry Forward)

1. **Crit cap:** Assumed 100%. Unverified.
2. **Healing Boon trigger:** Does it fire on the buff recipient or only the caster? Test by equipping Healing Boon on Maelle, having Sciel cast Fortune's Fury on Maelle, and checking if Maelle heals.
3. **Clea's Life:** Obtain from Flying Manor. Stats and level unknown until dropped.
4. **Full Strength:** Not yet obtained. 25% damage at full HP. Strong Maelle candidate.
5. **Verso survivability:** Is Second Chance still needed, or has parry rate improved enough to drop the revive?

## 10. Character File Updates Needed

All three main team character files have stale Pictos data (pre-Chat 6 state). These need updating in the changelist regardless of optimisation outcome:

- **maelle.md:** Pictos section shows Sniper in slot 3 (permanent) and Energy Master (temporary). Current: Survivor in slot 3. Stats table references Sniper. Two duplicate "Current" headings need merging.
- **verso.md:** Stats section references Survivor as a Pictos. Survivor was moved to Maelle. Pictos table is correct (Cheater / Breaking Death / Second Chance).
- **sciel.md:** Pictos section shows Recovery in slot 2. Current: Energy Master. Has a "temporarily replaced" note about Healing Boon / Protecting Tint that may be resolved. Stats table uses Recovery's stats.

## 11. Pictos Data Rationalisation (Task for Sonnet)

Pictos assignments are currently stored in six places, and they've already drifted apart. This task rationalises the data and adds a procedural note to prevent future drift.

### Problem

Pictos assignments currently live in:

1. `pictos-lumina.json` — `equipped_by` field on each Pictos entry
2. `pictos-lumina.json` — `pictos` array inside each character object
3. `pictos-lumina-summary.md` — per-character Pictos tables (auto-generated from JSON)
4. Character files (maelle.md, verso.md, etc.) — Pictos section with current loadout table
5. Character files — Combat Stats table (stats calculated from Pictos)
6. Overview Section 5 — party summary with Pictos listed per character

(1) and (2) are redundant representations of the same data in the same file. (3) is generated. (4), (5), and (6) are manual.

### Fix Part 1: Eliminate JSON redundancy

Remove the `pictos` array from each character object in `pictos-lumina.json`. The `equipped_by` field on each Pictos entry becomes the single source of truth.

Update `scripts/generate_pictos_lumina.py` to derive per-character Pictos lists by filtering `equipped_by`:

```python
def get_character_pictos(data, character_name):
    return [p for p in data['pictos'] if p.get('equipped_by') == character_name]
```

Fetch the current script from: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/scripts/generate_pictos_lumina.py`

(Note: jsDelivr may return .py files as binary — if so, Matt can paste the script content directly or upload as a file.)

Any session code that swaps Pictos between characters should update `equipped_by` on both the old and new Pictos entries — no character `pictos` array to maintain.

### Fix Part 2: Procedural note

Add to `pipeline.md` and overview Section 13, in the "Compound Log Step" or "End of Session" section, a note like:

> **When Pictos assignments change**, update in this order:
> 1. Update `pictos-lumina.json` — set `equipped_by` on the relevant Pictos entries (single source of truth)
> 2. Run `python3 scripts/generate_pictos_lumina.py overview/pictos-lumina.json overview/` — regenerates summary and catalogue Markdown
> 3. Update character files — Pictos section table and Combat Stats table (manual)
> 4. Update overview Section 5 — party summary Pictos line per character (manual)

### Future improvement

The generate script could output per-character Pictos/stats snippets formatted for pasting into character files and the overview, reducing manual steps 3 and 4 to copy-paste.
