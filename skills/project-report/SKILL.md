---
name: project-report
description: Read ONE market's project plan and produce the progress report in the customer's template — every task sorted into overdue, near deadline, in progress, done. Use when the user asks for a báo cáo tiến độ, asks how one market's project is doing, asks what is overdue, or hands over a plan file and asks for the report. Also covers management reports that are not progress
  reports — báo cáo điều hành, đề xuất quyết định, kế hoạch triển khai, báo cáo rủi ro/escalation,
  biên bản họp và bảng hành động — written from memos, notes or tables using the GX1–GX5 forms in
  `assets/form-report.md`. NOT the day's to-do list or team reminder (that is `reminder`), NOT issue classification or a completion forecast (that is `project-insights`), NOT for changing a value in the file (that is `project-update`). Load the `using-doox` skill first — it holds the identity gate and the file-reading rules this skill depends on.
---

# Project report

## 1. When to use

The user hands over a plan file (`.xlsx`) and asks about progress, or asks for a progress report for
one market.

**Two branches, and the wrong one silently destroys the deliverable.**

| The ask | Branch | Where the rules are |
|---|---|---|
| Tiến độ / quá hạn / một thị trường đang thế nào, từ file kế hoạch | **Progress report** | Sections 2–6 below. Four fixed tables. |
| Báo cáo điều hành, đề xuất quyết định, kế hoạch triển khai, báo cáo rủi ro/escalation, biên bản họp + bảng hành động — từ memo, ghi chú, email, bảng rời hoặc đầu ra của một skill khác | **Management report** | `assets/form-report.md`, forms GX1–GX5. |

The progress branch is the default and it is rigid: the four tables are the customer's own template,
not a layout choice. Never render a progress report as a GX form, never add a GX block to it, and
never drop a table because a GX form has no equivalent.

The management branch exists for the material the four tables cannot hold — a decision that needs an
approver, a plan that needs owners and gates, a meeting that needs a decision register. Read
`assets/form-report.md`, pick one form by the outcome the reader needs, and follow that form's
`reasoning`, `missing_data` and `template_*` fields. Output is the chat reply, same as the progress
branch; produce no file.

An ask that could be either — a plan file handed over with "viết cho tôi báo cáo gửi sếp" — is
**asked about, not guessed**. One question, then run one branch.

## 2. Input — progress branch

Sections 2 to 6 are the progress branch only. The management branch has its own input, its own form
and its own output, all in §7.

**Load the `using-doox` skill before anything else in this section.** If this skill was dispatched on
its own, that has not happened yet — do it now, before listing the folder and before opening the
file. The identity gate lives there, and a report printed before the role is known cannot be
un-shown.

- Who is running this — `using-doox`, "Who is running this". If the README does not answer it, ask
  before reading the file. A `Project Manager` gets every row, but only of a file whose `Tên PM`
  matches their name — the claim is verified there, and a failed check stops the run without
  revealing the real PM name. A `Chuyên gia` gets only the rows carrying their PIC code, as
  `Người phụ trách` or `Người hỗ trợ`. Print the identity line above the report.
- The plan file — a spreadsheet, `.xlsx` or a native Google Sheet.
- The market, the project and the PM name. They come from the filename, which follows
  `[Thị trường] - [Tên dự án] - [Tên PM]`, extension optional — use the `using-doox` skill to read them, and show
  what was read before printing the report. If the filename does not follow the convention, that
  skill says to ask the user; do that rather than guessing, or the report goes out under the wrong
  market.

## 3. Fields to collect

Read the file per `using-doox`, section "Reading a plan file" — the two sheets, the join by row
position, the built STT, the required columns, the section-heading rows to drop, and which sheet each
field comes from all live there. Do not re-derive any of it here.

Thirteen fields end up in the report: STT, Danh mục công việc, PIC, Ngày bắt đầu, Ngày kết thúc,
Trạng thái (text), the completion checkbox, Hiện trạng vấn đề, Vấn đề phát sinh, Phương án xử lý,
Ghi chú, Phương án triển khai, Tiêu chuẩn hoàn thành. `Rủi ro` is read but not printed.

## 4. Classification

`using-doox` defines done — checkbox TRUE **and** text `Hoàn thành`; anything failing either
condition counts as not done.

Table 4 holds only `Hoàn thành`; tables 1, 2 and 3 hold only `Chưa triển khai` and
`Đang triển khai`.

Test in order, top to bottom. A task placed in an earlier table never reappears in a later one.

| # | Table | Condition | Date column |
|---|---|---|---|
| 1 | Đầu việc quá deadline | not done + Ngày kết thúc < today | Ngày kết thúc |
| 2 | Các đầu việc gần deadline | not done + today ≤ Ngày kết thúc ≤ today+3 | Ngày kết thúc |
| 3 | Các đầu việc đang trong quá trình triển khai | not done + Ngày bắt đầu ≤ today + not already in 1/2 | Ngày bắt đầu |
| 4 | Các công việc đã hoàn thành | checkbox TRUE **and** text `Hoàn thành` | Ngày kết thúc |
| — | Chưa bắt đầu | everything left: Ngày bắt đầu in the future, or no dates | no table |

