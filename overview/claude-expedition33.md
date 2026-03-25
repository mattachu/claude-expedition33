# Clair Obscur: Expedition 33 — AI Overview File

*Fetched at the start of any session involving this game. Follow all instructions below.*

---

## Section 1: Topic-Specific Failure Modes

These are in addition to the general failure modes in the startup file:

- **Confabulation about game content:** Training data thin and patchy. Do not give confident answers about mechanics, routes, item availability, or missable content without searching first.
- **Missable/sequence-locked content:** Highest-risk category. Never assert content will be available later without verifying. Default: "I'm not certain — check the wiki." The Vale bosses incident is the clearest example of this failure mode: ChatGPT explicitly told Matt he could return to Visages after the Axon and would miss nothing. He could not. Three Vale bosses were permanently lost as a result.
- **Wrong advice on record:** Previous sessions contain specific errors. Check character files before advising on that character.
- **Recommending meta builds without checking playstyle fit:** Community recommendations often assume specific builds (e.g. Elemental Genesis). Always verify assumptions before recommending.
- **Not simulating combat turns before recommending changes:** Abstract reasoning from tier rankings is insufficient. Always trace actual turn sequences before advising on weapon or build changes.
- **Confabulating Lumina and skill effects:** Multiple effects described incorrectly across the session. Never assert Lumina or skill effects without verifying from a source.
- **LP arithmetic errors:** Always verify LP point totals before finalising a loadout. Healing Counter listed as 1 LP — it is 10 LP.
- **Accepting corrections without verification:** After repeated corrections, Claude began agreeing without independent checks. Default: acknowledge correction neutrally, flag whether independently verified.
- **Weapon scaling and drop-level assumptions:** Charnon stated as Defence + Agility (correct is Defence + Luck). Nusaro stated as Monoco's endgame weapon (it is Joyaro). Chevalam stated as available "right now" — correct recommended level to attempt the boss is 70–75+. Always verify weapon scaling, drop source, and recommended level before advising.
- **Passive vs active effect interactions:** Claimed Ramasson's passive heal triggered Energising Heal — it does not. Verify interaction type before assuming synergy.
- **Asserting rank-jump skills without checking weapon or skill dependency:** Quick Strike jumps to Rank B only with Glaceso equipped (Level 4 ability). Paradigm Shift was claimed to jump to S Rank — it generates 1–3 AP. Rank bonuses apply ONLY at the exact rank stated, not at higher ranks. Always verify.
- **Recommending skills the character doesn't have:** Light Holder and End Bringer recommended for Verso across multiple summaries — he now has both, but always confirm the character's actual skill list before recommending.
- **AoE vs single-target context:** Phantom Stars recommended for Verso's solo Golgra fight — AoE is useless in 1v1. Check fight context before recommending AoE skills.
- **Second Chance Pictos tracking:** Only one character can hold the Pictos at a time; the effect works once per battle, not repeatedly. Both constraints were forgotten at different points.
- **Overload mechanics:** Described as giving 9 AP to spend in the same turn. Correct: AP refills for the next turn.
- **Serpenphare difficulty:** Initially placed as Phase 2 content (level 60–70). Correct recommended level is 70–80+.
- **Confabulated Lumina entries:** "Plentiful Harvest synergy (6)" listed as a Lumina — not a Lumina, just a description of a synergy. Auto Shell and Base Shield confused (Shell = 20% damage reduction for 3 turns; Shield = damage-blocking HP buffer, 1 per turn from Base Shield).
- **Confirmation bias on skill recommendations:** Accepted the player's suggested skills (Évêque Spear, Chalier Combo) without independent verification. Always research before confirming.
- **Flying Manor incorrectly stated as required:** Claimed Flying Manor was a mandatory story chapter that must be completed before Renoir. Correct: it is optional. The only mandatory pre-Renoir story content is The Reacher. The final boss is fought inside Lumière at the end of that dungeon — not at the Monument.
- **Final boss location:** Said the Act 3 final fight was at the Monument. Correct: the final boss is fought inside Lumière at the end of that dungeon. The Monument fight was the Act 2 climax.
- **Joyaro drop location:** Said Joyaro drops exclusively from Flying Manor Lampmaster post-game. Correct: also drops from Ultimate Sakapatate in Endless Night Sanctuary (level 25), and is purchasable from a River of Life merchant.
- **Teamwork Lumina effect:** Said Teamwork gives AP when an ally uses a skill. Correct: passive damage bonus when the whole team is alive.
- **Stendhal AP cost:** Said 4 AP. Correct: 8 AP. Also applies Defenceless to Maelle herself on use. Was nerfed 40% in Patch 1.2.3 — no longer one-shots Alicia.
- **Gaulteram described as Act 3 best option:** Gaulteram is consensus Act 2 weapon. Community S-tier Act 3 weapons are Chevalam, Contorso, Corpeso, Simoso.

