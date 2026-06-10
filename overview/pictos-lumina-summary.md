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
| Slot | Pictos           | Level | Stat Bonus            | Effect                                                                  |
|------|------------------|-------|-----------------------|-------------------------------------------------------------------------|
| 1    | Clea's Life      | 30    | Health +5591          | On turn start, if no damage taken since last turn, recover 100% Health. |
| 2    | Empowering Break | 28    | Speed +546, Crit +32% | Gain Powerful on Breaking a target.                                     |
| 3    | Shortcut         | 31    | Speed +672, Crit +36% | Immediately play when falling below 30% Health. Once per battle.        |
<!-- GENERATED:END -->

### Verso

<!-- GENERATED:START characters:Verso:Pictos -->
| Slot | Pictos               | Level | Stat Bonus              | Effect                                                               |
|------|----------------------|-------|-------------------------|----------------------------------------------------------------------|
| 1    | Second Chance        | 31    | Health +3981, Crit +15% | Revive with 100% Health. Once per battle.                            |
| 2    | Sweet Kill           | 31    | Speed +672, Crit +36%   | Recover 50% Health on killing an enemy.                              |
| 3    | Alternating Critical | 29    | Speed +293, Crit +50%   | On Critical hit, 100% increased damage of the next non-Critical hit. |
<!-- GENERATED:END -->

### Sciel

<!-- GENERATED:START characters:Sciel:Pictos -->
| Slot | Pictos              | Level | Stat Bonus              | Effect                                       |
|------|---------------------|-------|-------------------------|----------------------------------------------|
| 1    | Augmented Counter I | 28    | Health +4058, Crit +16% | 25% increased Counterattack damage.          |
| 2    | Energising Shots    | 28    | Speed +779, Crit +16%   | 20% chance to gain 1 AP on Free Aim shot.    |
| 3    | Painter             | 28    | Speed +519, Crit +31%   | Converts all Physical damage to Void damage. |
<!-- GENERATED:END -->

---

## 4. Reserve Team Pictos

### Lune

<!-- GENERATED:START characters:Lune:Pictos -->
| Slot | Pictos         | Level | Stat Bonus            | Effect                                     |
|------|----------------|-------|-----------------------|--------------------------------------------|
| 1    | Critical Burn  | 25    | Speed +434, Crit +28% | 25% increased Crit rate on Burning enemies |
| 2    | Burn Affinity  | 21    | Speed +439, Crit +12% | 25% increased damage on Burning targets    |
| 3    | Breaking Death | 29    | Speed +586, Crit +33% | Fully charge enemy break bar on death      |
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
**Total: 246 LP** — applied to Maelle, Verso, Sciel.

*Applied via in-game Lumina set.*

| Lumina             | LP | Effect                                                           | Notes                                                                                             |
|--------------------|----|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Painted Power      | 5  | Damage can exceed 9,999.                                         | Essential for all characters from Act 3 onwards                                                   |
| Energising Turn    | 20 | +1 AP on turn start.                                             | Main AP flow generator; boosted by Energy Master                                                  |
| Cheater            | 40 | Extra turn after using a skill, once per turn                    | Essential for endgame builds                                                                      |
| Energy Master      | 40 | Every AP gain is increased by 1                                  | Add 1 to AP boosts (not double) — game-changing for AP generation                                 |
| Second Chance      | 40 | Revive with 100% Health. Once per battle.                        | Can save boss battles                                                                             |
| Survivor           | 20 | Survive fatal damage with 1 Health once per battle               | Secondary safety net before Second Chance                                                         |
| Base Shield        | 20 | Grants 1 Shield HP buffer per turn                               | Verso: previously non-functional with Chevalam L4; now available with Simoso — see open question. |
| Teamwork           | 5  | 10% increased damage while all allies are alive.                 |                                                                                                   |
| Energising Start I | 5  | +1 AP on battle start.                                           | Boosted by Energy Master to 8AP on battle start                                                   |
| Dodger             | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                       |                                                                                                   |
| Breaker            | 10 | 25% increased Break damage.                                      | Main break damage booster                                                                         |
| Dead Energy I      | 2  | +3 AP on killing an enemy.                                       |                                                                                                   |
| Dead Energy II     | 2  | +3 AP on killing an enemy.                                       |                                                                                                   |
| Breaking Death     | 5  | Fully charge enemy break bar on death                            | Extremely helpful in tough boss fights                                                            |
| Critical Break     | 5  | 25% increased Break damage on Critical hits.                     |                                                                                                   |
| Burning Shots      | 3  | 20% chance to Burn on Free Aim shot.                             |                                                                                                   |
| Breaking Burn      | 5  | 25% increased Break damage on Burning enemies.                   |                                                                                                   |
| Breaking Counter   | 3  | 50% increased Break damage on Counterattack.                     |                                                                                                   |
| Shortcut           | 5  | Immediately play when falling below 30% Health. Once per battle. |                                                                                                   |
| Anti-Blight        | 10 | Immune to Blight                                                 | Especially important in Renoir's Drafts                                                           |
<!-- GENERATED:END -->

