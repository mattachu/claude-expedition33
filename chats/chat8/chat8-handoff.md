## Chat 9 Handoff

### Status
Chat 8 complete. Flying Manor in progress — Clea next. Main party Verso/Maelle/Sciel, reserve Lune/Monoco.

### What was done in Chat 8
1. Monoco full skill audit — 46-skill table built; two missing (Creation Void from The Creation in Lumière; Sakapatate Fire from Ultimate Sakapatate — available in Endless Tower). Moissonneuse Vendange corrected (AP 3→5, wheel +3→+2). Equipped skills updated; full skill catalogue in `data/skills.json`.
2. Repo restructure design — new folder structure agreed: `overview/`, `data/`, `characters/`, `reference/`. JSON-as-source-of-truth extended across repo.
3. GitHub Actions workflow — auto-generates `LINKS.md` with pinned jsDelivr URLs on every push. Matt pastes link to latest `LINKS.md` at session start; Claude fetches it to get all file URLs, then fetches files on demand.
4. Schema design — finalised for `data/characters.json`, `data/weapons.json`, `data/skills.json`, `data/playthrough.json`. Key decisions: `lumina_core_exclusions` + `lumina_extras` (name+note only); `equipped_by` retained in `pictos-lumina.json` for uniqueness enforcement with cross-validation in `generate.py`; `obtained` explicit boolean on all weapon entries.
5. All five data files built — `playthrough.json`, `characters.json` (all five merged), `skills.json`, `weapons.json`. Stats partially stale — full update deferred to post-Flying Manor.

### Immediately pending (before or at start of Chat 9)
- Matt to finish Flying Manor and defeat Clea
- Matt to run end-of-session changelist from Chat 8
- Post-Flying Manor: record base stats and modified stats for all characters in `data/characters.json`
- Post-Flying Manor: update inventory counts in `data/playthrough.json`
- Post-Flying Manor: update list of strongest Pictos obtained ready for party optimisation

### Pictos optimisation
Reminder: when Flying Manor is complete, read the uploaded `pictos-optimisation-framework.md` before starting the Pictos session.

### Key file locations (fetch via LINKS.md)
- `overview/claude-expedition33.md` — main overview
- `data/playthrough.json`, `data/characters.json`, `data/skills.json`, `data/weapons.json` — new data files
- `characters/maelle.md` etc. — narrative character files (note: repo restructure not yet applied — files still at `overview/maelle.md` until changelist is run)

### Open questions carried forward
All items from Section 9 of the overview remain open. Additionally:
- Sciel Litheson level — confirm 32 or 33 in game
- Choralim (Lune) — future weapon or just obtained/uncertain?
- Verso gradient skills — Matt to verify in game
