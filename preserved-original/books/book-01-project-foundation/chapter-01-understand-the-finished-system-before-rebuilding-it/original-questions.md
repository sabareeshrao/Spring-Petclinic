# Chapter 1 — Understand the finished system before rebuilding it

Detailed sequence questions in this chapter: **20**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0001  _preserved from Q0001_

Spring PetClinic is a server-rendered Spring Boot application organized around owners, pets, visits, veterinarians, persistence, MVC controllers, and Thymeleaf views. Before creating files, which major application style are we rebuilding: a Spring Boot MVC web application or a client-only frontend?

## Q0002  _expands Q0001_

A reconstruction step should have a visible acceptance condition, not just an intention. For architecture, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0001, so it remains tied to that exact PetClinic decision.

## Q0003  _preserved from Q0002_

The current canonical PetClinic repository uses Java 17 as its minimum build level. Which Java language level should our reconstruction target so the build matches the repository baseline?

## Q0004  _expands Q0002_

Initializr is effectively the first project configuration screen: selections made here later appear in build files and source layout. Before generating the project, which visible value for Java version should be confirmed against the PetClinic target? This micro-check belongs specifically to legacy build step Q0002, so it remains tied to that exact PetClinic decision.

## Q0005  _preserved from Q0003_

The project keeps its main code under the package org.springframework.samples.petclinic. Which base package should we establish so component scanning and source paths align with the target project?

## Q0006  _expands Q0003_

A real developer usually validates Initializr choices before clicking Generate because fixing wrong metadata afterward means editing generated files. Which part of the Initializr form should remain focused to confirm Package name is correct? This micro-check belongs specifically to legacy build step Q0003, so it remains tied to that exact PetClinic decision.

## Q0007  _preserved from Q0004_

PetClinic supports both Maven and Gradle, while the Maven pom.xml is a primary build definition in the repository. Which build tool should we configure first if we want to reproduce the Maven path before adding Gradle parity?

## Q0008  _expands Q0004_

Spring Initializr changes one project setting at a time, and each visible selection becomes part of the generated project metadata. After this step affects Build tool, which control should you visually re-check before moving on so the generated archive does not carry an accidental default? This micro-check belongs specifically to legacy build step Q0004, so it remains tied to that exact PetClinic decision.

## Q0009  _preserved from Q0005_

The application renders HTML with Thymeleaf rather than exposing only JSON APIs. Which server-side template technology must be part of the reconstruction plan?

## Q0010  _expands Q0005_

Developers reduce rework by checking dependencies before coding the next feature. Looking at architecture, which downstream file or behavior depends on this step and therefore tells us what should be built next? This micro-check belongs specifically to legacy build step Q0005, so it remains tied to that exact PetClinic decision.

## Q0011  _preserved from Q0006_

Persistence is handled with Spring Data JPA and relational databases. Which persistence style should our domain model be designed for?

## Q0012  _expands Q0006_

PetClinic is a connected system rather than a pile of independent files. After inspecting architecture, which dependency relationship should be verified so the next step follows the real application graph? This micro-check belongs specifically to legacy build step Q0006, so it remains tied to that exact PetClinic decision.

## Q0013  _preserved from Q0007_

The default development database is H2, while MySQL and PostgreSQL are optional profiles. Which database should work with no external database server during the earliest build stages?

## Q0014  _expands Q0007_

A reconstruction step should have a visible acceptance condition, not just an intention. For database plan, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0007, so it remains tied to that exact PetClinic decision.

## Q0015  _preserved from Q0008_

The repository contains web UI, database schemas, tests, CI workflows, Docker Compose, and Kubernetes manifests. Should our build order stop after Java code, or continue through testing and operational assets so the question sequence reconstructs the full repository?

## Q0016  _expands Q0008_

Developers reduce rework by checking dependencies before coding the next feature. Looking at scope, which downstream file or behavior depends on this step and therefore tells us what should be built next? This micro-check belongs specifically to legacy build step Q0008, so it remains tied to that exact PetClinic decision.

## Q0017  _preserved from Q0009_

A realistic reconstruction should build dependency foundations before classes that depend on them. Should BaseEntity and Person be created before Owner, Pet, and Vet so inheritance has a valid foundation?

## Q0018  _expands Q0009_

PetClinic is a connected system rather than a pile of independent files. After inspecting build order, which dependency relationship should be verified so the next step follows the real application graph? This micro-check belongs specifically to legacy build step Q0009, so it remains tied to that exact PetClinic decision.

## Q0019  _preserved from Q0010_

Controllers depend on repositories and domain classes, and templates depend on controller model attributes. Which direction should the build follow: foundations to dependents, or UI-first with missing backend types?

## Q0020  _expands Q0010_

A reconstruction step should have a visible acceptance condition, not just an intention. For build order, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0010, so it remains tied to that exact PetClinic decision.
