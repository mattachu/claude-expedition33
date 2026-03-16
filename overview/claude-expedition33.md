# Clair Obscur: Expedition 33 — AI Overview File

*Fetched at the start of any session involving this game. Follow all instructions below.*

-----

## Section 1: Topic-Specific Failure Modes

These are in addition to the general failure modes in the startup file:

- **Confabulation about game content:** Training data thin and patchy. Do not give confident answers about mechanics, routes, item availability, or missable content without searching first.
- **Missable/sequence-locked content:** Highest-risk category. Never assert content will be available later without verifying. Default: “I’m not certain — check the wiki.” The Vale bosses incident is the clearest example of this failure mode: ChatGPT explicitly told Matt he could return to Visages after the Axon and would miss nothing. He could not. Three Vale bosses were permanently lost as a result.
- **Wrong advice on record:** Previous sessions contain specific errors. Check character files before advising on that character.
- **Recommending meta builds without checking playstyle fit:** Community recommendations often assume specific builds (e.g. Elemental Genesis). Always verify assumptions before recommending.
- **Not simulating combat turns before recommending changes:** Abstract reasoning from tier rankings is insufficient. Always trace actual turn sequences before advising on weapon or build changes.
- **Confabulating Lumina and skill effects:** Multiple effects described incorrectly across the session. Never assert Lumina or skill effects without verifying from a source.
- **LP arithmetic errors:** Always verify LP point totals before finalising a loadout. Healing Counter listed as 1 LP — it is 10 LP.
- **Accepting corrections without verification:** After repeated corrections, Claude began agreeing without independent checks. Default: acknowledge correction neutrally, flag whether independently verified.
- **Weapon scaling and drop-level assumptions:** Charnon stated as Defence + Agility (correct is Defence + Luck). Nusaro stated as Monoco’s endgame weapon (it is Joyaro, which drops at level 28 post-game). Chevalam stated as available “right now” — correct recommended level to attempt the boss is 70–75+. Always verify weapon scaling, drop source, and recommended level before advising.
- **Passive vs active effect interactions:** Claimed Ramasson’s passive heal triggered Energising Heal — it does not. Verify interaction type before assuming synergy.
- **Asserting rank-jump skills without checking weapon or skill dependency:** Quick Strike jumps to Rank B only with Glaceso equipped (Level 4 ability). Paradigm Shift was claimed to jump to S Rank — it generates 1–3 AP. Rank bonuses apply ONLY at the exact rank stated, not at higher ranks. Always verify.
- **Recommending skills the character doesn’t have:** Light Holder and End Bringer recommended for Verso across multiple summaries — he does not have them. Always confirm the character’s actual skill list before recommending.
- **AoE vs single-target context:** Phantom Stars recommended for Verso’s solo Golgra fight — AoE is useless in 1v1. Check fight context.
- **Second Chance Pictos tracking:** Only one character can hold the Pictos at a time; the effect works once per battle, not repeatedly. Both constraints were forgotten at different points.
- **Overload mechanics:** Described as giving 9 AP to spend in the same turn. Correct: AP refills for the next turn.
- **Serpenphare difficulty:** Initially placed as Phase 2 content (level 60–70). Correct recommended level is 70–80+.
- **Confabulated Lumina entries:** “Plentiful Harvest synergy (6)” listed as a Lumina — not a Lumina, just a description of a synergy. Auto Shell and Base Shield confused (Shell = 20% damage reduction for 3 turns; Shield = damage-blocking HP buffer, 1 per turn from Base Shield).
- **Confirmation bias on skill recommendations:** Accepted the player’s suggested skills (Évêque Spear, Chalier Combo) without independent verification. Always research before confirming.

-----

## Section 2: Playthrough Status

- **Platform:** Xbox Series X
- **Current playthrough:** First playthrough
- **Progress at end of Chat 1 (approx. 1–4 March 2026):**
  - Act 3. Entering Visages with new levelling team (Verso/Monoco/Sciel).
  - Levels: Maelle 64, Lune 63, Sciel 61, Verso 59, Monoco 61.
  - Paintress defeated. Painted Power Pictos equipped.
  - All 5 Gestral Beaches complete.
  - White Nevron quests complete + Blanche reward (100× Colour of Lumina).
  - The Canvas puzzle complete (Painted Me outfit for Maelle).
  - The Chosen Path complete (Base Shield Pictos).
  - Lune’s relationship quest complete (Sirene’s Dress / Chromatic Glissando).
  - Verso’s solo fights complete (vs Francois, vs Monoco).
  - Chromatics defeated: Abbest, Bruler, Lancelier, Orphelin, Troubadour, Luster, Glissando, Ramasseur.
  - **Vale bosses permanently missed** (Jovial Moissonneuse, Sorrowful Chapelier, Seething Boucheclier) — Axon defeated before riddle masks triggered.
  - Moissonneuse Vendange skill obtained by defeating a Moissonneuse in Visages — unrelated to the Vale bosses.
  - Karatom quest permanently missed (requires Gustave alive).
