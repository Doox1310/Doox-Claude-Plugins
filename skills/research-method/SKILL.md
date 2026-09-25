---
name: research-method
description: "Internal shared method for the Doox research skills — loaded FIRST by `market-research`, `contractor-search` and `competitor-research`, never invoked on its own. Carries what all three rely on: the file-on-disk contract, language rules, atomic claims and the four statuses, source classes A/B/C/X, freshness, the search engine with its budget and dispatch, the claim ledger and cross-run evidence cache, conflict normalisation, final audit gates A–D, the reply's ledger counts, and the RX1–RX5 forms, topic lenses R01–R52 and metrics K01–K56 for the electric-taxi domain."
---

# Research method

Shared method of the three research skills. It is not a skill a user asks for: `market-research`
(đánh giá thị trường/khu vực), `contractor-search` (tìm nhà thầu/đối tác) and `competitor-research`
(so sánh đối thủ) each say "load `research-method` first", and each carries only what is its own.
A request that combines them runs **one** run: one scope call, one claim split, one ledger, one cache
sweep, one final audit — never three runs over the same market.

The customer is an electric-taxi operator that **runs its own fleet**: it owns the cars, employs the
drivers, runs the app and dispatch, and charges its own vehicles at its depots. Everything here is
worded for that business. Charging appears only as charging *for the fleet* (depot, opportunity,
public back-up), never as a charging-station business.

### Section numbers are shared across the four skills

Each `§` number lives in exactly one skill, so a `§` reference means the same thing wherever it is
read:

| § | Where |
|---|---|
| §1, §4, §5, §8, §9, §10, §11, §13 (gates A–D), §14 | this skill |
| §2 scope, §3 framework, §12 progressive fill | `market-research` |
| §6 contractor enumeration, §13E | `contractor-search` (`../contractor-search/references/contractor-enumeration.md`) |
| §7 competitive position, §13F | `competitor-research` (`../competitor-research/references/competitor-comparison.md`) |

### Paths

Files below are relative to **this skill's directory**. The harness prints a skill's "Base
directory" when it loads; this skill's directory is the `research-method` folder, which sits beside
every calling skill's own directory (`<caller base>/../research-method`). Bash does not run from any
skill directory — it runs in the user's working folder — so always call the scripts by **absolute
path**, written below as `<RM>`:

```bash
python "<RM>/scripts/wb.py" ...      # <RM> = absolute path of the research-method directory
python "<RM>/scripts/cache.py" ...
```

## 1. Contract

Research output is **evidence for human review**, not an investment verdict, launch-readiness
certification, legal opinion, licence grant, utility commitment or vendor quotation.

**Every run leaves a file on the user's machine.** Write every deliverable — the workbook, and any RX
answer (below) — into the local working folder the user opened for the session (in Cowork, what shows
under Output); with no folder opened, the session's outputs folder. Never deliver through Claude
Docs, an artifact, or any document a connector creates or edits on a remote service: that is not a
file on the user's machine, and a run that leaves only that has produced no deliverable. The chat
reply summarises the file and names it; it never replaces it.

Permanent files of this skill, each read at the point named, never end to end:

- `assets/form-research.md` — RX1–RX5, the shape of a research answer that goes to its own `.docx`
  instead of the workbook. Read once the objective is settled.
- `references/topic-lenses.md` — R01–R52, per topic: what to sweep and the counting trap it carries.
  Read the matching row before searching that topic, never the whole file.
- `references/metrics.md` — K01–K56 metric definitions. Read the matching rows before putting two
  numbers in the same table (§11).
- `references/dispatch.md` — §9, read once at step 5, before the first batch fans out.
- `references/final-audit.md` — §13, read once after the last block is written.
- `scripts/wb.py` — writable-cell lister, workbook inspector and batch writer (`market-research` §3).
- `scripts/cache.py` — cross-run evidence cache (§10).

Each reference carries its rules in full; the section that points at it carries only the trigger.
Read the reference at the point named — never work a section from its stub.

Do not add permanent claim/source/config files. The ledger and the evidence cache are runtime state
stored with the user's reports, not plugin assets.

