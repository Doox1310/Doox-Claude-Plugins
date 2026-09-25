# Competitive position — mình so với đối thủ (§7)

§7 and §13F of `competitor-research`. Applies whenever the objective includes a competitor
comparison. Decision-grade throughout. `§5`, `§8`, `§9`, `§10`, `§11` are `research-method`'s (the
`§` numbers are shared across the research skills); `§6` is `contractor-search`'s.

The question this section answers is not "who else is in this market". It is **"where do we stand
against them, on what evidence, and where does that leave us exposed"**. A list of competitors with
their fleet sizes is the input, not the output.

Output goes to **its own `.docx` as tables** in RX2 shape (`competitor-research/SKILL.md`),
summarised in the chat reply, not into the workbook — the bundled framework has no competitor block.
Everything else in `research-method` still applies: sourcing (§5), freshness (§8), the evidence
record (§10), conflicts (§11).

## 7.1 "Mình" has to be stated, never assumed

The comparison needs our own side, and **our own side comes only from the user, from documents in the
session, or from a plan file they point at.** Never from model knowledge about the company, however
confidently it comes to mind — that knowledge is stale by construction, and a comparison built on a
half-remembered own-side is worse than no comparison.

Ask for the own-side profile in the same structured call as `market-research` §2's other unknowns,
along the same dimensions the competitors will be measured on (§7.3) — planned or active fleet, cities
covered, vehicle models, target segment, fare and commission, service levels, booking channels, driver
model, backing, licences and contracts held. Whatever the user does not supply stays
`Chưa có dữ liệu nội bộ` in its row — a visible blank, never a guess and never silently dropped.

The own-side unknown entirely: the section still runs, produces the **competitor landscape only**,
and says in one line that no comparison was made because the own-side was not supplied. Do not
quietly turn a comparison request into a landscape report and let the heading imply otherwise.

A market we have not launched in yet is still a comparison: our side is the **planned** offer, labelled
as planned in every cell, and it is compared against their **operating** side — never planned against
planned, and never planned presented as operating.

## 7.2 Define the competitor set before enumerating it

A competitor is a company chasing **the same rider for the same trip in the same market**. Say which,
in three buckets, and put every company in exactly one:

| Bucket | Meaning | Example shape |
|---|---|---|
| `Trực tiếp` | car-based on-demand passenger trips, same city, same rider segment | hãng taxi & gọi xe ô tô — Grab, Bolt, Uber, Yango, inDrive, local metered-taxi firms and cooperatives, other electric-taxi fleets |
| `Gián tiếp` | different mode, same trip need | xe ôm công nghệ / moto-taxi, xe buýt/BRT, minibus (matatu, jeepney, gbaka, wôro-wôro), private car |
| `Thay thế / tiềm năng` | not competing yet but holds the assets to start | vehicle OEM or distributor with its own mobility arm, transport or conglomerate group, car-rental fleet, airport or hotel transport concession holder |

**Segment before scale.** A platform ten times our size whose trips are mostly motorbike or
budget-hatchback rides is a weaker `Trực tiếp` competitor than a small fleet serving the same airport
and corporate riders. Ranking the set by fleet or trip count before segmenting it produces the wrong
list every time.

Enumeration is frame-first, exactly as `contractor-search` §6.2 argues — generic search surfaces
whoever bought the SEO:

| # | Frame | What it yields | Class |
|---|---|---|---|
| C1 | Transport licensing authority: lists of licensed taxi operators, ride-hailing/TNVS platforms and their accredited fleets, fare orders | who is legally allowed to operate, with territory and licence class | A |
| C2 | Vehicle-registration / taxi-plate data: registrations by operator or category, taxi plate or permit allocations, EV registrations in the taxi category | how many vehicles each actually has on record — the hardest thing to fake | A |
| C3 | Tenders and concessions: airport taxi concessions, corporate and government transport contracts, city e-mobility programmes | who holds privileged access now, at what terms and until when | A |
| C4 | Company filings of listed/state operators: annual reports, prospectuses, regulatory returns | fleet, trips, revenue model, stated plans — with a date | A |
| C5 | First-party: the operator's app, fare page, coverage map, driver-recruitment page | the service as its owner describes it — authoritative for its own offer only | B |
| C6 | App-store ratings and review counts, independent service reviews and mystery-shop tests | service quality signals, self-selected — never a population rate | C |
| C7 | Press announcing launches, fleet orders, electrification, OEM or investor tie-ups | direction of travel — plans, not assets | B/C |