- **Active party:** Verso, Monoco, Sciel (levelling team)
- **Reserve:** Maelle, Lune

-----

## Section 3: Playstyle Notes

- **Free-aim:** Used heavily with Lune (2–3 shots typically, up to 5–6 when stacking burn + mark). Each shot: shield removal, damage, burn (Burning Shots Lumina), mark (Marking Shots Lumina), stain generation (Trebuchim). Maelle uses free-aim less frequently. Free-aim usage expected to drop with Lune/Maelle not in the levelling team.
- **Parry rate:** ~20% against unfamiliar bosses; up to ~100% against well-known enemies after extended grinding. Pattern-recognition is the bottleneck — can require 20+ attempts. Skill is developing, not absent. This is a persistent constraint on risky builds (Overload without Cheater, Defiant Strike’s 30% HP cost, etc.).
- **AP management:** Prefers to use skills every turn if AP allows. Values AP flow highly. **Endgame team (Maelle/Sciel/Verso) AP note:** AP flow is sustainable with Sciel’s Litheson (+3 AP/turn for Sciel on buff/debuff) and Intervention, but requires active management — it is not as straightforward or as quick to refill as Monoco’s Potier Energy. Do not assume freely available AP when advising on endgame team builds.
- **Turn order (levelling team):** Sciel first (Fortune’s Fury before Verso acts), Verso second (Strike Storm with doubled damage), Monoco third (Potier Energy refills AP). Turn order: Sciel ~1812 → Verso ~1436 → Monoco ~1163.
- **Trash fights:** Maelle: Fencer’s Flurry to clear turn 1. With new team: Phantom Stars (Verso AoE at S Rank).
- **Boss fights:** Methodical; learns patterns over multiple attempts. Values break dynamics highly.
- **Status effects:** Primarily burn and mark; limited experience with others.
- **Risk tolerance:** Conservative while parry skills are developing. Prefers empirical testing (99-point attribute method established with Monoco and Sciel). Rejects builds that rely on low-HP states (Overload without Cheater, Berserk Slash) or skills with survival costs (Defiant Strike’s HP cost).

-----

## Section 4: Game Mechanics

### Gradient Skills

Each character has three Gradient Skills, costing 1, 2, and 3 Gradient Charges (GC) respectively. Gradient charges build by spending AP on skills. Gradient Skills are powerful abilities with effects ranging from damage to healing to revival — not all are attacks, hence "Gradient Skills" rather than "Gradient Attacks."

Individual character Gradient Skills are listed in each character file. Details for most characters are not yet confirmed in transcript — placeholders are in place.

-----

## Section 5: Party

**Levelling/mid-game team:** Verso + Monoco + Sciel (targeting Golgra fight and Chromatic Gold Chevaliere)
**Reserve:** Maelle, Lune
**Endgame team (building toward):** Maelle + Sciel + Verso

Character reference files

-----

### Maelle

|                               |                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|
| Level                         | 64                                                                                                            |
| Role                          | Primary DPS                                                                                                   |
| Weapon                        | Medalum (16) → Lithum after The Reacher (level 75–80)                                                         |
| Stats (no Pictos)             | Health 1467, Attack 1819, Speed 893, Defence 565, Crit 25%                                                    |
| Attributes                    | Agility 99, Defence 79, Luck 7, Vitality 7                                                                    |
| Key skills                    | Gustave’s Homage, Sword Ballet, Fleuret Fury, Percée, Fencer’s Flurry, Swift Stride, Stendhal (not yet equipped) |
| Pictos                        | Second Chance, Dead Energy I, Piercing Shot                                                                   |
| Solo Lumina set (The Reacher) | Add: Solo Fighter, Last Stand Critical, Accelerating Last Stand, Empowering Last Stand, Protecting Last Stand |

-----

### Lune

