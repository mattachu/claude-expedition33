<!-- SECTION: Endgame Team Transition -->
## Endgame Team Transition

**Matt:** I've completed the Sacred River mission to complete Monoco's relationship journey, and defeated Sprong to get the Cheater Pictos. I think I'm ready to switch to the endgame team and get used to playing with them. How should I set them up? Note, Cheater Lumina costs 40LP, unless someone has the Pictos equipped. But it might be worth paying the cost for at least one extra character.

**Claude:** Flagged two things before advising: (1) need to verify Steeled Strike + Cheater mechanics; (2) Second Chance conflict between Maelle and Verso needs resolving. Searched and confirmed: Steeled Strike charges T1, executes T2; Cheater gives a consecutive second turn so charge and execute happen back-to-back before any enemy action. Sciel's Intervention also enables safe Steeled Strike use. Verso: swap Second Chance → Cheater Pictos; add Steeled Strike, drop Phantom Stars. Second Chance goes cleanly to Maelle. Cheater Lumina for Maelle flagged as dependent on Energising Turn triggering on the Cheater turn — needs in-game testing before committing.

**Matt:** I think the +3AP for Litheson is only for Sciel, not the whole party. Could you check?

**Claude:** Confirmed: +3 AP at level 20 is Sciel's own AP gain only, not party-wide. Overview Section 7 wording ("replaces Potier Energy") is directionally right but misleading — Sciel stays AP-positive herself and generates turns/AP for allies via Intervention, rather than directly filling party AP bars. Flagged for correction in changelist.

**Matt:** Yes, that matches. With the Lumina set we currently have plus Intervention, it is generally possible to keep AP high for all three, but not as straightforward or as quick to refill as with Potier Energy.

**Claude:** Noted as a practical distinction: endgame team AP flow is sustainable but requires active management. Flagged for Section 3 (Playstyle Notes) in changelist.

**Matt:** One more thing before that: Cheater is less useful for Maelle than it could be, because Gustave's Homage costs 8AP and Sword Ballet costs 9AP, and characters can't have more than 9AP. [Detailed analysis of Gustave's Homage → Cheater → Percée vs Gustave's Homage → Intervention → Fencer's Flurry paths. Asked whether Gustave's Homage can apply Mark.]

**Claude:** Searched and confirmed: Gustave's Homage benefits from Mark (×2.25 damage on Marked target) but does not apply it, and does not remove it. Percée costs 2 AP in Virtuose and also benefits from Mark. Full Cheater sequence on pre-Marked target: Gustave's Homage (2.25× damage, enters Virtuose, 1 AP left) → Cheater turn → Energising Turn gives +1 AP = 2 AP → Percée (boosted by Mark, exits Virtuose). Caveat: uncertain whether Energising Turn triggers on a Cheater-granted extra turn — flagged for in-game testing. Verso's Marking Shot (100% Mark) enables pre-Marking before Maelle's turn given likely turn order. Two paths summarised: Cheater path = burst, exits Virtuose; Intervention path = sustained Virtuose, slower payoff. Both stronger with pre-applied Mark.

**Matt:** Are you sure that Steeled Strike's damage count is calculated on the second turn, not the windup turn?

**Claude:** Acknowledged uncertainty — had stated this confidently without verifying. Searched but no source directly confirms calculation timing. Wiki comment suggests Fortune's Fury applied on windup turn is wasted in the Cheater scenario, but doesn't address the general case. Retracted confident statement; recommended in-game testing.

**Matt:** Ok, I'll do some testing.

<!-- SECTION: Team Roles and Build Paths -->
## Team Roles and Build Paths

**Matt:** Before getting into the specifics, can we talk a bit about roles in the team? Maelle is Primary DPS and Sciel is Support. There are ways to push Sciel more towards healing than I currently have, but I think in endgame teams, a lot of people rely on passive healing strats instead. Verso is often described more like a support character, applying Marks, buffs and debuffs. But I've been using him much more as a DPS. I'd like to understand a bit better how the three characters work together.

**Claude:** Searched before advising. Community framing: Verso applies Mark and stacks Burn as setup unit; Maelle delivers damage payload; Sciel accelerates turns and amplifies Maelle. Dominant rotation: Verso → Sciel → Maelle. Alternative path: Verso as Steeled Strike DPS with Sciel amplifying him instead. Framed flexibility: Sciel's Fortune's Fury and Intervention can flex between amplifying Verso or Maelle depending on fight. Caveat: this flexibility framing is Claude's own synthesis, not validated community wisdom.

**Matt:** I like that flexibility framing, thanks. Was that your idea or is it coming from the community?

**Claude:** Confirmed: own synthesis. Community describes the two paths separately; the framing of Sciel's amplification as flexibly targeting either character is an inference, not documented community wisdom. Flagged that there may be practical reasons the community doesn't mix modes.

