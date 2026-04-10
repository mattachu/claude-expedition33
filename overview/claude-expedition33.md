# Clair Obscur: Expedition 33 — AI Overview File

*Fetched at the start of any session involving this game. Follow all instructions below.*

---

## Section 1: Topic-Specific Failure Modes

These are in addition to the general failure modes in the startup file:

- **Confabulation about game content:** Training data thin and patchy. Do not give confident answers about mechanics, routes, item availability, or missable content without searching first. Example: The Glissando incident (Chat 0) — asserted a bypass existed and escalated increasingly specific hints through multiple failed attempts; no bypass exists. For any navigation, bypass, or optional enemy question, treat prior knowledge as zero and search before answering. Two failed attempts from the player is a hard stop requiring premise re-evaluation, not hint escalation.
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

Full error log in [`reference/historical-errors.md`](../reference/historical-errors.md).
Fetch that file only when reviewing specific past errors.

---

## Section 2: Playthrough Status

<!-- GENERATED:START playthrough:summary -->
- **Platform:** Xbox Series X
- **Current playthrough:** First playthrough
- **Progress:**
  - Act 3, Phase 3.
  - Characters: Maelle L83, Verso L82, Sciel L82, Lune L78, Monoco L78.
  - The Reacher complete. Gommage unlocked. Serpenphare defeated. Chromatic Braseleur defeated (easy).
  - Flying Manor next — agreed to attempt at current level before Endless Tower.
<!-- GENERATED:END -->
- **Permanently missed:** Vale bosses (Jovial Moissonneuse, Sorrowful Chapelier, Seething Boucheclier); Karatom quest (requires Gustave alive).

### Party
<!-- GENERATED:START playthrough:party -->
- **Active:** Maelle, Verso, Sciel
- **Reserve:** Lune, Monoco
<!-- GENERATED:END -->

### Inventory
<!-- GENERATED:START playthrough:inventory -->
- Colour of Lumina: ~200 (reduced by EM pool expansions this session)
- Recoats: 26 (Lune used one this session for Hell + Lightning Dance)
- Chroma Catalysts: check in-game
<!-- GENERATED:END -->

### LP totals
<!-- GENERATED:START characters:summary:LP -->
- Maelle: 194/196
- Verso: 194/194
- Sciel: 175/176
- Lune: 120/123
- Monoco: 91/128
<!-- GENERATED:END -->

---

## Section 3: Playstyle Notes
*Last updated: Chat 4*

