---
name: reminder
description: "Read EVERY market's plan file in the project folder and produce the daily reminder — only the rows that are overdue, due within 3 days, or starting today — as the PM's full table or a specialist's own tasks, plus one Outlook draft per PIC on a PM run. Use when the user asks what has to be handled today, asks to nhắc việc or remind the PICs, or the scheduled morning run fires. NOT a full progress report of one market (that is `project-report`). Load `using-doox` first — it holds the identity gate and the file-reading rules this skill depends on."
---

# Reminder

**Load `using-doox` first** — it routes the request, settles who is running this, and holds the plan-file rules this skill relies on.

## Hard limits

On top of `using-doox`, "Hard limits":

- **Identity gate before any file.** Nothing from a plan file is read until `using-doox`, "Who is
  running this" is settled. A run then prints one view only: a `Project Manager` sees mục 2, a
  `Chuyên gia` sees mục 1 (§6) — never the other's, never another code's rows.
- **Read-only.** Never writes to a plan file (§8).
- **Chat only.** No `.docx`, `.md`, `.pdf` or `.xlsx`, and none offered.
- **Draft, never send** (§7) — including the unattended 9am run. Send only when the PM asks in that
  turn, and only the drafts already built. A `Chuyên gia` run writes no mail at all.
- **No invented addresses.** An email comes only from the plan files (§5); `Thầu` and a code with no
  address get no mail.
- **Always print**, even when nothing is due (§6).
- **Done is exact** — checkbox TRUE *and* text `Hoàn thành`, per `using-doox`, "Reading a plan file".

## 1. When to use

The user asks what has to be handled today, asks to remind the PICs, or the 9am run fires.

The 9am schedule is the harness's (Cowork), not this plugin's — `plugin.json` declares no hook, cron
or command, so installed anywhere else the skill runs only when asked. If a user expects a morning
mail that never came, say so: the skill was never fired, it did not fail.

## 2. Input

Every plan file in the project folder, not one. After identity is settled (`using-doox`, "Who is
running this"), take each spreadsheet named per `using-doox`, "Plan file naming" (lock files
ignored); the market from each name fills the `Thị trường` column so every row traces to its file.

A `Project Manager` run covers only files whose `Tên PM` matches them; a `Chuyên gia` run covers
every file, filtered to their own rows. A file outside the convention is neither skipped silently nor
guessed at — ask about it (`using-doox`, "When a file does not match a convention") and carry on with
the rest.

## 3. Reading a plan file

Per `using-doox`, "Reading a plan file", including the one column-mapping line per file before
anything is printed. Build STT even though the reminder does not print it — it is the only key when
the user asks about a row.

## 4. Which tasks appear

A task appears when it is **not done** and fits one case, tested in this order — first match wins,
so a row sits in exactly one table and is never counted twice:

| Case | Condition |
|---|---|
| Quá hạn | Ngày kết thúc < today |
| Sắp đến hạn | today ≤ Ngày kết thúc ≤ today+3 |
| Bắt đầu hôm nay | Ngày bắt đầu = today |

Nothing else — a task mid-way and due next month would repeat every morning and train the reader to
stop opening the mail. The 3-day threshold is the customer's (`idea.txt`: `ngày hoàn thành - 3 ngày`).

Default order inside a case: `Ngày kết thúc` ascending, then `Thị trường`, because the nearest
deadline is what the reader acts on first.

## 5. PIC codes and their emails

PM runs only — skip on a `Chuyên gia` run. Build the directory per `using-doox`, "The `PIC → email`
directory". Then:

- `Thầu` rows appear in the PM table and get no mail. A `Chuyên gia` sees a `Thầu` row only when their
  own code supports it.
- A code with no email keeps its rows in the PM table, gets no draft, and is listed after the report
  so the user can fill the address in.

## 6. Output

The chat reply is the report: every row, every column, each cell whole (only newlines inside a cell
collapsed), empty cell `-`, dates `dd/mm/yyyy`.