|                   |                                                                         |
|-------------------|-------------------------------------------------------------------------|
| Level             | 63                                                                      |
| Role              | Support/healer/stain DPS                                                |
| Weapon            | Trebuchim (16) — do not replace with Colim or Choralim                  |
| Stats (no Pictos) | Health 2282, Attack 1872, Defence 41, Speed 758, Crit 41%               |
| Attributes        | Luck 91, Vitality 55, Agility 19, Might 16, Defence 8                   |
| Key skills        | Wildfire, Mayhem, Crystal Crush, Healing Light, Revitalization, Rebirth |
| Future weapon     | Kralim (from Chromatic Orphelin, already defeated — check inventory)    |

-----

### Sciel

|                   |                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------|
| Level             | 61                                                                                                      |
| Role              | Pure support                                                                                            |
| Weapon            | Litheson (16) → upgrade to 20: +3 AP per turn when buff/debuff applied (IS her endgame weapon)          |
| Stats (no Pictos) | Health 1314, Attack 2641, Defence 182, Speed 991, Crit 38%                                              |
| Attributes        | Agility 99, Luck 84, Vitality 0, Might 0, Defence 0                                                     |
| Pictos            | Base Shield, Burning Break, Survivor → final: Health 2802, Speed 1812, Crit 82%                         |
| Key skills        | Fortune’s Fury, Intervention, Plentiful Harvest, Focused Foretell, Twilight Dance, Final Path           |
| Lumina (110 LP)   | Core suite + Energising Heal, Healing Parry, Accelerating Heal; Base Shield + Survivor free from Pictos |

-----

### Verso

|                       |                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level                 | 59                                                                                                                                                               |
| Role                  | Mid-game DPS/levelling; endgame main team DPS                                                                                                                    |
| Weapon                | Gaulteram (12) — do not upgrade further; same scaling as Chevalam (Agility + Luck), no respec needed when swapping                                               |
| Stats (no Pictos)     | Health 1184, Attack 1213, Defence 182, Speed 946, Crit 34%                                                                                                       |
| Attributes            | Agility 99, Luck 69                                                                                                                                              |
| Pictos                | Burning Death, Second Chance, Shortcut → final: Health 2291, Speed 1436, Crit 84%                                                                                |
| Skills                | Quick Strike, Assault Zero, Strike Storm, Marking Shot, Phantom Stars, Perfect Break                                                                             |
| Lumina (110 LP)       | Core suite; 4 LP spare. Note: Energising Attack I not appropriate for skill-focused build                                                                        |
| Future weapon         | Chevalam (level 27, from Chromatic Gold Chevaliere, Crimson Forest) — recommended level 70–75+                                                                   |
| Endgame skills to add | Steeled Strike (after getting Cheater Pictos from Sprong); Defiant Strike available but costs 30% HP per use — not recommended while parry skills are developing |

**Note:** Does not have Light Holder, End Bringer, or Steeled Strike yet. Current 6-skill loadout is verified against actual available skills.

-----

### Monoco

|                   |                                                                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level             | 61                                                                                                                                                             |
| Role              | AP battery/support/breaker (levelling team); reserve in endgame                                                                                                |
| Weapon            | Nusaro (10) → upgrade to 20: +1 AP per mask change. Endgame weapon is Joyaro (drops level 28 from Flying Manor Lampmaster, post-game — no Resplendent overlap) |
| Stats (no Pictos) | Health 2359, Attack 3570, Defence 182, Speed 900, Crit 16%                                                                                                     |
| Attributes        | Agility 99, Vitality 64, Luck 20, Might 0, Defence 0                                                                                                           |
| Pictos            | Recovery, Anti-Burn, Energising Turn → final: Health 5892, Speed 1163, Defence 1307                                                                            |
| Skills            | Potier Energy, Stalact Punches, Pelerin Heal, Abbest Wind, Moissonneuse Vendange, Chalier Combo                                                                |
| Lumina (110 LP)   | Core suite + Quick Break, Energising Heal; Energising Turn free from Pictos                                                                                    |

-----

### Core Lumina Suite (all three levelling team members, 106 LP)

Painted Power (5), Teamwork (5), Base Shield (20), Energising Turn (20), Energising Parry (15), Energising Start I (5), Dodger (1), Breaker (10), Breaking Burn (5), Marking Shots (3), Dead Energy I (2), Dead Energy II (2), Critical Break (5), Rewarding Mark (5), Burning Shots (3)

