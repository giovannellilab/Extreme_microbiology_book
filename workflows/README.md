# Chapter-production workflows

This directory contains the version-controlled Standard Operating Procedures (SOPs) used to turn curated source material into reviewed publication chapters. The workflow may be run manually or coordinated by a supervisor/orchestrator agent. These SOPs may evolve after each pilot chapter as editorial practice improves.

## Production artefacts and publication content

Production artefacts document editorial decisions, evidence and review. They live in a working chapter directory such as `chapters/<chapter-slug>/` and must remain outside the rendered TeachBooks structure. Examples include `SOURCE_AUDIT.md`, `EVIDENCE_PACKAGE.md`, `SCIENTIFIC_REVIEW.md`, `EDITORIAL_REVIEW.md` and `FIGURE_PLAN.md`.

Publication content is the final reader-facing chapter. Its file must live inside the repository's actual book-content directory and use the approved numbered path and established filename convention. Before creating it, inspect the current repository structure and TeachBooks configuration; never infer the path or chapter number from a draft, lecture or workflow file. A chapter file may exist there during Stages 1–7, but it must remain absent from `book/_toc.yml`: its path does not make it rendered or published. Only Stage 8 may add a chapter to the TOC, after verifying explicit manual editorial approval from Donato Giovannelli.

## Stage sequence

1. [Source audit](stage1_source_audit.md)
2. [Editorial review and architecture approval](stage2_editorial_review.md)
3. [Scientific verification and evidence package](stage3_evidence_package.md)
4. [Chapter reconstruction](stage4_chapter_reconstruction.md)
5. [Scientific review](stage5_scientific_review.md)
6. [Editorial and accessibility review](stage6_editorial_review.md)
7. [Figures and tables](stage7_figures_tables.md)
8. [Final publication and build validation](stage8_final_publication.md)

The editor should normally approve the chapter job and architecture after Stage 1 and explicitly authorise Stage 3. Scientific and editorial reviews may require revision before later stages proceed. The editor performs final review before merge, and substantive scientific changes require human approval.

Workflow files and production artefacts must not be added to the TeachBooks table of contents.
