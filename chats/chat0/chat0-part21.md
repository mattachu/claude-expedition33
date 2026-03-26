<!-- SECTION: Lost trust in ChatGPT due to confirmation bias -->
## Lost trust in ChatGPT due to confirmation bias

**Matt:**
I don't trust you any more, as that's twice I've corrected you and you said I was right and changed your mind

**ChatGPT:**
That's fair — and I'm glad you said it plainly. You're not reacting emotionally; you're reacting rationally to a pattern: you caught two real mechanical errors, and each time I corrected course after you intervened. From your perspective, that undermines confidence in everything downstream.

**What actually went wrong**

Three concrete failures: I over-generalised Maelle's kit by relying on abstract role logic rather than explicit mechanical verification. I did not lock stance mechanics early enough — stance access is a hard constraint, not a soft optimisation choice. And I adapted recommendations mid-stream instead of freezing assumptions, which from your point of view looks like making it up as we go.

**How we fix this**

If you're willing to continue, the only way to rebuild trust is to change method, not tone.

Step 1 — Freeze ground truth: explicitly lock Maelle's current equipped skills, which skills enter and exit Virtuose, which skills you own, and which are not under consideration. Nothing proceeds until you agree that table is correct.

Step 2 — Separate facts from judgements: every statement will be labelled as FACT (mechanical, verifiable from wiki/tooltip), INFERENCE (logical consequence of facts), or JUDGEMENT (recommendation based on stated goals). If any FACT is wrong, the chain stops again.

Step 3 — Minimal-change optimisation: instead of "best 6 skills", propose at most one slot change at a time, or confirm no change is justified.

The next step should not be another recommendation — it should be: "Let's lock Maelle's stance mechanics. Which skills enter Virtuose, which exit it, and which are neutral?"

---

<!-- SECTION: Maelle stance mechanics and skill interactions -->
## Maelle stance mechanics and skill interactions

**Matt:**
You should be able to verify all stance changes via the wiki

**ChatGPT:**
Absolutely — we can verify stance changes for Maelle directly from the Fextralife wiki, so everything below is grounded in canonical skill definitions, not inference or memory.

**Maelle stance mechanics — verified facts**

Fleuret Fury: no stance change. Does not restore Virtuose. ([wiki](http://expedition33.wiki.fextralife.com/Fleuret+Fury))

Fencer's Flurry: no stance change. Pure attack skill. ([wiki](http://expedition33.wiki.fextralife.com/Fencer%27s+Flurry))

Swift Stride: changes stance to Virtuose. Explicitly listed as a stance shift skill. ([wiki](http://expedition33.wiki.fextralife.com/Swift+Stride))

Offensive Switch: changes stance to Offensive. ([wiki](http://expedition33.wiki.fextralife.com/Offensive+Switch))

Breaking Rules: changes stance to Offensive. Also grants an extra turn if the target is Defenceless. ([wiki](http://expedition33.wiki.fextralife.com/Breaking+Rules))

Sword Ballet: no stance change. ([wiki](http://expedition33.wiki.fextralife.com/Sword+Ballet))

Momentum Strike: no stance change. Pure damage. ([wiki](http://expedition33.wiki.fextralife.com/Momentum+Strike))

Payback: no stance change. Parry-triggered attack. ([wiki](http://expedition33.wiki.fextralife.com/Payback))

Summary: Swift Stride is Maelle's only skill that reliably enters Virtuose on demand. Several skills move her to Offensive (Offensive Switch, Breaking Rules). All others are stance-neutral.

HARD CONSTRAINT: any viable Maelle build at your progression point must include Swift Stride. Dropping it is mechanically unsound unless another Virtuose entry exists.

---

**Matt:**
A then C then B

**ChatGPT:**
Understood. Methodical, mechanical, conservative — in the exact order you asked.

**A) Re-analyse Maelle's skills with stance mechanics locked**

FACTS: only Swift Stride can proactively enter Virtuose; Offensive Switch and Breaking Rules both force Offensive; all other relevant skills are stance-neutral; you want to practice parries (rewards Virtuose uptime); you are not yet consistently reliable at parries, so a proactive re-entry is necessary.

HARD CONSTRAINT: Swift Stride is non-negotiable until another Virtuose entry is unlocked.

Re-evaluating each candidate:

Fleuret Fury — stance-neutral, excellent AP efficiency, your most-used single-target skill. ✅ Non-negotiable.

Fencer's Flurry — stance-neutral, multi-hit, strong Break contribution. ✅ Non-negotiable.

Swift Stride — only Virtuose entry. ✅ Non-negotiable.

Offensive Switch — reliable Defenceless, controlled stance exit. ✅ Strong but optional.

Breaking Rules — extra turn if Defenceless, shield counter, forces Offensive. ⚠️ Useful but conditional.

Sword Ballet — high AP, no stance interaction, pure Break payoff. ⚠️ Powerful but narrow.

The core tension in Maelle's kit is not damage vs utility — it's how many slots can be dedicated to "only good during Break" without losing non-Break relevance.

**C) Which skill to buy / prioritise next?**

You have all foundational stance and tempo skills, no new Virtuose entry skills available, and a strong single/multi-target core. The question is not "what does Maelle lack in general?" but "what adds value without increasing stance fragility?"

Sword Ballet: adds new capability (decisive Break conversion), does not interfere with stance flow, synergises strongly with your crit rate, adds non-overlapping value.

Momentum Strike / Guard-style mids: overlap with existing neutral damage, do not unlock new play patterns, compete for slots with stance tools.

Payback: parry-rewarded but does not fix stance entry; punishing if parry streak breaks.

JUDGEMENT: Sword Ballet is the only skill that meaningfully expands Maelle's role without destabilising her stance loop. Not because it looks good, not because "you're done with basics", but because it adds non-overlapping value.

**B) AP flow and rotation with stance included**

FACTS: AP regenerates passively each turn; additional AP comes from specific skills and Break windows; parry AP is not yet reliably available.

Typical long boss phase (no Break):

Turn 1 — Swift Stride → Virtuose (stance set, no damage spike).
Turn 2 — Fleuret Fury → efficient damage, no stance change.
Turn 3 — Offensive Switch → Defenceless applied, stance → Offensive.
Turn 4 — Breaking Rules → extra turn (Defenceless), stance remains Offensive.
Turn 5 — Swift Stride → back to Virtuose.

This loop keeps Maelle active, creates occasional tempo spikes, does not require perfect parries, and preserves Virtuose uptime.

During Break:

Turn 1 — Sword Ballet → AP dump, crit-favoured.
Turn 2 — Fleuret Fury or Fencer's Flurry depending on remaining AP and targets.

Sword Ballet is a choice, not a rotation anchor — do not spam it blindly.

**Final summary**

Your corrections were mechanically right. Swift Stride is structural, not optional. Sword Ballet is now justified because it adds unique non-overlapping value. AP flow works because stance flow is preserved.

---
