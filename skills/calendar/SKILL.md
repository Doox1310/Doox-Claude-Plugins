---
name: calendar
description: Đặt lịch hẹn, xếp lịch tránh trùng và tổng hợp thời gian biểu trên Google Calendar — từ điều user nói, từ memo, hoặc từ deadline trong plan file. Use when the user asks to đặt lịch, tạo lịch họp, xếp lịch, dời lịch, or asks lịch tuần này/hôm nay có gì. Confirms every event before creating it. Load `using-doox` first.
---

# Calendar

**Load `using-doox` first** — it routes the request, settles who is running this, and holds the plan-file rules this skill relies on.

## Hard limits

On top of `using-doox` "Hard limits":

- **No create, move or cancel without a yes in this turn, per event.** An event with attendees fires
  invitations the moment it exists, so a wrong time or guest list is already in other inboxes. An
  approval for one event, or from an earlier turn, does not cover the next.
- **Attendee addresses only from the user or `using-doox` "The `PIC → email` directory".** A code with
  no address → ask; a guessed address is a meeting request in a stranger's inbox. `Thầu` is never an
  attendee.
- **Only the user's own calendar is written.** Other people get invitations, never entries, even when
  the connector would allow it.
- **Identity gate once a plan file is opened** — a deadline pull or a PIC lookup ("Who is running
  this"), and only the rows that role may see.
- **Nothing invented.** No duration nobody stated, no attendee because they were on a similar meeting,
  no guessed địa điểm — ask. A start time alone ("2h chiều") says nothing about the end; the one
  exception is a clear duration given ("họp 30 phút lúc 2h").

## 1. When to use

| Request | Section |
|---|---|
| đặt lịch hẹn, tạo cuộc họp, dời/huỷ một lịch đã có | §3 |
| xếp lịch cho nhiều việc, tìm giờ trống, tránh trùng | §4 |
| lịch tuần này có gì, tổng hợp thời gian biểu | §5 |

A plan-file deadline becomes a calendar block only when the user asks — never automatically
(`reminder` is the one that tells the team what is due).

**Google Calendar**, through the connector linked to Cowork — the one non-Microsoft piece of the
plugin; say nothing about that to the user. No connector → say so and print what would have been
created; never fall back to another calendar.

## 2. Time and date

Default to the user's local timezone unless they name another. A time with no date is today if it
has not passed, tomorrow if it has; a relative date ("thứ 5 tuần sau") is resolved to `dd/mm/yyyy`.
Either way, **state the reading** so a wrong one shows before anything is booked.

## 3. Creating, moving, cancelling

Print what is about to happen — tiêu đề, bắt đầu và kết thúc, người tham dự, địa điểm / link — and
wait for the yes (hard limits). **Dời và huỷ read before they write**: find the event, print it as it
stands, say what changes, then ask. Two events match → ask which, never pick the nearer one.

## 4. Xếp lịch — finding the slot

Read the existing calendar for the window **first**, then propose: each việc, the suggested slot,
and why. Name conflicts with what is already there rather than silently working around them. Propose,
do not book — the user will move things, and nothing is written until they accept.

Priority comes from the user or the file's deadline, never from this skill: two things colliding with
no stated priority → show the collision and ask. Deadlines pulled from a plan file are read per
`using-doox` "Reading a plan file", only from the files and rows the user pointed at.

## 5. Tổng hợp thời gian biểu

Read-only. Print the window asked for as a table — ngày, giờ, việc, người tham dự, địa điểm —
grouped by day, in time order. An empty window is a real answer: "tuần này lịch trống". Plan-file
deadlines appear only if the user asked for them, and then each line is marked calendar or plan file
— the user acts on the difference.

## 6. Output

The chat reply. After a create, echo the event title and time so the user sees what landed. Nothing
here writes to a plan file, a README or any document — a calendar change is not a plan change.
