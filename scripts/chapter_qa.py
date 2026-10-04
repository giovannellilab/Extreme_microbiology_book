#!/usr/bin/env python3
"""Minimal deterministic QA for book chapters.

Usage:

    python3 scripts/chapter_qa.py book/18_thermophiles_and_hyperthermophiles.md

Gate 2:

    python3 scripts/chapter_qa.py \
        book/18_thermophiles_and_hyperthermophiles.md \
        --gate2

With --gate2 the script also requires:

    book/18_thermophiles_and_hyperthermophiles.pdf

This script checks source consistency only.
It does not build the book or judge scientific/visual quality.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from collections import Counter
from pathlib import Path

import yaml


REQUIRED_FRONT_MATTER = (
    "chapter_title",
    "chapter_slug",
    "document_type",
    "document_version",
    "editor",
    "status",
)

PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|FIXME|XXX|PLACEHOLDER)\b",
    re.IGNORECASE,
)


class QA:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def report(self) -> int:
        for message in self.errors:
            print(f"ERROR: {message}")

        for message in self.warnings:
            print(f"WARN:  {message}")

        print(
            f"\nQA: {len(self.errors)} error(s), "
            f"{len(self.warnings)} warning(s)"
        )

        return 1 if self.errors else 0


def repo_root() -> Path:
    root = Path(__file__).resolve().parents[1]

    if not (root / "book").is_dir():
        raise RuntimeError("Could not locate repository root.")

    return root


def read_chapter(path: Path, qa: QA) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        qa.error(f"{path.name}: missing YAML front matter")
        return {}, text

    parts = text.split("---", 2)

    if len(parts) < 3:
        qa.error(f"{path.name}: malformed YAML front matter")
        return {}, text

    try:
        metadata = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        qa.error(f"{path.name}: invalid YAML: {exc}")
        return {}, parts[2]

    for key in REQUIRED_FRONT_MATTER:
        if not metadata.get(key):
            qa.error(
                f"{path.name}: missing front-matter field '{key}'"
            )

    return metadata, parts[2]


def check_identity(
    path: Path,
    metadata: dict,
    body: str,
    qa: QA,
) -> None:
    filename = re.fullmatch(
        r"(\d{2})_([a-z0-9_]+)\.md",
        path.name,
    )

    if not filename:
        qa.error(
            f"{path.name}: filename must use NN_chapter_slug.md"
        )
        return

    chapter_number, filename_slug = filename.groups()

    h1s = re.findall(
        r"^#\s+(.+)$",
        body,
        re.MULTILINE,
    )

    if len(h1s) != 1:
        qa.error(
            f"{path.name}: expected exactly one H1; found {len(h1s)}"
        )
        return

    h1 = re.fullmatch(
        r"(\d{2})\.\s+(.+)",
        h1s[0].strip(),
    )

    if not h1:
        qa.error(
            f"{path.name}: H1 must use '# NN. Chapter title'"
        )
        return

    h1_number, h1_title = h1.groups()

    if h1_number != chapter_number:
        qa.error(
            f"{path.name}: H1 number {h1_number} "
            f"does not match filename number {chapter_number}"
        )

    chapter_title = metadata.get("chapter_title")

    if (
        isinstance(chapter_title, str)
        and h1_title.strip() != chapter_title.strip()
    ):
        qa.error(
            f"{path.name}: H1 title does not match chapter_title"
        )

    chapter_slug = metadata.get("chapter_slug")

    if isinstance(chapter_slug, str):
        normalised_slug = re.sub(
            r"[^a-z0-9]+",
            "_",
            chapter_slug.lower(),
        ).strip("_")

        if normalised_slug != filename_slug:
            qa.error(
                f"{path.name}: filename slug '{filename_slug}' "
                f"does not match chapter_slug '{normalised_slug}'"
            )


def bibliography_keys(path: Path, qa: QA) -> set[str]:
    text = path.read_text(encoding="utf-8")

    keys = re.findall(
        r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,",
        text,
        re.MULTILINE,
    )

    duplicates = [
        key
        for key, count in Counter(keys).items()
        if count > 1
    ]

    if duplicates:
        qa.error(
            "Duplicate bibliography key(s): "
            + ", ".join(sorted(duplicates))
        )

    return set(keys)


def chapter_citation_keys(body: str) -> set[str]:
    keys: set[str] = set()

    for citation in re.findall(
        r"\{cite(?::[^}]*)?\}\s*`([^`]+)`",
        body,
    ):
        for key in re.split(r"[,;\s]+", citation):
            key = key.strip().lstrip("@")

            if key:
                keys.add(key)

    for key in re.findall(
        r"(?<![\w.-])@([A-Za-z0-9_.:+-]+)",
        body,
    ):
        keys.add(key)

    return keys


def check_citations(
    body: str,
    bibliography: set[str],
    path: Path,
    qa: QA,
) -> None:
    missing = sorted(
        chapter_citation_keys(body) - bibliography
    )

    if missing:
        qa.error(
            f"{path.name}: unresolved citation key(s): "
            + ", ".join(missing)
        )


def check_figures(
    path: Path,
    body: str,
    qa: QA,
) -> None:
    image_re = re.compile(
        r"!\[([^\]]*)\]\(([^)]+)\)"
    )

    for alt, target in image_re.findall(body):
        target = target.strip().split()[0]

        if not alt.strip():
            qa.error(
                f"{path.name}: figure with empty alt text: {target}"
            )

        if re.match(
            r"^(?:https?|data):",
            target,
        ):
            continue

        asset = (
            path.parent
            / target.split("#", 1)[0]
        ).resolve()

        if not asset.exists():
            qa.error(
                f"{path.name}: missing figure asset: {target}"
            )


def check_placeholders(
    path: Path,
    body: str,
    qa: QA,
) -> None:
    for number, line in enumerate(
        body.splitlines(),
        1,
    ):
        if PLACEHOLDER_RE.search(line):
            qa.error(
                f"{path.name}: unresolved marker "
                f"near chapter-body line {number}: {line.strip()}"
            )


def check_gate2_pdf(
    chapter: Path,
    qa: QA,
) -> None:
    pdf = chapter.with_suffix(".pdf")

    if not pdf.is_file():
        qa.error(
            f"{chapter.name}: Gate 2 PDF missing: {pdf.name}"
        )
        return

    if pdf.read_bytes()[:5] != b"%PDF-":
        qa.error(
            f"{chapter.name}: {pdf.name} is not a valid PDF"
        )


def check_git_diff(
    root: Path,
    qa: QA,
) -> None:
    result = subprocess.run(
        ["git", "diff", "--check"],
        cwd=root,
        text=True,
        capture_output=True,
    )

    if result.returncode:
        qa.error(
            "git diff --check failed:\n"
            + (result.stdout + result.stderr).strip()
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        "chapters",
        nargs="+",
        type=Path,
    )

    parser.add_argument(
        "--gate2",
        action="store_true",
        help="Require canonical PDF beside each Markdown chapter.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    qa = QA()

    bib = bibliography_keys(
        root / "references" / "bibliography.bib",
        qa,
    )

    for supplied in args.chapters:
        chapter = (
            supplied
            if supplied.is_absolute()
            else root / supplied
        ).resolve()

        if not chapter.is_file():
            qa.error(
                f"Chapter not found: {supplied}"
            )
            continue

        metadata, body = read_chapter(
            chapter,
            qa,
        )

        check_identity(
            chapter,
            metadata,
            body,
            qa,
        )

        check_citations(
            body,
            bib,
            chapter,
            qa,
        )

        check_figures(
            chapter,
            body,
            qa,
        )

        check_placeholders(
            chapter,
            body,
            qa,
        )

        if args.gate2:
            check_gate2_pdf(
                chapter,
                qa,
            )

    check_git_diff(
        root,
        qa,
    )

    return qa.report()


if __name__ == "__main__":
    raise SystemExit(main())