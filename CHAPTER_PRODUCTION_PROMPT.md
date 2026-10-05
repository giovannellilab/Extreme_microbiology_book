# CHAPTER_PRODUCTION_PROMPT.md

## Purpose

This is the canonical supervisor contract for producing one chapter of *Microbiology of Extreme Environments*.

It defines:

- chapter identity;
- source priority;
- the two human gates;
- the mandatory automated production sequence;
- substantive readiness requirements;
- editorial and visual rejection criteria;
- model allocation.

Scientific writing, repository structure, figure style and agent behaviour are defined in:

- `STYLE_GUIDE.md`
- `BOOK_CONVENTIONS.md`
- `FIGURE_STYLE.md`
- the relevant chapter template
- `AGENTS.md`

The workflow described here is authoritative for chapter production.

A chapter is not successful merely because it is scientifically correct, mechanically valid and renderable.

It must also be:

- chapter-specific;
- editorially strong;
- free of generic filler;
- consistent with the cumulative structure of the book;
- visually consistent with the approved figure family.

# 1. Chapter identity

Every chapter has one canonical numbered slug:

`NN_chapter_slug`

The production folder and publication files must use the same identity:

`chapters/NN_chapter_slug/`

`book/NN_chapter_slug.md`

`book/NN_chapter_slug.pdf`

Example:

`chapters/18_thermophiles_and_hyperthermophiles/`

`book/18_thermophiles_and_hyperthermophiles.md`

`book/18_thermophiles_and_hyperthermophiles.pdf`

Do not use unnumbered chapter-production folders.

The chapter number and slug must remain identical across production and publication paths.

# 2. Starting information

Before beginning a chapter, provide:

Chapter number and title: `[NN — Title]`

Canonical chapter slug: `[NN_chapter_slug]`

Chapter type: `[foundational / metabolism / extremophile / environment / synthesis / other]`

Curated source location: `[source folder or source-map path]`

Relevant supplied material: `[lectures / notes / draft / figures / other]`

Neighbouring or prerequisite chapters: `[chapter numbers or filenames]`

Create the production directory:

`chapters/NN_chapter_slug/`

Then begin Gate 1 preparation.

Do not draft chapter prose before Gate 1 approval.

Do not create publication figures before their scientific purpose and production mode are approved at Gate 1.

Do not modify the public TOC, publish, commit or push unless explicitly instructed.

# 3. Source priority

Use sources in this order:

1. author-provided chapter material, lectures, notes and drafts;
2. the author-curated chapter source list;
3. the central bibliography;
4. targeted external literature where needed.

The curated source selection is the intellectual starting point for the chapter.

Do not replace it with a generic literature survey.

Read the complete curated source package before proposing the chapter architecture.

Use external searching only for genuine needs such as:

- checking quantitative claims;
- verifying limits or records;
- resolving conflicting evidence;
- updating taxonomy;
- establishing an important recent development;
- filling an evidence gap required by the approved chapter plan.

Do not broaden the source base merely to make the chapter appear comprehensive.

Verify references before adding them to:

`references/bibliography.bib`

Retain useful verified bibliography records even when a draft is later rejected, unless the editor explicitly requests their removal.

# 4. Human Gate 1 — chapter architecture

Gate 1 has one authoritative human-facing file:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

The supervisor may create supporting internal notes where genuinely useful, but the editor should not need to inspect them.

Gate 1 is an architectural and intellectual decision.

It is not an administrative checkpoint.

A weak Gate 1 plan must be revised before drafting. It must not be approved on the assumption that generic sections can be repaired later.

`GATE1_PLAN.md` must contain the following.

## 4.1 Chapter purpose and unique contribution

State:

- the central scientific question;
- the chapter’s organising principle;
- what the reader should understand after the chapter;
- how the chapter differs from neighbouring chapters;
- why the material requires its own chapter.

Avoid generic purposes such as “introduce”, “provide an overview” or “explain the importance of”.

## 4.2 Knowledge assumed from earlier chapters

List the concepts the chapter will use without re-teaching.

Examples may include:

- redox reactions;
- electron donors and acceptors;
- chemolithotrophy;
- autotrophy and heterotrophy;
- carbon fixation;
- thermodynamic principles;
- chemiosmosis;
- basic cellular structures;
- general ecological terminology.