---

## 6. Reserve Team Core Lumina Set

<!-- GENERATED:START lumina:core:reserve -->
**Total: 202 LP** — applied to Lune, Monoco.

*Main team core minus Dead Energy I, Dead Energy II, Energy Master, Anti-Blight; plus Recovery.*

| Lumina             | LP | Effect                                                           |
|--------------------|----|------------------------------------------------------------------|
| Painted Power      | 5  | Damage can exceed 9,999.                                         |
| Energising Turn    | 20 | +1 AP on turn start.                                             |
| Cheater            | 40 | Extra turn after using a skill, once per turn                    |
| Shortcut           | 5  | Immediately play when falling below 30% Health. Once per battle. |
| Survivor           | 20 | Survive fatal damage with 1 Health once per battle               |
| Recovery           | 10 | Recovers 10% Health on turn start.                               |
| Teamwork           | 5  | 10% increased damage while all allies are alive.                 |
| Energising Start I | 5  | +1 AP on battle start.                                           |
| Dodger             | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                       |
| Breaker            | 10 | 25% increased Break damage.                                      |
| Critical Break     | 5  | 25% increased Break damage on Critical hits.                     |
| Burning Shots      | 3  | 20% chance to Burn on Free Aim shot.                             |
| Breaking Burn      | 5  | 25% increased Break damage on Burning enemies.                   |
| Breaking Counter   | 3  | 50% increased Break damage on Counterattack.                     |
| Breaking Death     | 5  | Fully charge enemy break bar on death                            |
| Base Shield        | 20 | Grants 1 Shield HP buffer per turn                               |
| Second Chance      | 40 | Revive with 100% Health. Once per battle.                        |
<!-- GENERATED:END -->

---

## 7. Character Loadouts

Adjustments each character makes to their team's core Lumina set — exclusions first, then additions.

### Maelle

<!-- GENERATED:START characters:Maelle:Lumina:adjustments -->
| Lumina                 | Change | LP | Notes                                                                                                                                                                |
|------------------------|--------|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Full Strength          | Added  | 15 | Damage bonus while on full HP — strong synergy with Clea's Life Pictos                                                                                               |
| Warming Up             | Added  | 15 | Damage bonus that increases with each attack, up to 20% at 5 stacks — strong synergy with multi-hit skills and Clea's Life Pictos enabling long uptime on this bonus |
| Gradient Fighter       | Added  | 5  | Damage bonus on Gradient Skill use. 5LP. Verify exact effect description in-game.                                                                                    |
| Solo Fighter           | Added  | 1  | Rounds up LP to cap.                                                                                                                                                 |
| Energising Break       | Added  | 3  | 3LP. +3 AP on Breaking a target.                                                                                                                                     |
| Augmented First Strike | Added  | 5  | 5LP. 50% increased damage on the first hit, once per battle.                                                                                                         |
| Greater Powerful       | Added  | 10 | 10LP. +15% to Powerful damage increase.                                                                                                                              |
| Charging Critical      | Added  | 10 | 10LP. +20% Gradient Charge on Critical Hit, once per turn.                                                                                                           |
<!-- GENERATED:END -->

### Verso

<!-- GENERATED:START characters:Verso:Lumina:adjustments -->
| Lumina                 | Change   | LP | Notes                                                           |
|------------------------|----------|----|-----------------------------------------------------------------|
| Second Chance          | Excluded | 40 | Free from Second Chance Pictos                                  |
| Sweet Kill             | Excluded | 5  | Free from Sweet Kill Pictos                                     |
| Survivor               | Excluded | 20 | Not used in current build                                       |
| Energising Start I     | Excluded | 5  | Not used in current build                                       |
| Burning Shots          | Excluded | 3  | Not used in current build                                       |
| Breaking Counter       | Excluded | 3  | Not used in current build                                       |
| Anti-Blight            | Excluded | 10 | Not used in current build                                       |
| AP Discount            | Added    | 30 | 30LP. Reduces skill AP cost by 1.                               |
| Alternating Critical   | Added    | —  | Free from Alternating Critical Pictos.                          |
| At Death's Door        | Added    | 5  | 5LP. 50% increased damage below 10% HP.                         |
| Augmented First Strike | Added    | 5  | 5LP. 50% increased damage on first hit, once per battle.        |
| Auto Rush              | Added    | 10 | 10LP. Apply Rush for 3 turns on battle start.                   |
| Burn Affinity          | Added    | 10 | 10LP. 25% increased damage against burning targets.             |
| Charging Critical      | Added    | 10 | 10LP. +20% Gradient Charge on Critical Hit, once per turn.      |
| Confident Fighter      | Added    | 15 | 15LP. 30% increased damage, can't be healed.                    |
| Double Third           | Added    | 10 | 10LP. Third hit in a sequence deals double damage.              |
| Energising Break       | Added    | 3  | 3LP. +3 AP on Breaking a target.                                |
| First Strike           | Added    | 10 | 10LP. Act first in battle.                                      |
| Frenzy                 | Added    | 20 | 20LP. Each successive hit increases damage by 10%.              |
| Warming Up             | Added    | 15 | 15LP. Damage increases with each attack, up to 20% at 5 stacks. |
<!-- GENERATED:END -->

