---
name: project-update
description: Update tasks in the plan files — status, dates, issues, handling — from what the user typed, across several markets in one message, confirming every change before writing (a new copy of a non-standard file excepted) and keeping the two sheets in step. Use when the user says a task is done, pending, late, blocked, moved, or hands over any change to a plan file — and when the user hands over a checklist, tracker or report file (a CEO checklist, a weekly progress report) and asks to update it from a source such as meeting minutes, news or the master plan; those are written to a new dated copy, never in place. The only Doox skill that writes to a plan file. Load `using-doox` first.
---

# Project Update

**Load `using-doox` first** — it routes the request, settles who is running this, and holds the plan-file rules this skill relies on.

## Hard limits

1. **Identity and role first** (`using-doox`, "Who is running this"). Only rows the role may write
   (§2) are written; a refused row is named with its reason, never written anyway.
2. **Every write is confirmed in its own turn** (§6). A yes covers the table it answered, nothing
   after it. Sole exception: the new dated copy of a file outside the convention (§9).
3. **Write only the confirmed cells.** No tidying, filling, recomputing, sorting or fixing anything
   else.
4. **Keep the two sheets in step** (§4) — every sheet carrying the field, in the same write, or not
   at all.
5. **A shifted pair of sheets stops the run** — nothing written to any file in the batch (§7).
6. **A file outside the convention is never written in place** — new dated copy only (§9).
7. **A connector-only file is not written** — print the confirmed change-set and say so (§9).
8. **Never invent or guess**: not a row, a market, a field, a year, a value the sources do not state,
   nor a `Phương án xử lý`. Never write a fourth `Trạng thái` value (§5). Data is not translated unless
   the user asked for the output in a language (`using-doox`, "Hard limits" 6).

## 1. When to use

The user reports a change to existing tasks — finished, pending, slipped, deadline moved, issue
found, fix decided — one task or twenty, one market or several. Reading the plan is `project-report`
/ `reminder`; a report that "fixed" a cell it printed is a bug.

**A file outside the plan-file convention** (`CEO_Personal_Checklist_CIV_21092026_v2.xlsx`,
`Progress report CIV.xlsx`) is updated the same way, from what the user typed or from attached sources
(master plan, minutes, news). Read it per `using-doox`, "When a file does not match a convention";
write it to a new copy (§9). Each changed cell names its source in the §6 table (`kế hoạch gốc R42`,
`biên bản 22/09`). A value the sources do not state stays as it was; a source contradicting the file
is shown, not silently applied. New values use the file's own vocabulary (`Done` in an English file).
Write rights follow view rights: every row of the attached file, never a row from a source plan file
the role could not see.

### Syncing from a source

Defaults for the common customer asks — each exists because the opposite reading has cost a redo:

- **Scope is what the user named.** "Chỉ bổ sung notes" writes the note field and nothing else; other
  differences between source and target are listed after the table, not applied.
- **Notes are added, not replaced.** A source note is appended to the target's note with its tag
  (`[File điều chỉnh, 26/09]`) unless the target already says the same; replace only when asked.
  Re-running from the same source refreshes that source's own tagged segment instead of stacking a
  second copy beside it.
- **Matching rows across files**: by the shared ID/STT first, then by task text plus dates. Files in
  different languages match on ID only — no matching by meaning. A row that matches several or none
  is listed, never forced onto the closest one.
  Free text with no IDs (a mail, minutes) is matched to rows by meaning — that is the only way — so
  each change it causes names the sentence it came from in the §6 table, for the user to check.
- **A source may be another sheet of the same workbook** (`Level 3_suggestion`). "Còn gì chưa bổ sung"
  first lists what the source has that the target lacks. Where the missing items should go is asked,
  unless the user already said; the target files are then updated from the sheet as it stands. A
  master or source file is never written in place — only into a new copy, if the user wants it.
