# Chapter 14 — Expose veterinarian pages, data, and caching

Detailed sequence questions in this chapter: **42**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0677  _preserved from Q0240_

VetController serves both an HTML page and a response-body representation. Which Spring stereotype should mark the controller?

## Q0678  _expands Q0240_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/vet/VetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0240, so it remains tied to that exact PetClinic decision.

## Q0679  _expands Q0240 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/vet/VetController.java exposes a missing or inconsistent contract in templates/vets/vetList.html, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0240, not by a generic file-order rule.

## Q0680  _preserved from Q0241_

The controller should obtain data through VetRepository. Which dependency should its constructor inject?

## Q0681  _expands Q0241_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/vet/VetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0241, so it remains tied to that exact PetClinic decision.

## Q0682  _expands Q0241 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/vet/VetController.java has a contract with VetRepository.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/vet/VetController.java? This revisit is triggered specifically by legacy build step Q0241, not by a generic file-order rule.

## Q0683  _preserved from Q0242_

The HTML list is requested from /vets.html and defaults to page 1. Which GET mapping and request parameter should the page handler use?

## Q0684  _expands Q0242_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/vet/VetController.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0242, so it remains tied to that exact PetClinic decision.

## Q0685  _expands Q0242 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/vet/VetController.java in isolation would be artificial. Because the next dependency is represented in Vets.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/vet/VetController.java? This revisit is triggered specifically by legacy build step Q0242, not by a generic file-order rule.

## Q0686  _preserved from Q0243_

The target page size is five veterinarians. Which PageRequest size should the pagination helper use?

## Q0687  _expands Q0243_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/vet/VetController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0243, so it remains tied to that exact PetClinic decision.

## Q0688  _expands Q0243 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/vet/VetController.java relies on behavior or metadata in CacheConfiguration.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0243, not by a generic file-order rule.

## Q0689  _preserved from Q0244_

Thymeleaf pagination needs current page, total pages, total items, and the page content. Which model attributes should the controller add?

## Q0690  _expands Q0244_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/vet/VetController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0244, so it remains tied to that exact PetClinic decision.

## Q0691  _expands Q0244 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/vet/VetController.java. Which related file—templates/vets/vetList.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0244, not by a generic file-order rule.

## Q0692  _preserved from Q0245_

The veterinarian HTML view lives under templates/vets. Which view name should the list handler return?

## Q0693  _expands Q0245_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/vet/VetController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0245, so it remains tied to that exact PetClinic decision.

## Q0694  _expands Q0245 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/vet/VetController.java exposes a missing or inconsistent contract in VetRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0245, not by a generic file-order rule.

## Q0695  _preserved from Q0246_

The /vets endpoint returns serialized data instead of a Thymeleaf view. Which response annotation should distinguish it from the HTML handler?

## Q0696  _expands Q0246_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/vet/VetController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0246, so it remains tied to that exact PetClinic decision.

## Q0697  _expands Q0246 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/vet/VetController.java has a contract with Vets.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/vet/VetController.java? This revisit is triggered specifically by legacy build step Q0246, not by a generic file-order rule.

## Q0698  _preserved from Q0247_

Serializing a wrapper object makes XML/JSON mapping simpler than returning a raw collection in this project. Which wrapper class should we create for the veterinarian list?

## Q0699  _expands Q0247_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/main/java/org/springframework/samples/petclinic/vet/Vets.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0247, so it remains tied to that exact PetClinic decision.

## Q0700  _expands Q0247 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/vet/Vets.java in isolation would be artificial. Because the next dependency is represented in CacheConfiguration.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/vet/Vets.java? This revisit is triggered specifically by legacy build step Q0247, not by a generic file-order rule.

## Q0701  _preserved from Q0248_

The Vets wrapper should lazily create its internal list so callers can always add items. What behavior should getVetList provide?

## Q0702  _expands Q0248_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/vet/Vets.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0248, so it remains tied to that exact PetClinic decision.

## Q0703  _expands Q0248 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/vet/Vets.java relies on behavior or metadata in templates/vets/vetList.html; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0248, not by a generic file-order rule.

## Q0704  _preserved from Q0249_

XML binding needs a root element around the list. Which JAXB annotation should mark Vets?

## Q0705  _expands Q0249_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/vet/Vets.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0249, so it remains tied to that exact PetClinic decision.

## Q0706  _expands Q0249 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/vet/Vets.java. Which related file—VetController.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0249, not by a generic file-order rule.

## Q0707  _preserved from Q0250_

Caching must be explicitly enabled in the Spring context. Which configuration annotation should activate Spring caching?

## Q0708  _expands Q0250_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0250, so it remains tied to that exact PetClinic decision.

## Q0709  _expands Q0250 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java exposes a missing or inconsistent contract in VetRepository.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0250, not by a generic file-order rule.

## Q0710  _preserved from Q0251_

PetClinic configures JCache rather than hard-coding Caffeine APIs in repository code. Which customizer bean type should the cache configuration expose?

## Q0711  _expands Q0251_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0251, so it remains tied to that exact PetClinic decision.

## Q0712  _expands Q0251 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java has a contract with Vets.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java? This revisit is triggered specifically by legacy build step Q0251, not by a generic file-order rule.

## Q0713  _preserved from Q0252_

The repository references a cache named vets, so that cache must exist at startup. Which cache should the customizer create?

## Q0714  _expands Q0252_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0252, so it remains tied to that exact PetClinic decision.

## Q0715  _expands Q0252 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java in isolation would be artificial. Because the next dependency is represented in templates/vets/vetList.html, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java? This revisit is triggered specifically by legacy build step Q0252, not by a generic file-order rule.

## Q0716  _preserved from Q0253_

Cache statistics are useful for monitoring through JMX. Which setting should the JCache MutableConfiguration enable?

## Q0717  _expands Q0253_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0253, so it remains tied to that exact PetClinic decision.

## Q0718  _expands Q0253 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/system/CacheConfiguration.java relies on behavior or metadata in VetController.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0253, not by a generic file-order rule.
