# Book 10 — Databases and Runtime Profiles

> PRESERVED BASELINE: question wording below is copied unchanged from the 1,150-question source set. Do not edit or delete during rebuild work.

# Chapter 21 — Add MySQL, PostgreSQL, and local database containers

Detailed sequence questions in this chapter: **28**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0909  _preserved from Q0330_

Spring profiles allow the same application to switch database settings without changing Java code. Which profile-specific properties file should configure MySQL?

## Q0910  _expands Q0330_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/resources/application-mysql.properties, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0330, so it remains tied to that exact PetClinic decision.

## Q0911  _preserved from Q0331_

The MySQL profile selects database=mysql so shared SQL locations resolve into db/mysql. Which database identifier should the profile set?

## Q0912  _expands Q0331_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/application-mysql.properties, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0331, so it remains tied to that exact PetClinic decision.

## Q0913  _preserved from Q0332_

Database URLs and credentials should be overrideable by environment variables. Which fallback pattern should the MySQL datasource URL, user, and password follow?

## Q0914  _expands Q0332_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/application-mysql.properties, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0332, so it remains tied to that exact PetClinic decision.

## Q0915  _preserved from Q0333_

External databases need schema/data initialization enabled even though they are not embedded. Which SQL initialization mode should the MySQL profile use?

## Q0916  _expands Q0333_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/application-mysql.properties, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0333, so it remains tied to that exact PetClinic decision.

## Q0917  _preserved from Q0334_

MySQL needs dialect-appropriate schema and seed scripts. Which db/mysql files should mirror the H2 logical schema while using MySQL syntax?

## Q0918  _expands Q0334_

This build step changes src/main/resources/db/mysql, and incremental development works best when each change has a visible success condition. Which immediate check should confirm the action completed correctly before the next question? This micro-check belongs specifically to legacy build step Q0334, so it remains tied to that exact PetClinic decision.

## Q0919  _preserved from Q0335_

A separate PostgreSQL profile selects PostgreSQL connection settings. Which profile properties file should we create?

## Q0920  _expands Q0335_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/application-postgres.properties, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0335, so it remains tied to that exact PetClinic decision.

## Q0921  _preserved from Q0336_

The PostgreSQL profile should resolve shared SQL locations into db/postgres. Which database identifier should it set?

## Q0922  _expands Q0336_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/application-postgres.properties, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0336, so it remains tied to that exact PetClinic decision.

## Q0923  _preserved from Q0337_

PostgreSQL credentials should also be overrideable through environment variables. Which fallback pattern should URL, user, and password follow?

## Q0924  _expands Q0337_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/application-postgres.properties, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0337, so it remains tied to that exact PetClinic decision.

## Q0925  _preserved from Q0338_

PostgreSQL needs database-specific schema and data SQL. Which db/postgres files should be created?

## Q0926  _expands Q0338_

Before moving away from src/main/resources/db/postgres, which observable state should a developer verify so a later failure is not caused by an unnoticed mistake in this step? This micro-check belongs specifically to legacy build step Q0338, so it remains tied to that exact PetClinic decision.

## Q0927  _preserved from Q0339_

Docker Compose gives developers local database services without manual installation. Which root-level file should define MySQL and PostgreSQL services?

## Q0928  _expands Q0339_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating docker-compose.yml, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0339, so it remains tied to that exact PetClinic decision.

## Q0929  _preserved from Q0340_

The target Compose file exposes MySQL on 3306 and creates the petclinic database/user. Which port and environment values should the MySQL service provide?

## Q0930  _expands Q0340_

Infrastructure changes are useful only when their external state can be observed. After the step involving docker-compose.yml mysql, which command output, container state, workflow status, or service response should be checked before proceeding? This micro-check belongs specifically to legacy build step Q0340, so it remains tied to that exact PetClinic decision.

## Q0931  _preserved from Q0341_

The target Compose file exposes PostgreSQL on 5432 and creates the same logical petclinic database/user. Which port and environment values should the PostgreSQL service provide?

## Q0932  _expands Q0341_

Operational files are executable configuration: a typo often appears only when the tool parses or applies them. Which tool-specific validation should be run immediately after changing docker-compose.yml postgres? This micro-check belongs specifically to legacy build step Q0341, so it remains tied to that exact PetClinic decision.

## Q0933  _preserved from Q0342_

Running the application with the mysql profile should point at the MySQL service or localhost. Which Spring profile should be activated for a MySQL verification run?

## Q0934  _expands Q0342_

PetClinic uses project-local wrappers so contributors do not depend on a globally installed Maven or Gradle version. Which wrapper command context should be preferred when running the operation related to Run Configuration? This micro-check belongs specifically to legacy build step Q0342, so it remains tied to that exact PetClinic decision.

## Q0935  _preserved from Q0343_

Running with PostgreSQL should exercise the PostgreSQL schema and driver independently. Which Spring profile should be activated for a PostgreSQL verification run?

## Q0936  _expands Q0343_

Commands are reproducible only when they run from the repository root with the expected JDK and build wrapper. Before executing the step for Run Configuration, which terminal working directory and wrapper context should be confirmed? This micro-check belongs specifically to legacy build step Q0343, so it remains tied to that exact PetClinic decision.


---