Print the identity line, then the opening line exactly (in the reply's language — see "Labels in
English and French" below):

```
Các công việc cần xử lý trong ngày:
```

Then the tables, with **no section heading** — `1. Đối với PIC:` / `2. Đối với PM:` are not printed;
a run shows one view and a lone `2.` only advertises the one they did not get. `Mục 1` / `mục 2` are
names used in this file only.

- `Project Manager` — **mục 2 only**: one six-column table of every due row of their files, `Thầu`
  included. No per-PIC tables.
- `Chuyên gia` — **mục 1 only**: their own rows (`Người phụ trách`), then a table headed `Hỗ trợ` for
  rows where they are `Người hỗ trợ`.

**Three tables, one per case, never merged**, headings written exactly (reply's language), in this
order:

```
Quá hạn:
Sắp đến hạn (trong 3 ngày):
Bắt đầu hôm nay:
```

An empty case still prints its heading and `_(không có)_` — an empty `Quá hạn` is what the reader most
wants to see, and a missing heading reads as a run that forgot it. Nothing due at all still prints the
opening line and the three empty headings: the 9am run is unattended and Cowork reports no failure,
so silence must mean the run broke. Inside `Hỗ trợ`, empty cases are dropped, and an empty `Hỗ trợ`
is dropped whole.

Mục 1, five columns (no `PIC` — every row is the specialist's own):

| Thị trường | Danh mục công việc | Timeline | Ghi chú | Trạng thái |
|---|---|---|---|---|

Mục 2, six columns, `PIC` third:

| Thị trường | Danh mục công việc | PIC | Timeline | Ghi chú | Trạng thái |
|---|---|---|---|---|---|

`Timeline` = `Ngày bắt đầu – Ngày kết thúc`, a missing side `-`. `Trạng thái` is the text column as
written. `Ghi chú` is empty on most rows — `-`, never invented. No other plan-file column is part of
the reminder.

After mục 2: the codes with no email, if any. A specialist sees only their own address status.

### Labels in English and French

The reply follows the user's language (`using-doox`, "Language"); the unattended 9am run has no
request to read it from, so it uses the plan files' language. Only these labels change — tables,
order and cases do not:

| vi | en | fr |
|---|---|---|
| `Các công việc cần xử lý trong ngày:` | `Tasks to handle today:` | `Tâches à traiter aujourd'hui :` |
| `Quá hạn:` | `Overdue:` | `En retard :` |
| `Sắp đến hạn (trong 3 ngày):` | `Due soon (within 3 days):` | `Échéance proche (sous 3 jours) :` |
| `Bắt đầu hôm nay:` | `Starting today:` | `Commence aujourd'hui :` |
| `Hỗ trợ` | `Supporting` | `En appui` |
| `_(không có)_` | `_(none)_` | `_(aucune)_` |

Column headers: `Thị trường` / `Market` / `Marché`, `Danh mục công việc` / `Task` / `Tâche`, `PIC`,
`Timeline` / `Timeline` / `Calendrier`, `Ghi chú` / `Notes` / `Remarques`, `Trạng thái` / `Status` /
`Statut`. Every cell stays as the file wrote it (`Đang triển khai` is quoted, not translated) — say so
in one line above the report when the languages differ.

## 7. Mail

**`Project Manager` runs only.** One Outlook **draft** per code that has an email and at least one due
row: to that address, subject `Nhắc việc [dd/mm/yyyy]` / `Task reminder [dd/mm/yyyy]` / `Rappel des tâches
[dd/mm/yyyy]`, body that code's rows in the mục 1 layout split into the three case tables, empty cases
dropped. Each draft is in the recipient's language, with the labels above; unknown — the user's
(`using-doox`, "Language"). No draft for the mục 2 table, for `Thầu`, or
for a code with no address.

**Stop at the drafts** — a draft costs a click, a wrong mail in a PIC's inbox cannot be recalled.
Send only when the PM asks in the same turn (`gửi đi`, `gửi mail cho PIC`): send the drafts already
built, nothing re-read, no new recipient. A send instruction from an earlier turn or run does not
carry over; silence is not a request.

**A `Chuyên gia` run writes no mail** — none to the team, none to themselves, none offered; a request
to send is refused, because mail on this project goes out from the PM.

After the report, say how many drafts were created and to which addresses; after a send, what went
out and to whom.

## 8. Boundaries

**`project-update` is the only skill that writes to a plan file; `reminder` never does.** A cell that
looks wrong is reported, and the fix goes through `project-update` with its confirmation. The only
file this skill writes is the project README (`using-doox`, "The project README").
