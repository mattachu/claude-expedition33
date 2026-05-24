<!-- SECTION -->
## Maelle — Powerful on Shell Investigation and Lumina Changes

**Matt:** We've been pretty thorough on Verso. Let's look at Maelle next. When she had space by removing Base Shield, she had Powerful on Shell and Energising Shell. This is because Lithum applies Shell automatically when leaving Virtuouse Stance. But I don't remember seeing her glow red, like characters normally do with Powerful. It's possible that these Lumina don't fire on passive applications. Could you do a web search to see whether anyone has discussed this issue before?

**Claude:** *[Turn 39. Last log: Turn 38.]*

*[web_search: Clair Obscur Expedition 33 Powerful on Shell Lithum Virtuose Maelle]*

Plenty of confirmation that Lithum L20 applies Shell on stance exit. But none of these results directly address whether **Powerful on Shell** or **Energising Shell** Lumina fire on that passive application. Let me search more specifically.

*[web_search: "Powerful on Shell" Lumina passive trigger Expedition 33]*

Notable hit — the Auto Powerful comment thread suggests the community has discussed Auto Shell + Powerful on Shell as a working combo, implying Powerful on Shell *does* fire on passive Shell application. But that's Auto Shell (a Lumina-triggered passive), not Lithum L20 (a weapon-triggered passive). Let me search more specifically.

*[web_search: Lithum Shell Powerful Lumina trigger Maelle virtuose stance switch]*

Still no direct discussion of whether Powerful on Shell fires off Lithum's passive Shell. Let me try one more angle — Reddit or forum-style discussion of trigger chains.

*[web_search: "on shell" pictos lumina passive doesn't trigger weapon expedition 33]*

**Found a relevant data point.** From the Shell On Rush Lumina wiki page:

> "Does not work with Litheson, sadly."

Litheson is Sciel's weapon, which has a passive that applies Rush. So community testing has confirmed at least one case where an "X on Y" Lumina **does not fire from a weapon's passive Y application**. That's strong indirect evidence that your observation about Powerful on Shell is correct — the Lumina likely doesn't fire when Shell comes from Lithum's passive.

Also relevant: the Powerful on Shell wiki comment about a Monoco-on-death scenario:

> "Monoco — Has insta death — Has pictos on that gives shell to other party members on death — Other party members have Power On Shell — Party members do not get power, only shell when Monoco insta death"

This suggests Powerful on Shell **specifically requires the Shell to come from the holder's own action**, not from a passive trigger from another source (weapon, ally's death, etc).

**Summary of findings:**

- No direct test results found for "Powerful on Shell with Lithum L20 trigger."
- **Indirect evidence is consistent and points the same way:** community testing confirms "X on Y" Lumina chains often fail to fire when Y comes from a weapon passive (Shell On Rush + Litheson explicitly tested as not working) or from external Shell application (Monoco death-Shell + Powerful On Shell on allies tested as not working).
- **Your empirical observation (no red Powerful glow when Lithum applies Shell) is corroborated.** It's very likely that Powerful on Shell and Energising Shell do not fire from Lithum's passive.

**Verification suggestion:** the cleanest in-game test is to give Maelle Guard Up (her active Shell-application skill) and watch for the red Powerful glow. If Guard Up triggers Powerful but Lithum's passive doesn't, that's a clear confirmation of the passive-Shell-fails behaviour. If even Guard Up fails to trigger Powerful on Shell, something else is wrong (Lumina not equipped properly, or the effect itself isn't behaving as documented).

**Implication for Maelle's loadout:** if confirmed, Powerful on Shell and Energising Shell are wasted LP on Maelle. She has Powerful on Shell (10LP) in her extras — that's 10LP that could be freed if you drop it. She doesn't currently have Energising Shell equipped per the data, so no change there. Empowering Tint and Healing Tint Energy are Tint-trigger, not Shell-trigger — not affected.

Want me to write an action for the empirical test, or hold off until you've verified in-game?

---

**Matt:** Let's assume it doesn't work. I've already removed Energising Shell. If we remove Powerful On Shell as well, we free up 10LP. What should go in instead?

**Claude:** *[Turn 40. Last log: Turn 38.]*

