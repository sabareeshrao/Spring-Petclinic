# Chapter 4 — Create the application entry point and runtime hints

Detailed sequence questions in this chapter: **30**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0149  _preserved from Q0060_

Java source for the root application belongs under src/main/java using the base package path. Which directory path should contain PetClinicApplication.java?

## Q0150  _expands Q0060_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/java/org/springframework/samples/petclinic/PetClinicApplication.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0060, so it remains tied to that exact PetClinic decision.

## Q0151  _expands Q0060 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/PetClinicApplication.java exposes a missing or inconsistent contract in pom.xml, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0060, not by a generic file-order rule.

## Q0152  _preserved from Q0061_

@SpringBootApplication combines configuration, component scanning, and auto-configuration. Which annotation should mark the PetClinicApplication class?

## Q0153  _expands Q0061_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing PetClinicApplication.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0061, so it remains tied to that exact PetClinic decision.

## Q0154  _expands Q0061 · file revisit_

Real development now requires a file jump: the change in PetClinicApplication.java has a contract with PetClinicRuntimeHints.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to PetClinicApplication.java? This revisit is triggered specifically by legacy build step Q0061, not by a generic file-order rule.

## Q0155  _preserved from Q0062_

Every executable Java application needs a main method as its entry point. Which method signature should PetClinicApplication expose so the JVM can launch it?

## Q0156  _expands Q0062_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in PetClinicApplication.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0062, so it remains tied to that exact PetClinic decision.

## Q0157  _expands Q0062 · file revisit_

PetClinic features cross layers, so finishing PetClinicApplication.java in isolation would be artificial. Because the next dependency is represented in pom.xml, which file should IntelliJ navigate to now for the supporting change before we come back to PetClinicApplication.java? This revisit is triggered specifically by legacy build step Q0062, not by a generic file-order rule.

## Q0158  _preserved from Q0063_

SpringApplication.run bootstraps the Spring context and embedded web server. Which Spring Boot call should the main method make to start PetClinicApplication?

## Q0159  _expands Q0063_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in PetClinicApplication.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0063, so it remains tied to that exact PetClinic decision.

## Q0160  _expands Q0063 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in PetClinicApplication.java relies on behavior or metadata in PetClinicRuntimeHints.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0063, not by a generic file-order rule.

## Q0161  _preserved from Q0064_

Native images need explicit runtime hints for resources and reflection that cannot be discovered automatically. Which supporting class should we create to register PetClinic-specific runtime hints?

## Q0162  _expands Q0064_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating PetClinicRuntimeHints.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0064, so it remains tied to that exact PetClinic decision.

## Q0163  _expands Q0064 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by PetClinicRuntimeHints.java. Which related file—pom.xml—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0064, not by a generic file-order rule.

## Q0164  _preserved from Q0065_

RuntimeHintsRegistrar is Spring AOT’s extension point for custom runtime hints. Which interface should PetClinicRuntimeHints implement?

## Q0165  _expands Q0065_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in PetClinicRuntimeHints.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0065, so it remains tied to that exact PetClinic decision.

## Q0166  _expands Q0065 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in PetClinicRuntimeHints.java exposes a missing or inconsistent contract in PetClinicApplication.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0065, not by a generic file-order rule.

## Q0167  _preserved from Q0066_

@ImportRuntimeHints connects a runtime-hints registrar to application configuration. Which annotation should PetClinicApplication use to import PetClinicRuntimeHints?

## Q0168  _expands Q0066_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing PetClinicApplication.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0066, so it remains tied to that exact PetClinic decision.

## Q0169  _expands Q0066 · file revisit_

Real development now requires a file jump: the change in PetClinicApplication.java has a contract with pom.xml, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to PetClinicApplication.java? This revisit is triggered specifically by legacy build step Q0066, not by a generic file-order rule.

## Q0170  _preserved from Q0067_

Database SQL resources live below db and must remain reachable in native images. Which resource pattern family should the runtime hints register for database files?

## Q0171  _expands Q0067_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in PetClinicRuntimeHints.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0067, so it remains tied to that exact PetClinic decision.

## Q0172  _expands Q0067 · file revisit_

PetClinic features cross layers, so finishing PetClinicRuntimeHints.java in isolation would be artificial. Because the next dependency is represented in PetClinicApplication.java, which file should IntelliJ navigate to now for the supporting change before we come back to PetClinicRuntimeHints.java? This revisit is triggered specifically by legacy build step Q0067, not by a generic file-order rule.

## Q0173  _preserved from Q0068_

Localized messages live below messages and must be packaged for runtime lookup. Which resource path family should runtime hints register for message bundles?

## Q0174  _expands Q0068_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in PetClinicRuntimeHints.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0068, so it remains tied to that exact PetClinic decision.

## Q0175  _expands Q0068 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in PetClinicRuntimeHints.java relies on behavior or metadata in pom.xml; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0068, not by a generic file-order rule.

## Q0176  _preserved from Q0069_

Some domain types participate in Java serialization and may require reflection metadata in native mode. Which base/domain types should be considered for reflection serialization hints before building a native image?

## Q0177  _expands Q0069_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to PetClinicRuntimeHints.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0069, so it remains tied to that exact PetClinic decision.

## Q0178  _expands Q0069 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by PetClinicRuntimeHints.java. Which related file—PetClinicApplication.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0069, not by a generic file-order rule.
