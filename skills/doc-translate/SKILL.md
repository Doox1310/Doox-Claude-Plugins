---
name: doc-translate
description: Use when the user hands over a .docx, .xlsx or .pptx and asks to dịch it — translate the document and hand back a file, not a chat reply. Also use when a translation must keep the original layout, formatting, images and formulas.
---

# Doc Translate

Translate a Word / Excel / PowerPoint document and return **a new file that looks
exactly like the original**. Chat-only translation of a document is `doc-compare`'s
job, not this one.

## The method, and why

An OOXML file is a ZIP of XML parts. Translating **in place** — swapping the text
nodes and copying every other part byte for byte — is what preserves the layout.
Rebuilding the document from extracted text loses it, always.

Never read the XML yourself and never rebuild the file by hand. `scripts/ooxml.py`
does both ends:

```bash
python scripts/ooxml.py extract "<file>" -o strings.json    # {"nguồn": ""}
# fill in every value
python scripts/ooxml.py apply "<file>" strings.json -o "<file>_VI.<ext>"
```

`extract` returns one entry per **unique paragraph**, filtered down to strings that
contain a letter. On a real 16-slide deck that is 166 strings out of 820 text nodes:
translate the JSON, never the document.

Read `scripts/ooxml.py` only if it errors. Its behaviour is the two commands above.

## Rules

**Translate into Vietnamese** unless the user names another target. Length of the
original, professional term the field uses. Condense only if the user also asked for
a summary.

**Names, codes and units pass through untouched** — rule `DR3` of
`../using-doox/references/document-rules.md`, which also governs this skill: tên pháp
lý, mã số thuế, mã hiệu, model, số hiệu tiêu chuẩn, đơn vị đo. `IEC 61851-1` stays
`IEC 61851-1`, `Công ty TNHH …` is not turned into English. A term with no settled
Vietnamese equivalent keeps the original in brackets the first time it appears.

`DR3` is inlined above because it is the rule this skill breaks most easily. The other
four still apply — `DR1` above all: a figure in the source document is translated, never
corrected against what the model believes it should be. Read the reference when a
document's own data looks wrong; do not read `using-doox/SKILL.md`, none of it applies
here.

**A key left `""`, or set to its own source text, is passed through untranslated** —
that is how a mã hiệu stays a mã hiệu. Both are treated as handled and neither is
reported as missing. Do not delete keys from the JSON.

**One entry per unique string, so the same source text gets the same translation
everywhere.** A word that must read differently in two places has to be edited in the
output document afterwards; say so rather than leaving the user to find it.

**Never overwrite the source.** Output is a new file, `[tên gốc]_[mã ngôn ngữ đích].[ext]` —
`_VI` for the default Vietnamese target, `_EN` when the user asked for English, and so on.
The suffix names where the file is going, so a `_VI` on an English translation mislabels
it for everyone who later opens the folder. The script takes the name from `-o` and
hardcodes nothing; it refuses only an output path equal to its input.

**Report `WARNING … matched nothing`** if `apply` prints it. It means the source
changed between the two commands, and those strings are missing from the output.

## What this cannot do, say so rather than hide it

- **Formatting that varies inside one paragraph is lost.** A sentence is routinely
  split across text nodes — `"Điện 1 "` + `"pha"` — so the paragraph is translated
  whole and written back into its first node. A bold word mid-sentence comes back
  unbolded. Translating the fragments instead produces nonsense; this is the
  deliberate trade.
- **PowerPoint text can overflow its box.** Vietnamese runs 20–30% longer than
  English. Font sizes are not shrunk and shapes are not resized. List the slides
  holding long strings so the user can check them.
- **Excel: only `sharedStrings.xml` is touched.** Formulas, named ranges, sheet
  names and number formats are out of scope by construction — renaming a sheet
  breaks every formula referring to it. Say so if the user asks for sheet names.
- **PDF is not supported.** Content can be translated into a chat reply; the layout
  cannot be reproduced. Do not pretend otherwise.
- **SmartArt** (`ppt/diagrams/`) is covered by the extract pattern but has not been
  verified on a real deck. Check the output if the deck uses it.

## Before replying

Run the round-trip check whenever the script changed:

```bash
python scripts/test_ooxml.py <any .docx/.xlsx/.pptx>
```

Then report: file written, how many strings translated, anything passed through
untranslated and why, and the slides/sheets the user should eyeball.
