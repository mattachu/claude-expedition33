<!-- SECTION -->
## Monoco Skill Loadout Finalised

**Matt:** What is outstanding on Monoco? I feel that he can benefit from more general Lumina discussions, but there's not many open questions left that are specific to him. What am I missing?

**Claude:** *[Turn 36. Last log: Turn 35.]*

*[Fetched monoco.md]*

*[Read monoco.md]*

*[Turn 36. Last log: Turn 35.]*

Good — full file read. You're right that there aren't many Monoco-specific open questions. Here's what I can identify:

**Genuinely open:**

1. **Post-Simon skill loadout** — the file explicitly flags this as unresolved. The current equipped set is the Simon build (Lancelier Impale, Orphelin Cheers, Chapelier Slash, Moissonneuse Vendange, Grosse Tête Whack, Potier Energy). The reserve build wants Abbest Wind back, and Stalact Punches, Portier Crash, Chalier Combo reviewed. This is a concrete outstanding item.

2. **Death Bomb variant vs reserve build** — you lost against the Chromatic Lampmaster and noted the Death Bomb build was still on when the reserve team came in, which was an oversight. So the question is: which build does Monoco run as his default going forward? The Death Bomb build was designed to pair with solo Maelle, but you're now running a team build. Does Death Bomb still have a use case, or does he revert to the reserve support build permanently?

3. **Sniper as third Pictos** — the file lists it as current but the stat block shows "Longer Break / The One" for the Death Bomb variant. After reverting from Death Bomb, his third Pictos should be confirmed back to Sniper.

**Things that belong to the general Lumina review rather than Monoco specifically:**

- Death on revival (Protecting Death three shields) — you raised this as potentially good for everyone. That's the general review.
- Whether the Greater/Longer buff suite in the Death Bomb build has any value in the reserve build — again, general Lumina question.

So the Monoco-specific work is really just: **settle which build is his default and fix the skill loadout**. Do you want to do that now?

---

**Matt:** Thinking about skills, I’ve currently swapped Lancelier Impale out for Stalact Punches and Grosse Tête Whack for Sakapatate Fire. That last one was more just to see how much damage it does — the answer was not much compared to the DPS builds, but it does apply Burn. Maybe fetch data/skills.json and check Sakapatate Fire and Grosse Tête Whack — or have you read the details already in Monoco’s file?

Monoco is built for Break, and that affects his damage. This is epitomised by Break Specialist, which increases Break damage by 50% but reduces hit damage by 20%. Even Monoco’s strongest attacks are weak with build. He has to focus on utility: Stalact Punches builds break, Moissonneuse Vendance converts this to Break (should probably give him Breaking Attack Lumina for a cheaper options to Break), Orphelin Cheers applies Powerful and provides AP if on the right Mask, Potier Energy provides reliable AP, Chapelier Slash applies Mark. Grosse Tête Whack was there to apply Defenceless, and I’m minded to switch back to that as Lune can source her own Burn, so Sakapatate Fire isn’t necessarily as useful as providing Defenceless.

**Claude:** *[Turn 37. Last log: Turn 35.]*

The Monoco file has the skill table but without full effects for skills not yet acquired — let me check Sakapatate Fire specifically since it's not in the main table.

*[Fetched skills.json]*

*[Queried Sakapatate Fire and Grosse Tête Whack]*

*[Turn 37. Last log: Turn 35.]*

That confirms your read clearly. Sakapatate Fire: Extreme Fire AoE, 3 hits, 3 Burn per hit — but the AP cost is unconfirmed and unknown in your data, and crucially it only advances the wheel by **+1** (the lowest of any skill). That's a poor fit for Monoco's rotation — wheel cycling is central to his utility, and a +1 skill stalls it. It also fires on Almighty Mask, so it consumes the Joyaro L20 doubled Break damage bonus without contributing to break. And as you say, Lune can source her own Burn through Hell and other skills, so the Burn application isn't filling a gap.

Grosse Tête Whack: High Physical single-target, 5 hits, Defenceless 3 turns. +4 wheel, Heavy Mask with increased damage bonus. Far better fit: the wheel advance keeps the rotation moving, 5 hits contributes to break bar, and Defenceless is a team-wide damage multiplier nobody else is reliably applying now that Lune is pivoting to Lightning Dance as payoff rather than setup.

So: **Sakapatate Fire → Grosse Tête Whack** is the right revert. Your reasoning on Defenceless is correct — it amplifies Maelle, Verso, and Lune's payoff hits, which is exactly where Monoco's utility should land.

On **Breaking Attack Lumina** for Monoco — good idea. Moissonneuse Vendange costs 3 AP to Break; Breaking Attack (10 LP) lets a base attack Break if the bar is full, costing 0 AP. That's a real saving in rounds where the break bar is charged but you need AP elsewhere for Potier Energy or Orphelin Cheers. Worth adding, and 10 LP is cheap.

So the settled Monoco skill loadout for general reserve use is:
- Stalact Punches (break building)
- Moissonneuse Vendange (break trigger)
- Grosse Tête Whack (Defenceless)
- Orphelin Cheers (Powerful + AP)
- Potier Energy (AP battery)
- Chapelier Slash (Mark)

