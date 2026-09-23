# Chapter 20 — Add localization and static resources

Detailed sequence questions in this chapter: **20**.

> Questions only. No answer key is stored in this learner-facing sequence.

## Q0889  _preserved from Q0320_

Spring MessageSource loads default messages from messages/messages.properties. Which base message file should we create first?

## Q0890  _expands Q0320_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/messages/messages.properties, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0320, so it remains tied to that exact PetClinic decision.

## Q0891  _preserved from Q0321_

The UI contains reusable keys for navigation, owner fields, pet fields, visits, buttons, and validation text. Should templates reference message keys instead of duplicating English labels across files?

## Q0892  _expands Q0321_

IntelliJ performs continuous syntax and symbol analysis while you type, which is why real developers fix local errors before piling on more code. After changing src/main/resources/messages/messages.properties, which editor indicators should you inspect for unresolved symbols, invalid annotations, or type mismatches before continuing? This micro-check belongs specifically to legacy build step Q0321, so it remains tied to that exact PetClinic decision.

## Q0893  _preserved from Q0322_

The telephone validation annotation references a message key rather than a hard-coded final sentence. Which kind of bundle entry should define the localized invalid-telephone message?

## Q0894  _expands Q0322_

Java code often introduces imports as soon as a Spring, Jakarta, or collection type is referenced. After this change in src/main/resources/messages/messages.properties, which IntelliJ import/inspection action should keep the file compilable without manually guessing package names? This micro-check belongs specifically to legacy build step Q0322, so it remains tied to that exact PetClinic decision.

## Q0895  _preserved from Q0323_

Pet and visit date validation errors use message codes from BindingResult. Which message-bundle entries should be added for those date errors?

## Q0896  _expands Q0323_

Incremental development is safer when each small edit leaves the current file structurally valid. After this step in src/main/resources/messages/messages.properties, which quick compile or IDE error check should confirm braces, method signatures, annotations, and imports are still consistent? This micro-check belongs specifically to legacy build step Q0323, so it remains tied to that exact PetClinic decision.

## Q0897  _preserved from Q0324_

PetClinic ships translations for multiple locales. Which naming convention should localized message files follow after the base file is stable?

## Q0898  _expands Q0324_

A realistic build creates the smallest file shell first and lets compiler feedback guide the next edits. When creating src/main/resources/messages/messages_<locale>.properties, which IntelliJ New-file action should be used so the file is immediately opened in the editor for incremental implementation? This micro-check belongs specifically to legacy build step Q0324, so it remains tied to that exact PetClinic decision.

## Q0899  _preserved from Q0325_

All locale files should remain key-compatible so switching languages does not expose missing placeholders. What consistency rule should we enforce across translated bundles?

## Q0900  _expands Q0325_

A reconstruction step should have a visible acceptance condition, not just an intention. For src/main/resources/messages/*.properties, which concrete project-tree, build, route, or runtime observation should confirm this step is actually satisfied? This micro-check belongs specifically to legacy build step Q0325, so it remains tied to that exact PetClinic decision.

## Q0901  _preserved from Q0326_

Application CSS is served from src/main/resources/static/resources/css. Which static directory should contain petclinic.css?

## Q0902  _expands Q0326_

Package location is part of application behavior because Spring component scanning begins from the root application package. Before adding src/main/resources/static/resources/css/petclinic.css, which Project-view path should you verify so the new file lands inside the intended package tree? This micro-check belongs specifically to legacy build step Q0326, so it remains tied to that exact PetClinic decision.

## Q0903  _preserved from Q0327_

Images such as the favicon, pet illustration, and Spring logo are static resources. Which resource directory should hold image assets referenced by templates?

## Q0904  _expands Q0327_

A realistic workflow records not only what to change but how to know the change worked. Which verification should follow the action on src/main/resources/static/resources/images? This micro-check belongs specifically to legacy build step Q0327, so it remains tied to that exact PetClinic decision.

## Q0905  _preserved from Q0328_

Custom Montserrat and Varela Round font files are served from static resources. Which static folder should contain font assets?

## Q0906  _expands Q0328_

This build step changes src/main/resources/static/resources/fonts, and incremental development works best when each change has a visible success condition. Which immediate check should confirm the action completed correctly before the next question? This micro-check belongs specifically to legacy build step Q0328, so it remains tied to that exact PetClinic decision.

## Q0907  _preserved from Q0329_

The source SCSS can be compiled by the Maven css profile into the generated CSS path. Which source directory should contain the SCSS input used by the CSS build?

## Q0908  _expands Q0329_

Before moving away from src/main/scss, which observable state should a developer verify so a later failure is not caused by an unnoticed mistake in this step? This micro-check belongs specifically to legacy build step Q0329, so it remains tied to that exact PetClinic decision.
