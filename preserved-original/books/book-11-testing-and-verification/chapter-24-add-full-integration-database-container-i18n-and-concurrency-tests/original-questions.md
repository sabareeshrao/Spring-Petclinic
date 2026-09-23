# Chapter 24 — Add full integration, database-container, i18n, and concurrency tests

Detailed sequence questions in this chapter: **24**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0993  _preserved from Q0372_

A full Spring context test confirms that configuration, repositories, controllers, templates, and H2 startup work together. Which integration test class should load the default application context?

## Q0994  _expands Q0372_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/PetClinicIntegrationTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0372, so it remains tied to that exact PetClinic decision.

## Q0995  _preserved from Q0373_

MySQL behavior should be tested against a real database engine rather than assuming H2 equivalence. Which Testcontainers-backed integration test should activate the MySQL profile?

## Q0996  _expands Q0373_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating src/test/java/org/springframework/samples/petclinic/MySqlIntegrationTests.java, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0373, so it remains tied to that exact PetClinic decision.

## Q0997  _preserved from Q0374_

A helper test application can wire Docker/Testcontainers-specific database details for MySQL tests. Which supporting test application class should be created?

## Q0998  _expands Q0374_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/MysqlTestApplication.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0374, so it remains tied to that exact PetClinic decision.

## Q0999  _preserved from Q0375_

PostgreSQL also deserves a profile-specific integration path. Which test class should activate and verify the PostgreSQL profile?

## Q1000  _expands Q0375_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/PostgresIntegrationTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0375, so it remains tied to that exact PetClinic decision.

## Q1001  _preserved from Q0376_

Testcontainers should publish container connection details into Spring automatically where supported. Which Spring Boot test integration should connect container service details to the application?

## Q1002  _expands Q0376_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by Integration test configuration, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0376, so it remains tied to that exact PetClinic decision.

## Q1003  _preserved from Q0377_

Message bundles across languages should expose a compatible key set. Which system test should compare i18n properties files for synchronization?

## Q1004  _expands Q0377_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/test/java/org/springframework/samples/petclinic/system/I18nPropertiesSyncTest.java, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0377, so it remains tied to that exact PetClinic decision.

## Q1005  _preserved from Q0378_

A web application can fail under concurrent access even when single-request tests pass. Which test class should exercise PetClinic concurrency behavior?

## Q1006  _expands Q0378_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/test/java/org/springframework/samples/petclinic/PetClinicConcurrencyTests.java, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0378, so it remains tied to that exact PetClinic decision.

## Q1007  _preserved from Q0379_

Concurrent tests should focus on operations where shared persistence state or cache behavior could race. Which kinds of owner/pet or read operations should be stressed rather than only starting the context?

## Q1008  _expands Q0379_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by src/test/java/org/springframework/samples/petclinic/PetClinicConcurrencyTests.java, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0379, so it remains tied to that exact PetClinic decision.

## Q1009  _preserved from Q0380_

Integration tests should verify profiles start with their own schema/data scripts. What should MySQL and PostgreSQL tests assert beyond simple container startup?

## Q1010  _expands Q0380_

Fast feedback comes from running a focused test first and the full build later. Which focused test execution should validate Integration tests before we spend time on every PetClinic test? This micro-check belongs specifically to legacy build step Q0380, so it remains tied to that exact PetClinic decision.

## Q1011  _preserved from Q0381_

The application exposes Actuator endpoints during development. Should an integration test verify the application context can expose management endpoints without breaking normal MVC routes?

## Q1012  _expands Q0381_

When a test fails, the useful signal is the first assertion or application exception, not the cascade that follows. Which part of the IntelliJ test runner should you inspect first for Integration tests before changing production code? This micro-check belongs specifically to legacy build step Q0381, so it remains tied to that exact PetClinic decision.

## Q1013  _preserved from Q0382_

Tests should remain isolated so one database mutation does not unpredictably affect another test. Which isolation strategy should we apply through rollback, fresh context, or container lifecycle where appropriate?

## Q1014  _expands Q0382_

A test only protects behavior when we can run the narrowest relevant scope quickly during development. After adding or changing the behavior represented by Integration tests, which IntelliJ test-run action should execute the nearest test class or method before the full suite? This micro-check belongs specifically to legacy build step Q0382, so it remains tied to that exact PetClinic decision.

## Q1015  _preserved from Q0383_

A successful integration suite should run from the same build command used in CI. Which Maven lifecycle command should we use to exercise verification before considering the build complete?

## Q1016  _expands Q0383_

A successful command should leave observable evidence rather than just returning to a prompt. After running the operation for Terminal, which exit status or application/build message should be checked before moving forward? This micro-check belongs specifically to legacy build step Q0383, so it remains tied to that exact PetClinic decision.