Identify the chapter that owns each foundational concept where practical.

## 4.3 Concepts explicitly excluded from re-teaching

List:

- foundational explanations that must not be repeated;
- neighbouring-chapter material;
- generic background;
- tangential mechanisms;
- catalogues or surveys that would dilute the chapter.

This section is mandatory.

It should be specific enough to prevent the drafting agent from using excluded material as filler.

## 4.4 Evidence backbone

Identify the small number of sources, observations, experiments, datasets or case studies that will carry the chapter’s argument.

For each evidence anchor, state:

- what it demonstrates;
- where it belongs in the chapter;
- what it does not establish;
- whether its conclusion is site-specific or general.

A broad review may establish the framework, but the chapter should not rely entirely on review-level generalisation.

## 4.5 Proposed architecture

Provide the proposed section and subsection structure.

Use subject-specific working titles.

For every major section, state:

- the scientific question answered;
- the chapter-specific mechanism or pattern developed;
- the evidence anchor;
- representative examples;
- prerequisite concepts assumed rather than re-taught;
- material explicitly excluded;
- why the section is necessary to the chapter’s unique argument.

Do not create a section solely to supply background.

Do not create sections merely because they appear in a chapter template.

Do not use headings that describe authorial caution, writing strategy or evidence management.

Avoid headings such as:

- “Why this matters”;
- “What we can and cannot say”;
- “Significance without overstatement”;
- “A note of caution”;
- “Putting it all together”;
- “Research frontiers” without a more specific scientific subject.

## 4.6 Representative organisms, systems and case studies

Use a small number of examples, each with a defined teaching role.

For every example, state whether it is used to show:

- a mechanism;
- an ecological role;
- a discovery;
- a physiological limit;
- a spatial pattern;
- succession;
- symbiosis;
- environmental contrast;
- a quantitative result.

Do not include examples merely to demonstrate diversity or geographical coverage.

## 4.7 Figures

For every proposed major figure, specify:

- working title;
- scientific question;
- main visual object;
- what the reader must be able to see;
- evidence or source concepts;
- scientific constraints;
- intended production mode;
- successful book figures that provide a quality reference;
- rejected visual approaches.

Production mode must be one of:

- scientific illustration;
- photograph with restrained annotation;
- image-generated scientific illustration with vector/text overlay;
- quantitative plot;
- simple vector schematic;
- hybrid composition.

A pure vector schematic must not replace an approved environmental illustration or hybrid merely because it is easier to generate.

The editor must be able to rewrite or reject the visual concept directly in the Gate 1 file.

## 4.8 Tables

Include only tables that provide a necessary repeated-field comparison.

For every proposed table, explain why prose or a figure would not communicate the relationship more effectively.

Do not propose tables as containers for background, organism lists or metabolic catalogues.

## 4.9 Claims or questions requiring verification

Include only issues that could materially affect:

- scientific framing;
- quantitative claims;
- limits or records;
- taxonomy;
- mechanism;
- interpretation;
- chapter architecture.

Do not turn this section into a general list of scientific caveats.

## 4.10 Author notes and chapter boundaries

Record instructions about:

- emphasis;
- narrative;
- teaching logic;
- terminology;
- source priorities;
- overlap with other chapters;
- material that must remain brief;
- visual direction.

# 5. Gate 1 readiness test

The supervisor must test the Gate 1 plan before presenting it to the editor.

The plan is not ready unless the answer to every relevant question is yes:

- Does the chapter have one recognisable organising principle?
- Is its unique contribution distinct from neighbouring chapters?
- Is prerequisite knowledge explicit?
- Are concepts forbidden from re-teaching explicit?
- Does every major section answer a chapter-specific question?
- Does every major section have an evidence anchor?
- Does every section justify its inclusion?
- Are headings descriptive and scientifically informative?
- Are representative examples assigned clear teaching roles?
- Is generic background embedded only where needed?
- Is the proposed architecture derived from the subject rather than copied from the template?
- Is every major figure tied to a production mode and quality reference?
- Are generic infographic approaches explicitly rejected where inappropriate?
- Could any proposed section be removed without weakening the chapter’s unique argument?

If a section can be removed without weakening the argument, remove or redesign it before Gate 1.

# 6. Gate 1 approval

The editor reviews and directly edits:

`chapters/NN_chapter_slug/GATE1_PLAN.md`

