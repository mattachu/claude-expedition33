# Lune — Clair Obscur: Expedition 33

*Last updated: 2026-04-10*

---

## Role

- **Primary role:** DPS + Healer (reserve team)
- **Party position:** Reserve team with Monoco (fallback if main party wiped)
- **Synergies:**
    + Elemental Genesis requires one of each element stain (Fire, Earth, Lightning, Ice)
    + Light stains act as wildcards for any missing element
    + Any two of Wildfire/Terraquake/Thunderfall cover all four elements
    + Kralim Level 10 generates 2 random stains on turn start to accelerate Genesis setup
    + Reserve team role: Lune as DPS + healing, Monoco as break + AP flow

---

## Mechanics

Lune's central system is **stain generation and consumption**. Skills generate stains by element; Elemental Genesis consumes one of each of the four elements (Fire, Earth, Lightning, Ice) for extreme damage. **Light stains act as wildcards** — a Light stain can substitute for any missing element. Maximum 4 stains at once.

**Elemental Genesis stain setup:** Any two of Wildfire (Fire+Light), Terraquake (Earth+Light), Lightning Dance (Lightning+Light) produce 4 stains covering all four elements via the Light wildcard. Kralim Level 10 generates 2 random stains on turn start, giving a head start each turn.

**Kralim Level 4 damage stacking:** Casting a skill increases skill damage of all other elements by +20%. Resets when casting a skill of a previously used element. Encourages varied element usage.

**Stain interactions:**
- Mayhem: consumes ALL stains for damage and Break. Requires 4 stains for Break.
- Healing Light: consumes 2 Earth stains to cost 0 AP.
- Kralim Level 20: +1 AP when Stains are consumed.

---

## Stats

### Level and Attributes

<!-- GENERATED:START characters:Lune:attributes -->
| Attribute | Value |
|-----------|-------|
| Level     | 99    |
| Vitality  | 99    |
| Agility   | 99    |
| Luck      | 51    |
| Might     | 48    |
| Defence   | 0     |
<!-- GENERATED:END -->

### Combat Stats

<!-- GENERATED:START characters:Lune:stats -->
*Stats with Kralim (33), Critical Burn (L25), Burn Affinity (L21), Breaking Death (L29) equipped.*

| Stat    | Base        | Modified |
|---------|-------------|----------|
| Health  | *[unknown]* | 3809     |
| Attack  | *[unknown]* | 11155    |
| Speed   | *[unknown]* | 2691     |
| Defence | *[unknown]* | 182      |
| Crit    | *[unknown]* | 102%     |
<!-- GENERATED:END -->

---

## Weapons

### Current (Endgame)

<!-- GENERATED:START weapons:Lune:Kralim -->
- **Name:** Kralim (33)
- **Power:** 9054
- **Element:** Lightning
- **Scaling:** Agility S, Vitality A
- **Effects:**
    - Level 4: Casting a Skill increases Skill damage of all other elements by +20%. Resets when casting a previously used element.
    - Level 10: On turn start, if no Stains, 2 random Stains generated.
    - Level 20: +1 AP when Stains are consumed.
<!-- GENERATED:END -->
- **Notes:** Required for Elemental Genesis build. Note: If both generated stains are the same element, the duplicate cannot contribute to Elemental Genesis (which requires one of each element) — though it can still be used for other purposes such as Mayhem damage. A Light wildcard stain from a skill mitigates the Genesis-specific gap.

### Previous
<!-- GENERATED:START weapons:Lune:Trebuchim -->
- **Name:** Trebuchim (25)
- **Power:** 3089
- **Element:** Lightning
- **Scaling:** Vitality A, Luck B
- **Effects:**
    - Level 4: 1 random stain on free-aim.
    - Level 10: +1 AP when Stains are consumed.
    - Level 20: Base attack generates 2 random stains.
<!-- GENERATED:END -->
- **Notes:** Stain generation weapon, used with Mayhem. Replaced by Kralim for Genesis build.

