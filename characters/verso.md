# Verso — Clair Obscur: Expedition 33

*Last updated: 2026-03-11*

---

## Role

- **Primary role:** Mid-game DPS (levelling team); endgame main DPS
- **Party position:** Active in Act 3 levelling team (Verso / Monoco / Sciel); planned endgame team (Maelle / Sciel / Verso)
- **Synergies:** Receives Fortune's Fury from Sciel (doubled damage); Intervention from Sciel grants extra turn + 4 AP for burst; Monoco's Stalact Punches fills Break bar for Verso's Perfect Break (triggers Break + jumps to S Rank); Marking Shot + Rewarding Mark Lumina generate AP return for party

---

## Mechanics

Verso's central system is **Perfection and Rank**. Perfection is a resource that fills a rank meter; higher ranks give higher damage multipliers and unlock skill bonuses. Rank order: **D → C → B → A → S**. Skills and parries generate Perfection. D is the true base rank — previous note of C as starting rank was because Lighteram's Level 4 set a floor of C. With Chevalam there is no floor; hits can take Verso back to D.

**Critical mechanic:** Rank bonuses apply ONLY at the **exact rank stated** — not at higher ranks. Yellow skill text in-game indicates an active rank bonus.

| Event | Perfection effect |
|-------|-------------------|
| Parry | Gains Perfection; successful full parry sequence triggers Counterattack (powerful free damage, does not cost a turn) |
| Dodge | Prevents rank loss; Perfect Dodge (same timing window as Parry) gives +1 AP via Dodger Lumina |
| Hit taken (general) | Full rank demotion |
| Hit taken (Gaulteram) | Lose 1 Perfection only (not full rank demotion) — Gaulteram-specific, not general |
| Quick Strike | D: gives more Perfection |
| Light Holder | +1 Rank on completion; A: +2 AP |
| Perfect Break (at B Rank) | Triggers Break → jump to S Rank |
| End Bringer | A: can reapply stun on broken target |

**Dodge vs Parry timing:** Dodge has a wider window than Parry. Dodge > Perfect Dodge == Parry in terms of timing windows. If a Dodge is Perfect, a Parry would also work. Dodge is used to safely learn parry timings — the game indicates whether a Dodge was Perfect.

**Counterattack:** Successfully completing all parries in an enemy's attack sequence launches a highly powerful Counterattack. This does not consume a turn. This is the primary reason to prioritise Parry over Dodge.

**Stun:** Enemies are stunned on Break. End Bringer deals increased damage to stunned targets, and at A Rank can reapply stun to extend the window.

**Steeled Strike:** Charges for 1 turn; executes following turn for extreme damage. Interrupted if Verso takes any damage during charge. Requires Cheater (consecutive turns) to use safely. S Rank bonus active with Chevalam (starts at S).

**Burst sequence (endgame):** Verso (normal turn): base attack to farm AP → Verso (Cheater turn): Steeled Strike charge → Sciel (normal turn): Fortune's Fury on Verso → Sciel (Cheater turn): Intervention on Verso → Verso (Greater Rush turn): Steeled Strike executes with Fortune's Fury active. Combined multiplier: Rank S (×3.0) × Chevalam stacks (×1.4+) × Fortune's Fury (×2.0) = ×8.4+ before Steeled Strike's own multiplier.

**Solo fights:** Both completed (vs Francois, vs Monoco).

---

## Current Stats

### Level and Attributes

| Attribute | Value | Priority  | Reason                                                                         |
|-----------|-------|-----------|--------------------------------------------------------------------------------|
| Level     | 81    | —         |                                                                                |
| Agility   | 99    | Primary   | Chevalam scales Agility A, Luck B; Agility raises Speed, Attack, Defence       |
| Luck      | 99    | Primary   | Increases crit rate; same weapon scaling priority as Agility                   |
| Might     | 27    | Tertiary  | Extra attack power; spare points                                               |
| Vitality  | 0     | None      | Weapon does not scale off Vitality                                             |
| Defence   | 0     | None      | No benefit for this build                                                      |

### Combat Stats

| Stat                          | Base    | From weapon/Pictos              | Total  |
|-------------------------------|---------|--------------------------------|--------|
| Health                        | 1698    | +2305 (Pictos)                 | 4003   |
| Attack                        | 942     | +3263 (Chevalam scaling)       | 4205   |
| Speed                         | 1096    | +839 (Pictos)                  | 1935   |
| Defence                       | 182     | —                              | 182    |
| Critical Rate                 | 41%     | +20% (Pictos)                  | 61%    |

### Pictos Breakdown

