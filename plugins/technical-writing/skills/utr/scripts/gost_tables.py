"""Editable tables for the exact PDF editions in originals.py."""

import html
import re

import cv2
import numpy as np
import pymupdf as fitz


# Borderless tables in the correction sheets and the approval register.
# Coordinates in PDF points delimit successive columns and rows.
FIXED = {
    ("GOST-34.602-2020", 2): ([70, 212, 326, 556], [290, 317, 335, 365, 382, 400, 418, 436, 453]),
    ("GOST-34.602-2020", 13): ([71, 239, 317, 412, 455, 555], [105, 126, 154]),
    ("GOST-34.602-2020", 14): ([71, 239, 317, 412, 455, 555], [89, 106, 136]),
    ("GOST-R-2.105-2019", 56): ([42, 169, 351, 530], [105, 125, 191]),
    ("GOST-R-2.105-2019", 57): ([42, 369, 529], [105, 126, 219, 327, 409, 485, 571, 670, 744]),
    ("GOST-R-2.105-2019", 58): ([69, 400, 556], [79, 102, 200, 233, 284, 332, 408, 460]),
}
RULED = {
    "GOST-R-58049-2017": {12, 13, 14, 15, 16, 21, 22, 23},
    "GOST-R-59194-2020": {12, 13, 14, 15},
    "GOST-R-2.105-2019": {*range(16, 23), 25, 43, 52, 53},
}


def cell_text(value):
    value = re.sub(r"\u00ad\s*", "", value or "")
    return html.escape(" ".join(value.split()), quote=False)


def pipe_table(rows):
    def row(values):
        return "| " + " | ".join(cell_text(v).replace("|", "&#124;") for v in values) + " |"
    return "\n".join([row(rows[0]), row(["---"] * len(rows[0])), *map(row, rows[1:])])


def ruled_tables(page):
    # Some editions are scans. Expose straight raster lines to the PDF table detector.
    factor = 1500 / page.rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(factor, factor), colorspace=fitz.csGRAY, alpha=False)
    gray = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
    ink = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)[1]
    lines = []
    for horizontal, shape in [(True, (1, 35)), (False, (16, 1))]:
        mask = cv2.morphologyEx(ink, cv2.MORPH_OPEN, np.ones(shape, np.uint8))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if horizontal and h <= 9:
                mid = (y + h / 2) / factor
                lines.append(((x / factor, mid), ((x + w) / factor, mid)))
            elif not horizontal and w <= 9:
                mid = (x + w / 2) / factor
                lines.append(((mid, y / factor), (mid, (y + h) / factor)))
    return page.find_tables(add_lines=lines, snap_tolerance=2, join_tolerance=3,
                            intersection_tolerance=4).tables


def ruled_markup(table, values):
    if all(cell is not None for row in table.rows for cell in row.cells):
        return pipe_table(values)
    # None marks either the covered part of a merged cell or an open edge.
    xs = sorted({c[0] for c in table.cells} | {c[2] for c in table.cells})
    ys = sorted({c[1] for c in table.cells} | {c[3] for c in table.cells})
    anchors = {}
    covered = set()
    for row, row_values in zip(table.rows, values):
        for box, value in zip(row.cells, row_values):
            if box is None:
                continue
            left, top, right, bottom = box
            x, y = xs.index(left), ys.index(top)
            width, height = xs.index(right) - x, ys.index(bottom) - y
            cols = f' colspan="{width}"' if width > 1 else ''
            rows = f' rowspan="{height}"' if height > 1 else ''
            tag = 'th' if y == 0 else 'td'
            anchors[x, y] = f'<{tag}{cols}{rows}>{cell_text(value)}</{tag}>'
            covered.update((i, j) for i in range(x, x + width) for j in range(y, y + height))
    result = ["<table>"]
    for y in range(len(ys) - 1):
        cells = [anchors.get((x, y), "" if (x, y) in covered else "<td></td>")
                 for x in range(len(xs) - 1)]
        result.append("<tr>" + "".join(cells) + "</tr>")
    return "\n".join([*result, "</table>"])


def tables_on(page, stem, number):
    key = (stem, number)
    if key in FIXED:
        xs, ys = FIXED[key]
        rows = [[page.get_text("text", clip=(l, t, r, b), sort=True)
                 for l, r in zip(xs, xs[1:])] for t, b in zip(ys, ys[1:])]
        # The following short readings and dashes were checked against the printed cells.
        if stem == "GOST-34.602-2020" and number == 2:
            rows[1][2] = "Азстандарт"
        if stem == "GOST-34.602-2020" and number in (13, 14):
            rows[1][1] = "—"
            header = "".join(f"<th>{cell_text(v)}</th>" for v in rows[0][:2])
            body = "".join(f"<td>{cell_text(v)}</td>" for v in rows[1])
            markup = (f'<table>\n<tr>{header}<th colspan="3">Должно быть</th></tr>\n'
                      f'<tr>{body}</tr>\n</table>')
        else:
            if stem == "GOST-R-2.105-2019" and number == 56:
                rows[1][1] = rows[1][1].replace("при-\n", "при")
                rows[1][2] = re.sub(r"приме-\s*йены", "применены", rows[1][2])
            if stem == "GOST-R-2.105-2019" and number in (57, 58):
                for row in rows[2 if number == 57 else 1:]:
                    row[1] = "—"
            markup = pipe_table(rows)
        return [((xs[0], ys[0], xs[-1], ys[-1]), markup)]
    if number in RULED.get(stem, ()):
        tables = []
        for table in ruled_tables(page):
            if table.col_count >= 2 and table.row_count >= 2:
                values = table.extract()
                if key == ("GOST-R-59194-2020", 14):
                    values[0][1] = "Пояснение"
                tables.append((table.bbox, ruled_markup(table, values)))
        return tables
    return []


