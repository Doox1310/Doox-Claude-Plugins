# Dispatch — who opens the gated documents

Read once, before the first authority batch fans out (§9).

The triage decides *whether* a document is worth opening; dispatch decides *who pays* for opening it.
Both are needed: dispatching an unfiltered result list only moves the waste, and triaging without
dispatching still leaves every opened document in the main context for the rest of the run.

Defaults, each with the reason behind it:

- **What goes out.** Gate survivors only. Open inline only a single short page — roughly under
  ~2,000 words of visible text, judged before opening. Two or more documents in a batch, any PDF,
  anything long or of unknown length, and anything drawn against the decision-grade allowance go to a
  worker: a document read inline stays in context for every later turn.
- **The brief.** A list of gate-approved URLs plus the claims the batch must close, with
  non-overlapping authority/domain boundaries and the already-seen sources. An open-ended "research
  this topic" reopens the gate inside the worker, where you cannot see it. (Contractor frames are the
  exception — §6.6.)
- **The model.** The smallest fast model available, set explicitly via the agent tool's model
  override — transcribing a figure, date, article number or fee from a gated URL is not judgement.
  Use a mid-size worker when extraction needs reading law or reconciling definitions: a long legal
  instrument, a tariff order with customer classes, a §6.4 role determination.
- **The return.** One §10 ledger row per claim — the value, its conditions and the sentence or table
  cell carrying it, no narrative or document summary. State the row shape in the brief; prose in a
  return brings the document into main context by another route, so send such a return back rather
  than reformatting it in the main thread.
- **Fan out.** Send every ready batch in one message — batches are independent by construction (§4),
  and sending them one per turn pays the main context once per batch.
- **Shortfall.** A worker whose documents prove insufficient returns the shortfall and the leads it
  saw; re-run the triage in the main thread before any follow-up dispatch.

With no workers available, run sequentially with the same triage and the same extract-and-drop
discipline.
