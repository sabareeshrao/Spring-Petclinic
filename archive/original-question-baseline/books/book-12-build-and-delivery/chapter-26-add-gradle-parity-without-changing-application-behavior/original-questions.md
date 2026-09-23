# Chapter 26 — Add Gradle parity without changing application behavior

Detailed sequence questions in this chapter: **24**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q1045  _preserved from Q0398_

The canonical repository supports both Maven and Gradle builds. Which root Gradle build file should mirror the application dependencies and plugins?

## Q1046  _expands Q0398_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding build.gradle, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0398, so it remains tied to that exact PetClinic decision.

## Q1047  _preserved from Q0399_

Gradle needs the Java, Spring Boot, dependency-management, native, SBOM, format, checkstyle, and no-http capabilities used by the Maven build. Which plugin categories should the Gradle plugins block include?

## Q1048  _expands Q0399_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to build.gradle, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0399, so it remains tied to that exact PetClinic decision.

## Q1049  _preserved from Q0400_

The Gradle project uses the same group and version as Maven. Which group and version should be configured?

## Q1050  _expands Q0400_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in build.gradle before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0400, so it remains tied to that exact PetClinic decision.

## Q1051  _preserved from Q0401_

A Gradle toolchain makes the Java baseline explicit and reproducible. Which language version should the toolchain request?

## Q1052  _expands Q0401_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing build.gradle, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0401, so it remains tied to that exact PetClinic decision.

## Q1053  _preserved from Q0402_

Runtime and test dependency scopes differ from compile-time implementation dependencies. How should H2, MySQL, PostgreSQL, WebJars, and devtools be scoped in Gradle?

## Q1054  _expands Q0402_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in build.gradle, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0402, so it remains tied to that exact PetClinic decision.

## Q1055  _preserved from Q0403_

JUnit Jupiter is the test platform used by the Spring Boot test stack. Which test task configuration should enable it?

## Q1056  _expands Q0403_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in build.gradle, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0403, so it remains tied to that exact PetClinic decision.

## Q1057  _preserved from Q0404_

CycloneDX output should not pull test configurations into the direct production SBOM. Which configuration filtering behavior should the Gradle SBOM task apply?

## Q1058  _expands Q0404_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to build.gradle, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0404, so it remains tied to that exact PetClinic decision.

## Q1059  _preserved from Q0405_

Checkstyle should read the same custom config files as Maven. Which config directory and XML file should the Gradle checkstyle tasks use?

## Q1060  _expands Q0405_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in build.gradle before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0405, so it remains tied to that exact PetClinic decision.

## Q1061  _preserved from Q0406_

The repository provides a Gradle wrapper so developers do not need a globally installed matching Gradle version. Which wrapper files should be committed?

## Q1062  _expands Q0406_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating gradle/wrapper, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0406, so it remains tied to that exact PetClinic decision.

## Q1063  _preserved from Q0407_

settings.gradle gives the Gradle build its project identity. Which project name should it define?

## Q1064  _expands Q0407_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding settings.gradle, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0407, so it remains tied to that exact PetClinic decision.

## Q1065  _preserved from Q0408_

Maven and Gradle should compile and test the same application behavior. Which Gradle wrapper command should we run to verify parity?

## Q1066  _expands Q0408_

PetClinic uses project-local wrappers so contributors do not depend on a globally installed Maven or Gradle version. Which wrapper command context should be preferred when running the operation related to Terminal? This micro-check belongs specifically to legacy build step Q0408, so it remains tied to that exact PetClinic decision.

## Q1067  _preserved from Q0409_

If Maven passes but Gradle fails, build parity is incomplete even when application code is unchanged. Should the question sequence treat both builds as required repository verification?

## Q1068  _expands Q0409_

A reconstruction step should have a visible acceptance condition, not just an intention. For Build verification, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0409, so it remains tied to that exact PetClinic decision.
