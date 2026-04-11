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

## Current Stats

### Level and Attributes

<!-- GENERATED:START characters:Lune:attributes -->
| Attribute | Value | Priority  |
|-----------|-------|-----------|
| Level     | 78    | —         |
| Vitality  | 99    | Primary   |
| Agility   | 99    | Primary   |
| Luck      | 36    | Secondary |
| Might     | 0     | None      |
| Defence   | 0     | None      |
<!-- GENERATED:END -->

### Combat Stats

<!-- GENERATED:START characters:Lune:stats -->
*Stats with Kralim (29), Powerful On Shell (23), Burn Affinity (21), Burning Death (21) equipped*

| Stat    | Base        | Modified |
|---------|-------------|----------|
| Health  | *[unknown]* | 4047     |
| Attack  | *[unknown]* | 5401     |
| Speed   | *[unknown]* | 1797     |
| Defence | *[unknown]* | 1056     |
| Crit    | *[unknown]* | 84%      |
<!-- GENERATED:END -->

---

## Weapons

### Current (Endgame)

<!-- GENERATED:START weapons:Lune:Kralim -->
- **Name:** Kralim (29)
- **Power:** 4454
- **Element:** *[unknown]*
- **Scaling:** Vitality A, Agility B
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
    - Level 10: *[unknown]*
    - Level 20: Base attack generates 2 random stains.
<!-- GENERATED:END -->
- **Notes:** Stain generation weapon, used with Mayhem. Replaced by Kralim for Genesis build.

### Future Options
<!-- GENERATED:START weapons:Lune:Choralim -->
- **Name:** Choralim (20)
- **Power:** *[unknown]*
- **Element:** *[unknown]*
- **Scaling:** *[unknown]*
- **Effects:**
    - Level 4: 100% crit when 4 stains are active.
<!-- GENERATED:END -->
- **Notes:** Circular dependency as primary weapon; may serve as crit-maintenance layer once base 100% crit established. Role in endgame build needs clarification.

### Rejected
- **Colim:** Tested Act 2. 14% attack loss; identical AP economy; no free-aim stain generation. Rejected.
- **Trebuchim for Genesis:** Trebuchim's free-aim random stain generation incompatible with precise Genesis element requirements — replaced by Kralim for first two stains plus varied skills for another stain plus a light stain.

---

## Pictos

<!-- GENERATED:START characters:Lune:Pictos -->
| Slot | Pictos            | Level | Stat Bonus              | Effect                                  |
|------|-------------------|-------|-------------------------|-----------------------------------------|
| 1    | Powerful On Shell | 23    | Defence +874, Crit +25% | Apply Powerful on applying Shell.       |
| 2    | Burn Affinity     | 21    | Speed +439, Crit +12%   | 25% increased damage on Burning targets |
| 3    | Burning Death     | 21    | Speed +308, Crit +24%   | Apply 3 Burn to all enemies on death    |
<!-- GENERATED:END -->

*Previous Pictos (Longer Shell, Healing Share, Powerful on Shell) replaced Chat 5. Longer Shell moved to Monoco; Healing Share retired.*

*Powerful on Shell fires when Lune casts Healing Light (Shell applied via Protecting Heal Lumina) — cascades to Longer Shell on Monoco and boosts Lune's own damage.*

---

## Lumina

### LP Budget
<!-- GENERATED:START characters:Lune:LP -->
- **Current capacity:** 123 LP
- **Used:** 120 LP
- **Spare:** 3 LP
<!-- GENERATED:END -->

### Current Loadout

<!-- GENERATED:START characters:Lune:Lumina -->
| Lumina             | LP | Notes                                                                        |
|--------------------|----|------------------------------------------------------------------------------|
| Accelerating Heal  | 5  | Rush on heal — synergy with Healing Light                                    |
| Base Shield        | 20 |                                                                              |
| Breaker            | 10 |                                                                              |
| Breaking Burn      | 5  |                                                                              |
| Breaking Counter   | 3  |                                                                              |
| Breaking Death     | 5  |                                                                              |
| Burning Shots      | 3  |                                                                              |
| Critical Break     | 5  |                                                                              |
| Dodger             | 1  |                                                                              |
| Energising Parry   | 15 |                                                                              |
| Energising Start I | 5  |                                                                              |
| Energising Turn    | 20 |                                                                              |
| Marking Shots      | 3  |                                                                              |
| Painted Power      | 5  |                                                                              |
| Protecting Heal    | 5  | Shell on heal — triggers Powerful On Shell Pictos and Longer Shell on Monoco |
| Rewarding Mark     | 5  |                                                                              |
| Teamwork           | 5  |                                                                              |
<!-- GENERATED:END -->

---

## Skills

<!-- GENERATED:START characters:Lune:skills -->
**Currently equipped (6):** Elemental Genesis, Healing Light, Hell, Lightning Dance, Mayhem, Terraquake

