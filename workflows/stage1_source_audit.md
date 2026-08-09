# Stage 1 — Source audit

## Purpose

Map the curated source package onto a coherent chapter job and provisional architecture. This stage identifies the source's teaching logic, strengths, weaknesses, duplication and unsupported claims. It does not write polished chapter prose.

## Inputs

- `AGENTS.md`, `STYLE_GUIDE.md` and the relevant chapter template.
- The complete curated source package, including drafts, lectures, notes, transcripts and explicitly associated material.
- Relevant neighbouring chapters when duplication or terminology conflicts are likely.

## Procedure

1. Register every supplied source and preserve attribution.
2. Reconstruct the central pedagogical argument rather than mechanically polishing source prose.
3. Consolidate the material into no more than 10 major concepts.
4. Classify material as **KEEP**, **CUT**, **MOVE**, **VERIFY** or **GAP**.
5. Identify scientific risks, scope risks, duplication, prerequisites and figure opportunities.
6. Do not search external literature unless the editor explicitly requests it. Put checks into a prioritised verification queue for Stage 3.
7. Treat templates as structural guides, not checklists; omit or merge optional sections when narrative flow improves.

## Required output

Create `chapters/<chapter-slug>/SOURCE_AUDIT.md`, normally 6–10 pages excluding the source register if necessary. Place an editorial summary near the top that states source quality, strongest and weakest areas, approximate usable proportion, work required, risks, recommended decision and confidence.

End the audit with:

- recommended chapter job;
- proposed architecture;
- evidence gaps;
- material to move elsewhere;
- prioritised verification queue.

## Approval gate

The audit proceeds to Stage 2. It does not authorise scientific verification or chapter reconstruction.

## Metadata

New production documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Production artefacts must set `publication_content: false` and `teachbooks_rendered: false`.