C1–C3 are the required core: they carry assets and rights, not announcements. Skipping one is allowed
only when the frame demonstrably does not exist in the jurisdiction, and that is recorded as a coverage
note.

## 7.3 The comparison dimensions — fixed, applied to everyone alike

Ten dimensions, same ten for us and for every competitor. A dimension measured for one side and not
the other is not a comparison and does not go in the table. Metric definitions come from
`research-method/references/metrics.md`; the K-codes name the rows to read.

| # | Dimension | What is actually compared |
|---|---|---|
| D1 | Đội xe hoạt động | **active fleet** (K05), with the definition the source uses; trips where published (K01) |
| D2 | Vùng phủ | cities/zones with bookable service, airport and pickup rights; same administrative level for every side |
| D3 | Điện hoá & xe | share of the active fleet that is BEV, vehicle models and class, vehicle age |
| D4 | Phân khúc khách | street hail vs app vs airport vs corporate — who the main rider is, and at what price tier |
| D5 | Giá cước & hoa hồng | fare per trip and per paid km on the same reference trip (K12, K13), surcharges, promotions; platform take rate (K14) |
| D6 | Chất lượng dịch vụ | acceptance, cancellation, completion, pickup wait (K39–K42); rating/NPS (K37); public complaints and safety incidents |
| D7 | Kênh đặt xe & công nghệ | app, call centre, street hail, corporate portal, payment methods, dispatch model |
| D8 | Mô hình tài xế & thu nhập | employee vs partner vs lease-to-drive; active drivers (K06); driver net income on a stated basis (K15) |
| D9 | Hậu thuẫn | ownership, capital, parent group, OEM/utility/government relationships |
| D10 | Rào cản cơ cấu | licences and plate/permit quotas held, airport and corporate contracts, depots and charging access, exclusive arrangements |

D10 is where the durable advantage usually sits and where public data is thinnest — an empty D10 is a
real finding, recorded as `Chưa có dữ liệu công khai`, never inferred from the absence. A trend in D1
needs two dated observations, not a press release.

## 7.4 Normalise before comparing — and split active from announced

Two failures account for almost every wrong competitive read in this industry. Both are avoidable.

**7.4a — The unit.** `12.000 tài xế đăng ký` and `3.000 xe đang chạy` are not comparable figures.
**Active vehicles (K05) are the comparison unit for D1**; registered drivers, app downloads, licensed
plates and "partners" are different populations. Where a source gives only one of those, record it as
that population, mark the cell `Không so sánh được — chỉ có số tài xế đăng ký` (or the population it
is), and do not convert with an assumed ratio. A platform's drivers are also another platform's
drivers: never add multi-app driver counts across competitors. Same discipline for fares (same
reference trip, same currency, same tax basis, promotion stated), for commission (the base it is taken
on) and for coverage (same administrative level).

**7.4b — Đang vận hành ≠ đã công bố.** An operator announcing 1.000 electric taxis by next year and
running 180 today is an operator with 180. Every scale figure carries its state, in its own column,
and the comparison runs on the operating column:

| State | Counts in the comparison |
|---|---|
| `Đang vận hành` | yes — this is the comparison |
| `Đã đặt mua / đang giao` | shown in its own column, read as pipeline |
| `Đã công bố kế hoạch` | shown, never added to either of the above |

Aggregating the three into one headline number is the single most common way a competitor is
overstated, and it is done by the competitor's own press office on purpose.

Every scale figure also carries **as-of date**. Two competitors measured six months apart are not a
comparison; pull both to the report's data-lock date or mark the gap.

## 7.5 The asymmetry rule — the one that matters

**Our own data is complete and internal. Theirs is partial and public. The two are never symmetric,
and the gap always flatters us.**