| Pictos       | Level | Health | Speed | Crit | Effect                                      |
|--------------|-------|--------|-------|------|---------------------------------------------|
| Cheater      | 24    | +1198  | +400  | —    | Always play twice in a row.    |
| Survivor     | 21    | —      | +439  | +12% | Survive fatal damage with 1 Health once per battle. |
| Second Chance| 16    | +1107  | —     | +8%  | Revive with 100% Health once per battle. |

---

## Weapons

### Current
- **Name:** Chevalam (32)
- **Power:** 5033
- **Element:** Physical
- **Scaling:** Agility A, Luck B
- **Effects:**
    - Level 4: Start battle at Rank S, but can't be Healed or gain Shields.
    - Level 10: 20% increased damage for each consecutive no-damage turn, stacks up to 5×.
    - Level 20: Apply Rush on Rank S.
- **Notes:** The Cheater extra turn counts as a no-damage turn and stacks the Level 10 bonus — Verso builds damage stacks mechanically just by taking his Cheater turns normally, not only by successfully avoiding hits. Confident (20LP) and Confident Fighter (15LP) are the recommended Lumina pairing: since Chevalam already prevents healing, the "cannot be healed" downside of both Lumina is fully priced in, while the benefits (take half damage; deal 30% more damage) are entirely available.

### Also obtained (not in active use)
| Weapon      | Level | Notes                                                                                                         |
|-------------|-------|---------------------------------------------------------------------------------------------------------------|
| Corpeso     | 23    | Fire, Vitality + Agility. L4: Base Attack applies 2 Burn per Rank. L10: +1 AP on Rank Up. L20: Burn damage +50% per Rank up to 300% at S. Burn-stacking build; synergises with Maelle's Burning Canvas. |
| Contorso    | 23    | Lightning, Defence + Agility. L4: Switch to Rank S on Break; Base Attack can Break. L10: 100% Crit at Rank S. L20: Lightning strike on Crits. S-tier; deferred — same rank-loss-on-hit vulnerability, no forgiveness. |
| Glaceso     | 29    | Defence + Luck scaling — respec required. Previously rejected.                                                |
| Gaulteram   | 12    | Agility + Luck. Act 2 weapon. L4: lose only 1 Perfection on hit. Replaced by Chevalam.                       |
| Dualiso     | 9     | Lightning, Vitality + Defence. L4: Play again after Base Attack. L10: +50% Base Attack damage. L20: Base Attack gives 4 Perfection. Conflicts with Cheater; base-attack-spam build. |
| Sakaram     | 25    | Details not confirmed.                                                                                        |
| Cruleram    | 26    | Details not confirmed.                                                                                        |
| Lanceram    | 15    | Details not confirmed.                                                                                        |
| Liteso      | 16    | Details not confirmed.                                                                                        |
| Abysseram   | 10    | Details not confirmed.                                                                                        |
| Confuso     | 11    | Details not confirmed.                                                                                        |
| Danseso     | 10    | Details not confirmed.                                                                                        |
| Delaram     | 7     | Details not confirmed.                                                                                        |
| Demonam     | 5     | Details not confirmed.                                                                                        |
| Noahram     | 1     | Details not confirmed.                                                                                        |
| Sireso      | 14    | Details not confirmed.                                                                                        |
| Verleso     | 7     | Details not confirmed.                                                                                        |

