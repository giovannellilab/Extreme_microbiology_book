# Stage 2 — Editorial review and architecture approval

## Purpose

Give the editor a short, decision-focused review of the source audit before scientific verification begins. The editor is not expected to review every audit entry unless a specific issue requires it.

## Minimum editorial review

Review, in order:

1. Editorial summary.
2. Recommended chapter job.
3. Proposed chapter architecture.
4. Material to move elsewhere.
5. Evidence gaps.
6. Quick scan of the verification queue.

Check that the proposed chapter is necessary, appropriately scoped, causal rather than encyclopaedic, and consistent with neighbouring chapters. Merge or remove optional template sections when they weaken chapter rhythm.

## Required output

Record:

- the approved chapter job;
- the approved architecture;
- editorial additions or deletions;
- explicit permission, or refusal, to proceed to Stage 3.

The decision may be recorded in the source audit, a review note or the issue/PR used to supervise the work, provided it is versioned and unambiguous. Mark the source audit `editorially approved` only after approval.

## Approval gate

Stage 3 must not begin without explicit editorial permission.

## Metadata

Any new production document must begin with YAML front matter containing, where relevant: `chapter_title`, `chapter_slug`, `document_type`, `workflow_stage`, `workflow_version`, `document_version`, `editor`, `status`, `created`, `last_updated`, `publication_content` and `teachbooks_rendered`. Allowed status values are `draft`, `under review`, `revision required`, `editorially approved`, `superseded` and `published`. Production artefacts must set `publication_content: false` and `teachbooks_rendered: false`.
