---
name: mail-draft
description: Draft one Outlook mail from what the user hands over — a memo pasted into the chat, a file, or data already on screen — filled into the saved form, recipient resolved from the request, the memo or the plan files. Use when the user asks to soạn mail, viết mail, draft mail or gửi mail về a subject. Never sends without being told to in the same turn.
---

# Mail Draft

## 1. When to use

The user hands over material — a memo pasted into the chat, a file, a report this session already
produced — and asks for a mail to be written from it.

Not the daily reminder: `reminder` already writes that mail, on its own schedule, with its own
tables. A user asking "nhắc việc hôm nay" gets `reminder`, not this skill. Not a research errand
either — this skill never goes out to look anything up. What is in the material is what goes in the
mail.

Any role may use it. Unlike `reminder`, this mail is the user's own, not one sent on behalf of the
whole team, so there is no `Project Manager` gate.

## 2. Input

Whatever the user supplied in this session: pasted text, an attached file, or the output of an
earlier skill in the same conversation. Read it whole before drafting.

**Extract, do not re-ask.** From the request and the material, settle in one pass: what the mail is
for, who reads it, the scope (thị trường / dự án), the evidence cutoff, the deadline being asked
about, the language and the output format. Ask only about a gap that changes the mail — a question
whose answer is already in the memo is a turn spent for nothing.

**Never replace the material's data with model knowledge.** The date in the memo is the date, the
figure in the memo is the figure, the name in the memo is the name — carried across exactly, in any
language.

**Missing data is named, never filled.** A form section with nothing to put in it is dropped. A fact
the mail genuinely needs but the material does not carry — a deadline the user asked to state, a
number they asked to quote — is written `[INPUT NEEDED: <field>]`, in every language, and listed
after the draft. Never invent a plausible value to make the form look complete. That is the single
failure this skill exists to prevent.

**Missing is not zero.** An absent figure is not nought, an absent status is not `Hoàn thành`, an
absent approval is not approval, and silence from an approver is not agreement. Each of those stays
an unknown with its name written out.

**Dates carry their basis.** `as_of` is the cutoff of the material, not automatically today. Keep a
baseline date and a revised date apart, and never resolve a vague `cuối tuần` or `end of day` into a
calendar date the material does not support — that is an `[INPUT NEEDED: …]`.

## 3. Recipient

Three sources, in this order:

1. **The user named it in the request** — an address, or a person. Takes precedence over everything.
2. **The material names it** — an address or a name written in the memo or file.
3. **A PIC code resolved against the plan files** — the user says "gửi cho Doox3". Build the
   `code → email` directory per `using-doox`, section "The `PIC → email` directory": scan every row
   of every plan file in the Cowork project folder, collect each pair, handle all four separators
   (newline, en dash `–` U+2013, parentheses, bare space). `Thầu` is a contractor and has no
   personal address.

Two sources disagreeing is not resolved by picking one — **ask**. A source producing nothing is not a
failure: the draft is still written, with the recipient left empty and that said plainly after it.

**Never guess an address.** Not from a name, not from a pattern seen in other addresses, not from the
domain of a colleague's.

A recipient who resolved to nothing but a PIC code is addressed by that code — `Kính gửi anh/chị
Doox3`. The code is what the plan file calls them; inventing a personal name to make the salutation
read better puts a person who does not exist at the top of the mail.

## 4. Pick the form

**Read `assets/form-mail.md` before writing a line of the mail.** It holds the selection table, the
five forms and the context rules; this skill holds no copy of any of it, so a user who edited that
file gets what they edited.

Pick **one** form by the result the sender needs, never by topic, by the recipient's job title or by
a reporting cadence — a weekly update and a monthly one are the same form:

| The sender needs | Form |
|---|---|
| thông báo, cập nhật kết quả, chia sẻ thông tin, báo mốc đã đạt | EX1 |
| xin phê duyệt, xin chọn phương án, xin đổi baseline | EX2 |
| báo rủi ro/sự cố nghiêm trọng, xin can thiệp gấp | EX3 |
| nhờ một bộ phận/thị trường khác làm một đầu việc cụ thể | EX4 |
| chốt biên bản họp, báo tiến độ một cam kết đã có | EX5 |

An active incident needing intervention takes EX3 over everything else. Otherwise: EX2 → EX4 → EX5 →
EX1. Material fitting no row uses the closest intent and says what was assumed, in the note after the
draft — it never becomes a second mail (§7).

Then read the one `90_Context_Rules` row matching the situation — họp, escalation, mua sắm, sự cố,
tài chính, nhân sự and so on. That row adds checks to the form already chosen; it never selects a
different form and never adds a second one.

