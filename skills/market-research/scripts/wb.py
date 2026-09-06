#!/usr/bin/env python3
"""Compact workbook inspector and batch writer for the market-report framework.

The report sheet declares roughly 22,000 cells but fills fewer than 300 of them,
so an unguarded dump costs orders of magnitude more than the content is worth.
Both subcommands exist to keep that cost bounded and predictable.

    python wb.py cells   <file.xlsx> [--sheet NAME]...
    python wb.py inspect <file.xlsx> [--sheet NAME]... [--rows 15:25] [--max-chars N]
    python wb.py write   <file.xlsx> <cells.json>
    python wb.py selftest
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter


def merged_anchors(ws):
    """Map every cell inside a merged range to that range's top-left anchor."""
    anchors = {}
    for rng in ws.merged_cells.ranges:
        anchor = f"{get_column_letter(rng.min_col)}{rng.min_row}"
        for row in range(rng.min_row, rng.max_row + 1):
            for col in range(rng.min_col, rng.max_col + 1):
                anchors[f"{get_column_letter(col)}{row}"] = anchor
    return anchors


DEDUPE_MIN_CHARS = 40


def inspect(path, sheets, max_chars, rows=None):
    wb = openpyxl.load_workbook(path)
    lo, hi = rows if rows else (1, None)
    for ws in wb:
        if sheets and ws.title not in sheets:
            continue
        ranges = sorted(str(r) for r in ws.merged_cells.ranges)
        print(f"# sheet: {ws.title} | dims {ws.dimensions} | merged {len(ranges)}")
        if ranges:
            print("# merged: " + " ".join(ranges))
        count = 0
        # The framework repeats the same placeholder paragraph down whole blocks
        # (rows 17-25, 28-34): ~44% of this sheet's text is literal duplication.
        # Print each distinct string once and point later cells at it.
        first_seen = {}
        for row in ws.iter_rows(min_row=lo, max_row=hi):
            for cell in row:
                if cell.value is None:
                    continue
                text = str(cell.value)
                count += 1
                if len(text) >= DEDUPE_MIN_CHARS:
                    origin = first_seen.get(text)
                    if origin:
                        print(f"{cell.coordinate}\t<same as {origin}>")
                        continue
                    first_seen[text] = cell.coordinate
                if len(text) > max_chars:
                    text = f"{text[:max_chars]}…(+{len(text) - max_chars} chars)"
                print(f"{cell.coordinate}\t" + text.replace("\n", "\\n"))
        print(f"# non-empty: {count}\n")


HEADER_LABEL_MAX = 60


def _is_title_row(ws, row):
    """A block title: column A in caps, alone on its row apart from framework notes."""
    label = ws[f"A{row}"].value
    return bool(label) and str(label) == str(label).upper() and len(str(label)) > 3


def writable_cells(ws, max_col=6):
    """Coordinates the report may write, by the framework's own layout conventions.

    Column A holds fixed row labels. A block title row, and the column-header row
    directly beneath it, are structure. Everything else that already carries
    placeholder text is an output cell; an empty cell was never required.
    """
    cols = [get_column_letter(i) for i in range(1, max_col + 1)]
    used = [
        r
        for r in range(1, ws.max_row + 1)
        if any(ws[f"{c}{r}"].value is not None for c in cols)
    ]
    titles = [r for r in used if _is_title_row(ws, r)]
    headers = [
        r
        for r in used
        if r - 1 in titles
        and all(
            len(str(ws[f"{c}{r}"].value)) < HEADER_LABEL_MAX
            for c in cols
            if ws[f"{c}{r}"].value is not None
        )
    ]
    skip = set(titles) | set(headers)
    cells = {
        r: [c for c in cols[1:] if ws[f"{c}{r}"].value is not None]
        for r in used
        if r not in skip
    }
    return {r: c for r, c in cells.items() if c}, titles, headers


def cells_cmd(path, sheets):
    for ws in openpyxl.load_workbook(path):
        if sheets and ws.title not in sheets:
            continue
        cells, titles, headers = writable_cells(ws)
        print(f"# sheet: {ws.title}")
        print(f"# title rows (never write): {titles}")
        print(f"# header rows (never write): {headers}")
        for row in sorted(cells):
            print(f"{row}: " + " ".join(cells[row]))
        print(f"# writable: {sum(len(c) for c in cells.values())}\n")


