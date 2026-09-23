# Chapter 16 — Build the Thymeleaf layout and reusable form fragments

Detailed sequence questions in this chapter: **45**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0764  _preserved from Q0269_

Thymeleaf templates belong under src/main/resources/templates. Which resource directory should we create before adding HTML views?

## Q0765  _expands Q0269_

Before moving away from src/main/resources/src/main/resources/templates, which observable state should a developer verify so a later failure is not caused by an unnoticed mistake in this step? This micro-check belongs specifically to legacy build step Q0269, so it remains tied to that exact PetClinic decision.

## Q0766  _expands Q0269 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/resources/src/main/resources/templates. Which related file—messages/messages.properties—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0269, not by a generic file-order rule.

## Q0767  _preserved from Q0270_

Most pages share navigation, CSS, footer, and scripts. Which reusable layout template should centralize that structure?

## Q0768  _expands Q0270_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/resources/templates/fragments/layout.html, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0270, so it remains tied to that exact PetClinic decision.

## Q0769  _expands Q0270 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/resources/templates/fragments/layout.html exposes a missing or inconsistent contract in templates/fragments/selectField.html, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0270, not by a generic file-order rule.

## Q0770  _preserved from Q0271_

A Thymeleaf fragment can accept the page body and active-menu identifier as parameters. Which two fragment inputs should the layout expose?

## Q0771  _expands Q0271_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/templates/fragments/layout.html, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0271, so it remains tied to that exact PetClinic decision.

## Q0772  _expands Q0271 · file revisit_

Real development now requires a file jump: the change in src/main/resources/templates/fragments/layout.html has a contract with messages/messages.properties, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/resources/templates/fragments/layout.html? This revisit is triggered specifically by legacy build step Q0271, not by a generic file-order rule.

## Q0773  _preserved from Q0272_

The layout page title should come from the message bundle so it can be localized. Which Thymeleaf expression style should supply the title text?

## Q0774  _expands Q0272_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/templates/fragments/layout.html, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0272, so it remains tied to that exact PetClinic decision.

## Q0775  _expands Q0272 · file revisit_

PetClinic features cross layers, so finishing src/main/resources/templates/fragments/layout.html in isolation would be artificial. Because the next dependency is represented in petclinic.css, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/resources/templates/fragments/layout.html? This revisit is triggered specifically by legacy build step Q0272, not by a generic file-order rule.

## Q0776  _preserved from Q0273_

Font Awesome and application CSS are loaded from classpath web/static resources. Which resource links should the shared head include?

## Q0777  _expands Q0273_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/templates/fragments/layout.html, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0273, so it remains tied to that exact PetClinic decision.

## Q0778  _expands Q0273 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/resources/templates/fragments/layout.html relies on behavior or metadata in templates/fragments/inputField.html; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0273, not by a generic file-order rule.

## Q0779  _preserved from Q0274_

Navigation should indicate which section is active. What dynamic class behavior should the reusable menu item implement?

## Q0780  _expands Q0274_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/resources/templates/fragments/layout.html, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0274, so it remains tied to that exact PetClinic decision.

## Q0781  _expands Q0274 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/resources/templates/fragments/layout.html. Which related file—templates/fragments/selectField.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0274, not by a generic file-order rule.

## Q0782  _preserved from Q0275_

The main navigation exposes Home, Find Owners, Veterinarians, and Error. Which four routes should the layout menu link to?

## Q0783  _expands Q0275_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/resources/templates/fragments/layout.html before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0275, so it remains tied to that exact PetClinic decision.

## Q0784  _expands Q0275 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/resources/templates/fragments/layout.html exposes a missing or inconsistent contract in messages/messages.properties, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0275, not by a generic file-order rule.

## Q0785  _preserved from Q0276_

Each page supplies its own body fragment into the shared shell. Which Thymeleaf insertion mechanism should place the page template inside the layout?

## Q0786  _expands Q0276_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/templates/fragments/layout.html, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0276, so it remains tied to that exact PetClinic decision.

