---
name: market-research
description: Use when a user asks for EV-charging market research, a market report, market screening, deployment evidence, legal/utility/vendor research, or completion of the saved EV market-report workbook for a named country, city, region, or site cluster.
---

# Market Research

## 1. Contract

Produce a **sourced EV-charging market report in the saved `.xlsx` framework**. The report is evidence for human review, not an investment verdict, site-readiness certification, legal opinion, utility commitment, or vendor quotation.

Permanent plugin files stay minimal:

- `SKILL.md` — research and verification method.
- `references/final-audit.md` — §12, read once after the last block is written.
- `references/contractor-enumeration.md` — §6 and §12E, read only for a contractor objective.
- `scripts/wb.py` — writable-cell lister, workbook inspector and batch writer.
- `scripts/cache.py` — cross-run evidence cache (§9).
- `assets/khung-bao-cao-thi-truong.xlsx` — output schema and cell-level requirements.

Each reference carries its rules in full; the section that points at it carries only the trigger. Read the reference at the point named — never work a section from its stub.

Do not add permanent claim/source/config files. The ledger and the evidence cache are runtime state stored with the user's reports, not plugin assets.

### Run order

| # | Step | Owns it | Runs |
|---|---|---|---|
| 1 | Settle scope, objective, data-lock date, mode | §2 | once — one structured-question call, or none |
| 2 | Copy the asset; list the writable cells; inspect the report sheet in full | §3 | once |
| 3 | Split every writable row into atomic claims, mark the decision-grade set, batch by authority, open the ledger | §4, §9 | once |
| 4 | Sweep the cache for the whole split | §8.0 | once, before any search |
| 5 | Per authority batch: search → gate → dispatch → extract → close ledger rows → add to cache | §8.1–8.7 | repeats, batches fan out in parallel |
| 6 | Write each finished block cluster and audit it in place | §11 | repeats, alternating with 5 |
| 7 | One targeted pass over what is still open | §8.8 | once |
| 8 | Final audit, from the ledger | §12 | once |
| 9 | Completion check and reply | §13 | once |

Steps 5 and 6 alternate; everything else runs exactly once. §6 (contractor enumeration) hangs off step 5 with its own budget. §5, §7 and §10 are standing rules that apply throughout, not steps — never treat them as a stage to pass through.

Do not interleave the research and writing phases beyond the 5/6 alternation, and never return to a completed step: re-entering step 2 or 3 mid-run means re-reading the framework that is already in the ledger.

## 2. Scope and mode

Use facts already supplied; do not ask again. Resolve only what materially changes the research:

- market/jurisdiction and geographic scope;
- objective(s): market screening, investment due diligence, site selection, legal/permit, contractor/vendor, competitor/CPO;
- report data-lock date;
- relevant project facts already known (station model, fleet, vehicle type, candidate sites);
- when the objective includes contractor selection: the **contractor target profile** — default `tổng thầu turnkey` (see §6). Do not ask again if the user already stated it.

Ask for a missing essential in one structured-question call covering everything still unknown — never as a numbered list of questions in prose, and never one question per turn.

Default to the latest public data available as of the report date. Mode is `nhanh` unless the user explicitly asks for `sâu` — no objective escalates the mode on its own. What the objective does instead is decide **which claims are decision-grade** (§4), and depth is bought for those claims out of a separate allowance (§8). A site-selection run therefore pays for depth on interconnection, permits and site cost without also paying for it on climate normals and payment methods.

If a requested city/site conclusion has only national evidence, keep the local claim `Chưa xác minh`; never scale or infer it silently.

## 3. Read the framework first

Before researching, inspect the actual workbook being used. If the user supplies a framework, it wins over the bundled asset. Otherwise copy `assets/khung-bao-cao-thi-truong.xlsx` to the output path and never edit the asset.

Treat the workbook as the **output contract**:

- `00 - Hướng dẫn` defines status, evidence, date, estimate, gap, and conclusion rules and remains unchanged.
- Default output name: `Báo cáo thị trường [Thị trường] dd_mm_yyyy.xlsx`, unless the user/project specifies another naming convention. Whatever the name, it must not split into three parts on ` - `: `using-doox` reads any such spreadsheet as a project plan file and pulls the report into the daily reminder.
- The report sheet defines what each row/column requires and its quality standard.
- Instruction text in writable report cells is placeholder text to replace, not content to preserve.
- Do not rely on remembered row numbers, merged ranges, or layouts; inspect them before writing. Write a merged range at its top-left anchor cell; writing any other cell of the range fails.
- Do not insert, delete, renumber, retitle, or reorder framework rows unless the workbook itself explicitly requires repeatable rows or the user asks.
- The contractor-list sheet (`Bảng 3B - Danh sách nhà thầu` in the bundled asset) **is** a repeatable-row sheet: one row per company, one row per exclusion, plus the coverage block. It ships with blank rows already reserved for both lists — fill those first, and insert further rows only when they run out, taking care not to overwrite the block titles below. Inspect the actual row positions before writing.

Inspect and write with the bundled script, never with ad-hoc spreadsheet code. The report sheet declares about 22,000 cells and fills under 300 of them; an unguarded row loop prints thousands of empty rows and can cost more than the entire research run.

```bash
python scripts/wb.py cells   <file.xlsx> --sheet "NAME"                     # which cells may be written
python scripts/wb.py inspect <file.xlsx> [--sheet "NAME"] [--rows 15:25] [--max-chars N]
python scripts/wb.py write   <file.xlsx> cells.json    # {"sheet": {"B7": "value", "C7": ["• line", "• line"]}}
```

### Which cells may be written

**Run `cells` before the split and treat its output as the definitive list.** Do not decide writability by eye — the framework mixes output cells, fixed labels, block titles and column headers in the same columns, and getting it wrong either destroys the table structure or leaves the report half empty.

The rule it applies, for reading its output:

- **Column A is never written.** It holds the fixed row label or the block title.
- **A block-title row is never written** — column A in capitals — and neither is the **column-header row directly beneath it**. On the bundled asset those are rows 1, 15, 26, 35, 47, 51 and rows 2, 16, 27, 36. Note that a title row may itself carry framework metadata further along: `B47` and `B51` state the required field list for the conclusion block beneath them, and overwriting either destroys that block's output contract.
- **Every other non-empty cell in columns B onward is an output cell**, and its text is a placeholder describing what must replace it — including the `Tiêu chuẩn chất lượng và kiểm chứng` column, which asks for the verification content of that row, not for the standard to be preserved.
- **An empty cell in columns B onward was never required** and stays empty.

On the bundled asset this comes to **154 writable cells**; the count differs for a user-supplied framework, which is why it is computed rather than remembered. That set is the coverage denominator for §12 gate A.

Inspection happens in exactly two phases, and never anywhere else in the run:

1. **Once, at claim-split time:** inspect the **report sheet in full** — `--sheet` with no `--rows`. §4 splits every writable row into claims in this same pass, which a single block cannot support. That one dump also prints the sheet's merged ranges, which is the layout information every later `write` needs. Do not inspect the other sheets: `00 - Hướng dẫn` is a rules sheet you already follow, and `Bảng 3B` is inspected only if the objective includes contractor selection.
2. **Again only when the layout has actually moved under you** — that is, on `Bảng 3B` after inserting rows, or on a sheet phase 1 did not cover. Then `--sheet` plus `--rows` over the affected rows only.

Do **not** re-inspect target rows before an ordinary `write`. Nothing between phase 1 and the write can have changed them: this skill is forbidden from inserting, deleting or reordering framework rows, so phase 1's merged map is still correct, and a confirmation dump per write cluster is a tool round-trip that buys nothing. Never inspect a sheet you are not about to write, and never re-read a block already written. Repeated placeholder text is printed once and echoed as `<same as C17>`; a cell showing that marker carries the requirement written at the referenced coordinate.

`write` validates the whole batch first: an unknown sheet or a non-anchor merged cell fails the batch and writes nothing, so a rejection costs one error line instead of a corrupted file. Batch each report block into a single `write` call.

A cell value may be a **JSON list**, which is joined with newlines. `write` forces `wrap_text` on and releases the framework's pinned row height so the reader's spreadsheet auto-fits the wrapped text. Prefer the list form for every prose cell — see §11 for the required line shape.

## 4. Atomic claims: research only what the workbook needs