### Future (post-game)
- **Simoso** — from Simon (Renoir's Drafts). S-tier. Scaling: Vitality + Agility. Level 20: Can't die if at least Rank A.
- **Dreameso** — Agility + Luck scaling; Rank gain on Counterattack; deferred until parry/counterattack rate improves.
- **Seeram** — Vitality + Agility. Can't reach Rank S. S-tier ONLY for End Bringer stunlock build on Simon. Purchased from Unfinished Cruler, Coastal Cave.

---

## Pictos

| Slot | Pictos        | Level | Stat Bonus                        | Effect                                      |
|------|---------------|-------|-----------------------------------|---------------------------------------------|
| 1    | Cheater       | 24    | Health +1198, Speed +400          | Extra turn once per turn                    |
| 2    | Breaking Death| 29    | Speed +586, Crit +33%             | Fully charge enemy break bar on death       |
| 3    | Second Chance | 16    | Health +1107, Crit +8%            | Revive with 100% Health once per battle     |

**Breaking Death synergy:** On death → break bar fills instantly → Second Chance revives at Rank D → Perfect Break triggers break → Rank S in one move → Steeled Strike burst immediately active.

---

## Lumina

### LP Budget
- **Current capacity:** 154 LP
- **Used:** 154 LP
- **Spare:** 0 LP

### Current Loadout

| Lumina              | LP  | Notes                                                         |
|---------------------|-----|---------------------------------------------------------------|
| Breaking Burn       | 5   |                                                               |
| Breaking Counter    | 3   |                                                               |
| Breaking Death      | 5   |                                                               |
| Burning Shots       | 3   |                                                               |
| Cheater             | —   | FREE from Cheater Pictos                                      |
| Confident           | 20  | Take half damage; cannot be healed (already Chevalam-gated)   |
| Confident Fighter   | 15  | +30% damage; cannot be healed                                 |
| Critical Break      | 5   |                                                               |
| Dead Energy I       | 2   |                                                               |
| Dead Energy II      | 2   |                                                               |
| Dodger              | 1   |                                                               |
| Energising Parry    | 15  |                                                               |
| Energising Start I  | 5   |                                                               |
| Energising Turn     | 20  |                                                               |
| Enfeebling Mark     | 10  | Marked targets deal 30% less damage                           |
| Marking Shots       | 3   |                                                               |
| Painted Power       | 5   |                                                               |
| Rewarding Mark      | 5   |                                                               |
| Second Chance       | —   | FREE from Second Chance Pictos                                |
| Survivor            | 20  | Added Chat 5 — both Survivor and Breaking Death effects now on Verso |
| Teamwork            | 5   |                                                               |

---

## Skills

**Currently equipped (6):** Quick Strike, Light Holder, Marking Shot, Perfect Break, End Bringer, Steeled Strike

| Skill          | AP Cost         | Equipped | Rank Bonus                                     | Notes                                                                                                                                                              |
|----------------|-----------------|----------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quick Strike   | 2               | ✅       | D: gives more Perfection                       | Low physical. Modest Perfection gain. Does NOT jump to Rank B without Glaceso.                                                                                     |
| Light Holder   | 4               | ✅       | A: +2 AP                                       | Medium Light damage, 5 hits. Gains +1 Rank at completion.                                                                                                          |
| Marking Shot   | 2               | ✅       | C: increased damage                            | Low damage + 100% Mark. No HP cost. 2 AP.                                                                                                                         |
| Perfect Break  | 7 (5 at B Rank) | ✅       | B: costs 5 AP instead of 7                    | Very high Light damage; can Break; Rank S on Break.                                                                                                                |
| End Bringer    | 8               | ✅       | A: can reapply stun                            | Extreme Physical damage, 6 hits. Increased damage if target Stunned. Break → Stun is the reliable setup: enemies are Stunned on Break, enabling End Bringer's bonus immediately. A Rank ability reapplies Stun to extend the window. |
| Steeled Strike | 9               | ✅       | S: increased damage                            | After 1 turn charge, extreme Physical damage. Interrupted if damage taken. Safe with Cheater. S Rank bonus active given Chevalam starts at S.                      |

**Skills available but not equipped:**

| Skill            | AP  | Rank Bonus                   | Notes                                                                                                                    |
|------------------|-----|------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Assault Zero     | 3   | B: increased damage          | B→A rank progression. Replaced by Light Holder.                                                                          |
| Berserk Slash    | 4   | C: increased damage          | Medium Physical, 3 hits. Damage scales with missing HP — at 1 HP ~1485% scaling. Niche; high risk.                      |
| Blitz            | 3   | B: bonus only                | Insta-kills low-health enemies; otherwise deals damage. Occasional cleanup utility.                                      |
| Burden           | 1   | —                            | Removes status effects from all allies. Best paired with Purification.                                                   |
| Defiant Strike   | 3   | B: increased damage          | 2-hit Physical, 100% Mark. Costs 30% current HP. Not recommended at current parry rate.                                 |
| From Fire        | 4   | B: increased damage          | Healing from Burn. Situational — only useful if enemies consistently have burn.                                          |
| Leadership       | 3   | C: +1 more AP to allies      | Extra AP to all allies. Invaluable in some builds; conflicts with Verso's DPS role.                                      |
| Paradigm Shift   | 1   | C: bonus                     | Generates 1–3 AP. NOT a rank jump. Redundant given team AP generation.                                                   |
| Perfect Recovery | 3   | C: 100% HP                   | Heals Verso only. Non-functional with Chevalam.                                                                          |
| Phantom Stars    | 9 (5 at S) | —                   | AoE multi-hit, all enemies. Trash only — useless in 1v1.                                                                 |
| Purification     | 5   | B: increased damage          | Medium Light damage, 2 hits. Dispels self status effects. Niche.                                                         |
| Strike Storm     | 7   | C: crits give +2 Perfection  | 5-hit high single-target, weapon element. Previously core skill; displaced by End Bringer/Steeled Strike.               |

---

## Gradient Skills

| Gradient Skill | Gradient Cost | Acquired | Notes                                   |
|----------------|---------------|----------|-----------------------------------------|
| [unconfirmed]  | 1             | [?]      | Details not confirmed — verify in game. |
| [unconfirmed]  | 2             | [?]      | Details not confirmed — verify in game. |
| [unconfirmed]  | 3             | [?]      | Details not confirmed — verify in game. |

---

## Build Options

| Build Name                   | Role     | Key Skills                                                                               | Key Lumina | Status   | Notes                                                                  |
|------------------------------|----------|------------------------------------------------------------------------------------------|------------|----------|------------------------------------------------------------------------|
| Levelling team (pre-Cheater) | DPS      | Quick Strike, Assault Zero, Strike Storm, Marking Shot, Phantom Stars, Perfect Break     | Core suite | Complete | Rank build via Strike Storm crits; Perfect Break for S Rank jump       |
| Solo fights (completed)      | Solo DPS | Quick Strike, Assault Zero, Defiant Strike, Perfect Break, Perfect Recovery, Paradigm Shift | Solo Pictos | Complete | Second Chance borrowed from Maelle; now returned                    |
| Endgame (post-Cheater)       | Main DPS | Quick Strike, Assault Zero, Strike Storm, Marking Shot, Perfect Break, Steeled Strike   | Core suite | Current  | Phantom Stars → Steeled Strike confirmed. Second Chance → Cheater Pictos. Fortune's Fury + Steeled Strike incompatible (buff consumed on windup turn — Sciel should use Intervention instead when Verso is winding up). Steeled Strike damage calculation timing (windup vs execution turn) unresolved — needs in-game testing. |

---

## Key Decisions

- **Gaulteram over Glaceso:** Glaceso costs 2 Recoats net; no forgiveness mechanic. Gaulteram Level 4 forgiveness critical while parry skills developing. Same scaling as Chevalam = clean future swap.
- **Marking Shot over Defiant Strike:** Same 100% Mark. Defiant Strike costs 30% HP per use — unacceptable at ~20% parry rate. Marking Shot: 2 AP, no HP cost.
- **Strike Storm over Defiant Strike (damage slot):** More damage, synergises with Fortune's Fury. Mark handled by Marking Shot.
- **Phantom Stars retained:** Essential for AoE in Visages and multi-enemy areas. Useless in 1v1 — never use in boss fights.
- **Steeled Strike deferred:** Available but requires Cheater Pictos for safe use. Obtain Cheater (Sprong) first.

---

## Open Questions

- **Recovery + Chevalam interaction:** Chevalam prevents healing and shields. Does Recovery Lumina (10% health per turn start) count as healing? Unverified — worth testing in practice.
- **Defiant Strike timing:** When parry rate improves enough to justify 30% HP cost per use.
- **Dreameso timing:** When parry/counterattack rate is high enough to make Rank gain on Counterattack reliable. Post-game.
- **Seeram + End Bringer stunlock build:** Worth investigating for post-game Simon fight specifically.
- **Verso stat allocation:** Agility 99, Luck 99, Might 27. Whether Might is optimal over other allocations — unconfirmed.
- **Unconfirmed weapon details:** Sakaram, Cruleram, Lanceram, Liteso, Abysseram, Confuso, Danseso, Delaram, Demonam, Noahram, Sireso, Verleso — abilities/scaling not yet documented.

---

## Errors to Avoid

- **Light Holder and End Bringer recommended before available:** These skills were recommended in session summaries before Matt had obtained them. The "Confirmed NOT in skill list" note was accurate at the time — the error was recommending skills without checking current availability.
- **Glaceso recommendation:** Recommended over Gaulteram based on higher weapon level. Wrong: costs 2 Recoats net; no forgiveness; Gaulteram was the right choice at the time.
- **Phantom Stars in 1v1/solo fights:** AoE is useless vs single target.
- **Paradigm Shift rank jump:** Said it jumps to S Rank. Correct: generates 1–3 AP; C Rank bonus only.
- **Quick Strike rank jump (inherent):** Requires Glaceso Level 4. Without Glaceso = modest Perfection gain only.
- **Rank bonuses persist to higher ranks:** WRONG. Exact rank only. Yellow text = active.
- **Overload AP in same turn:** AP from Overload carries to the next turn, not the same turn.
- **Second Chance on multiple characters:** Only one character can hold this Pictos at a time.
- **Chevalam "available right now at Level 56":** Recommended level is 65–70+.
- **Gaulteram as Act 3 endgame weapon:** It is an Act 2 weapon.
- **Rank loss on hit as weapon-specific:** General Verso mechanic. Gaulteram's forgiveness is the exception.
- **Rank starts at C:** Rank starts at D. C was the effective floor with Lighteram equipped. With Chevalam there is no floor — hits can send Verso back to D.
- **Base Shield with Chevalam:** Non-functional — Chevalam prevents shields. Remove from loadout.