---

## Section 2: Playthrough Status

- **Platform:** Xbox Series X
- **Current playthrough:** First playthrough
- **Status as at end of Chat 5 (approx. 24 March 2026):**
  - Act 3, Phase 3. All characters level 76–82.
  - Active endgame team: Verso (81), Maelle (82), Sciel (81). Reserve: Lune (76), Monoco (77).
  - The Reacher complete. Gommage unlocked (Relationship Level 7). Serpenphare defeated.
  - **Permanently missed:** Vale bosses (Jovial Moissonneuse, Sorrowful Chapelier, Seething Boucheclier); Karatom quest (requires Gustave alive).

- **Inventory:**
  - Colour of Lumina: reduced from 150 (multiple LP pool expansions this session) — check in-game
  - Recoats: 27 (as at Chat 4 — may have changed)
  - Chroma Catalysts: 67 standard, 61 Polished, 52 Resplendent, Grandiose count unknown (spent heavily this session)

- **Reserve:** Lune, Monoco

---

## Section 3: Playstyle Notes
*Last updated: Chat 4*

- **Free-aim:** Used heavily with Lune (2–3 shots typically, up to 5–6 when stacking burn + mark). Each shot: shield removal, damage, burn (Burning Shots Lumina), mark (Marking Shots Lumina), stain generation (Trebuchim). Maelle uses free-aim less frequently. Free-aim usage expected to drop with Lune/Maelle not in the levelling team.
- **Parry rate:** ~20% against unfamiliar bosses; up to ~100% against well-known enemies after extended grinding. Pattern-recognition is the bottleneck — can require 20+ attempts. Skill is developing, not absent. This is a persistent constraint on risky builds (Overload without Cheater, Defiant Strike’s 30% HP cost, etc.).
- **AP management:** Prefers to use skills every turn if AP allows. Values AP flow highly. **Endgame team (Maelle/Sciel/Verso) AP note:** AP flow is sustainable with Sciel’s Litheson (+3 AP/turn for Sciel on buff/debuff) and Intervention, but requires active management — it is not as straightforward or as quick to refill as Monoco’s Potier Energy. Do not assume freely available AP when advising on endgame team builds.
- **Turn order (levelling team):** Sciel first (Fortune’s Fury before Verso acts), Verso second (Strike Storm with doubled damage), Monoco third (Potier Energy refills AP). Turn order: Sciel ~1812 → Verso ~1436 → Monoco ~1163.
- **Trash fights:** Maelle: Fencer’s Flurry to clear turn 1. With new team: Phantom Stars (Verso AoE at S Rank).
- **Boss fights:** Methodical; learns patterns over multiple attempts. Values break dynamics highly.
- **Status effects:** Primarily burn and mark; limited experience with others.
- **Risk tolerance:** Conservative while parry skills are developing. Prefers empirical testing (99-point attribute method established with Monoco and Sciel). Rejects builds that rely on low-HP states (Overload without Cheater, Berserk Slash) or skills with survival costs (Defiant Strike’s HP cost).

---

## Section 4: Game Mechanics

### Gradient Skills

Each character has three Gradient Skills, costing 1, 2, and 3 Gradient Charges (GC) respectively. Gradient charges build by spending AP on skills. Gradient Skills are powerful abilities with effects ranging from damage to healing to revival — not all are attacks, hence "Gradient Skills" rather than "Gradient Attacks."

Individual character Gradient Skills are listed in each character file. Details for most characters are not yet confirmed in transcript — placeholders are in place.

### Break Mechanics