10LP for Maelle, plus her existing 1LP headroom = **11LP total to spend**.

Looking at what Maelle doesn't have that the data files identify as plausible:

**From Section 6 open questions (Maelle-tagged):**
- **Longer Shell (5LP)** — Extends Shell duration. **But this is "X on Shell"-adjacent — would it also fail if Shell comes from Lithum passive?** Worth flagging that uncertainty. Distinct from Powerful on Shell in that Longer Shell modifies the Shell *duration* once applied, not a trigger off the Shell *application event*. Less likely to fail, but not certain.
- **Empowering Dodge (5LP)** — +damage per consecutive dodge, doesn't reset on parry. Stacks with Empowering Parry (which Verso just got). Maelle would benefit from this similarly.

**From the Turn 27 missing-Lumina list (effects on others but not Maelle):**

Filtering to "Maelle would actually use the effect":

| Lumina | LP | On | Fit for Maelle |
|---|---|---|---|
| Recovery | 10 | Sciel, Lune, Monoco | Clea's Life is super-Recovery; Recovery itself less essential, but Clea's Life only triggers on no-damage turns. Recovery would cover damage-taken turns. Hmm — but if Maelle gets damaged, Lithum likely puts her into Shell so damage is mitigated anyway. Marginal. |
| Augmented First Strike | 5 | Monoco | +50% first hit damage. Maelle's first hit each fight matters (Phantom Stars opener). Strong fit. |
| Burn Affinity | 10 | Lune | Maelle uses Burn (Burning Canvas, Pyrolyse). +25% damage on burning enemies is very strong for her, especially since she stays in fights long enough for burns to stack. |
| Critical Burn | 5 | Lune | +25% Crit on burning enemies. Maelle is at 109% Crit already, overcapped. Wasted on her. |

**From Verso's web search results that apply to Maelle:**

- **Auto Rush (10LP)** — Rush at battle start. Maelle's Speed is 2462. Rush at battle start gets her acting earlier on turn 1. Strong fit and same reasoning that worked for Verso.
- **Empowering Parry (5LP)** — already implied above via Empowering Dodge but worth listing separately. Maelle parries when she can. Stacks up to 50% damage.

**Filtering down to best 11LP options:**

| Combo | LP | Why |
|---|---|---|
| Augmented First Strike (5) + Empowering Parry (5) | 10 | Aggressive offence on first hit + scaling parry damage. Synergises with Maelle's playstyle. |
| Augmented First Strike (5) + Empowering Dodge (5) | 10 | Same first-hit boost + dodge-scaled damage (easier to land than parry). |
| Auto Rush (10) | 10 | Speed boost turn 1. Maelle already moves second after Verso; this would close the gap. |
| Burn Affinity (10) | 10 | +25% damage when target is burning. Maelle applies Burn frequently. Could be the strongest single 10LP add for her. |

**My pick: Burn Affinity (10LP).**

Reasoning: Maelle's damage routine is Burn-heavy — Burning Canvas and Pyrolyse both apply or interact with Burn. +25% damage on burning targets is a flat multiplier on a large fraction of her output, not a niche trigger. Augmented First Strike only fires once per battle and Auto Rush only matters for turn 1; Burn Affinity applies on every hit against a burning enemy, which is most of them.

The 1LP spare from Maelle's headroom can go on **Solo Fighter (1LP) — wait, she has that. Healing Tint Energy — she doesn't have it but the JSON says it's 1LP for Sciel; not sure if same cost for Maelle... actually any 1LP option. Worth checking pictos-lumina.json properly for 1LP candidates Maelle doesn't have:

- Break Specialist (1LP) — +50% Break damage / -20% base damage. Trade-off; Maelle isn't a breaker. Skip.
- Healing Tint Energy (1LP) — +1 AP on Healing Tint use. Maelle rarely uses Healing Tints if Clea's Life works. Marginal.
- Charging Tint (2LP — not 1LP) — wait, that's 2LP not 1LP, doesn't fit.

The 1LP headroom is hard to use well. Probably leave unfilled or accept Healing Tint Energy as a 1LP "why not" pick.

Want Burn Affinity for the 10LP? Or one of the combinations?

---