**Lumina expansion cost:** Verso 92→110 (18 Colour), Monoco 90→110 (20 Colour), Sciel 84→110 (26 Colour). Total: 64 Colour of Lumina. Resources at end of chat: 202 available, ~138 remaining after expansion.

-----

## Section 6: Character Reference Files
*Fetch the relevant file at the start of any session focusing on that character in detail. These supersede the brief summaries in Section 5.*

| Character | Role                           | File                                                                                                                                                               |
|-----------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maelle    | Primary DPS                    | [Formatted](maelle.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/maelle.md)     |
| Lune      | Support/healer/stain DPS       | [Formatted](lune.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/lune.md)         |
| Sciel     | Pure support                   | [Formatted](sciel.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/sciel.md)       |
| Verso     | Mid-game DPS / endgame DPS     | [Formatted](verso.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/verso.md)       |
| Monoco    | AP battery / support / breaker | [Formatted](monoco.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/monoco.md)     |

-----
## Section 7: Key Decisions & Context

- **Trebuchim over Colim for Lune:** Colim tested and rejected. 14% attack loss, no free-aim stain generation. Trebuchim optimal for Mayhem/free-aim playstyle. Colim only appropriate for Elemental Genesis builds.
- **Monoco stat respec (Agility 72→99, Vitality 61, Luck 20, Nusaro):** Empirically tested. Key finding: Luck 2× more efficient than Defence for crit. Agility increases Speed, Attack, and Defence stat simultaneously.
- **Sciel over Monoco in main team:** Litheson’s +3 AP/turn (Sciel only, when buff/debuff applied) keeps Sciel self-sufficient. Combined with Intervention (grants extra turn +4 AP to another character), she effectively generates turns and AP for allies — but this is not a direct party-wide AP refill. AP management in the endgame team requires more active attention than with Monoco’s Potier Energy. Ramasson rejected after confirming its passive heal does not trigger Energising Heal.
- **Sciel stat allocation:** Actual at end of chat: Agility 99/Luck 78. Planned optimum (from testing): Luck 89/Agility 49 — Speed 1111 with Pictos, higher attack/crit, still goes before Maelle. With current Pictos (Burning Break instead of Burn Affinity), speed 1812, which still achieves correct turn order. May need recoat to Luck 89 when optimising further.
- **Gaulteram over Glaceso for Verso:** Gaulteram prevents rank loss on hit (loses 1 Perfection only). Same scaling as Chevalam (Agility + Luck) = no respec needed when swapping. Glaceso requires respec now and again when getting Chevalam — net cost 2 Recoats + harder learning.
- **Nusaro upgrade to 20:** Resplendent Catalysts cap at level 19; Joyaro drops at level 28. No overlap. Nusaro Level 20 (+1 AP per mask change) is worth the upgrade.
- **Litheson is Sciel’s endgame weapon:** Confirmed by multiple sources. Upgrade to level 20.
- **Marking Shot over Defiant Strike for Verso:** Both apply Mark 100%. Defiant Strike costs 30% current HP per use — too risky with developing parry skills. Marking Shot: 2 AP, no health cost, damage bonus at C Rank.
- **Rank bonuses work ONLY at exact rank:** Confirmed by multiple community sources and in-game highlighting. Skills show bonus text in yellow at the relevant rank. Passing through a rank means the bonus is only active briefly.
- **Vale bosses missed:** Axon defeated before triggering the mask riddles. All three Vale bosses permanently inaccessible. Moissonneuse Vendange obtained by defeating a Moissonneuse in Visages — unrelated to the Vale bosses.
- **Endgame team:** Maelle + Sciel + Verso. Sciel: Fortune’s Fury (double damage) + Intervention (extra turn + 4 AP). Verso with Cheater + Steeled Strike is primary endgame DPS.
- **Maelle must complete The Reacher before Renoir:** Required for Lithum (endgame weapon) and Gustave resurrection path. Choose “Truth” to reach Relationship Level 7.

-----

## Section 8: Progression Plan

### Phase 1 — Complete (Level 54–63)

- ✅ All 5 Gestral Beaches
- ✅ White Nevron quests + Blanche (100× Colour of Lumina)
- ✅ The Canvas puzzle
- ✅ The Chosen Path (Base Shield Pictos)
- ✅ Verso solo fights
- ✅ Sirene's Dress (Lune relationship)
- ✅ Easy chromatics
- ❌ Vale bosses permanently missed
- ❌ Karatom quest permanently missed

