# CHAPTER_PRODUCTION_PROMPT.md

## Purpose

This is the canonical supervisor prompt for producing one chapter of *Microbiology of Extreme Environments*.

It defines the two human gates and the order of work between them.

Scientific writing, repository structure, figure style and detailed conventions are defined elsewhere:

- `STYLE_GUIDE.md`
- `BOOK_CONVENTIONS.md`
- `FIGURE_STYLE.md`
- `AGENTS.md`

Do not duplicate or reinterpret those rules here.

Use the existing `workflows/` material only as supporting SOPs where useful. The workflow described in this file is authoritative for chapter production.

## Start a chapter

Provide:

Chapter number and title: [NN — Title]
Chapter slug: [slug]
Chapter type: [foundational / metabolism / extremophile / environment / synthesis / other]
Curated source location: [chapter source folder or source-map path]

Then begin with Human Gate 1.

Do not modify the public TOC, publish, commit or push unless explicitly instructed.

# Sources

Use chapter sources in this order:

1. author-provided chapter material, lectures, notes and existing drafts;
2. the author-curated chapter source list;
3. the central bibliography;
4. targeted external literature search when needed.

The curated source list is the intended intellectual starting point for the chapter.

Do not replace it with a generic literature survey.

Use external searching only for genuine needs such as:

- checking records or numerical claims;
- resolving conflicting evidence;
- current taxonomy;
- important recent developments;
- filling an evidence gap required by the approved chapter architecture.

Verify references before adding them to `references/bibliography.bib`.

# Human Gate 1 — chapter architecture

Before drafting the chapter, return a compact Gate 1 package containing:

## Chapter job

One short paragraph explaining what this chapter must teach and how it differs from neighbouring chapters.

## Proposed TOC

The proposed section and subsection structure.

## Learning outcomes

Concise, testable outcomes.

## Representative organisms / case studies

Usually 3–6 where appropriate, each with a clear teaching role.

## Claims needing careful verification

Only important quantitative, ecological, taxonomic or record-level claims likely to need explicit checking.

## Figures and tables

For each proposed major figure or table provide:

- working title;
- what it should teach;
- type of visual;
- intended location in the chapter.

Keep this concise. Detailed figure design happens later under `FIGURE_STYLE.md`.

## Evidence gaps or conflicts

Only issues that could materially change the chapter structure or scientific framing.

Stop here.

Human Gate 1 decision:

- approve;
- approve with changes;
- return for revision.

Do not draft the chapter until Gate 1 is approved.

# Automated production after Gate 1

Once Gate 1 is approved, complete the chapter without further human interruption unless a genuine scientific problem would require changing the approved architecture.

Run the following sequence:

1. evidence synthesis;
2. chapter drafting;
3. independent scientific review;
4. scientific revision;
5. editorial pass;
6. figures and tables;
7. final integration;
8. QA, HTML rendering and PDF generation.

Use the approved Gate 1 architecture as the chapter contract.

## Evidence synthesis

Read and use the complete curated source package.

Identify:

- key mechanisms;
- representative examples;
- important quantitative evidence;
- useful lecture material and analogies;
- evidence boundaries and unresolved questions.

Use targeted external literature only where needed.

Create only the production records that are genuinely useful.

## Drafting

Write the chapter according to:

- the approved Gate 1 architecture;
- `STYLE_GUIDE.md`;
- `BOOK_CONVENTIONS.md`;
- the relevant chapter template where one exists.

Preserve the author's teaching logic and distinctive source selection.

The chapter must begin with:

# NN. Chapter title

The chapter should be independently readable without becoming encyclopaedic.

## Scientific review

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

Focus on scientific correctness, causal coherence, evidence support, representative examples, quantitative claims, overgeneralisation, redundancy and missing conceptual links.

Do not expand the chapter merely because additional literature exists.

## Scientific revision

Resolve the review findings with targeted changes.

Do not reconstruct the chapter unless a genuine structural failure has been identified.

## Editorial pass

Improve clarity, flow and accessibility.

Remove generic filler, unnecessary repetition and review-article accumulation.

Preserve the author's voice and the approved scientific scope.

## Figures and tables

Produce the figures and tables approved at Gate 1.

Follow `FIGURE_STYLE.md`.

A figure is not complete merely because an image has been generated.

Before Gate 2, every final figure must be:

- scientifically checked;
- selected from any candidates;
- assigned a final filename;
- integrated into the chapter;
- accompanied by caption and alt text;
- referenced in the prose;
- rendered successfully.

Do not leave ambiguous competing figure versions in the publication directory.

## Final integration

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

python3 scripts/chapter_qa.py book/NN_chapter_slug.md

Then render the chapter using the repository's established TeachBooks/Jupyter Book workflow.

Produce both:

- rendered HTML;
- canonical review PDF.

The canonical Gate 2 PDF must be:

book/NN_chapter_slug.pdf

Temporary build files under `build/` are not Gate 2 deliverables.

Inspect the HTML and PDF for obvious rendering problems, including:

- correct chapter number and title;
- missing or cropped figures;
- unreadable figure labels;
- broken tables;
- misplaced captions;
- unresolved placeholders;
- broken citations or references.

If the canonical PDF cannot be produced, Gate 2 is blocked.

# v0.1

For this project:

v0.1 = Gate 1 approved + automated production complete + Gate 2 pending

A v0.1 chapter therefore has:

- complete text;
- scientific review and revision completed;
- figures and tables integrated;
- QA passed;
- HTML rendered;
- canonical PDF produced;
- Human Gate 2 still pending.

v0.1 does not mean published or author-approved.

# Human Gate 2 — author review

Gate 2 is review of the complete chapter package.

Return:

1. chapter path;
2. canonical PDF path;
3. chapter version/status;
4. scientific-review result;
5. figures and tables included;
6. QA and render result;
7. remaining genuine scientific uncertainties, if any.

The primary review artefact is:

book/NN_chapter_slug.pdf

Human Gate 2 decision:

- approve;
- approve with changes;
- return for revision.

Requested changes are implemented and the PDF is regenerated.

This remains Gate 2; it does not create additional gates.

After Gate 2 approval, the author may make a final direct edit of the Markdown for voice, wording and teaching refinement.

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

Use a different model only when necessary.

Model allocation must not create additional workflow stages or human gates.