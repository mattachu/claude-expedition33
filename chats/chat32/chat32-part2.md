<!-- SECTION -->
## Solo Maelle — Monoco Death Build and Damage Analysis

**Matt:** I'm interested in building a max-powered solo Maelle.

Firstly, I'm wondering about using Monoco for Auto Death — there are five characters and can only have three in the reserve team (strongest three are Verso, Sciel and Lune), so it makes sense to have Monoco in the original party to make sure I get the three I want in reserve. If I give Monoco Auto Death and Death Bomb, he does damage to all enemies when he dies at the start. There are also a load of death-related Lumina that I've stacked on him. Could you query a list of all Pictos in the data file where the category includes "death" and show me the name and effect, please?

**Claude:** *[Turn 28. Last log: Turn 27.]*

*[Queried pictos-lumina.json for all Pictos with category including death]*

Eight death-category Pictos, all obtained:

| Pictos | Effect |
|---|---|
| Auto Death | Kill self on turn start |
| Breaking Death | Fully charge enemy break bar on death |
| Burning Death | Apply 3 Burn to all enemies on death |
| Death Bomb | On death, deal damage to all enemies |
| Energising Death | On death, +4 AP to allies |
| Healing Death | On death, rest of Expedition recover all Health |
| Protecting Death | On death, allies gain Shell |
| Shielding Death | On death, allies gain 3 Shield points |

That's a strong death-trigger package. With Auto Death + Death Bomb as Pictos (two slots used), you've still got one Pictos slot free on Monoco. The Lumina versions (Breaking Death, Burning Death, Energising Death etc.) can stack on top via LP. What's the third Pictos slot, and how are you thinking about the Lumina loadout?

---

**Matt:** I'll probably do them all as Lumina, as he doesn't really need high stats except Crit so the Death Bomb goes Critical (I think). He won't need any survival Lumina, so I have loads of LP free.

There is some overlap here with the solo Lumina, such as Protecting Death and Protecting Last Stand. So I can possibly skip some of the solo Lumina and rely on the death effects, as I want as many LP as possible on Maelle for damage Lumina.

Next, could you search for endgame solo builds for Maelle and compile a list of relevant Lumina and effects.

**Claude:** *[Turn 29. Last log: Turn 27.]*

*[web_search: Clair Obscur Expedition 33 Maelle solo build endgame Lumina damage 2025]* *[web_search: Clair Obscur Expedition 33 Maelle best weapon post-patch endgame 2025 Stendhal party build]* *[web_fetch: screenrant.com best solo build]* *[web_fetch: keengamer.com Maelle build guide]*

Dead Energy I & II — our data shows both as "+3 AP on killing an enemy," not a damage scaling effect. The Keengamer guide described them as "high damage and crit scaling" but that appears to be a guide error. For a solo single-target boss fight, AP-on-kill is end-of-battle and largely useless.

Sweet Kill — our data shows "Recover 50% Health on killing an enemy," not a damage boost. For a Last Chance low-HP build, this is actually counterproductive — it would heal Maelle back up and cancel the low-HP synergies.

Critical Moment — LP cost shows as null, suggesting it's Pictos-granted (free LP).

Last Stand — not in our data file at all.

Here's the compiled list of genuinely relevant solo Maelle Lumina, filtered for Stendhal single-hit boss damage:

| Lumina | LP | Effect | Notes |
|---|---|---|---|
| Painted Power | 5 | Damage can exceed 9,999 | Essential |
| Confident Fighter | 15 | 30% increased damage, can't be healed | Strong, no downside in solo |
| Augmented Attack | 7 | 50% increased Base Attack damage | Stacks well |
| Augmented First Strike | 5 | 50% increased damage on first hit, once per battle | One-shot builds love this |
| Critical Moment | free? | 50% increased Crit Chance if Health below 30% | Pairs with Last Chance |
| Shortcut | 5 | Play immediately when falling below 30% HP, once per battle | Pairs with Last Chance |
| AP Discount | 30 | Skills cost 1 less AP | Helps chain Stendhal |
| Energy Master | 40 | Every AP gain increased by 1 | Good with Cheater rotation |
| Cheater | 40 | Extra turn after using a skill, once per turn | Already central to build |
| Auto Rush | 10 | Apply Rush for 3 turns on battle start | Speed/damage boost opener |
| Survivor | 20 | Survive fatal damage with 1 HP, once per battle | Keeps alive at 1 HP for low-HP synergies |
| Dodger | 1 | +1 AP on Perfect Dodge | Cheap AP generation |

Lumina to avoid: Sweet Kill (heals, kills low-HP synergy), Dead Energy I & II (AP on kill = useless vs single bosses).

Painted Power is consistently cited as essential for endgame Maelle. The solo build works by pairing Last Chance with Stendhal to deal extreme single-target Void damage, with the downsides of losing all shields and becoming Defenceless being offset by the massive damage output.