### Future Options
<!-- GENERATED:START weapons:Lune:Choralim -->
- **Name:** Choralim (20)
- **Power:** *[unknown]*
- **Element:** Fire
- **Scaling:** Defence A, Agility B
- **Effects:**
    - Level 4: 100% Critical Chance when 4 Stains are simultaneously active.
    - Level 10: 20% increased damage for each consecutive turn without taking damage. Can stack up to 5 times.
    - Level 20: Critical hits apply Burn.
<!-- GENERATED:END -->
- **Notes:** Circular dependency as primary weapon; may serve as crit-maintenance layer once base 100% crit established. Role in endgame build needs clarification.

### Rejected
- **Colim:** Tested Act 2. 14% attack loss; identical AP economy; no free-aim stain generation. Rejected.
- **Trebuchim for Genesis:** Trebuchim's free-aim random stain generation incompatible with precise Genesis element requirements — replaced by Kralim for first two stains plus varied skills for another stain plus a light stain.

---

## Pictos

<!-- GENERATED:START characters:Lune:Pictos -->
| Slot | Pictos           | Level | Stat Bonus            | Effect                                                                  |
|------|------------------|-------|-----------------------|-------------------------------------------------------------------------|
| 1    | Clea's Life      | 30    | Health +5591          | On turn start, if no damage taken since last turn, recover 100% Health. |
| 2    | Sweet Kill       | 31    | Speed +672, Crit +36% | Recover 50% Health on killing an enemy.                                 |
| 3    | Rush On Powerful | 31    | Speed +639, Crit +35% | Apply Rush on applying Powerful.                                        |
<!-- GENERATED:END -->

*Previous Pictos (Longer Shell, Healing Share, Powerful on Shell) replaced Chat 5. Longer Shell moved to Monoco; Healing Share retired.*

*Powerful on Shell fires when Lune casts Healing Light (Shell applied via Protecting Heal Lumina) — cascades to Longer Shell on Monoco and boosts Lune's own damage.*

---

## Lumina

### LP Budget
<!-- GENERATED:START characters:Lune:LP -->
- **Current capacity:** 460 LP
- **Used:** 460 LP
- **Spare:** 0 LP
<!-- GENERATED:END -->

### Lumina Adjustments

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

### Current Loadout