**Matt:** I'm not sure how Fortune's Fury works with Cheater. It says it amplifies the character's "next turn", so that might be the Steeled Strike setup turn rather than payoff turn, in which case it is wasted. Can you check?

**Claude:** Searched and confirmed: Fortune's Fury buffs the target's next turn for double damage. Wiki comment explicit: "if running Cheater, you will lose this buff if used on turn 1." Fortune's Fury + Cheater + Steeled Strike don't work together — buff is consumed on the windup turn. Practical implication: when Verso uses Steeled Strike, Sciel should use Intervention (guarantees execution turn) rather than Fortune's Fury. Fortune's Fury better reserved for Maelle, or for turns when Verso uses immediate-damage skills.

**Matt:** Can you explain more about the burn-stacking?

**Claude:** Searched. Key findings: Medalum Level 10 doubles Burn applied in Virtuose; Level 20 doubles Burn damage in Virtuose. Pyrolyse applies up to 60 Burn stacks from Virtuose in one action. Burning Canvas consumes all Burn stacks with no limit — the nuke skill. With Cheater: Pyrolyse T1, Swift Stride to re-enter Virtuose, Burning Canvas T2. Verso's burn-stacking role uses Corpeso (2 Burn stacks per hit per rank, up to 80 stacks per turn with Double Burn Lumina) — a completely different weapon to Chevalam. Flagged clearly: burn-stack team and current Verso Perfection DPS build are two separate paths. Chevalam recommended level discrepancy noted: Verso file says 65–70+, overview says 70–75+ — flagged for changelist. Simoso noted as a third Verso weapon (post-game only).

**Matt:** I can't get Simoso until well into post-game.

**Claude:** Noted — Simoso doesn't affect current planning. Will mention in changelist as post-game option only.

**Matt:** Why was Chevalam recommended? What Verso build is that for? What teams suit that particular build?

**Claude:** Searched and confirmed Chevalam's actual effects: starts every fight at Rank S (200% damage boost); up to additional 100% if Verso avoids all damage; grants Rush at battle start. Tradeoff: disables healing and shields. Designed for Perfection Rank DPS Verso — no need to spend turns building rank, can fire Steeled Strike immediately at S Rank. Same Agility + Luck scaling as Gaulteram = no respec needed. Chevalam Verso appears alongside Maelle in community compositions, not instead of her. Timing caveat: Chevalam disables healing and shields — higher risk at ~20% parry rate; Gaulteram's forgiveness mechanic is still the safer choice while parry skills develop.

**Matt:** That framing helps, thanks. Do people using Chevalam also have Maelle in the party, or does this Perfection DPS replace Maelle?

**Claude:** Searched. Chevalam doesn't feature prominently in team composition guides specifically. Maelle and Verso consistently appear together across top endgame compositions — Verso as setup/Mark unit, Maelle as primary DPS. Chevalam Verso still in a team with Maelle, not replacing her. Also flagged Simoso as a middle path (Gaulteram → Chevalam → Simoso post-game).

**Matt:** I'm a little concerned that you haven't asked to read the Maelle or Verso character files yet. Do you think you need to do so?

**Claude:** Agreed — should have fetched them earlier. Fetched both. Key findings: (1) Maelle LP cap is 112, fully used, zero spare; (2) Verso has only 4 LP spare; (3) Medalum Level 4 starts Maelle in Virtuose — relevant to opening turns; (4) Phantom Stars flagged as suboptimal in 1v1 in Verso file; (5) Chevalam recommended level discrepancy confirmed (65–70+ in Verso file vs 70–75+ in overview).

**Matt:** I don't agree that Phantom Stars is "useless" in boss fights — it still does decent damage, I think. Just optimised for AoE.

**Claude:** Fair correction accepted. "Useless" is too strong — Phantom Stars still hits the boss, just without AoE benefit. Suboptimal in 1v1, not worthless. Flagged for changelist.

**Matt:** In terms of LP, I think Monoco currently has the Energising Turn Pictos. If we give that to Maelle, it would free up 20LP (I think) for her.

**Claude:** Confirmed mechanic (Pictos and Lumina are the same — equipping Pictos grants the Lumina free). Evaluated three swap options. Best option: replace Dead Energy I Pictos with Energising Turn Pictos. Net: ~+98 Speed, −17% Crit, +18 LP freed within current cap. To add Cheater Lumina (40 LP): needs 18 LP freed + 22 LP capacity expansion = 22 Colour of Lumina. Achievable given resources. Flagged Crit reduction (~65% → ~48%) as meaningful but not critical given Virtuose multipliers. Still contingent on Energising Turn triggering on Cheater turn.

**Matt:** Don't forget I can up her capacity with Colour of Lumina.

**Claude:** Corrected LP arithmetic: 18 LP freed by swap + 22 Colour of Lumina expansion = 40 LP for Cheater Lumina. Total cost: 22 Colour of Lumina.

**Matt:** Yes, I can test that too.
