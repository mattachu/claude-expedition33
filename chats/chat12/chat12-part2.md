# Clair Obscur: Expedition 33 — Chat 12 — Part 2: Reserve Team Pictos

<!-- SECTION: Reserve Team Pictos -->
## Reserve Team Pictos

**Matt:** Looks good. I suggest doing Pictos for the reserve team before moving onto Lumina.

**Claude:** Good call — let me check what's actually available after the main team takes their picks.Good analysis. Let me give you the reserve team proposal.

**Current reserve state:**

| Character | Pictos | HP | Speed | Crit | Def |
|-----------|--------|----|----|------|------|
| Lune | Critical Burn, Burn Affinity, Burning Death | 3289 | 2519 | 100% | 182 |
| Monoco | Longer Shell, Powerful Mark, Energising Turn | 4687 | 2201 | 63% | 2301 |

Lune is optimally built — stats at cap, burn theme consistent, nothing to fix. Monoco has the real problem: **crit at 63%, 37% under cap.** Energising Turn contributes zero crit and is a level-14 Pictos carried over from much earlier. Swapping it out is the obvious win.

**Monoco — proposed change**

Energising Turn (Lv14, Spd+270, 0% crit) is badly underlevelled and the effect is already in the reserve core Lumina set. Replacing it with a high-crit Pictos closes the 37% gap without losing anything.

**Best candidate: Burning Break** (Lv21, HP+1541, Crit+24%) — just freed by Maelle's swap.

| Stat | Current | Proposed | Change |
|------|---------|----------|--------|
| Health | 4687 | **6228** | +1541 |
| Speed | 2201 | 1931 | −270 |
| Crit | 63% | **87%** | +24% |
| Defence | 2301 | 2301 | — |

Still 13% short of cap, but +HP and +crit dominate the −270 speed loss. Monoco is reserve — he's not competing for turn order with the main team, and his role on break/mark doesn't depend on a specific speed tier.

