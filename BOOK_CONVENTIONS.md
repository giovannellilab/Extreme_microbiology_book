# BOOK_CONVENTIONS.md

## Purpose

This document defines repository-wide conventions for the production of *Microbiology of Extreme Environments*. It complements, but does not replace:

* `STYLE_GUIDE.md` (writing style and scientific conventions)
* `AGENTS.md` (agent behaviour)
* `workflows/` (chapter production SOPs)

These conventions aim to ensure that the book remains internally consistent across many contributors, editors and AI-assisted production workflows.

---

# Repository structure

The repository distinguishes **production artefacts** from **publication content**.

Production artefacts (source audits, evidence packages, reviews, figure plans, etc.) must never appear in the rendered TeachBooks book.

Chapter files intended for publication live inside the TeachBooks content directory and may remain there while under audit or review. A chapter is rendered and published only when it is listed in `book/_toc.yml`; its location in `book/` does not publish it. No chapter may be added to `book/_toc.yml` before explicit manual editorial approval from Donato Giovannelli, and only Stage 8 may make that TOC change.

Typical structure:

```text
book/
chapters/
workflows/
figures/
references/
```

---

# Chapter filenames

Publication chapters use the convention

```text
NN_short_title.md
```

Examples

```text
01_introduction.md
02_extreme_environments.md
17_psychrophiles.md
18_thermophiles.md
```

Rules

* two-digit numbering
* lowercase
* snake_case
* concise descriptive title
* avoid abbreviations unless universally recognised

Every publication chapter begins with exactly one visible H1 in this form:

```markdown
# NN. Chapter title
```

The H1 number must match the two-digit filename prefix. Its title text must match `chapter_title` in front matter and the canonical TOC title; its chapter identity must also agree with the filename and `chapter_slug`. When a TOC entry has no separate title override, this numbered H1 supplies the rendered chapter title.

---

# Development documents

Working documents remain outside the rendered book.

Typical files include

```text
SOURCE_AUDIT.md
EVIDENCE_PACKAGE.md
EDITORIAL_REPORT.md
SCIENTIFIC_REVIEW.md
EDITORIAL_REVIEW.md
FIGURE_PLAN.md
```

These documents include YAML metadata and are not added to the TeachBooks table of contents.

---

# YAML metadata

All production artefacts begin with YAML front matter.

Publication chapters also include YAML front matter appropriate for TeachBooks.

Minimum metadata:

```yaml
chapter_title:
chapter_slug:
document_type:
workflow_stage:
workflow_version:
document_version:
editor:
status:
created:
last_updated:
publication_content:
teachbooks_rendered:
```

---

# Figures

Figures should be explanatory rather than decorative.

Preferred formats

* SVG (preferred)
* PDF (vector)
* PNG (only when raster is unavoidable)

Naming convention

```text
fig17_01.svg
fig17_02.svg
```

Rules

* one conceptual message per figure
* avoid unnecessary colours
* readable in print
* include descriptive alt text
* maintain editable source whenever possible

A figure is complete only when its scientific concept is approved; one final asset is selected; rejected or intermediate candidates are removed from publication directories or clearly excluded from publication; the final production filename, caption, alt text, prose callout and provenance/licensing are complete; the chapter references that final asset; and the rendered result has been inspected successfully. Generating candidates alone is not completion.

Publication directories must not contain ambiguous competing figure versions without an explicit production reason. Retained editable bases or overlays must be named clearly as source assets.

---

# Tables

Naming convention

```text
tab17_01
tab17_02
```

Tables should summarise concepts or evidence rather than duplicate prose.

---

# Equations

Equations should use LaTeX.

Only number equations that are referenced later.

Variables should follow SI conventions.

---

# Citations

All references are managed through BibTeX.

The manuscript contains citation keys only.

Example

```markdown
...as previously proposed [@cavicchioli2016].
```

Do not manually format references within the text.

The rendered output will use the repository CSL style (Nature-style numbered citations unless changed globally).

---

# Bibliography

Maintain a single central bibliography whenever possible.

Avoid duplicate BibTeX entries.

Every entry should include

* authors
* year
* title
* journal or publisher
* volume
* pages (where available)
* DOI
* URL only when appropriate

Reference metadata must be verified before inclusion.

---

# Internal links

Use relative links and repository-supported cross-references.

Avoid hard-coded URLs to rendered pages.

---

# Cross-references

Cross-reference concepts instead of repeating explanations.

Prefer

> See Chapter X.

rather than reproducing background material.

---

# Boxes

Boxes should be used sparingly.

Appropriate uses include

* historical notes
* representative case studies
* important conceptual warnings
* definitions
* outstanding questions

Boxes are not intended for long digressions.

---

# Representative organisms

Representative organisms illustrate mechanisms.

They should not become taxonomic catalogues.

Each organism included in a chapter should have a clear pedagogical purpose and answer: “Why is this organism the best example here?” Familiarity alone is not sufficient.

---

# Teaching anchors

Each reconstructed chapter should contain approximately five to ten memorable conceptual statements integrated naturally into the prose. They should summarise difficult ideas, make causal relationships explicit, correct misconceptions or connect mechanisms into a general principle. They are not slogans or a separate summary device.

---

# Chapter rhythm

Chapters should alternate explanation, evidence and synthesis. Avoid long uninterrupted blocks of mechanistic detail. Use an essential figure, concise table, representative case or short synthesis paragraph where it materially improves comprehension.

---

# Applications

Applications illustrate biological significance.

Detailed biotechnology belongs in the dedicated applications chapter.

Extremophile chapters should include only a few mechanism-driven examples.

---

# Numbering

Figures

```text
Figure 17.1
Figure 17.2
```

Tables

```text
Table 17.1
Table 17.2
```

Boxes

```text
Box 17.1
```

---

# Language

Writing conventions are defined in `STYLE_GUIDE.md`.

Repository conventions never override the Style Guide.

---

# Workflow

All chapter production follows the SOPs in `workflows/`.

The workflow is:

1. Source audit
2. Editorial approval
3. Evidence package
4. Chapter reconstruction
5. Scientific review
6. Editorial review
7. Figures and tables
8. Final publication

Stages should not normally be skipped.

Human Gate 2 requires passing static QA, a successful repository-system HTML render and a mandatory chapter-review PDF produced through the supported TeachBooks/Jupyter Book route. Both rendered outputs must be inspected for the visible numbered title, figure and table placement, caption association, cropping, legibility, obvious broken references and unresolved placeholders. A missing or failed PDF is a Gate 2 blocker; missing standard dependencies must be resolved rather than used to waive the requirement.

---

# Editorial principle

The objective is not to maximise information.

The objective is to maximise understanding.

Every figure, table, reference, example and paragraph should have a clear pedagogical purpose.

Whenever there is a choice between completeness and clarity, prefer clarity.

When a conceptual diagram can replace a long explanation, prefer a precise figure placeholder to additional prose.
