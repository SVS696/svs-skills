"""Build Markdown reading copies of the fingerprinted editions in originals.py."""

from collections import defaultdict
import html
import re


def descendants(node):
    yield node
    for child in node.get("children", []):
        yield from descendants(child)


def index_structure(roots):
    """Index the publisher's logical table cells by physical page and marked-content ID."""
    pages = defaultdict(list)

    def visit(node):
        if node["type"] == "Table":
            page_rows = defaultdict(list)
            for row in descendants(node):
                if row["type"] != "TR":
                    continue
                cells = [c for c in row["children"] if c["type"] in ("TD", "TH")]
                for page in sorted({c["page_number"] for c in cells}):
                    page_rows[page].append([
                        [i for part in descendants(c) if part.get("page_number") == page
                         for i in part.get("mcids", [])] for c in cells])
            for page, rows in page_rows.items():
                pages[page].append(("table", rows))
        else:
            if node.get("mcids"):
                pages[node["page_number"]].append((node["type"], node["mcids"]))
            for child in node.get("children", []):
                visit(child)
    for node in roots:
        visit(node)
    return pages


def marked_text(chars):
    parts = []
    previous = None
    for ch in chars:
        if previous is not None and ch['x0'] < previous['x0'] and abs(ch['top'] - previous['top']) > 3:
            parts.append(" ")
        parts.append(ch["text"])
        previous = ch
    return " ".join("".join(parts).split())


def table_markup(rows, dictionary):
    def cell(text):
        return text.replace("|", "&#124;")

    width = max(map(len, rows))
    if not dictionary and width == 1:
        return "\n\n".join(row[0] for row in rows if row[0])
    if dictionary and width != 4:
        raise ValueError(f"Expected four dictionary columns, found {width}")
    if any(len(row) != width for row in rows):
        result = ["<table>"]
        for row in rows:
            # This edition also uses single full-width rows for section labels.
            span = f' colspan="{width}"' if len(row) == 1 else ""
            result.append("<tr>" + "".join(f"<td{span}>{v}</td>" for v in row) + "</tr>")
        return "\n".join([*result, "</table>"])
    if dictionary:
        header = ["Word (part of speech)", "Approved meaning / ALTERNATIVES", "STE EXAMPLE", "Non-STE example"]
    else:
        # Some tagged tables start directly with an example. Keep the first row as data.
        header = [""] * width
    return "\n".join("| " + " | ".join(map(cell, row)) + " |"
                     for row in [header, ["---"] * width, *rows])


def ste_pages(path, output):
    import pdfplumber
    import pymupdf

    with pdfplumber.open(path) as pdf, pymupdf.open(path) as visual:
        if len(pdf.pages) != 434:
            raise ValueError("Expected the 434-page Issue 9 edition.")
        index = index_structure(pdf.structure_tree)
        for number, page in enumerate(pdf.pages, 1):
            chars = defaultdict(list)
            for ch in page.chars:
                chars[ch.get("mcid")].append(ch)
            blocks = []
            used = set()
            dictionary = 149 <= number <= 433
            for kind, item in index[number]:
                ids = [i for row in item for cell in row for i in cell] if kind == "table" else item
                used.update(ids)
                positions = [c["top"] for i in ids for c in chars[i] if c["text"].strip()]
                if not positions:
                    continue
                if kind == "table":
                    rows = [["<br>".join(html.escape(t, quote=False) for i in cell
                                         if (t := marked_text(chars[i]))) for cell in row] for row in item]
                    if dictionary and any(len(row) != 4 for row in rows):
                        # Empty structural cells can be absent from the PDF tag tree.
                        # Position the remaining cells under their printed headings.
                        headings = ("Word", "Approved", "STE", "Non-STE")
                        labels = {w["text"]: w["x0"] for w in page.extract_words()
                                  if 60 < w["top"] < 88 and w["text"] in headings}
                        for idx, row in enumerate(rows):
                            if len(row) == 4:
                                continue
                            fixed = [""] * 4
                            for cell_ids, value in zip(item[idx], row):
                                if value:
                                    x = min(ch["x0"] for i in cell_ids for ch in chars[i] if ch["text"].strip())
                                    col = min(range(4), key=lambda j: abs(labels[headings[j]] - x))
                                    if fixed[col]:
                                        raise ValueError(f"Overlapping dictionary cells on page {number}")
                                    fixed[col] = value
                            rows[idx] = fixed
                    body = table_markup(rows, dictionary)
                else:
                    body = html.escape(marked_text([c for i in ids for c in chars[i]]), quote=False)
                    if kind in {"H1", "H2", "H3"}:
                        body = "### " + body
                blocks.append((min(positions), body))
            # Retain body text outside the structure tree, including inserted pages.
            extra = defaultdict(list)
            for i, group in chars.items():
                if i in used:
                    continue
                for ch in group:
                    if (i is not None or 58 < ch["top"] < 720) and not (dictionary and ch["top"] < 89):
                        extra[round(ch["top"])].append(ch)
            for top, group in extra.items():
                body = marked_text(sorted(group, key=lambda c: c["x0"]))
                if body:
                    blocks.append((top, html.escape(body, quote=False)))
            sheet = visual[number - 1]
            for idx, image in enumerate(sheet.get_image_info(), 1):
                box = pymupdf.Rect(image["bbox"])
                if box.y1 < 58 or box.is_empty:
                    continue
                asset = f"{path.stem}-p{number:03d}-{idx}.png"
                sheet.get_pixmap(matrix=pymupdf.Matrix(2, 2), clip=box).save(output / asset)
                blocks.append((box.y0, f"![Illustration on page {number}]({asset})"))
            page.close()
            yield "\n\n".join(value for _, value in sorted(blocks, key=lambda pair: pair[0]) if value)


