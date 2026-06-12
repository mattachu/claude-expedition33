# Verso — Clair Obscur: Expedition 33

*Last updated: 2026-04-10*

---

## Role

- **Primary role:** Mid-game DPS (levelling team); endgame main DPS
- **Party position:** Active in Act 3 levelling team (Verso / Monoco / Sciel); planned endgame team (Maelle / Sciel / Verso)
- **Synergies:**
    + Receives Fortune's Fury from Sciel (doubled damage)
    + Intervention from Sciel grants extra turn (good for Steeled Strike) + 4 AP for burst
    + Monoco's Stalact Punches fills Break bar for Verso's Perfect Break (triggers Break + jumps to S Rank)
    + Marking Shot + Rewarding Mark Lumina generate AP return for party
    + Breaking Death Lumina fills Break bar on death, which allows Verso to jump back to Rank S when revived using Perfect Break

---

## Mechanics

Verso's central system is **Perfection and Rank**. Perfection is a resource that fills a rank meter; higher ranks give higher damage multipliers and unlock skill bonuses. Rank order: **D → C → B → A → S**. Skills and parries generate Perfection. D is the true base rank — previous note of C as starting rank was because Lighteram's Level 4 set a floor of C. With Simoso there is no rank floor; hits can take Verso back to D.

**Critical mechanic:** Rank bonuses apply ONLY at the **exact rank stated** — not at higher ranks. Yellow skill text in-game indicates an active rank bonus.

| Event                     | Perfection effect                |
|---------------------------|----------------------------------|
| Parry                     | Gains Perfection                 |
| Dodge                     | Prevents rank loss               |
| Hit taken (general)       | Full rank demotion               |
| Hit taken (Gaulteram)     | Lose 1 Perfection only           |
| Death                     | Drop back to Rank D              |
| Battle start (general)    | Start on Rank D                  |
| Battle start (Lanceram)   | Start on Rank C                  |
| Battle start (Chevalam)   | Start on Rank S                  |
| Light Holder              | +1 Rank on completion            |
| Perfect Break (at B Rank) | Jump to S Rank if triggers Break |

**Dodge vs Parry timing:** Dodge has a wider window than Parry. Dodge > Perfect Dodge == Parry in terms of timing windows. If a Dodge is Perfect, a Parry would also work. Dodge is used to safely learn parry timings — the game indicates whether a Dodge was Perfect.

**Counterattack:** Successfully completing all parries in an enemy's attack sequence launches a highly powerful Counterattack. This does not consume a turn. This is the primary reason to prioritise Parry over Dodge.

**Stun:** Enemies are stunned on Break. End Bringer deals increased damage to stunned targets, and at A Rank can reapply stun to extend the window.

**Steeled Strike:** Charges for 1 turn; executes following turn for extreme damage. Interrupted if Verso takes any damage during charge. Requires Cheater (consecutive turns) to use safely. S Rank bonus requires building to Rank S (no longer auto-starts at S with Simoso).

**Burst sequence (endgame):** Verso (normal turn): base attack to farm AP → Verso (Cheater turn): Steeled Strike charge → Sciel (normal turn): Fortune's Fury on Verso → Sciel (Cheater turn): Intervention on Verso → Verso (Intervention turn): Steeled Strike executes with Fortune's Fury active. Combined multiplier: Rank S (×3.0) × Fortune's Fury (×2.0) × Simoso (~9 of 13 hits doubled) = very high total output before Steeled Strike's own multiplier. With Frenzy Pictos: additional compound ×1.1 per Steeled Strike hit (ceiling ×3.14 at hit 13).

**Solo fights:** Both completed (vs Francois, vs Monoco).

---

## Stats

### Level and Attributes

<!-- GENERATED:START characters:Verso:attributes -->
| Attribute | Value |
|-----------|-------|
| Level     | 99    |
| Vitality  | 99    |
| Might     | 99    |
| Agility   | 99    |
| Defence   | 0     |
| Luck      | 0     |
<!-- GENERATED:END -->

