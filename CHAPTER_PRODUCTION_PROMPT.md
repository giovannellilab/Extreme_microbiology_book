# Canonical chapter-production supervisor prompt

Use this prompt to supervise production of one chapter in *Microbiology of Extreme Environments*. Replace the bracketed chapter details before starting.

```text
Chapter number and title: [NN — Title]
Chapter slug: [slug]
Chapter type/template: [extremophile / environment / general / other]
Curated source location: [path or connected source folder]
Editor: Donato Giovannelli
```

This is the canonical two-human-gate production contract. Follow `AGENTS.md`, `STYLE_GUIDE.md`, `BOOK_CONVENTIONS.md`, `FIGURE_STYLE.md`, the relevant chapter template and the stage SOPs in `workflows/`. For a chapter explicitly started with this prompt, approval at Human Gate 1 authorises the supervisor to run the existing evidence, reconstruction, review, revision, editorial, figure and validation stages without further human interruption. Stage-level decisions and artefacts remain auditable, but they are not additional human gates. Stop only for Human Gate 2 or for a genuine scientific conflict that would materially change the approved architecture.

Do not modify `book/_toc.yml`, mark a chapter published, commit, push or publish unless Donato Giovannelli has approved Human Gate 2 and explicitly instructed the relevant action. Preserve production artefacts outside the rendered book structure.

## Operating principles

- The supervisor owns scope, sequence, status and integration. Do not proliferate roles or create an elaborate agent hierarchy.
- Preserve the repository architecture and use existing stage artefacts where they remain valid.
- Treat the approved architecture as a contract. A later discovery may refine wording or evidence, but only an architecture-changing scientific conflict returns to the user before Gate 2.
- Prefer deterministic checks and explicit evidence boundaries over claims of completeness.
- Update the chapter's row in `CHAPTER_STATUS.md` when a stage materially changes state.
- Do not invent claims, references, quantitative values, organismal properties or completion states.

## Source precedence

Use sources in this order:

1. Existing chapter-folder material and the lecture, notes, transcript, draft or other source files explicitly associated with the chapter.
2. The chapter's `RECOMMENDED_SOURCES`.
3. The existing book bibliography in `references/bibliography.bib`.
4. Targeted external literature search only when needed to:
   - verify a numerical record;
   - resolve conflicting claims;
   - update taxonomy;
   - verify the current state of knowledge;
   - fill a real evidence gap; or
   - support an approved chapter concept not covered by the source pack.

Do not perform broad literature discovery by default when the curated source pack is sufficient. External searching must have a named claim or approved concept as its purpose. Prefer primary literature for specific experiments and quantitative claims, and authoritative reviews for synthesis. Verify every added bibliography record.

## Preflight

Before substantive work:

1. Read the repository instructions and relevant template completely.
2. Read the complete target chapter if one exists, the complete curated source package and relevant neighbouring chapters where duplication or terminology conflicts are likely.
3. Inspect the repository structure, current bibliography, TeachBooks configuration and public TOC.
4. Inventory existing chapter artefacts and decide which can be reused.
5. Confirm that the chapter is absent from the public TOC unless it is already an approved published chapter.

## Human Gate 1 — architecture approval

Produce a compact, regular Gate 1 package and then stop. Do not draft the publication chapter, produce final figures or begin the full evidence package until the user approves.

Return exactly these sections:

### Chapter job

One short paragraph defining what the chapter must teach and how it differs from neighbouring chapters.

### Proposed TOC

The final proposed section and subsection structure. The template is a guide, not a checklist; merge or omit sections when narrative flow improves.

### Learning outcomes

Concise, testable outcomes describing what the reader should be able to explain, distinguish, predict or evaluate.

### Representative organisms / case studies

Usually three to six where appropriate. Give each a distinct pedagogical role; do not create a taxonomic catalogue.

### Key quantitative or ecological claims requiring verification

List only claims likely to need careful checking, with the endpoint, condition or unit that matters.

### Provisional visual plan

For every proposed major figure or table give:

- working title;
- question answered;
- type: mechanism / environment / comparison / quantitative diagram / photograph / table;
- a two-to-four-sentence concept description;
- why the concept is better represented visually than in prose; and
- intended chapter location.

This plan defines the visual architecture but does not freeze minor compositional decisions.

### Evidence gaps / conflicts

List only issues that could materially alter chapter architecture or scientific framing.

End with: **Human Gate 1 decision required: approve, approve with changes, or return for revision.**

Do not proceed until the user approves Gate 1.

## Post-Gate-1 automated production

After Gate 1 approval, run the following sequence without further human interruption unless a genuine architecture-changing scientific conflict emerges. Record internal findings in the existing chapter production artefacts; do not ask the user to approve routine stage transitions.

### 1. Evidence package

- Inventory all existing chapter sources and preserve provenance and contributor attribution.
- Extract useful claims, examples, analogies and distinctive teaching logic.
- Map claims to sources and distinguish established knowledge, interpretation, hypothesis and speculation.
- Verify high-risk quantitative, taxonomic and ecological claims.
- Use targeted external literature search only where the source-precedence rules permit it.
- Build a concise claim–reference map and a bounded list of unresolved issues.
- Update `references/bibliography.bib` only with verified records actually used by the approved chapter.

