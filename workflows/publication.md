# Publication

## Purpose

Publish a chapter after Human Gate 2 approval.

Publication is a technical release step, not another scientific-review stage.

Do not publish without explicit instruction.

## Before publication

The editor may make final direct edits to:

`book/NN_chapter_slug.md`

for wording, voice or teaching refinement.

After those edits:

- rerun QA;
- rebuild the chapter;
- regenerate the PDF if required;
- check citations, links, figures and tables.

## Public chapter list

Only after Gate 2 approval should the chapter be added under `book.chapters` in:

`_quarto.yml`

Use the approved chapter number, title and filename, and place it in the correct chapter order.

Do not add production records to `book.chapters`.

## Final check

Confirm:

- canonical Markdown is present;
- final figures are present;
- references resolve;
- the chapter builds correctly;
- the TOC entry is correct;
- no temporary production artefacts are being published.

Then publish through the normal repository workflow.