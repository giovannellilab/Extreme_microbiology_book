# AGENTS.md — Instructions for AI agents

This repository contains *Microbiology of Extreme Environments*, an open academic textbook edited by Donato Giovannelli.

Agents must follow:

- `BOOK_CONVENTIONS.md`
- `STYLE_GUIDE.md`
- `FIGURE_STYLE.md`
- `CHAPTER_PRODUCTION_PROMPT.md`

Do not duplicate or reinterpret those rules here.

# Core behaviour

Work conservatively and keep the production system simple.

Do not create new workflow layers, directories, metadata fields, agent roles or supporting files unless they solve a clear and demonstrated need.

Prefer the smallest change that correctly completes the requested task.

Scientific accuracy and explicit instructions from the editor take precedence over automation convenience.

# Scientific work

Never invent:

- references
- DOIs
- quantitative values
- experimental results
- organismal properties
- gene or protein functions
- metabolic pathways
- taxonomic assignments

If something cannot be verified, flag it rather than guessing.

Distinguish clearly among:

- established knowledge
- interpretation
- hypothesis
- speculation

Do not confuse detection, survival, viability, activity, growth and reproduction.

# Source material

Lecture slides, notes, transcripts, existing drafts and curated sources are intellectual source material.

Preserve their:

- reasoning
- examples
- conceptual sequence
- teaching logic
- distinctive scientific angle

Do not mechanically polish source text.

Do not replace distinctive source material with generic textbook prose.

The curated chapter source list is the intended starting point for chapter production. External literature searching should fill real gaps, not replace that selection with a generic survey.

# Writing and editing

Follow `STYLE_GUIDE.md`.

In particular:

- use British English
- explain mechanisms causally
- write for interdisciplinary scientific readers
- prefer representative examples over catalogues
- avoid generic AI prose
- avoid encyclopaedic expansion
- avoid repetitive summaries and filler
- preserve useful analogies when scientifically accurate
- keep cross-references locally understandable

When editing existing prose, preserve strong wording and teaching logic unless there is a reason to change them.

Do not rewrite material merely to make it sound different.

# Chapter production

Follow `CHAPTER_PRODUCTION_PROMPT.md`.

There are two human gates:

- Gate 1 — chapter architecture
- Gate 2 — complete chapter review

Do not introduce additional human approval stages.

After Gate 1 approval, complete the automated production sequence unless a genuine scientific problem would require changing the approved architecture.

A chapter is not Gate-2-ready until the canonical review PDF exists at:

`book/NN_chapter_slug.pdf`

# Figures

Follow `FIGURE_STYLE.md`.

Figures must serve a scientific or pedagogical purpose.

Do not create decorative figures.

Do not treat generated candidates as completed figures.

Only final selected assets should be referenced by publication chapters.

# Repository changes

Keep production artefacts outside the rendered book.

Do not modify:

- the public TOC
- publication status
- licensing
- overall book architecture

unless explicitly instructed.

Do not add a new chapter without explicit editorial approval.

Do not commit, push, merge or publish unless the current task explicitly authorises it.

When asked to make a focused change, do not include unrelated cleanup.

# Validation

Use the repository QA script for mechanical chapter checks:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md`

For Gate 2:

`python3 scripts/chapter_qa.py book/NN_chapter_slug.md --gate2`

Rendering, visual inspection and PDF generation belong to the production workflow, not to the QA script.

# Definition of done

A task is complete when the requested work is actually finished, not when additional process has been created around it.

Before reporting completion, verify only what is relevant to the task.

Do not claim that scientific, visual, build or publication checks passed unless they were actually performed.