- **Free-aim:** Used heavily with Lune (2–3 shots typically, up to 5–6 when stacking burn + mark). Each shot: shield removal, damage, burn (Burning Shots Lumina), mark (Marking Shots Lumina), stain generation (Trebuchim). Maelle uses free-aim less frequently. Free-aim usage expected to drop with Lune/Maelle not in the levelling team.
- **Parry rate:** ~20% against unfamiliar bosses; up to ~100% against well-known enemies after extended grinding. Pattern-recognition is the bottleneck — can require 20+ attempts. Skill is developing, not absent. Dodge is used actively to learn timings: the dodge window is wider than the parry window, and Perfect Dodge shares the same timing as Parry — so Dodge rate is meaningfully higher than parry rate. Dodger Lumina gives +1 AP on Perfect Dodge. This is a persistent constraint on risky builds (Overload without Cheater, Defiant Strike's 30% HP cost, etc.).
- **AP management:** Prefers to use skills every turn if AP allows. Values AP flow highly. **Endgame team (Maelle/Sciel/Verso) AP note:** AP flow is sustainable with Sciel's Litheson (+3 AP/turn for Sciel on buff/debuff) and Intervention, but requires active management — it is not as straightforward or as quick to refill as Monoco's Potier Energy. Do not assume freely available AP when advising on endgame team builds.
- **Turn order (levelling team):** Sciel first (Fortune's Fury before Verso acts), Verso second (Strike Storm with doubled damage), Monoco third (Potier Energy refills AP). Turn order: Sciel ~1812 → Verso ~1436 → Monoco ~1163.
- **Trash fights:** Maelle: Fencer's Flurry to clear turn 1. With new team: Phantom Stars (Verso AoE at S Rank).
- **Boss fights:** Methodical; learns patterns over multiple attempts. Values break dynamics highly.
- **Status effects:** Primarily burn and mark; limited experience with others.
- **Risk tolerance:** Conservative while parry skills are developing. Prefers empirical testing (99-point attribute method established with Monoco and Sciel). Rejects builds that rely on low-HP states (Overload without Cheater, Berserk Slash) or skills with survival costs (Defiant Strike's HP cost).

---

## Section 4: Game Mechanics

*More detailed descriptions of mechanics are included in [`reference/mechanics.md`](../reference/mechanics.md).*

### Parry, Dodge, Jump and Counterattack

Most enemy attacks can be avoided by triggering a parry, dodge or jump. These must be triggered within a quick-time window. Parrying has the shortest windows. Successfully completing all parries in an enemy's attack sequence triggers a Counterattack, which deals high damage.

### AP

Skills cost AP to use. Every character gains 1 AP at the start of their turn as a baseline, before any skills, Lumina, or Pictos effects.

### Free-Aim

Free-aim is a distinct targeting mode costing 1 AP, used before selecting a skill, item, or basic attack.

### Gradient Skills

Gradient Skills are powerful abilities with effects ranging from damage to healing to revival. Each character has three Gradient Skills, costing 1, 2, and 3 Gradient Charges (GC) respectively. Gradient charges build by spending AP on skills.

### Break Mechanics

There are two distinct types of Break skills:
- **Break bar filling skills** deal damage and also advance the break bar to fill it up over multiple hits.
- **Break trigger skills** land the final hit that actually triggers the Break after the bar is full.

### Pictos and Lumina

Pictos are collectible items (3 slots per character) giving stat boosts and effects. Learning a Pictos (4 battles) unlocks it as a Lumina — effect only, no stat boosts, costs LP. Any Lumina costs 0LP for a character who has that Pictos equipped. With attributes maxed at 99, Pictos stat boosts are the primary source of character growth.

Key rules: each Pictos is a unique copy (only one character can equip it); duplicates upgrade the existing copy; extra-turn effects don't stack (bonus turns can't trigger further bonus turns); passive "on turn start" effects fire on Cheater/Intervention bonus turns too; Pictos stat boosts cover Health, Defence, Speed, and Crit only — not Attack. For status immunity, add the relevant Lumina rather than swapping Pictos.

**Lumina Point (LP) pools:** Each character's LP pool equals their level by default. Pools can be permanently increased by spending **Colour of Lumina** items (1 Colour = 1 LP per character). The increase is permanent and irreversible. Current stock: ~200 Colour of Lumina. Pools have already been expanded for main team members (Maelle 196, Verso 194, Sciel 176).

**Full reference:**

| File                                   | Purpose                                                                                         | When to read                                            |
|----------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `overview/pictos-lumina-summary.md`    | Full Pictos/Lumina mechanics, Core Lumina sets, per-character loadouts, situational, candidates | Any session involving Pictos/Lumina advice              |
| `reference/pictos-lumina-catalogue.md` | All 194 Pictos grouped by category with effects and LP costs                                    | When browsing or searching the full catalogue           |
| `data/pictos-lumina.json`              | Raw JSON — query directly for specific Pictos data                                              | When Claude needs to look up or modify specific entries |

### Tints

Tints are consumable items, distinct from skills. Healing Tints restore HP, Revive Tints revive a fallen ally, and Energy Tints provide AP.

### Reserve Party

If the main party is fully wiped in a battle, the player can continue the battle using the reserve party. This is most relevant for hard bosses.

---

## Section 5: Party
*Last updated: Chat 6*

<!-- GENERATED:START playthrough:party -->
- **Active:** Maelle, Verso, Sciel
- **Reserve:** Lune, Monoco
<!-- GENERATED:END -->

**Speed order (intended):** Verso goes first via Chevalam Rush (Rank S at battle start). Sciel second, Maelle third. Current turn order: Verso 2132 > Maelle 2027 > Sciel 2014. Needs tweaking.
Note: base speed scales with level independently of Agility — keep levels close when speeds are close and turn order matters.

**Turn rotation (endgame burst):** Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).

<!-- GENERATED:START characters:summary:party -->
*[Placeholder for table including level, role, weapon, skills, Pictos, LP, etc.]*
<!-- GENERATED:END -->

### Core Lumina Suite

**Main team core:**
<!-- GENERATED:START pictos:core:main -->
**194LP** Painted Power, Teamwork, Base Shield, Energising Turn, Energising Parry, Energising Start I, Dodger, Breaker, Marking Shots, Dead Energy I, Dead Energy II, Critical Break, Rewarding Mark, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death, Cheater, **Energy Master**. Note: Cheater/Breaking Death free for Verso (Pictos); Base Shield non-functional for Verso; Energy Master free for Sciel (Pictos).
<!-- GENERATED:END -->

**Reserve team core:**
<!-- GENERATED:START pictos:core:reserve -->
**110LP** Main team core minus Cheater, Dead Energy I, Dead Energy II, Energy Master.
<!-- GENERATED:END -->

Full breakdown with effects in [pictos-lumina-summary.md](pictos-lumina-summary.md) §3–4. Character-specific additions on top of core sets in §5.

---

## Section 6: Character Reference Files
*Fetch the relevant file at the start of any session focusing on that character in detail. These supersede the brief summaries in Section 5.*

| Character | Role                           | File                                              |
|-----------|--------------------------------|---------------------------------------------------|
| Maelle    | Primary DPS                    | [`characters/maelle.md`](../characters/maelle.md) |
| Verso     | Mid-game DPS / endgame DPS     | [`characters/verso.md`](../characters/verso.md)   |
| Sciel     | Pure support                   | [`characters/sciel.md`](../characters/sciel.md)   |
| Lune      | Support/healer/stain DPS       | [`characters/lune.md`](../characters/lune.md)     |
| Monoco    | AP battery / support / breaker | [`characters/monoco.md`](../characters/monoco.md) |

---

## Section 7: Key Decisions & Context

- **Trebuchim over Colim for Lune:** Colim tested and rejected. 14% attack loss, no free-aim stain generation. Trebuchim optimal for Mayhem/free-aim playstyle. Colim only appropriate for Elemental Genesis builds.
- **Monoco stat respec (Agility 72→99, Vitality 61, Luck 20, Nusaro):** Empirically tested. Key finding: Luck 2× more efficient than Defence for crit. Agility increases Speed, Attack, and Defence stat simultaneously.
- **Sciel over Monoco in main team:** Litheson's +3 AP/turn (Sciel only, when buff/debuff applied) keeps Sciel self-sufficient. Combined with Intervention (grants extra turn +4 AP to another character), she effectively generates turns and AP for allies. Ramasson rejected after confirming its passive heal does not trigger Energising Heal.
- **Sciel stat allocation:** Agility 99, Luck 99, Defence 48. Critical Burn Pictos fixes turn order.
- **Gaulteram over Glaceso for Verso:** Gaulteram prevents rank loss on hit (loses 1 Perfection only). Same scaling as Chevalam (Agility + Luck) = no respec needed when swapping.
- **Nusaro upgrade to 20:** Resplendent Catalysts cap at level 19; Joyaro drops at level 28. No overlap. Nusaro Level 20 (+1 AP per mask change) is worth the upgrade.
- **Litheson is Sciel's endgame weapon:** Confirmed by multiple sources.
- **Marking Shot over Defiant Strike for Verso:** Both apply Mark 100%. Defiant Strike costs 30% current HP per use — too risky with developing parry skills.
- **Rank bonuses work ONLY at exact rank:** Confirmed by multiple community sources and in-game highlighting.
- **Vale bosses missed:** Axon defeated before triggering the mask riddles. All three Vale bosses permanently inaccessible.
- **Endgame team:** Maelle + Sciel + Verso. Turn rotation: Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).
- **Maelle must complete The Reacher before Renoir:** Required for Lithum and Gustave resurrection path. Choose "Truth" to reach Relationship Level 7. ✅ Complete.
- **Renoir self-nerf strategy:** Drop to Gaulteram (Verso) and Medalum (Maelle) before entering Lumière. Use earlier fights inside Lumière to calibrate — add back weapons if too hard before the final save point. Avoid removing Cheater or changing rotation; weapon downgrade is cleaner and preserves playstyle.

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