So: **a competitor's blank cell is never evidence of their weakness.** `Chưa có dữ liệu công khai`
means we cannot see it, not that it is absent. Any conclusion of the form "mình mạnh hơn ở D*n*" is
only allowed when the competitor's side of D*n* is **sourced**, not when it is empty.

Where an advantage rests on a dimension we can see for ourselves and cannot see for them, say exactly
that: `Chưa kết luận được — thiếu dữ liệu đối thủ ở D6`. That sentence is the honest output, and it
is more useful than a flattering table, because it names what to go and find out.

## 7.6 Output

Four parts, in the `.docx`, in this order.

**1. Bảng so sánh ngang.** Rows D1–D10, columns: `Mình` then one per competitor. Each cell carries
value, `Nguồn`, `Ngày`, and `Độ chắc chắn` (Đã xác minh / Ước tính / Chưa xác minh). Competitors
ordered by bucket then by D1 active fleet.

**2. Đọc bảng.** Not a restatement of it — four short lists, each line naming the dimension and the
measured gap:
- **Mình hơn** — dimension, how much, and on what sourced comparison;
- **Mình kém** — same, and what it costs operationally;
- **Ngang nhau** — where nobody has an edge, so competing there spends money for nothing;
- **Chưa kết luận được** — dimension, which side is missing, what source would close it.

**3. Khoảng trống và hướng đi của họ.** Segments, cities or pickup points nobody in the set serves —
with the reason, since an empty segment is usually empty for a reason. Then where each competitor is
putting capital, read from C3/C4/C7 with dates: fleet orders, electrification, new cities, concessions.
Pipeline is direction, and direction is what we are actually competing against, not today's fleet.

**4. Rủi ro cạnh tranh.** Each one: what would have to happen, how likely on current evidence, and
which of our dimensions it hits — a fare war, a platform locking up the airport, drivers poached by a
higher advertised income. A competitor holding D10 advantages we cannot match goes here, not in the
strengths list.

## 7.7 Boundaries and budget

**No verdict.** This section reports position and exposure. It does not recommend entering, exiting,
pricing, or acquiring — those are the reader's, and `research-method` §1's contract holds here as
everywhere.

**No modelled internals.** A competitor's cost per trip, margin, utilisation, driver churn or payback
is not public and is not to be estimated into the table as though it were. Where the user asks for
one, it is an explicit `Ước tính` row with the formula and every assumption written out, kept out of
the comparison table itself.

**No scoring from marketing.** An operator's own "hãng taxi điện lớn nhất" or "tài xế thu nhập đến …"
is class B wording about itself — recorded as a claim, never as a D1 or D8 value.

**Budget:** roughly **12–18 searches, 4–6 opened documents**, inside the §9 quota. Cap the set at
**5 `Trực tiếp`** competitors plus whatever `Gián tiếp`/`Thay thế` genuinely bear on the objective;
beyond that, list the remainder by name in one line and say the comparison was capped. Run another
search before opening another document — `contractor-search` §6.6's reasoning applies unchanged.

## F. Competitor-comparison audit

Only when the objective includes a competitor comparison. Check before printing:

- every D1–D10 row is measured on the same basis for both sides, or the cell says
  `Không so sánh được` with the reason (§7.4a);
- every scale figure carries its state — `Đang vận hành` / `Đã đặt mua / đang giao` /
  `Đã công bố kế hoạch` — and the comparison ran on the operating column only (§7.4b); our planned
  side is labelled planned;
- every scale figure carries an as-of date, pulled to the data-lock date or with the gap stated;
- **no "mình hơn" line rests on a competitor cell that is empty** (§7.5) — those belong in
  `Chưa kết luận được`;
- every competitor sits in exactly one bucket, and the set was segmented before it was ranked;
- C1–C3 were worked or recorded as unavailable;
- no D1 value came from an operator's own superlative wording, and no driver count was summed across
  platforms;
- no competitor cost, margin or utilisation appears as a fact;
- the own-side row is sourced from the user/documents, never from model knowledge (§7.1);
- the section recommends nothing (§7.7).
