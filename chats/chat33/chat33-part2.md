<!-- SECTION -->
## Lune Damage Rebuild — Choralim, Frenzy, Lightning Dance

**Matt:** I think we look at that with the full lumina question.

I think more important than Monoco is looking at Lune. I could give her some of the damage boosting Lumina that work well for Verso and Maelle, but without the At Death’s Door low-HP options. I could also give her Clea’s Life and Full Strength. But I don’t think that’s the whole picture on why her damage is much lower. Could you do some searches on Endgame Lune builds using Elemental Genesis and see how people get such high damage?

**Claude:** *[Turn 19. Last log: Turn 18.]*

Lune's file read. Let me now search for endgame Lune / Elemental Genesis builds.

*[Turn 19. Last log: Turn 18.]*

Good findings across those results. Let me separate what's clearly relevant to your build from what's noise.

**The core answer to "why is her damage lower"** comes from two distinct sources, one structural and one that appeared post-release:

**1. Elemental Genesis is an 8-hit AoE — it spreads damage.** Maelle's Stendhal is single-target. Against a boss, Genesis hits the boss 8 times but those hits are random-element and lower individual multiplier than a focused Lightning Dance or Stendhal. Lightning Dance outdamages Genesis against bosses unless the boss is Lightning-resistant. You're probably using Genesis against single bosses when Lightning Dance would hit harder — Lightning Dance does 6 hits (12 on crit) consuming three stains, with a much higher per-hit multiplier.

**2. Elemental Trick + Genesis is the meta setup, and you're not running Elemental Trick.** The core combo is Elemental Trick followed by Elemental Genesis — Lune gets two turns via Cheater, allowing the two skills to work immediately. This plan only works if Lune has max Critical Chance, because Elemental Trick generates the four stains Elemental Genesis needs only if Lune crits on every hit. Your current rotation generates stains across two skills (Terraquake + Lightning Dance or similar), which takes an extra turn. Elemental Trick as a one-turn full-stain loader is a genuine rotation upgrade — though you'd need to check it's in your skill list (it is, unequipped, and with 100% crit already confirmed, it would reliably give all 4 stains in one cast).

**3. Post-patch: Frenzy now works on Lune.** With Patch 1.5.0, you can use most of the damage-increasing Lumina that scale well with multiple skill hits, like Frenzy. Elemental Genesis is 8 hits, Lightning Dance is 6–12 — both are prime Frenzy targets. Frenzy wasn't viable on Lune before that patch. This may be the single biggest gap between your current build and an optimised one.

**4. Burn-stacking on Genesis is underexploited.** Your current Pictos (Critical Burn + Burn Affinity) are already oriented toward this, but pairing Frenzy with Bonbim to deal a lot of damage with Burn, then using a Lightning Skill, deals massive damage. I don't know what Bonbim does — worth a query.

**One flag before proceeding:** several guides recommend Choralim over Kralim as Lune's best endgame weapon — its Level 10 passive enhances Lumina that grant multiple turns, and its Level 20 passive ramps up damage especially with multi-hit skills like Lightning Dance. Your file already has Choralim listed as a future option but noted a circular dependency concern. Worth revisiting with the Elemental Trick approach, since Choralim's 100% crit condition (4 stains active) is met *before* Genesis fires, not relying on Choralim to generate the stains.

So the priority list for Lune looks like: swap Elemental Trick in (replacing one of the stain-gen skills); investigate Frenzy and whether it's in your Lumina pool; check Choralim; and look at Lightning Dance vs Genesis for single-boss fights. Want me to query Frenzy and the relevant Lumina from your data now?

---

**Matt:** Yes please

**Claude:** *[Turn 20. Last log: Turn 18.]**[Turn 20. Last log: Turn 18.]*

Good — Bonbim isn't in your data at all (probably a weapon, not Lumina), but the key things are here. The picture is clear:

**Frenzy (20 LP, obtained, unequipped)** — "Each successive Skill hit deals 10% more damage." This is the big one. Elemental Genesis is 8 hits, Lightning Dance is 6–12. On Genesis: hit 1 is baseline, hit 8 is +70%. On Lightning Dance with crits: hit 12 is +110%. The stacking is per-skill, so it resets each cast — but with multi-hit skills that's still a massive multiplier on the back end. **This is almost certainly the largest single gap in Lune's current build.** It's a Pictos with LP cost 20, not a Lumina — so it would replace one of her three current Pictos.

**Glass Canon (10 LP, obtained, unequipped)** — note the spelling is "Glass Canon" not "Glass Cannon" in your data. Same effect: +25% damage, +25% damage taken. Directly usable on Lune as she doesn't have the same HP-maintenance Lumina constraints that complicate it on Maelle.

