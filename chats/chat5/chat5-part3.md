# Clair Obscur: Expedition 33 — Chat 5 Transcript

<!-- SECTION: Break Mechanics and Into The Reacher -->
## Break Mechanics and Into The Reacher

**Matt:** I've noticed that my main party has no skills that have high break damage. Are there any suggested skills that have high break damage?

**Claude:** Good observation. Before I search, let me note what I already know from the files: the break mechanic requires bar-fillers (high break damage) and a trigger (Can Break). From what's recorded, the main party has break triggers — Perfect Break (Verso), Fleuret Fury (Maelle, Can Break) — but you're right that I don't see any bar-fillers in the active skill lists. Stalact Punches (Monoco's bar-filler) is on the reserve team.

Let me search rather than guess at what's available to the main party.

[searched "Expedition 33 Verso Maelle Sciel high break damage skills list"]

The search results aren't as specific as I'd like on the bar-filler vs trigger distinction for the main party, so I'll be clear about what's confirmed vs inferred.

**What the main party already has:**
- Fleuret Fury (Maelle) — Can Break (trigger), already equipped
- Perfect Break (Verso) — jumps to Rank S on Break, already equipped
- Quick Break Pictos (Sciel) — adds break damage, already equipped
- Phantom Stars (Verso) — mentioned as a break attack, already in his skill list; at Rank S costs only 5 AP

**Potentially worth adding — bar-fillers:**
- **Final Path (Sciel)** — multiple sources confirm it Can Break, and it's a 4-hit extreme damage skill. Already in her skill list. Notably, one source suggests it can combine with Verso's End Bringer for damage without retaliation. Not clear if it's a bar-filler or trigger though — I'd flag that as unverified.
- **Phantom Stars (Verso)** — described as a break attack dealing 5 hits of extreme damage. Already equipped. At Rank S the 5 AP cost is very reasonable. This may be doing more break bar work than you realise.

Honest caveat: the search results don't clearly identify any main-party skill as a dedicated high-break-damage bar-filler in the way Stalact Punches is for Monoco. It's possible the endgame team is expected to rely on Phantom Stars + Perfect Break as the break pair, and the bar-filling role is simply less developed without Monoco. Worth checking in-game whether Phantom Stars is labelled as high break damage.

---

**Matt:** Looking in-game, there are very few moves marked as high break damage: two each for Lune and Monoco:

Lune
* Crystal Crush: 7AP. Deals high single target Earth and Break damage. 5 hits. Generates 1 Earth + 1 Light Stain. If consumes 2 Lightning Stains: Increased damage. 
* Terraquake: 5AP. Deals low Earth damage and Break damage to all enemies every turn. Also increases all Break damage received by 50%. Duration: 3 turns. Generates 1 Earth + 1 Light Stain. If consumes 2 Lightning, increases duration to 5 turns. 

I recently replaced Crystal Crush with Terraquake in my loadout. 

Monoco
* Stalact Punches. 4AP. Deals medium single target Ice damage. 4 hits. High Break damage.  Moves +4. Heavy Mask: Increased damage. 
* Demineur Thunder. 2AP. Deals low single target Lightning damage. Deals extra Break damage. Moves +5. Caster Mask: Increased Break damage. 

I currently have Stalact Punches equipped on Monoco. 

Both Lune and Monoco are in the reserve team.

**Claude:** That's a significant gap. The main party has break triggers (Perfect Break, Fleuret Fury) but no bar-fillers whatsoever — both high break damage options are on the reserve team, which can only enter when the main party is wiped. So against enemies with tough break bars, the current main party has limited options.

A few things worth thinking through:

**Terraquake's debuff is the most interesting angle.** It increases all break damage received by 50% for 3 turns — that's a party-wide multiplier. If Lune were in the main team even temporarily, one Terraquake could make Verso's Phantom Stars or Maelle's Fleuret Fury punch much harder against the break bar. Worth considering whether Lune warrants a slot in the main team for break-heavy boss fights specifically.