There are two distinct types of Break skills:
- **Break bar filling skills** (labelled "High Break damage"): Deal high damage to the break bar to fill it up over multiple hits. Example: Stalact Punches, Terraquake.
- **Break trigger skills** (labelled "Can Break"): Land the final hit that actually triggers the Break when the bar is full. Example: Moissonneuse Vendange, Mayhem, Final Path.

A team typically needs both types — a filler to build the bar and a trigger to fire it. Some gradient skills combine both (e.g. Monoco's Break Point fills and triggers simultaneously).

**Note:** By late game, Lumina (particularly Breaker) contributes significantly to break bar filling across all characters. The break capability of a team depends more on Lumina sets than on individual skills labelled as "high break damage." Multi-hit skills (e.g. Phantom Stars, Final Path) fill the break bar substantially even without that label. The skill label is not the sole indicator of break capability.

### Pictos and Lumina

Pictos are collectible items (3 slots per character) giving stat boosts and effects. Learning a Pictos (4 battles) unlocks it as a Lumina — effect only, no stat boosts, costs LP. Any Lumina costs 0LP for a character who has that Pictos equipped. With attributes maxed at 99, Pictos stat boosts are the primary source of character growth.

**Full reference:** `overview/pictos-lumina.json` (definitive data source — 194 Pictos, obtained status, equipped/Lumina loadouts). Two generated Markdown files:

| File | Purpose | When to read |
|---|---|---|
| `pictos-lumina-summary.md` [Formatted](pictos-lumina-summary.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/pictos-lumina-summary.md) | Core Lumina sets, per-character loadouts, situational, candidates | Any session involving Pictos/Lumina advice |
| `pictos-lumina-catalogue.md` [Formatted](pictos-lumina-catalogue.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/pictos-lumina-catalogue.md) | All 194 Pictos grouped by category with effects and LP costs | When browsing or searching the full catalogue |
| `pictos-lumina.json` [Repo](pictos-lumina.json) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/pictos-lumina.json) | Raw JSON — query directly for specific Pictos data | When Claude needs to look up or modify specific entries |

Generated by: `python3 scripts/generate_pictos_lumina.py overview/pictos-lumina.json overview/`

### Tints

Tints are consumable items, distinct from skills. There are three types: Healing Tints (restore HP), Revive Tints (revive a fallen ally), and Energy Tints (restore AP). Tints are upgraded using Shapes; the maximum number carried is increased using Shards. Tints are consumed on use and refilled on Rest.

**Important:** Pictos/Lumina effects that trigger "on applying a heal" or "on applying Shell" behave differently depending on source:
- *Protecting Tint Lumina*: fires when a **Tint** is used — not when a healing skill is used.
- *Protecting Heal Lumina*: fires when a **skill** heals an ally — not on Tint use.

### Attribute System

Characters gain 3 attribute points per level up. Points are held in reserve and can be spent at any Flag. Points committed to an attribute are permanent unless a Recoat is used (resets all attributes and skill points to zero, returning all spent points). Attributes cap at 99 — points cannot be spent on an attribute already at 99.

### Reserve Party

If the main party (Verso/Maelle/Sciel) is fully wiped in a battle, the player can continue the battle using the reserve party (Lune and Monoco). This is most relevant for hard bosses. Lune and Monoco should not be stripped of all useful Pictos/Lumina — but main party optimisation takes priority for the vast majority of battles.

---

## Section 5: Party
*Last updated: Chat 4*

**Active endgame team:** Verso + Maelle + Sciel (Cheater equipped on all three via Lumina)
**Reserve:** Lune, Monoco

**Speed order (intended):** Verso goes first via Chevalam Rush (Rank S at battle start). Sciel second, Maelle third. Gradient Break Pictos on Maelle has pushed her above Sciel — needs tweaking.

### Maelle

