---
name: market-research
description: "Use when a user asks to research an electric-taxi market for our own-fleet taxi operation — đánh giá / nghiên cứu thị trường hoặc khu vực, thông tin và từ khoá quan trọng của thị trường, market report or screening, entry (Côte d'Ivoire / Bờ Biển Ngà, Philippines, Kenya…), taxi and ride-hailing licensing, vehicle sourcing, depot and fleet charging, cost/TCO, étude de marché, or a single sourced question about such a market; to tìm nhà thầu / đối tác (xây depot & lắp sạc cho đội xe, tổng thầu turnkey, OEM, financier/insurer, workshop, dispatch tech, legal/tax adviser) or review a named one; or to so sánh đối thủ / mình so với đối thủ / how we compare (Grab, Bolt, Uber, Yango, local taxi firms, analyse de la concurrence). Produces the market workbook `.xlsx` (contractor list in `Bảng 3B`) or an RX1–RX5 `.docx`. Load `using-doox` first. Researches public sources, not the user's files: quotes or bids handed over → `bid-review`; summarising, key terms or fact-checking of a supplied document → `doc-compare`."
---

# Market Research — thị trường, nhà thầu, đối thủ

**`using-doox` is loaded first and routes here.** This skill uses from it only "Language"; it runs
no identity gate and opens no plan file.

One skill, three jobs, all for an electric-taxi operator that **runs its own fleet** — it owns the
cars, employs the drivers, runs app and dispatch, and charges its vehicles at its own depots.
Charging only ever means charging *for the fleet* (depot, opportunity, public back-up), never a
charging-station business.

| Job | Typical ask | Read before starting it | Output |
|---|---|---|---|
| **Đánh giá thị trường / khu vực** | market report, screening, entry, licensing, vehicles, depot, TCO, key facts and terms of a market | `references/workbook.md` for a full report; `assets/form-research.md` for anything else | workbook `.xlsx`, or RX1 / RX4 / RX5 `.docx` |
| **Tìm nhà thầu / đối tác** | full contractor list, shortlist, review of a named firm | `references/contractor-enumeration.md`, RX3 in `assets/form-research.md` | `Bảng 3B` of the workbook + RX3 summary; RX3 `.docx` for a named review |
| **So sánh đối thủ** | how we compare, competitor landscape | `references/competitor-comparison.md`, RX2 in `assets/form-research.md` | RX2 `.docx` |

A request naming two or three jobs is **one run**: one scope question, one claim split, one ledger,
one cache sweep, one final audit. Read the reference of each job named, and only those. Each job
runs at its full method — combining saves the scope question, split, ledger and audit, never the
method.

## How to read this skill

Rules here come in three strengths. Know which is which, and use your own judgement for the rest.

**Hard limits — never cross them, whatever the request or the budget:**

- Never write a factual claim — a number, licence or permit, quota, fare, driver pay, vehicle
  availability or delivery time, depot power capacity, site hazard, cost, commercial term, operator
  fact or project reference — that is not traced to a source opened in this run, a `FRESH` cache record (§10), or a labelled calculation.
  Never fill a gap from model knowledge. A gap is written as a gap.
- Class X sources (§5) are leads, never evidence.
- Every cited URL was opened in this run, or returned `FRESH` by the cache and is still inside the
  report's data window.
- Conclusions use only evidence already populated, add no new facts, and never carry a stronger
  status than their weakest material premise.
- Never declare a market ready for launch, or a depot ready to build, without confirmed transport
  licensing, vehicle supply, land/right-of-use, electrical capacity and interconnection, and cost.
- Our own side in a competitor comparison comes from the user or their documents only — never from
  model knowledge (`references/competitor-comparison.md` §7.1). Figures recalled from memory or past
  conversations may be shown to the user to confirm; unconfirmed, they are not used.
