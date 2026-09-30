# The market workbook — §3 read the framework, §12 fill it

Read when the deliverable is the workbook: a full market evaluation, or a contractor list (which
lives in its `Bảng 3B`). An RX-only run does not need this file.

## 3. Read the framework first

A framework the user supplies wins over the bundled one. Otherwise copy
`assets/khung-bao-cao-thi-truong.xlsx` to the output path and leave the asset untouched. If a file of
that name already exists and is not this run's own copy or a resume the user asked for, add ` (2)`,
` (3)`… rather than write into it.

- **Output name**: `Báo cáo thị trường [Thị trường] dd_mm_yyyy.xlsx` unless the user or project uses
  another convention. Whatever the name, it must not split into three parts on ` - ` — `using-doox`
  would read it as a project plan file and pull it into the daily reminder.
- **Sheets of the bundled asset**: `Khung báo cáo thị trường mẫu` (the report sheet — this exact
  string is what `--sheet` takes), `00 - Hướng dẫn` (status, evidence, date, estimate, gap and
  conclusion rules; follow it, never change it) and `Bảng 3B - Danh sách nhà thầu` (the contractor
  list, §6). A user-supplied framework names its sheets differently — list them, never guess a name
  from here.
- Instruction text in a writable cell is a placeholder to replace, not content to keep.
- Rows are never inserted, deleted, renumbered, retitled or reordered unless the workbook itself
  marks them repeatable (`Bảng 3B` does) or the user asks.
- A merged range is written at its top-left anchor cell.

Use the bundled script rather than ad-hoc spreadsheet code — the report sheet declares about 22,000
cells and fills under 300, so an unguarded row loop can print thousands of empty rows and cost more
than the research:

```bash
python "<skill dir>/scripts/wb.py" cells   <file.xlsx> --sheet "NAME"                     # writable cells
python "<skill dir>/scripts/wb.py" inspect <file.xlsx> [--sheet "NAME"] [--rows 17:27] [--max-chars N]
python "<skill dir>/scripts/wb.py" write   <file.xlsx> cells.json    # {"sheet": {"B7": "value", "C7": ["• line", "• line"]}}
```

### Which cells may be written

`cells` computes the writable set — trust it over reading the sheet by eye, because the framework
mixes output cells, fixed labels, block titles and headers in the same columns. The rule it applies:

- column A (fixed row label or block title) is never written;
- a block-title row (column A in capitals) and the column-header row beneath it are never written —
  on the bundled asset rows 1, 17, 28, 38, 49, 53 and 2, 18, 29, 39. `B49` and `B53` hold the field
  list of the conclusion block beneath them and must survive;
- every other non-empty cell from column B on is an output cell whose text describes what replaces it
  — including `Tiêu chuẩn chất lượng và kiểm chứng`, which asks for that row's verification content;
- an empty cell was never required and stays empty.

The bundled asset has **158 writable cells**; a user framework differs, which is why the set is
computed. It is the coverage denominator of audit gate A.

Orientation only (the `cells` output is what counts): Bảng 1 thị trường rows 3–16, one topic per row
with its lens — R01 quy mô & cấu trúc, R02/R03 nhu cầu & điểm cầu, R04 vĩ mô & vận hành địa phương,
R07 giá cước, R08 tài xế, R10 nguồn xe, R11/R21 sạc cho đội xe, R20 điện & đấu nối depot, R19 depot &
mặt bằng, R25 bảo dưỡng, R27 thanh toán & dữ liệu, R12 TCO, R32 chất lượng & an toàn, then the Bảng 1
conclusion; Bảng 2 pháp lý rows 19–27 (R14, R15, R16, R17, R22, labour, data/payment); Bảng 3 đối tác
rows 30–37 (row 30 summarises `Bảng 3B`; the rest are RX3-style counterparty rows on R10, R18, R25,
R45, R49, R51, R08); Bảng 4 rủi ro rows 40–48; Kết luận pháp lý rows 50–52; Kết luận phân tích cuối
cùng rows 54–60. The competitor landscape has no block — it goes to its RX2 `.docx`.

