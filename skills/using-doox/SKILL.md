---
name: using-doox
description: "REQUIRED FIRST for every Doox skill that opens a plan file — `project-report`, `reminder`, `project-insights`, `project-update`, `plan-consolidation`, `mail-draft`, and `calendar` once it reads a file. Load this before that skill, not after: it carries the identity gate that decides whose rows may be shown at all, which Doox skill answers which request, how a plan file's name encodes its market and project, how the two sheets are joined and which sheet each field comes from, what counts as done, and which of the three interface languages (vi/en/fr) the reply is written in. Skipping it shows one person another person's rows."
---

# Using Doox

Shared conventions. Individual skills carry their own logic; anything more than one of them relies on
belongs here.

## Which skill does what

| Skill | Use it when | Output |
|---|---|---|
| `using-doox` | always, before the others | nothing — conventions only |
| `project-report` | the user asks how one market's project is doing, or hands over a plan file and asks for the report | 4 tables in the customer's template, in the chat reply |
| `reminder` | the user asks what has to be handled today, asks to remind the PICs, or the 9am run fires | PM: one table across their markets + an Outlook draft per PIC (gửi khi PM yêu cầu). Chuyên gia: their own tables, no mail |
| `market-research` | the user names a target market and asks to research it, asks for a market report, asks to tìm nhà thầu, or asks how we compare against competitors/CPO | a new `.xlsx` built from the saved report framework, filled, every figure sourced — plus, for a competitor objective, the comparison tables in the chat reply |
| `mail-draft` | the user hands over a memo, a file or session data and asks to soạn/viết/draft a mail about it | one Outlook draft + the same content in the chat reply, filled into the saved form. Draft never sent unless the user says so in the same turn |
| `calendar` | the user asks to đặt lịch, dời lịch, xếp lịch tránh trùng, or asks what is on the calendar | the proposed event or arrangement in the chat reply, written to Google Calendar only after the user confirms. Reads the calendar freely, writes never without a yes |
| `candidate-review` | the user hands over a CV, hồ sơ ứng viên or interview transcript/recording and asks to đánh giá, chấm, so sánh or đề cử nhân sự | the scoring tables in the chat reply — per the saved evaluation framework, every mức carrying its evidence and source. Reads only what the user supplied |
| `project-update` | the user reports a change to a task — done, pending, slipped, blocked, deadline moved | the confirmed cells written into the plan files, and a report of what changed. The only skill that writes to a plan file |
| `project-insights` | the user asks what is stuck or going wrong, asks to summarise/classify issues, asks what finished projects taught, asks how far along a project is, or hands over a plan file with every task done | 4 sections in the chat reply — open issues by work area and issue type, past issues and their patterns, lessons across the archived plans, progress forecast. No mail, ever |
| `doc-compare` | the user hands over documents and asks to tóm tắt, đọc, so sánh, or what differs and what looks bất thường | tables in the chat reply. Reads only what the user supplied, never a plan file |
| `doc-translate` | the user hands over a `.docx` / `.xlsx` / `.pptx` and asks to dịch it | a new translated file keeping the original layout, plus what was passed through untranslated |
| `bid-review` | the user hands over báo giá or hồ sơ năng lực and asks to duyệt, chấm, xếp hạng, đề cử | a normalised comparison plus a shortlist, in the chat reply |
| `plan-consolidation` | the user hands over several kế hoạch files of different structures and asks to quy hoạch về một form chung, or to gộp kế hoạch nhiều phòng ban | new `.xlsx` files — normalised, or one merged read-only file. Two commands, never chained |

`project-report` reads **one** file and answers "where does this market stand"; `reminder` reads
**every** file in the project folder and answers "what has to happen today"; `project-insights` reads
every file too and answers "what is going wrong, of what kind, what was done about the same kind
before, and where this ends up"; `project-update` is the only one that **writes** — it changes the
cells the user named, after confirming them. Do not use one to approximate the other — a reminder is
not a shortened progress report, a progress report of one market does not tell a PIC what is due,
neither of them classifies an issue or forecasts anything, and none of them edits a cell.
`doc-compare`, `doc-translate` and `bid-review` sit outside that group entirely: they never open a
plan file, and they work only on the documents the user handed over in the session. `plan-consolidation`
does read plan files, but it reshapes and copies them rather than reporting on them — it answers
neither "where does this stand" nor "what is due", and it never writes to a file it read.

