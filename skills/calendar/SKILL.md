---
name: calendar
description: Đặt lịch hẹn, xếp lịch tránh trùng và tổng hợp thời gian biểu trên Google Calendar — từ điều user nói, từ memo, hoặc từ deadline trong plan file. Use when the user asks to đặt lịch, tạo lịch họp, xếp lịch, dời lịch, or asks lịch tuần này/hôm nay có gì. Confirms every event before creating it.
---

# Calendar

## 1. When to use

Three requests, one skill:

| Request | Section |
|---|---|
| đặt lịch hẹn, tạo cuộc họp, dời/huỷ một lịch đã có | §3 |
| xếp lịch cho nhiều việc, tìm giờ trống, tránh trùng | §4 |
| lịch tuần này có gì, tổng hợp thời gian biểu | §5 |

Not `reminder`: that one reads plan files and tells the team what is due today. This one touches the
calendar itself. The two do meet — a deadline in a plan file can become a calendar block — but only
when the user asks for it, never automatically.

**Google Calendar**, through the connector already linked to Cowork. This is the one place in the
plugin that is not Microsoft; it is a tạm thời arrangement and the skill says nothing about it to the
user either way. No connector available → say so plainly and print what would have been created.
Never fall back to another calendar.

## 2. Before anything: what timezone, whose calendar

Every time written or read is in the user's local timezone unless they say otherwise. A time with no
date is **today** if it has not passed, tomorrow if it has — and that reading is stated out loud when
it is used, never assumed silently.

The calendar written to is the user's own. Never another person's calendar, even when their address
is known and the connector would allow it — other people get **invitations**, not entries.

## 3. Creating, moving, cancelling

**Confirm before writing. Every time.**

Print what is about to happen — tiêu đề, ngày giờ bắt đầu và kết thúc, người tham dự, địa điểm /
link — and wait for the user to say yes. Then create it. An event with attendees fires invitations
the moment it exists; a wrong time or a wrong guest list has already reached other people's inboxes
by the time anyone notices. This is the same rule as `mail-draft` and `reminder`: **soạn sẵn, người
gật mới bắn đi.**

The confirmation is per event and per turn. A user who approved one event has not approved the next
one, and an approval from an earlier turn does not carry forward.

Missing details are asked for, not filled in. No default duration invented for a meeting whose length
nobody stated, no attendee added because they were on a similar meeting before, no địa điểm guessed.
The one exception: an end time missing where the user gave a clear duration ("họp 30 phút lúc 2h").

A start time with no duration and no end time is the ordinary case of that rule, not a gap in it —
"2h chiều" says when it begins and nothing about when it ends. Ask; do not reach for an hour because
an hour is what meetings usually are.

**An attendee named by PIC code needs a real address, and this skill has no way to invent one.**
Build the `code → email` directory per `using-doox`, section "The `PIC → email` directory" — scan
every row of every plan file in the project folder, handle all four separators — and use what it
returns. Nothing returned means asking the user for the address: an invitation fires the moment the
event exists, so a guessed address is a meeting request in a stranger's inbox. `Thầu` is a contractor
and has no personal address at all.

Reading the directory opens plan files, so it puts the identity gate back on for that run — the same
condition as pulling deadlines out of a plan file (§4).

**Dời và huỷ read before they write.** Find the event, print it as it stands now, say what will change,
then ask. Two events match the description → ask which, never pick the nearer one.

## 4. Xếp lịch — finding the slot

The user hands over several things to be scheduled — from what they typed, from a memo, or from
deadlines in a plan file — and asks for them to be laid out.

Read the existing calendar for the window in question **first**. Then propose an arrangement:
each việc, the slot suggested, and why that slot. Conflicts with what is already there are named,
not silently worked around.

Nothing is written until the user accepts the arrangement. They will move things; propose, do not
book.

**What this skill does not decide:** which việc matters more. Priority comes from the user or from the
deadline in the file. Two things genuinely colliding with no stated priority → present the collision
and ask. Never rank someone's work for them.

Pulling từ plan file: per `using-doox` — the filename convention, the two-sheet join, which field is
the deadline. Only the files and rows the user pointed at.

## 5. Tổng hợp thời gian biểu

Read the window asked for — today, this week, a named range — and print it as a table: ngày, giờ,
việc, người tham dự, địa điểm. Grouped by day, in time order.

Read-only. A request to see the week is not a request to change it, and this section creates nothing.

Nothing in the window is a real answer: "tuần này lịch trống". Never pad it with the plan file's
deadlines unless the user asked for those too — and when they did, mark which lines came from the
calendar and which from a plan file. The two are not the same thing and the user is about to act on
the difference.

## 6. Output

The chat reply. Every section prints what it found or what it created — after a create, say the
event title and its time back, so the user can see what landed without opening the calendar.

Nothing here writes to a plan file, a README, or any document. `project-update` is the only skill that
writes to a plan file, and a calendar change is not a plan change.