How does this compare against what Maelle currently has equipped? Want me to fetch her character file to check?

---

**Matt:** "Last Stand" refers to a suite of about seven different Lumina. Query the data file for Lumina where the name **contains** Last Stand rather than **is** Last Stand.

**Claude:** *[Turn 30. Last log: Turn 27.]*

*[Queried pictos-lumina.json for all Lumina with names containing Last Stand]*

Four in the file, all obtained, all 3LP each:

| Lumina | LP | Effect |
|---|---|---|
| Accelerating Last Stand | 3 | Gain Rush if fighting alone |
| Empowering Last Stand | 3 | Gain Powerful if fighting alone |
| Last Stand Critical | 3 | 100% Critical Chance while fighting alone |
| Protecting Last Stand | 3 | Gain Shell if fighting alone |

All four fire on "fighting alone" — so solo Maelle gets Rush, Powerful, Shell, and 100% Crit Chance for just 12LP total. That's exceptional value. Last Stand Critical in particular is transformative — it makes crit-scaling Lumina fully reliable rather than probabilistic.

The data only has four, so there are more in the game not yet obtained. Do you know which others you have or are missing?

---

**Matt:** Also "Solo Fighter" isn't in your list.

Critical Moment is irrelevant once you have Last Stand Critical, as far as I can tell. So might as well keep Clea's Life and use Full Strength.

Can you pull out all Lumina from the data file with category "damage"? I've seen things like Immaculate and Glass Cannon suggested for this build.

**Claude:** *[Turn 31. Last log: Turn 27.]*

Agreed on Critical Moment — Last Stand Critical gives 100% crit chance while fighting alone, which fully supersedes it. And Full Strength (25% damage on full health) is interesting given that point: Clea's Life restores her to full HP on turn start after Overload, potentially enabling Full Strength on the turn she fires Stendhal if the timing works. Worth thinking through.

*[Queried pictos-lumina.json for all Lumina with category damage]*

40 damage-category Lumina, all obtained except Inverted Affinity (5LP) and Powerful Shield (5LP). Highlighting the ones most relevant to solo Maelle Stendhal:

**Core damage amplifiers:**
- Solo Fighter (1LP) — 50% more damage fighting alone. Absurdly cheap.
- Glass Canon (10LP) — 25% more damage, take 25% more. Irrelevant downside when one-shotting.
- Immaculate (10LP) — 30% more damage until hit received. Fires reliably on the first Stendhal.
- Confident Fighter (15LP) — 30% more damage, can't be healed. No downside in solo.
- At Death's Door (5LP) — 50% more damage below 10% HP. Pairs perfectly with Last Chance.
- Greater Defenceless (15LP) — +15% to Defenceless damage amplification. Stendhal leaves her Defenceless, so this amplifies the next hit.
- Full Strength (15LP) — 25% on full health. Situational with Clea's Life.
- Warming Up (15LP) — +5% per turn up to 25%. Only useful if the fight goes multiple turns.
- Gradient Overcharge (15LP) — consume 3 Gradient charges for 200% more damage this turn. Huge if Sciel can supply charges.
- Augmented First Strike (5LP) — 50% on first hit, once per battle.
- Frenzy (20LP) — 10% per successive skill hit. Only relevant for multi-hit skills, not Stendhal.
- Feint (15LP) — 5th hit of a skill deals 600% more. Again multi-hit, not Stendhal.

**Ones to skip for single-hit Stendhal:**
Frenzy, Feint, Double Third, Trigger-Happy, Consuming Attack — all multi-hit dependent.

The cheap high-value picks for solo Stendhal are clearly Solo Fighter (1LP), At Death's Door (5LP), Glass Canon (10LP), and Immaculate (10LP). Greater Defenceless (15LP) is also interesting since Stendhal itself triggers Defenceless — does that mean Greater Defenceless applies to the following hit rather than Stendhal itself?

---

**Matt:** I have Inverted Affinity and Powerful Shield now, I think that's in an update action above already.

Greater Defenceless is about applying Defenceless to an enemy, not to self. Doesn't work with Stendhal. Also, it seems like the Shell from Lithum cancels out the Defenceless from Stendhal. I might look that up and check.

Interesting, I had forgotten At Death's Door. Combined with Confident Fighter that is pushing more towards sticking on 1HP after Last Stand rather than healing. Risky though. If she's not being healed, we can add in Inverted Affinity as well, which is quite a combo.

There are also burn-related Lumina that increase damage. Could you have a look at that category too? Burning Death on Monoco means all enemies will be burning at the start, and I can use Pyrolyse and Burning Canvas with Maelle if needed.

**Claude:** *[Turn 32. Last log: Turn 27.]*