- Deliverables are files on the user's machine (§1), never Claude Docs, an artifact or a remote
  document. Never overwrite an existing file; never edit the bundled assets.
- The workbook is an output contract: its four status words stay in Vietnamese, its rows are not
  inserted, deleted, renumbered or reordered (only `Bảng 3B` repeats rows), and its output name never
  splits into three parts on ` - ` (`using-doox` would read it as a plan file).
- Research output is evidence for human review — not an investment verdict, legal opinion, licence,
  utility commitment or vendor quote. Recommend nothing the evidence does not carry.

**Defaults — follow them unless you have a reason, and say the reason in the reply:** the budget
figures (§9), the RX `default_length`, the run order, `nhanh` mode, the order of the enumeration
frames and the loose frames F6–F10 / C4–C7, the scoring thresholds (a changed threshold changes what
audit E calls Nhóm A — say so). Working the registry frames F1–F5 and C1–C3, or recording them as
unavailable, stays required: they are what makes a list or a comparison checkable. They encode what has worked; a market or a question they do not
fit is a reason to adapt them, not to force the fit.

**Everything else is explanation** — the reason behind a rule, so you can apply it to a case this
file did not foresee. Where a situation is not covered, choose what best serves a reviewable,
sourced deliverable at the least cost in searches and opened documents.

## Files and section numbers

`§` numbers are fixed and live in one place each:

| § | File |
|---|---|
| §1, §2, §4, §5, §8, §9, §10, §11, §13, §14 | this file |
| §3 read the framework, §12 fill the workbook | `references/workbook.md` |
| §6 contractor enumeration, audit E | `references/contractor-enumeration.md` |
| §7 competitive position, audit F | `references/competitor-comparison.md` |

Other files, each read at the point it is needed, never end to end:

- `assets/khung-bao-cao-thi-truong.xlsx` — the market workbook template (copy it; never edit it).
- `assets/form-research.md` — RX1–RX5, the shape of any answer that is not the workbook.
- `references/topic-lenses.md` — R01–R52: per topic, what to sweep and the counting trap it carries.
  Look up the rows the output touches.
- `references/metrics.md` — K01–K56 definitions. Look up the rows before putting two numbers side by
  side.
- `references/dispatch.md` — how to hand gated documents to workers (§9).
- `references/final-audit.md` — gates A–F (§13).
- `scripts/wb.py` — workbook cell lister, inspector and batch writer (§3).
- `scripts/cache.py` — cross-run evidence cache (§10).

Bash runs in the user's working folder, not in this skill's directory, so call the scripts by the
absolute path of this skill's Base directory: `python "<skill dir>/scripts/wb.py" …`.

The ledger and the evidence cache are runtime state stored beside the user's reports (§10), never
plugin files.

## 1. Contract

**Every run leaves a file on the user's machine**, in the working folder the user opened for the
session (in Cowork, what shows under Output); with no folder opened, the session's outputs folder.
The chat reply summarises the file and names it; it never replaces it.

Two deliverable shapes, not interchangeable:

- **The market workbook** — a full market evaluation, and the home of the contractor list
  (`Bảng 3B`). How to read and fill it: `references/workbook.md`.
