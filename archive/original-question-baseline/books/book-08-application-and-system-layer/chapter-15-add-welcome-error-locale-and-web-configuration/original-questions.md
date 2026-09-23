# Chapter 15 — Add welcome, error, locale, and web configuration

Detailed sequence questions in this chapter: **45**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0719  _preserved from Q0254_

The root URL needs a controller that selects the welcome template. Which small controller should we create for GET /?

## Q0720  _expands Q0254_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0254, so it remains tied to that exact PetClinic decision.

## Q0721  _expands Q0254 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java. Which related file—templates/welcome.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0254, not by a generic file-order rule.

## Q0722  _preserved from Q0255_

Spring MVC maps GET requests with @GetMapping. Which mapping should the welcome handler declare?

## Q0723  _expands Q0255_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0255, so it remains tied to that exact PetClinic decision.

## Q0724  _expands Q0255 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java exposes a missing or inconsistent contract in templates/error.html, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0255, not by a generic file-order rule.

## Q0725  _preserved from Q0256_

The welcome handler returns a logical view name, not raw HTML. Which view name should it return?

## Q0726  _expands Q0256_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0256, so it remains tied to that exact PetClinic decision.

## Q0727  _expands Q0256 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java has a contract with CrashController.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/system/WelcomeController.java? This revisit is triggered specifically by legacy build step Q0256, not by a generic file-order rule.

## Q0728  _preserved from Q0257_

PetClinic intentionally includes an endpoint that throws an exception so the error page can be demonstrated. Which controller should we create for that behavior?

## Q0729  _expands Q0257_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/java/org/springframework/samples/petclinic/system/CrashController.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0257, so it remains tied to that exact PetClinic decision.

## Q0730  _expands Q0257 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/system/CrashController.java in isolation would be artificial. Because the next dependency is represented in WebConfiguration.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/system/CrashController.java? This revisit is triggered specifically by legacy build step Q0257, not by a generic file-order rule.

## Q0731  _preserved from Q0258_

The demonstration error route is /oups. Which GET mapping should trigger the intentional exception?

## Q0732  _expands Q0258_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/system/CrashController.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0258, so it remains tied to that exact PetClinic decision.

## Q0733  _expands Q0258 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/system/CrashController.java relies on behavior or metadata in messages/messages.properties; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0258, not by a generic file-order rule.

## Q0734  _preserved from Q0259_

Throwing a RuntimeException allows Spring Boot’s error handling to render the configured error view. What should the crash handler do instead of returning a normal view?

## Q0735  _expands Q0259_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/system/CrashController.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0259, so it remains tied to that exact PetClinic decision.

## Q0736  _expands Q0259 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/system/CrashController.java. Which related file—templates/welcome.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0259, not by a generic file-order rule.

## Q0737  _preserved from Q0260_

PetClinic supports changing language through a query parameter such as ?lang=de. Which web configuration class should we create for internationalization?

## Q0738  _expands Q0260_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0260, so it remains tied to that exact PetClinic decision.

## Q0739  _expands Q0260 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java exposes a missing or inconsistent contract in templates/error.html, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0260, not by a generic file-order rule.

## Q0740  _preserved from Q0261_

Custom MVC configuration can be added without taking over all Spring Boot MVC auto-configuration. Which interface should WebConfiguration implement?

## Q0741  _expands Q0261_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0261, so it remains tied to that exact PetClinic decision.

## Q0742  _expands Q0261 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java has a contract with WelcomeController.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java? This revisit is triggered specifically by legacy build step Q0261, not by a generic file-order rule.

## Q0743  _preserved from Q0262_

A LocaleResolver decides which locale applies to each request. Which session-based resolver should be exposed as a bean?

## Q0744  _expands Q0262_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0262, so it remains tied to that exact PetClinic decision.

## Q0745  _expands Q0262 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java in isolation would be artificial. Because the next dependency is represented in CrashController.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java? This revisit is triggered specifically by legacy build step Q0262, not by a generic file-order rule.

## Q0746  _preserved from Q0263_

English is the default when no user language has been chosen. Which default locale should the resolver set?

## Q0747  _expands Q0263_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0263, so it remains tied to that exact PetClinic decision.

## Q0748  _expands Q0263 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java relies on behavior or metadata in messages/messages.properties; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0263, not by a generic file-order rule.

## Q0749  _preserved from Q0264_

A LocaleChangeInterceptor watches a request parameter and switches locale. Which interceptor bean should we create?

## Q0750  _expands Q0264_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0264, so it remains tied to that exact PetClinic decision.

## Q0751  _expands Q0264 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java. Which related file—templates/welcome.html—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0264, not by a generic file-order rule.

## Q0752  _preserved from Q0265_

The project uses lang as the locale-switching query parameter. Which parameter name should the interceptor watch?

## Q0753  _expands Q0265_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0265, so it remains tied to that exact PetClinic decision.

## Q0754  _expands Q0265 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java exposes a missing or inconsistent contract in templates/error.html, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0265, not by a generic file-order rule.

## Q0755  _preserved from Q0266_

Defining an interceptor bean is not enough; MVC must register it. Which WebMvcConfigurer method should add the locale interceptor to the registry?

## Q0756  _expands Q0266_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0266, so it remains tied to that exact PetClinic decision.

## Q0757  _expands Q0266 · file revisit_

Real development now requires a file jump: the change in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java has a contract with WelcomeController.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java? This revisit is triggered specifically by legacy build step Q0266, not by a generic file-order rule.

## Q0758  _preserved from Q0267_

Configuration classes are discovered by component scanning. Which class-level annotation should WebConfiguration use?

## Q0759  _expands Q0267_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0267, so it remains tied to that exact PetClinic decision.

## Q0760  _expands Q0267 · file revisit_

PetClinic features cross layers, so finishing src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java in isolation would be artificial. Because the next dependency is represented in CrashController.java, which file should IntelliJ navigate to now for the supporting change before we come back to src/main/java/org/springframework/samples/petclinic/system/WebConfiguration.java? This revisit is triggered specifically by legacy build step Q0267, not by a generic file-order rule.

## Q0761  _preserved from Q0268_

Package-level documentation files help describe architectural packages without executable logic. Where should package-info.java files be added for root, model, owner, system, and vet packages?

## Q0762  _expands Q0268_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/main/java/org/springframework/samples/petclinic/**/package-info.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0268, so it remains tied to that exact PetClinic decision.

## Q0763  _expands Q0268 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in src/main/java/org/springframework/samples/petclinic/**/package-info.java relies on behavior or metadata in messages/messages.properties; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0268, not by a generic file-order rule.