<!-- GENERATED:START characters:Lune:Lumina -->
| Lumina                 | LP | Notes                                                                                                                                                            |
|------------------------|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AP Discount            | 30 | Reduces skill AP cost by 1.                                                                                                                                      |
| Accelerating Heal      | 5  | Personal addition. Healing an ally also applies Rush for 1 turn.                                                                                                 |
| Aegis Revival          | 5  | +1 Shield on being revived.                                                                                                                                      |
| Augmented First Strike | 5  | DPS expansion. 50% increased damage on first hit, once per battle.                                                                                               |
| Base Shield            | 20 | Grants 1 Shield HP buffer per turn.                                                                                                                              |
| Breaker                | 10 | 25% increased Break damage.                                                                                                                                      |
| Breaker                | 10 | Personal addition. 25% increased Break damage - Lune contributes to Break alongside Monoco, accelerating her own Defenceless/Exposing Break window.              |
| Breaking Attack        | 10 | Personal addition. Apply Break damage on base attack if Break bar full.                                                                                          |
| Breaking Burn          | 5  | 25% increased Break damage on Burning enemies.                                                                                                                   |
| Breaking Death         | 5  | Fully charge enemy break bar on death.                                                                                                                           |
| Burn Affinity          | 10 | DPS expansion. 25% increased damage against burning targets. Burn seeded primarily by Hell as setup skill.                                                       |
| Charging Critical      | 10 | DPS expansion. +20% Gradient Charge on Critical Hit, once per turn. Fires every turn at 100% crit.                                                               |
| Cheater                | 40 | Extra turn after using a skill, once per turn.                                                                                                                   |
| Clea's Life            | —  | FREE from Clea's Life Pictos                                                                                                                                     |
| Critical Break         | 5  | 25% increased Break damage on Critical hits.                                                                                                                     |
| Critical Break         | 5  | Personal addition. 25% increased Break damage on Critical hits.                                                                                                  |
| Dead Energy I          | 2  | DPS expansion. +3 AP on killing an enemy.                                                                                                                        |
| Dead Energy II         | 2  | DPS expansion. +3 AP on killing an enemy (stacks with Dead Energy I).                                                                                            |
| Dodger                 | 1  | Gain 1 AP on Perfect Dodge. Once per turn.                                                                                                                       |
| Double Third           | 10 | DPS expansion. Every 3rd hit deals double damage. Fires on hits 3/6/9/12 of 12-hit Lightning Dance.                                                              |
| Empowering Dodge       | 5  | DPS expansion. 5% increased damage per consecutive dodge, stacks to 10. Parry does not reset the stack.                                                          |
| Energising Burn        | 10 | Personal addition. +1 AP on applying Burn, once per turn - fires on Hell setup turn.                                                                             |
| Energising Start I     | 5  | +1 AP on battle start. Boosted by Energy Master.                                                                                                                 |
| Energising Turn        | 20 | +1 AP on turn start. Main AP flow generator; boosted by Energy Master.                                                                                           |
| Energy Master          | 40 | Every AP gain is increased by 1.                                                                                                                                 |
| First Strike           | 10 | Act first in battle.                                                                                                                                             |
| Frenzy                 | 20 | DPS expansion. Each successive Skill hit deals 10% more damage. Major multiplier on 12-hit Lightning Dance with 3-stain consumption (x5 base damage multiplier). |
| Full Strength          | 15 | Full-health expansion. 25% increased damage at full Health. Maintained by Clea's Life restoring full HP each clean turn.                                         |
| Glass Cannon           | 10 | DPS expansion. 25% increased damage, 25% increased damage taken. Risk mitigated by Clea's Life maintaining full HP each clean turn.                              |
| Immaculate             | 10 | DPS expansion. 30% increased damage until first hit received.                                                                                                    |
| Painted Power          | 5  | Damage can exceed 9,999. Essential for all characters from Act 3 onwards.                                                                                        |
| Protecting Death       | 5  | Allies gain Shell on death.                                                                                                                                      |
| Protecting Heal        | 5  | Personal addition. Shell on healing an ally.                                                                                                                     |
| Rush On Powerful       | —  | FREE from Rush On Powerful Pictos                                                                                                                                |
| SOS Power              | 5  | Apply Powerful when falling below 50% Health.                                                                                                                    |
| SOS Rush               | 5  | Apply Rush when falling below 50% Health.                                                                                                                        |
| SOS Shell              | 5  | Apply Shell when falling below 50% Health.                                                                                                                       |
| Second Chance          | 40 | Revive with 100% Health. Once per battle.                                                                                                                        |
| Shielding Death        | 10 | Allies gain 3 Shield points on death.                                                                                                                            |
| Shortcut               | 5  | Immediately play when falling below 30% Health. Once per battle.                                                                                                 |
| Survivor               | 20 | Survive fatal damage with 1 Health, once per battle.                                                                                                             |
| Sweet Kill             | —  | FREE from Sweet Kill Pictos                                                                                                                                      |
| Teamwork               | 5  | 10% increased damage while all allies are alive.                                                                                                                 |
| Warming Up             | 15 | DPS expansion. Damage increases with each attack, up to 20% at 5 stacks.                                                                                         |
<!-- GENERATED:END -->

---

## Skills

<!-- GENERATED:START characters:Lune:skills -->
**Currently equipped (6):** Elemental Genesis, Healing Light, Hell, Lightning Dance, Terraquake, Thermal Transfer

