# Stage 5 — Scientific review

## Purpose

Independently test the reconstructed chapter's scientific accuracy before any revision is made. The scientific reviewer should not be the reconstruction agent.

## Review procedure

Check the complete chapter against the evidence package and cited literature. Identify:

- factual errors and outdated claims;
- overstatement of evidence or uncertainty;
- claim–citation mismatches;
- conflation of detection, survival, viability, maintenance, activity, growth or reproduction;
- outdated taxonomy or incorrect nomenclature;
- unsupported generalisation from a particular organism, protein or lineage;
- inference of function from gene presence, comparative genomics or expression alone;
- numerical, unit and chemical errors.

Classify every actionable comment:

- **Critical** — invalidates a central claim or creates a serious scientific error.
- **Major** — materially changes interpretation, evidence or chapter logic.
- **Minor** — local correction that does not alter the argument.
- **Editorial** — clarity or presentation issue without scientific impact.

## Scope discipline

Do not recommend adding material simply because it is scientifically interesting.

Recommend additions only when:

- a factual error would otherwise remain;
- the approved chapter job cannot be fulfilled;
- a key concept lacks adequate support;
- an essential scientific caveat is missing.

Do not ask for greater completeness for its own sake. Judge whether the chapter fulfils its approved educational objective, not whether it covers every aspect of the topic.

## Required output

Create `chapters/<chapter-slug>/SCIENTIFIC_REVIEW.md`. For each finding, identify the location, problem, evidence and recommended action. Report before rewriting. Apply accepted changes only in a separate revision pass so the review remains independently auditable.

The review must also contain the following sections.

## Scientific strengths

List up to five scientifically strong aspects of the chapter, such as particularly clear mechanistic explanation, appropriate handling of uncertainty, strong evidence use, good distinction between evidence levels or especially effective scientific synthesis.

## Scientific quality

Choose one:

- **Excellent**
- **Good**
- **Adequate**
- **Unsatisfactory**

Provide a brief justification.

## Publication readiness

Choose one:

- **Ready**
- **Minor revision**
- **Major revision**
- **Reject**

Provide a brief justification.

## Approval gate

Critical and major findings must be resolved or explicitly accepted by the editor/scientific lead before Stage 6.

## Metadata

New production documents must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Production artefacts must set `publication_content: false` and `teachbooks_rendered: false`.
