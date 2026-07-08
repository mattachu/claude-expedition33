# Clair Obscur: Expedition 33 — AI Overview File

*Fetched at the start of any session involving this game. Follow all instructions below.*

---

## Section 1: Topic-Specific Failure Modes

These are in addition to the general failure modes in the startup file:

- **Confabulation about game content:** Training data thin and patchy. Do not give confident answers about mechanics, routes, item availability, or missable content without searching first. Example: The Glissando incident (Chat 0) — asserted a bypass existed and escalated increasingly specific hints through multiple failed attempts; no bypass exists. For any navigation, bypass, or optional enemy question, treat prior knowledge as zero and search before answering. Two failed attempts from the player is a hard stop requiring premise re-evaluation, not hint escalation.
- **Missable/sequence-locked content:** Highest-risk category. Never assert content will be available later without verifying. Default: "I'm not certain — check the wiki." The Vale bosses incident is the clearest example of this failure mode.
- **Wrong advice on record:** Previous sessions contain specific errors. Check character files before advising on that character.
- **Recommending meta builds without checking playstyle fit:** Community recommendations often assume specific builds (e.g. Elemental Genesis). Always verify assumptions before recommending.
- **Not simulating combat turns before recommending changes:** Abstract reasoning from tier rankings is insufficient. Always trace actual turn sequences before advising on weapon or build changes.
- **Confabulating Lumina and skill effects:** Multiple effects described incorrectly across sessions. Never assert Lumina or skill effects without verifying from a source.
- **LP arithmetic errors:** Always verify LP point totals before finalising a loadout. Example: Full Strength stated as 10LP in Chat 13 — correct is 15LP.
- **General arithmetic errors:** LLM is not designed for arithmetic. For any sum over more than a handful of values, use bash rather than mental arithmetic.
- **Accepting corrections without verification:** After repeated corrections, Claude began agreeing without independent checks. Default: acknowledge correction neutrally, flag whether independently verified.
- **Weapon scaling and drop-level assumptions:** Always verify weapon scaling attributes, drop source, and recommended level before advising. Do not assert weapon stats from memory.
- **Passive vs active effect interactions:** Verify interaction type before assuming synergy. Example: Ramasson's passive heal does not trigger Energising Heal.
- **Rank bonuses work ONLY at exact rank:** Confirmed by multiple community sources and in-game highlighting. Do not apply rank bonuses at higher ranks.
- **AoE vs single-target context:** Check fight context before recommending AoE skills. Example: Phantom Stars recommended for Verso's solo Golgra fight — AoE is useless in 1v1.

Full error log in [`reference/historical-errors.md`](../reference/historical-errors.md).
Fetch that file only when reviewing specific past errors.

---

## Section 2: Playthrough Status

<!-- GENERATED:START playthrough:summary -->
- **Platform:** Xbox Series X
- **Current playthrough:** First playthrough
- **Progress:**
  - Act 3, Phase 4.
  - Characters: Maelle L99, Verso L99, Sciel L99, Lune L99, Monoco L99.
  - Current area: Endless Tower.
<!-- GENERATED:END -->
  - For detailed progression plan, see [`overview/progress.md`](progress.md)

### Party
<!-- GENERATED:START playthrough:party -->
- **Active:** Maelle, Verso, Sciel
- **Reserve:** Lune, Monoco
<!-- GENERATED:END -->

<!-- GENERATED:START characters:summary:party -->
| Character                         | Level | Role                         | Weapon        | Pictos                                                 | LP      |
|-----------------------------------|-------|------------------------------|---------------|--------------------------------------------------------|---------|
| [Maelle](../characters/maelle.md) | 99    | Primary DPS                  | Lithum (33)   | Energising Turn, Empowering Break, Shortcut            | 521/521 |
| [Verso](../characters/verso.md)   | 99    | Endgame main DPS             | Simoso (33)   | Alternating Critical, Quick Break, Energising Stun     | 469/469 |
| [Sciel](../characters/sciel.md)   | 99    | Pure support                 | Litheson (33) | Energy Master, Breaking Death, Powerful Revive         | 326/326 |
| [Lune](../characters/lune.md)     | 99    | DPS / healer (reserve)       | Kralim (33)   | Clea's Life, Sweet Kill, Rush On Powerful              | 461/461 |
| [Monoco](../characters/monoco.md) | 99    | Break + AP support (reserve) | Joyaro (33)   | Augmented First Strike, Charging Critical, Pro Retreat | 348/348 |
<!-- GENERATED:END -->

