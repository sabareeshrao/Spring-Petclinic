# Chapter 11 — Implement pet create and edit flows

Detailed sequence questions in this chapter: **81**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0497  _preserved from Q0180_

Pet routes are nested beneath a specific owner because pets are managed inside the owner aggregate. Which class-level request mapping should PetController use?

## Q0498  _expands Q0180_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0180, so it remains tied to that exact PetClinic decision.

## Q0499  _expands Q0180 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0180, not by a generic file-order rule.

## Q0500  _preserved from Q0181_

PetController needs both owner persistence and pet-type lookup. Which two repositories should its constructor receive?

## Q0501  _expands Q0181_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0181, so it remains tied to that exact PetClinic decision.

## Q0502  _expands Q0181 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java has a contract with Owner.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0181, not by a generic file-order rule.

## Q0503  _preserved from Q0182_

Every pet form needs the list of available types. Which @ModelAttribute method should expose those types to the view?

## Q0504  _expands Q0182_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0182, so it remains tied to that exact PetClinic decision.

## Q0505  _expands Q0182 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetController.java in isolation would be artificial. Because the next dependency is represented in Pet.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0182, not by a generic file-order rule.

## Q0506  _preserved from Q0183_

Every nested pet request needs the owning Owner loaded from ownerId. Which model attribute should load and expose the owner?

## Q0507  _expands Q0183_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0183, so it remains tied to that exact PetClinic decision.

## Q0508  _expands Q0183 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetController.java relies on behavior or metadata in PetValidator.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0183, not by a generic file-order rule.

## Q0509  _preserved from Q0184_

Create requests need a fresh Pet, while edit requests need the existing pet from the owner. How should the pet model-attribute loader distinguish missing petId from present petId?

## Q0510  _expands Q0184_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0184, so it remains tied to that exact PetClinic decision.

## Q0511  _expands Q0184 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetController.java. Which related file—templates/pets/createOrUpdatePetForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0184, not by a generic file-order rule.

## Q0512  _preserved from Q0185_

The owner object is loaded from persistence and its ID must not be editable from form fields. Which binder should protect Owner IDs?

## Q0513  _expands Q0185_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0185, so it remains tied to that exact PetClinic decision.

## Q0514  _expands Q0185 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0185, not by a generic file-order rule.

## Q0515  _preserved from Q0186_

Pet forms should use the custom PetValidator and also block ID binding. Which binder configuration should be attached to the pet model attribute?

## Q0516  _expands Q0186_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0186, so it remains tied to that exact PetClinic decision.

## Q0517  _expands Q0186 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java has a contract with Owner.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0186, not by a generic file-order rule.

## Q0518  _preserved from Q0187_

A GET on /pets/new should prepare a new Pet inside the owner aggregate. What should the creation initializer do before returning the form view?

## Q0519  _expands Q0187_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0187, so it remains tied to that exact PetClinic decision.

## Q0520  _expands Q0187 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetController.java in isolation would be artificial. Because the next dependency is represented in Pet.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0187, not by a generic file-order rule.

## Q0521  _preserved from Q0188_

The create and edit pet screens share one Thymeleaf template. Which shared view should both flows return?

## Q0522  _expands Q0188_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0188, so it remains tied to that exact PetClinic decision.

## Q0523  _expands Q0188 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetController.java relies on behavior or metadata in PetValidator.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0188, not by a generic file-order rule.

## Q0524  _preserved from Q0189_

Duplicate pet names are prohibited per owner. Which pre-save check should the create handler perform when the submitted pet is new?

## Q0525  _expands Q0189_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0189, so it remains tied to that exact PetClinic decision.

## Q0526  _expands Q0189 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetController.java. Which related file—templates/pets/createOrUpdatePetForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0189, not by a generic file-order rule.

## Q0527  _preserved from Q0190_

A pet cannot have a birth date in the future. Which date comparison should the create handler perform against LocalDate.now()?

## Q0528  _expands Q0190_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0190, so it remains tied to that exact PetClinic decision.

## Q0529  _expands Q0190 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0190, not by a generic file-order rule.

## Q0530  _preserved from Q0191_

Validation errors should preserve the form rather than redirect. What should the create handler return when BindingResult contains errors?

## Q0531  _expands Q0191_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0191, so it remains tied to that exact PetClinic decision.

## Q0532  _expands Q0191 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java has a contract with Owner.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0191, not by a generic file-order rule.

## Q0533  _preserved from Q0192_

A valid pet should become part of the owner aggregate before persistence. Which Owner helper should be used to attach the pet?

## Q0534  _expands Q0192_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0192, so it remains tied to that exact PetClinic decision.

## Q0535  _expands Q0192 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetController.java in isolation would be artificial. Because the next dependency is represented in Pet.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0192, not by a generic file-order rule.

## Q0536  _preserved from Q0193_

saveAndFlush pushes the owner aggregate change to the database immediately, allowing constraint violations to surface in the request. Which persistence method should pet creation use?

## Q0537  _expands Q0193_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0193, so it remains tied to that exact PetClinic decision.

