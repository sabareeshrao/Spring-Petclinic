# Chapter 23 — Test controller routes and MVC behavior

Detailed sequence questions in this chapter: **32**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0961  _preserved from Q0356_

MockMvc can test Spring MVC routing, validation, model attributes, views, and redirects without launching a real browser. Which test class should focus on OwnerController?

## Q0962  _expands Q0356_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0356, so it remains tied to that exact PetClinic decision.

## Q0963  _preserved from Q0357_

Owner controller tests should verify new-form GET behavior. Which view and model expectations should the creation-form test assert?

## Q0964  _expands Q0357_

When a test fails, the useful signal is the first assertion or application exception, not the cascade that follows. Which part of the IntelliJ test runner should you inspect first for src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java before changing production code? This micro-check belongs specifically to legacy build step Q0357, so it remains tied to that exact PetClinic decision.

## Q0965  _preserved from Q0358_

Owner creation should redisplay invalid submissions and redirect valid submissions. Which two paths should the POST creation tests cover?

## Q0966  _expands Q0358_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0358, so it remains tied to that exact PetClinic decision.

## Q0967  _preserved from Q0359_

Owner search has zero, one, and many-result branches. Which three result shapes should processFindForm tests exercise?

## Q0968  _expands Q0359_

Fast feedback comes from running a focused test first and the full build later. Which focused test execution should validate src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java before we spend time on every PetClinic test? This micro-check belongs specifically to legacy build step Q0359, so it remains tied to that exact PetClinic decision.

## Q0969  _preserved from Q0360_

Owner editing protects URL/form ID consistency. Which mismatch case should update tests include?

## Q0970  _expands Q0360_

When a test fails, the useful signal is the first assertion or application exception, not the cascade that follows. Which part of the IntelliJ test runner should you inspect first for src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java before changing production code? This micro-check belongs specifically to legacy build step Q0360, so it remains tied to that exact PetClinic decision.

## Q0971  _preserved from Q0361_

Owner details should produce the correct template with the loaded owner. Which GET route should the detail test invoke?

## Q0972  _expands Q0361_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/owner/OwnerControllerTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0361, so it remains tied to that exact PetClinic decision.

## Q0973  _preserved from Q0362_

PetController has custom validators, duplicate-name handling, and date rules. Which test class should focus on pet routes?

## Q0974  _expands Q0362_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/owner/PetControllerTests.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0362, so it remains tied to that exact PetClinic decision.

## Q0975  _preserved from Q0363_

Pet creation should reject a future birth date. Which invalid submission should a controller test send?

## Q0976  _expands Q0363_

When a test fails, the useful signal is the first assertion or application exception, not the cascade that follows. Which part of the IntelliJ test runner should you inspect first for src/test/java/org/springframework/samples/petclinic/owner/PetControllerTests.java before changing production code? This micro-check belongs specifically to legacy build step Q0363, so it remains tied to that exact PetClinic decision.

## Q0977  _preserved from Q0364_

Pet creation should reject a duplicate name within the same owner. Which owner fixture condition should the duplicate-name test prepare?

## Q0978  _expands Q0364_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/owner/PetControllerTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0364, so it remains tied to that exact PetClinic decision.

## Q0979  _preserved from Q0365_

Pet editing must allow unchanged names but reject collisions with a different pet. Which two update cases should the tests distinguish?

## Q0980  _expands Q0365_

Fast feedback comes from running a focused test first and the full build later. Which focused test execution should validate src/test/java/org/springframework/samples/petclinic/owner/PetControllerTests.java before we spend time on every PetClinic test? This micro-check belongs specifically to legacy build step Q0365, so it remains tied to that exact PetClinic decision.

## Q0981  _preserved from Q0366_

VisitController requires a valid owner-pet relationship and future date. Which test class should cover visit booking?

## Q0982  _expands Q0366_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/owner/VisitControllerTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0366, so it remains tied to that exact PetClinic decision.

## Q0983  _preserved from Q0367_

The new-visit GET should expose visit, owner, pet, and minVisitDate model data. Which model attributes should the GET test assert?

## Q0984  _expands Q0367_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/owner/VisitControllerTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0367, so it remains tied to that exact PetClinic decision.

## Q0985  _preserved from Q0368_

Posting today or a past visit date should be rejected. Which boundary cases should visit tests include?

## Q0986  _expands Q0368_

Fast feedback comes from running a focused test first and the full build later. Which focused test execution should validate src/test/java/org/springframework/samples/petclinic/owner/VisitControllerTests.java before we spend time on every PetClinic test? This micro-check belongs specifically to legacy build step Q0368, so it remains tied to that exact PetClinic decision.

## Q0987  _preserved from Q0369_

VetController supports both HTML pagination and a response-body endpoint. Which test class should cover both representations?

## Q0988  _expands Q0369_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/vet/VetControllerTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0369, so it remains tied to that exact PetClinic decision.

## Q0989  _preserved from Q0370_

The home page controller is intentionally tiny but still part of routing. Which test class should verify GET / resolves to welcome?

## Q0990  _expands Q0370_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/test/java/org/springframework/samples/petclinic/system/WelcomeControllerTests.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0370, so it remains tied to that exact PetClinic decision.

## Q0991  _preserved from Q0371_

The crash endpoint exists to verify error behavior. Which controller and integration tests should cover the /oups path?

## Q0992  _expands Q0371_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/system/CrashControllerTests.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0371, so it remains tied to that exact PetClinic decision.
