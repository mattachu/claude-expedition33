FILE: overview/claude-expedition33.md
SECTION: ## Section 5: Party > ### Core Lumina Suite
CONTENT:
### Core Lumina Suite

**Main team core:**
<!-- GENERATED:START pictos:core:main -->
**234LP** Painted Power, Teamwork, Base Shield, Energising Turn, Energising Parry, Energising Start I, Dodger, Breaker, Marking Shots, Dead Energy I, Dead Energy II, Critical Break, Rewarding Mark, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death, Cheater, Energy Master, Second Chance. Note: Painted Power (Essential for all characters from Act 3 onwards); Base Shield (Verso: non-functional with Chevalam as L4 effect prevents shields); Energising Turn (Main AP flow generator; boosted by Energy Master); Second Chance (Revive with 100% HP once per battle — universally recommended for endgame).
<!-- GENERATED:END -->

**Reserve team core:**
<!-- GENERATED:START pictos:core:reserve -->
**120LP** Painted Power, Teamwork, Base Shield, Energising Turn, Energising Parry, Energising Start I, Dodger, Breaker, Marking Shots, Critical Break, Rewarding Mark, Burning Shots, Breaking Burn, Breaking Counter, Breaking Death, Recovery. Note: Recovery (10% HP regen per turn — passive sustain for reserve characters entering under pressure).
<!-- GENERATED:END -->

Full breakdown with effects in [pictos-lumina-summary.md](pictos-lumina-summary.md) §3–4. Character-specific additions on top of core sets in §5.

FILE: overview/claude-expedition33.md
SECTION: ## Section 9: Open Questions
CONTENT:
## Section 9: Open Questions

- **Verso survivability without Survivor:** Survivor (20LP) dropped to test whether Second Chance alone is sufficient. If Verso dies frequently with only Second Chance, add Survivor back (20 CoL to expand pool). Monitor during Renoir and early postgame.
- **Clea's Life + Shield interaction: ✅ CONFIRMED.** Clea's Life triggers even after Shield absorbs a hit. Reliable full-heal engine on Maelle with Lithum's Shield generation. Recovery not needed on Maelle.
- **Recovery on Sciel:** Dropped for now to save LP. Revisit if Sciel takes more damage than expected in postgame. 10LP, would need CoL expansion.
- **Powerful On Shell as Lumina:** Consider for Maelle (synergy with Lithum L20 Shell generation). LP cost 10. Add when levels create headroom.
- **Energising Shell (10LP):** Alternative to Powerful On Shell for Maelle — +2 AP on Shell application. Evaluate alongside Powerful On Shell.
- **Anti-Blight (10LP):** Near-requisite for postgame content. Add to all main team characters when levels create LP headroom. 67 CoL remaining.
- **Second Chance upgrade:** Available at L31 from defeating Création near Grour in Renoir's Drafts. Substantially better stats than current L16.
- **Pictos data rationalisation:** Remove character `pictos` arrays from JSON; derive from `equipped_by` field. Update `generate_pictos_lumina.py`. See framework document Section 11 for full spec.
- **Healing Boon trigger mechanic:** "Heal 15% HP on applying a buff" — may fire on the buff *recipient* rather than the caster. Needs in-game confirmation before building around it.
- **Crit cap:** Believed to be 100%, not 99%. Verify in-game.
- **Empowering Dodge (5LP):** Reset behaviour on parry unconfirmed — test empirically before committing LP.
- **Session architecture:** Switched to 1 section per part from Chat 10 onwards. Splitter command: `python3 scripts/split_transcript.py --sections-per-part 1 chatN.md`. Update pipeline.md to reflect this default.

FILE: overview/claude-expedition33.md
SECTION: ## Section 10: Chat Logs
CONTENT:
## Section 10: Chat Logs

*For reference only — do not fetch unless specifically asked. These are large files.*

