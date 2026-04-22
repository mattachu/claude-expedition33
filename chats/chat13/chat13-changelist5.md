FILE: overview/claude-expedition33.md
SECTION: ## Section 1: Topic-Specific Failure Modes
CONTENT:
## Section 1: Topic-Specific Failure Modes

These are in addition to the general failure modes in the startup file:

- **Confabulation about game content:** Training data thin and patchy. Do not give confident answers about mechanics, routes, item availability, or missable content without searching first. Example: The Glissando incident (Chat 0) — asserted a bypass existed and escalated increasingly specific hints through multiple failed attempts; no bypass exists. For any navigation, bypass, or optional enemy question, treat prior knowledge as zero and search before answering. Two failed attempts from the player is a hard stop requiring premise re-evaluation, not hint escalation.
- **Missable/sequence-locked content:** Highest-risk category. Never assert content will be available later without verifying. Default: "I'm not certain — check the wiki." The Vale bosses incident is the clearest example of this failure mode.
- **Wrong advice on record:** Previous sessions contain specific errors. Check character files before advising on that character.
- **Recommending meta builds without checking playstyle fit:** Community recommendations often assume specific builds (e.g. Elemental Genesis). Always verify assumptions before recommending.
- **Not simulating combat turns before recommending changes:** Abstract reasoning from tier rankings is insufficient. Always trace actual turn sequences before advising on weapon or build changes.
- **Confabulating Lumina and skill effects:** Multiple effects described incorrectly across sessions. Never assert Lumina or skill effects without verifying from a source.
- **LP arithmetic errors:** Always verify LP point totals before finalising a loadout. Example: Full Strength stated as 10LP in Chat 13 — correct is 15LP.
- **Accepting corrections without verification:** After repeated corrections, Claude began agreeing without independent checks. Default: acknowledge correction neutrally, flag whether independently verified.
- **Weapon scaling and drop-level assumptions:** Always verify weapon scaling attributes, drop source, and recommended level before advising. Do not assert weapon stats from memory.
- **Passive vs active effect interactions:** Verify interaction type before assuming synergy. Example: Ramasson's passive heal does not trigger Energising Heal.
- **Rank bonuses work ONLY at exact rank:** Confirmed by multiple community sources and in-game highlighting. Do not apply rank bonuses at higher ranks.
- **AoE vs single-target context:** Check fight context before recommending AoE skills. Example: Phantom Stars recommended for Verso's solo Golgra fight — AoE is useless in 1v1.

Full error log in [`reference/historical-errors.md`](../reference/historical-errors.md).
Fetch that file only when reviewing specific past errors.

FILE: overview/claude-expedition33.md
SECTION: ## Section 3: Playstyle Notes
CONTENT:
## Section 3: Playstyle Notes
*Last updated: Chat 13*

- **Free-aim:** Used heavily with Lune (2–3 shots typically, up to 5–6 when stacking burn + mark). Each shot: shield removal, damage, burn (Burning Shots Lumina), mark (Marking Shots Lumina), stain generation (Trebuchim). Maelle uses free-aim less frequently.
- **Parry rate:** Improving with experience — ~20% against unfamiliar bosses initially; up to ~100% against well-known enemies after extended grinding. Pattern-recognition is the bottleneck. Dodge is used actively to learn timings: the dodge window is wider than the parry window, and Perfect Dodge shares the same timing as Parry. Dodger Lumina gives +1 AP on Perfect Dodge. This is a persistent constraint on risky builds (Overload without Cheater, etc.).
- **AP management:** Prefers to use skills every turn if AP allows. Values AP flow highly. **Endgame team (Maelle/Sciel/Verso) AP note:** AP flow is sustainable with Sciel's Litheson (+3 AP/turn for Sciel on buff/debuff) and Intervention, but requires active management. Do not assume freely available AP when advising on endgame team builds.
- **Turn rotation (endgame burst):** Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).
- **Maelle Last Chance rotation:** Last Chance (1 AP) reduces HP to 1, refills all AP, switches to Virtuose. Cheater fires an immediate extra turn. Clea's Life restores HP to 100% on that turn start. Net result: full AP reset + Virtuose + full HP in one move. Used as a deliberate rotation tool, not an emergency skill.
- **Trash fights:** Maelle: Phantom Stars (Verso AoE at S Rank) to clear turn 1.
- **Boss fights:** Methodical; learns patterns over multiple attempts. Values break dynamics highly.
- **Status effects:** Primarily burn and mark; limited experience with others.
- **Risk tolerance:** Conservative while parry skills are developing. Prefers empirical testing. Rejects builds that rely on low-HP states (Overload without Cheater, Berserk Slash) or skills with survival costs (Defiant Strike's HP cost).

FILE: overview/claude-expedition33.md
SECTION: ## Section 4: Game Mechanics > ### Pictos and Lumina
CONTENT:
### Pictos and Lumina

Pictos are collectible items (3 slots per character) giving stat boosts and effects. Learning a Pictos (4 battles) unlocks it as a Lumina — effect only, no stat boosts, costs LP. Any Lumina costs 0LP for a character who has that Pictos equipped. With attributes maxed at 99, Pictos stat boosts are the primary source of character growth.

Key rules: each Pictos is a unique copy (only one character can equip it); duplicates upgrade the existing copy; extra-turn effects don't stack (bonus turns can't trigger further bonus turns); passive "on turn start" effects fire on Cheater/Intervention bonus turns too; Pictos stat boosts cover Health, Defence, Speed, and Crit only — not Attack. For status immunity, add the relevant Lumina rather than swapping Pictos.

