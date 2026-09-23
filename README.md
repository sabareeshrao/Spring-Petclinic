# Spring PetClinic — Question-Driven Reconstruction

This repository rebuilds the canonical Spring PetClinic project from zero to final state through teaching questions.

## Non-negotiable UI contract

This repository does **not** own a custom playback UI. Its GitHub Pages build copies the authoritative `player.html`, `app.js`, `styles.css`, and `simulator/` package from `sabareeshrao/Experiment-VS-Code`.

PetClinic owns only:

- `project/` — complete finished Spring PetClinic reference source for **View Full Code**.
- `curriculum/` — **Book → Chapter → Lesson → Question** learning data.
- `scripts/build-player-data.py` — adapts PetClinic curriculum/project data to the master player contract.
- `archive/original-question-baseline/` — preserved old 1,150-question experiment; not the active curriculum.

Any missing IntelliJ, Spring Initializr, Git, GitHub, database, terminal, or other software capability must be implemented in `Experiment-VS-Code`, then consumed here.

Expected Pages URL:

`https://sabareeshrao.github.io/Spring-Petclinic/`
