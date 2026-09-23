# Chapter 6 — Create the relational schema and seed data

Detailed sequence questions in this chapter: **60**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0203  _preserved from Q0082_

PetClinic’s default database is H2 and its initialization scripts live under db/h2. Which directory should we create for the H2 schema and seed data?

## Q0204  _expands Q0082_

This build step changes src/main/resources/db/h2, and incremental development works best when each change has a visible success condition. Which immediate check should confirm the action completed correctly before the next question? This micro-check belongs specifically to legacy build step Q0082, so it remains tied to that exact PetClinic decision.

## Q0205  _expands Q0082 · file revisit_

PetClinic features cross layers, so finishing src/main/resources/db/h2 in isolation would be artificial. Because the next dependency is represented in application.properties, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/resources/db/h2? This revisit is triggered specifically by legacy build step Q0082, not by a generic file-order rule.

## Q0206  _preserved from Q0083_

Re-running development schema scripts should start from a predictable clean state. Before CREATE TABLE statements, what should the schema script do with tables from an older run?

## Q0207  _expands Q0083_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in db/h2/schema.sql, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0083, so it remains tied to that exact PetClinic decision.

## Q0208  _expands Q0083 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in db/h2/schema.sql relies on behavior or metadata in db/h2/data.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0083, not by a generic file-order rule.

## Q0209  _preserved from Q0084_

Veterinarians have generated integer IDs plus first and last names. Which table should represent veterinarians and which three core columns must it contain?

## Q0210  _expands Q0084_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to db/h2/schema.sql vets, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0084, so it remains tied to that exact PetClinic decision.

## Q0211  _expands Q0084 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by db/h2/schema.sql vets. Which related file—application.properties—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0084, not by a generic file-order rule.

## Q0212  _preserved from Q0085_

Owner and veterinarian search benefits from indexing last-name lookups. Which veterinarian column should receive an index?

## Q0213  _expands Q0085_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in db/h2/schema.sql vets index before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0085, so it remains tied to that exact PetClinic decision.

## Q0214  _expands Q0085 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in db/h2/schema.sql vets index exposes a missing or inconsistent contract in db/h2/data.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0085, not by a generic file-order rule.

## Q0215  _preserved from Q0086_

Specialties such as dentistry are named lookup records. Which table should hold specialties and what reusable name field does it need?

## Q0216  _expands Q0086_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing db/h2/schema.sql specialties, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0086, so it remains tied to that exact PetClinic decision.

## Q0217  _expands Q0086 · file revisit_

Real development now requires a file jump: the change in db/h2/schema.sql specialties has a contract with application.properties, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to db/h2/schema.sql specialties? This revisit is triggered specifically by legacy build step Q0086, not by a generic file-order rule.

## Q0218  _preserved from Q0087_

A veterinarian can have many specialties and one specialty can belong to many veterinarians. Which junction table should represent that many-to-many relationship?

## Q0219  _expands Q0087_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in db/h2/schema.sql vet_specialties, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0087, so it remains tied to that exact PetClinic decision.

## Q0220  _expands Q0087 · file revisit_

PetClinic features cross layers, so finishing db/h2/schema.sql vet_specialties in isolation would be artificial. Because the next dependency is represented in db/h2/data.sql, which file should IntelliJ navigate to now for the supporting change before we come back to db/h2/schema.sql vet_specialties? This revisit is triggered specifically by legacy build step Q0087, not by a generic file-order rule.

## Q0221  _preserved from Q0088_

Junction rows must reference valid veterinarians. Which foreign key should vet_specialties define for vet_id?

## Q0222  _expands Q0088_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in db/h2/schema.sql vet_specialties FK, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0088, so it remains tied to that exact PetClinic decision.

## Q0223  _expands Q0088 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in db/h2/schema.sql vet_specialties FK relies on behavior or metadata in application.properties; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0088, not by a generic file-order rule.

## Q0224  _preserved from Q0089_

Junction rows must also reference valid specialties. Which foreign key should vet_specialties define for specialty_id?

## Q0225  _expands Q0089_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to db/h2/schema.sql vet_specialties FK, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0089, so it remains tied to that exact PetClinic decision.

## Q0226  _expands Q0089 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by db/h2/schema.sql vet_specialties FK. Which related file—db/h2/data.sql—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0089, not by a generic file-order rule.

## Q0227  _preserved from Q0090_

Pet types such as cat and dog are stored as reusable lookup data. Which table should hold pet types?

## Q0228  _expands Q0090_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in db/h2/schema.sql types before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0090, so it remains tied to that exact PetClinic decision.

## Q0229  _expands Q0090 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in db/h2/schema.sql types exposes a missing or inconsistent contract in application.properties, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0090, not by a generic file-order rule.

## Q0230  _preserved from Q0091_

Owners inherit personal names and add address, city, and telephone. Which table should hold owner records and these contact fields?

## Q0231  _expands Q0091_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing db/h2/schema.sql owners, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0091, so it remains tied to that exact PetClinic decision.

## Q0232  _expands Q0091 · file revisit_

