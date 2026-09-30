---
name: mail-draft
description: Draft one Outlook mail from what the user hands over — a memo pasted into the chat, a file, or data already on screen — filled into the saved form, recipient resolved from the request, the memo or the plan files. Use when the user asks to soạn mail, viết mail, draft mail or gửi mail về a subject. Never sends without being told to in the same turn. Load `using-doox` first.
---

# Mail Draft

**Load `using-doox` first** — it routes the request, settles who is running this, and holds the plan-file rules this skill relies on.

## Hard limits

On top of `using-doox` "Hard limits":

- **Draft, never send**, unless the user says `gửi đi` / `gửi mail này` or the like **in this turn**. An
  earlier instruction does not carry forward to a later draft — a mail in someone's inbox cannot be
  recalled.
- **Identity before drafting.** The sign-off uses `Tên` and `Vai trò` from "Who is running this", so
  the gate runs even when no plan file is opened; the role filter ("What each role sees") applies the
  moment a PIC code is resolved.
- **Addresses are never guessed** — not from a name, a pattern or a colleague's domain (§3).
- **The mail is in the recipient's language**, the chat reply in the user's ("Language"); recipient's
  language unknown → the fallback there, and say which was assumed.
- **Customer forms as defined.** For CEO / leadership / anyone outside the company, the chosen EX
  form's `template_subject`, `template_opening`, `template_body`, `template_closing` are followed
  exactly (translated into the recipient's language, structure and order kept). The EX library in
  `assets/form-mail.md` is the customer's; its fields decide the content of every mail (§5).
- **Never invent data.** Figures, dates and names cross from the material exactly. A fact the user
  asked the mail to state that the material lacks is `[INPUT NEEDED: <field>]`, in every language —
  a plausible invented value is the failure this skill exists to prevent.

## 1. When to use

The user hands over material — pasted text, a file, a report produced earlier in the session — and
asks for a mail from it. Any role may use it: the mail is the user's own, so there is no
`Project Manager` gate. Routing against `reminder` is in `using-doox` "Routing". This skill never looks
anything up; what is in the material is what goes in the mail.

## 2. Input

Read the material whole, then **extract, do not re-ask**: purpose, reader, scope (thị trường / dự án),
evidence cutoff, deadline, language, output format. Ask only about a gap that changes the mail.

- **Missing is named, never filled.** A form section with no data is dropped. A fact the user asked
  to state but the material lacks is `[INPUT NEEDED: <field>]`, listed after the draft.
- **Missing is not zero** — an absent figure is not nought, an absent status is not `Hoàn thành`,
  silence from an approver is not agreement.
- **Dates carry their basis.** `as_of` is the material's cutoff, not automatically today; keep
  baseline and revised dates apart; a vague `cuối tuần` / `end of day` the material does not pin
  down is `[INPUT NEEDED: …]`.

## 3. Recipient

In order: (1) named by the user in the request, (2) named in the material, (3) a PIC code resolved
through `using-doox` "The `PIC → email` directory". Two sources disagreeing → ask, do not pick. Nothing
found → the draft is still written, recipient empty, said plainly after it. `Thầu` gets no mail.

A recipient known only by PIC code is addressed by that code (`Kính gửi anh/chị Doox3`) — an invented
personal name puts a person who does not exist at the top of the mail.

## 4. Pick the form

**Read `assets/form-mail.md` before writing** — the selection table, the five EX forms and the
`90_Context_Rules` live there, not here, so a user who edited that file gets what they edited.

Pick **one** form by the result the sender needs (not by topic, job title or cadence), with the
library's precedence: an active incident needing intervention is EX3; otherwise EX2 → EX4 → EX5 → EX1.
Material fitting no row takes the closest intent and says what was assumed after the draft. Then read
the one context-rule row matching the situation; it adds checks to the chosen form, never a second
form.

## 5. Fill the form

**Frame** ("Chọn khung" in the asset): CEO / leadership / external → the EX `template_*` fields (hard
limit above). Internal project mail in Vietnamese → the **form nhà** by default, because the team
reads that layout fastest; use the EX template instead when the user asks or the case calls for it,
and say why. Anything else (internal in another language, a memo/chat format asked for) → the EX
`template_*` fields.

**Content**, whatever the frame, comes from the chosen EX form: `reasoning` is the argument's order,
`core_output` must survive any shortening, `missing_data` names the gap that may not be hidden,
`boundary` what the mail may not claim. Three claims the draft never makes on its own:

- **Authority** — a request is not an approval; budget approval, vendor award, signature, permit and
  acceptance stay separate states.
- **Attachments** — write `đính kèm` only when the file is actually on the draft.
- **Commitments** — a proposed owner or date stays proposed.

Drop a section with no data, heading included — never an empty heading or `(không có)`. Form IDs and
field keys (`EX2`, `core_output`) never appear in the mail. Length: the form's `default_length` unless
the user asked otherwise.

## 6. Output

**An Outlook draft, and the same text in the chat** — the copy is what the user checks, the draft is
what they click. Outlook only, never another provider. No Outlook in the harness → print the mail,
say plainly no draft was created.

A mail still carrying `[INPUT NEEDED: …]` is a **review draft** — say so, and keep the gap list
outside the mail body. Verified uncertainty (`nguyên nhân đang được xác minh`) is not a gap and stays
in.

Before returning, check the draft against its inputs: the opening answers the request, figures and
dates match the material, gaps are visible, no `{{placeholder}}` or assembly note survived. Then say:
recipient, subject, form used, gap list.

## 7. One mail, not a batch

Default one request → one mail → one form, because fanning one memo out to every PIC is `reminder`'s
job. Several recipients go on the same mail unless the user asks for one each. Two intents in one memo
→ the dominant one by §4's precedence, the rest as context; split only when asked or when two
audiences may not see the same content. A mail that needs research or a report first follows
`using-doox` "Chains"; keep figures, cutoff and decision wording identical across the stages.