def write(path, payload):
    """Write {sheet: {cell: value}}. Validates everything before saving anything.

    A list value is joined with newlines, so a JSON batch can express the one
    line per fact shape the report requires without escaping "\\n" by hand.
    """
    wb = openpyxl.load_workbook(path)
    errors = []
    planned = []
    for sheet, cells in payload.items():
        if sheet not in wb.sheetnames:
            errors.append(f"no such sheet: {sheet!r} (have {wb.sheetnames})")
            continue
        ws = wb[sheet]
        anchors = merged_anchors(ws)
        for coord, value in cells.items():
            anchor = anchors.get(coord)
            if anchor and anchor != coord:
                errors.append(
                    f"{sheet}!{coord} is inside a merged range; write {anchor} instead"
                )
                continue
            if isinstance(value, list):
                value = "\n".join(str(line) for line in value)
            planned.append((ws, coord, value, anchor is not None))

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        raise SystemExit(1)

    for ws, coord, value, merged in planned:
        cell = ws[coord]
        cell.value = value
        if not isinstance(value, str):
            continue
        align = cell.alignment
        cell.alignment = Alignment(
            horizontal=align.horizontal,
            vertical=align.vertical or "top",
            indent=align.indent,
            wrap_text=True,
        )
        # The framework pins row heights (104, 122.75, 133.25), which clips any
        # answer longer than the placeholder it replaced. Dropping the height
        # lets Excel/LibreOffice auto-fit the wrapped text on open.
        # ponytail: merged cells never auto-fit, so leave their height alone
        # rather than shipping a font-metrics estimator for the few title rows.
        if "\n" in value and not merged:
            ws.row_dimensions[cell.row].height = None
    wb.save(path)
    print(f"wrote {len(planned)} cells to {path}")


def selftest():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "S"
    ws.merge_cells("B2:C3")
    ws["A1"] = "keep"
    ws["A4"] = "placeholder"
    ws.row_dimensions[4].height = 104
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "t.xlsx"
        wb.save(path)

        write(path, {"S": {"A2": "value", "B2": 42}})
        check = openpyxl.load_workbook(path)["S"]
        assert check["A1"].value == "keep", "existing cell was clobbered"
        assert check["A2"].value == "value"
        assert check["B2"].value == 42, "merged anchor write failed"
        assert check["A2"].alignment.wrap_text, "wrap_text must be forced on"

        write(path, {"S": {"A4": ["• one", "• two"], "A6": "flat"}})
        check = openpyxl.load_workbook(path)["S"]
        assert check["A4"].value == "• one\n• two", "list value must join on newline"
        assert check["A4"].alignment.wrap_text
        assert check.row_dimensions[4].height is None, (
            "a pinned row height clips multi-line text and must be released"
        )
        assert check.row_dimensions[6].height is None, "single-line row untouched"

        try:
            write(path, {"S": {"C3": "bad"}})
        except SystemExit:
            pass
        else:
            raise AssertionError("writing a non-anchor merged cell must fail")

        try:
            write(path, {"S": {"A5": "ok"}, "Nope": {"A1": "x"}})
        except SystemExit:
            pass
        else:
            raise AssertionError("unknown sheet must fail")
        assert openpyxl.load_workbook(path)["S"]["A5"].value is None, (
            "a rejected batch must write nothing at all"
        )

    # writable_cells must skip block titles and the column-header row beneath them,
    # while keeping a data row that happens to sit directly under a title.
    probe = openpyxl.Workbook().active
    probe["A1"] = "BẢNG 1 — TIÊU ĐỀ KHỐI"
    probe["A2"], probe["B2"], probe["C2"] = "Nhóm", "Nội dung đầu ra", "Tiêu chuẩn"
    probe["A3"], probe["B3"], probe["C3"] = "Nhãn dòng", "x" * 120, "y" * 120
    probe["A4"] = "KẾT LUẬN"
    probe["A5"], probe["B5"] = "Dòng kết luận", "z" * 120
    cells, titles, headers = writable_cells(probe)
    assert titles == [1, 4], titles
    assert headers == [2], headers
    assert cells == {3: ["B", "C"], 5: ["B"]}, cells

    print("selftest ok")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("inspect", help="dump non-empty cells and merged ranges")
    p.add_argument("file")
    p.add_argument("--sheet", action="append", default=[])
    p.add_argument("--max-chars", type=int, default=1000)
    p.add_argument("--rows", help="row range of one block, e.g. 15:25")

    p = sub.add_parser("cells", help="list the cells the report may write")
    p.add_argument("file")
    p.add_argument("--sheet", action="append", default=[])

    p = sub.add_parser("write", help="write a {sheet: {cell: value}} JSON batch")
    p.add_argument("file")
    p.add_argument("json")

    sub.add_parser("selftest", help="run the built-in checks")

    args = parser.parse_args()
    if args.cmd == "inspect":
        rows = None
        if args.rows:
            lo, _, hi = args.rows.partition(":")
            rows = (int(lo), int(hi) if hi else None)
        inspect(args.file, set(args.sheet), args.max_chars, rows)
    elif args.cmd == "cells":
        cells_cmd(args.file, set(args.sheet))
    elif args.cmd == "write":
        write(args.file, json.loads(Path(args.json).read_text(encoding="utf-8")))
    else:
        selftest()


if __name__ == "__main__":
    main()
