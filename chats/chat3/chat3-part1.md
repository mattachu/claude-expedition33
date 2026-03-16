# Clair Obscur: Expedition 33 — Chat 3 — Part 1: Endgame Team Transition

## Setup

**Matt:** matteaston.net/claude

**Claude:** Startup file read and understood. Conversation defaults 1–14 are active, shortcut commands noted, and known failure modes flagged.

What's this session about?

---

**Matt:** Expedition 33. Please fetch the latest version of the overview file: https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@0474d12/overview/claude-expedition33.md

**Claude:** Overview file read. All failure modes and session state noted.

**Chat number:** Section 12 lists Chat 0, Chat 1, and Chat 2 — so this is **Chat 3**.

Setting up session files now.All clear. Session ready:

- **Chat number:** 3
- **Files created:** `chat3.md`, `chat3-index.md`, `session-state.json`
- **Transcripts directory:** empty ✓

What's this session about?

<!-- SECTION: Endgame Team Transition -->
## Endgame Team Transition

**Matt:** I’ve completed the Sacred River mission to complete Monoco’s relationship journey, and defeated Sprong to get the Cheater Pictos. I think I’m ready to switch to the endgame team and get used to playing with them. How should I set them up?

Note, Cheater Lumina costs 40LP, unless someone has the Pictos equipped. But it mighty be worth paying the cost for at least one extra character.

**Claude:** Good progress — Sacred River and Sprong are both Phase 2 targets, so you're right on track. Before I give you a full setup recommendation, I want to flag two things:

**1. I need to verify Steeled Strike + Cheater mechanics before advising on Verso's build.** The overview notes he should add Steeled Strike after getting Cheater, but doesn't specify the exact interaction or which skill to drop. Given the error history around rank-jump skills and interactions, I shouldn't guess. Let me search first.

**2. Second Chance conflict.** The overview lists Second Chance in both Maelle's and Verso's Pictos — but only one character can hold it at a time. That needs resolving as part of this setup.Good, I have what I need. Here's the verified picture, with a few things to flag.

---

**Steeled Strike — how it actually works**

The skill effect is: after 1 turn, deals extreme single-target physical damage, 13 hits. Interrupted if any damage taken. So Verso spends a turn winding up, and if the enemy hits him before his next turn, the skill is cancelled and the turn is wasted.

With Cheater equipped, Verso plays twice in a row — he casts Steeled Strike on his first turn, then executes it immediately on his second turn, before any enemy action can interrupt it.

There's also a second safe route: Sciel's Intervention skill triggers Steeled Strike's attack move, so it can be cast and executed in the same turn rather than two. Since Sciel is in your endgame team and already has Intervention, you have two independent ways to use Steeled Strike safely. Cheater gives Verso the ability to do it on any turn independently; Intervention is available when Sciel acts before him.

Given your ~20% parry rate against unfamiliar bosses, using Steeled Strike without either option is very risky. With Cheater on Verso, it's reliable from turn 1.

---

**Verso — changes to make**

*Pictos:* Swap **Second Chance → Cheater**. This resolves the Second Chance conflict with Maelle (only one copy exists), and Cheater is more valuable to Verso than a once-per-battle revival anyway. Keep Burning Death and Shortcut. One flag: I don't have Shortcut's effect confirmed — check what it does in case it's worth reconsidering the third slot.

*Skills:* Add **Steeled Strike**, drop **Phantom Stars**. Phantom Stars is AoE — useful for trash, but the endgame team already clears trash fine and it's dead weight against bosses. Your new 6: Quick Strike, Assault Zero, Strike Storm, Marking Shot, Perfect Break, Steeled Strike.

Note that Steeled Strike gets increased damage at S Rank, so the core loop stays the same — build rank with Quick Strike/Assault Zero/Strike Storm, then fire Steeled Strike at S.

---

**Second Chance → Maelle**

With Verso giving up Second Chance, it goes to Maelle. She's your primary DPS and benefits more from the once-per-battle safety net. Her current Pictos were listed as Second Chance, Dead Energy I, Piercing Shot — this is actually already correct, it just wasn't possible to have both hers and Verso's active simultaneously. Now it's cleanly hers.

---

**Cheater Lumina (40 LP) for additional characters**

Your instinct is worth thinking through. The most relevant candidate is **Maelle**: a double turn could let her use Gustave's Homage to enter Virtuous stance and then immediately fire a full-damage skill in the same round, rather than waiting a turn. That's a meaningful DPS gain. However, 40 LP is expensive and I don't have her full current LP total confirmed — I'd need to check her Lumina loadout against her LP cap before recommending it. What's her current LP capacity?