- **Several targets in one ask** each get their own new copy (§9); the §6 table groups by file.
- **List-only** — "chỉ ra các cập nhật để tôi tự điền vào kế hoạch gốc": print the change-set table
  (file to fill, row ID, task, field, current value in that file, new value, source) and write
  nothing; no yes needed.
- **Output language**: a note you compose (a summary of a mail or minutes) is your own text, not
  data — write it in the language the user asked for, or else in the target file's language (an
  English progress report gets English notes). Only a verbatim quotation keeps its original words.
  Status values use the target file's own vocabulary (`Done` in an English file); names, codes,
  numbers and dates never change.

## 2. Identity and permission — the gate

| Role | May write |
|---|---|
| `Project Manager` | every row of the files whose `Tên PM` matches their name |
| `Chuyên gia` | rows where their PIC code is `Người phụ trách` **or** `Người hỗ trợ` |

`Người hỗ trợ` counts as owner here — a supporter reporting their part done is the core case. A row
outside the set is refused in one line (`Doox3 không phụ trách công việc này`) and the rest of the
batch goes through; one refused row never rejects the batch.

## 3. Reading the request

Parse the free text into one intent per task **before touching anything**: market → file, task,
field(s), new value.

Default keyword map (extend by obvious meaning; a word whose field is unclear is asked about —
a wrong column is worse than one question):

| Keyword | Sets |
|---|---|
| `hoàn thành`, `xong`, `đã xong`, `done` | Trạng thái `Hoàn thành`, checkbox TRUE |
| `đang làm`, `đang triển khai` | `Đang triển khai`, checkbox FALSE |
| `chưa làm`, `chưa triển khai`, `chưa bắt đầu` | `Chưa triển khai`, checkbox FALSE |
| `pending`, `treo`, `tạm dừng`, `chờ …` | not a column value — §5 |
| `lùi deadline`, `dời hạn`, `gia hạn`, a date | Ngày kết thúc |
| `bắt đầu từ …` | Ngày bắt đầu |
| `vướng`, `chưa đủ`, `thiếu`, `bị …` | Vấn đề phát sinh |
| `đã xử lý bằng …`, `phương án là …` | Phương án xử lý |
| `hiện tại đang …` | Cập nhật hiện trạng |

### Finding the market

Users write `BBN`, `Bờ Biển Ngà`, `PLP`; files say `Bo Bien Nga`, `Philippines` ("Plan file naming").
Default matching: equal ignoring diacritics/case/spaces/dots/hyphens; else initials (`BBN`); else a
prefix of ≥3 characters. One file matched — take it and name it in the §6 table, so a wrong match is
caught before the write. None or several — ask with a picker.

### Finding the task

`Danh mục CV` repeats (4 labels cover 14 rows on the reference file), so **a label matching several
rows is never resolved by guessing**: show the candidates with built STT, dates and PIC, and ask. The
built STT ("Reading a plan file") identifies the row in every question and confirmation. Match on
labels containing the user's words, diacritics and case ignored; no match — say so, never fall back
to the closest-looking task.

## 4. What syncs with what

