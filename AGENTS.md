# AGENTS.md — Instructions for AI Agents

This repository contains *Microbiology of Extreme Environments*, an open, evolving academic textbook edited by Donato Giovannelli.

AI agents working in this repository must follow the rules in this file and in [`STYLE_GUIDE.md`](STYLE_GUIDE.md).

When these instructions conflict with a task prompt, scientific accuracy and explicit instructions from the editor take precedence.

# Chapter-production workflow

The authoritative chapter-production process is defined in [`workflows/`](workflows/README.md). Agents must follow the SOP for the requested stage and must not skip stages without explicit editorial approval. The relevant workflow file overrides generic workflow assumptions.

Maintain the YAML metadata required by the SOPs. Keep production artefacts outside the rendered TeachBooks structure and separate from publication content; never add production artefacts to the TeachBooks table of contents. A chapter file may exist in the book-content directory while under review, but it is rendered only when listed in `book/_toc.yml`. Only Stage 8 may add a chapter to that TOC, and only after explicit manual editorial approval from Donato Giovannelli.

# 1. Core principles

The book is intended for advanced undergraduate, MSc and early PhD students from interdisciplinary scientific backgrounds, including biology, chemistry, geology, Earth sciences, environmental sciences and astrobiology.

Readers should not be assumed to have extensive previous training in microbiology.

The book should be scientifically rigorous but accessible.

It is intentionally **not encyclopaedic**.

Do not add material merely because it could be included.

## Chapter rhythm

The template is a guide rather than a checklist.

Do not create sections simply because they exist in the template.

A strong extremophile chapter typically contains 5–7 substantive sections.

Optional template elements should be merged whenever doing so improves narrative flow.

## Representative systems

Representative organisms are teaching tools.

Introduce them only where they illuminate a mechanism.

Avoid standalone organism catalogues.

## Methods

Methods belong only where they help interpret evidence.

Do not create a standalone methods section unless explicitly requested by the editor.

## Applications

Applications are supporting material.

Their purpose is to demonstrate why a biological mechanism matters.

Avoid catalogues of industrial, medical or commercial applications.

Refer readers to the dedicated biotechnology and applications chapter, `Extremophiles' contributions to society`, for detailed discussion.

Version 1.0 should contain the strongest coherent material currently available. Additional topics and environments can be added in later versions when appropriate expertise and evidence are available.

# 2. Required reading before substantial work

Before modifying scientific content, read:

1. `STYLE_GUIDE.md`
2. the relevant chapter template;
3. the complete target chapter;
4. any source notes, lecture transcripts or source-material files explicitly associated with the chapter;
5. relevant neighbouring chapters when the requested change may cause duplication or terminology conflicts.

Do not modify a chapter solely from a short excerpt when the complete chapter is available.

# 3. Scientific priority

Use the following priority order:

1. scientific accuracy;
2. correct representation of evidence and uncertainty;
3. conceptual clarity;
4. pedagogical usefulness;
5. consistency with the intellectual structure of the book;
6. conciseness;
7. stylistic consistency.

Never preserve wording when doing so would preserve an error.

Never improve style at the expense of scientific precision.

# 4. Source material is not publication-ready prose

Lecture slides, recordings, transcripts, notes and existing drafts are source material.

They may contain:

* transcription errors;
* informal shorthand;
* repetition;
* outdated information;
* teaching simplifications;
* partially developed arguments;
* AI-generated expansions;
* unverified citations.

Do not mechanically polish this material.

Instead:

1. identify the scientific argument;
2. identify useful examples and analogies;
3. reconstruct the conceptual sequence;
4. verify claims when requested or when they appear doubtful;
5. rewrite the material into coherent textbook prose.

Preserve the **reasoning, examples, conceptual sequence and pedagogical intent** of the source.

During chapter reconstruction, preserve memorable explanations, intuitive causal reasoning, elegant transitions and scientifically sound analogies. Integrate approximately five to ten concise teaching anchors that clarify difficult ideas or connect mechanisms, without turning them into slogans.

Do not preserve weak wording merely because it exists.

Do not replace distinctive teaching logic with generic textbook prose.

# 5. Never fabricate scientific information

Never invent:

* references;
* DOIs;
* quantitative values;
* gene or protein functions;
* organismal properties;
* metabolic pathways;
* taxonomic assignments;
* experimental results;
* environmental measurements.

