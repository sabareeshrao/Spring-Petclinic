# Chapter 3 — Shape pom.xml to match PetClinic

Detailed sequence questions in this chapter: **90**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0059  _preserved from Q0030_

A Spring Boot parent POM centralizes dependency versions and plugin defaults. Which parent artifact should pom.xml declare so Spring Boot manages compatible versions?

## Q0060  _expands Q0030_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml parent, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0030, so it remains tied to that exact PetClinic decision.

## Q0061  _expands Q0030 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in pom.xml parent exposes a missing or inconsistent contract in PetClinicApplication.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0030, not by a generic file-order rule.

## Q0062  _preserved from Q0031_

The pinned repository uses Spring Boot 4.1.0 as its parent version. Which parent version should we place in pom.xml?

## Q0063  _expands Q0031_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml parent version, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0031, so it remains tied to that exact PetClinic decision.

## Q0064  _expands Q0031 · file revisit_

Real development now requires a file jump: the change in pom.xml parent version has a contract with Maven tool window, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to pom.xml parent version? This revisit is triggered specifically by legacy build step Q0031, not by a generic file-order rule.

## Q0065  _preserved from Q0032_

Maven coordinates define group, artifact, and version. Which groupId should pom.xml use to match the target repository?

## Q0066  _expands Q0032_

When a new starter or plugin is added to pom.xml groupId, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0032, so it remains tied to that exact PetClinic decision.

## Q0067  _expands Q0032 · file revisit_

PetClinic features cross layers, so finishing pom.xml groupId in isolation would be artificial. Because the next dependency is represented in PetClinicApplication.java, which file should IntelliJ navigate to now for the supporting change before we come back to pom.xml groupId? This revisit is triggered specifically by legacy build step Q0032, not by a generic file-order rule.

## Q0068  _preserved from Q0033_

The artifactId identifies the build output and dependency coordinate. Which artifactId should pom.xml use?

## Q0069  _expands Q0033_

Changing pom.xml artifactId in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0033, so it remains tied to that exact PetClinic decision.

## Q0070  _expands Q0033 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in pom.xml artifactId relies on behavior or metadata in Maven tool window; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0033, not by a generic file-order rule.

## Q0071  _preserved from Q0034_

A SNAPSHOT version signals a development build that may change. Which project version should we set if the target is 4.0.0-SNAPSHOT?

## Q0072  _expands Q0034_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml version, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0034, so it remains tied to that exact PetClinic decision.

## Q0073  _expands Q0034 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by pom.xml version. Which related file—PetClinicApplication.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0034, not by a generic file-order rule.

## Q0074  _preserved from Q0035_

The java.version property is used by Spring Boot and build plugins to enforce a baseline. Which value should java.version have?

## Q0075  _expands Q0035_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml properties, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0035, so it remains tied to that exact PetClinic decision.

## Q0076  _expands Q0035 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in pom.xml properties exposes a missing or inconsistent contract in Maven tool window, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0035, not by a generic file-order rule.

## Q0077  _preserved from Q0036_

The application uses Actuator for management endpoints. Which starter dependency should we add for management and health features?

## Q0078  _expands Q0036_

When a new starter or plugin is added to pom.xml dependencies, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0036, so it remains tied to that exact PetClinic decision.

## Q0079  _expands Q0036 · file revisit_

Real development now requires a file jump: the change in pom.xml dependencies has a contract with PetClinicApplication.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to pom.xml dependencies? This revisit is triggered specifically by legacy build step Q0036, not by a generic file-order rule.

## Q0080  _preserved from Q0037_

The application caches veterinarian queries. Which starter dependency should we add for Spring cache abstractions?

## Q0081  _expands Q0037_

Changing pom.xml dependencies in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0037, so it remains tied to that exact PetClinic decision.

## Q0082  _expands Q0037 · file revisit_

PetClinic features cross layers, so finishing pom.xml dependencies in isolation would be artificial. Because the next dependency is represented in Maven tool window, which file should IntelliJ navigate to now for the supporting change before we come back to pom.xml dependencies? This revisit is triggered specifically by legacy build step Q0037, not by a generic file-order rule.