**Sciel** almost certainly has no room — her 110 LP cap is essentially full with the core suite plus Energising Heal, Healing Parry, and Accelerating Heal, and she already enables Verso's Steeled Strike via Intervention anyway.

---

**Sciel — one pending task**

Has Litheson been upgraded to level 20 yet? That's the +3 AP per turn when a buff/debuff is applied, which is a significant support boost. If not, that should be a priority before settling into the endgame team.

---

**Summary of immediate actions**

1. Verso: equip Cheater Pictos (replaces Second Chance), learn Cheater Lumina over 4 battles, add Steeled Strike (drops Phantom Stars)
2. Maelle: equip Second Chance (now uncontested)
3. Confirm Shortcut's effect
4. Upgrade Sciel's Litheson to 20 if not done
5. Check Maelle's LP total before deciding on Cheater Lumina for her

What are their current levels, and has Litheson been upgraded?

---

**Matt:** I think the +3AP for Litheson is only for Sciel, not the whole party. Could you check?

**Claude:** Good catch — I should have verified that before stating it. Let me check now.

*[Searched: "Expedition 33 Litheson weapon effect level 20 AP bonus"]*

You're right to flag it. The +3 AP at level 20 is gained by Sciel herself whenever a buff or debuff is applied — once per turn. There's no indication in any source that it applies to the party. So the benefit is that Sciel's own AP economy becomes self-sustaining, which frees Monoco's Potier Energy role from the endgame team rather than replacing it with a party-wide equivalent.

That's a meaningful distinction: the overview's wording ("replaces Potier Energy") is still directionally right — Sciel does generate her own AP and her Intervention gives another character an extra turn plus AP — but the mechanism is Sciel staying AP-positive herself, not directly filling allies' AP bars.

I'll note this as a correction to the overview. The summary wording in Section 7 should change from "Litheson's +3 AP/turn replaces Potier Energy" to something like "Litheson's +3 AP/turn (Sciel only) keeps her self-sufficient; combined with Intervention she effectively generates turns and AP for allies."

Does that match what you've seen in play? And do you want to continue with the endgame team setup from where we left off, or deal with any other corrections first?

---

**Matt:** Yes, that matches. With the Lumina set we currently have plus Intervention, it is generally possible to keep AP high for all three, but not as straightforward or as quick to refill as with Potier Energy.

**Claude:** That's a useful practical distinction — noted. The endgame team's AP flow is sustainable but requires more active management, whereas Monoco's Potier Energy was more mechanical and reliable. Worth keeping in mind when advising on builds or skill loadouts that assume freely available AP.

I'll flag this in the changelist at end of session: Section 7 entry for Sciel needs that correction, and it's probably worth adding a brief note in Section 3 (Playstyle Notes) acknowledging that AP management is a real consideration for the endgame team, not just a solved problem.

Picking back up from where we were — do you know Maelle's current LP cap, and has Litheson been upgraded to 20? Those were the two open questions before deciding on her final setup.

---

**Matt:** One more thing before that: Cheater is less useful for Maelle than it could be, because Gustave’s Homage costs 8AP and Sword Ballet costs 9AP, and characters can’t have more than 9AP. So if Maelle uses Gustave’s Homage to attack and get into Virtuose Stance, she then only has 1AP. If Sciel is able to use Intervention straight after Gustave’s Homage, then Maelle  gets the additional 4AP from that. But with Cheater, it would be Maelle’s turn again. With Energising Turn, she would have 2AP and be in Virtuose Stance, so could use Percée, which, to be fair, does an awful lot of damage, if not quite as dramatically as Sword Ballet. If the target is Marked, Percée does even more damage, and possibly more than Sword Ballet even. Is there a way in which Gustave’s Homage can be used to Mark? Marking Shots I think only has a 20% Mark rate, so it can often take four of five Free Aim shots to Mark, and each shot costs 1AP.

Gustave’s Homage + Cheater + Percée can do a lot of damage, but then Maelle drops out of Virtuose. 

Gustave’s Homage + Intervention + Fencer’s Flurry does less damage, but stays in Virtuose and could set up for Sword Ballet or Stendhal in the next turn.

**Claude:** Good analysis — and the Mark question is the crux of it. I shouldn't guess on Gustave's Homage's exact effects, so let me check.

*[Searched: "Expedition 33 Gustave's Homage skill effect description Mark"; searched: "Expedition 33 Percée skill Maelle AP cost Mark effect"]*

Key findings on Gustave's Homage: Gustave's Homage doesn't apply Mark — it benefits from it. If the target is already Marked, base damage is increased by 50%, multiplicative with the 50% Mark damage bonus, giving 2.25× damage overall. Crucially, it also doesn't *remove* Mark.

