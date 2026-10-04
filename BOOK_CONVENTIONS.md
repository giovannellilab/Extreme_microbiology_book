# BOOK_CONVENTIONS.md

## Purpose

This file defines the repository and publication conventions for *Microbiology of Extreme Environments*.

Writing style is defined in `STYLE_GUIDE.md`.

Figure style is defined in `FIGURE_STYLE.md`.

Agent behaviour is defined in `AGENTS.md`.

Chapter production is defined in `CHAPTER_PRODUCTION_PROMPT.md`.

Keep this file limited to repository structure, canonical artefacts and publication state.

# Repository structure

Publication content lives in:

`book/`

Chapter-production records live in:

`chapters/`

Shared references live in:

`references/`

Production scripts live in:

`scripts/`

Temporary build output may live in:

`build/`

Anything under `build/` is disposable and is not a canonical publication artefact.

ach chapter-production directory must use the same canonical numbered slug as the publication chapter:

`chapters/NN_chapter_slug/`

For example:

`chapters/18_thermophiles_and_hyperthermophiles/`

corresponds to:

`book/18_thermophiles_and_hyperthermophiles.md`

Do not create unnumbered production folders.

# Chapter files

Publication chapters use:

`NN_chapter_slug.md`

Examples:

`17_psychrophiles.md`

`18_thermophiles_and_hyperthermophiles.md`

`28_deep_sea_hydrothermal_vents.md`

Rules:

- two-digit chapter number
- lowercase
- snake_case
- concise descriptive slug

Every chapter begins with exactly one visible H1:

`# NN. Chapter title`

The following must agree:

- chapter number
- filename
- `chapter_title`
- `chapter_slug`
- visible H1
- canonical TOC

# Canonical chapter artefacts

For every chapter reaching Gate 2, the canonical review files are:

`book/NN_chapter_slug.md`

`book/NN_chapter_slug.pdf`

The Markdown and PDF must share the same basename.

Example:

`book/18_thermophiles_and_hyperthermophiles.md`

`book/18_thermophiles_and_hyperthermophiles.pdf`

Temporary build files such as:

`build/chapter18/_build/pdf/book.pdf`

are internal build artefacts only.

They do not count as the final Gate 2 PDF.

# Publication state

A chapter may exist in `book/` without being published.

A chapter is part of the public book only when it is included in:

`book/_toc.yml`

Do not add a chapter to the public TOC merely to test rendering.

Publication requires explicit author approval.

# Human gates and v0.1

The project uses two human gates.

## Gate 1

Gate 1 approves chapter architecture before drafting.

## v0.1

For this project:

`v0.1 = Gate 1 approved + automated production complete + Gate 2 pending`

A v0.1 chapter must have:

- complete text
- scientific review and revision completed
- figures and tables integrated
- citations resolved
- QA passed
- HTML rendered
- canonical PDF produced

## Gate 2

Gate 2 is author review of the complete chapter package.

The primary Gate 2 review artefact is:

`book/NN_chapter_slug.pdf`

Gate 2 may require revision and regeneration of the PDF.

It remains the same gate until approved.

# Figures

Publication figures live in:

`book/figures/`

Use stable names such as:

`fig18_01_cardinal_temperatures.svg`

`fig18_02_cellular_adaptations.png`

Editable source files may be retained where useful, but must be clearly marked as sources, for example:

`fig18_02_cellular_adaptations_source.svg`

Publication chapters must reference only the selected final assets.

Detailed visual rules are defined in `FIGURE_STYLE.md`.

# Tables

Number tables by chapter:

`Table 18.1`

`Table 18.2`

Tables should be integrated directly into the chapter unless there is a clear technical reason to store them separately.

# References

The central bibliography is:

`references/bibliography.bib`

The citation style is:

`references/nature.csl`

Do not create separate chapter bibliographies.

Do not duplicate bibliography records unnecessarily.

# Production records

Production records remain outside `book/`.

Typical examples include:

`EVIDENCE_PACKAGE.md`

`SCIENTIFIC_REVIEW.md`

`REVISION_CHANGELOG.md`

`VALIDATION_REPORT.md`

Create only records that are useful.

Do not create files merely to satisfy a workflow formality.

# Internal links

Use relative repository links where practical.

Do not hard-code rendered website URLs when a repository-relative reference is sufficient.

# Final publication

After Gate 2 approval, the author may make final direct edits to the Markdown.

The publication pass should then be primarily technical:

- rebuild
- check links and citations
- verify figures and tables
- update TOC
- regenerate required outputs

Do not introduce substantial new scientific content during the publication pass without returning it to author review.

# Editorial principle

Keep the repository simple.

Prefer one clear convention over multiple parallel mechanisms.

Do not add new workflow layers, directories, metadata fields or production artefacts unless they solve a real problem.