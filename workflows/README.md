# Chapter-production workflow

The authoritative chapter-production contract is:

`CHAPTER_PRODUCTION_PROMPT.md`

This directory contains short procedures for the automated work between the two human gates.

## Chapter identity

Every chapter uses one canonical numbered slug:

`NN_chapter_slug`

The same identity must be used for:

`chapters/NN_chapter_slug/`

`book/NN_chapter_slug.md`

`book/NN_chapter_slug.pdf`

Do not create unnumbered chapter-production folders.

## Human Gate 1

The single human-facing Gate 1 file is:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

The editor directly edits and approves this file.

Once approved, it is the authoritative contract for chapter production.

## Automated production

After Gate 1 approval, run:

1. `evidence_and_draft.md`
2. `scientific_review_and_revision.md`
3. `editorial_figures_integration.md`
4. `validation_and_gate2.md`

These steps run without further human approval unless a genuine scientific problem requires changing the approved Gate 1 architecture.

## Human Gate 2

The primary Gate 2 review artefact is:

`book/NN_chapter_slug.pdf`

The editor reviews the rendered chapter rather than internal production records.

Requested changes remain within Gate 2 until approval.

## Publication

After Gate 2 approval and explicit instruction, follow:

`publication.md`

## Production records

Internal production records belong in:

`chapters/NN_chapter_slug/`

Create only records that are useful.

The workflow exists to produce the chapter, not to generate documentation about producing the chapter.