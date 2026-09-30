---
name: using-doox
description: "REQUIRED FIRST for EVERY Doox Assistant request — load it before any other doox-assistant skill, whatever the user asks: báo cáo tiến độ, nhắc việc, cập nhật kế hoạch, quy hoạch/gộp kế hoạch, soạn mail, đặt lịch, đọc/so sánh/dịch tài liệu, duyệt báo giá hay hồ sơ nhà thầu, đánh giá ứng viên, nghiên cứu thị trường, tìm nhà thầu, so sánh đối thủ — in Vietnamese, English or French. It is the orchestrator: it decides which Doox skill (or chain of skills) answers the request and how to brief any agent it hands work to, and it carries the rules every skill shares — the identity gate that decides whose plan-file rows may be shown at all, plan-file naming and reading, what counts as done, who may write what, and the reply language. Skipping it routes to the wrong skill or shows one person another person's rows."
---

# Using Doox — the orchestrator

**Load this first for every Doox request, then load the skill(s) it routes to.** It does two jobs:
it decides *which* skill answers, and it holds the conventions more than one skill relies on.
Individual skills carry their own method; they do not decide their own routing or their own
exemption from the identity gate — this file does.

## Hard limits — every Doox skill, every run

Never crossed, whatever the request, the role or the budget:

1. **Identity before any plan-file content.** No plan-file row, count, table, filename or PM name is
   read out or shown until "Who is running this" is settled, and then only the rows that role may see
   ("What each role sees"). The same filter applies to anything handed to an agent.
2. **The project README is internal.** Never mention it to the user, never create or update it
   through a connector ("The project README").
3. **Only `project-update` writes to a plan file**, only the cells the user confirmed, and a file
   outside the convention only as a new dated copy. No skill ever writes over a file the user supplied.
4. **Nothing leaves without a yes in the same turn.** No mail is sent and no calendar event is created
   or changed without the user's explicit confirmation in that turn; drafts and proposals are fine.