**Verso's Phantom Stars** — does it have any break damage label in-game? It's described as a multi-hit attack and is his current go-to for AoE, but it's not confirmed as a bar-filler. Worth checking.

**The post-Reacher Pictos/Lumina review** you already have flagged would be a good moment to look at this more broadly — are there Lumina that increase break damage you could slot in?

Honest bottom line: this looks like a genuine weakness in the current main party composition for break-heavy fights. Do you want to note it as an open question, or investigate solutions now?

---

**Matt:** Both Phantom Stars and Final Path seem to fill the break bar a lot. I just fought a Mime (which rely on Break mechanics to defeat) and one Phantom Stars got the bar to almost half, the Maelle's attack didn't contribute much, then Sciel filled the bar **and broke** with one hit from Final Path. All characters have the Breaker Lumina equipped, plus other Lumina that increase Break damage (i.e. fill the Break bar). I think, by this stage in the game, characters are more dependent on Lumina sets than specific moves for things like this. Might be swapping in Lune for tough enemies that require multiple breaks.

**Claude:** That's a useful correction, and it makes sense — at this level the Lumina suite is doing a lot of the heavy lifting rather than individual skill labels. Breaker Lumina on all three characters plus whatever other break-boosting Lumina they have means the bar-filling role is distributed across the team rather than concentrated in one dedicated skill.

The practical result from the Mime fight is clear: Phantom Stars fills a significant portion, Final Path fills and triggers reliably. The main party has a working break sequence, it just doesn't look like Stalact Punches on paper.

Worth noting in the error log: I made an assumption that "high break damage" skill labels were the primary indicator of break capability, when in practice Lumina sets and multi-hit skills are doing comparable work by late game. That's a framing error I should guard against in future sessions.

Should I add a note to the overview's game mechanics section clarifying that Lumina (particularly Breaker) contributes significantly to break bar filling, and that the skill label is not the only indicator of break capability?

---

**Matt:** Yes, add the note. Thanks.

**Claude:** [updated session-state.json — added Break Mechanics section to modified_sections]

Noted. Break Mechanics section added to the changelist — will add a note clarifying that Lumina sets and multi-hit skills are the primary break capability drivers by late game, and that the "high break damage" skill label is not the only indicator.

Also adding this to the failure modes list mentally: don't assume break capability is determined by skill labels alone — check Lumina loadout first.

Ready for The Reacher when you are, or anything else first?

---

**Matt:** I'm in the Reacher now, just working my way up.

**Claude:** Good luck! Let me know when you reach the Expedition Flag and we can run through the loadout changes together.

---

**Matt:** !log


<!-- SECTION: Alicia Defeated — Maelle Post-Reacher Build -->
## Alicia Defeated — Maelle Post-Reacher Build

**Matt:** Completed The Reacher! Killed Alicia in two hits… I'm a bit overpowered, I think. I now have Lithum for Maelle. Please load her file. You may need to construct the link so I can paste it for you.

Lithum
* Level 21
* Power 2068
* Element: Void
* Scaling: Luck A, Agility B
* Level 4: In Virtuose Stance, hitting a Marked enemy doesn't remove Mark
* Level 10: Switch to Virtuose Stance on Counterattack
* Level 20: Gain Shell when switching out of Virtuose Stance

So I respecced Maelle to Luck 99, Agility 99 (with 45 attribute points left to spend):
* Health: 3412 = 1871 + 1541 from Pictos
* Attack: 3599 = 1001 + 2598 from weapon scaling
* Speed: 2012 = 1139 + 873 from Pictos
* Defense: 182
* Crit: 105% = 41% + 64% from Pictos

45 in Vitality gives base Health 2624
45 in Might gives Attack 3978 = 1086 + 2892 from weapon scaling
45 in Defence gives base Defense 371 and base Crit 52%

