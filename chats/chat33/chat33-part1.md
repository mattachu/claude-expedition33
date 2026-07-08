<!-- SECTION -->
## Maelle Solo-to-Main Build Import — Turn Order

**Matt:** Hi Claude! Let’s continue to chat about Expedition 33.

Latest startup file is at https://raw.githubusercontent.com/mattachu/claude-tools/318be20/startup.md

Links file attached. You’ll want to read the overview.

(Attached: LINKS.md — session links file, commit 75c47440, latest chat 32)

**Claude:** Welcome back, Matt. Let me grab the startup file.

*[Downloaded startup.md to disk]*

*[Read startup.md]*

Startup file read and defaults loaded. Now the overview, using the pinned commit from your LINKS.md.

*[Downloaded overview file]*

*[Read overview]*

Let me read the truncated mechanics section.

*[Read overview lines 93–132]*

Overview read. Following session-start procedure — fetching the playthrough JSON and setting up the chat 33 transcript file.

*[Fetched playthrough.json; created chat33.md transcript file]*

*[Read playthrough.json]*

Startup file and overview both read, defaults loaded, and the chat 33 transcript is set up. Current state confirmed: Act 3 Phase 4, all five at L99, Endless Tower.

*[Turn 1. No log yet.]*

A couple of standing items before we start, in case any are relevant today:

The one open question in Section 6 — **First Life (15LP)** — is still unresolved, and the playthrough checklist shows why: **Chromatic Lampmaster** (the Endless Tower superboss that drops it) is still `done: false`, as are the **Endless Tower DLC superbosses** (Clea Unleashed, Simon the Divergent Star). So both of those are outstanding if you're heading that way.

I also have a note from the Chat 32 wrap that ended mid-work: an unresolved question about how to handle a superseded **Clea's Life ACTION for Verso's At Death's Door Frenzy build** in `characters/verso.md`, plus a deferred **core Lumina suite review**. I haven't fetched the character or reference files yet — I'll pull those only if today's topic needs them.

What's the session about?

---

**Matt:** I'm pretty much at the end of the game now. I discovered that grinding Renoir's Drafts can provide lots of XP and Colour of Lumina, so all my characters are all level 99 and I have 132 Colour of Lumina to spend on building them up.

There are three issues to deal with, then move on to tweaking Lumina loadouts:

1. I've been testing Maelle with a solo build that does huge one-hit damage. I need to import the learnings from this into her main-team build. 
2. Lune is good but her DPS is nowhere near Maelle and Verso. I think I'm missing something and she could be much more powerful. 
3. Core sets are out of date: I need to update what is possible with the new Colour of Lumina and possibly rethink whether I instead have "DPS" / "Support" core sets rather than "main team" / "reserves" core sets. This can wait until after looking at Lumina for everyone. 

I suggest you download and read overview/party-summary and characters/maelle and then we can look at point 1. You should also download data/pictos-lumina.json but don't read the whole thing — query what is needed.

**Claude:** *[Turn 2. No log yet.]*

Right, that's a clear plan. Fetching the two files to read in full, plus the Pictos/Lumina JSON to query on demand.

*[Fetched party-summary.md, maelle.md, pictos-lumina.json]*

*[Read party-summary.md]*

*[Read maelle.md]*

*[Turn 3. No log yet.]*

All three files loaded. Before proposing changes, here's the core finding from comparing the two builds — and it's mostly a constraints story, so let me lead with the bad news.

**The central problem: most of the solo build's damage can't transfer**

The Solo At Death's Door build's ~2.3× edge (peak 21M) comes overwhelmingly from multipliers **gated on conditions the Clea's Life main build deliberately breaks** — being at ≤10% HP, fighting alone, and refusing healing. Clea's Life is a full-HP, healed, three-person strategy. So the headline numbers do not carry over. Sorting every solo multiplier:

| Solo multiplier | Gate | Transfers to main team? |
|---|---|---|
| At Death's Door (×1.5) | ≤10% HP | ❌ — Clea's Life keeps her at 100% |
| Inverted Affinity (×1.5) | blocks healing | ❌ — kills Clea's Life |
| Confident Fighter (×1.3) | blocks healing | ❌ — kills Clea's Life |
| Solo Fighter (×1.5) | fighting alone | ❌ — allies present |
| Last Stand Critical (100% crit) | fighting alone | ❌ — allies present |
| **Glass Cannon (×1.25)** | none (×1.25 dmg taken) | ✅ — best import, with a caveat below |
| **Immaculate (×1.3)** | until first hit received | ✅ — front-loaded, persists if parrying |
| **First Offensive (×1.5)** | first hit dealt | ✅ — one-shot, front-loaded |
| **Burn Affinity (×1.25)** | target burning | ✅ — if burn uptime arranged |
| **Powerful Shield (×1.1)** | shield on self | ✅ — permanent with Base Shield |
| Augmented First Strike (×1.5) | first hit | already in main build |

The five biggest multipliers are the five that don't transfer. That's the honest ceiling.

**The reframe that matters**

