**HANDOFF: Pictos/Lumina Optimisation — Opus session**

**Fetch and read startup file first**
- Startup file: `https://cdn.jsdelivr.net/gh/mattachu/claude-tools@67415612/startup.md`

**Task for this session**

Matt has recently acquired the Energy Master Pictos and completed the Reacher, and is about to go into the Flying Manor. This is a good point to re-optimise Pictos and Lumina. The task is to select the best three Pictos and the best set of Lumina for each character, to equip them for Flying Manor and final boss in Lumiere, and then into post-game content.

**Fetch and read these files before starting optimisation** (commit hash `d5d4d353`):
- Overview: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/claude-expedition33.md`
- Pictos/Lumina summary: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/pictos-lumina-summary.md`
- Maelle: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/maelle.md`
- Verso: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/verso.md`
- Sciel: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/sciel.md`
- Lune: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/lune.md`
- Monoco: `https://cdn.jsdelivr.net/gh/mattachu/claude-expedition33@d5d4d353/overview/monoco.md`

Also note uploaded `pictos-lumina.json` — this has been updated this session and is the authoritative data source for all Pictos stats and assignments. It can be queried programmatically (e.g. "top 10 by speed") rather than read in full.

**Current character stats (post Chat 6 updates):**

| Char | Level | HP (base+Pictos) | Speed (base+Pictos) | Crit (base+Pictos) | LP used/cap |
|------|-------|-----------------|--------------------|--------------------|-------------|
| Maelle | 83 | 1930+1541=3471 | 1154+873=2027 | 41+64=105% | 194/196 |
| Verso | 82 | 1900+2305=4205 | 1146+986=2132 | 41+41=82% | 194/194 |
| Sciel | 82 | 1900+4979=6879 | 1146+868=2014 | 52+56=108% | 175/176 |
| Lune | 78 | 3173+874=4047 | 1050+747=1797 | 23+61=84% | 120/123 |
| Monoco | 78 | 1784+2757=4541 | 1050+795=1845 | 41+13=54% | 91/128 |

**Current Pictos per character:**
- Maelle: Burning Break (HP+1541, Crit+24%), Gradient Break (Spd+434, Crit+28%), Survivor (Spd+439, Crit+12%)
- Verso: Breaking Death (Spd+586, Crit+33%), Cheater (HP+1198, Spd+400), Second Chance (HP+1106, Crit+8%)
- Sciel: Critical Burn (Spd+434, Crit+28%), Energy Master (HP+4979), Quick Break (Spd+434, Crit+28%)
- Lune: Powerful On Shell (Def+874, Crit+25%), Burn Affinity (Spd+439, Crit+12%), Burning Death (Spd+308, Crit+24%)
- Monoco: Longer Shell (HP+2757, Def+1572), Sniper (Spd+525, Crit+13%), Energising Turn (Spd+270)

**Key constraints:**
- Verso: Chevalam L4 blocks ALL healing and shields — Recovery, Base Shield, and healing Lumina effects are all non-functional. Confirmed in-game.
- Cheater turns fire immediately after the character's own turn. Turn order: Verso→Verso(C)→Sciel→Sciel(C)→Verso(Intervention). Sciel does not need to go before Verso — only before his Intervention turn.
- Crit cap believed to be 100% — unverified, confirm before optimising.
- Quick Break effect never fires with Cheater — pure stat stick on Sciel.
- Base speed scales with level independently of Agility. Maelle (L83) is 13 points faster than Sciel (L82) due to level divergence. Levels should be kept close when speeds are close and turn order matters.
- Energy Master (40LP) is now in the main team core Lumina set (194LP total). All three main team members already have EM. Sciel holds the Pictos (saves 40LP, provides HP+4979). The Pictos holder question is purely about who gets the health stat.

**Unverified mechanic — important:**
- Healing Boon (Pictos/Lumina): "Heal 15% HP on applying a buff." Sciel's file documents a mechanism where Dark Cleansing (applies buffs to allies) triggers Healing Boon for each ally buffed. This suggests the trigger may fire on the *recipient* of the buff rather than only on the caster — meaning Healing Boon on Maelle would trigger whenever Sciel uses Fortune's Fury or Intervention on her. Needs confirmation before building around it.

**Recommended approach for the optimisation:**
Start from raw base stats (no Pictos) per character, establish what each character needs from Pictos (speed targets, health floor, crit to cap, any specific effects), then work out which Pictos best meet those needs, then reconcile against LP cost of replacing Pictos effects with Lumina where a Pictos effect is not needed as a Pictos.

**Key open questions:**
1. Energy Master Pictos holder: currently Sciel (HP+4979, saves 40LP). Is she the best holder, or does another character benefit more from the health boost?
2. Maelle slot 3 (Survivor): Spd+439, Crit+12%, survive one fatal hit. Crit is partially overcapped. Alternatives: Recovery (HP+2000, Def+324, 10% regen — good health/survivability) or others. Survivor as Lumina costs 20LP.
3. Sciel slot 3 (Quick Break): pure stat stick. Best replacement given her needs?
4. Verso: Confident is currently a 20LP Lumina. If equipped as Pictos it saves 20LP and frees a Lumina slot — but displaces one of his current three. Worth it?
5. Healing Boon (unequipped, Spd+266, Def+647, 10LP Lumina): strong candidate for Sciel if it fires on buff application to allies. Also potentially for Maelle if the recipient-trigger mechanic is confirmed.
6. Reserve team (Lune, Monoco) Pictos not reviewed this session.