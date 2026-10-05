# Validation and Gate 2 preparation

## Purpose

Validate the completed chapter, inspect its rendered form and produce the canonical artefact used for Human Gate 2.

This stage verifies and packages work that has already passed substantive review.

It does not replace:

- scientific review;
- editorial review;
- figure-quality review.

Successful QA and rendering do not establish substantive quality.

# Readiness preflight

Before mechanical validation, confirm that the chapter has:

- an approved `GATE1_PLAN.md`;
- Scientific readiness: `Ready`;
- Editorial readiness: `Ready`;
- Figure readiness: `Ready` when major figures are present;
- resolved citations;
- final figures and tables integrated;
- complete captions and alt text;
- no unresolved placeholders.

Required review records are:

- `chapters/NN_chapter_slug/SCIENTIFIC_REVIEW.md`
- `chapters/NN_chapter_slug/EDITORIAL_REVIEW.md`
- `chapters/NN_chapter_slug/FIGURE_REVIEW.md` when applicable

If a required review is absent or not ready, stop and return the chapter to the relevant workflow stage.

Do not describe the chapter as Gate-2-ready.

# Mechanical QA

Before rendering, run:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md`

Resolve all errors.

Review warnings individually.

Do not suppress a warning merely to obtain a clean report.

Mechanical QA checks technical consistency.

It does not assess scientific, editorial or visual quality.

# Rendering

Render the chapter using the established TeachBooks/Jupyter Book workflow.

Produce:

- rendered HTML;
- canonical review PDF.

The canonical PDF must be:

`book/NN_chapter_slug.pdf`

The Markdown and PDF must share the same basename.

Temporary files under:

`build/`

are disposable and are not Gate 2 deliverables.

Do not modify the public TOC merely to test or render an unpublished chapter.

Use an isolated or temporary rendering configuration where necessary.

# Gate 2 QA

After the canonical PDF exists, run:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md --gate2`

Resolve all errors before proceeding.

Confirm that the command checks the canonical Markdown and PDF rather than a temporary build copy.

# Render inspection

Inspect the actual rendered HTML and PDF.

Do not rely only on:

- build success;
- log output;
- file existence;
- PDF metadata;
- source Markdown;
- figure source files.

Inspect the complete PDF, including:

- chapter number and title;
- heading hierarchy;
- page breaks;
- paragraph spacing;
- figures at placed size;
- figure cropping;
- label legibility;
- captions;
- tables;
- mathematical and chemical notation;
- citation rendering;
- reference list;
- internal links;
- unresolved placeholders;
- obvious layout failures.

Inspect every major figure page at sufficient resolution to judge:

- typography;
- hierarchy;
- colour;
- visual consistency;
- whether the final asset matches the figure that passed review.

If rendering reveals a substantive figure defect, return to figure review.

If rendering reveals generic, repetitive or weak prose missed earlier, return to editorial review.

Do not correct a substantive failure silently inside the validation stage.

After any correction:

- regenerate the affected output;
- rerun the relevant checks;
- reinspect the affected pages.

# Validation record

Create:

`chapters/NN_chapter_slug/VALIDATION_REPORT.md`

Record:

- chapter identity;
- scientific-readiness result;
- editorial-readiness result;
- figure-readiness result;
- figures and tables included;
- mechanical QA command and result;
- rendering method;
- HTML output location;
- canonical PDF location;
- Gate 2 QA command and result;
- pages or outputs inspected;
- corrections made during validation;
- unresolved issues.

Do not state “no unresolved issues” unless substantive and technical checks are complete.

# Definition of v0.1

For this project:

`v0.1 = Gate 1 approved + automated production complete + Gate 2 pending`

A v0.1 chapter must have:

- complete chapter text;
- Scientific readiness: `Ready`;
- Editorial readiness: `Ready`;
- Figure readiness: `Ready` where applicable;
- figures and tables integrated;
- citations resolved;
- mechanical QA passed;
- HTML rendered;
- canonical PDF produced;
- Gate 2 QA passed;
- rendered outputs inspected;
- Gate 2 still pending.

A chapter that is merely complete, accurate or renderable is not v0.1.

v0.1 does not mean published or author-approved.

# Human Gate 2

The primary Gate 2 review artefact is:

`book/NN_chapter_slug.pdf`

Return the PDF together with:

- chapter path;
- canonical PDF path;
- version and status;
- scientific-review result;
- editorial-review result;
- figure-review result;
- figures and tables included;
- QA and render result;
- genuine unresolved issues, if any.

The editor reviews the complete rendered chapter.

Possible decisions:

- approve;
- approve with changes;
- return for revision;
- reject and reconstruct;
- reject and restart from Gate 1.

Corrections remain within Gate 2 unless the editor explicitly returns the chapter to Gate 1.

After corrections, regenerate and reinspect the canonical PDF.

Do not modify the public TOC, publish, commit or push without explicit instruction.