- **An RX answer in its own `.docx`** — everything else: RX1 a question, a landscape or a brief of key
  facts and terms; RX2 a comparison (the competitor job); RX3 a named counterparty or a shortlist;
  RX4 an entry or scenario thesis; RX5 what changed against a dated baseline. The form decides the
  shape of the answer only — evidence rules, ledger, budget and statuses are unchanged by it. Name:
  `Nghiên cứu [Chủ đề] [Thị trường] dd_mm_yyyy.docx` (the name keeps this pattern whatever the reply
  language; `[Chủ đề]` may be in the user's language) beside the workbook if there is one; `.md` of the
  same name only when a `.docx` cannot be produced; add ` (2)`, ` (3)`… rather than overwrite. The
  enumerated contractor list is the one exception: it lives in `Bảng 3B` only, and RX3 shapes its
  summary in the reply.

**Length follows the form's `default_length`** (`assets/form-research.md`); the word counts are for
English — Vietnamese and French run about a third longer for the same content. A user-stated length wins;
depth beyond it goes to an appendix; a material gap is never cut to fit. Padding a comparison into a
report fails the form as much as dropping its gap line.

**Two kinds of gap, two markers.** Missing public evidence is a claim status, `Chưa xác minh`, with
who or what must confirm it. A missing **user input** the answer needs — own fleet size, launch date,
own fare — is `[INPUT NEEDED: <field>]` at the point it is needed, never guessed, never zero. The
workbook uses only the four statuses; `[INPUT NEEDED: …]` belongs to RX answers and the reply.

### Language

Three languages meet in one run. **The reply and RX deliverables follow the user** — vi, en or fr,
the language of the request (`using-doox`, "Language"). **The workbook keeps its own**: the bundled framework is Vietnamese, so
sheet names, field labels and the statuses `Đã xác minh` / `Ước tính` / `Chưa xác minh` /
`Không áp dụng` are written exactly as the framework has them — a status rendered as `Verified` breaks
every downstream read. A user-supplied framework is filled in its own language. **Searching follows
the market**: French for Côte d'Ivoire, English (and Filipino where the source is) for the
Philippines, English (and Swahili where the source is) for Kenya — that is where the primary sources
are. A figure, legal citation or quoted clause keeps its published language; a translation is
labelled as one and never replaces the original in the ledger. In an English or French RX answer give
each status as the Vietnamese term with the reader's gloss on first use — `Chưa xác minh (not
verified)`.

## 2. Scope

Use facts already supplied; never ask again for them. Resolve only what materially changes the
research:

- market and geographic scope (country, city, metro area);
- objective(s): market screening, entry/expansion, legal/licensing (taxi, platform, driver, vehicle),
  fleet and vehicle sourcing, depot and fleet charging, cost/TCO and unit economics, key facts and
  terms of the market, contractor/partner search (§6), competitor comparison (§7);
- data-lock date (default: latest public data as of today);
- project facts already known: planned fleet size and vehicle model, service model (street taxi,
  app, airport, corporate), launch phase, depot plans and candidate sites;
- for a contractor search, the target profile (§6.1); for a competitor comparison, our own-side
  profile (§7.1).

Ask everything still missing and essential in **one** structured-question call — not a prose list,
not one question per turn. Where a sensible default exists, take it and say so instead of asking.
When the fields outnumber what the question tool holds (the own-side profile has ten), ask *how* the
user will supply them — a file, pasted in chat, or not at all — and list the fields in the question
text. Project facts that only sharpen the answer can stay `[INPUT NEEDED: …]` rather than be asked.

**Settle the deliverable together with the objective.** A full market evaluation fills the workbook.
A single question, a brief on the market's key facts and terms, an entry thesis or a change against a
dated baseline takes one RX form instead. Choose by the result the user needs, not by topic; each lens
row names its likely forms in `form_ids`.

**Key facts and terms.** When the user asks for the important information or keywords of a market,
give an RX1 brief whose appendix lists the official local terms that matter for the operation — the
term in the market's language, what it means for us, the issuing authority and source. These terms
are also the search vocabulary of the run (§9), so collecting them early pays twice.

**Mode is `nhanh`** unless the user asks for `sâu`. The objective does not change the mode; it decides
which claims are decision-grade (§4), and depth is bought for those claims from their own allowance
(§9). A licensing run pays for depth on taxi, platform and driver authorisation, not on climate
normals; a depot run pays for it on interconnection, land use and permit cost.

If a city- or depot-level conclusion has only national evidence, keep the local claim
`Chưa xác minh`; never scale national data down silently.

### Run shape

The usual order, one pass each except the 5–6 loop:

1. Scope, objective(s), deliverable, data-lock date, mode (§2).
2. Workbook only: copy the template, list writable cells, inspect the report sheet (§3).
3. Split the deliverable into claims, mark the decision-grade set, batch by authority, open the
   ledger (§4, §10).
4. Sweep the cache for the whole split (§9).
5. Per authority batch: search → gate → open or dispatch → extract → close ledger rows → cache.
   Contractor enumeration (§6) and the competitor set (§7) hang off this step.
6. Write each finished block (§12) or RX section, auditing it as you write.
7. One targeted pass over what is still open (§9).
8. Final audit from the ledger (§13), then reply (§14).

Going back to steps 2–3 mid-run means re-reading what is already in the ledger — avoid it unless the
scope itself changed.

## 4. Atomic claims

Split the whole deliverable into **atomic claims** in the same pass that reads the framework or
settles the RX form. Every number, percentage, date, range, currency value, legal assertion,
licence/permit status, named operator/partner fact and factual premise of a conclusion is a claim.

Look up the matching rows of `references/topic-lenses.md` while splitting. Each carries the counting
trap of its topic — registered versus active fleet, advertised versus net driver income, gross
bookings versus operator revenue, application versus approval, national versus city — and the trap
decides how a claim is worded, which is cheaper at the split than as a rewrite at the audit.

**Batch claims by the authority that will answer them**, not by row: one regulation, registry page
or statistics release usually closes claims spread across unrelated rows.

**Write the split into the ledger (§10) as open rows** rather than holding it in the conversation —
it is the largest artefact before research starts, and in the ledger it is queryable, survives an
interruption and doubles as the coverage checklist. The run is finished when no row is open.

Each claim ends as exactly one status from `00 - Hướng dẫn`:

- `Đã xác minh` — directly supported for the stated scope/period and valid for that wording;
- `Ước tính` — reproducible calculation or inference with sourced inputs and stated assumptions;
- `Chưa xác minh` — public evidence insufficient or local confirmation required;
- `Không áp dụng` — positive evidence shows the requirement does not apply.

An RX answer also labels analytical sentences **`Suy luận`** or **`Kịch bản`**
(`assets/form-research.md`); those labels sit beside the statuses, never carry `Đã xác minh`.

**Decision-grade claims** get the strongest verification, first, out of their own budget line. A
claim is decision-grade when it affects one of: `legal`, `licence`, `permit`, `interconnection`,
`cost`, `tax`, `schedule`, `homologation`, `feasibility`, `contractor`, `partner`, `competitor`,
`conclusion` — record that one-word reason in the ledger row. "The report is about X" is not a
reason; what *that claim* affects is. If more than roughly a third of the split ends up `dg`, recheck the reasons before the first search:
a split that heavy is marking the topic rather than the claim and roughly doubles the cost for no
verification gain.

For contractors, **supply-chain role** (§6.1) is its own decision-grade claim, never inferred from a
first-party capability statement. A candidate list is built from the §6 frames, not from a generic
web search.

## 5. Source quality and claim authority

A reputable source is not automatically authoritative. Verify each claim with the source that has
authority or direct knowledge for **that claim**:

| Claim type | Preferred evidence |
|---|---|
| law, licence requirement, permit, official fee, tax | current legislation/gazette, issuing authority, regulator, municipality, tax authority |
| taxi / ride-hailing licensing, operator and driver authorisation, fare rules | transport ministry or land-transport regulator, city transport authority, published fare orders and licensed-operator lists |
| vehicle registrations, taxi plates, fleet counts, population | vehicle-registration / transport / statistics authority |
| vehicle type approval, homologation, import status | homologation/standards authority, customs; OEM material for specifications |
| electricity tariff, depot interconnection, grid outlook | regulator-approved tariff/order, utility, system operator |
| public charging used as fleet back-up | government/open dataset; the network owner for its own network; credible independent source only without primary data |
| operator scale, fares, service area | licensing authority and filings first; the operator's app/fare page for its own offer; press only for direction |
| contractor/vendor services and contact | first-party site for self-described capability/contact; licence status from the issuing registry; project experience from owner/tender/permit evidence |
| contractor supply-chain role and turnkey capability | never first-party self-description alone — §6 |
| driver pay, labour rules, social contributions | labour ministry/code, social-security authority; platform pages only for their own advertised terms |
| payment / telecom | regulator and provider first-party terms/coverage |
| climate, hazards, public and road safety | meteorological, environmental, police/road-safety or municipal authority |
| costs | official fees/tariffs, published prices, quotations, transparent industry studies; model assumptions labelled as assumptions |

Evidence classes:

- **A — authoritative primary:** government, regulator, legislation, statistics, utility/system
  operator, official registry, licensed-operator list.
- **B — first-party:** OEM, taxi/ride-hailing operator, contractor, supplier, bank/telco; valid only
  within its direct self-knowledge.
- **C — credible independent:** academic/professional bodies, IEA/World Bank-type bodies, reputable
  journalism and industry associations.
- **X — discovery only:** SEO pages, aggregators, generic blogs, social posts, forums, directories,
  AI summaries and listicles. X may point to a lead; it never supports a fact.

Confirm publisher identity and document provenance before relying on a source — ranking, branding or
a plausible URL is not proof. Follow a secondary source's citation to the origin and use the origin;
two URLs from one origin are **one** source, not a cross-check. User-supplied documents may be
evidence, identified as supplied, and never override a current regulator on regulatory claims.

## 8. Freshness, scope and meaning

For every sourced claim capture, when they apply: data/reference period, publication date,
effective/version date, access date (say so when a page has no date), and geography, customer class,
unit and conditions.

A current webpage does not make an old figure current. Fares, tariffs, fees, law, licences, permits
and FX use the current effective version; fleet, driver and trip counts use the latest official
period found, stated explicitly; specs use the right model, version and market. A latest-public figure
older than the report date is written as dated, with the current-data gap named. A cache `FRESH`
verdict only means "no need to reopen this page" — the figure is still judged by these dates.

Preserve source definitions. These are not synonyms without evidence: registered / licensed / active
/ on-road fleet; ordered / delivered / in-service vehicles; driver / licensed / active driver; trip /
booking / completed trip; gross bookings / operator revenue / driver earnings; advertised / gross /
net driver income; quoted / final / post-promotion fare; taxi / ride-hailing / private hire as legal
categories; BEV / PHEV / hybrid; rated / duty-cycle range; and, for fleet charging, site / connector /
simultaneous power, charger output / vehicle acceptance, energy rate / demand charge / fixed charge /
tax / total delivered cost.

## 9. Research engine — minimum search for sufficient evidence

Every search answers an open claim. The goal is the correct-authority document for each claim at the
least cost — and **opened documents are the real cost**: a result list is small, a fetched page or PDF
is one to two orders of magnitude larger and stays in context for the rest of the run.

How that usually plays out:

- **Cache first.** Before the first search, look up every `claim_type` in the split at once (§10). A
  `FRESH` hit closes its claim without a fetch, subject to the verification strength below; a `STALE`
  hit still names the exact URL to go back to. Mark those rows `origin=cache`.
- **Known authority → go direct** to the regulator, ministry, utility, registry, statistics office,
  municipality or company site; domain-restricted queries help.
- **Unknown authority → one discovery pass** in the market's language to learn the agency, dataset,
  document name or official term, then move to the primary source. Short, one-claim queries work best
  — e.g. `"licence de taxi" Abidjan arrêté`, `LTFRB "Transport Network Vehicle Service" memorandum
  circular`, `NTSA "PSV licence" taxi Kenya`. Contractor work uses the §6 frames and competitor work
  the §7 frames instead.
- **Triage the result list before opening anything.** From titles, domains and snippets, drop class
  X, wrong-authority sources when a right one is present, duplicates of an origin already listed,
  snippets already showing the wrong geography/period/class/unit, and anything answering a closed
  claim. Keep the one correct-authority document. Open a second only when there is no A-class
  authority for the claim, the first contradicts another closed claim, or its scope is ambiguous on
  the point at issue. If nothing usable survives, refine the query once; a second empty result is a
  named gap.
- **Read the relevant section, extract immediately**, reuse each document for every claim it
  supports, and add its records to the cache as the batch closes.
- **Stop when sufficient**; after the first pass re-search only what is unresolved, stale,
  contradictory, ambiguous or under-verified. Contractor enumeration stops on saturation instead
  (§6.6).
- **Hand gated documents to workers** so their text does not land in the main context — read
  `references/dispatch.md` before the first batch fans out.

**Verification strength.** A low-risk fact needs one direct A source (or B for a first-party fact).
A decision-grade claim needs the authoritative source; with none public, two genuinely independent
credible sources; otherwise `Chưa xác minh` with who/what must confirm it. One targeted re-check per
doubtful claim is normally enough — failure then is a named gap, not a licence to keep searching.
An authority that exists but cannot be opened (403, login wall, dead link) is not "absent": the claim
stays `Chưa xác minh`, naming the blocked URL, even if press quotes it — press quoting one order is
one source. A failed open does not count as an opened document.

### Budget

Default ceilings, never targets — stop earlier when claims are closed:

| Line | `nhanh` (default) | `sâu` (user asks) |
|---|---|---|
| Base, any claim | 20–35 searches, 10–14 documents | 30–45 searches, 16–20 documents |
| Decision-grade allowance, on top | +10–20 searches, +6–10 documents | +20–30 searches, +12–16 documents |

Keep the lines separate: a low-risk claim does not draw on the decision-grade allowance, and a
decision-grade claim left open while its allowance has room is a budgeting error, not a gap.
Contractor enumeration has its own budget (§6.6); the competitor comparison's claims are
decision-grade and draw on the allowance (§7.7). A combined run's ceiling is the sum of the lines it
uses. If a market clearly needs more (a thin web, a second language, a federal and a state layer),
exceed the default once and say by how much and why in the reply; the ceiling you declared is then
final. When a ceiling is hit, finish with
explicit gaps and say the gap came from the ceiling, not from absent evidence.

## 10. Runtime ledger and evidence cache

Both live in `doox-sources/<market-slug>/` beside the deliverable (slug = the country, e.g. `kenya`, so
national registries and laws are shared by every city report; the city goes in each record's scope) — the only place besides the
deliverables that this skill writes (scratch files for building a `.docx` go to the system temp
folder and are removed after). The ledger is per run; the cache is per market and outlives runs.
A combined run writes one ledger.

```
doox-sources/<market-slug>/
  evidence.jsonl          # cross-run cache, one JSON record per line
  ledger-<dd_mm_yyyy>.tsv # this run's claim ledger