<!-- GENERATED:START playthrough:phase_3_checklist -->
- ✅ The Reacher (Maelle solo) → Lithum weapon, Maelle Level 7, Gustave resurrection path
- ✅ Chromatic Braseleur (inside The Reacher) — complete (easy)
- ✅ Serpenphare (SE Boat Graveyard)
- ⬜ Flying Manor (if too difficult at current level, use Endless Tower floors 1–20 first) → Clea's Life Pictos, Perfect Chroma Catalyst
- ⬜ **Renoir (final boss)** — enter Lumière → fight at end of dungeon. *[Choose Maelle → "A Life to Paint" → Gustave returns]*. Self-nerf: enter with Gaulteram/Medalum, calibrate on earlier fights, add back before final save point.
<!-- GENERATED:END -->

### Phase 4 — Post-game (Level 80+)

<!-- GENERATED:START playthrough:phase_4_checklist -->
- ⬜ Endless Tower floors 1–20 + Chromatic Eveque (good first post-game activity; also serves as level-up fallback if Flying Manor too hard)
- ⬜ Dark Gestral Arena
- ⬜ Hard chromatics: Gault, Reaper Cultist, Petank, Goblu, Aberration, Lampmaster
- ⬜ Chromatic Bourgeon (Monolith)
- ⬜ Chromatic Clair Obscur (Monolith Peak) → Combo Attack II Pictos
- ⬜ Chromatic Echassier (Level 80–85+)
- ⬜ Chromatic Pétank superboss
- ⬜ Renoir's Drafts (Level 80+, recommended 90+ for Simon) — hardest optional area; Aberrations, Bouchecliers, Contorsionnistes
- ⬜ Purchase Charnon (89,884 Chromas, Renoir's Drafts merchant) — Sciel alternative endgame weapon
- ⬜ Chromatic Creation (Renoir's Drafts)
- ⬜ Verso's Drafts (DLC, Level 80+) — recommended after Renoir's Drafts; final boss (Root of All Evil) is hardest boss in game, reported to beat level 99 parties
- ⬜ Chromatic Barbasucette (Verso's Drafts)
- ⬜ Chromatic Franctale (Verso's Drafts)
- ⬜ Endless Tower floors 21–33 + DLC bosses (Clea Unleashed, Simon the Divergent Star — accessed via Tower canvases after beating originals; added by Thank You Update, no ordering dependency with Verso's Drafts)
<!-- GENERATED:END -->

---

## Section 9: Open Questions

- **Pictos optimisation (main team):** Framework prepared (Chat 7, `pictos-optimisation-framework.md`). Deferred until after Flying Manor — new Pictos expected. Key decisions: Verso slot 3 (Second Chance vs Confident), Maelle slot 3 (Survivor vs Recovery vs Clea's Life), turn order fix (Sciel must be faster than Maelle). Energy Master stays on Sciel.
- **Pictos data rationalisation:** Remove character `pictos` arrays from JSON; derive from `equipped_by` field. Update `generate_pictos_lumina.py`. See framework document Section 11 for full spec.
- **Healing Boon trigger mechanic:** "Heal 15% HP on applying a buff" — may fire on the buff *recipient* rather than the caster. Evidence: Dark Cleansing triggers it for each ally buffed (from Sciel's file). Also potentially triggers when Litheson phase changes apply Greater Rush to allies. Needs in-game confirmation before building around it.
- **Crit cap:** Believed to be 100%, not 99%. Verify in-game.
- **Maelle Lumina additions:** Longer Shell (10LP) and Powerful on Shell (10LP) synergise with Lithum L20 Shell generation. 2LP spare currently — needs pool expansion.
- **Energising Burn (10LP):** Consider when next expanding core Lumina suite — all characters have Burning Shots.
- **Full Strength Pictos:** Not yet obtained. Effect: 25% increased damage at full Health. Strong candidate for Maelle given Recovery + Shell from Lithum. Find as you progress.
- **Clea's Life Pictos:** From Flying Manor (Phase 3). Recovers 100% Health on turn start if no damage taken since last turn. Strong survivability for Maelle.
- **Verso skills file:** May still be stale — verify current skill loadout in next session.
- **Empowering Dodge (5LP):** Reset behaviour on parry unconfirmed — test empirically before committing LP.

---

## Section 10: Chat Logs
*For reference only — do not fetch unless specifically asked. These are large files.*

| Chat   | Index                                                                                                                                        | Full Transcript                     | Summary                                                                                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Chat 0 | [Formatted](../chats/chat0/chat0-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat0/chat0-index.md) | [chat0.md](../chats/chat0/chat0.md) | Prior (abandoned) conversation with ChatGPT                                                                                                                                                                                              |
| Chat 1 | [Formatted](../chats/chat1/chat1-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat1/chat1-index.md) | [chat1.md](../chats/chat1/chat1.md) | Initial build analysis across all five characters; Monoco stat respec; Lune weapon comparison; Sciel and Verso builds; full progression plan                                                                                             |
| Chat 2 | [Formatted](../chats/chat2/chat2-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat2/chat2-index.md) | [chat2.md](../chats/chat2/chat2.md) | Endgame skill research; character stat update via voice; chromatic progress; compaction mechanics; session procedure design                                                                                                              |
| Chat 3 | [Formatted](../chats/chat3/chat3-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat3/chat3-index.md) | [chat3.md](../chats/chat3/chat3.md) | Endgame team transition (Cheater Pictos acquired); team role framing; burn-stacking vs stance cycling paths; Chevalam mechanics; Maelle LP planning; transcript logging problems                                                         |
| Chat 4 | [Formatted](../chats/chat4/chat4-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat4/chat4-index.md) | [chat4.md](../chats/chat4/chat4.md) | Progress update; story ordering research; Verso weapon selection; Steeled Strike burst sequence analysis; Maelle Reacher preparation; session logging procedure improvements                                                             |
| Chat 5 | [Formatted](../chats/chat5/chat5-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat5/chat5-index.md) | [chat5.md](../chats/chat5/chat5.md) | Maelle respec for Lithum; Gommage unlocked; full Pictos/Lumina review all five characters; core Lumina sets defined; Energy Master obtained; Pictos/Lumina reference created                                                             |
| Chat 6 | [Formatted](../chats/chat6/chat6-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat6/chat6-index.md) | [chat6.md](../chats/chat6/chat6.md) | Flying Manor ordering decided; Renoir self-nerf strategy; progression plan restructured; all character stats updated; Pictos optimisation deferred to Opus session                                                                       |
| Chat 7 | [Formatted](../chats/chat7/chat7-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat7/chat7-index.md) | [chat7.md](../chats/chat7/chat7.md) | Pictos optimisation framework designed and prepared for Sonnet handoff; actual optimisation and assignment deferred until after Flying Manor; Colour of Lumina pool expansion mechanism documented; Pictos data rationalisation designed |
| Chat 8 | [Formatted](../chats/chat8/chat8-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat8/chat8-index.md) | [chat8.md](../chats/chat8/chat8.md) | Monoco full skill audit; Repo restructure design: new folder structure, JSON reference files, GitHub Actions workflow; All five data files built; Session procedure updated; hand-off for script design                                  |

---

## Section 11: Session Procedure

*Full design rationale in [`scripts/pipeline.md`](../scripts/pipeline.md)*

### Session Start

1. Matt pastes link to the latest `LINKS.md` (auto-generated by GitHub Actions on every push to main — fetch from repo root)
2. Fetch `LINKS.md` — extract all file URLs for use during session
3. Extract commit hash from `LINKS.md` — all subsequent file fetches use this hash — avoid using `@main` as it can be stale.
4. Fetch overview file URL from `LINKS.md`
5. Determine chat number N: count Claude chats in Section 10 + 1
6. Review Section 9 open questions; flag any resolved items
7. Fetch `data/playthrough.json` — current phase, inventory, checklist
8. Ask what the session is about — do not fetch character files until topic confirmed
9. Create in `/mnt/user-data/outputs/`:
   - `chatN.md` — empty transcript file
   - `chatN-index.md` — index file with header (see Index File format below)
   - `session-state.json` — `{"chat": "chatN", "commit_hash": "<hash>", "last_write_timestamp": null, "modified_sections": [], "actions": [], "pictos_lumina_changes": []}`
10. Check `/mnt/transcripts/` — flag if any files present
11. Confirm to user: chat number, files created, ready

### Turn counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response. Track from context — no tool calls needed.

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
3. Run splitter (`split_transcript.py --sections-per-part 4`) on `chatN.md`
4. Edit `chatN-index.md` directly to add Part Files list under `## Part Files (Claude-readable)`
5. If `pictos_lumina_changes` is non-empty: apply changes to `data/pictos-lumina.json`. Markdown will be regenerated via `python3 scripts/generate.py`.
6. Produce `chatN-changelist.md`:
   - For each entry in `modified_sections`, use the `changes` array as the basis for writing the full replacement content for that section.
   - Also include the new Chat N row for Section 10 of the overview: read the existing Section 10 entries and write a new row in the same style — concise prose covering topics discussed, decisions made, and any pipeline/infrastructure changes. Do not generate this mechanically from the `actions` list; write it as a genuine summary.
   - **Write the changelist once at end of session only** — do not write changelist entries incrementally during the session. The `modified_sections` list in session state is the tracking mechanism throughout.
7. If any significant new errors were made during this session, note them for manual addition to `overview/historical-errors.md`.
8. Matt runs the updater script, makes any manual changes, and pushes to GitHub

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
- Separators (`---`) between `##` sections are inserted automatically by the updater script — do not include them in CONTENT or use them between FILE blocks
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