Does that match what you're running, minus the Sakapatate Fire swap?

---

**Matt:** Yep. With Breaking Attack, it might make sense to swap out Moissonneuse Vendange, but I don't think there's a strong candidate to take its place.

**Claude:** *[Turn 38. Last log: Turn 35.]*

Agreed — Breaking Attack doesn't fully replace Moissonneuse Vendange. Breaking Attack only fires when the bar is already full, whereas Vendange actively *triggers* the break from a charged but not-yet-full bar. They're doing different jobs: Vendange finishes a partially-filled bar, Breaking Attack mops up the rare case where the bar is full but it's not worth spending 3 AP. So Vendange stays as the primary break trigger and Breaking Attack is a cheap supplementary option.

The stronger case for Breaking Attack is actually just as an LP-efficient addition rather than a replacement — 10 LP to occasionally save 3 AP is worth it at this stage of the game where LP isn't tight. No swap needed.

Without a strong candidate to replace Vendange, the six-skill loadout is settled. Are you ready to move to the general Lumina review, or is there anything else on Monoco first?

---

**Matt:** I think that's it for Monoco. !log

**Claude:** *[Turn 39. Last log: Turn 38 (this log).]*

Logged — Turns 36–39 appended, transcript now at 769 lines. Last logged turn is **Turn 39**.

*[Turn 39. Last log: Turn 39.]*

Ready for the general Lumina review. To recap the three things on the agenda there: the death-on-revival question (Protecting Death shields for everyone), the DPS/Support core set rethink (replacing main team / reserves split), and whatever else surfaces from reviewing Maelle and Verso's current Lumina loads. Where do you want to start?

---

<!-- SECTION -->
## Full Lumina Screenshot Audit — All Five Characters

**Matt:** [Uploaded six screenshots of active Lumina for all five characters]

Here are the current Lumina loadouts for all characters. There are two screens for Maelle as they don’t fit on one page. 

To read them, note that active Lumina come first, with a purple background, and run in alphabetical order from left to right then top to bottom. They are then followed by inactive Lumina in alphabetical order. So when you see Warming Up followed by Accelerating Heal, that means everything before and including Warming Up is active, and everything after and including Accelerating Heal is not active.

The first thing to do is match the lists against your expectations: what have I added/removed/not added that I haven’t told you about.

I actually ran out of Colour of Lumina when adding to Lune, so that’s not finished. I will have to grind some more CoL. but that’s not a problem — I’ve worked out I can grind it out at 1 CoL per minute.

**Claude:** *[Turn 40. Last log: Turn 39.]*

Let me read all six screenshots carefully and compile what I see against expectations.

*[Transcribed active Lumina from all six screenshots: Verso 30, Maelle 43, Sciel 28, Lune 26, Monoco 24]*

*[Turn 40. Last log: Turn 39.]*

Good — I've read all six screens. Let me work through each character against expectations.

**Verso** — matches expectations well. Energising Stun confirmed active (new Pictos, replacing Second Chance). Double Third is there. One surprise: **Charging Critical (10 LP)** is active — this wasn't in my model of his build. What does it do? Also **Energising Break (3 LP)** is active — the file notes this was replaced by Energising Heal as it only triggers on Break (1–2 per boss fight). Worth reviewing. Otherwise looks correct.

**Maelle** — a lot here. The big surprises against expectations:
- **Inverted Affinity (5 LP)** is active — this blocks healing, which conflicts with any scenario where Sciel needs to heal her. Noted as a deliberate At Death's Door choice (×1.5 multiplier), but worth confirming it's intentional.
- **Confident Fighter (15 LP)** is active — same conflict with healing. Both Inverted Affinity and Confident Fighter together strongly commit her to the no-heal build.
- **Energising Shell (10 LP)** — wasn't in my model. What's the effect?
- **Charging Critical (10 LP)** — same unknown as Verso.
- **Exposing Break (5 LP)** — wasn't in my model.
- **Anti-Blight (10 LP)** — situational defensive, not in my model.
- **Burning Shots (3 LP)** — wasn't in my model.
- **Marking Shots (3 LP)** — wasn't in my model.
- **Greater Shell (10 LP)** and **Longer Powerful (10 LP)** — buff extenders, not in my model.
- Notably **Frenzy is not active** on Maelle — was this intentional, or not yet added?

**Sciel** — mostly as expected. **Charging Alteration (10 LP)** and **Gradient Break (5 LP)** and **Healing Tint Energy (1 LP)** weren't in my model. Also **Recovery (10 LP)** is active — was that previously excluded for Sciel? And she has 5 spare LP showing.

**Lune** — as expected but incomplete due to running out of CoL. Missing from the active list vs plan: **Frenzy, Double Third, Full Strength, Glass Canon** are absent. Double Third is there actually — yes it is. So missing: **Frenzy, Full Strength, Glass Canon**. Also **Critical Burn** is absent — was that dropped intentionally with the Pictos change?

**Monoco** — currently running the reserve build with **Shielding Death** active (one of the death suite Lumina). That's a remnant from the Death Bomb build. Also **Recovery (10 LP)** and **Staggering Attack (1 LP)** — weren't in my model. And he still has 6 spare LP.