In the same pass that reads the framework, silently split every writable row into **atomic claims** — the whole workbook at once, not row by row. Every number, percentage, date, range, currency value, legal assertion, licence/certification status, named operator/partner fact, and factual premise used in a conclusion is a claim.

Then **batch the claims by the authority that will answer them**, not by row. One tariff order, registry page or statistics release usually answers several claims spread across unrelated rows; researching row by row fetches the same document repeatedly. A batch is one authority/document plus every claim it can close.

**Write the split straight into the ledger (§9) as open rows — do not hold it in the conversation.** The split is the largest artefact the run produces before any research happens: one row per claim, forty-odd rows for a full report, each carrying its target cell, its authority batch and whether it is decision-grade. Held in context it is re-sent on every turn for the rest of the run; held in the ledger it is queryable, survives an interruption, and doubles as the coverage checklist §12 gate A needs. The run is finished when no row is still open.

Each claim must end as exactly one report status from `00 - Hướng dẫn`:

- `Đã xác minh` — directly supported for the stated scope/period and valid for that wording;
- `Ước tính` — reproducible calculation/inference with sourced inputs and assumptions;
- `Chưa xác minh` — public evidence is insufficient or local confirmation is required;
- `Không áp dụng` — positive evidence shows the requirement does not apply.

Never write an untracked factual number or silently fill a gap from model knowledge.

**The objective selects the decision-grade set, and that set is the whole depth decision of the run** (§2, §8). Decision-grade claims — anything affecting legal applicability, permit, interconnection, cost, tax, schedule, current licence/certification, site feasibility, contractor selection, or a final conclusion — receive the strongest verification, first and out of their own budget line. Mark the set explicitly during the split; a claim not marked then is researched at base depth, so marking everything decision-grade defeats the split and marking too little quietly under-verifies the decision.

For contractor/vendor claims, **supply-chain role** (§6 taxonomy) is its own decision-grade claim, separate from licence and project-experience claims. Never infer it from a first-party capability statement alone. Building the candidate list itself is a claim-generating task with its own method — see §6; do not start it with a generic web search.

## 5. Source quality and claim authority

A reputable source is not automatically authoritative for every claim. Verify a claim with the source that has authority or direct knowledge for **that claim**.

| Claim type | Preferred evidence |
|---|---|
| law, licence requirement, permit, official fee, tax | current legislation/gazette, issuing authority, regulator, municipality, tax authority |
| electricity tariff, riders, interconnection, grid outlook | regulator-approved tariff/order, utility, system operator/ISO |
| EV registrations, fleet, population, official counts | registration/transport/statistics authority |
| vehicle/equipment specifications | OEM technical material; certification authority for certification status |
| public charging network | government/open dataset when available; CPO first-party for its own network; credible independent source only when primary data is unavailable |
| contractor/vendor services and contact | first-party website is valid for self-described capability/contact; licence/certification status requires the issuing registry; project experience is stronger from owner/tender/permit evidence |
| contractor supply-chain role and turnkey capability | first-party self-description alone is never sufficient — see §6 |
| payment/telecom | regulator and provider first-party terms/coverage |
| climate, hazards, public safety | meteorological, environmental, emergency/public-safety or municipal authority |
| costs | official fees/tariffs, published prices, quotations, or transparent industry studies; modelling assumptions must be labelled as assumptions |

Evidence classes:

- **A — authoritative primary:** government, regulator, legislation, statistics, utility/ISO, official registry.
- **B — first-party:** OEM, CPO, contractor, supplier, bank/telco/provider; valid only within its direct self-knowledge.
- **C — credible independent:** academic/professional institutions, IEA/World Bank-type bodies, reputable journalism/industry associations.
- **X — discovery only:** SEO pages, aggregators, generic blogs, social posts, forums, directories, AI/listicles. X may identify a lead but never supports a report fact.

Before using a source, confirm the publisher/domain identity and document provenance; search ranking, branding or a plausible URL is not proof of legitimacy. Every cited URL must have been opened/read in the run, or returned `FRESH` by the evidence cache (§9) and still inside the report's data window.