**The Roulette question:** I want to flag Roulette explicitly because the data keeps surfacing it. Lv28, Crit+32%, Def+1501 — would give Monoco 95% crit and 3802 Def, both significantly better. But the effect ("every hit has 50% chance to deal 50% or 200%") is a direct damage variance gamble. For a reserve breaker doing consistent break work, the 50% damage outcome is actively bad — missing break thresholds costs more than the 200% upside compensates for. Your established playstyle rejects variance builds (you've skipped Glass Canon, Overload). Wouldn't recommend it.

**Alternative: Energising Stun** (Lv28, Spd+519, Crit+31%, 0 HP) — would give Monoco 94% crit, 2450 speed, but drops HP back to 1930. Trade-off: reaches near-cap crit + keeps speed at cost of HP. Burning Break is the safer pick.

**Lune — no change needed**

She's at 100% crit, 2519 speed, full burn synergy across all three Pictos. Her HP (3289) is lower than Monoco's but she doesn't have a defensive role. Any swap would break her burn engine for marginal stat gain.

The only theoretical upgrade I considered: swap Burn Affinity (weakest: Spd+439, Crit+12%, effect 25% dmg on Burning) for something like Powerful Revive (Spd+546, Crit+32%) — trades 3% raw speed and effect synergy for +20% crit. But she's already at crit cap, so the crit gain is wasted. Not worth losing "25% damage on Burning targets" when Lune's whole identity is attacking burning targets.

**Summary — Reserve Team Proposal**

| Character | Current Pictos | Proposed Pictos |
|-----------|---------------|-----------------|
| Lune | Critical Burn, Burn Affinity, Burning Death | *no change* |
| Monoco | Longer Shell, Powerful Mark, **Energising Turn** | Longer Shell, Powerful Mark, **Burning Break** |

**Full main + reserve summary:**

| Character | Current | Proposed |
|-----------|---------|----------|
| Maelle | Burning Break, Gradient Break, Survivor | Clea's Life, Empowering Break, Gradient Break |
| Verso | Cheater, Breaking Death, Second Chance | Augmented Counter I, Breaking Death, Confident |
| Sciel | Painter, Energy Master, Energising Shots | *no change* |
| Lune | Critical Burn, Burn Affinity, Burning Death | *no change* |
| Monoco | Longer Shell, Powerful Mark, Energising Turn | Longer Shell, Powerful Mark, Burning Break |

**Pictos freed by all changes:** Cheater, Second Chance, Survivor, Energising Turn — available for future alternate builds or to hand to Verso as Lumina.

Ready for Lumina when you are.

---

**Matt:** I’m not sure why you say Monoco’s HP drops back to 1930. If Energising Turn is only Spd+270 and his current HP is 4687, wouldn’t he stay at 4687? So we want to swap Energising Turn for a high-Crit Pictos that also has at least 270 Speed, really. That suggests Energising Stun.

**Claude:** You're absolutely right. I made an arithmetic error. Energising Turn contributes Spd+270 only, so swapping it affects only the speed/crit columns — HP stays at 4687 regardless of the replacement (unless the replacement itself adds HP).

Let me redo the comparison properly.

**Monoco — keeping Longer Shell + Powerful Mark, swapping Energising Turn**

Current contribution from Energising Turn: HP+0, Spd+270, Crit+0%, Def+0.

| Replacement | HP | Speed | Crit | Def | vs current |
|-------------|-----|-------|------|------|------------|
| **Energising Turn (current)** | 4687 | 2201 | 63% | 2301 | baseline |
| **Burning Break** | 6228 | 1931 | 87% | 2301 | +1541 HP, −270 Spd, +24% crit |
| **Energising Stun** | 4687 | **2450** | **94%** | 2301 | +249 Spd, +31% crit |
| **Powerful Revive** | 4687 | 2477 | 95% | 2301 | +276 Spd, +32% crit |
| **Quick Break** | 4687 | 2365 | 91% | 2301 | +164 Spd, +28% crit |

You're right — **Energising Stun is the best pick**. Net: +249 Speed, +31% crit, zero trade-offs.

Actually, **Powerful Revive is marginally better**: 95% crit (vs 94%), +276 speed (vs +249). Same level (28), same HP/Def impact. The only difference is the effect: "Apply Powerful for 3 turns when revived" vs Energising Stun's "+1 AP on hitting a Stunned target with a Skill."

For Monoco as reserve specifically, Powerful Revive's effect is situationally relevant — reserve comes in *after* a wipe, which is the ideal trigger condition. When he gets revived (via Revive Tint, Sciel's Resurrect, or coming in from reserve), he gets 3 turns of Powerful. Energising Stun requires him to hit a Stunned target, which needs setup and is narrower.

**Revised proposal: Powerful Revive over Energising Stun.**

| Character | Current Pictos | Proposed Pictos |
|-----------|---------------|-----------------|
| Monoco | Longer Shell, Powerful Mark, Energising Turn | Longer Shell, Powerful Mark, **Powerful Revive** |

**Monoco stats:**

| Stat | Current | Proposed |
|------|---------|----------|
| Health | 4687 | 4687 |
| Speed | 2201 | **2477** |
| Crit | 63% | **95%** |
| Defence | 2301 | 2301 |

5% shy of cap but a clean upgrade. Nothing is lost.

One more question worth flagging before committing: does the "revive" in Powerful Revive's effect trigger when a character enters battle from reserve after a wipe? I don't know this from memory and it matters for the effect's value. If it only triggers on mid-battle revive (Revive Tint, Sciel's skill), then Energising Stun might be the equal-or-better pick since Monoco-in-reserve is specifically the "coming in after a wipe" case. Worth a quick in-game test before or after committing.

Thanks for catching the error. Updated summary for Pictos changes:

| Character | Current | Proposed |
|-----------|---------|----------|
| Maelle | Burning Break, Gradient Break, Survivor | Clea's Life, Empowering Break, Gradient Break |
| Verso | Cheater, Breaking Death, Second Chance | Augmented Counter I, Breaking Death, Confident |
| Sciel | Painter, Energy Master, Energising Shots | *no change* |
| Lune | Critical Burn, Burn Affinity, Burning Death | *no change* |
| Monoco | Longer Shell, Powerful Mark, Energising Turn | Longer Shell, Powerful Mark, Powerful Revive |