The three things I'd most want your input on before drawing conclusions: what do **Charging Critical** and **Energising Shell** do, and is Frenzy's absence on Maelle intentional?

---

**Matt:** Lots of questions there! I think it might help if you read chats/chat-index.md, as we have discussed a fair few of these before. The per-chat summaries may give you enough detail on some of those questions. The file is short but fairly dense.

**Claude:** *[Turn 41. Last log: Turn 39.]*

*[Fetched chat-index.md]*

*[Read chat-index.md — 37 lines, Chat 0–32 summaries]*

*[Turn 41. Last log: Turn 39.]*

That fills in most of my questions. Let me work through the surprises now with this context:

**Charging Critical (Verso and Maelle)** — added in Chat 25 ("full Lumina loadout review, adding Charging Critical"). I don't know the effect but it's been a deliberate addition for some time. Not a surprise, just a gap in my knowledge this session. Can you tell me what it does, or shall I query it?

**Energising Break on Verso** — Chat 26 explicitly added this ("Verso gains Energising Break, enabling a Perfect Break → Stun → End Bringer rotation"). So it's intentional and the file's note that it "only triggers on Break 1–2 per boss fight" is the acknowledged tradeoff for that rotation. Not a problem.

**Energising Shell, Exposing Break, Burning Shots, Marking Shots, Anti-Blight on Maelle** — likely from Chat 25's full review or Chat 32's build finalisation. I don't have their effects to hand and shouldn't guess. Rather than list them all as questions, the most efficient thing is probably for me to query the pictos-lumina.json for all of them at once.

**Frenzy absent on Maelle** — now I understand: Frenzy was tested on Verso in Chat 31 ("Frenzy stacking tested"). Maelle wasn't mentioned as getting it. With a 13-hit Steeled Strike, Verso's Frenzy payoff is huge; Maelle's single-hit Stendhal nuke gets zero benefit from Frenzy. So Frenzy on Maelle makes no sense — it's a multi-hit mechanic and her payoff skill is one hit. My Turn 23 suggestion was wrong.

**Recovery on Sciel and Monoco** — situtational survivability, added in prior chats. Fine.

**Shielding Death on Monoco** — remnant of the Death Bomb build, as flagged. Needs reverting to reserve build.

**Lune's missing Lumina** — Frenzy, Full Strength, Glass Canon ran out of CoL before adding. Confirmed.

Let me query the unknowns:

*[Queried effects of unknown Lumina: Charging Critical, Energising Shell, Exposing Break, Burning Shots, Marking Shots, Gradient Break, Charging Alteration, Healing Tint Energy, Staggering Attack]*

*[Turn 41. Last log: Turn 39.]*

That resolves most of the picture. Working through the findings:

**Charging Critical** — "+20% Gradient Charge on crit, once per turn." On Verso's 13-hit Steeled Strike with 100% crit, that's +20% GC every turn he crits, which is every turn. Solid. On Maelle, same — she crits every hit too. Both make sense.

**Exposing Break** — "Apply Defenceless on Break." Maelle has this, which means she's applying Defenceless herself on a break, supplementing whatever Monoco provides. Fine.

**Burning Shots and Marking Shots** — both trigger "on Free Aim shot" with 20% chance. Free Aim is Maelle's rifle mechanic, so these are tailored to her. Low probability (20%) but cheap (3 LP each) and they seed burn/mark for the rest of the team. Makes sense.

**Energising Shell** — LP cost and effect both showing as None in the data, meaning it's not in your pictos-lumina.json yet. Do you know what it does?

**Gradient Break (Sciel, 5 LP)** — "+50% Gradient Charge on Breaking." Chat 26 added this explicitly. Sciel breaking targets charges her gauge for Fortune's Fury. Makes sense.