| Skill             | AP | Stains Generated     | Equipped | Notes                                                                                                                                                                         |
|-------------------|----|----------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Elemental Genesis | 4  | —                    | ✅        | Extreme damage to all enemies, 8 hits. Each hit deals random element damage. Requires Lightning, Earth, Fire and Ice Stains.                                                  |
| Healing Light     | 3  | Light                | ✅        | Heals targeted ally 30–50% HP and dispels all status effects. Consumes Earth Stain ×2 for 0 AP cost. Generates Light Stain.                                                   |
| Hell              | 9  | Fire, Light          | ✅        | Very high Fire AoE, 2 hits. Applies 5 Burn per hit. Deals self-damage if failed. Consumes Ice, Earth and Lightning Stains for greatly increased damage (×3).                  |
| Lightning Dance   | 7  | Lightning, Light     | ✅        | Very high single-target Lightning damage, 6 hits. Crits trigger an additional hit. Consumes Earth, Ice and Fire Stains for greatly increased damage (×5).                     |
| Terraquake        | 5  | Earth, Light         | ✅        | Earth AoE + deals Earth and Break damage to all enemies every turn for 3 turns. Increases all Break damage received by 50%. Consumes Lightning Stain ×2 to extend to 5 turns. |
| Thermal Transfer  | 2  | Ice                  | ✅        | Low single-target Ice damage, 2 hits. Gains 4 AP if target is Burning. Consumes Earth Stain ×2: Play a second turn.                                                           |
| Crustal Crush     | 7  | Earth, Light         | ❌        | High single-target Earth damage + Break damage, 5 hits. Consumes Lightning Stain ×2 for increased damage (×3).                                                                |
| Earth Rising      | 3  | Earth                | ❌        | Low Earth AoE, 1 hit. Consumes Lightning Stain for increased damage (×1.5).                                                                                                   |
| Electrify         | 1  | Lightning, Lightning | ❌        | Low single-target Lightning damage, 3 hits. Crits trigger an additional hit. Consumes Fire Stain to generate Light Stain.                                                     |
| Elemental Trick   | 3  | —                    | ❌        | Low single-target Ice, Fire, Lightning, and Earth damage, 4 hits. Critical hits generate the corresponding Stain.                                                             |
| Fire Rage         | 5  | Fire, Light          | ❌        | Increasingly high Fire AoE every turn until Lune receives damage. Stuns itself if interrupted. Consumes Ice Stain ×2 for increased damage (×2).                               |
| Ice Lance         | 4  | Ice, Light           | ❌        | Medium single-target Ice damage, 1 hit. Slows target 3 turns. Consumes Earth Stain for increased damage (×1.5).                                                               |
| Immolation        | 2  | Fire                 | ❌        | Low single-target Fire damage, 1 hit. Applies 3 Burn. Applies 2 more Burn if target is Marked. Consumes Ice Stain for increased damage (×1.5).                                |
| Mayhem            | 3  | —                    | ❌        | Consumes all Stains to deal high elemental damage, 1–4 hits. Can Break if 4 Stains consumed.                                                                                  |
| Rebirth           | 5  | Light                | ❌        | Revives an ally with 30–70% Health and 2 AP. Consumes Lightning Stain ×3 for 0 AP cost.                                                                                       |
| Revitalisation    | 5  | Light                | ❌        | Heals 1–3 allies 40–60% Health. Consumes Fire Stain ×3 to also apply Regen for 3 turns.                                                                                       |
| Rockslide         | 5  | Earth, Light         | ❌        | Medium single-target Earth damage, 2 hits. Can Break. Consumes Lightning, Ice and Fire Stains for greatly increased damage (×5).                                              |
| Thunderfall       | 5  | Lightning, Light     | ❌        | Medium Lightning damage to random enemies, 2–6 hits. Crits trigger an additional hit. Consumes Fire Stain for increased damage (×1.5).                                        |
| Wildfire          | 4  | Fire, Light          | ❌        | Medium Fire AoE, 1 hit. Applies 3 Burn. Consumes Ice Stain ×2 for increased damage (×2).                                                                                      |
| Typhoon           | 8  | Ice, Light           | ❌        | Ice AoE + on turn start deals high Ice damage to all enemies and heals allies 20% HP for 3 turns. Consumes Earth Stain ×2 to extend to 5 turns.                               |
<!-- GENERATED:END -->

---

## Gradient Skills

<!-- GENERATED:START characters:Lune:gradients -->
| Gradient Skill | Gradient Cost | Acquired | Notes                                                                    |
|----------------|---------------|----------|--------------------------------------------------------------------------|
| Tremor         | 1             | ✅        | High Earth damage to all enemies and removes all enemies' Shields.       |
| Tree of Life   | 2             | ✅        | Heals party and removes ALL status effects.                              |
| Sky Break      | 3             | ✅        | Extreme damage to all enemies using element with most stains. Can Break. |
<!-- GENERATED:END -->

---

## Build Options

