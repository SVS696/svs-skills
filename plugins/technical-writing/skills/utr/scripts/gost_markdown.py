"""Build local Markdown reading copies of the five verified GOST PDFs (Poppler)."""

import re
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

# Pages where the original layout illustrates a rule, form, diagram or formula.
# Page indices count from the PDF cover, including unnumbered sheets.
LAYOUT_PAGES = {
    "GOST-2.105-95": (25, {5, 6, *range(9, 18), *range(20, 26)}),
    "GOST-34.602-2020": (14, set()),
    "GOST-R-2.105-2019": (58, {14, *range(15, 26), 29, *range(31, 38),
                                *range(42, 47), 52, 53}),
    "GOST-R-58049-2017": (24, {10, 21, 22}),
    "GOST-R-59194-2020": (19, {14, 18}),
}


CLAUSE = re.compile(r"^(\d+(?:\.\d+){1,5})\.?\s+(?=\S)")
SECTION = re.compile(r"^\d{1,2}\.?\s+[А-ЯЁ][а-яё]")
APPENDIX = re.compile(r"^Приложение\s+[А-ЯЁA-Z](?:\s*\(.+\))?$")
GAP = re.compile(r"\S {4,}\S")


def format_block(lines):
    stripped = [line.strip() for line in lines]
    # Preserve columns, rules and diagrams in the PDF text layer.
    if (sum(bool(GAP.search(line)) for line in stripped) >= 2
            or any(re.search(r"[_─━]{5,}|[│┌┼┐]", line) for line in stripped)):
        return ["```text", *lines, "```"]
    parts = []
    for line in stripped:
        line = re.sub(r"[ \t]+", " ", line)
        if SECTION.match(line) and len(line) <= 100 and not re.search(r"[.…]{2,}", line):
            parts.append("### " + line)
        elif APPENDIX.fullmatch(line):
            parts.append("### " + line)
        elif match := CLAUSE.match(line):
            parts.append("**" + line[:match.end()].rstrip() + "** " + line[match.end():])
        elif line.startswith(("- ", "— ", "• ")) or not parts:
            parts.append(line)
        elif parts[-1].startswith("### "):
            parts.append(line)
        elif parts[-1].endswith("\u00ad"):
            parts[-1] = parts[-1][:-1] + line
        else:
            parts[-1] += " " + line
    return ["\n\n".join(parts)]


def files_for(stem):
    _, pages = LAYOUT_PAGES[stem]
    return [f"{stem}.md", *(f"{stem}-p{n:02d}.png" for n in sorted(pages))]


def output_hashes(directory, stem):
    return {name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
            for name in files_for(stem)}


def check_copy(directory, stem, source_hash):
    receipt = json.loads((directory / f"{stem}.json").read_text(encoding="utf-8"))
    if receipt != {"source_sha256": source_hash, "files": output_hashes(directory, stem)}:
        raise ValueError(f"Контрольные суммы копии {stem} различаются.")


def convert(pdf, destination, url, source_hash):
    # The caller verifies the PDF bytes against the source manifest first.
    from PIL import Image
    import pymupdf
    from gost_tables import old_page_parts, page_parts, tables_on

    raw = subprocess.check_output(["pdftotext", "-enc", "UTF-8", "-layout", str(pdf), "-"],
                                  encoding="utf-8")
    pages = raw.split("\f")
    if pages[-1] == "":
        pages.pop()
    stem = pdf.stem
    count, illustrated = LAYOUT_PAGES[stem]
    if len(pages) != count:
        raise ValueError(f"{stem}: ожидалось {count} страниц, извлечено {len(pages)}")
    title = stem.replace("GOST-R-", "ГОСТ Р ").replace("GOST-", "ГОСТ ")
    with tempfile.TemporaryDirectory(dir=destination) as tmp, pymupdf.open(pdf) as source:
        staging = Path(tmp)
        doc = [f"# {title}", "", f"[Исходное издание]({url}) · {count} страниц PDF.", "",
               "Текст извлечён автоматически. Номера страниц отсчитаны от обложки. Для точной цитаты сверьте текст со страницей издания.", "",
               "## Указатель страниц", ""]
        sections = []
        for number, page in enumerate(pages, start=1):
            anchor = f"pdf-{number}"
            doc.append(f"- [Страница {number}](#{anchor})")
            sections.extend(["", f'<a id="{anchor}"></a>', "", f"## Страница {number}", "",
                             f"[Сверить с изданием]({url}#page={number})", ""])
            if number in illustrated:
                prefix = staging / "render"
                subprocess.run(["pdftoppm", "-f", str(number), "-l", str(number),
                                "-scale-to", "2200", "-gray", "-singlefile", str(pdf), str(prefix)],
                               check=True)
                picture = staging / f"{stem}-p{number:02d}.png"
                with Image.open(prefix.with_suffix(".pgm")) as im:
                    im.point(lambda value: 255 if value > 185 else 0, mode="1").save(picture)
                sections.extend([f"![Макет страницы {number}]({picture.name})", ""])
            if not page.strip():
                sections.append("В исходном издании эта страница пустая.")
            if stem == "GOST-2.105-95":
                parts = old_page_parts(page, number)
            else:
                sheet = source[number - 1]
                tables = tables_on(sheet, stem, number)
                parts = page_parts(sheet, tables) if tables else [(False, page)]
            for is_table, content in parts:
                if is_table:
                    sections.extend([content, ""])
                else:
                    for block in re.split(r"\n[ \t]*\n", content.strip("\n")):
                        if block.strip():
                            sections.extend(format_block(block.splitlines()))
                            sections.append("")
        (staging / f"{stem}.md").write_text("\n".join(doc + sections).rstrip() + "\n",
                                             encoding="utf-8")
        receipt = f"{stem}.json"
        (staging / receipt).write_text(json.dumps({"source_sha256": source_hash,
                                                   "files": output_hashes(staging, stem)},
                                                  indent=2) + "\n", encoding="utf-8")
        for name in [*files_for(stem), receipt]:
            (staging / name).replace(destination / name)
