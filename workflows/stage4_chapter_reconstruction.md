# Stage 4 — Chapter reconstruction

## Purpose

Reconstruct the publication chapter from the approved editorial and scientific package. This is not generic writing and not a new open-ended literature review.

## Required inputs

- Approved architecture.
- `SOURCE_AUDIT.md`.
- `EVIDENCE_PACKAGE.md`.
- `STYLE_GUIDE.md`.
- `AGENTS.md`.
- The relevant chapter template.

Resolve a genuinely missing claim through a narrowly targeted check or flag it for review; do not reopen Stage 3 by default.

## Repository placement

Before choosing a path, inspect the current repository tree, TeachBooks configuration and table of contents. Determine the actual book-content directory, approved chapter number and established filename convention. Never guess the final path or number from lecture numbering, production folders or templates.

Place the final Markdown chapter at the approved numbered path inside the actual TeachBooks content directory and add it to the relevant TeachBooks table of contents. Production artefacts remain outside that directory and outside the TOC.

## Reconstruction requirements

- Preserve the approved chapter job and architecture.
- Build causal explanations from the verified evidence rather than copying source prose.
- Use working citations and descriptive internal cross-references.
- Follow British English, nomenclature, SI units, chemical notation and Markdown conventions.
- Preserve contributor attribution and distinctive teaching logic.
- Flag unresolved scientific issues instead of inventing content.

For extremophile chapters, five to seven substantive sections are normally sufficient. Do not create a standalone methods section unless explicitly approved. Embed representative organisms as mechanistic case studies rather than a catalogue. Keep applications brief and mechanism-led; move substantial biotechnology to the dedicated applications chapter.

## Required output and gate

Produce a complete draft publication chapter ready for independent scientific review. Set its status to `under review`. Do not treat successful reconstruction as scientific approval.

## Metadata

New documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Publication chapters must set `publication_content: true` and `teachbooks_rendered: true`; production notes must set both values to `false`.
