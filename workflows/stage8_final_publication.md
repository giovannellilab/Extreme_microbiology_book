# Stage 8 — Final publication and build validation

## Purpose

Validate the complete chapter in its publication location, prepare a reviewable pull request and obtain human approval before merge.

## Final checks

1. Confirm the chapter's approved number, filename and path inside the actual TeachBooks content directory.
2. Confirm the TeachBooks table of contents includes the publication chapter once and includes no production artefacts or workflow files.
3. Validate Markdown headings, directives, equations and internal cross-references.
4. Validate the central bibliography, citation keys, rendered citations and reference list.
5. Check DOI metadata and claim–citation alignment for substantive claims.
6. Check internal and external links.
7. Confirm figure paths, captions, alt text, print/digital legibility and source records.
8. Confirm licences, permissions, attribution and contributor metadata.
9. Run the final TeachBooks build and inspect the rendered chapter, navigation, figures, equations and references.
10. Update contributor metadata where approved and prepare a substantive PR description covering science, structure, sources, references, figures, cross-chapter effects and unresolved questions.

## Required output

Produce a clean, build-validated publication chapter and focused pull request. Record the commands run and any warnings that remain.

## Approval and merge gate

The editor performs final review. Agents must not self-merge substantive scientific changes, chapter restructures, major reference changes or new chapters. Merge only after explicit human approval and according to repository policy.

## Metadata

New documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Publication chapters must set `publication_content: true` and `teachbooks_rendered: true`; production artefacts must set both values to `false`.