|                               |                                                                                                     |
|-------------------------------|-----------------------------------------------------------------------------------------------------|
| Level                         | 82                                                                                                  |
| Role                          | Primary DPS                                                                                         |
| Weapon                        | Lithum (33) — Power 9254, Void, Luck S / Agility A. L4: In Virtuose, hitting Marked enemy doesn't remove Mark. L10: Switch to Virtuose on Counterattack. L20: Gain Shell on leaving Virtuose. |
| Stats (with Pictos)           | Health 8411, Attack 10363, Speed 1580, Defence 182, Crit 93% — **Speed too low, Pictos review pending** |
| Attributes                    | Luck 99, Agility 99, Might 48                                                                       |
| Pictos                        | Burning Break (21), Gradient Break (25), Energy Master (30) — **temporary while learning Energy Master** |
| Key skills (active)           | Phantom Strike, Fleuret Fury, Gustave's Homage, Percée, Stendhal + test Burning Canvas vs Sword Ballet |
| Gommage                       | ✅ Unlocked (Relationship Level 7). Confirmed extremely powerful — 3.4M damage on Serpenphare. Required for Renoir fight. |
| Lumina                        | 164LP used / 165LP total. See [pictos-lumina-summary.md](pictos-lumina-summary.md) §5 for full loadout. |
| Note                          | Lithum L4: Mark not removed in Virtuose. L10: Counterattack → Virtuose. L20: Shell on leaving Virtuose — Longer Shell and Powerful on Shell will synergise. Shell ≠ Shield. |

### Verso

|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Level             | 81                                                                                                               |
| Role              | Endgame main DPS                                                                                                 |
| Weapon            | Chevalam (32) — Agility A, Luck B; Power 5033                                                                   |
| Stats (with Pictos) | Health 3776, Attack ~6500+, Speed 2125, Defence 182, Crit 82%                                                |
| Attributes        | Agility 99, Luck 99, Might 27                                                                                    |
| Pictos            | Cheater (24), Breaking Death (29), Second Chance (16)                                                            |
| Key skills        | Quick Strike, Light Holder, Marking Shot, Perfect Break, End Bringer, Steeled Strike                            |
| Lumina            | 154LP used / 154LP total. See [pictos-lumina-summary.md](pictos-lumina-summary.md) §5 for full loadout. |
| Note              | Chevalam L20: Rush on Rank S — Verso always goes first. Breaking Death synergy: on death → break bar fills → Perfect Break → Rank S in one move. Survivor Lumina (20LP) covers survival. Breaking Death Pictos kept for stat boosts (Speed +586, Crit +33%). |

### Sciel

|                     |                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------|
| Level               | 81                                                                                                           |
| Role                | Pure support                                                                                                 |
| Weapon              | Litheson (32) — Power 4226, Physical, Luck A, Agility B. L4: Moon = Greater Rush all allies / Sun = Greater Slow all enemies. L10: Twilight = both. L20: +3 AP on applying Buff or Debuff, once per turn. |
| Stats (with Pictos) | Health 3755, Attack 3010, Speed 1978, Defence 636, Crit 100% (capped)                                      |
| Attributes          | Agility 99, Luck 99, Defence 33                                                                              |
| Pictos              | Critical Burn (25), Recovery (20), Quick Break (25) — **note: temporarily replaced by Healing Boon/Protecting Tint while learning; revert when learnt** |
| Key skills          | Fortune's Fury, Intervention, Plentiful Harvest, Final Path, Twilight Dance, Grim Harvest                   |
| Lumina              | 170LP used / 175LP total. See [pictos-lumina-summary.md](pictos-lumina-summary.md) §5 for full loadout. |
| Note                | Critical Burn Pictos fixed turn order — Sciel now goes before Maelle (Speed 1978 vs 1956). Quick Break never fires with Cheater — pure stat stick. Grim Harvest replaces Focused Foretell. |

### Lune

|                   |                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| Level             | 76                                                                                                           |
| Role              | DPS / healer (reserve)                                                                                       |
| Weapon            | Kralim (29)                                                                                                  |
| Stats (with Pictos) | Health 3989, Attack 5365, Speed 1772, Defence 1056, Crit 81%                                              |
| Attributes        | Vitality 99, Agility 99, Luck 30                                                                             |
| Pictos            | Powerful on Shell (23), Burn Affinity, Burning Death (21)                                                   |
| Key skills        | Wildfire, Terraquake, Thunderfall, Elemental Genesis, Healing Light, Mayhem                                  |
| Lumina            | 133LP used / 133LP total. See [pictos-lumina-summary.md](pictos-lumina-summary.md) §5 for full loadout. |
| Note              | Protecting Heal activates Shell on every Healing Light cast — synergises with Longer Shell on Monoco. Burn Affinity fires immediately from Wildfire turn 1. Cheater deferred. |

