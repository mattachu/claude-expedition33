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
| Luck      | 36    | Tertiary  |
| Might     | 0     | None      |
| Defence   | 0     | None      |
<!-- GENERATED:END -->

### Combat Stats

<!-- GENERATED:START characters:Lune:stats -->
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
- **Power:** ~3390
- **Element:** [unconfirmed — verify in game]
- **Scaling:** Vitality A, Agility B
- **Effects:**
    - Level 4: Casting a Skill increases Skill damage of all other elements by +20%; resets when casting a previously used element.
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
    - Level 4: 1 random stain on free-aim
    - Level 10: [unconfirmed]
    - Level 20: base attack generates 2 random stains
<!-- GENERATED:END -->
- **Notes:** Stain generation weapon, used with Mayhem. Replaced by Kralim for Genesis build.

### Future Options
<!-- GENERATED:START weapons:Lune:Choralim -->
- **Choralim (20):** 100% crit when 4 stains are active.
<!-- GENERATED:END -->
- **Notes:** Circular dependency as primary weapon; may serve as crit-maintenance layer once base 100% crit established. Role in endgame build needs clarification.

### Rejected
- **Colim:** Tested Act 2. 14% attack loss; identical AP economy; no free-aim stain generation. Rejected.
- **Trebuchim for Genesis:** Trebuchim's free-aim random stain generation incompatible with precise Genesis element requirements — replaced by Kralim for first two stains plus varied skills for another stain plus a light stain.

---

## Pictos

<!-- GENERATED:START characters:Lune:Pictos -->
| Slot | Pictos             | Level | Stat Bonus                    | Effect                                           |
|------|--------------------|-------|-------------------------------|--------------------------------------------------|
| 1    | Powerful on Shell  | 23    | Defence +874, Crit +25%       | Apply Powerful when applying Shell               |
| 2    | Burn Affinity      | —     | Speed +439, Crit +12%         | 25% increased damage on Burning targets          |
| 3    | Burning Death      | 21    | Speed +308, Crit +24%         | Apply 3 Burn to all enemies on death             |
<!-- GENERATED:END -->

*Previous Pictos (Longer Shell, Healing Share, Powerful on Shell) replaced Chat 5. Longer Shell moved to Monoco; Healing Share retired.*

*Powerful on Shell fires when Lune casts Healing Light (Shell applied via Protecting Heal Lumina) — cascades to Longer Shell on Monoco and boosts Lune's own damage.*

---

## Lumina

### LP Budget
<!-- GENERATED:START characters:Lune:LP -->
- **Current capacity:** 133 LP (expanded 13 Colour of Lumina Chat 5)
- **Used:** 133 LP
- **Spare:** 0 LP
<!-- GENERATED:END -->

### Current Loadout

<!-- GENERATED:START characters:Lune:Lumina -->
*Reserve team core (110LP) + character-specific additions.*

| Lumina             | LP  | Notes                                       |
|--------------------|-----|---------------------------------------------|
| Accelerating Heal  | 5   | Character-specific                          |
| Base Shield        | 20  | Core                                        |
| Breaker            | 10  | Core                                        |
| Breaking Burn      | 5   | Core                                        |
| Breaking Counter   | 3   | Core                                        |
| Breaking Death     | 5   | Core + character-specific                   |
| Burn Affinity      | —   | FREE from Burn Affinity Pictos              |
| Burning Shots      | 3   | Core                                        |
| Critical Break     | 5   | Core + character-specific                   |
| Dodger             | 1   | Core                                        |
| Energising Parry   | 15  | Core                                        |
| Energising Start I | 5   | Core                                        |
| Energising Turn    | 20  | Core                                        |
| Healing Tint Energy| 1   | Character-specific                          |
| Marking Shots      | 3   | Core                                        |
| Painted Power      | 5   | Core                                        |
| Powerful on Shell  | —   | FREE from Powerful on Shell Pictos          |
| Protecting Heal    | 5   | Character-specific — Shell on Healing Light |
| Rewarding Mark     | 5   | Core + character-specific                   |
| Teamwork           | 5   | Core                                        |
<!-- GENERATED:END -->

---

## Skills

<!-- GENERATED:START characters:Lune:skills -->
**Currently equipped (6):** Hell, Terraquake, Lightning Dance, Healing Light, Mayhem, Elemental Genesis

| Skill             | AP  | Stains Generated     | Equipped | Notes                                                                                                     |
|-------------------|-----|----------------------|----------|-----------------------------------------------------------------------------------------------------------|
| Hell              | —   | —                    | ✅       | Guarantees 4 stains and AoE burn on turn 1, enabling Genesis or Lightning Dance on turn 2.                |
| Terraquake        | 5   | Earth, Light         | ✅       | Earth damage over 3 turns; increases all Break damage received by 50% for 3 turns.                        |
| Lightning Dance   | —   | Lightning, Light     | ✅       | Primary single-target nuke for Kralim burst build; requires Fire + Ice + Earth stains.                    |
| Healing Light     | 3   | Light (consumes 2×Earth for 0AP) | ✅ | Heals targeted ally 30–50% HP; dispels ALL status effects including Cursed.                        |
| Mayhem            | 3   | —                    | ✅       | Consumes all stains for damage; Breaks with 4 stains.                                                     |
| Elemental Genesis | 4   | —                    | ✅       | Requires 1 of each element stain (Fire, Earth, Lightning, Ice — Light wildcards). Extreme damage.         |
| Wildfire          | 4   | Fire, Light          | ❌       | Medium Fire AoE; applies 3 Burn.                                                                          |
| Thunderfall       | 5   | Lightning, Light     | ❌       | Lightning damage; flexible vs lightning-weak enemies.                                                     |
<!-- GENERATED:END -->

---

## Gradient Skills

<!-- GENERATED:START characters:Lune:gradients -->
| Gradient Skill  | Gradient Cost | Acquired | Notes                                                                             |
|-----------------|---------------|----------|-----------------------------------------------------------------------------------|
| Tremor          | 1             | ✅       | High Earth damage to all enemies and removes all enemies' Shields.                |
| Tree of Life    | 2             | ✅       | Heals party + removes ALL status effects. Reliable only when charges accumulated. |
| Sky Break       | 3             | ✅       | Extreme damage to all enemies using element with most stains; can break.          |
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