Don't benchmark the main-team Maelle against 21M. The main team gives her **Sciel's Fortune's Fury (×2)** and Intervention — a multiplier the solo build *can't* use. The two builds rest on different foundations. Importing solo learnings = layering the HP-independent multipliers on top of the Fortune's Fury base, not chasing the solo number.

**What's genuinely worth importing**

1. **Glass Cannon (×1.25)** — the clear pick. *Caveat I want to be honest about:* its downside is ×1.25 incoming damage, and Clea's Life only heals if she took **no** damage since last turn. So it's "free" only when she's parrying/dodging cleanly — fine against known bosses, a real risk against unfamiliar ones. Given your documented conservative risk tolerance, this is a "known fights only" toggle, not a permanent fixture.
2. **Powerful On Shell** — your main loadout has Greater Powerful but *not* Powerful On Shell, so the Chat 32 Lithum Shell→Powerful loop (~40% Powerful) isn't fully active on the main build. Cheap to complete.
3. **Front-loaded suite** (Immaculate, First Offensive) + **Burn Affinity** — situational opener gains, worth it given LP isn't tight.

**LP is not your binding constraint:** 56 spare now, plus 132 Colour of Lumina (= +132 to the pool). You can add all the transferable Lumina without cutting anything.

**The bigger lever I can't evaluate yet**

**ACTION:** Open question — Maelle's crit % on the *main* build (Clea's Life / Empowering Break / Shortcut Pictos) is not in the data. The 41% in the files is the solo variant's stat block (Energising Turn / Energy Master / Cheater Pictos). For a single-hit Stendhal nuke, a non-crit halves the hit — so if main-build Maelle isn't effectively crit-capped, fixing crit dwarfs every Lumina above. Solo solves this with Last Stand Critical (100% solo); the main team has no equivalent unless Sciel's kit supplies it.

**ACTION:** Evaluate Glass Cannon + Powerful On Shell for Maelle's main-team build (Chat 33).

Two caveats on my own reasoning: I'm treating the ×-values as your recorded data, and I am **not** asserting the whole chain stacks multiplicatively — EX33 mixes additive and multiplicative, and I haven't verified which of these compound. I can search specific effects against a source if you want that nailed down.

Can you check Maelle's crit % in-game with the main Pictos loadout (Clea's Life / Empowering Break / Shortcut)? That decides whether we're tuning multipliers or fixing a crit hole first.

---

**Matt:** Couple of things:

1. Don't write any actions without checking first. This chat will probably tweak things multiple times, and we don't need to record it until the end.

2. There are two choices for Last Chance builds: either the At Death's Door low-HP build or the Clea's Life Full Strength build. The At Death's Door option unlocks huge damage bonuses but leaves her vulnerable. There's an identical issue with Verso and Overload, and this is what I wrote in his file:

At Death's Door vs Clea's Life (Chat 32): There are two ways of handling the reduction to 1HP from Overload — Clea's Life restores health to full immediately on the following Cheater turn and removes the risk from the health reduction. Alternatively, At Death's Door and several other Lumina provide huge damage boosts when on low health. For most battles, the At Death's Door option is best, as fights are over quickly due to huge damage spikes from Steeled Strike and End Bringer. For some tough boss battles, the Clea's Life option may be required for survivability.

**Claude:** *[Turn 4. No log yet.]*

Both noted — no more ACTION lines until the end, and you're right that I mis-framed it. Let me correct.

I wrongly equated "At Death's Door" with "solo." The low-HP multipliers aren't solo-locked — At Death's Door, Inverted Affinity, Confident Fighter, Glass Cannon, Immaculate, First Offensive, Burn Affinity and Powerful Shield all work in the main team. Only **two** things in that build are genuinely solo-only:

- **Solo Fighter** (×1.5 while alone)
- **Last Stand Critical** (100% crit while alone)

So the real choice for main-team Maelle is the same one you wrote for Verso: At Death's Door as the high-damage default, Clea's Life Full Strength as the survivability fallback for the few bosses that need it. The "import" is just building the **team version** of the At Death's Door build = the solo build minus those two Lumina, minus Monoco's death suite.

Two things make Maelle's case different from Verso's, though, and both point the same way:

1. **Losing Last Stand Critical is a Maelle-only problem.** Verso is already crit-capped from his Pictos (106%), so dropping the solo crit guarantee costs him nothing. Maelle's crit in the solo build was *entirely* Last Stand Critical — her Pictos there (Energising Turn / Energy Master / Cheater) give no crit. Take her out of solo and her crit collapses unless she re-sources it from Pictos (Empowering Break +32%, Shortcut +36%) or elsewhere. For a single-hit Stendhal nuke, a missed crit halves the hit. This is the crux of the whole build.

2. **No Monoco means less survivability than the solo build had.** Her solo 1HP state was scaffolded by Monoco's Auto Death suite firing at battle start — 3 shields, Shell, +4 AP, burns. In Maelle/Sciel/Verso that scaffold is gone, so the team At Death's Door Maelle is genuinely more exposed than either the solo build or Verso's Overload build. And Inverted Affinity / Confident Fighter block Sciel from healing her, so they actively waste Sciel's support.