Full Cheater sequence on a pre-Marked target:

1. Gustave's Homage (8AP) → 2.25× damage, enters Virtuose, Mark still on enemy, 1AP left
2. Cheater turn → Energising Turn gives +1AP (see caveat below) = 2AP
3. Percée costs only 2AP when used in Virtuose Stance, and deals increased damage to Marked targets — so Percée fires on a still-Marked target, then drops to Defensive Stance

Percée on a Marked target deals roughly double its base damage (×2 multiplier), so that's a meaningful hit, not a consolation prize. The full Cheater sequence is quite strong burst if the target enters already Marked.

**One caveat I can't resolve without testing:** I'm not certain whether Energising Turn grants its +1AP at the start of a Cheater-granted extra turn, or only at the start of a "real" turn. If it doesn't trigger, Maelle has 1AP on the Cheater turn — not enough for Percée's 2AP. Worth testing in a trash fight before relying on this in a boss fight.

**On getting a reliable Mark**

You're right that Marking Shots (20% per shot) is too unreliable for a planned combo. The good news is that in the endgame team, Verso has Marking Shot in his skill list, which applies Mark at 100%. If the turn order is Sciel → Verso → Maelle (which seems likely given Maelle's speed), Verso can Mark the target before Maelle acts — enabling both Gustave's Homage and Percée to fire at full boosted damage.

That's a strong case for keeping Marking Shot in Verso's loadout even in the endgame team, at least in boss fights. The cost is one Verso action that turn, but given Maelle's 2.25× on Gustave's Homage plus boosted Percée, the trade seems worth it.

**Summary of the two paths**

The Cheater path (Gustave's Homage → Percée) is a burst sequence that exits Virtuose — high total damage on that turn, then resets. The Intervention path (Gustave's Homage → Fencer's Flurry → Sword Ballet next turn) stays in Virtuose for a potentially larger payoff across two turns. Which is better will depend on the fight: burst is better when you need to race a mechanic or kill phase; sustained Virtuose is better in longer fights where Sciel can reliably use Intervention at the right moment.

Both paths are significantly stronger with pre-applied Mark. That arguably makes Verso's turn management — choosing when to Mark vs. when to deal his own damage — the key variable in the endgame team's overall output.

Given all this, I'd hold off on recommending Cheater Lumina for Maelle until you've tested whether Energising Turn triggers on the Cheater turn. What are her current LP capacity and Lumina loadout? That'll let me assess whether there's even room for it.

---

**Matt:** I have lots of Colour of Lumina, so I can raise LP capacity. I’ve been waiting to set up the endgame team before doing that. Now is the time!

**Claude:** Good timing. From the overview, Verso and Sciel are already at 110 LP from the Chat 1 expansion. So the main question is Maelle.

Before I can recommend her LP target, I need two things I can't assume:

1. **Maelle's current LP cap** — not recorded in the overview
2. **Whether 110 LP is the maximum, or if caps can go higher**

Let me check that second point.

Good news on both fronts: there's no cap on LP — it's simply your level plus however many Colour of Lumina you've spent, at 1 LP per item. And Colours of Lumina are farmable post-game, so supply isn't a permanent constraint. Spend freely now.

Verso and Sciel are already at 110 LP. The gap is Maelle — her LP cap isn't recorded in the overview. A couple of quick questions before I work out a target for her:

1. **What is Maelle's current LP cap?** (Check the Curator screen — it'll show her current max.)
2. **What Lumina does she currently have equipped?** The overview lists her Pictos (Second Chance, Dead Energy I, Piercing Shot) and notes a Solo Lumina set for The Reacher, but her actual equipped Lumina loadout isn't recorded.

Once I have those, I can work out what she has, what she'd need for any additions (including whether Cheater Lumina at 40 LP is feasible or worth the cost given the interaction uncertainty we discussed), and give you a concrete LP target to spend toward.

---

<!-- SECTION: Team Roles and Build Paths -->
## Team Roles and Build Paths

**Matt:** Before getting into the specifics, can we talk a bit about roles in the team? Maelle is Primary DPS and Sciel is Support. There are ways to push Sciel more towards healing than I currently have, but I think in endgame teams, a lot of people rely on passive healing strats instead. Verso is often described more like a support character, applying Marks, buffs and debuffs. But I've been using him much more as a DPS. I'd like to understand a bit better how the three characters work together.

**Claude:** Good question to ask before diving into builds — getting the role framing right shapes every decision downstream. Let me search before offering analysis, since I've confabulated skill interactions before and the community understanding of this team is likely more developed than my training data.

