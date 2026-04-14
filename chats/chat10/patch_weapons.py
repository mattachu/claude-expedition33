#!/usr/bin/env python3
"""
Chat 10 patch script for data/weapons.json
Run from repo root: python3 patch_weapons.py
"""
import json, sys
from pathlib import Path

path = Path("data/weapons.json")
if not path.exists():
    sys.exit("ERROR: data/weapons.json not found. Run from repo root.")

with open(path) as f:
    data = json.load(f)

def find(character, name):
    for w in data[character]:
        if w["name"] == name:
            return w
    return None

def add_weapon(character, weapon):
    if not find(character, weapon["name"]):
        data[character].append(weapon)
        print(f"  Added {character}/{weapon['name']}")
    else:
        print(f"  SKIP (already exists): {character}/{weapon['name']}")

def patch(character, name, **kwargs):
    w = find(character, name)
    if not w:
        print(f"  NOT FOUND: {character}/{name}")
        return
    for k, v in kwargs.items():
        old = w.get(k)
        if old != v:
            w[k] = v
            print(f"  {character}/{name}.{k}: {old!r} → {v!r}")

def set_effects(character, name, effects):
    w = find(character, name)
    if not w:
        print(f"  NOT FOUND: {character}/{name}")
        return
    w["effects"] = effects
    print(f"  {character}/{name}.effects: set ({len(effects)} entries)")

print("=== Patching weapons.json ===")

# ── VERSO ──────────────────────────────────────────────────────────────────
print("\n[Verso]")

patch("Verso", "Chevalam", scaling="Agility S, Luck A")

patch("Verso", "Glaceso",
      element="Ice",
      scaling="Defence B, Luck A")
set_effects("Verso", "Glaceso", [
    {"level": 4,  "description": "+1 Perfection on Critical hit."},
    {"level": 10, "description": "Self-Heal by 2% Health on dealing a Critical hit."},
    {"level": 20, "description": "Counterattack is always a Critical hit."},
])

patch("Verso", "Dualiso", level=28)

patch("Verso", "Abysseram",
      level=28,
      scaling="Vitality A, Defence B")
set_effects("Verso", "Abysseram", [
    {"level": 4,  "description": "50% increased damage on Rank D. No damage increase on other ranks."},
    {"level": 10, "description": "50% increased Base Attack damage."},
    {"level": 20, "description": "On Rank D, recover 20% Health with Base Attack."},
])

patch("Verso", "Sakaram",
      scaling="Agility A, Luck B")
set_effects("Verso", "Sakaram", [
    {"level": 4,  "description": "Can't lose Perfection. No damage increase from Rank."},
    {"level": 10, "description": "50% increased Base Attack damage."},
    {"level": 20, "description": "Base Attack gives 4 Perfection."},
])

patch("Verso", "Tireso",
      level=20,
      element="Nature",
      scaling="Vitality A, Defence B")
set_effects("Verso", "Tireso", [
    {"level": 4,  "description": "Gain 1 Rank on applying Mark."},
    {"level": 10, "description": "Mark an enemy on Base Attack."},
    {"level": 20, "description": "Apply Powerless on Marking an enemy."},
])

# ── SCIEL ──────────────────────────────────────────────────────────────────
print("\n[Sciel]")

patch("Sciel", "Litheson", scaling="Luck S, Agility A")

patch("Sciel", "Chation", level=28)

patch("Sciel", "Ramasson",
      scaling="Vitality B, Luck A")
set_effects("Sciel", "Ramasson", [
    {"level": 4,  "description": "Can consume 1 Moon charge on turn start to recover 20% of each ally's Health."},
    {"level": 10, "description": "Base Attack gives 1 Moon charge."},
    {"level": 20, "description": "Moon Skills give one more charge."},
])

add_weapon("Sciel", {
    "name": "Gobluson",
    "level": 30,
    "power": 4003,
    "element": "Fire",
    "scaling": "Defence A, Agility B",
    "obtained": True,
    "effects": [
        {"level": 4,  "description": "During Twilight, every time Foretell is applied it also affects another random enemy."},
        {"level": 10, "description": "Apply 1 Burn every 3 Foretell applied with Skills."},
        {"level": 20, "description": "20% increased Fire damage with Skills."},
    ]
})

add_weapon("Sciel", {
    "name": "Minason",
    "level": 22,
    "power": 1998,
    "element": "Physical",
    "scaling": "Vitality B, Luck A",
    "obtained": True,
    "effects": [
        {"level": 4,  "description": "Sun Skills have increased damage for each Foretell on the target. Moon Skills don't generate Moon charges anymore."},
        {"level": 10, "description": "With at least 1 active Sun charge, gain one additional AP per Foretell consumed."},
        {"level": 20, "description": "Base attack can consume 1 Sun charge to apply 5 Foretell."},
    ]
})

add_weapon("Sciel", {
    "name": "Blizzon",
    "level": 14,
    "power": None,
    "element": None,
    "scaling": None,
    "obtained": True,
    "effects": []
})

add_weapon("Sciel", {
    "name": "Corderon",
    "level": 13,
    "power": None,
    "element": None,
    "scaling": None,
    "obtained": True,
    "effects": []
})

add_weapon("Sciel", {
    "name": "Tisseron",
    "level": 13,
    "power": None,
    "element": None,
    "scaling": None,
    "obtained": True,
    "effects": []
})

# ── MAELLE ─────────────────────────────────────────────────────────────────
print("\n[Maelle]")