def page_parts(page, tables):
    # Read text above and below each band. Preserve captions or notes beside a table.
    groups = []
    for box, markup in sorted(tables, key=lambda item: item[0][1]):
        if not groups or box[1] >= max(b[3] for b, _ in groups[-1]) - 1:
            groups.append([])
        groups[-1].append((box, markup))

    def text_region(left, top, right, bottom):
        if right > left and bottom > top:
            text = page.get_text("text", clip=(left, top, right, bottom), sort=True)
            if text.strip():
                yield False, text

    bottom = 0
    for group in groups:
        top = min(b[1] for b, _ in group)
        yield from text_region(0, bottom, page.rect.width, top)
        bottom = max(b[3] for b, _ in group)
        left = 0
        for box, markup in sorted(group):
            yield from text_region(left, top, box[0], bottom)
            yield from text_region(box[0], top, box[2], box[1])
            yield True, markup
            yield from text_region(box[0], box[3], box[2], bottom)
            left = box[2]
        yield from text_region(left, top, page.rect.width, bottom)
    yield from text_region(0, bottom, page.rect.width, page.rect.height)


def box_tables(lines, continues=False):
    """Read the typeset box characters in the 1995 edition before reflowing prose."""
    lines = [line.strip() for line in lines]
    top = lines[0]
    open_sides = top.startswith("─")
    if top.count("┌") > 1:
        edges = [m.end() for m in re.finditer("┐", top)][:-1]
        columns = [[] for _ in range(len(edges) + 1)]
        for line in lines:
            gaps = list(re.finditer(r"(?<=[│┐┤┘]) +(?=[│┌├└])", line))
            cuts = [min(gaps, key=lambda m: abs(m.start() - x)).start() for x in edges]
            for column, a, b in zip(columns, [0, *cuts], [*cuts, len(line)]):
                column.append(line[a:b].strip())
        return "\n\n".join(box_tables(column) for column in columns)

    # The wide bearing table wraps each physical row onto a second printed line.
    if (top.startswith("┌") and not top.endswith("┐")) or (
            continues and len(lines) > 1 and lines[1].startswith("│") and len(lines[1]) < 22):
        lines = [(a + " " + b if "│" in a else a + b)
                 for a, b in zip(lines[::2], lines[1::2], strict=True)]

    bands = []
    border = ""
    values = []
    def finish():
        if not values:
            return
        cells = [(line if open_sides else line.removeprefix("│").removesuffix("│")).split("│") for line in values]
        if len({len(row) for row in cells}) != 1:
            raise ValueError(f"Число ячеек меняется внутри строки: {values}")
        # Blank lines of cells and repeated part numbers separate unruled data rows.
        split_rows = (len(cells) > 1 and (
            any(all(not v.strip() for v in row) for row in cells)
            or all(re.match(r"^(?:\d|ПНР-)", row[0].strip()) for row in cells)))
        if split_rows:
            bands.extend((border, row) for row in cells if any(v.strip() for v in row))
            if not any(any(v.strip() for v in row) for row in cells):
                bands.append((border, cells[0]))
        else:
            bands.append((border, [" ".join(v.strip() for v in col if v.strip()) for col in zip(*cells)]))

    for line in lines:
        if line.startswith("│Примечание") and values:
            finish()
            border, values = "", []
        if "─" in line and "│" in line and not re.search(r"[а-я0-9]", line, re.I):
            finish()
            if "┘" in line:
                border = ""
            values = []
        elif "─" in line and "│" not in line:
            finish()
            border, values = line, []
        else:
            values.append(line)
    finish()
    if not bands:
        raise ValueError("В таблице не найдены строки.")
    widths = [len(row) for _, row in bands]
    if len(set(widths)) == 1:
        rows = [row for _, row in bands]
        return pipe_table(([[""] * widths[0]] if continues else []) + rows)
    # Junctions in the horizontal rules identify merged headers.
    all_edges = sorted({i for rule, _ in bands for i, c in enumerate(rule) if c in "┬┼"})
    result = ["<table>"]
    for idx, (rule, row) in enumerate(bands):
        edges = [0, *(all_edges.index(i) + 1 for i, c in enumerate(rule) if c in "┬┼"), len(all_edges) + 1]
        if len(edges) != len(row) + 1:
            raise ValueError(f"Границы строки расходятся с числом ячеек: {row}")
        tag = "th" if idx == 0 and not continues else "td"
        markup = []
        for a, b, value in zip(edges, edges[1:], row):
            span = f' colspan="{b-a}"' if b-a > 1 else ''
            markup.append(f"<{tag}{span}>{cell_text(value)}</{tag}>")
        result.append("<tr>" + "".join(markup) + "</tr>")
    return "\n".join([*result, "</table>"])


def old_page_parts(text, number):
    if number not in {7, *range(10, 18)}:
        yield False, text
        return
    lines = text.splitlines()
    start = 0
    i = 0
    while i < len(lines):
        if not re.search("[┬┼┌│]", lines[i]):
            i += 1
            continue
        yield False, "\n".join(lines[start:i])
        j = i + 1
        while j < len(lines) and re.search("[─│┘]", lines[j]):
            j += 1
        yield True, box_tables(lines[i:j], continues=not lines[i].strip().startswith(("┌", "─")))
        start = i = j
    yield False, "\n".join(lines[start:])
