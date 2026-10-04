---
chapter_title: "Thermophiles and hyperthermophiles"
chapter_slug: "thermophiles"
document_type: "figure_table_plan"
workflow_stage: 7
workflow_version: "1.0"
document_version: "1.3"
editor: "Donato Giovannelli"
status: "under review"
created: "2026-10-01"
last_updated: "2026-10-04"
publication_content: false
teachbooks_rendered: false
---

# Chapter 18 final figure and table plan

This plan records the final three-figure architecture and Table 18.1 integrated for Human Gate 2. It supersedes the earlier heat-accelerator figure, the box-driven maintenance diagram and the evidence-audit Beowulf schematic. The final figures follow the Natural History Museum Minimal house style and contain no third-party artwork.

## Figure 18.1 — Cardinal temperature ranges

- **Purpose / question:** Compare approximate demonstrated growth envelopes and typical optimum zones for psychrophiles, mesophiles, thermophiles and hyperthermophiles while keeping the 122 °C proliferation record distinct from group properties.
- **Chapter location:** Section 1, immediately after the cardinal-temperature definitions and upper-growth record.
- **Visual logic:** An open quantitative axis with overlapping schematic envelopes and directly labelled optimum zones. A separate point identifies *Methanopyrus kandleri* strain 116 proliferation at 122 °C in high-pressure culture at 20 or 40 MPa.
- **Evidence boundary:** The group ranges are approximate rather than universal fixed boundaries. The record marker represents one specified experiment, not the normal or maximum temperature of every hyperthermophile {cite:p}`canganella2014,hedlund2015,takai2008`.
- **Publication asset:** `book/figures/fig18_01_cardinal_temperatures.svg` — original editable vector diagram.
- **Production method:** Programmatic SVG.
- **Accessibility:** The chapter provides descriptive alt text and a self-contained caption. The white field, direct labels and line/position encoding do not depend on colour alone.

## Figure 18.2 — Thermophile cellular adaptations

- **Purpose / question:** Show how membrane permeability, protein integrity and genome maintenance pose linked whole-cell problems at high temperature.
- **Chapter location:** Section 3, after the membrane, protein and genome subsections.
- **Visual logic:** A central thermophilic archaeal cell is connected to three balanced magnified insets: membrane-spanning lipid architecture and reduced leakage; folded/non-native proteins and chaperonin quality control; and DNA organisation and repair.
- **Evidence boundary:** The illustrated features are selected, lineage-specific examples rather than a universal thermophile or archaeal cell plan {cite:p}`canganella2014,ranawat2017,takemata2024`.
- **Publication asset:** `book/figures/fig18_02_cellular_adaptations.png` — 2400 × 1800 px, fully opaque white background.
- **Editable source:** `book/figures/fig18_02_cellular_adaptations_source.svg`, with required image base `book/figures/fig18_02_cellular_adaptations_source_base.png`.
- **Production method:** Image-generated scientific-illustration base plus vector/text overlay; flattened to high-resolution PNG for robust publication rendering.
- **Accessibility:** All overlay text corresponds to at least 8.5 pt at 180 mm placement; the chapter provides descriptive alt text and a self-contained caption.

## Figure 18.3 — Thermal–geochemical habitat

- **Purpose / question:** Show how a geothermal outflow creates spatially distinct niches through coupled temperature, oxygen/redox and geochemical gradients.
- **Chapter location:** Section 5, after the Beowulf Spring discussion of field, sequence and culture evidence.
- **Visual logic:** The geothermal environment remains the dominant object. Sparse direct labels follow a hot reduced source through an open-air mixing zone and Fe(III)-oxide mat to a cooler oxygenated outflow; three aligned bars make the coupled gradients explicit.
- **Evidence boundary:** Beowulf Spring informs the Fe(II)-oxidising interface, but the illustration teaches the broader spatial principle. It does not show an evidence-audit panel, invent a quantitative transect or attribute an environmental rate to one lineage {cite:p}`inskeep2010,kozubal2012`.
- **Publication asset:** `book/figures/fig18_03_thermal_geochemical_gradient.png` — 2400 × 1467 px, fully opaque white background.
- **Editable source:** `book/figures/fig18_03_thermal_geochemical_gradient_source.svg`, with required image base `book/figures/fig18_03_thermal_geochemical_gradient_source_base.png`.
- **Production method:** Image-generated natural-history-style environment base plus vector/text overlay; flattened to high-resolution PNG for robust publication rendering.
- **Accessibility:** All overlay text corresponds to at least 8.5 pt at 180 mm placement; the chapter provides descriptive alt text and a self-contained caption.

## Table 18.1 — Evidence behind an upper-temperature claim

- **Purpose / question:** Distinguish demonstrated proliferation from assayed activity, survival after heat exposure and biomolecular persistence or detection.
- **Chapter location:** Section 1, immediately after Figure 18.1.
- **Evidence boundary:** Only the first row is a numerical record. It retains the organism, supplied substrates and discrete pressure conditions from Takai et al. 2008; the remaining rows are conceptual evidence categories rather than invented records {cite:p}`takai2008`.
- **Format:** Native Markdown table with an integrated prose callout and caption.

## Production tracking

| Item | Final publication asset | Editable/source asset | Integration status |
|---|---|---|---|
| Figure 18.1 | `book/figures/fig18_01_cardinal_temperatures.svg` | same SVG | integrated; Gate 2 pending |
| Figure 18.2 | `book/figures/fig18_02_cellular_adaptations.png` | `fig18_02_cellular_adaptations_source.svg` + `_source_base.png` | integrated; Gate 2 pending |
| Figure 18.3 | `book/figures/fig18_03_thermal_geochemical_gradient.png` | `fig18_03_thermal_geochemical_gradient_source.svg` + `_source_base.png` | integrated; Gate 2 pending |
| Table 18.1 | native Markdown | chapter source | integrated; Gate 2 pending |