## Q0787  _expands Q0276 · file revisit_

Real development now requires a file jump: the change in src/main/resources/templates/fragments/layout.html has a contract with petclinic.css, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/resources/templates/fragments/layout.html? This revisit is triggered specifically by legacy build step Q0276, not by a generic file-order rule.

## Q0788  _preserved from Q0277_

Bootstrap JavaScript is supplied as a WebJar. Which script resource should the layout load at the end of the body?

## Q0789  _expands Q0277_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/templates/fragments/layout.html, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0277, so it remains tied to that exact PetClinic decision.

## Q0790  _expands Q0277 · file revisit_

PetClinic features cross layers, so finishing src/main/resources/templates/fragments/layout.html in isolation would be artificial. Because the next dependency is represented in templates/fragments/inputField.html, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/resources/templates/fragments/layout.html? This revisit is triggered specifically by legacy build step Q0277, not by a generic file-order rule.

## Q0791  _preserved from Q0278_

Owner and pet forms repeatedly need labeled inputs plus validation errors. Which reusable input fragment should we create?

## Q0792  _expands Q0278_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/templates/fragments/inputField.html, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0278, so it remains tied to that exact PetClinic decision.

## Q0793  _expands Q0278 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/resources/templates/fragments/inputField.html relies on behavior or metadata in templates/fragments/selectField.html; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0278, not by a generic file-order rule.

## Q0794  _preserved from Q0279_

Select controls such as pet type need similar reusable rendering. Which select-field fragment should we create?

## Q0795  _expands Q0279_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/resources/templates/fragments/selectField.html, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0279, so it remains tied to that exact PetClinic decision.

## Q0796  _expands Q0279 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/resources/templates/fragments/selectField.html. Which related file—messages/messages.properties—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0279, not by a generic file-order rule.

## Q0797  _preserved from Q0280_

Reusable form fragments should bind to the current th:object path rather than hard-code object names. Which Thymeleaf field-binding pattern should the fragments use?

## Q0798  _expands Q0280_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/resources/templates/fragments/*.html before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0280, so it remains tied to that exact PetClinic decision.

## Q0799  _expands Q0280 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/resources/templates/fragments/*.html exposes a missing or inconsistent contract in petclinic.css, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0280, not by a generic file-order rule.

## Q0800  _preserved from Q0281_

Validation feedback should appear next to the corresponding bound field. Which Thymeleaf error expression should form fragments support?

## Q0801  _expands Q0281_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/templates/fragments/*.html, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0281, so it remains tied to that exact PetClinic decision.

## Q0802  _expands Q0281 · file revisit_

Real development now requires a file jump: the change in src/main/resources/templates/fragments/*.html has a contract with templates/fragments/layout.html, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/resources/templates/fragments/*.html? This revisit is triggered specifically by legacy build step Q0281, not by a generic file-order rule.

## Q0803  _preserved from Q0282_

The shared layout expects a body fragment plus a menu key from each page. How should individual templates invoke or replace themselves with the layout fragment?

## Q0804  _expands Q0282_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/templates/*.html, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0282, so it remains tied to that exact PetClinic decision.

## Q0805  _expands Q0282 · file revisit_

PetClinic features cross layers, so finishing src/main/resources/templates/*.html in isolation would be artificial. Because the next dependency is represented in templates/fragments/inputField.html, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/resources/templates/*.html? This revisit is triggered specifically by legacy build step Q0282, not by a generic file-order rule.

## Q0806  _preserved from Q0283_

All visible labels should prefer message keys instead of fixed English where localization is expected. Which Thymeleaf message syntax should templates use for translatable text?

## Q0807  _expands Q0283_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/templates/**/*.html, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0283, so it remains tied to that exact PetClinic decision.

## Q0808  _expands Q0283 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/resources/templates/**/*.html relies on behavior or metadata in templates/fragments/selectField.html; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0283, not by a generic file-order rule.