**Status conflicts.** A task whose checkbox is TRUE while the text column is not `Hoàn thành`, or the
reverse, counts as not done and still lands in table 1/2/3 by its dates. Flag it twice:

- In its own row, append `[đã tick, cột chữ chưa cập nhật]` to whatever `Ghi chú` already holds.
- List it again after table 4: Danh mục công việc plus both status values, so the user can fix the
  file.

## 5. Output

**The report is the chat reply itself.** Produce no `.docx`, `.md`, `.pdf`, `.xlsx` or any other
file, and do not offer to. A file attachment is not a delivery of this report; it is a way of not
delivering it.

**Print every table in full, as Markdown, in the reply.** All four sections, every row of every
section, every column in the order given below, each cell carried whole. `Phương án triển khai` and
`Tiêu chuẩn hoàn thành` run to several hundred characters with numbered sub-steps — carry them
whole, only collapsing newlines inside a cell so the Markdown row stays valid. An empty cell prints
as `-`. An empty section still prints its header row plus `_(không có)_`.

A prose recap of the counts is not the report. `"Quá deadline: 4, Đang triển khai: 14"` states the
numbers correctly and still fails, because it drops `Hiện trạng vấn đề`, `Vấn đề phát sinh` and
`Phương án xử lý` — exactly the columns the PM acts on.

The report runs long on a real market: reading the file in slices and printing the tables in
consecutive messages marked `(tiếp)` is fine. Shortening is not. Never cut rows, never cut cells,
never replace a table with a sentence, never point at a file instead.

Opening lines, verbatim:

```
Báo cáo tiến độ dự án:
Cập nhật tiến độ dự án tại thị trường [Tên thị trường] dựa theo cập nhật mới nhất:
```

Then four sections, each heading written exactly like this — number, label, colon, row count in
brackets, then the table:

```
1. Đầu việc quá deadline: (4)
2. Các đầu việc gần deadline: (1)
3. Các đầu việc đang trong quá trình triển khai: (14)
4. Các công việc đã hoàn thành: (3)
```

Do not rename, reorder, merge or drop a section, and do not add one — no `Các công việc sắp tới`, no
`Chưa bắt đầu` table, no count-total line at the end. A `Chuyên gia` still gets all four sections,
filtered to their rows; a section left empty by the filter prints `_(không có)_` like any other.

### The same four sections in English and French

The Vietnamese above is **canonical** — it is the customer's template, and the four sections, their
order and their numbering never change. What changes with the reply's language (`using-doox`,
"Language") is the wording of the labels, and only to these:

| # | vi | en | fr |
|---|---|---|---|
| — | `Báo cáo tiến độ dự án:` | `Project progress report:` | `Rapport d'avancement du projet :` |
| — | `Cập nhật tiến độ dự án tại thị trường [X] dựa theo cập nhật mới nhất:` | `Progress at [X], as of the latest update:` | `Avancement sur le marché [X], selon la dernière mise à jour :` |
| 1 | `Đầu việc quá deadline` | `Overdue tasks` | `Tâches en retard` |
| 2 | `Các đầu việc gần deadline` | `Tasks near deadline` | `Tâches proches de l'échéance` |
| 3 | `Các đầu việc đang trong quá trình triển khai` | `Tasks in progress` | `Tâches en cours` |
| 4 | `Các công việc đã hoàn thành` | `Completed tasks` | `Tâches terminées` |

Empty section: `_(không có)_` / `_(none)_` / `_(aucune)_`. Continued message: `(tiếp)` / `(cont.)` /
`(suite)`. The status-conflict tag is the skill's own annotation, so it follows the reply's language:
`[đã tick, cột chữ chưa cập nhật]` / `[checkbox ticked, text column not updated]` /
`[case cochée, colonne texte non mise à jour]` — but the two conflicting values it reports are quoted
from the file exactly as written.

Column headers follow the same split: the eight/seven headers below are rendered in the reply's
language, while **every cell under them is quoted from the file untouched** — `Danh mục công việc`
values, PIC codes, `Trạng thái` words and note text stay exactly as the plan file wrote them, in the
plan file's language. Say so in one line above the report when the two languages differ.

Tables 1, 2, 3 — eight columns:

| STT | Danh mục công việc | PIC | Ngày kết thúc | Hiện trạng vấn đề | Vấn đề phát sinh | Phương án xử lý | Ghi chú |
|---|---|---|---|---|---|---|---|

Table 3 swaps `Ngày kết thúc` for `Ngày bắt đầu`. Every other column keeps its place.

Dates print as `dd/mm/yyyy`. One real row, to fix the level of detail expected:

```
| II.3.1 | Chuẩn bị hồ sơ & đầu mối nộp hồ sơ | Doox4 | 21/08/2026 | Đã nhận checklist bản mềm, chờ tư vấn xác nhận | - | - | - |
```

`Hiện trạng vấn đề`, `Vấn đề phát sinh`, `Phương án xử lý` and `Ghi chú` come from the control
sheet and are empty on most rows — print `-`, never leave the cell out and never invent content.

Table 4 — seven columns:

| STT | Danh mục công việc | PIC | Ngày kết thúc | Ghi chú | Phương án triển khai | Tiêu chuẩn hoàn thành |
|---|---|---|---|---|---|---|

`Phương án triển khai` and `Tiêu chuẩn hoàn thành` are the long ones — print them whole, they appear
only in table 4.

After table 4: the status-conflict list, if there is one.

## 6. Boundaries

**Quy tắc chung — `project-update` là skill duy nhất được ghi vào file kế hoạch.**

**Quy tắc riêng của skill này — `project-report` không ghi vào file kế hoạch.** A status conflict it
finds is listed, never corrected; the correction goes through `project-update`, with its
confirmation. The one file it writes is the project `README.md`, per `using-doox`.

Both rules hold on the management branch too. A GX report reads the plan file; it never edits it.

## 7. Management branch

For the material the four tables cannot hold. Read `assets/form-report.md` before writing anything —
it holds the selection table, the five forms and the twelve context rules, and a user who edited it
gets what they edited.

### 7.1 Input

Whatever the user supplied in this session: a memo, meeting notes, an email, a loose table, a plan
file, or the output of an earlier skill in the same conversation. Read it whole first.

The identity gate still applies, and for the same reason: run `using-doox` before reading a plan file
or printing anything. A `Chuyên gia` gets a report built only from rows carrying their PIC code,
exactly as on the progress branch.

**Extract, do not re-ask** — purpose, audience, scope, period or cutoff, deadline, format. Ask only
about a gap that changes the report.

Three rules decide what the report may say, and they are the reason this branch exists rather than
free-form writing:

- **A figure in the material is the figure.** Never replaced by model knowledge, never rounded into a
  nicer number, never carried across with a different unit or period than the source used.
- **Missing is named, not filled.** A critical input that is absent is written
  `[INPUT NEEDED: <field>]` and listed after the report. Missing is not zero, not "no issue", not
  approved and not complete.
- **States are kept apart.** Đã giao ≠ đã nghiệm thu ≠ đã đóng; đề xuất ≠ đã duyệt; baseline gốc ≠
  ngày điều chỉnh chưa được duyệt. Owner-complete does not establish reviewer acceptance, and an
  unapproved change is a proposal, not a new baseline.

### 7.2 Pick the form

One form, by the outcome the reader needs — not by cadence and not by topic:

| The reader needs | Form |
|---|---|
| kết quả hiện tại / tiến độ so với baseline | GX1 |
| một lựa chọn, một phê duyệt, một thay đổi baseline | GX2 |
| biến một mục tiêu thành kế hoạch triển khai hoặc khắc phục | GX3 |
| đánh giá rủi ro / sự cố và định phương án, hoặc escalate vượt thẩm quyền | GX4 |
| ghi nhận quyết định, giao việc, theo dõi cam kết đã có | GX5 |

A risk needing intervention takes GX4 first. Otherwise: GX2 → GX3 → GX5 → GX1. Then read the one
`90_Context_Rules` row matching the source report type — weekly, project status, escalation,
milestone, change proposal and so on. That row adds checks; it never selects a second form.

Material fitting no row uses the closest intent and states the assumption. A request that is really
two reports — a decision proposal and a meeting record — is asked about, not merged.

### 7.3 Output

The chat reply, in the shape the chosen form's `template_*` fields give: its title line, its
conclusion first, then its tables. `reasoning` is the order the argument is made in, `core_output` is
what must survive any shortening, `missing_data` is the gap that may not be hidden, and
`adaptive_blocks` are added only when the material actually triggers them.

Produce no file and do not offer to — same as the progress branch. Default length is one page, around
250–450 words, shorter for an alert or an action register, unless the user asked otherwise.

Written in the user's language (`using-doox`, "Language"), with every value quoted from the material
left in the material's own language. The GX `template_*` fields are English because they are the
frame, not the output language. Form IDs and field keys — `GX2`, `template_options` — are internal and
never printed.

Before returning, check the report against its own inputs: arithmetic and denominators reproduce,
periods and units match the wording, every `[INPUT NEEDED: …]` is still visible, and no
`{{placeholder}}` survived. Then say which form was used and list the gaps.

### 7.4 Boundaries

This branch writes a report from supplied internal facts. It does not go out and research an external
question — that is `market-research` — and it does not send anything. A report the user then wants
mailed goes to `mail-draft`, with the figures, the cutoff and the wording of any decision carried
across unchanged. Run only the stage that was asked for.