Possible decisions:

- approve;
- approve with edits;
- return for revision;
- reject and redesign.

Once approved, `GATE1_PLAN.md` becomes the authoritative chapter contract.

If a later production record conflicts with the approved Gate 1 plan, the Gate 1 plan takes precedence.

No additional human approval is required before Gate 2 unless:

- a genuine scientific problem requires changing the architecture;
- the approved architecture proves unable to support a chapter-specific draft;
- the approved figure concept proves scientifically inappropriate;
- evidence needed for a central section cannot be verified.

Automated editorial and visual reviews are quality checks, not additional human gates.

# 7. Automated production after Gate 1

After Gate 1 approval, follow these workflow files in order:

1. `workflows/evidence_and_draft.md`
2. `workflows/scientific_review_and_revision.md`
3. `workflows/editorial_figures_integration.md`
4. `workflows/validation_and_gate2.md`

Use the approved `GATE1_PLAN.md` as the authoritative chapter contract throughout.

The automated sequence must not stop merely because a draft exists.

It continues until the chapter passes:

- scientific review;
- scientific revision;
- independent editorial-quality review;
- editorial revision;
- figure-quality review;
- integration;
- mechanical QA;
- rendering;
- final visual inspection.

A technical pass cannot override a substantive failure.

# 8. Evidence synthesis

Read and use the complete curated source package.

Identify:

- key mechanisms;
- representative examples;
- quantitative evidence;
- useful lecture material and analogies;
- evidence boundaries;
- unresolved questions;
- chapter-specific observations;
- material that belongs elsewhere in the book.

Use targeted external literature only where needed.

Do not perform a generic literature review.

Do not add material merely because it is interesting or well documented.

Create only production records that are genuinely useful.

# 9. Drafting

Write the publication chapter at:

`book/NN_chapter_slug.md`

It must begin with:

`# NN. Chapter title`

Follow:

- the approved `GATE1_PLAN.md`;
- `STYLE_GUIDE.md`;
- `BOOK_CONVENTIONS.md`;
- the relevant chapter template.

Preserve the author’s teaching logic and distinctive source selection.

Do not write towards a minimum word count.

Do not fill an approved heading merely because it exists.

If a planned section lacks sufficient chapter-specific evidence, stop and flag the architectural problem instead of filling it with foundational explanation or generic prose.

During drafting:

- use prerequisite knowledge directly;
- cross-reference foundational chapters;
- keep reminders brief;
- centre concrete mechanisms, observations and cases;
- delete paragraphs that fail the transfer test;
- avoid repeated caveats;
- avoid generic transitions and summaries;
- use direct, subject-specific headings.

A chapter may be shorter than expected.

Concise and distinctive is preferable to long and generic.

# 10. Independent scientific review

The scientific reviewer must be independent from the drafting pass.

Review the complete draft against:

- the approved Gate 1 plan;
- the evidence package;
- cited literature;
- current scientific knowledge where verification is required.

Create:

`chapters/NN_chapter_slug/SCIENTIFIC_REVIEW.md`

Focus on:

- factual errors;
- causal coherence;
- outdated claims;
- unsupported generalisations;
- claim–citation mismatch;
- quantitative errors;
- taxonomy and nomenclature;
- incorrect mechanisms;
- overstatement of evidence;
- confusion among detection, survival, activity, growth and reproduction;
- missing caveats that materially affect interpretation.

Do not recommend additions merely to make the chapter more comprehensive.

Report:

Scientific quality:

- Excellent
- Good
- Adequate
- Unsatisfactory

Scientific readiness:

- Ready
- Minor revision
- Major revision
- Reject

“Ready” means scientifically ready only.

It does not imply editorial or visual readiness.

# 11. Scientific revision

Resolve scientific-review findings with targeted corrections.

Do not expand the chapter merely because additional literature exists.

Do not reconstruct a strong chapter unnecessarily.

If the review identifies a structural scientific failure, determine whether it can be corrected within the approved architecture.

If not, return the issue to the editor and reopen Gate 1.

# 12. Independent editorial-quality review

After scientific revision, perform an independent editorial-quality review.

The reviewer must not simply confirm that the prose is grammatical.

Create:

`chapters/NN_chapter_slug/EDITORIAL_REVIEW.md`

Test:

- chapter-specific intellectual value;
- authorial voice;
- clarity;
- flow;
- concision;
- unnecessary definitions;
- duplication of earlier chapters;
- generic filler;
- repeated evidence disclaimers;
- review-article accumulation;
- section-title quality;
- paragraph specificity;
- strength of examples;
- whether the chapter follows the approved organising principle;
- whether the chapter could be shortened without losing unique content.

Apply the transfer test:

> Could this paragraph appear substantially unchanged in another chapter?

Apply the deletion test:

> Would removing this paragraph reduce understanding of the chapter’s unique argument?

Identify text that should be deleted, not merely polished.

Report:

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

A chapter rated Generic or Unsatisfactory cannot proceed to Gate 2.

A chapter rated Reject and reconstruct returns to the approved architecture if that architecture remains sound.

If the architecture itself caused the failure, reopen Gate 1.

Scientific readiness cannot override editorial rejection.

# 13. Editorial revision

Resolve the editorial review before figure integration and final validation.

Revision should:

- remove generic definitions;
- remove filler;
- remove repeated caveats;
- replace abstract explanation with chapter-specific evidence where needed;
- improve directness and flow;
- restore the author’s teaching logic;
- rename weak or process-oriented headings;
- preserve scientific meaning.

Do not lengthen the chapter to replace every deleted paragraph.

Deletion may be the complete correction.

If revision would require replacing most of the chapter, treat the draft as a reconstruction rather than a surgical edit.

# 14. Figures

Produce figures according to the approved Gate 1 concepts and production modes.

Follow:

`FIGURE_STYLE.md`

A major figure is not complete merely because it is:

- scientifically correct;
- technically valid;
- readable;
- uncropped;
- rendered successfully.

For every major figure:

1. verify the scientific concept;
2. use the approved production mode;
3. inspect the actual visual output;
4. compare it with the designated successful book references;
5. reject generic or stylistically inconsistent candidates;
6. select one final asset;
7. integrate accurate labels, caption and alt text;
8. inspect it at publication size.

Environmental illustrations approved as raster, image-generated or hybrid must not be replaced with flat vector schematics without returning the change to the editor.

Do not leave ambiguous competing versions in the publication directory.

Final assets belong in:

`book/figures/`

Editable source files may be retained with clearly identified source filenames.

# 15. Figure-quality review

When a chapter contains major figures, perform a documented figure-quality review.

Create:

`chapters/NN_chapter_slug/FIGURE_REVIEW.md`

For each figure, assess:

- scientific purpose;
- scientific accuracy;
- production-mode compliance;
- visual hierarchy;
- typography at placed size;
- clarity of labels;
- consistency with `FIGURE_STYLE.md`;
- consistency with the designated successful references;
- whether the result resembles a generic infographic;
- whether the image contains decorative or invented scientific detail;
- whether the figure materially improves understanding.

Report:

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

A figure rated Generic or Unsatisfactory cannot proceed to Gate 2.

Correct rendering cannot override visual rejection.

# 16. Tables

Produce only tables approved at Gate 1 or clearly required by later evidence.

A final table must:

- enable a useful repeated-field comparison;
- avoid duplicating a figure or surrounding prose;
- avoid becoming an organism or metabolism catalogue;
- render legibly;
- include a complete caption;
- be called out in the text.

Delete a table when prose communicates the comparison more clearly.

# 17. Final integration

Before validation:

- integrate final figures and tables;
- resolve citations;
- update the central bibliography;
- remove placeholders;
- verify chapter number and title;
- verify internal cross-references;
- verify figure and table numbering;
- verify callouts;
- ensure Further Reading is selective;
- confirm that no rejected figure asset is referenced;
- confirm that scientific, editorial and figure reviews have passed.

# 18. Validation and rendering

Run:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md`

For Gate 2, run:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md --gate2`

Then render the chapter using the established TeachBooks/Jupyter Book workflow.

Produce:

- rendered HTML;
- canonical review PDF.

The canonical Gate 2 PDF must be:

`book/NN_chapter_slug.pdf`

Temporary build files under `build/` are not Gate 2 deliverables.

Inspect the rendered outputs for:

- incorrect title or chapter number;
- missing or cropped figures;
- unreadable labels;
- weak figure placement;
- broken tables;
- misplaced captions;
- unresolved placeholders;
- broken citations or references;
- poor page breaks;
- visually inconsistent figures;
- obvious blocks of generic or repetitive prose.