When a secondary source cites an original dataset/order/law, follow the citation chain and use the origin. Two URLs that derive from the same origin are **one** evidence source, not an independent cross-check. User-supplied documents may be evidence when relevant; identify them as supplied documents and do not let them override a current regulatory authority on regulatory claims.

## 6. Contractor enumeration and tier classification

**When the objective includes contractor selection, read `references/contractor-enumeration.md` before starting the candidate list, and follow it.** It carries the target profile and role taxonomy (§6.1), the frame-first enumeration frames F1–F10 (§6.2), mã ngành reading (§6.3), turnkey evidence (§6.4), credibility scoring (§6.5), the saturation stop rule and separate budget (§6.6), and audit E (§12E). Everything in it is decision-grade, and the rest of this file cites its subsection numbers directly.

Do not attempt contractor work from the summary above: a generic web search ranks intermediaries first, so a list built without the frames is a list of resellers.

## 7. Freshness, scope and meaning

For every sourced claim capture separately when applicable (if a page has no publication date, say so and retain the access date):

- data/reference period;
- publication date;
- effective/version date;
- access date;
- geography, population/customer class, unit and conditions.

A current webpage does not make an old figure current. For a current-state question:

- FX, tariffs, fees, law, permits, licence/certification status and service pricing: use the current effective version/date;
- market/fleet/charger counts: use the latest official reporting period found and state that period explicitly;
- vehicle/equipment specs: use the correct model/version;
- climate/geography: use the latest authoritative canonical dataset appropriate to the metric.

If the latest public figure is older than the report date, write it as a dated historical/latest-public figure and name the current-data gap; do not relabel it as current.

A cache `FRESH` verdict (§9) answers only "this page need not be opened again"; it never makes the figure inside it current. Judge the figure by the dates above, exactly as if the document had just been fetched.

Preserve source definitions. Do not treat these as synonyms without evidence: `station/location/site`, `port/connector/EVSE/charger`, `BEV/PHEV/ZEV`, `registered/on-road/ordered/planned`, `charger output/vehicle acceptance`, `energy rate/demand charge/rider/tax/total delivered cost`.

## 8. Research engine: minimum search for sufficient evidence

Every search must answer an unresolved claim.

0. **Sweep the cache once, before the first search of the run.** The cheapest document is one already extracted in an earlier report on this market. Run one `lookup` per distinct `claim_type` in the split, all in a single shell invocation — not one lookup per batch spread through the run, which pays a tool round-trip each time and re-prints records already seen. Every `FRESH` hit closes its claim with no search and no fetch, subject to §9's verification rule. A `STALE` hit is still worth having: it names the exact URL and publisher to go back to, so the claim skips discovery entirely and enters at step 1. Mark each closed row `origin=cache` in the ledger. A resumed run (§9) re-enters here with whatever claims are still open.

1. **Known authority → go direct.** Search/fetch the regulator, ministry, utility, registry, statistics office, municipality or company site first; use domain-restricted queries when useful.
2. **Unknown authority → one discovery pass.** Use short local-language/English queries to identify the agency, dataset, document name or official terminology, then move to the primary source. Keep one claim/question per query; avoid multi-topic sentences. Useful patterns are `[metric] [jurisdiction] [year]`, `site:official-domain [metric/document] [year]`, and `site:official-domain filetype:pdf "[official term]"`. Contractor work uses the §6 frames, not these patterns; within a frame, useful queries are `site:muasamcong.mpi.gov.vn "[EPC | thiết kế và thi công | chìa khóa trao tay]" "[lĩnh vực]" [tỉnh]`, `"chứng chỉ năng lực hoạt động xây dựng" "[lĩnh vực]" [tỉnh]`, `"[chủ đầu tư | dự án]" "nhà thầu thi công"`, `"[company]" "thi công" OR "tổng thầu" OR "EPC"` for role corroboration, and `site:linkedin.com/company "[company]"` for the social-profile check. Do not use `-"đại lý" -"phân phối"` as an exclusion — it hides firms that both build and distribute (§6.1).
3. **Triage the result list before opening anything.** A search result list is cheap; a fetch is not. Never open a document to find out whether it is relevant. From the titles, domains and snippets alone, build a candidate line per URL — `URL | publisher identity | evidence class (§5) | claim(s) it could close | date/period signal` — then drop, without fetching:

   - class **X** (SEO pages, aggregators, listicles, directories, forums, AI summaries) — a lead only, never opened as evidence;
   - a source whose class is wrong for the claim's authority (§5 table), when a correct-authority candidate is present in the same list;
   - duplicates: same origin document, same publisher's mirror, or a secondary that visibly quotes an origin already in the list — keep the origin, drop the rest;
   - a snippet already showing the wrong geography, period, customer class or unit;
   - anything answering a claim already closed in the ledger.

   Then rank the survivors by class → directness → recency and keep **one** document — the correct-authority one. This holds for a decision-grade claim too: an A-class regulator order, registry entry or statistics release *is* the authority, and opening a second document to agree with it buys nothing (§5 — two URLs from one origin are not an independent check). Open a second only when the verification-strength rule below actually calls for one: no A-class authority exists for the claim, the first document contradicts another closed claim, or its scope/period/customer class is ambiguous on the point at issue. Everything else stays unopened in the ledger as an unused lead. If the gate leaves nothing usable, refine the query once rather than opening a weak source; a second empty gate is a named gap, not a third search.

