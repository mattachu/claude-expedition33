#!/usr/bin/env python3
"""
Chat 10 patch script for data/pictos-lumina.json
Run from repo root: python3 patch_pictos_lumina.py
"""
import json, sys
from pathlib import Path

path = Path("data/pictos-lumina.json")
if not path.exists():
    sys.exit("ERROR: data/pictos-lumina.json not found. Run from repo root.")

with open(path) as f:
    data = json.load(f)

pictos = data["pictos"]

def find(name):
    for p in pictos:
        if p["name"] == name:
            return p
    return None

def patch(name, **kwargs):
    p = find(name)
    if not p:
        print(f"  NOT FOUND: {name}")
        return
    for k, v in kwargs.items():
        old = p.get(k)
        if old != v:
            p[k] = v
            print(f"  {name}.{k}: {old!r} → {v!r}")

def set_stats(name, **kwargs):
    p = find(name)
    if not p:
        print(f"  NOT FOUND: {name}")
        return
    if "stats" not in p:
        p["stats"] = {}
    for k, v in kwargs.items():
        old = p["stats"].get(k)
        if old != v:
            p["stats"][k] = v
            print(f"  {name}.stats.{k}: {old!r} → {v!r}")

def add_pictos(entry):
    if find(entry["name"]):
        print(f"  SKIP (exists): {entry['name']}")
        return
    pictos.append(entry)
    print(f"  Added: {entry['name']}")

print("=== Patching pictos-lumina.json ===")

# ── NEW OBTAINS ────────────────────────────────────────────────────────────
print("\n[New obtains]")

patch("Clea's Life", obtained=True, level=30)

patch("Painter",
      obtained=True, level=28, lp_cost=10,
      equipped_by="Sciel")
set_stats("Painter", speed=519, crit="31%")

patch("Energising Shots",
      obtained=True, level=28, lp_cost=10,
      equipped_by="Sciel")
set_stats("Energising Shots", speed=779, crit="16%")

patch("Powerful Mark",
      obtained=True, level=28, lp_cost=5,
      equipped_by="Monoco")
set_stats("Powerful Mark", speed=819, crit="16%")

patch("Break Specialist",
      obtained=True, level=28)
set_stats("Break Specialist", health=2705, speed=546)

patch("Empowering Break",
      obtained=True, level=28)
set_stats("Empowering Break", speed=546, crit="32%")

patch("Charging Alteration",
      obtained=True, level=28)
set_stats("Charging Alteration", defence=1426, speed=519)

patch("Energising Stun",
      obtained=True, level=28)
set_stats("Energising Stun", speed=519, crit="31%")

# ── LEVEL AND STATS UPDATES ────────────────────────────────────────────────
print("\n[Level and stats updates]")

patch("Anti-Burn", level=29)
set_stats("Anti-Burn", health=2757, defence=1572)

patch("Augmented Counter I", level=28)
set_stats("Augmented Counter I", health=4058, crit="16%")

patch("Burning Death", level=28)
set_stats("Burning Death", speed=546, crit="32%")

set_stats("Energising Burn", defence=401, speed=321)

patch("Energising Pain", level=28)
set_stats("Energising Pain", health=3855, defence=713)

patch("Perilous Parry", level=28)
set_stats("Perilous Parry", speed=546, crit="32%")

patch("Powerful Revive", level=28)
set_stats("Powerful Revive", speed=546, crit="32%")

patch("Roulette", level=28)
set_stats("Roulette", defence=1501, crit="32%")

set_stats("Cleansing Tint", health=818, defence=335)

set_stats("Dead Energy I", speed=162, crit="17%")

set_stats("Gradient Fighter", speed=182, crit="18%")

# ── equipped_by CHANGES ────────────────────────────────────────────────────
print("\n[equipped_by changes]")

patch("Critical Burn",    equipped_by="Lune")
patch("Quick Break",      equipped_by=None)
patch("Powerful On Shell", equipped_by=None)
patch("Sniper",           equipped_by=None)

# ── LP POOL EXPANSIONS ─────────────────────────────────────────────────────
# These live in characters.json, not here — skip

# ── SAVE ───────────────────────────────────────────────────────────────────
with open(path, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✅ data/pictos-lumina.json written successfully.")