*[Searched: "Expedition 33 endgame team Maelle Sciel Verso synergy roles guide"]*

Good results — clear picture emerging. Let me give you a genuine role breakdown rather than just summarising community builds, because there are some important tensions with your playstyle worth discussing.

**The community framing**

The dominant community understanding is: Verso applies Mark and stacks Burn as the setup unit, Maelle delivers the damage payload, and Sciel accelerates turns and amplifies Maelle's output. In the most optimised builds, the turn order for single bosses is Verso → Sciel → Maelle: Verso stacks burns and marks, Sciel then doubles Maelle's damage with Fortune's Fury and gives her a turn via Intervention, and Maelle nukes.

Under this framing, Verso is Support DPS — marking and applying pressure — while Sciel handles AP regeneration and burst damage support.

**Where your approach differs — and whether that's a problem**

You've been using Verso as a primary DPS via Steeled Strike, not primarily as a burn-stacker. That's actually a legitimate and separately-recognised build path: some compositions have Verso focus entirely on Steeled Strike, with Sciel doubling his damage and giving him his turn back via Intervention immediately after he acts. In that model, Sciel is doing the same job — doubling damage and granting extra turns — but the target of that amplification shifts from Maelle to Verso.

The practical question is whether Maelle or Verso is your primary damage dealer, because Sciel's Fortune's Fury and Intervention can only fully amplify one character per rotation.

**The honest trade-off**

The community consensus is that Maelle is the stronger damage ceiling — her Virtuose stance and the burn stacking loop are what enable the team's most extreme damage outputs. Verso as a burn-stacker is setting up multipliers that make Maelle's damage exponentially higher, not just additively. Verso as a Steeled Strike DPS is doing large independent damage, but not creating that multiplier effect for Maelle.

However — and this matters for your playstyle — the burn-stack route with Medalum relies on stacks building over multiple turns and Maelle having a specific weapon and build. You're currently using Medalum (not Lithum, which you get from The Reacher, not yet done), and your Maelle build is oriented around Gustave's Homage and stance cycling rather than Pyrolyse/burn stacking. So the full community burn-stack rotation isn't available to you yet anyway.

**A practical framing for now**

Given where you actually are, I'd suggest thinking about the team in two modes:

**Mode 1 — Verso as amplified DPS:** Sciel uses Fortune's Fury on Verso, then Intervention to give him an immediate second turn. Verso winds up Steeled Strike on turn 1, executes on turn 2 (or uses Cheater independently). Maelle applies Mark and deals her own damage. This is what you've been moving toward and it works.

**Mode 2 — Maelle as primary DPS:** Verso Marks and applies pressure, Sciel Fortune's Furies Maelle and gives her an extra turn. Maelle chains Gustave's Homage into Sword Ballet or the Cheater combo we discussed. Verso acts as secondary damage and utility.

You don't have to pick one permanently — the value of this team is that Sciel's Fortune's Fury and Intervention can flex between Verso and Maelle depending on the fight. Against a boss where Maelle is more effective (long fights with time to build stance), amplify her. Against a boss where you need fast burst (or where Steeled Strike's multi-hit is good for Break), amplify Verso.

That flexibility is arguably the team's strongest feature. Does that framing make sense as a way to think about it?

---

**Matt:** I like that flexibility framing, thanks. Was that your idea or is it coming from the community?

**Claude:** That was my own synthesis. The community sources describe the two build paths separately — Verso as setup for Maelle, or Verso as the Steeled Strike DPS — but I didn't read anyone explicitly framing Sciel's Fortune's Fury and Intervention as a flexible amplifier that can target either character depending on the fight. That's my inference from how the mechanics work.

Worth flagging because it means you shouldn't treat it as validated community wisdom. It's a reasonable inference, but I haven't seen it tested or discussed. It's possible there's a practical reason the community doesn't mix the two modes — maybe committing to one role for Sciel's actions each turn is more reliable than flexing mid-fight. That's worth keeping in mind as you play.

---

**Matt:** I'm not sure how Fortune's Fury works with Cheater. It says it amplifies the character's "next turn", so that might be the Steeled Strike setup turn rather than payoff turn, in which case it is wasted. Can you check, please?

**Claude:** Good catch — that's exactly the kind of interaction I shouldn't guess at.

*[Searched: "Expedition 33 Fortune's Fury effect 'next turn' how it works"]*

Your suspicion is confirmed. Fortune's Fury buffs the target's next turn — double damage for 1 turn. And a comment on the wiki page is explicit: "if running Cheater, you will lose this buff if used on turn 1" — meaning Fortune's Fury fires on the Steeled Strike wind-up turn, not the execution turn, and is wasted.