**Matt:** I'm not actually using Maelle's burn skills at the moment. Neither Pyrolyse nor Burning Canvas are active. I think if I struggle in Verso's Drafts or against the Superbosses in the Endless Tower, I may need to switch to the burn-stacking build to get extreme damage. But for now she doesn't need Burn Affinity.

I wonder about Breaking Attack — that would mean I could swap out Fleuret Fury for another skill. It's only there for the Can Break ability.

**Claude:** *[Turn 41. Last log: Turn 38.]*

Good reasoning. Let me check Breaking Attack against the data.

**Breaking Attack (10LP):** per `pictos-lumina.json`, "Base Attack can Break." Currently equipped: Sciel only. So this would put Break capability on Maelle's basic attack.

**Sense-check the trade — does it free Fleuret Fury?**

Fleuret Fury's role is the Can Break tag, letting her trigger Breaks. If Base Attack gets Can Break, Fleuret Fury becomes redundant *for that purpose*. But Fleuret Fury may have other properties — let me think about what it does. It's a Maelle skill, but I don't have it in the data I've fetched. I should be honest about that.

What I'd need to check before recommending the swap:
1. **Fleuret Fury's actual effect** — base damage, stance interaction, AP cost, any other tag beyond Can Break. If it's a strong damage skill that also has Can Break, removing it costs damage output even if Break is covered. If it's purely a low-damage Break trigger, removing it is a clean win.
2. **Whether Breaking Attack's "Base Attack" includes Maelle's stance-modified attacks** — Maelle's basic attack varies by stance. Does Breaking Attack fire from a Virtuose Stance attack, or only the neutral base attack?

These are both questions I shouldn't answer from memory given the failure modes flagged at session start ("Confabulating Lumina and skill effects" and "Wrong advice on record"). Let me search.

*[web_search: "Fleuret Fury" Maelle skill effect Expedition 33]*

**Fleuret Fury confirmed:** 6 AP cost, high single-target Physical damage, 3 hits, "If in Virtuose Stance, stay in Virtuose Stance," Can Break. So it does have other properties beyond Can Break:

- **6 AP cost** — expensive
- **3 hits of high Physical damage** — meaningful damage output
- **Virtuose preservation** — keeps her in Virtuose Stance if already there
- **Can Break** — what you're using it for

Notable from the wiki comment: "Best damage dealer both early and midgame, becomes just a better mezzoforte late Game, still worth a slot." So by Act 3 it's "just a better Mezzo Forte" — not the top damage skill in her endgame kit. The Game8 Act 3 build doesn't list Fleuret Fury among top skills (Stendhal, Payback, Sword Ballet are highlighted instead).

**So Fleuret Fury in Maelle's current loadout is essentially serving as her Break trigger + a moderate damage option, not a peak damage skill.**

**Trade analysis: Breaking Attack + drop Fleuret Fury:**