### Run order

| # | Step | Owns it | Runs |
|---|---|---|---|
| 1 | Settle scope, objective(s), deliverable, data-lock date, mode; pick the RX form for anything outside the workbook | `market-research` §2 (and the calling skill's own scope rules) | once — one structured-question call, or none |
| 2 | Workbook only: copy the asset; list the writable cells; inspect the report sheet in full | `market-research` §3 | once |
| 3 | Split every required output into atomic claims, mark the decision-grade set, batch by authority, open the ledger | §4, §10 | once |
| 4 | Sweep the cache for the whole split | §9.0 | once, before any search |
| 5 | Per authority batch: search → gate → dispatch → extract → close ledger rows → add to cache | §9.1–9.8 | repeats, batches fan out in parallel |
| 6 | Write each finished block cluster and audit it in place | `market-research` §12; the RX form for a `.docx` | repeats, alternating with 5 |
| 7 | One targeted pass over what is still open | §9.8 | once |
| 8 | Final audit, from the ledger | §13 | once |
| 9 | Completion check and reply | §14 | once |

Steps 5 and 6 alternate; everything else runs exactly once. Contractor enumeration (§6) and the
competitor set (§7) hang off step 5 with their own budgets. §5, §8 and §11 are standing rules that
apply throughout, not steps — never treat them as a stage to pass through.

Do not interleave the research and writing phases beyond the 5/6 alternation, and never return to a
completed step: re-entering step 2 or 3 mid-run means re-reading the framework that is already in the
ledger.

### RX answers — anything that is not the workbook

Two deliverable shapes exist and they are not interchangeable: the market workbook
(`market-research` §3, §12), and a research answer written to its own `.docx`. Whatever does not go
into the workbook takes the shape of one RX form — RX1 for a question or a landscape, RX2 for a
comparison or benchmark (this is `competitor-research`), RX3 for a named counterparty or shortlist
(`contractor-search`), RX4 for an entry or scenario thesis, RX5 for what changed against a dated
baseline. The RX form decides the **shape of the answer only**. Evidence classes (§5), the ledger and
cache (§10), the budget (§9) and the four statuses (§4) are unchanged by it, and no RX form replaces
`../contractor-search/references/contractor-enumeration.md` or
`../competitor-research/references/competitor-comparison.md`.

Write an RX answer, in its form, to `Nghiên cứu [Chủ đề] [Thị trường] dd_mm_yyyy.docx` in the
working folder — beside the workbook when the run also makes one; a `.md` of the same name only when
a `.docx` cannot be produced — then summarise it in the reply. If that name already exists, add
` (2)`, ` (3)`… rather than overwrite it. The one exception is `contractor-search`'s enumerated list:
it lives in the workbook (`Bảng 3B`) only, and RX3 shapes its summary in the reply — never a second
copy in a `.docx`.

**Length follows the form.** Each RX form carries a `default_length` (`assets/form-research.md`) —
RX1 50–120 words for a lookup and 200–400 for a brief, RX2 one table plus 100–200 words, RX3 one
shortlist table plus a short conclusion (250 words for a single candidate), RX4 250–450 words plus a
small table, RX5 150–300 words or one change table. Write to it: a user-stated length wins, depth
beyond it goes to an appendix (the evidence table, the calculation), and a material gap is never cut
to fit. Padding an RX2 into a report is as much a form failure as dropping its gap line.

**Two kinds of gap, two markers.** An evidence gap — public evidence insufficient — is a claim status,
`Chưa xác minh`, with who/what must confirm it (§4). A missing **user input** that the answer needs —
own fleet size, target launch date, own-side fare for a comparison — is written as
`[INPUT NEEDED: <field>]` at the point it is needed, never guessed and never turned into zero. The
workbook uses only the four statuses; `[INPUT NEEDED: …]` belongs to RX answers and the reply.

### Language

**Three languages meet in a single run, and they are not the same language.** The reply and any
RX deliverable follow the user (`using-doox`, "Language" — vi, en or fr). **The workbook keeps its
own**: the bundled framework is Vietnamese, so its sheet names, its field labels and the four status
words `Đã xác minh` / `Ước tính` / `Chưa xác minh` / `Không áp dụng` are written into the cells
exactly as the framework has them, whatever language the user is working in — they are the output
contract of that file, not a translation choice, and a status rendered as `Verified` breaks every
downstream read of the report. A user-supplied framework is filled in *its* language, the same way.
**Searching follows the market**: queries, official terminology and document names are in the
jurisdiction's own language — French for Côte d'Ivoire, English (and Filipino where the source is)
for the Philippines, English (and Swahili where the source is) for Kenya — because that is where the
primary sources are. A figure, a legal citation or a quoted clause keeps the language it was
published in; a translation of it is labelled as one and never replaces the original in the ledger.

When an RX deliverable in English or French carries a status, give it as the canonical Vietnamese
term with the reader's gloss once — `Chưa xác minh (not verified)` — so the chat and the workbook
still say the same thing.

## 4. Atomic claims: research only what the output needs

In the same pass that reads the framework (or settles the RX form), silently split every required
output into **atomic claims** — the whole deliverable at once, not row by row. Every number,
percentage, date, range, currency value, legal assertion, licence/permit status, named
operator/partner fact, and factual premise used in a conclusion is a claim.

**Read the matching rows of `references/topic-lenses.md` while splitting, one row per topic the
output actually touches.** Each row carries the scope to sweep and the counting trap that topic
carries — registered versus active fleet, advertised versus net driver income, gross bookings versus
operator revenue, application versus approval, national versus city. The trap belongs in the split,
where it decides how a claim is worded, not in the audit where it becomes a rewrite. Never read the
file end to end; it is a lookup.

Then **batch the claims by the authority that will answer them**, not by row. One transport-authority
regulation, registry page or statistics release usually answers several claims spread across
unrelated rows; researching row by row fetches the same document repeatedly. A batch is one
authority/document plus every claim it can close.

**Write the split straight into the ledger (§10) as open rows — do not hold it in the conversation.**
The split is the largest artefact the run produces before any research happens: one row per claim,
forty-odd rows for a full report, each carrying its target cell, its authority batch and whether it
is decision-grade. Held in context it is re-sent on every turn for the rest of the run; held in the
ledger it is queryable, survives an interruption, and doubles as the coverage checklist §13 gate A
needs. The run is finished when no row is still open.

Each claim must end as exactly one report status from `00 - Hướng dẫn`:

- `Đã xác minh` — directly supported for the stated scope/period and valid for that wording;
- `Ước tính` — reproducible calculation/inference with sourced inputs and assumptions;
- `Chưa xác minh` — public evidence is insufficient or local confirmation is required;
- `Không áp dụng` — positive evidence shows the requirement does not apply.

An RX answer additionally labels analytical sentences as **suy luận (inference)** or **kịch bản
(scenario)** — see `assets/form-research.md`. Those labels sit beside the four statuses, never
replace them, and never carry `Đã xác minh`.

Never write an untracked factual number or silently fill a gap from model knowledge.

**The objective selects the decision-grade set, and that set is the whole depth decision of the run**
(`market-research` §2, §9). Decision-grade claims — anything affecting legal applicability, a
transport/operating licence, permit, depot interconnection, cost, tax, schedule, vehicle
homologation, site feasibility, contractor or partner selection, competitive position, or a final
conclusion — receive the strongest verification, first and out of their own budget line. Mark the set
explicitly during the split; a claim not marked then is researched at base depth, so marking
everything decision-grade defeats the split and marking too little quietly under-verifies the
decision.

**A `dg` mark needs a one-word reason from that list, recorded in the ledger row at split time**
(`legal`, `licence`, `permit`, `interconnection`, `cost`, `tax`, `schedule`, `homologation`,
`feasibility`, `contractor`, `partner`, `competitor`, `conclusion`) — never the bare tag with no
reason. A claim justified only by "the report is about X" rather than by what *that specific claim*
affects is `base`, not `dg`. If more than roughly a third of the split ends up `dg`, stop and recheck
the reasons before researching anything — a split that heavy is marking the topic, not the claim, and
it doubles the run's cost for no verification gain.

For contractor/vendor claims, **supply-chain role** (§6 taxonomy) is its own decision-grade claim,
separate from licence and project-experience claims. Never infer it from a first-party capability
statement alone. Building a candidate list is a claim-generating task with its own method — §6 in
`contractor-search`; do not start it with a generic web search.

## 5. Source quality and claim authority

A reputable source is not automatically authoritative for every claim. Verify a claim with the source
that has authority or direct knowledge for **that claim**.

| Claim type | Preferred evidence |
|---|---|
| law, licence requirement, permit, official fee, tax | current legislation/gazette, issuing authority, regulator, municipality, tax authority |
| taxi / ride-hailing licensing, operator and driver authorisation, fare rules | transport ministry or land-transport regulator, city/municipal transport authority, published fare orders and licensed-operator lists |
| vehicle registrations, taxi plates, fleet counts, population | vehicle-registration/transport/statistics authority |
| vehicle type approval, homologation, import status | homologation/standards authority, customs; OEM technical material for specifications |
| electricity tariff, depot interconnection, grid outlook | regulator-approved tariff/order, utility, system operator |
| public charging used as fleet back-up | government/open dataset when available; the network owner's first-party data for its own network; credible independent source only when primary data is unavailable |
| operator scale, fares, service area | licensing authority and filings first; the operator's app/fare page for its own offer (first-party); press only for direction |
| contractor/vendor services and contact | first-party website is valid for self-described capability/contact; licence/certification status requires the issuing registry; project experience is stronger from owner/tender/permit evidence |
| contractor supply-chain role and turnkey capability | first-party self-description alone is never sufficient — see §6 |
| driver pay, labour rules, social contributions | labour ministry/code, social-security authority; platform pages only for their own advertised terms |
| payment/telecom | regulator and provider first-party terms/coverage |
| climate, hazards, public safety, road safety | meteorological, environmental, police/road-safety or municipal authority |
| costs | official fees/tariffs, published prices, quotations, or transparent industry studies; modelling assumptions must be labelled as assumptions |

Evidence classes:

- **A — authoritative primary:** government, regulator, legislation, statistics, utility/system
  operator, official registry, licensed-operator list.
- **B — first-party:** OEM, taxi/ride-hailing operator, contractor, supplier, bank/telco/provider;
  valid only within its direct self-knowledge.
- **C — credible independent:** academic/professional institutions, IEA/World Bank-type bodies,
  reputable journalism/industry associations.
- **X — discovery only:** SEO pages, aggregators, generic blogs, social posts, forums, directories,
  AI/listicles. X may identify a lead but never supports a report fact.

Before using a source, confirm the publisher/domain identity and document provenance; search ranking,
branding or a plausible URL is not proof of legitimacy. Every cited URL must have been opened/read in
the run, or returned `FRESH` by the evidence cache (§10) and still inside the report's data window.

When a secondary source cites an original dataset/order/law, follow the citation chain and use the
origin. Two URLs that derive from the same origin are **one** evidence source, not an independent
cross-check. User-supplied documents may be evidence when relevant; identify them as supplied
documents and do not let them override a current regulatory authority on regulatory claims.

## 8. Freshness, scope and meaning

For every sourced claim capture separately when applicable (if a page has no publication date, say so
and retain the access date):

- data/reference period;
- publication date;
- effective/version date;
- access date;
- geography, population/customer class, unit and conditions.

A current webpage does not make an old figure current. For a current-state question:

- FX, fares, tariffs, fees, law, licences, permits and service pricing: use the current effective
  version/date;
- market/fleet/driver/trip counts: use the latest official reporting period found and state that
  period explicitly;
- vehicle/equipment specs: use the correct model/version/market;
- climate/geography: use the latest authoritative canonical dataset appropriate to the metric.

If the latest public figure is older than the report date, write it as a dated
historical/latest-public figure and name the current-data gap; do not relabel it as current.

A cache `FRESH` verdict (§10) answers only "this page need not be opened again"; it never makes the
figure inside it current. Judge the figure by the dates above, exactly as if the document had just
been fetched.

Preserve source definitions. Do not treat these as synonyms without evidence:
`registered/licensed/active/on-road fleet`, `ordered/delivered/in-service vehicles`,
`driver/licensed driver/active driver`, `trip/booking/completed trip`,
`gross bookings (GMV)/operator revenue/driver earnings`, `advertised/gross/net driver income`,
`quoted fare/final fare/fare net of promotion`, `taxi/ride-hailing/private hire` as legal categories,
`BEV/PHEV/hybrid`, `rated range/duty-cycle range`, and — for fleet charging only —
`site/connector/simultaneous power`, `charger output/vehicle acceptance`,
`energy rate/demand charge/fixed charge/tax/total delivered cost`.

## 9. Research engine: minimum search for sufficient evidence

Every search must answer an unresolved claim.

0. **Sweep the cache once, before the first search of the run.** The cheapest document is one already
   extracted in an earlier report on this market. Run one `lookup` per distinct `claim_type` in the
   split, all in a single shell invocation — not one lookup per batch spread through the run, which
   pays a tool round-trip each time and re-prints records already seen. Every `FRESH` hit closes its
   claim with no search and no fetch, subject to §10's verification rule. A `STALE` hit is still
   worth having: it names the exact URL and publisher to go back to, so the claim skips discovery
   entirely and enters at step 1. Mark each closed row `origin=cache` in the ledger. A resumed run
   (§10) re-enters here with whatever claims are still open.

1. **Known authority → go direct.** Search/fetch the transport regulator, ministry, utility, registry,
   statistics office, municipality or company site first; use domain-restricted queries when useful.
2. **Unknown authority → one discovery pass.** Use short local-language/English queries to identify
   the agency, dataset, document name or official terminology, then move to the primary source. Keep
   one claim/question per query; avoid multi-topic sentences. Useful patterns are
   `[metric] [jurisdiction] [year]`, `site:official-domain [metric/document] [year]`, and
   `site:official-domain filetype:pdf "[official term]"` — e.g. `"licence de taxi" Abidjan arrêté`,
   `LTFRB "Transport Network Vehicle Service" memorandum circular`, `NTSA "PSV licence" taxi Kenya`.
   Contractor work uses the §6 frames and competitor work the §7 frames, not these patterns; within a
   frame, useful queries are `site:muasamcong.mpi.gov.vn "[EPC | thiết kế và thi công | chìa khóa trao tay]" "[lĩnh vực]" [tỉnh]`,
   `"chứng chỉ năng lực hoạt động xây dựng" "[lĩnh vực]" [tỉnh]`,
   `"[chủ đầu tư | dự án]" "nhà thầu thi công"`,
   `"[company]" "thi công" OR "tổng thầu" OR "EPC"` for role corroboration, and
   `site:linkedin.com/company "[company]"` for the social-profile check. Do not use
   `-"đại lý" -"phân phối"` as an exclusion — it hides firms that both build and distribute (§6.1).
3. **Triage the result list before opening anything.** A search result list is cheap; a fetch is not.
   Never open a document to find out whether it is relevant. From the titles, domains and snippets
   alone, build a candidate line per URL — `URL | publisher identity | evidence class (§5) | claim(s)
   it could close | date/period signal` — then drop, without fetching:

   - class **X** (SEO pages, aggregators, listicles, directories, forums, AI summaries) — a lead only,
     never opened as evidence;
   - a source whose class is wrong for the claim's authority (§5 table), when a correct-authority
     candidate is present in the same list;
   - duplicates: same origin document, same publisher's mirror, or a secondary that visibly quotes an
     origin already in the list — keep the origin, drop the rest;
   - a snippet already showing the wrong geography, period, customer class or unit;
   - anything answering a claim already closed in the ledger.

   Then rank the survivors by class → directness → recency and keep **one** document — the
   correct-authority one. This holds for a decision-grade claim too: an A-class regulator order,
   registry entry or statistics release *is* the authority, and opening a second document to agree
   with it buys nothing (§5 — two URLs from one origin are not an independent check). Open a second
   only when the verification-strength rule below actually calls for one: no A-class authority exists
   for the claim, the first document contradicts another closed claim, or its scope/period/customer
   class is ambiguous on the point at issue. Everything else stays unopened in the ledger as an unused
   lead. If the gate leaves nothing usable, refine the query once rather than opening a weak source; a
   second empty gate is a named gap, not a third search.

4. **Read evidence, not snippets.** Open only the documents that passed the gate, and extract the
   exact section carrying the value and its conditions. For long documents, find the relevant
   article/table/fare schedule/customer class instead of reading the whole file.
5. **Extract immediately.** Reduce each useful source to a compact evidence record before moving on.
6. **Reuse and deduplicate.** Fetch a document once and reuse it for every claim it supports, then
   write its evidence records to the cache (§10) so the next report on this market does not fetch it
   again.
7. **Stop when sufficient.** A low-risk claim directly answered by the correct authoritative source
   needs no decorative extra searches. This does not apply to contractor enumeration, which stops on
   the §6.6 saturation rule instead.
8. **Target gaps only.** After the first pass, re-search only unresolved, stale, contradictory,
   semantically ambiguous, or under-verified decision-grade claims. Do not rerun a whole batch.

Verification strength:

- Low-risk factual claim: one direct appropriate A source, or appropriate B source for first-party
  facts, is normally sufficient.
- Decision-grade claim: require the appropriate authoritative source. If no authoritative public
  source exists, use two genuinely independent credible sources when possible; otherwise mark
  `Chưa xác minh` and name who/what must confirm it.
- One targeted re-check per doubtful claim is normally enough. Failure to close it becomes a named
  gap, not an invitation to unlimited searching.

### Budget: depth is bought per claim, not per run

Quota is a ceiling, never a target; stop earlier when claims are closed. The budget has two lines,
and the objective decides how big the second one is by deciding which claims are decision-grade (§4)
— it never raises the first.

| Budget line | `nhanh` — default | `sâu` — only when the user asks |
|---|---|---|
| Base, spent on any claim | 20–35 searches, 10–14 documents | 30–45 searches, 16–20 documents |
| Decision-grade allowance, on top | +10–20 searches, +6–10 documents | +20–30 searches, +12–16 documents |

The two lines do not lend to each other. Climate normals, telecom coverage and payment methods are
paid for out of the base line even in a licensing run; a taxi-licence deadline or a depot
interconnection cost is paid out of the allowance even in a screening run. Exhausting the base line is
never a reason to spend the allowance on a low-risk claim, and a decision-grade claim left open while
the allowance still has room is a budgeting error, not a gap.

Contractor enumeration (§6.6) carries its own budget on top of both and is not charged against
either; the competitor comparison (§7.7) runs inside the §9 quota.

**Opened documents are the real cost, not searches.** A search result list is small; a fetched page
or PDF is one to two orders of magnitude larger and it stays in context for the rest of the run.
Extract the needed section rather than carrying the document forward. When a document ceiling is
reached, finish the deliverable with explicit gaps instead of starting another broad round — and say
in the reply (§14) that the gap came from the ceiling, not from an absent public source.

### Dispatch — see `references/dispatch.md`

**At step 5, before the first batch fans out, read `references/dispatch.md` and follow it.** It
carries what goes out to a worker and what may be opened inline, the brief, the model override, the
required return shape, the fan-out rule and the shortfall path.

The rule it exists to enforce, so the trigger is not missed: the gate decides *whether* a document is
opened, dispatch decides *who pays* for opening it, and gating without dispatching still leaves every
document in the main context for the rest of the run.

## 10. Runtime ledger and the cross-run evidence cache

Both live in the report's **source-log folder**, `doox-sources/<market-slug>/`, beside the output
workbook or `.docx` — the only place besides the deliverables themselves that the research skills
write. The ledger is per-run; the cache is per-market and outlives every run. A combined run
(market + contractor + competitor) writes **one** ledger.

```
doox-sources/<market-slug>/
  evidence.jsonl          # cross-run cache, one JSON record per line
  ledger-<dd_mm_yyyy>.tsv # this run's claim ledger
```

### The ledger

One row per claim, opened by the §4 split and closed as the claim resolves:

`claim | grade | dg reason | batch | state | origin | result | status candidate | scope/unit/period | source/publisher/URL | publication/effective/access date | condition/definition | output cell(s)`

For an RX answer, `output cell(s)` names the section of the `.docx` the claim feeds (e.g.
`RX2:D5`, `RX3:table`). For calculated claims also record:

`formula | sourced inputs | assumptions | rounding | output unit`

Four of those columns exist to make the run auditable without holding counters in context:

- `grade` — `base` or `dg`. Set at the split (§4); it decides which budget line the claim spends from
  (§9). A `dg` row carries its one-word reason in `dg reason`; a `base` row leaves that column empty.
- `batch` — the authority batch the claim belongs to, so a batch can be dispatched and closed as a
  unit.
- `state` — `open` until resolved, then the §4 status. No `open` rows left is the definition of a
  finished run and the input to §13 gate A.
- `origin` — `fetch`, `cache`, `estimate`, or `gap`. Distinct URLs with `origin=fetch` are the
  documents actually opened, so the §14 budget figures are counted from the file rather than
  recalled.

`origin` and `state` must agree, and a row where they do not is a defect the run introduced: `gap`
requires `Chưa xác minh`, `estimate` requires `Ước tính`, and `fetch` or `cache` requires a source URL
in the row. Check it whenever a batch closes — it is one pass over the file and it catches an
estimate that quietly became a verified figure.

A source may support multiple claims. A claim may have multiple sources.

Because the counts are derivable, query the ledger for the budget when a batch closes rather than
tracking numbers in the conversation — claims by `grade`, documents by distinct URL where
`origin=fetch`, cache closures, estimates and gaps by `origin`. One pass over the file answers all of
them and answers §14 as well.

Keep the ledger as a **file**, appended as claims close, not as text repeated in the conversation. It
grows to hundreds of rows over a full report, and a ledger carried in context is re-sent on every turn
for the rest of the run and re-emitted whole each time it is updated. Write it once, append to it, and
read back only the rows a block or an audit actually needs.

**Resuming an interrupted run starts here, not at `market-research` §3.** Read the ledger and the
cache first, then inspect only the rows still unwritten. A claim the ledger already closed is never
re-researched and its sources are never re-opened; a block the ledger shows as written is never
re-inspected. Only genuinely unresolved claims re-enter §9, and they re-enter at step 0.

### The cache

A decree, a fare order, a registry page or a climate normal does not change between two reports on the
same market, but re-opening it costs exactly what it cost the first time — and opened documents are
the dominant cost of a run (§9). Every source opened in a run is written to `evidence.jsonl` once its
records are extracted, and every claim batch consults the cache before its first search (§9.0).

```bash
python "<RM>/scripts/cache.py" lookup <cache.jsonl> --as-of <data-lock date> [--claim-type T] [--q TEXT] [--url U]
python "<RM>/scripts/cache.py" add    <cache.jsonl> records.json
```

A record is the ledger row plus what the cache needs to age it:

`url | publisher | evidence_class | claim_type | value | scope | period | published | effective | accessed`

`claim_type` is what picks the re-verification window, so use the script's own vocabulary — `fx`,
`tariff`, `fee`, `tax`, `law`, `permit`, `licence`, `pricing`, `statistics`, `network`,
`contractor`, `spec`, `climate`. Fares and commissions are `pricing`; taxi/driver/platform licences
`licence`; fleet and registration counts `statistics`; an operator's coverage or fleet page
`network`. An unlisted type still caches, but falls back to the shortest window.

Three rules keep the cache from becoming a source of stale reports:

- **`FRESH` means "do not open this page again", never "this figure is current."** The figure is
  judged by §8 against the dates the lookup prints back, exactly as if the document had just been
  fetched. Gate D audits this specifically.
- **A `FRESH` hit is subject to the same verification strength as a fresh fetch** (§9). It closes a
  decision-grade claim only if it is the A-class authority for that claim; where the rule would have
  called for a second independent source, the cache does not excuse it. The cache reduces fetches,
  not evidence standards.
- **Never cache a class X source, an unverified extraction, or a value the run itself marked
  `Chưa xác minh`.** The cache holds evidence, not leads.

Add records as each batch closes rather than in one dump at the end, so an interrupted run still
leaves the market better cached than it found it.

## 11. Conflicts and normalisation

**Read the matching rows of `references/metrics.md` before putting two numbers in the same table.**
It gives each measure its definition, unit and the scope that must travel with it, and it names the
pairs that look comparable and are not — GMV against operator revenue, registered against active
fleet, advertised against net driver income, asking price against realised value, online against
charge success. A source whose own definition differs from the dictionary keeps its own definition,
and the difference is reconciled before the comparison rather than absorbed into it.

Before comparing values, normalise only when definitions permit it:

- geography (city vs metro vs national) and customer class;
- data period;
- currency and FX date;
- tax-inclusive/exclusive basis;
- per trip / per paid km / per total km / per vehicle-day / per active driver;
- fare quoted vs fare paid after promotion; gross bookings vs operator revenue;
- registered vs active vehicles and drivers;
- kW vs kWh, rated vs duty-cycle range, nominal vs usable battery capacity;
- official deadline vs observed licensing/delivery duration.

Every conversion is an `Ước tính`/calculated claim unless the source already publishes the converted
value. Record formula and inputs; never silently convert.

When sources disagree, do not average or silently choose. Record both material figures and resolve
downstream use by: **authority → directness → recency/effective status → scope match → methodology →
independence**. State the reason for the preferred figure. If the conflict remains decision-relevant,
mark it as a limitation/gap.

## 13. Final audit — see `references/final-audit.md`

**After the last block is written and before the reply, read `references/final-audit.md` and run
every gate in it.** Gates A–D always apply; gate E only for a contractor objective, and it defers to
`../contractor-search/references/contractor-enumeration.md`; gate F only for a competitor objective,
and it defers to `../competitor-research/references/competitor-comparison.md`. Running out of budget
is a reason to ship with named gaps, never a reason to skip the audit.

## 14. Completion and reply

The deliverable is complete only when:

- framework coverage = 100% (workbook), or every required part of the RX form is present (`.docx`);
- factual-claim coverage = 100% processed;
- numeric coverage = 100% processed;
- unsupported numbers/factual claims = 0;
- unresolved decision-grade items are explicitly `Chưa xác minh` rather than guessed;
- arithmetic/unit/date/scope inconsistencies are resolved or openly reported;
- discovery-only sources do not appear as evidence;
- conclusion lineage is traceable to populated rows;
- for a contractor objective: audit E passes and the coverage block on `Bảng 3B` is filled;
- for a competitor objective: audit F passes.

"100% processed" means every required claim is verified, estimated with evidence, positively not
applicable, or explicitly unresolved. It does **not** mean public information exists for every
project-specific fact.

A deliverable outside the workbook is written in its RX form (§1) and is complete on that form's
terms: its evidence carries scope and date, its material gap is still visible, its conclusion stays
conditional on the evidence behind it, and its length is the form's `default_length` unless the user
set another. Name the form used in the reply, and the `.docx` it was written to.

Every figure in the reply is **counted from the ledger** (§10), never recalled: claims by `grade`,
documents by distinct URL where `origin=fetch`, cache closures where `origin=cache`, gaps where
`origin=gap`. State: output file(s), mode (`nhanh`/`sâu`), data-lock date, claims marked
decision-grade out of the total, searches and documents opened **split into base line versus
decision-grade allowance**, candidates gated out, claims closed from the cache without a fetch, unique
evidence sources, decision-grade claims still `Chưa xác minh`, whether any gap came from hitting a
ceiling rather than from absent public evidence, and whether all final audit gates passed. The calling
skill adds its own lines (contractor: `contractor-search` §6; competitor: `competitor-research` §7).
Offer follow-up work only when the user asks or when it directly closes a named gap already present in
the deliverable.