## 5. Fill the form

The frame is set by who reads the mail (`assets/form-mail.md`, "Chọn khung"):

- **CEO / leadership, or anyone outside the company** — the chosen EX form's `template_subject`,
  `template_opening`, `template_body` and `template_closing`, exactly, in the recipient's language.
- **Internal project mail in Vietnamese, between project members** — the **form nhà** (4 numbered
  sections, subject `[Chủ đề] — [Thị trường / Dự án]`). It exists in Vietnamese only.
- **Anything else** — internal mail in another language, or a memo/chat format the user asked for —
  the EX `template_*` fields.

Whatever the frame, the chosen EX form decides the content: its `reasoning` is the order the argument
is made in, its `core_output` is what must survive any shortening, its `missing_data` says which gap
may not be hidden, and its `boundary` says what the mail is not allowed to claim.

Section with no data → drop the whole section, heading included. Never leave an empty heading and
never write `(không có)` under one.

**The mail is written in the recipient's language, the chat reply in the user's** — `using-doox`,
"Language" — pick it by the recipient, not by the language the user is typing in. The gap marker is
`[INPUT NEEDED: <field>]` in every language. The EX `template_*` fields are written in English because
they are the frame, not the output language — translate them as they are filled. Figures, names,
codes, units and quoted sentences cross into the mail untouched whatever the language, and dates print
`dd/mm/yyyy` in every language. Recipient's language unknown: use the language of the
thread being answered, then the user's, and say which was assumed.

Form IDs and field keys — `EX2`, `core_output`, `template_body` — are internal. They never appear in
the mail or in the chat copy of it.

The sender's name and chức vụ for the sign-off come from the identity `using-doox` settles. Unknown
identity means asking the way `using-doox` asks, before drafting.

Three claims the draft may never make on its own:

- **Authority.** A request is not an approval, and a draft does not grant one. Keep budget approval,
  vendor award, signature, permit and acceptance as separate states — the mail asks for one of them,
  it does not record it as done.
- **Attachments.** A file the user handed over is not automatically attached to the outgoing mail.
  Write `đính kèm` only when the attachment is actually on the draft; otherwise name the document in
  the body or drop the sentence.
- **Commitments.** An owner or a date the material marks as proposed stays proposed in the mail. Never
  turn a suggestion into a commitment to make a sentence read cleanly.

Length follows the chosen form's `default_length` unless the user asked for something else — roughly
150–250 words for an update, 180–300 for a decision request, 100–200 for a first alert, 120–220 for a
support request, 120–250 for a record or follow-up.

## 6. Output

**An Outlook draft, and the same content printed in the chat reply.** The printed copy is what the
user checks before clicking; the draft is what they click.

**Draft, never send.** Sending happens only when the user says so — `gửi đi`, `gửi mail này` and the
like — **in the same turn**. An instruction to send given earlier in the conversation does not carry
forward to a later draft: the request is per draft, and silence is not a request. A draft costs a
click; a mail already in someone's inbox cannot be recalled.

**A finished draft and a review draft are said apart.** A mail with no gap marker left in it
(`[INPUT NEEDED: …]`) is finished. A mail still carrying one is a review draft: say so, and keep the
gap list outside the mail body so nothing meant for the user leaves in the message itself. Verified uncertainty that
belongs to the situation — `nguyên nhân đang được xác minh` — is not a gap and stays in the mail.

Before returning, check the draft against its own inputs: the opening answers what the user asked
for, every figure and date matches the material, each material gap is still visible, and no
`{{placeholder}}` or assembly note survived into the text.

Then say what was created: the recipient, the subject, the form used, and the list of
`[INPUT NEEDED: …]` gaps if there are any.

**Microsoft only.** Outlook, not Gmail — as everywhere else in this plugin.

**No Outlook available in the harness?** Print the mail in the chat reply and say plainly that no
draft was created and the content is there to copy. Never fail silently, and never fall back to a
different mail provider.

## 7. One mail, not a batch

One request, one mail, one form. Several recipients needing the same text get one draft each only when
the user asks for that; otherwise they go on the same mail. Fanning one memo out to every PIC in a
plan file is `reminder`'s job, not this one's.

Two intents in one memo — an update and an approval request — is still one mail: pick the dominant
intent by the precedence in §4 and carry the rest as context. Split into two drafts only when the user
asks, or when two audiences may not see the same content.

This skill communicates; it does not research and it does not analyse. An external question the mail
needs answered goes to `market-research` first, and a report the mail is meant to carry is produced by
`project-report` first. Run only the stage the user asked for, and keep the figures, the cutoff and
the wording of a decision identical across whatever stages did run.