**Lumina Point (LP) pools:** Each character's LP pool equals their level by default. Pools can be permanently increased by spending **Colour of Lumina** items (1 Colour = 1 LP per character). The increase is permanent and irreversible.

**Full reference:**

| File                                                                              | Purpose                                                                                         | When to read                                            |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [`overview/pictos-lumina-summary.md`](pictos-lumina-summary.md)                   | Full Pictos/Lumina mechanics, Core Lumina sets, per-character loadouts, situational, candidates | Any session involving Pictos/Lumina advice              |
| [`reference/pictos-lumina-catalogue.md`](../reference/pictos-lumina-catalogue.md) | All 194 Pictos grouped by category with effects and LP costs                                    | When browsing or searching the full catalogue           |
| [`data/pictos-lumina.json`](../data/pictos-lumina.json)                           | Raw JSON — query directly for specific Pictos data                                              | When Claude needs to look up or modify specific entries |

FILE: overview/claude-expedition33.md
SECTION: ## Section 5: Party
CONTENT:
## Section 5: Party
*Last updated: Chat 13*

<!-- GENERATED:START playthrough:party -->
- **Active:** Maelle, Verso, Sciel
- **Reserve:** Lune, Monoco
<!-- GENERATED:END -->

**Speed order:** Verso goes first via Chevalam Rush (Rank S at battle start). Sciel second, Maelle third. Current turn order resolved via Chat 12 Pictos optimisation.
Note: base speed scales with level independently of Agility — keep levels close when speeds are close and turn order matters.

**Turn rotation (endgame burst):** Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).

<!-- GENERATED:START characters:summary:party -->
| Character | Level | Role                         | Weapon        | Pictos                                         | LP      |
|-----------|-------|------------------------------|---------------|------------------------------------------------|---------|
| Maelle    | 91    | Primary DPS                  | Lithum (33)   | Clea's Life, Empowering Break, Gradient Break  | 234/234 |
| Verso     | 91    | Endgame main DPS             | Chevalam (33) | Augmented Counter I, Breaking Death, Confident | 224/224 |
| Sciel     | 90    | Pure support                 | Litheson (33) | Painter, Energy Master, Energising Shots       | 215/215 |
| Lune      | 86    | DPS / healer (reserve)       | Kralim (33)   | Critical Burn, Burn Affinity, Burning Death    | 130/130 |
| Monoco    | 87    | Break + AP support (reserve) | Joyaro (33)   | Longer Shell, Powerful Mark, Powerful Revive   | 125/133 |
<!-- GENERATED:END -->

### Core Lumina Suite

**Main team core:**
<!-- GENERATED:START pictos:core:main -->
**239LP** Painted Power, Teamwork, Base Shield, Energising Turn, Cheater, Energy Master, Second Chance, Energising Parry, Energising Start I, Dodger, Breaker, Marking Shots, Dead Energy I, Dead Energy II, Critical Break, Rewarding Mark, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death, Shortcut. Note: Painted Power (Essential for all characters from Act 3 onwards); Base Shield (Verso: non-functional with Chevalam as L4 effect prevents shields); Energising Turn (Main AP flow generator; boosted by Energy Master).
<!-- GENERATED:END -->

**Reserve team core:**
<!-- GENERATED:START pictos:core:reserve -->
**120LP** Painted Power, Teamwork, Base Shield, Energising Turn, Recovery, Energising Parry, Energising Start I, Dodger, Breaker, Marking Shots, Critical Break, Rewarding Mark, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death.
<!-- GENERATED:END -->

