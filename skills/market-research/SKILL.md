---
name: market-research
description: Use when a user asks to evaluate or research an electric-taxi market, country, city or region — đánh giá thị trường, nghiên cứu thị trường/khu vực, market report, market screening, entry or expansion (e.g. Côte d'Ivoire / Bờ Biển Ngà, Philippines, Kenya), taxi and ride-hailing licensing and legal requirements, fleet and vehicle sourcing, depot and fleet charging, cost/TCO, étude de marché — or to complete the saved taxi market-report workbook, or asks a single sourced question about such a market. Hands off to `contractor-search` for a contractor/partner list and to `competitor-research` for a comparison against competitors.
---

# Market Research — đánh giá thị trường/khu vực

**Load `research-method` first** (`../research-method/SKILL.md`, beside this skill's Base
directory). It carries the file-on-disk contract, language rules, claims and statuses (§4), source
classes (§5), freshness (§8), search engine, budget and dispatch (§9), ledger and cache (§10),
normalisation (§11), audit (§13) and reply counts (§14). This skill carries only what is its own:
scope (§2), the workbook (§3) and progressive fill (§12). `§` numbers are shared across the research
skills; see the map in `research-method`.

## 1. What it produces

A **sourced electric-taxi market report in the saved `.xlsx` framework**, or — for a question that
does not need the whole workbook — an RX answer in its own `.docx`. The customer runs its own EV taxi
fleet (owns the cars, employs the drivers, runs app and dispatch, charges at its own depots), so the
report asks what that operator needs to enter or expand in a market, not what a charging business
would need.

Permanent files of this skill:

- `assets/khung-bao-cao-thi-truong.xlsx` — output schema and cell-level requirements.

Everything else it uses lives in `research-method` (`<RM>` below = the absolute path of that
directory): `<RM>/scripts/wb.py`, `<RM>/scripts/cache.py`, `<RM>/assets/form-research.md`,
`<RM>/references/topic-lenses.md`, `<RM>/references/metrics.md`,
`<RM>/references/dispatch.md`, `<RM>/references/final-audit.md`.

### When another skill takes over

- **Tìm nhà thầu / đối tác** (a full list, a named firm, a shortlist) → `contractor-search`. It writes
  `Bảng 3B` of this same workbook; this skill's `Bảng 3` rows only summarise it.
- **So sánh mình với đối thủ** → `competitor-research`, RX2 `.docx`. `Bảng 3` has no competitor row;
  the competitive landscape does not go into the workbook.
- A request naming two or three of these runs **one** run: one scope call, one split, one ledger, one
  cache sweep, one audit (`research-method` §1). Load each skill named; none runs as a lighter version
  of itself.

## 2. Scope and mode

Use facts already supplied; do not ask again. Resolve only what materially changes the research:

- market/jurisdiction and geographic scope (country, city, metro area);
- objective(s): **market screening**, **entry/expansion**, **legal/licensing** (taxi, platform,
  driver, vehicle), **fleet & vehicle sourcing**, **depot & fleet charging**, **cost/TCO & unit
  economics** — plus contractor/partner (→ `contractor-search`) and competitor (→ `competitor-research`);
- report data-lock date;
- relevant project facts already known: planned fleet size and vehicle model, service model (street
  taxi, app, airport, corporate), launch phase, depot plans and candidate depot sites;
- when the objective includes contractor selection: the target profile — `contractor-search` §6.1;
- when the objective includes a competitor comparison: the own-side profile — `competitor-research` §7.1.

**Settle the deliverable at the same time as the objective, and read `<RM>/assets/form-research.md`
once it is settled.** A full market evaluation fills the workbook (§3, §12). A single question, an
entry thesis or a change against a dated baseline takes one RX form instead — **RX1** for a question
or a landscape, **RX4** for an entry/expansion or scenario thesis, **RX5** for what changed since a
dated report — written to its own `.docx` per `research-method` §1, at that form's `default_length`.
Choose by the result the user needs, not by topic; the lens rows name the likely form in their
`form_ids` column.

Ask for a missing essential in one structured-question call covering everything still unknown —
never as a numbered list of questions in prose, and never one question per turn.

Default to the latest public data available as of the report date. Mode is `nhanh` unless the user
explicitly asks for `sâu` — no objective escalates the mode on its own. What the objective does
instead is decide **which claims are decision-grade** (`research-method` §4), and depth is bought for
those claims out of a separate allowance (§9). A licensing run therefore pays for depth on taxi,
platform and driver authorisation without also paying for it on climate normals and payment methods;
a depot run pays for it on interconnection, land use and permit cost.

If a requested city/depot conclusion has only national evidence, keep the local claim
`Chưa xác minh`; never scale or infer it silently.

## 3. Read the framework first

Before researching, inspect the actual workbook being used. If the user supplies a framework, it wins
over the bundled asset. Otherwise copy `assets/khung-bao-cao-thi-truong.xlsx` (in this skill's
directory) to the output path and never edit the asset.

Treat the workbook as the **output contract**:

- `00 - Hướng dẫn` defines status, evidence, date, estimate, gap, and conclusion rules and remains
  unchanged.
- Default output name: `Báo cáo thị trường [Thị trường] dd_mm_yyyy.xlsx`, unless the user/project
  specifies another naming convention. Whatever the name, it must not split into three parts on
  ` - `: `using-doox` reads any such spreadsheet as a project plan file and pulls the report into the
  daily reminder.
- The report sheet defines what each row/column requires and its quality standard. On the bundled
  asset it is named **`Khung báo cáo thị trường mẫu`** — that exact string is what `--sheet` takes;
  the other two sheets are `00 - Hướng dẫn` and `Bảng 3B - Danh sách nhà thầu`. A user-supplied
  framework names its sheets differently: list them before guessing, never pass a name from here.
- Instruction text in writable report cells is placeholder text to replace, not content to preserve.
- Do not rely on remembered row numbers, merged ranges, or layouts; inspect them before writing.
  Write a merged range at its top-left anchor cell; writing any other cell of the range fails.
- Do not insert, delete, renumber, retitle, or reorder framework rows unless the workbook itself
  explicitly requires repeatable rows or the user asks.
- The contractor-list sheet (`Bảng 3B - Danh sách nhà thầu`) **is** a repeatable-row sheet, and it
  belongs to `contractor-search`; this skill does not write it.

Inspect and write with the bundled script, never with ad-hoc spreadsheet code. The report sheet
declares about 22,000 cells and fills under 300 of them; an unguarded row loop prints thousands of
empty rows and can cost more than the entire research run.

```bash
python "<RM>/scripts/wb.py" cells   <file.xlsx> --sheet "NAME"                     # which cells may be written
python "<RM>/scripts/wb.py" inspect <file.xlsx> [--sheet "NAME"] [--rows 17:27] [--max-chars N]
python "<RM>/scripts/wb.py" write   <file.xlsx> cells.json    # {"sheet": {"B7": "value", "C7": ["• line", "• line"]}}
```

### Which cells may be written

**Run `cells` before the split and treat its output as the definitive list.** Do not decide
writability by eye — the framework mixes output cells, fixed labels, block titles and column headers
in the same columns, and getting it wrong either destroys the table structure or leaves the report
half empty.

The rule it applies, for reading its output:

- **Column A is never written.** It holds the fixed row label or the block title.
- **A block-title row is never written** — column A in capitals — and neither is the
  **column-header row directly beneath it**. On the bundled asset those are rows 1, 17, 28, 38, 49,
  53 and rows 2, 18, 29, 39. Note that a title row may itself carry framework metadata further along:
  `B49` and `B53` state the required field list for the conclusion block beneath them, and
  overwriting either destroys that block's output contract.
- **Every other non-empty cell in columns B onward is an output cell**, and its text is a placeholder
  describing what must replace it — including the `Tiêu chuẩn chất lượng và kiểm chứng` column, which
  asks for the verification content of that row, not for the standard to be preserved.
- **An empty cell in columns B onward was never required** and stays empty.

On the bundled asset this comes to **158 writable cells**; the count differs for a user-supplied
framework, which is why it is computed rather than remembered. That set is the coverage denominator
for §13 gate A.

The bundled report sheet's blocks, for orientation only (the `cells` output is what counts):
Bảng 1 thị trường rows 3–16, one row per topic with its lens — R01 quy mô & cấu trúc, R02/R03 nhu cầu
& điểm cầu, R04 vĩ mô & vận hành địa phương, R07 giá cước, R08 tài xế, R10 nguồn xe, R11/R21 sạc cho
đội xe, R20 điện & đấu nối depot, R19 depot & mặt bằng, R25 bảo dưỡng, R27 thanh toán & dữ liệu, R12
TCO, R32 chất lượng & an toàn, then the Bảng 1 conclusion; Bảng 2 pháp lý rows 19–27 (R14, R15, R16,
R17, R22 and labour, data/payment); Bảng 3 đối tác rows 30–37 (row 30 summarises `Bảng 3B`; the
others are RX3-style counterparty rows on R10, R18, R25, R45, R49, R51, R08); Bảng 4 rủi ro rows
40–48; Kết luận pháp lý rows 50–52; Kết luận phân tích cuối cùng rows 54–60. Read the lens row of each
topic while splitting (`research-method` §4).

Inspection happens in exactly two phases, and never anywhere else in the run:

1. **Once, at claim-split time:** inspect the **report sheet in full** — `--sheet` with no `--rows`.
   `research-method` §4 splits every writable row into claims in this same pass, which a single block
   cannot support. That one dump also prints the sheet's merged ranges, which is the layout
   information every later `write` needs. Do not inspect the other sheets: `00 - Hướng dẫn` is a
   rules sheet you already follow, and `Bảng 3B` is `contractor-search`'s.
2. **Again only when the layout has actually moved under you** — on a sheet phase 1 did not cover.
   Then `--sheet` plus `--rows` over the affected rows only.

Do **not** re-inspect target rows before an ordinary `write`. Nothing between phase 1 and the write
can have changed them: this skill is forbidden from inserting, deleting or reordering framework rows,
so phase 1's merged map is still correct, and a confirmation dump per write cluster is a tool
round-trip that buys nothing. Never inspect a sheet you are not about to write, and never re-read a
block already written. Repeated placeholder text is printed once and echoed as `<same as C19>`; a cell
showing that marker carries the requirement written at the referenced coordinate.

`write` validates the whole batch first: an unknown sheet or a non-anchor merged cell fails the batch
and writes nothing, so a rejection costs one error line instead of a corrupted file. Batch each report
block into a single `write` call.

A cell value may be a **JSON list**, which is joined with newlines. `write` forces `wrap_text` on and
releases the framework's pinned row height so the reader's spreadsheet auto-fits the wrapped text.
Prefer the list form for every prose cell — see §12 for the required line shape.

## 12. Fill the workbook progressively

Write each completed report block as soon as its claims are resolved; write conclusion blocks last.
Preserve the workbook's style, merges, headers and `00 - Hướng dẫn`.

One authority batch (`research-method` §4) usually closes claims spread across several blocks, so
blocks finish in clusters rather than in order. Write every block that finished in the same cluster
in **one** `write` call, and never split a single block across two calls — a half-written block
cannot be audited, and the second call pays for the whole context again to finish what the first one
started.

For each result, follow the exact output shape required by the framework. Include exact
URLs/documents, not generic homepages when a specific page/order/table exists.

### Cell layout: the framework's field list, one field per line

**The required fields are set by the workbook, not by this file.** Three specs are in force, and the
applicable one wins:

| Where | Required fields |
|---|---|
| `00 - Hướng dẫn` A20 — every ordinary result | `Kết quả \| Trạng thái \| Phạm vi/đơn vị/kỳ dữ liệu \| Nguồn và ngày \| Phương pháp/giả định (nếu có) \| Giới hạn \| Hành động xác minh` |
| `B49` — the legal-conclusion block | `kết luận \| trạng thái \| nguồn và ngày \| giới hạn \| hành động xác minh` |
| `B53` — the final-analysis block | `kết luận \| trạng thái \| nguồn và ngày \| giới hạn \| bước tiếp theo` |

Read the applicable spec off the workbook during the §3 inspect; a user-supplied framework may state
a different one. Dropping `Giới hạn` or the closing action is a coverage failure, not a stylistic
choice — they are what makes the report reviewable.

A report cell is read on screen inside a fixed column, so a wall of prose is unusable no matter how
correct it is. Write every prose cell as a **JSON list of short lines** (§3) and let `write` join
them:

- lead with the content lines: one claim, figure or procedural step per line, never two facts joined
  by `và`/`;`, and keep the placeholder's own `•` prefix where it uses one;
- put the status word (`Đã xác minh` / `Ước tính` / `Chưa xác minh` / `Không áp dụng`) at the end of
  the content line it qualifies, not once at the end of the cell;
- then one line per remaining field, each opening with the field's own name — `Phạm vi/đơn vị/kỳ:`,
  `Nguồn và ngày:`, `Phương pháp/giả định:`, `Giới hạn:`, `Hành động xác minh:` — so a reviewer can
  find a field without reading the cell;
- one source per `Nguồn và ngày:` line, as `<publisher>, <date> — <URL>`.

A single short value (a date, a fee, a name, one status word) stays a plain string; the list form is
for anything carrying a full field list.

Rules:

- A required field with no adequate evidence says `Chưa xác minh` and identifies the missing data,
  confirming body and effect of the gap.
- Estimates show formula, inputs, assumptions and limits.
- Do not invent current licences or permits, taxi quotas, fare levels, vehicle availability or
  delivery times, driver pay, project references, costs, permit times, depot power capacity, local
  network quality, site hazards or commercial terms.
- Company self-publication must be labelled as such when it matters to reliability.
- Conclusion rows may use only evidence already populated above. They introduce no new factual claims
  and cannot carry a stronger status than the weakest material premise they depend on.
- Never conclude that a market is ready for launch, or a specific depot ready to build, without
  confirmed transport licensing, vehicle supply, land/right-of-use, electrical capacity and
  interconnection, and cost.

### Audit each block while writing it

Most of the audit belongs here, not at the end: the block and its evidence are already in context, so
checking them now is nearly free, whereas re-reading the finished workbook later reloads everything at
the point where context is largest. Before moving to the next block, confirm within the block just
written:

- every factual assertion — including non-numeric legal, licence, operator, vendor and causal
  statements — traces to the runtime ledger, or is explicitly labelled analysis/estimate/gap;
- every numeric token (integer, decimal, percentage, currency amount, date, range, fare, kW/kWh value,
  count, rate, CAGR, duration) is sourced evidence, a reproducible calculation, or structural
  metadata/label — anything else is verified, relabelled `Chưa xác minh`, or removed;
- components = reported total; percentages use the stated denominator and stay in plausible bounds;
  min ≤ max; FX, CAGR, totals and subtotals reproduce; units and tax basis match the wording;
- dates/effective periods match the claim, and national/regional data is not presented as city/depot
  data;
- source wording and report metric mean the same thing (`research-method` §8 non-synonyms);
- no instruction placeholder is left behind.

Example: if a registry gives `1.200 + 3.400 = 4.600` licensed taxis by class but a press release
states an active fleet of `5.100`, preserve the discrepancy and verify the underlying definitions and
dates — licensed and active are different populations; never force the components to fit the total.
Any mismatch is reported as a conflict; never average it away.

## 13–14. Audit and reply

Run `research-method` §13 and §14 as written. For a combined run, also add the lines
`contractor-search` and `competitor-research` require in their own replies.
