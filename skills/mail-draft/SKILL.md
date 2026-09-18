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

**Never replace the material's data with model knowledge.** The date in the memo is the date, the
figure in the memo is the figure, the name in the memo is the name — carried across exactly, in any
language.

**Missing data is named, never filled.** A form section with nothing to put in it is dropped. A fact
the mail genuinely needs but the material does not carry — a deadline the user asked to state, a
number they asked to quote — is written `[cần bổ sung: …]` and listed after the draft. Never invent a
plausible value to make the form look complete. That is the single failure this skill exists to
prevent.

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

## 4. Fill the form

Read `assets/form-mail.md` and follow it — section order, subject line, sign-off. That file is the
form; this skill holds no copy of it. A user who edited it gets what they edited.

The sender's name and chức vụ for the sign-off come from the identity `using-doox` settles. Unknown
identity means asking the way `using-doox` asks, before drafting.

Section with no data → drop the whole section, heading included. Never leave an empty heading and
never write `(không có)` under one.

## 5. Output

**An Outlook draft, and the same content printed in the chat reply.** The printed copy is what the
user checks before clicking; the draft is what they click.

**Draft, never send.** Sending happens only when the user says so — `gửi đi`, `gửi mail này` and the
like — **in the same turn**. An instruction to send given earlier in the conversation does not carry
forward to a later draft: the request is per draft, and silence is not a request. A draft costs a
click; a mail already in someone's inbox cannot be recalled.

Then say what was created: the recipient, the subject, and the list of `[cần bổ sung: …]` gaps if
there are any.

**Microsoft only.** Outlook, not Gmail — as everywhere else in this plugin.

**No Outlook available in the harness?** Print the mail in the chat reply and say plainly that no
draft was created and the content is there to copy. Never fail silently, and never fall back to a
different mail provider.

## 6. One mail, not a batch

One request, one mail. Several recipients needing the same text get one draft each only when the user
asks for that; otherwise they go on the same mail. Fanning one memo out to every PIC in a plan file
is `reminder`'s job, not this one's.
