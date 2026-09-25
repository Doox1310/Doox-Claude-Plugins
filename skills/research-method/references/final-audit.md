# Final audit

`research-method` §13. Read once, after the last block is written and before the reply.

Blocks were already audited as they were written (`market-research` §12; an RX answer is audited
against its form's `review_check`), so this pass covers only what a single block cannot see. Run it
against the runtime ledger and the blocks written in this run; do not re-read the whole workbook to
perform it.

## A. Framework coverage

Coverage is checked **ledger-side**, not by re-reading the file. For the workbook the denominator is
`wb.py cells` (`market-research` §3) — the writable set, already computed at the split — and the §4
split opened one ledger row per claim against it; for an RX answer it is the form's required parts.
So:

- no ledger row is still `state=open` — an open row is an unfilled cell, whether or not anyone looked
  at it;
- every coordinate in the `cells` output appears in some ledger row's `output cell(s)`, and every one
  of those rows was included in a `write` batch that succeeded;
- `origin` and `state` agree on every row (§10): `gap`→`Chưa xác minh`, `estimate`→`Ước tính`,
  `fetch`/`cache`→ a source URL present;
- every required report cell therefore holds evidence, an estimate, `Chưa xác minh`, or
  `Không áp dụng`.

Then confirm, without a full re-read:

- no original instruction placeholder remains in a writable report cell, and no
  `[INPUT NEEDED: …]` marker was written into the workbook (it belongs to RX answers);
- no cell outside the `cells` set was written — column A labels, block titles and column headers are
  intact, and the conclusion-block field lists on the title rows (`B49`/`B53` on the bundled asset)
  are still there;
- prose cells carry the framework's full field list (`market-research` §12), `Giới hạn` and the
  closing action included, one field per line rather than one paragraph;
- an RX answer sits at its form's `default_length` or the user's stated length, with depth in an
  appendix rather than in the body.

A cell whose block was skipped or interrupted is a coverage failure — fill it with a named gap rather
than leaving it blank.

## B. Cross-block consistency

- The same metric stated in two blocks agrees, or the difference is explained.
- A lower-level count does not exceed its parent total in another block without an explained
  definition difference (city fleet ≤ national fleet; EV taxis ≤ all taxis).
- Scope, unit, period and currency basis stay consistent where blocks reference each other.

## C. Conclusion lineage

Every conclusion row draws only on rows already populated above, introduces no new factual claim, and
carries no stronger status than the weakest material premise beneath it. In an RX answer, a sentence
labelled suy luận or kịch bản never carries `Đã xác minh`.

## D. Adversarial audit of decision-grade claims

Applies to decision-grade claims and to the conclusions — not to every claim in the report. Try to
disprove them:

- Is a source merely reputable but wrong authority for the claim?
- Is a current page carrying stale data?
- Is a cached record being reported as current because the cache said `FRESH`, when `FRESH` only
  means the page need not be re-opened?
- Is a secondary source being mistaken for the original evidence?
- Is a first-party licence/project claim being treated as independently verified?
- Is a registered or licensed fleet being read as an active one, gross bookings as operator revenue,
  or an advertised driver income as net income?
- Is a licence application or a draft rule being read as an approval or an in-force rule; does a
  general driving licence stand in for a passenger-carrying authorisation?
- For fleet charging: is a charger rating being mistaken for vehicle acceptance, or a rider/fee for
  the underlying commodity price?
- Is a legal rule/version generalized beyond its conditions or no longer effective?
- Is any conclusion stronger than the evidence below it?

Fix the claim or expose the limitation before delivery.

## E. Contractor-list audit

Only when the objective includes a contractor list. Run audit E as written in
`../../contractor-search/references/contractor-enumeration.md`. It is short by design — running out of budget is a reason to
ship the workbook with named gaps, never a reason to skip it.

## F. Competitor-comparison audit

Only when the objective includes a competitor comparison. Run audit F as written in
`../../competitor-research/references/competitor-comparison.md`.
