# Chapter 7 — Build the reusable domain model foundation

Detailed sequence questions in this chapter: **36**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0263  _preserved from Q0102_

Multiple entities need the same generated integer identifier, so centralizing that field avoids duplication. Which reusable base class should we create for entity IDs?

## Q0264  _expands Q0102_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0102, so it remains tied to that exact PetClinic decision.

## Q0265  _expands Q0102 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java in isolation would be artificial. Because the next dependency is represented in db/h2/schema.sql, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java? This revisit is triggered specifically by legacy build step Q0102, not by a generic file-order rule.

## Q0266  _preserved from Q0103_

@MappedSuperclass lets JPA inherit mapped fields without giving the base class its own table. Which annotation should BaseEntity use?

## Q0267  _expands Q0103_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0103, so it remains tied to that exact PetClinic decision.

## Q0268  _expands Q0103 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java relies on behavior or metadata in NamedEntity.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0103, not by a generic file-order rule.

## Q0269  _preserved from Q0104_

@Id marks the primary-key property. Which annotation should the Integer id field receive?

## Q0270  _expands Q0104_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0104, so it remains tied to that exact PetClinic decision.

## Q0271  _expands Q0104 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java. Which related file—Person.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0104, not by a generic file-order rule.

## Q0272  _preserved from Q0105_

IDENTITY generation lets the database assign numeric IDs. Which generation strategy should be applied to the id field?

## Q0273  _expands Q0105_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0105, so it remains tied to that exact PetClinic decision.

## Q0274  _expands Q0105 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java exposes a missing or inconsistent contract in db/h2/schema.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0105, not by a generic file-order rule.

## Q0275  _preserved from Q0106_

New unsaved entities can be recognized by a missing generated ID. What condition should an isNew helper evaluate?

## Q0276  _expands Q0106_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0106, so it remains tied to that exact PetClinic decision.

## Q0277  _expands Q0106 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java has a contract with NamedEntity.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/model/BaseEntity.java? This revisit is triggered specifically by legacy build step Q0106, not by a generic file-order rule.

## Q0278  _preserved from Q0107_

Named lookup entities such as PetType and Specialty share both an ID and a name. Which intermediate base class should extend BaseEntity and add a name property?

## Q0279  _expands Q0107_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0107, so it remains tied to that exact PetClinic decision.

## Q0280  _expands Q0107 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java in isolation would be artificial. Because the next dependency is represented in Person.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java? This revisit is triggered specifically by legacy build step Q0107, not by a generic file-order rule.

## Q0281  _preserved from Q0108_

JPA should map the inherited name field into concrete entity tables. Which class-level mapping annotation should NamedEntity also use?

## Q0282  _expands Q0108_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0108, so it remains tied to that exact PetClinic decision.

## Q0283  _expands Q0108 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java relies on behavior or metadata in db/h2/schema.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0108, not by a generic file-order rule.

## Q0284  _preserved from Q0109_

Names used in lookup entities cannot be blank. Which Bean Validation constraint should protect the name field?

## Q0285  _expands Q0109_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0109, so it remains tied to that exact PetClinic decision.

## Q0286  _expands Q0109 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java. Which related file—BaseEntity.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0109, not by a generic file-order rule.

## Q0287  _preserved from Q0110_

Templates and logs benefit when a named entity prints its human-readable name. Which Object method should NamedEntity override to return its name safely?

## Q0288  _expands Q0110_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0110, so it remains tied to that exact PetClinic decision.

## Q0289  _expands Q0110 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/model/NamedEntity.java exposes a missing or inconsistent contract in Person.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0110, not by a generic file-order rule.

## Q0290  _preserved from Q0111_

Owners and veterinarians share first and last names. Which reusable Person superclass should we create above those concrete entities?

## Q0291  _expands Q0111_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/model/Person.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0111, so it remains tied to that exact PetClinic decision.

## Q0292  _expands Q0111 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/model/Person.java has a contract with db/h2/schema.sql, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/model/Person.java? This revisit is triggered specifically by legacy build step Q0111, not by a generic file-order rule.

## Q0293  _preserved from Q0112_

The database columns for first and last name are limited to 30 characters. Which validation constraint should mirror that maximum length in Java?

## Q0294  _expands Q0112_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/model/Person.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0112, so it remains tied to that exact PetClinic decision.

## Q0295  _expands Q0112 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/model/Person.java in isolation would be artificial. Because the next dependency is represented in BaseEntity.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/model/Person.java? This revisit is triggered specifically by legacy build step Q0112, not by a generic file-order rule.

## Q0296  _preserved from Q0113_

First and last names are required business data. Which validation constraint should reject blank name values?

## Q0297  _expands Q0113_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/model/Person.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0113, so it remains tied to that exact PetClinic decision.

## Q0298  _expands Q0113 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/model/Person.java relies on behavior or metadata in NamedEntity.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0113, not by a generic file-order rule.