4. **Read evidence, not snippets.** Open only the documents that passed the gate, and extract the exact section carrying the value and its conditions. For long documents, find the relevant article/table/tariff/customer class instead of reading the whole file.
5. **Extract immediately.** Reduce each useful source to a compact evidence record before moving on.
6. **Reuse and deduplicate.** Fetch a document once and reuse it for every claim it supports, then write its evidence records to the cache (§9) so the next report on this market does not fetch it again.
7. **Stop when sufficient.** A low-risk claim directly answered by the correct authoritative source needs no decorative extra searches. This does not apply to contractor enumeration, which stops on the §6.6 saturation rule instead.
8. **Target gaps only.** After the first pass, re-search only unresolved, stale, contradictory, semantically ambiguous, or under-verified decision-grade claims. Do not rerun a whole batch.

Verification strength:

- Low-risk factual claim: one direct appropriate A source, or appropriate B source for first-party facts, is normally sufficient.
- Decision-grade claim: require the appropriate authoritative source. If no authoritative public source exists, use two genuinely independent credible sources when possible; otherwise mark `Chưa xác minh` and name who/what must confirm it.
- One targeted re-check per doubtful claim is normally enough. Failure to close it becomes a named gap, not an invitation to unlimited searching.

### Budget: depth is bought per claim, not per run

Quota is a ceiling, never a target; stop earlier when claims are closed. The budget has two lines, and the objective decides how big the second one is by deciding which claims are decision-grade (§4) — it never raises the first.

| Budget line | `nhanh` — default | `sâu` — only when the user asks |
|---|---|---|
| Base, spent on any claim | 20–35 searches, 10–14 documents | 30–45 searches, 16–20 documents |
| Decision-grade allowance, on top | +10–20 searches, +6–10 documents | +20–30 searches, +12–16 documents |

The two lines do not lend to each other. Climate normals, telecom coverage and payment methods are paid for out of the base line even in a site-selection run; a permit deadline or an interconnection cost is paid out of the allowance even in a screening run. Exhausting the base line is never a reason to spend the allowance on a low-risk claim, and a decision-grade claim left open while the allowance still has room is a budgeting error, not a gap.

Contractor enumeration (§6.6) carries its own budget on top of both and is not charged against either.

**Opened documents are the real cost, not searches.** A search result list is small; a fetched page or PDF is one to two orders of magnitude larger and it stays in context for the rest of the run. Extract the needed section rather than carrying the document forward. When a document ceiling is reached, finish the workbook with explicit gaps instead of starting another broad round — and say in the reply (§13) that the gap came from the ceiling, not from an absent public source.

### Dispatch

The step-3 gate decides *whether* a document is worth opening; the worker decides *who pays* for opening it. Both are needed — dispatching an unfiltered result list only moves the waste, and gating without dispatching still leaves every opened document in the main context for the rest of the run.