Full breakdown with effects in [pictos-lumina-summary.md](pictos-lumina-summary.md) §3–4. Character-specific additions on top of core sets in §5.

FILE: overview/claude-expedition33.md
SECTION: ## Section 7: Key Decisions & Context
CONTENT:
## Section 7: Key Decisions & Context

- **Trebuchim over Colim for Lune:** Colim tested and rejected. 14% attack loss, no free-aim stain generation. Trebuchim optimal for Mayhem/free-aim playstyle. Colim only appropriate for Elemental Genesis builds.
- **Monoco stat respec (Agility 72→99, Vitality 61, Luck 20, Nusaro):** Empirically tested. Key finding: Luck 2× more efficient than Defence for crit. Agility increases Speed, Attack, and Defence stat simultaneously.
- **Sciel over Monoco in main team:** Litheson's +3 AP/turn (Sciel only, when buff/debuff applied) keeps Sciel self-sufficient. Combined with Intervention (grants extra turn +4 AP to another character), she effectively generates turns and AP for allies. Ramasson rejected after confirming its passive heal does not trigger Energising Heal.
- **Sciel stat allocation:** Agility 99, Luck 99, Defence 63. Critical Burn Pictos fixes turn order.
- **Nusaro upgrade to 20:** Resplendent Catalysts cap at level 19; Joyaro drops at level 28. No overlap. Nusaro Level 20 (+1 AP per mask change) is worth the upgrade.
- **Litheson is Sciel's endgame weapon:** Confirmed by multiple sources.
- **Marking Shot over Defiant Strike for Verso:** Both apply Mark 100%. Defiant Strike costs 30% current HP per use — too risky with developing parry skills.
- **Rank bonuses work ONLY at exact rank:** Confirmed by multiple community sources and in-game highlighting.
- **Vale bosses missed:** Axon defeated before triggering the mask riddles. All three Vale bosses permanently inaccessible.
- **Endgame team:** Maelle + Sciel + Verso. Turn rotation: Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).
- **End Bringer vs Steeled Strike for Verso:** Steeled Strike deals more damage in general; End Bringer wins when target is stunned due to stun-extension bonus at Rank A. Verso keeps both and uses situationally.
- **Might is correct post-crit-cap:** For Maelle and Verso (A99, L99 already), additional attribute points go into Might. All weapons factor Might into power; gains scale with weapon base power (level 33 weapons = maximum return). More Luck gives nothing once crit-capped.

FILE: overview/claude-expedition33.md
SECTION: ## Section 9: Open Questions
CONTENT:
## Section 9: Open Questions

- **Verso survivability without Survivor:** Survivor (20LP) dropped. Second Chance alone has been sufficient through Renoir and early post-game. Continue monitoring against harder post-game content.
- **Recovery on Sciel:** Dropped for now to save LP. Revisit if Sciel takes more damage than expected in postgame. 10LP, would need CoL expansion.
- **Powerful On Shell as Lumina:** Consider for Maelle (synergy with Lithum L20 Shell generation). LP cost 10. Add when levels create headroom.
- **Energising Shell (10LP):** Alternative to Powerful On Shell for Maelle — +2 AP on Shell application. Evaluate alongside Powerful On Shell.
- **Anti-Blight (10LP):** Used situationally (swap in without CoL expansion, fits within existing headroom). Add permanently to main team when LP headroom grows.
- **Second Chance upgrade:** Available at L31 from defeating Création near Grour in Renoir's Drafts. Substantially better stats than current L16.
- **Healing Boon trigger mechanic:** "Heal 15% HP on applying a buff" — may fire on the buff *recipient* rather than the caster. Needs in-game confirmation before building around it.
- **Crit cap:** Believed to be 100%, not 99%. Verify in-game.
- **Empowering Dodge (5LP):** Reset behaviour on parry unconfirmed — test empirically before committing LP.
- **Scaverim for Lune:** Likely already in inventory — check, as Scaverim drops from Chromatic Scavenger which was beaten during Phase 2. If obtained, evaluate as Lune best-in-slot (Dark stain generation).
- **First Life (15LP):** Drops from Chromatic Lampmaster in Endless Tower (Stage 11 / DLC superboss area). 25% damage while alive, no downside for a well-supported DPS. Strong candidate for Maelle once obtained.
- **Frenzy:** Drops from Licornapieds in Verso's Drafts. Unconditional skill damage boost for multi-hit skills. Relevant for Maelle (multi-hit stances) and Verso (Strike Storm). Review when Verso's Drafts is accessible.

