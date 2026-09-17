# Final audit

`SKILL.md` §12. Read once, after the last block is written and before the reply.

Blocks were already audited as they were written (§11), so this pass covers only what a single block cannot see. Run it against the runtime ledger and the blocks written in this run; do not re-read the whole workbook to perform it.

## A. Framework coverage

Coverage is checked **ledger-side**, not by re-reading the file. The denominator is `wb.py cells` (§3) — the writable set, already computed at the split — and the §4 split opened one ledger row per claim against it. So:

- no ledger row is still `state=open` — an open row is an unfilled cell, whether or not anyone looked at it;
- every coordinate in the `cells` output appears in some ledger row's `output cell(s)`, and every one of those rows was included in a `write` batch that succeeded;
- `origin` and `state` agree on every row (§9): `gap`→`Chưa xác minh`, `estimate`→`Ước tính`, `fetch`/`cache`→ a source URL present;
- every required report cell therefore holds evidence, an estimate, `Chưa xác minh`, or `Không áp dụng`.

Then confirm, without a full re-read:

- no original instruction placeholder remains in a writable report cell;
- no cell outside the `cells` set was written — column A labels, block titles and column headers are intact, and `B47`/`B51` still carry their conclusion-block field lists;
- prose cells carry the framework's full field list (§11), `Giới hạn` and the closing action included, one field per line rather than one paragraph.

A cell whose block was skipped or interrupted is a coverage failure — fill it with a named gap rather than leaving it blank.

## B. Cross-block consistency

- The same metric stated in two blocks agrees, or the difference is explained.
- A lower-level count does not exceed its parent total in another block without an explained definition difference.
- Scope, unit, period and currency basis stay consistent where blocks reference each other.

## C. Conclusion lineage

Every conclusion row draws only on rows already populated above, introduces no new factual claim, and carries no stronger status than the weakest material premise beneath it.

## D. Adversarial audit of decision-grade claims

Applies to decision-grade claims and to the conclusions — not to every claim in the report. Try to disprove them:

- Is a source merely reputable but wrong authority for the claim?
- Is a current page carrying stale data?
- Is a cached record being reported as current because the cache said `FRESH`, when `FRESH` only means the page need not be re-opened?
- Is a secondary source being mistaken for the original evidence?
- Is a first-party licence/project claim being treated as independently verified?
- Is a charger rating being mistaken for vehicle acceptance, or a rider/fee for the underlying commodity price?
- Is a legal rule/version generalized beyond its conditions or no longer effective?
- Is any conclusion stronger than the evidence below it?

Fix the claim or expose the limitation before delivery.

## E. Contractor-list audit

Only when the objective includes contractor selection. Run audit E as written in `contractor-enumeration.md`. It is short by design — running out of budget is a reason to ship the workbook with named gaps, never a reason to skip it.

## F. Competitor-comparison audit

Only when the objective includes `competitor/CPO`. Check before printing:

- every D1–D10 row is measured on the same basis for both sides, or the cell says `Không so sánh được` with the reason (§7.4a);
- every scale figure carries its state — `Đang vận hành` / `Đang xây` / `Đã công bố` — and the comparison ran on the operating column only (§7.4b);
- every scale figure carries an as-of date, pulled to the data-lock date or with the gap stated;
- **no "mình hơn" line rests on a competitor cell that is empty** (§7.5) — those belong in `Chưa kết luận được`;
- every competitor sits in exactly one bucket, and the set was segmented before it was ranked;
- C1–C3 were worked or recorded as unavailable;
- no D1 value came from a CPO's own superlative wording;
- no competitor cost, margin or utilisation appears as a fact;
- the own-side row is sourced from the user/documents, never from model knowledge (§7.1);
- the section recommends nothing (§7.7).