So Fortune's Fury + Cheater + Steeled Strike don't work together as a combo. The interaction is worse than neutral — it burns Sciel's action on a buff that achieves nothing.

This has a meaningful implication for the flexibility framing I suggested earlier. The two modes aren't as symmetric as I presented:

- **Fortune's Fury → Maelle:** Works cleanly. Sciel buffs, then Intervention hands Maelle the turn immediately. One action each, full payoff.
- **Fortune's Fury → Verso (Steeled Strike):** Wasted if Verso then winds up Steeled Strike. Only works if Verso uses a different skill on that turn — Strike Storm, Quick Strike, etc. — and saves Steeled Strike for a separate turn.

So the practical picture is: when Verso is using Steeled Strike, Sciel should use Intervention (to guarantee the execution turn safely) rather than Fortune's Fury. Fortune's Fury is better reserved for Maelle, or for turns when Verso is doing immediate-damage skills rather than winding up.

That actually makes the flexibility framing more nuanced than I initially put it — it's not just "point Sciel's amplification at either character," it's "choose the right Sciel skill depending on what Verso is doing that turn." Worth noting as a correction to my earlier synthesis.

Does that change how you're thinking about Sciel's skill priorities or AP allocation in boss fights?

---

**Matt:** Are you sure that Steeled Strike's damage count is calculated on the second turn, not the windup turn?

**Claude:** Honest answer: I'm not sure. I stated that confidently but I was reasoning from "Fortune's Fury buffs the next turn" without actually verifying when Steeled Strike's damage is calculated. If the damage is calculated on the execution turn (turn 2), then Fortune's Fury applied before the windup turn would have expired by then — but I don't actually know whether the buff tracks turns or the point of calculation. Let me check properly.

*[Searched: "Expedition 33 Steeled Strike damage calculated windup turn or execution turn"]*

The search results don't directly answer this. The best evidence I have is the wiki comment I cited earlier — "if running Cheater, you will lose this buff if used on turn 1" — which implies the buff is consumed on the windup turn and wasted. But that comment is specifically about the Cheater scenario, not the general case of Sciel applying Fortune's Fury before Verso's windup.

There are two possibilities and I genuinely don't know which is correct:

1. **Damage calculated at cast time** — the game locks in the damage multiplier when Steeled Strike is activated, so Fortune's Fury applied beforehand would boost it even if the buff visually expires before execution.
2. **Damage calculated at execution** — the buff has expired by turn 2, and Fortune's Fury is wasted.

The wiki comment suggests option 2, but that comment might only apply to the specific Cheater scenario. I haven't found a source that explicitly addresses the calculation timing.

This is worth testing in a low-stakes fight: apply Fortune's Fury to Verso, have him wind up Steeled Strike normally (no Cheater), and compare the execution damage against baseline. That would give you a definitive answer. I'd recommend testing before building around the combination either way.

I'll retract my earlier confident statement on this — I overstated certainty I didn't have.

---

**Matt:** Ok, I'll do some testing.

Can you explain more about the burn-stacking?

**Claude:** Sure — but given my track record on Lumina and skill effects, I want to search before explaining rather than reasoning from what I think I know.

*[Searched: "Expedition 33 Maelle burn stacking Pyrolyse Medalum endgame build"]*

Good rich results. Here's the honest picture — including one significant flag for your build plans.

**How burn stacking works**

Medalum is the engine. At level 10, it applies double burn stacks when Maelle is in Virtuose Stance. At level 20, all burn damage is doubled while in Virtuose. These stack multiplicatively with burn-enhancing Luminas like Double Burn and Burning Shots.

The payoff skill is Burning Canvas — similar to Combustion, but with no limit on how many burn stacks it can consume. This skill scales with the number of burn stacks on the target, which is what allows the team to delete bosses with a single use.

With Cheater, Maelle can use Pyrolyse from Virtuose Stance and apply up to 60 burn stacks to the target in one action, then on her next turn use Swift Stride to re-enter Virtuose and fire Burning Canvas.

So the actual rotation is: **stack burns → Burning Canvas nuke**, not the Gustave's Homage + stance cycling you've been building toward. Those are two genuinely different Maelle builds.

**The significant flag: Verso's burn-stacking weapon isn't Chevalam**

The community burn-stacking build uses Corpeso for Verso — obtained from Noires in the Dark Shores. On each hit of his basic attack, it inflicts 2 burn stacks per rank, which at S-Rank means 10 burns per hit, doubled to 20 by Double Burn Lumina, giving 80 burn stacks in a single turn.