**More details:**
- **Party composition and roles:** See [`overview/party-summary.md`](party-summary.md) — fetch when comparing builds across the team or reviewing stat totals and Lumina loadouts.
- **Pictos/Lumina mechanics and loadouts:** See [`overview/pictos-lumina-summary.md`](pictos-lumina-summary.md) — fetch when reviewing Lumina sets, evaluating Pictos candidates, or planning LP expansion.
- **Character builds and decisions:** See character files for each character — fetch when diving into a specific character's strategy, weapon choices, or past decisions.

### Inventory
<!-- GENERATED:START playthrough:inventory -->
- Colour of Lumina: 132
- Recoats: 59
- Chroma Catalysts: 67 standard, 77 polished, 113 resplendent, 271 grandiose, 6 perfect
- Chroma: 1801759
<!-- GENERATED:END -->

---

## Section 3: Playstyle Notes
*Last updated: Chat 30*

- **Parry rate:** Improving with experience — ~20% against unfamiliar bosses initially; up to ~100% against well-known enemies after extended grinding. Pattern-recognition is the bottleneck. Dodge is used actively to learn timings: the dodge window is wider than the parry window, and Perfect Dodge shares the same timing as Parry. Dodger Lumina gives +1 AP on Perfect Dodge. This is a persistent constraint on risky builds (Overload without Cheater, etc.).
- **Risk tolerance:** Conservative while parry skills are developing. Prefers empirical testing. Rejects builds that rely on low-HP states (Overload without Cheater, Berserk Slash) or skills with survival costs (Defiant Strike's HP cost).
- **AP management:** Prefers to use skills every turn if AP allows. Values AP flow highly. **Endgame team (Maelle/Sciel/Verso) AP note:** AP flow is sustainable with Sciel's Litheson (+3 AP/turn for Sciel on buff/debuff) and Intervention, but requires active management. Do not assume freely available AP when advising on endgame team builds.
- **Turn rotation (endgame burst):** Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).
- **Maelle Last Chance rotation:** Last Chance (1 AP) reduces HP to 1, refills all AP, switches to Virtuose. Cheater fires an immediate extra turn. Clea's Life restores HP to 100% on that turn start. Net result: full AP reset + Virtuose + full HP in one move. Used as a deliberate rotation tool, not an emergency skill. Confirmed three-turn sequence (Chat 30): Normal turn → Cheater → Shortcut (triggered when Last Chance drops HP below 30%). With Clea's Life active, Shortcut's intended low-health tide-turner purpose is bypassed — it functions as a free third turn rather than an emergency response. Also triggers on Verso's Overload. One-per-battle limit.
- **Trash fights:** Maelle: Phantom Stars (Verso AoE at S Rank) to clear turn 1.
- **Boss fights:** Methodical; learns patterns over multiple attempts. Values break dynamics highly.
- **Status effects:** Primarily burn and mark; limited experience with others.
- **Free-aim:** Previously used heavily by Lune with Trebuchim (2–3 shots typically, up to 5–6 when stacking burn + mark). With Kralim, Free Aim is used less frequently — Lune primarily applies Burn via the Hell skill rather than Free Aim + Burning Shots. Other characters use free-aim occasionally, mostly for removing shields.

---

## Section 4: Game Mechanics

*More detailed descriptions of mechanics are included in [`reference/mechanics.md`](../reference/mechanics.md).*

### Weapons

- Weapons are character-locked: each weapon can only be used by a particular character.
- Each weapon has attribute scaling categories that contribute to weapon damage. Recoats can realign attribute allocation to match a new weapon's scaling requirements.

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