### Combat Stats

<!-- GENERATED:START characters:Verso:stats -->
*Stats with Simoso (33), Second Chance (L31), Sweet Kill (L31), Alternating Critical (L29) equipped.*

| Stat    | Base        | Modified |
|---------|-------------|----------|
| Health  | *[unknown]* | 7790     |
| Attack  | *[unknown]* | 11583    |
| Speed   | *[unknown]* | 2100     |
| Defence | *[unknown]* | 182      |
| Crit    | *[unknown]* | 106%     |
<!-- GENERATED:END -->

---

## Weapons

### Current (Endgame)
<!-- GENERATED:START weapons:Verso:Simoso -->
- **Name:** Simoso (33)
- **Power:** 9480
- **Element:** Light
- **Scaling:** Vitality A, Agility S
- **Effects:**
    - Level 4: An ethereal Sword deals Light damage on any damage dealt with Skills.
    - Level 10: 20% chance to apply Burn on dealing Light damage.
    - Level 20: Can't die if at least Rank A.
<!-- GENERATED:END -->
- **Notes:**
    - The L4 extra hit copies the main hit exactly — same damage value and crit multiplier, including from Frenzy stacking.
    - With Steeled Strike (13 hits), approximately 9 hits are doubled by Simoso.
    - Frenzy (Pictos) stacks compound ×1.1 per Steeled Strike hit only; Simoso copies do not advance the Frenzy stack — ceiling ×3.14 at hit 13.
    - Alternating Critical has no synergy at 100% crit (all hits including Simoso copies benefit from guaranteed crits).
    - Base Shield now functional (was blocked by Chevalam L4).

### Future (post-game)
- **Dreameso** — Agility + Luck scaling; Rank gain on Counterattack; deferred until parry/counterattack rate improves.
- **Seeram** — Vitality + Agility. Can't reach Rank S. S-tier ONLY for End Bringer stunlock build. Purchased from Unfinished Cruler, Coastal Cave.

### Previous
- **Lanceram** — Rank can't be lower than C
- **Gaulteram** — Lose Perfection rather than Rank when hit
- **Chevalam** (previous endgame weapon, replaced by Simoso at Chat 24)
    - Physical, Agility S / Luck A.
    - L4: Start battle at Rank S, can't be healed or gain Shields.
    - L10: +20% damage per consecutive no-damage turn, up to 5× (Cheater turns stack this automatically).
    - L20: Apply Rush at Rank S.

---

## Pictos

<!-- GENERATED:START characters:Verso:Pictos -->
| Slot | Pictos               | Level | Stat Bonus            | Effect                                                               |
|------|----------------------|-------|-----------------------|----------------------------------------------------------------------|
| 1    | Alternating Critical | 29    | Speed +293, Crit +50% | On Critical hit, 100% increased damage of the next non-Critical hit. |
| 2    | Quick Break          | 31    | Speed +672, Crit +36% | Play again on Breaking a target.                                     |
| 3    | Energising Stun      | 28    | Speed +519, Crit +31% | +1 AP on hitting a Stunned target with a Skill.                      |
<!-- GENERATED:END -->

**Breaking Death synergy:** On death → break bar fills instantly → Second Chance revives at Rank D → Perfect Break triggers break → Rank S in one move → Steeled Strike burst immediately active.

---

## Lumina

### LP Budget
<!-- GENERATED:START characters:Verso:LP -->
- **Current capacity:** 448 LP
- **Used:** 448 LP
- **Spare:** 0 LP
<!-- GENERATED:END -->

### Lumina Adjustments