**Feint (15 LP, obtained, unequipped)** — "Every 5th hit with a Skill deals 600% more damage." Intriguing on an 8-hit Genesis or 12-hit Lightning Dance, but the Barbapapa stack mechanic is unfamiliar to me and I'd want to understand how it works before recommending it.

Now the Pictos question. Lune currently runs: **Critical Burn** (crit 28%, speed 434) + **Burn Affinity** (crit 12%, speed 439) + **Breaking Death** (crit 24%, speed 586). Total crit from Pictos: +64%. Her Luck is 51, giving a base crit floor of roughly 26%. Total ~90% — so she's *under* 100% without a third crit source, and her file shows 102% measured, meaning Breaking Death's 24% is doing real work to cap her.

The problem: **Frenzy gives no crit** (just defence 1572, speed 557). Swapping it in means dropping one of the three crit Pictos and potentially falling under 100% crit, which breaks the Elemental Trick → Genesis combo that the community considers her core DPS pattern.

Let me check the arithmetic... The crunch is real. Lune's crit floor at 38% is lower than Verso's (5%) but much lower than Maelle's (41% from Luck 99), so she can't afford to drop any of her crit Pictos without falling well short of 100%. None of the three swaps work cleanly.

This actually resolves the **Choralim question** at the same time: Choralim's Level 4 gives 100% Critical Chance when 4 stains are simultaneously active. That's exactly when she fires Genesis. So swapping Kralim → Choralim and Breaking Death Pictos → Frenzy gives: Critical Burn (28) + Burn Affinity (12) + Frenzy (0 crit) = 50% from Pictos + 38% base = **88% without stains**, but Choralim's L4 pushes it to **100%+ the moment 4 stains are loaded** — which is the only moment she fires Genesis or Lightning Dance anyway. Outside that window she'd miss some crits, but Elemental Trick's stain generation from crits is the reason 100% matters, and with the Elemental Trick → Genesis one-turn combo the "outside the 4-stain window" state is mostly the setup turn.

So the path is: **Kralim → Choralim + Breaking Death → Frenzy.** But I want to be honest about two things I don't know: whether Choralim is obtained in your playthrough (it's in your file as "future options" with unknown Power — do you have it?), and what Choralim's Level is. The L10 and L20 effects are also relevant, not just L4.

Do you have Choralim, and if so what level is it?

---

**Matt:** That info is in data/weapons.json

I think you should also read reference/mechanics and overview/pictos-lumina-summary

**Claude:** *[Turn 21. Last log: Turn 18.]*

*[Fetched weapons.json, mechanics.md, pictos-lumina-summary.md]*

*[Read mechanics.md]*

*[Read pictos-lumina-summary.md]*

*[Queried Frenzy, Bonbim, and key damage Lumina from pictos-lumina.json — found Frenzy (20LP Pictos, obtained), Glass Canon (10LP), Feint (15LP, Barbapapa stacks), Bonbim (weapon L29); Licorum/Glass Cannon not found by that name]*

*[Searched all entries by keyword for burn/multi-hit damage Lumina]*

*[Turn 21. Last log: Turn 18.]*

Good — now I have the full picture. Several things become clear that I couldn't see before.

**Choralim is L20, obtained.** The circular dependency note in the file is now resolved: with Frenzy as a Pictos (no crit) + Critical Burn + Burn Affinity, she'd be at 78% crit outside the 4-stain window, but Choralim L4 pushes to capped exactly when it matters. And **Choralim L20: "Critical hits apply Burn"** — this is a significant find. On an 8-hit Genesis with 100% crit, every hit applies Burn. That makes Burn Affinity (×1.25) fire on every hit *within the same cast* from hit 2 onward, and seeds Critical Burn's crit bonus for subsequent turns.

**Bonbim is a weapon (L29, obtained).** Its effects: L4 +5% crit per Burn on target, L10 crit hits apply Burn, L20 Lightning skills consume up to 100 Burn for +2% damage per stack. This is a Burn-stacking weapon that synergises with Lightning Dance specifically — but Lune needs Kralim or Choralim for stain generation/Genesis, so Bonbim likely isn't the right weapon unless you're running a pure Lightning Dance boss build. Lower priority than the Choralim switch.

**Frenzy is already on the main team's Verso additions list** (20 LP, added). So the question of whether it stacks with multi-hit skills is settled in your playthrough — you've already committed to it on Verso. That's strong evidence it works well on multi-hit skills, and Genesis + Lightning Dance have comparable or higher hit counts.

Now the key question is Lune's LP budget, because the Choralim switch removes Kralim's L20 (+1 AP on stain consumption), which is currently funding part of her AP loop. Let me check...