### Phase 2 — Mid-game (Level 60–70)

- Sacred River (Monoco relationship, Level 60–65, Verso + Monoco vs Golgra) → 3× Grandiose, Monoco Level 7
- ✅ Sprong (NW Stone Wave Cliffs, in water, Level 55–75) → Cheater Pictos — essential for Verso's Steeled Strike combo
- Serpenphare (SE Boat Graveyard, Level 70–80+) — try here if confident, otherwise defer to Phase 4
- Chromatic Gold Chevaliere (Crimson Forest, recommended Level 70–75+) → Chevalam for Verso
- Moderate chromatics: Veilleur, Chalier, Chapelier, Braseleur, Hexga, Ballet, Portier, Benisseur, Glaise, Boucheclier, Cruler, Eveque, Bourgeon, Demineur, Barbasucette, Franctale
- Endless Tower floors 1–20

### Phase 3 — Late game (Level 75–80, before Renoir)

- **The Reacher (Maelle solo, MUST do before Renoir)** → Lithum weapon, Maelle Level 6→7, Gustave resurrection path. Choose “Truth” when asked about Gustave.
- Hard chromatics optional here (can defer to post-game): Gault, Reaper Cultist, Petank, Goblu, Aberration, Creation, Lampmaster
- Renoir (final boss, Level 75–80+) → Choose Maelle → “A Life to Paint” → Gustave returns

### Phase 4 — Post-game (Level 80+)

- Flying Manor (4 mini-bosses → Clea superboss) → Clea’s Life Pictos, Perfect Chroma Catalyst; **Joyaro (Monoco’s endgame weapon)** from Lampmaster
- Chromatic Echassier (Level 80–85+)
- Chromatic Pétank superboss
- Chromatic Clair Obscur (Monolith Peak) → Combo Attack II Pictos
- Serpenphare (if not defeated earlier) → Energy Master Pictos (+1 to all AP gained)
- Painting Workshop Beast (Level 80+)
- Endless Tower floors 21–33
- Purchase Charnon (89,884 Chromas, Renoir’s Drafts merchant) — Sciel alternative endgame weapon
- Kill White Nevrons for extra rewards (safe after Blanche reward)
- Karatom quest (now accessible with Gustave alive)
- DLC (Verso’s Drafts, Root of All Evil, secret Endless Tower bosses)

-----

## Section 9: Known Errors from Chat 1