Noted on Greater Defenceless — correction taken. And the Shell/Defenceless interaction is worth checking; if Lithum's Shell overwrites Stendhal's Defenceless debuff that could be a real issue for any build relying on Defenceless amplification.

*[Queried pictos-lumina.json for all Lumina with category burn]*

Nine burn-category Lumina, all obtained:

| Lumina | LP | Effect |
|---|---|---|
| Burn Affinity | 10 | 25% increased damage on Burning targets |
| Burning Break | 3 | Apply 3 Burn stacks on Breaking a target |
| Burning Death | 5 | Apply 3 Burn to all enemies on death |
| Burning Mark | 15 | Apply Burn on hitting a Marked enemy |
| Burning Shots | 3 | 20% chance to Burn on Free Aim shot |
| Consuming Attack | 10 | Base attack consumes up to 100 Burns to deal 10% more damage per Burn consumed |
| Critical Burn | 5 | 25% increased Crit rate on Burning targets |
| Double Burn | 30 | On applying a Burn stack, apply a second one |
| Longer Burn | 15 | Burn duration increased by 2 |

For the solo Maelle build with Burning Death on Monoco, the most directly relevant is Burn Affinity (10LP) — if all enemies start burning from Monoco's death, every Stendhal hit gets 25% bonus damage for just 10LP. Very efficient.

Critical Burn (5LP) is also cheap and useful — 25% extra crit rate on burning targets stacks on top of Last Stand Critical's 100% (though arguably redundant once you're already at 100% crit).

The rest (Double Burn, Longer Burn, Burning Mark) are more useful for a sustained burn-stacking build with Burning Canvas than for a single Stendhal hit.

One question worth flagging: does Burning Death fire before Maelle's first turn, giving her time to use Stendhal on a burning enemy? That depends on turn order — specifically whether Monoco dies before Maelle acts.

---

**Matt:** Double Burn and Longer Burn could be put on Monoco to power up Burning Death. Yes, Auto Death is at Battle Start, not Turn Start.

You still haven't got Defenceless right. Defenceless is a debuff that means damage on the Defenceless character is increased. If you apply it to an enemy (e.g. Grosse Tete Whack) then you can do more damage on that enemy. Some enemies have attacks that apply Defenceless to my characters, which means they take more damage. Stendhal applies Defenceless to Maelle, which makes her more vulnerable. It's not a good thing.

It would be good if there was a Marking Death as well. Using Lithum means I can't use any of the marking weapons like Licorum. Could possibly add Marking Shots, but that uses AP for the Free Shots.

**Claude:** *[Turn 33. Last log: Turn 27.]*

Defenceless correction understood and taken — it's purely a debuff (damage received multiplier), so Stendhal applying it to Maelle is a vulnerability, not a benefit. Greater Defenceless amplifies damage dealt to Defenceless enemies, which is why it's useful against bosses you can inflict it on, and irrelevant to Maelle's own Stendhal use. Sorry for the repeated confusion on that.

The Monoco burn stack setup is clever — Double Burn and Longer Burn on him mean Burning Death fires with amplified stacks that last longer, giving Maelle more turns of Burn Affinity uptime. And Auto Death at Battle Start before any turns are taken means the burns are definitely up before Maelle acts.

On Marking Death — let me check whether it exists in the data at all.

*[Queried pictos-lumina.json for all Mark-related Lumina]*

No Marking Death in the data — it doesn't exist as a Lumina. The mark-related options are all hit-triggered rather than death-triggered.

For getting Mark onto enemies without a marking weapon, the options in the data are: Marking Shots (3LP, 20% chance on Free Aim — AP cost as noted), Marking Break (5LP, on Break — requires breaking the enemy first). Neither is ideal for a solo build where you want Mark up immediately.

One thought: Sciel is in your reserve team and she has strong Mark application natively. If reserve characters can apply buffs/debuffs before or during combat in some way, that might be worth investigating. Otherwise, for a true one-turn Stendhal kill, Mark probably isn't reliably available without a dedicated support turn.

The burn route via Monoco seems more reliable for the solo build — guaranteed at battle start with no AP cost, and Burn Affinity (10LP) gives a clean 25% damage bonus with no conditions beyond the burns being present.

---

**Matt:** Ok, so two options are Clea's Life vs At Death's Door:

**Clea's Life**
- heal after Last Chance
- 25% damage boost from Full Strength
- hard to kill

**At Death's Door**
- don't heal after Last Chance
- 50% damage boost from At Death's Door
- 30% damage boost from Confident Fighter
- Inverted Affinity blocks healing, 50% damage for three turns at battle start
- highly vulnerable

**Available to both**
- Glass Cannon 25% damage boost
- Immaculate 30% damage boost
- Solo Fighter 50% damage boost
- Burn Affinity 25% boost while burning
- Augmented First Strike 50% boost on first hit
- Powerful Shield 10% boost per shield on self (3 at start from Shielding Death, at least 1 guaranteed by Base Shield)