FILE: overview/claude-expedition33.md
SECTION: ## Section 11: Session Procedure > ### End of Session
CONTENT:
### End of Session

1. Output the in-game actions checklist from `actions` for Matt to implement before the next session — **do this BEFORE step 2 so it appears verbatim in the transcript**
2. Run compound log step — transcript and index now complete
3. Run splitter (`split_transcript.py --sections-per-part 3`) on `chatN.md` — default is 3; override via `sections_per_part` in session-state.json if a different value was agreed at session start
4. Edit `chatN-index.md` directly to add Part Files list under `## Part Files (Claude-readable)`
5. If `pictos_lumina_changes` is non-empty: apply changes to `data/pictos-lumina.json` directly or via `DATA:` blocks in the changelist. Markdown will be regenerated via `scripts/generate.py`.
6. Produce `chatN-changelist.md`:
   - For each entry in `modified_sections`, use the `changes` array as the basis for writing the full replacement content for that section.
   - Also include the new Chat N row for Section 10 of the overview: read the existing Section 10 entries and write a new row in the same style — concise prose covering topics discussed, decisions made, and any pipeline/infrastructure changes. Do not generate this mechanically from the `actions` list; write it as a genuine summary.
   - **Write the changelist once at end of session only** — do not write changelist entries incrementally during the session. The `modified_sections` list in session state is the tracking mechanism throughout.
7. If any significant new errors were made during this session, note them for manual addition to `overview/historical-errors.md`.
8. Matt runs the updater script, makes any manual changes, and pushes to GitHub

FILE: overview/claude-expedition33.md
SECTION: ## Section 11: Session Procedure > ### Session State JSON
CONTENT:
### Session State JSON
```json
{"chat": "chatN", "commit_hash": "abc12345", "sections_per_part": 3, "last_write_timestamp": null, "modified_sections": [{"file": "path/to/file.md", "parent": "## Section", "section": "### Subsection", "changes": ["Change note 1", "Change note 2"]}], "actions": ["In-game action 1"], "pictos_lumina_changes": ["Mark Full Strength obtained, level 25"]}
```

`commit_hash`: extracted from the jsDelivr URL at session start (e.g. `@6ab23396` → `"6ab23396"`). Used to construct all mid-session file fetch URLs — Claude outputs the full URL with this hash for Matt to paste. Never use `@main` for mid-session fetches.

`sections_per_part`: controls the splitter at end of session. Default is 3. Override by setting a different value in session-state.json at session start if agreed with Matt.

`last_write_timestamp`: only set during compaction recovery (step 3 of the compound log step), sourced from the `start_timestamp` in the JSON transcript output. In a no-compaction session it remains null throughout — this is correct, not an error.

`modified_sections`: each entry tracks one file section that needs updating. The `changes` array accumulates concise notes of what changed in that section throughout the session. At end of session, Claude uses these notes to write the full replacement content for each section.

`actions`: in-game actions to implement before the next session. Output as a checklist at end of session.

`pictos_lumina_changes`: changes to apply to `data/pictos-lumina.json` at end of session. Each entry is a concise note (e.g. "Mark Full Strength obtained, level 25", "Swap Maelle Pictos: Energy Master → Survivor"). At end of session, Claude applies these to the JSON and regenerates both Markdown files via `python3 scripts/generate.py`.

FILE: characters/maelle.md
SECTION: ## Mechanics > ### Key Synergies
AFTER: ### Stances
CONTENT:
### Key Synergies

**Last Chance + Cheater + Clea's Life loop:**

Last Chance (1 AP) reduces HP to 1, refills all AP, and switches to Virtuose. Cheater fires an immediate extra turn. Clea's Life triggers at the start of that extra turn (condition: no damage taken since last turn — met because Cheater bonus turn is immediate), restoring 100% HP.

Net effect: full AP reset + Virtuose stance + full HP in a single 1 AP move. Full Strength Lumina (25% damage at full Health) is also active on the Cheater turn after HP is restored.

Use Last Chance as a deliberate rotation tool rather than an emergency skill. Practical usage: when AP is low and you want to re-enter Virtuose with full resources.

**Caveats:**
- Stendhal applies Defenceless to Maelle on use. If Stendhal is used in the same turn sequence before Last Chance, Maelle has both HP-1 and Defenceless simultaneously — a vulnerability window if the enemy gets a turn between moves. Rare with good turn economy but plan accordingly.
- If an enemy has any interrupt-style mechanic that allows them to act during a Cheater bonus turn, Clea's Life will not fire (condition fails if damage taken). No known enemies in the current content do this.