**Charging Alteration (Sciel, 10 LP)** — "+10% GC on applying a buff, once per turn." Sciel buffs allies constantly (Fortune's Fury, Rush, Intervention setup) so this fires regularly. Good fit.

**Healing Tint Energy (Sciel, 1 LP)** — "Healing Tints also give 1 AP." 1 LP, free AP on Tint use. Trivially worth it.

**Staggering Attack (Monoco, 1 LP)** — "+50% break damage on Base Attack." Fits the break-focused build perfectly. 1 LP.

So the only remaining genuine unknown is **Energising Shell** on Maelle. Everything else is accounted for. What does Energising Shell do?

---

**Matt:** Energising Shell provides energy from shell. So applying Shell gives extra AP, perhaps +2. I’m surprised the details are not there for that one.

This is part of her Lithum suite. When she exits Virtuose, Lithum applies Shell. This removes the Defenceless from Stendhal, provides additional defence itself, boosted by Greater Shell and Longer Shell, provides AP through Energising Shell, and provides damage boost through Powerful On Shell boosted by Greater Powerful and Longer Powerful. This happens every time she uses Last Chance > Stendhal or Last Chance > Gommage.

There is also a Rush on Shell, but I don’t think I gave it to her as Sciel applies Greater Rush already through Litheson. Could still be worth adding to complete the suite.

**Claude:** *[Turn 42. Last log: Turn 39.]*

That's a clean suite — Shell is doing a lot of work on exit from Virtuose. Let me check whether Rush On Shell is in the data and what it costs.

*[Queried Rush On Shell and Energising Shell — both not found or missing data]*

*[Turn 42. Last log: Turn 39.]*

Neither is in the data — Energising Shell has a placeholder entry with no details, and Rush On Shell isn't recorded at all. Both need adding to pictos-lumina.json as part of the wrap.

On the question of whether Rush On Shell is worth adding to Maelle: your reasoning is sound that Sciel's Litheson Greater Rush already covers the team. But there's a nuance — Litheson's Rush fires during Moon/Twilight phases, whereas Shell triggers every time she exits Virtuose via Last Chance. If she's firing Last Chance → Stendhal in a phase where Litheson Rush isn't active, Rush On Shell would fill that gap and give her an extra turn. Against that, Sciel's Intervention already grants extra turns on demand, so the marginal value of a conditional Rush on top is probably low.

The honest answer is: it depends on how often she's in Virtuose outside of Litheson-active phases. If that's rare, skip it. If it's common (e.g. early in fights before Moon phase), it's worth the LP. Do you know the cost? Neither of us has it confirmed — it's not in the data. Worth checking in-game before deciding.

On the suite as a whole — it's coherent and the Defenceless removal on Shell exit is the most important part mechanically, since Stendhal applies Defenceless to Maelle herself which would otherwise debuff her own next hit. The rest of the suite (AP, defence, Powerful) layers on top cleanly. The only thing I'd flag is that **Inverted Affinity + Confident Fighter block Sciel from healing her**, so if she takes a hit at 1 HP in a phase where the Shell defence and shields don't absorb it, there's no heal fallback — that's the deliberate At Death's Door risk you've accepted, just worth keeping in mind.

Want to move on to a broader review of what should change across all characters, or is there anything else to examine first?

---

**Matt:** If it's not in the file, maybe there isn't a Rush On Shell. I thought the file was comprehensive. Can you query how many entries don't have LP value or effect listed?

**Claude:** *[Turn 43. Last log: Turn 39.]*

*[Queried all entries missing LP cost or effect — 218 total entries, 13 missing LP, 10 missing effect, 10 missing both]*

*[Turn 43. Last log: Turn 39.]*

Two findings:

**Energising Shell is in the data** — it's in the `candidates_for_review` section with LP 10 and effect "Give 2 AP on applying Shell." So your recollection (+2 AP) is exactly right. The earlier query failed because I was searching across pictos and lumina sections but not candidates_for_review correctly. The data entry just had a display issue in the initial lookup. No data gap there — it just needs moving from candidates to the active lumina list in the JSON.

**Rush On Shell genuinely doesn't exist** — 218 entries total and it's not among them. You're right that the file is comprehensive (merged from the Fandom wiki), so if it's not there, it's not a Lumina. The Shell suite is: Energising Shell (+2 AP), Powerful On Shell (Powerful), Longer Shell (+2 duration), Greater Shell (stronger Shell) — and that's it. No Rush variant exists.

The three Pictos with missing LP are just stat-only Pictos entries where LP cost isn't recorded — not a data problem, just those three don't have LP values noted. Not urgent.

The `candidates_for_review` section also has Empowering Dodge (5LP, +5% damage per consecutive dodge stacks to 10) — that one's interesting for Maelle if she's parrying/dodging cleanly in the At Death's Door build, but probably marginal given everything else she's stacking.

So the Shell suite on Maelle is complete as-is — no Rush On Shell to add. Anything else to address before moving to the broader Lumina review?

---

**Matt:** Worth keeping Empowering Dodge in mind. !log

**Claude:** *[Turn 44. Last log: Turn 43 (this log).]*

Noted — Empowering Dodge (5 LP, +5% per consecutive dodge, stacks to 10 = +50% max) is worth revisiting once the core Lumina review is done. Cheap enough that if her dodge rate is high it's essentially free damage.

*[Turn 44. Last log: Turn 43 (this log).]*

Logged — Turns 40–44 appended, transcript now at 867 lines. Last logged turn is **Turn 44**.

*[Turn 44. Last log: Turn 44.]*

Ready to move into the broader Lumina review. The main threads still open:

1. Lune's remaining additions once CoL is ground (Frenzy, Full Strength, Glass Canon)
2. Monoco's Shielding Death revert and skill loadout finalisation
3. The DPS/Support core set rethink (point 3 from session start)
4. Empowering Dodge for Maelle
5. Data gaps to fix in wrap: Energising Shell entry, Empowering Dodge if added

Where do you want to start?

---

<!-- SECTION -->
## General Survivability Lumina — Death/Shell/SOS Suite for All Five

**Matt:** Shielding Death I think Monoco can keep. It’s probably the most helpful of the Death Bomb build when in team play against big bosses. It’s a candidate for giving to everyone. 

What else is active as a candidate to give to everyone?

**Claude:** *[Turn 45. Last log: Turn 44.]*

Good point on Shielding Death — the three shields on death are useful regardless of the build context, and against big bosses where characters die and revive repeatedly it's genuinely valuable. That reframes it from "Death Bomb remnant" to "general survivability Lumina."

Let me look at what's currently distributed unevenly that could benefit everyone...

*[Turn 45. Last log: Turn 44.]*

Clean picture. The "on 4, missing one" list is the most actionable:

**Breaker and Critical Break missing from Lune** — these are break-contribution Lumina. Lune's reserve role doesn't prioritise break building (that's Monoco's job), and with Lightning Dance as her payoff she wants to fire into a broken target rather than build the bar herself. Probably intentional omissions.

**Dead Energy I missing from Monoco** — worth checking what Dead Energy I does before deciding. Do you know offhand?

**Energising Start I missing from Verso** — also worth checking. Is this the +AP at battle start?

**Energy Master missing from Monoco** — "+1 to every AP gain." Monoco's AP loop is driven by Potier Energy and Orphelin Cheers; Energy Master amplifying those would be meaningful. Cheap addition at 40 LP, though 40 LP is expensive. Worth considering.

**First Strike missing from Monoco** — Monoco is reserve, so First Strike matters less for him. Omission makes sense.

On the **"on 3" candidates for everyone** — the most interesting ones:

**Augmented First Strike** (missing Sciel and Monoco) — Sciel's first action is usually a buff not a damage hit, so the ×1.5 on first hit isn't useful for her. Monoco's first hit does minimal damage by design (Break Specialist −20%). Both omissions are justified.

**Survivor** (missing Verso and Lune) — "Survive a killing blow once per battle." Verso at 1 HP from Overload is the obvious case for this. Lune in reserve enters at full HP so less critical. Worth asking: why doesn't Verso have it?

**Shielding Death** — currently only on Monoco, not in the "on 3" list at all. That's the candidate you raised. Before recommending it for everyone, what does it actually give — three shields on death, but what size?

---

**Matt:** [Uploaded Lune Lumina screenshot showing Frenzy, Full Strength, Glass Cannon now active]

Ok, about 45 mins grinding in Renoir's Drafts got me 60CoL, so I've added all of those to Lune and given her everything you mentioned except Survivor. Need a bit more grinding for that. I've intentionally not given her Critical Burn as it won't do anything — she is already on 100% Crit now. Have a look at this screenshot and see if I've done it right. Survivor still to be added.

**Claude:** *[Turn 46. Last log: Turn 44.]*

Reading the screenshot carefully. Lune's active Lumina (everything up to and including Teamwork before the greyed-out section):

AP Discount, Accelerating Heal, Augmented First Strike, Base Shield, Breaker, Breaking Attack, Breaking Burn, Breaking Death, Burn Affinity, Cheater, Clea's Life, Critical Break, Dead Energy I, Dead Energy II, Dodger, Double Third, Energising Burn, Energising Start I, Energising Turn, Energy Master, First Strike, Frenzy, Full Strength, Glass Cannon, Painted Power, Protecting Heal, Quick Break, Rush On Powerful, Second Chance, Shortcut, Teamwork.

That looks correct against the plan. Frenzy, Full Strength, and Glass Cannon are all active. Frenzy's effect is confirmed on screen: "Each successive Skill hit deals 10% more damage." Stats all match: Health 9400, Speed 2543, Crit 100%.

Three things I notice:

**Breaker and Critical Break are now active** — these weren't in the plan and you'd omitted them previously. Was that intentional, or carried over from the core set? They're break-contribution Lumina which fit Monoco's role better than Lune's DPS role, but they're cheap (10 LP and 5 LP) so not a meaningful cost if you want her to contribute to break occasionally.

**Critical Burn absent** — correct, as you explained. At 100% crit it adds nothing.

**Survivor still to add** — noted, pending more CoL.

Otherwise looks right. One question on Glass Cannon specifically — the in-game name shows as "Glass Cannon" with two n's, whereas your data has it as "Glass Canon" (one n). Worth correcting the data spelling in the wrap.

---

**Matt:** I'm not sure whether Breaker and Critical Break were ever in the reserve team core, but they are the primary drivers for Break damage. Monoco contributes most, but adding them to Lune will speed up Break bar filling.

Glass Cannon — I had thought it was some kind of pun and was actually Canon, but that must have been an error in the source data.

You asked about Dead Energy a few times: it gives +3AP to the character that killed an enemy. Excluded from reserve team as they often enter late in single-boss fights and so it won't fire.

**Claude:** *[Turn 47. Last log: Turn 44.]*

On Breaker and Critical Break — makes sense. Lune contributing to break bar fills alongside Monoco means less time waiting for break, and break-state multiplies her Lightning Dance payoff (Defenceless from Grosse Tête Whack + her own Exposing Break firing). The synergy is real, not just passive contribution.

On Dead Energy — that clarifies why it's excluded from reserve builds but present on the main team (Verso and Maelle both active in prolonged fights where they'll get kills). And it answers my earlier "worth checking" question about Dead Energy I missing from Monoco — he's reserve, so the same logic applies and the omission is correct.

