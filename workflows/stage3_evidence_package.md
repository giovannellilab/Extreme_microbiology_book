# Stage 3 — Scientific verification and evidence package

## Purpose

Create the scientific contract for the reconstruction agent. The evidence package decides which evidence deserves to support the approved chapter; it is not a comprehensive literature review and must not change the approved architecture.

## Inputs

- The editorially approved `SOURCE_AUDIT.md` and architecture.
- The curated source package.
- `AGENTS.md`, `STYLE_GUIDE.md` and the relevant template.

## Research boundaries

Use targeted searches only to verify claims, update outdated information, resolve conflicts, locate important primary studies and fill genuine evidence gaps. Prefer primary papers for specific claims, authoritative reviews for synthesis and recent high-quality updates where needed. Do not expand chapter scope or accumulate references without a clear chapter use.

## Required output

Create `chapters/<chapter-slug>/EVIDENCE_PACKAGE.md`, normally 10–15 pages, containing:

1. Executive editorial summary.
2. Reading priority: essential, supporting and background.
3. Verified terminology.
4. Evidence organised by each approved chapter section, including claims, qualifications, representative evidence, at most one or two systems where helpful, material to avoid and figure opportunities.
5. Claims requiring careful wording, with preferred and rejected formulations.
6. Concise claim–reference matrix.
7. Figure evidence.
8. No more than four representative case studies, each with a distinct teaching purpose.
9. Remaining scientific, evidential and editorial uncertainties.
10. Explicit instructions for the reconstruction agent: do, avoid, cross-reference and remember.

Update the central BibTeX bibliography with verified references. If no central bibliography exists, create `chapters/<chapter-slug>/REFERENCES_TO_IMPORT.bib` containing only references used in the package.

## Approval gate

The editor or designated scientific lead reviews unresolved decisions before Stage 4. An evidence package does not itself authorise reconstruction.

## Metadata

`EVIDENCE_PACKAGE.md` and any new production document must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Production artefacts must set `publication_content: false` and `teachbooks_rendered: false`.