```

### The ledger

One row per claim, opened by the §4 split, closed as the claim resolves:

`claim | grade | dg reason | batch | state | origin | result | status candidate | scope/unit/period | source/publisher/URL | publication/effective/access date | condition/definition | output cell(s)`

Calculated claims also record `formula | sourced inputs | assumptions | rounding | output unit`. For
an RX answer `output cell(s)` names the section it feeds (`RX2:D5`, `RX3:table`).

- `grade` — `base` or `dg` (with its reason); decides the budget line.
- `batch` — the authority batch, so a batch is dispatched and closed as a unit.
- `state` — `open` until resolved, then the §4 status.
- `origin` — `fetch`, `cache`, `estimate` or `gap`. It must agree with `state`: `gap` →
  `Chưa xác minh`, `estimate` → `Ước tính`, `fetch`/`cache` → a URL in the row. Check this when a
  batch closes; it catches an estimate that quietly became a verified figure.

Keep the ledger as a file, appended as claims close, and read back only the rows a block or audit
needs. Budget and reply figures are counted from it, not recalled.

**Resuming an interrupted run starts from the ledger and the cache**: closed claims are not
re-researched, written blocks are not re-inspected, and only open claims re-enter §9.

### The cache

```bash
python "<skill dir>/scripts/cache.py" lookup <cache.jsonl> --as-of <data-lock date> [--claim-type T] [--q TEXT] [--url U]
python "<skill dir>/scripts/cache.py" add    <cache.jsonl> records.json
```

A record is `url | publisher | evidence_class | claim_type | value | scope | period | published |
effective | accessed`. `claim_type` picks the re-verification window, so use the script's vocabulary —
`fx`, `tariff`, `fee`, `tax`, `law`, `permit`, `licence`, `pricing`, `statistics`, `network`,
`contractor`, `spec`, `climate` (fares and commissions are `pricing`, fleet counts `statistics`, an
operator's coverage page `network`). An unlisted type falls back to the shortest window.

- `FRESH` means "do not open this page again", never "this figure is current" (§8).
- A `FRESH` hit meets the same verification strength as a fetch: it closes a decision-grade claim
  only if it is that claim's A-class authority.
- Never cache class X, an unverified extraction, or a value the run marked `Chưa xác minh`.

Add records as each batch closes, so an interrupted run still leaves the market better cached.

## 11. Conflicts and normalisation

Look up the rows of `references/metrics.md` before putting two numbers in one table. A source whose
definition differs from the dictionary keeps its own, and the difference is reconciled before the
comparison.

Normalise only when definitions permit: geography and customer class; period; currency and FX date;
tax basis; per trip / paid km / total km / vehicle-day / active driver; quoted vs paid fare; gross
bookings vs operator revenue; registered vs active; kW vs kWh, rated vs duty-cycle range, nominal vs
usable battery; official deadline vs observed duration. Every conversion is an `Ước tính` with formula
and inputs unless the source publishes the converted value.

When sources disagree, never average or silently pick. Record both and prefer by **authority →
directness → recency/effective status → scope match → methodology → independence**, stating why. A
decision-relevant conflict that remains is a named limitation.

## 13. Final audit

After the last block is written and before the reply, read `references/final-audit.md` and run its
gates: A–D always, E for a contractor list, F for a competitor comparison. Running out of budget is a
reason to ship with named gaps, never to skip the audit.

## 14. Completion and reply

The deliverable is complete when every required cell or RX part is filled; every claim is verified,
estimated with evidence, positively not applicable, or explicitly `Chưa xác minh`; no unsupported
number or fact remains; arithmetic, units, dates and scope are consistent or the inconsistency is
reported; no class X source appears as evidence; and every conclusion traces to populated rows.
"Complete" does not mean public evidence exists for every project fact.

The reply names the file(s) and the RX form used, and gives, **counted from the ledger**: mode,
data-lock date, decision-grade claims out of the total, searches and documents opened split into base
line and decision-grade allowance, candidates gated out, claims closed from the cache, unique sources,
decision-grade claims still `Chưa xác minh`, whether any gap came from a ceiling, any default you
departed from and why, and whether all audit gates passed. Then, per job present:

- **contractor list** — the frame mapping used outside Vietnam, frames worked, companies listed, how
  many `Tổng thầu turnkey`, how many in Nhóm A, whether saturation was reached, residual blind spots;
  for a counterparty review, the lens used and which items stayed claimed rather than proven;
- **competitor comparison** — competitors compared per bucket, which of C1–C3 were worked, how many
  D-rows ended `Chưa kết luận được` for lack of competitor data, whether the own side was supplied in
  full.

Offer follow-up work only when asked, or when it directly closes a gap named in the deliverable.