<!-- GENERATED:START characters:Verso:Lumina:adjustments -->
| Lumina                 | Change | LP | Notes                                                                                                                                                                                                                    |
|------------------------|--------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Augmented First Strike | Added  | 5  | DPS expansion. 50% increased damage on first hit, once per battle.                                                                                                                                                       |
| Burn Affinity          | Added  | 10 | DPS expansion. 25% increased damage against burning targets. Synergy: Simoso 20% burn chance on Light damage can seed this.                                                                                              |
| Charging Critical      | Added  | 10 | DPS expansion. +20% Gradient Charge on Critical Hit, once per turn. Fires every turn at 122% crit.                                                                                                                       |
| Dead Energy I          | Added  | 2  | DPS expansion. +3 AP on killing an enemy.                                                                                                                                                                                |
| Dead Energy II         | Added  | 2  | DPS expansion. +3 AP on killing an enemy (stacks with Dead Energy I).                                                                                                                                                    |
| Double Third           | Added  | 10 | DPS expansion. Every 3rd hit deals double damage. Fires on hits 3/6/9/12 of 13-hit Steeled Strike.                                                                                                                       |
| Empowering Dodge       | Added  | 5  | DPS expansion. 5% increased damage per consecutive dodge, stacks to 10. Parry does not reset the stack.                                                                                                                  |
| Frenzy                 | Added  | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Major multiplier on 13-hit Steeled Strike.                                                                                                               |
| Glass Cannon           | Added  | 10 | DPS expansion. 25% increased damage, 25% increased damage taken.                                                                                                                                                         |
| Immaculate             | Added  | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                                                                            |
| Warming Up             | Added  | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks.                                                                                                                                                 |
| At Death's Door        | Added  | 5  | Low-health expansion. 50% increased damage below 10% HP. Active permanently while at 1 HP from Overload.                                                                                                                 |
| Confident Fighter      | Added  | 15 | Low-health expansion. 30% increased damage, cannot be healed.                                                                                                                                                            |
| In Medias Res          | Added  | 10 | Low-health expansion. +3 Shields at battle start, max Health halved. HP penalty irrelevant at 1 HP from Overload.                                                                                                        |
| Inverted Affinity      | Added  | 5  | Low-health expansion. 50% increased damage while Inverted (cannot be healed).                                                                                                                                            |
| Auto Rush              | Added  | 10 | Personal addition. Apply Rush for 3 turns on battle start - secures first-action priority before Litheson Greater Rush takes effect.                                                                                     |
| Energising Break       | Added  | 3  | Personal addition. +3 AP on Breaking a target - enables Perfect Break -> Stun -> End Bringer rotation. Frequency depends on boss: varies from rarely breaking (e.g. Simon) to easily broken (e.g. Chromatic Lampmaster). |
| Alternating Critical   | Added  | —  | Free from Pictos. Effect not used at 100% crit - pure stat stick.                                                                                                                                                        |
| Quick Break            | Added  | —  | Free from Pictos. Effect (play again on Breaking a target) does not fire alongside Cheater - pure stat stick.                                                                                                            |
| Energising Stun        | Added  | —  | Free from Pictos. +1 AP on hitting Stunned target with Skill - synergy with End Bringer.                                                                                                                                 |
<!-- GENERATED:END -->

### Current Loadout