patch("Maelle", "Glaisum", level=29)
patch("Maelle", "Stalum", level=29)

patch("Maelle", "Battlum",
      level=28,
      element="Physical",
      scaling="Defence A, Luck B")
set_effects("Maelle", "Battlum", [
    {"level": 4,  "description": "Double Gradient generation while in Defensive Stance."},
    {"level": 10, "description": "If Stanceless, Base Attack switches to Defensive Stance."},
    {"level": 20, "description": "+5% of a Gradient Charge on Parry."},
])

add_weapon("Maelle", {
    "name": "Facesum",
    "level": 22,
    "power": 2964,
    "element": "Physical",
    "scaling": "Vitality B, Luck A",
    "obtained": True,
    "effects": [
        {"level": 4,  "description": "In Offensive Stance, double the amount of Burn applied."},
        {"level": 10, "description": "50% increased Burn damage."},
        {"level": 20, "description": "Base Attack propagates Burn."},
    ]
})

# ── LUNE ───────────────────────────────────────────────────────────────────
print("\n[Lune]")

patch("Lune", "Kralim",
      level=32,
      element="Lightning",
      scaling="Agility A, Vitality B")

patch("Lune", "Choralim",
      element="Fire",
      scaling="Defence A, Agility B")
# L4 already present; add L10 and L20
set_effects("Lune", "Choralim", [
    {"level": 4,  "description": "100% Critical Chance when 4 Stains are simultaneously active."},
    {"level": 10, "description": "20% increased damage for each consecutive turn without taking damage. Can stack up to 5 times."},
    {"level": 20, "description": "Critical hits apply Burn."},
])

patch("Lune", "Angerim",
      element="Fire",
      scaling="Defence B, Luck A")
set_effects("Lune", "Angerim", [
    {"level": 4,  "description": "Base Attack applies 2 Burn per Fire Stain."},
    {"level": 10, "description": "Generate one Fire Stain at the beginning of each turn."},
    {"level": 20, "description": "30% increased Burn damage per Fire Stain."},
])

# Trebuchim L10 was null
t = find("Lune", "Trebuchim")
if t:
    for e in t["effects"]:
        if e["level"] == 10 and e["description"] is None:
            e["description"] = "+1 AP when Stains are consumed."
            print("  Lune/Trebuchim.effects[L10]: null → '+1 AP when Stains are consumed.'")

patch("Lune", "Troubadim",
      level=28,
      element="Physical",
      scaling="Vitality B, Defence A")
set_effects("Lune", "Troubadim", [
    {"level": 4,  "description": "Free Aim Shots deal damage to an additional random target."},
    {"level": 10, "description": "50% increased Free Aim damage."},
    {"level": 20, "description": "Generate a random Stain on Free Aim shot."},
])

patch("Lune", "Saperim",
      level=28,
      element="Lightning",
      scaling="Defence A, Luck B")
set_effects("Lune", "Saperim", [
    {"level": 4,  "description": "Using a Gradient Attack generates 1 additional Light Stain."},
    {"level": 10, "description": "When a Fire Stain is generated, a Lightning Stain is also generated. Once per turn."},
    {"level": 20, "description": "Gradient Attacks and Gradient Counters deal 50% more damage."},
])

patch("Lune", "Benisim",
      element="Nature",
      scaling="Vitality A, Defence B")
set_effects("Lune", "Benisim", [
    {"level": 4,  "description": "Healing Skills cost 1 less AP."},
    {"level": 10, "description": "Generate one Earth Stain at the beginning of each turn."},
    {"level": 20, "description": "Replay instantly on consuming Stains with a Healing Skill."},
])

# ── MONOCO ─────────────────────────────────────────────────────────────────
print("\n[Monoco]")

patch("Monoco", "Joyaro", level=32)

# Rename Grander → Grandaro
for w in data["Monoco"]:
    if w["name"] == "Grander":
        w["name"] = "Grandaro"
        print("  Monoco/Grander → Grandaro")

patch("Monoco", "Grandaro",
      element="Nature",
      scaling="Vitality A, Defence B")
set_effects("Monoco", "Grandaro", [
    {"level": 4,  "description": "Start battle in Heavy Mask."},
    {"level": 10, "description": "Heavy Mask applies Shell for 3 turns."},
    {"level": 20, "description": "+1 AP per hit taken."},
])

patch("Monoco", "Urnaro",
      element="Nature",
      scaling="Vitality A, Luck B")
set_effects("Monoco", "Urnaro", [
    {"level": 4,  "description": "Switch to Almighty Mask on Breaking an enemy."},
    {"level": 10, "description": "Almighty Mask gives 2 AP to all allies."},
    {"level": 20, "description": "50% increased Break damage."},
])

patch("Monoco", "Nusaro",
      element="Moon",
      scaling="Vitality B, Agility A")
# Add L4 and L10 to Nusaro (L20 already present)
n = find("Monoco", "Nusaro")
if n and len(n["effects"]) == 1:
    n["effects"] = [
        {"level": 4,  "description": "Parries increase the Bestial Wheel by 1. Taking damage resets the Bestial Wheel."},
        {"level": 10, "description": "Upgraded Skills deal 30% more damage."},
        n["effects"][0],
    ]
    print("  Monoco/Nusaro.effects: added L4 and L10")

# ── SAVE ───────────────────────────────────────────────────────────────────
with open(path, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✅ data/weapons.json written successfully.")
