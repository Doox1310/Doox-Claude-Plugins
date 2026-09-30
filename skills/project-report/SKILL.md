---
name: project-report
description: "Read ONE market's project plan — or any progress checklist/tracker the user hands over, e.g. a launch checklist — and produce the progress report in the customer's template, or in the layout the user names (an Excel with Summary + Details sheets, a bilingual Word) — every task sorted into overdue, near deadline, in progress, done. Use when the user asks for a báo cáo tiến độ, asks how one market's project is doing, asks what is overdue, or hands over a plan file and asks for the report. Also covers management reports that are not progress reports — báo cáo điều hành, đề xuất quyết định, kế hoạch triển khai, báo cáo rủi ro/escalation, biên bản họp và bảng hành động — written from memos, notes or tables using the GX1–GX5 forms in `assets/form-report.md`. NOT the day's to-do list or team reminder (that is `reminder`), NOT for changing a value in the file (that is `project-update`). Load `using-doox` first — it holds the identity gate and the file-reading rules this skill depends on."
---

# Project report

**Load `using-doox` first** — it routes the request, settles who is running this, and holds the plan-file rules this skill relies on.

## Hard limits

On top of `using-doox`, "Hard limits":

- **Identity gate before the file.** Nothing from the plan file — row, count, filename, PM name — is
  read out until `using-doox`, "Who is running this" is settled; then only the rows that role may see
  ("What each role sees" — for a `Chuyên gia`, rows where their code is `Người phụ trách` or
  `Người hỗ trợ`, together in the four tables), in the reply **and** in the saved file. A claimed `Project Manager` whose
  name does not match the file's `Tên PM` is stopped without the real PM name being shown. Both
  branches.
- **Read-only.** This skill never writes to a plan file (§6). A status conflict is listed, not fixed.
- **The four tables are the customer's template** (§5): opening lines, section headings, their order,
  numbering and the six columns are fixed. Never render a progress report as a GX form, never add a
  GX block to it, never add, merge, rename or drop a section. The one exception is a layout the user
  names (§5): its Details sheet adds a fifth group; the chat reply still keeps the four tables.
- **Done is exact** (§4): checkbox TRUE *and* text `Hoàn thành`, per `using-doox`, "Reading a plan file".
- **Print in full.** Every row, every cell, in the chat reply; the saved file is a copy, never a
  substitute. Never invent a cell, never translate a value.
- **Never overwrite** an existing file; a new name gets ` (2)`, ` (3)`…

## 1. When to use

| The ask | Branch | Rules |
|---|---|---|
| Tiến độ / quá hạn / một thị trường đang thế nào, từ file kế hoạch hoặc checklist/tracker | **Progress report** | §2–§6. Four fixed tables. |
| Báo cáo điều hành, đề xuất quyết định, kế hoạch triển khai, báo cáo rủi ro/escalation, biên bản họp + bảng hành động — từ memo, ghi chú, email, bảng rời hoặc đầu ra của skill khác | **Management report** | §7, forms GX1–GX5 in `assets/form-report.md`. |

The progress branch is the default. An ask that could be either — a plan file with "viết cho tôi báo
cáo gửi sếp" — is **asked about in one question, not guessed**: the wrong branch silently loses the
deliverable.

## 2. Input — progress branch

- **Identity** — `using-doox`, "Who is running this"; print the identity line above the report.
- **The file** — a plan file (`.xlsx` or native Google Sheet), or any checklist/tracker the user
  attached, read per `using-doox`, "When a file does not match a convention".
- **Market and project** — from the filename (`using-doox`, "Plan file naming"), shown per "Say what
  was read" before the report. Not readable from the name — ask the market once; a guess sends the
  report out under the wrong market.
- **Other sources handed over with it** (minutes, a mail, news) — their facts go into `Ghi chú` of
  the rows they concern, tagged with the source (`theo biên bản họp 22/09`). They never change a
  status or a date the file holds.

## 3. Fields to collect

Read per `using-doox`, "Reading a plan file" (join, built STT, required columns, heading rows, which
sheet each field comes from, the one column-mapping line per file).

Eight fields: STT, Danh mục công việc, PIC, Ngày bắt đầu, Ngày kết thúc, Trạng thái (text), the
checkbox (classification only, not printed), Ghi chú. The other columns are not part of the report.

## 4. Classification