On Glass Cannon — I'll flag it as a data correction for the wrap: the in-game spelling is "Glass Cannon" (two n's), the JSON has "Glass Canon" (one n). All references in the data need updating.

That also retroactively validates a small concern: back in Turn 4 I listed "Glass Cannon" as a transferable multiplier, which matches the in-game name. The JSON just had a typo.

So to summarise where Lune stands now: complete except for Survivor (pending ~20 CoL). Once that's added her build is fully settled.

Coming back to the open question from Turn 45 — Survivor missing from Verso. Given he's at 1 HP from Overload for most of a fight, Survivor ("survive a killing blow once per battle") seems like exactly the insurance he'd want. Do you know why it's not there, or was it just never added?

---

**Matt:** Was probably removed to make room for something else temporarily and never restored. Should be added.

**Claude:** *[Turn 48. Last log: Turn 44.]*

Agreed — straightforward addition. At 1 HP for the whole fight, Survivor is effectively mandatory insurance. 20 LP and already in the core set for others, so no LP budget concern.

That brings us back to the Shielding Death question — you raised it as a candidate for everyone. I asked what size the three shields are but we haven't confirmed that. Do you know, or would you need to check in-game? The size matters for whether it's meaningful on high-HP fights: three small shields on a character with 9000+ HP against a boss hitting for thousands is very different from three substantial ones.