<!-- GENERATED:START characters:Verso:Lumina -->
| Lumina                 | LP | Notes                                                                                                                                                                                                                    |
|------------------------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AP Discount            | 30 | Reduces skill AP cost by 1.                                                                                                                                                                                              |
| Aegis Revival          | 5  | +1 Shield on being revived.                                                                                                                                                                                              |
| Alternating Critical   | —  | FREE from Alternating Critical Pictos                                                                                                                                                                                    |
| At Death's Door        | 5  | Low-health expansion. 50% increased damage below 10% HP. Active permanently while at 1 HP from Overload.                                                                                                                 |
| Augmented First Strike | 5  | DPS expansion. 50% increased damage on first hit, once per battle.                                                                                                                                                       |
| Auto Rush              | 10 | Personal addition. Apply Rush for 3 turns on battle start - secures first-action priority before Litheson Greater Rush takes effect.                                                                                     |
| Base Shield            | 20 | Grants 1 Shield HP buffer per turn.                                                                                                                                                                                      |
| Breaker                | 10 | 25% increased Break damage.                                                                                                                                                                                              |
| Breaking Burn          | 5  | 25% increased Break damage on Burning enemies.                                                                                                                                                                           |
| Breaking Death         | 5  | Fully charge enemy break bar on death.                                                                                                                                                                                   |
| Burn Affinity          | 10 | DPS expansion. 25% increased damage against burning targets. Synergy: Simoso 20% burn chance on Light damage can seed this.                                                                                              |
| Charging Critical      | 10 | DPS expansion. +20% Gradient Charge on Critical Hit, once per turn. Fires every turn at 122% crit.                                                                                                                       |
| Cheater                | 40 | Extra turn after using a skill, once per turn.                                                                                                                                                                           |
| Confident Fighter      | 15 | Low-health expansion. 30% increased damage, cannot be healed.                                                                                                                                                            |
| Critical Break         | 5  | 25% increased Break damage on Critical hits.                                                                                                                                                                             |
| Dead Energy I          | 2  | DPS expansion. +3 AP on killing an enemy.                                                                                                                                                                                |
| Dead Energy II         | 2  | DPS expansion. +3 AP on killing an enemy (stacks with Dead Energy I).                                                                                                                                                    |
| Dodger                 | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                                                                                                                                                                               |
| Double Third           | 10 | DPS expansion. Every 3rd hit deals double damage. Fires on hits 3/6/9/12 of 13-hit Steeled Strike.                                                                                                                       |
| Empowering Dodge       | 5  | DPS expansion. 5% increased damage per consecutive dodge, stacks to 10. Parry does not reset the stack.                                                                                                                  |
| Energising Break       | 3  | Personal addition. +3 AP on Breaking a target - enables Perfect Break -> Stun -> End Bringer rotation. Frequency depends on boss: varies from rarely breaking (e.g. Simon) to easily broken (e.g. Chromatic Lampmaster). |
| Energising Start I     | 5  | +1 AP on battle start. Boosted by Energy Master.                                                                                                                                                                         |
| Energising Stun        | —  | FREE from Energising Stun Pictos                                                                                                                                                                                         |
| Energising Turn        | 20 | +1 AP on turn start. Main AP flow generator; boosted by Energy Master.                                                                                                                                                   |
| Energy Master          | 40 | Every AP gain is increased by 1.                                                                                                                                                                                         |
| First Strike           | 10 | Act first in battle.                                                                                                                                                                                                     |
| Frenzy                 | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Major multiplier on 13-hit Steeled Strike.                                                                                                               |
| Glass Cannon           | 10 | DPS expansion. 25% increased damage, 25% increased damage taken.                                                                                                                                                         |
| Immaculate             | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                                                                            |
| In Medias Res          | 10 | Low-health expansion. +3 Shields at battle start, max Health halved. HP penalty irrelevant at 1 HP from Overload.                                                                                                        |
| Inverted Affinity      | 5  | Low-health expansion. 50% increased damage while Inverted (cannot be healed).                                                                                                                                            |
| Painted Power          | 5  | Damage can exceed 9,999. Essential for all characters from Act 3 onwards.                                                                                                                                                |
| Protecting Death       | 5  | Allies gain Shell on death.                                                                                                                                                                                              |
| Quick Break            | —  | FREE from Quick Break Pictos                                                                                                                                                                                             |
| SOS Power              | 5  | Apply Powerful when falling below 50% Health.                                                                                                                                                                            |
| SOS Rush               | 5  | Apply Rush when falling below 50% Health.                                                                                                                                                                                |
| SOS Shell              | 5  | Apply Shell when falling below 50% Health.                                                                                                                                                                               |
| Second Chance          | 40 | Revive with 100% Health. Once per battle.                                                                                                                                                                                |
| Shielding Death        | 10 | Allies gain 3 Shield points on death.                                                                                                                                                                                    |
| Shortcut               | 5  | Immediately play when falling below 30% Health. Once per battle.                                                                                                                                                         |
| Survivor               | 20 | Survive fatal damage with 1 Health, once per battle.                                                                                                                                                                     |
| Teamwork               | 5  | 10% increased damage while all allies are alive.                                                                                                                                                                         |
| Warming Up             | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks.                                                                                                                                                 |
<!-- GENERATED:END -->