Both sheets carry `Ngày bắt đầu`, `Ngày kết thúc`, `Trạng thái`, `Ghi chú` ("Where each field comes
from"):

| Change | Cells written |
|---|---|
| Trạng thái `Hoàn thành` | detail text `Hoàn thành` **and** control checkbox TRUE |
| any other Trạng thái | text **and** checkbox FALSE |
| Ngày bắt đầu / Ngày kết thúc | both sheets, wherever the column exists |
| Ghi chú | the sheet the user meant; both carry a value — ask |

Half a status change is the bug this prevents: `reminder` reads the text, `project-report` the
checkbox, and they would disagree. Rows are joined by position after the STT alignment check
("Reading a plan file").

## 5. Values not in the file's vocabulary

`Trạng thái` holds only `Chưa triển khai`, `Đang triển khai`, `Hoàn thành`; one `pending` cell breaks
the done-check in every skill. Propose the nearest value plus the detail as text, confirmed in the §6
table:

```
"pending" không phải trạng thái có trong file. Bạn xác nhận cách ghi sau nhé:
  Trạng thái: Chưa triển khai
  Vấn đề phát sinh: chưa đủ hồ sơ
```

Default: `pending` / `treo` / `chờ …` → `Chưa triển khai`, reason in `Vấn đề phát sinh`, checkbox
FALSE; work genuinely under way but blocked is `Đang triển khai` — the user decides which.

Dates are written as real date values. `20/08` has no year — ask, do not assume the current one.

## 6. Confirm before writing

No exception for a one-cell change, a clearly worded request, `cứ làm đi`, or an earlier yes. Print
the whole change-set as one table, one line per cell (the checkbox is its own line), `-` for empty:

```
Xác nhận các thay đổi sau:

| Thị trường | STT | Danh mục CV | Trường | Giá trị hiện tại | Giá trị mới |
|---|---|---|---|---|---|
| Bo Bien Nga | II.3.1 | Phê duyệt ngân sách & nhà thầu | Trạng thái | Đang triển khai | Hoàn thành |
| Bo Bien Nga | II.3.1 | Phê duyệt ngân sách & nhà thầu | Checkbox | FALSE | TRUE |

Bạn xác nhận cập nhật các nội dung trên chứ?
```

Below it, whatever applies: rows refused (§2); rows already at the asked value (`không thay đổi`,
dropped); desync found (§7); fields still missing (§8). Then wait. A reply that changes something
("đúng rồi nhưng deadline là 21/08") is not a yes — rebuild and ask again.

**No row resolved at all** (a past failure: the skill had no output for this): print no table and ask
for no yes. Print what §3 produced — candidates per ambiguous intent, intents with no match — and one
line saying nothing was written (`Chưa ghi ô nào vào file — cả ba nội dung đều chưa xác định được
đúng một dòng.`). Never pick a row so the batch has something in it.

## 7. Desync already in the file

Before writing a row, compare what both sheets say about it. Report any existing disagreement and
ask; do not fix it as a side effect:

```
Lưu ý: công việc II.3.1 đang bất đồng bộ giữa 2 sheet —
  sheet chi tiết: Trạng thái = Hoàn thành
  sheet kiểm soát: checkbox = FALSE
Bạn muốn ghi thành Hoàn thành (checkbox TRUE) hay giữ nguyên?
```

The answer becomes rows in the §6 table; unanswered, it is left as is and reported next time.

A failed STT alignment check is worse: stop the whole run, name the first differing row index with
both values, write nothing — a write into a shifted join lands on the wrong task and looks fine.

## 8. Missing information

A change to a blocked state without a reason leaves `Vấn đề phát sinh` / `Phương án xử lý` empty. Ask
once, in one message, for everything missing across the batch. `chưa có phương án` is a valid answer,
written as said. No answer — the cell stays empty and the reply says which fields were left empty.

## 9. Writing

After the yes (or, for a non-convention copy, straight away), write exactly the confirmed cells.
Where the write lands follows `using-doox`, "Writing a plan file": a local or synced `.xlsx` in place,
cell by cell, formatting and formulas untouched; a connector-only file is not written — never upload a
"corrected" copy or create a second plan file.

**A file outside the convention → a new copy** `<tên file gốc>_ddmmyyyy.<đuôi>` in the local working
folder (run date; ` (2)`, ` (3)`… if taken): copy the original whole, write the confirmed cells into
the copy. The original is never modified; since nothing shared changes, the §6 table is shown and the
copy written in the same turn, and the user reviews the copy.

Then re-read the written cells and report what actually changed:

```
Đã cập nhật 4 ô trong 2 file:
  Bo Bien Nga - II.3.1 Phê duyệt ngân sách & nhà thầu: Trạng thái → Hoàn thành, checkbox → TRUE
```

A cell that failed is named as failed; no write is reported unverified.

## 10. Boundaries

Batches are per row. `Hoàn thành hết các việc của tôi` is expanded into the actual rows and
confirmed row by row — never a sweep, never a count instead of rows.