Mechanical QA confirms technical consistency.

It does not establish scientific, editorial or visual quality.

If the canonical PDF cannot be produced and inspected, Gate 2 is blocked.

# 19. Definition of v0.1

For this project:

`v0.1 = Gate 1 approved + automated production complete + Gate 2 pending`

A v0.1 chapter must have:

- complete text;
- scientific review passed;
- scientific revision completed;
- independent editorial review passed;
- editorial revision completed;
- figures and tables integrated;
- figure-quality review passed where applicable;
- citations resolved;
- QA passed;
- HTML rendered;
- canonical PDF produced;
- final rendered output inspected;
- Gate 2 still pending.

A chapter that is merely complete, accurate and renderable is not v0.1.

v0.1 does not mean published or author-approved.

# 20. Human Gate 2 — author review

Gate 2 has one primary human-facing artefact:

`book/NN_chapter_slug.pdf`

Return the PDF together with:

- chapter path;
- canonical PDF path;
- version and status;
- scientific-review result;
- editorial-review result;
- figure-review result;
- figures and tables included;
- QA and render result;
- genuine unresolved scientific issues, if any.

The editor reviews the rendered chapter.

Possible decisions:

- approve;
- approve with changes;
- return for revision;
- reject and reconstruct;
- reject and restart from Gate 1.

Gate 2 rejection is evidence that the automated quality system failed.

Do not minimise it as a preference or isolated wording issue.

# 21. Reconstructing or restarting a rejected chapter

When the editor rejects a chapter as structurally or editorially weak:

- stop publication work;
- do not perform surgical edits unless requested;
- preserve or export the rejected artefacts if the editor wants a record;
- identify which workflow or Gate 1 assumptions allowed the failure;
- correct the governing workflow before restarting;
- remove rejected chapter prose and figures from the active production state only after backup or explicit approval;
- return to Gate 1 when the architecture is no longer trusted.

A fresh Gate 1 restart must not treat the rejected plan, prose or figures as authoritative source material.

The following may still be reused after verification:

- author-curated sources;
- verified bibliography records;
- source extraction;
- factual evidence notes;
- correctly identified scientific uncertainties.

The following must not constrain the restart:

- rejected section structure;
- rejected prose;
- rejected headings;
- rejected figure compositions;
- claims of readiness from the failed production run.

Do not modify the public TOC during reconstruction.

# 22. Final publication

After Gate 2 approval, the author may make final direct edits to the Markdown.

Publication is a separate technical step and requires explicit instruction.

The publication pass should:

- rebuild outputs;
- verify links and citations;
- verify figures and tables;
- update the public TOC only when authorised;
- avoid introducing substantial new scientific content.

# 23. Model allocation

Use the lightest model capable of each task while protecting scientific, editorial and visual quality.

Default allocation when available:

- Supervisor and orchestration: Sol, HIGH reasoning
- Gate 1 architecture: Sol, HIGH reasoning
- Source inventory and extraction: Luna, MEDIUM reasoning
- Mechanical reference checks: Luna, MEDIUM reasoning
- Evidence synthesis requiring scientific judgement: Sol, HIGH reasoning
- Chapter drafting: Sol, HIGH reasoning
- Independent scientific review: Astra, HIGH reasoning, bounded to the completed draft
- Scientific revision: Sol, HIGH reasoning
- Independent editorial-quality review: independent Sol, HIGH reasoning; escalate to Astra only when necessary
- Editorial revision: Sol, HIGH reasoning
- Figure planning and scientific art direction: Sol, HIGH reasoning
- Image generation: approved image-generation workflow
- Vector labels, overlays and mechanical figure preparation: Luna, MEDIUM reasoning
- Figure-quality review: independent Sol, HIGH reasoning
- Mechanical QA, rendering and build checks: Luna, MEDIUM reasoning

Do not use Luna as the final authority for:

- Gate 1 architecture;
- chapter drafting;
- scientific interpretation;
- editorial acceptance;
- figure art direction;
- figure-quality acceptance.

Changing to a lighter model to conserve usage must not silently lower the acceptance standard.

If a lighter model reaches the limit of its assigned task, escalate the task rather than accepting a weak output.

Model allocation must not create additional human gates.