Tables 1–3 hold only `Chưa triển khai` / `Đang triển khai`; table 4 only done tasks. Test top to
bottom; a task placed in an earlier table never reappears later.

| # | Table | Condition | Date column |
|---|---|---|---|
| 1 | Đầu việc quá deadline | not done + Ngày kết thúc < today | Ngày kết thúc |
| 2 | Các đầu việc gần deadline | not done + today ≤ Ngày kết thúc ≤ today+3 | Ngày kết thúc |
| 3 | Các đầu việc đang trong quá trình triển khai | not done + Ngày bắt đầu ≤ today + not in 1/2 | Ngày bắt đầu |
| 4 | Các công việc đã hoàn thành | checkbox TRUE **and** text `Hoàn thành` | Ngày kết thúc |
| — | Chưa bắt đầu | the rest: start in the future, or no dates | no table |

**Status conflict** — checkbox and text disagree: not done, placed in 1/2/3 by its dates, and flagged
twice so the user can fix the file: `[đã tick, cột chữ chưa cập nhật]` appended to its `Ghi chú`, and
listed after table 4 with Danh mục công việc and both status values quoted as written.

## 5. Output

**The chat reply is the report; the same content is also saved as a file** in the local working
folder: `Báo cáo tiến độ [Thị trường] dd_mm_yyyy.docx` (GX branch: `Báo cáo [tên form] [Thị trường]
dd_mm_yyyy.docx` — GX1 `Kết quả và tiến độ`, GX2 `Đề xuất quyết định`, GX3 `Kế hoạch triển khai`, GX4
`Rủi ro và xử lý`, GX5 `Quyết định và hành động`; `[Thị trường]` omitted when not about one market). A
name must never split into three parts on ` - `, or `using-doox` reads it as a plan file. A layout the
user named (an `.xlsx` with Summary + Details, bilingual cells, a colour rule) replaces the `.docx`,
content rules unchanged; `.md` only when a `.docx` cannot be produced.
In such a layout a **Details** sheet holds every task **the role may see** — the four groups plus a fifth,
`Chưa bắt đầu` / `Not started`, so a "toàn dự án" ask leaves no task invisible — and a **Summary**
sheet holds the count per group, the status conflicts and the points the reader must act on. The
chat reply keeps the four tables of the template.

**Print every table in full, as Markdown.** Every row, every column in order, each cell whole (only
newlines inside a cell collapsed). Empty cell `-`; empty section keeps its heading and header row plus
`_(không có)_`. A count recap (`"Quá deadline: 4, Đang triển khai: 14"`) is not the report — it drops
which task, whose, when, which is what the PM acts on. A long report may run over consecutive messages
marked `(tiếp)`; shortening it may not.

Opening lines, verbatim:

```
Báo cáo tiến độ dự án:
Cập nhật tiến độ dự án tại thị trường [Tên thị trường] dựa theo cập nhật mới nhất:
```

Then the four sections, heading written exactly — number, label, colon, row count — then the table:

```
1. Đầu việc quá deadline: (4)
2. Các đầu việc gần deadline: (1)
3. Các đầu việc đang trong quá trình triển khai: (14)
4. Các công việc đã hoàn thành: (3)
```

No extra section (`Các công việc sắp tới`, `Chưa bắt đầu`), no total line. A `Chuyên gia` gets all
four sections, filtered to their rows.

All four tables, six columns:

| STT | Danh mục công việc | PIC | Timeline | Ghi chú | Trạng thái |
|---|---|---|---|---|---|

`Timeline` = `Ngày bắt đầu – Ngày kết thúc`, `dd/mm/yyyy`, a missing side `-`. `Trạng thái` is the text
column as written. `Ghi chú` is empty on most rows — `-`, never invented. Level of detail expected:

```
| II.3.1 | Chuẩn bị hồ sơ & đầu mối nộp hồ sơ | Doox4 | 01/08/2026 – 21/08/2026 | - | Đang triển khai |
```

After table 4: the status-conflict list, if any.

### Labels in English and French