- **What goes out.** Only gate survivors. Dispatch is the default at every mode; open inline only one or two short pages. Three or more, any long PDF, or anything drawn against the decision-grade allowance goes to a worker. `nhanh` is where a stray document hurts most, because the budget it eats is the smaller one.
- **The brief.** A fixed list of gate-approved URLs plus the claims that batch must close — never an open-ended "research this topic", which reopens the gate inside the worker where you cannot see it. Give each worker non-overlapping authority/domain boundaries and the seen-source set.
- **The model.** Set it explicitly to the **smallest fast model available**, via the agent tool's model override rather than the inherited default. Transcribing a figure, date, article number or fee schedule from a gated URL is not judgement; the judgement already happened at the gate. Step up to a mid-size worker only for extraction that requires reading law or reconciling definitions — a long legal instrument, a tariff order with customer classes, a §6.4 role determination. Dispatching at the inherited default pays the main model's rate for transcription and captures none of the saving.
- **The return.** A §9 ledger row per claim and nothing else: no narrative, no document summary, no quoted passage beyond the sentence or table cell carrying the value and its conditions. Prose in a return has moved the document into main context by another route — the exact cost dispatch exists to avoid. State the row shape in the brief; reject a return that ignores it instead of reformatting it in the main thread.
- **Fan out.** Dispatch every ready batch in one message. Authority batches are independent by construction (§4), so gating three and sending them one per turn pays the whole main-thread context three times instead of once.
- **Shortfall.** A worker whose assigned documents prove insufficient returns the shortfall and the leads it saw. The gate is re-run in the main thread before any follow-up dispatch.

When workers are unavailable, run sequentially with the same gate and the same extract-and-drop discipline.

## 9. Runtime ledger and the cross-run evidence cache

Both live in the report's **source-log folder**, `doox-sources/<market-slug>/`, beside the output workbook — the only place besides the report itself that this skill writes. The ledger is per-run; the cache is per-market and outlives every run.

```
doox-sources/<market-slug>/
  evidence.jsonl          # cross-run cache, one JSON record per line
  ledger-<dd_mm_yyyy>.tsv # this run's claim ledger
```

### The ledger

One row per claim, opened by the §4 split and closed as the claim resolves:

`claim | grade | batch | state | origin | result | status candidate | scope/unit/period | source/publisher/URL | publication/effective/access date | condition/definition | output cell(s)`

For calculated claims also record:

`formula | sourced inputs | assumptions | rounding | output unit`

Four of those columns exist to make the run auditable without holding counters in context:

- `grade` — `base` or `dg`. Set at the split (§4); it decides which budget line the claim spends from (§8).
- `batch` — the authority batch the claim belongs to, so a batch can be dispatched and closed as a unit.
- `state` — `open` until resolved, then the §4 status. No `open` rows left is the definition of a finished run and the input to §12 gate A.
- `origin` — `fetch`, `cache`, `estimate`, or `gap`. Distinct URLs with `origin=fetch` are the documents actually opened, so the §13 budget figures are counted from the file rather than recalled.

`origin` and `state` must agree, and a row where they do not is a defect the run introduced: `gap` requires `Chưa xác minh`, `estimate` requires `Ước tính`, and `fetch` or `cache` requires a source URL in the row. Check it whenever a batch closes — it is one pass over the file and it catches an estimate that quietly became a verified figure.

A source may support multiple claims. A claim may have multiple sources.

Because the counts are derivable, query the ledger for the budget when a batch closes rather than tracking numbers in the conversation — claims by `grade`, documents by distinct URL where `origin=fetch`, cache closures, estimates and gaps by `origin`. One pass over the file answers all of them and answers §13 as well.

Keep the ledger as a **file**, appended as claims close, not as text repeated in the conversation. It grows to hundreds of rows over a full report, and a ledger carried in context is re-sent on every turn for the rest of the run and re-emitted whole each time it is updated. Write it once, append to it, and read back only the rows a block or an audit actually needs.

**Resuming an interrupted run starts here, not at §3.** Read the ledger and the cache first, then inspect only the rows still unwritten. A claim the ledger already closed is never re-researched and its sources are never re-opened; a block the ledger shows as written is never re-inspected. Only genuinely unresolved claims re-enter §8, and they re-enter at step 0.

### The cache

A decree, a tariff order, a registry page or a climate normal does not change between two reports on the same market, but re-opening it costs exactly what it cost the first time — and opened documents are the dominant cost of a run (§8). Every source opened in a run is written to `evidence.jsonl` once its records are extracted, and every claim batch consults the cache before its first search (§8.0).

