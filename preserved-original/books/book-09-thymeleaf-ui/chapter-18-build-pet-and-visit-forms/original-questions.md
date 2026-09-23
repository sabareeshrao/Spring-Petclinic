# Chapter 18 — Build pet and visit forms

Detailed sequence questions in this chapter: **24**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0841  _preserved from Q0300_

Creating and editing pets share one form because the fields are the same. Which template should serve both pet flows?

## Q0842  _expands Q0300_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/resources/templates/pets/createOrUpdatePetForm.html, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0300, so it remains tied to that exact PetClinic decision.

## Q0843  _preserved from Q0301_

The pet form binds to the pet model attribute prepared by PetController. Which Thymeleaf object should the form declare?

## Q0844  _expands Q0301_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/templates/pets/createOrUpdatePetForm.html, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0301, so it remains tied to that exact PetClinic decision.

## Q0845  _preserved from Q0302_

Pet input includes name, birth date, and type. Which form controls should be rendered for these fields?

## Q0846  _expands Q0302_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/templates/pets/createOrUpdatePetForm.html, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0302, so it remains tied to that exact PetClinic decision.

## Q0847  _preserved from Q0303_

Pet types come from the controller’s types model attribute. Which options collection should populate the type select control?

## Q0848  _expands Q0303_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/templates/pets/createOrUpdatePetForm.html, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0303, so it remains tied to that exact PetClinic decision.

## Q0849  _preserved from Q0304_

Browser date controls should receive the existing birth date and submit yyyy-MM-dd. Which input type should be used for birthDate?

## Q0850  _expands Q0304_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/resources/templates/pets/createOrUpdatePetForm.html, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0304, so it remains tied to that exact PetClinic decision.

## Q0851  _preserved from Q0305_

A visit form is nested beneath a specific pet and owner. Which template should render new-visit booking?

## Q0852  _expands Q0305_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/templates/pets/createOrUpdateVisitForm.html, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0305, so it remains tied to that exact PetClinic decision.

## Q0853  _preserved from Q0306_

The visit form binds to the visit model attribute. Which fields should it expose from Visit?

## Q0854  _expands Q0306_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/templates/pets/createOrUpdateVisitForm.html, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0306, so it remains tied to that exact PetClinic decision.

## Q0855  _preserved from Q0307_

The server exposes minVisitDate so the browser can prevent selecting today or an earlier day. Which HTML input attribute should use that model value?

## Q0856  _expands Q0307_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/templates/pets/createOrUpdateVisitForm.html, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0307, so it remains tied to that exact PetClinic decision.

## Q0857  _preserved from Q0308_

The booking page should remind the user which pet is being scheduled. Which pet model value should the form display prominently?

## Q0858  _expands Q0308_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/templates/pets/createOrUpdateVisitForm.html, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0308, so it remains tied to that exact PetClinic decision.

## Q0859  _preserved from Q0309_

Validation errors from the controller should remain visible on the same form. Which fragment/error rendering behavior should both pet and visit forms use?

## Q0860  _expands Q0309_

Real developers frequently navigate by symbol rather than scrolling through long files. Before applying the next change to src/main/resources/templates/pets/*.html, which IntelliJ Structure/Search action would take you directly to the class member or annotation being extended? This micro-check belongs specifically to legacy build step Q0309, so it remains tied to that exact PetClinic decision.

## Q0861  _preserved from Q0310_

The form action is determined by the nested owner/pet route. Which URL pieces must remain present when editing a pet or adding a visit?

## Q0862  _expands Q0310_

Because PetClinic wires classes through Spring and JPA annotations, a green Java syntax check alone is not enough; annotation arguments and referenced types must also resolve. Which IDE inspection should you clear in src/main/resources/templates/pets/*.html before treating this micro-step as complete? This micro-check belongs specifically to legacy build step Q0310, so it remains tied to that exact PetClinic decision.

## Q0863  _preserved from Q0311_

After successful submit, controllers redirect to owner details rather than rendering the form directly. Why should the templates focus only on GET/form rendering and error redisplay rather than success navigation?

## Q0864  _expands Q0311_

Developers reduce rework by checking dependencies before coding the next feature. Looking at src/main/resources/templates/pets/*.html, which downstream file or behavior depends on this step and therefore tells us what should be built next? This micro-check belongs specifically to legacy build step Q0311, so it remains tied to that exact PetClinic decision.