That's an entirely different weapon and build to what's currently planned for Verso. Chevalam is an Agility + Luck weapon suited to his Steeled Strike / Mark-based DPS build. Corpeso is a burn-stacking support weapon. They're not interchangeable — they serve different roles and likely require different stat allocations.

This is worth flagging clearly: **the community burn-stacking team and your current Verso build are two separate paths.** You don't have to choose the community path, but it's important to know they diverge, because the overview currently treats Chevalam as Verso's endgame weapon without acknowledging this alternative.

**What this means for your current situation**

You have Medalum at level 16. Level 20 doubles all burn damage in Virtuose stance — a very significant upgrade worth prioritising. That's two levels away and worth doing before settling on a build direction.

You have two coherent paths available:

**Path A — Burn stack nuke (community meta):** Verso builds burns with Corpeso, Maelle nukes with Burning Canvas. Requires Corpeso, different Verso stats and skills, and Pyrolyse + Burning Canvas on Maelle. Highest damage ceiling.

**Path B — Stance cycling DPS (your current direction):** Maelle cycles Virtuose with Gustave's Homage, Sword Ballet, Stendhal. Verso uses Steeled Strike and Marking Shot. More mechanical variety, relies less on one-shot burst. This is viable — it's just not the burn-stack route.

I'd suggest deciding which path you want before committing to LP expansions and stat recoats, since they'll push the characters in different directions. Which appeals more to your playstyle?

---

**Matt:** Why was Chevalam recommended? What Verso build is that for? What teams suit that particular build?

**Claude:** Good question to pressure-test. Let me check what Chevalam actually does before explaining the reasoning — the overview records it as Verso's endgame weapon and notes its scaling, but doesn't spell out its special effect, and I shouldn't assume.

*[Searched: "Expedition 33 Chevalam weapon effect Verso build"]*

Here's what Chevalam actually does: it starts every fight with Verso already at Rank S, granting a 200% damage boost immediately, and if he continues avoiding damage throughout the battle, it adds up to an additional 100% damage on top of that. It also applies Rush automatically at the start of combat, nearly guaranteeing Verso the first move. The tradeoff: it disables healing and prevents gaining shields.

So the build it's designed for is **Perfection Rank DPS Verso** — the exact build you've been developing. Starting at S Rank means he doesn't need to spend turns building up via Quick Strike and Assault Zero. He can fire Steeled Strike or Strike Storm immediately at maximum damage. That's directly synergistic with the current skill loadout.

Why was it recommended specifically over alternatives? The overview notes it has the same Agility + Luck scaling as Gaulteram, so no respec needed when you swap. It's essentially the natural endpoint of the current stat investment.

**The significant caveat for your playstyle**

Chevalam is a low margin for error weapon — it intentionally locks out healing, and shields are one of the strongest things in the game, so being unable to gain them hurts a lot. Multiple community sources frame it as a weapon for players who can parry reliably. At your current ~20% parry rate against unfamiliar bosses, that's a real risk. Gaulteram's rank-protection passive was explicitly chosen as a safer alternative while parry skills develop — Chevalam removes that safety net entirely and goes further by disabling healing too.

It's the right weapon for the right build — but the timing of when to switch from Gaulteram matters. When you're consistently parrying familiar bosses and your rate against new bosses is rising, that's the signal. It's probably not the right switch to make at the same time as transitioning to the new team.

Does that answer the question? Worth flagging in the overview that Chevalam is right for this build but contingent on parry confidence — it's not an unconditional upgrade from Gaulteram.

---

**Matt:** That framing helps, thanks. Do people using Chevalam also have Maelle in the party, or does this Perfection DPS replace Maelle?

**Claude:** Good question — I shouldn't assume. Let me check what team compositions Chevalam Verso actually appears in.

*[Searched: "Expedition 33 Chevalam Verso team composition best party"]*

Honest answer first: Chevalam doesn't appear prominently in the team composition guides I'm finding. The community's most-discussed Verso builds in the context of best teams are either the burn-stacking Corpeso build, or a Mark-and-setup role using Gaulteram or Simoso. Chevalam comes up more in individual Verso build discussions than in team composition guides.

What the results do make clear about the Maelle question: Maelle and Verso consistently appear together on the top line across most endgame compositions — she isn't replaced by a Perfection DPS Verso, she's the reason to have him. Verso's job in those teams is to apply Mark at the end of his turn with Marking Shot or Defiant Strike, increasing damage for Maelle on her next hit.

The Perfection DPS Verso build (Rank S, Steeled Strike) also appears alongside Maelle — Verso maintains Rank S for his own damage output and Mark pressure simultaneously, while Maelle handles Burn scaling and Burning Canvas. So Chevalam Verso is still in a team *with* Maelle, not instead of her — his extra damage is a bonus on top of setup, not a replacement for hers.

