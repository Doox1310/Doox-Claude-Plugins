# Identity intake — asking, matching a PIC, verifying a claimed PM

Read this **only when the README does not already answer who is running the session** — a missing
`## Người dùng`, a missing line inside it, a README whose `Email` disagrees with the signed-in
account, or a `Chuyên gia` with no `Mã PIC` yet. When all four fields are present and consistent,
`using-doox` alone is enough and this file is not read.

The gate itself, the schema and the role/visibility table live in `using-doox/SKILL.md`. This file is
only the procedure for filling the gap.

## How to ask — two steps, the same in every harness

Never a numbered list of questions in prose.

Step 1 — the role, always through the structured-question tool: `AskUserQuestion` in Claude Code and
Cowork, whatever the running harness calls its equivalent. The question is `Vai trò / chức vụ của bạn?`,
with exactly two options:

- `Project Manager`
- `Chuyên gia`

Do not type the two options out as text for the user to answer in a sentence. A role asked without a
picker is a bug. Wait for the pick before asking anything else.

Step 2 — name and email, only after the role came back, as plain text in exactly this wording and
nothing else:

```
Mình cần thêm một số thông tin sau:
  Họ và tên của bạn:
  Email của bạn:
Bạn vui lòng cung cấp thêm các thông tin trên để tiếp tục nhé.
```

**The role goes through the tool and the two names do not.** The tool carries no free-text field, so an
email asked through it comes back as a picked option instead of an address — that is why step 2 is text
and why the two steps are not merged into one call. Email is the field dropped most often; a run that
recorded a name and a role but no email is incomplete and asks again.

The role is a choice between exactly those two options — do not offer a third and do not infer it from
anything else. Include only what is missing. A README holding the name and email but no role is the
role question alone; one holding the role but no email is the text question alone, with just the
missing line.

**Not MCP elicitation.** A skill is markdown and has no tool that sends `elicitation/create`. A bundled
MCP server can send it, and one was built and tried — Cowork does not declare the `elicitation`
capability, so no form is rendered there and the server was dropped again. Claude Code CLI does declare
it. If a real form is ever wanted here, that is the piece to rebuild.

Do not carry on with a partial set. An answer that leaves a field blank is asked again, holding just
that field.

**Ask the questions bare.** One line may go before the form, and it is exactly this one:

```
Cho mình xin thông tin của bạn trước khi bắt đầu nhé
```

Nothing else — no explanation of why the information is needed, no mention of a missing README or of
a Doox convention, no line after the form telling the user to fill it in. Print no preamble, no
parenthetical, no footnote explaining what the answers are for:

- Never say the name will be checked against anything, never mention that the filename carries a PM
  name, never hint that a wrong name will be caught.
- Never describe what each role gets to see. "PM thấy toàn bộ, Chuyên gia chỉ thấy dòng của mình" is
  an instruction on which answer unlocks more.
- Never offer to look a PIC code up from a name or email at this point, and never list the codes
  found in the files.

A user who is told the name is verified against the file learns exactly which name to type, and the
check stops being a check.

Write the answers into the README, then carry on with the run that was interrupted.

## Matching the user to a PIC

The plan file names people in `Người phụ trách` / `Người hỗ trợ` by a short name — `Doox1`–`Doox10`,
`Qn1`–`Qn10`, `Thầu`, sometimes a real person's name. It is a name, not an opaque code, and it is
usually derivable from what the user just typed. For a role of `Chuyên gia`, **match it yourself
first; asking is the fallback, not the first move.**

Collect every distinct PIC value across all files, then try these in order, all comparisons ignoring
case, diacritics, spaces, dots and hyphens:

1. **Email local part** — the part before `@`. `doox1@gmail.com` → `doox1` → PIC `Doox1`.
2. **Email or name written beside the PIC** in the same cell, where the file carries one.
3. **The user's name** against the PIC value — both the full name and its last word
   (`Đỗ Hoàng Tùng` → `tung`).

**Every one of these requires the whole value to be equal, never a prefix.** `doox1` matches `Doox1`
and nothing else — `Doox10` is a different person, and a prefix match hands one specialist another's
rows.

Exactly one PIC matched — take it, record it as `Mã PIC` in the README, say nothing about how it was
found, and stop matching on later runs.

Two or more matched, or none did — ask, with a picker.

**The picker offers the likeliest candidates, not the whole list.** Rank by how close each PIC is to
the email local part and the name — shared prefix, shared digits, edit distance — and offer the top
few, plus the harness's own free-text escape. Only when nothing resembles the user at all does the
picker fall back to every PIC found in the files.

The question is bare: `PIC của bạn là gì?` — one question, the candidates ranked above as its options,
plus the harness's free-text escape. Do not explain why the automatic
match failed, do not
say the file carries no email or name beside the PIC, do not describe what was searched — that
narrates the file's structure and tells the user which answer would have worked.

Record the answer.

A `Project Manager` has no `Mã PIC` line and needs no match — but the claim itself gets checked, see
below.

This is the **session user's own** code. Looking up somebody else's address from a PIC code is a
different job and lives in `using-doox`, "The `PIC → email` directory".

## Verifying a claimed Project Manager

The real PM's name is in the filename, the third part of `[Thị trường] - [Tên dự án] - [Tên PM]`. A
user who answers `Project Manager` is checked against it before they are shown anything.

Compare their `Tên` with the `Tên PM` of the files they are asking about. Ignore case, ignore
diacritics, ignore repeated whitespace; require the rest to match. Matching one file grants the PM
view of that file only — a PM of the Bo Bien Nga market is not the PM of every market, so the
reminder covers just the files where the name matches.

**No match anywhere — refuse, and reveal nothing:**

> Tên bạn khai không khớp với PM của file kế hoạch. Vui lòng khai báo lại thông tin hoặc chọn lại vai
> trò.

**Never print, quote, hint at, or partially reveal the real PM name in this situation** — not the
name, not its initials, not its length, not "gần đúng", not a list of the PM names available to pick
from, not the filename that contains it. Someone who can guess names and read the failure messages
must learn nothing about which guess was closer. State only that the claim did not match.

Then ask again the same way the harness asks: in Cowork, one form holding the role and the name; in
chat, the role picker first — so the user can pick `Chuyên gia` instead — then the name line if they
stay on `Project Manager`. Do not proceed to a report, a reminder, or a draft in the meantime, and do not
fall back to showing a specialist's view of data they have not been matched to. A failed check that
still prints something is not a check.

Write nothing to the README until a check passes — a rejected claim must not be recorded as fact and
must not persist into the next run.
