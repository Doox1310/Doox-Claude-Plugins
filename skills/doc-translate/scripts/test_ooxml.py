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


def _hostile(k):
    """HOSTILE around the text, keeping leading/trailing empty lines where they are —
    a translation keeps the paragraph's line structure."""
    body = k.strip("\n")
    lead = k[: len(k) - len(k.lstrip("\n"))]
    trail = k[len(k.rstrip("\n")):]
    return lead + HOSTILE.format(body) + trail


def check(path):
    src_parts, src_formulas, src_sheets = probe(path)
    strings = list(ooxml.extract(path))
    assert strings, f"{path}: nothing extracted"
    table = {k: _hostile(k) for k in strings}
    # One string deliberately passed through untranslated, the way a mã hiệu is.
    passthrough = strings[0]
    table[passthrough] = passthrough

    out = os.path.join(tempfile.mkdtemp(), "out" + os.path.splitext(path)[1])
    written, used, collapsed = ooxml.apply(path, table, out)
    assert not collapsed, f"{path}: {len(collapsed)} strings collapsed onto one line"
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


def _mini(ext, body):
    """A two-part OOXML stub: enough for extract/apply, not for an office app."""
    part = {".docx": "word/document.xml", ".pptx": "ppt/slides/slide1.xml"}[ext]
    path = os.path.join(tempfile.mkdtemp(), "mini" + ext)
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("[Content_Types].xml", "<Types/>")
        z.writestr(part, body)
    return path, part


def selftest():
    """Line breaks inside one paragraph survive a round trip (a past bug: the
    translation landed on the first line and left the break lines empty)."""
    cases = {
        ".docx": '<w:p><w:r><w:t>Thị trường: BBN</w:t></w:r><w:r><w:br/></w:r>'
                 '<w:r><w:t>Tình trạng: </w:t><w:t>xong</w:t><w:br/><w:t>Hạn: 2/11</w:t></w:r></w:p>',
        ".pptx": '<a:p><a:r><a:t>Dòng một</a:t></a:r><a:br/><a:r><a:t>Dòng hai</a:t></a:r></a:p>',
    }
    for ext, body in cases.items():
        path, part = _mini(ext, body)
        src = list(ooxml.extract(path))
        assert len(src) == 1 and src[0].count("\n") == body.count("br"), (ext, src)
        dst = "\n".join(f"EN {i}" for i in range(src[0].count("\n") + 1))
        out = path.replace("mini", "out")
        _, _, collapsed = ooxml.apply(path, {src[0]: dst}, out)
        assert not collapsed, ext
        assert list(ooxml.extract(out)) == [dst], (ext, list(ooxml.extract(out)))
        with zipfile.ZipFile(out) as z:
            xml = z.read(part).decode("utf-8")
        # every line sits before the break that ends it, never piled onto line 1
        order = [xml.index(f"EN {i}") for i in range(dst.count("\n") + 1)]
        brs = [m.start() for m in re.finditer(r"<(w|a):br", xml)]
        assert all(order[i] < brs[i] < order[i + 1] for i in range(len(brs))), (ext, xml)
    print("selftest passed")


if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        selftest()
        sys.exit(0)
    for f in files:
        check(f)
    print("all passed")
