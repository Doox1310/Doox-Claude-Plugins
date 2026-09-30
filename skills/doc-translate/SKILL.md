---
name: doc-translate
description: "Use when the user hands over a .docx, .xlsx or .pptx and asks to dịch it — translate the document and hand back a file, not a chat reply. Also use when a translation must keep the original layout, formatting, images and formulas. Load `using-doox` first. Reading, summarising or comparing documents is `doc-compare`; scoring quotes or dossiers is `bid-review`."
---

# Doc Translate

**`using-doox` is loaded first and routes here.** This skill uses from it only "Language" and `references/document-rules.md` (DR1–DR5); it runs no identity gate and opens no plan file.

Translate a Word / Excel / PowerPoint document into **a new file that looks exactly like the
original**. A chat-only translation is `doc-compare`'s job.

## Hard limits

- `DR1`–`DR5`. `DR3` above all — tên pháp lý, mã số thuế, mã hiệu, model, số hiệu tiêu chuẩn, đơn vị
  đo, tên riêng pass through untouched (`IEC 61851-1` stays `IEC 61851-1`, `Công ty TNHH …` is not
  turned into English). `DR1`: a figure is translated, never corrected.
- Keep layout, formatting, images and formulas: translate only through `scripts/ooxml.py`, never by
  reading or rebuilding the XML by hand. Sheet names and formulas are never touched.
- Read only the file the user supplied; never a plan file.
- **Never overwrite the source.** Output is a new local file (`using-doox` hard limit 7).
- Report what the script could not do (below) instead of hiding it.

## The method, and why

An OOXML file is a ZIP of XML parts. Swapping the text nodes and copying every other part byte for byte
preserves the layout; rebuilding from extracted text always loses it.

```bash
python scripts/ooxml.py extract "<file>" -o strings.json    # {"nguồn": ""}
# fill in every value
python scripts/ooxml.py apply "<file>" strings.json -o "<file>_VI.<ext>"
```

`extract` returns one entry per unique paragraph that contains a letter (166 strings from 820 text
nodes on a real 16-slide deck) — translate the JSON, not the document. Read `scripts/ooxml.py` only if
it errors.

## Rules

**Target language:** default Vietnamese; the user may name another. Keep the original's length and the
field's professional terms; condense only if a summary was also asked for. A term with no settled
equivalent keeps the original in brackets on first use.

**A key left `""` or set to its own source text passes through untranslated** — that is how a mã hiệu
stays a mã hiệu. Neither is reported as missing. Do not delete keys.

**One entry per unique string**, so the same source text translates the same everywhere. A word that
must read differently in two places has to be edited in the output afterwards — say so.

**Output name:** `[tên gốc]_[mã ngôn ngữ đích].[ext]` — `_VI`, `_EN`, … by the **target** language,
because a `_VI` on an English translation mislabels it (TEST-PLAN #15). The script takes the name from
`-o` and refuses only an output equal to its input.

**Report `WARNING … matched nothing`** if `apply` prints it: the source changed between the two
commands and those strings are missing from the output.

## What this cannot do — say so

- **Formatting that varies inside a paragraph is lost.** A paragraph split across nodes
  (`"Điện 1 "` + `"pha"`) is translated whole into its first node; a mid-sentence bold word comes back
  unbolded. Translating fragments produces nonsense — deliberate trade.
- **PowerPoint text can overflow** (Vietnamese runs 20–30% longer than English); fonts and shapes are
  not resized. List the slides with long strings.
- **Excel: only `sharedStrings.xml` is touched.** Formulas, named ranges, sheet names and number
  formats are out of scope by construction — renaming a sheet breaks its formulas.
- **PDF is not supported.** Content can go into a chat reply; the layout cannot be reproduced.
- **SmartArt** (`ppt/diagrams/`) is covered but not verified on a real deck — check the output.

## Before replying

Run `python scripts/test_ooxml.py <any .docx/.xlsx/.pptx>` whenever the script changed. Then report:
file written, strings translated, what passed through untranslated and why, and the slides/sheets to
eyeball.
