# Clair Obscur: Expedition 33 — Pictos and Lumina Summary

*Generated from `pictos-lumina.json`.*

See [`pictos-lumina-catalogue.md`](pictos-lumina-catalogue.md) for the full list of all 194 Pictos.

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

**In-game Lumina Sets:** The game allows saving up to 50 Lumina Sets per character. Sets apply a group of Lumina in one action. The recommended workflow is: apply core set first, then add character-specific extras on top.

---

## 3. Main Team Pictos

### Maelle

<!-- GENERATED:START characters:Maelle:Pictos -->
| Slot | Pictos           | Level | Stat Bonus            | Effect                                                                  |
|------|------------------|-------|-----------------------|-------------------------------------------------------------------------|
| 1    | Clea's Life      | 30    | Health +5591          | On turn start, if no damage taken since last turn, recover 100% Health. |
| 2    | Empowering Break | 28    | Speed +546, Crit +32% | Gain Powerful on Breaking a target.                                     |
| 3    | Gradient Break   | 25    | Speed +434, Crit +28% | +50% of a Gradient Charge on Breaking a target.                         |
<!-- GENERATED:END -->

### Verso

<!-- GENERATED:START characters:Verso:Pictos -->
| Slot | Pictos              | Level | Stat Bonus              | Effect                                     |
|------|---------------------|-------|-------------------------|--------------------------------------------|
| 1    | Augmented Counter I | 28    | Health +4058, Crit +16% | 25% increased Counterattack damage.        |
| 2    | Breaking Death      | 29    | Speed +586, Crit +33%   | Fully charge enemy break bar on death      |
| 3    | Confident           | 29    | Speed +557, Crit +32%   | Take 50% less damage, but can't be healed. |
<!-- GENERATED:END -->

### Sciel

<!-- GENERATED:START characters:Sciel:Pictos -->
| Slot | Pictos           | Level | Stat Bonus            | Effect                                       |
|------|------------------|-------|-----------------------|----------------------------------------------|
| 1    | Painter          | 28    | Speed +519, Crit +31% | Converts all Physical damage to Void damage. |
| 2    | Energy Master    | 30    | Health +4979          | Every AP gain is increased by 1              |
| 3    | Energising Shots | 28    | Speed +779, Crit +16% | 20% chance to gain 1 AP on Free Aim shot.    |
<!-- GENERATED:END -->

---

## 4. Reserve Team Pictos

### Lune

<!-- GENERATED:START characters:Lune:Pictos -->
| Slot | Pictos        | Level | Stat Bonus            | Effect                                     |
|------|---------------|-------|-----------------------|--------------------------------------------|
| 1    | Critical Burn | 25    | Speed +434, Crit +28% | 25% increased Crit rate on Burning enemies |
| 2    | Burn Affinity | 21    | Speed +439, Crit +12% | 25% increased damage on Burning targets    |
| 3    | Burning Death | 28    | Speed +546, Crit +32% | Apply 3 Burn to all enemies on death       |
<!-- GENERATED:END -->

### Monoco

<!-- GENERATED:START characters:Monoco:Pictos -->
| Slot | Pictos          | Level | Stat Bonus                  | Effect                                             |
|------|-----------------|-------|-----------------------------|----------------------------------------------------|
| 1    | Longer Shell    | 29    | Health +2757, Defence +1572 | On applying Shell, its duration is increased by 2. |
| 2    | Powerful Mark   | 28    | Speed +819, Crit +16%       | Gain Powerful on hitting a Marked target.          |
| 3    | Powerful Revive | 28    | Speed +546, Crit +32%       | Apply Powerful for 3 turns when revived.           |
<!-- GENERATED:END -->

---

## 5. Main Team Core Lumina Set

<!-- GENERATED:START lumina:core:main -->
**Total: 234 LP** — applied to Maelle, Verso, Sciel.

*Applied via in-game Lumina set.*

