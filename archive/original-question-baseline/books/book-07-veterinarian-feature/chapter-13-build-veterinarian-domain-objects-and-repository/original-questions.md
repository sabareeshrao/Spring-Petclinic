# Chapter 13 — Build veterinarian domain objects and repository

Detailed sequence questions in this chapter: **54**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0623  _preserved from Q0222_

A Specialty is a persisted named lookup value such as dentistry. Which class should extend NamedEntity and map to specialties?

## Q0624  _expands Q0222_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/vet/Specialty.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0222, so it remains tied to that exact PetClinic decision.

## Q0625  _expands Q0222 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/vet/Specialty.java in isolation would be artificial. Because the next dependency is represented in VetRepository.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/vet/Specialty.java? This revisit is triggered specifically by legacy build step Q0222, not by a generic file-order rule.

## Q0626  _preserved from Q0223_

A veterinarian is a person with zero or more specialties. Which class should extend Person and map to vets?

## Q0627  _expands Q0223_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0223, so it remains tied to that exact PetClinic decision.

## Q0628  _expands Q0223 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/vet/Vet.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0223, not by a generic file-order rule.

## Q0629  _preserved from Q0224_

One veterinarian can have many specialties and one specialty can belong to many vets. Which JPA relationship should Vet.specialties use?

## Q0630  _expands Q0224_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0224, so it remains tied to that exact PetClinic decision.

## Q0631  _expands Q0224 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/vet/Vet.java. Which related file—NamedEntity.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0224, not by a generic file-order rule.

## Q0632  _preserved from Q0225_

The many-to-many relationship is stored in vet_specialties. Which join table should the Vet mapping declare?

## Q0633  _expands Q0225_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/vet/Vet.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0225, so it remains tied to that exact PetClinic decision.

## Q0634  _expands Q0225 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/vet/Vet.java exposes a missing or inconsistent contract in Person.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0225, not by a generic file-order rule.

## Q0635  _preserved from Q0226_

The join table references vets through vet_id. Which join column should represent the owning side?

## Q0636  _expands Q0226_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0226, so it remains tied to that exact PetClinic decision.

## Q0637  _expands Q0226 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/vet/Vet.java has a contract with Specialty.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/vet/Vet.java? This revisit is triggered specifically by legacy build step Q0226, not by a generic file-order rule.

## Q0638  _preserved from Q0227_

The join table references specialties through specialty_id. Which inverse join column should be declared?

## Q0639  _expands Q0227_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0227, so it remains tied to that exact PetClinic decision.

## Q0640  _expands Q0227 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/vet/Vet.java in isolation would be artificial. Because the next dependency is represented in VetRepository.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/vet/Vet.java? This revisit is triggered specifically by legacy build step Q0227, not by a generic file-order rule.

## Q0641  _preserved from Q0228_

Vet lists display specialties without requiring lazy-session access later in the view. Which fetch strategy should the specialties relationship use in the target project?

## Q0642  _expands Q0228_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0228, so it remains tied to that exact PetClinic decision.

## Q0643  _expands Q0228 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/vet/Vet.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0228, not by a generic file-order rule.

## Q0644  _preserved from Q0229_

The internal specialty set may be null when a Vet is first created. What lazy-initialization behavior should getSpecialtiesInternal provide?

## Q0645  _expands Q0229_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0229, so it remains tied to that exact PetClinic decision.

## Q0646  _expands Q0229 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/vet/Vet.java. Which related file—NamedEntity.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0229, not by a generic file-order rule.

## Q0647  _preserved from Q0230_

Users see specialties alphabetically. How should getSpecialties transform the internal set before returning the public list?

## Q0648  _expands Q0230_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/vet/Vet.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0230, so it remains tied to that exact PetClinic decision.

## Q0649  _expands Q0230 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/vet/Vet.java exposes a missing or inconsistent contract in Person.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0230, not by a generic file-order rule.

## Q0650  _preserved from Q0231_

XML/serialization views need the specialty list exposed as a bindable element. Which XML binding annotation should be placed on the public specialties getter?

## Q0651  _expands Q0231_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0231, so it remains tied to that exact PetClinic decision.

## Q0652  _expands Q0231 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/vet/Vet.java has a contract with Specialty.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/vet/Vet.java? This revisit is triggered specifically by legacy build step Q0231, not by a generic file-order rule.

## Q0653  _preserved from Q0232_

Views may want a simple count of specialties. Which convenience method should Vet expose for the specialty count?

## Q0654  _expands Q0232_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0232, so it remains tied to that exact PetClinic decision.

## Q0655  _expands Q0232 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/vet/Vet.java in isolation would be artificial. Because the next dependency is represented in VetRepository.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/vet/Vet.java? This revisit is triggered specifically by legacy build step Q0232, not by a generic file-order rule.

## Q0656  _preserved from Q0233_

Adding a specialty should update the internal set. Which aggregate helper should Vet provide?

## Q0657  _expands Q0233_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/vet/Vet.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0233, so it remains tied to that exact PetClinic decision.

## Q0658  _expands Q0233 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/vet/Vet.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0233, not by a generic file-order rule.

## Q0659  _preserved from Q0234_

The repository only needs selected read operations rather than the full JpaRepository contract. Which lightweight Spring Data repository interface should VetRepository extend?

## Q0660  _expands Q0234_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0234, so it remains tied to that exact PetClinic decision.

## Q0661  _expands Q0234 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java. Which related file—NamedEntity.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0234, not by a generic file-order rule.

## Q0662  _preserved from Q0235_

Vet lists can be requested as a full collection. Which repository method should retrieve all vets without pagination?

## Q0663  _expands Q0235_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0235, so it remains tied to that exact PetClinic decision.

## Q0664  _expands Q0235 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java exposes a missing or inconsistent contract in Person.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0235, not by a generic file-order rule.

## Q0665  _preserved from Q0236_

The HTML vet list is paginated. Which repository method should accept Pageable and return Page<Vet>?

## Q0666  _expands Q0236_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0236, so it remains tied to that exact PetClinic decision.

## Q0667  _expands Q0236 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java has a contract with Vet.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java? This revisit is triggered specifically by legacy build step Q0236, not by a generic file-order rule.

## Q0668  _preserved from Q0237_

Vet lookup operations are read-only. Which transaction setting should protect these repository methods from accidental writes?

## Q0669  _expands Q0237_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0237, so it remains tied to that exact PetClinic decision.

## Q0670  _expands Q0237 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java in isolation would be artificial. Because the next dependency is represented in Specialty.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java? This revisit is triggered specifically by legacy build step Q0237, not by a generic file-order rule.

## Q0671  _preserved from Q0238_

Veterinarian data changes infrequently and is repeatedly requested. Which cache annotation should be applied to vet read methods?

## Q0672  _expands Q0238_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0238, so it remains tied to that exact PetClinic decision.

## Q0673  _expands Q0238 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0238, not by a generic file-order rule.

## Q0674  _preserved from Q0239_

Both vet query variants should share the same cache region. Which cache name should the repository methods use?

## Q0675  _expands Q0239_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0239, so it remains tied to that exact PetClinic decision.

## Q0676  _expands Q0239 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/vet/VetRepository.java. Which related file—NamedEntity.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0239, not by a generic file-order rule.