The practical upshot for your question: Chevalam suits the Perfection DPS build you've been developing, and that build sits alongside Maelle rather than replacing her. The choice between Gaulteram and Chevalam is really about when you feel ready to trade the safety net for the immediate S-Rank bonus — it's a timing question, not a team composition question.

What the results also clarify is that there's a third Verso weapon worth knowing about: Simoso, which accelerates Rank progression and amplifies follow-up attacks on Marked targets. That's a middle path between Gaulteram (defensive) and Chevalam (all-in) that the overview doesn't currently mention. Worth flagging for the changelist.

---

**Matt:** I can't get Simoso until well into post-game.

**Claude:** Fair enough — then it doesn't affect the current decision. The practical choice remains Gaulteram now, Chevalam when parry confidence is there. I'll note Simoso in the changelist as a post-game option worth being aware of, but it doesn't need to be a factor in current build planning.

Where does that leave you? The main open threads before settling on LP targets and builds are:

1. **Which Maelle path** — stance cycling (current direction) vs. burn-stack nuke (requires Pyrolyse, Burning Canvas, Medalum to 20). These need different Lumina and possibly different skills.
2. **Maelle's Lumina loadout and LP cap** — needed before recommending LP expansion targets.
3. **Fortune's Fury + Steeled Strike interaction** — flagged for in-game testing.
4. **Energising Turn on Cheater turn** — also flagged for testing.

Do you want to nail down Maelle's path first, or go check her current Lumina state and come back with the numbers?

---

**Matt:** I'm a little concerned that you haven't asked to read the Maelle or Verso character files yet. Do you think you need to do so?

**Claude:** Yes, you're right — I should have fetched them earlier. Section 6 of the overview explicitly says character files supersede the Section 5 summaries, and we're now making detailed build decisions for both Maelle and Verso. The Section 5 entries don't include full skill lists, Lumina loadouts, or LP caps, and I've already been working from incomplete information as a result. Let me fetch both now.

*[Fetched maelle.md and verso.md from jsDelivr CDN]*

Good — I have both files. A few immediate corrections and clarifications from what I've been working from:

1. **Maelle's LP cap is 112 LP exactly, with zero spare.** Cheater Lumina costs 40 LP — she can't add it without dropping 40 LP of existing Lumina. That's a significant trade-off that needs evaluating properly, not a simple add.
2. **Verso has only 4 LP spare.** Also nowhere near enough for Cheater Lumina without removing other Lumina.
3. **Medalum Level 4 starts Maelle in Virtuose Stance.** I knew Virtuose was her power stance but hadn't registered this — it means she enters every fight already in position for Sword Ballet's tripled damage. Relevant to how the opening turns of boss fights actually play.
4. **Phantom Stars is clearly the skill Steeled Strike should replace in Verso's loadout.** The file already flags it as suboptimal in 1v1 boss fights, and Steeled Strike is a boss-fight skill. That answers the open question.
5. **Chevalam recommended level discrepancy:** The Verso file says 65–70+, the overview says 70–75+. Worth reconciling — I'll flag for the changelist.
6. **Second Chance is still currently held by Verso** for the levelling team. Swapping to the endgame team means returning it to Maelle and giving Verso the Cheater Pictos as his replacement.

Before going further — with Maelle at exactly 112 LP and no spare, do you want to work through whether Cheater Lumina is worth the trade-off, or focus first on other aspects of the endgame team setup?

---

**Matt:** I don't agree that Phantom Stars is "useless" in boss fights — it still does decent damage, I think. Just optimised for AoE.

In turns of LP, I think Monoco currently has the Energising Turn Pictos. If we give that to Maelle, it would free up 20LP (I think) for her.

**Claude:** Fair correction on Phantom Stars — "useless" is too strong. It still hits the boss, just without the AoE spread. It's suboptimal compared to a single-target skill in a 1v1 fight, not worthless. I'll soften that in the changelist. The point stands that Steeled Strike is probably a better use of that slot for boss fights, but that's a different claim.

On Energising Turn Pictos — that's a smart observation. Maelle currently pays 20 LP for Energising Turn Lumina. If she equips the Pictos, she gets it free and recovers that 20 LP for other use. But it would mean replacing one of her three current Pictos: Second Chance, Dead Energy I, or Piercing Shot. Those aren't free either — they're giving her meaningful stat bonuses and their own free Lumina.

Before I can evaluate whether that trade is worth it, I need to check two things I shouldn't assume:

