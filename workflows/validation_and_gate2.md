# Validation and Gate 2 preparation

## Purpose

Validate the complete chapter and produce the single rendered artefact used for Human Gate 2.

## Mechanical QA

Run:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md`

Resolve errors before proceeding.

## Rendering

Render the chapter using the established TeachBooks/Jupyter Book workflow.

Produce:

- rendered HTML;
- canonical review PDF.

The canonical PDF must be:

`book/NN_chapter_slug.pdf`

The Markdown and PDF must have the same basename.

Temporary files under `build/` are disposable and are not Gate 2 deliverables.

## Render inspection

Inspect the rendered chapter for:

- correct chapter number and title;
- missing or cropped figures;
- unreadable figure text;
- misplaced captions;
- broken tables;
- unresolved placeholders;
- broken citations;
- obvious layout failures.

Correct problems and regenerate the output as necessary.

## v0.1

When this step is complete:

`v0.1 = Gate 1 approved + automated production complete + Gate 2 pending`

The chapter is now ready for Human Gate 2.

## Gate 2

The primary review artefact is:

`book/NN_chapter_slug.pdf`

Return the PDF together with only the essential status information:

- chapter version;
- scientific-review result;
- figures and tables included;
- QA/render result;
- genuine unresolved scientific issues, if any.

The editor reviews the PDF.

Requested corrections are implemented and the PDF regenerated.

This remains Gate 2 until approval.