### 2. Chapter reconstruction / drafting

- Begin every publication chapter with one visible H1 in the exact form `# NN. Chapter title`. The two-digit number must match the publication filename and chapter identity; the title text must match front matter and the canonical TOC entry.
- Write to the approved job, architecture and learning outcomes.
- Preserve the author's lecture logic, memorable explanations, strong analogies and distinctive material where scientifically defensible.
- Use clear British English for interdisciplinary advanced undergraduate, MSc and early PhD readers.
- Lead with mechanisms and causal sequences rather than catalogues.
- Avoid generic filler, rhetorical boilerplate, fact stacking and review-article accumulation.
- Use concrete examples that perform a defined pedagogical role.
- Preserve local meaning when cross-referencing other chapters.
- Make the chapter independently readable but not independently comprehensive.
- Keep methods only where they help interpret evidence and applications brief and mechanism-led.

### 3. Independent scientific review

Review the complete chapter independently against the evidence package and cited literature. Report findings before revision.

Assign both ratings:

- **Scientific quality:** Excellent / Good / Adequate / Unsatisfactory
- **Publication readiness:** Ready / Minor / Major / Reject

Review specifically for:

- factual correctness and current taxonomy;
- causal coherence;
- representative examples and whether each performs distinct work;
- quantitative and ecological relevance;
- overgeneralisation or inference beyond the evidence;
- unsupported claims and claim–citation mismatch;
- uneven depth among parallel concepts;
- confusing or incomplete mechanisms;
- redundancy and fact stacking;
- abrupt cross-references that remove necessary local explanation; and
- caveats that are scientifically necessary rather than defensive prose.

Classify actionable findings by severity and identify the evidence and bounded corrective action. Do not expand scope merely because more material exists.

### 4. Scientific revision

- Apply a targeted revision against the review findings.
- Do not reconstruct the chapter unless the review identifies a genuine structural failure.
- Preserve strong teaching anchors, contributor insights and the author's voice.
- Record every material review finding and its resolution.

### 5. Editorial pass

Focus on:

- clarity, continuity and causal order;
- accessibility without removal of scientific depth;
- removal of generic or filler sentences;
- comparable depth for parallel mechanisms unless the evidence justifies asymmetry;
- chapter rhythm: explanation, evidence and synthesis;
- avoiding repeated use of the same organism unless the later use genuinely builds on the first; and
- concise, locally meaningful cross-references.

Do not reopen scientific scope during copy-editing.

### 6. Figures and tables

- Use the visual architecture approved at Gate 1 and follow `FIGURE_STYLE.md`.
- Major figures must visualise major chapter concepts, not evidence bookkeeping.
- Begin from the scientific object, environment or dataset rather than from boxes and arrows.
- Use programmatic SVG for quantitative plots and genuinely schematic diagrams.
- Use image generation for illustrated mechanism and environment figures.
- Use a hybrid image-generated base plus vector/text overlays where it improves scientific illustration, typography, axes or annotations.
- Put the figure title inside the figure.
- Use a pure white background and sans serif text.
- Assume a maximum placed width of approximately 180 mm.
- Use no text below 8.5 pt at final size; prefer 9–11 pt labels.
- Do not add decorative or random microorganisms to abstract diagrams.
- Keep figures editable where practical and record source, provenance and licensing.
- Treat a figure as complete only when its scientific concept is approved; one final asset has been selected; rejected or intermediate candidates have been removed from publication directories or clearly excluded from publication; a final production filename has been assigned; caption, alt text, prose callout and provenance/licensing are complete; the chapter references that final asset; and the rendered result has been inspected successfully. Generating one or more candidates does not complete a figure.
- Do not leave ambiguous competing figure versions in publication directories without an explicit production reason. Editable sources must be named clearly as sources rather than as alternative publication assets.
- Produce complete figures before Gate 2. Placeholders do not qualify for Gate 2.

### 7. Final integration

Before Gate 2:

- integrate all figures and tables into the chapter;
- add complete captions and descriptive alt text;
- add meaningful figure and table callouts in the prose;
- verify that figure content and text make the same scientific claim;
- verify provenance, permissions, licensing and attribution;
- resolve all citation keys and update the central bibliography where needed; and
- remove superseded placeholders and production language from publication prose.

### 8. Validation

Run the repository QA command for the chapter:

```bash
python3 scripts/chapter_qa.py book/NN_chapter_slug.md
```

For Gate 2 readiness, rerun QA with the completed PDF artefact:

```bash
python3 scripts/chapter_qa.py book/NN_chapter_slug.md --gate2 --pdf path/to/chapter-review.pdf
```

Static QA must pass before Gate 2. The default build mode runs TeachBooks when its CLI is available and otherwise reports the missing runtime. Before Gate 2, render the chapter with the repository build system. If an unapproved chapter is absent from the public TOC, use an isolated temporary build configuration; do not modify the canonical TOC merely to test rendering.

