# Maelle — Clair Obscur: Expedition 33

*Last updated: 2026-04-10*

---

## Role

- **Primary role:** Main DPS
- **Party position:** Endgame main team (Maelle / Sciel / Verso); reserve during Act 3 levelling
- **Synergies:**
    + Sciel's Fortune's Fury doubles Maelle's damage
    + Verso's Marking Shot + Maelle's Rewarding Mark Lumina generate AP return
    + Burn from Lune or Verso (Corpeso) enables Swift Stride entry and Breaking Burn multiplier
    + Burning Canvas damage scales with burn stacks on target — synergises with Corpeso's base attack applying 2 burn per Rank

---

## Mechanics

### Stances

Maelle's central system is **stances**. She starts each battle in Stanceless (unless her weapon causes her to start in a different stance — Medalum's Level 4 ability starts her in Virtuose). Skills either switch stance, maintain current stance, or are stance-neutral.

| Stance     | Effect                                              |
|------------|-----------------------------------------------------|
| Stanceless | No special effects. Default starting stance.        |
| Defensive  | Take 50% less damage; gain 1 AP per Parry or Dodge. |
| Offensive  | Deal 50% more damage; also take 50% more damage.    |
| Virtuose   | Deal 200% more damage.                              |

**Virtuose** is her most powerful stance. Key interactions:
- Percée costs 2 AP instead of 5 in Virtuose — but Maelle **leaves Virtuose after using it**; cannot be spammed at 2 AP (one use per Virtuose window)
- Using the same stance trigger twice in succession puts Maelle into Stanceless — e.g. two consecutive Virtuose-entry skills will leave her Stanceless after the second
- Fleuret Fury keeps her in Virtuose if already there
- Entering Virtuose triples the damage of follow-up skills (e.g. Sword Ballet deals 3× damage after Gustave's Homage switches to Virtuose)

Lithum (endgame weapon) changes the entry mechanic: re-enters Virtuose after every successful counterattack (repeatable), does not remove Mark when hitting in Virtuose, and grants a free Shell charge on leaving Virtuose.

Stendhal is the Virtuose nuke — 8 AP, extreme single-hit Void damage, switches to Stanceless, applies Defenceless to Maelle herself. Nerfed 40% in Patch 1.2.3 — no longer guaranteed to one-shot Alicia.

### Key Synergies

**Last Chance + Cheater + Clea's Life loop:**

Last Chance (1 AP) reduces HP to 1, refills all AP, and switches to Virtuose. Cheater fires an immediate extra turn. Clea's Life triggers at the start of that extra turn (condition: no damage taken since last turn — met because Cheater bonus turn is immediate), restoring 100% HP.

Net effect: full AP reset + Virtuose stance + full HP in a single 1 AP move. Full Strength Lumina (25% damage at full Health) is also active on the Cheater turn after HP is restored.

Use Last Chance as a deliberate rotation tool rather than an emergency skill. Practical usage: when AP is low and you want to re-enter Virtuose with full resources.

**Lithum Shell-Powerful loop (Chat 32):**

Lithum applies Shell when leaving Virtuose Stance (L20). Powerful On Shell converts that Shell to Powerful. Greater Powerful then amplifies it by +15%, giving a total ~40% Powerful damage bonus. This fires reliably on every Last Chance rotation and the uplift is meaningful in practice. Note: Energising Shell, Powerful On Shell, and Greater Powerful are all Lithum-dependent — remove them if swapping weapons.

**Lithum Shell overrides Defenceless (Chat 32):**

Stendhal applies Defenceless to Maelle, but in the standard Last Chance rotation Lithum's Shell (triggered on leaving Virtuose Stance) immediately overwrites it. Net result: Shell provides approximately 30% damage reduction below baseline — the rotation is net positive defensively. Empirically confirmed: baseline incoming 1637 / Defenceless 2046 (+25%) / Shell after Last Chance 1146 (−30%). Stendhal used without prior Virtuose (no Shell trigger) leaves Maelle Defenceless — avoid this in the standard build.

---

## Stats

### Level and Attributes

<!-- GENERATED:START characters:Maelle:attributes -->
| Attribute | Value |
|-----------|-------|
| Level     | 99    |
| Might     | 99    |
| Agility   | 99    |
| Luck      | 99    |
| Vitality  | 0     |
| Defence   | 0     |
<!-- GENERATED:END -->

*Lithum scales Luck S / Agility A — respec from Medalum (Defence+Agility) required when switching.*

### Combat Stats

<!-- GENERATED:START characters:Maelle:stats -->
*Stats with Lithum (33) and Energising Turn (L31), Empowering Break (L28), Shortcut (L31) Pictos equipped.*

| Stat    | Base | Modified |
|---------|------|----------|
| Health  | 2420 | 2420     |
| Attack  | 1503 | 11583    |
| Speed   | 1274 | 3769     |
| Defence | 182  | 182      |
| Crit    | 41%  | 109%     |
<!-- GENERATED:END -->

---

## Weapons

### Current (Endgame)
<!-- GENERATED:START weapons:Maelle:Lithum -->
- **Name:** Lithum (33)
- **Power:** 9302
- **Element:** Void
- **Scaling:** Luck S, Agility A
- **Effects:**
    - Level 4: In Virtuose Stance, hitting a Marked enemy doesn't remove Mark.
    - Level 10: Switch to Virtuose Stance on Counterattack.
    - Level 20: Gain Shell when switching out of Virtuose Stance.
<!-- GENERATED:END -->
- **Notes:** Nearly doubled in power from level 32 to 33 (from 4651 to 9254). Respec required from Medalum (Defence+Agility) to Lithum (Luck+Agility). Shell from L20 synergises with Longer Shell and Powerful On Shell Lumina.
- **Core rotation:** Any skill switching to Defensive stance → parry/counterattack → Counterattack triggers Virtuose entry (L10) → attack in Virtuose → Shell applied on leaving Virtuose (L20) → repeat. Phantom Strike is a useful Defensive-entry option as it also contributes +35% Gradient Charge per use.
- **L4 Mark synergy:** Hitting a Marked enemy in Virtuose does not consume the Mark. This enables repeated Percée use in Virtuose on a Marked enemy (each cast benefits from reduced 2 AP cost, increased damage, and Rewarding Mark AP return) without losing the Mark. Burning Canvas can similarly be used in Virtuose on a Marked enemy for repeated burn-scaling damage without consuming the Mark. Both synergies make these skills substantially stronger with Lithum than with Medalum.

### Future candidates
- **Licorum** — Physical. L4: "Each successive Skill hit deals 10% more damage" — stacks multiplicatively with Frenzy Pictos (×1.21 compound per hit, confirmed Chat 31 vs Gargant using Gustave's Homage). Strong candidate to replace Lithum for multi-hit builds once Frenzy is available. Verify scaling attributes and respec requirements before switching.

---

## Pictos

### Current (party loadout)

<!-- GENERATED:START characters:Maelle:Pictos -->
| Slot | Pictos           | Level | Stat Bonus            | Effect                                                           |
|------|------------------|-------|-----------------------|------------------------------------------------------------------|
| 1    | Energising Turn  | 31    | Speed +1277           | +1 AP on turn start.                                             |
| 2    | Empowering Break | 28    | Speed +546, Crit +32% | Gain Powerful on Breaking a target.                              |
| 3    | Shortcut         | 31    | Speed +672, Crit +36% | Immediately play when falling below 30% Health. Once per battle. |
<!-- GENERATED:END -->

*Cheater equipped via Lumina (40 LP) rather than Pictos slot.*

---

## Lumina

### LP Budget
<!-- GENERATED:START characters:Maelle:LP -->
- **Current capacity:** 506 LP
- **Used:** 491 LP
- **Spare:** 15 LP
<!-- GENERATED:END -->

### Lumina Adjustments

<!-- GENERATED:START characters:Maelle:Lumina:adjustments -->
| Lumina                 | Change | LP | Notes                                                                                                                                                                                                                       |
|------------------------|--------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Augmented First Strike | Added  | 5  | DPS expansion. 50% increased damage on first hit, once per battle.                                                                                                                                                          |
| Burn Affinity          | Added  | 10 | DPS expansion. 25% increased damage against burning targets. Synergy: Burning Shots and Marking Shots (Free Aim) can seed burn.                                                                                             |
| Charging Critical      | Added  | 10 | DPS expansion. +20% Gradient Charge on Critical Hit, once per turn. Fires every turn at 109% crit.                                                                                                                          |
| Dead Energy I          | Added  | 2  | DPS expansion. +3 AP on killing an enemy.                                                                                                                                                                                   |
| Dead Energy II         | Added  | 2  | DPS expansion. +3 AP on killing an enemy (stacks with Dead Energy I).                                                                                                                                                       |
| Double Third           | Added  | 10 | DPS expansion. Every 3rd hit deals double damage. Fires on multi-hit skills (Sword Ballet, Burning Canvas).                                                                                                                 |
| Empowering Dodge       | Added  | 5  | DPS expansion. 5% increased damage per consecutive dodge, stacks to 10. Parry does not reset the stack.                                                                                                                     |
| First Offensive        | Added  | 5  | DPS expansion. 50% increased damage on first hit dealt, once per battle.                                                                                                                                                    |
| Frenzy                 | Added  | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Fires on multi-hit skills (Sword Ballet, Burning Canvas) - not on single-hit Stendhal/Gommage.                                                              |
| Glass Cannon           | Added  | 10 | DPS expansion. 25% increased damage, 25% increased damage taken.                                                                                                                                                            |
| Immaculate             | Added  | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                                                                               |
| Powerful Shield        | Added  | 5  | DPS expansion. 10% increased damage per Shield Point on self.                                                                                                                                                               |
| Warming Up             | Added  | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks. Strong with sustained multi-turn presence.                                                                                                         |
| At Death's Door        | Added  | 5  | Low-health expansion. 50% increased damage below 10% HP. Active permanently while at 1 HP from Last Chance.                                                                                                                 |
| Confident Fighter      | Added  | 15 | Low-health expansion. 30% increased damage, cannot be healed. Conflicts with Sciel's healing - accepted tradeoff for the Low-health build.                                                                                  |
| In Medias Res          | Added  | 10 | Low-health expansion. +3 Shields at battle start, max Health halved. HP penalty irrelevant at 1 HP from Last Chance.                                                                                                        |
| Inverted Affinity      | Added  | 5  | Low-health expansion. 50% increased damage while Inverted (cannot be healed).                                                                                                                                               |
| Gradient Fighter       | Added  | 5  | Personal addition. 25% increased damage with Gradient Attacks - large boost for Gommage.                                                                                                                                    |
| Greater Powerful       | Added  | 10 | Personal addition (Lithum suite). +15% to Powerful bonus - boosts Powerful On Shell.                                                                                                                                        |
| Greater Shell          | Added  | 10 | Personal addition (Lithum suite). Stronger Shell from Lithum on Virtuose exit.                                                                                                                                              |
| Longer Powerful        | Added  | 10 | Personal addition (Lithum suite). +2 turn duration to Powerful from Powerful On Shell.                                                                                                                                      |
| Longer Shell           | Added  | 10 | Personal addition (Lithum suite). On applying Shell, duration +2 - extends Lithum Shell from Virtuose exit.                                                                                                                 |
| Powerful On Shell      | Added  | 10 | Personal addition (Lithum suite). Apply Powerful on applying Shell - Lithum applies Shell on Virtuose exit (Last Chance -> Stendhal/Gommage), triggering this every cycle. Boosted by Greater Powerful and Longer Powerful. |
| Energising Shell       | Added  | 10 | Personal addition (Lithum suite). Give 2 AP on applying Shell - fires every Virtuose exit via Lithum.                                                                                                                       |
| Empowering Break       | Added  | —  | Free from Pictos.                                                                                                                                                                                                           |
<!-- GENERATED:END -->

### Current Loadout

<!-- GENERATED:START characters:Maelle:Lumina -->
| Lumina                 | LP | Notes                                                                                                                                                                                                                       |
|------------------------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AP Discount            | 30 | Reduces skill AP cost by 1.                                                                                                                                                                                                 |
| Aegis Revival          | 5  | +1 Shield on being revived.                                                                                                                                                                                                 |
| At Death's Door        | 5  | Low-health expansion. 50% increased damage below 10% HP. Active permanently while at 1 HP from Last Chance.                                                                                                                 |
| Augmented First Strike | 5  | DPS expansion. 50% increased damage on first hit, once per battle.                                                                                                                                                          |
| Base Shield            | 20 | Grants 1 Shield HP buffer per turn.                                                                                                                                                                                         |
| Breaker                | 10 | 25% increased Break damage.                                                                                                                                                                                                 |
| Breaking Burn          | 5  | 25% increased Break damage on Burning enemies.                                                                                                                                                                              |
| Breaking Death         | 5  | Fully charge enemy break bar on death.                                                                                                                                                                                      |
| Burn Affinity          | 10 | DPS expansion. 25% increased damage against burning targets. Synergy: Burning Shots and Marking Shots (Free Aim) can seed burn.                                                                                             |
| Burning Shots          | 3  | 20% chance to Burn on Free Aim shot.                                                                                                                                                                                        |
| Charging Critical      | 10 | DPS expansion. +20% Gradient Charge on Critical Hit, once per turn. Fires every turn at 109% crit.                                                                                                                          |
| Cheater                | 40 | Extra turn after using a skill, once per turn.                                                                                                                                                                              |
| Confident Fighter      | 15 | Low-health expansion. 30% increased damage, cannot be healed. Conflicts with Sciel's healing - accepted tradeoff for the Low-health build.                                                                                  |
| Critical Break         | 5  | 25% increased Break damage on Critical hits.                                                                                                                                                                                |
| Dead Energy I          | 2  | DPS expansion. +3 AP on killing an enemy.                                                                                                                                                                                   |
| Dead Energy II         | 2  | DPS expansion. +3 AP on killing an enemy (stacks with Dead Energy I).                                                                                                                                                       |
| Dodger                 | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                                                                                                                                                                                  |
| Double Third           | 10 | DPS expansion. Every 3rd hit deals double damage. Fires on multi-hit skills (Sword Ballet, Burning Canvas).                                                                                                                 |
| Empowering Break       | —  | FREE from Empowering Break Pictos                                                                                                                                                                                           |
| Empowering Dodge       | 5  | DPS expansion. 5% increased damage per consecutive dodge, stacks to 10. Parry does not reset the stack.                                                                                                                     |
| Energising Shell       | 10 | Personal addition (Lithum suite). Give 2 AP on applying Shell - fires every Virtuose exit via Lithum.                                                                                                                       |
| Energising Start I     | 5  | +1 AP on battle start. Boosted by Energy Master.                                                                                                                                                                            |
| Energising Turn        | —  | FREE from Energising Turn Pictos                                                                                                                                                                                            |
| Energy Master          | 40 | Every AP gain is increased by 1.                                                                                                                                                                                            |
| First Offensive        | 5  | DPS expansion. 50% increased damage on first hit dealt, once per battle.                                                                                                                                                    |
| First Strike           | 10 | Act first in battle.                                                                                                                                                                                                        |
| Frenzy                 | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Fires on multi-hit skills (Sword Ballet, Burning Canvas) - not on single-hit Stendhal/Gommage.                                                              |
| Glass Cannon           | 10 | DPS expansion. 25% increased damage, 25% increased damage taken.                                                                                                                                                            |
| Gradient Fighter       | 5  | Personal addition. 25% increased damage with Gradient Attacks - large boost for Gommage.                                                                                                                                    |
| Greater Powerful       | 10 | Personal addition (Lithum suite). +15% to Powerful bonus - boosts Powerful On Shell.                                                                                                                                        |
| Greater Shell          | 10 | Personal addition (Lithum suite). Stronger Shell from Lithum on Virtuose exit.                                                                                                                                              |
| Immaculate             | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                                                                               |
| In Medias Res          | 10 | Low-health expansion. +3 Shields at battle start, max Health halved. HP penalty irrelevant at 1 HP from Last Chance.                                                                                                        |
| Inverted Affinity      | 5  | Low-health expansion. 50% increased damage while Inverted (cannot be healed).                                                                                                                                               |
| Longer Powerful        | 10 | Personal addition (Lithum suite). +2 turn duration to Powerful from Powerful On Shell.                                                                                                                                      |
| Longer Shell           | 10 | Personal addition (Lithum suite). On applying Shell, duration +2 - extends Lithum Shell from Virtuose exit.                                                                                                                 |
| Marking Shots          | 3  | 20% chance to apply Mark on Free Aim shot.                                                                                                                                                                                  |
| Painted Power          | 5  | Damage can exceed 9,999. Essential for all characters from Act 3 onwards.                                                                                                                                                   |
| Powerful On Shell      | 10 | Personal addition (Lithum suite). Apply Powerful on applying Shell - Lithum applies Shell on Virtuose exit (Last Chance -> Stendhal/Gommage), triggering this every cycle. Boosted by Greater Powerful and Longer Powerful. |
| Powerful Shield        | 5  | DPS expansion. 10% increased damage per Shield Point on self.                                                                                                                                                               |
| Protecting Death       | 5  | Allies gain Shell on death.                                                                                                                                                                                                 |
| SOS Power              | 5  | Apply Powerful when falling below 50% Health.                                                                                                                                                                               |
| SOS Rush               | 5  | Apply Rush when falling below 50% Health.                                                                                                                                                                                   |
| SOS Shell              | 5  | Apply Shell when falling below 50% Health.                                                                                                                                                                                  |
| Second Chance          | 40 | Revive with 100% Health. Once per battle.                                                                                                                                                                                   |
| Shielding Death        | 10 | Allies gain 3 Shield points on death.                                                                                                                                                                                       |
| Shortcut               | —  | FREE from Shortcut Pictos                                                                                                                                                                                                   |
| Survivor               | 20 | Survive fatal damage with 1 Health, once per battle.                                                                                                                                                                        |
| Teamwork               | 5  | 10% increased damage while all allies are alive.                                                                                                                                                                            |
| Warming Up             | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks. Strong with sustained multi-turn presence.                                                                                                         |
<!-- GENERATED:END -->

---

## Skills

<!-- GENERATED:START characters:Maelle:skills -->
**Currently equipped (6):** Phantom Strike, Fleuret Fury, Stendhal, Burning Canvas, Last Chance, Pyrolyse

| Skill            | AP                | Stance     | Equipped | Notes                                                                                                                                           |
|------------------|-------------------|------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Phantom Strike   | 4                 | Defensive  | ✅        | 4-hit very high Void AoE. Switches to Defensive stance. Gives +35% of a Gradient Charge.                                                        |
| Fleuret Fury     | 6                 | —          | ✅        | 3-hit high single-target Physical. Stays in Virtuose if already there. Can Break.                                                               |
| Stendhal         | 8                 | Stanceless | ✅        | Extreme single-target Void damage, 1 hit. Switches to Stanceless. Removes self-shields. Applies Defenceless to self. Nerfed 40% in Patch 1.2.3. |
| Burning Canvas   | 5                 | Offensive  | ✅        | High Void damage + 1 burn per hit. Damage increased for each burn stack on target.                                                              |
| Last Chance      | 1                 | Virtuose   | ✅        | Reduces self-health to 1. Refills all AP.                                                                                                       |
| Pyrolyse         | —                 | —          | ✅        |                                                                                                                                                 |
| Percée           | 5 (2 in Virtuose) | Stanceless | ❌        | Increased damage to Marked target. 2 AP in Virtuose but leaves Virtuose after — one use per Virtuose window.                                    |
| Gustave's Homage | 8                 | Virtuose   | ❌        | 8-hit extreme Physical damage. Switches to Virtuose Stance.                                                                                     |
| Sword Ballet     | 9                 | —          | ❌        | 5-hit extreme single-target weapon element. Crits deal double damage. Primary Virtuose damage skill.                                            |
| Breaking Rules   | 3                 | Offensive  | ❌        | Destroys all target shields. Gains 1 AP per shield destroyed. If target is Defenceless: grants a second turn.                                   |
| Combustion       | 4                 | Offensive  | ❌        | Medium single target Physical damage. 2 hits. Consumes up to 10 Burn for increased damage.                                                      |
| Degagement       | 2                 | Offensive  | ❌        | Low Fire damage. Target becomes weak to Fire.                                                                                                   |
| Égide            | 3                 | Defensive  | ❌        | Protects allies by taking damage in their place for 2 turns.                                                                                    |
| Fencer's Flurry  | 4                 | Offensive  | ❌        | Medium AoE. Applies Defenceless 1 turn.                                                                                                         |
| Guard Up         | 3                 | Offensive  | ❌        | Shell buff for allies.                                                                                                                          |
| Mezzo Forte      | 1                 | —          | ❌        | Reapply current stance. Give 2–4 AP.                                                                                                            |
| Momentum Strike  | 7                 | Defensive  | ❌        | High damage. Costs 4 AP in Virtuose.                                                                                                            |
| Offensive Switch | 1                 | Offensive  | ❌        | Low damage. Applies Defenceless to enemy.                                                                                                       |
| Payback          | 9                 | Defensive  | ❌        | Very high Physical damage. Reduced AP cost for each attack parried since last turn. Can Break.                                                  |
| Rain of Fire     | 5                 | Offensive  | ❌        | Medium Fire damage + 3 burn per hit, 2 hits. Applies 2 more burn per hit if in Defensive.                                                       |
| Spark            | 3                 | Defensive  | ❌        | Low Fire damage + 3 burn. Applies 2 more burn if in Offensive.                                                                                  |
| Swift Stride     | 3                 | Virtuose   | ❌        | Low Physical. Switches to Virtuose if target burning. Regains 0–2 AP.                                                                           |
| Revenge          | —                 | —          | ❌        |                                                                                                                                                 |
<!-- GENERATED:END -->

---

## Gradient Skills

<!-- GENERATED:START characters:Maelle:gradients -->
| Gradient Skill  | Gradient Cost | Acquired | Notes                                                                                                |
|-----------------|---------------|----------|------------------------------------------------------------------------------------------------------|
| Virtuose Strike | 1             | ✅        | High single-target physical damage, 5 hits; switches to Virtuose Stance.                             |
| Phoenix Flame   | 2             | ✅        | Applies 10 Burn to all enemies; revives all allies with 50–70% Health; switches to Offensive Stance. |
| Gommage         | 3             | ✅        | Kills weak targets; otherwise extreme Void damage 1 hit, then switches to Virtuose Stance.           |
<!-- GENERATED:END -->

---

## Build Options

| Build         | Role      | Key Skills                                                                         | Key Lumina                       | Status                                                                                   | Notes                                                                 |
|---------------|-----------|------------------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Standard DPS  | Main DPS  | Gustave's Homage, Sword Ballet, Fleuret Fury, Percée, Phantom Strike, Stendhal.    | Full 158 LP loadout (149 used)  | Current                                                                                   | Cheater via Lumina (40 LP)                                            |
| Solo          | Solo DPS  | Stendhal, Phantom Strike, Last Chance, Gustave's Homage, Fleuret Fury, Mezzo Forte | Swap Cheater to Pictos; add Last Stand suite + Recovery + Energising Attack I; remove Teamwork/Breaking Counter/Dead Energy | Previous / Shelved | Borrow Cheater Pictos + Second Chance from Verso |
| Burn-stacking | Burn DPS  | Burning Canvas as primary; Stalum weapon; Swift Stride for Virtuose entry          | Investigate separately           | Future                                                                                   | Synergises with Corpeso (Verso), Kralim (Lune)                        |

### Solo build (The Reacher)

**Pictos:** Cheater (from Verso) / Second Chance (from Verso) / Gradient Break. Solo Lumina build applied and reversed after completing The Reacher.

**Lumina changes (from standard loadout):**
- Remove: Cheater (40LP, swap to Pictos), Teamwork (5LP), Breaking Counter (3LP), Dead Energy I (2LP), Dead Energy II (2LP) — total freed: 52LP
- Add: Solo Fighter (1LP), Last Stand Critical (3LP), Accelerating Last Stand (3LP), Empowering Last Stand (3LP), Protecting Last Stand (3LP), Recovery (10LP), Energising Attack I (10LP) — total added: 33LP
- Net: 19LP spare within 158LP budget at time

**Skills:** Community standard — Stendhal, Phantom Strike, Last Chance, Gustave's Homage, Fleuret Fury, Mezzo Forte. Alternative: swap Fleuret Fury for Sword Ballet if preferring burst over Break utility.

**Gradient Break over Burning Break:** Chosen for speed advantage (1821 vs 1397) to handle Alicia's Rush phase at 25% HP. Second Chance covers survivability.

**Revert:** Return Cheater and Second Chance Pictos to Verso. Remove Last Stand suite + Recovery + Energising Attack I. Restore Teamwork, Breaking Counter, Dead Energy I+II. ✅ Completed.

### Simon fight

**Lumina changes (from standard loadout):**
- Remove: Base Shield (20LP) — not effective given Simon's damage output; frees LP for other options
- Add: First Strike Lumina — for Simon fight only; revert after

**Skills:** Standard loadout. Maelle enters as reserve (Team 2: Maelle + Sciel) with Last Chance providing full AP reset on cold entry into Phase 3. Key role: apply Defenceless (via Offensive Switch) then use Last Chance → Gommage burst sequence. Maelle must act before Sciel in Phase 3 for Defenceless to be active during Gommage.

**Gradient skill priority:** Gommage (3GP) is the primary Phase 3 burst. Requires 3GP banked before Phase 3 starts — GP carries over from Phase 2.

**Revert after Simon:** Remove First Strike Lumina; restore Base Shield (20LP).

### Burn-stacking

Burning Canvas (5 AP, switches to Offensive, high Void damage + 1 burn per hit) deals increased damage for each burn stack on target. Corpeso (Verso's weapon) applies 2 burn per Rank on base attack — synergises to stack burn quickly before Maelle fires Burning Canvas.

### Solo At Death's Door

High-damage solo build using Monoco as a self-destructing support. Monoco's Auto Death fires at battle start (before any turns), applying Death Bomb damage and a death suite of buffs. Maelle operates at 1HP to maximise her low-health damage multipliers.

**Pictos:** Energising Turn (L31) / Energy Master (L30) / Cheater (L24)

**Skills:** Phantom Strike (7), Fleuret Fury (6), Stendhal (8), Burning Canvas (5), Last Chance (1), Pyrolyse (9)

**LP:** 361/361

**Key multipliers (all apply to Stendhal):**
- At Death's Door (5LP) — ×1.5 below 10% HP
- Inverted Affinity (5LP) — ×1.5 while Inverted; blocks healing
- Confident Fighter (15LP) — ×1.3; can't be healed (redundant with Inverted but stacks)
- Glass Cannon (10LP) — ×1.25 damage, take ×1.25 more
- Immaculate (10LP) — ×1.3 until first hit received
- Solo Fighter (1LP) — ×1.5 while fighting alone
- Burn Affinity (10LP) — ×1.25 against burning targets (Monoco's Burning Death provides burns)
- Augmented First Strike (5LP) — ×1.5 on first hit of battle
- First Offensive (5LP) — ×1.5 on first hit dealt and taken
- Last Stand Critical (3LP) — 100% crit chance while fighting alone
- Powerful Shield (5LP) — ×1.1 per shield on self at time of hit (Monoco's Shielding Death provides 3 Shields)

**Active Lumina (full list):** AP Discount (30), Accelerating Last Stand (3), At Death's Door (5), Augmented First Strike (5), Base Shield (20), Breaker (10), Breaking Burn (5), Breaking Counter (3), Breaking Death (5), Burn Affinity (10), Charging Critical (10), Cheater (40, Pictos), Confident Fighter (15), Critical Break (5), Dead Energy I (2), Dead Energy II (2), Dodger (1), Empowering Last Stand (3), Energising Shell (10), Energising Start I (5), Energising Turn (20, Pictos), Energy Master (40, Pictos), Exposing Break (5), First Offensive (5), First Strike (10), Glass Cannon (10), Gradient Fighter (5), Greater Defenceless (15), Greater Powerful (10), Greater Shell (10), Immaculate (10), Inverted Affinity (5), Last Stand Critical (3), Longer Powerful (10), Longer Shell (10), Painted Power (5), Powerful On Shell (10), Powerful Shield (5), Protecting Last Stand (3), Second Chance (40), Shortcut (5), Solo Fighter (1), Survivor (20), Warming Up (15)

**Survivability:** Monoco's death suite (Shielding Death: 3 shields, Protecting Death: Shell, Burning Death: burns for Burn Affinity, Energising Death: +4 AP) fires before Maelle acts. Base Shield retains 1 shield per turn. Protecting Last Stand and Lithum L20 provide Shell which reduces damage taken, but this doesn't help while on 1HP. Rely on shields, dodging and parrying, with high speed Pictos so Maelle can finish fights quickly, and Survivor and Second Chance provide safety nets.

**Peak performance:** 21m damage recorded on Last Chance + Stendhal (Chat 32).

---

## Key Decisions

- **Lithum over all alternatives:** Strictly better than Medalum for parry-competent players. Same scaling = no respec. The Reacher must be completed before Renoir — choose "Truth" for Gustave resurrection path and Relationship Level 7.
- **Lithum confirmed — Medalum obsolete for Stendhal builds (Chat 32):** Community research confirms Medalum's L20 double-damage was a bug, fixed in Patch 1.2.3 (now doubles only burn damage). For a single-hit Stendhal build without burn stacking, Medalum offers no meaningful advantage. Lithum advantages: Void element (no enemy resistances), Agility/Luck scaling matches Maelle's attribute spread, reliable Shell-Powerful loop. Do not upgrade Medalum unless switching to a burn-stacking build.
- **Solo At Death's Door build (Chat 32):** High-risk high-reward variant using Monoco as self-destructing support (Auto Death at battle start). Maelle runs At Death's Door (×1.5 below 10% HP) + Inverted Affinity (×1.5, blocks healing) + Confident Fighter (×1.3) for approximately 2.3× damage advantage over Clea's Life build. LP 361/361. Peak recorded: 21m damage. See Solo At Death's Door build subsection.
- **Glaisum as Lithum alternative:** Same scaling as Medalum/Lithum (Defence + Agility), no respec, higher base power. More defensive/supportive (ally heals, self-cleanse) vs Lithum's offensive (Mark persistence, Virtuose on Counterattack). Lithum preferred for standard DPS build; Glaisum worth considering if survivability becomes a priority.
- **Stalum for burn-stacking:** Core weapon for the burn-stacking build path. Not current priority but available at level 23 when ready.
- **Cheater via Lumina:** All three endgame team members use Cheater via Lumina (40 LP) rather than Pictos. For solo fights, swap Cheater to Pictos to free 40 LP.
- **Phantom Strike over Fencer's Flurry:** Phantom Strike replaced Fencer's Flurry. Better damage, adds Defensive stance utility and Gradient generation. AoE function preserved.
- **Gradient Break over Burning Break for solo:** For The Reacher, Gradient Break chosen for speed advantage (1821 vs 1397) to handle Alicia's Rush phase at 25% HP. Second Chance covers survivability.
- **Licorum for multi-hit builds only:** Licorum L4 and Frenzy Pictos stack multiplicatively (×1.21 per hit compound, confirmed Chat 31). Doesn't help for Stendhal or Gommage, so only really useful for a different playstyle.

---

## Errors to Avoid

- **Fueling Break effect:** Said it gives AP on Break damage. Correct: breaking an enemy doubles Burn stacks on that enemy.
- **Healing Parry effect:** Said 10% heal on parry. Correct: 3%.
- **Last Stand Lumina triggers:** Said HP-threshold triggers (below 25%). Correct: solo-fighting bonuses only — irrelevant in party fights.
- **Percée spam in Virtuose:** 2 AP cost only applies once per Virtuose window — Maelle leaves Virtuose after using it.
- **Gustave's Homage stance:** Switches TO Virtuose; does not keep her in Virtuose indefinitely.
- **LP overrun:** Previous calculation reached 118 LP against 112 LP budget. Always recount before finalising. Current budget is 158 LP.
- **Drop Fencer's Flurry:** Claude recommended dropping it in Chat 1. Incorrect at the time — it was Maelle's best AoE. Now correctly replaced by Phantom Strike.
- **Stendhal AP cost:** Said 4 AP. Correct: 8 AP.
- **Stendhal one-shots Alicia:** Was true pre-patch. Nerfed 40% in Patch 1.2.3 — no longer assumed.
- **Stendhal self-Defenceless:** Stendhal applies Defenceless to Maelle herself on use. Plan accordingly.
- **Teamwork effect:** Said it gives AP when an ally uses a skill. Correct: passive damage bonus when whole team is alive — non-functional in solo fights for a different reason than originally stated.
- **Melarum source:** Do not assert "Old Lumiere post-Renoir" — this is likely wrong.
- **Shell vs Shield confusion (recurring):** Shell = 20% damage reduction for 3 turns. Shield = damage-blocking HP buffer (1 per turn from Base Shield Lumina, or other sources). Stendhal removes self-shields (HP buffer), not Shell. Lithum L20 grants Shell (damage reduction) on leaving Virtuose. These are entirely separate mechanics — do not conflate them.
- **Lithum scaling:** Lithum scales Luck S / Agility A — not Defence + Agility like Medalum. Respec is required when switching. Glaisum (Defence A / Agility B) also requires a respec from Lithum.
