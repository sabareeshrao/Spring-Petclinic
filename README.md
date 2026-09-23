# Spring PetClinic — Question-Driven Reconstruction

This repository is the project-specific learning/navigation repository for rebuilding the canonical Spring PetClinic application from zero to final state through teaching questions.

## Architecture

- `project/` — full snapshot of the finished canonical `spring-projects/spring-petclinic` repository. This is the reference/end-state source used by **View Full Code**.
- `curriculum/` — active learning data in the hierarchy **Book → Chapter → Lesson → Question**.
- `site/` — this project's GitHub Pages navigation/player shell.
- `archive/original-question-baseline/` — preserved legacy 1,150-question baseline. It is retained for reference and is **not** the active course.
- Software simulators are owned by `sabareeshrao/Experiment-VS-Code`. This repo does not fork their product UI.

## Simulator model

GitHub Pages builds this project by checking out the current master simulator repository and copying its simulator package into the Pages artifact. The PetClinic repo owns the curriculum and project state; the master software repo owns IntelliJ, Spring Initializr, Git, GitHub, database tools, and other simulator UIs.

Expected Pages URL:

`https://sabareeshrao.github.io/Spring-Petclinic/`

## Learning rule

Questions must teach before asking:

1. explain the concept,
2. explain why it matters at the current PetClinic step,
3. ask the learner to identify/apply the next change,
4. carry an answer and hidden software action,
5. advance cumulative project state deterministically.
