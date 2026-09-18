# Dispatch — who opens the gated documents

Read this at run-order step 5, once, immediately before fanning out the first authority batch. It is
not a standing rule and nothing earlier in the run needs it.

The step-3 gate decides *whether* a document is worth opening; the worker decides *who pays* for opening it. Both are needed — dispatching an unfiltered result list only moves the waste, and gating without dispatching still leaves every opened document in the main context for the rest of the run.

- **What goes out.** Only gate survivors. Dispatch is the default at every mode. Inline is allowed only for a single page **under ~2,000 words / ~12,000 characters of visible text** — check the page length before opening it, not after; a source with no visible length signal (behind a viewer, a scanned PDF, an unknown-length feed) is dispatched, never guessed short. Two or more documents in the same batch, any PDF, anything over that size, or anything drawn against the decision-grade allowance goes to a worker — no exception for a page that merely "reads fast." `nhanh` is where a stray document hurts most, because the budget it eats is the smaller one.
- **The brief.** A fixed list of gate-approved URLs plus the claims that batch must close — never an open-ended "research this topic", which reopens the gate inside the worker where you cannot see it. Give each worker non-overlapping authority/domain boundaries and the seen-source set.
- **The model.** Set it explicitly to the **smallest fast model available**, via the agent tool's model override rather than the inherited default. Transcribing a figure, date, article number or fee schedule from a gated URL is not judgement; the judgement already happened at the gate. Step up to a mid-size worker only for extraction that requires reading law or reconciling definitions — a long legal instrument, a tariff order with customer classes, a §6.4 role determination. Dispatching at the inherited default pays the main model's rate for transcription and captures none of the saving.
- **The return.** A §10 ledger row per claim and nothing else: no narrative, no document summary, no quoted passage beyond the sentence or table cell carrying the value and its conditions. Prose in a return has moved the document into main context by another route — the exact cost dispatch exists to avoid. State the row shape in the brief; reject a return that ignores it instead of reformatting it in the main thread.
- **Fan out.** Dispatch every ready batch in one message. Authority batches are independent by construction (§4), so gating three and sending them one per turn pays the whole main-thread context three times instead of once.
- **Shortfall.** A worker whose assigned documents prove insufficient returns the shortfall and the leads it saw. The gate is re-run in the main thread before any follow-up dispatch.

When workers are unavailable, run sequentially with the same gate and the same extract-and-drop discipline.
