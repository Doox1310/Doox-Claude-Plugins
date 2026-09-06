#!/usr/bin/env python3
"""Round-trip check for ooxml.py: translate every string, reopen the document.

    python test_ooxml.py <file.docx|file.xlsx|file.pptx> [more files...]

The stand-in translation is deliberately hostile — it carries `&`, `<`, `"` and a
leading space, the four things that silently corrupt an OOXML part. A file that
still opens, keeps its sheets/slides/formulas and shows the translated text is the
whole contract of the script.
"""

import json
import os
import re
import sys
import tempfile
import zipfile

import ooxml

HOSTILE = ' <EN> {} & "co" '


def probe(path):
    """Structural fingerprint that translation must not change."""
    with zipfile.ZipFile(path) as z:
        parts = sorted(z.namelist())
        formulas = sum(
            len(re.findall(r"<f[ >]", z.read(n).decode("utf-8", "replace")))
            for n in parts
            if n.startswith("xl/worksheets/")
        )
        sheets = re.findall(
            r'<sheet name="([^"]*)"', z.read("xl/workbook.xml").decode("utf-8")
        ) if "xl/workbook.xml" in parts else []
    return parts, formulas, sheets


def check(path):
    src_parts, src_formulas, src_sheets = probe(path)
    strings = list(ooxml.extract(path))
    assert strings, f"{path}: nothing extracted"
    table = {k: HOSTILE.format(k) for k in strings}
    # One string deliberately passed through untranslated, the way a mã hiệu is.
    passthrough = strings[0]
    table[passthrough] = passthrough

    out = os.path.join(tempfile.mkdtemp(), "out" + os.path.splitext(path)[1])
    written, used = ooxml.apply(path, table, out)
    assert used == set(table), f"{path}: {len(set(table) - used)} strings not written"
    assert written, f"{path}: no part rewritten"

    out_parts, out_formulas, out_sheets = probe(out)
    assert out_parts == src_parts, f"{path}: part list changed"
    assert out_formulas == src_formulas, f"{path}: formulas lost"
    assert out_sheets == src_sheets, f"{path}: sheet names changed"

    # Re-extracting the output must yield exactly the translations, which proves the
    # text landed in the document and is readable back out of it.
    again = set(ooxml.extract(out))
    assert again == set(table.values()), f"{path}: text did not round-trip"
    assert passthrough in again, f"{path}: pass-through string was altered"

    os.remove(out)
    print(f"OK  {len(table):4d} strings, {written} parts, {src_formulas} formulas  {path}")


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        sys.exit(__doc__)
    for f in files:
        check(f)
    print("all passed")
