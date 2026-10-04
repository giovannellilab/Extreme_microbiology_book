---
chapter_title: "Thermophiles and hyperthermophiles"
chapter_slug: "thermophiles"
document_type: "technical_validation_report"
workflow_stage: 7
workflow_version: "1.0"
document_version: "1.6"
editor: "Donato Giovannelli"
status: "under review"
created: "2026-10-01"
last_updated: "2026-10-04"
publication_content: false
teachbooks_rendered: false
---

# Chapter 18 technical validation — final Gate 2 package

## Conclusion

Chapter 18 now contains the approved Table 18.1 and exactly three final figures: cardinal temperature ranges in Section 1, thermophile cellular adaptations in Section 3 and a thermal–geochemical habitat in Section 5. The superseded heat-accelerator figure, box-driven maintenance graphic and evidence-audit Beowulf schematic are no longer referenced or retained as ambiguous Chapter 18 assets.

Static QA passes with zero errors. Isolated Jupyter Book HTML and PDF builds using the repository configuration, bibliography page and a temporary Chapter 18-only TOC succeed. The 18-page PDF contains the complete chapter, Table 18.1, all three final figures, captions and rendered references. The sole build warning is the pre-existing `_config.yml` reference to missing `figures/xxxx.ico`. The public TOC remains unchanged and `teachbooks_rendered` remains false.

## Final assets and integration

| Item | Publication asset | Result |
|---|---|---|
| Figure 18.1 | `book/figures/fig18_01_cardinal_temperatures.svg` | Vector diagram renders at full column width with white background, legible labels and explicit 122 °C high-pressure proliferation record. |
| Figure 18.2 | `book/figures/fig18_02_cellular_adaptations.png` | 2400 × 1800 px opaque-white PNG renders without clipping; the three insets and central archaeal cell remain legible. |
| Figure 18.3 | `book/figures/fig18_03_thermal_geochemical_gradient.png` | 2400 × 1467 px opaque-white PNG renders without clipping; the coupled gradients and four habitat labels remain legible. |
| Table 18.1 | native Markdown | Callout, table and caption render in the correct Section 1 sequence. |

The two illustrated publication PNGs retain explicitly named editable hybrid SVG/source-base pairs. No publication image depends on an external linked raster. Captions identify the image-generated-base plus vector-overlay method, scientific evidence boundaries, original-book provenance and CC BY-NC-SA 4.0 licensing. Descriptive Markdown alt text is present for every figure.

## QA result

Command:

```bash
python3 scripts/chapter_qa.py book/18_thermophiles_and_hyperthermophiles.md \
  --build never --gate2 --pdf build/chapter18/_build/pdf/book.pdf
```

Result: zero errors. Metadata, heading hierarchy, citation keys, bibliography uniqueness, figure paths, captions, alt text, table caption, filename conventions, final-asset cleanliness, TOC state, whitespace, PDF structure, PDF page count, numbered PDF title and `git diff --check` passed. The explicit `--build never` warning records that the isolated build was run separately against the temporary Chapter 18-only TOC.

## Build result

Repository dependencies were installed into the isolated environment `/tmp/ch18-teachbooks-venv` from `requirements.txt`. The public `book/_toc.yml` was not edited. A temporary copy of the book used a two-page TOC containing Chapter 18 and the existing bibliography page so the unapproved chapter could be tested without publication.

The supported chapter-review PDF route is Jupyter Book's built-in `pdfhtml` builder. It renders the temporary Chapter 18 book as single-page HTML and uses Playwright Chromium to print that output to PDF:

```bash
PLAYWRIGHT_BROWSERS_PATH=/tmp/ch18-playwright-browsers \
  /tmp/ch18-teachbooks-venv/bin/jupyter-book build /tmp/ch18-build.z8dId7/book \
  --path-output /home/giovannelli/github/Extreme_microbiology_book/build/chapter18 \
  --builder pdfhtml --all
```

Playwright 1.63.0 and its standard Chromium 153.0.8010.12 runtime were installed in the isolated build environment; `pyee` and `greenlet` were installed as Playwright dependencies. `playwright` is now declared in `requirements.txt`. No parallel PDF system was introduced.

Result: build succeeded with one warning, the repository's missing placeholder favicon `figures/xxxx.ico`. All 15 distinct Chapter 18 citation keys resolve. HTML output: `build/chapter18/_build/html/18_thermophiles_and_hyperthermophiles.html`. PDF output: `build/chapter18/_build/pdf/book.pdf` (18 pages).

## Visual render check

The generated HTML was inspected in the local browser in light and dark modes. In light mode each figure displays at approximately 676 CSS px wide with its intended aspect ratio:

- Figure 18.1: 676 × 406 px;
- Figure 18.2: 676 × 507 px;
- Figure 18.3: 676 × 413 px.

The HTML image dimensions show no cropping or aspect-ratio distortion. All 18 PDF pages were rasterised and visually inspected. The numbered title appears at the top of page 1; Figure 18.1 and its caption render together on page 3; Table 18.1 and its caption render together on page 4; Figure 18.2 and its caption render together on page 10; Figure 18.3 and its caption render together on page 13; and the reference list is complete on pages 16–18. The figures are uncropped, labels remain readable and citations are visibly linked to rendered references. A print-only MyST/Sphinx container rule prevents figure captions from splitting across pages. Source-file checks confirmed fully opaque white corner pixels for both publication PNGs and pure-white SVG background for Figure 18.1. Minimum vector-overlay type corresponds to 8.5 pt at the declared 180 mm source width.

## Remaining technical issues

- The repository config still points to missing `book/figures/xxxx.ico`; this pre-existing warning does not affect Chapter 18 content or the PDF.

No remaining visual or layout issue blocks review. The complete HTML-and-PDF package is **READY** for Human Gate 2. This readiness status is not Human Gate 2 approval or authorisation to publish.