| Chat   | Index                                                                                                                                          | Full Transcript                       | Summary                                                                                                                                                                                                                                  |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Chat 0 | [Formatted](../chats/chat0/chat0-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat0/chat0-index.md)   | [chat0.md](../chats/chat0/chat0.md)   | Prior (abandoned) conversation with ChatGPT                                                                                                                                                                                              |
| Chat 1 | [Formatted](../chats/chat1/chat1-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat1/chat1-index.md)   | [chat1.md](../chats/chat1/chat1.md)   | Initial build analysis across all five characters; Monoco stat respec; Lune weapon comparison; Sciel and Verso builds; full progression plan                                                                                             |
| Chat 2 | [Formatted](../chats/chat2/chat2-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat2/chat2-index.md)   | [chat2.md](../chats/chat2/chat2.md)   | Endgame skill research; character stat update via voice; chromatic progress; compaction mechanics; session procedure design                                                                                                              |
| Chat 3 | [Formatted](../chats/chat3/chat3-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat3/chat3-index.md)   | [chat3.md](../chats/chat3/chat3.md)   | Endgame team transition (Cheater Pictos acquired); team role framing; burn-stacking vs stance cycling paths; Chevalam mechanics; Maelle LP planning; transcript logging problems                                                         |
| Chat 4 | [Formatted](../chats/chat4/chat4-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat4/chat4-index.md)   | [chat4.md](../chats/chat4/chat4.md)   | Progress update; story ordering research; Verso weapon selection; Steeled Strike burst sequence analysis; Maelle Reacher preparation; session logging procedure improvements                                                             |
| Chat 5 | [Formatted](../chats/chat5/chat5-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat5/chat5-index.md)   | [chat5.md](../chats/chat5/chat5.md)   | Maelle respec for Lithum; Gommage unlocked; full Pictos/Lumina review all five characters; core Lumina sets defined; Energy Master obtained; Pictos/Lumina reference created                                                             |
| Chat 6 | [Formatted](../chats/chat6/chat6-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat6/chat6-index.md)   | [chat6.md](../chats/chat6/chat6.md)   | Flying Manor ordering decided; Renoir self-nerf strategy; progression plan restructured; all character stats updated; Pictos optimisation deferred to Opus session                                                                       |
| Chat 7 | [Formatted](../chats/chat7/chat7-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat7/chat7-index.md)   | [chat7.md](../chats/chat7/chat7.md)   | Pictos optimisation framework designed and prepared for Sonnet handoff; actual optimisation and assignment deferred until after Flying Manor; Colour of Lumina pool expansion mechanism documented; Pictos data rationalisation designed |
| Chat 8 | [Formatted](../chats/chat8/chat8-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat8/chat8-index.md)   | [chat8.md](../chats/chat8/chat8.md)   | Monoco full skill audit; Repo restructure design: new folder structure, JSON reference files, GitHub Actions workflow; All five data files built; Session procedure updated; hand-off for script design                                  |
| Chat 9 | [Formatted](../chats/chat9/chat9-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat9/chat9-index.md)   | [chat9.md](../chats/chat9/chat9.md)   | Repo restructure completed: generate_scripts_md.py built; generate.py written (unified generator for all GENERATED blocks, party-summary, Pictos catalogue); apply_changelist.py updated with GENERATED marker detection; session procedure and pipeline.md updated |
| Chat 10 | [Formatted](../chats/chat10/chat10-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat10/chat10-index.md) | [chat10.md](../chats/chat10/chat10.md) | Comprehensive data update post-Flying Manor. All five characters updated via screenshot: levels, attributes, stats, Pictos, weapons, Lumina loadouts, and inventory. Extensive weapons corrections and additions. Pictos: 8 new obtains including Clea's Life; 7 level+stats updates; 4 missing stats filled.|
| Chat 11 | [Formatted](../chats/chat11/chat11-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat11/chat11-index.md) | [chat11.md](../chats/chat11/chat11.md) | Partial Pictos optimisation session. Turn order confirmed resolved (Sciel 2466 >> Maelle 2049 via Chat 10 Pictos). Sciel crit at cap. Speed spread identified as new constraint (~200 target; current spread 417). Clea's Life stats confirmed (Health +5591 only). Session handed off to Opus for full multi-character constraint optimisation. |
| Chat 12 | [Formatted](../chats/chat12/chat12-index.md) / [Raw](https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@main/chats/chat12/chat12-index.md) | [chat12.md](../chats/chat12/chat12.md) | Full Pictos optimisation (Opus). All five characters reviewed bottom-up from stat data. Main team: Maelle gets Clea's Life + Empowering Break (HP doubled to 7610); Verso gets Aug Counter I + Confident (HP +40%, crit fixed, speed +157); Sciel unchanged. Reserve: Monoco gets Powerful Revive (+32% crit). Lumina: Second Chance added to main core (234LP); Recovery added to reserve core (120LP); filler dropped. Clea's Life Shield interaction confirmed in-game. CoL spend: 100 of 167. |