## Q0083  _preserved from Q0038_

Spring Data JPA connects entities and repositories to Hibernate. Which starter dependency should we add for JPA persistence?

## Q0084  _expands Q0038_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml dependencies, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0038, so it remains tied to that exact PetClinic decision.

## Q0085  _expands Q0038 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in pom.xml dependencies relies on behavior or metadata in PetClinicApplication.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0038, not by a generic file-order rule.

## Q0086  _preserved from Q0039_

Thymeleaf is the server-side HTML view engine. Which starter dependency should we add for Thymeleaf views?

## Q0087  _expands Q0039_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml dependencies, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0039, so it remains tied to that exact PetClinic decision.

## Q0088  _expands Q0039 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by pom.xml dependencies. Which related file—Maven tool window—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0039, not by a generic file-order rule.

## Q0089  _preserved from Q0040_

Validation constraints are used throughout model objects. Which starter dependency should provide Jakarta Bean Validation integration?

## Q0090  _expands Q0040_

When a new starter or plugin is added to pom.xml dependencies, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0040, so it remains tied to that exact PetClinic decision.

## Q0091  _expands Q0040 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in pom.xml dependencies exposes a missing or inconsistent contract in PetClinicApplication.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0040, not by a generic file-order rule.

## Q0092  _preserved from Q0041_

The project uses the Spring MVC servlet stack. Which web MVC starter should be present?

## Q0093  _expands Q0041_

Changing pom.xml dependencies in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0041, so it remains tied to that exact PetClinic decision.

## Q0094  _expands Q0041 · file revisit_

Real development now requires a file jump: the change in pom.xml dependencies has a contract with Maven tool window, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to pom.xml dependencies? This revisit is triggered specifically by legacy build step Q0041, not by a generic file-order rule.

## Q0095  _preserved from Q0042_

JCache is the standard caching API used by the cache configuration. Which javax.cache API dependency should be present?

## Q0096  _expands Q0042_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml dependencies, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0042, so it remains tied to that exact PetClinic decision.

## Q0097  _expands Q0042 · file revisit_

PetClinic features cross layers, so finishing pom.xml dependencies in isolation would be artificial. Because the next dependency is represented in PetClinicApplication.java, which file should IntelliJ navigate to now for the supporting change before we come back to pom.xml dependencies? This revisit is triggered specifically by legacy build step Q0042, not by a generic file-order rule.

## Q0098  _preserved from Q0043_

Vets is XML-bindable and native/runtime support needs JAXB APIs. Which Jakarta XML Bind API dependency should be present?

## Q0099  _expands Q0043_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml dependencies, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0043, so it remains tied to that exact PetClinic decision.

## Q0100  _expands Q0043 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in pom.xml dependencies relies on behavior or metadata in Maven tool window; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0043, not by a generic file-order rule.

## Q0101  _preserved from Q0044_

H2 is only needed while the application is running, not while compiling domain code. Which scope should the H2 dependency use?

## Q0102  _expands Q0044_

When a new starter or plugin is added to pom.xml H2 dependency, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0044, so it remains tied to that exact PetClinic decision.

## Q0103  _expands Q0044 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by pom.xml H2 dependency. Which related file—PetClinicApplication.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0044, not by a generic file-order rule.

## Q0104  _preserved from Q0045_

The project can run against MySQL when the mysql profile is active. Which JDBC driver dependency should be added for MySQL?

## Q0105  _expands Q0045_

Changing pom.xml runtime dependencies in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0045, so it remains tied to that exact PetClinic decision.

## Q0106  _expands Q0045 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in pom.xml runtime dependencies exposes a missing or inconsistent contract in Maven tool window, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0045, not by a generic file-order rule.

## Q0107  _preserved from Q0046_

The project can run against PostgreSQL when the postgres profile is active. Which JDBC driver dependency should be added for PostgreSQL?

## Q0108  _expands Q0046_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml runtime dependencies, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0046, so it remains tied to that exact PetClinic decision.

## Q0109  _expands Q0046 · file revisit_

Real development now requires a file jump: the change in pom.xml runtime dependencies has a contract with PetClinicApplication.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to pom.xml runtime dependencies? This revisit is triggered specifically by legacy build step Q0046, not by a generic file-order rule.

