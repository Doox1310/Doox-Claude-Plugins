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

# part pattern -> (paragraph tag, text tag, line-break pattern)
# The paragraph is the translation unit: a single sentence is routinely split
# across several text nodes ("Điện 1 " + "pha"), so nodes must be merged first.
# A line break inside the paragraph becomes "\n" in the merged text, so each line
# of the translation can go back in front of its own break.
FORMATS = {
    ".docx": (
        re.compile(r"^word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$"),
        "w:p",
        "w:t",
        re.compile(r"<w:(?:br|cr)\b[^>]*/>"),
    ),
    ".pptx": (
        re.compile(r"^ppt/(slides|notesSlides|diagrams)/[^/]+\.xml$"),
        "a:p",
        "a:t",
        re.compile(r"<a:br\b[^>]*/>|<a:br\b[^>]*>.*?</a:br>", re.S),
    ),
    # Every string in a workbook lives in sharedStrings.xml. Worksheet XML holds
    # formulas and cell references and is deliberately out of scope: renaming a
    # sheet or rewriting a formula string breaks the workbook. A newline in a cell
    # is a literal "\n" inside <t>, so no break pattern is needed.
    ".xlsx": (re.compile(r"^xl/sharedStrings\.xml$"), "si", "t", None),
}

def _fmt(path):
    ext = os.path.splitext(path)[1].lower()
    if ext not in FORMATS:
        sys.exit(f"unsupported format: {ext} (expected .docx, .xlsx or .pptx)")
    return FORMATS[ext]


def _paragraphs(xml, ptag, ttag, brk):
    """Yield (match, lines) for every paragraph holding text.

    `lines` holds one list of text-node matches per line of the paragraph — the
    line breaks split it — so a line may be an empty list.
    """
    para = re.compile(rf"<{ptag}(?:\s[^>]*)?>.*?</{ptag}>", re.S)
    text = re.compile(rf"(<{ttag}(?:\s[^>]*)?>)(.*?)(</{ttag}>)", re.S)
    for p in para.finditer(xml):
        body = p.group(0)
        nodes = list(text.finditer(body))
        if not nodes:
            continue
        breaks = [b.start() for b in brk.finditer(body)] if brk else []
        lines = [[] for _ in range(len(breaks) + 1)]
        for n in nodes:
            lines[sum(b < n.start() for b in breaks)].append(n)
        yield p, lines


def _merged(lines):
    """The paragraph's full text, one "\n" per line break, XML entities resolved."""
    return html.unescape("\n".join("".join(n.group(2) for n in line) for line in lines))


def _translatable(s):
    """A string with no letter in it has no prose: numbers, dates, bullets, "220V".

    Dropping these before the model sees them is most of the cost saving, and it
    cannot lose wording — there is none to lose.
    """
    return bool(s.strip()) and not re.fullmatch(r"[\W\d_]+", s, re.UNICODE)


def extract(path):
    ppat, ptag, ttag, brk = _fmt(path)
    found = {}
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not ppat.match(name):
                continue
            xml = z.read(name).decode("utf-8")
            for _, lines in _paragraphs(xml, ptag, ttag, brk):
                s = _merged(lines)
                if _translatable(s):
                    found.setdefault(s, "")
    return found


def apply(path, table, out):
    """Returns (parts rewritten, sources written, sources whose line count differed)."""
    ppat, ptag, ttag, brk = _fmt(path)
    used, collapsed, rewritten = set(), set(), 0
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(
        out, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if ppat.match(item.filename):
                new = _rewrite(data.decode("utf-8"), ptag, ttag, brk, table, used, collapsed)
                if new is not None:
                    data, rewritten = new.encode("utf-8"), rewritten + 1
            zout.writestr(item, data)
    return rewritten, used, collapsed


def _rewrite(xml, ptag, ttag, brk, table, used, collapsed):
    """Put each line of a translation into the first text node of that line, empty
    the rest of the line's nodes, and leave every break where it was.

    A translation whose line count differs from the paragraph's is written on the
    first line with its newlines turned into spaces, and reported, rather than
    guessed onto lines it may not belong to.

    Formatting that varies inside one paragraph (a bold word mid-sentence) is lost;
    the alternative is translating fragments, which produces nonsense. Text is
    re-escaped on the way in: a translation containing & or < corrupts the file
    otherwise, and the corruption is silent until the document is opened.
    """
    edits = []
    for p, lines in _paragraphs(xml, ptag, ttag, brk):
        src = _merged(lines)
        dst = table.get(src)
        if not dst:
            continue
        # A translation identical to its source is a deliberate pass-through — a mã
        # hiệu, a tên pháp lý. It is handled, so it must not be reported as missing;
        # rewriting it would only collapse the paragraph's runs for nothing.
        used.add(src)
        if dst == src:
            continue
        # Without a break tag (xlsx) a "\n" is literal cell text and stays in place.
        parts = dst.split("\n") if brk else [dst]
        # Translators often drop trailing empty lines; those lines hold no text.
        if len(parts) < len(lines) and not any(lines[len(parts):]):
            parts += [""] * (len(lines) - len(parts))
        fits = len(parts) == len(lines) and all(
            line or not part for line, part in zip(lines, parts)
        )
        if not fits:
            collapsed.add(src)
            parts = [" ".join(parts)] + [""] * (len(lines) - 1)
            lines = [[n for line in lines for n in line]] + [[] for _ in lines[1:]]
        for line, part in zip(lines, parts):
            for i, n in enumerate(line):
                # Node offsets are relative to the paragraph; edits are applied to
                # the whole part, so shift them. Without this the replacements land
                # inside neighbouring tags and the document will not open.
                start, end = p.start() + n.start(), p.start() + n.end()
                open_tag = n.group(1)
                if i == 0:
                    # Leading/trailing spaces are dropped by readers unless the node
                    # says to keep them, and merging often moves a space to the front.
                    if "xml:space" not in open_tag:
                        open_tag = f"{open_tag[:-1]} xml:space={quoteattr('preserve')}>"
                    edits.append((start, end, open_tag + escape(part) + n.group(3)))
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
    parts, used, collapsed = apply(args.file, table, args.out)
    missing = sorted(set(table) - used)
    print(f"{len(used)} strings written across {parts} parts -> {args.out}")
    if collapsed:
        print(f"WARNING {len(collapsed)} translations have a different number of lines")
        print("than their source and were written on one line (keep one \\n per line):")
        for s in sorted(collapsed)[:10]:
            print("  " + s.replace("\n", " / ")[:70])
    if missing:
        print(f"WARNING {len(missing)} translations matched nothing:")
        for s in missing[:10]:
            print("  " + s[:70])


if __name__ == "__main__":
    main()
