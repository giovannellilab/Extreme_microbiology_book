# Stage 8 — Final publication and build validation

## Purpose

After explicit manual editorial approval by Donato Giovannelli, validate the complete chapter in its publication location, add it to the TeachBooks table of contents, and prepare a reviewable pull request.

## Final checks

1. Verify that Donato Giovannelli has explicitly given manual editorial approval for publication before modifying `book/_toc.yml`. Stage 8 is the only stage permitted to add a new chapter to that file.
2. Confirm the approved chapter number, filename and path inside the actual TeachBooks content directory, then add it to the TeachBooks table of contents once.
3. Confirm the TeachBooks table of contents includes no production artefacts or workflow files.
4. Validate Markdown headings, directives, equations and internal cross-references.
5. Validate the central bibliography, citation keys, rendered citations and reference list.
6. Check DOI metadata and claim–citation alignment for substantive claims.
7. Check internal and external links.
8. Confirm figure paths, captions, alt text, print/digital legibility and source records.
9. Confirm licences, permissions, attribution and contributor metadata.
10. Run the final TeachBooks build and inspect the rendered chapter, navigation, figures, equations and references.
11. Update contributor metadata where approved and prepare a substantive PR description covering science, structure, sources, references, figures, cross-chapter effects and unresolved questions.

## Required output

Produce a clean, build-validated publication chapter and focused pull request. Record the commands run and any warnings that remain.

## Approval and merge gate

Do not add a chapter to `book/_toc.yml` without the explicit manual editorial approval verified above. Agents must not self-merge substantive scientific changes, chapter restructures, major reference changes or new chapters. Merge only after explicit human approval and according to repository policy.

## Metadata

New documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Publication chapters must set `publication_content: true` and `teachbooks_rendered: true`; production artefacts must set both values to `false`.