Ready for Lumina when you are.

---

**Matt:** Not sure I agree with you on the revive. Coming in from reserve is not a revive, that’s closer to a new battle start. Would not trigger Powerful. And Sciel won’t be there in the reserve team, and she doesn’t have a Resurrect skill anyway. Lune **will** be there, and she **does** have a Revive skill, but I’m not sure whether I’ve equipped that skill at the moment. I might have done. 

Enemies are stunned when they are broken. Monoco builds Break damage, either he or Lune triggers Break, then the enemy is stunned and he can trigger Energising Stun.

I think both triggers are fairly low likelihood in the reserve team, and a low likelihood of three turns of Powerful is probably more useful than a low likelihood of +1AP.

**Claude:** Fair analysis — I agree with your conclusion and the mechanical reasoning is sharper than mine.

Your point about break/stun is a correction worth recording: I was thinking of it as a separate setup requirement, but if Monoco's role *is* break-building, stun is already on the critical path. The trigger condition is essentially free when it happens. That said, +1 AP once is still modest vs 3 turns of Powerful, so the magnitude argument wins.

So: **Powerful Revive** on Monoco, accepting the revive trigger is low-likelihood but valuable when it fires.

Two small corrections to my record — I had Sciel down as having a revive, which is wrong (she doesn't); and I was vague about what "revive" means mechanically. For future reference: "revive" specifically means bringing a downed character back during battle, not entering from reserve after a party wipe.

**Confirmed reserve proposal:**

| Character | Current | Proposed |
|-----------|---------|----------|
| Lune | Critical Burn, Burn Affinity, Burning Death | *no change* |
| Monoco | Longer Shell, Powerful Mark, Energising Turn | Longer Shell, Powerful Mark, Powerful Revive |

**In-game check worth doing:** Lune's skill loadout — specifically whether she has a revive skill equipped. If not, and you want the Powerful Revive effect to be accessible, equipping one on Lune (or keeping Revive Tints handy) is the way to make the effect active rather than dormant.

Ready for Lumina.

---

**Matt:** I have just updated the skills in the characters data file, so whatever’s in there for Lune should be correct. What’s in the party summary for her skill set?

**Claude:** Let me check — the party summary I already have doesn't include skills (just Pictos and Lumina), so I'll need to fetch the characters.json or her character file... Lune's equipped skills: **Hell, Terraquake, Lightning Dance, Healing Light, Mayhem, Elemental Genesis.**

No Rebirth or Revitalisation equipped (both learned but not on the active list) — so Lune has no revive skill available right now. **Healing Light is a heal, not a revive.**

Her 2 GC Gradient skill is Tree of Life (heals party, clears status effects) — also healing, not revive.

So in the current reserve team configuration, the **only** way for a character to be revived during battle is a Revive Tint.

That doesn't kill the Powerful Revive proposal, but it does narrow the trigger surface. Revive Tints cost an inventory slot and an action, so you'd only use one when actually needing to bring someone back — making the trigger itself relatively rare.

**The question becomes: does Monoco get enough value from +32% crit + 546 speed + 3 turns of Powerful (rare trigger) to prefer it over +31% crit + 519 speed + 1 AP on Stunned hit (more frequent trigger)?**

The stat difference is marginal (Powerful Revive has +1% crit and +27 speed). It's effectively down to the effect:
- Powerful Revive: rare trigger (Revive Tint only), big payoff (3 turns of +damage on the break-dealer)
- Energising Stun: frequent trigger (every time Monoco hits a stunned target with a skill, which is most break-follow-up turns), small payoff (+1 AP)

Given reserve play tends to happen when things are already going wrong (and may well involve Revive Tint use in practice), I think **Powerful Revive still edges it** — but it's marginal, and the stats-only difference is small enough that either works.

Your call. Happy to commit to either; my weak preference is Powerful Revive, but Energising Stun is equally defensible given Lune doesn't have a revive skill equipped.

---

**Matt:** To be fair, it doesn’t affect the frequency, only the mechanism. I will revive Monoco as soon as he dies, whether or not Lune has a revive skill. It just gives me less options for the mechanism.

**Claude:** You're right — the mechanism is different but the trigger frequency is roughly the same either way. Revive Tints are always available as a fallback, and you'll use whatever's at hand the moment Monoco goes down. I was mentally discounting Revive Tints as inferior/rare, but in practice they're the default tool for exactly this situation.

That makes the Powerful Revive case stronger: trigger frequency is roughly equivalent to Energising Stun (both fire on a predictable recurring event), and the magnitude clearly favours Powerful Revive (3 turns of Powerful vs +1 AP once).

**Committed: Powerful Revive for Monoco's slot 3.**

**Final Pictos plan — all five characters:**

| Character | Current | Proposed |
|-----------|---------|----------|
| Maelle | Burning Break, Gradient Break, Survivor | Clea's Life, Empowering Break, Gradient Break |
| Verso | Cheater, Breaking Death, Second Chance | Augmented Counter I, Breaking Death, Confident |
| Sciel | Painter, Energy Master, Energising Shots | *no change* |
| Lune | Critical Burn, Burn Affinity, Burning Death | *no change* |
| Monoco | Longer Shell, Powerful Mark, Energising Turn | Longer Shell, Powerful Mark, Powerful Revive |

**Freed Pictos:** Burning Break, Survivor, Cheater, Second Chance, Energising Turn — all available for Lumina swaps or future reassignment.

Ready for Lumina whenever you are.

---

<!-- SECTION: Lumina Loadout Design -->
## Lumina Loadout Design

**Matt:** Great, thanks. Let’s go for the Lumina check. The count of Colour of Lumina is in the playthrough JSON and probably in the overview. List of equipped Lumina is, I think, in the party summary. You have the full directory of Lumina effects in the Pictos/Lumina JSON that I uploaded.

I would probably start by comparing the currently equipped list with community recommended builds for post-game, see what we are missing, then see if we have enough Colour of Lumina to add them on top of what we have, and if not, look at what we might possibly drop.

Note that we definitely need to use Colour of Lumina to get Verso Cheater back, and probably Second Chance too. I’m minded to add Second Chance to the core set if we can afford it. Is it 20LP or 40LP?

**Claude:** Second Chance is **40LP** — one of the three expensive ones alongside Cheater and Energy Master.

Let me map out the LP impact of the Pictos changes first, then search community builds... Important numbers. Let me search community builds before we commit... Here's where we stand on the budget, plus what the community recommends.

**CoL budget summary:**

| Scenario | CoL needed | Remaining |
|----------|-----------|-----------|
| Minimum (Pictos swaps only, no new Lumina) | 35 | 132 |
| + Second Chance on Verso only | 75 | 92 |
| + Second Chance on all 3 main chars | 146 | 21 |

Second Chance in the core set (all three) costs **146 CoL** — that's nearly the entire stock. It's tight but technically affordable, leaving only 21 in reserve.

**Community consensus on "every character should have":**

The search results consistently highlight the same Lumina as universal essentials: Painted Power (you have it ✓), Cheater (you have it ✓), Energy Master (you have it ✓), Energising Turn (you have it ✓), Base Shield (you have it ✓), Second Chance (you **don't** have it on Maelle or Sciel).

Second Chance is described across multiple sources as a game-changer for endgame/postgame — one source calls it "the best Lumina effect in the game" after Cheater.

**Other community picks you're currently missing from the main team:**

- **Recovery** (10LP) — on Maelle and Sciel currently? Let me check... Not in either loadout. 10% HP regen per turn fires on Cheater bonus turns too. Strong on Maelle especially at 7610 HP.
- **Anti-Blight** (10LP) — described as "near-requisite in endgame/postgame." You don't have it on anyone. Could be added situationally rather than permanently.

**The Second Chance question:**

Adding SC to the core set at 40LP per character is expensive. But it's also the single most impactful Lumina you're not running. With 167 CoL available:

| Character | Current LP | After Pictos swap | + SC | Pool needed | CoL |
|-----------|-----------|-------------------|------|-------------|-----|
| Verso | 194/198 | 214 (Cheater costs 40, Confident saves 20) | 254 | 254 | 56 |
| Maelle | 194/199 | 194 (no Lumina changes yet) | 234 | 234 | 35 |
| Sciel | 175/179 | 175 (no change) | 215 | 215 | 36 |
| Monoco | 132/133 | 152 (ET costs 20) | — | 152 | 19 |
| **Total** | | | | | **146** |

That leaves 21 CoL. Not much room for Recovery or anything else. But levels increase LP pools naturally (1 LP per level), and you're at 85-86 heading into postgame content that'll push you toward 90+. Each level gained across three characters is 3 more LP headroom.

**My recommendation:** Add Second Chance to the core set. It's the single biggest survivability upgrade available and the community unanimously recommends it. The 146 CoL spend is steep but the stock exists for exactly this purpose — permanent, irreversible investment in your endgame team. The 21 remaining CoL plus natural level-up LP gains gives enough flex for situational Lumina like Anti-Blight later.

Burning Break (3LP) and Survivor (20LP) as Lumina for Maelle can wait — she doesn't desperately need either at 7610 HP with Second Chance now covering the fatal-hit case. Recovery (10LP) is a strong future add once levels create headroom.

Does that allocation make sense to you, or do you want to hold back CoL for other purposes?

---

**Matt:** Another thing to consider is whether we use the Cheater and Second Chance Pictos. They are currently saving Verso and Maelle 40LP each, and we’re proposing to spend those 80LP in order to get better stat boost Pictos. Is that worth it? Energy Master is staying on Sciel, so that’s a saving. 

What are the stat boosts for Cheater and Second Chance? Are they worth considering? Also, I think I read somewhere there was an updated version of Second Chance with better stats somewhere. Could you search that?

**Claude:** Good challenge. From the JSON:

- **Cheater** (L24): HP+1198, Spd+400
- **Second Chance** (L16): HP+1106, Crit+8%

Both are relatively low-level Pictos with modest stats. Let me search for the upgrade.Found it. Second Chance can be upgraded to level 31 by defeating Création near Grour in Renoir's Drafts. That's postgame content — on your Phase 4 checklist. At L31, the stats would be substantially better than the current L16.

Also a noteworthy finding from the wiki comments: apparently Second Chance triggers infinitely during Chromatic boss fights — the revive resets each time. Might be a bug, but if it's still unpatched, it makes SC even more valuable.

Now to your core question. Let me lay out the actual comparison:

**What we're trading: current Verso Pictos vs proposed**

| Pictos set | HP | Speed | Crit | Free Lumina |
|------------|-----|-------|------|-------------|
| **Current** (Cheater + BD + SC) | +2304 | +986 | +41% | Cheater (40), BD (5), SC (40) = 85LP free |
| **Proposed** (AC1 + BD + Confident) | +4058 | +1143 | +81% | AC1 (3), BD (5), Confident (20) = 28LP free |

**Net stat gain from swap:** HP+1754, Spd+157, Crit+40%.

**Net LP cost of swap:** 85 − 28 = 57LP of previously-free Lumina now costs real LP. (The full 60LP figure I calculated earlier includes Confident going from paid to free, which offsets slightly.)

So the question is: **is HP+1754, Spd+157, Crit+40% worth 57LP (= 57 CoL)?**

That's roughly 31 HP per CoL, 2.75 Speed per CoL, and 0.7% Crit per CoL. Given that CoL has no other use except expanding LP pools, and you have 167 in stock, I'd say yes — the stat gains are substantial and CoL is the currency specifically designed for this purpose.

**But** — if Second Chance upgrades to L31 in Renoir's Drafts, the stats improve significantly. I don't have exact L31 numbers, but based on scaling patterns (L16 → L31 is roughly a doubling), it might reach ~HP+2500, Crit+18%. Even at L31, the proposed set still wins on total stats — Aug Counter I alone (HP+4058, Crit+16%) outweighs an upgraded Second Chance.

**The Cheater Pictos specifically** (HP+1198, Spd+400) is decent but not exceptional — it's only L24, and neither stat is best-in-class. If it could be upgraded further that might change the calculus, but I don't see an upgrade path for Cheater in the data.

**My assessment:** The swap is worth it. The stat gains are real and large, the LP cost is payable from existing CoL stock, and the freed Pictos effects (Cheater, Second Chance) are preserved as Lumina. The only scenario where keeping Cheater/SC as Pictos would be better is if you were severely CoL-constrained — and at 167 stock, you're not.

Want to proceed with the Lumina loadout design on this basis?

---

**Matt:** Yes

**Claude:** Let me work through this systematically... Here's the full picture. It works, but it's tight.

**Total CoL: 149 of 167 (18 remaining). Zero spare LP on any character.**

**Verso — 254LP (56 CoL expansion)**

| Lumina | LP | Change |
|--------|-----|--------|
| Aug Counter I | FREE | *new from Pictos* |
| Breaking Death | FREE | *unchanged* |
| Confident | FREE | *was 20LP, now Pictos* |
| Breaker | 10 | |
| Breaking Burn | 5 | |
| Breaking Counter | 3 | |
| Burning Shots | 3 | |
| Cheater | **40** | *was FREE, now Lumina* |
| Confident Fighter | 15 | |
| Critical Break | 5 | |
| Dead Energy I | 2 | |
| Dead Energy II | 2 | |
| Dodger | 1 | |
| Energising Parry | 15 | |
| Energising Start I | 5 | |
| Energising Turn | 20 | |
| Energy Master | 40 | |
| Enfeebling Mark | 10 | |
| Marking Shots | 3 | |
| Painted Power | 5 | |
| Rewarding Mark | 5 | |
| **Second Chance** | **40** | *NEW — added to core* |
| Survivor | 20 | |
| Teamwork | 5 | |
| **Total** | **254** | |

Note: still no Base Shield (non-functional with Chevalam).

**Maelle — 237LP (38 CoL expansion)**

| Lumina | LP | Change |
|--------|-----|--------|
| Clea's Life | FREE | *new from Pictos* |
| Empowering Break | FREE | *new from Pictos* |
| Gradient Break | FREE | *unchanged* |
| Base Shield | 20 | |
| Breaker | 10 | |
| Breaking Burn | 5 | |
| Breaking Counter | 3 | |
| Breaking Death | 5 | |
| **Burning Break** | **3** | *was FREE, now Lumina* |
| Burning Shots | 3 | |
| Cheater | 40 | |
| Critical Break | 5 | |
| Dead Energy I | 2 | |
| Dead Energy II | 2 | |
| Dodger | 1 | |
| Energising Parry | 15 | |
| Energising Start I | 5 | |
| Energising Turn | 20 | |
| Energy Master | 40 | |
| Marking Shots | 3 | |
| Painted Power | 5 | |
| Rewarding Mark | 5 | |
| **Second Chance** | **40** | *NEW — added to core* |
| Teamwork | 5 | |
| **Total** | **237** | |

Survivor dropped — redundant at 7610 HP with Second Chance now covering the fatal-hit case.

**Sciel — 215LP (36 CoL expansion)**

Unchanged except adding Second Chance (40LP). Full list same as current + SC.

**Monoco — 152LP (19 CoL expansion)**

Unchanged except Energising Turn now costs 20LP (was free from Pictos). Powerful Revive free from new Pictos.

**Lune — 120LP. No changes.**

**Budget summary:**

| | CoL | Spare LP |
|---|-----|---------|
| Verso | 56 | 0 |
| Maelle | 38 | 0 |
| Sciel | 36 | 0 |
| Monoco | 19 | 0 |
| Lune | 0 | 7 |
| **Total** | **149** | |
| **Remaining CoL** | **18** | |

It's tight but functional. Every character levelling up naturally adds 1LP headroom, so by level 90 (4–5 levels from now) each main character has 4–5LP spare — enough for situational additions like Anti-Blight (10LP) or Recovery (10LP).

The community picks we're still missing (Recovery, Anti-Blight) can be added as levels create room. Anti-Blight in particular should go on before any post-game content where Blight is common.

Does this look right to you?

---

**Matt:** Yes, I think so. Can you write it out as Main team core set, Reserve team core set, changes per character?

**Claude:** All verified. Here's the clean write-up:

**Main Team Core Lumina Set — 234LP**

*Previous core + Second Chance. Applied to Maelle, Verso, Sciel.*

| Lumina | LP |
|--------|-----|
| Painted Power | 5 |
| Teamwork | 5 |
| Base Shield | 20 |
| Energising Turn | 20 |
| Energising Parry | 15 |
| Energising Start I | 5 |
| Dodger | 1 |
| Breaker | 10 |
| Marking Shots | 3 |
| Dead Energy I | 2 |
| Dead Energy II | 2 |
| Critical Break | 5 |
| Rewarding Mark | 5 |
| Burning Shots | 3 |
| Breaking Burn | 5 |
| Breaking Counter | 3 |
| Breaking Death | 5 |
| Cheater | 40 |
| Energy Master | 40 |
| **Second Chance** | **40** |

**Reserve Team Core Lumina Set — 110LP (unchanged)**

*Main core minus Cheater, Energy Master, Dead Energy I, Dead Energy II, Second Chance. Applied to Lune, Monoco.*

**Per-character changes**

**Verso** — 254LP (56 CoL)

Core exclusion: Base Shield (non-functional with Chevalam).
Free from Pictos: Breaking Death, Confident, Aug Counter I.

| Extra Lumina | LP | Notes |
|-------------|-----|-------|
| Confident | FREE | *was 20LP, now Pictos* |
| Aug Counter I | FREE | *new from Pictos* |
| Confident Fighter | 15 | |
| Enfeebling Mark | 10 | |
| Survivor | 20 | |

**Maelle** — 237LP (38 CoL)

Free from Pictos: Clea's Life, Empowering Break, Gradient Break.

| Extra Lumina | LP | Notes |
|-------------|-----|-------|
| Burning Break | 3 | *was Pictos, now Lumina* |
| Clea's Life | FREE | *new from Pictos* |
| Empowering Break | FREE | *new from Pictos* |
| Gradient Break | FREE | *unchanged* |

Dropped: Survivor (redundant at 7610 HP with Second Chance).

**Sciel** — 215LP (36 CoL)

Free from Pictos: Energy Master, Painter, Energising Shots.

| Extra Lumina | LP | Notes |
|-------------|-----|-------|
| Accelerating Heal | 5 | |
| Energising Heal | 10 | |
| Energising Shots | FREE | *from Pictos* |
| Healing Tint Energy | 1 | |
| Painter | FREE | *from Pictos* |
| Protecting Heal | 5 | |

No changes beyond adding Second Chance to core.

**Monoco** — 152LP (19 CoL)

Free from Pictos: Longer Shell, Powerful Mark, Powerful Revive.

| Extra Lumina | LP | Notes |
|-------------|-----|-------|
| Break Specialist | 1 | |
| Cheater | 40 | |
| Longer Shell | FREE | *from Pictos* |
| Powerful Mark | FREE | *from Pictos* |
| Powerful Revive | FREE | *new from Pictos* |
| Staggering Attack | 1 | |

Energising Turn now costs 20LP (was free from Pictos).

**Lune** — 120LP (no CoL needed)

Free from Pictos: Critical Burn, Burn Affinity, Burning Death.

| Extra Lumina | LP | Notes |
|-------------|-----|-------|
| Accelerating Heal | 5 | |
| Burn Affinity | FREE | *from Pictos* |
| Burning Death | FREE | *from Pictos* |
| Critical Burn | FREE | *from Pictos* |
| Protecting Heal | 5 | |

No changes.

**CoL Budget: 149 of 167 (18 remaining)**

Future adds as levels create headroom: Recovery (10LP), Anti-Blight (10LP), Powerful On Shell (10LP), Energising Shell (10LP).

---

