# Chapter 10 — Build pets, pet types, formatting, and validation

Detailed sequence questions in this chapter: **66**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0431  _preserved from Q0158_

PetType is a named lookup entity such as cat, dog, or hamster. Which class should extend NamedEntity and map to the types table?

## Q0432  _expands Q0158_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/java/org/springframework/samples/petclinic/owner/PetType.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0158, so it remains tied to that exact PetClinic decision.

## Q0433  _expands Q0158 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetType.java relies on behavior or metadata in PetTypeRepository.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0158, not by a generic file-order rule.

## Q0434  _preserved from Q0159_

Pet is a named persistent entity with birth date, type, and visits. Which class should extend NamedEntity and map to the pets table?

## Q0435  _expands Q0159_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0159, so it remains tied to that exact PetClinic decision.

## Q0436  _expands Q0159 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/Pet.java. Which related file—PetTypeFormatter.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0159, not by a generic file-order rule.

## Q0437  _preserved from Q0160_

Pet birth dates are calendar dates without times. Which Java time type should represent birthDate?

## Q0438  _expands Q0160_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/Pet.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0160, so it remains tied to that exact PetClinic decision.

## Q0439  _expands Q0160 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/Pet.java exposes a missing or inconsistent contract in PetValidator.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0160, not by a generic file-order rule.

## Q0440  _preserved from Q0161_

HTML date inputs and Spring binding use a predictable yyyy-MM-dd representation. Which formatting annotation should be applied to birthDate?

## Q0441  _expands Q0161_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0161, so it remains tied to that exact PetClinic decision.

## Q0442  _expands Q0161 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/Pet.java has a contract with db/h2/schema.sql, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/Pet.java? This revisit is triggered specifically by legacy build step Q0161, not by a generic file-order rule.

## Q0443  _preserved from Q0162_

Many pets can share one PetType. Which JPA relationship should connect Pet.type to PetType?

## Q0444  _expands Q0162_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0162, so it remains tied to that exact PetClinic decision.

## Q0445  _expands Q0162 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/Pet.java in isolation would be artificial. Because the next dependency is represented in Owner.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/Pet.java? This revisit is triggered specifically by legacy build step Q0162, not by a generic file-order rule.

## Q0446  _preserved from Q0163_

The pets table stores type_id. Which join column should the Pet.type relationship use?

## Q0447  _expands Q0163_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0163, so it remains tied to that exact PetClinic decision.

## Q0448  _expands Q0163 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/Pet.java relies on behavior or metadata in PetType.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0163, not by a generic file-order rule.

## Q0449  _preserved from Q0164_

A pet can have many visits and saving aggregate changes should cascade to them. Which relationship should Pet define for visits?

## Q0450  _expands Q0164_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0164, so it remains tied to that exact PetClinic decision.

## Q0451  _expands Q0164 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/Pet.java. Which related file—PetTypeRepository.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0164, not by a generic file-order rule.

## Q0452  _preserved from Q0165_

The visits table stores pet_id. Which join column should the Pet.visits relationship use?

## Q0453  _expands Q0165_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/Pet.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0165, so it remains tied to that exact PetClinic decision.

## Q0454  _expands Q0165 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/Pet.java exposes a missing or inconsistent contract in PetTypeFormatter.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0165, not by a generic file-order rule.

## Q0455  _preserved from Q0166_

Owner details should show visits chronologically. Which ordering rule should be applied to the visits collection?

## Q0456  _expands Q0166_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0166, so it remains tied to that exact PetClinic decision.

## Q0457  _expands Q0166 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/Pet.java has a contract with PetValidator.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/Pet.java? This revisit is triggered specifically by legacy build step Q0166, not by a generic file-order rule.

## Q0458  _preserved from Q0167_

A Set prevents duplicate visit object entries while LinkedHashSet preserves iteration order. Which collection shape should back visits?

## Q0459  _expands Q0167_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/Pet.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0167, so it remains tied to that exact PetClinic decision.

## Q0460  _expands Q0167 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/Pet.java in isolation would be artificial. Because the next dependency is represented in db/h2/schema.sql, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/Pet.java? This revisit is triggered specifically by legacy build step Q0167, not by a generic file-order rule.

## Q0461  _preserved from Q0168_

PetController needs a list of valid pet types in consistent order. Which repository interface should we create for PetType?

## Q0462  _expands Q0168_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/owner/PetTypeRepository.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0168, so it remains tied to that exact PetClinic decision.

