# Chapter 28 — Add Kubernetes database and application deployment manifests

Detailed sequence questions in this chapter: **28**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q1089  _preserved from Q0420_

Kubernetes deployment separates database resources from application resources. Which manifest should define the database Secret, Service, and Deployment?

## Q1090  _expands Q0420_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating k8s/db.yml, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0420, so it remains tied to that exact PetClinic decision.

## Q1091  _preserved from Q0421_

Service binding data can be stored in a Secret with database type, provider, host, port, database, username, and password. Which Secret name should the target manifest use?

## Q1092  _expands Q0421_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing k8s/db.yml Secret, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0421, so it remains tied to that exact PetClinic decision.

## Q1093  _preserved from Q0422_

The PostgreSQL Service gives the database a stable network name. Which service port should expose PostgreSQL inside the cluster?

## Q1094  _expands Q0422_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in k8s/db.yml Service, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0422, so it remains tied to that exact PetClinic decision.

## Q1095  _preserved from Q0423_

The database Deployment should run the PostgreSQL image version pinned by the repository snapshot. Which database image should the container use?

## Q1096  _expands Q0423_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in k8s/db.yml Deployment, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0423, so it remains tied to that exact PetClinic decision.

## Q1097  _preserved from Q0424_

Database credentials should come from the Secret instead of being duplicated in the container spec. Which environment fields should reference secretKeyRef values?

## Q1098  _expands Q0424_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to k8s/db.yml Deployment, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0424, so it remains tied to that exact PetClinic decision.

## Q1099  _preserved from Q0425_

Startup, readiness, and liveness probes let Kubernetes distinguish booting, ready, and unhealthy database states. Which simple probe type should the database container use on its PostgreSQL port?

## Q1100  _expands Q0425_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in k8s/db.yml probes before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0425, so it remains tied to that exact PetClinic decision.

## Q1101  _preserved from Q0426_

The application needs its own Service and Deployment manifest. Which file should define PetClinic runtime resources?

## Q1102  _expands Q0426_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating k8s/petclinic.yml, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0426, so it remains tied to that exact PetClinic decision.

## Q1103  _preserved from Q0427_

The application listens on 8080 internally while the Service exposes port 80. Which targetPort mapping should the PetClinic Service use?

## Q1104  _expands Q0427_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in k8s/petclinic.yml Service, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0427, so it remains tied to that exact PetClinic decision.

## Q1105  _preserved from Q0428_

The target Service type is NodePort for demonstration access. Which Service type should be declared?

## Q1106  _expands Q0428_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in k8s/petclinic.yml Service, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0428, so it remains tied to that exact PetClinic decision.

## Q1107  _preserved from Q0429_

The Kubernetes application activates PostgreSQL rather than H2. Which SPRING_PROFILES_ACTIVE value should the container receive?

## Q1108  _expands Q0429_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to k8s/petclinic.yml Deployment, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0429, so it remains tied to that exact PetClinic decision.

## Q1109  _preserved from Q0430_

Spring Boot service binding support reads mounted binding data from a root directory. Which SERVICE_BINDING_ROOT path should the container set?

## Q1110  _expands Q0430_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in k8s/petclinic.yml Deployment before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0430, so it remains tied to that exact PetClinic decision.

## Q1111  _preserved from Q0431_

Kubernetes health probes should use dedicated liveness and readiness endpoints. Which HTTP paths should the application probes call?

## Q1112  _expands Q0431_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing k8s/petclinic.yml probes, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0431, so it remains tied to that exact PetClinic decision.

## Q1113  _preserved from Q0432_

The database Secret is projected into the application pod as a read-only volume. Which volume-mount pattern should connect the Secret to the service-binding directory?

## Q1114  _expands Q0432_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in k8s/petclinic.yml volumes, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0432, so it remains tied to that exact PetClinic decision.

## Q1115  _preserved from Q0433_

Deployment is only credible after manifests can be applied and the service becomes ready. Which kubectl verification sequence should apply the DB first, then the app, then inspect pod/service readiness?

## Q1116  _expands Q0433_

Commands are reproducible only when they run from the repository root with the expected JDK and build wrapper. Before executing the step for Terminal, which terminal working directory and wrapper context should be confirmed? This micro-check belongs specifically to legacy build step Q0433, so it remains tied to that exact PetClinic decision.