Questions:
1. Best use of attribute points?
2. How to adjust Pictos? — she now has probably more speed and more Crit than she needs
3. What 6 skills to keep on her now?

Current Pictos: Survivor (21), Gradient Break (25), Burning Break (21) — do you have the stats and effects for all these?

**Claude:** Congratulations! Two hits is very satisfying. Here's the link:

`https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d79ec03/overview/maelle.md`

---

**Matt:** It's less satisfying than you might think

https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d79ec03/overview/maelle.md

I think I should upgrade Lithum to level 32. I have 31 Grandiose Chroma Catalysts. I've already upgraded Verso's Chevalam and Sciel's Litheson to level 32. Lune's Kralim is level 29 and Monoco's Joyaro is level 25 (there might be a higher level drop of Joyaro later).

**Claude:** [fetched https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d79ec03/overview/maelle.md]

Good, file read. Several things to flag immediately before answering your questions:

**Lithum scaling correction — this is important.** The file says Lithum scales Defence + Agility (same as Medalum, no respec needed). You've just confirmed it's actually Luck A, Agility B — which is why you respecced. The file is wrong on this point, and the "no respec needed" note is incorrect. This needs fixing. It also means the Glaisum comparison in the file is now different — Glaisum is Defence A, Agility B, so swapping to Glaisum would require a respec back.

**Lithum ability order — now confirmed:**
- Level 4: Mark not removed when hitting in Virtuose ✅
- Level 10: Counterattack → Virtuose ✅
- Level 20: Shell on leaving Virtuose ✅

The open question in the file is resolved.

---

Now to your questions. I want to think carefully rather than rush, so let me be explicit about my reasoning:

**1. Best use of 45 attribute points:**

Luck and Agility are both at 99 — primary and secondary scaling maxed. The options are:
- **Vitality (45):** Base health 1871 → 2624, total health ~4165. Pure survivability.
- **Might (45):** Attack 3599 → 3978, roughly +10.5% damage output. Best for DPS.
- **Defence (45):** Base defence 182 → 371, base crit 41% → 52%. The extra crit is wasted (already at cap with Pictos). Marginal defence gain.

Defence is clearly the weakest option given crit is capped. Between Vitality and Might: for a primary DPS character, Might giving +10.5% attack is hard to argue against, but you're already very powerful (two-hit Alicia). If survivability is a concern, Vitality. If you want to maximise damage, Might. I'd lean Might, but flag that this is a genuine trade-off rather than a clear answer.

**2. Pictos adjustment:**

Current Pictos stats:
- Burning Break (21): Health +1541, Crit +24%
- Gradient Break (25): Speed +424, Crit +28%
- Survivor (21): Speed +439, Crit +12%

Total crit from Pictos: +64%. Base crit: 41%. Total: 105% — 5% over cap, already wasted. Speed total 2012 is very high.

This is a good moment for the full Pictos review flagged post-Reacher. Before I recommend swaps, I'd want to know the stats on the three new Pictos from The Reacher (Draining Cleanse, Protecting Tint, Healing Boon) — you picked them up just before the flag. Do you have their stats and effects?

**3. Skills with Lithum:**

Lithum's L10 (counterattack → Virtuose) changes the rotation significantly. Phantom Strike (switches to Defensive, giving +1AP per parry/dodge) now sets up repeated Virtuose entry via counterattack — it's no longer just an AoE filler, it's a core rotation piece. The loop becomes:

Phantom Strike (→ Defensive) → parry/counterattack → Virtuose (via Lithum L10) → Fleuret Fury or damage skill in Virtuose → repeat

With L4 (Mark persists in Virtuose), Percée becomes more interesting again — the mark doesn't vanish when she attacks in Virtuose, so Rewarding Mark keeps generating AP. Percée still exits Virtuose after one use, but Lithum L10 gives her a way back in without Gustave's Homage every time.

