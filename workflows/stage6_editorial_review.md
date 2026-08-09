# Stage 6 — Editorial and accessibility review

## Purpose

Combine pedagogical, accessibility and cross-chapter consistency review into an editor-facing final assessment after scientific issues have been addressed.

## Review questions

- Is the approved chapter job fulfilled?
- Is the causal argument clear?
- Are concepts introduced before use?
- Is the chapter unnecessarily comprehensive?
- Is material duplicated from another chapter?
- Are cross-references accurate and useful?
- Does the prose preserve the book's expert, accessible voice?
- Do examples perform intellectual work?
- Is the chapter rhythm clear?
- Should any section be cut, merged or moved?

Also check terminology, assumed prior knowledge, paragraph progression, headings, tables, boxes, and whether qualifications obscure the main argument. Accessibility means explaining difficult material clearly, not removing scientific depth.

## Required output

Create `chapters/<chapter-slug>/EDITORIAL_REVIEW.md` with:

- an overall assessment;
- required changes grouped by section;
- cross-chapter actions;
- accessibility issues;
- recommended cuts, merges or moves;
- a clear readiness decision for Stage 7.

Apply accepted changes in a separate revision pass where practical.

## Approval gate

The editor must approve the revised narrative before final figures and publication validation proceed.

## Metadata

New production documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Production artefacts must set `publication_content: false` and `teachbooks_rendered: false`.
