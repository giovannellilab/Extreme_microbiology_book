# CHAPTER_PRODUCTION_PROMPT.md

## Purpose

This is the canonical supervisor prompt for producing one chapter of *Microbiology of Extreme Environments*.

It defines:

- the two human gates;
- the chapter identity convention;
- the order of work between the gates.

Scientific writing, repository structure, figure style and agent behaviour are defined in:

- `STYLE_GUIDE.md`
- `BOOK_CONVENTIONS.md`
- `FIGURE_STYLE.md`
- `AGENTS.md`

The workflow described here is authoritative for chapter production.

# Chapter identity

Every chapter has one canonical numbered slug:

`NN_chapter_slug`

The production folder and publication file must use the same identity.

Example:

`chapters/18_thermophiles_and_hyperthermophiles/`

`book/18_thermophiles_and_hyperthermophiles.md`

`book/18_thermophiles_and_hyperthermophiles.pdf`

Do not use unnumbered chapter-production folders such as:

`chapters/thermophiles/`

The chapter number and slug must remain identical across production and publication paths.

# Start a chapter

Provide:

Chapter number and title: [NN — Title]

Canonical chapter slug: [NN_chapter_slug]

Chapter type: [foundational / metabolism / extremophile / environment / synthesis / other]

Curated source location: [source folder or source-map path]

Create the production directory:

`chapters/NN_chapter_slug/`

Then begin Gate 1 preparation.

Do not draft the chapter before Gate 1 approval.

Do not modify the public TOC, publish, commit or push unless explicitly instructed.

# Sources

Use sources in this order:

1. author-provided chapter material, lectures, notes and drafts;
2. the author-curated chapter source list;
3. the central bibliography;
4. targeted external literature search where needed.

The curated source list is the intellectual starting point for the chapter.

Do not replace it with a generic literature survey.

Use external searching only for genuine needs such as:

- checking quantitative claims;
- verifying limits or records;
- resolving conflicting evidence;
- current taxonomy;
- important recent developments;
- filling an evidence gap required by the chapter plan.

Verify references before adding them to:

`references/bibliography.bib`

# Human Gate 1 — chapter plan

Gate 1 has one authoritative human-facing file:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

The supervisor may create supporting internal production records where useful, but the editor should not need to inspect them.

`GATE1_PLAN.md` must contain:

## Chapter purpose

A short statement of what the chapter must teach and how it differs from neighbouring chapters.

## Proposed structure

The proposed section and subsection structure.

For each major section, include the main concepts and examples expected there.

## Concepts that must be included

Important scientific or pedagogical points that must appear in the chapter.

## Concepts to exclude, minimise or move elsewhere

Material that would duplicate another chapter, broaden scope unnecessarily or distract from the chapter's main purpose.

## Representative organisms, systems or case studies

Usually a small number of examples, each with a clear teaching role.

## Figures

For each proposed major figure:

- working title;
- scientific point;
- what should be shown;
- any important constraints.

The editor must be able to rewrite or replace figure ideas directly in this file.

## Tables

Include only tables that are likely to add clear conceptual value.

## Sources to prioritise

List specific papers, reviews, books or supplied sources that should play an important role.

Include why each source matters where useful.

## Claims or questions requiring verification

Only issues that could materially affect scientific framing, quantitative claims, limits, taxonomy or chapter structure.

## Author notes

Any additional instructions about emphasis, narrative, teaching logic or chapter boundaries.

# Gate 1 approval

The editor reviews and directly edits:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

Possible decisions:

- approve;
- approve with edits;
- return for revision.

Once approved, `GATE1_PLAN.md` becomes the authoritative chapter contract.

If a later production record conflicts with the approved Gate 1 plan, the Gate 1 plan takes precedence.

No additional human approval is required before Gate 2 unless a genuine scientific problem would require changing the approved architecture.

# Automated production after Gate 1

Once Gate 1 is approved, complete the chapter without further human interruption.

The production sequence is:

1. evidence synthesis;
2. chapter drafting;
3. independent scientific review;
4. scientific revision;
5. editorial pass;
6. figures and tables;
7. final integration;
8. QA, HTML rendering and PDF generation.

Use the approved `GATE1_PLAN.md` as the chapter contract throughout.

# Evidence synthesis

Read and use the complete curated source package.

Identify:

- key mechanisms;
- representative examples;
- important quantitative evidence;
- useful lecture material and analogies;
- evidence boundaries;
- unresolved questions.

Use targeted external literature only where needed.

Create only internal production records that are genuinely useful.

# Drafting

Write the chapter according to:

- the approved `GATE1_PLAN.md`;
- `STYLE_GUIDE.md`;
- `BOOK_CONVENTIONS.md`;
- the relevant chapter template.

Preserve the author's teaching logic and distinctive source selection.

The publication chapter must be:

`book/NN_chapter_slug.md`

and begin with:

`# NN. Chapter title`

The chapter should be independently readable without becoming encyclopaedic.

# Scientific review

Review the complete draft independently against the evidence.

Report:

Scientific quality:

- Excellent
- Good
- Adequate
- Unsatisfactory

Publication readiness:

- Ready
- Minor
- Major
- Reject

Focus on:

- scientific correctness;
- causal coherence;
- evidence support;
- representative examples;
- quantitative claims;
- overgeneralisation;
- redundancy;
- missing conceptual links.

Do not expand the chapter merely because more literature exists.

# Scientific revision

Resolve the scientific review findings with targeted changes.

Do not reconstruct the chapter unless a genuine structural failure has been identified.

If a required change would materially alter the approved Gate 1 architecture, stop and return the issue to the editor.

# Editorial pass

Improve:

- clarity;
- flow;
- accessibility;
- concision.

Remove:

- generic filler;
- unnecessary repetition;
- review-article accumulation.

Preserve the approved scientific scope and authorial teaching logic.

# Figures and tables

Produce the figures and tables approved at Gate 1.

Follow `FIGURE_STYLE.md`.

A figure is complete only when it is:

- scientifically checked;
- selected from any candidates;
- assigned a final filename;
- integrated into the chapter;
- accompanied by caption and alt text;
- referenced in the prose;
- rendered successfully.

Do not leave ambiguous competing figure versions in the publication directory.

# Final integration

Before Gate 2:

- integrate all figures and tables;
- resolve citations;
- update the central bibliography;
- remove placeholders;
- verify chapter number and title;
- verify internal cross-references;
- verify figure and table callouts.

# Validation and rendering

Run:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md`

Then render the chapter using the established TeachBooks/Jupyter Book workflow.

Produce:

- rendered HTML;
- canonical review PDF.

The canonical Gate 2 PDF must be:

`book/NN_chapter_slug.pdf`

Temporary build files under `build/` are not Gate 2 deliverables.

Inspect the rendered outputs for obvious problems including:

- incorrect title or chapter number;
- missing or cropped figures;
- unreadable labels;
- broken tables;
- misplaced captions;
- unresolved placeholders;
- broken citations or references.

If the canonical PDF cannot be produced, Gate 2 is blocked.

# v0.1

For this project:

`v0.1 = Gate 1 approved + automated production complete + Gate 2 pending`

A v0.1 chapter has:

- complete text;
- scientific review and revision completed;
- figures and tables integrated;
- QA passed;
- HTML rendered;
- canonical PDF produced;
- Gate 2 still pending.

v0.1 does not mean published or author-approved.

# Human Gate 2 — author review

Gate 2 has one primary human-facing artefact:

`book/NN_chapter_slug.pdf`

Return only the essential status information together with the PDF path:

- chapter path;
- canonical PDF path;
- version/status;
- scientific review result;
- figures/tables included;
- QA/render result;
- remaining genuine scientific uncertainties, if any.

The editor reviews the rendered PDF.

Possible decisions:

- approve;
- approve with changes;
- return for revision.

Requested changes are implemented and the PDF is regenerated.

This remains Gate 2 and does not create additional human gates.

After Gate 2 approval, the author may make final direct edits to the Markdown for voice, wording and teaching refinement.

Final publication is a separate technical step and requires explicit instruction.

# Model allocation

Use these defaults when available:

- Supervisor / orchestration: Sol HIGH
- Source inventory and routine mechanical work: Luna MEDIUM
- Evidence synthesis and reference verification: Terra HIGH
- Chapter drafting: Sol HIGH
- Independent scientific review: Astra HIGH
- Scientific revision: Sol HIGH
- Routine QA and build: Luna MEDIUM

Model allocation must not create additional workflow stages or human gates.