```bash
python scripts/cache.py lookup <cache.jsonl> --as-of <data-lock date> [--claim-type T] [--q TEXT] [--url U]
python scripts/cache.py add    <cache.jsonl> records.json
```

A record is the ledger row plus what the cache needs to age it:

`url | publisher | evidence_class | claim_type | value | scope | period | published | effective | accessed`

`claim_type` is what picks the re-verification window, so use the script's own vocabulary — `fx`, `tariff`, `fee`, `tax`, `law`, `permit`, `licence`, `pricing`, `statistics`, `network`, `contractor`, `spec`, `climate`. An unlisted type still caches, but falls back to the shortest window.

Three rules keep the cache from becoming a source of stale reports:

- **`FRESH` means "do not open this page again", never "this figure is current."** The figure is judged by §7 against the dates the lookup prints back, exactly as if the document had just been fetched. Gate D audits this specifically.
- **A `FRESH` hit is subject to the same verification strength as a fresh fetch** (§8). It closes a decision-grade claim only if it is the A-class authority for that claim; where the rule would have called for a second independent source, the cache does not excuse it. The cache reduces fetches, not evidence standards.
- **Never cache a class X source, an unverified extraction, or a value the run itself marked `Chưa xác minh`.** The cache holds evidence, not leads.

Add records as each batch closes rather than in one dump at the end, so an interrupted run still leaves the market better cached than it found it.

## 10. Conflicts and normalisation

Before comparing values, normalise only when definitions permit it:

- geography and population/customer class;
- data period;
- currency and FX date;
- tax-inclusive/exclusive basis;
- kW vs kWh and power vs energy;
- per site / station / port / charger / vehicle;
- nominal vs usable battery capacity;
- official deadline vs observed project duration.

Every conversion is an `Ước tính`/calculated claim unless the source already publishes the converted value. Record formula and inputs; never silently convert.

When sources disagree, do not average or silently choose. Record both material figures and resolve downstream use by: **authority → directness → recency/effective status → scope match → methodology → independence**. State the reason for the preferred figure. If the conflict remains decision-relevant, mark it as a limitation/gap.

## 11. Fill the workbook progressively

Write each completed report block as soon as its claims are resolved; write conclusion blocks last. Preserve the workbook's style, merges, headers and `00 - Hướng dẫn`.

One authority batch (§4) usually closes claims spread across several blocks, so blocks finish in clusters rather than in order. Write every block that finished in the same cluster in **one** `write` call, and never split a single block across two calls — a half-written block cannot be audited, and the second call pays for the whole context again to finish what the first one started.

For each result, follow the exact output shape required by the framework. Include exact URLs/documents, not generic homepages when a specific page/order/table exists.

### Cell layout: the framework's field list, one field per line

**The required fields are set by the workbook, not by this file.** Three specs are in force, and the applicable one wins:

| Where | Required fields |
|---|---|
| `00 - Hướng dẫn` A20 — every ordinary result | `Kết quả \| Trạng thái \| Phạm vi/đơn vị/kỳ dữ liệu \| Nguồn và ngày \| Phương pháp/giả định (nếu có) \| Giới hạn \| Hành động xác minh` |
| `B47` — the legal-conclusion block | `kết luận \| trạng thái \| nguồn và ngày \| giới hạn \| hành động xác minh` |
| `B51` — the final-analysis block | `kết luận \| trạng thái \| nguồn và ngày \| giới hạn \| bước tiếp theo` |

Read the applicable spec off the workbook during the §3 inspect; a user-supplied framework may state a different one. Dropping `Giới hạn` or the closing action is a coverage failure, not a stylistic choice — they are what makes the report reviewable.

A report cell is read on screen inside a fixed column, so a wall of prose is unusable no matter how correct it is. Write every prose cell as a **JSON list of short lines** (§3) and let `write` join them:

