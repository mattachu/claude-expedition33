DATA: data/characters.json
PATH: Maelle.level
OP: SET
VALUE: 91

DATA: data/characters.json
PATH: Maelle.attributes
OP: SET
VALUE: {"vitality": 0, "might": 75, "agility": 99, "defence": 0, "luck": 99}

DATA: data/characters.json
PATH: Maelle.stats_base
OP: SET
VALUE: {"health": 2171, "attack": 1322, "speed": 1213, "defence": 182, "crit": "41%"}

DATA: data/characters.json
PATH: Maelle.stats_modified
OP: SET
VALUE: {"health": 7762, "attack": 11013, "speed": 2193, "defence": 182, "crit": "101%", "_note": "Clea's Life + Empowering Break + Gradient Break; Lithum L33"}

DATA: data/characters.json
PATH: Maelle.skills_equipped
OP: SET
VALUE: ["Phantom Strike", "Fleuret Fury", "Last Chance", "Mezzo Forte", "Gustave's Homage", "Stendhal"]

DATA: data/characters.json
PATH: Verso.level
OP: SET
VALUE: 91

DATA: data/characters.json
PATH: Verso.attributes
OP: SET
VALUE: {"vitality": 0, "might": 75, "agility": 99, "defence": 0, "luck": 99}

DATA: data/characters.json
PATH: Verso.stats_base
OP: SET
VALUE: {"health": 2171, "attack": 1322, "speed": 1213, "defence": 182, "crit": "41%"}

DATA: data/characters.json
PATH: Verso.stats_modified
OP: SET
VALUE: {"health": 6229, "attack": 10529, "speed": 2356, "defence": 182, "crit": "122%", "_note": "Augmented Counter I + Breaking Death + Confident; Chevalam L33"}

DATA: data/characters.json
PATH: Sciel.level
OP: SET
VALUE: 90

DATA: data/characters.json
PATH: Sciel.attributes
OP: SET
VALUE: {"vitality": 0, "might": 9, "agility": 99, "defence": 63, "luck": 99}

DATA: data/characters.json
PATH: Sciel.stats_base
OP: SET
VALUE: {"health": 2140, "attack": 1182, "speed": 1206, "defence": 481, "crit": "55%"}

DATA: data/characters.json
PATH: Sciel.stats_modified
OP: SET
VALUE: {"health": 7110, "attack": 8685, "speed": 2504, "defence": 481, "crit": "102%", "_note": "Painter + Energy Master + Energising Shots; Litheson L33"}

DATA: data/characters.json
PATH: Lune.level
OP: SET
VALUE: 86

DATA: data/characters.json
PATH: Lune.attributes
OP: SET
VALUE: {"vitality": 99, "might": 9, "agility": 99, "defence": 0, "luck": 51}

DATA: data/characters.json
PATH: Lune.stats_base
OP: SET
VALUE: {"health": 3408, "attack": 1106, "speed": 1134, "defence": 182, "crit": "29%"}

DATA: data/characters.json
PATH: Lune.stats_modified
OP: SET
VALUE: {"health": 3408, "attack": 10160, "speed": 2553, "defence": 182, "crit": "101%", "_note": "Critical Burn + Burn Affinity + Burning Death; Kralim L33"}

DATA: data/characters.json
PATH: Monoco.level
OP: SET
VALUE: 87

DATA: data/characters.json
PATH: Monoco.attributes
OP: SET
VALUE: {"vitality": 0, "might": 0, "agility": 99, "defence": 99, "luck": 63}

DATA: data/characters.json
PATH: Monoco.stats_base
OP: SET
VALUE: {"health": 2049, "attack": 1113, "speed": 1157, "defence": 729, "crit": "50%"}

DATA: data/characters.json
PATH: Monoco.stats_modified
OP: SET
VALUE: {"health": 4805, "attack": 10863, "speed": 2522, "defence": 2301, "crit": "98%", "_note": "Longer Shell + Powerful Mark + Powerful Revive; Joyaro L33"}

DATA: data/characters.json
PATH: Monoco.skills_learned
OP: ADD
VALUE: "Sakapatate Fire"

DATA: data/weapons.json
PATH: Monoco[name=Joyaro].level
OP: SET
VALUE: 33

DATA: data/weapons.json
PATH: Monoco[name=Joyaro].power
OP: SET
VALUE: 9750

DATA: data/weapons.json
PATH: Monoco[name=Joyaro].scaling
OP: SET
VALUE: "Agility S, Defence A"

DATA: data/weapons.json
PATH: Lune[name=Kralim].level
OP: SET
VALUE: 33

DATA: data/weapons.json
PATH: Lune[name=Kralim].power
OP: SET
VALUE: 9054

DATA: data/weapons.json
PATH: Lune[name=Kralim].scaling
OP: SET
VALUE: "Agility S, Vitality A"

DATA: data/playthrough.json
PATH: inventory.chroma_catalyst_perfect
OP: SET
VALUE: 0

DATA: data/playthrough.json
PATH: current_phase_checklist[id=endless_tower_1_20]
OP: REMOVE

DATA: data/playthrough.json
PATH: current_phase_checklist
OP: ADD
VALUE: {"id": "endless_tower_stages_1_10", "label": "Endless Tower Stages 1–10 (30 fights)", "done": true}

DATA: data/playthrough.json
PATH: current_phase_checklist
OP: ADD
VALUE: {"id": "endless_tower_stage_11", "label": "Endless Tower Stage 11 — 3 fights; Trial 3 (Painted Love) gives Perfect Catalyst + Clair Outfit for Verso", "done": false}

DATA: data/playthrough.json
PATH: current_phase_checklist
OP: ADD
VALUE: {"id": "endless_tower_dlc", "label": "Endless Tower DLC superbosses (4 — accessed via canvases, Thank You Update)", "done": false}
