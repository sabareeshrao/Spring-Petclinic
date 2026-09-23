# Chapter 25 — Add formatting, quality gates, coverage, SBOM, and native support

Detailed sequence questions in this chapter: **28**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q1017  _preserved from Q0384_

Repository-wide style rules should be deterministic across IDEs. Which root editor configuration file should define whitespace and formatting basics?

## Q1018  _expands Q0384_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating .editorconfig, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0384, so it remains tied to that exact PetClinic decision.

## Q1019  _preserved from Q0385_

Git should normalize text behavior consistently across platforms. Which root file should define Git attribute rules?

## Q1020  _expands Q0385_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating .gitattributes, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0385, so it remains tied to that exact PetClinic decision.

## Q1021  _preserved from Q0386_

Build outputs and IDE metadata should not be committed. Which root ignore file should exclude target, build, IDE, and local artifacts?

## Q1022  _expands Q0386_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding .gitignore, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0386, so it remains tied to that exact PetClinic decision.

## Q1023  _preserved from Q0387_

The no-http rule uses Checkstyle configuration under src/checkstyle. Which checkstyle XML files should be created for the rule and suppressions?

## Q1024  _expands Q0387_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/checkstyle, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0387, so it remains tied to that exact PetClinic decision.

## Q1025  _preserved from Q0388_

Formatting should be validated automatically instead of depending on manual IDE formatting. Which Spring Java Format plugin should participate in Maven verification?

## Q1026  _expands Q0388_

When a new starter or plugin is added to pom.xml, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0388, so it remains tied to that exact PetClinic decision.

## Q1027  _preserved from Q0389_

JaCoCo should instrument tests and generate a coverage report before packaging completes. Which two lifecycle responsibilities should its plugin executions cover?

## Q1028  _expands Q0389_

Changing pom.xml in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0389, so it remains tied to that exact PetClinic decision.

## Q1029  _preserved from Q0390_

Software supply-chain metadata can be represented with a CycloneDX SBOM. Which plugin capability should generate that bill of materials?

## Q1030  _expands Q0390_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0390, so it remains tied to that exact PetClinic decision.

## Q1031  _preserved from Q0391_

Actuator can expose build metadata when META-INF/build-info.properties exists. Which Spring Boot build-info goal should we retain?

## Q1032  _expands Q0391_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0391, so it remains tied to that exact PetClinic decision.

## Q1033  _preserved from Q0392_

Actuator can expose Git metadata when git.properties is generated. Which build plugin should generate commit information?

## Q1034  _expands Q0392_

When a new starter or plugin is added to pom.xml, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0392, so it remains tied to that exact PetClinic decision.

## Q1035  _preserved from Q0393_

Native compilation needs the GraalVM build tools plugin. Which Maven plugin family should be included for native-image support?

## Q1036  _expands Q0393_

Changing pom.xml in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0393, so it remains tied to that exact PetClinic decision.

## Q1037  _preserved from Q0394_

Native images need resources and reflection registrations not always inferable from bytecode. Which runtime-hints class should remain connected to the application?

## Q1038  _expands Q0394_

A reconstruction step should have a visible acceptance condition, not just an intention. For PetClinicRuntimeHints.java, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0394, so it remains tied to that exact PetClinic decision.

## Q1039  _preserved from Q0395_

The Maven css profile should unpack Bootstrap SCSS before compiling PetClinic SCSS. Which Maven phase should generate those frontend resources?

## Q1040  _expands Q0395_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml css profile, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0395, so it remains tied to that exact PetClinic decision.

## Q1041  _preserved from Q0396_

Quality checks are useful only if developers can run them with one reproducible command. Which Maven Wrapper verification command should be treated as the pre-commit quality gate?

## Q1042  _expands Q0396_

PetClinic uses project-local wrappers so contributors do not depend on a globally installed Maven or Gradle version. Which wrapper command context should be preferred when running the operation related to Terminal? This micro-check belongs specifically to legacy build step Q0396, so it remains tied to that exact PetClinic decision.

## Q1043  _preserved from Q0397_

A quality gate should fail on formatting, checkstyle, compilation, or test errors rather than hiding them. Should CI continue after a failed verify step or stop the build?

## Q1044  _expands Q0397_

A reconstruction step should have a visible acceptance condition, not just an intention. For CI policy, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0397, so it remains tied to that exact PetClinic decision.