## Q0110  _preserved from Q0047_

Caffeine supplies the concrete cache implementation behind JCache integration. Which runtime caching library should we include?

## Q0111  _expands Q0047_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml runtime dependencies, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0047, so it remains tied to that exact PetClinic decision.

## Q0112  _expands Q0047 · file revisit_

PetClinic features cross layers, so finishing pom.xml runtime dependencies in isolation would be artificial. Because the next dependency is represented in Maven tool window, which file should IntelliJ navigate to now for the supporting change before we come back to pom.xml runtime dependencies? This revisit is triggered specifically by legacy build step Q0047, not by a generic file-order rule.

## Q0113  _preserved from Q0048_

Bootstrap and Font Awesome are delivered as WebJars so templates can load frontend assets from the classpath. Which type of dependencies should be added for Bootstrap and Font Awesome?

## Q0114  _expands Q0048_

When a new starter or plugin is added to pom.xml WebJars, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0048, so it remains tied to that exact PetClinic decision.

## Q0115  _expands Q0048 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in pom.xml WebJars relies on behavior or metadata in PetClinicApplication.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0048, not by a generic file-order rule.

## Q0116  _preserved from Q0049_

Developer Tools can speed local feedback but should not be a required production dependency. How should spring-boot-devtools be marked so it remains optional for consumers?

## Q0117  _expands Q0049_

Changing pom.xml devtools in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0049, so it remains tied to that exact PetClinic decision.

## Q0118  _expands Q0049 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by pom.xml devtools. Which related file—Maven tool window—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0049, not by a generic file-order rule.

## Q0119  _preserved from Q0050_

PetClinic has specialized test starters for JPA, MVC, validation, Actuator, REST client, cache, and Thymeleaf. Which scope should all of those test-focused Spring Boot dependencies use?

## Q0120  _expands Q0050_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml test dependencies, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0050, so it remains tied to that exact PetClinic decision.

## Q0121  _expands Q0050 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in pom.xml test dependencies exposes a missing or inconsistent contract in PetClinicApplication.java, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0050, not by a generic file-order rule.

## Q0122  _preserved from Q0051_

Testcontainers is used to start real database containers during integration tests. Which two Testcontainers capabilities are needed for JUnit Jupiter and MySQL container support?

## Q0123  _expands Q0051_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml testcontainers, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0051, so it remains tied to that exact PetClinic decision.

## Q0124  _expands Q0051 · file revisit_

Real development now requires a file jump: the change in pom.xml testcontainers has a contract with Maven tool window, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to pom.xml testcontainers? This revisit is triggered specifically by legacy build step Q0051, not by a generic file-order rule.

## Q0125  _preserved from Q0052_

The Maven Enforcer plugin prevents unsupported JDKs from building the project. Which minimum Java version should its requireJavaVersion rule enforce?

## Q0126  _expands Q0052_

When a new starter or plugin is added to pom.xml enforcer, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0052, so it remains tied to that exact PetClinic decision.

## Q0127  _expands Q0052 · file revisit_

PetClinic features cross layers, so finishing pom.xml enforcer in isolation would be artificial. Because the next dependency is represented in PetClinicApplication.java, which file should IntelliJ navigate to now for the supporting change before we come back to pom.xml enforcer? This revisit is triggered specifically by legacy build step Q0052, not by a generic file-order rule.

## Q0128  _preserved from Q0053_

Spring Java Format validates formatting as part of the Maven lifecycle. At which lifecycle phase should formatting validation run before packaging?

## Q0129  _expands Q0053_

Changing pom.xml spring-javaformat in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0053, so it remains tied to that exact PetClinic decision.

## Q0130  _expands Q0053 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in pom.xml spring-javaformat relies on behavior or metadata in Maven tool window; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0053, not by a generic file-order rule.

## Q0131  _preserved from Q0054_

The no-http Checkstyle rule scans repository content for disallowed plain HTTP references. Which Maven plugin should execute the custom checkstyle configuration during validate?

## Q0132  _expands Q0054_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml checkstyle, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0054, so it remains tied to that exact PetClinic decision.