**Lumina Point (LP) pools:** Each character's LP pool equals their level by default. Pools can be permanently increased by spending **Colour of Lumina** items (1 Colour = 1 LP per character). The increase is permanent and irreversible.

**Full reference:**

| File                                                                              | Purpose                                                                                         | When to read                                            |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [`overview/pictos-lumina-summary.md`](pictos-lumina-summary.md)                   | Full Pictos/Lumina mechanics, Core Lumina sets, per-character loadouts, situational, candidates | Any session involving Pictos/Lumina advice              |
| [`reference/pictos-lumina-catalogue.md`](../reference/pictos-lumina-catalogue.md) | All 194 Pictos grouped by category with effects and LP costs                                    | When browsing or searching the full catalogue           |
| [`data/pictos-lumina.json`](../data/pictos-lumina.json)                           | Raw JSON — query directly for specific Pictos data                                              | When Claude needs to look up or modify specific entries |

### Tints

Tints are consumable items, distinct from skills. Healing Tints restore HP, Revive Tints revive a fallen ally, and Energy Tints provide AP.

### Reserve Party

If the main party is fully wiped in a battle, the player can continue the battle using the reserve party. This is most relevant for hard bosses.

---

## Section 5: Key Decisions & Context

- **Sciel over Monoco in main team:** Litheson's +3 AP/turn (Sciel only, when buff/debuff applied) keeps Sciel self-sufficient. Combined with Intervention (grants extra turn +4 AP to another character), she effectively generates turns and AP for allies. Ramasson rejected after confirming its passive heal does not trigger Energising Heal.
- **Litheson is Sciel's endgame weapon:** Confirmed by multiple sources.
- **Verso's Rank bonuses work ONLY at exact Rank:** Confirmed by multiple community sources and in-game highlighting.
- **Vale bosses missed:** Axon defeated before triggering the mask riddles. All three Vale bosses permanently inaccessible.
- **Endgame team:** Maelle + Sciel + Verso. Turn rotation: Verso (base attack) → Verso(C) (Steeled Strike charge) → Sciel (Fortune's Fury on Verso) → Sciel(C) (Intervention on Verso) → Verso(Intervention) (Steeled Strike executes at Rank S with doubled damage).
- **End Bringer vs Steeled Strike for Verso:** Steeled Strike deals more damage in general; End Bringer wins when target is stunned. Verso keeps both and uses situationally.
- **Might is correct post-crit-cap:** For Maelle and Verso (A99, L99 already), additional attribute points go into Might. All weapons factor Might into power; gains scale with weapon base power (level 33 weapons = maximum return). More Luck gives nothing once crit-capped.
- **Scaverim evaluated for Lune, Kralim retained:** Scaverim (Dark element, Vit B/Agi C) offers high burst ceiling via Dark Stain accumulation — passive +50% skill damage per active stain at L4, 300% burst with 4 stains at L20 — but requires multi-turn ramp-up with no output during accumulation. Incompatible with reserve role where Lune enters mid-fight and needs immediate contribution. Kralim + Elemental Genesis fires effectively from turn 1. Revisit if Lune ever moves to main team for sustained fights.
- **Simon fight (Plan F) — complete (Chat 24):** 30-minute controlled fight. Sciel's Twilight + Litheson applied Greater Rush to allies / Greater Slow to Simon for turn-order dominance. Overload + End Bringer maintained near-continuous stun through all phases. Seeram L4 kept Verso at Rank A throughout (enabling stun extension). Simon never vanished the party. One slip when Sciel briefly left Twilight.
- **Simoso acquired (Chat 24):** Verso's endgame weapon. Power 9480, Light element, Vitality A / Agility S scaling. L4: ethereal Sword on any skill damage. L10: 20% chance Burn on Light damage. L20: Can't die at Rank A or above. Verso respecced to Vitality 99 / Agility 99 / Might 62 / Luck 22 — Luck 22 is the minimum to maintain 100% crit; do not reduce further.
- **Lune damage vs main team (Chat 24):** Genesis hitting ~1m vs Maelle/Verso at 4m+ in Simon fight. Gap partly reflects absence of Fortune's Fury/Intervention multiplier. Frenzy (drops from Licornapieds, Verso's Drafts) identified as the most direct damage multiplier for Genesis (8 hits). Burn Affinity 25% was underused in Simon because Hell was AP-constrained; Thermal Transfer loop should fix this.
- **Monoco post-Simon loadout (Chat 24):** Abbest Wind confirmed redundant with Cheater (extra turn doesn't stack). Final reserve loadout: Stalact Punches (Break, Almighty opener), Chapelier Slash (Mark, Agile), Grosse Tête Whack (Defenceless, Heavy), Orphelin Cheers (Powerful support), Potier Energy (AP), Moissonneuse Vendange (wheel cycling, Can Break). Lancelier Impale retained as situational for Slow. Creation Void and Duallist Storm noted as future main-team DPS candidates.
- **Charnon purchased but deferred:** Earth element, Defence B/Luck A. 100% Crit in Twilight (L4), Foretell on Crit (L10). Not suitable for Sciel's current support role. Revisit only for a dedicated DPS Sciel build.

---

## Section 6: Open Questions

*(none currently)*

---

## Section 7: Session Procedure

*Full procedure in [`reference/session-procedure.md`](../reference/session-procedure.md) — fetched at `!wrap`.*

### Session Start

1. Read `LINKS.md` — extract all file URLs for use during session
2. Determine new chat number N: add 1 to "latest chat number" in `LINKS.md`
3. Fetch `overview/claude-expedition33.md`
4. Review Section 6 open questions; flag any resolved items
5. Fetch `data/playthrough.json`
6. Create `/mnt/user-data/outputs/chatN.md` (transcript file, to be filled later) with title `# Clair Obscur: Expedition 33 — Chat N`
7. Ask what the session is about — do not fetch character or reference files unless topic requires them

### Turn Counter

Display `*[Turn N. Last log: Turn L.]*` at the top of every Claude response.

### ACTION Flags

When a decision, in-game action, data change, or open question arises, write `**ACTION:** <brief note>` as a standalone line in the response. The end-of-session pass collects and categorises these.

### Commands

Matt types these commands to trigger specific actions:

`!log` — log conversation to transcript, following the logging process below

`!check` — critical review of Claude's most recent response. Does not trigger a log write.

`!close` — end-of-session for the current chat; follow the Close Steps below

`!wrap` — full end-of-session pass; run in a separate chat with the transcript uploaded; fetch `reference/session-procedure.md` and follow the steps there

### Logging process

Triggered by `!log`. Follow these two steps exactly, adhering to all constraints detailed in the paragraphs below:

1. Append `<!-- SECTION -->` into `chatN.md` followed by a blank line
2. Append all turns since last log into `chatN.md` — **verbatim**

**Turn format:** Matt's turn first, labelled `**Matt:**`, then a blank line, then Claude's turn, labelled `**Claude:**`, then a blank line, then a horizontal rule `---`.

**Verbatim logging:** Copy every turn exactly as it appears in context — Matt's turns and Claude's turns alike, including all pasted content. Do not paraphrase, compress, summarise, or represent any turn, regardless of length or content. The pull to summarise long or repetitive content is strong — resist it explicitly. If in doubt, copy more rather than less.

**Bracket notation:** for tool calls only: `*[Fetched X]*`, `*[Created file Y]*`. Never use brackets to summarise substantive response text.

**Lists:** If Matt's turn begins with a list, insert a blank line between `**Matt:**` and the first list item so Markdown renders correctly.

**Appending to file:** Use bash `>>` redirection to append turns to the transcript file. No need to view the file before appending — just construct the content and redirect.

### Close Steps

1. Complete transcript: run a final `!log` step
2. Verbatim check: sample 3–4 turns spread across the transcript file (beginning, middle, end) — read each from disk, compare against context, report pass/fail per sample
3. Output transcript: present `chatN.md` and stop