| Build                | Role              | Key Skills                                                                  | Key Weapon | Status   | Notes                                                                                             |
|----------------------|-------------------|-----------------------------------------------------------------------------|------------|----------|---------------------------------------------------------------------------------------------------|
| Mayhem               | DPS / healer      | Mayhem, Wildfire, Crustal Crush, Thunderfall, Healing Light, Rebirth        | Trebuchim  | Previous | Use Trebuchim + skills to generate stains, Mayhem for damage + break. Heavily used in Acts 1 & 2. |
| Elemental Genesis    | DPS / healer      | Hell, Terraquake, Lightning Dance, Elemental Genesis, Mayhem, Healing Light | Kralim     | Current  | Vitality 99, Agility 99, Luck 30. Reserve team role.                                              |

### Simon fight

**Party position:** Main team (Team 1) with Verso and Lune.

**Lumina changes:** Base Shield not in reserve team core — no change needed.

**Skills changes (from standard):**
- Swap: Mayhem → Rebirth (better utility in boss fight; Mayhem less effective in 1v1)
- Note: Lightning Dance → Ice Lance swap was applied in Chat 22 for Simon (Ice Lance applies Slow, useful for turn order control)

**Current equipped:** Hell, Terraquake, Ice Lance, Healing Light, Rebirth, Elemental Genesis

**Role in Simon Phase 3:** Elemental Genesis for damage; Ice Lance to apply Slow on Simon; Healing Light for party sustain; Rebirth to revive fallen allies. Lune contributes AP generation for Verso via Overload if Verso is active. Healing less effective given Simon's high damage output.

**Revert after Simon:** Swap Ice Lance → Lightning Dance; swap Rebirth → Mayhem (or reassess — Rebirth may be worth keeping permanently).

---

## Key Decisions

- **Trebuchim over Colim:** Tested and confirmed. 14% attack loss with Colim, identical AP economy, no stain generation on free-aim. Trebuchim optimal for prior playstyle.
- **Kralim over Trebuchim:** Kralim required for Elemental Genesis build. Respec to Vitality 99 / Agility 99 completed Chat 5.
- **Burn Affinity over Warming Up for Pictos:** Warming Up takes 5 turns to reach 25% damage cap — too slow for reserve entry. Burn Affinity fires immediately from turn 1 via Wildfire.
- **Burning Death over Sniper as third Pictos:** Higher Crit (+24% vs +13%) and useful on-death burn effect more relevant for Lune's role than Sniper's Speed advantage.
- **Protecting Heal added:** Activates Shell on every Healing Light cast, enabling Longer Shell extension on Monoco and Powerful on Shell bonus for Lune.

---

## Errors to Avoid

- **Colim recommendation:** Recommended over Trebuchim based on Light stain wildcards and community meta. Wrong for this playstyle. Root cause: didn't simulate turns, didn't check playstyle assumptions.
- **Trebuchim AP economy:** Initially implied +1 AP per individual stain consumed. Correct: +1 AP per consumption event. Mayhem consuming 4 stains = +1 AP total.
- **Colim AP economy:** Same error. Colim Level 10 gives +1 AP when Light stains consumed — also per consumption event, not per stain.
- **Revitalization removes status effects:** Said it does. Correct: heals only. Only Healing Light and Tree of Life remove status.
- **Tree of Life gradient cost:** Said 1 Gradient charge. Correct: 2 Gradient charges.
- **Energising Cleanse confabulated:** Initially said it didn't exist. Correct: it exists. Effect: dispels first negative status received + grants 2 AP, once per battle.
- **Elemental Genesis + Trebuchim compatibility:** Incompatible. Trebuchim generates random stains; Genesis requires exactly 1 of each element.
- **Mayhem break condition:** Needs 4 stains consumed to Break. With only 2–3 stains, Mayhem deals damage but cannot Break.
- **Choralim as primary Elemental Trick weapon:** Circular dependency — gives 100% crit only when 4 stains already active. Cannot be the stain-generation weapon. Base 100% crit must come from Luck + Pictos independently.
- **Protecting Tint fires on skill heals:** Incorrect. Protecting Tint fires on Tint use only, not on skill heals like Healing Light. Protecting Heal Lumina fires on skill heals.