## Q0463  _expands Q0168 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetTypeRepository.java relies on behavior or metadata in Owner.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0168, not by a generic file-order rule.

## Q0464  _preserved from Q0169_

Normal PetType CRUD can come from Spring Data JPA. Which repository base interface should PetTypeRepository extend?

## Q0465  _expands Q0169_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetTypeRepository.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0169, so it remains tied to that exact PetClinic decision.

## Q0466  _expands Q0169 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetTypeRepository.java. Which related file—Pet.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0169, not by a generic file-order rule.

## Q0467  _preserved from Q0170_

The pet-type dropdown should be ordered by name. Which repository query behavior should findPetTypes provide?

## Q0468  _expands Q0170_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/owner/PetTypeRepository.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0170, so it remains tied to that exact PetClinic decision.

## Q0469  _expands Q0170 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetTypeRepository.java exposes a missing or inconsistent contract in PetType.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0170, not by a generic file-order rule.

## Q0470  _preserved from Q0171_

Spring MVC formatters translate between form text and domain objects. Which component should implement Formatter<PetType>?

## Q0471  _expands Q0171_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0171, so it remains tied to that exact PetClinic decision.

## Q0472  _expands Q0171 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java has a contract with PetTypeRepository.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java? This revisit is triggered specifically by legacy build step Q0171, not by a generic file-order rule.

## Q0473  _preserved from Q0172_

Formatting a PetType for display should use its name. What should the formatter’s print operation return?

## Q0474  _expands Q0172_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0172, so it remains tied to that exact PetClinic decision.

## Q0475  _expands Q0172 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java in isolation would be artificial. Because the next dependency is represented in PetValidator.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java? This revisit is triggered specifically by legacy build step Q0172, not by a generic file-order rule.

## Q0476  _preserved from Q0173_

Parsing a submitted pet type requires matching the incoming text to one of the repository’s known types. What lookup behavior should parse implement?

## Q0477  _expands Q0173_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0173, so it remains tied to that exact PetClinic decision.

## Q0478  _expands Q0173 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0173, not by a generic file-order rule.

## Q0479  _preserved from Q0174_

Unknown pet-type text should not silently create a new type. Which kind of error should parse signal when no known type matches?

## Q0480  _expands Q0174_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0174, so it remains tied to that exact PetClinic decision.

## Q0481  _expands Q0174 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetTypeFormatter.java. Which related file—Owner.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0174, not by a generic file-order rule.

## Q0482  _preserved from Q0175_

Pet form rules are more complex than a few field annotations, so the project uses a custom Spring Validator. Which validation class should we create?

## Q0483  _expands Q0175_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0175, so it remains tied to that exact PetClinic decision.

## Q0484  _expands Q0175 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java exposes a missing or inconsistent contract in Pet.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0175, not by a generic file-order rule.

## Q0485  _preserved from Q0176_

A custom Spring Validator must declare which object types it supports. What should supports return for Pet and its subclasses?

## Q0486  _expands Q0176_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0176, so it remains tied to that exact PetClinic decision.

## Q0487  _expands Q0176 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java has a contract with PetType.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java? This revisit is triggered specifically by legacy build step Q0176, not by a generic file-order rule.

## Q0488  _preserved from Q0177_

Pet names are required and limited to 30 characters. Which two checks should the validator apply to name?

## Q0489  _expands Q0177_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0177, so it remains tied to that exact PetClinic decision.

## Q0490  _expands Q0177 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java in isolation would be artificial. Because the next dependency is represented in PetTypeRepository.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java? This revisit is triggered specifically by legacy build step Q0177, not by a generic file-order rule.

## Q0491  _preserved from Q0178_

A new pet cannot be saved without selecting a type. Which validation rule should apply to type when pet.isNew() is true?

## Q0492  _expands Q0178_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0178, so it remains tied to that exact PetClinic decision.

## Q0493  _expands Q0178 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java relies on behavior or metadata in PetTypeFormatter.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0178, not by a generic file-order rule.

## Q0494  _preserved from Q0179_

A pet cannot be saved without a birth date. Which validation rule should apply to birthDate?

## Q0495  _expands Q0179_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0179, so it remains tied to that exact PetClinic decision.

## Q0496  _expands Q0179 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/owner/PetValidator.java. Which related file—db/h2/schema.sql—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0179, not by a generic file-order rule.