### Monoco

|                     |                                                                                                                    |
|---------------------|--------------------------------------------------------------------------------------------------------------------|
| Level               | 77                                                                                                                 |
| Role                | Break + AP support (reserve team with Lune)                                                                        |
| Weapon              | Joyaro (25)                                                                                                        |
| Stats (with Pictos) | Health 4483, Attack 4810, Speed 1824, Defence 2301, Crit 51%                                                      |
| Attributes          | Agility 99, Defence 99, Luck 24                                                                                    |
| Pictos              | Longer Shell (29), Energising Turn (14), Sniper (23)                                                               |
| Key skills          | Potier Energy, Stalact Punches, Abbest Wind, Moissonneuse Vendange, Portier Crash, Chalier Combo                   |
| Lumina              | 111LP used / 127LP total. See [pictos-lumina-summary.md](pictos-lumina-summary.md) §5 for full loadout. |
| Note                | Longer Shell extends Shell applied by Lune's Healing Light (via Protecting Heal). Sniper is pure stat stick — effect irrelevant for Joyaro build. |

### Core Lumina Suite

Main team core: 154LP (Maelle, Verso, Sciel). Reserve team core: 110LP (Lune, Monoco). Full breakdown with effects in [pictos-lumina-summary.md](pictos-lumina-summary.md) §3–4. Character-specific additions on top of core sets in §5.

---

## Section 6: Character Reference Files
*Fetch the relevant file at the start of any session focusing on that character in detail. These supersede the brief summaries in Section 5.*

| Character | Role                           | File                                                                                                                                                               |
|-----------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maelle    | Primary DPS                    | [Formatted](maelle.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/maelle.md)     |
| Lune      | Support/healer/stain DPS       | [Formatted](lune.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/lune.md)         |
| Sciel     | Pure support                   | [Formatted](sciel.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/sciel.md)       |
| Verso     | Mid-game DPS / endgame DPS     | [Formatted](verso.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/verso.md)       |
| Monoco    | AP battery / support / breaker | [Formatted](monoco.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/monoco.md)     |

---

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

---

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
- ❌ Karatom quest permanently missed (requires Gustave alive)

### Phase 2 — Mid-game (Level 60–70) — Complete

- ✅ Sacred River (Monoco relationship, Golgra) → 3× Grandiose, Monoco Level 7
- ✅ Sprong (NW Stone Wave Cliffs, in water) → Cheater Pictos
- ✅ Chromatic Gold Chevaliere (Crimson Forest) → Chevalam for Verso
- ✅ Dark Shore → Corpeso for Verso
- ✅ Grosse Tete, Frost Eveque, Thunder Eveque
- ✅ Chromatics: Veilleur, Chalier, Glaise, Demineur, Chapelier, Hexga, Ballet, Portier, Benisseur, Boucheclier, Cruler
- ✅ Ultimate Sakapatate (Endless Night Sanctuary) → Joyaro for Monoco

### Phase 3 — Late game (Level 75–80, before Renoir)

- **The Reacher (Maelle solo, MUST do before Renoir)** → Lithum weapon, Maelle Level 6→7, Gustave resurrection path. Choose "Truth" when asked about Gustave.
- Chromatic Braseleur (inside The Reacher)
- Serpenphare (SE Boat Graveyard, Level 70–80+)
- Endless Tower floors 1–20
- Chromatic Eveque (Endless Tower)
- Flying Manor (Clea, optional but recommended before finale) → Clea's Life Pictos, Perfect Chroma Catalyst; Joyaro also available here if not already obtained
- **Renoir (final boss)** → enter Lumière → fight at end of dungeon. *[Choose Maelle → "A Life to Paint" → Gustave returns]*

### Phase 4 — Post-game (Level 80+)