---

## Skills

<!-- GENERATED:START characters:Verso:skills -->
**Currently equipped (6):** End Bringer, Light Holder, Perfect Break, Phantom Stars, Steeled Strike, Overload

| Skill             | AP              | Rank Bonus                           | Equipped | Notes                                                                                    |
|-------------------|-----------------|--------------------------------------|----------|------------------------------------------------------------------------------------------|
| End Bringer       | 9               | A: Can reapply stun on broken target | ✅        | Extreme Physical damage, 6 hits. Increased damage if target Stunned.                     |
| Light Holder      | 4               | A: +2 AP                             | ✅        | Medium Light damage, 5 hits. Gains +1 Rank at completion.                                |
| Perfect Break     | 7 (5 at Rank B) | B: Reduced AP cost                   | ✅        | Very high Light damage. Can Break. Rank S on Break.                                      |
| Phantom Stars     | 9 (5 at Rank S) | S: Reduced AP cost                   | ✅        | AoE multi-hit all enemies. Trash fights only — useless in 1v1.                           |
| Steeled Strike    | 9               | S: Increased damage                  | ✅        | After 1 turn charge, extreme Physical damage. Interrupted if damage taken during charge. |
| Overload          | —               | —                                    | ✅        |                                                                                          |
| Assault Zero      | 3               | B: Increased damage                  | ❌        | Medium Physical single target.                                                           |
| Berserk Slash     | 4               | C: Increased damage                  | ❌        | Medium Physical, 3 hits. Damage scales with missing HP.                                  |
| Blitz             | 3               | B: Bonus only                        | ❌        | Insta-kills low-health enemies; otherwise deals damage.                                  |
| Burden            | 1               | —                                    | ❌        | Removes status effects from all allies.                                                  |
| Defiant Strike    | 3               | B: Increased damage                  | ❌        | 2-hit Physical, 100% Mark. Costs 30% current HP.                                         |
| From Fire         | 4               | B: Increased damage                  | ❌        | Healing from Burn. Situational — only useful if enemies have burn.                       |
| Leadership        | 3               | C: +1 more AP to allies              | ❌        | Extra AP to all allies.                                                                  |
| Marking Shot      | 2               | C: Increased damage                  | ❌        | Low damage + 100% Mark. No HP cost.                                                      |
| Paradigm Shift    | 1               | C: Bonus only                        | ❌        | Generates 1–3 AP. C Rank: bonus only. NOT a rank jump to S.                              |
| Perfect Recovery  | 3               | C: 100% HP heal                      | ❌        | Heals Verso only. Non-functional with Chevalam.                                          |
| Purification      | 5               | B: Increased damage                  | ❌        | Medium Light damage, 2 hits. Dispels self status effects.                                |
| Quick Strike      | 2               | D: Gives more Perfection             | ❌        | Low Physical.                                                                            |
| Strike Storm      | 7               | C: Crits give +2 Perfection          | ❌        | 5-hit high single-target weapon element.                                                 |
| Ascending Assault | —               | —                                    | ❌        |                                                                                          |
| Follow Up         | —               | —                                    | ❌        |                                                                                          |
| Radiant Slash     | —               | —                                    | ❌        |                                                                                          |
| Powerful          | —               | —                                    | ❌        |                                                                                          |
<!-- GENERATED:END -->

---

## Gradient Skills