1. **Vale bosses missable (ChatGPT error, not Claude):** ChatGPT said the Vale bosses could be accessed after defeating the Axon, and that nothing in Visages was permanently missable. This was wrong. Three Vale bosses permanently lost: Jovial Moissonneuse, Sorrowful Chapelier, Seething Boucheclier. Matt had explicitly asked whether to explore before fighting the boss; ChatGPT said he could come back later. Moissonneuse Vendange was obtained separately by defeating a Moissonneuse in Visages — unrelated to the Vale bosses. Retained here as a real consequence affecting this playthrough, and as a category to guard against — but not a Claude error.
1. **Colim recommendation:** Recommended over Trebuchim based on Light stain wildcards and community meta. Wrong for Matt’s playstyle. Root error: didn’t simulate turns, didn’t check playstyle assumptions.
1. **Monoco Defence stat advice:** Recommended 0 Defence without knowing Defence contributes to crit rate. Testing showed 0 Defence dropped crit from 23% to 5%.
1. **Fueling Break effect:** Said it gives AP on Break damage. Correct: doubles Burn stacks when enemy is broken.
1. **“Energising Cleanse” invented with wrong effects:** Claude described an “Energising Cleanse” Lumina with incorrect effects. A real Energising Cleanse does exist but its actual effects are different.
1. **Last Stand Lumina effects:** Described as HP-threshold triggers. Correct: solo-fighting bonuses only.
1. **Perfect Recovery:** Described as party heal. Correct: heals Verso only.
1. **Tree of Life gradient cost:** Said 1 Gradient. Correct: 2 Gradient charges.
1. **Revitalization:** Said it removes status effects. Correct: heals only.
1. **Cleansing Tint Lumina:** Said it removes Curse via skills. Correct: only affects Healing Tint consumable items.
1. **Healing Parry effect:** Said 10% heal on parry. Correct: 3%.
1. **Maelle LP budget overrun:** Calculated 118 LP against a 112 LP budget.
1. **Trebuchim AP economy:** Implied +1 AP per individual stain consumed. Correct: +1 AP per consumption event.
1. **Charnon scaling:** Said Defence + Agility. Correct: Defence + Luck.
1. **Charnon/Litheson quote conflation:** Attributed “god tier” and “changes how you play her” quotes to wrong weapons.
1. **Ramasson + Energising Heal synergy:** Claimed passive heal triggers Energising Heal. Correct: weapon passive heals explicitly cannot trigger on-heal Lumina effects.
1. **Quick Strike rank jump:** Said it jumps to Rank B. Correct: requires Glaceso Level 4 ability. Without Glaceso, Quick Strike gives modest Perfection gain.
1. **Phantom Stars for solo fight:** Recommended for Verso’s Golgra solo. AoE is useless in 1v1.
1. **Second Chance Pictos tracking:** Recommended for multiple characters simultaneously. Only one character can hold the Pictos at a time; also only works once per battle.
1. **Paradigm Shift rank jump:** Said it jumps Verso to S Rank. Correct: generates 1–3 AP, with bonus at C Rank.
1. **Lumina skill tree claim:** Said Lumina are unlocked via a skill tree. Correct: unlocked by equipping the corresponding Pictos and winning battles.
1. **Verso’s endgame skills assumed available:** Light Holder and End Bringer recommended across multiple summaries. Verso does not have either.
1. **Renoir described as mid-game boss:** Initially placed in Phase 2 of the progression plan. Correct: Renoir is the final boss.
1. **Nusaro as Monoco’s endgame weapon:** Said Nusaro should be upgraded to 20 as his endgame weapon. Correct endgame weapon is Joyaro (drops at level 28 from Flying Manor Lampmaster, post-game).
1. **Chevalam available “right now”:** Claimed Chevalam accessible at current level (~56). Recommended level for Chromatic Gold Chevaliere is 70–75+.
1. **Serpenphare placed in Phase 2:** Initially said Level 60–70 was appropriate. Correct recommended level is 70–80+.
1. **Rank bonuses claimed to work at rank and above:** Confirmed by community sources and in-game behaviour: bonuses apply ONLY at the exact rank stated. Passing through a rank means the bonus is active only briefly in that window.
1. **Overload AP usage:** Implied 9 AP could be spent on multiple skills in the same turn. Correct: AP from Overload is available the following turn.
1. **“Plentiful Harvest synergy (6)” as a Lumina:** Listed as a Lumina in a loadout. It is not a Lumina — it was a mislabelled description.
1. **Healing Counter cost:** Listed as 1 LP. Correct: 10 LP.
1. **Shell and Shield confused:** Auto Shell gives 20% damage reduction for 3 turns (Shell). Base Shield gives 1 absorb-type defensive buffer per turn (Shield). Described as interchangeable at one point.
1. **Confirmation bias on Monoco skills:** Accepted Évêque Spear and Chalier Combo immediately when Matt suggested them, without independent research. Both were later revised.
1. **Compaction continuity overclaim:** After a compaction event mid-chat, Claude described the compaction summary as fully preserving all context. Some nuance is lost in compaction; this was slightly misleading.

-----

## Section 10: Open Questions

- **Sciel stat recoat:** Actual allocation at end of chat was Agility 99/Luck 78. Planned optimum was Luck 89/Agility 49. Worth recoating to optimum when convenient?
- **Verso skill additions:** Does not yet have Steeled Strike. After obtaining Cheater Pictos (Sprong), swap Paradigm Shift or another slot → Steeled Strike. Also consider whether Defiant Strike is worth adding when parry skills improve (30% HP cost becomes acceptable with high parry rate).
- **Serpenphare timing:** Phase 2 attempt at risk (recommended 70–80+), or defer to Phase 4?
- **Energising Break (3 LP):** Removed from core suite as infrequent. Worth reconsidering in endgame when Break frequency is higher?
- **Maelle relationship level:** Check current level — must reach Level 5 before The Reacher unlocks, Level 7 (via “Truth” choice) for Gustave resurrection path.
- **Lune weapon progression:** Kralim already in inventory. When to switch from Trebuchim to Kralim for Elemental Genesis build? Requires different stat allocation and Cheater for looping.
- **Choralim for Lune:** Already at level 20 in inventory. Sources suggested it as an endgame option alongside Kralim — worth investigating before Lune’s next build session.
- **Gradient Skill details:** All characters have 3 Gradient Skills (1GC, 2GC, 3GC). Most details unconfirmed in transcript — placeholders in character files. Fill in during gameplay sessions.