### Inspecting

Inspect the report sheet in full once, at claim-split time: that one dump gives the placeholders the
split needs and the merged ranges every later `write` needs. After that, inspect again only what has
actually changed shape (rows inserted into `Bảng 3B`, a sheet not yet seen), with `--rows` over the
affected rows. Nothing else can move the layout, so a confirmation dump before each write just costs
context. Repeated placeholder text is printed once and echoed as `<same as C19>`.

`write` validates the whole batch first — an unknown sheet or a non-anchor merged cell fails the
batch and writes nothing. A value may be a JSON list, joined with newlines; `write` turns on
`wrap_text` and releases the pinned row height so the text auto-fits.

## 12. Fill the workbook progressively

Write each block as soon as its claims are resolved; conclusion blocks last. Keep the workbook's
styles, merges, headers and `00 - Hướng dẫn`. One authority batch often closes claims across several
blocks, so blocks finish in clusters — write a finished cluster in one `write` call, and keep a
block within one call so it can be audited whole.

Cite exact URLs or documents, not a homepage, when a specific page, order or table exists.

### Cell layout: the framework's field list, one field per line

The workbook sets the required fields; the applicable spec wins:

| Where | Required fields |
|---|---|
| `00 - Hướng dẫn` A20 — every ordinary result | `Kết quả \| Trạng thái \| Phạm vi/đơn vị/kỳ dữ liệu \| Nguồn và ngày \| Phương pháp/giả định (nếu có) \| Giới hạn \| Hành động xác minh` |
| `B49` — legal-conclusion block | `kết luận \| trạng thái \| nguồn và ngày \| giới hạn \| hành động xác minh` |
| `B53` — final-analysis block | `kết luận \| trạng thái \| nguồn và ngày \| giới hạn \| bước tiếp theo` |

A user framework may state a different spec — read it off the workbook. `Giới hạn` and the closing
action are what make the report reviewable; dropping them is a coverage failure.

A cell is read on screen in a fixed column, so write prose cells as a **JSON list of short lines**:
content first, one claim, figure or step per line, keeping the placeholder's `•` where it uses one;
the status word at the end of the line it qualifies; then one line per remaining field, each opening
with the field name (`Phạm vi/đơn vị/kỳ:`, `Nguồn và ngày:`, `Phương pháp/giả định:`, `Giới hạn:`,
`Hành động xác minh:`); one source per `Nguồn và ngày:` line as `<publisher>, <date> — <URL>`. A
single short value (a date, a fee, a name) stays a plain string.

Rules:

- A required field with no adequate evidence says `Chưa xác minh` and names the missing data, who can
  confirm it and what the gap affects.
- Estimates show formula, inputs, assumptions and limits.
- Company self-publication is labelled as such where it matters to reliability.
- Conclusion rows use only evidence populated above and never carry a stronger status than their
  weakest material premise.

### Audit each block as you write it

The block and its evidence are in context now, so checking here is nearly free; re-reading the
finished workbook later is not. Before moving on, confirm within the block:

- every factual assertion — legal, licence, operator, vendor and causal statements included — traces
  to the ledger or is labelled estimate, analysis or gap;
- every numeric token is sourced, a reproducible calculation, or a structural label;
- components add up to the stated total, percentages use the stated denominator, min ≤ max, FX, CAGR
  and subtotals reproduce, units and tax basis match the wording;
- dates and effective periods fit the claim, and national data is not presented as city/depot data;
- source wording and report metric mean the same thing (§8);
- no placeholder is left behind.

Example: a registry gives `1.200 + 3.400 = 4.600` licensed taxis by class and a press release states
an active fleet of `5.100`. Keep both and check definitions and dates — licensed and active are
different populations. Report the mismatch as a conflict; never force the components to fit.
