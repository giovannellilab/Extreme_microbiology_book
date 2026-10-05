# Evidence and draft

## Purpose

Turn the approved Gate 1 architecture into a scientifically supported, chapter-specific draft.

The authoritative input is:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

Follow:

- `AGENTS.md`
- `CHAPTER_PRODUCTION_PROMPT.md`
- `STYLE_GUIDE.md`
- `BOOK_CONVENTIONS.md`
- the relevant chapter template

Do not change the approved architecture unless a scientific or evidential problem requires returning to Gate 1.

# Pre-draft check

Before drafting, confirm that the Gate 1 plan identifies:

- the chapter’s organising principle;
- prerequisite knowledge;
- concepts excluded from re-teaching;
- the scientific question answered by every major section;
- an evidence anchor for every major section;
- representative examples with defined teaching roles;
- figure production modes.

If any of these is materially absent, stop and return the plan for Gate 1 revision.

Do not compensate for a weak section plan with generic background.

# Evidence work

Use sources in this order:

1. author-provided lectures, notes, drafts and other material;
2. author-curated chapter sources;
3. the central bibliography;
4. targeted external literature where needed.

Use external searching only to:

- verify quantitative values;
- verify limits or records;
- resolve conflicting evidence;
- update taxonomy;
- check a specific mechanism;
- establish what an experiment actually demonstrated;
- fill an evidence gap required by the approved plan.

Do not perform a general literature review.

Do not broaden the chapter merely because more literature exists.

# Evidence package

Create:

`chapters/NN_chapter_slug/EVIDENCE_PACKAGE.md`

Organise it by the approved chapter sections.

For every major section, record:

- the scientific question;
- the principal evidence anchor;
- supporting sources;
- important claims requiring verification;
- the endpoint demonstrated by the evidence;
- limits that materially affect interpretation;
- whether conclusions are site-specific or more general.

Keep the evidence package concise.

It is not an annotated bibliography or a catalogue of possible content.

If a planned section lacks a convincing evidence anchor, stop and return the problem to the supervisor.

Do not fill the section with general knowledge.

# References

Verify references before adding them to:

`references/bibliography.bib`

Check as relevant:

- authors;
- title;
- year;
- publication details;
- DOI;
- study site;
- experimental conditions;
- measured endpoint;
- quantitative values.

Use the central bibliography.

Do not create a chapter-specific bibliography.

Do not duplicate existing records unnecessarily.

# Drafting

Write the publication chapter at:

`book/NN_chapter_slug.md`

The chapter must begin with:

`# NN. Chapter title`

Draft each section from:

1. its approved scientific question;
2. its evidence anchor;
3. its representative examples;
4. its connection to the chapter’s organising principle.

Stop when the section’s question has been answered.

Do not write towards a minimum word count.

Do not give every section equal length.

Do not fill an approved heading merely because it exists.

If the available evidence cannot support the planned section, stop and flag the problem instead of adding generic explanation.

# Chapter boundaries

Use prerequisite concepts established elsewhere in the book.

Do not re-teach material listed in Gate 1 as assumed knowledge or excluded content.

Provide only the local orientation needed for the argument, then cross-reference the primary chapter.

Preserve the author’s teaching logic, source priorities and distinctive examples.

Apply the specificity, transfer and deletion tests defined in `STYLE_GUIDE.md`.

# Evidence and uncertainty

State the endpoint actually demonstrated by the evidence.

Place necessary qualifications next to the claims they affect.

Do not repeat general evidence hierarchies or methodological disclaimers throughout the chapter.

Flag unresolved scientific issues rather than inventing answers.

# Figures and tables

Use the figure and table programme approved at Gate 1.

During drafting:

- place figure and table callouts where they support the argument;
- prepare provisional captions or caption briefs;
- identify which prose the figure will replace or clarify;
- retain the approved figure production mode;
- do not create a generic substitute for an approved illustration;
- avoid repeating the same information in prose, figure and table.

Final figure production and visual review occur in:

`workflows/editorial_figures_integration.md`

# Pre-review check

Before scientific review, confirm that:

- every major section answers its approved question;
- every major section uses its evidence anchor;
- citations support the associated claims;
- foundational material has not been re-taught;
- examples retain their assigned teaching roles;
- headings identify scientific content;
- generic background and filler have been removed;
- the chapter follows its organising principle;
- no section was expanded to satisfy an expected length.

Correct failures before handing the draft to scientific review.

# Output

Produce:

- `chapters/NN_chapter_slug/EVIDENCE_PACKAGE.md`
- `book/NN_chapter_slug.md`

The draft must be:

- complete in argument;
- scientifically supportable;
- chapter-specific;
- consistent with the approved Gate 1 architecture;
- ready for independent scientific review.

“Complete” does not mean that every possible topic or template category has been filled.

No human approval is required before the next automated workflow stage unless the Gate 1 architecture must change.