That's quite a lot of multipliers! Along with 300% from Virtuose.

Definitely looks like the At Death's Door build has strong damage benefits. I should try it for a bit and see if I can handle the vulnerability.

**Claude:** *[Turn 34. Last log: Turn 27.]*

The damage gap is substantial. Those three extra multipliers on the At Death's Door build — At Death's Door (×1.5), Confident Fighter (×1.3), Inverted Affinity (×1.5) — multiply together to roughly ×2.9 extra on top of everything else, vs Full Strength's ×1.25. If the multipliers are applied multiplicatively (which they appear to be in this game), the At Death's Door build is around 2.3× more powerful than Clea's Life, all else equal. That's not close.

A few things worth flagging:

**Inverted blocking healing** — our data just says "50% increased damage while Inverted," it doesn't explicitly mention blocking healing. Worth verifying in-game whether the Inverted status has that additional effect, or whether Confident Fighter is doing all the healing-blocking work.

**The shell buffer helps more than it might seem.** Protecting Last Stand (Shell) + Shielding Death (3 shields from Monoco) + Base Shield (1 per turn) means she has meaningful shield HP at battle start even in the glass cannon build. Glass Cannon's "take 25% more damage" only matters if something gets through all that.

**Augmented First Strike timing** — worth noting this fires on the first hit of the battle, so ideally Stendhal is that first hit. If she has to take a turn before Stendhal for any reason, that 50% is lost.

**LP headroom** — At Death's Door (5LP) + Confident Fighter (15LP) + Inverted Affinity (5LP) = 25LP extra vs Full Strength (15LP). Net cost of the upgrade is only 10LP.

Trying it is the right call. The vulnerability is real but the shield buffer from Monoco's death suite gives more protection than a raw 1HP figure suggests.

---

**Matt:** Inverted means applying healing causes damage.

I think Last Chance > Stendhal still counts Stendhal as the first "hit", as Last Chance is a skill but doesn't do any hits. Worth testing.

There's another first hit Lumina — First Offensive: First hit dealt and taken deals 50% more damage. Could add that in too.

LP costs is more than the 10LP you mention, as I want to add all the Last Stand Lumina too. However, I've found you can grind CoL in Renoir's Drafts at about 1LP per minute, which is a game changer. So the only barrier to adding all Lumina is my boredom threshold.

**Claude:** *[Turn 35. Last log: Turn 27.]*

Inverted noted — so healing applied to Maelle converts to damage while Inverted. In solo with no healer that's effectively neutral, but it would interact badly with anything like Healing Death from Monoco (which heals the whole Expedition on death). Worth checking whether Healing Death affects Maelle if she's Inverted — she might take damage from it rather than receiving the heal.

First Offensive is a nice addition — that's another ×1.5 on Stendhal for just 5LP, and the "first hit taken" risk is largely absorbed by the shield stack from Monoco's death suite before she acts.

With CoL grinding removing LP as a constraint, the build essentially becomes: stack every multiplicative damage Lumina that reliably fires on Stendhal's first hit, and trust the shields to cover the vulnerability window. The "boredom threshold" framing is honest — at 1LP/minute you could theoretically add 50LP worth of Lumina per hour, so it's just a question of how optimised you want to be before tackling the remaining superbosses.

