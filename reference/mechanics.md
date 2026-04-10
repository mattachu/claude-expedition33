# Mechanics reference

## Parry, Dodge, Jump and Counterattack

Most enemy attacks can be avoided by triggering a parry, dodge or jump. These must be triggered within a quick-time window. Parrying has the shortest windows. Successfully completing all parries in an enemy's attack sequence triggers a Counterattack automatically. This deals significant damage and does not consume a turn — it is the primary mechanical reward for parrying, beyond damage avoidance. Some weapon abilities add further effects on Counterattack: Lithum Level 10 (Maelle) switches her to Virtuose stance on a successful Counterattack.

## AP

Skills cost AP to use. Every character gains 1 AP at the start of their turn. A skill costing 4 AP therefore requires 4 turns of baseline generation with no other AP sources. Skills, Pictos and Lumina can provide extra AP.

## Free-Aim

Free-aim is a distinct targeting mode costing 1 AP, used before selecting a skill, item, or basic attack. It is separate from both skills and basic attacks. Lumina and weapon effects that specify "free-aim shots" (e.g. Burning Shots, Marking Shots, Augmented Aim) apply only to free-aim shots — not to skills or basic attacks. Conversely, effects that trigger on "base attacks" do not trigger on free-aim. This distinction matters when evaluating Lumina synergies.

## Gradient Skills

Each character has three Gradient Skills, costing 1, 2, and 3 Gradient Charges (GC) respectively. Gradient charges build by spending AP on skills only — not from basic attacks, parries, or free-aim shots. Gradient Skills are powerful abilities with effects ranging from damage to healing to revival — not all are attacks, hence "Gradient Skills" rather than "Gradient Attacks."

Individual character Gradient Skills are listed in each character file. Details for most characters are not yet confirmed in transcript — placeholders are in place.

## Break Mechanics

There are two distinct types of Break skills:
- **Break bar filling skills** (labelled "High Break damage"): Deal high damage to the break bar to fill it up over multiple hits. Example: Stalact Punches, Terraquake.
- **Break trigger skills** (labelled "Can Break"): Land the final hit that actually triggers the Break when the bar is full. Example: Moissonneuse Vendange, Mayhem, Final Path.

A team typically needs both types — a filler to build the bar and a trigger to fire it. Some gradient skills combine both (e.g. Monoco's Break Point fills and triggers simultaneously).

**Note:** By late game, Lumina (particularly Breaker) contributes significantly to break bar filling across all characters. The break capability of a team depends more on Lumina sets than on individual skills labelled as "high break damage." Multi-hit skills (e.g. Phantom Stars, Final Path) fill the break bar substantially even without that label. The skill label is not the sole indicator of break capability.

## Damage Cap

A 9,999 damage cap applies by default. Painted Power (5 LP Lumina) removes this cap and is essential from Act 3 onwards. It is included in the core Lumina suite for all characters.

## Pictos and Lumina

Pictos are collectible items (3 slots per character) giving stat boosts and effects. Learning a Pictos (4 battles) unlocks it as a Lumina — effect only, no stat boosts, costs LP. Any Lumina costs 0LP for a character who has that Pictos equipped. With attributes maxed at 99, Pictos stat boosts are the primary source of character growth.

Key rules: each Pictos is a unique copy (only one character can equip it); duplicates upgrade the existing copy; extra-turn effects don't stack (bonus turns can't trigger further bonus turns); passive "on turn start" effects fire on Cheater/Intervention bonus turns too; Pictos stat boosts cover Health, Defence, Speed, and Crit only — not Attack. For status immunity, add the relevant Lumina rather than swapping Pictos.

**Lumina Point (LP) pools:** Each character's LP pool equals their level by default. Pools can be permanently increased by spending **Colour of Lumina** items (1 Colour = 1 LP per character). The increase is permanent and irreversible. Current stock: ~200 Colour of Lumina. Pools have already been expanded for main team members (Maelle 196, Verso 194, Sciel 176).

**Full reference:**

| File                                   | Purpose                                                                                         | When to read                                            |
|----------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `overview/pictos-lumina-summary.md`    | Full Pictos/Lumina mechanics, Core Lumina sets, per-character loadouts, situational, candidates | Any session involving Pictos/Lumina advice              |
| `reference/pictos-lumina-catalogue.md` | All 194 Pictos grouped by category with effects and LP costs                                    | When browsing or searching the full catalogue           |
| `data/pictos-lumina.json`              | Raw JSON — query directly for specific Pictos data                                              | When Claude needs to look up or modify specific entries |

## Tints

Tints are consumable items, distinct from skills. There are three types: Healing Tints (restore HP), Revive Tints (revive a fallen ally), and Energy Tints (restore AP). Tints are upgraded using Shapes; the maximum number carried is increased using Shards. Tints are consumed on use and refilled on Rest.

**Important:** Pictos/Lumina effects that trigger "on applying a heal" or "on applying Shell" behave differently depending on source:
- *Protecting Tint Lumina*: fires when a **Tint** is used — not when a healing skill is used.
- *Protecting Heal Lumina*: fires when a **skill** heals an ally — not on Tint use.

"Can't be healed" effects (e.g. Chevalam Level 4, Confident, Confident Fighter) block active healing actions — Tints and healing skills. They do not block passive on-turn-start Lumina effects such as Recovery (10% health per turn start).

## Attribute System

Characters gain 3 attribute points per level up. Points are held in reserve and can be spent at any Flag. Points committed to an attribute are permanent unless a Recoat is used (resets all attributes and skill points to zero, returning all spent points). Attributes cap at 99 — points cannot be spent on an attribute already at 99.

Primary attribute effects are universal: Vitality → Health; Might → Attack Power; Agility → Speed; Defence → Defence stat; Luck → Critical Rate. Two secondary effects have been confirmed consistently across multiple characters: Agility also increases Defence stat; Luck also increases Speed. These are likely universal but have not been verified on every character. Weapon scaling contributes to Attack Power via two attributes at different rates — the contributing attributes vary per weapon and are listed in each character file.

## Reserve Party

If the main party is fully wiped in a battle, the player can continue the battle using the reserve party. This is most relevant for hard bosses. Reserve party members should not be stripped of all useful Pictos/Lumina — but main party optimisation takes priority for the vast majority of battles.