## Q0133  _expands Q0054 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by pom.xml checkstyle. Which related file—PetClinicApplication.java—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0054, not by a generic file-order rule.

## Q0134  _preserved from Q0055_

The Spring Boot Maven plugin can generate build-info metadata for Actuator. Which plugin goal should be configured to write build information?

## Q0135  _expands Q0055_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml spring-boot-maven-plugin, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0055, so it remains tied to that exact PetClinic decision.

## Q0136  _expands Q0055 · file revisit_

Compiler, binding, and persistence feedback commonly force a short detour. If the current step in pom.xml spring-boot-maven-plugin exposes a missing or inconsistent contract in Maven tool window, which file should be fixed first before returning here? This revisit is triggered specifically by legacy build step Q0055, not by a generic file-order rule.

## Q0137  _preserved from Q0056_

JaCoCo instruments tests and creates coverage reports. Which Maven plugin should we configure for coverage preparation and reporting?

## Q0138  _expands Q0056_

When a new starter or plugin is added to pom.xml JaCoCo, IntelliJ may need to download artifacts before code completion works. Which dependency-resolution state should you wait to see complete before relying on imports from that dependency? This micro-check belongs specifically to legacy build step Q0056, so it remains tied to that exact PetClinic decision.

## Q0139  _expands Q0056 · file revisit_

Real development now requires a file jump: the change in pom.xml JaCoCo has a contract with PetClinicApplication.java, and mismatches between the two usually surface later as mapping, binding, or compilation bugs. Which previously created file should we reopen now to verify that contract before returning to pom.xml JaCoCo? This revisit is triggered specifically by legacy build step Q0056, not by a generic file-order rule.

## Q0140  _preserved from Q0057_

Git commit metadata can be exposed by Actuator when git.properties is available. Which kind of plugin should be added to generate Git commit information during builds?

## Q0141  _expands Q0057_

Changing pom.xml git metadata in Maven is not complete until IntelliJ reloads the project model; otherwise editor imports may stay red even when the XML is correct. Which Maven refresh/reload action should follow this change before we edit Java code? This micro-check belongs specifically to legacy build step Q0057, so it remains tied to that exact PetClinic decision.

## Q0142  _expands Q0057 · file revisit_

PetClinic features cross layers, so finishing pom.xml git metadata in isolation would be artificial. Because the next dependency is represented in Maven tool window, which file should IntelliJ navigate to now for the supporting change before we come back to pom.xml git metadata? This revisit is triggered specifically by legacy build step Q0057, not by a generic file-order rule.

## Q0143  _preserved from Q0058_

CycloneDX creates a software bill of materials that describes project components. Which build capability should we add so an SBOM can be generated?

## Q0144  _expands Q0058_

Maven dependencies and plugins affect the IDE classpath as well as the command-line build. After updating pom.xml SBOM, which IntelliJ Maven view should you inspect to confirm the model re-imported without errors? This micro-check belongs specifically to legacy build step Q0058, so it remains tied to that exact PetClinic decision.

## Q0145  _expands Q0058 · file revisit_

A developer often discovers the next requirement from the code just written. The current work in pom.xml SBOM relies on behavior or metadata in PetClinicApplication.java; which earlier file should we jump back to and adjust before continuing this feature? This revisit is triggered specifically by legacy build step Q0058, not by a generic file-order rule.

## Q0146  _preserved from Q0059_

The css Maven profile compiles SCSS and needs Bootstrap sources unpacked first. Which profile should we create for CSS generation rather than running that work on every normal build?

## Q0147  _expands Q0059_

A malformed POM can invalidate every later Java step, so developers validate build configuration incrementally. After editing pom.xml profile, which lightweight Maven validation/build action should confirm the POM is still parseable before we continue? This micro-check belongs specifically to legacy build step Q0059, so it remains tied to that exact PetClinic decision.

## Q0148  _expands Q0059 · file revisit_

Instead of completing one file top-to-bottom, we should follow the dependency revealed by pom.xml profile. Which related file—Maven tool window—needs to be reopened now so both sides of the contract evolve together? This revisit is triggered specifically by legacy build step Q0059, not by a generic file-order rule.
