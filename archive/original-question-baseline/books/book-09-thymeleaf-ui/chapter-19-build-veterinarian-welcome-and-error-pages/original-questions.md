# Chapter 19 — Build veterinarian, welcome, and error pages

Detailed sequence questions in this chapter: **24**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0865  _preserved from Q0312_

The home controller returns the logical view name welcome. Which template should we create for the home page?

## Q0866  _expands Q0312_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/resources/templates/welcome.html, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0312, so it remains tied to that exact PetClinic decision.

## Q0867  _expands Q0312 · file revisit_

PetClinic features cross layers, so finishing src/main/resources/templates/welcome.html in isolation would be artificial. Because the next dependency is represented in VetController.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/resources/templates/welcome.html? This revisit is triggered specifically by legacy build step Q0312, not by a generic file-order rule.

## Q0868  _preserved from Q0313_

The home page should reuse the shared layout and mark Home active. Which menu key should welcome pass to the layout?

## Q0869  _expands Q0313_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/templates/welcome.html, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0313, so it remains tied to that exact PetClinic decision.

## Q0870  _expands Q0313 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/resources/templates/welcome.html relies on behavior or metadata in templates/vets/vetList.html; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0313, not by a generic file-order rule.

## Q0871  _preserved from Q0314_

The veterinarian controller places listVets in the model. Which template should render the paginated vet list?

## Q0872  _expands Q0314_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/templates/vets/vetList.html, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0314, so it remains tied to that exact PetClinic decision.

## Q0873  _expands Q0314 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/resources/templates/vets/vetList.html. Which related file—CrashController.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0314, not by a generic file-order rule.

## Q0874  _preserved from Q0315_

Each veterinarian row should show the vet’s name and specialties. Which nested values should vetList iterate and display?

## Q0875  _expands Q0315_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/resources/templates/vets/vetList.html before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0315, so it remains tied to that exact PetClinic decision.

## Q0876  _expands Q0315 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/resources/templates/vets/vetList.html exposes a missing or inconsistent contract in templates/error.html, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0315, not by a generic file-order rule.

## Q0877  _preserved from Q0316_

Vet pagination uses the same currentPage/totalPages model pattern as owners. Which navigation controls should the vet page include?

## Q0878  _expands Q0316_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/templates/vets/vetList.html, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0316, so it remains tied to that exact PetClinic decision.

## Q0879  _expands Q0316 · file revisit_

Real development now requires a file jump: the change in src/main/resources/templates/vets/vetList.html has a contract with WelcomeController.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/resources/templates/vets/vetList.html? This revisit is triggered specifically by legacy build step Q0316, not by a generic file-order rule.

## Q0880  _preserved from Q0317_

Spring Boot resolves templates/error.html for unhandled application errors. Which template should we create for the crash demonstration?

## Q0881  _expands Q0317_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/templates/error.html, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0317, so it remains tied to that exact PetClinic decision.

## Q0882  _expands Q0317 · file revisit_

PetClinic features cross layers, so finishing src/main/resources/templates/error.html in isolation would be artificial. Because the next dependency is represented in templates/welcome.html, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/resources/templates/error.html? This revisit is triggered specifically by legacy build step Q0317, not by a generic file-order rule.

## Q0883  _preserved from Q0318_

The Error navigation entry triggers /oups so developers can verify error handling. Which shared layout menu state should the error page identify?

## Q0884  _expands Q0318_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/templates/error.html, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0318, so it remains tied to that exact PetClinic decision.

## Q0885  _expands Q0318 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/resources/templates/error.html relies on behavior or metadata in VetController.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0318, not by a generic file-order rule.

## Q0886  _preserved from Q0319_

Error pages should communicate failure without exposing unnecessary internals to normal users. Which kind of friendly content should error.html render while the server logs retain diagnostic detail?

## Q0887  _expands Q0319_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/resources/templates/error.html, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0319, so it remains tied to that exact PetClinic decision.

## Q0888  _expands Q0319 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/resources/templates/error.html. Which related file—templates/vets/vetList.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0319, not by a generic file-order rule.