### Sciel

<!-- GENERATED:START characters:Sciel:Lumina:adjustments -->
| Lumina              | Change   | LP | Notes                                                    |
|---------------------|----------|----|----------------------------------------------------------|
| Energy Master       | Excluded | 40 | Not used — Augmented Counter I Pictos prioritised        |
| Dead Energy II      | Excluded | 2  | Not used in current build                                |
| Burning Shots       | Excluded | 3  | Not used in current build                                |
| Anti-Blight         | Excluded | 10 | Not used in current build                                |
| AP Discount         | Added    | 30 | 30LP. Reduces skill AP cost by 1.                        |
| Accelerating Heal   | Added    | 5  | 5LP. Rush on healing an ally.                            |
| Augmented Counter I | Added    | —  | Free from Augmented Counter I Pictos.                    |
| Breaking Attack     | Added    | 10 | 10LP. Apply Break damage on base attack.                 |
| Charging Alteration | Added    | 10 | 10LP. +20% Gradient Charge on applying buffs or debuffs. |
| Energising Heal     | Added    | 10 | 10LP. +2 AP on healing an ally.                          |
| Energising Shots    | Added    | —  | Free from Energising Shots Pictos.                       |
| First Strike        | Added    | 10 | 10LP. Act first in battle.                               |
| Gradient Break      | Added    | 5  | 5LP. +50% Gradient Charge on Breaking.                   |
| Healing Tint Energy | Added    | 1  | 1LP. +1 AP on Healing Tint use.                          |
| Painter             | Added    | —  | Free from Painter Pictos.                                |
| Protecting Heal     | Added    | 5  | 5LP. Shell on healing an ally.                           |
| Recovery            | Added    | 10 | 10LP. Passive heal on turn start.                        |
<!-- GENERATED:END -->

### Lune

<!-- GENERATED:START characters:Lune:Lumina:adjustments -->
| Lumina            | Change   | LP | Notes                                                                         |
|-------------------|----------|----|-------------------------------------------------------------------------------|
| Breaking Death    | Excluded | 5  | Free from Breaking Death Pictos                                               |
| Survivor          | Excluded | 20 | Not used in current build                                                     |
| Breaker           | Excluded | 10 | Not used in current build                                                     |
| Critical Break    | Excluded | 5  | Not used in current build                                                     |
| Burning Shots     | Excluded | 3  | Not used in current build                                                     |
| Breaking Counter  | Excluded | 3  | Not used in current build                                                     |
| Recovery          | Excluded | 10 | Not used in current build                                                     |
| AP Discount       | Added    | 30 | 30LP. Reduces skill AP cost by 1.                                             |
| Accelerating Heal | Added    | 5  | 5LP. Rush on healing an ally.                                                 |
| Breaking Attack   | Added    | 10 | 10LP. Apply Break damage on base attack.                                      |
| Burn Affinity     | Added    | —  | Free from Burn Affinity Pictos. 25% increased damage against burning targets. |
| Critical Burn     | Added    | —  | Free from Critical Burn Pictos. 25% increased crit chance on burning targets. |
| Energy Master     | Added    | 40 | 40LP. +5 AP on turn start.                                                    |
| Dead Energy I     | Added    | 2  | 2LP. +2 AP on death of an ally.                                               |
| Dead Energy II    | Added    | 2  | 2LP. +2 AP on death of an ally (stacks with Dead Energy I).                   |
| Energising Burn   | Added    | 10 | 10LP. +1 AP on applying Burn, once per turn.                                  |
| First Strike      | Added    | 10 | 10LP. Act first in battle.                                                    |
| Protecting Heal   | Added    | 5  | 5LP. Shell on healing an ally.                                                |
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