When a claim cannot be verified, mark it explicitly for review.

Use comments such as:

```text
TODO: verify reference
TODO: verify temperature limit
TODO: scientific review required
```

rather than inventing a plausible answer.

# 6. References

AI-generated references must never be accepted without verification.

When adding or checking references:

* prefer primary literature for specific discoveries and experimental claims;
* use authoritative reviews for broad synthesis;
* verify title, authors, year, journal and DOI;
* use the central BibTeX bibliography where available;
* do not duplicate bibliography records unnecessarily;
* do not cite secondary websites when appropriate scientific literature exists.

If browsing or literature verification is outside the scope of the task, flag unsupported claims instead of inventing citations.

# 7. Scientific uncertainty

Distinguish clearly between:

* established knowledge;
* interpretation;
* hypothesis;
* speculation.

Do not convert tentative evidence into certainty.

Be especially conservative when discussing:

* limits of life;
* uncultivated organisms;
* deep biosphere activity;
* origin-of-life scenarios;
* astrobiology;
* environmental processes inferred only from genomic data.

Detection, viability, metabolic activity, growth and reproduction must never be treated as equivalent.

# 8. Causal explanation

Prefer causal explanation over descriptive lists.

For extremophile chapters, use the conceptual logic:

```text
environmental condition
        ↓
physicochemical consequence
        ↓
cellular challenge
        ↓
adaptation
        ↓
ecological/evolutionary consequence
```

For environment chapters:

```text
geological/physical process
        ↓
environmental chemistry
        ↓
energetic opportunities and constraints
        ↓
microbial metabolisms
        ↓
community structure
        ↓
biogeochemical consequences
```

For metabolism chapters:

```text
substrates + environmental conditions
        ↓
chemical reaction
        ↓
thermodynamic and kinetic constraints
        ↓
molecular machinery
        ↓
energy conservation / biomass production
        ↓
environmental consequence
```

# 9. Avoid unnecessary comprehensiveness

Do not create exhaustive:

* taxonomic lists;
* gene catalogues;
* metabolic inventories;
* literature reviews;
* adaptation lists.

Select representative examples that explain general principles. Every organism included must perform an explanatory role; do not include an organism solely because it is well known.

When useful material would interrupt the chapter narrative, propose a:

* concept box;
* case study;
* methods box;
* frontier box;
* application box;
* table.

# 10. Cross-chapter consistency

Do not re-teach foundational concepts unnecessarily.

Important concepts should have a primary home and later chapters should cross-reference them.

Examples include:

* membrane architecture;
* chemiosmosis;
* Gibbs free energy;
* thermodynamics versus kinetics;
* electron donors and acceptors;
* carbon fixation;
* water activity;
* osmotic stress;
* cardinal growth parameters;
* protein stability;
* sequencing terminology.

Before adding a long foundational explanation to an advanced chapter, search the repository for an existing treatment.

# 11. Terminology and nomenclature

Follow `STYLE_GUIDE.md`.

In particular:

* genus and species names are italicised: *Escherichia coli*;
* bacterial and archaeal gene symbols are lowercase italics: *prtC*;
* proteins are roman type with conventional capitalisation: PrtC;
* strains are not italicised;
* chemical formulae use correct subscripts and superscripts;
* SI units are used where appropriate;
* British English is used throughout.

Do not silently change established gene, protein or taxonomic nomenclature merely to impose a generic pattern.

# 12. Style

Write in clear British English.

The prose should sound like an expert scientist explaining a difficult subject clearly to an interdisciplinary reader.

Avoid:

* generic AI prose;
* excessive headings;
* excessive bullet lists;
* repetitive summaries;
* rhetorical filler;
* unsupported superlatives;
* unnecessary adjectives;
* formulaic introductions and conclusions.

Avoid phrases such as:

> It is important to note that...

> Interestingly...

> In today's rapidly evolving field...

unless they genuinely carry meaning.

Do not use a review-article style unless explicitly requested.

# 13. Analogies

Preserve strong teaching analogies when they help understanding.

Examples from the source material include:

* membranes as biological batteries;
* electron bifurcation as a pulley;
* life as an electrical/redox system.

An analogy must always be accompanied by the precise scientific mechanism.

Do not extend analogies beyond where they remain scientifically useful.

# 14. Figures

Agents may:

* propose figures;
* write detailed figure specifications;
* create editable conceptual diagrams when requested;
* identify where a figure would improve comprehension.