<!-- GENERATED:START characters:Verso:gradients -->
| Gradient Skill | Gradient Cost | Acquired | Notes                                                                                                          |
|----------------|---------------|----------|----------------------------------------------------------------------------------------------------------------|
| Sabotage       | 1             | ✅        | Medium Physical damage to all enemies, 1 hit. Applies Mark.                                                    |
| Striker        | 2             | ✅        | High single-target Physical damage, 1 hit. Can Break.                                                          |
| Angel Eyes     | 3             | ✅        | Extreme Physical damage, 8 hits. Gain 1 Perfection per hit. Applies Aureole to Verso, reviving him if he dies. |
<!-- GENERATED:END -->

---

## Build Options

| Build Name                   | Role     | Key Skills                                                                                  | Key Lumina  | Status   | Notes                                                                     |
|------------------------------|----------|---------------------------------------------------------------------------------------------|-------------|----------|---------------------------------------------------------------------------|
| Levelling team (pre-Cheater) | DPS      | Quick Strike, Assault Zero, Strike Storm, Marking Shot, Phantom Stars, Perfect Break        | Core suite  | Complete | Rank build via Strike Storm crits; Perfect Break for S Rank jump          |
| Solo fights (completed)      | Solo DPS | Quick Strike, Assault Zero, Defiant Strike, Perfect Break, Perfect Recovery, Paradigm Shift | Solo Pictos | Complete | Second Chance borrowed from Maelle; now returned                          |
| Endgame (post-Cheater)       | Main DPS | Quick Strike, End Bringer, Phantom Stars, Perfect Break, Steeled Strike, Overload           | Core suite  | Current  | Light Holder → Overload swap Chat 23.                                     |
| End Bringer stunlock         | DPS      | End Bringer, Overload, Perfect Break, Quick Strike, Phantom Stars, Steeled Strike           | Core suite  | Future   | Seeram caps at Rank A, Overload jumps to A + End Bringer reapplies stun   |

### Simon fight

**Plan E:** Verso in main party (Team 1: Verso + Lune + Monoco). Standard endgame loadout applies with the following notes:
- Base Shield excluded (20LP freed) — not useful given Simon's damage output
- Overload replaces Light Holder — better AP generation for Verso in sustained fight
- Angel Eyes gradient skill used defensively as well as offensively (applies Aureole auto-revive)

**Plan F:** Team: Verso/Sciel/Maelle (same as Plan A/B). Sciel sets up Twilight for speed advantage; Verso stunlocks using Overload + End Bringer (see stunlock build); Maelle executes Gommage burst as in other plans.

**Lumina changes:** Base Shield excluded from main team core for Simon fight (non-functional vs Simon's damage output; Verso's Base Shield already excluded permanently due to Chevalam). No further Lumina changes.

**Skills changes (from standard):**
- Swap: Light Holder → Overload (better AP generation for sustained fight; functionally similar Rank climbing)

**Role:** Main DPS in Team 1 (Verso + Lune + Monoco). Primary damage dealer across all three phases. Angel Eyes gradient used both offensively and defensively (Aureole auto-revive). Second Chance provides revival safety net.