| Lumina             | LP | Effect                                                     | Notes                                                             |
|--------------------|----|------------------------------------------------------------|-------------------------------------------------------------------|
| Painted Power      | 5  | Damage can exceed 9,999.                                   | Essential for all characters from Act 3 onwards                   |
| Teamwork           | 5  | 10% increased damage while all allies are alive.           |                                                                   |
| Base Shield        | 20 | Grants 1 Shield HP buffer per turn                         | Verso: non-functional with Chevalam as L4 effect prevents shields |
| Energising Turn    | 20 | +1 AP on turn start.                                       | Main AP flow generator; boosted by Energy Master                  |
| Cheater            | 40 | Extra turn after using a skill, once per turn              |                                                                   |
| Energy Master      | 40 | Every AP gain is increased by 1                            |                                                                   |
| Second Chance      | 40 | Revive with 100% Health. Once per battle.                  |                                                                   |
| Energising Parry   | 15 | +1 AP on successful Parry.                                 |                                                                   |
| Energising Start I | 5  | +1 AP on battle start.                                     |                                                                   |
| Dodger             | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                 |                                                                   |
| Breaker            | 10 | 25% increased Break damage.                                |                                                                   |
| Marking Shots      | 3  | 20% chance to apply Mark on Free Aim shot.                 |                                                                   |
| Dead Energy I      | 2  | +3 AP on killing an enemy.                                 |                                                                   |
| Dead Energy II     | 2  | +3 AP on killing an enemy.                                 |                                                                   |
| Critical Break     | 5  | 25% increased Break damage on Critical hits.               |                                                                   |
| Rewarding Mark     | 5  | +2 AP on dealing damage to a Marked target. Once per turn. |                                                                   |
| Burning Shots      | 3  | 20% chance to Burn on Free Aim shot.                       |                                                                   |
| Breaking Burn      | 5  | 25% increased Break damage on Burning enemies.             |                                                                   |
| Breaking Counter   | 3  | 50% increased Break damage on Counterattack.               |                                                                   |
| Breaking Death     | 5  | Fully charge enemy break bar on death                      |                                                                   |
<!-- GENERATED:END -->

---

## 6. Reserve Team Core Lumina Set

<!-- GENERATED:START lumina:core:reserve -->
**Total: 120 LP** — applied to Lune, Monoco.

*Main team core minus Cheater, Dead Energy I, Dead Energy II, Second Chance; Plus Recovery.*

| Lumina             | LP | Effect                                                     |
|--------------------|----|------------------------------------------------------------|
| Painted Power      | 5  | Damage can exceed 9,999.                                   |
| Teamwork           | 5  | 10% increased damage while all allies are alive.           |
| Base Shield        | 20 | Grants 1 Shield HP buffer per turn                         |
| Energising Turn    | 20 | +1 AP on turn start.                                       |
| Recovery           | 10 | Recovers 10% Health on turn start.                         |
| Energising Parry   | 15 | +1 AP on successful Parry.                                 |
| Energising Start I | 5  | +1 AP on battle start.                                     |
| Dodger             | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                 |
| Breaker            | 10 | 25% increased Break damage.                                |
| Marking Shots      | 3  | 20% chance to apply Mark on Free Aim shot.                 |
| Critical Break     | 5  | 25% increased Break damage on Critical hits.               |
| Rewarding Mark     | 5  | +2 AP on dealing damage to a Marked target. Once per turn. |
| Burning Shots      | 3  | 20% chance to Burn on Free Aim shot.                       |
| Breaking Burn      | 5  | 25% increased Break damage on Burning enemies.             |
| Breaking Counter   | 3  | 50% increased Break damage on Counterattack.               |
| Breaking Death     | 5  | Fully charge enemy break bar on death                      |
<!-- GENERATED:END -->

---

## 7. Situational Lumina

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

## 8. Candidates for Future Review

<!-- GENERATED:START lumina:future -->
| Lumina            | LP | Effect                                                     | Notes                                                                                    |
|-------------------|----|------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Energy Master     | 40 | Every AP gain is increased by 1                            | Game-change but expensive; consider when expanding core set.                             |
| Healing Boon      | 10 | Heal 15% HP on applying a buff                             | Consider for Sciel with Litheson.                                                        |
| Energising Shell  | 10 | Give 2 AP on applying Shell.                               | Consider for Maelle with Lithum.                                                         |
| Longer Shell      | 5  | On applying Shell, its duration is increased by 2.         | Consider for Maelle with Lithum.                                                         |
| Powerful On Shell | 10 | Apply Powerful on applying Shell.                          | Consider for Maelle with Lithum.                                                         |
| Energising Burn   | 10 | +1 AP on applying Burn. Once per turn.                     | Consider when expanding core set — all characters have Burning Shots so fires regularly. |
| Empowering Dodge  | 5  | 5% increased damage per consecutive dodge, stacks up to 10 | Test empirically before committing — reset on parry unconfirmed.                         |
<!-- GENERATED:END -->

---