Prefer original conceptual figures over copied published figures.

Do not import copyrighted figures without explicit permission or an appropriate licence.

Every proposed figure should have a clear pedagogical purpose.

# 15. Chapter boundaries

Do not create a new chapter simply because sufficient material exists.

New chapters require an explicit editorial decision.

This is particularly important for Part IV, which is intentionally extensible.

A new extreme-environment chapter should normally be added only when:

* the topic materially improves the book;
* sufficient high-quality material exists;
* appropriate expertise is available;
* the chapter has a clear conceptual contribution distinct from existing chapters.

# 16. Editing existing contributions

Respect intellectual contributions already present in the manuscript.

Substantial rewriting is allowed when necessary for coherence, accuracy or style, but agents should preserve:

* original scientific insights;
* useful examples;
* distinctive explanations;
* attribution;
* contributor credit.

Do not erase contributor attribution merely because prose has been substantially edited.

# 17. Git workflow

Unless explicitly instructed otherwise:

* do not commit directly to `main`;
* work on a dedicated branch;
* make focused commits;
* avoid mixing unrelated changes;
* open a pull request;
* explain substantive scientific or structural changes in the PR description.

A substantive chapter rewrite should normally be reviewable independently from infrastructure or formatting changes.

# 18. Pull-request descriptions

For substantive work, describe:

* what changed;
* why it changed;
* what source material was used;
* any scientific claims requiring verification;
* references added or removed;
* figures affected;
* cross-chapter implications;
* unresolved questions.

Do not describe a major conceptual rewrite merely as “cleaned up chapter”.

# 19. Do not self-merge substantive scientific changes

Agents may prepare branches and pull requests.

Substantive scientific changes require human review before integration into the default branch.

Agents must not autonomously merge:

* new scientific claims;
* chapter restructures;
* major reference changes;
* new chapters;
* changes affecting interpretation of evidence.

Mechanical changes may be automated separately if explicitly authorised.

# 20. Appropriate agent tasks

Agents are particularly suitable for:

## Source audit

Map lecture material, notes and drafts onto a chapter structure.

Output:

* concepts present;
* useful examples;
* duplicated material;
* unsupported claims;
* missing concepts;
* candidate figures;
* candidate references requiring verification.

## Chapter reconstruction

Reconstruct an approximately 90% publication-ready chapter from the approved architecture, source audit, evidence package, style guide and chapter template. This is not a new literature review. Preserve the source's strongest scientifically correct teaching logic, use figures instead of unnecessary explanatory expansion, and alternate explanation, evidence and synthesis. Produce both the publication chapter and a concise, non-rendered `EDITORIAL_REPORT.md` for the editor.

## Reference audit

Identify:

* unsupported claims;
* missing references;
* duplicate references;
* questionable references;
* references requiring DOI verification.

Do not fabricate replacements.

## Accessibility review

Read the chapter from the perspective of a scientifically literate reader with limited microbiology training.

Identify concepts that are used before being explained.

## Cross-chapter review

Identify:

* duplicated explanations;
* conflicting definitions;
* inconsistent nomenclature;
* concepts introduced in the wrong order.

## Figure planning

Produce figure specifications including:

* question addressed;
* visual structure;
* labels;
* data requirements;
* caption concept;
* source/licensing considerations.

## Technical validation

Check:

* Markdown structure;
* links;
* citations;
* references;
* figure paths;
* TeachBooks/Jupyter Book build;
* spelling and nomenclature.

# 21. Tasks requiring particular caution

Do not autonomously:

* determine authorship or contributor status;
* classify scientific contributions as major or minor;
* resolve disputed scientific interpretations;
* remove contributors;
* change licensing terms;
* change the overall book architecture;
* add new chapters to the official table of contents;
* substantially alter the pedagogical philosophy.

These decisions belong to the editor.

# 22. Definition of done

A chapter is not complete merely because its prose reads well.

Before declaring work complete, check:

* scientific claims are supported or flagged;
* uncertainty is represented correctly;
* terminology follows the style guide;
* causal reasoning is clear;
* avoidable duplication has been removed;
* source material has been represented faithfully;
* references are verified or explicitly marked for checking;
* figures and tables serve a pedagogical purpose;
* Markdown builds correctly;
* unresolved issues are documented.

When uncertain, flag the issue for human review rather than silently making a high-impact assumption.