- lead with the content lines: one claim, figure or procedural step per line, never two facts joined by `và`/`;`, and keep the placeholder's own `•` prefix where it uses one;
- put the status word (`Đã xác minh` / `Ước tính` / `Chưa xác minh` / `Không áp dụng`) at the end of the content line it qualifies, not once at the end of the cell;
- then one line per remaining field, each opening with the field's own name — `Phạm vi/đơn vị/kỳ:`, `Nguồn và ngày:`, `Phương pháp/giả định:`, `Giới hạn:`, `Hành động xác minh:` — so a reviewer can find a field without reading the cell;
- one source per `Nguồn và ngày:` line, as `<publisher>, <date> — <URL>`.

A single short value (a date, a fee, a name, one status word) stays a plain string; the list form is for anything carrying a full field list.

Rules:

- A required field with no adequate evidence says `Chưa xác minh` and identifies the missing data, confirming body and effect of the gap.
- Estimates show formula, inputs, assumptions and limits.
- Do not invent current licence/certification, project references, costs, permit times, utility capacity, local network quality, site hazards or commercial terms.
- Company self-publication must be labelled as such when it matters to reliability.
- Conclusion rows may use only evidence already populated above. They introduce no new factual claims and cannot carry a stronger status than the weakest material premise they depend on.
- Never conclude a specific site is ready without project-specific land/right-of-use, electrical capacity/interconnection, legal/permit and cost confirmation.

### Audit each block while writing it

Most of the audit belongs here, not at the end: the block and its evidence are already in context, so checking them now is nearly free, whereas re-reading the finished workbook later reloads everything at the point where context is largest. Before moving to the next block, confirm within the block just written:

- every factual assertion — including non-numeric legal, licence, operator, vendor and causal statements — traces to the runtime ledger, or is explicitly labelled analysis/estimate/gap;
- every numeric token (integer, decimal, percentage, currency amount, date, range, kW/kWh/MW value, count, rate, CAGR, duration) is sourced evidence, a reproducible calculation, or structural metadata/label — anything else is verified, relabelled `Chưa xác minh`, or removed;
- components = reported total; percentages use the stated denominator and stay in plausible bounds; min ≤ max; FX, CAGR, totals and subtotals reproduce; units and tax basis match the wording;
- dates/effective periods match the claim, and national/regional data is not presented as city/site data;
- source wording and report metric mean the same thing;
- no instruction placeholder is left behind.

Example: if components are `22 + 322 = 344` but a source/report also states total `407`, preserve the discrepancy and verify the underlying definitions/source dates; never force the components to fit the total. Any mismatch is reported as a conflict; never average it away.

## 12. Final audit — see `references/final-audit.md`

**After the last block is written and before the reply, read `references/final-audit.md` and run every gate in it.** Gates A–D always apply; gate E only for a contractor objective, and it defers to `references/contractor-enumeration.md`. Running out of budget is a reason to ship the workbook with named gaps, never a reason to skip the audit.

## 13. Completion and reply

The report is complete only when:

- framework coverage = 100%;
- factual-claim coverage = 100% processed;
- numeric coverage = 100% processed;
- unsupported numbers/factual claims = 0;
- unresolved decision-grade items are explicitly `Chưa xác minh` rather than guessed;
- arithmetic/unit/date/scope inconsistencies are resolved or openly reported;
- discovery-only sources do not appear as evidence;
- conclusion lineage is traceable to populated rows;
- for a contractor objective: audit E passes and the coverage block on `Bảng 3B` is filled.

“100% processed” means every required claim is verified, estimated with evidence, positively not applicable, or explicitly unresolved. It does **not** mean public information exists for every project-specific fact.

Every figure in the reply is **counted from the ledger** (§9), never recalled: claims by `grade`, documents by distinct URL where `origin=fetch`, cache closures where `origin=cache`, gaps where `origin=gap`. State: output file, mode (`nhanh`/`sâu`), data-lock date, claims marked decision-grade out of the total, searches and documents opened **split into base line versus decision-grade allowance**, candidates gated out, claims closed from the cache without a fetch, unique evidence sources, decision-grade claims still `Chưa xác minh`, whether any gap came from hitting a ceiling rather than from absent public evidence, and whether all final audit gates passed. For a contractor objective also state: frames worked, companies listed, how many are `Tổng thầu turnkey`, how many in Nhóm A, whether saturation was reached, and the residual blind spots. Offer follow-up work only when the user asks or when it directly closes a named gap already present in the report.
