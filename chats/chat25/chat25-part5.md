<!-- SECTION -->
## Maelle — Web Search and Greater Powerful Addition

**Matt:** Ok then. Just to finish off on Maelle, can you do a web search on endgame builds with Lithum and see if there are any Lumina we've missed. I think a lot of the endgame builds are burn-stacking, so those ones won't be that relevant.

**Claude:** *[Turn 47. Last log: Turn 45.]*

*[web_search: Lithum Maelle build Lumina endgame non-burn Virtuose Stendhal]*  
*[web_search: Expedition 33 "Critical Moment" "Augmented Attack" "First Offensive" Lumina effects]*

A few hits to follow up. The Glass Almanac mentions "Full Power, Overcharged Power, and Initiation" as instant-buff Lumina I should check, and "Critical Moment" is mentioned for crit damage. Let me search for those specific Lumina to see if they exist in the data.

Useful new candidates found. Let me also flag one important community finding: **First Strike is party-wide, not per-character** — "First strike works so that the entire party always goes first, does not effect turn order." Verso already has Augmented First Strike, which appears to be different (a first-hit damage boost, not a turn-order effect). Worth keeping that distinction in mind.

**Endgame Lumina candidates for Maelle that came up, filtered for non-burn and ones we haven't already considered:**

| Lumina | LP (per data) | Effect | Worth adding for Maelle? |
|---|---|---|---|
| **Critical Moment** | 5 (per JSON) | +50% damage when target HP <10% | Only fires on low-HP targets. Could be strong on Stendhal finishing hits but situational. Maelle's burst usually one-shots before <10% phase. |
| **First Strike** | 1 | Party goes first at battle start | Party-wide effect, not per-character. If anyone has it, the party benefits. **Worth checking if anyone already has it** — if not, putting it on Maelle (cheap at 1LP) is free turn-order dominance. |
| **At Death's Door** | 5 | +50% damage when HP <10% | Maelle's Last Chance rotation drops her to 1HP — this would fire reliably during her Cheater bonus turn. **Strong fit.** |
| **Powered Attack** | unknown | (cited in lists, can't find effect) | Need to verify |
| **Immaculate** | unknown | +30% damage until hit is received | Maelle stays untouched in Last Chance loop (Clea's Life heals + Cheater turn before damage). Could be strong but conditional on not getting hit between fully-healed states. |
| **Glass Canon** | 10 | +25% damage, +25% damage taken | **Conflicts with Maelle's defensive setup** (Clea's Life relies on no-damage turns to fire). Probably skip. |
| **Greater Powerful** | unknown | +15% to Powerful damage increase (Powerful becomes 40% not 25%) | Only fires when Powerful is active. With Empowering Break setup this matters. |
| **Longer Powerful** | unknown | Extends Powerful duration | Same dependency on having Powerful. |
| **Augmented Attack** | unknown | +damage on Base Attack | Maelle doesn't base attack in current build. Skip. |
| **Empowering Attack** | unknown | Similar | Skip same reason. |

**Three stand out:**

1. **At Death's Door (5LP):** Maelle is at 1HP during her Cheater bonus turn from Last Chance, before Clea's Life heals her at turn start. Wait — Clea's Life triggers *at the start of* the Cheater turn, so by the time Stendhal fires she's already at 100%. So At Death's Door wouldn't fire on her Cheater turn Stendhal. **Re-checking carefully:** the sequence is: Last Chance (HP→1) → Cheater bonus turn starts → Clea's Life triggers (HP→100%) → Maelle plays. So by the time she casts Stendhal, HP is already full. **At Death's Door does NOT fire reliably in her current rotation.** Skip.

2. **First Strike (1LP):** I should check whether any current team member has First Strike Lumina equipped. Looking through the data — no one has it. **This is a 1LP add that gives the entire party first-action at battle start.** This is genuinely free value, and fits Maelle's spare 2LP exactly.

3. **Critical Moment (5LP):** +50% damage at <10% target HP. Doesn't fit Maelle's burst pattern. Skip.

**Suggestion: First Strike (1LP) for Maelle, using 1 of her 2 spare LP.**

The other 1LP can stay unfilled, or — if I check more carefully for 1LP options Maelle doesn't have:

Looking at the JSON for 1LP Lumina:
- Solo Fighter (1LP) — has it
- Break Specialist (1LP) — Maelle isn't a breaker; -20% damage penalty is bad
- Healing Tint Energy (1LP) — marginal
- Dodger (1LP) — has it

**Final: First Strike (1LP) + leave 1LP unfilled** is the cleanest play. Or just take First Strike and accept 1LP unfilled.

Want me to write that up as an action, or is the 1LP First Strike not worth the extra slot?

---

**Matt:** I was thinking of spending CoL if there was something worth getting. Greater Powerful and Longer Powerful would trigger on Break, and there can be several Breaks in a long boss battle. Can you look up the LP cost online for those two? Also, I can't believe First Strike is 1LP. That must be a mistake. Can you search to verify please?

**Claude:** *[Turn 48. Last log: Turn 45.]*

Good calls on both. Let me verify all three.

*[web_search: "Greater Powerful" Lumina points cost Expedition 33]*  
*[web_fetch: https://expedition33.wiki.fextralife.com/Greater+Powerful]*

**Greater Powerful confirmed: 10 LP.** Drops from Klaudiso in Sirene for 37,100 Chroma — would need to verify whether you already have this Pictos.

Now Longer Powerful and First Strike:

*[web_search: "Longer Powerful" Lumina cost LP Expedition 33 wiki]*  
*[web_fetch: https://expedition33.wiki.fextralife.com/Longer+Powerful]*

**Longer Powerful confirmed: 10 LP.** Effect: "On applying Powerful, its duration is increased by 2." Drops from Mandelgo in Old Lumiere for 20,400 Chroma.

Now First Strike — you suspected the 1LP figure was wrong:

*[web_fetch: https://expedition33.wiki.fextralife.com/First+Strike]*

The Fextralife page didn't render the table for First Strike's LP cost (the page is short and lacks the standard info block in the rendered text). But the forum comments reveal a wiki dispute: "Wiki is wrong, this is level 7" — referring to Pictos level, not LP cost. Let me check another source for the LP cost directly.

*[web_fetch attempt to expedition33hub.com — permission denied]*  
*[web_search: "First Strike" lumina points cost expedition 33 "20 LP"]*  
*[web_search: "First Strike" pictos "Lumina Points Cost" expedition 33 wiki]*

All three confirmed. Summary:

| Lumina | LP cost | Notes |
|---|---|---|
| **Greater Powerful** | 10 | +15% to Powerful damage (becomes ~40% total). Confirmed works with Powerful on Shell, but more relevantly for Maelle — works with Powerful from Empowering Break. From Klaudiso in Sirene (37,100 Chroma). |
| **Longer Powerful** | 10 | +2 turns to Powerful duration. Confirmed works with Powerful on Shell. From Mandelgo in Old Lumiere (20,400 Chroma). |
| **First Strike** | **10** (not 1) | "Play first" — character with this Pictos/Lumina acts first in battle, *unless* an enemy or party member has higher Speed. Pictos lost its hidden +10% damage in Patch 1.5.0. |

**You were right to push back on First Strike — it's 10LP, not 1LP. Apologies for the data error.** I should flag this for `pictos-lumina.json` correction.

**On First Strike caveat:** "Characters with a higher Speed stat in the current Party will still go first." There's also significant community discussion about it being inconsistent and turn-order being determined by party order when multiple characters have it. Worth knowing before committing 10LP.

**Costs for the Powerful-extension package:**

- Greater Powerful: 10LP
- Longer Powerful: 10LP
- Total: 20LP

Maelle currently has 2LP spare. To fit both, she needs **18 CoL**. To fit just one of them, **8 CoL**.

**Analysis for Maelle specifically:**

- **Greater Powerful (10LP):** When Maelle triggers Empowering Break (her own Break → Powerful), the Powerful effect goes from +25% to +40%. On Stendhal in Virtuose + Powerful + Broken: that's ×3 × 1.40 × 1.20 = **×5.04** instead of ×4.5. About 12% damage uplift on the burst Stendhal.
- **Longer Powerful (10LP):** Adds 2 turns to Powerful duration. Default Powerful duration is 3 turns. With +2, becomes 5 turns. Useful if Maelle Breaks early in a fight and wants Powerful active for a later Cheater-turn burst. Less critical for the immediate Break→Cheater→Stendhal chain (Powerful is already active that turn) but valuable for repeated Powerful applications across a long boss fight where you'd otherwise re-apply.

**Greater Powerful is the higher-impact pick** because it directly multiplies the damage on the burst turn. Longer Powerful only helps if you have a separate damage opportunity within the extended window — which is possible across multiple Cheater rotations in a long fight, but less direct.

**Recommendation: Greater Powerful (10LP) for 8 CoL.** Skip Longer Powerful unless you're committed to spending more CoL — the 12% Stendhal uplift is meaningful on a burst that's already in the millions of damage. Longer Powerful is a smaller incremental win.

**ACTION:** Correct First Strike Lumina cost in `data/pictos-lumina.json` (currently 1LP, should be 10LP)

Want to commit to Greater Powerful for Maelle? Or hold pending the Section 6 review and consider all CoL spend together at end of session?

---

**Matt:** The search results suggests that the earlier claim about First Strike affecting the whole party is wrong. I think you might have conflated two effects — when entering an encounter, you can click a button to trigger party-wide First Strike. That doesn't work in most boss fights. The First Strike Lumina I think only pushes the current character to the top.

**ACTION:** Spend 8 CoL to increase Maelle's LP pool to 308, then add Greater Powerful.

!log

**Claude:** *[Turn 49. Last log: Turn 45. Logging turns 46–49.]*

You're right — I did conflate two effects. The "click R1/triangle to ambush" pre-combat advantage triggers party-wide First Strike. The Lumina/Pictos is per-character, pushing only the holder to the top (subject to Speed and turn-order rules). My Turn 47 framing of "First Strike is party-wide" was wrong, drawn from one comment that conflated the two systems.

Also flagging: my Turn 47 "First Strike (1LP)" data point came from the JSON, which is the error I noted in Turn 48. Apologies for compounding errors there.

Logged turns 46–49 (143 lines added) with section marker before Turn 46. File at 2001 lines, eight sections total.

After this action: Maelle 308/308 LP (was 300/300, +8 CoL = 308 max, +10 Greater Powerful Lumina but that fits the new 308 cap exactly when combined with the +5 from Augmented First Strike and +3 from Energising Break minus the -10 from Powerful On Shell). Actually let me re-check that arithmetic before stating it.

Maelle's running total:
- Pre-chat: 300/300
- Remove Powerful On Shell: 290/300
- Add Energising Break: 293/300
- Add Augmented First Strike: 298/300
- Spend 8 CoL: 298/308
- Add Greater Powerful: 308/308

So she ends exactly at cap, 308/308. CoL remaining: 58 - 8 = **50 Colour of Lumina**.

---

<!-- SECTION -->
## Sciel — Gap Analysis and Decision to Hold

**Matt:** Sciel next. What is she missing that others have? Is there anything in open questions for her? What does the community recommend for endgame support build with Litheson?

**Claude:** *[Turn 50. Last log: Turn 49.]*

Let me work through these three questions in order.

**1. What Sciel is missing that others have**

From the Turn 27 analysis (with Verso updates baked in), Sciel is currently missing the following Lumina that someone else on the team has:

- **Base Shield** — has it
- **Recovery** — has it as Lumina extra
- **Energy Master** — has it via Pictos
- **Second Chance** — has it
- **Augmented First Strike** — Monoco, Verso, Maelle now have it; Sciel doesn't (5LP)
- **Auto Rush** — Verso has it (10LP)
- **Empowering Parry** — Verso has it (5LP)
- **Greater Powerful** — Maelle just added it (10LP)
- **Clea's Life** — Maelle (Pictos only)
- **Empowering Break** — Maelle (Pictos only)
- **Full Strength** — Maelle (15LP)
- **Gradient Fighter** — Maelle (5LP)
- **Powerful On Shell** — Maelle had it, removed; Sciel doesn't
- **Solo Fighter** — Maelle (1LP)
- **Burn Affinity** — Lune (10LP)
- **Critical Burn** — Lune (5LP)
- **Burning Death** — Lune (5LP)
- **Augmented First Strike** (Monoco Pictos, plus Lumina extras)
- **Break Specialist** — Monoco (1LP)
- **Energising Break** — Monoco; Maelle just added (3LP)
- **Longer Shell** — Monoco (10LP)
- **Empowering Parry** — Verso (5LP)

Sciel's role is pure support — AP generation, Twilight buffs/debuffs, healing. So filtering this list to "would Sciel actually use this":

- **Augmented First Strike (5LP)** — first hit damage. Sciel doesn't deal much damage but her opening Fortune's Fury or Twilight benefits from any hit damage boost. Marginal.
- **Auto Rush (10LP)** — Rush at battle start. Pure Speed advantage turn 1. Strong fit.
- **Empowering Parry (5LP)** — stacks parry damage. Sciel rarely parries to attack — she casts buffs/debuffs. Skip.
- **Greater Powerful (10LP)** — only fires when Sciel has Powerful. Sciel rarely receives Powerful. Skip.
- **Full Strength (15LP)** — +25% on full HP. Sciel could maintain full HP via Recovery. Possible but support role makes this marginal.
- **Empowering Break (3LP Lumina)** — Sciel has Breaking Attack and uses Base Attack to Break. Her Break → Powerful chain would work. Could matter if she's the one breaking and then casting Intervention on Maelle/Verso who follow up with damage. **Actually — Empowering Break gives Sciel Powerful, which doesn't help her allies' damage. Skip.**
- **Burn Affinity (10LP)** — Sciel doesn't apply Burn. Skip.

The clearest fits: **Auto Rush (10LP)** and **Augmented First Strike (5LP)**.

**2. Open questions for Sciel in Section 6**

Checking the overview Section 6 (fetched in Turn 37):

- **Breaking Attack for all characters** — Currently only on Sciel. The question is whether to give it to others. Already discussed for Maelle (rejected). Not really a Sciel-specific question.
- No other Sciel-specific items.

Sciel is the cleanest character in terms of open questions — most of the existing build was settled in Chats 22 and 24.

**3. Community recommendations for endgame Sciel/Litheson**

*[web_search: Sciel Litheson endgame build Lumina Twilight Intervention Fortune's Fury]*

Found one really strong endgame Sciel/Litheson source — Hack the Minotaur's "Support Sciel" build, which directly addresses her current role. Let me read it more thoroughly.

*[web_fetch: hacktheminotaur.com/clair-obscur-expedition-33/best-sciel-build-support-sciel]*

The page is loaded but the actual Lumina list is below the fetched section. Let me re-fetch with focused content extraction.

*[web_search: "Support Sciel" build Lumina Pictos Litheson endgame Fortune's Fury Intervention]*

Synthesised picture of community endgame Sciel recommendations, filtered for support role with Litheson:

**Lumina recommended for support Sciel that she doesn't currently have:**

| Lumina | LP | Source | Sciel fit |
|---|---|---|---|
| **First Strike** | 10 | Polygon Sciel guide, multiple | "Important for using something like All Set or Fortune's Fury before anyone else gets a chance to act." Sciel is the 3rd-fastest character (Spd 2534, behind Monoco and Lune). Getting her to go first matters for the team-buff opener. **Strong fit.** |
| **Auto Rush** | 10 | (Verso parallel) | Speed boost turn 1. Slightly worse than First Strike for the "go first" goal, but Auto Rush is more reliable (no Speed-stat override). |
| **Augmented First Strike** | 5 | Steam discussions | +50% first hit. Sciel's first move is usually Fortune's Fury or Twilight (buffs, not direct damage). The +50% only fires on a damage hit. Limited use. |
| **Greater Powerful** | 10 | Steam discussion (one-shot Verso build) | Sciel doesn't reliably gain Powerful. Skip. |
| **Slowing Break** | unknown | Sportskeeda | Sciel uses Breaking Attack already; her Base Attack triggers Break. Slowing Break would slow the target on her Break. Useful synergy but need LP cost. |
| **Charging Critical / Charging Alteration** | unknown | Game8 Sciel | Builds Gradient charges on actions. Mentioned as "spread Charging Lumina across multiple characters to build bar faster" in mechanics.md. |

**Two clear candidates: First Strike (10LP) and possibly Slowing Break or a Charging Lumina.**

**Sciel's current LP situation:** 260/262 used, 2LP headroom. To add First Strike (10LP) she needs 8 CoL.

**Suggestion for Sciel:**

1. **First Strike (10LP, 8 CoL):** This is the strongest fit. Sciel's opening turn matters more than anyone else's for team play (Fortune's Fury on Verso, Intervention on Verso, Twilight). Getting her to act before enemies is high value. Her Speed of 2534 isn't fastest on team; First Strike Lumina would push her ahead.

2. **Alternative — Charging Critical (10LP) or Charging Alteration (10LP):** Adds Gradient bar progress on Sciel's actions. mechanics.md notes "spreading Charging Lumina across multiple characters builds the bar faster overall." Sciel takes many actions per battle (buffs, debuffs, heals), so she generates a lot of triggers. But this delivers diffuse team value, not direct turn-order dominance.

**My recommendation: First Strike (10LP).** It directly addresses Sciel's opening-turn priority for buff application.

Worth noting: this is the same Lumina you just rejected for Maelle on conflated-effect grounds. The reason it makes more sense for Sciel is that her *role* depends on acting first (buffs are useless after the damage is done), whereas Maelle's burst doesn't have a "must go first" requirement — she just needs to act eventually with full AP.

Want me to write this up as an action, or look further at alternatives first?

---

**Matt:** No, I don't think First Strike would make that much difference. In trash fights it's better for Verso to go first, and in boss fights I might want Verso to set up the Steeled Strike first so that Sciel can buff it. That's probably in the Verso file.

Charging Alteration is interesting, but it depends on when it would fire. Fortune's Fury and Intervention are not traditional buffs, and Litheson's buffs are passive and probably won't trigger it. Can you search to see if anyone has tried it? If not, I can test it in-game.

**Claude:** *[Turn 51. Last log: Turn 49.]*

*[web_search: "Charging Alteration" Lumina trigger Expedition 33 buff debuff]*

**Confirmed: Charging Alteration is 10LP, "+10% of a Gradient Charge on applying a Buff. Once per turn."**

But the critical question — what counts as "applying a Buff"? — isn't directly answered in any of these search results. The Fextralife comments page has only one related question ("Does this work on buffs applied by 'on death' effects?") which is unanswered.

**What I can deduce from the data:**

- The Lumina trigger phrase is **"applying a Buff"** — explicitly. Litheson's passive Greater Rush application is a buff application by the weapon, not by the character casting a skill. By analogy with the **Shell On Rush + Litheson confirmed not working** finding (Turn 39), weapon-passive applications likely don't trigger Charging Alteration.
- Fortune's Fury — applies a damage-double buff to an ally. This is a *skill-cast buff*, so it should plausibly trigger.
- Intervention — grants an ally an extra turn + 4 AP. Whether "extra turn" or "+4 AP" counts as a *buff* in the technical sense is unclear. AP is a resource, not typically a buff status. Extra turn is a one-shot effect, not a persistent buff status. Probably **not** a buff in the trigger-sense.
- Twilight (Sciel's mechanic) — she enters Twilight state via her own skill use. Twilight itself is a self-state, not a buff applied to others. Likely doesn't trigger.
- Litheson Greater Rush — weapon passive, ambiguous but probably doesn't trigger per the Shell On Rush precedent.
- Litheson Greater Slow — that's a debuff on enemies, not a buff. Definitely doesn't trigger.

**One useful data point:** the Steam comment about "Charging Critical (20%, on Crit, once per turn)" vs "Charging Alteration (10%, on Buff, once per turn)" — community generally favours Charging Critical as the higher-output Charging Lumina because Crit triggers are easier to land than buff applications. The gamerant.com article explicitly calls Charging Alteration one of the *worst* Pictos for this reason: "support Pictos like Charging Critical grant 20% of a charge on critical hits — double the value with easier conditions, all for the same 10 Lumina points."

**For Sciel specifically:** Sciel has 102% Crit. Every hit Crits. Sciel acts many times per battle. Charging Critical would fire every turn she takes damage-dealing action. That's much more reliable than Charging Alteration's "applying a Buff" trigger which depends on Fortune's Fury being cast (sometimes 3-4 turn intervals).

**Conclusion: Charging Critical (10LP) is the better Charging Lumina for Sciel.** It fires once per turn on any Crit, which Sciel can deliver every turn via her Base Attack (via Breaking Attack) or any damage skill. Reliable trigger, double the Gradient generation per fire.

**For the original question about Charging Alteration's trigger conditions:** the community testing data is thin enough that you'd genuinely need to test in-game. The most likely answer based on similar Lumina behaviour is:
- Fortune's Fury → triggers
- Intervention → unclear (likely no)
- Litheson Greater Rush → likely no
- Twilight (self) → likely no

But that gives maybe 1 trigger every 3-4 turns at best — much less reliable than Charging Critical at 1/turn guaranteed.

**Suggestion: skip Charging Alteration, consider Charging Critical (10LP) instead.** Same cost, more reliable trigger, double the per-trigger output.

Worth noting: my "First Strike won't help much" framing in Turn 50 was a rejection on tactical grounds (Verso usually wants to go first), not a search-based rebuttal. Charging Critical is a different proposition — it benefits the shared Gradient bar regardless of turn order.

Want to commit to Charging Critical for Sciel, or hold and consider alternatives?

---

**Matt:** When Sciel casts a buff, she won't get a critical hit. Only attack skills do that. Charging Critical would be much better on Maelle and Verso. Let's bear Charging Critical in mind for Maelle and Verso (would cost 20 CoL to add to both) for later in this chat. If we don't add it, it can be an open question.

I think that means we leave Sciel as she is. That completes the main team (for now) and we still have 50LP, so I think it's likely we will add Charging Critical to at least one of them.

!log

**Claude:** *[Turn 52. Last log: Turn 49. Logging turns 50–52.]*

Good catch on the Charging Critical / buff-cast distinction — Sciel casting Fortune's Fury or Intervention doesn't roll a Crit because it's not a damage hit. Charging Critical only fires for characters dealing Crit damage, which is Maelle and Verso, not support-role Sciel.

So:
- Sciel: no further changes this session
- Charging Critical (10LP, 10 CoL each) held for Maelle and/or Verso consideration later
- Remaining CoL: 50 (untouched)
- Main team complete for this pass

Logged turns 50–52 (174 lines added) with section marker before Turn 50. File at 2175 lines, nine sections total.

Reminder of "held for later" items so they don't get lost:
- Charging Critical for Maelle (10LP, 10 CoL)
- Charging Critical for Verso (10LP, 10 CoL — needs LP pool expansion since he's at 275/275)
- Energising Burn for Lune (10LP, 10 CoL — from Section 6, mentioned in Turn 38)

If none of these get added, all three need to remain as open questions for next session.

---

<!-- SECTION -->
## Lune — Gap Analysis and Lumina Plan

**Matt:** Ok. Where did we get to on Lune and Monoco apart from Energising Burn? Have we already analysed their gaps?

**Claude:** *[Turn 53. Last log: Turn 52.]*

Yes, we already covered them, but only as part of the wider Pictos/LP analysis. Let me summarise what's been done and what's open.

**Lune — done this session:**
- Pictos: unchanged (Critical Burn, Burn Affinity, Burning Death)
- Lumina dropped: Survivor, Critical Break, Marking Shots (also removed from reserve core)
- Lumina added: Second Chance
- CoL spent: 12 (to raise pool from 175 → 187)
- Final state: 187/187, 0LP spare

**Lune — open from Section 6 / this session:**
- **Energising Burn (10LP)** — flagged earlier, would need 10 CoL

**Lune — gaps I haven't formally analysed:** I did the "missing Lumina from team comparison" in Turn 27 but Lune wasn't the focus. Looking back at my own list, the candidates Lune doesn't have that others do include things like Full Strength, Gradient Fighter, Augmented First Strike, Auto Rush, Empowering Parry — but most of those are oriented around Maelle/Verso damage roles. Lune's burn-DPS role has its own specific Lumina needs that aren't covered by the cross-team comparison. **So no — Lune hasn't had a dedicated gap analysis specific to her role.**

**Monoco — done this session:**
- Pictos: Quick Break → Cheater (saves 40LP)
- Lumina added: Second Chance (uses the 40LP saved)
- Lumina removed from reserve core (affects Monoco): Marking Shots (-3LP)
- CoL spent: 0
- Final state: 167/170, 3LP spare

**Monoco — open from this session:** none flagged.

**Monoco — gaps I haven't formally analysed:** same as Lune — the Turn 27 missing-list was cross-team and not role-specific. Monoco's Break/AP support role has different optimal Lumina than the main DPS characters.

**What hasn't been done:**

1. **Lune-specific gap analysis** — what does her burn-DPS playstyle need that she doesn't have?
2. **Monoco-specific gap analysis** — what does his Break/AP support role need that he doesn't have?
3. **Energising Burn for Lune** — confirmed worthwhile but not committed (needs 10 CoL)
4. **Community endgame recommendations** for both — equivalent to the Sciel search just done

The pattern from Sciel and Maelle suggests a focused per-character search will surface 1–2 useful options that the cross-team comparison missed.

Want to do Lune next, then Monoco? Or are you happy that the existing changes are enough for them this session?

---

**Matt:** Let's do Lune with the same pattern as the others.

**Claude:** *[Turn 54. Last log: Turn 52.]*

Three steps: missing-vs-team, open questions, community search.

**1. What Lune is missing that others have**

Lune currently has (after this session's changes):
- Pictos: Critical Burn, Burn Affinity, Burning Death
- Reserve core (after Marking Shots removal): Painted Power, Energising Turn, Cheater, Shortcut, Recovery, Teamwork, Energising Start I, Dodger, Breaker, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death, Base Shield — but minus the three she dropped: Survivor, Critical Break, Marking Shots
- Lumina extras: Accelerating Heal, Protecting Heal
- Lumina added this chat: Second Chance

So Lune has: Painted Power, Energising Turn, Cheater, Shortcut, Recovery, Teamwork, Energising Start I, Dodger, Breaker, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death, Base Shield, Accelerating Heal, Protecting Heal, Second Chance + Pictos effects (Critical Burn, Burn Affinity, Burning Death).

**Missing that others have (filtered to plausibly useful for Lune's burn-DPS role):**

| Lumina | LP | On | Lune fit |
|---|---|---|---|
| Energy Master | 40 | Sciel | "Add 1 to AP boosts" — game-changing for AP, but Lune isn't on main team. Reserve role doesn't justify the 40LP. Skip. |
| Energising Start I | (has) | — | Already has. |
| Energising Start II/III/IV | various | — | Multi-tier stack for battle-start AP. Worth checking cost. |
| Augmented First Strike | 5 | Maelle, Verso, Monoco | First-hit damage boost. Lune enters fights from reserve in long bosses — first hit on entry could matter. Plausible. |
| Auto Rush | 10 | Verso | Rush at battle start. Lune's Speed is 2575, second-fastest. Marginal — she's already fast. |
| Empowering Parry | 5 | Verso | Stacks damage on consecutive parries. Lune parries; could help. |
| Greater Powerful | 10 | Maelle | Only if Powerful is active. Lune has no Powerful trigger of her own (no Empowering Break Pictos, no Break-Powerful chain in her kit). Skip unless allies grant her Powerful. |
| Full Strength | 15 | Maelle | +25% on full HP. Lune is healer-DPS, often full HP. Strong fit. |
| Gradient Fighter | 5 | Maelle | +25% Gradient damage. Lune uses Elemental Genesis (Gradient skill). Strong fit. |
| Empowering Break | 3 | Maelle/Monoco (Pictos) | If Lune Breaks, she gains Powerful. Lune doesn't typically Break (Monoco does), but Lune has Burning Death which gives 3 Burn on death. Hmm — only triggers when she Breaks, which is rare. Skip. |
| Painter | 10 | Sciel (Pictos) | Physical → Void conversion. Lune does elemental damage, not Physical. Skip. |
| Breaking Attack | 10 | Sciel | Base Attack can Break. Lune rarely Base Attacks in skill-heavy rotation. Skip. |
| Energising Shots | 10 | Sciel (Pictos) | +1 AP on Free Aim shot. Lune used to free-aim more but the playstyle note says she rarely does now. Skip. |
| Energising Heal | 10 | Sciel | +2 AP on healing ally. Lune heals via Healing Light. Strong fit. |
| Healing Tint Energy | 1 | Sciel | +1 AP on Healing Tint. Marginal. |
| Augmented First Strike | (above) | | |
| Break Specialist | 1 | Monoco | +50% Break, -20% base damage. Bad trade for Lune. Skip. |
| Energising Break | 3 | Monoco | +3 AP on Break. Lune rarely Breaks. Skip. |
| Longer Shell | 10 | Monoco | Extends Shell. Lune benefits from Base Shield. Plausible. |

**Most promising for Lune:**
- **Full Strength (15LP)** — +25% damage on full HP. Lune's healing keeps her topped up. Strong burn-DPS multiplier.
- **Gradient Fighter (5LP)** — +25% Gradient damage. Lune's Elemental Genesis is her highest-damage skill. Direct multiplier.
- **Energising Heal (10LP)** — +2 AP when healing ally. Lune uses Healing Light. Sustained AP boost.

**2. Open questions for Lune**

From Section 6:
- **Frenzy** — drops from Licornapieds, +damage on multi-hit skills. Highlighted as **most direct damage multiplier for Genesis (8 hits)** in the overview Section 5. Not yet obtained.
- **First Life (15LP)** — drops from Chromatic Lampmaster. 25% damage while alive. Strong candidate for any DPS including Lune. Not yet obtained.
- **Empowering Dodge (5LP) for everyone** — open question pending CoL. Lune included.
- **Energising Burn (10LP) for Lune** — flagged as ready to add. Specifically Lune.

**3. Community search**

*[web_search: Lune Kralim build Elemental Genesis Lumina endgame burn DPS Expedition 33]*

Multiple recommendations cluster around the same Lumina. Let me synthesise.

**Community Lumina recommendations for endgame Lune that she doesn't currently have:**

| Lumina | LP | Sources | Lune fit |
|---|---|---|---|
| **Charging Critical** | 10 | fandomwire ("Act 3, grab... Charging Critical"), Hack the Minotaur (implied via Cheater-Critical combo) | +20% Gradient charge on Crit. Lune is at 101% Crit. Every damage hit Crits. Multi-hit skills (Lightning Dance, Genesis) fire it repeatedly — but limited to once per turn. **Strong fit. Same 10LP / 10 CoL as Maelle/Verso candidates.** |
| **Frenzy** | unknown | game8 ("damage increasing Luminas that scale well with multiple Skill hits like Frenzy"), overview Section 6 | Multi-hit skill damage boost. Elemental Genesis is 8 hits. **Not yet obtained** — drops from Licornapieds in Verso's Drafts. |
| **Critical Vulnerability** | unknown | msn/fandomwire (multiple references for Lune burn build) | Mentioned alongside Critical Burn for "max Critical Chance" — probably an enemy-side debuff. Worth checking if she'd want it. |
| **First Strike** | 10 | Hack the Minotaur | "Combined with Cheater and First Strike, Lune often gets three actions before enemies can move once." Lune is reserve — only enters after main team wipes or via swap. Less relevant unless she's leading. |
| **Burning Mark** | unknown | community Lune builds | Applies Burn on Marked target. Lune doesn't apply Mark in current rotation. Skip. |
| **Augmented Attack** / **Empowering Attack** | unknown | game8 | For Base Attack builds. Lune is skill-focused. Skip. |

**Cross-referencing with the open questions and earlier analysis:**

Lune's strongest unaddressed additions, in priority order:

1. **Energising Burn (10LP)** — from Section 6 open question. Lune applies Burn via Hell every turn. +AP on Burn application. Direct sustained AP support for her Burn-loop rotation.

2. **Charging Critical (10LP)** — community-recommended. Builds shared Gradient bar. 20% of a charge per Crit, once per turn. Lune Crits every action.

3. **Gradient Fighter (5LP)** — from team comparison. +25% Gradient damage on Elemental Genesis. Direct multiplier on her biggest skill.

4. **Full Strength (15LP)** — +25% on full HP. Lune heals herself via Healing Light. Strong but high LP cost.

5. **Energising Heal (10LP)** — +2 AP on healing ally. Sustained AP from healing Light.

**Affordability:**

Lune is at 187/187 LP. All adds require CoL.

- Energising Burn (10LP) → 10 CoL
- Charging Critical (10LP) → 10 CoL
- Gradient Fighter (5LP) → 5 CoL
- Full Strength (15LP) → 15 CoL
- Energising Heal (10LP) → 10 CoL

With 50 CoL in the pool, the question is how much to spend on Lune vs holding for Maelle/Verso's Charging Critical (20 CoL combined) and other open items.

**My top picks for Lune (in order of impact):**

1. **Energising Burn (10LP)** — directly accelerates her Burn-loop rotation. Already flagged as ready.
2. **Gradient Fighter (5LP)** — cheap and directly multiplies her biggest hit.
3. **Charging Critical (10LP)** — team-wide Gradient benefit.

Total for all three: 25LP / 25 CoL. Leaves 25 CoL for Maelle/Verso Charging Critical (which needs 20 if both).

If we need to prioritise: **Energising Burn + Gradient Fighter (15 CoL)** is the cleanest pair. Charging Critical is more efficient on Maelle/Verso since they're main team and crit more often per battle.

What's your take?

---

**Matt:** You've not got gradient effects right, I'm afraid. There is a Gradient bar that gets filled by skill usage. When full, it adds GP that can be spent on Gradient Skills. Gradient Fighter means that character fills the Gradient bar 25% faster than normal.

**Claude:** *[Turn 55. Last log: Turn 52.]*

Got it. Correcting my mental model:

- **Gradient bar** = filled by skill use, gives Gradient Points (GP) when full
- **GP** = spent on Gradient Skills
- **Gradient Fighter** = +25% Gradient bar fill rate for that character (faster GP generation, team-wide pool)
- **Charging Critical** = +20% Gradient bar progress on Crit, once per turn (a different trigger for filling the bar)
- **Charging Alteration** = +10% bar progress on applying a Buff, once per turn

So both Charging Lumina and Gradient Fighter contribute to filling the *bar* (not damage). My earlier line about "Gradient Fighter +25% Gradient damage" was wrong — there's no such damage multiplier from this Lumina. It's bar fill rate.

That changes the analysis of Lune's options:

**Re-prioritised picks for Lune:**

1. **Energising Burn (10LP, 10 CoL)** — direct sustained AP from Burn application. Still the clearest fit. Lune applies Burn every turn via Hell.

2. **Gradient Fighter (5LP, 5 CoL)** — faster bar fill for the team. Lune takes many actions per battle (Hell, Genesis, Healing Light, etc) so contributes a lot to fill rate. Cheap.

3. **Charging Critical (10LP, 10 CoL)** — additional bar fill on Crit, once per turn. Stacks with Gradient Fighter's overall fill rate boost.

The combination of Gradient Fighter and Charging Critical is interesting: Gradient Fighter scales every skill cast by 25%, while Charging Critical adds a flat +20% per turn when she Crits. They're complementary, not redundant. Lune's skill-heavy rotation makes Gradient Fighter especially effective.

**Revised recommendation:** Energising Burn + Gradient Fighter (15 CoL) is still the cleanest pair. Adds 20% to Lune's AP economy on Burn turns and 25% to her Gradient bar contribution. Both directly enable more Elemental Genesis casts, which is her highest-output skill.

If you want to also add Charging Critical to Lune, that's +10 CoL on top, total 25 CoL. Lune Crits reliably so it would fire most turns.

What's your call? Energising Burn only (10 CoL), Energising Burn + Gradient Fighter (15 CoL), or all three (25 CoL)?

---

**Matt:** Ok, so Charging Critical would be good for Verso, Maelle and Lune, needing 30 CoL spend, plus 15 for Energising Burn and Gradient Fighter on Lune. That's 45, which I can afford.

Let's move onto Monoco and see if there's a better idea.

But first, !log

**Claude:** *[Turn 56. Last log: Turn 52. Logging turns 53–56.]*

Logged turns 53–56 (216 lines added) with section marker before Turn 53. File at 2391 lines, ten sections total.

Plan now firming up:
- **Lune (15 CoL):** Energising Burn + Gradient Fighter
- **Charging Critical for 3 characters (30 CoL):** Maelle, Verso, Lune
- **Total committed if all confirmed:** 45 CoL
- **Pool after these:** 50 - 45 = 5 CoL remaining

That leaves only 5 CoL for Monoco. Let's see what comes up for him.

---