-----

## Section 11: Character File Template

See `overview/character-file-template.md` in the repo. Fetch only when creating a new character file.

-----

## Section 12: Chat Logs
*For reference only — do not fetch unless specifically asked. These are large files.*

| Chat   | Index                                                                                                                                                         | Full Transcript                     | Summary                                                                                                                                      |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Chat 0 | _None_                                                                                                                                                        | [chat0.md](../chats/chat0/chat0.md) | Prior (abandoned) conversation with ChatGPT; not yet indexed                                                                                 |
| Chat 1 | [Formatted](../chats/chat1/chat1-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat1/chat1-index.md)                  | [chat1.md](../chats/chat1/chat1.md) | Initial build analysis across all five characters; Monoco stat respec; Lune weapon comparison; Sciel and Verso builds; full progression plan |
| Chat 2 | [Formatted](../chats/chat2/chat2-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat2/chat2-index.md)                  | [chat2.md](../chats/chat2/chat2.md) | Endgame skill research; character stat update via voice; chromatic progress; compaction mechanics; session procedure design                  |
| Chat 3 | [Formatted](../chats/chat3/chat3-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat3/chat3-index.md)                  | [chat3.md](../chats/chat3/chat3.md) | Endgame team transition (Cheater Pictos, Steeled Strike, Second Chance resolution); team role framing; burn-stacking vs stance cycling paths; Chevalam mechanics; Maelle LP planning; transcript logging problems identified |

-----

## Section 13: Session Procedure

*Full design rationale: [pipeline.md](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/scripts/pipeline.md)*

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
4. Append turns since last write to `chatN.md` — **verbatim**. Copy turns exactly as they appear in context. No paraphrasing, summarising, or compression. If in doubt, copy more rather than less.
5. Append to `chatN-index.md` under `## Table of Contents`: if this is the first section in a new part, first write part header `### [Part N](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md)`; then append section entry `- **[Section Title](https://github.com/mattachu/claude-expedition33/blob/main/chats/chatN/chatN.md#anchor)** — paragraph description`
6. Update `session-state.json`: append changed `###` sections to `modified_sections`. Set `last_write_timestamp` only if compaction recovery was run in step 3 — otherwise leave as null.

### End of Session

1. Run compound log step — transcript and index now complete
2. Run splitter (`split_transcript.py`) on `chatN.md`
3. Edit `chatN-index.md` directly to add Part Files list under `## Part Files (Claude-readable)`
4. Produce `chatN-changelist.md` covering:
   - Changelist entries for all sections in `modified_sections`
   - New Chat N row for Section 12 of overview (generate summary at this point)
5. Matt pushes to GitHub

### Index File

Header (written at session start, replacing N with actual chat number):

```
# Clair Obscur: Expedition 33 — Chat N

Chat between Matt and Claude.

## Continuous Transcript

* [Formatted](https://github.com/mattachu/claude-expedition33/blob/main/chats/chatN/chatN.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN.md)

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
- **[Section Title](https://github.com/mattachu/claude-expedition33/blob/main/chats/chatN/chatN.md#section-title-anchor)** — paragraph description
```

Part number for section S: ⌈S/4⌉. Part file link: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md`

Anchor derived from `## Title` heading: lowercase, spaces to hyphens, punctuation removed.

End-of-session additions to `chatN-index.md` (done as part of end-of-session step 3):

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
FILE: path/to/file.md
SECTION: ## Parent > ### Child
AFTER: ### Sibling (inserts only — omit for replacements)
CONTENT:
### Child
...full replacement content...

```

- `##`-level replacements: include trailing `-----` separator in CONTENT
- `###` heading must be unique within its `##` parent; renames require direct edit
- Failure mode: loud


### Session State JSON
```json
{"chat": "chatN", "last_write_timestamp": null, "modified_sections": [{"file": "path/to/file.md", "parent": "## Section", "section": "### Subsection"}]}
```

`last_write_timestamp` is only set during compaction recovery (step 3 of the compound log step), sourced from the `start_timestamp` in the JSON transcript output. In a no-compaction session it remains null throughout — this is correct, not an error. The converter script uses this field as an anchor via `--after-timestamp`; it is never needed in the live-writing path.

-----
