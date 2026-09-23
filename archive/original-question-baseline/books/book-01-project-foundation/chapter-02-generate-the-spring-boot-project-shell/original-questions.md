# Chapter 2 — Generate the Spring Boot project shell

Detailed sequence questions in this chapter: **38**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0021  _preserved from Q0011_

Spring Initializr generates a compilable Spring Boot project and lets us choose language, build tool, metadata, Java, and dependencies. Which project generator should we open to create the initial skeleton?

## Q0022  _expands Q0011_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Project generator should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0011, so it remains tied to that exact PetClinic decision.

## Q0023  _preserved from Q0012_

Maven stores dependency and plugin configuration in pom.xml and is supported by the target repository. Which build system should we select for the first reconstruction path?

## Q0024  _expands Q0012_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Build system is correct? This micro-check belongs specifically to legacy build step Q0012, so it remains tied to that exact PetClinic decision.

## Q0025  _preserved from Q0013_

The application source is Java, not Kotlin or Groovy. Which language should we select?

## Q0026  _expands Q0013_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Language, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0013, so it remains tied to that exact PetClinic decision.

## Q0027  _preserved from Q0014_

The current repository pom declares Spring Boot parent version 4.1.0. Which Spring Boot version should we select to align with the pinned source snapshot?

## Q0028  _expands Q0014_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Spring Boot version should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0014, so it remains tied to that exact PetClinic decision.

## Q0029  _preserved from Q0015_

The Maven coordinates identify the project independently of Java package names. Which groupId should we enter if the target group is org.springframework.samples?

## Q0030  _expands Q0015_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Group is correct? This micro-check belongs specifically to legacy build step Q0015, so it remains tied to that exact PetClinic decision.

## Q0031  _preserved from Q0016_

The artifactId becomes the project artifact name used by Maven. Which artifactId should we use if the target project is spring-petclinic?

## Q0032  _expands Q0016_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Artifact, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0016, so it remains tied to that exact PetClinic decision.

## Q0033  _preserved from Q0017_

The repository version is 4.0.0-SNAPSHOT. Which initial project version should we set so generated metadata matches the target?

## Q0034  _expands Q0017_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Version should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0017, so it remains tied to that exact PetClinic decision.

## Q0035  _preserved from Q0018_

The project name is petclinic even though the artifactId is spring-petclinic. Which project display name should we configure?

## Q0036  _expands Q0018_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Name is correct? This micro-check belongs specifically to legacy build step Q0018, so it remains tied to that exact PetClinic decision.

## Q0037  _preserved from Q0019_

The base package drives the default source path created by Initializr. Which package name should be entered to produce org/springframework/samples/petclinic?

## Q0038  _expands Q0019_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Package name, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0019, so it remains tied to that exact PetClinic decision.

## Q0039  _preserved from Q0020_

The repository is packaged as an executable Spring Boot jar. Which packaging type should we choose: JAR or WAR?

## Q0040  _expands Q0020_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Packaging should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0020, so it remains tied to that exact PetClinic decision.

## Q0041  _preserved from Q0021_

The build enforces Java 17 or newer and the Gradle toolchain also targets 17. Which Java version should we select in Initializr?

## Q0042  _expands Q0021_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Java version is correct? This micro-check belongs specifically to legacy build step Q0021, so it remains tied to that exact PetClinic decision.

## Q0043  _preserved from Q0022_

Spring MVC supplies controllers, request mappings, data binding, and the servlet web stack used by PetClinic. Which web dependency should we add so MVC controllers can handle browser requests?

## Q0044  _expands Q0022_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Dependencies, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0022, so it remains tied to that exact PetClinic decision.

## Q0045  _preserved from Q0023_

Thymeleaf resolves server-side HTML templates from src/main/resources/templates. Which template-engine dependency should we add?

## Q0046  _expands Q0023_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Dependencies should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0023, so it remains tied to that exact PetClinic decision.

## Q0047  _preserved from Q0024_

Spring Data JPA supplies repository abstractions and Hibernate integration for entities. Which data dependency should we add?

## Q0048  _expands Q0024_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Dependencies is correct? This micro-check belongs specifically to legacy build step Q0024, so it remains tied to that exact PetClinic decision.

## Q0049  _preserved from Q0025_

Bean Validation supplies annotations such as @NotBlank, @Size, and @Pattern. Which validation dependency should we add?

## Q0050  _expands Q0025_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Dependencies, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0025, so it remains tied to that exact PetClinic decision.

## Q0051  _preserved from Q0026_

PetClinic exposes health and management information during development. Which Spring Boot dependency should we add for Actuator endpoints?

## Q0052  _expands Q0026_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Dependencies should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0026, so it remains tied to that exact PetClinic decision.

## Q0053  _preserved from Q0027_

Spring caching is used for veterinarian lookups. Which starter should we add so @Cacheable and cache infrastructure can be enabled?

## Q0054  _expands Q0027_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Dependencies is correct? This micro-check belongs specifically to legacy build step Q0027, so it remains tied to that exact PetClinic decision.

## Q0055  _preserved from Q0028_

H2 lets the application start with an embedded relational database. Which runtime database dependency should we include for the default profile?

## Q0056  _expands Q0028_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Dependencies, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0028, so it remains tied to that exact PetClinic decision.

## Q0057  _preserved from Q0029_

Once metadata and starter dependencies are selected, Initializr can generate the archive. Which action should we perform to create the project files?

## Q0058  _expands Q0029_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Generate should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0029, so it remains tied to that exact PetClinic decision.
