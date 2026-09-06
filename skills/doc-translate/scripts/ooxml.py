#!/usr/bin/env python3
"""Extract translatable text from an OOXML file, and write translations back.

.docx / .xlsx / .pptx are ZIP archives of XML. Translating them in place — rather
than rebuilding the document — is what preserves the formatting: every part we do
not touch is copied byte for byte.

    python ooxml.py extract <file> [-o strings.json]
    python ooxml.py apply   <file> <translations.json> -o <out>

`extract` writes a JSON object mapping each unique source string to "". Fill in the
values and hand the file to `apply`. A key left empty is left untranslated.
"""

import argparse
import html
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape, quoteattr

# part pattern -> (paragraph tag, text tag)
# The paragraph is the translation unit: a single sentence is routinely split
# across several text nodes ("Điện 1 " + "pha"), so nodes must be merged first.
FORMATS = {
    ".docx": (
        re.compile(r"^word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$"),
        "w:p",
        "w:t",
    ),
    ".pptx": (
        re.compile(r"^ppt/(slides|notesSlides|diagrams)/[^/]+\.xml$"),
        "a:p",
        "a:t",
    ),
    # Every string in a workbook lives in sharedStrings.xml. Worksheet XML holds
    # formulas and cell references and is deliberately out of scope: renaming a
    # sheet or rewriting a formula string breaks the workbook.
    ".xlsx": (re.compile(r"^xl/sharedStrings\.xml$"), "si", "t"),
}

def _fmt(path):
    ext = os.path.splitext(path)[1].lower()
    if ext not in FORMATS:
        sys.exit(f"unsupported format: {ext} (expected .docx, .xlsx or .pptx)")
    return FORMATS[ext]


def _paragraphs(xml, ptag, ttag):
    """Yield (match, [text node matches]) for every paragraph holding text."""
    para = re.compile(rf"<{ptag}(?:\s[^>]*)?>.*?</{ptag}>", re.S)
    text = re.compile(rf"(<{ttag}(?:\s[^>]*)?>)(.*?)(</{ttag}>)", re.S)
    for p in para.finditer(xml):
        nodes = list(text.finditer(p.group(0)))
        if nodes:
            yield p, nodes


def _merged(nodes):
    """The paragraph's full text, XML entities resolved."""
    return html.unescape("".join(n.group(2) for n in nodes))


def _translatable(s):
    """A string with no letter in it has no prose: numbers, dates, bullets, "220V".

    Dropping these before the model sees them is most of the cost saving, and it
    cannot lose wording — there is none to lose.
    """
    return bool(s.strip()) and not re.fullmatch(r"[\W\d_]+", s, re.UNICODE)


def extract(path):
    ppat, ptag, ttag = _fmt(path)
    found = {}
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not ppat.match(name):
                continue
            xml = z.read(name).decode("utf-8")
            for _, nodes in _paragraphs(xml, ptag, ttag):
                s = _merged(nodes)
                if _translatable(s):
                    found.setdefault(s, "")
    return found


def apply(path, table, out):
    ppat, ptag, ttag = _fmt(path)
    used, rewritten = set(), 0
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(
        out, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if ppat.match(item.filename):
                new = _rewrite(data.decode("utf-8"), ptag, ttag, table, used)
                if new is not None:
                    data, rewritten = new.encode("utf-8"), rewritten + 1
            zout.writestr(item, data)
    return rewritten, used


def _rewrite(xml, ptag, ttag, table, used):
    """Put each paragraph's translation into its first text node, empty the rest.

    Formatting that varies inside one paragraph (a bold word mid-sentence) is lost;
    the alternative is translating fragments, which produces nonsense. Text is
    re-escaped on the way in: a translation containing & or < corrupts the file
    otherwise, and the corruption is silent until the document is opened.
    """
    edits = []
    for p, nodes in _paragraphs(xml, ptag, ttag):
        src = _merged(nodes)
        dst = table.get(src)
        if not dst:
            continue
        # A translation identical to its source is a deliberate pass-through — a mã
        # hiệu, a tên pháp lý. It is handled, so it must not be reported as missing;
        # rewriting it would only collapse the paragraph's runs for nothing.
        used.add(src)
        if dst == src:
            continue
        for i, n in enumerate(nodes):
            # Node offsets are relative to the paragraph; edits are applied to the
            # whole part, so shift them. Without this the replacements land inside
            # neighbouring tags and the document will not open.
            start, end = p.start() + n.start(), p.start() + n.end()
            open_tag = n.group(1)
            if i == 0:
                # Leading/trailing spaces are dropped by readers unless the node
                # says to keep them, and merging often moves a space to the front.
                if "xml:space" not in open_tag:
                    open_tag = f"{open_tag[:-1]} xml:space={quoteattr('preserve')}>"
                edits.append((start, end, open_tag + escape(dst) + n.group(3)))
            else:
                edits.append((start, end, n.group(1) + n.group(3)))
    if not edits:
        return None
    out, last = [], 0
    for start, end, repl in sorted(edits):
        out.append(xml[last:start])
        out.append(repl)
        last = end
    out.append(xml[last:])
    return "".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract")
    e.add_argument("file")
    e.add_argument("-o", "--out")
    a = sub.add_parser("apply")
    a.add_argument("file")
    a.add_argument("translations")
    a.add_argument("-o", "--out", required=True)
    args = ap.parse_args()

    if args.cmd == "extract":
        found = extract(args.file)
        text = json.dumps(found, ensure_ascii=False, indent=1)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"{len(found)} strings -> {args.out}")
        else:
            print(text)
        return

    with open(args.translations, encoding="utf-8") as f:
        table = {k: v for k, v in json.load(f).items() if v}
    if os.path.abspath(args.file) == os.path.abspath(args.out):
        sys.exit("refusing to overwrite the source document")
    parts, used = apply(args.file, table, args.out)
    missing = sorted(set(table) - used)
    print(f"{len(used)} strings written across {parts} parts -> {args.out}")
    if missing:
        print(f"WARNING {len(missing)} translations matched nothing:")
        for s in missing[:10]:
            print("  " + s[:70])


if __name__ == "__main__":
    main()
