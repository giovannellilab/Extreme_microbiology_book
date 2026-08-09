# Stage 7 — Figures and tables

## Purpose

Plan and produce only visuals that materially improve explanation, comparison or accessibility.

## Requirements

For every proposed figure or table record:

- conceptual purpose;
- question addressed;
- visual logic or comparison dimensions;
- evidence base and any required data;
- caption concept;
- source, authorship and licensing status;
- recommended file format;
- alt text;
- digital and print readability requirements.

Prefer original SVG conceptual diagrams, versionable plotting scripts and concise comparative tables. Ensure legible labels, colour-independent meaning, appropriate contrast and useful rendering at page width.

Avoid decorative images, copied copyrighted figures, large taxonomic catalogues and visuals that merely duplicate prose. Do not recreate published data without checking accuracy, attribution and reuse conditions.

## Required output

Create `chapters/<chapter-slug>/FIGURE_PLAN.md` and, only when requested and approved, the associated assets or plotting scripts. Record final asset paths and caption/alt-text ownership.

## Approval gate

The editor approves the figure plan and any material licensing decisions before assets are treated as final.

## Metadata

New production documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Production artefacts must set `publication_content: false` and `teachbooks_rendered: false`.
