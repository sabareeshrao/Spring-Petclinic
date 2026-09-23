# Chapter 22 — Test domain rules, validators, and repository-adjacent behavior

Detailed sequence questions in this chapter: **24**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0937  _preserved from Q0344_

Unit tests should verify domain helpers independently of the browser. Which test class should cover Owner aggregate behavior?

## Q0938  _expands Q0344_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/OwnerTests.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0344, so it remains tied to that exact PetClinic decision.

## Q0939  _preserved from Q0345_

Owner.addPet should ignore null and avoid duplicate persistent entries. Which cases should OwnerTests exercise for pet aggregation?

## Q0940  _expands Q0345_

When a test fails, the useful signal is the first assertion or application exception, not the cascade that follows. Which part of the IntelliJ test runner should you inspect first for src/test/java/org/springframework/samples/petclinic/OwnerTests.java before changing production code? This micro-check belongs specifically to legacy build step Q0345, so it remains tied to that exact PetClinic decision.

## Q0941  _preserved from Q0346_

Validation behavior deserves focused tests because form correctness depends on it. Which test class should cover PetValidator?

## Q0942  _expands Q0346_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/test/java/org/springframework/samples/petclinic/PetValidatorTests.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0346, so it remains tied to that exact PetClinic decision.

## Q0943  _preserved from Q0347_

PetValidator has separate rules for blank name, excessive name length, missing type, and missing birth date. Which invalid cases should validator tests cover individually?

## Q0944  _expands Q0347_

Fast feedback comes from running a focused test first and the full build later. Which focused test execution should validate src/test/java/org/springframework/samples/petclinic/PetValidatorTests.java before we spend time on every PetClinic test? This micro-check belongs specifically to legacy build step Q0347, so it remains tied to that exact PetClinic decision.

## Q0945  _preserved from Q0348_

PetTypeFormatter should print names and parse known types. Which test class should verify formatting behavior?

## Q0946  _expands Q0348_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/PetTypeFormatterTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0348, so it remains tied to that exact PetClinic decision.

## Q0947  _preserved from Q0349_

Formatter parse must fail for an unknown type. Which negative case should the formatter tests include?

## Q0948  _expands Q0349_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/PetTypeFormatterTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0349, so it remains tied to that exact PetClinic decision.

## Q0949  _preserved from Q0350_

General Bean Validation constraints on model objects can be checked without starting the full web layer. Which test class should exercise Jakarta validation annotations across entities?

## Q0950  _expands Q0350_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/ValidatorTests.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0350, so it remains tied to that exact PetClinic decision.

## Q0951  _preserved from Q0351_

Vet specialty behavior includes sorted output and specialty count. Which test class should cover Vet domain helpers?

## Q0952  _expands Q0351_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/VetTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0351, so it remains tied to that exact PetClinic decision.

## Q0953  _preserved from Q0352_

A small EntityUtils helper can locate entities by ID inside collections during tests. Which test utility should be created for reusable entity lookup?

## Q0954  _expands Q0352_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/test/java/org/springframework/samples/petclinic/service/EntityUtils.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0352, so it remains tied to that exact PetClinic decision.

## Q0955  _preserved from Q0353_

Service-level persistence tests can verify owners, pets, visits, vets, and pet types work together. Which broader test class should cover clinic repository interactions?

## Q0956  _expands Q0353_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/service/ClinicServiceTests.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0353, so it remains tied to that exact PetClinic decision.

## Q0957  _preserved from Q0354_

Database tests should verify expected seed data as well as write behavior. What balance of read assertions and persistence changes should ClinicServiceTests include?

## Q0958  _expands Q0354_

When a test fails, the useful signal is the first assertion or application exception, not the cascade that follows. Which part of the IntelliJ test runner should you inspect first for src/test/java/org/springframework/samples/petclinic/service/ClinicServiceTests.java before changing production code? This micro-check belongs specifically to legacy build step Q0354, so it remains tied to that exact PetClinic decision.

## Q0959  _preserved from Q0355_

Tests should cleanly fail when repository contracts change unexpectedly. Should repository-oriented tests assert both returned content and important ordering/pagination behavior?

## Q0960  _expands Q0355_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/service/ClinicServiceTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0355, so it remains tied to that exact PetClinic decision.
