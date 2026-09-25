# The five document rules — `DR1` – `DR5`

These govern `doc-compare`, `doc-translate` and `bid-review` — every line those skills print.
They are the whole reason those skills exist: scoring and summarising need no instructions,
**not inventing** does.

`DR1` – `DR5` are stable rule IDs. A skill that cites one keeps the ID wherever it is quoted,
and renumbering a skill's own sections never renumbers a rule.

**DR1 — Never replace the document's data with model knowledge.** The price in the file is the price,
the model number in the file is the model number, even when a better-known figure exists. The user
asking to verify the document's own claims against public sources is `doc-compare` §7, run only on
that request; researching a market is `market-research`.

**DR2 — Missing data is named, never filled.** `Chưa có thông tin` when the document is silent,
`Chưa xác minh` when the document asserts something it does not evidence. Both are real answers.
A blank cell quietly filled with a plausible value is the failure these skills exist to prevent.

**DR3 — Names, codes and units pass through untouched.** Tên pháp lý, mã số thuế, mã hiệu, model,
số hiệu tiêu chuẩn, đơn vị đo — carried over exactly as written, in any language, including inside a
translation. `IEC 61851-1` stays `IEC 61851-1`. `Công ty TNHH …` is not translated into English and
not "corrected".

**DR3b — The reply's language is the user's; the document's language is the document's.** The plugin
is used in Vietnamese, English and French. Headings, labels and the skill's own sentences follow the
user's request; everything quoted from the document stays in the document's language, and a quoted
sentence that also needs a translation carries the original beside it, marked as a translation. Dates
print `dd/mm/yyyy` in all three. `doc-translate` is the one exception and only where the user asked:
it translates the body, and `DR3` still holds inside the translation.

**DR4 — Compare only within the same scope.** Two figures are comparable after they have been put on
the same basis: same hạng mục, same đơn vị tính, same khối lượng, same tax basis, same currency, same
inclusions. Anything that resists normalisation is reported as `Không so sánh được` with the reason —
never forced onto the table because the row needed a value.

**DR5 — Every finding names its source and position.** Which document, which page/sheet/mục/dòng. A
difference between two documents that does not say where each side came from cannot be checked by the
person who has to act on it.