Every Gate 2 package must include a rendered chapter PDF produced through the repository's supported TeachBooks/Jupyter Book build route. The PDF is mandatory: Gate 2 cannot be marked **READY** when it is absent, and any PDF-build failure is a Gate 2 **BLOCKER** that sets readiness to **BLOCKED**. Missing standard build dependencies must be installed or otherwise resolved within the established toolchain; they are not grounds for waiving the PDF requirement. For the current Jupyter Book `pdfhtml` route, install the repository requirements and run `python -m playwright install chromium` when the Playwright browser runtime is absent.

Inspect the rendered HTML and the complete PDF, not only the source files. Confirm:

- the visible chapter number and title;
- figure and table placement;
- caption association;
- absence of cropping or aspect-ratio distortion;
- legibility at the intended placement size;
- absence of obvious broken references; and
- absence of unresolved placeholders.

Record the HTML build location, exact PDF path, PDF page count and inspection result. Static QA and successful build commands do not by themselves establish visual correctness. Resolve purely mechanical, unambiguous issues, but do not change scientific meaning merely to satisfy a heuristic warning. Distinguish chapter errors, repository-wide errors and pre-existing warnings, and record what static checks, builds and manual render inspection can and cannot establish.

## Human Gate 2 — complete chapter approval

Gate 2 is approval of the complete publication package, not a prose-only review. Present Gate 2 only when:

- the final scientific text is integrated;
- every figure is complete under the final-asset definition above and every table is final or near-final;
- captions are complete;
- alt text is present;
- figure and table callouts are present;
- bibliography entries are verified and citation keys resolve;
- static repository QA passes;
- the repository HTML build has succeeded, the mandatory chapter PDF exists, and both rendered outputs have passed the required inspection;
- remaining genuine scientific uncertainties are listed.

Return the package in a compact review form containing:

1. publication chapter path and version/status;
2. approved job and learning outcomes for reference;
3. figures and tables with final paths and production/provenance status;
4. scientific-review ratings and resolution summary;
5. citation and bibliography status;
6. QA command and result, HTML build status, exact PDF path, PDF page count and visual-inspection result;
7. remaining genuine scientific uncertainties or `none`; and
8. an explicit Gate 2 decision request: approve, approve with changes, or return for revision.

The user reviews:

- scientific accuracy;
- causal and conceptual coherence;
- interdisciplinary accessibility;
- representative examples;
- quantitative and ecological relevance;
- figure–text integration;
- visual scientific accuracy;
- whether figures clarify rather than duplicate prose; and
- voice and pedagogy.

Changes requested at Gate 2 are Gate 2 revision, not a third gate. Repeat the integrated package review after those changes.

After Gate 2 approval:

- allow only technical corrections or changes explicitly requested by the user;
- do not add new science, major sections or new conceptual figures without returning the affected material to the user;
- modify the public TOC, mark the chapter published, commit, push or publish only after explicit instruction and in accordance with Stage 8 and repository policy.

## Permanent pedagogical lessons from the Psychrophiles pilot

Apply these rules explicitly:

- Concrete explanation is better than defensive boilerplate.
- If a sentence could be moved unchanged to another extremophile chapter, make it parameter-specific, move it to its primary conceptual home, or delete it.
- Explain a complex mechanism first as a simple causal chain, then add qualifications and exceptions.
- Give parallel concepts comparable conceptual resolution unless there is a scientific reason not to.
- A representative organism should normally do its main pedagogical work once; a later use must add a genuinely new connection.
- A cross-reference must preserve local meaning in this order: what the concept means here; why it matters here; the specific connection being made; then the deeper treatment elsewhere.
- Avoid fact stacking. Normal section logic is: question or problem → explanatory sequence → examples or evidence → synthesis.
- Preserve memorable lecture and course material when scientifically defensible.
- Include concrete limits and representative organisms in extremophile chapters where relevant.
- Distinguish growth, reproduction, activity, maintenance, survival, viability, detection and biomolecular persistence when discussing limits.
- Ecology must answer “why does this matter on Earth?” through robust, system-specific examples, measurements, processes, reservoirs or effects.
- Do not write generic sentences saying ecological importance “must be demonstrated”; demonstrate it with a bounded example or omit the claim.
- Avoid excessive qualification that weakens clear science. Keep only caveats that change interpretation.

## Default model allocation

Use this allocation when the named models and reasoning levels are available; otherwise use the nearest capable option and record the substitution.

| Work | Default model and effort |
|---|---|
| Supervisor / orchestration | Sol HIGH |
| Source inventory, file inspection, mechanical extraction, duplication checks and routine QA | Luna MEDIUM |
| Evidence synthesis, reference verification, targeted literature and claim–reference mapping | Terra HIGH |
| Chapter reconstruction | Sol HIGH |
| Independent final scientific review | Astra HIGH |
| Scientific revision | Sol HIGH |
| Routine validation and build | Luna MEDIUM |

Escalate model capability or reasoning effort only when the task actually requires it. Model allocation does not create extra human gates or authorise additional scope.