`mail-draft` and `reminder` are the only two skills that write mail, and they do not overlap:
`reminder` fans the day's rows out to every PIC on its own schedule; `mail-draft` turns one piece of
material the user just handed over into one mail. "Nhắc việc hôm nay" is `reminder`; "soạn mail về
việc này" is `mail-draft`.

`candidate-review` scores **a person**, `bid-review` scores **a contractor** — different frameworks,
never one in place of the other. `calendar` is the only skill that touches the calendar, and it does
not read plan files unless the user asks for deadlines to be pulled from them.

## The five document rules — `references/document-rules.md`

`DR1` – `DR5` govern `doc-compare`, `doc-translate` and `bid-review`: never substitute model
knowledge for what the document says, name missing data instead of filling it, pass codes and units
through untouched, compare only within the same scope, source every finding.

**Those three skills read `references/document-rules.md` directly and do not load this file.** They
run no identity gate and touch no plan file, so nothing else here applies to them — pulling the whole
of `using-doox` in to reach thirty lines is the cost this split exists to avoid.

## Language — vi / en / fr

This plugin is used in **Vietnamese, English and French**. Every skill answers in the user's language;
none of them assumes Vietnamese.

**Which language.** The language the user wrote the request in. If the request is too short to tell —
a bare filename, `ok`, `báo cáo` — use the language of the material being worked on. Still unclear,
ask; it is one question and it decides the whole reply. A user who names a language outranks both.

**What translates: the plugin's own words.** Headings, labels, column titles, explanations, the
sentences the skill writes itself.

**What never translates: the data.** This is `DR1` and `DR3` applied to language, and it holds in all
three directions:

- a value taken from a plan file, a document, a quote or a source — carried across exactly as written,
  in whatever language it was written in;
- tên pháp lý, mã số thuế, mã hiệu, model, số hiệu tiêu chuẩn, đơn vị đo, tên riêng — untouched;
- a status word that lives in a file (`Hoàn thành`, `Đang triển khai`, `Đã xác minh`) — quoted as the
  file has it, never rendered into the reply's language and written back;
- a quoted sentence used as evidence — original first, a translation beside it only if the reader
  needs one, and marked as a translation.

So a Vietnamese plan file reported to a French user comes back with **French labels around Vietnamese
cell values**. That is correct output, not a half-done translation. Say once, at the top of the
report, that the data is quoted in the file's language.

**Column matching is done on the file's own headers**, in the language the file uses. A plan file
written in English or French is read by matching its headers to the five required columns; a header
that cannot be matched stops the run and is asked about, exactly as a missing column is.

**Dates are `dd/mm/yyyy` in all three languages.** Never `mm/dd`, in any reply, whatever the
interface language — `03/04/2026` has to mean one thing across a team that reads three.

**A mail is written in the recipient's language, not the user's.** A Vietnamese PM drafting to a
French counterpart gets a French mail with a Vietnamese chat preview. Where the recipient's language
is unknown, use the language of the thread being answered, then the user's.

Numbers keep the source's decimal and thousands convention when quoted, and currencies keep their
code (`VND`, `EUR`, `USD`) rather than a symbol, so a figure cannot change meaning by crossing a
language.

## Plan file naming

```
[Thị trường] - [Tên dự án] - [Tên PM]
```

**The extension is optional and is not part of the convention.** A native Google Sheets file has no
extension at all — `Bo Bien Nga - Ke hoach lap dat tram sac - Do Hoang Tung` is a plan file, and
requiring `.xlsx` is what makes a run report "no plan file found" while the file sits in the folder.
Strip a trailing `.xlsx`/`.xls`/`.xlsm` if there is one, then split. A plan file is any spreadsheet
whose name splits into the three parts — Google Sheets
(`application/vnd.google-apps.spreadsheet`) and Excel alike.

Example — `Bo Bien Nga - Ke hoach xay dung tram sac EV - Nguyen Van A`:

| Field | Value |
|---|---|
| Thị trường | `Bo Bien Nga` |
| Tên dự án | `Ke hoach xay dung tram sac EV` |
| Tên PM | `Nguyen Van A` |

Split on ` - ` — space, hyphen, space. **Everything before the first separator is the market,
everything after the last is the PM, everything between them is the project name.** Taking the outer
two first matters: a project name may hold further ` - ` separators, a market name and a PM name will
not.

The separator needs a space on both sides. A bare hyphen is part of a name, not a separator:
`HerioGreen-Vietnam.xlsx` has no separator at all and yields nothing.

Fewer than two separators means the name does not follow the convention — ask the user, do not
treat the last part as a PM name that happens to be a project name.

Trim whitespace from all three parts. Names carry no diacritics and follow no capitalisation rule —
pass them through exactly as written, do not "correct" `Bo Bien Nga` into `Bờ Biển Ngà`.

Ignore Excel lock files: `~$…` and `.~lock.…#`.

## Reading a plan file

Every skill reads a plan file the same way. This section is the only description of it — a skill
that needs a field takes it from here.

**How the file is opened.** No harness here parses `.xlsx` with its file-reading tool — reading one
means a small `openpyxl` script run through the shell, and that is the expected mechanism, not a
workaround. Load with `data_only=True` so a formula cell yields its cached value rather than the
formula text. A native Google Sheet reached through a connector is read through that connector
instead; it cannot be written (see "Writing a plan file").

The data lives in two sheets and has to be joined:

- The plan detail sheet — Danh mục CV, Phương án triển khai, Tiêu chí hoàn thành, Người phụ trách,
  Người hỗ trợ, Ngày bắt đầu, Ngày kết thúc, **Trạng thái (text)**, Rủi ro, Ghi chú.
- The control sheet — Cập nhật hiện trạng, Vấn đề phát sinh, **Trạng thái (checkbox TRUE/FALSE)**,
  Phương án giải quyết.

**Join the two sheets by row position** — row *n* of the detail sheet is row *n* of the control
sheet. Both other keys are broken on real files: STT restarts at every section, and `Danh mục CV`
repeats (on the reference file 4 labels cover 14 rows, e.g. `Nghiệm thu giấy phép` appears 4 times,
so joining by label silently merges four different tasks into one).

Before joining, check the two sheets line up by **comparing the STT columns — the raw numbering cells
(`A`, `II`, `3.1`, `5.1.2`…) of one sheet against the other, row index by row index, over the full
sheet.** STT is not usable as a join key, but as an alignment check it is the right column: it is
present on section rows and stub rows alike, it is short, and a shift shows up at the first row
where the two disagree.

**Do not compare "how many rows have data".** Each sheet carries its own columns, filled to its own
extent — a stub row may be blank in the detail sheet and hold a `FALSE` checkbox in the control one,
and either sheet may run further with formatting or stray cells. Counting rows that way gives two
different numbers for sheets that are perfectly aligned, and reports a mismatch that is not there.

**An STT cell filled on one sheet and empty on the other is not a mismatch.** The control sheet
leaves the level-3 numbering out on the rows where the detail sheet types it (8 rows of the reference
file, `3,1,1` through `4,1,4`) — the two sheets are perfectly aligned there and `Danh mục CV` on both
rows proves it. Compare only the row indexes where **both** sheets carry a value; treat a blank on
either side as agreement.

If the STT cells differ at some row index, the sheets are shifted — stop and report it, naming the
first row index that differs and quoting both values. A shifted join produces output that looks
fine and is wrong throughout. If every STT matches, the sheets are aligned: carry on and produce the
report. Never claim one sheet "has extra task rows" without that first differing row index.

Five required columns: **Danh mục công việc**, **Trạng thái (text)**, the **checkbox**, **Ngày bắt
đầu**, **Ngày kết thúc**. If any one of them is missing, stop and ask the user — do not guess.

Report which columns were matched before printing anything. **One line per file — not one per column
and not one per sheet**, even though a file has two. The five required columns go on that one line,
each with the sheet and the column letter it was found at:

