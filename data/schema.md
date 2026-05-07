# Data Schema Reference

All JSON files live in `data/`. JSON is source of truth — Markdown files are generated from it via `scripts/generate.py`. Do not edit generated Markdown manually.

---

## playthrough.json

Tracks current game state and inventory. Updated each session.

```
act                          int       Current act number
phase                        int       Current phase within act
current_area                 string    Current in-game location
active_party                 string[]  Names of the three active party members
reserve_party                string[]  Names of the two reserve party members

inventory
  colour_of_lumina           int       Consumable — 1 per character per LP pool expansion
  recoats                    int       Consumable — used to reset attribute points
  chroma                     int       Currency
  chroma_catalyst            int       Weapon upgrade material (base tier)
  chroma_catalyst_polished   int
  chroma_catalyst_resplendent int
  chroma_catalyst_grandiose  int
  chroma_catalyst_perfect    int       Upgrades weapons to level 33 (max)

current_phase_checklist      object[]  Ordered checklist for the current phase

  id                         string    Unique stable identifier (snake_case)
  label                      string    Display text (Markdown allowed)
  
  done                       bool      Completion state (leaf items only)

  items                      object[]  Optional child checklist items (1 level nesting supported)
    id                       string
    label                    string
    done                     bool

---

## characters.json

One entry per character. Tracks current state — levels, loadout, skills. Stats are snapshot values at time of last update and will drift as characters level; re-capture from screenshots periodically.

```
level                        int
role                         string       Descriptive — e.g. "Primary DPS"

attributes
  <stat>                     int          Allocated attribute points. Only non-zero stats need listing.
                                          Valid keys: vitality, might, agility, defence, luck.

stats_base
  health                     int|null     Intrinsic stat — no Pictos or weapon scaling.
  attack                     int|null
  speed                      int|null
  defence                    int|null
  crit                       string|null  e.g. "41%"

stats_modified
  health                     int       Total stat with current Pictos and weapon equipped.
  attack                     int
  speed                      int
  defence                    int
  crit                       string    e.g. "105%"
  _note                      string    Documents which Pictos/weapon the snapshot was taken with.

weapon_equipped              string    Name of currently equipped weapon. Must match a weapon in weapons.json.

pictos_equipped              string[]  Exactly 3 entries. Names must match pictos-lumina.json.
                                       Order: slot 1, slot 2, slot 3.

lp_total                     int       Current LP pool size (base level + Colour of Lumina expansions).
lp_used                      int       LP currently spent on Lumina. lp_total - lp_used = spare LP.

lumina_core_exclusions       object[]  Core Lumina suite entries that are modified for this character.
  name                       string    Lumina name
  notes                      string    Why this entry differs — e.g. "FREE from Pictos", "non-functional with weapon"

lumina_extras                object[]  Lumina active for this character that are not in the core suite.
  name                       string
  notes                      string    Why this Lumina is included for this character specifically.

skills_equipped              string[]  Exactly 6 entries. Names must match skills.json.

skills_learned               string[]  All skills unlocked in the skill tree. Superset of skills_equipped.

gradient_skills              object[]  Exactly 3 entries (costs 1, 2, 3).
  name                       string
  cost                       int       Gradient Charges required (1, 2, or 3)
  unlocked                   bool      false if not yet reached in skill tree
  effect                     string    Description of effect
```

---

## weapons.json

One array per character. Static fields (element, scaling, effects) don't change once recorded. Mutable fields (level, power) update as weapons are upgraded.

```
name                         string       In-game weapon name
level                        int          Current upgrade level (max 33)
power                        int|null     Attack power at current level. Omit or null if not recorded.
element                      string|null  Damage element: Physical, Fire, Ice, Lightning, Nature, Moon, Void, Dark, null if unknown
scaling                      string|null  Primary and secondary attribute scaling, e.g. "Agility S, Luck A".
                                          Grade jumps to S for primary at level 33 for most weapons.
obtained                     bool         true = player owns this weapon

effects                      object[]     Weapon ability effects, one per unlock level.
  level                      int          Unlock level (typically 4, 10, 20)
  description                string|null  Effect text. null if not yet recorded.

notes                        string       (optional) Strategic notes — why accepted/rejected, synergies, etc.
rejected                     bool         (optional, omit if false) Weapon tested and not recommended for current build.
future                       bool         (optional, omit if false) Weapon not yet obtainable; recorded for future planning.
```

---

## pictos-lumina.json

Single flat array of all 194 Pictos. Each Pictos is unique — only one character can equip it at a time. Learning a Pictos (4 battles) unlocks its effect as a Lumina for all characters at 0 LP cost when that Pictos is equipped; otherwise costs `lp_cost` LP.

```
pictos[]

  name                       string       In-game name
  category                   string[]     Tags: damage, support, survival, healing, ap, break, burn, mark,
                                          critical, gradient, shots, death, solo, combat, misc
  effect                     string       Lumina effect description (what it does when learned/active)
  lp_cost                    int|null     LP cost when used as Lumina without equipping the Pictos.
                                          null = cost unconfirmed.
  obtained                   bool         true = player owns this Pictos
  equipped_by                string|null  Character currently equipping this Pictos, or null.
                                          Only one character can hold a given Pictos at a time.
  level                      int          (optional) Current Pictos level. Higher = better stats.
  stats                      object       (optional) Stat bonuses granted by equipping this Pictos.
                                          Keys: health, attack, speed, defence, crit (string e.g. "24%")
  notes                      string       (optional) Strategic notes — synergies, caveats, interactions.

core_lumina_suite            object       Defines the standard Lumina loadout applied to all characters,
                                          with per-team variants. Generated Markdown uses this.
  main_team / reserve_team
    total_lp                 int          Sum of all LP costs in this suite.
    entries                  object[]     List of Lumina in the suite.
      name                   string
      lp                     int|null     0 or FREE if covered by a Pictos for all main team members.
      notes                  string       (optional)

candidates_for_review        object[]     Lumina worth considering for the core suite or specific characters.
  name, lp, notes

situational_lumina           object[]     Lumina worth adding for specific boss fights or scenarios.
  name, lp, notes
```

---

## skills.json

Static reference — skill effects and AP costs do not change. Character state (which skills are learned/equipped) lives in `characters.json`, not here.

```
Maelle[] / Verso[] / Sciel[] / Lune[] / Monoco[]

  name                       string
  ap                         int          Base AP cost
  ap_adjusted                string       (optional) Reduced cost under specific conditions, e.g. "2 in Virtuose"
  description                string       Effect summary

Maelle[]
  stance_change              string|null  Which stance this skill switches to, or null.

Verso[]
  rank_bonus                 object       Bonus effect at a specific Rank.
    rank                     string       e.g. "S", "A", "B"
    effect                   string

Sciel[]
  charge                     string       Moon or Sun charge

Lune[]
  stains_generated           string[]     Stains added to Lune's pool when this skill is used
  stains_consumed            string[]     Stains consumed by this skill. ["all"] means all current stains.

Monoco[]
  mask                       string       Which mask this skill belongs to: Almighty, Agile, Balanced,
  wheel                      int          Bestial Wheel position (1–6) at which this skill is available
                                          Heavy, or Caster
  mask_bonus                 string       Additional effect when used in the correct mask
```