One thing worth tracking: some of these multipliers may be additive with each other rather than multiplicative (the game isn't always consistent). If Glass Cannon, Immaculate, Solo Fighter, and Burn Affinity all add into a single damage bucket rather than multiplying separately, the maths looks quite different. Might be worth a quick empirical test on a dummy enemy once the build is assembled — hit without each one individually to see how much it changes the output.

---

**Matt:** I think they are multiplicative. I just went from 1.8m damage to 5.3m damage with a few Lumina changes. I'll keep tweaking the build and report back when it's finished.

!log

**Claude:** *[Turn 36. Last log: Turn 36.]*

*[Appended turns 28–36 to chat32.md]*

Logged. 1.8m to 5.3m is a nearly 3× jump — very much in line with the multipliers being multiplicative. Good luck with the tweaking — looking forward to hearing the final numbers.

---

<!-- SECTION -->
## Maelle Build Finalised — 21m Hit and Variant Logged

**Matt:** Ok, I got a hit of 21m!

**Claude:** *[Turn 37. Last log: Turn 36.]*

That's extraordinary. From 1.8m to 21m in one session — roughly 12× improvement. At that point you're not just killing superbosses, you're insulting them.

What's the current build that got you there? Worth logging the loadout while it's fresh.

---

**Matt:** So that same build only did 10m against Simon, partly due to higher Defence, but also because she got hit a lot before her first attack, so lost Immaculate and some others. I need to give her First Strike. On the other hand, my modified Verso build with Frenzy, Double Third and the At Death's Door set of low-health damage boosts did over 27m damage on Simon with Fortune's Fury on a Steeled Strike!

**Claude:** *[Turn 38. Last log: Turn 36.]*

27m from Verso is remarkable — especially since that's a multi-hit build working exactly as designed. Frenzy stacking across Steeled Strike's hits, Double Third firing on the third, and Fortune's Fury amplifying the whole chain at low health. That's a very different architecture to Maelle's single-hit build but clearly hitting the same stratosphere.

The Maelle situation makes sense — Simon has elevated Defense, and losing Immaculate plus Augmented First Strike to taking hits before she acts probably cost her 30% + 50% in multipliers. First Strike should fix that entirely. Is First Strike a Pictos that gives turn-priority, or a specific Lumina? I don't recall seeing it in the data queries — if it's something you haven't obtained yet it might be worth checking where it drops.

The interesting question now is which of the two builds you want to invest in for the remaining superbosses. Verso at 27m is already there; Maelle at 21m potential with the right setup is close. Running both as options depending on the fight seems sensible.

---

**Matt:** *[Screenshot 1 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-02.png]* *[Screenshot 2 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-09-53.png]* *[Screenshot 3 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-09-34.png]* *[Screenshot 4 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-09-38.png]*

Here is the Maelle solo build. You can see that she is levelled to 99 now — in fact, all characters are now level 99.

* Level 99
* Attributes V0 M99 A99 D0 L99
* Combat stats (modified) H8588 A11583 S2951 C41%

Please can you extract from these screenshots:

* Skills equipped
* Pictos equipped
* Lumina equipped (from AP Discount through to Warming Up)

Then can you write one or more actions to update the data file with her new level and attributes, and add this build as a variant.

**Claude:** *[Turn 39. Last log: Turn 36.]*

Reading all four screenshots carefully. Let me compile everything before writing the actions.

**Level & Attributes (Image 3):**
Level 99, Vitality 0 / Might 99 / Agility 99 / Defense 0 / Luck 99

**Modified Combat Stats (Images 3 & 4):**
Health 8,588 / Attack Power 11,583 / Speed 2,951 / Defense 182 / Critical Rate 41%

**Weapon (Image 3):** Lithum, Level 33

**Pictos (Images 3 & 4):**
Energising Turn (Level 31), Energy Master (Level 30), Cheater (Level 24)

**Skills (Image 3):**
Phantom Strike (7), Fleuret Fury (6), Stendhal (8), Burning Canvas (5), Last Chance (1), Pyrolyse (9)

**Active Lumina — AP Discount to Warming Up (Images 1 & 2):**
AP Discount (30), Accelerating Last Stand (3), At Death's Door (5), Augmented First Strike (5), Base Shield (20), Breaker (10), Breaking Burn (5), Breaking Counter (3), Breaking Death (5), Burn Affinity (10), Charging Critical (10), Cheater (40, Pictos), Confident Fighter (15), Critical Break (5), Dead Energy I (2), Dead Energy II (2), Dodger (1), Empowering Last Stand (3), Energising Shell (10), Energising Start I (5), Energising Turn (20, Pictos), Energy Master (40, Pictos), Exposing Break (5), First Offensive (5), First Strike (10), Glass Cannon (10), Gradient Fighter (5), Greater Defenceless (15), Greater Powerful (10), Greater Shell (10), Immaculate (10), Inverted Affinity (5), Last Stand Critical (3), Longer Powerful (10), Longer Shell (10), Painted Power (5), Powerful On Shell (10), Powerful Shield (5), Protecting Last Stand (3), Second Chance (40), Shortcut (5), Solo Fighter (1), Survivor (20), Warming Up (15)

LP check: 361 paid LP + 100 free from Pictos (Cheater 40 + Energising Turn 20 + Energy Master 40) = 361/361 total. ✓

**ACTION:** Update Maelle in data/characters.json — Level 99, attributes Vitality 0 / Might 99 / Agility 99 / Defense 0 / Luck 99, modified combat stats Health 8588 / Attack Power 11583 / Speed 2951 / Defense 182 / Critical Rate 41%.

**ACTION:** Update Maelle's active weapon, Pictos, and skills in data/characters.json — Weapon Lithum Level 33; Pictos: Energising Turn (L31), Energy Master (L30), Cheater (L24); Skills: Phantom Strike (7), Fleuret Fury (6), Stendhal (8), Burning Canvas (5), Last Chance (1), Pyrolyse (9).

**ACTION:** Add variant "Solo At Death's Door" for Maelle in data/characters.json — Pictos: Energising Turn, Energy Master, Cheater; LP 361/361; active Lumina: AP Discount (30), Accelerating Last Stand (3), At Death's Door (5), Augmented First Strike (5), Base Shield (20), Breaker (10), Breaking Burn (5), Breaking Counter (3), Breaking Death (5), Burn Affinity (10), Charging Critical (10), Cheater (40, Pictos), Confident Fighter (15), Critical Break (5), Dead Energy I (2), Dead Energy II (2), Dodger (1), Empowering Last Stand (3), Energising Shell (10), Energising Start I (5), Energising Turn (20, Pictos), Energy Master (40, Pictos), Exposing Break (5), First Offensive (5), First Strike (10), Glass Cannon (10), Gradient Fighter (5), Greater Defenceless (15), Greater Powerful (10), Greater Shell (10), Immaculate (10), Inverted Affinity (5), Last Stand Critical (3), Longer Powerful (10), Longer Shell (10), Painted Power (5), Powerful On Shell (10), Powerful Shield (5), Protecting Last Stand (3), Second Chance (40), Shortcut (5), Solo Fighter (1), Survivor (20), Warming Up (15).

One flag: I notice "Greater Defenceless" is in the active loadout — I'd assumed from our earlier discussion you'd removed it, but evidently it's useful for fights where you can inflict Defenceless on the enemy. Worth noting in the variant description if the schema supports notes.

---

**Matt:** !log

**Claude:** *[Turn 40. Last log: Turn 40.]*

*[Appended turns 37–40 to chat32.md]*

---

<!-- SECTION -->
## Monoco Death Bomb Build Logged

**Matt:** *[Screenshot 1 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-11-32.png]* *[Screenshot 2 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-11-24.png]* *[Screenshot 3 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-11-17.png]*

This is the Monoco Death Bomb build. Same process as for Maelle, please.

**Claude:** *[Turn 41. Last log: Turn 40.]*

Reading all three screenshots. Compiling before writing actions.

**Level & Attributes (Image 3):**
Level 99, Vitality 0 / Luck 99 / Might 0 / Defense 99 / Agility 99

**Combat Stats (Image 3):**
Health 5,177 / Attack Power 11,097 / Speed 1,553 / Defense 1,515 / Critical Rate 167%

**Weapon (Image 3):** Joyaro, Level 33

**Pictos (Images 2 & 3):**
Slot 1: Empty / Longer Break (L29) / The One (L31)

**Skills (Image 3):**
Orphelin Cheers (3), Stalact Punches (4), Potier Energy (4), Moissonneuse Vendange (5), Chapelier Slash (7), Sakapatate Fire (9)

**Active Lumina (Image 1):**
Auto Death (1), Breaking Death (5), Burning Death (5), Death Bomb (5), Energising Death (5), Greater Defenceless (15), Greater Powerful (10), Greater Powerless (15), Greater Rush (10), Greater Shell (10), Greater Slow (15), Healing Death (5), Longer Break (10, Pictos), Longer Burn (15), Longer Powerful (10), Longer Rush (10), Longer Shell (10), Painted Power (5), Protecting Death (5), Shielding Death (10), The One (1, Pictos)

LP check: 1+5+5+5+5+15+10+15+10+10+15+5+15+10+10+10+5+5+10 = 166 paid LP. Display shows 166/186 (20 available). ✓

**ACTION:** Update Monoco in data/characters.json — Level 99, attributes Vitality 0 / Luck 99 / Might 0 / Defense 99 / Agility 99, combat stats Health 5177 / Attack Power 11097 / Speed 1553 / Defense 1515 / Critical Rate 167%.

**ACTION:** Update Monoco's weapon, Pictos, and skills in data/characters.json — Weapon Joyaro Level 33; Pictos: empty slot / Longer Break (L29) / The One (L31); Skills: Orphelin Cheers (3), Stalact Punches (4), Potier Energy (4), Moissonneuse Vendange (5), Chapelier Slash (7), Sakapatate Fire (9).

**ACTION:** Add variant "Death Bomb" for Monoco in data/characters.json — Pictos: empty / Longer Break / The One; LP 166/186 (20 available); active Lumina: Auto Death (1), Breaking Death (5), Burning Death (5), Death Bomb (5), Energising Death (5), Greater Defenceless (15), Greater Powerful (10), Greater Powerless (15), Greater Rush (10), Greater Shell (10), Greater Slow (15), Healing Death (5), Longer Break (10, Pictos), Longer Burn (15), Longer Powerful (10), Longer Rush (10), Longer Shell (10), Painted Power (5), Protecting Death (5), Shielding Death (10), The One (1, Pictos).

Two notes: The One (Max Health reduced to 1) makes Monoco's death from Auto Death certain even before it fires, and ensures Healing Death heals allies from a depleted state. Painted Power on Monoco is interesting — implies Death Bomb can exceed the 9,999 cap on a crit. That 167% crit rate is doing real work.

---

**Matt:** !log

**Claude:** *[Turn 42. Last log: Turn 42.]*

*[Appended turns 41–42 to chat32.md]*

---

<!-- SECTION -->
## Verso Frenzy Build Logged

**Matt:** *[Screenshot 1 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-34.png]* *[Screenshot 2 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-25.png]* *[Screenshot 3 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-28.png]*

This is the Verso build that's doing so much damage. Could you log this as his main build please?

**Claude:** *[Turn 43. Last log: Turn 42.]*

Reading all three screenshots carefully.

**Level & Attributes (Images 2 & 3):**
Level 99, Vitality 99 / Luck 0 / Might 99 / Defense 0 / Agility 99

**Combat Stats:**
Health 7,790 / Attack Power 11,583 / Speed 2,100 / Defense 182 / Critical Rate 106%

**Weapon (Image 2):** Simoso, Level 33

**Pictos (Images 2 & 3):**
Second Chance (L31) / Sweet Kill (L31) / Alternating Critical (L29)

**Skills (Image 2):**
Overload (6), Perfect Break (7), Light Holder (4), End Bringer (9), Phantom Stars (9), Steeled Strike (9)

**Active Lumina (Image 1):**
AP Discount (30), Alternating Critical (10, Pictos), At Death's Door (5), Augmented First Strike (5), Auto Rush (10), Base Shield (20), Breaker (10), Breaking Burn (5), Breaking Death (5), Burn Affinity (10), Charging Critical (10), Cheater (40), Confident Fighter (15), Critical Break (5), Dead Energy I (2), Dead Energy II (2), Dodger (1), Double Third (10), Energising Break (3), Energising Turn (20), Energy Master (40), First Strike (10), Frenzy (20), Painted Power (5), Second Chance (40, Pictos), Shortcut (5), Sweet Kill (5, Pictos), Teamwork (5), Warming Up (15)

LP check: 308 paid LP (Alternating Critical 10 + Second Chance 40 + Sweet Kill 5 = 55 free from Pictos). Display 308/308. ✓

**ACTION:** Update Verso in data/characters.json — Level 99, attributes Vitality 99 / Might 99 / Agility 99 / Luck 0 / Defense 0, modified combat stats Health 7790 / Attack Power 11583 / Speed 2100 / Defense 182 / Critical Rate 106%.

**ACTION:** Update Verso's weapon, Pictos, and skills in data/characters.json — Weapon Simoso Level 33; Pictos: Second Chance (L31), Sweet Kill (L31), Alternating Critical (L29); Skills: Overload (6), Perfect Break (7), Light Holder (4), End Bringer (9), Phantom Stars (9), Steeled Strike (9).

**ACTION:** Add variant "Frenzy Multi-Hit At Death's Door" for Verso in data/characters.json — Pictos: Second Chance, Sweet Kill, Alternating Critical; LP 308/308; active Lumina: AP Discount (30), Alternating Critical (10, Pictos), At Death's Door (5), Augmented First Strike (5), Auto Rush (10), Base Shield (20), Breaker (10), Breaking Burn (5), Breaking Death (5), Burn Affinity (10), Charging Critical (10), Cheater (40), Confident Fighter (15), Critical Break (5), Dead Energy I (2), Dead Energy II (2), Dodger (1), Double Third (10), Energising Break (3), Energising Turn (20), Energy Master (40), First Strike (10), Frenzy (20), Painted Power (5), Second Chance (40, Pictos), Shortcut (5), Sweet Kill (5, Pictos), Teamwork (5), Warming Up (15); note: achieved 27m damage on Simon with Fortune's Fury on Steeled Strike.

---

**Matt:** !log

**Claude:** *[Turn 44. Last log: Turn 44.]*

*[Appended turns 43–44 to chat32.md]*

---

<!-- SECTION -->
## Lune and Sciel Main Builds Logged

**Matt:** *[Screenshot 1 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-11-13.png]* *[Screenshot 2 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-11-06.png]* *[Screenshot 3 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-11-09.png]* *[Screenshot 4 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-52.png]* *[Screenshot 5 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-59.png]* *[Screenshot 6 uploaded: Clair_Obscur__Expedition_33-2026_06_08-20-10-48.png]*

Oh, actually, I didn't want that as a variant.

**ACTION:** Adjust the last action: this is not a variant, but Verso's main build.

For completeness, here are Lune and Sciel. Please pull out the same details and log them as the main build.

**Claude:** *[Turn 45. Last log: Turn 44.]*

Noted on Verso — that ACTION correction is logged. Reading all six screenshots now.

---

**LUNE — Images 1–3**

Level 99, Vitality 99 / Luck 51 / Might 48 / Agility 99 / Defense 0
Health 3,809 / Attack Power 11,155 / Speed 2,691 / Defense 182 / Critical Rate 102%
Weapon: Kralim L33
Pictos: Critical Burn (L25) / Burn Affinity (L21) / Breaking Death (L29)
Skills: Terraquake (5), Healing Light (3), Hell (9), Thermal Transfer (2), Lightning Dance (7), Elemental Genesis (4)
Active Lumina: AP Discount (30), Accelerating Heal (5), Base Shield (20), Breaking Attack (10), Breaking Burn (5), Breaking Death (5, Pictos), Burn Affinity (10, Pictos), Cheater (40), Critical Burn (5, Pictos), Dead Energy I (2), Dead Energy II (2), Dodger (1), Energising Burn (10), Energising Start I (5), Energising Turn (20), Energy Master (40), First Strike (10), Painted Power (5), Protecting Heal (5), Second Chance (40), Shortcut (5), Teamwork (5)
LP check: 260 paid + 20 free from Pictos. Display 260/260. ✓

---

**SCIEL — Images 4–6**

Level 99, Vitality 0 / Luck 99 / Might 99 / Agility 99 / Defense 0
Health 7,396 / Attack Power 10,275 / Speed 2,572 / Defense 182 / Critical Rate 106%
Weapon: Litheson L33
Pictos: Augmented Counter I (L31) / Energising Shots (L28) / Painter (L28)
Skills: Fortune's Fury (5), Final Path (9), Intervention (5), Delaying Slash (5), All Set (6), Plentiful Harvest (4)
Active Lumina: AP Discount (30), Accelerating Heal (5), Augmented Counter I (3, Pictos), Base Shield (20), Breaker (10), Breaking Attack (10), Breaking Burn (5), Breaking Counter (3), Breaking Death (5), Charging Alteration (10), Cheater (40), Critical Break (5), Dead Energy I (2), Dodger (1), Energising Heal (10), Energising Shots (10, Pictos), Energising Start I (5), Energising Turn (20), First Strike (10), Gradient Break (5), Healing Tint Energy (1), Painted Power (5), Painter (10, Pictos), Protecting Heal (5), Recovery (10), Second Chance (40), Shortcut (5), Survivor (20), Teamwork (5), Accelerating Last Stand (3)
LP check: paid LP sums to 290, but display shows 287/287 — 3LP discrepancy, likely one 3LP Lumina misread as active. Flag for wrap.

---

**ACTION:** Update Lune in data/characters.json — Level 99, attributes Vitality 99 / Luck 51 / Might 48 / Agility 99 / Defense 0, combat stats Health 3809 / Attack Power 11155 / Speed 2691 / Defense 182 / Critical Rate 102%, weapon Kralim Level 33, Pictos: Critical Burn (L25) / Burn Affinity (L21) / Breaking Death (L29), Skills: Terraquake (5), Healing Light (3), Hell (9), Thermal Transfer (2), Lightning Dance (7), Elemental Genesis (4), Luminas 260/260, active Lumina: AP Discount (30), Accelerating Heal (5), Base Shield (20), Breaking Attack (10), Breaking Burn (5), Breaking Death (5, Pictos), Burn Affinity (10, Pictos), Cheater (40), Critical Burn (5, Pictos), Dead Energy I (2), Dead Energy II (2), Dodger (1), Energising Burn (10), Energising Start I (5), Energising Turn (20), Energy Master (40), First Strike (10), Painted Power (5), Protecting Heal (5), Second Chance (40), Shortcut (5), Teamwork (5).

**ACTION:** Update Sciel in data/characters.json — Level 99, attributes Vitality 0 / Luck 99 / Might 99 / Agility 99 / Defense 0, combat stats Health 7396 / Attack Power 10275 / Speed 2572 / Defense 182 / Critical Rate 106%, weapon Litheson Level 33, Pictos: Augmented Counter I (L31) / Energising Shots (L28) / Painter (L28), Skills: Fortune's Fury (5), Final Path (9), Intervention (5), Delaying Slash (5), All Set (6), Plentiful Harvest (4), Luminas 287/287 (verify — 3LP discrepancy flagged), active Lumina: AP Discount (30), Accelerating Heal (5), Augmented Counter I (3, Pictos), Base Shield (20), Breaker (10), Breaking Attack (10), Breaking Burn (5), Breaking Counter (3), Breaking Death (5), Charging Alteration (10), Cheater (40), Critical Break (5), Dead Energy I (2), Dodger (1), Energising Heal (10), Energising Shots (10, Pictos), Energising Start I (5), Energising Turn (20), First Strike (10), Gradient Break (5), Healing Tint Energy (1), Painted Power (5), Painter (10, Pictos), Protecting Heal (5), Recovery (10), Second Chance (40), Shortcut (5), Survivor (20), Teamwork (5), Accelerating Last Stand (3).

---

**Matt:**

**ACTION:** The discrepancy in the last action is because Accelerating Last Stand shouldn't be included.

!log

**Claude:** *[Turn 46. Last log: Turn 46.]*

*[Appended turns 45–46 to chat32.md]*

---

