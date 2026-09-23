# Chapter 27 — Automate builds with GitHub Actions

Detailed sequence questions in this chapter: **20**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q1069  _preserved from Q0410_

Continuous integration should run on changes to the main branch and on pull requests targeting main. Which GitHub Actions triggers should the Maven workflow use?

## Q1070  _expands Q0410_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding .github/workflows/maven-build.yml, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0410, so it remains tied to that exact PetClinic decision.

## Q1071  _preserved from Q0411_

CI should build on a clean hosted Linux environment. Which runner should the Maven job use?

## Q1072  _expands Q0411_

Real developers verify infrastructure incrementally instead of waiting until final deployment. Which smallest runnable check should confirm the change to .github/workflows/maven-build.yml works in isolation? This micro-check belongs specifically to legacy build step Q0411, so it remains tied to that exact PetClinic decision.

## Q1073  _preserved from Q0412_

The supported Java baseline is 17. Which JDK version should the workflow matrix install?

## Q1074  _expands Q0412_

Infrastructure changes are useful only when their external state can be observed. After the step involving .github/workflows/maven-build.yml, which command output, container state, workflow status, or service response should be checked before proceeding? This micro-check belongs specifically to legacy build step Q0412, so it remains tied to that exact PetClinic decision.

## Q1075  _preserved from Q0413_

Dependency caching shortens repeated CI builds. Which setup-java cache mode should the Maven workflow enable?

## Q1076  _expands Q0413_

Operational files are executable configuration: a typo often appears only when the tool parses or applies them. Which tool-specific validation should be run immediately after changing .github/workflows/maven-build.yml? This micro-check belongs specifically to legacy build step Q0413, so it remains tied to that exact PetClinic decision.

## Q1077  _preserved from Q0414_

The repository wrapper guarantees the expected Maven version/configuration. Which command should Maven CI run?

## Q1078  _expands Q0414_

Real developers verify infrastructure incrementally instead of waiting until final deployment. Which smallest runnable check should confirm the change to .github/workflows/maven-build.yml works in isolation? This micro-check belongs specifically to legacy build step Q0414, so it remains tied to that exact PetClinic decision.

## Q1079  _preserved from Q0415_

Gradle deserves a separate build path so either build definition cannot silently rot. Which second workflow should we create?

## Q1080  _expands Q0415_

IntelliJ creates Java and resource files relative to the selected package or folder, so creating a file from the wrong node silently produces the wrong path. Before creating .github/workflows/gradle-build.yml, which parent package or resource directory should be selected in the Project tool window? This micro-check belongs specifically to legacy build step Q0415, so it remains tied to that exact PetClinic decision.

## Q1081  _preserved from Q0416_

Gradle CI uses the same Java baseline as Maven CI. Which JDK version should that workflow install?

## Q1082  _expands Q0416_

Operational files are executable configuration: a typo often appears only when the tool parses or applies them. Which tool-specific validation should be run immediately after changing .github/workflows/gradle-build.yml? This micro-check belongs specifically to legacy build step Q0416, so it remains tied to that exact PetClinic decision.

## Q1083  _preserved from Q0417_

The Gradle setup action prepares caching and build environment. Which setup step should run before invoking the wrapper?

## Q1084  _expands Q0417_

Real developers verify infrastructure incrementally instead of waiting until final deployment. Which smallest runnable check should confirm the change to .github/workflows/gradle-build.yml works in isolation? This micro-check belongs specifically to legacy build step Q0417, so it remains tied to that exact PetClinic decision.

## Q1085  _preserved from Q0418_

The wrapper should perform the complete Gradle build. Which command should the final Gradle CI step run?

## Q1086  _expands Q0418_

Infrastructure changes are useful only when their external state can be observed. After the step involving .github/workflows/gradle-build.yml, which command output, container state, workflow status, or service response should be checked before proceeding? This micro-check belongs specifically to legacy build step Q0418, so it remains tied to that exact PetClinic decision.

## Q1087  _preserved from Q0419_

A repository can also validate deployment assets against a temporary cluster. Which additional workflow should be reserved for deploy-and-test cluster behavior?

## Q1088  _expands Q0419_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding .github/workflows/deploy-and-test-cluster.yml, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0419, so it remains tied to that exact PetClinic decision.
