# Stage 4 — Chapter reconstruction

## Purpose

Reconstruct the best possible textbook chapter from approved editorial decisions and verified evidence. Stage 4 is chapter reconstruction, not creative writing, generic drafting or a new open-ended literature review. The reconstruction agent assembles the approved architecture, `SOURCE_AUDIT.md`, `EVIDENCE_PACKAGE.md`, `STYLE_GUIDE.md` and relevant chapter template into a coherent publication chapter.

The target is a chapter that is approximately 90% publication-ready. Work remaining after Stage 4 should consist primarily of scientific corrections, editorial refinement and figure production; major structural rewriting should be exceptional.

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
- Preserve contributor attribution and the strongest scientifically correct pedagogical logic from the source, including memorable explanations, intuitive causal reasoning, elegant transitions and useful analogies.
- Remove transcript artefacts, informal repetition and unsupported statements; the polished chapter should retain the intellectual character of the original course rather than its incidental wording.
- Flag unresolved scientific issues instead of inventing content.

For extremophile chapters, five to seven substantive sections are normally sufficient. Do not create a standalone methods section unless explicitly approved. Embed representative organisms as mechanistic case studies rather than a catalogue. Every organism must perform an explanatory role and answer the implicit question, “Why is this the best example here?” Familiarity alone is not a reason for inclusion. Keep applications brief and mechanism-led; move substantial biotechnology to the dedicated applications chapter.

### Teaching anchors

Develop approximately five to ten memorable conceptual statements across the chapter. Each teaching anchor should arise naturally from the prose and do at least one of the following:

- summarise a difficult idea;
- express a causal relationship;
- correct a common misconception;
- connect mechanisms into a general principle.

Teaching anchors are not slogans, call-outs or a separate list. They should be concise sentences integrated where the corresponding idea is explained.

### Figure-first explanation

Recognise when a conceptual diagram would explain a relationship more effectively than additional prose. Where a figure could replace a long explanation, insert a precise figure placeholder and keep the prose focused. List only essential figures in the Editorial Report; the objective is understanding, not word count.

### Chapter rhythm

Alternate explanation, evidence and synthesis. Avoid long uninterrupted blocks of mechanistic detail. Where appropriate, use an essential figure, a concise table, a representative case or a short synthesis paragraph to restore rhythm without fragmenting the narrative.

## Required output and gate

Stage 4 always produces two deliverables:

1. A complete publication chapter ready for independent scientific review. Set its status to `under review`.
2. `EDITORIAL_REPORT.md`, stored with the chapter's production artefacts and excluded from the TeachBooks table of contents. It is for the editor, normally one or two pages, and must set `publication_content: false` and `teachbooks_rendered: false`.

The Editorial Report must contain:

- **Editorial summary** — no more than 250 words, covering overall reconstruction quality, confidence and remaining weaknesses.
- **Major editorial decisions** — concepts merged, material removed or moved, evidence reinterpreted and duplication eliminated.
- **Material intentionally omitted** — exclusions and their reasons, such as duplication, outdated science, scope or insufficient evidence.
- **Essential figures** — only figures necessary for understanding, each with one sentence stating its pedagogical purpose.
- **Remaining scientific uncertainties** — unresolved issues inherited from the Evidence Package.
- **Recommendations for Stage 5** — sections or claims requiring particular attention in scientific review.

Do not treat successful reconstruction as scientific approval.

## Metadata

New documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Publication chapters must set `publication_content: true` and `teachbooks_rendered: true`; production notes must set both values to `false`.

## Validation

Before hand-off:

- confirm that the publication chapter, and no production artefact, appears in the TeachBooks table of contents;
- validate Markdown, metadata, citations, internal links and figure paths;
- run the available TeachBooks build and distinguish new errors from pre-existing warnings;
- confirm that the Editorial Report reflects the reconstructed chapter and the unresolved Evidence Package items;
- confirm that existing workflow references remain valid.