**Plan F:** Verso/Sciel/Maelle — same composition as Plans A and B. Sciel sets up Twilight for speed advantage; Verso stunlocks using Overload + End Bringer (stunlock is Verso's mechanic; the team around him is unchanged). Maelle executes Gommage burst. Equip Seeram instead of Chevalam — caps Verso at Rank A, required for the End Bringer loop. Not yet attempted.

**Revert after Simon:** swap Overload → Light Holder (or reassess); re-equip Chevalam if Seeram was used.

### Stunlock

- Equip Seeram — caps Verso at Rank A (cannot reach Rank S), which is required for the End Bringer to reapply stun
- Overload jumps to Rank A and fills to 9AP, ready for End Bringer
- End Bringer does massive damage to stunned targets
- At Rank A, End Bringer also reapplies stun on a broken target and this can be repeated each turn as long as Verso goes between target turns
- Use Sciel for tempo control so Verso can act every turn

---

## Key Decisions

- **Gaulteram over Glaceso:** Glaceso costs 2 Recoats net; no forgiveness mechanic. Gaulteram Level 4 forgiveness critical while parry skills developing. Same scaling as Chevalam = clean future swap.
- **Marking Shot over Defiant Strike:** Same 100% Mark. Defiant Strike costs 30% HP per use — unacceptable at ~20% parry rate. Marking Shot: 2 AP, no HP cost.
- **Strike Storm over Defiant Strike (damage slot):** More damage, synergises with Fortune's Fury. Mark handled by Marking Shot.
- **Phantom Stars retained:** Essential for AoE in Visages and multi-enemy areas. Useless in 1v1 — never use in boss fights.
- **Energising Break rotation confirmed (Chat 31):** Perfect Break (7 AP, 5 at B Rank) → Energising Break trigger (+3 AP via Energy Master) → Cheater turn → End Bringer (9 AP) on stunned target. Very effective — use when stun is available as an alternative to Steeled Strike burst.
- **Frenzy Pictos:** Stacks compound ×1.1 per Steeled Strike hit; Simoso copies do not advance the stack. Ceiling: ×3.14 at hit 13. Strong multiplier for endgame burst.
- **Powerful Shield:** 5LP. +10% damage per Shield Point on self — effectively permanent with Base Shield active. High value at low LP cost.
- **At Death's Door vs Clea's Life (Chat 32):** There are two ways of handling the reduction to 1HP from Overload — Clea's Life restores health to full immediately on the following Cheater turn and removes the risk from the health reduction. Alternatively, At Death's Door and several other Lumina provide huge damage boosts when on low health. For most battles, the At Death's Door option is best, as fights are over quickly due to huge damage spikes from Steeled Strike and End Bringer. For some tough boss battles, the Clea's Life option may be required for survivability.
- **Empowering Parry removed (Chat 32):** 5LP Lumina removed from loadout — not firing often enough in Endless Tower to justify the LP cost.

---

## Errors to Avoid

- **Light Holder and End Bringer recommended before available:** These skills were recommended in session summaries before Matt had obtained them. The "Confirmed NOT in skill list" note was accurate at the time — the error was recommending skills without checking current availability.
- **Glaceso recommendation:** Recommended over Gaulteram based on higher weapon level. Wrong: costs 2 Recoats net; no forgiveness; Gaulteram was the right choice at the time.
- **Phantom Stars in 1v1/solo fights:** AoE is useless vs single target.
- **Paradigm Shift rank jump:** Said it jumps to S Rank. Correct: generates 1–3 AP; C Rank bonus only.
- **Quick Strike rank jump (inherent):** Requires Glaceso Level 4. Without Glaceso = modest Perfection gain only.
- **Rank bonuses persist to higher ranks:** WRONG. Exact rank only. Yellow text = active.
- **Overload AP in same turn:** AP from Overload carries to the next turn, not the same turn.
- **Second Chance on multiple characters:** Only one character can hold this Pictos at a time.
- **Chevalam "available right now at Level 56":** Recommended level is 65–70+.
- **Gaulteram as Act 3 endgame weapon:** It is an Act 2 weapon.
- **Rank loss on hit as weapon-specific:** General Verso mechanic. Gaulteram's forgiveness is the exception.
- **Rank starts at C:** Rank starts at D. C was the effective floor with Lighteram equipped. With Chevalam there is no floor — hits can send Verso back to D.
- **Base Shield with Chevalam:** Non-functional — Chevalam prevents shields. Remove from loadout.
- **Alternating Critical + Simoso:** No synergy at 100% crit. All hits including Simoso extra hits benefit from guaranteed crits — Alternating Critical's boost applies only to non-crit hits, leaving nothing to boost.