```
Bo Bien Nga: chi tiết 'KH Bảng 3 - Chi tiết' cột D = Danh mục CV, I = Ngày bắt đầu, J = Ngày kết thúc, K = Trạng thái (chữ); kiểm soát 'KH Kiểm soát tiến độ & sự cố' cột J = Trạng thái (checkbox)
```

A row with no Danh mục CV, or with a Danh mục but both date cells empty, is a section heading
(`A`, `1`, `2`…). It is not a task: drop it from every table and from every count.

**Where each field comes from.** The two sheets both carry `Ngày bắt đầu`, `Ngày kết thúc`,
`Trạng thái` and `Ghi chú` under the same name — take each from the sheet named here, not from
whichever one is found first:

| Field | Sheet | Source column |
|---|---|---|
| STT | detail | built, see below |
| Danh mục công việc | detail | `Danh mục CV` |
| PIC | detail | `Người phụ trách` |
| Ngày bắt đầu / Ngày kết thúc | detail | same names |
| Phương án triển khai | detail | `Phương án triển khai` |
| Tiêu chuẩn hoàn thành | detail | `Tiêu chí hoàn thành/ bằng chứng xác nhận` |
| Rủi ro | detail | `Rủi ro` |
| Trạng thái (text) | detail | `Trạng thái` |
| Hiện trạng vấn đề | control | `Cập nhật hiện trạng` |
| Vấn đề phát sinh | control | `Vấn đề phát sinh` |
| Phương án xử lý | control | `Phương án giải quyết` |
| Ghi chú | control | `Ghi chú` |
| checkbox | control | `Trạng thái` |

**STT is built, not copied.** The numbering sits in several columns — a section marker (`A`, `B`,
`I`, `II`…), then level-2 numbers (`3.1`), then level-3 (`5.1.2`). Print the nearest section marker
above the row, a dot, then the row's own number: `II` + `3.1` = `II.3.1`. Only letters and Roman
numerals are section markers; a purely numeric heading (`1`, `2`, `3`) is a sub-group, not a section.
Without the prefix, `3.1` appears many times over and no row can be identified.

Some level-3 numbers are typed with commas instead of dots — `3,1,1` where `3.1.1` was meant (8 of 28
on the reference file). Normalise commas to dots, so the printed STT reads `II.3.1.1`.

**Done = the checkbox is TRUE *and* the text column reads `Hoàn thành`.** The checkbox alone is not
enough, and a past end date is not a completion signal at all. Anything failing either condition
counts as not done. The text column holds three values: `Chưa triển khai`, `Đang triển khai`,
`Hoàn thành`.

Dates print as `dd/mm/yyyy` everywhere.

### The `PIC → email` directory

A third party's address is read out of the plan files and never from anywhere else. This is the one
description of how; `reminder`, `mail-draft` and `calendar` all take it from here.

The PIC cell holds an anonymised code — `Doox1`–`Doox10`, `Qn1`–`Qn10`, `Thầu`. The address is typed
**once, on one row**, next to its code; every other row carries the bare code. So build the directory
before needing it: scan every row of every plan file in the project folder, collect each `code →
email` pair found, and apply it to all rows carrying that code.

**The cell separates code from email four different ways** — a newline, an en dash `–` (U+2013, not
the ASCII `-`), parentheses, or nothing but a space. Handle all four; matching only the ASCII hyphen
drops most of the file.

`Thầu` is a contractor, not a person, and has no personal address at all. Its rows still appear
wherever rows are printed; it never receives mail and is never an attendee.

**A code with no email anywhere in the files gets no address, and none is invented.** Not from a
name, not from a pattern seen in the other addresses, not from a colleague's domain. What each skill
does with that is its own: `reminder` lists the code at the end of the report, `mail-draft` leaves
the recipient empty and says so, `calendar` asks the user. None of them guesses.

This is not the same thing as "Matching the user to a PIC" below — that settles which code belongs to
the **person running the session**. This one looks up somebody else's contact.

## Writing a plan file

**`project-update` is the only skill that writes to a plan file. Every other skill is read-only** —
`reminder`, `project-report` and `project-insights` read and print, never touch a cell. A report
that "fixed a wrong date while it was in there" is a bug in that skill, not a service.
`plan-consolidation` reads plan files and writes **new** ones; it never writes back to a file it
read, and a "corrected" source file is the same bug.