My tentative suggestion for the 6 skills, pending your input:
- Phantom Strike (Defensive setup + AoE)
- Fleuret Fury (sustained Virtuose damage, Can Break)
- Gustave's Homage (Virtuose entry when not countering, 8-hit physical)
- Sword Ballet (big Virtuose burst)
- Percée (2AP in Virtuose, mark stays now)
- Stendhal (nuke option)

That drops Last Chance and Mezzo Forte (solo skills, no longer needed) and restores the party loadout. But I want to flag: this is reasoning from mechanics, not from verified community recommendations for Lithum specifically. Worth a quick search before committing?

**On Lithum upgrade to level 32:** Yes, straightforward. Same as Chevalam and Litheson — Grandiose Chroma Catalysts, 31 available, upgrade away.

**On Lune's Kralim and Monoco's Joyaro:** I'd hold both for now. Kralim at 29 isn't the priority while Lune is reserve. Joyaro — agreed, worth checking if a higher level drop exists post-game before committing Grandiose Catalysts.

---

**Matt:** I ran out of Grandiose. Got from level 21 to level 31 by spending 28. Need 5 to get to level 32, only 3 left. Apparently, Serpenphare rewards include 3 Grandiose + 1 Perfect (level up to 33).

Lithum:
* level: 31
* power: 4651
* scaling unchanged, effects unchanged

Maelle
* Attack: 5652 = 1001 + 4651 from weapon scaling
* Other stats unchanged 

I disagree that defence increase from 182 to 371 is "marginal". But I think I agree that Might is the best option.

**Claude:** Fair correction on Defence — doubling from 182 to 371 is a meaningful survivability gain, and I understated it. The crit being wasted doesn't make the defence stat itself marginal. Might is still the better pick for a primary DPS, but the trade-off is more genuine than I made it sound.

On the Grandiose situation: Serpenphare now has a clear payoff — 3 Grandiose gets Lithum to level 32, and the Perfect Chroma Catalyst takes it to 33. That makes Serpenphare a higher priority than it might otherwise have been, and it's already in Phase 3. Good to know before we finalise the progression order.

Updated Lithum record: level 31, power 4651, scaling Luck A / Agility B, effects confirmed as stated.

Updated Maelle attack: 5652 (1001 base + 4651 weapon scaling). Other stats unchanged.

So — Might it is for the 45 attribute points. That puts Maelle's attack at approximately 3978 base, weapon scaling contribution will increase accordingly. Do you want me to calculate the new total attack figure, or will you check in-game after spending the points?

And shall we move on to the Pictos and skills questions once you have the stats on Draining Cleanse, Protecting Tint, and Healing Boon?

---

**Matt:** With Might 45: Attack 6264 = 1086 + 5178

Without Pictos:
* Monoco: Level 76, Health 1726, Attack 4845, Speed 1025, Defense 729, Crit 38%
* Maelle: Level 81, Health 1871, Attack 6264, Speed 1139, Defense 182, Crit 41%
* Verso: Level 81, Health 1871, Attack 6224, Speed 1139, Defence 182, Crit 41%
* Lune: Level 76, Health 3115, Attack 5365, Speed 1025, Defence 182, Crit 20%
* Sciel: Level 81, Health 1871, Attack 5227, Speed 1139, Defence 371, Crit 52%

New Pictos:
* Protecting Tint: level 20, Health +1403, Defense +681, Healing Tints also apply Shell, 5LP as Lumina
* Healing Boon: level 20, Defense +647, Speed +266, Heal 15% HP on applying a buff (great for Sciel?), 10LP as Lumina
* Energising Shell: level 15, Defense +319, Speed +154, Give 2AP on applying Shell, 10LP as Lumina
* Draining Cleanse: level 20, Health +2000, Defense +324, Consume 1AP to prevent Status Effects application, if possible, 15LP as Lumina
* Breaking Death (29)
* Anti-Blight (24)