What you lose:
- 3-hit Physical damage skill, 6 AP cost
- Virtuose-stay property (but Lithum's counter mechanic already covers this — Maelle stays in Virtuose by parrying)

What you gain:
- 10LP committed to Breaking Attack (but you have 10LP to spend)
- A free skill slot for something more useful in Act 3

**One important uncertainty I can't resolve from search:** Breaking Attack says "Base Attack can Break." It's unclear whether:
- "Base Attack" means only the basic attack (1 AP, the default attack action), OR
- "Base Attack" means any of Maelle's normal attacks across stances

If it's the strict interpretation (basic 1 AP attack only), then dropping Fleuret Fury means you'd need to use Maelle's basic attack to Break, which deals less damage than Fleuret Fury's 3-hit Physical. Trade may not be net-positive on Break output, though it would be net-positive on AP economy.

**Also worth flagging:** Maelle has a *Pictos* called Empowering Break equipped (Powerful on Break effect, Lumina version 3LP). If Maelle uses her own basic attack to Break via Breaking Attack, does she become Powerful from Empowering Break? That synergy chain may be the real win — base attack → Break → Maelle becomes Powerful → next turn's heavy skill gets +25% damage.

**Recommendation:** Breaking Attack is a good fit *if* you've confirmed in-game that Maelle's basic attack can actually fill the break bar enough to be useful. Fleuret Fury (3 hits) probably fills the bar faster than a single basic attack. If basic attack alone doesn't break reliably, you'd be replacing a working Break trigger with a worse one.

**Suggestion before committing:** test Breaking Attack in-game with Maelle's basic attack against a high-break-bar enemy. If it triggers Break in 1-2 basic attacks, swap Fleuret Fury out. If it takes 4+ basic attacks, keep Fleuret Fury.

Or — **add Breaking Attack now (10LP) and keep Fleuret Fury for now**, freeing up a skill swap only after empirical confirmation. That uses your 10LP, gives you flexibility, and you can decide on the skill slot later.

Want to commit either way, or hold pending the test?

---

**Matt:** I think you should read mechanics.md for the Break mechanics and Maelle.md for the stance mechanics.

Breaking Attack will only modify Base Attacks.

I more often use Verso or Sciel to Break. Maelle's Empowering Break is worth remembering — Break > Powerful gives a very cheap and easy method for Powerful. However, to do most damage, Maelle wants to be in Virtuose. Basic Attack will drop her out of Virtuose, whereas Fleuret Fury keeps her in it. If the aim of breaking is to set up Powerful for a big hit on the Cheater turn, then Fleuret Fury is much better, if she's in Virtuose already. Best way to get back into Virtuose is Counter + Lithum. Counter > Virtuose > Fleuret Fury > Break > Powerful > Stendhal.

However, Fleuret Fury costs 6AP, so she is unlikely to have enough AP left for Stendhal straight after. Base Attack gives 1AP, not costs 1AP, so Base Attack + Breaking Attack > Break > Powerful > Stendhal is doable.

Virtuose is a 300% boost compared to the Powerful 25% boost. Last Chance > Virtuose > Stendhal is repeatable and reliable, and creates a much bigger modifier.

Conclusions?

**Claude:** *[Turn 42. Last log: Turn 38.]*

You're right that I should read those files before continuing. Let me fetch them.

*[Fetched reference/mechanics.md]*

Mechanics read. Now Maelle's file:

*[Fetched characters/maelle.md]*

Now I have the full picture. Working through your reasoning:

**Confirmed from the files:**

1. **Virtuose = 200% more damage (i.e. 300% total = 3x), not the 200% I'd vaguely had in mind from search.** Per Maelle.md: "Deal 200% more damage." So your "300% boost" is the right framing for the total multiplier. Powerful is +25%, which is much smaller. The relative weight of "stay in Virtuose" vs "trigger Powerful" is therefore heavily skewed toward Virtuose.

2. **Base Attack drops Maelle out of Virtuose.** Maelle.md doesn't say this explicitly, but it's implicit in stance mechanics — Base Attack isn't a Virtuose-preserving skill (only Fleuret Fury and Mezzo Forte are listed as Virtuose-preserving). So your statement is correct.

3. **Base Attack gives +1 AP (it doesn't cost AP).** I was wrong earlier — I'd written "1 AP basic attack" implying cost. Correcting: Base Attack is the no-cost default action. AP economy works in Base Attack's favour.

4. **Fleuret Fury costs 6 AP, keeps her in Virtuose.** Confirmed.

5. **Stendhal costs 8 AP, applies Defenceless to self, ends in Stanceless.** Confirmed.

**Working through the two sequences:**

**Sequence A: Counter → Virtuose → Fleuret Fury → Break → Powerful → Stendhal**
- Counter (free, switches to Virtuose via Lithum L10)
- Fleuret Fury (-6 AP, stays in Virtuose, triggers Break via Can Break)
- Empowering Break Pictos: gain Powerful
- Stendhal (-8 AP, single-hit Void)
- **Total AP cost: 14 AP across two skills, both in Virtuose, both with Powerful active on Stendhal**
- Damage multiplier: Virtuose ×3, Powerful ×1.25 = ×3.75 on Stendhal hit
- Problem: 14 AP is a lot. Even with Energy Master + Energising Turn she's unlikely to have this stockpiled at once.

**Sequence B: Base Attack + Breaking Attack → Break → Powerful → Stendhal**
- Base Attack (+1 AP, drops out of Virtuose, triggers Break via Breaking Attack)
- Empowering Break Pictos: gain Powerful
- Stendhal (-8 AP, single-hit Void, Stanceless)
- **But Maelle is now Stanceless, not Virtuose.** No Virtuose multiplier on Stendhal.
- Damage multiplier: Powerful ×1.25 only = ×1.25

**Sequence B loses the Virtuose multiplier entirely.** Stanceless Stendhal × Powerful (1.25×) is dramatically worse than Virtuose Stendhal without Powerful (3×). Powerful is +25%, Virtuose alone is +200%. Even unboosted Virtuose Stendhal outdamages Powerful-boosted Stanceless Stendhal by a factor of ~2.4×.

**Sequence C: Last Chance → Virtuose → Stendhal (your other option)**
- Last Chance (-1 AP, refills all AP, switches to Virtuose, drops HP to 1)
- Stendhal (-8 AP, single-hit Void, Stanceless after)
- **Total AP cost: 9 AP, but Last Chance refills all AP, so effective cost is 8 AP from initial pool, then refill**
- Damage multiplier: Virtuose ×3
- Plus: Cheater fires extra turn → Clea's Life heals to 100% → Full Strength active (+25%) → another Stendhal possible if AP available
- Damage on the Cheater bonus turn: Virtuose ×3 × Full Strength ×1.25 = ×3.75

**Conclusion:**

1. **Breaking Attack to replace Fleuret Fury is net negative for damage.** The Virtuose multiplier (3x) dominates the Powerful multiplier (1.25x). Even with the AP savings, Base Attack drops her out of Virtuose, which costs more damage than Powerful adds. Confirmed by your reasoning.

2. **Maelle's strongest single-turn damage line is Last Chance → Virtuose → Stendhal (with Cheater bonus turn for Full Strength multiplier).** This doesn't involve Breaking Attack or Empowering Break at all — and is already supported by her current loadout (Last Chance, Cheater Lumina, Clea's Life Pictos, Full Strength Lumina).

3. **Empowering Break is still useful situationally** — when Sciel or Verso (rather than Maelle) does the Break, Maelle is still in Virtuose and gets Powerful for "free" without spending AP. So keep Empowering Break Pictos equipped. The Pictos itself, not the Lumina, is what matters.

4. **Don't add Breaking Attack.** It enables a sub-optimal damage line. The 10LP should go elsewhere.

**Revised question: what should the 10LP (from Powerful on Shell removal) go on?**

Going back to the Turn 40 list, filtering by what survives this analysis:
- **Augmented First Strike (5LP)** — first-hit damage, fires once per battle. Doesn't conflict with anything.
- **Auto Rush (10LP)** — Rush at battle start, gets Maelle moving earlier turn 1.
- **Empowering Parry (5LP)** — stacks parry damage up to +50%.
- **Empowering Dodge (5LP)** — same but for dodge (open question item).
- **Burn Affinity (10LP)** — flagged but you've ruled it out unless switching to burn-stacking build.
- **Longer Shell (5LP)** — open question. Same caveat as Powerful on Shell — may not trigger from Lithum's passive Shell. Risky.

**Suggested: Augmented First Strike (5LP) + Empowering Parry (5LP) = 10LP exactly.** Both stack with Virtuose multiplier and apply to Stendhal hits. No conditional trigger that might fail.

Alternative: **Auto Rush (10LP)** alone, mirroring Verso. Speed Maelle into turn 1 action faster.

Your call — but I'd back the 5+5 split over Auto Rush for Maelle, because her turn-1 problem is less acute than Verso's (she's faster than Verso to begin with at Spd 2462 vs 2284).

---

**Matt:** A couple of extra points:

1. A broken enemy takes 20% more damage, so that should be factored into Sequence A and B.

2. Empowering Break will **only** trigger if it's Maelle that does the Break.

Let's look at AP. If Maelle has 9AP at the start of her turn, spends 6 on Fleuret Fury (3 remaining), Cheater turn +1 new turn, +1 Energising Turn, +1 Energy Master, now on 6AP, which is not enough for Stendhal. So Sequence A isn't possible.

Sequence B drops her out of Virtuouse, so even with the extra 20% for broken enemy and 25% for Powerful, that's nowhere near the 300% of Sequence C.

We want a sequence that ends with Virtuouse + Broken to give 345% modifier to Stendhal. Sequence A would do that but there's not enough AP. **Unless** either Breaking or Base Attack gives AP as well. That points to Energising Attack I or Energising Break. What is the cost of those?

**Claude:** *[Turn 43. Last log: Turn 38.]*

Corrections noted on points 1 and 2 — both right and important.

**Looking up costs from the data:**

- **Energising Attack I:** 10LP. Effect: "Add 1 AP per base attack."
- **Energising Break:** 3LP. Effect: "Add 3 AP on Break."

Maelle already has **Energising Attack I (10LP)** in her loadout — listed in the solo build add list ("Energising Attack I (10): +1 AP per base attack — important for solo AP generation"). Cross-checking against the current Lumina table for Maelle… looking at her Lumina table, **Energising Attack I is not in her current standard loadout** — it appears in the solo build add list only. So she doesn't have it active in party play right now.

**Energising Break is not on Maelle at all.**

**Re-checking the sequences with these:**

**Sequence A revised: Counter → Virtuose → Fleuret Fury → Break → Powerful + Energising Break → Stendhal**

- Start: 9 AP, Virtuose (from Counter via Lithum L10)
- Fleuret Fury: -6 AP, stays in Virtuose, triggers Break (3 AP remaining)
- Break: Empowering Break Pictos → Powerful gained. Energising Break → +3 AP (6 AP)
- Cheater bonus turn: +1 AP (7) + Energising Turn (+1 turn-start AP boosted to +2 by Energy Master = +2 → 9) + Energising Start I is battle-start only, doesn't fire here
- Wait — let me check turn-start AP carefully. "Every character gains 1 AP at the start of their turn" baseline. Energising Turn says "+1 AP per turn, boosted by Energy Master to +2." So turn-start adds: 1 (baseline) + 2 (Energising Turn with Energy Master) = 3 AP at start of Cheater bonus turn.
- After Break: 6 AP. After Cheater turn start: 6 + 3 = 9 AP.
- Stendhal: -8 AP, Virtuose (still! Cheater turn doesn't change stance, and Fleuret Fury kept her in Virtuose). 1 AP remaining.
- Damage multiplier on Stendhal: Virtuose ×3 × Powerful ×1.25 × Broken ×1.20 = **×4.5**

**Energising Break (3LP) makes Sequence A work.** And it's cheap.

Actually wait, let me re-verify by tracing without Energising Break:

Without Energising Break: after Fleuret Fury, 3 AP. Cheater turn start: 3 + 3 = 6 AP. Stendhal needs 8 AP. **Doesn't fit.**

With Energising Break (+3 AP on Break): after Fleuret Fury + Break, 3 + 3 = 6 AP. Cheater turn start: 6 + 3 = 9 AP. Stendhal at 8 AP fits. **Works.**

**Sequence A enabled by Energising Break (3LP).**

Now the alternative path:

**Sequence B revised: Base Attack + Breaking Attack + Energising Attack I → Break → Powerful → Stendhal**

But this still drops Maelle out of Virtuose, so even with Broken's +20%, the multiplier is Powerful ×1.25 × Broken ×1.20 = ×1.5. Far worse than Sequence A's ×4.5.

**Even with Energising Attack I, Sequence B is dominated by Sequence A.**

**Conclusion:**

- **Energising Break (3LP) is the unlock for the Counter → Virtuose → Fleuret Fury → Break → Stendhal damage sequence.**
- The 10LP from Powerful on Shell removal would cover: Energising Break (3LP) + 7LP remaining.
- Energising Attack I (10LP) doesn't help, because the sequence it enables (Base Attack route) is worse.
- **Don't add Breaking Attack** — confirms the earlier conclusion.

**For the remaining 7LP after Energising Break:** I'd suggest **Augmented First Strike (5LP)** as it stacks multiplicatively with Virtuose on Stendhal hits when used first in a battle. Leaves 2LP unfilled — Maelle has Solo Fighter (1LP) already so a 1LP slot or 2LP slot is the only fit. **Dead Energy I (2LP)** is in her loadout already. The 2LP would have to go on something new — Healing Tint Energy (1LP) doesn't fit at 2LP. Charging Tint (2LP) might be a candidate if it's a Maelle-relevant Gradient builder. Or just leave 2LP unfilled.

Total spend: Energising Break (3) + Augmented First Strike (5) = 8LP, with 2LP unfilled out of the 10LP freed.

Does this match your reasoning? And does it change anything about the broader plan?

---

**Matt:** Yes, that is actually helpful. Let's drop Solo Attack to give her 3LP after that. What could we add for 3LP?

**Claude:** *[Turn 44. Last log: Turn 38.]*

Quick check before suggesting: I want to make sure I'm reading "Solo Attack" right. Maelle's Lumina table has **Solo Fighter (1LP)** with the note "Rounds up LP to cap." Did you mean Solo Fighter, or is there a different Solo Attack Lumina I'm not finding?

If Solo Fighter, dropping it frees 1LP, giving 3LP total (the 2LP I left unfilled + the 1LP from Solo Fighter). That matches your "3LP" figure.

**3LP candidates Maelle doesn't currently have:**

Looking at the JSON for Lumina at exactly 3LP that aren't already on Maelle:

| Lumina | LP | Effect | Fit for Maelle |
|---|---|---|---|
| Empowering Break | 3 | Apply Powerful on Break | She has the Pictos. Lumina version would be redundant for her (already gets it from Pictos). But adding the Lumina costs 0LP for the Pictos holder anyway — so it's already free. Skip. |
| Powerful Revive | 3 | Apply Powerful when reviving | Maelle has Phoenix Flame (2GC revive). Reviving allies grants Maelle Powerful — would synergise with a follow-up Stendhal that turn. Niche but real. |
| Breaking Counter | 3 | +50% Break damage on Counter | Already on her loadout. Skip. |
| Burning Shots | 3 | 20% chance Burn on Free Aim | Already on her. Skip. |
| Marking Shots | 3 | 20% chance Mark on Free Aim | Already on her. Skip. |

Looking wider — Lumina at 1-3LP she might benefit from:

| Lumina | LP | Effect | Fit |
|---|---|---|---|
| Dead Energy III | — | Need to check JSON | Maelle has I and II. If III exists at 2-3LP it would extend the AP-on-kill chain |
| Auto Defenceless | unknown | Apply Defenceless on battle start (if it exists) | Would set up Sequence A faster |

Actually, the strongest candidate from the *open questions list* in Section 6:

**Empowering Dodge (5LP)** — too expensive at 3LP budget. Doesn't fit.

**Honest read:** at exactly 3LP, the options are thin. The realistic candidates:

- **Powerful Revive (3LP)** — minor synergy with Phoenix Flame revives
- **Stay 3LP unfilled** — there's no strong case at this price point

There's a sanity check worth doing: is dropping Solo Fighter (1LP) the right move? Its effect is "+50% damage when last fighter alive" — only fires in solo situations. In party play it's always inactive. The 1LP "rounds up LP to cap" comment in Maelle's file is the only reason it's there. So yes, dropping it is fine, but accepting a 3LP unfilled slot is also fine. It's not like 3LP gets converted to anything useful if unspent.

**Suggestion: leave the 3LP unfilled or take Powerful Revive (3LP) as a marginal-synergy filler.** Neither is materially impactful.

Want me to keep digging for 3LP options I might have missed, or hold here?

---

**Matt:** I almost never use Phoenix Flame. Let's keep Solo Fighter for now and leave her with 2LP spare. So the swap for Maelle is:

**ACTION:** Remove Powerful On Shell Lumina from Maelle and add Energising Break and Augmented First Strike.

!log

**Claude:** *[Turn 45. Last log: Turn 38. Logging turns 39–45.]*

Logged turns 39–45 (407 lines added) with new section marker before Turn 39. File at 1858 lines, seven sections total.

Two flags for awareness:

1. **The action you wrote is in your turn**, not mine. Standard practice has worked fine — wrap will pick it up from the `**ACTION:**` line regardless of which speaker wrote it.

2. **Verification note for the action:** the swap is Powerful On Shell out (-10LP), Energising Break in (+3LP), Augmented First Strike in (+5LP). Net: -2LP, so Maelle goes from 299/300 to 297/300 with 3LP headroom. The 2LP we discussed leaving spare is now actually 3LP spare. Not a problem — just noting the arithmetic for the wrap session.

---