The Vietnamese is canonical (the customer's template). In an en/fr reply (`using-doox`, "Language")
only these labels change; sections, order and numbering do not:

| # | vi | en | fr |
|---|---|---|---|
| — | `Báo cáo tiến độ dự án:` | `Project progress report:` | `Rapport d'avancement du projet :` |
| — | `Cập nhật tiến độ dự án tại thị trường [X] dựa theo cập nhật mới nhất:` | `Progress at [X], as of the latest update:` | `Avancement sur le marché [X], selon la dernière mise à jour :` |
| 1 | `Đầu việc quá deadline` | `Overdue tasks` | `Tâches en retard` |
| 2 | `Các đầu việc gần deadline` | `Tasks near deadline` | `Tâches proches de l'échéance` |
| 3 | `Các đầu việc đang trong quá trình triển khai` | `Tasks in progress` | `Tâches en cours` |
| 4 | `Các công việc đã hoàn thành` | `Completed tasks` | `Tâches terminées` |

Empty: `_(không có)_` / `_(none)_` / `_(aucune)_`. Continued: `(tiếp)` / `(cont.)` / `(suite)`.
Conflict tag: `[đã tick, cột chữ chưa cập nhật]` / `[checkbox ticked, text column not updated]` /
`[case cochée, colonne texte non mise à jour]`. Column headers translate; every cell stays as the file
wrote it — say so in one line above the report when the languages differ.

## 6. Boundaries

**`project-update` is the only skill that writes to a plan file; `project-report` never does**, on
either branch. A conflict it finds goes to `project-update`, with its confirmation. It writes only the
report file (§5) and the project README (`using-doox`, "The project README").

## 7. Management branch

Read `assets/form-report.md` before writing — it holds the selection table, the five forms and the
context rules, and a user who edited it gets what they edited.

### 7.1 Input

Whatever the user supplied this session — memo, notes, email, loose table, plan file, an earlier
skill's output. Read it whole. The identity gate still runs before a plan file is read; a `Chuyên
gia` report is built only from their own rows.

Extract purpose, audience, scope, period, deadline and format rather than re-asking; ask only about a
gap that changes the report. Three rules are why this branch exists:

- **A figure in the material is the figure** — never replaced by model knowledge, rounded, or carried
  across in another unit or period.
- **Missing is named, not filled** — `[INPUT NEEDED: <field>]`, listed after the report. Missing is not
  zero, not "no issue", not approved, not complete.
- **States are kept apart** — đã giao ≠ đã nghiệm thu ≠ đã đóng; đề xuất ≠ đã duyệt; baseline gốc ≠
  ngày điều chỉnh chưa duyệt. Owner-complete is not reviewer acceptance.

### 7.2 Pick the form

One form, by the outcome the reader needs — not by cadence or topic:

| The reader needs | Form |
|---|---|
| kết quả hiện tại / tiến độ so với baseline | GX1 |
| một lựa chọn, một phê duyệt, một thay đổi baseline | GX2 |
| biến một mục tiêu thành kế hoạch triển khai hoặc khắc phục | GX3 |
| đánh giá rủi ro / sự cố và định phương án, hoặc escalate vượt thẩm quyền | GX4 |
| ghi nhận quyết định, giao việc, theo dõi cam kết đã có | GX5 |

A risk needing intervention takes GX4 first; otherwise GX2 → GX3 → GX5 → GX1. Then apply the one
`90_Context_Rules` row for the source report type — it adds checks, never a second form. Material
fitting no row takes the closest intent and says so; a request that is really two reports is asked
about, not merged.

### 7.3 Output

The chat reply in the chosen form's `template_*` shape — title, conclusion first, then tables —
following its `reasoning`, `minimum_inputs`, `missing_data` and, only when triggered,
`adaptive_blocks`. Saved as a `.docx` as in §5.

Default length about one page (250–450 words), shorter for an alert or action register, because the
reader is a manager; go longer when the user asks or the material needs it, and say why.

Written in the user's language (`using-doox`, "Language"), not the library's English default; quoted
values stay in the material's language. Form IDs and field keys (`GX2`, `template_options`) are never
printed — name the form by its Vietnamese name from §5.

Before returning, check: arithmetic and denominators reproduce, periods and units match, every
`[INPUT NEEDED: …]` is visible, no `{{placeholder}}` survived. Then name the form used and list the
gaps.

### 7.4 Boundaries

Writes from supplied internal facts only: no external research (that is `market-research`), nothing
sent. A report the user wants mailed goes to `mail-draft`, figures, cutoff and decision wording
carried across unchanged. Run only the stage asked for.