def bernth_pages(path):
    import pymupdf

    with pymupdf.open(path) as doc:
        if len(doc) != 7:
            raise ValueError("Expected the seven-page ANLP paper.")
        for page in doc:
            # The publisher's OCR stores blocks in reading order across the two columns.
            paragraphs = []
            for block in page.get_text("blocks", sort=False):
                lines = [s.strip() for s in block[4].splitlines() if s.strip()]
                paragraph = re.sub(r"(?<=[a-z])-\n(?=[a-z])", "", "\n".join(lines)).replace("\n", " ")
                # Two errors in the embedded OCR were checked against the scanned page.
                paragraph = paragraph.replace("Clarity Indez", "Clarity Index")
                paragraph = paragraph.replace("arendse@wat son. ibm. cora", "arendse@watson.ibm.com")
                if paragraph:
                    heading = (paragraph in {"Abstract", "References"}
                               or re.match(r"^[1-8] [A-Z]", paragraph) and len(paragraph) < 80)
                    paragraphs.append(("### " if heading else "") + html.escape(paragraph, quote=False))
            yield "\n\n".join(paragraphs)



def iso_pages(path, output):
    import pymupdf

    # Top edges of the eight vector illustrations in the fingerprinted course edition.
    figures = {19: 498, 25: 62, 27: 86, 28: 62, 60: 109, 61: 261, 63: 80, 64: 260}
    with pymupdf.open(path) as doc:
        if len(doc) != 104:
            raise ValueError("Expected the 104-page BYU course copy of the second edition.")
        for n, page in enumerate(doc, 1):
            blocks = page.get_text("blocks", sort=True)
            paragraphs = []
            for box in blocks:
                raw = box[4].replace("\ufeff", "").strip()
                text = " ".join(raw.split())
                if not text:
                    continue
                if n in figures and re.match(r"^Figure \d+ —", text):
                    top = figures[n]
                    area = pymupdf.Rect()
                    for drawing in page.get_drawings():
                        bounds = drawing["rect"]
                        if bounds.y0 >= top and bounds.y1 <= box[1] + 1:
                            area |= bounds + (-2, -2, 2, 2)
                    if area.is_empty:
                        raise ValueError(f"Figure bounds missing on page {n}")
                    asset = f"{path.stem}-p{n:03d}.png"
                    page.get_pixmap(matrix=pymupdf.Matrix(2, 2), clip=area).save(output / asset)
                    paragraphs.append(f"![{text}]({asset})")
                if re.match(r"^\d+(?:\.\d+){0,4}\s+[A-Z]", text) and len(text) < 110:
                    paragraphs.append("### " + text)
                else:
                    paragraphs.append(html.escape(text, quote=False))
            yield "\n\n".join(paragraphs)

def rfc_text(path):
    pages = path.read_text(encoding="utf-8").strip().split("\f")
    blocks = []
    for number, page in enumerate(pages, 1):
        lines = [line for line in page.splitlines()
                 if not re.match(r"^(?:Bradner|Leiba).*\[Page \d+\]", line)
                 and not (number > 1 and re.match(r"^RFC (?:2119|8174)\s", line))]
        for block in re.split(r"\n\s*\n", "\n".join(lines).strip()):
            text = " ".join(block.split())
            if not text:
                continue
            if ". . ." in block:
                blocks.append("\n".join("- " + line.strip() for line in block.splitlines() if line.strip()))
            elif re.match(r"^\d+\. +", text):
                if path.stem == "RFC2119" and "   " in block.splitlines()[0].lstrip():
                    heading, rest = re.split(r" {2,}", block.lstrip(), maxsplit=1)
                    blocks.extend(["## " + heading, " ".join(rest.split())])
                else:
                    blocks.append("## " + text)
            else:
                blocks.append(text)
    return "\n\n".join(blocks)


def build(path, output, url):
    if path.suffix == ".txt":
        body = f"# {path.stem}\n\n[Source edition]({url})\n\n" + rfc_text(path)
    else:
        is_ste = path.stem.startswith("ASD-")
        if is_ste:
            title = "ASD-STE100 Simplified Technical English, Issue 9"
            pages = ste_pages(path, output)
        elif path.stem.startswith("ISO-"):
            title = "ISO/IEC/IEEE 29148:2018 — Requirements engineering"
            pages = iso_pages(path, output)
        else:
            title = "EasyEnglish: A Tool for Improving Document Quality"
            pages = bernth_pages(path)
        parts = [f"# {title}", f"[Source edition]({url}). Local reading copy. Page numbers include the cover."]
        if is_ste:
            parts.append("[Writing rules](#page-43) · [Dictionary introduction](#page-129) · [Alphabetical entries](#page-149)")
        for n, text in enumerate(pages, 1):
            parts.extend([f"## Page {n}", f"[Source page {n}]({url}#page={n})", text])
        body = "\n\n".join(parts)
    (output / path.with_suffix(".md").name).write_text(body.rstrip() + "\n", encoding="utf-8")