Also while we're cataloguing universal candidates — two others from the Turn 45 analysis worth a quick decision:

**Energy Master (missing from Monoco)** — "+1 to every AP gain." His AP loop runs on Potier Energy and Orphelin Cheers; Energy Master would amplify both. The cost is 40 LP which is steep, but with CoL available it's not a blocker. Does Monoco have AP pressure in longer fights?

**Survivor for Lune** — you mentioned this is still pending CoL. Same logic as Verso: reserve entry at full HP means she's less likely to need it than Verso, but against the Chromatic Lampmaster where characters are dying repeatedly it's good insurance. Probably worth adding alongside Verso's.

---

**Matt:** Yes, Monoco should get Energy Master.

Shields are breakable one-hit defence: if a character has a shield, any attack against that character will break the shield but not do any damage. So effectively infinite in size but one-shot in usage.

**Claude:** *[Turn 49. Last log: Turn 44.]*

That makes Shielding Death much more valuable than I was treating it — three free one-hit absorbs on death means the character that just died can survive the next three hits regardless of damage magnitude. Against bosses with multi-hit attacks or fast follow-ups after a kill, that's three turns of immunity. Worth having on everyone.

So the additions to action across the party:

- **Verso:** Survivor (20 LP)
- **Monoco:** Energy Master (40 LP)
- **All five:** Shielding Death (10 LP each = 50 LP total, but Monoco already has it so 40 LP across the other four)

Before committing to Shielding Death on everyone, one check: Maelle at 1 HP from Overload/Last Chance — if she dies and gets three shields, then Clea's Life fires on her next turn and restores full HP, does that interact cleanly? The shields would absorb the first three hits while she's back at full HP, which seems strictly good. And with Inverted Affinity + Confident Fighter blocking heals, Clea's Life wouldn't fire on her anyway in the At Death's Door build — so she'd stay at 1 HP with three shields. That's actually ideal: three free hit absorbs while remaining in the damage-boosted state. No conflict.

CoL cost for all these additions: Survivor ×2 (Verso + Lune) = 40 LP, Energy Master for Monoco = 40 LP, Shielding Death ×4 = 40 LP. Total 120 LP / 120 CoL additional. At 1 CoL per minute that's two hours of grinding — worth flagging before committing. Is that acceptable, or do you want to prioritise some over others?

---

**Matt:** Maelle doesn't have Clea's Life any more: Lune has it.

Shielding Death gives 3 shields to all *other* players, not the one that dies.

Could you look up SOS Shield in the data file — is that a one-off application or repeatable?

**Claude:** *[Turn 50. Last log: Turn 44.]*

You're right on Maelle — Clea's Life moved to Lune, I shouldn't have said that. And the Shielding Death correction changes the picture significantly: it's not self-protection on death, it's giving your allies three shields each when you die. Against a boss that just killed one character and is about to follow up on the rest of the party, that's three free hit absorbs for each surviving ally. Very strong in multi-phase boss fights.

*[Queried SOS Shield (not found), Shielding Death, Protecting Death]*

*[Turn 50. Last log: Turn 44.]*

SOS Shield isn't in the data. Either it doesn't exist as a Lumina or it goes by a different name — do you have an alternate name in mind?

On what's there: the data confirms Shielding Death as "allies gain 3 Shield points" on death, and surfaces **Protecting Death (5 LP): "allies gain Shell on death"** — which is a separate Lumina you mentioned earlier as being active on Monoco (the one that was "very helpful" in the Chromatic Lampmaster fight). Shell is a larger defensive buff than shields — it's a damage-reducing layer rather than a one-hit absorb.

So the two death Lumina are complementary:
- **Protecting Death (5 LP):** allies get Shell when you die — damage reduction layer
- **Shielding Death (10 LP):** allies get 3 shields when you die — three one-hit absorbs

Together on a character who dies they give allies Shell + 3 shields — substantial protection for the follow-up turns. Both are cheap (15 LP combined). Both are already on Monoco. The question of giving them to everyone becomes: do you want every character to be a death-protection distributor, or just Monoco?

