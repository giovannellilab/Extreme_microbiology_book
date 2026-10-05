# Editorial, figures and integration

## Purpose

Turn the scientifically revised draft into a complete reader-facing chapter suitable for final validation.

This stage includes:

1. independent editorial-quality review;
2. editorial revision;
3. figure and table production;
4. independent figure-quality review;
5. final integration.

It does not create an additional human gate.

Follow:

- `GATE1_PLAN.md`
- `STYLE_GUIDE.md`
- `FIGURE_STYLE.md`
- `BOOK_CONVENTIONS.md`
- the completed scientific review

# Independent editorial review

The editorial reviewer must be independent from the drafting and scientific-revision passes.

Review the complete chapter against:

- its approved purpose and organising principle;
- prerequisite knowledge and exclusions in Gate 1;
- the editorial standards in `STYLE_GUIDE.md`;
- the author’s supplied material and teaching logic.

Test:

- chapter-specific intellectual value;
- authorial voice;
- clarity and flow;
- concision;
- unnecessary definitions;
- duplication of earlier chapters;
- generic filler;
- repeated caveats;
- review-article accumulation;
- weak or process-oriented headings;
- unnecessary sections;
- whether representative examples perform their approved teaching roles;
- whether the chapter could be shortened without losing unique content.

Apply the transfer and deletion tests defined in `STYLE_GUIDE.md`.

Identify material that should be deleted rather than cosmetically rewritten.

Do not treat grammatical correctness as editorial quality.

Do not expand the chapter merely to make its sections appear balanced.

# Editorial review record

Create:

`chapters/NN_chapter_slug/EDITORIAL_REVIEW.md`

For every actionable finding, state:

- location;
- problem;
- required action;
- severity: minor, major or structural.

Finish with:

Editorial quality:

- Distinctive
- Strong
- Generic
- Unsatisfactory

Editorial readiness:

- Ready
- Minor revision
- Major revision
- Reject and reconstruct

A chapter rated `Generic` or `Unsatisfactory` cannot proceed to final integration.

Scientific readiness does not override editorial rejection.

If the approved architecture caused the editorial failure, return to Gate 1.

# Editorial revision

Resolve every editorial finding before final figure integration.

Revision may include:

- deleting generic explanations;
- removing repeated caveats;
- replacing abstract discussion with approved evidence;
- tightening transitions;
- restoring authorial teaching logic;
- renaming headings;
- removing unnecessary sections;
- reducing duplication with other chapters.

Do not alter scientific meaning without verification.

Do not replace every deletion with new text.

If most of the chapter requires replacement, treat the work as reconstruction rather than surgical editing.

Record resolutions in `EDITORIAL_REVIEW.md`.

Editorial revision is complete only when Editorial readiness is `Ready`.

# Figure and table production

Produce the figures and tables approved in:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

Follow:

`FIGURE_STYLE.md`

For every major figure:

- retain the approved scientific question;
- retain the approved production mode;
- use the designated quality references;
- verify the underlying science;
- inspect every candidate visually;
- select one final asset;
- use a stable production filename;
- add controlled labels and annotations;
- prepare a complete caption and alt text;
- integrate the figure into the prose.

Do not replace an approved illustration, photograph or hybrid with a pure vector schematic because it is easier to produce.

If the approved production mode proves scientifically inappropriate, return the proposed change to the editor.

Final publication assets belong in:

`book/figures/`

Clearly distinguish editable source assets from final publication assets.

Do not leave ambiguous competing final versions in the publication directory.

# Figure inspection

Open and inspect the actual figure.

Do not assess visual quality from:

- source code;
- SVG structure;
- filenames;
- metadata;
- successful export;
- successful rendering alone.

Inspect each major figure:

- at full resolution;
- at expected publication size;
- alongside the quality references designated at Gate 1;
- in the rendered chapter when available.

Technical validity is not visual acceptance.

# Figure review record

For chapters containing major figures, create:

`chapters/NN_chapter_slug/FIGURE_REVIEW.md`

The reviewer should be independent from figure production where practical.

For every figure, assess:

- scientific purpose;
- scientific accuracy;
- production-mode compliance;
- visual hierarchy;
- illustration or photographic quality;
- typography and label clarity;
- accessibility;
- consistency with `FIGURE_STYLE.md`;
- consistency with the designated quality references;
- whether it resembles a generic infographic or presentation slide;
- whether it materially improves understanding.

Finish with:

Visual quality:

- Publication quality
- Strong
- Generic
- Unsatisfactory

Figure readiness:

- Ready
- Minor revision
- Major revision
- Reject and regenerate

A figure rated `Generic` or `Unsatisfactory` cannot proceed to Gate 2.

Successful rendering does not override visual rejection.

Record required corrections and their resolution in `FIGURE_REVIEW.md`.

# Tables

Produce only tables approved at Gate 1 or clearly required by the evidence.

A table must:

- enable a useful repeated-field comparison;
- avoid duplicating a figure;
- avoid duplicating surrounding prose;
- avoid becoming an organism or metabolism catalogue;
- include a complete caption;
- be called out in the prose;
- render legibly.

Delete a table when prose or a figure communicates the relationship more clearly.

# Integration

After editorial and figure readiness are both `Ready`:

- integrate final figures and tables;
- resolve citations;
- update the central bibliography;
- remove placeholders;
- check chapter number and title;
- check internal cross-references;
- check figure and table numbering;
- check prose callouts;
- ensure Further Reading is selective;
- confirm that only accepted final assets are referenced.

# Completion condition

This workflow stage is complete only when:

- scientific readiness is `Ready`;
- editorial readiness is `Ready`;
- figure readiness is `Ready` where major figures are present;
- editorial findings are resolved;
- figure findings are resolved;
- final figures and tables are integrated;
- captions, alt text and provenance are complete;
- no unresolved placeholders remain.

The completed chapter may then proceed to:

`workflows/validation_and_gate2.md`