*[Turn 21. Last log: Turn 18.]*

Right, let me bring this together clearly.

**The proposed changes for Lune:**

**1. Weapon: Kralim → Choralim (L20)**
The "circular dependency" note in the file is now resolved: with Frenzy as a Pictos (no crit stat) + Critical Burn + Burn Affinity, she sits at 78% crit outside the 4-stain window — but Choralim L4 pushes her to capped exactly at the moment she fires Genesis or Lightning Dance (when 4 stains are loaded). The three Choralim effects are all live:
- L4: 100% crit when 4 stains active → eliminates crit dependency problem
- L10: +20% damage per consecutive turn without taking damage, stacks to 5 — real upside in reserve entry (she enters fresh, hasn't been hit)
- L20: crit hits apply Burn → on an 8-hit Genesis, all 8 hits apply Burn, feeding Burn Affinity within the same cast from hit 2 onward

The cost is losing Kralim L20 (+1 AP per stain consumption). That's a real AP hit — Elemental Trick + Genesis in one Cheater combo consumes stains twice (once on each cast), so she loses ~2 AP per Genesis turn. Worth modelling whether that breaks her AP loop, but with Energy Master (+1 to every AP gain) and AP Discount (−1 skill cost) she should absorb it.

**2. Pictos: Breaking Death → Frenzy**
Breaking Death effect paid as 5 LP Lumina instead. Net cost: +5 LP. Frenzy becomes free. The payoff on Genesis (8 hits) is +10% per successive hit: hits 1–8 deal 100/110/120/130/140/150/160/170% — average ~135% vs 100% baseline, roughly a ×1.35 multiplier on the whole cast. On Lightning Dance (6 hits, 12 with crits): +110% on the last hit. This is large.

**3. Consider Glass Canon (10 LP, obtained)** — +25% damage, +25% damage taken. Lune doesn't have health-maintenance Lumina constraints like Maelle, and the reserve role means she often enters mid-fight. The incoming damage penalty is a real risk in that context — but with Base Shield + Second Chance + Survivor in the core set she has more cushioning than the main team. Worth adding once you're comfortable with the Choralim build.

One thing I want to flag honestly: I haven't verified whether Choralim's L4 crit fires specifically during the Genesis hit sequence, or only at cast time. If it checks "4 stains active" at cast initiation, all 8 hits benefit. If stains are consumed mid-cast and it checks per-hit, later hits might lose the crit. This is the kind of interaction worth testing before fully committing — though your existing 102% crit with current Pictos would still cover partial misses.

Also I haven't yet thought about **Elemental Trick** as the rotation enabler — that's worth discussing separately. Currently it's in her skill list (unequipped). Do you want to look at that now, or work through the weapon/Pictos changes first?

---

**Matt:** Ok, a few things:

1. Pictos effects can be applied as either Pictos or Lumina. There’s no reason she can’t have Frenzy as a Lumina and keep above 100% Crit.

2. I’m still not convinced about Choralim. L4 gives 100% Crit in certain situations, but she already has 100% Crit all the time. L10 gives bonus when not taking damage, which is focused on a high-success parry playstyle. L20 applies burn that feeds burn affinity, but so do Hell and other burn skills that she already has.

3. I’m not convinced you’ve handled the circular dependency. The issue was that Choralim was recommended for Elemental Trick as 100% Crit would create all four elemental stains, but it only gives 100% after there are four stains already. EG requires four stains, so when ready for EG then it will give 100%, but it doesn’t help with the setup. And I already have 100% anyway from Pictos.

4. Building Lune to 100% and using ET to generate the four stains is a quicker setup for EG, but doesn’t affect the damage level. The key question is getting more damage from her. Frenzy and Lightning Dance are part of the answer, but I thought there would be more to it. Burn Affinity only does more damage if burning, right? So not burn stacking.

**Claude:** *[Turn 22. Last log: Turn 18.]*

All four points are correct — let me take them properly.

1. **Frenzy as Lumina** — you're right, I overcomplicated it. 20 LP, obtained, she buys it as Lumina, keeps all three crit Pictos, stays capped. Simple.

2 & 3. **Choralim** — agreed on all counts. L4 gives nothing she doesn't already have. L10 is a parry-playstyle bonus that doesn't fit reserve entry. L20's Burn application is redundant with Hell and other existing sources. And the circular dependency isn't resolved — it was never the problem I claimed it was solving. Choralim is out. Kralim stays.

4. **Burn Affinity** — you're right to push back on that too. It's ×1.25 on burning targets, which is already in her loadout. It's not scaling with burn stack count; it's a flat conditional multiplier she's already getting. So that's not a gap — it's already captured.

So let me reframe the actual damage gap from scratch, looking at what Verso and Maelle have that Lune doesn't...

That makes the gap very concrete. Lune currently has essentially **one damage multiplier** (Burn Affinity, which she's already getting). Maelle and Verso stack five or six. The candidates to close the gap:

**Clear additions — no conditions that conflict with her build:**

**Frenzy (20 LP)** — the biggest win. 8-hit Genesis: average ~135% vs baseline. 12-hit Lightning Dance with crits: even better. No condition, works immediately.

**Confident Fighter (15 LP)** — +30% damage, can't be healed. The healing restriction matters less for Lune than for Maelle since she heals *herself* via Healing Light — that would be blocked. So this is usable but it disables her own healing, which is part of her reserve role. Situational — DPS fights yes, fights where she needs to heal the team, no.

**Augmented First Strike (5 LP)** — +50% on the first hit of the battle. Cheap, no condition beyond "first hit." Easy addition.

**Full Strength (15 LP)** — +25% at full HP. In reserve entry she typically comes in at full HP. Synergises cleanly with her entry timing. No conflicts.

**Glass Canon (10 LP)** — +25% damage, +25% taken. As discussed — real upside, real risk in reserve.

**The harder question you're right to raise: is there a bigger structural lever?**

Looking at Verso and Maelle's real edge, it's not just Lumina stacking — it's the **Steeled Strike / Stendhal multiplier on the payoff skill itself.** Verso's Steeled Strike and Maelle's Stendhal both have intrinsically higher damage multipliers per AP than Elemental Genesis. Genesis is 8 hits at a moderate per-hit multiplier. Lightning Dance is 6–12 hits with a ×5 stain consumption bonus — that's the better single-target comparison and is already in her kit. Are you using Lightning Dance against bosses, or Genesis? That single skill choice may account for more of the gap than all the Lumina combined.

---

**Matt:** I have tended to use Lightning Dance earlier, without the three-stain bonus. I had no idea it was a x5 multiplier! That's a game changer. Together with Frenzy, Double Third, Glass Canon, Full Strength (kept up by Clea's Life) and possibly Feint as well, that's a lot of multipliers. That x5 stain bonus is the equivalent of Maelle's x3 Virtuose or Verso's Rank S (possibly x4? I can't remember).