So the team At Death's Door build is viable, but it lives or dies on the crit answer, and it's the riskier of the two modes by a wider margin for Maelle than for Verso.

Before I go further: what's her crit % with the crit-giving Pictos (Empowering Break / Shortcut) equipped, and how are you running Cheater on the At Death's Door build — Pictos slot or the 40 LP Lumina? That determines whether the third Pictos slot is free for more crit.

---

**Matt:** I'm not sure about your logic for it being more riskier for Maelle than Verso — I think it's more being riskier in the team than in solo. In the team, both Maelle and Verso will be in exactly the same state.

**Claude:** *[Turn 5. No log yet.]*

On the risk point — you're right, my logic was faulty. The Monoco scaffold (Auto Death suite) was specific to the *solo* build; in the team neither Maelle nor Verso has it, so its loss is a team-vs-solo difference, not a Maelle-vs-Verso one. I'll drop that framing. (The one genuine survivability asymmetry that does remain is Verso's Simoso L20 "can't die at Rank A+", which Maelle has no equivalent of — but that's a separate point and not the one I was making.)

On crit — here are the three main-build Pictos as logged:

| Slot | Pictos | Stat boost |
|---|---|---|
| 1 | Clea's Life (L30) | Health +5591 |
| 2 | Empowering Break (L28) | Speed +546, **Crit +32%** |
| 3 | Shortcut (L31) | Speed +672, **Crit +36%** |

So yes — the 41% is her crit with the *solo* Pictos (Energising Turn / Energy Master / Cheater), none of which give crit. It's effectively her crit floor from Luck 99 + Lithum with no crit Pictos. The crit all came from the two Pictos you swapped out:

41 + 32 + 36 = **109% → crit-capped.** That matches your recollection of "above 100%."

This collapses my Turn 3 "crit hole" worry, and it changes the whole calculus:

**If the team At Death's Door build keeps Empowering Break + Shortcut, she's crit-capped without Last Stand Critical.** That was one of the only two genuinely solo-locked Lumina. So losing it costs nothing here. The *only* solo multiplier she actually forfeits going team is **Solo Fighter (×1.5)** — and against that she gains **Fortune's Fury (×2)** plus Intervention, which the solo build never had. Net strongly favourable.

The cost is the third Pictos slot: keeping both crit Pictos means Clea's Life comes out (correct — it's the wrong Pictos for a low-HP build anyway), leaving slot 1 free.

So: how are you running Cheater on this build — 40 LP Lumina, or Pictos? If it's the Lumina, slot 1 is wide open, and the question is just what goes there (AP/utility — Energising Turn or Energy Master being the obvious candidates from the solo loadout). What's your instinct for that slot?

---

**Matt:** Good point on the Simoso perk — that's a huge difference. On the other hand, in a team build, I can use Revive Tints, but when solo, when she's dead, she's dead. 

The question of the the Pictos can be a bit wider than just Clea's Life. We have three Pictos slots, which we can use to:

1. Build critical rate up to 100%
2. Build speed up to similar values with Sciel and Verso
3. Replace high-cost Lumina with free Pictos versions
4. Add extra effects that aren't in her Lumina set

With the availability of CoL, 3 and 4 are much less important. For the solo build, I optimised for speed + Lumina savings. For the team build, the speed should be high but not too separated from team members. It might be worth thinking about turn order at this point.

**Claude:** *[Turn 6. No log yet.]*

Fair on Revive Tints — that's a real team-only safety valve the solo build lacks, though it costs an ally's turn/AP and needs someone standing. It softens the 1HP risk rather than removing it, but it's a genuine point in the team build's favour.

Agreed on devaluing 3 and 4: with CoL plentiful you just buy the Lumina, so a Pictos slot spent to "save LP" is wasted potential. That leaves slots competing between **crit** and **speed**. Let me nail down how many slots crit actually demands before we talk turn order — let me query the data for crit Pictos.

*[Inspected pictos-lumina.json structure; queried all Pictos stat fields for crit/speed values]*

Found something important. Let me pull the full entries for the standout candidates.

*[Queried full entries: The One, Feint, Quick Break, Empowering Break, Shortcut, Energising Turn, Augmented First Strike, Roulette]*

*[Turn 7. No log yet.]*

The data turned up a genuine keystone candidate and reframes the slot question. Let me check the crit arithmetic before I lay it out.

