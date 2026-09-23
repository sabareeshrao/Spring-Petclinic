# Chapter 8 — Build the Owner aggregate and repository

Detailed sequence questions in this chapter: **54**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0299  _preserved from Q0114_

An owner is a persisted person with contact information. Which concrete class should extend Person and be mapped to the owners table?

## Q0300  _expands Q0114_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0114, so it remains tied to that exact PetClinic decision.

## Q0301  _expands Q0114 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/Owner.java. Which related file—Person.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0114, not by a generic file-order rule.

## Q0302  _preserved from Q0115_

@Entity tells JPA that a concrete class participates in persistence. Which annotation should Owner receive?

## Q0303  _expands Q0115_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/Owner.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0115, so it remains tied to that exact PetClinic decision.

## Q0304  _expands Q0115 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/Owner.java exposes a missing or inconsistent contract in OwnerRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0115, not by a generic file-order rule.

## Q0305  _preserved from Q0116_

The physical table is named owners. Which table mapping should Owner declare?

## Q0306  _expands Q0116_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0116, so it remains tied to that exact PetClinic decision.

## Q0307  _expands Q0116 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/Owner.java has a contract with db/h2/schema.sql, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/Owner.java? This revisit is triggered specifically by legacy build step Q0116, not by a generic file-order rule.

## Q0308  _preserved from Q0117_

Address is required owner information. Which field and validation rule should we add for the owner address?

## Q0309  _expands Q0117_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0117, so it remains tied to that exact PetClinic decision.

## Q0310  _expands Q0117 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/Owner.java in isolation would be artificial. Because the next dependency is represented in Person.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/Owner.java? This revisit is triggered specifically by legacy build step Q0117, not by a generic file-order rule.

## Q0311  _preserved from Q0118_

City is required owner information. Which field and validation rule should we add for the owner city?

## Q0312  _expands Q0118_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0118, so it remains tied to that exact PetClinic decision.

## Q0313  _expands Q0118 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/Owner.java relies on behavior or metadata in OwnerRepository.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0118, not by a generic file-order rule.

## Q0314  _preserved from Q0119_

Telephone must be present and contain exactly ten digits in the target project. Which validation approach should we use to enforce the ten-digit telephone format?

## Q0315  _expands Q0119_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0119, so it remains tied to that exact PetClinic decision.

## Q0316  _expands Q0119 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/Owner.java. Which related file—db/h2/schema.sql—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0119, not by a generic file-order rule.

## Q0317  _preserved from Q0120_

An owner contains a collection of pets and saving an owner should cascade changes to those pets. Which one-to-many relationship should be created between Owner and Pet?

## Q0318  _expands Q0120_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/Owner.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0120, so it remains tied to that exact PetClinic decision.

## Q0319  _expands Q0120 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/Owner.java exposes a missing or inconsistent contract in Person.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0120, not by a generic file-order rule.

## Q0320  _preserved from Q0121_

Pet rows store owner_id instead of using a separate owner-pet join table. Which join column should the Owner.pets relationship use?

## Q0321  _expands Q0121_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0121, so it remains tied to that exact PetClinic decision.

## Q0322  _expands Q0121 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/Owner.java has a contract with OwnerRepository.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/Owner.java? This revisit is triggered specifically by legacy build step Q0121, not by a generic file-order rule.

## Q0323  _preserved from Q0122_

The UI lists an owner’s pets in name order. Which ordering rule should be applied to the pets collection?

## Q0324  _expands Q0122_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0122, so it remains tied to that exact PetClinic decision.

## Q0325  _expands Q0122 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/Owner.java in isolation would be artificial. Because the next dependency is represented in db/h2/schema.sql, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/Owner.java? This revisit is triggered specifically by legacy build step Q0122, not by a generic file-order rule.

## Q0326  _preserved from Q0123_

Aggregate helper methods should prevent null or duplicate pets from being appended accidentally. What responsibility should Owner.addPet perform before modifying the collection?

## Q0327  _expands Q0123_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0123, so it remains tied to that exact PetClinic decision.

## Q0328  _expands Q0123 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/Owner.java relies on behavior or metadata in Person.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0123, not by a generic file-order rule.

## Q0329  _preserved from Q0124_

Controllers need to find a pet by persistent identifier within one owner. Which helper should Owner expose for lookup by pet ID?

## Q0330  _expands Q0124_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0124, so it remains tied to that exact PetClinic decision.

## Q0331  _expands Q0124 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/Owner.java. Which related file—OwnerRepository.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0124, not by a generic file-order rule.

## Q0332  _preserved from Q0125_

Pet creation validation needs case-insensitive name lookup and an option to ignore unsaved pets. Which helper behavior should Owner provide for pet-name lookup?

## Q0333  _expands Q0125_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/Owner.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0125, so it remains tied to that exact PetClinic decision.

## Q0334  _expands Q0125 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/Owner.java exposes a missing or inconsistent contract in db/h2/schema.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0125, not by a generic file-order rule.

## Q0335  _preserved from Q0126_

A visit belongs to a pet, but controller logic starts from the owner aggregate. Which Owner helper should delegate adding a Visit to the pet identified by petId?

## Q0336  _expands Q0126_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/Owner.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0126, so it remains tied to that exact PetClinic decision.

## Q0337  _expands Q0126 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/Owner.java has a contract with Person.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/Owner.java? This revisit is triggered specifically by legacy build step Q0126, not by a generic file-order rule.

## Q0338  _preserved from Q0127_

Spring Data can generate common CRUD persistence code from repository interfaces. Which repository interface should we create for Owner?

## Q0339  _expands Q0127_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0127, so it remains tied to that exact PetClinic decision.

## Q0340  _expands Q0127 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java in isolation would be artificial. Because the next dependency is represented in Owner.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java? This revisit is triggered specifically by legacy build step Q0127, not by a generic file-order rule.

## Q0341  _preserved from Q0128_

Owner needs normal CRUD, pagination, save, and saveAndFlush behavior. Which Spring Data repository base interface should OwnerRepository extend?

## Q0342  _expands Q0128_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0128, so it remains tied to that exact PetClinic decision.

## Q0343  _expands Q0128 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0128, not by a generic file-order rule.

## Q0344  _preserved from Q0129_

Owner search matches last names that start with the submitted text. Which derived-query method shape should the repository expose for prefix searching with Pageable?

## Q0345  _expands Q0129_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0129, so it remains tied to that exact PetClinic decision.

## Q0346  _expands Q0129 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java. Which related file—Person.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0129, not by a generic file-order rule.

## Q0347  _preserved from Q0130_

Controller code handles missing owners explicitly. Which repository lookup type should findById return so absence is represented without null?

## Q0348  _expands Q0130_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0130, so it remains tied to that exact PetClinic decision.

## Q0349  _expands Q0130 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java exposes a missing or inconsistent contract in Owner.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0130, not by a generic file-order rule.

## Q0350  _preserved from Q0131_

The repository works with Owner entities whose IDs are Integer values. Which two generic types should the repository base declaration use?

## Q0351  _expands Q0131_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0131, so it remains tied to that exact PetClinic decision.

## Q0352  _expands Q0131 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java has a contract with db/h2/schema.sql, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java? This revisit is triggered specifically by legacy build step Q0131, not by a generic file-order rule.