Plan files are co-authored — Google Drive, OneDrive, SharePoint — so a write lands in someone else's
file the moment it is saved. The rules that make it safe live in `project-update`, and hold for
anything that writes: write only the cells the user named and confirmed, keep the two sheets in step,
never rewrite a cell to "tidy" it.

**Where the write can land.** A file open through the local project folder — including a Drive /
OneDrive / SharePoint folder synced onto local disk — is written in place, and the sync carries it
up. A file reachable **only** through a connector cannot be written: the Drive connector reads,
searches, creates and copies, it has no cell-level update. Never fake it by creating a second file or
uploading a "corrected" copy — that splits the project across two files and the team keeps editing
the old one. Print the confirmed change-set for the user to apply by hand instead, and say plainly
that the file was not written.

## The project README

The Cowork project folder — the one holding the plan files — carries a `README.md` describing what
is in it. **Read it before doing anything else**, and update it whenever the run turned up something
it does not yet say. If there is no `README.md` at all, see "Who is running this" below before
anything else.

It holds what cannot be re-derived by looking at the files: which markets and projects are live and
which file each lives in, naming conventions in use, quirks of the customer's template found the
hard way, and decisions the user has settled. Not a changelog, not a run history, not a copy of the
data — a picture of the current state that a new session can be handed.

Update it when a run reveals:

- a new plan file, a renamed one, a new market or project;
- something about the data worth not rediscovering — a duplicated label, a status column that
  disagrees with a checkbox, a sheet that changed shape;
- a convention or rule the user has just settled.

Rewrite the affected lines rather than appending; a README that only grows stops being read.

A Doox skill writes to these things and nothing else: a plan file under `project-update`; this README;
under `market-research`, the market report `.xlsx` it produces plus its source-log folder
(`doox-sources/<market-slug>/`, holding that market's evidence cache and the run's claim ledger);
under `plan-consolidation`, the new `.xlsx` files it generates; under `doc-translate`, the translated
copy it generates. Every other skill is read-only, and none of them ever writes over a file the user
supplied.

### The README lives locally, never on a connector

**Absolute rule: never create, upload, copy, sync or update a `README.md` through a connector.** Not
Google Drive, not SharePoint, not OneDrive, not Dropbox, not Box, not a Gmail attachment, not any
other remote store reached through a connector or MCP server — whatever the connector is called and
however convenient it looks. The README is a local file in the local working folder, and that is the
only place it exists.

This holds even though `project-update` may write to a plan file: the plan file is the team's, the
README is not. A run that reads a plan file off Drive still keeps its README on the local disk. Never "put the README next to the plan file so the team can see it" — the identity fields it
carries decide what each person is allowed to see, and a copy on a shared drive is a copy anyone
there can edit.

No local disk to write to means writing nothing — keep it in the session and ask again next time.
Never fall back to a connector for lack of anywhere else.

**The README is internal. Never mention it to the user — not in any skill, not at any point.** Not
its name, not that one exists, not that one is missing, not that it is being read, written, or
searched for, not the identity fields kept in it. Lines like `Giờ tôi cần tìm folder dự án và file
README trên Google Drive trước khi đọc file kế hoạch` are the bug: they name an internal file, tell
the user where the identity check gets its answers, and point at a file they could edit to hand
themselves a role.

Say what is being done in terms of the user's own request instead — `Đang đọc file kế hoạch của thị
trường Bo Bien Nga` — or say nothing. Reading and updating the README happens silently, with no
narration before, during, or after. The same holds for tool-call narration: do not announce the
folder listing or the file read that finds it.

## Who is running this

Every Doox skill shows the user their own work, not everyone's. That needs three facts, and they
live in the README:

```markdown
## Người dùng
- Tên: Nguyễn Văn A
- Email: a.nguyen@example.com
- Vai trò: Project Manager
- Mã PIC: Doox3          <!-- chỉ với vai trò Chuyên gia -->
```

Those four are the whole schema. There is no separate `Chức vụ` field and none is asked for: a skill
that needs a job title for a signature — `mail-draft` is the only one — uses `Vai trò` as written.

**Missing the section, or missing any one of those lines, means asking — no matter which run this
is.** No `README.md` at all, a README with no `## Người dùng`, a section with a name but no email:
all the same case.

