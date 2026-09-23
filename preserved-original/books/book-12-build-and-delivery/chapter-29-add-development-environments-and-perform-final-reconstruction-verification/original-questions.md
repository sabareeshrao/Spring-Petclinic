# Chapter 29 — Add development environments and perform final reconstruction verification

Detailed sequence questions in this chapter: **34**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q1117  _preserved from Q0434_

A devcontainer can standardize JDK and tooling for contributors using container-based IDE environments. Which .devcontainer files should describe the development image and editor environment?

## Q1118  _expands Q0434_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding .devcontainer, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0434, so it remains tied to that exact PetClinic decision.

## Q1119  _preserved from Q0435_

Gitpod configuration can define a cloud development startup workflow. Which root file should hold Gitpod settings?

## Q1120  _expands Q0435_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating .gitpod.yml, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0435, so it remains tied to that exact PetClinic decision.

## Q1121  _preserved from Q0436_

Maven Wrapper files should be executable and committed so builds do not depend on a global Maven install. Which wrapper scripts and properties should be present?

## Q1122  _expands Q0436_

A reconstruction step should have a visible acceptance condition, not just an intention. For .mvn/wrapper + mvnw, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0436, so it remains tied to that exact PetClinic decision.

## Q1123  _preserved from Q0437_

Gradle Wrapper should likewise make Gradle builds reproducible. Which wrapper scripts and jar/properties should be present?

## Q1124  _expands Q0437_

Developers reduce rework by checking dependencies before coding the next feature. Looking at gradle/wrapper + gradlew, which downstream file or behavior depends on this step and therefore tells us what should be built next? This micro-check belongs specifically to legacy build step Q0437, so it remains tied to that exact PetClinic decision.

## Q1125  _preserved from Q0438_

The reconstructed source tree should contain the root application, model, owner, vet, and system packages before final build. Which package directories should we inspect in IntelliJ’s Project view?

## Q1126  _expands Q0438_

PetClinic is a connected system rather than a pile of independent files. After inspecting src/main/java, which dependency relationship should be verified so the next step follows the real application graph? This micro-check belongs specifically to legacy build step Q0438, so it remains tied to that exact PetClinic decision.

## Q1127  _preserved from Q0439_

The resource tree should contain application profiles, database scripts, messages, static assets, and templates. Which major resource directories should we verify before running?

## Q1128  _expands Q0439_

A reconstruction step should have a visible acceptance condition, not just an intention. For src/main/resources, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0439, so it remains tied to that exact PetClinic decision.

## Q1129  _preserved from Q0440_

The Maven wrapper can launch the application directly. Which command should we run for a local development start?

## Q1130  _expands Q0440_

A successful command should leave observable evidence rather than just returning to a prompt. After running the operation for Terminal, which exit status or application/build message should be checked before moving forward? This micro-check belongs specifically to legacy build step Q0440, so it remains tied to that exact PetClinic decision.

## Q1131  _preserved from Q0441_

A successful default startup should use H2 and expose the web application on localhost:8080. Which browser URL should we open first?

## Q1132  _expands Q0441_

A realistic workflow records not only what to change but how to know the change worked. Which verification should follow the action on Browser? This micro-check belongs specifically to legacy build step Q0441, so it remains tied to that exact PetClinic decision.

## Q1133  _preserved from Q0442_

The home page alone does not prove business flows work. Which navigation areas should we manually exercise: owners, owner creation/editing, pets, visits, vets, and error handling?

## Q1134  _expands Q0442_

A reconstruction step should have a visible acceptance condition, not just an intention. For Browser, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0442, so it remains tied to that exact PetClinic decision.

## Q1135  _preserved from Q0443_

Pet uniqueness and date validation are core business safeguards. Which invalid UI submissions should we deliberately try to verify those rules?

## Q1136  _expands Q0443_

Developers reduce rework by checking dependencies before coding the next feature. Looking at Browser, which downstream file or behavior depends on this step and therefore tells us what should be built next? This micro-check belongs specifically to legacy build step Q0443, so it remains tied to that exact PetClinic decision.

## Q1137  _preserved from Q0444_

Internationalization should switch message bundles without restarting the application. Which query-parameter behavior should we test on a page?

## Q1138  _expands Q0444_

PetClinic is a connected system rather than a pile of independent files. After inspecting Browser, which dependency relationship should be verified so the next step follows the real application graph? This micro-check belongs specifically to legacy build step Q0444, so it remains tied to that exact PetClinic decision.

## Q1139  _preserved from Q0445_

Actuator endpoints are exposed for development in this project. Which management area should we inspect to confirm Actuator is active?

## Q1140  _expands Q0445_

A reconstruction step should have a visible acceptance condition, not just an intention. For Browser, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0445, so it remains tied to that exact PetClinic decision.

## Q1141  _preserved from Q0446_

Maven verification should pass before publishing the reconstruction. Which wrapper command should run the full Maven quality/test lifecycle?

## Q1142  _expands Q0446_

A successful command should leave observable evidence rather than just returning to a prompt. After running the operation for Terminal, which exit status or application/build message should be checked before moving forward? This micro-check belongs specifically to legacy build step Q0446, so it remains tied to that exact PetClinic decision.

## Q1143  _preserved from Q0447_

Gradle parity should also pass. Which wrapper command should run the full Gradle build?

## Q1144  _expands Q0447_

PetClinic uses project-local wrappers so contributors do not depend on a globally installed Maven or Gradle version. Which wrapper command context should be preferred when running the operation related to Terminal? This micro-check belongs specifically to legacy build step Q0447, so it remains tied to that exact PetClinic decision.

## Q1145  _preserved from Q0448_

A clean Git history makes the question-driven rebuild auditable. Which Git sequence should stage the completed question repository, create a commit, and push it to a GitHub remote?

## Q1146  _expands Q0448_

Infrastructure changes are useful only when their external state can be observed. After the step involving Git / Terminal, which command output, container state, workflow status, or service response should be checked before proceeding? This micro-check belongs specifically to legacy build step Q0448, so it remains tied to that exact PetClinic decision.

## Q1147  _preserved from Q0449_

The question clone should not contain the finished upstream Java source because the learner is meant to reconstruct it through answers. Which final repository check should confirm that learner-facing content contains questions and metadata, not copied PetClinic implementation files?

## Q1148  _expands Q0449_

Developers reduce rework by checking dependencies before coding the next feature. Looking at File Explorer, which downstream file or behavior depends on this step and therefore tells us what should be built next? This micro-check belongs specifically to legacy build step Q0449, so it remains tied to that exact PetClinic decision.

## Q1149  _preserved from Q0450_

Every question should advance the build in dependency order and teach the concept inside the wording itself. Which final content audit should verify there are no unexplained jump steps between project generation and deployment?

## Q1150  _expands Q0450_

PetClinic is a connected system rather than a pile of independent files. After inspecting Question Repository, which dependency relationship should be verified so the next step follows the real application graph? This micro-check belongs specifically to legacy build step Q0450, so it remains tied to that exact PetClinic decision.
