# Scientific review and revision

## Purpose

Independently test the complete chapter for scientific accuracy, then correct the identified problems.

This stage assesses scientific quality only.

It does not assess final editorial quality, figure quality, rendering or Gate 2 readiness.

The authoritative inputs are:

- `chapters/NN_chapter_slug/GATE1_PLAN.md`
- `chapters/NN_chapter_slug/EVIDENCE_PACKAGE.md`
- `book/NN_chapter_slug.md`
- cited scientific literature
- the governing repository files

# Independent review

The scientific reviewer must be independent from the drafting pass.

The reviewer must test the chapter’s claims rather than reproduce the drafter’s reasoning.

Check the complete chapter against the approved Gate 1 purpose, evidence package and cited literature.

Focus on:

- factual errors;
- outdated claims;
- unsupported generalisations;
- claim–citation mismatches;
- quantitative errors;
- taxonomy and nomenclature;
- incorrect mechanisms;
- causal errors;
- overstatement of evidence;
- inappropriate extrapolation from one site or study;
- confusion among detection, survival, viability, activity, maintenance, growth and reproduction;
- missing qualifications that materially alter interpretation;
- inconsistency between the evidence and the chapter’s central argument.

Do not recommend additions merely to make the chapter more comprehensive.

Do not expand the scientific scope beyond the approved Gate 1 plan.

If the review reveals that a central section cannot be supported, identify this as an architectural problem rather than proposing generic replacement material.

# Review record

Create:

`chapters/NN_chapter_slug/SCIENTIFIC_REVIEW.md`

Keep the review concise and actionable.

For every finding, state:

- location;
- problem;
- required correction;
- severity: minor, major or structural.

Finish with:

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

Use `Ready` only when no unresolved scientific correction remains.

Scientific readiness does not mean:

- editorial readiness;
- figure readiness;
- technical readiness;
- Gate 2 readiness;
- publication readiness.

# Revision

After review, revise the chapter to resolve every actionable scientific finding.

Use targeted corrections when the approved architecture remains sound.

Do not add background, definitions or literature merely to make a correction appear more complete.

Record the resolution beneath each finding in `SCIENTIFIC_REVIEW.md`.

If a required correction would materially alter the approved Gate 1 architecture, stop and return the issue to the editor.

If the architecture remains sound, complete the scientific revision and continue to the independent editorial-quality stage.

# Completion condition

This workflow stage is complete only when:

- all scientific findings have been resolved;
- the scientific review records their resolution;
- Scientific readiness is `Ready`;
- no unresolved structural scientific problem remains.

A scientific pass cannot override a later editorial or visual rejection.