**A README that disagrees with the operator is the same case too.** Where the harness exposes the
signed-in account's address and it is not the `Email` in the README, the recorded identity belongs to
somebody else — a shared folder, a copied README, a machine handed over. Do not run on it and do not
reconcile it by picking the more senior of the two: clear the three facts and ask again from step 1.
A specialist silently inheriting a `Project Manager` README reads every row of every market, which is
the one failure this whole section exists to prevent. Where the harness exposes no address, the
README stands as written.

**This is the first step of every run that touches a plan file, and it is a gate.** Which skill sits
where is settled here and nowhere else — a skill claiming to be exempt in its own file does not make
it so:

| Skill | Gate |
|---|---|
| `project-report`, `reminder`, `project-insights`, `project-update` | always |
| `plan-consolidation` | always, **and** restricted to a verified `Project Manager`; see its own skill for the one case where no gate applies |
| `market-research`, `doc-compare`, `doc-translate`, `bid-review`, `candidate-review` | never — they read no plan file and show nobody's rows, so they run for either role |
| `calendar` | conditional — ungated until the run opens a plan file, which is either a deadline pull or a `PIC → email` lookup; that puts the gate back on and the rows are filtered by role like any other |
| `mail-draft` | always, for a different reason — it signs the mail with the user's `Tên` and `Vai trò`, so it needs the identity even when it opens no plan file. The role filter applies too, the moment it resolves a PIC code |

The five ungated skills read only what the user handed over in the session. That is the whole test:
a skill that can reach a plan file is gated, and no other consideration exempts it.

Settle who is running this before
anything else happens — before listing the project folder, before opening a plan file, before
parsing a sheet, before counting a task, before printing a table, before drafting mail. Nothing about
a plan file is read or shown while any of the three facts is missing, and a `Chuyên gia` has no rows
selected for them until their PIC is settled too. Do not "get a head start" on the file while waiting
for the answer: work done before the identity is known is work that may belong to someone else, and a
report printed first cannot be un-shown once the role turns out to be wrong.

**The procedure lives in `references/identity-intake.md`.** How to ask (the role through the
structured-question tool, the name and email as text, both bare), how a `Chuyên gia` is matched to a
PIC code, and how a claimed `Project Manager` is verified against the filename — all of it is there,
verbatim and unchanged.

**Read it only when there is a gap to fill.** A README carrying all four fields, with its `Email`
agreeing with the signed-in account, answers the gate on its own — that is the ordinary run after the
first one, and it reads nothing further. Open the reference when the section is missing, a line
inside it is missing, the recorded email disagrees with the operator, or a `Chuyên gia` has no
`Mã PIC` yet.

Once the answers are in and the role has passed its check, carry on with the run that was
interrupted, from the beginning.

### What each role sees

Internal — this table decides what to print. Do not recite it to the user, least of all while asking
for their role.

| Role | Sees |
|---|---|
| `Project Manager` | every row of the files whose `Tên PM` matches their name |
| `Chuyên gia` | only rows where their code is `Người phụ trách`, plus rows where it is `Người hỗ trợ`, kept in a separate table |

This applies to every Doox skill, not just the reminder. State the identity in use before printing,
one line, so a wrong match shows up immediately:

```
Người dùng: Nguyễn Văn A (a.nguyen@example.com) | Vai trò: Chuyên gia | Mã PIC: Doox3
```

## When a file does not match a convention

Ask the user. Never guess a market from a filename with no separator, and never fall back to the
whole filename — a report published under the wrong market is worse than one that stopped to ask.

## Say what was read

State the reading before acting on it, one line:

```
Thị trường: Bo Bien Nga | Dự án: Ke hoach xay dung tram sac EV (từ tên file)
```

A wrong reading then shows up immediately, instead of after a full report has been built on it.

**The third part of the filename stays out of that line, and out of every other line printed before
the user has been verified.** Market and project only. Do not print the raw filename either — it
carries the PM name, and a line that quotes the filename hands over the answer to the check the
skill is about to run. After a `Project Manager` has matched, their own name is theirs to see; a
`Chuyên gia` never needs it.