## Q0538  _expands Q0193 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetController.java relies on behavior or metadata in PetValidator.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0193, not by a generic file-order rule.

## Q0539  _preserved from Q0194_

The database unique constraint is a second line of defense against duplicate owner/pet names. Which exception type should the controller catch around saveAndFlush?

## Q0540  _expands Q0194_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0194, so it remains tied to that exact PetClinic decision.

## Q0541  _expands Q0194 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetController.java. Which related file—templates/pets/createOrUpdatePetForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0194, not by a generic file-order rule.

## Q0542  _preserved from Q0195_

Not every DataIntegrityViolationException means duplicate pet name. How should the controller distinguish the expected unique-owner-pet-name violation from unrelated integrity failures?

## Q0543  _expands Q0195_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0195, so it remains tied to that exact PetClinic decision.

## Q0544  _expands Q0195 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0195, not by a generic file-order rule.

## Q0545  _preserved from Q0196_

Unexpected integrity violations should remain visible to developers. What should happen when the caught integrity exception is not the duplicate-name constraint?

## Q0546  _expands Q0196_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0196, so it remains tied to that exact PetClinic decision.

## Q0547  _expands Q0196 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java has a contract with Owner.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0196, not by a generic file-order rule.

## Q0548  _preserved from Q0197_

Successful creation should show feedback after redirecting to owner details. Which flash-message mechanism and redirect target should be used?

## Q0549  _expands Q0197_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0197, so it remains tied to that exact PetClinic decision.

## Q0550  _expands Q0197 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetController.java in isolation would be artificial. Because the next dependency is represented in Pet.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0197, not by a generic file-order rule.

## Q0551  _preserved from Q0198_

Editing a pet starts at a route containing both ownerId and petId. Which GET route should open the edit form?

## Q0552  _expands Q0198_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0198, so it remains tied to that exact PetClinic decision.

## Q0553  _expands Q0198 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetController.java relies on behavior or metadata in PetValidator.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0198, not by a generic file-order rule.

## Q0554  _preserved from Q0199_

When editing, a name collision matters only if the matching pet is a different persistent record. Which ID comparison should the update validation perform after name lookup?

## Q0555  _expands Q0199_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0199, so it remains tied to that exact PetClinic decision.

## Q0556  _expands Q0199 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetController.java. Which related file—templates/pets/createOrUpdatePetForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0199, not by a generic file-order rule.

## Q0557  _preserved from Q0200_

Future birth dates are invalid during edits as well as creates. Which validation must be repeated in the update flow?

## Q0558  _expands Q0200_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0200, so it remains tied to that exact PetClinic decision.

## Q0559  _expands Q0200 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0200, not by a generic file-order rule.

## Q0560  _preserved from Q0201_

The submitted Pet is a bound form object, while the owner aggregate may already contain a managed pet instance. Why should update logic copy submitted fields into the existing aggregate pet rather than blindly replacing the collection element?

## Q0561  _expands Q0201_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0201, so it remains tied to that exact PetClinic decision.

## Q0562  _expands Q0201 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java has a contract with Owner.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0201, not by a generic file-order rule.

## Q0563  _preserved from Q0202_

A persistent pet must have an ID before updatePetDetails can target it. Which state assertion should protect the update helper?

## Q0564  _expands Q0202_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0202, so it remains tied to that exact PetClinic decision.

## Q0565  _expands Q0202 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetController.java in isolation would be artificial. Because the next dependency is represented in Pet.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0202, not by a generic file-order rule.

## Q0566  _preserved from Q0203_

If the owner already contains the pet ID, its name, birth date, and type should be updated. Which three business properties should updatePetDetails copy?

## Q0567  _expands Q0203_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0203, so it remains tied to that exact PetClinic decision.

## Q0568  _expands Q0203 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetController.java relies on behavior or metadata in PetValidator.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0203, not by a generic file-order rule.

## Q0569  _preserved from Q0204_

If the pet is not already in the aggregate, the helper can fall back to owner.addPet. Which aggregate method should handle that fallback?

## Q0570  _expands Q0204_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0204, so it remains tied to that exact PetClinic decision.

## Q0571  _expands Q0204 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetController.java. Which related file—templates/pets/createOrUpdatePetForm.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0204, not by a generic file-order rule.

## Q0572  _preserved from Q0205_

Database uniqueness can still race with application-level duplicate checks. Why should the edit path keep the database-exception handling even after checking names in memory?

## Q0573  _expands Q0205_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0205, so it remains tied to that exact PetClinic decision.

## Q0574  _expands Q0205 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetController.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0205, not by a generic file-order rule.

## Q0575  _preserved from Q0206_

A successful edit returns to the owner details page. Which redirect should the update handler return?

## Q0576  _expands Q0206_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0206, so it remains tied to that exact PetClinic decision.

## Q0577  _expands Q0206 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetController.java has a contract with Owner.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetController.java? This revisit is triggered specifically by legacy build step Q0206, not by a generic file-order rule.
