#!/usr/bin/env python3
"""Deterministic static QA for publication chapters in this repository.

Usage:
    python3 scripts/chapter_qa.py book/17_psychrophiles.md
    python3 scripts/chapter_qa.py book/17_psychrophiles.md book/18_thermophiles_and_hyperthermophiles.md
    python3 scripts/chapter_qa.py book/18_thermophiles_and_hyperthermophiles.md --gate2 --pdf build/chapter18/_build/pdf/book.pdf

The default build mode is ``auto``: run the TeachBooks build when its CLI is
available, otherwise report that the build was not run. Static checks always run.
Gate 2 mode additionally requires and validates a supplied chapter-review PDF.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:  # pragma: no cover - exercised only in incomplete environments
    yaml = None


REQUIRED_FRONT_MATTER = (
    "chapter_title",
    "chapter_slug",
    "document_type",
    "workflow_stage",
    "workflow_version",
    "document_version",
    "editor",
    "status",
    "created",
    "last_updated",
    "publication_content",
    "teachbooks_rendered",
)

ALLOWED_STATUS = {
    "draft",
    "under review",
    "revision required",
    "editorially approved",
    "superseded",
    "published",
}

US_TO_BRITISH = {
    "behavior": "behaviour",
    "behaviors": "behaviours",
    "color": "colour",
    "colors": "colours",
    "colored": "coloured",
    "organization": "organisation",
    "organizations": "organisations",
    "organize": "organise",
    "organized": "organised",
    "organizing": "organising",
    "analyze": "analyse",
    "analyzed": "analysed",
    "analyzes": "analyses",
    "center": "centre",
    "centers": "centres",
    "fiber": "fibre",
    "fibers": "fibres",
    "liter": "litre",
    "liters": "litres",
    "sulfur": "sulphur",
    "sulfide": "sulphide",
    "sulfate": "sulphate",
}


@dataclass
class Finding:
    severity: str
    scope: str
    message: str


class Report:
    def __init__(self) -> None:
        self.findings: list[Finding] = []

    def error(self, scope: str, message: str) -> None:
        self.findings.append(Finding("ERROR", scope, message))

    def warning(self, scope: str, message: str) -> None:
        self.findings.append(Finding("WARN", scope, message))

    def info(self, scope: str, message: str) -> None:
        self.findings.append(Finding("INFO", scope, message))

    def emit(self) -> None:
        for finding in self.findings:
            print(f"{finding.severity:5} [{finding.scope}] {finding.message}")
        counts = Counter(item.severity for item in self.findings)
        print(
            "\nSummary: "
            f"{counts['ERROR']} error(s), {counts['WARN']} warning(s), "
            f"{counts['INFO']} informational result(s)."
        )

    @property
    def has_errors(self) -> bool:
        return any(item.severity == "ERROR" for item in self.findings)


def find_repo_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / "book" / "_config.yml").is_file() and (
            candidate / "references" / "bibliography.bib"
        ).is_file():
            return candidate
    raise RuntimeError("Could not locate repository root from script path.")


def load_yaml(path: Path, report: Report, scope: str) -> Any:
    if yaml is None:
        report.error(scope, "PyYAML is unavailable; YAML validity cannot be checked.")
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # PyYAML exposes several exception subclasses
        report.error(scope, f"Invalid YAML in {path}: {exc}")
        return None


def split_front_matter(text: str) -> tuple[str | None, str, int]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text, 0
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "".join(lines[1:index]), "".join(lines[index + 1 :]), index + 1
    return None, text, 0


def parse_front_matter(
    chapter: Path, text: str, report: Report
) -> tuple[dict[str, Any], str, int]:
    scope = chapter.name
    raw, body, offset = split_front_matter(text)
    if raw is None:
        report.error(scope, "Missing or unterminated YAML front matter.")
        return {}, body, offset
    if yaml is None:
        report.error(scope, "PyYAML is unavailable; front matter was not validated.")
        return {}, body, offset
    try:
        data = yaml.safe_load(raw)
    except Exception as exc:
        report.error(scope, f"Invalid YAML front matter: {exc}")
        return {}, body, offset
    if not isinstance(data, dict):
        report.error(scope, "Front matter must be a YAML mapping.")
        return {}, body, offset
    for key in REQUIRED_FRONT_MATTER:
        if key not in data or data[key] in (None, ""):
            report.error(scope, f"Front matter is missing required key '{key}'.")
    if data.get("status") not in ALLOWED_STATUS:
        report.error(
            scope,
            f"Invalid status {data.get('status')!r}; expected one of {sorted(ALLOWED_STATUS)}.",
        )
    for key in ("publication_content", "teachbooks_rendered"):
        if key in data and not isinstance(data[key], bool):
            report.error(scope, f"Front matter key '{key}' must be a YAML boolean.")
    if data.get("document_type") != "publication_chapter":
        report.warning(
            scope,
            f"document_type is {data.get('document_type')!r}, not 'publication_chapter'.",
        )
    return data, body, offset


def active_markdown_lines(body: str) -> list[tuple[int, str]]:
    """Return lines outside fenced code blocks, numbered from one within body."""
    active: list[tuple[int, str]] = []
    in_fence = False
    fence_token = ""
    for number, line in enumerate(body.splitlines(), 1):
        stripped = line.lstrip()
        match = re.match(r"(```+|~~~+)", stripped)
        if match:
            token = match.group(1)
            if not in_fence:
                in_fence = True
                fence_token = token[0]
            elif token[0] == fence_token:
                in_fence = False
            continue
        if not in_fence:
            active.append((number, line))
    return active


def check_headings(
    chapter: Path, active: list[tuple[int, str]], offset: int, report: Report
) -> None:
    headings: list[tuple[int, int, str]] = []
    for number, line in active:
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            headings.append((number + offset, len(match.group(1)), match.group(2)))
    scope = chapter.name
    if not headings:
        report.error(scope, "No Markdown headings found.")
        return
    h1_count = sum(level == 1 for _, level, _ in headings)
    if h1_count != 1:
        report.error(scope, f"Expected exactly one H1, found {h1_count}.")
    previous = headings[0][1]
    if previous != 1:
        report.error(scope, f"First heading is H{previous}, not H1.")
    for number, level, title in headings[1:]:
        if level > previous + 1:
            report.error(
                scope,
                f"Line {number}: heading hierarchy skips from H{previous} to H{level} ({title!r}).",
            )
        previous = level
    report.info(scope, f"Heading hierarchy checked: {len(headings)} heading(s).")


def bibtex_keys(bibliography: Path, report: Report) -> set[str]:
    scope = bibliography.as_posix()
    text = bibliography.read_text(encoding="utf-8")
    keys = re.findall(r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", text, re.MULTILINE)
    duplicates = sorted(key for key, count in Counter(keys).items() if count > 1)
    if duplicates:
        report.error(scope, "Duplicate bibliography key(s): " + ", ".join(duplicates))
    else:
        report.info(scope, f"Bibliography keys are unique ({len(keys)} entries).")
    return set(keys)


def citation_keys(body: str) -> set[str]:
    keys: set[str] = set()
    myst_pattern = re.compile(r"\{cite(?::[^}]*)?\}\s*`([^`]+)`")
    for content in myst_pattern.findall(body):
        for key in re.split(r"[,;\s]+", content):
            if key:
                keys.add(key.lstrip("@"))
    for key in re.findall(r"(?<![\w.-])@([A-Za-z0-9_.:+-]+)", body):
        keys.add(key)
    return keys


def check_citations(
    chapter: Path, body: str, known_keys: set[str], report: Report
) -> None:
    used = citation_keys(body)
    missing = sorted(used - known_keys)
    if missing:
        report.error(chapter.name, "Unresolved citation key(s): " + ", ".join(missing))
    else:
        report.info(chapter.name, f"Citation keys resolve ({len(used)} distinct key(s)).")


def line_number_from_offset(text: str, offset: int, front_matter_lines: int) -> int:
    return text.count("\n", 0, offset) + 1 + front_matter_lines


def normalise_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    return unquote(target)


def is_external_target(target: str) -> bool:
    scheme = urlsplit(target).scheme.lower()
    return scheme in {"http", "https", "mailto", "ftp", "data"} or target.startswith("#")


def check_links_figures_and_captions(
    chapter: Path, body: str, offset: int, report: Report
) -> None:
    scope = chapter.name
    image_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    images = list(image_pattern.finditer(body))
    chapter_number_match = re.match(r"(\d{2})_", chapter.name)
    chapter_number = chapter_number_match.group(1) if chapter_number_match else None
    body_lines = body.splitlines()

    for match in images:
        alt = match.group(1).strip()
        target = normalise_link_target(match.group(2))
        line_number = line_number_from_offset(body, match.start(), offset)
        if not alt or alt.lower() in {"figure", "image", "illustration"}:
            report.error(scope, f"Line {line_number}: figure alt text is empty or uninformative.")
        if not is_external_target(target):
            target_path = (chapter.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                report.error(scope, f"Line {line_number}: referenced figure does not exist: {target}")
            else:
                filename = target_path.name
                if re.search(
                    r"_(?:source|draft|candidate|redesign|excluded|rejected|final|v\d+)(?:_|$)",
                    target_path.stem,
                ):
                    report.error(
                        scope,
                        f"Line {line_number}: chapter references a non-production figure candidate: {filename}",
                    )
                if chapter_number:
                    convention = re.compile(
                        rf"^fig{chapter_number}_\d{{2}}(?:_[a-z0-9]+)*\.(?:svg|pdf|png|tif|tiff)$"
                    )
                    if not convention.match(filename):
                        report.error(
                            scope,
                            f"Line {line_number}: figure filename does not follow chapter convention: {filename}",
                        )
                if target_path.suffix.lower() == ".svg":
                    try:
                        root = ET.parse(target_path).getroot()
                        tags = {element.tag.rsplit("}", 1)[-1] for element in root.iter()}
                        if "title" not in tags or "desc" not in tags:
                            report.warning(
                                scope,
                                f"Line {line_number}: SVG lacks an internal title or description: {filename}",
                            )
                    except ET.ParseError as exc:
                        report.error(scope, f"Line {line_number}: invalid SVG XML in {filename}: {exc}")

        body_line_index = body.count("\n", 0, match.start())
        next_nonempty = ""
        for candidate in body_lines[body_line_index + 1 : body_line_index + 6]:
            if candidate.strip():
                next_nonempty = candidate.strip()
                break
        caption_match = re.match(
            r"^(?:\*+)?Figure\s+(\d+\.\d+)\b", next_nonempty
        )
        if not caption_match:
            report.error(
                scope,
                f"Line {line_number}: no conventional figure caption found immediately after image.",
            )
        else:
            figure_label = caption_match.group(1)
            if not re.search(
                rf"\bFigure\s+{re.escape(figure_label)}\b", body[: match.start()]
            ):
                report.error(
                    scope,
                    f"Line {line_number}: no prose callout found before Figure {figure_label}.",
                )
            if not re.search(
                r"\b(?:source|authorship|provenance)\b", next_nonempty, re.IGNORECASE
            ):
                report.error(
                    scope,
                    f"Line {line_number}: Figure {figure_label} caption lacks source/provenance information.",
                )
            if not re.search(
                r"\b(?:licen[cs]e|CC\s+BY|public domain)\b",
                next_nonempty,
                re.IGNORECASE,
            ):
                report.error(
                    scope,
                    f"Line {line_number}: Figure {figure_label} caption lacks licensing information.",
                )

    referenced_assets: set[Path] = set()
    for match in images:
        target = normalise_link_target(match.group(2))
        if is_external_target(target):
            continue
        target_path = (chapter.parent / target.split("#", 1)[0]).resolve()
        if target_path.exists():
            referenced_assets.add(target_path)

    image_suffixes = {".svg", ".pdf", ".png", ".tif", ".tiff"}
    for final_asset in sorted(referenced_assets):
        figure_prefix = re.match(r"^(fig\d{2}_\d{2})(?:_|$)", final_asset.stem)
        if not figure_prefix:
            continue
        allowed_role_prefixes = (
            final_asset.stem + "_source",
            final_asset.stem + "_excluded",
            final_asset.stem + "_rejected",
        )
        ambiguous = []
        for sibling in final_asset.parent.iterdir():
            if not sibling.is_file() or sibling.suffix.lower() not in image_suffixes:
                continue
            if sibling.resolve() == final_asset:
                continue
            if not sibling.stem.startswith(figure_prefix.group(1)):
                continue
            if sibling.stem.startswith(allowed_role_prefixes):
                continue
            ambiguous.append(sibling.name)
        if ambiguous:
            report.error(
                scope,
                f"Ambiguous competing assets for {final_asset.name}: "
                + ", ".join(sorted(ambiguous)),
            )
    report.info(
        scope,
        f"Final-asset cleanliness checked for {len(referenced_assets)} referenced figure(s).",
    )

    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for match in link_pattern.finditer(body):
        target = normalise_link_target(match.group(1))
        if not target or is_external_target(target):
            continue
        path_part = target.split("#", 1)[0]
        if not path_part:
            continue
        resolved = (chapter.parent / path_part).resolve()
        if not resolved.exists():
            line_number = line_number_from_offset(body, match.start(), offset)
            report.error(scope, f"Line {line_number}: broken internal link: {target}")

    report.info(scope, f"Figure/link scan completed ({len(images)} figure reference(s)).")


def check_tables(
    chapter: Path, active: list[tuple[int, str]], offset: int, report: Report
) -> None:
    lines = [line for _, line in active]
    numbers = [number + offset for number, _ in active]
    separators = []
    separator_re = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$")
    for index, line in enumerate(lines):
        if separator_re.match(line) and index > 0 and "|" in lines[index - 1]:
            separators.append(index)
    for index in separators:
        start = index - 1
        end = index + 1
        while end < len(lines) and "|" in lines[end] and lines[end].strip():
            end += 1
        nearby = []
        for candidate in range(max(0, start - 3), min(len(lines), end + 4)):
            if candidate < start or candidate >= end:
                if lines[candidate].strip():
                    nearby.append(lines[candidate].strip())
        if not any(re.match(r"^(?:\*+)?Table\s+\d+\.\d+\b", item) for item in nearby):
            report.error(
                chapter.name,
                f"Line {numbers[start]}: Markdown table has no nearby conventional table caption.",
            )
    report.info(chapter.name, f"Table caption scan completed ({len(separators)} table(s)).")


def check_placeholders_spelling_and_names(
    chapter: Path,
    body: str,
    active: list[tuple[int, str]],
    offset: int,
    report: Report,
) -> None:
    placeholder_re = re.compile(
        r"\b(?:TODO|FIXME|XXX)\b|(?:FIGURE|TABLE)\s+PLACEHOLDER|\bPLACEHOLDER\b",
        re.IGNORECASE,
    )
    for number, line in active:
        if placeholder_re.search(line):
            report.error(chapter.name, f"Line {number + offset}: unresolved marker: {line.strip()}")

    for number, line in active:
        line_without_urls = re.sub(r"https?://\S+", "", line)
        for us_word, british_word in US_TO_BRITISH.items():
            if re.search(rf"\b{re.escape(us_word)}\b", line_without_urls, re.IGNORECASE):
                report.warning(
                    chapter.name,
                    f"Line {number + offset}: possible US spelling '{us_word}'; consider '{british_word}' (manual review required).",
                )

    full_candidates = re.findall(r"\*([A-Z][a-z]{2,}\s+[a-z][a-z-]{2,})\*", body)
    abbreviated_names = set(re.findall(r"\*([A-Z]\.\s*[a-z][a-z-]{2,})\*", body))
    abbreviated_pairs = {
        (name[0], name.split()[-1]) for name in abbreviated_names
    }
    full_counts = Counter(full_candidates)
    full_names = {
        name
        for name in full_candidates
        if full_counts[name] > 1
        or (name[0], name.split()[-1]) in abbreviated_pairs
    }
    known_names = sorted(full_names | abbreviated_names)
    for number, line in active:
        if line.lstrip().startswith("!["):
            continue  # Markdown alt text cannot reliably preserve taxonomic italics.
        plain_line = re.sub(r"\*[^*]+\*", "", line)
        for name in known_names:
            if re.search(rf"(?<![\w*]){re.escape(name)}(?![\w*])", plain_line):
                report.warning(
                    chapter.name,
                    f"Line {number + offset}: scientific name may require italics: {name}",
                )


def check_whitespace(chapter: Path, text: str, report: Report) -> None:
    trailing = [number for number, line in enumerate(text.splitlines(), 1) if line.rstrip() != line]
    if trailing:
        shown = ", ".join(map(str, trailing[:10]))
        suffix = "…" if len(trailing) > 10 else ""
        report.error(chapter.name, f"Trailing whitespace on line(s): {shown}{suffix}")
    else:
        report.info(chapter.name, "No trailing whitespace found in chapter file.")


def collect_toc_entries(node: Any) -> Iterable[dict[str, Any]]:
    if isinstance(node, dict):
        if isinstance(node.get("file"), str):
            yield node
        for value in node.values():
            yield from collect_toc_entries(value)
    elif isinstance(node, list):
        for value in node:
            yield from collect_toc_entries(value)


def toc_entry_for_chapter(
    chapter: Path, book_dir: Path, toc_data: Any
) -> dict[str, Any] | None:
    try:
        relative = chapter.resolve().relative_to(book_dir.resolve())
    except ValueError:
        return None
    target = relative.with_suffix("").as_posix()
    for entry in collect_toc_entries(toc_data):
        if Path(entry["file"]).with_suffix("").as_posix() == target:
            return entry
    return None


def chapter_in_toc(chapter: Path, book_dir: Path, toc_data: Any) -> bool:
    return toc_entry_for_chapter(chapter, book_dir, toc_data) is not None


def normalise_identity_token(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def check_chapter_identity(
    chapter: Path,
    metadata: dict[str, Any],
    active: list[tuple[int, str]],
    offset: int,
    book_dir: Path,
    toc_data: Any,
    report: Report,
) -> None:
    scope = chapter.name
    filename_match = re.fullmatch(r"(\d{2})_([a-z0-9_]+)\.md", chapter.name)
    if not filename_match:
        report.error(
            scope,
            "Publication filename must use NN_short_title.md with a two-digit chapter number.",
        )
        return

    h1s: list[tuple[int, str]] = []
    for number, line in active:
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            h1s.append((number + offset, match.group(1)))
    if len(h1s) != 1:
        return  # check_headings reports the structural error.

    line_number, h1_text = h1s[0]
    h1_match = re.fullmatch(r"(\d{2})\.\s+(.+)", h1_text)
    if not h1_match:
        report.error(
            scope,
            f"Line {line_number}: publication H1 must use '# NN. Chapter title'.",
        )
        return

    file_number, filename_identity = filename_match.groups()
    h1_number, h1_title = h1_match.groups()
    if h1_number != file_number:
        report.error(
            scope,
            f"Line {line_number}: H1 chapter number {h1_number} does not match filename prefix {file_number}.",
        )

    front_matter_title = metadata.get("chapter_title")
    if isinstance(front_matter_title, str) and h1_title.strip() != front_matter_title.strip():
        report.error(
            scope,
            f"Line {line_number}: H1 title {h1_title!r} does not match front matter chapter_title {front_matter_title!r}.",
        )

    chapter_slug = metadata.get("chapter_slug")
    if isinstance(chapter_slug, str):
        normalised_slug = normalise_identity_token(chapter_slug)
        if normalised_slug and normalised_slug not in normalise_identity_token(filename_identity):
            report.error(
                scope,
                f"Filename identity {filename_identity!r} does not contain chapter_slug {chapter_slug!r}.",
            )

    toc_entry = toc_entry_for_chapter(chapter, book_dir, toc_data)
    if toc_entry is None:
        report.info(
            scope,
            "Chapter is absent from the canonical TOC; TOC title comparison is deferred until publication listing.",
        )
    elif isinstance(toc_entry.get("title"), str):
        toc_title = toc_entry["title"].strip()
        if toc_title != h1_text.strip():
            report.error(
                scope,
                f"Canonical TOC title {toc_title!r} does not match visible H1 {h1_text!r}.",
            )
    else:
        report.info(
            scope,
            "Canonical TOC entry has no title override; the numbered H1 supplies the rendered title.",
        )

    report.info(scope, f"Chapter identity checked: {h1_number}. {h1_title.strip()}")


def check_toc_consistency(
    chapter: Path,
    metadata: dict[str, Any],
    book_dir: Path,
    toc_data: Any,
    report: Report,
) -> bool:
    listed = chapter_in_toc(chapter, book_dir, toc_data)
    rendered = metadata.get("teachbooks_rendered")
    if rendered is True and not listed:
        report.error(
            chapter.name,
            "teachbooks_rendered is true, but the chapter is absent from book/_toc.yml.",
        )
    elif rendered is False and listed:
        report.error(
            chapter.name,
            "teachbooks_rendered is false, but the chapter is listed in book/_toc.yml.",
        )
    else:
        report.info(
            chapter.name,
            f"TOC/metadata state is consistent (listed={listed}, teachbooks_rendered={rendered}).",
        )
    return listed


def check_git_diff(paths: list[Path], root: Path, report: Report) -> None:
    relative_paths = []
    for path in paths:
        try:
            relative_paths.append(str(path.resolve().relative_to(root.resolve())))
        except ValueError:
            continue
    command = ["git", "diff", "--check", "--", *relative_paths]
    result = subprocess.run(command, cwd=root, text=True, capture_output=True)
    output = (result.stdout + result.stderr).strip()
    if result.returncode:
        report.error("git diff --check", output or f"Exited with code {result.returncode}.")
    else:
        report.info("git diff --check", "Passed for checked chapter and reference paths.")


def run_build(
    mode: str,
    root: Path,
    book_dir: Path,
    any_target_listed: bool,
    report: Report,
) -> None:
    if mode == "never":
        report.warning("build", "Build skipped by --build never.")
        return
    teachbooks = shutil.which("teachbooks")
    jupyter_book = shutil.which("jupyter-book")
    if teachbooks:
        command = [teachbooks, "build", str(book_dir)]
    elif jupyter_book:
        command = [jupyter_book, "build", str(book_dir), "--all"]
    else:
        message = (
            "TeachBooks/Jupyter Book runtime unavailable; no site build was run. "
            "Install the repository requirements and rerun with --build always."
        )
        if mode == "always":
            report.error("build", message)
        else:
            report.warning("build", message)
        return
    result = subprocess.run(command, cwd=root, text=True, capture_output=True)
    command_text = " ".join(command)
    if result.returncode:
        combined = (result.stdout + "\n" + result.stderr).strip().splitlines()
        excerpt = "\n".join(combined[-30:])
        report.error("build", f"Build failed: {command_text}\n{excerpt}")
    else:
        report.info("build", f"Build passed: {command_text}")
        if not any_target_listed:
            report.warning(
                "build",
                "The checked chapter is absent from the public TOC, so the site build did not render that chapter.",
            )


def check_pdf_artifact(
    supplied: Path,
    root: Path,
    expected_titles: list[str],
    report: Report,
) -> None:
    scope = "Gate 2 PDF"
    pdf = supplied if supplied.is_absolute() else root / supplied
    pdf = pdf.resolve()
    if not pdf.is_file():
        report.error(scope, f"Required PDF artifact does not exist: {pdf}")
        return
    if pdf.suffix.lower() != ".pdf":
        report.error(scope, f"Gate 2 artifact is not a .pdf file: {pdf}")
        return
    try:
        header = pdf.read_bytes()[:5]
    except OSError as exc:
        report.error(scope, f"Could not read PDF artifact {pdf}: {exc}")
        return
    if header != b"%PDF-":
        report.error(scope, f"Artifact lacks a PDF file signature: {pdf}")
        return

    pages: int | None = None
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        result = subprocess.run([pdfinfo, str(pdf)], text=True, capture_output=True)
        if result.returncode:
            report.error(scope, f"pdfinfo could not validate {pdf}: {result.stderr.strip()}")
        else:
            match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
            if not match or int(match.group(1)) < 1:
                report.error(scope, f"Could not establish a positive PDF page count for {pdf}.")
            else:
                pages = int(match.group(1))
    else:
        report.warning(scope, "pdfinfo is unavailable; page count was not mechanically checked.")

    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        result = subprocess.run(
            [pdftotext, str(pdf), "-"], text=True, capture_output=True
        )
        if result.returncode:
            report.error(scope, f"pdftotext could not inspect {pdf}: {result.stderr.strip()}")
        else:
            pdf_text = re.sub(r"\s+", " ", result.stdout)
            for title in expected_titles:
                if title not in pdf_text:
                    report.error(scope, f"Numbered chapter title missing from PDF text: {title}")
    else:
        report.warning(scope, "pdftotext is unavailable; numbered PDF title was not checked.")

    page_summary = f", {pages} page(s)" if pages is not None else ""
    report.info(scope, f"Required PDF artifact exists and has a valid signature{page_summary}: {pdf}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapters", nargs="+", type=Path, help="Publication chapter Markdown file(s).")
    parser.add_argument(
        "--build",
        choices=("auto", "always", "never"),
        default="auto",
        help="Build policy: auto when CLI exists (default), require a build, or skip.",
    )
    parser.add_argument(
        "--gate2",
        action="store_true",
        help="Run Gate 2 readiness checks; requires --pdf.",
    )
    parser.add_argument(
        "--pdf",
        type=Path,
        help="Path to the rendered chapter-review PDF artifact.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = find_repo_root(Path(__file__).resolve())
    book_dir = root / "book"
    bibliography = root / "references" / "bibliography.bib"
    csl = root / "references" / "nature.csl"
    toc = root / "book" / "_toc.yml"
    report = Report()

    known_keys = bibtex_keys(bibliography, report)
    toc_data = load_yaml(toc, report, "book/_toc.yml") or {}
    try:
        ET.parse(csl)
        report.info("references/nature.csl", "CSL is well-formed XML.")
    except ET.ParseError as exc:
        report.error("references/nature.csl", f"Invalid XML: {exc}")

    checked_paths: list[Path] = [bibliography, csl, toc]
    target_listed_states: list[bool] = []
    expected_pdf_titles: list[str] = []
    for supplied in args.chapters:
        chapter = supplied if supplied.is_absolute() else root / supplied
        chapter = chapter.resolve()
        if not chapter.is_file():
            report.error(str(supplied), "Chapter file does not exist.")
            continue
        checked_paths.append(chapter)
        text = chapter.read_text(encoding="utf-8")
        metadata, body, front_matter_lines = parse_front_matter(chapter, text, report)
        chapter_number_match = re.match(r"(\d{2})_", chapter.name)
        chapter_title = metadata.get("chapter_title")
        if chapter_number_match and isinstance(chapter_title, str):
            expected_pdf_titles.append(
                f"{chapter_number_match.group(1)}. {chapter_title.strip()}"
            )
        active = active_markdown_lines(body)
        check_headings(chapter, active, front_matter_lines, report)
        check_chapter_identity(
            chapter,
            metadata,
            active,
            front_matter_lines,
            book_dir,
            toc_data,
            report,
        )
        check_citations(chapter, body, known_keys, report)
        check_links_figures_and_captions(chapter, body, front_matter_lines, report)
        check_tables(chapter, active, front_matter_lines, report)
        check_placeholders_spelling_and_names(
            chapter, body, active, front_matter_lines, report
        )
        check_whitespace(chapter, text, report)
        target_listed_states.append(
            check_toc_consistency(chapter, metadata, book_dir, toc_data, report)
        )

    check_git_diff(checked_paths, root, report)
    if args.gate2 and args.pdf is None:
        report.error("Gate 2 PDF", "Gate 2 readiness requires --pdf PATH.")
    if args.pdf is not None:
        check_pdf_artifact(args.pdf, root, expected_pdf_titles, report)
    run_build(args.build, root, book_dir, any(target_listed_states), report)
    report.emit()
    return 1 if report.has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
