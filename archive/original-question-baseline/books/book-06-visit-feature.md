# Book 6 — Visit Feature

> PRESERVED BASELINE: question wording below is copied unchanged from the 1,150-question source set. Do not edit or delete during rebuild work.

# Chapter 12 — Build visits and appointment booking

Detailed sequence questions in this chapter: **45**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0578  _preserved from Q0207_

A Visit is a persisted record with a generated ID, date, and description. Which class should extend BaseEntity and map to the visits table?

## Q0579  _expands Q0207_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/owner/Visit.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0207, so it remains tied to that exact PetClinic decision.

## Q0580  _expands Q0207 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/Visit.java in isolation would be artificial. Because the next dependency is represented in Owner.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/Visit.java? This revisit is triggered specifically by legacy build step Q0207, not by a generic file-order rule.

## Q0581  _preserved from Q0208_

The database column is visit_date while the Java property is date. Which column mapping should the date field declare?

## Q0582  _expands Q0208_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/Visit.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0208, so it remains tied to that exact PetClinic decision.

## Q0583  _expands Q0208 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/Visit.java relies on behavior or metadata in Pet.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0208, not by a generic file-order rule.

## Q0584  _preserved from Q0209_

Visit dates are date-only values formatted yyyy-MM-dd for the form. Which Java type and formatting annotation should the date field use?

## Q0585  _expands Q0209_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/Visit.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0209, so it remains tied to that exact PetClinic decision.

## Q0586  _expands Q0209 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/Visit.java. Which related file—templates/pets/createOrUpdateVisitForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0209, not by a generic file-order rule.

## Q0587  _preserved from Q0210_

A visit description is required. Which validation annotation should guard description?

## Q0588  _expands Q0210_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/Visit.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0210, so it remains tied to that exact PetClinic decision.

## Q0589  _expands Q0210 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/Visit.java exposes a missing or inconsistent contract in db/h2/schema.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0210, not by a generic file-order rule.

## Q0590  _preserved from Q0211_

The canonical constructor pre-populates a new visit for tomorrow. Which default date should a newly constructed Visit receive?

## Q0591  _expands Q0211_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/Visit.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0211, so it remains tied to that exact PetClinic decision.

## Q0592  _expands Q0211 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/Visit.java has a contract with VisitController.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/Visit.java? This revisit is triggered specifically by legacy build step Q0211, not by a generic file-order rule.

## Q0593  _preserved from Q0212_

VisitController persists through OwnerRepository because visits are managed through the owner/pet aggregate. Which repository should the controller inject?

## Q0594  _expands Q0212_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0212, so it remains tied to that exact PetClinic decision.

## Q0595  _expands Q0212 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/VisitController.java in isolation would be artificial. Because the next dependency is represented in Owner.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/VisitController.java? This revisit is triggered specifically by legacy build step Q0212, not by a generic file-order rule.

## Q0596  _preserved from Q0213_

Form binding must not allow client-provided IDs to overwrite persistent IDs. Which binder protection should VisitController install?

## Q0597  _expands Q0213_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0213, so it remains tied to that exact PetClinic decision.

## Q0598  _expands Q0213 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java relies on behavior or metadata in Pet.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0213, not by a generic file-order rule.

## Q0599  _preserved from Q0214_

Before visit handlers execute, the controller needs the owner, pet, and a fresh visit in the model. Which @ModelAttribute preparation method should load those objects?

## Q0600  _expands Q0214_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0214, so it remains tied to that exact PetClinic decision.

## Q0601  _expands Q0214 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/VisitController.java. Which related file—templates/pets/createOrUpdateVisitForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0214, not by a generic file-order rule.

## Q0602  _preserved from Q0215_

A pet ID is only valid if it belongs to the owner in the URL. What validation should the visit model loader perform after loading the owner?

## Q0603  _expands Q0215_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0215, so it remains tied to that exact PetClinic decision.

## Q0604  _expands Q0215 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java exposes a missing or inconsistent contract in db/h2/schema.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0215, not by a generic file-order rule.

## Q0605  _preserved from Q0216_

The visit form needs owner and pet model entries in addition to the visit itself. Which objects should the loader place into the model map?

## Q0606  _expands Q0216_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0216, so it remains tied to that exact PetClinic decision.

## Q0607  _expands Q0216 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java has a contract with Visit.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/VisitController.java? This revisit is triggered specifically by legacy build step Q0216, not by a generic file-order rule.

## Q0608  _preserved from Q0217_

A fresh Visit should be attached to the pet before the form is rendered. Which aggregate helper should the loader call?

## Q0609  _expands Q0217_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0217, so it remains tied to that exact PetClinic decision.

## Q0610  _expands Q0217 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/VisitController.java in isolation would be artificial. Because the next dependency is represented in Owner.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/VisitController.java? This revisit is triggered specifically by legacy build step Q0217, not by a generic file-order rule.

## Q0611  _preserved from Q0218_

The HTML date input can use a minimum allowed appointment date. Which model attribute should expose tomorrow as the minimum visit date?

## Q0612  _expands Q0218_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0218, so it remains tied to that exact PetClinic decision.

## Q0613  _expands Q0218 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java relies on behavior or metadata in Pet.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0218, not by a generic file-order rule.

## Q0614  _preserved from Q0219_

GET /owners/{ownerId}/pets/{petId}/visits/new should render the visit form. Which template should the initializer return?

## Q0615  _expands Q0219_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0219, so it remains tied to that exact PetClinic decision.

## Q0616  _expands Q0219 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/VisitController.java. Which related file—templates/pets/createOrUpdateVisitForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0219, not by a generic file-order rule.

## Q0617  _preserved from Q0220_

A visit must be scheduled after today. Which date rule should the POST handler enforce before saving?

## Q0618  _expands Q0220_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0220, so it remains tied to that exact PetClinic decision.

## Q0619  _expands Q0220 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java exposes a missing or inconsistent contract in db/h2/schema.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0220, not by a generic file-order rule.

## Q0620  _preserved from Q0221_

Successful booking should add the visit to the owner aggregate, save the owner, show a flash message, and return to owner details. Which sequence of actions should complete the booking flow?

## Q0621  _expands Q0221_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/VisitController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0221, so it remains tied to that exact PetClinic decision.

## Q0622  _expands Q0221 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/VisitController.java has a contract with Visit.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/VisitController.java? This revisit is triggered specifically by legacy build step Q0221, not by a generic file-order rule.


---