- Kill White Nevrons for extra rewards (safe after Blanche reward)
- Dark Gestral Arena
- Hard chromatics: Gault, Reaper Cultist, Petank, Goblu, Aberration, Lampmaster
- Chromatic Bourgeon (Monolith)
- Chromatic Clair Obscur (Monolith Peak) → Combo Attack II Pictos
- Chromatic Echassier (Level 80–85+)
- Chromatic Pétank superboss
- Renoir's Drafts (Simon, Level 90+) — post-game; connects to Julie/Verso journal thread
- Purchase Charnon (89,884 Chromas, Renoir's Drafts merchant) — Sciel alternative endgame weapon
- Chromatic Creation (Renoir's Drafts)
- Verso's Drafts (DLC) — post-game epilogue; extends the Verso/Expedition 00 story
- Chromatic Barbasucette (Verso's Drafts)
- Chromatic Franctale (Verso's Drafts)
- Endless Tower floors 21–33

---

## Section 9: Open Questions

- **Maelle Pictos review:** Speed dropped to 1580 after swapping Survivor for Energy Master (temp). Review Pictos once Energy Master is learnt and long-term holder decided.
- **Energy Master long-term holder:** Maelle (AP synergy — every AP gain +1 is very strong with Lithum rotation) vs Sciel (Health +4979). Decide after 4 battles learning. LP cost: 40LP.
- **Monoco Pictos slot:** If paying 20LP for Energising Turn Lumina, what replaces the Energising Turn Pictos slot? Deferred until Pictos catalogue complete. Quick Break (10LP) as Lumina also a candidate.
- **Maelle Lumina additions:** Longer Shell (10LP) and Powerful on Shell (10LP) synergise with Lithum L20 Shell generation. Add — expand pool by 20 Colour of Lumina.
- **Maelle skills:** Test Burning Canvas vs Sword Ballet as 6th skill slot empirically.
- **Sciel Lumina:** Add Healing Boon (10LP) once Healing Boon and Protecting Tint are learnt (one battle remaining). Revert Pictos to Critical Burn / Recovery / Quick Break after learning.
- **Empowering Dodge (5LP):** Reset behaviour on parry unconfirmed — test empirically before committing LP.
- **Energising Burn (10LP):** Consider when next expanding core Lumina suite — all characters have Burning Shots.
- **Full Strength Pictos:** Not yet obtained. Effect: 25% increased damage at full Health. Strong candidate for Maelle given Recovery + Shell from Lithum. Find as you progress.
- **Clea's Life Pictos:** From Flying Manor (Phase 3). Recovers 100% Health on turn start if no damage taken since last turn. Strong survivability for Maelle. Note for Flying Manor visit.
- **Verso skills file:** Stale — still shows Assault Zero and Strike Storm as equipped. Correct loadout: Quick Strike, Light Holder, Marking Shot, Perfect Break, End Bringer, Steeled Strike.
- **Pictos/Lumina reference file:** Complete ✅ — `overview/pictos-lumina.json` (194 entries, 133 obtained), two generated Markdown files. Pipeline updated for session tracking. See Section 4 for links.

---

## Section 10: Chat Logs
*For reference only — do not fetch unless specifically asked. These are large files.*

| Chat   | Index                                                                                                                                                         | Full Transcript                     | Summary                                                                                                                                      |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Chat 0 | _None_                                                                                                                                                        | [chat0.md](../chats/chat0/chat0.md) | Prior (abandoned) conversation with ChatGPT; not yet indexed                                                                                 |
| Chat 1 | [Formatted](../chats/chat1/chat1-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat1/chat1-index.md)                  | [chat1.md](../chats/chat1/chat1.md) | Initial build analysis across all five characters; Monoco stat respec; Lune weapon comparison; Sciel and Verso builds; full progression plan |
| Chat 2 | [Formatted](../chats/chat2/chat2-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat2/chat2-index.md)                  | [chat2.md](../chats/chat2/chat2.md) | Endgame skill research; character stat update via voice; chromatic progress; compaction mechanics; session procedure design                  |
| Chat 3 | [Formatted](../chats/chat3/chat3-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat3/chat3-index.md)                  | [chat3.md](../chats/chat3/chat3.md) | Endgame team transition (Cheater Pictos, Steeled Strike, Second Chance resolution); team role framing; burn-stacking vs stance cycling paths; Chevalam mechanics; Maelle LP planning; transcript logging problems identified |
| Chat 4 | [Formatted](../chats/chat4/chat4-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat4/chat4-index.md) | [chat4.md](../chats/chat4/chat4.md) | Progress update (Sacred River, Chevaliere, Dark Shore, Sakapatate/Joyaro, all chars 70+); story ordering research (Flying Manor optional, final boss in Lumière); Verso weapon selection (Chevalam reinstated with Cheater synergy confirmed); Steeled Strike burst sequence analysis; Maelle Reacher preparation (stats, skills, Pictos, solo build); session logging procedure improvements (verbatim instruction strengthened, sections-per-part changed to 2, session state step added); Verso full update (stats, Lumina, skills, weapons inventory) |
| Chat 5 | [Formatted](../chats/chat5/chat5-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat5/chat5-index.md) | [chat5.md](../chats/chat5/chat5.md) | Progress update (Reacher, Serpenphare, chromatics); Maelle respec to Luck/Agility/Might + Lithum equipped (level 33, Power 9254); Gommage unlocked; full Pictos/Lumina review all five characters; core Lumina sets defined (154LP main, 110LP reserve); Energy Master obtained; Pictos/Lumina reference file started (JSON scaffold); Tints mechanics clarified; Protecting Heal + Longer Shell synergy established for reserve team. |

---

## Section 11: Historical Error Log

Full error log in `overview/historical-errors.md`: [Formatted](historical-errors.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/historical-errors.md).

Fetch that file only when reviewing specific past errors. Active failure mode categories extracted from the log are maintained in Section 1 of this overview.

---

## Section 12: Character File Template

See `overview/character-file-template.md`: [Formatted](character-file-template.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/overview/character-file-template.md)

Fetch only when creating a new character file.

---

## Section 13: Session Procedure

*Full design rationale in `scripts/pipeline.md`: [Formatted](../scripts/pipeline.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/scripts/pipeline.md)*

### Session Start

1. Fetch overview file (jsDelivr raw; use commit hash if provided)
2. Determine chat number N: count Claude chats in Section 10 + 1
3. Review Section 9 open questions. Check each against Section 2 playthrough status; flag any resolved items for removal in the changelist.
4. Ask what the session is about — do not fetch character files until topic confirmed
5. Create in `/mnt/user-data/outputs/`:
   - `chatN.md` — empty transcript file
   - `chatN-index.md` — index file with header (see Index File format below)
   - `session-state.json` — `{"chat": "chatN", "commit_hash": "<hash>", "last_write_timestamp": null, "modified_sections": [], "actions": [], "pictos_lumina_changes": []}`

   Extract the commit hash from the jsDelivr URL used to fetch the overview file (e.g. `@6ab23396`) and store it in `commit_hash`. When a mid-session file fetch is needed, output the full jsDelivr URL with this hash for Matt to paste — avoid using `@main` as it can be stale.
6. Check `/mnt/transcripts/` — flag if any files present (unexpected at session start)
7. Confirm to user: chat number, files created, ready

### !log Command

Matt types `!log` at any natural pause to trigger the compound log step. Claude does not self-trigger log writes. `!check` does not trigger a log write — it often fires mid-topic and would create misleading section boundaries.

### Compound Log Step

Triggered by `!log` and always at end of session.

1. Write `<!-- SECTION: Title -->` and `## Title` heading to `chatN.md` — title must be unique within transcript; qualify if needed (e.g. "Verso Build — Pre-Sprong" / "Verso Build — Post-Sprong")
2. Check `/mnt/transcripts/` — if compaction found since last check, notify Matt immediately (memory of earlier conversation may be incomplete; Matt may want to re-paste context or ask Claude to fetch files); note internally
3. If compaction noted: run converter script (`transcript_to_md.py --after-timestamp <last_write_timestamp>`), append reconstructed turns to `chatN.md`, insert compaction markers in transcript and index, update `last_write_timestamp` to `start_timestamp` of last reconstructed turn, sourced from JSON output
4. Append turns since last write to `chatN.md` — **verbatim**. Copy every turn exactly as it appears in context — Matt's turns and Claude's turns alike, including all pasted content. Do not paraphrase, compress, or represent. This applies even when there are many turns, when content is long, or when the transcript would read more cleanly if summarised. The pull to summarise in these cases is strong — resist it explicitly. If in doubt, copy more rather than less.
5. Append to `chatN-index.md` under `## Table of Contents`: if this is the first section in a new part (every 2 sections), first write part header `### [Part N](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md)`; then append section entry `- **[Section Title](chatN.md#anchor)** — paragraph description`
6. Update `session-state.json`:
   - For each file section with confirmed changes since the last log write: if not already present in `modified_sections`, add an entry with an empty `changes` array; then append one concise bullet per change to that entry's `changes` array.
   - For each concrete in-game action arising since the last log write (equip, swap, respec, attempt), append a one-line entry to `actions`.
   - For each Pictos/Lumina change confirmed since the last log write (obtained, equipped, swapped, Lumina added/removed, LP expanded), append a one-line entry to `pictos_lumina_changes`.
   - Set `last_write_timestamp` only if compaction recovery was run in step 3 — otherwise leave as null.

### End of Session

1. Output the in-game actions checklist from `actions` for Matt to implement before the next session — **do this BEFORE step 2 so it appears verbatim in the transcript**
2. Run compound log step — transcript and index now complete
3. Run splitter (`split_transcript.py --sections-per-part 2`) on `chatN.md`
4. Edit `chatN-index.md` directly to add Part Files list under `## Part Files (Claude-readable)`
5. If `pictos_lumina_changes` is non-empty: apply all accumulated changes to `overview/pictos-lumina.json`, then regenerate Markdown: `python3 scripts/generate_pictos_lumina.py overview/pictos-lumina.json overview/`. Include the updated JSON and both Markdown files in the changelist commit. Also update the per-character Lumina totals in the overview (Section 5) if LP used/total changed.
6. Produce `chatN-changelist.md`:
   - For each entry in `modified_sections`, use the `changes` array as the basis for writing the full replacement content for that section.
   - Also include the new Chat N row for Section 10 of the overview: read the existing Section 10 entries and write a new row in the same style — concise prose covering topics discussed, decisions made, and any pipeline/infrastructure changes. Do not generate this mechanically from the `actions` list; write it as a genuine summary.
   - **Write the changelist once at end of session only** — do not write changelist entries incrementally during the session. The `modified_sections` list in session state is the tracking mechanism throughout.
7. Matt runs the updater script and pushes to GitHub

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

Part boundaries are determined by `--sections-per-part` (default: 2). Part 1 covers sections 1–2, Part 2 covers sections 3–4, and so on — adjust if `--sections-per-part` is changed. Part file link: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chatN/chatN-partN.md`

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

- `###` heading must be unique within its `##` parent; renames require direct edit
- Separators (`---`) between `##` sections are inserted automatically by the updater script — do not include them in CONTENT
- Failure mode: loud

### Session State JSON
```json
{"chat": "chatN", "commit_hash": "abc12345", "last_write_timestamp": null, "modified_sections": [{"file": "path/to/file.md", "parent": "## Section", "section": "### Subsection", "changes": ["Change note 1", "Change note 2"]}], "actions": ["In-game action 1"], "pictos_lumina_changes": ["Mark Full Strength obtained, level 25"]}
```

`commit_hash`: extracted from the jsDelivr URL at session start (e.g. `@6ab23396` → `"6ab23396"`). Used to construct all mid-session file fetch URLs — Claude outputs the full URL with this hash for Matt to paste. Never use `@main` for mid-session fetches.

`last_write_timestamp`: only set during compaction recovery (step 3 of the compound log step), sourced from the `start_timestamp` in the JSON transcript output. In a no-compaction session it remains null throughout — this is correct, not an error.

`modified_sections`: each entry tracks one file section that needs updating. The `changes` array accumulates concise notes of what changed in that section throughout the session. At end of session, Claude uses these notes to write the full replacement content for each section.

`actions`: in-game actions to implement before the next session. Output as a checklist at end of session.

`pictos_lumina_changes`: changes to apply to `overview/pictos-lumina.json` at end of session. Each entry is a concise note (e.g. "Mark Full Strength obtained, level 25", "Swap Maelle Pictos: Energy Master → Survivor"). At end of session, Claude applies these to the JSON and regenerates both Markdown files via `python3 scripts/generate_pictos_lumina.py`.