**Claude:** *[Turn 23. Last log: Turn 18.]*

Yes, that's the core of it. Let me pull the exact multipliers to compare properly.

*[Calculated Frenzy (×1.55 avg on 12 hits), Double Third (×1.33 avg on 12 hits), combined Frenzy + Double Third (×2.10 avg)]*

*[Turn 23. Last log: Turn 18.]*

The comparison lands well. Lightning Dance's ×5 stain bonus is genuinely in Maelle/Verso territory — and unlike Virtuose or Rank S it applies to *every* hit across 12 hits, not a single nuke. Frenzy and Double Third then multiply on top of that ×5 base, giving a combined ×2.10 average across the cast. So the full Lightning Dance payoff is roughly:

**base hit × ×5 (stains) × ×2.10 (Frenzy + Double Third avg) = ×10.5 effective multiplier on a full 12-hit consumed cast.**

That's comparable to Maelle's setup — and she's doing it across 12 hits rather than one, which matters for Frenzy ramping.

On Verso's Rank S: I haven't loaded his file this session so I won't assert the exact value, but your ×4 recollection is plausible from what I've seen previously. Lightning Dance isn't quite Verso's single-hit ceiling, but it's 12 hits which is a very different damage distribution.

**One thing to verify before committing to this:** Frenzy and Double Third — do they interact additively or multiplicatively? The calculation above treats them multiplicatively (Frenzy applies to each hit's value, then Double Third doubles the 3rd-hit result including its Frenzy bonus). If they're additive (both bonuses summed before applying to base), the combined multiplier would be lower. Your existing Verso data may already confirm this — he has Frenzy on Steeled Strike (13 hits), so you can observe whether Double Third compounds or adds.

**On Feint:** "Every 5th hit deals 600% more damage, Barbapapa stacks." I flagged uncertainty about Barbapapa stacks last turn and still don't know what they are — I'd want to look that up before recommending it. On 12-hit Lightning Dance, hits 5 and 10 would trigger it, so two ×600% hits. That's enormous if it compounds with Frenzy, but the Barbapapa mechanic is the unknown.

**On Full Strength + Clea's Life:** Good catch — Clea's Life restores to full HP on turn start if no damage taken, so Full Strength (+25%) should be permanently active on Lune in most reserve fights where she's entering clean. That's a clean, no-condition multiplier.

So the build shape is becoming: **Lightning Dance (3-stain consumed) + Frenzy + Double Third + Full Strength + Glass Canon + Augmented First Strike** — with Confident Fighter switchable in for fights where her healing isn't needed. Want me to check Feint/Barbapapa from a web search, then look at LP budget for all of these together?

---

**Matt:** Barbapapa means your first hit with a skill does 1 point of damage, which is effectively zero. So Feint does zero damage for the first four hits, then x6 for the fifth hit, then later hits as usual. With Frenzy, that x6 on the fifth hit is more powerful because the fifth hit is already multiplied by Frenzy. But it means that skills with less than five hits do zero damage.

**Claude:** *[Turn 24. Last log: Turn 18.]*

That's a nasty tradeoff. Let me work out whether it's worth it on Lightning Dance.

*[Turn 24. Last log: Thread 18.]*

**Feint is worth it on 12-hit Lightning Dance — a +74.6% gain over Frenzy + Double Third alone.** The zero first hit costs you ×1.0, but hits 5 (×9.80) and 10 (×13.30) more than compensate. The Frenzy ramp makes Feint dramatically better the later the ×7 trigger fires — hit 5 at ×1.4 frenzy is already strong, hit 10 at ×1.9 frenzy is enormous.

But — and this is the constraint — **Feint resets per skill cast, and hit 1 of every skill does zero.** That makes it worthless on Genesis (you'd be casting it as a setup skill into Lightning Dance, which is fine — Genesis still does damage on hits 2–8) but it means any skill with fewer than 5 hits essentially does no damage with Feint equipped. In Lune's current skill set that affects Thermal Transfer (2 hits), Terraquake (1 hit AoE + DoT), and Healing Light (0 damage). Those are mostly setup/utility skills so the practical cost is low — but it's worth being aware that Terraquake's initial AoE hit goes to zero, leaving only the DoT component.

One firm caveat: **Feint has 66% crit on its stats block.** That means equipping it as a Pictos pushes crit well over cap and potentially displaces a crit Pictos. But you've already established Frenzy works as Lumina — so does Feint. At 15 LP it's affordable, and as Lumina you get the effect without touching the Pictos slots.

So the proposed Lightning Dance build for Lune shapes up as:

| Lumina | LP | Note |
|---|---|---|
| Frenzy | 20 | ×1.55 avg across 12 hits |
| Double Third | 10 | ×1.33 avg, compounds with Frenzy |
| Feint | 15 | +74.6% on top of the above |
| Full Strength | 15 | ×1.25, maintained by Clea's Life |
| Glass Canon | 10 | ×1.25, +25% taken |
| Augmented First Strike | 5 | ×1.5 on first battle hit |

That's 75 LP of additions. Want to check whether that fits her budget, and look at whether any of her current Lumina should come out to make room?

---

**Matt:** You’ve not quite got Feint right, I don’t think.
- Hits 1,2,3,4 — x0
- Hit 5 — x6
- Hit 6+ — x1

**Claude:** *[Turn 25. Last log: Turn 18.]*

Ah — the Barbapapa stacks don't reset per hit, they drain four charges meaning hits 1–4 are all zero, not just hit 1. Let me redo the calculation...

*[Turn 25. Last log: Turn 18.]*

The conclusion flips entirely. Losing hits 1–4 is devastating — Feint on 12-hit Lightning Dance is only **+4.8%** over Frenzy + Double Third alone. That's not worth a Lumina slot. And without Double Third it's actually a **−16.7% net loss** — Feint actively hurts there.

The core problem: hits 1–4 contribute 0, but with Frenzy those are hits at ×1.0 through ×1.3 — not huge individually but together they're 4.6× base damage you're simply throwing away. Hit 5's ×8.40 barely covers what you lost.

Feint only makes sense on Lightning Dance if the rest of the skill were fewer hits — or on a skill with a very high per-hit base multiplier where the ×6 spike lands on a hit that already has a large multiplier. On a 12-hit skill, you're sacrificing too much of the Frenzy ramp.

**Feint is out.** The build without it is cleaner and substantially stronger:

| Lumina | LP | Avg multiplier contribution |
|---|---|---|
| Frenzy | 20 | ×1.55 across 12 hits |
| Double Third | 10 | ×1.33, compounds with Frenzy |
| Full Strength | 15 | ×1.25 flat |
| Glass Canon | 10 | ×1.25 flat |
| Augmented First Strike | 5 | ×1.5 on first battle hit |

That's 60 LP of additions. Confident Fighter (15 LP, ×1.30) is the optional extra for fights where she won't need to self-heal. Want to check her LP budget to see what fits?

---

**Matt:** Confident Fighter isn't compatible with Full Strength. I'd like to give her Clea's Life as well, but that is 30LP. Is it possible to give her the Clea's Life Pictos without bringing her Crit below 100%?

**Claude:** *[Turn 26. Last log: Turn 18.]*

Good catch on Confident Fighter — can't be healed blocks Clea's Life's full-HP restore, so they're mutually exclusive. Let me check the Clea's Life Pictos question.

*[Checked crit impact of swapping each Pictos for Clea's Life:]*

*[Turn 26. Last log: Turn 18.]*

Unfortunately no — she can't hold Clea's Life Pictos and stay at 100% crit. The closest is dropping Burn Affinity (12%), which leaves her at 99% — one point short. All three swaps fall under.

However, there's a compound benefit here worth flagging: **Maelle is moving to the At Death's Door build, which actively wants to be at low HP — Clea's Life is the wrong Pictos for her anyway.** So Maelle needs to vacate that slot regardless. The question is just whether Lune can absorb it.

The resolution is the same one you used for Frenzy: **Clea's Life as Lumina (30 LP)** rather than Pictos. Lune keeps all three crit Pictos (stays at 111%), gets the full-HP restore effect, and pays 30 LP. Full Strength then fires reliably every turn.

Two things that follow from that:

**Maelle's vacated Pictos slot** — with Clea's Life out and the At Death's Door build confirmed, what goes in that slot? The two candidates from the earlier Turn 7 layout were Energising Turn (already in slot 3 as you've confirmed) and Energy Master. But you've settled Maelle's Pictos as Empowering Break / Shortcut / Energising Turn, so that slot is already filled. Clea's Life just comes out entirely from Maelle.

**Lune's LP budget** — she's now looking at adding: Frenzy (20) + Double Third (10) + Full Strength (15) + Glass Canon (10) + Augmented First Strike (5) + Clea's Life (30) = **90 LP** of additions on top of her current 260 LP load = **350 LP total**. With ~200 CoL available and her pool presumably needing expansion, that's achievable but worth confirming. Want me to check the full budget now?

---

**Matt:** I gave you a list of Maelle's Pictos earlier.

I'll look for some good Pictos for Lune in-game.

!log

**Claude:** *[Turn 27. Last log: Turn 26 (this log).]*

You're right — Maelle's Pictos are already settled as Empowering Break / Shortcut / Energising Turn from Turn 18. I shouldn't have re-raised it. Logging now... Logged — Turns 19–27 appended, transcript now at 629 lines. Last logged turn is **Turn 27**.

*[Turn 27. Last log: Turn 27.]*

While you're looking for Pictos in-game, the open threads ready to pick up when you're back:

- Lune's LP budget check (to confirm 350 LP is feasible with available CoL)
- Whether to swap Elemental Trick in as the stain setup skill
- Lune's Lumina loadout written up formally for the data update

What would you like to tackle next?

---

<!-- SECTION -->
## Lune Rotation, AP Loop, and Finalised Lumina List

**Matt:** The thing with Elemental Trick is that it doesn’t do much damage. With Kralim, I start with two random stains. They are very rarely the same. If there is no fire stain from Kralim, I do Hell, which does a lot of damage and applies burn. If there is fire but no earth, I do Terraquake, which does a bit of damage every turn and boosts break damage. If there is both fire and earth, I currently do Lightning Dance, but I would hold off that and use it as the payoff skill, and use something like Thermal Transfer instead. After that, I have four different stains, except in the very unlikely scenario that both Kralim stains are the same. I don’t see how Elemental Trick improves that situation much.

**Claude:** *[Turn 28. Last log: Turn 27.]*

That's a well-reasoned rotation and I think you're right — Elemental Trick doesn't improve it. Your Kralim-seeded setup already reaches four stains in one cast (Hell or Terraquake depending on what's missing), so Elemental Trick is solving a problem you don't have. It would only win if Kralim's two random stains were frequently the same — which you've observed is rare. Elemental Trick is out.

One thing your rotation description surfaces that I hadn't appreciated: **Hell is doing real damage work as a setup skill**, not just seeding the burn condition. That's relevant to the Clea's Life question — Clea's Life restores full HP on Lune's turn if she took no damage, which keeps Full Strength active. But does Lune typically take damage in the turns before she fires Lightning Dance? In reserve entry she comes in fresh, so the first full rotation should be clean. The risk is fights where she's been on field for multiple turns and takes incidental hits.

The other thing your rotation clarifies: **the Choralim question is definitively closed.** Kralim's L10 (+1 AP on stain consumption by a skill) fires on Hell (consumes fire stain? — actually I'm not certain Hell *consumes* a stain vs *adds* one, I shouldn't assert that) and on Lightning Dance (consumes three stains = +3 AP). That AP is what funds the rotation. Choralim has no equivalent AP generation, and with Lune's AP loop already tight after removing Kralim's L20, switching weapons would break it.

Actually — let me flag that uncertainty clearly. Does Hell *consume* the fire stain or *add* one? If it adds fire, Kralim's L10 doesn't fire on it. If it consumes, it does. That affects how much AP the rotation actually generates and whether the loop is as tight as I'm assuming.

---

**Matt:** Hell adds a stain. It can consume three stains, but there are only two when I use it. I think Lune has Energising Burn to generate AP on Burn application through Hell.

**Claude:** *[Turn 29. Last log: Turn 27.]*

That makes sense — so the AP loop on the setup turn is: Hell adds fire stain + applies Burn → Energising Burn fires (+1 AP). Kralim L10 isn't contributing on that turn since nothing is consumed. The AP from Kralim L10 lands on the payoff turn: Lightning Dance consumes three stains = +3 AP, which funds the next cycle.

So the loop is self-sustaining: setup turn generates +1 AP from Energising Burn, payoff turn generates +3 AP from Kralim L10. That's actually a clean loop and confirms Kralim is the right weapon — Choralim would lose the +3 AP on the payoff turn entirely, which would be crippling.

On the rotation, one thing I want to check before we finalise the Lumina list: **Double Third on Lightning Dance.** The skill does 6 base hits, with crits triggering an additional hit each — so 12 hits with 100% crit. Double Third fires on hits 3, 6, 9, 12. But I want to flag I'm not certain whether the "additional hit from crit" counts as hits 7–12 in sequence, or whether they interleave differently. If the crit hits are treated as a separate burst rather than extending the sequence, Double Third might not fire on hits 9 and 12 as I assumed. Worth a quick in-game check — equip Double Third, fire Lightning Dance, and see if damage noticeably spikes on the later hits.

Other than that, is the Lumina additions list settled for Lune? To confirm what we've landed on:

| Lumina | LP |
|---|---|
| Frenzy | 20 |
| Double Third | 10 |
| Full Strength | 15 |
| Glass Canon | 10 |
| Augmented First Strike | 5 |
| Clea's Life | 30 |

90 LP of additions. Want me to check her current LP load and available CoL budget now?

---

**Matt:** Ok, so I swapped some Pictos around with Sciel.

- Lune: Clea's Life, Quick Break, Rush On Powerful => Health 9400, Speed 2543, Crit 100%
- Sciel: Energy Master, Breaking Death, Powerful Revive => Health 7390, Speed 2406, Crit 106%

**Claude:** *[Turn 30. Last log: Turn 27.]*

Good. Let me check the speed picture with these changes.

*[Recalculated speed order with updated Sciel and Lune Pictos]*

*[Turn 30. Last log: Turn 27.]*

The speed picture looks good. Main team order is now **Maelle > Verso > Sciel** naturally — which is exactly what you settled on, with Sciel last to react with Intervention. The Verso-Sciel gap is 213 points, which is tighter than before but still enough separation for Rush effects to keep them distinct rather than alternating unpredictably.

Lune sitting at 2543 is fine for a reserve character — her entry timing is driven by Intervention/Revive rather than natural order.

A few things to note on the Pictos changes:

**Lune** — Clea's Life Pictos gives health 9400 which is a substantial survivability boost for reserve entry, and Rush On Powerful's effect (Rush when applying Powerful) is live for her since Painting Power applies Powerful. Quick Break gives crit 36 + speed — but as we noted, Quick Break's retrigger effect is dead with Cheater. It's purely a stat stick here. Crit check: she's now at 100% exactly — any rounding or in-game calculation quirk that puts her fractionally under would matter. Worth keeping an eye on whether crits are landing 100% of the time in practice.

**Sciel** — Powerful Revive (apply Powerful for 3 turns when revived) is interesting given your observation that characters die and get revived multiple times against the Chromatic Lampmaster. In a fight like that, Sciel could be getting free Powerful on every revive. That's a genuine upside. Breaking Death free from Pictos saves LP. Speed drops from 2572 to 2406 — still behind Verso, which is correct.

Ready to check Lune's LP budget and then move to the Lumina additions?

---

**Matt:** Yes, now that Clea's Life is Pictos that saves us 30LP.

**Claude:** *[Turn 31. Last log: Turn 27.]*

*[Calculated Lune's full LP budget with new Pictos and proposed additions]*

*[Turn 31. Last log: Turn 27.]*

Comfortable — she needs 60 additional CoL, well within the 132 available. That leaves 72 CoL for the other characters.

One thing I need to flag: the current total came out at 280 LP rather than the 260 I estimated in Turn 21. The difference is that Burn Affinity (15 LP) and Critical Burn (5 LP) were previously free from her old Pictos — they're now paid Lumina since the new Pictos don't cover them. So the Clea's Life Pictos saving is partially offset by losing those two freebies: net change is −30 (Clea's Life free) +20 (Burn Affinity + Critical Burn now paid) = **−10 LP net saving** vs the Turn 26 estimate. Still very manageable.

So the final Lune additions to action:

| Lumina | LP |
|---|---|
| Frenzy | 20 |
| Double Third | 10 |
| Full Strength | 15 |
| Glass Canon | 10 |
| Augmented First Strike | 5 |
| **Total** | **60 LP / 60 CoL** |

Clea's Life free from Pictos. Total load 340 LP, 241 CoL spent on Lune in total.

Ready to move on — Monoco, Lumina review for the other characters, or the core set rethink?

---

**Matt:** Can you show me the full list of Lumina for Lune after these changes?

**Claude:** *[Turn 32. Last log: Turn 27.]*

*[Generated full Lune Lumina list in bash]*

*[Turn 32. Last log: Turn 27.]*

Here's the full list. A few things worth eyeing:

**AP Discount (30 LP)** — this is her single most expensive addition. Worth confirming it's still pulling its weight now that she's pivoting to Lightning Dance as the payoff skill rather than Genesis. If Lightning Dance's AP cost is already manageable through Kralim L10 (+3 AP on consumption) + Energising Burn (+1 AP on burn), this might be a candidate to trim if CoL becomes tight elsewhere.

**Energy Master (40 LP)** — second most expensive. Amplifies every AP gain, so it multiplies the value of Energising Burn and Kralim L10. Justified given the AP-hungry rotation.

**Accelerating Heal (5 LP)** — "healing an ally applies Rush for 1 turn." Low cost but worth confirming it still fits Lune's role. If she's primarily DPS with self-healing via Healing Light, the ally-Rush trigger may rarely fire.

**Dead Energy I + II (2 LP each)** — worth checking what these do; I don't have the effects to hand and want to flag rather than assume they're still relevant.

Everything else looks clean. Want to proceed to Monoco, or go straight to the Lumina review for Maelle and Verso?

---

**Matt:** Sorry, I don't see the full list from the tool output. That doesn't come through to me automatically.

**Claude:** *[Turn 33. Last log: Turn 27.]*

Here it is written out:

**Reserve Core**
- Painted Power — 5 LP
- Energising Turn — 20 LP
- Cheater — 40 LP
- Shortcut — 5 LP
- Teamwork — 5 LP
- Energising Start I — 5 LP
- Dodger — 1 LP
- Breaking Burn — 5 LP
- Base Shield — 20 LP
- Second Chance — 40 LP

**Existing Additions**
- AP Discount — 30 LP
- Accelerating Heal — 5 LP
- Breaking Attack — 10 LP
- Burn Affinity — 15 LP *(was free from old Pictos)*
- Critical Burn — 5 LP *(was free from old Pictos)*
- Energy Master — 40 LP
- Dead Energy I — 2 LP
- Dead Energy II — 2 LP
- Energising Burn — 10 LP
- First Strike — 10 LP
- Protecting Heal — 5 LP

**New Additions**
- Frenzy — 20 LP
- Double Third — 10 LP
- Full Strength — 15 LP
- Glass Canon — 10 LP
- Augmented First Strike — 5 LP
- Clea's Life — free *(from Pictos)*

**Total: 340 LP**

---

**Matt:** Could you do me just the full list of names in alphabetical order, no extra detail.

**Claude:** *[Turn 34. Last log: Turn 27.]*

- Accelerating Heal
- AP Discount
- Augmented First Strike
- Base Shield
- Breaking Attack
- Breaking Burn
- Burn Affinity
- Cheater
- Clea's Life
- Critical Burn
- Dead Energy I
- Dead Energy II
- Dodger
- Double Third
- Energy Master
- Energising Burn
- Energising Start I
- Energising Turn
- First Strike
- Frenzy
- Full Strength
- Glass Canon
- Painted Power
- Protecting Heal
- Second Chance
- Shortcut
- Teamwork

---

**Matt:** !log

**Claude:** *[Turn 35. Last log: Turn 34 (this log).]*

Logged — Turns 28–35 appended, transcript now at 703 lines. Last logged turn is **Turn 35**.

*[Turn 35. Last log: Turn 35.]*

Where to next — Monoco, Maelle/Verso Lumina review, or the core set rethink?

---