*[Verified crit totals in bash: The One alone 149%; Empowering Break + Shortcut 109%; At Death's Door + Quick Break 111% — all cap]*

The data changes the picture. Three findings:

**1. The One is a potential keystone — crit 108%, "Max Health reduced to 1", 1 LP, obtained, unequipped.** It caps her crit *by itself* (41 + 108 = 149%, hard overshoot), so it frees **both** other slots, and its drawback — permanent 1 HP — is exactly the state the At Death's Door build wants. One slot does the work that currently takes two.

**But there's a critical unknown I won't gloss over:** At Death's Door is "×1.5 **below 10% HP**." If Max HP = 1, she sits at 1/1 = 100%, which may read as *not* below 10% — in which case The One silently switches At Death's Door OFF and guts the build it's meant to serve. I don't know how the game evaluates the threshold when max HP is 1, and this is precisely the kind of interaction the error log says not to assert. So: **test first.** Equip The One, open a fight, and check whether At Death's Door (and any other "below X% HP" Lumina) shows as active. That single test decides the whole Pictos layout:

- **Active** → The One is the build's anchor: caps crit, locks the low-HP state for the whole fight, frees two slots. (Last Chance stays useful for the AP refill + Virtuose entry, just no longer needed to drop HP.)
- **Inactive** → discard The One, cap crit with two crit Pictos instead.

**2. Shortcut is the wrong Pictos for a low-HP build.** Its effect ("immediately play below 30% HP, once per battle") fires and is consumed instantly when she's deliberately at 1 HP — dead weight. **Quick Break** gives identical stats (speed 672 / crit 36%) plus a live effect: "Play again on Breaking a target" — a conditional extra turn. Strict upgrade over Shortcut here, regardless of the The One question.

**3. At Death's Door also exists as a Pictos** (crit 34% + the ×1.5 Lumina free when equipped). So if you go the two-crit-Pictos route, At Death's Door Pictos + Quick Break caps crit at 111% *and* bakes in the build's signature multiplier in one slot.

So the two clean layouts are:

| If The One works | If it doesn't |
|---|---|
| The One (crit cap + 1HP lock) | At Death's Door (crit 34 + ×1.5 free) |
| Energising Turn (speed 1277 + AP) | Quick Break (crit 36 + speed + break retrigger) |
| Quick Break *or* utility slot | Energising Turn (speed + AP) |

On **turn order**: the Fortune's Fury ×2 lands best if Maelle acts *after* Sciel, so Sciel can pre-buff her — which argues for Maelle's speed sitting just *below* Sciel's (~2572), not maxed. But your documented burst is driven by Sciel's **Intervention**-granted turn, which ignores speed order entirely, so raw speed-matching matters less than it first appears. Energising Turn's big speed bump is worth it mainly for the AP and for non-burst turns; it won't break the combo either way.

Can you run the The One test? Everything downstream forks on it.

---

**Matt:** The problem with Fortune's Fury and Cheater is that you can only apply the Fortune's Fury to the first turn, so it doesn't work for Fortune's Fury > Last Chance > Cheater > Stendhal/Gommage. It means that Maelle has to be on Virtuose before Sciel's turn, either through her previous turn or through Lithum's Counterattack effect.

If the turn order is Verso > Sciel > Maelle then Sciel can choose to buff Verso and bring him back in with Intervention, or to buff Maelle in advance of her turn, if she's already in Virtuose. 

If the turn order is Verso > Maelle > Sciel, then there is the option of using Maelle's turn to set up Virtuose and use Fortune's Fury + Intervention for the payoff. 

If the turn order is Sciel > Verso > Maelle, then Sciel could apply Fortune's Fury to both. That loses the ability to setup in advance, though. 

The question really is more about how Sciel acts: acting earlier means she can preapply buffs; acting later means she can judge the situation and rely on Intervention. I lean towards later, I think. Probably Verso > Maelle > Sciel.

**Claude:** *[Turn 8. No log yet.]*

Absorbed the correction — Fortune's Fury buffs only the target's *next* turn and is consumed by the first turn after it lands. So the buffed turn must itself be the Virtuose payoff; she can't spend it entering Virtuose. The free entry route is Lithum's Counterattack→Virtuose (L10), or ending her prior turn in Virtuose.

Your lean toward Sciel-last is right, and the cleanest reason is the one-turn window you just described: applying Fortune's Fury early **commits the ×2 before you know the payoff lands** — if the target's next turn turns out to be setup, or they get interrupted/the enemy reorders, the buff is wasted. Acting last collapses that risk: Sciel sees the board (break state, who's threatened, who's in Virtuose) and applies Fortune's Fury + Intervention *together*, so the buffed turn is guaranteed to be the nuke. Early-Sciel only wins in the narrow case where Maelle is *already* in Virtuose from a counterattack — and Intervention reproduces that payoff anyway, without the timing gamble. Late dominates.

Verso > Maelle > Sciel also gives you the most **reliable** Virtuose entry: Maelle sets up on her own (middle) turn rather than depending on landing a counterattack to trigger Lithum. And with Cheater, that middle turn can be setup *plus* an unbuffed Virtuose nuke, then Sciel's Intervention delivers a second, Fortune's-Fury-buffed nuke — two Virtuose hits per round, one of them ×2. AP permitting, that's the real prize of this ordering.

One dependency this creates that touches the build directly, and I want to flag rather than assume: that order needs Verso leading, Maelle middle, Sciel last. Verso leads fine — he has First Strike. But **Sciel currently also has First Strike** (10 LP in her loadout), which pulls her *early* — the opposite of acting last. And Maelle would need speed above Sciel's (~2572 modified) to sit ahead of her.

So if you commit to Sciel-last, two things follow:
- **Drop First Strike from Sciel.** With both Verso and Sciel carrying it, I'd also want to confirm how First Strike resolves among multiple holders before trusting the order — I don't want to assert the rule. If it's "all First-Strikers act before non-holders, ordered by speed among themselves," then with Maelle *not* holding it she'd be pushed to act *last*, breaking your plan entirely. Worth a quick in-game check.
- **Keep Maelle's speed up** — which lands neatly on the earlier slot question: Energising Turn (speed 1277 + AP) in a free slot keeps her ahead of Sciel and feeds AP for the double-nuke. That's a point in favour of the The One layout, since freeing two slots lets you run The One + Energising Turn + Quick Break.

So before I'd finalise anything: the The One / At Death's Door test, and the First Strike multi-holder check. Do you want to run those, or keep reasoning on paper first?

---

**Matt:** I would want to test them with all three having First Strike. I've done the The One test, but let's finish turn order first. Any good reason why either Verso or Maelle should go first, or does it not really matter?

**Claude:** *[Turn 9. No log yet.]*

Marginal edge to **Verso first**, but it's genuinely marginal — the dominant lever is Sciel-last + Intervention, and that's settled regardless of how the other two are ordered.

The reasoning that does favour Verso first is the same logic you used for Sciel: the character who acts later acts with more information. Verso's opening is fixed setup — base attack to start building Rank/charge — and it needs no knowledge of the board. Maelle's opening is conditional: is she already in Virtuose, is the target burning (for Burn Affinity ×1.25), is break close, does she nuke now or set up for Intervention? Putting the information-independent turn (Verso) first lets Maelle's more reactive turn resolve with Verso's outcome already known.

There's one concrete cross-dependency pointing the same way: Verso's Simoso has a 20% burn chance on Light damage, so a Verso-first turn can seed a burn for Maelle's Burn Affinity. It's unreliable (one-in-five, and you'd want it more consistent than that), so don't weight it heavily — but it only helps if Verso precedes her.

The reverse case — Maelle first — only wins if Maelle applies an enemy debuff that Verso then exploits that same round (enemy Defenceless via Offensive Switch, or pushing the break). That's a real pattern, but it's situational and you'd typically be driving Maelle's payoff through Sciel's Intervention anyway, not front-loading it for Verso's benefit.

Honest caveat: I haven't loaded Verso's file this session, so beyond the Simoso burn (which is in the overview) I'm not asserting what else Verso's skills apply. If he has a reliable Mark or Defenceless application on his opener, that could tip it either way and I'd want to check before treating Verso-first as fixed.

So: Verso > Maelle > Sciel, with the Verso/Maelle ordering held lightly. Net effect on the build — Maelle needs speed above Sciel's (~2572) and below Verso's, which the Energising Turn slot comfortably handles.

Now — what did the The One test show? At Death's Door active or not at 1/1 HP?

---

**Matt:** !log

**Claude:** *[Turn 10. Last log: Turn 10 (this log).]*

Logging the session so far — first log, so all turns from the start, verbatim. Appending in three parts... Logged. Section appended with all nine turns verbatim (Turns 1–9), tool calls reduced to bracket notes, everything else copied as-is. Transcript now stands at 278 lines.

Correction to my header above — last logged turn is **Turn 9**, not 10; this logging action is Turn 10 and isn't itself logged yet.

*[Turn 10. Last log: Turn 9.]*

Ready for the The One test result — At Death's Door active or inactive at 1/1 HP? That forks the whole Pictos layout.

---

<!-- SECTION -->
## The One Test Result and Turn-Order Speed Analysis

**Matt:** Could you present the transcript file please

**Claude:** *[Turn 11. Last log: Turn 9.]*

*[Presented chat33.md]*

Here's `chat33.md` — the session transcript through Turn 9. Note this isn't a full `!close` (no verbatim sampling check run yet); it's the current state of the log if you want to eyeball it.

Still holding for the The One test result whenever you're ready.

---

**Matt:** So, The One counts 1HP as max health, so At Death's Door didn't fire, and possibly some others. Rather than 21m damage, she only did 13m.

**Claude:** *[Turn 12. Last log: Turn 9.]*

That settles it — **The One is out.** Confirmed empirically rather than assumed, which is exactly why it was worth the test: it would have cost you ~38% of her damage silently. The 1/1 = "full HP" reading kills At Death's Door, just as flagged.

Quick sanity-check on the number:

*[Confirmed damage-drop logic in bash: At Death's Door alone (1.5x) would predict ~14m; observed 13m implies at least one more %-HP-gated bonus also dark]*

Confirmed: 13m is *below* the 14m that losing At Death's Door alone would predict, so at least one more %-HP-gated bonus also went dark. The One is disqualified for this build.

So the fork resolves to the right-hand column, and the build reverts to the **genuine** low-HP method: **Last Chance drops her to 1 HP against a normal max**, so 1/8588 is well below 10% and At Death's Door fires properly. The One's mistake was changing *max* HP; Last Chance changes *current* HP, which is what the multipliers actually read.

That leaves the Pictos as **two crit + one dial**:

- **Quick Break** (crit 36, speed 672, "play again on Break") — replaces Shortcut, whose effect is dead weight at 1 HP
- **Empowering Break** (crit 32, speed 546, Powerful on Break — feeds the Powerful On Shell loop) — already hers, keep it
- Crit lands at **109%, capped.** Clea's Life comes out (wrong Pictos for low-HP), Shortcut comes out.

The **third slot is your turn-order dial**, and here's the catch I can't resolve on paper: the two crit Pictos already add +1218 speed. Adding **Energising Turn** (speed 1277 + AP) on top brings Pictos speed to ~2495 — which may well shove Maelle *past* Verso, flipping your Verso > Maelle > Sciel order into Maelle-first. That's only a marginal loss (we agreed Verso-first is a slight preference, not load-bearing), but it's the opposite of what you set out to build.

So the third slot is a genuine choice between **AP/max speed** (Energising Turn) and **holding Maelle below Verso** — and I can't pick it without the actual in-game speed values.

Can you read off the modified Speed for all three — Maelle (with Quick Break + Empowering Break equipped), Verso, and Sciel? That tells us whether Energising Turn fits or overshoots, and pins the third slot.

---

**Matt:** Did you already fetch party-summary.md? Are the speeds in there?

**Claude:** Yes — I have them, and I shouldn't have asked you to read them off. My mistake. The one wrinkle that made me hesitate (but doesn't excuse it) is that the Maelle row in party-summary is her **solo** stat block, so I can't read her team-build speed directly — but I can derive it. Let me do that.

*[Derived Maelle's team-build speed from base + Pictos in bash]*

Derived base speed is ~1274, and the numbers reframe the whole turn-order question:

| Maelle build | Maelle spd | Natural order (fast → slow) |
|---|---|---|
| 2 crit Pictos only | 2492 | Sciel > Maelle > Verso |
| 2 crit + Energising Turn | 3769 | Maelle > Sciel > Verso |

Two things fall out, and the second is the important one:

**1. Verso is the *slowest* of the three (2100 < Sciel 2572).** So "Verso first" cannot come from speed at all — it can *only* come from First Strike. No amount of Maelle tuning changes that.

**2. This collides with your "all three have First Strike" plan.** If all three carry First Strike, the party acts before enemies but intra-party order just falls back to *speed among the holders* — which is Maelle (with ET) > Sciel > Verso, i.e. **Verso ends up last, not first.** The exact opposite of Verso > Maelle > Sciel.

So you can't have both "all three First Strike" *and* "Verso first." They're mutually exclusive if First Strike resolves by speed among holders (which is the rule your in-game test needs to confirm — I'm not certain of it).

To actually get **Verso > Maelle > Sciel**, the configuration would be: **First Strike on Verso only**, Sciel drops it, and Maelle runs **Energising Turn** to clear Sciel's 2572 (the two crit Pictos alone leave her at 2492, just *under* Sciel — so without ET, Sciel beats her). That gives Verso (First Strike) → Maelle (3769) → Sciel (2572). ✓

Caveats: Verso's 2100 and Sciel's 2572 are their *current* builds — if you retune either this session those shift. And I'm treating "higher speed acts earlier" as the model; the First-Strike-among-multiple-holders rule is the thing to pin down in your test.

So Energising Turn earns the third slot *if* you want Maelle ahead of Sciel — which the Verso-first plan requires. Does that change how you want to run First Strike?

---

**Matt:** Ok, interesting. I think Verso's speed used to be higher. It needs to be higher. I think we need to think about Pictos for all three at the same time. 

Note on Quick Break: its effect never fires with Cheater. However, Shortcut's effect does fire with Cheater. So Maelle gets three turns in a row if she uses Last Chance. That allows Last Chance > Stendhal > Last Chance > Fortune's Fury > Intervention > Stendhal. So it is valuable, if not quite as intended. 

Shortcut is cheap in LP, so if not used as a Pictos is not a big deal. 

Let's download and read Sciel and Verso's character files.

**Claude:** *[Turn 13. Last log: Turn 9.]*

Taking the Shortcut correction — and I got that one wrong twice over. I called Shortcut "dead weight at 1 HP," which directly contradicts your own documented Chat 30 finding (the confirmed three-turn sequence: normal → Cheater → Shortcut on the sub-30% drop). I should have caught that in the file. And I didn't know Quick Break's retrigger doesn't fire off a Cheater turn. Both corrections point the same way:

**Shortcut stays.** Same stats as Quick Break (speed 672 / crit 36) but its effect is the *third* turn that enables Last Chance → Stendhal → Last Chance → [Sciel: Fortune's Fury + Intervention] → buffed Stendhal. Quick Break's effect is dead next to Cheater. So Quick Break is off the table; my Turn 7 "strict upgrade" claim was backwards.

And you're right that the effect being cheap as Lumina (5 LP) means the *slot* decision is really just about stats — but since Shortcut-as-Pictos gives the stats *and* the effect for free, there's no reason to displace it.

Agreed on doing all three together — turn order is a three-body problem, and "Verso needs to be faster" is a Verso-Pictos change, not a Maelle one. Let me get his and Sciel's files.

*[Fetched verso.md and sciel.md]*

*[Read verso.md]*

Let me read Verso's Pictos and Lumina sections.

*[Read verso.md Pictos/Lumina/skills section]*

Verso read. One thing already stands out before I get Sciel: Verso has **Luck 0**, so essentially all his crit (106%) comes from his three Pictos — Second Chance (15) + Sweet Kill (36) + Alternating Critical (50). All three slots are doing crit duty, which is exactly why he has no room for speed. And Alternating Critical's *effect* is dead weight on him (your own note: no synergy at 100% crit) — it's there purely as a 293-speed / 50-crit stat stick. That's the lever, but it's tangled with the crit cap. Let me get Sciel before I work it.

*[Read sciel.md]*

*[Turn 14. Last log: Turn 9.]*

(Side note: Sciel's file line 267 already documents the Quick Break / Cheater rule as a logged error-to-avoid — so that correction was on record and I missed it. Noted.)

Reading the three together, the turn-order problem isn't really a Maelle problem — it's a **Verso problem with a structural cause**, and there's a confounder that may make the whole thing moot. Three findings:

**1. Verso is the slowest *and* the hardest to speed up.** Base speeds: Verso 1135, Maelle 1274, Sciel 1274. So Verso is intrinsically last. Worse, he has **Luck 0**, so all his crit (106%) is bought with all three Pictos slots — he has *zero* room for a speed Pictos without dropping under the crit cap, which on a 13-hit Steeled Strike is ruinous. Maelle (Luck 99, crit in 2 slots) and Sciel (Luck 99) don't have this problem. Verso does. "Verso needs to be faster" runs straight into "Verso can't free a slot for speed."

**2. The only real unlock for Verso's speed is a Luck respec.** Move some points Might→Luck so crit comes partly from the *attribute*, which frees a Pictos slot for a high-speed stick (Energising Turn 1277, etc.). Alternating Critical is the slot to reclaim — its effect is already dead on him (no synergy at 100% crit), so it's a pure 293-speed stat stick you'd be upgrading. Cost: Might points = less raw Steeled Strike damage. That's a real trade and worth modelling, but note it reopens the "Might post-crit-cap" decision, which assumed crit stays on Pictos.

**3. The confounder — and I think this is the big one: static Speed may barely matter in your actual fights.** Look at what's on the field every turn: Litheson L4/L10 gives **all allies Greater Rush + all enemies Greater Slow** during Moon/Twilight; Verso's **Auto Rush** (3 turns from battle start); Sciel's **All Set** (Rush to all); plus **Intervention** grants turns on demand and **Delaying Slash** pushes an enemy's turn back. Between them, the team manipulates turn order dynamically far more than the Speed stat does. The static 1135/2492/2572 numbers really only govern the *opening* actions before any of that lands.

So before you respec Verso or jockey Pictos for raw speed, I'd want to know: **what does the turn order actually look like in a real fight once Litheson phases + Auto Rush are active?** It's plausible the "Verso too slow" problem is an artefact of reading static stats and is already solved in play. If so, the speed spend is wasted and those slots/attribute points are better used elsewhere.

One genuine tension to name regardless: Sciel's file says she was *deliberately* built fast ("needs high speed… ideally goes first or second," and two logged decisions to guarantee it). Your Turn-8 "Sciel acts last" reverses that. It's justified by the Intervention-react logic, but it is a reversal — worth being deliberate, not incidental.

So my recommendation on sequencing: confirm the in-fight order first (one Endless Tower fight, watch the turn track with Litheson active). That tells us whether Verso needs the Luck respec at all. Want to check that before we commit to any speed plan?

---

**Matt:** !log

**Claude:** *[Turn 15. Last log: Turn 14.]*

Logging Turns 11–14 (everything since the last section). Appending now... Logged — Turns 11–14 appended as a new section, transcript now at 399 lines. Last logged turn is **Turn 14**.

*[Turn 15. Last log: Turn 14.]*

Back to you on the open question: do you want to check the actual in-fight turn order with Litheson phases active before we commit to any speed plan for Verso?

---

<!-- SECTION -->
## Verso and Sciel Speed Tuning — Final Pictos Set

**Matt:** Verso, when he had Chevalam, started every fight with Rush. That meant he could always act first. When I switched to Simoso, I gave him Auto Rush to keep that situation.

Once Sciel applies her Greater Rush, that replaces Verso's Auto Rush and all three characters have the same Greater Rush effect. From that point on, I think they go in turn order.

I haven't observed what happens with First Strike too.

A problem to avoid is that Sciel drops behind Verso, and an enemy gets a chance to interrupt Steeled Strike before she can use Intervention. But then the same thing happens if she pushes ahead of Verso. I think the key thing is to keep Verso and Sciel's speeds similar. That has been lost by swapping in Alternating Critical for the 50% Crit.

Verso did used to have some points in Luck. I moved them into Might to maximise damage. I'd still prefer to keep him that way if possible.

How about swapping out Second Chance instead for a Pictos that gives at least 9% Crit chance but also boosts speed?

**Claude:** *[Turn 16. Last log: Turn 14.]*

Good framing. Let me check what's available that gives both crit and speed, with enough crit to stay capped when replacing Second Chance (currently giving 15%)...

*[Turn 16. Last log: Turn 14.]*

With Sweet Kill (36) + Alternating Critical (50) staying, the crit floor from those two plus Luck 0 is ~91%. So the replacement needs **≥9% crit** to stay capped — and it needs meaningful speed.

The standout candidates from the list, filtered for ones Verso would actually use...

All of them cap crit, so the question is purely about which effect is most useful. Here's the shortlist with honest assessments:

**Energising Attack I** (speed 958, crit 18%) — highest speed of the lot, nearly matching Energising Turn's 1277. Effect (+1 AP on base attack) is live every turn since Verso's rotation starts with a base attack. Good fit both as a stat stick and as a working effect.

**Energising Stun** (speed 519, crit 31%) — effect (+1 AP on hitting a Stunned target with a Skill) synergises directly with End Bringer, which you use on stunned targets regularly. Real value, though only in fights where stun is active.

**Rush On Powerful** (speed 639, crit 35%) — I need to flag uncertainty: does Verso actually *apply* Powerful in his rotation? If yes (e.g. Empowering Break Lumina firing), this grants Rush on top. If not, the effect is dead. I don't want to assert which without checking — but the stats (639 / 35) are strong regardless.

**Quick Break** (speed 672, crit 36%) — pure stat stick for Verso same as Maelle (effect dead with Cheater), but better stats than Energising Stun. Honest pick if you just want raw speed + crit with no effect dependency.

**Second Chance's *effect*** is worth naming explicitly before dropping it: once-per-battle full-HP revive. You have it as Lumina in the core set (40 LP) already, so dropping the Pictos version doesn't actually lose the effect — it just costs 40 LP. Given LP is no longer tight, that's probably fine, but worth confirming that's your intention.

My read: **Energising Attack I** if you want speed-maximised and the AP utility; **Quick Break** if you want the cleanest stats with no effect uncertainty; **Energising Stun** if end Bringer stun fights are common enough to justify slightly less speed. What's your instinct?

---

**Matt:** I think Energising Attack I would be too much speed — he would be over 3000 speed and would pull away from Sciel. Worth considering if Sciel gets faster later. Energising Stun seems the best fit.

**Claude:** *[Turn 17. Last log: Turn 14.]*

Agreed — let me verify the numbers before we commit.

*[Calculated Verso speed with Energising Stun vs Energising Attack I replacing Second Chance]*

- Verso current (Second Chance): 2100
- Verso + Energising Stun: 2619 (gap to Sciel: −47)
- Verso + Energising Attack I: 3058 (gap to Sciel: −486)

*[Turn 17. Last log: Turn 14.]*

That confirms your instinct exactly. Energising Stun puts Verso at **2619** — just **47 above Sciel** at 2572. Close enough that Rush/Greater Rush effects will keep them moving together, which is exactly what you want for the Steeled Strike + Intervention timing. Energising Attack I would push him to 3058, a 486-point gap that risks the separation problem you described.

One thing to flag on the 47-point margin: that's tight enough that any speed change to Sciel later this session could flip their order. Worth keeping in mind as we look at Sciel's Pictos. But for the core objective — Verso and Sciel staying close — Energising Stun is the right call.

So for Verso, the proposed change is: **swap Second Chance Pictos → Energising Stun Pictos.** Second Chance effect is retained via the 40 LP Lumina already in his loadout, so nothing is lost there.

That leaves Verso's Pictos as: Sweet Kill (31) / Alternating Critical (29) / Energising Stun — crit 91 + 36 + 31 = ~122%, capped, speed 2619.

Ready to move to Sciel and Maelle's Pictos, or do you want to settle anything else on Verso first?

---

**Matt:** I've gone with:
* Maelle: Empowering Break, Shortcut, Energising Turn => Crit 109%, Speed 3769
* Verso: Alternating Critical, Sweet Kill, Energising Stun => Crit 122%, Speed 2619
* Sciel: Energy Master, Rush On Powerful, Painter => Health 7390, Speed 2432, Crit 107%

In terms of who goes first, it's still unclear, as in one fight Maelle went first, but against a different enemy, Verso went first. I will monitor turn order in a few fights.

I lost a fight against the Chromatic Lampmaster. When the reserve team came in, Monoco still had his Auto Death build, which was an oversight. But the three shields from Protecting Death were very helpful. Characters can die and be revived multiple times, so these death buffs might be good for everyone.

!log

**Claude:** *[Turn 18. Last log: Turn 17 (this log).]*

Two things to pick up after logging — noted on both. Logging Turns 15–17 now... Logged — Turns 15–18 appended, transcript at 480 lines. Last logged turn is **Turn 18**.

Two things to pick up:

**Turn order** — the variance (Maelle first vs Verso first in different fights) is consistent with enemy Speed affecting where party members slot in among themselves. Worth a few more observations before drawing conclusions, as you said.

**Death buffs for everyone** — this is worth thinking about properly. You've confirmed that characters can die and be revived multiple times, which means Protecting Death's three shields aren't a one-fight fringe case — they're a reliable mid-fight resource for any character who goes down. The question is whether that's worth a Lumina slot on characters who aren't currently running death builds. Want to park that as a Lumina review item for when we get to point 3, or look at it now alongside the Monoco question?

---

