# Clair Obscur: Expedition 33 — Pictos and Lumina Summary

*Generated from `data/pictos-lumina.json`.*

See [`reference/pictos-lumina-catalogue.md`](../reference/pictos-lumina-catalogue.md) for the full list of all 194 Pictos.

---

## 1. Pictos Mechanics

Pictos are collectible items giving stat boosts and effects. Each character has 3 Pictos slots. Equipping a Pictos applies both its **stat boosts** and its **effect**. After winning 4 battles with a Pictos equipped, it is learnt as a Lumina.

Higher level Pictos give higher stat boosts. Pictos stat boosts cover Health, Defence, Speed, and Crit only — they do not boost Attack. Attack scaling comes from base stats, weapons, attributes, and Lumina. With attributes maxed at 99, Pictos stat boosts are the primary source of character growth.

Each Pictos exists as a single unique copy — only one character can equip it at a time. Any other character wanting the same Lumina effect must pay the full LP cost. Finding a duplicate of an already-owned Pictos upgrades the existing copy (increases level and stat boosts) rather than adding a second copy.

Extra-turn effects (e.g. Quick Break's "play again on Break") do not stack — if a character is already on a bonus turn, any further extra-turn trigger is nullified. Quick Break is therefore a pure stat stick for any Cheater user.

---

## 2. Lumina Mechanics

Lumina are passive effects derived from Pictos. They apply the **effect only** — not the stat boosts. A character cannot equip the Lumina of a Pictos they already have equipped (the effect would be redundant and the game prevents it).

Each character has a pool of Lumina Points (LP). LP = character level by default. Permanently increase LP by spending Colour of Lumina items (1 Colour = 1 LP).

Any Lumina costs 0 LP for a character who has that Pictos equipped — the stat boosts and the Lumina effect are both active from the Pictos, so there's no LP charge for the Lumina. For example, a character holding the Cheater Pictos gets the Cheater Lumina effect at no LP cost, rather than 40 LP. If characters hold a Pictos from the core set, they free up those LP to use on other Lumina.

Passive Lumina effects that trigger "on turn start" (e.g. Recovery: 10% health regen) fire on bonus turns granted by Cheater or Intervention, not only on normal turns.

For status immunity, add the relevant Lumina (e.g. Anti-Blight, 10LP) rather than swapping Pictos. The Pictos stays on its holder for the stat boosts; Lumina is the situational layer.

**In-game Lumina Sets:** The game allows saving up to 50 Lumina Sets. Sets apply a group of Lumina in one action. The recommended workflow is: apply core set first, then add character-specific extras on top.

---

## 3. Main Team Pictos

### Maelle

<!-- GENERATED:START characters:Maelle:Pictos -->
| Slot | Pictos           | Level | Stat Bonus            | Effect                                                           |
|------|------------------|-------|-----------------------|------------------------------------------------------------------|
| 1    | Energising Turn  | 31    | Speed +1277           | +1 AP on turn start.                                             |
| 2    | Empowering Break | 28    | Speed +546, Crit +32% | Gain Powerful on Breaking a target.                              |
| 3    | Shortcut         | 31    | Speed +672, Crit +36% | Immediately play when falling below 30% Health. Once per battle. |
<!-- GENERATED:END -->

### Verso

<!-- GENERATED:START characters:Verso:Pictos -->
| Slot | Pictos               | Level | Stat Bonus            | Effect                                                               |
|------|----------------------|-------|-----------------------|----------------------------------------------------------------------|
| 1    | Alternating Critical | 29    | Speed +293, Crit +50% | On Critical hit, 100% increased damage of the next non-Critical hit. |
| 2    | Quick Break          | 31    | Speed +672, Crit +36% | Play again on Breaking a target.                                     |
| 3    | Energising Stun      | 28    | Speed +519, Crit +31% | +1 AP on hitting a Stunned target with a Skill.                      |
<!-- GENERATED:END -->

### Sciel

<!-- GENERATED:START characters:Sciel:Pictos -->
| Slot | Pictos          | Level | Stat Bonus            | Effect                                   |
|------|-----------------|-------|-----------------------|------------------------------------------|
| 1    | Energy Master   | 30    | Health +4979          | Every AP gain is increased by 1          |
| 2    | Breaking Death  | 29    | Speed +586, Crit +33% | Fully charge enemy break bar on death    |
| 3    | Powerful Revive | 28    | Speed +546, Crit +32% | Apply Powerful for 3 turns when revived. |
<!-- GENERATED:END -->

---

## 4. Reserve Team Pictos

### Lune

<!-- GENERATED:START characters:Lune:Pictos -->
| Slot | Pictos           | Level | Stat Bonus            | Effect                                                                  |
|------|------------------|-------|-----------------------|-------------------------------------------------------------------------|
| 1    | Clea's Life      | 30    | Health +5591          | On turn start, if no damage taken since last turn, recover 100% Health. |
| 2    | Sweet Kill       | 31    | Speed +672, Crit +36% | Recover 50% Health on killing an enemy.                                 |
| 3    | Rush On Powerful | 31    | Speed +639, Crit +35% | Apply Rush on applying Powerful.                                        |
<!-- GENERATED:END -->

### Monoco

<!-- GENERATED:START characters:Monoco:Pictos -->
| Slot | Pictos                 | Level | Stat Bonus                  | Effect                                                  |
|------|------------------------|-------|-----------------------------|---------------------------------------------------------|
| 1    | Longer Shell           | 29    | Health +2757, Defence +1572 | On applying Shell, its duration is increased by 2.      |
| 2    | Augmented First Strike | 31    | Speed +1008, Crit +18%      | 50% increased damage on the first hit. Once per battle. |
| 3    | Cheater                | 24    | Health +1198, Speed +400    | Extra turn after using a skill, once per turn           |
<!-- GENERATED:END -->

---

## 5. Main Team Core Lumina Set

<!-- GENERATED:START lumina:core:main -->
**Total: 301 LP** — applied to Maelle, Verso, Sciel.

*Unified core set, applied to all five characters.*

| Lumina             | LP | Effect                                                           | Notes                                                                     |
|--------------------|----|------------------------------------------------------------------|---------------------------------------------------------------------------|
| AP Discount        | 30 | Skills cost 1 less AP.                                           | Reduces skill AP cost by 1.                                               |
| Aegis Revival      | 5  | +1 Shield on being revived.                                      | +1 Shield on being revived.                                               |
| Base Shield        | 20 | Grants 1 Shield HP buffer per turn                               | Grants 1 Shield HP buffer per turn.                                       |
| Breaker            | 10 | 25% increased Break damage.                                      | 25% increased Break damage.                                               |
| Breaking Burn      | 5  | 25% increased Break damage on Burning enemies.                   | 25% increased Break damage on Burning enemies.                            |
| Breaking Death     | 5  | Fully charge enemy break bar on death                            | Fully charge enemy break bar on death.                                    |
| Cheater            | 40 | Extra turn after using a skill, once per turn                    | Extra turn after using a skill, once per turn.                            |
| Critical Break     | 5  | 25% increased Break damage on Critical hits.                     | 25% increased Break damage on Critical hits.                              |
| Dodger             | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                       | Gain 1 AP on Perfect Dodge. Once per turn.                                |
| Energising Start I | 5  | +1 AP on battle start.                                           | +1 AP on battle start. Boosted by Energy Master.                          |
| Energising Turn    | 20 | +1 AP on turn start.                                             | +1 AP on turn start. Main AP flow generator; boosted by Energy Master.    |
| Energy Master      | 40 | Every AP gain is increased by 1                                  | Every AP gain is increased by 1.                                          |
| First Strike       | 10 | Play first.                                                      | Act first in battle.                                                      |
| Painted Power      | 5  | Damage can exceed 9,999.                                         | Damage can exceed 9,999. Essential for all characters from Act 3 onwards. |
| Protecting Death   | 5  | On death, allies gain Shell.                                     | Allies gain Shell on death.                                               |
| Second Chance      | 40 | Revive with 100% Health. Once per battle.                        | Revive with 100% Health. Once per battle.                                 |
| Shielding Death    | 10 | On death, allies gain 3 Shield points.                           | Allies gain 3 Shield points on death.                                     |
| Shortcut           | 5  | Immediately play when falling below 30% Health. Once per battle. | Immediately play when falling below 30% Health. Once per battle.          |
| SOS Power          | 5  | Apply Powerful when falling below 50% Health.                    | Apply Powerful when falling below 50% Health.                             |
| SOS Rush           | 5  | Apply Rush when falling below 50% Health.                        | Apply Rush when falling below 50% Health.                                 |
| SOS Shell          | 5  | Apply Shell when falling below 50% Health.                       | Apply Shell when falling below 50% Health.                                |
| Survivor           | 20 | Survive fatal damage with 1 Health once per battle               | Survive fatal damage with 1 Health, once per battle.                      |
| Teamwork           | 5  | 10% increased damage while all allies are alive.                 | 10% increased damage while all allies are alive.                          |
<!-- GENERATED:END -->

---

## 6. Reserve Team Core Lumina Set

<!-- GENERATED:START lumina:core:reserve -->
**Total: 301 LP** — applied to Lune, Monoco.

*Unified core set, applied to all five characters.*

| Lumina             | LP | Effect                                                           |
|--------------------|----|------------------------------------------------------------------|
| AP Discount        | 30 | Skills cost 1 less AP.                                           |
| Aegis Revival      | 5  | +1 Shield on being revived.                                      |
| Base Shield        | 20 | Grants 1 Shield HP buffer per turn                               |
| Breaker            | 10 | 25% increased Break damage.                                      |
| Breaking Burn      | 5  | 25% increased Break damage on Burning enemies.                   |
| Breaking Death     | 5  | Fully charge enemy break bar on death                            |
| Cheater            | 40 | Extra turn after using a skill, once per turn                    |
| Critical Break     | 5  | 25% increased Break damage on Critical hits.                     |
| Dodger             | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                       |
| Energising Start I | 5  | +1 AP on battle start.                                           |
| Energising Turn    | 20 | +1 AP on turn start.                                             |
| Energy Master      | 40 | Every AP gain is increased by 1                                  |
| First Strike       | 10 | Play first.                                                      |
| Painted Power      | 5  | Damage can exceed 9,999.                                         |
| Protecting Death   | 5  | On death, allies gain Shell.                                     |
| Second Chance      | 40 | Revive with 100% Health. Once per battle.                        |
| Shielding Death    | 10 | On death, allies gain 3 Shield points.                           |
| Shortcut           | 5  | Immediately play when falling below 30% Health. Once per battle. |
| SOS Power          | 5  | Apply Powerful when falling below 50% Health.                    |
| SOS Rush           | 5  | Apply Rush when falling below 50% Health.                        |
| SOS Shell          | 5  | Apply Shell when falling below 50% Health.                       |
| Survivor           | 20 | Survive fatal damage with 1 Health once per battle               |
| Teamwork           | 5  | 10% increased damage while all allies are alive.                 |
<!-- GENERATED:END -->

---

## 7. Character Loadouts

Adjustments each character makes to their team's core Lumina set — exclusions first, then additions.

### Maelle

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
| Frenzy                 | Added  | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Fires on multi-hit skills (Sword Ballet, Burning Canvas) - not on single-hit Stendhal/Gommage.                                                              |
| Glass Cannon           | Added  | 10 | DPS expansion. 25% increased damage, 25% increased damage taken.                                                                                                                                                            |
| Immaculate             | Added  | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                                                                               |
| Warming Up             | Added  | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks. Strong with sustained multi-turn presence.                                                                                                         |
| At Death's Door        | Added  | 5  | Low-health expansion. 50% increased damage below 10% HP. Active permanently while at 1 HP from Last Chance.                                                                                                                 |
| Confident Fighter      | Added  | 15 | Low-health expansion. 30% increased damage, cannot be healed. Conflicts with Sciel's healing - accepted tradeoff for the Low-health build.                                                                                  |
| In Medias Res          | Added  | 10 | Low-health expansion. +3 Shields at battle start, max Health halved. HP penalty irrelevant at 1 HP from Last Chance.                                                                                                        |
| Inverted Affinity      | Added  | 5  | Low-health expansion. 50% increased damage while Inverted (cannot be healed).                                                                                                                                               |
| Anti-Blight            | Added  | 10 | Personal addition. Immune to Blight - relevant for Renoir's Drafts farming.                                                                                                                                                 |
| Burning Shots          | Added  | 3  | Personal addition. 20% chance to Burn on Free Aim shot - seeds Burn Affinity.                                                                                                                                               |
| Exposing Break         | Added  | 5  | Personal addition. Apply Defenceless on Break - supplements Monoco's Defenceless application.                                                                                                                               |
| First Offensive        | Added  | 5  | Personal addition. 50% increased damage on first hit dealt, once per battle.                                                                                                                                                |
| Gradient Fighter       | Added  | 5  | Personal addition. 25% increased damage with Gradient Attacks - large boost for Gommage.                                                                                                                                    |
| Greater Powerful       | Added  | 10 | Personal addition (Lithum suite). +15% to Powerful bonus - boosts Powerful On Shell.                                                                                                                                        |
| Greater Shell          | Added  | 10 | Personal addition (Lithum suite). Stronger Shell from Lithum on Virtuose exit.                                                                                                                                              |
| Longer Powerful        | Added  | 10 | Personal addition (Lithum suite). +2 turn duration to Powerful from Powerful On Shell.                                                                                                                                      |
| Longer Shell           | Added  | 10 | Personal addition (Lithum suite). On applying Shell, duration +2 - extends Lithum Shell from Virtuose exit.                                                                                                                 |
| Marking Shots          | Added  | 3  | Personal addition. 20% chance to apply Mark on Free Aim shot.                                                                                                                                                               |
| Powerful On Shell      | Added  | 10 | Personal addition (Lithum suite). Apply Powerful on applying Shell - Lithum applies Shell on Virtuose exit (Last Chance -> Stendhal/Gommage), triggering this every cycle. Boosted by Greater Powerful and Longer Powerful. |
| Powerful Shield        | Added  | 5  | Personal addition. 10% increased damage per Shield Point on self.                                                                                                                                                           |
| Energising Shell       | Added  | 10 | Personal addition (Lithum suite). Give 2 AP on applying Shell - fires every Virtuose exit via Lithum.                                                                                                                       |
| Empowering Break       | Added  | —  | Free from Pictos.                                                                                                                                                                                                           |
<!-- GENERATED:END -->

### Verso

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

### Sciel

<!-- GENERATED:START characters:Sciel:Lumina:adjustments -->
| Lumina              | Change | LP | Notes                                                                                                                                                                                            |
|---------------------|--------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Breaking Attack     | Added  | 10 | Support expansion. Apply Break damage on base attack if Break bar is full.                                                                                                                       |
| Breaking Counter    | Added  | 3  | Support expansion. 50% increased Break damage on Counterattack.                                                                                                                                  |
| Recovery            | Added  | 10 | Support expansion. Recovers 10% Health on turn start. Passive self-heal - practical substitute for Clea's Life given Sciel spends turns on Fortune's Fury/Intervention rather than self-healing. |
| Accelerating Heal   | Added  | 5  | Personal addition. Healing an ally also applies Rush for 1 turn.                                                                                                                                 |
| Charging Alteration | Added  | 10 | Personal addition. +10% Gradient Charge on applying a Buff, once per turn - fires regularly given Sciel's buff-heavy turns.                                                                      |
| Energising Heal     | Added  | 10 | Personal addition. +2 AP on healing an ally.                                                                                                                                                     |
| Gradient Break      | Added  | 5  | Personal addition. +50% Gradient Charge on Breaking a target - charges Fortune's Fury gauge.                                                                                                     |
| Healing Tint Energy | Added  | 1  | Personal addition. Healing Tints also give 1 AP.                                                                                                                                                 |
| Protecting Heal     | Added  | 5  | Personal addition. Shell on healing an ally.                                                                                                                                                     |
| Powerful Revive     | Added  | —  | Free from Pictos. Apply Powerful for 3 turns when revived - synergy with repeated revives in long boss fights.                                                                                   |
<!-- GENERATED:END -->

### Lune

<!-- GENERATED:START characters:Lune:Lumina:adjustments -->
| Lumina                 | Change | LP | Notes                                                                                                                                                            |
|------------------------|--------|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Augmented First Strike | Added  | 5  | DPS expansion. 50% increased damage on first hit, once per battle.                                                                                               |
| Burn Affinity          | Added  | 10 | DPS expansion. 25% increased damage against burning targets. Burn seeded primarily by Hell as setup skill.                                                       |
| Charging Critical      | Added  | 10 | DPS expansion. +20% Gradient Charge on Critical Hit, once per turn. Fires every turn at 100% crit.                                                               |
| Dead Energy I          | Added  | 2  | DPS expansion. +3 AP on killing an enemy.                                                                                                                        |
| Dead Energy II         | Added  | 2  | DPS expansion. +3 AP on killing an enemy (stacks with Dead Energy I).                                                                                            |
| Double Third           | Added  | 10 | DPS expansion. Every 3rd hit deals double damage. Fires on hits 3/6/9/12 of 12-hit Lightning Dance.                                                              |
| Empowering Dodge       | Added  | 5  | DPS expansion. 5% increased damage per consecutive dodge, stacks to 10. Parry does not reset the stack.                                                          |
| Frenzy                 | Added  | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Major multiplier on 12-hit Lightning Dance with 3-stain consumption (x5 base damage multiplier). |
| Glass Cannon           | Added  | 10 | DPS expansion. 25% increased damage, 25% increased damage taken. Risk mitigated by Clea's Life maintaining full HP each clean turn.                              |
| Immaculate             | Added  | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                    |
| Warming Up             | Added  | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks.                                                                                         |
| Clea's Life            | Added  | —  | Full-health expansion. Free from Pictos. Restore to full Health on turn start if no damage taken.                                                                |
| Full Strength          | Added  | 15 | Full-health expansion. 25% increased damage at full Health. Maintained by Clea's Life restoring full HP each clean turn.                                         |
| Accelerating Heal      | Added  | 5  | Personal addition. Healing an ally also applies Rush for 1 turn.                                                                                                 |
| Breaking Attack        | Added  | 10 | Personal addition. Apply Break damage on base attack if Break bar full.                                                                                          |
| Breaker                | Added  | 10 | Personal addition. 25% increased Break damage - Lune contributes to Break alongside Monoco, accelerating her own Defenceless/Exposing Break window.              |
| Critical Break         | Added  | 5  | Personal addition. 25% increased Break damage on Critical hits.                                                                                                  |
| Energising Burn        | Added  | 10 | Personal addition. +1 AP on applying Burn, once per turn - fires on Hell setup turn.                                                                             |
| Protecting Heal        | Added  | 5  | Personal addition. Shell on healing an ally.                                                                                                                     |
| Sweet Kill             | Added  | —  | Free from Pictos. Recover 50% Health on killing an enemy - synergy with Lightning Dance securing kills, supports Full Strength uptime.                           |
| Rush On Powerful       | Added  | —  | Free from Pictos. Apply Rush on applying Powerful.                                                                                                               |
<!-- GENERATED:END -->

### Monoco

<!-- GENERATED:START characters:Monoco:Lumina:adjustments -->
| Lumina                 | Change | LP | Notes                                                                                     |
|------------------------|--------|----|-------------------------------------------------------------------------------------------|
| Staggering Attack      | Added  | 1  | Break damage on base attack — small break bar contribution                                |
| Break Specialist       | Added  | 1  | 50% increased Break damage, 20% reduced base damage — net positive for break-focused role |
| Energising Break       | Added  | 3  | Extra AP on breaking an enemy                                                             |
| Augmented First Strike | Added  | —  |                                                                                           |
| Empowering Break       | Added  | 3  | 3LP. Gain Powerful on Breaking a target.                                                  |
| Gradient Break         | Added  | 5  | Earn 50% of Gradient Charge when breaking an enemy.                                       |
<!-- GENERATED:END -->

---

## 8. Situational Lumina

Add these as Lumina for specific boss fights — no need to change Pictos.

<!-- GENERATED:START lumina:situational -->
| Lumina           | LP | Effect                                                        | Notes                                                                              |
|------------------|----|---------------------------------------------------------------|------------------------------------------------------------------------------------|
| Anti-Blight      | 10 | Immune to Blight                                              | All characters — vs bosses applying Blight. Add as Lumina; no need to move Pictos. |
| Anti-Burn        | 15 | Immune to Burn                                                | All characters — vs bosses applying Burn regularly.                                |
| Anti-Freeze      | 15 | Immune to Freeze                                              | All characters — vs bosses applying Freeze. LP cost unconfirmed.                   |
| Draining Cleanse | 15 | Consume 1AP to prevent Status Effect application, if possible | Status effect prevention — 1AP cost per use. High LP cost; situational.            |
<!-- GENERATED:END -->

---

## 9. Candidates for Future Review

<!-- GENERATED:START lumina:future -->
| Lumina            | LP | Effect                                                     | Notes                                                                                    |
|-------------------|----|------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Energy Master     | 40 | Every AP gain is increased by 1                            | Game-change but expensive; consider when expanding core set.                             |
| Energising Shell  | 10 | Give 2 AP on applying Shell.                               | Consider for Maelle with Lithum.                                                         |
| Longer Shell      | 5  | On applying Shell, its duration is increased by 2.         | Consider for Maelle with Lithum.                                                         |
| Powerful On Shell | 10 | Apply Powerful on applying Shell.                          | Consider for Maelle with Lithum.                                                         |
| Energising Burn   | 10 | +1 AP on applying Burn. Once per turn.                     | Consider when expanding core set — all characters have Burning Shots so fires regularly. |
| Empowering Dodge  | 5  | 5% increased damage per consecutive dodge, stacks up to 10 | Test empirically before committing — reset on parry unconfirmed.                         |
<!-- GENERATED:END -->

---
