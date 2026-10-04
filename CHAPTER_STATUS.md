# CHAPTER_STATUS.md

# Chapter production status

This file is the lightweight project-level dashboard for chapter production.

Detailed evidence, review and revision records belong in the relevant chapter-production folder. This table should record only the major state of each chapter.

## Status definitions

### Gate 1

- `not started` — no architecture review yet
- `pending` — Gate 1 package prepared and awaiting author decision
- `approved` — chapter architecture approved by the author

### v0.1

For this project:

`v0.1 = Gate 1 approved + automated production complete + Gate 2 pending`

A chapter reaches `complete` v0.1 only when it has:

- complete integrated prose
- scientific review and revision completed
- figures and tables integrated
- citations resolved
- QA passed
- HTML rendered
- canonical review PDF at `book/NN_chapter_slug.pdf`

Possible values:

- `not started`
- `in progress`
- `complete`
- `blocked`

### Gate 2

- `not ready` — v0.1 is not complete
- `pending` — complete Gate 2 package exists and awaits author review
- `revision` — author reviewed the package and requested changes
- `approved` — author approved the complete chapter

### Publication

- `not published`
- `published`

A chapter is not published merely because it exists in `book/`.

Publication requires explicit author approval and inclusion in the canonical public TOC.

## Chapter status

| Chapter | Title | Gate 1 | v0.1 | Gate 2 | Publication | Notes |
|---:|---|---|---|---|---|---|
| 01 | A brief history of environmental microbiology | not started | not started | not ready | not published | |
| 02 | The microbial cell | not started | not started | not ready | not published | |
| 03 | Viruses | not started | not started | not ready | not published | |
| 04 | Microbial genetics: genes and genomes | not started | not started | not ready | not published | |
| 05 | Microbial metabolism: the basics | not started | not started | not ready | not published | |
| 06 | Microbial evolution | not started | not started | not ready | not published | |
| 07 | Microbial ecology | not started | not started | not ready | not published | |
| 08 | Studying microbial diversity: an overview | not started | not started | not ready | not published | |
| 09 | Microbial energetic metabolism 101 | not started | not started | not ready | not published | |
| 10 | Thermodynamics and kinetics | not started | not started | not ready | not published | |
| 11 | Phototrophy: energy from the Sun | not started | not started | not ready | not published | |
| 12 | Chemolithotrophy: energy from the Earth | not started | not started | not ready | not published | |
| 13 | Carbon fixation: making biomass | not started | not started | not ready | not published | |
| 14 | Chemoheterotrophy: energy from others | not started | not started | not ready | not published | |
| 15 | Extremophiles and life's extremes | not started | not started | not ready | not published | |
| 16 | Polyextremophiles: the norm rather than the exception | not started | not started | not ready | not published | |
| 17 | Life at low temperature: psychrophiles | approved | blocked | not ready | not published | Legacy pilot; final visuals and Gate 2 package remain incomplete |
| 18 | Thermophiles and hyperthermophiles | approved | complete | pending | not published | Final integrated chapter, HTML and canonical PDF available |
| 19 | Acidophiles | not started | not started | not ready | not published | |
| 20 | Alkaliphiles | not started | not started | not ready | not published | |
| 21 | Halophiles | not started | not started | not ready | not published | |
| 22 | Piezophiles | not started | not started | not ready | not published | |
| 23 | Xerophiles | not started | not started | not ready | not published | |
| 24 | Other adaptations: metals, hydrocarbons, radiation and beyond | not started | not started | not ready | not published | |
| 25 | Extreme environments on our planet | not started | not started | not ready | not published | |
| 26 | Oceans | not started | not started | not ready | not published | |
| 27 | Marine sediments | not started | not started | not ready | not published | |
| 28 | Deep-sea hydrothermal vents | not started | not started | not ready | not published | Final pipeline test chapter |
| 29 | Cold seeps and mud volcanoes | not started | not started | not ready | not published | |
| 30 | Oxygen minimum zones | not started | not started | not ready | not published | |
| 31 | Deep hypersaline anoxic basins | not started | not started | not ready | not published | |
| 32 | Whale falls and other massive organic falls | not started | not started | not ready | not published | |
| 33 | Shallow-water hydrothermal vents | not started | not started | not ready | not published | |
| 34 | Marine polar regions | not started | not started | not ready | not published | |
| 35 | Soils | not started | not started | not ready | not published | |
| 36 | Hot springs and geothermal environments | not started | not started | not ready | not published | |
| 37 | Serpentinising environments | not started | not started | not ready | not published | |
| 38 | Subsurface ecosystems: oceanic and continental | not started | not started | not ready | not published | |
| 39 | Alkaline and soda lakes | not started | not started | not ready | not published | |
| 40 | Continental polar regions | not started | not started | not ready | not published | |
| 41 | Ice and snow | not started | not started | not ready | not published | |
| 42 | Atmosphere and aerosols | not started | not started | not ready | not published | |
| 43 | Biogeochemical cycles | not started | not started | not ready | not published | |
| 44 | Coevolution of the geosphere and biosphere | not started | not started | not ready | not published | |
| 45 | Extremophiles' contributions to society | not started | not started | not ready | not published | |
| 46 | Life beyond Earth: astrobiology | not started | not started | not ready | not published | |
| 47 | Future research directions | not started | not started | not ready | not published | |

## Maintenance rule

Update this file only when one of these major transitions occurs:

- Gate 1 becomes pending or approved
- v0.1 starts, completes or becomes blocked
- Gate 2 becomes pending, enters revision or is approved
- publication status changes

Do not use this table to track individual evidence, drafting, review, figure or QA subtasks.