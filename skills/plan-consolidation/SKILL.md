---
name: plan-consolidation
description: Use when the user hands over several kế hoạch spreadsheets built to different structures and asks to quy hoạch chúng về một form chung, or to gộp kế hoạch của nhiều phòng ban vào một file tổng hợp.
---

# Plan Consolidation

Two commands, run separately. **Never chain them.**

| Lệnh | Vào | Ra |
|---|---|---|
| `quy hoạch` | N file khác cấu trúc | N file cùng một form chung |
| `gộp` | N file **đã cùng form** | 1 file tổng hợp, thêm cột `Phòng ban` |

`gộp` adds a column, so its output schema is not the form. Running it automatically
after `quy hoạch` hands the user a file they did not ask for, in a shape they did not
approve. Finish `quy hoạch`, print the form, stop.

## Identity gate — required

This skill reads whole plan files, which is exactly the row filter that `using-doox`
exists to enforce. Settle identity first, per `using-doox`, and **only a verified
`Project Manager` may run it**, on the files whose `Tên PM` matches their name. A
`Chuyên gia` is refused: consolidating is how every row of every market would leave
the filter.

Exception: input files that do **not** split into three parts on ` - ` carry no PM
name to check against. There is nothing to verify and nothing to leak a role past —
run them without the gate, as ordinary documents.

## The script does the rows

```bash
python scripts/sheets.py scan      <file.xlsx>...
python scripts/sheets.py normalize <file.xlsx> mapping.json -o "<out>.xlsx"
python scripts/sheets.py merge     <normalized>... -o "<out>.xlsx" --key "Danh mục CV"
python scripts/sheets.py selftest
```

`scan` prints each sheet's header row and two sample rows. That is enough to decide a
mapping; reading every row to decide it costs far more and decides nothing extra.
**Never read a whole sheet into the reply.** `normalize` and `merge` copy the rows
themselves, so no row passes through the model.

`scan` **guesses** the header row and the guess is sometimes wrong — a company
letterhead beats the real header on a form with a title block. Read the `HEAD` line:
if it holds `CÔNG TY …` or `CỘNG HOÀ …` instead of column names, set `header_row`
yourself in the mapping.

## Deriving the form (`quy hoạch`)

There is no fixed template. The form is derived from the files themselves, and it
must come out the same on the next run or the normalized files stop matching.

**1. Group sheets by role, not by name.** Every department names its sheets
differently. Group on the columns they carry — chi tiết công việc, kiểm soát tiến
độ, tổng quan. A sheet in only one file still belongs in the form, marked optional;
the other files leave it empty. A sheet whose role is unclear is asked about.

**2. Group columns within each role.** Three tiers, first match wins:

- identical after normalising (bỏ dấu, lowercase, bỏ dấu câu và khoảng trắng thừa);
- known synonyms — `PIC` = `Người phụ trách` = `Người TH` = `Chủ trì`; `Hạn hoàn thành` = `Ngày kết thúc` = `Deadline`;
- the column's **values**, not its name — mostly dates → a date column; three repeating labels → a status column. This tier only proposes; the user confirms.

**3. Name each column with the variant used most often across the sources.** Never
invent a new name: the user has to recognise their own column.

**4. Order.** Columns in ≥50% of files first, then the rest — **kept, never
dropped** — then the three provenance columns the script appends.

**5. Print the form and stop.** This is a gate.

```
Form đề xuất (từ 5 file):
Sheet:   Chi tiết CV (5/5) · Kiểm soát tiến độ (3/5, tùy chọn)
Cột lõi: Danh mục CV (5/5) | Người phụ trách (5/5) | Ngày kết thúc (4/5)
Bổ sung: Rủi ro (2/5) | Ghi chú nội bộ (1/5)
Gộp:     "PIC" (B, C) + "Người TH" (A) → "Người phụ trách"
Chưa xếp: cột "Ghi chú 2" ở file D — nội dung không nhận dạng được
```

Normalising five files and then asking is five files done twice.

**6. The form is recorded in sheet `00 - Form` of every output file**, so the next
run reuses it instead of deriving a different one.

## Rules

**Never touch a source file.** Output is new files. `project-update` still writes to
the originals.

**A form column with no source column is written empty**, mapped to `null`. Never
filled with a plausible value, never dropped.

**Do not merge rows that share a `Danh mục CV`.** The label repeats — on the
reference file four labels cover fourteen rows. Row position is the identity; the
provenance columns preserve it.

**Values are copied, not formulas.** The output is derived and read-only. Say so.
A workbook not written by Excel — a Google Sheets export — can carry formulas with no
cached result; those cells become `Chưa có giá trị (công thức chưa tính)` and
`normalize` prints how many. Pass that count on to the user: the number is missing
from the output, not zero.

**`--key` must name a real column.** `merge` stops if it does not, rather than
reporting no duplicates for a key it never looked at — an all-clear that was never
checked is worse than no check.

## Merging (`gộp`)

`--key` reports rows whose key value appears under more than one department. The
script **does not de-duplicate and does not resolve anything** — it lists the groups.
Take them to the user:

- same task in two departments → giữ cả hai / gộp / bỏ một, their call;
- same task, different deadline or PIC or status → print both values with both
  sources and let them settle it. Never pick the more plausible side.

The output opens with a `00 - Đọc trước` sheet stating it is generated and read-only.
Updates happen in the department files; a refreshed total is a re-run, not an edit.

**Name the output so it does not split into three parts on ` - `.** Anything that
does is read as a plan file by `using-doox` and pulled into the daily reminder.
`Ke hoach tong hop [dự án] dd_mm_yyyy.xlsx` is safe.

## Before replying

- rows out = rows in, per file — print the comparison;
- every source column appears in the form, in the optional tier, or in `Chưa xếp`;
- the form was confirmed before any file was written;
- every duplicate group was reported, none silently merged;
- source files unchanged.