1. **Does the Energising Turn Pictos actually grant Energising Turn Lumina for free?** The overview confirms this for Monoco, but I should verify it's the same Pictos and same mechanic rather than assuming.
2. **What stat bonuses does Energising Turn Pictos provide?** That's the other side of the trade — it might be weaker or stronger than what she'd be giving up.

Do you know what stats the Energising Turn Pictos provides? And is it currently equipped on Monoco, meaning it's free to move across since he's going to reserve?

---

**Matt:** 1. Yes. Every Lumina is a learnt Pictos, so when I got the Energising Turn Pictos, I used that to learn the Energising Turn Lumina, so they are the same.

2. Energising Turn grants a Speed bonus only. From memory, somewhere around +260.

If the overview says Monoco has it, that should be up to date, as I’ve been using him in the levelling party recently.

**Claude:** Good, that confirms the mechanic. And since Monoco is moving to reserve, the Pictos is free to move.

The trade-off is clear in principle: Maelle drops 20 LP of paid Energising Turn Lumina, equips the Pictos, and gets it free — recovering 20 LP. But she has to give up one of her three current Pictos to make room, and each of those is doing two jobs: providing stat bonuses *and* granting its own Lumina for free. So dropping any of them has a hidden LP cost too.

Running through the three options:

**Replace Dead Energy I Pictos:** Lose Speed +162, Crit +17%, and free Dead Energy I Lumina (2 LP value). Gain ~+260 Speed and free Energising Turn. Net: ~+98 Speed, −17% Crit, +18 LP freed.

**Replace Piercing Shot Pictos:** Lose Health +546, Crit +15%, and free Piercing Shot Lumina (3 LP value). Net: +20 Speed or so, −15% Crit, −Health, +17 LP freed.

**Replace Second Chance Pictos:** Lose Health +1107, Crit +8%, and free Second Chance Lumina. She also loses the revival safety net entirely — that seems too costly.

The most attractive swap is probably Dead Energy I: you gain net Speed (~+98) and recover 18 LP, at the cost of 17% Crit. Her current Crit with Pictos is ~65%, so dropping to ~48% is meaningful but not catastrophic given she has Breaking Burn, Critical Break, and the damage multipliers from Virtuose.

That said — even recovering 18–20 LP still leaves her 20+ LP short of Cheater Lumina at 40 LP. So the question is what you'd use that freed space for. What are you hoping to add?

---

**Matt:** Don't forget I can up her capacity with Colour of Lumina.

**Claude:** Right, of course — I set that aside when doing the LP arithmetic and shouldn't have. Let me redo it properly.

Current state: 112 LP cap, 112 LP used, 0 spare.

If she swaps Dead Energy I Pictos → Energising Turn Pictos:
- Saves 20 LP (Energising Turn no longer paid)
- Costs 2 LP (Dead Energy I Lumina now needs to be paid, since she loses the free version from the Pictos)
- Net: **+18 LP freed** within current cap

To add Cheater Lumina (40 LP) she needs 40 LP total space. She has 18, so needs **22 more from capacity expansion** — 22 Colour of Lumina.

Total cost: 22 Colour of Lumina, plus the stat trade (−Speed +162, −Crit 17%, +Speed ~260, net roughly +98 Speed and −17% Crit).

That's very achievable given your resources. The remaining question is whether the −17% Crit is acceptable. At ~65% current Crit with Pictos, dropping to ~48% is a real reduction, though Virtuose's 200% damage multiplier and Burning Canvas scaling both dwarf Crit as damage drivers for Maelle. 

But before committing: should we verify what Cheater Lumina actually does? I've been assuming it mirrors the Pictos effect — giving an extra consecutive turn — but I haven't confirmed that.

---

**Matt:** Pictos and Lumina always have the same passive effect.

**Claude:** Understood — so Cheater Lumina definitively gives Maelle an extra consecutive turn, same as the Pictos. That's confirmed.

The investment case then comes down to the combo we discussed earlier: Gustave's Homage → Cheater turn → Percée. And that still hinges on the unresolved question we flagged: whether Energising Turn grants its +1 AP at the start of the Cheater turn. Without that +1 AP, Maelle has only 1 AP after Gustave's Homage and can't afford Percée's 2 AP cost in Virtuose.

So before spending 22 Colour of Lumina and making the Pictos swap, I'd suggest testing Energising Turn on the Cheater turn first — using Verso, who already has both. If it triggers, the Maelle investment is well justified. If it doesn't, Cheater Lumina on Maelle only works if she has another source of AP, or if there's a different skill worth using on 1 AP — which seems unlikely.

Does Verso have a chance to test that in the next play session before you commit to the Maelle build?

---

