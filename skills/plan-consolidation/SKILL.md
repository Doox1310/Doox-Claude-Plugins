---
name: plan-consolidation
description: Use when the user hands over several kế hoạch spreadsheets built to different structures and asks to quy hoạch chúng về một form chung, or to gộp kế hoạch của nhiều phòng ban vào một file tổng hợp. Load `using-doox` first.
---

# Plan Consolidation

**Load `using-doox` first** — it routes the request, settles who is running this, and holds the plan-file rules this skill relies on.

## Hard limits

1. **Only a verified `Project Manager`**, on files whose `Tên PM` matches their name (gate below).
2. **Never write to a source file.** Output is new files; `project-update` alone writes the originals.
3. **Never chain the two commands** — `gộp` does not run after `quy hoạch` unasked.
4. **The form is confirmed before any file is written** (step 5).
5. **Never invent data**: a form column with no source is written empty (`null`), never filled, never
   dropped; rows sharing a `Danh mục CV` are never merged; duplicate conflicts go to the user.
6. **The output name must not split into three parts on ` - `** — anything that does is read as a plan
   file and pulled into the reminder. `Ke hoach tong hop [dự án] dd_mm_yyyy.xlsx` is safe.
7. **No row passes through the model** — never read a whole sheet into the reply.

| Lệnh | Vào | Ra |
|---|---|---|
| `quy hoạch` | N file khác cấu trúc | N file cùng một form chung |
| `gộp` | N file **đã cùng form** | 1 file tổng hợp, thêm cột `Phòng ban` |

`gộp` adds a column, so chaining it would hand the user a shape they never approved. Finish
`quy hoạch`, print the form, stop.

## Identity gate

Settle identity per `using-doox`, "Who is running this". A `Chuyên gia` is refused — consolidating
is how every row of every market would leave the role filter. The refusal says exactly this and
nothing more, in the user's language (`using-doox`, "Language"):

```
Quy hoạch và gộp kế hoạch chỉ chạy được với vai trò Project Manager. Vai trò hiện tại
của bạn là Chuyên gia nên mình không thực hiện được yêu cầu này.
```

No PM name, no file list, no row count, no filtered version instead — a refusal that shows the shape
of the data has already leaked part of it.

Exception: input files whose names do **not** split into three parts on ` - ` carry no PM to check —
run them without the gate, as ordinary documents.

## The script does the rows

```bash
python scripts/sheets.py scan      <file.xlsx>...
python scripts/sheets.py normalize <file.xlsx> mapping.json -o "<out>.xlsx"
python scripts/sheets.py merge     <normalized>... -o "<out>.xlsx" --key "Danh mục CV"
python scripts/sheets.py selftest
```

`scan` prints each sheet's header and two sample rows — enough to decide a mapping. Its header-row
guess can lose to a letterhead: if the `HEAD` line holds `CÔNG TY …` / `CỘNG HOÀ …`, set `header_row`
in the mapping.

## Deriving the form (`quy hoạch`)

No fixed template: the form comes from the files and must come out the same next run, or normalised
files stop matching.

1. **Group sheets by role** (chi tiết công việc, kiểm soát tiến độ, tổng quan), not by name. A sheet
   in one file only is kept as optional; an unclear role is asked about.
2. **Group columns within each role**, first match wins:
   - identical after normalising (bỏ dấu, lowercase, bỏ dấu câu và khoảng trắng thừa);
   - known synonyms (default list, open — an obvious pair belongs here, not in a question to the user):
     - `Danh mục CV` = `Nội dung công việc` = `Đầu việc` = `Hạng mục công việc`
     - `Người phụ trách` = `PIC` = `Người TH` = `Chủ trì`
     - `Ngày bắt đầu` = `Start` = `Ngày BĐ`
     - `Ngày kết thúc` = `Hạn hoàn thành` = `Deadline` = `Ngày KT`
     - `Trạng thái` = `Tình trạng` = `Tình trang` = `Status`
     - `Vấn đề phát sinh` = `Vướng mắc` = `Issue`
     - `Phương án giải quyết` = `Hướng xử lý` = `Phương án xử lý`
     - `Cập nhật hiện trạng` = `Hiện trạng` = `Tình hình hiện tại`
   - by the column's **values** (mostly dates, three repeating labels) — proposes only; the user
     confirms.
3. **Name each column by the variant used most across sources**, never a new name — the user must
   recognise their column. Two files make every merge a tie; default tie-break: first in the synonym
   group, then the variant also used in the workbook's other sheets, then the unabbreviated form.
   State the pick in the `Gộp:` line — a silent tie-break is the column nobody checks.
4. **Order** (default): columns in ≥50% of files, then the rest — kept, never dropped — then the three
   provenance columns the script appends.
5. **Print the form and stop** — normalising first and asking after is the work done twice:

   ```
   Form đề xuất (từ 5 file):
   Sheet:   Chi tiết CV (5/5) · Kiểm soát tiến độ (3/5, tùy chọn)
   Cột lõi: Danh mục CV (5/5) | Người phụ trách (5/5) | Ngày kết thúc (4/5)
   Bổ sung: Rủi ro (2/5) | Ghi chú nội bộ (1/5)
   Gộp:     "PIC" (B, C) + "Người TH" (A) → "Người phụ trách"
   Chưa xếp: cột "Ghi chú 2" ở file D — nội dung không nhận dạng được
   ```
6. **Record the form in sheet `00 - Form`** of every output file, so the next run reuses it.

## Output rules

- Row position is the identity (a label repeats — four labels cover fourteen rows on the reference
  file); the provenance columns preserve it.
- Values are copied, not formulas; the output is derived and read-only — say so. Formulas with no
  cached result (a Google Sheets export) become `Chưa có giá trị (công thức chưa tính)`; pass on the
  count `normalize` prints — missing, not zero.
- `--key` must name a real column; `merge` stops otherwise, because an all-clear on a key never
  checked is worse than no check.

## Merging (`gộp`)

`--key` lists rows whose key appears under more than one department; the script resolves nothing.
Take each group to the user: same task twice → giữ cả hai / gộp / bỏ một; same task with different
deadline, PIC or status → both values with both sources, their call, never the more plausible side.

The output opens with a `00 - Đọc trước` sheet stating it is generated and read-only; a refreshed
total is a re-run, not an edit.

## Before replying

- rows out = rows in, per file — print the comparison;
- every source column is in the form, the optional tier, or `Chưa xếp`;
- the form was confirmed before any file was written;
- every duplicate group reported, none silently merged;
- source files unchanged.