| Skill             | AP | Stains Generated     | Equipped | Notes                                                                                                                                                                         |
|-------------------|----|----------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Elemental Genesis | 4  | —                    | ✅        | Extreme damage to all enemies, 8 hits. Each hit deals random element damage. Requires Lightning, Earth, Fire and Ice Stains.                                                  |
| Healing Light     | 3  | Light                | ✅        | Heals targeted ally 30–50% HP and dispels all status effects. Consumes Earth Stain ×2 for 0 AP cost. Generates Light Stain.                                                   |
| Hell              | 9  | Fire, Light          | ✅        | Very high Fire AoE, 2 hits. Applies 5 Burn per hit. Deals self-damage if failed. Consumes Ice, Earth and Lightning Stains for greatly increased damage (×3).                  |
| Lightning Dance   | 7  | Lightning, Light     | ✅        | Very high single-target Lightning damage, 6 hits. Crits trigger an additional hit. Consumes Earth, Ice and Fire Stains for greatly increased damage (×5).                     |
| Mayhem            | 3  | —                    | ✅        | Consumes all Stains to deal high elemental damage, 1–4 hits. Can Break if 4 Stains consumed.                                                                                  |
| Terraquake        | 5  | Earth, Light         | ✅        | Earth AoE + deals Earth and Break damage to all enemies every turn for 3 turns. Increases all Break damage received by 50%. Consumes Lightning Stain ×2 to extend to 5 turns. |
| Crustal Crush     | 7  | Earth, Light         | ❌        | High single-target Earth damage + Break damage, 5 hits. Consumes Lightning Stain ×2 for increased damage (×3).                                                                |
| Earth Rising      | 3  | Earth                | ❌        | Low Earth AoE, 1 hit. Consumes Lightning Stain for increased damage (×1.5).                                                                                                   |
| Electrify         | 1  | Lightning, Lightning | ❌        | Low single-target Lightning damage, 3 hits. Crits trigger an additional hit. Consumes Fire Stain to generate Light Stain.                                                     |
| Elemental Trick   | 3  | —                    | ❌        | Low single-target Ice, Fire, Lightning, and Earth damage, 4 hits. Critical hits generate the corresponding Stain.                                                             |
| Fire Rage         | 5  | Fire, Light          | ❌        | Increasingly high Fire AoE every turn until Lune receives damage. Stuns itself if interrupted. Consumes Ice Stain ×2 for increased damage (×2).                               |
| Ice Lance         | 4  | Ice, Light           | ❌        | Medium single-target Ice damage, 1 hit. Slows target 3 turns. Consumes Earth Stain for increased damage (×1.5).                                                               |
| Immolation        | 2  | Fire                 | ❌        | Low single-target Fire damage, 1 hit. Applies 3 Burn. Applies 2 more Burn if target is Marked. Consumes Ice Stain for increased damage (×1.5).                                |
| Rebirth           | 5  | Light                | ❌        | Revives an ally with 30–70% Health and 2 AP. Consumes Lightning Stain ×3 for 0 AP cost.                                                                                       |
| Revitalisation    | 5  | Light                | ❌        | Heals 1–3 allies 40–60% Health. Consumes Fire Stain ×3 to also apply Regen for 3 turns.                                                                                       |
| Rockslide         | 5  | Earth, Light         | ❌        | Medium single-target Earth damage, 2 hits. Can Break. Consumes Lightning, Ice and Fire Stains for greatly increased damage (×5).                                              |
| Thunderfall       | 5  | Lightning, Light     | ❌        | Medium Lightning damage to random enemies, 2–6 hits. Crits trigger an additional hit. Consumes Fire Stain for increased damage (×1.5).                                        |
| Wildfire          | 4  | Fire, Light          | ❌        | Medium Fire AoE, 1 hit. Applies 3 Burn. Consumes Ice Stain ×2 for increased damage (×2).                                                                                      |
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

---

## Key Decisions

- **Trebuchim over Colim:** Tested and confirmed. 14% attack loss with Colim, identical AP economy, no stain generation on free-aim. Trebuchim optimal for prior playstyle.
- **Kralim over Trebuchim:** Kralim required for Elemental Genesis build. Respec to Vitality 99 / Agility 99 completed Chat 5.
- **Burn Affinity over Warming Up for Pictos:** Warming Up takes 5 turns to reach 25% damage cap — too slow for reserve entry. Burn Affinity fires immediately from turn 1 via Wildfire.
- **Burning Death over Sniper as third Pictos:** Higher Crit (+24% vs +13%) and useful on-death burn effect more relevant for Lune's role than Sniper's Speed advantage.
- **Protecting Heal added:** Activates Shell on every Healing Light cast, enabling Longer Shell extension on Monoco and Powerful on Shell bonus for Lune.

---

## Open Questions

- **Kralim element:** Not confirmed in transcript — verify in game.
- **Choralim role in Genesis build:** Can it serve as crit-maintenance layer alongside Kralim? Needs clarification before next Lune build session.
- **Reserve team optimisation:** Lune as DPS + healing, Monoco as break + AP flow — roles agreed; builds reviewed Chat 5.
- **Cheater deferred:** 40LP — not added to reserve team core yet. May add in future if Speed proves insufficient substitute.

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