FILE: data/pictos-lumina.json
NOTES: Apply these equipped_by changes:
- Burning Break: equipped_by "Maelle" → null
- Survivor: equipped_by "Maelle" → null
- Clea's Life: equipped_by null → "Maelle"
- Empowering Break: equipped_by null → "Maelle"
- Gradient Break: unchanged (stays "Maelle")
- Cheater: equipped_by "Verso" → null
- Second Chance: equipped_by "Verso" → null
- Augmented Counter I: equipped_by null → "Verso"
- Confident: equipped_by null → "Verso"
- Breaking Death: unchanged (stays "Verso")
- Energising Turn: equipped_by "Monoco" → null
- Powerful Revive: equipped_by null → "Monoco"
- Longer Shell: unchanged (stays "Monoco")
- Powerful Mark: unchanged (stays "Monoco")

Update core_lumina_suite.main_team:
- Add entry: {"name": "Second Chance", "lp": 40}
- Update total_lp: 194 → 234

Update core_lumina_suite.reserve_team:
- Add entry: {"name": "Recovery", "lp": 10}
- Update total_lp: 110 → 120
- Update notes: "Main team core minus Cheater, Energy Master, Dead Energy I, Dead Energy II, Second Chance. Plus Recovery."

FILE: data/characters.json
NOTES: Update pictos_equipped arrays:
- Maelle: ["Clea's Life", "Empowering Break", "Gradient Break"]
- Verso: ["Augmented Counter I", "Breaking Death", "Confident"]
- Monoco: ["Longer Shell", "Powerful Mark", "Powerful Revive"]
Update lp_total for each character after CoL expansion:
- Verso: 224
- Maelle: 234
- Sciel: 215
- Lune: 130
Update lumina_core_exclusions for Verso:
- Remove: Second Chance (no longer Pictos)
- Remove: Cheater (no longer Pictos)
- Add: Confident (now free from Pictos)
- Add: Augmented Counter I (now free from Pictos)
- Keep: Base Shield (still excluded)
- Keep: Breaking Death (still free from Pictos)
Update lumina_extras for Verso:
- Remove: Confident (now Pictos, listed in core_exclusions)
- Remove: Enfeebling Mark (dropped)
- Remove: Survivor (dropped, testing without)
- Keep: Confident Fighter
Update lumina_extras for Maelle:
- Remove all (no character extras beyond core)
- Note: Clea's Life, Empowering Break, Gradient Break all free from Pictos
Update lumina_extras for Monoco:
- Remove: Cheater (dropped)
- Add: Energising Break (3LP)
- Add: Recovery (10LP) — actually now in reserve core, so not an extra
- Keep: Break Specialist, Staggering Attack
- Add to core_exclusions: Energising Turn (no longer free from Pictos)

FILE: reference/historical-errors.md
NOTES: Add these errors from Chat 12:
- **Speed arithmetic error:** Wrote Verso Option Z speed as 3319 instead of 2319. The 3319 figure was from an earlier calculation (Cheater+BD+Confident = 2719) that was then incorrectly carried forward. Matt caught it.
- **Monoco HP error:** Claimed Monoco's HP would drop to 1930 when swapping Energising Turn for a new Pictos. Energising Turn contributes zero HP — HP stays at 4687 regardless. Matt caught it.
- **Sciel Resurrect claim:** Said Sciel has a Resurrect skill. She does not. Also said "she" when Sciel is the character being discussed but the correction is about the skill, not the pronoun.
- **Framework bias / not doing bottom-up analysis:** Initially worked from the Chat 7 framework's shortlist of candidate Pictos rather than querying the full JSON for highest stat boosts. Missed Augmented Counter I (the single highest HP+Crit Pictos in the pool) entirely. Matt caught this and pushed back: "it's suspicious that the Pictos I currently have selected just happen to be the best ones."
- **Turn counter lost:** Displayed "Turn 6" when the actual turn count was much higher. Turn counter became unreliable partway through the session.