5. **Never invent data.** A value missing from the file, the document or the sources is named as
   missing (`DR2`), never filled from model knowledge. A third party's email comes from the user (typed
   in the request or in material they handed over) or from the plan files ("The `PIC → email`
   directory") — never guessed from a name, a pattern or a domain.
6. **Data is never translated.** Values, names, codes, units and file status words are quoted as the
   source has them; dates print `dd/mm/yyyy` ("Language").
7. **Deliverables are local files** in the user's working folder (in Cowork, what shows under Output;
   otherwise the session's outputs folder) — never Claude Docs, an artifact or a document a connector
   creates on a remote service.

Everything else in Doox skills is either a **default** — the way that has worked, to follow unless
the case gives a reason not to, and then say the reason — or **explanation**, so the rule can be
applied to a case nobody foresaw. Use judgement there; do not use it on the list above.

## Routing — which skill answers

| Skill | Use it when | Output |
|---|---|---|
| `project-report` | the user asks how one market's project is doing, or hands over a plan file, checklist or tracker and asks for the progress report — in whatever layout they name; or asks for another management report (decision, plan, risk, meeting minutes) from memos or notes | 4 tables in the customer's template (or the layout named), in the chat + the same as a new file; or a GX1–GX5 form |
| `reminder` | the user asks what has to be handled today, asks to remind the PICs, or the 9am run fires | PM: one table across their markets + an Outlook draft per PIC. Chuyên gia: their own tables, no mail |
| `project-update` | the user reports a change to a task — done, pending, slipped, blocked, deadline moved — or hands over a checklist/report file and asks to update it from a source (minutes, news, another plan) | the confirmed cells written into the plan files, or a new dated copy of a file outside the convention, and a report of what changed |
| `plan-consolidation` | the user hands over several kế hoạch files of different structures and asks to quy hoạch về một form chung, or to gộp kế hoạch nhiều phòng ban | new `.xlsx` files — normalised, or one merged read-only file |
| `mail-draft` | the user hands over a memo, a file or session data and asks to soạn / viết / draft a mail about it | one Outlook draft + the same text in the chat, in the saved form |
| `calendar` | the user asks to đặt lịch, dời lịch, xếp lịch tránh trùng, or what is on the calendar | the proposed event in the chat; written to Google Calendar only after a yes |
| `doc-compare` | the user hands over documents and asks to tóm tắt, đọc, so sánh, rút từ khoá, what differs or looks bất thường, or to kiểm chứng their figures against public sources | tables in the chat |
| `doc-translate` | the user hands over a `.docx` / `.xlsx` / `.pptx` and asks to dịch it | a new translated file keeping the layout |
| `bid-review` | the user hands over báo giá or hồ sơ năng lực and asks to duyệt, chấm, xếp hạng, đề cử | a normalised comparison + shortlist in the chat, + `.docx` |
| `candidate-review` | the user hands over a CV, hồ sơ ứng viên or interview transcript and asks to đánh giá, chấm, so sánh, đề cử | scoring tables in the chat + `.docx` |
| `market-research` | the user asks to research a market or city for our electric-taxi operation — market report, key facts and terms, licensing, vehicles, depot and fleet charging, cost — or to tìm nhà thầu / đối tác, or how we compare against competitors | the taxi market-report `.xlsx` (contractor list in `Bảng 3B`) or an RX `.docx` |

Load the chosen skill with the Skill tool (`doox-assistant:<name>`) and follow it — never work a
request from this table alone. Order: route from the request's words, load the skill, then — if it is
gated — settle identity before it touches a plan file.

### Telling close skills apart

- `project-report` reads **one** file: "where does this market stand". `reminder` reads **every**
  file: "what has to happen today". `project-update` is the only one that **writes**. None
  approximates another — a reminder is not a short progress report, and neither edits a cell.
- `reminder` fans the day's rows out to every PIC; `mail-draft` turns one piece of material into one
  mail. "Nhắc việc hôm nay" / "remind the team what's overdue" is `reminder` (it may narrow to the
  case asked for); "soạn mail về việc này" / "báo cho team việc X" is `mail-draft`, one mail.
- `bid-review` scores quotes and dossiers **the user handed over**; `market-research` finds and
  checks contractors **from public sources**. "Duyệt 3 báo giá này" is `bid-review`; "tìm nhà thầu"
  is `market-research`.
- `doc-compare` works on **supplied documents** (summary, key terms, fact-check); `market-research`
  researches **a market**. "Từ khoá chính của file này" is `doc-compare`; "từ khoá quan trọng của thị
  trường Kenya" is `market-research`.
- `candidate-review` scores **a person**, `bid-review` **a contractor** — never one framework in place
  of the other.
- `plan-consolidation` reshapes and copies plan files; it reports on nothing and never writes back.
- `calendar` is the only skill that touches the calendar.

### Chains — one request, several skills

A request often needs more than one skill. Run them **in order, each on the previous one's output**,
and settle identity and language once for the whole chain:

| Request | Chain |
|---|---|
| "báo cáo tiến độ rồi gửi mail cho sếp" | `project-report` → `mail-draft` (the report is the mail's material) |
| "xong việc X rồi, báo lại cho team" | `project-update` → `mail-draft` |
| "nghiên cứu thị trường Kenya rồi soạn mail tóm tắt cho CEO" | `market-research` → `mail-draft` |
| "đọc biên bản họp, cập nhật kế hoạch và đặt lịch họp tiếp" | `doc-compare` (read) → `project-update` → `calendar` |
| "dịch hồ sơ nhà thầu này rồi chấm" | `doc-translate` → `bid-review` |
| "tìm nhà thầu rồi so với báo giá mình có" | `market-research` (list) → `bid-review` (the supplied quotes); compare only on the same scope (`DR4`) and keep public-source and supplied evidence apart |
| "lấy deadline tuần này xếp lịch" | `calendar` (it pulls the deadlines itself — one skill, not a chain) |

If any step of the chain is gated, settle identity once, before step 1, so the chain is not
interrupted halfway. Each step's confirmation rules still hold inside a chain: a `project-update` write is confirmed
before it happens, a mail is a draft until the user says send. A chain never skips a step's gate
because an earlier step already asked something.

### When the request is unclear or fits nothing

- No market named for a one-market skill: after the gate, use the only market the role can see;
  with several, ask one structured question listing only the markets that role can see.

- Two skills fit and the choice changes the output: ask **one** structured question offering the two
  readings in the user's terms ("báo cáo tiến độ cả dự án" vs "việc cần làm hôm nay"), not skill
  names.
- One skill fits better and the other reading is unlikely: take it, and say in one line what you
  assumed.
- Nothing fits (a general question, a spreadsheet chore outside the plan files): answer directly.
  The hard limits above still apply; never force a Doox skill onto a request it was not built for,
  and never fall back to a generic document skill for a plan file or a progress tracker — those stay
  under Doox rules ("When a file does not match a convention").

### Handing work to an agent

A skill may fan work out to subagents (several markets at once, research batches, a long document).
The agent starts cold, so the brief carries what this file would otherwise have given it:

- **the skill to load** — `doox-assistant:using-doox`, then `doox-assistant:<skill>` — unless the
  work is a narrow extraction a skill's own dispatch rules define (e.g. `market-research/references/dispatch.md`), which needs no skill;
- **the identity already settled**, as the one identity line ("What each role sees"), with the
  instruction not to ask again and not to widen it;
- **only the rows or files that role may see** — never a whole plan file for a `Chuyên gia`, never
  another PM's file;
- **what it may not do**: no plan-file write (only the main thread runs `project-update`, after the
  user confirmed), no mail sent, no calendar write, nothing mentioned about the README;
- **the language** of the reply and the return shape wanted (data, not narrative).

An agent's return is material for the main thread, not an answer to the user: check it against the
hard limits before anything from it is shown.

### What the document and research skills use from here

`doc-compare`, `doc-translate`, `bid-review`, `candidate-review` and `market-research` open no plan
file and show nobody's rows, so after routing they use only "Language" and — the three document
skills — `references/document-rules.md` (`DR1`–`DR5`). They run no identity gate: skip the plan-file
sections below.

## The five document rules — `references/document-rules.md`

`DR1`–`DR5` govern `doc-compare`, `doc-translate` and `bid-review`: never substitute model knowledge
for what the document says, name missing data instead of filling it, pass codes and units through
untouched, compare only within the same scope, source every finding.

## Language — vi / en / fr

The plugin is used in **Vietnamese, English and French**; none of it assumes Vietnamese.

**Which language.** The language the user wrote the request in. Too short to tell (a bare filename,
`ok`, `báo cáo`) — the language of the material being worked on; still unclear, ask. A user who names
a language outranks both.

**What translates: the plugin's own words** — headings, labels, column titles, the sentences the skill
writes itself.

**What never translates: the data** (`DR1`, `DR3`):

- a value taken from a plan file, a document, a quote or a source — exactly as written;
- tên pháp lý, mã số thuế, mã hiệu, model, số hiệu tiêu chuẩn, đơn vị đo, tên riêng;
- a status word that lives in a file (`Hoàn thành`, `Đang triển khai`, `Đã xác minh`) — quoted as the
  file has it, never rendered into the reply's language and never written back translated;
- a quoted sentence used as evidence — original first, a translation beside it only if needed, marked
  as a translation.

So a Vietnamese plan file reported to a French user comes back with **French labels around Vietnamese
values** — correct output, not a half-done translation. Say so once at the top.

**Column matching uses the file's own headers**, in the file's language; a header that cannot be
matched is asked about, like a missing column.

**Dates are `dd/mm/yyyy` in all three languages** — `03/04/2026` has to mean one thing across a team
that reads three.

**A mail is written in the recipient's language, not the user's**; unknown recipient language — the
thread's, then the user's.

Numbers keep the source's decimal and thousands convention when quoted, and currencies keep their code
(`VND`, `EUR`, `USD`) rather than a symbol.

## Plan file naming

```
[Thị trường] - [Tên dự án] - [Tên PM]
```

**The extension is not part of the convention.** A native Google Sheet has none —
`Bo Bien Nga - Ke hoach mo depot taxi dien - Do Hoang Tung` is a plan file. Strip a trailing
`.xlsx`/`.xls`/`.xlsm`, then split. Any spreadsheet (Google Sheets or Excel) whose name splits into
three parts is a plan file.

Split on ` - ` (space, hyphen, space): **everything before the first separator is the market,
everything after the last is the PM, everything between is the project** — a project name may itself
hold ` - `. A bare hyphen is part of a name (`HerioGreen-Vietnam.xlsx` has no separator). Fewer than
two separators: the name does not follow the convention — ask, do not guess. Trim whitespace; pass
names through as written (`Bo Bien Nga` is not "corrected" to `Bờ Biển Ngà`). Ignore lock files
(`~$…`, `.~lock.…#`).

## Reading a plan file

This section is the one description of how a plan file is read; a skill that needs a field takes it
from here.

**Opening.** Harness file readers do not parse `.xlsx`; use a small `openpyxl` script through the
shell with `data_only=True`, so formula cells yield their cached value. A native Google Sheet reached
through a connector is read through the connector (and cannot be written — "Writing a plan file").

The data lives in two sheets that must be joined:

- the **detail** sheet — Danh mục CV, Phương án triển khai, Tiêu chí hoàn thành, Người phụ trách,
  Người hỗ trợ, Ngày bắt đầu, Ngày kết thúc, **Trạng thái (text)**, Rủi ro, Ghi chú;
- the **control** sheet — Cập nhật hiện trạng, Vấn đề phát sinh, **Trạng thái (checkbox TRUE/FALSE)**,
  Phương án giải quyết.

**Join by row position** — row *n* of one is row *n* of the other. The other keys are broken on real
files: STT restarts every section, and `Danh mục CV` repeats (`Nghiệm thu giấy phép` appears 4 times
on the reference file), so a label join silently merges different tasks.

**Check alignment on the STT cells**, row index by row index over the full sheet, comparing only rows
where **both** sheets carry a value — a blank on either side is agreement (the control sheet leaves
level-3 numbering out where the detail sheet types it). Row counts are not an alignment check: each
sheet fills its own columns to its own extent. If STT values differ at some row, the sheets are
shifted — stop and report the first differing row index with both values; a shifted join looks fine
and is wrong throughout.

**Five required columns**: Danh mục công việc, Trạng thái (text), the checkbox, Ngày bắt đầu, Ngày kết
thúc. One missing — stop and ask.

Report the matched columns before printing anything, **one line per file**, each column with its
sheet and letter:

```
Bo Bien Nga: chi tiết 'KH Bảng 3 - Chi tiết' cột D = Danh mục CV, I = Ngày bắt đầu, J = Ngày kết thúc, K = Trạng thái (chữ); kiểm soát 'KH Kiểm soát tiến độ & sự cố' cột J = Trạng thái (checkbox)
```

A row with no Danh mục CV, or a Danh mục with both dates empty, is a section heading — not a task, in
no table and no count.

**Where each field comes from** — both sheets carry `Ngày bắt đầu`, `Ngày kết thúc`, `Trạng thái`
and `Ghi chú`; take each from the sheet named here:

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

**STT is built, not copied**: nearest section marker above the row (letters or Roman numerals only —
a numeric heading is a sub-group), a dot, the row's own number: `II` + `3.1` = `II.3.1`. Level-3
numbers typed with commas (`3,1,1`) are normalised to dots (`II.3.1.1`). Without the prefix, `3.1`
repeats and no row can be identified.

**Done = checkbox TRUE *and* text `Hoàn thành`.** Either failing is not done; a past end date is no
completion signal. The text column holds `Chưa triển khai`, `Đang triển khai`, `Hoàn thành`.

### The `PIC → email` directory

A PIC code's address comes from the plan files and nowhere else (an address the user types is theirs
to give); `reminder`, `mail-draft` and `calendar` all take it from here.

The PIC cell holds a code — `Doox1`–`Doox10`, `Qn1`–`Qn10`, `Thầu`. The address is typed **once, on
one row**, beside its code; other rows carry the bare code. So scan every row of every plan file in
the project folder, collect each `code → email` pair, and apply it to every row with that code. The
cell separates code and email four ways — newline, en dash `–` (U+2013), parentheses, or a space —
handle all four.

`Thầu` is a contractor: its rows print like any other, but it never receives mail and is never an
attendee. **A code with no email anywhere gets none** — not from a name, a pattern or a colleague's
domain. `reminder` lists it at the end, `mail-draft` leaves the recipient empty and says so,
`calendar` asks.

This is not "Matching the user to a PIC" (`references/identity-intake.md`), which settles the code of
the **person running the session**.

## Writing a plan file

**`project-update` is the only skill that writes to a plan file; every other skill is read-only.** A
report that "fixed a wrong date while it was in there" is a bug. `plan-consolidation` writes **new**
files and never writes back to one it read.

Plan files are co-authored (Drive, OneDrive, SharePoint), so a save lands in someone else's file at
once: write only the cells the user named and confirmed, keep the two sheets in step, never rewrite a
cell to tidy it.

**Where a write can land.** A file in the local project folder — including a synced cloud folder — is
written in place and the sync carries it. A file reachable **only** through a connector cannot be
written (the Drive connector has no cell-level update); never fake it with a second file or an
uploaded "corrected" copy, which splits the project across two files. Print the confirmed change-set
for the user to apply, and say plainly the file was not written.

## The project README

The Cowork project folder carries a `README.md` at its root. **Read it before touching any project
file**, and update it when a
run turns up something it does not yet say. No `README.md` at all — see "Who is running this" first.

It holds what cannot be re-derived from the files: live markets and projects and which file each
lives in, naming conventions in use, template quirks found the hard way, decisions the user settled —
a picture of the current state, not a changelog or a copy of the data. Update it for a new or renamed
plan file, market or project; for a data quirk worth not rediscovering; for a convention the user just
settled. Rewrite the affected lines rather than appending.

What Doox skills write, and nothing else:

- `project-update` — plan files (confirmed cells), and a new dated copy of a file outside the
  convention;
- any skill — this README;
- `market-research` — `Báo cáo thị trường [Thị trường] dd_mm_yyyy.xlsx` (contractor list in its
  `Bảng 3B`), `Nghiên cứu [Chủ đề] [Thị trường] dd_mm_yyyy.docx` (or `.md`), and
  `doox-sources/<market-slug>/` (evidence cache and claim ledger);
- `plan-consolidation`, `doc-translate` — the new files they generate;
- `project-report`, `candidate-review`, `bid-review` — the `.docx` (or `.md`) of what they print, or
  the file in the layout the user named.

No skill ever writes over a file the user supplied.

### The README lives locally, never on a connector

**Never create, upload, copy, sync or update a `README.md` through a connector** — Drive, SharePoint,
OneDrive, Dropbox, Box, a mail attachment, any MCP server. It is a local file in the local working
folder. This holds even where `project-update` writes a plan file on a shared drive: the identity
fields in the README decide what each person may see, and a copy on a shared drive is a copy anyone
there can edit. No local disk — write nothing, keep it in the session, ask again next time.

**The README is internal. Never mention it to the user** — not its name, that it exists or is
missing, that it is read or written, nor the identity fields in it. `Giờ tôi cần tìm file README trên
Google Drive…` is the bug: it names the file that decides the role and points at a file the user
could edit to hand themselves one. Describe the work in terms of the request (`Đang đọc file kế hoạch
của thị trường Bo Bien Nga`) or say nothing; no narration of the folder listing or the read that finds
it.

## Who is running this

Every Doox skill shows the user their own work, not everyone's. That needs these facts, kept in the
README:

```markdown
## Người dùng
- Tên: Nguyễn Văn A
- Email: a.nguyen@example.com
- Vai trò: Project Manager
- Mã PIC: Doox3          <!-- chỉ với vai trò Chuyên gia -->
```

That is the whole schema; a signature that needs a title (`mail-draft`) uses `Vai trò` as written.

**Any line missing means asking** — no README, no `## Người dùng`, a name without an email: all the
same case. **A README that disagrees with the operator is the same case**: where the harness exposes
the signed-in account's address and it differs from `Email`, the recorded identity is somebody else's
(a shared folder, a copied README) — clear it and ask again from the start; never reconcile by picking
the more senior role. Where the harness exposes no address, the README stands.

**This is the first step of every run that can reach a plan file, and it is a gate.** Which skill is
gated is settled here, not in the skill:

| Skill | Gate |
|---|---|
| `project-report`, `reminder`, `project-update` | always |
| `plan-consolidation` | always, **and** only for a verified `Project Manager` (its own skill names the one case with no gate) |
| `mail-draft` | always — it signs with the user's `Tên` and `Vai trò` even when it opens no plan file; the role filter applies the moment it resolves a PIC code |
| `calendar` | once the run opens a plan file (a deadline pull or a `PIC → email` lookup) |
| `market-research`, `doc-compare`, `doc-translate`, `bid-review`, `candidate-review` | never — they read no plan file and show nobody's rows |

A skill that can reach a plan file is gated; nothing else exempts it.

Settle identity **before** opening a plan file, counting a task, printing a table or drafting mail.
Listing the folder to find the README is fine; nothing from the listing — filenames carry PM names —
is shown or used until identity is settled. Nothing about a plan file is read or shown while a fact is missing, and a
`Chuyên gia` has no rows until their PIC is settled. Do not get a head start on the file while waiting:
a report printed first cannot be un-shown when the role turns out to be wrong.

**The procedure is in `references/identity-intake.md`** — how to ask (role through the
structured-question tool, name and email as text), how a `Chuyên gia` is matched to a PIC code, how a
claimed `Project Manager` is verified against the filename. Read it only when there is a gap: a README
with all fields and an agreeing email answers the gate on its own. Once the answers are in and the
role has passed its check, restart the interrupted run from the beginning.

### What each role sees

Internal — decides what to print; never recite it to the user, least of all while asking the role.

| Role | Sees |
|---|---|
| `Project Manager` | every row of the files whose `Tên PM` matches their name |
| `Chuyên gia` | only rows where their code is `Người phụ trách` or `Người hỗ trợ` — `reminder` puts the `Người hỗ trợ` rows in a separate table, `project-report` keeps both in its four tables |

State the identity in use before printing, one line, so a wrong match shows at once:

```
Người dùng: Nguyễn Văn A (a.nguyen@example.com) | Vai trò: Chuyên gia | Mã PIC: Doox3
```

## When a file does not match a convention

A progress file outside the plan-file convention — a launch checklist, a tracker, a weekly report
(`20260826_Launch_Checklist_Standard_CIV_vf ENG.xlsx`) — is still read by `project-report` and
`project-update` under Doox rules, never by a generic spreadsheet skill. Differences:

- **Market and project — ask once**, in one structured question, when the file does not say; never
  guess from a filename with no separator.
- **Columns by meaning, not name**, in any of the three languages: task, owner, start and end dates,
  status text, and if present a checkbox, an issue and a next-step column. Use each sheet alone unless
  two are plainly a detail/control pair. **Required: task, status, end date** — missing one, ask.
  Report the mapping on one line per file.
- **Status mapped, mapping shown**: every distinct value to `Chưa triển khai` / `Đang triển khai` /
  `Hoàn thành`, printed on the column line; a value that fits none is asked about. Done = maps to
  `Hoàn thành` (and agrees with the checkbox if there is one). The file's own values are quoted in
  every table.
- **Row key**: the file's own ID/STT, else the sheet row (`R12`). A task row with no dates is a heading
  only when visibly one (bold, merged, numbered as a section); otherwise a task with a missing date,
  printed `-`.
- **Identity**: the gate still runs first. A file outside the convention **that the user attached in
  this session** is already theirs whole, so a verified identity sees every row of it. A plan file
  that follows the convention is filtered by role however it arrived, and so is every plan file used as
  a *source* for another file. A non-convention file found in the project folder is not opened — ask
  the user to attach it or rename it.
- **Output**: a layout the user names (Summary + Details sheets, a bilingual Word, a colour rule) is
  followed; the content rules do not bend. No layout named — the skill's own form.
- **Writing**: never in place; `project-update` writes a new copy.

## Say what was read

State the reading before acting on it, one line:

```
Thị trường: Bo Bien Nga | Dự án: Ke hoach khai truong taxi dien (từ tên file)
```

**The PM part of the filename stays out of that line, and out of everything printed before the user
is verified** — and so does the raw filename, which carries it. After a `Project Manager` has matched,
their own name is theirs to see; a `Chuyên gia` never needs it.