I think I've described the last two already.

Do you have the list of best Pictos by stat boost, or was that in another chat?

I think it might be worth creating a new overview file with things like lists of Pictos and Lumina, so it can be fetched when needed. What do you think?

**Claude:** No, a ranked Pictos list by stat boost isn't in any file I've read this session — it may have been discussed in an earlier chat but isn't in the overview or Maelle's file. I don't have it in context.

**On the new overview file idea:** yes, I think that's a good call. The main overview is already large and the session procedure requires fetching it every session regardless of topic. A separate reference file for Pictos and Lumina would let you fetch it only when doing a build session, keeping the main file leaner. It could include things like:

- All known Pictos with level, stat boosts, effect, LP cost
- Core Lumina suite definition
- Per-character Lumina loadouts
- Ranked or grouped views (e.g. by stat type, by LP cost)

Worth scoping properly before creating it. I'd suggest we note it as a post-session infrastructure task rather than doing it now — you've got Maelle's build to resolve first.

**Quick note on the new Pictos:** you listed four, not three — Protecting Tint, Healing Boon, Energising Shell, and Draining Cleanse. Energising Shell wasn't in your earlier list. All noted.

**Healing Boon for Sciel** — your instinct is right. Sciel applies buffs constantly (Fortune's Fury, Intervention, Twilight Dance) so 15% HP heal per buff application would fire very frequently. At 10LP it's cheap. Strong candidate for her loadout, either as Pictos or Lumina.

Before I can answer the Pictos optimisation question properly, I need the stat figures for Maelle's current Pictos at their actual levels. From the file, the Pictos breakdown table shows Burning Break (21), Gradient Break (25), and Survivor (21) — but the stat entries for Survivor aren't in the file (it only had Speed +439, Crit +12% which you gave me earlier). I have:

- Burning Break (21): Health +1541, Crit +24%
- Gradient Break (25): Speed +424, Crit +28%
- Survivor (21): Speed +439, Crit +12%

Is that correct for her current party loadout? And do you want to do the Pictos review just for Maelle now, or wait and do all characters together as the full post-Reacher review?

---

**Matt:** That is correct.

I think it's worth doing all characters now. Will that require loading all the character files? I think it probably will. Before that, is there anything else to change on Maelle now she has Lithum?

**Claude:** Two immediate things:

**1. Solo loadout — has it been restored?** Skills, Pictos, and Lumina all need reverting to party configuration before the full review makes sense. Specifically: Cheater and Second Chance back to Verso, Burning Break and Survivor back as Pictos, solo Lumina swapped back. If you haven't done this yet, do it now before we go further.

**2. Gommage — did you choose "Truth"?** If yes, she's now at Relationship Level 7 and Gommage should be available to learn. That's her 3GC Gradient Skill and described as required for the Renoir fight — worth confirming and adding to her skill list now.

On the skills question with Lithum, I flagged earlier that Lithum L10 (counterattack → Virtuose) changes the rotation meaningfully, and suggested a tentative six-skill loadout. I'd like to do a quick search on Lithum-specific skill recommendations before finalising that, rather than just reasoning from mechanics. Shall I do that now, or hold it for the full character review?

**On the full review requiring character files:** yes, almost certainly. I have Maelle's file in context, but for Verso, Sciel, Lune, and Monoco I'd need to fetch their files — and the stats in those files are already out of date based on changes this session. The most efficient approach is probably to fetch each file as we reach that character, rather than all at once. That way we can also update the changelist accurately as we go.

---

**Matt:** 1. Done
2. Good point, I need to complete the relationship side before that. I'll do that now.

Yes, please search recommended skill loadout with Lithum.

**Claude:** [searched "Expedition 33 Maelle Lithum best skill loadout recommended"]

Good results. Key findings for Lithum specifically:

**The core rotation with Lithum is:**
Phantom Strike (→ Defensive) → parry/counterattack → Virtuose (via Lithum L10) → attack in Virtuose → Lithum L20 grants Shell on leaving Virtuose → repeat

This is confirmed by multiple sources. The counterattack entry into Virtuose is the weapon's defining mechanic, and Phantom Strike setting up Defensive stance is the natural enabler.

**On skills — what sources agree on for Lithum:**

- **Phantom Strike** — core setup skill, confirmed
- **Fleuret Fury** — stays in Virtuose, Can Break, confirmed as essential
- **Gustave's Homage** — still valued for its 8-hit damage and Virtuose entry when you can't counterattack
- **Percée** — with Lithum L4 keeping Mark active in Virtuose, Percée becomes stronger than it was with Medalum. Sources specifically call this out as a key Lithum synergy
- **Burning Canvas** — one wiki source calls it "by far her most damaging ability" with Lithum specifically, because Mark persists through hits. This is a notable departure from the current loadout — worth flagging
- **Stendhal** — still viable as a nuke option but sources note it depletes shields which conflicts with Lithum L20's Shell generation

**What this suggests for your 6 slots:**

The strong core is Phantom Strike, Fleuret Fury, Gustave's Homage, Percée. The 5th and 6th slots are the interesting question — Stendhal vs Burning Canvas vs Sword Ballet. Burning Canvas being flagged as potentially her best skill with Lithum is something I wasn't expecting from the file's contents, and it's a playstyle shift worth considering. Sword Ballet is expensive at 9AP but hits hard in Virtuose.

**Important caveat on Burning Canvas:** it requires burn stacks on the target to reach full potential. Without Lune in the main team, burn application relies on Burning Shots Lumina (free-aim) and possibly Verso's Corpeso base attacks. Worth checking whether burn is reliably on enemies in your current team setup before committing to Burning Canvas as a primary skill.

My suggested 6 for Lithum, pending your call on Burning Canvas:

1. Phantom Strike
2. Fleuret Fury
3. Gustave's Homage
4. Percée
5. Burning Canvas (if burn is reliable) **or** Sword Ballet (if not)
6. Stendhal (nuke option, use sparingly given Shell conflict)

---

**Matt:** Note that Shields and Shell are not the same thing.

**Claude:** You're right — I conflated them again. From the file:

- **Shell** = 20% damage reduction for 3 turns
- **Shield** = damage-blocking HP buffer

Stendhal removes self-shields (the HP buffer), not Shell. Lithum L20 grants Shell (the damage reduction) on leaving Virtuose. There's no conflict between Stendhal and Lithum L20 — they interact with different things entirely. Stendhal remains a clean nuke option with no downside relative to Lithum's Shell generation.

Noted as a recurring error to guard against. Shall I add it to the errors list in Maelle's file?

---

**Matt:** Sure

**Claude:** [updated session-state.json — added Shell vs Shield error to Maelle's errors list]

Added. So — back to the skill loadout. Are you happy with the suggested six (Phantom Strike, Fleuret Fury, Gustave's Homage, Percée, Burning Canvas or Sword Ballet, Stendhal), or do you want to discuss further before deciding?

---

**Matt:** Yes, looks good. Similar to what I had before. I might test out Burning Canvas vs Sword Ballet.

**Claude:** Good plan — the Lithum rotation gives burn more value than Medalum did (mark persistence in Virtuose means Rewarding Mark keeps firing), so Burning Canvas may outperform Sword Ballet in practice even with modest burn stacks. Empirical testing will tell you more than theorycrafting at this point.

Shall I note the skill loadout as confirmed in the changelist, with Burning Canvas/Sword Ballet as "test both" rather than committing to one?

[updated session-state.json with Maelle Lithum build changes and actions]

Done. Maelle's changes are fully tracked. Ready to move on to the full Pictos review — shall I construct the links for the remaining character files so you can paste them one by one?

---

**Matt:** !log