Given characters die and revive repeatedly against the Chromatic Lampmaster, having all five distribute these on death means every death is also a party buff. At 15 LP per character × 4 remaining characters = 60 LP total for both, it's affordable. Worth it?

---

**Matt:** Shielding Death is definitely most useful, but Protecting Death is probably worth having too. What other Lumina are listed in the "shields" category?

**Claude:** *[Turn 51. Last log: Turn 44.]*

*[Queried all shield/shell Lumina by keyword — 23 results]*

*[Turn 51. Last log: Turn 44.]*

Rich list — and SOS *Shell* is there (5 LP, "Apply Shell when falling below 50% Health"), which is probably what you were thinking of. Several things stand out:

**Already in use on the party:** Base Shield (universal), Energising Shell / Greater Shell / Longer Shell / Powerful On Shell (Maelle's Lithum suite), Powerful Shield (Maelle), Protecting Heal (Sciel and Lune).

**Immediately interesting for the "give to everyone" question:**

**SOS Shell (5 LP)** — Shell when falling below 50% HP. Fires automatically, no action required. Pairs cleanly with Shielding Death and Protecting Death as a survivability layer. Very cheap.

**Aegis Revival (5 LP)** — +1 Shield on being revived. Given characters are dying and being revived repeatedly against the Chromatic Lampmaster, this fires reliably and stacks with the shields from Shielding Death. 5 LP each.

**Shell On Rush (10 LP)** — Shell on applying Rush. Sciel's Litheson applies Greater Rush to all allies, so this would give all three main team members Shell every time Litheson fires. That's potentially very strong — passive team-wide Shell every Moon/Twilight phase. Worth considering specifically for Sciel.

**In Medias Res (10 LP)** — +3 Shields on battle start, but max Health halved. Interesting for characters where HP matters less (Verso at 1 HP anyway, Maelle at 1 HP). For them the HP penalty is irrelevant, and +3 shields at battle start is the same as Shielding Death's proc — free early-fight protection.

**Shield Affinity (15 LP)** — +30% damage while having shields, but any damage removes *all* shields at once. Very high risk — one hit strips everything. Probably not worth it.

Given the boss-fight context, the most universally useful additions look like: **Shielding Death + Protecting Death** (already proposed, 15 LP), **SOS Shell** (5 LP, passive safety net), and **Aegis Revival** (5 LP, stacks with revive loops). That's 25 LP per character for a substantial survivability package. Does that feel right, or are some of these overkill?

---

**Matt:** Litheson doesn't trigger Shell On Rush, sadly. Doesn't work with passives.

I have always ignored In Media Res, but you're right about it working well with the 1HP strategy. Yes for Verso and Maelle.

Aegis Revival is probably worth it too for everyone.

The SOS suite might all be interesting for the 1HP builds. Could you pull out all Lumina where name contains "SOS" please?

Does anyone have Shield Affinity at the moment? I feel like I gave that to Maelle. Or was that Powerful Shield or something?

**Claude:** *[Turn 52. Last log: Turn 44.]*

Good correction on Shell On Rush — passive Rush applications don't trigger it. Noted for the data.

*[Queried all SOS Lumina and Shield Affinity]*

*[Turn 52. Last log: Turn 44.]*

**SOS suite:**

- **SOS Shell (5 LP)** — Shell below 50% HP. Useful for anyone.
- **SOS Power (5 LP)** — Powerful below 50% HP. Free damage buff trigger.
- **SOS Rush (LP unknown)** — Rush below 50% HP. LP cost missing from data.
- **SOS Healing Tint (10 LP)** — auto-consumes a Healing Tint below 50% HP. Less relevant for 1 HP builds since they're permanently "below 50%."

For the 1 HP builds specifically (Verso and Maelle), all three non-Tint SOS Lumina fire permanently from the moment Last Chance/Overload drops them to 1 HP — they never leave the sub-50% state. So SOS Shell, SOS Power and SOS Rush become permanent passive buffs rather than emergency triggers. That's very strong for cheap LP. SOS Rush in particular gives permanent Rush to both without needing Sciel or Litheson — and SOS Power gives permanent Powerful on top of the Lithum Shell suite. SOS Healing Tint would just auto-consume Tints constantly, which is wasteful — definitely skip that one.

**Shield Affinity** — shows as unequipped (`equipped_by: None`). So Maelle doesn't currently have it. You may be thinking of **Powerful Shield** (5 LP, +10% damage per shield point) which is in Maelle's active list from the screenshot. That's the one that's deliberately part of her build. Shield Affinity's "all shields removed on any damage" is too punishing for a 1 HP character who can't afford to lose all protection at once.

So the additions shaping up for Verso and Maelle specifically: In Medias Res (+3 shields at battle start, HP halved — irrelevant at 1 HP) + SOS Shell + SOS Power + SOS Rush. Want to add all three SOS to both of them?

---

**Matt:** Is it worth adding the three SOS Lumina to everyone?

**Claude:** *[Turn 53. Last log: Turn 44.]*

Depends on the character. Let me think through each:

**Verso and Maelle (1 HP builds)** — all three fire permanently. Unambiguously yes. The "trigger" is just entering combat after Last Chance/Overload.

**Lune** — enters at full HP and Clea's Life keeps her there. SOS suite fires only if she takes a hit dropping her below 50%. That's the failure state, not the normal state — so these become emergency fallbacks rather than permanent buffs. Still worth having at 5 LP each since they provide meaningful protection when she does get hit, and she has room in the budget. Probably yes.

**Sciel** — same situation as Lune. Full HP normally, SOS only fires on damage. But Sciel is the support anchor — if she goes down the whole combo engine breaks. The emergency fallback case is arguably *more* valuable for her than for Lune. SOS Shell in particular giving her a damage-reduction layer when threatened is worth 5 LP. Probably yes.

**Monoco** — high health pool (9158), Break Specialist build. SOS suite firing on a tanky break-builder isn't particularly synergistic but it's cheap insurance. SOS Rush at battle start might help him act faster for the early break setup. Weakest case of the five, but at 5 LP each it's not a meaningful cost. Marginal yes.

So: clear yes for all five on SOS Shell and SOS Power. SOS Rush has an unknown LP cost — worth checking in-game before committing since "None" in the data could mean it's expensive. Would you want to check the SOS Rush cost before deciding on that one?

---

**Matt:** Probably 5LP. Powerful is not as important for Sciel and Monoco as support characters. Let's just budget for everyone to get everything! Why not?!

Does Sciel have Clea's Life?

**Claude:** *[Turn 54. Last log: Turn 44.]*

Ha — fair enough, at 1 CoL per minute and with builds this deep into optimisation, the marginal cost of a few extra Lumina is trivial.

Sciel doesn't have Clea's Life — looking at her active Lumina from the screenshot, it's not in her list. Her healing is through Protecting Heal and Accelerating Heal (healing allies applies Shell/Rush). She doesn't have a full-HP restore mechanic. Is that intentional, or an oversight? Given her support role she's often spending turns buffing/healing rather than attacking, so she may take incidental damage that Clea's Life can't reliably maintain — but if she's parrying well it could keep her topped up and feed Full Strength if you ever gave her that.

On the broader additions budget, let me tally what we've now agreed for everyone:

- **Shielding Death** (10 LP) — all except Monoco who has it
- **Protecting Death** (5 LP) — all except Monoco who has it  
- **Aegis Revival** (5 LP) — all five
- **In Medias Res** (10 LP) — Verso and Maelle only
- **SOS Shell** (5 LP) — all five
- **SOS Power** (5 LP) — all five
- **SOS Rush** (5 LP est.) — all five
- **Survivor** — Verso and Lune still pending
- **Energy Master** — Monoco pending

That's a substantial CoL spend. Want me to tally the full estimate so you know how much grinding is ahead?

---

**Matt:** Does Sciel have Recovery?

Yes please for the tally.

**Claude:** *[Turn 55. Last log: Turn 44.]*

Sciel does have Recovery active — it's in her screenshot list. Do you know what it does? It's not in my pictos-lumina.json with a clear effect — worth checking if it's a health-restore mechanic that might substitute for Clea's Life for her.

*[Queried Recovery effect and ran full tally]*

*[Turn 55. Last log: Turn 44.]*

**Recovery (10 LP): "Recovers 10% Health on turn start."** That's a meaningful heal-over-time for Sciel — 10% per turn keeps her topped up passively without spending actions on self-healing. It doesn't restore to full like Clea's Life, but for a support character who's spending her turns on Fortune's Fury and Intervention rather than healing herself, it's a practical substitute. Probably why she has it and doesn't need Clea's Life.

**Tally: 270 LP / 270 CoL = 4.5 hours of grinding at the current rate.**

That's a solid session of grinding. A few things to note before you commit:

I included **Breaking Attack for Monoco (10 LP)** from the earlier decision — let me know if that shouldn't be in the list. Also I haven't included Lune's Survivor in the tally since that was already agreed and partially pending — it's 20 LP but I assumed you'd already counted that separately. If not, add another 20 CoL.

One way to reduce the grind: **SOS Rush** has an unknown LP cost (I estimated 5 LP). If it turns out to be higher, the tally shifts. Worth checking before you start grinding.

Also worth asking: does Monoco need Shielding Death and Protecting Death himself, or since he already has them, do we want to give the *other four* those Lumina so that *any* death triggers the buff for survivors — meaning Monoco's death covers allies and vice versa? That's what the tally assumes, which I think is correct.

---

**Matt:** Yes, that's correct. !log

**Claude:** *[Turn 56. Last log: Turn 55 (this log).]*

Logged — Turns 45–56 appended, transcript now at 1016 lines. Last logged turn is **Turn 56**.

*[Turn 56. Last log: Turn 56.]*

A good natural pause point. To summarise where we stand:

**Decided but not yet done (requires CoL grinding):**
- 270 CoL of additions across all five characters (4.5h at current rate)
- Lune's Survivor (20 CoL, separate from the 270)

**Still to discuss:**
- Point 3 from session start: DPS/Support core set rethink
- Empowering Dodge for Maelle
- Data updates for the wrap

Anything else before we move to the core set question?

---