Real development now requires a file jump: the change in db/h2/schema.sql owners has a contract with db/h2/data.sql, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to db/h2/schema.sql owners? This revisit is triggered specifically by legacy build step Q0091, not by a generic file-order rule.

## Q0233  _preserved from Q0092_

Owner search is implemented by last-name prefix queries. Which owners column should receive an index to support that lookup?

## Q0234  _expands Q0092_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in db/h2/schema.sql owners index, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0092, so it remains tied to that exact PetClinic decision.

## Q0235  _expands Q0092 · file revisit_

PetClinic features cross layers, so finishing db/h2/schema.sql owners index in isolation would be artificial. Because the next dependency is represented in application.properties, which file should IntelliJ navigate to now for the supporting change before we come back to db/h2/schema.sql owners index? This revisit is triggered specifically by legacy build step Q0092, not by a generic file-order rule.

## Q0236  _preserved from Q0093_

Each pet has a name, birth date, type, and owner. Which table and columns should represent those facts?

## Q0237  _expands Q0093_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in db/h2/schema.sql pets, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0093, so it remains tied to that exact PetClinic decision.

## Q0238  _expands Q0093 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in db/h2/schema.sql pets relies on behavior or metadata in db/h2/data.sql; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0093, not by a generic file-order rule.

## Q0239  _preserved from Q0094_

A pet must point to a valid type record. Which foreign key should connect pets.type_id to the types table?

## Q0240  _expands Q0094_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to db/h2/schema.sql pets FK, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0094, so it remains tied to that exact PetClinic decision.

## Q0241  _expands Q0094 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by db/h2/schema.sql pets FK. Which related file—application.properties—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0094, not by a generic file-order rule.

## Q0242  _preserved from Q0095_

Pets belong to owners. Which foreign key should connect pets.owner_id to the owners table?

## Q0243  _expands Q0095_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in db/h2/schema.sql pets FK before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0095, so it remains tied to that exact PetClinic decision.

## Q0244  _expands Q0095 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in db/h2/schema.sql pets FK exposes a missing or inconsistent contract in db/h2/data.sql, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0095, not by a generic file-order rule.

## Q0245  _preserved from Q0096_

Within one owner, two pets should not share the same name in the canonical project. Which composite unique constraint should enforce owner-scoped pet-name uniqueness?

## Q0246  _expands Q0096_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing db/h2/schema.sql pets unique, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0096, so it remains tied to that exact PetClinic decision.

## Q0247  _expands Q0096 · file revisit_

Real development now requires a file jump: the change in db/h2/schema.sql pets unique has a contract with application.properties, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to db/h2/schema.sql pets unique? This revisit is triggered specifically by legacy build step Q0096, not by a generic file-order rule.

## Q0248  _preserved from Q0097_

Visits belong to pets and include a date and description. Which table should represent visits and which business columns should it include?

## Q0249  _expands Q0097_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in db/h2/schema.sql visits, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0097, so it remains tied to that exact PetClinic decision.

## Q0250  _expands Q0097 · file revisit_

PetClinic features cross layers, so finishing db/h2/schema.sql visits in isolation would be artificial. Because the next dependency is represented in db/h2/data.sql, which file should IntelliJ navigate to now for the supporting change before we come back to db/h2/schema.sql visits? This revisit is triggered specifically by legacy build step Q0097, not by a generic file-order rule.

## Q0251  _preserved from Q0098_

Every visit should reference its pet. Which foreign key should link visits.pet_id to pets.id?

## Q0252  _expands Q0098_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in db/h2/schema.sql visits FK, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0098, so it remains tied to that exact PetClinic decision.

## Q0253  _expands Q0098 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in db/h2/schema.sql visits FK relies on behavior or metadata in application.properties; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0098, not by a generic file-order rule.

## Q0254  _preserved from Q0099_

Visit lookup by pet is common when rendering owner details. Which visits column should receive an index?

## Q0255  _expands Q0099_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to db/h2/schema.sql visits index, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0099, so it remains tied to that exact PetClinic decision.

## Q0256  _expands Q0099 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by db/h2/schema.sql visits index. Which related file—db/h2/data.sql—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0099, not by a generic file-order rule.

## Q0257  _preserved from Q0100_

A demo application is easier to verify when it starts with representative owners, pets, vets, types, specialties, and visits. Which companion SQL file should contain initial rows after the schema is created?

## Q0258  _expands Q0100_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/main/resources/db/h2/data.sql, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0100, so it remains tied to that exact PetClinic decision.

## Q0259  _expands Q0100 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/resources/db/h2/data.sql exposes a missing or inconsistent contract in application.properties, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0100, not by a generic file-order rule.

## Q0260  _preserved from Q0101_

Seed data must respect foreign-key order so referenced rows exist before dependent rows. Should lookup and parent records be inserted before pets, visits, and veterinarian-specialty junction rows?

## Q0261  _expands Q0101_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing db/h2/data.sql, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0101, so it remains tied to that exact PetClinic decision.

## Q0262  _expands Q0101 · file revisit_

Real development now requires a file jump: the change in db/h2/data.sql has a contract with db/h2/schema.sql, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to db/h2/data.sql? This revisit is triggered specifically by legacy build step Q0101, not by a generic file-order rule.
