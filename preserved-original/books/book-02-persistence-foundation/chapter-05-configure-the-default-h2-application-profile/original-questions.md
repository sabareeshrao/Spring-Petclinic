# Chapter 5 — Configure the default H2 application profile

Detailed sequence questions in this chapter: **24**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0179  _preserved from Q0070_

Spring Boot loads application.properties automatically from src/main/resources. Which resource file should we create for defaults shared by all database choices?

## Q0180  _expands Q0070_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/resources/application.properties before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0070, so it remains tied to that exact PetClinic decision.

## Q0181  _preserved from Q0071_

PetClinic chooses SQL scripts through a custom database property whose default value is h2. Which database identifier should the default configuration select?

## Q0182  _expands Q0071_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing application.properties database, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0071, so it remains tied to that exact PetClinic decision.

## Q0183  _preserved from Q0072_

Spring SQL initialization can load a schema script from a classpath pattern. Which property should point schema initialization at db/${database}/schema.sql?

## Q0184  _expands Q0072_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in application.properties schema locations, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0072, so it remains tied to that exact PetClinic decision.

## Q0185  _preserved from Q0073_

Seed data is loaded separately from schema creation. Which property should point data initialization at db/${database}/data.sql?

## Q0186  _expands Q0073_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in application.properties data locations, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0073, so it remains tied to that exact PetClinic decision.

## Q0187  _preserved from Q0074_

Thymeleaf renders HTML templates and can be told which template mode to use. Which template mode should be selected for PetClinic pages?

## Q0188  _expands Q0074_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to application.properties thymeleaf, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0074, so it remains tied to that exact PetClinic decision.

## Q0189  _preserved from Q0075_

PetClinic uses explicit SQL scripts instead of Hibernate generating tables. Which Hibernate DDL setting should prevent automatic schema creation?

## Q0190  _expands Q0075_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in application.properties JPA before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0075, so it remains tied to that exact PetClinic decision.

## Q0191  _preserved from Q0076_

Disabling Open Session in View keeps persistence access from leaking into view rendering. Which JPA property should be set false to disable Open Session in View?

## Q0192  _expands Q0076_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing application.properties JPA, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0076, so it remains tied to that exact PetClinic decision.

## Q0193  _preserved from Q0077_

Database naming maps Java-style property names to snake_case database columns. Which physical naming strategy should Hibernate use?

## Q0194  _expands Q0077_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in application.properties JPA, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0077, so it remains tied to that exact PetClinic decision.

## Q0195  _preserved from Q0078_

Batch fetching can reduce repeated relationship queries when loading collections. Which Hibernate batch fetch size should we configure to match the target repository?

## Q0196  _expands Q0078_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in application.properties JPA, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0078, so it remains tied to that exact PetClinic decision.

## Q0197  _preserved from Q0079_

Spring MessageSource finds localized bundles from a base path. Which basename should point to messages/messages?

## Q0198  _expands Q0079_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to application.properties i18n, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0079, so it remains tied to that exact PetClinic decision.

## Q0199  _preserved from Q0080_

The development app exposes all Actuator web endpoints for demonstration and testing. Which management exposure setting should be used, while recognizing that it is not a production-safe default?

## Q0200  _expands Q0080_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in application.properties actuator before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0080, so it remains tied to that exact PetClinic decision.

## Q0201  _preserved from Q0081_

Static resources can be browser-cached to reduce repeated downloads. Which cache-control max-age should we configure to match the target project?

## Q0202  _expands Q0081_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing application.properties static resources, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0081, so it remains tied to that exact PetClinic decision.
