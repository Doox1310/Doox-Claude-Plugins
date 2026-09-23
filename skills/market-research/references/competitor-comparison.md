# Competitive position — mình so với đối thủ (§7)

Applies whenever the objective includes `competitor/CPO`. Decision-grade throughout.

The question this section answers is not "who else is in this market". It is **"where do we stand
against them, on what evidence, and where does that leave us exposed"**. A list of competitors with
their station counts is the input, not the output.

Output goes to **its own `.docx` as tables** (SKILL.md §2), summarised in the chat reply, not into
the workbook — the bundled framework has no competitor block yet. Everything else in this skill still applies: sourcing (§5), freshness (§8),
the evidence record (§10), conflicts (§11).

## 7.1 "Mình" has to be stated, never assumed

The comparison needs our own side, and **our own side comes only from the user, from documents in the
session, or from a plan file they point at.** Never from model knowledge about the company, however
confidently it comes to mind — that knowledge is stale by construction, and a comparison built on a
half-remembered own-side is worse than no comparison.

Ask for the own-side profile in the same structured call as §2's other unknowns, along the same
dimensions the competitors will be measured on (§7.3). Whatever the user does not supply stays
`Chưa có dữ liệu nội bộ` in its row — a visible blank, never a guess and never silently dropped.

The own-side unknown entirely: the section still runs, produces the **competitor landscape only**,
and says in one line that no comparison was made because the own-side was not supplied. Do not
quietly turn a comparison request into a landscape report and let the heading imply otherwise.

## 7.2 Define the competitor set before enumerating it

A competitor is a company chasing **the same customer in the same market**. Say which, in three
buckets, and put every company in exactly one:

| Bucket | Meaning | Example shape |
|---|---|---|
| `Trực tiếp` | same service, same customer segment, same geography | another public CPO on the same fleet segment |
| `Gián tiếp` | different service, same need | home/depot charging, battery swap, xe xăng cho cùng tuyến |
| `Thay thế / tiềm năng` | not competing yet but holds the assets to start | utility, oil retailer with forecourt sites, OEM with its own network |

**Segment before scale.** A network ten times our size serving private cars is a weaker `Trực tiếp`
competitor than a small one serving the same taxi fleet. Ranking the set by station count before
segmenting it produces the wrong list every time.

Enumeration is frame-first, exactly as §6.2 argues — generic search surfaces whoever bought the SEO:

| # | Frame | What it yields | Class |
|---|---|---|---|
| C1 | Regulator / cơ quan quản lý: danh sách đơn vị được cấp phép vận hành trạm sạc, công bố quy hoạch | the licensed operators, with địa bàn | A |
| C2 | Utility / EVN: đơn vị đã đấu nối, công suất được cấp, phụ tải đăng ký | who actually has grid capacity — the hardest thing to fake | A |
| C3 | Tender results (§6 F1, reused): gói thầu trạm sạc và bên trúng | who is building now, at what value | A |
| C4 | Filings of listed/state operators: báo cáo thường niên, bản cáo bạch, báo cáo quản trị | station counts, capex, revenue model, stated plans — with a date | A |
| C5 | CPO first-party: bản đồ trạm, app, trang phủ sóng, bảng giá | the network as its owner describes it — authoritative for its own network only | B |
| C6 | Roaming/aggregator apps and open charge maps | cross-network coverage, often the only per-cổng data available | C |
| C7 | Press announcing new deployments, partnerships, OEM tie-ups | direction of travel — plans, not assets | B/C |

C1–C3 are the required core: they carry assets, not announcements. Skipping one is allowed only when
the frame demonstrably does not exist in the jurisdiction, and that is recorded as a coverage note.

## 7.3 The comparison dimensions — fixed, applied to everyone alike

Ten dimensions, same ten for us and for every competitor. A dimension measured for one side and not
the other is not a comparison and does not go in the table.

| # | Dimension | What is actually compared |
|---|---|---|
| D1 | Quy mô phủ | số **cổng** đang vận hành, số trạm, số tỉnh/thành có mặt |
| D2 | Công suất & công nghệ | tỷ lệ DC/AC, kW mỗi cổng, chuẩn cổng, khả năng nâng công suất |
| D3 | Vị trí & loại site | cao tốc / nội đô / depot / TTTM; site độc quyền hay chia sẻ |
| D4 | Phân khúc khách | fleet/taxi vs cá nhân vs logistics — ai là khách chính |
| D5 | Giá & mô hình doanh thu | giá/kWh, phí đỗ/phí chờ, gói thuê bao, B2B contract vs bán lẻ |
| D6 | Chất lượng vận hành | uptime công bố, thời gian sửa chữa, khiếu nại công khai |
| D7 | Hệ sinh thái | app, thanh toán, roaming với mạng khác, tích hợp OEM |
| D8 | Năng lực triển khai | tốc độ mở trạm (cổng/quý, đo qua nhiều mốc), nhà thầu, nguồn thiết bị |
| D9 | Hậu thuẫn | sở hữu, vốn, quan hệ với utility/địa phương |
| D10 | Rào cản cơ cấu | hợp đồng site dài hạn, độc quyền, giấy phép, quyền đấu nối đã có |

D8 needs two dated observations of D1, not a press release. D10 is where the durable advantage
usually sits and where public data is thinnest — an empty D10 is a real finding, recorded as
`Chưa có dữ liệu công khai`, never inferred from the absence.

## 7.4 Normalise before comparing — and split built from announced

Two failures account for almost every wrong competitive read in this industry. Both are avoidable.

**7.4a — The unit.** `500 trạm` and `2.000 cổng` are not comparable figures. **Cổng (connector) is the
comparison unit**; a station is a site whose port count varies by an order of magnitude. Where a
source gives only stations, record it as stations, mark the cell `Không so sánh được — chỉ có số
trạm`, and do not convert with an assumed ports-per-station ratio. Same discipline for giá (same
currency, same tax basis, same tier), for công suất (kW per cổng, not per trạm) and for coverage
(same administrative level).

**7.4b — Đang vận hành ≠ đã công bố.** A CPO announcing 1.000 cổng by next year and operating 180
today is a company with 180. Every scale figure carries its state, in its own column, and the
comparison runs on the operating column:

| State | Counts in the comparison |
|---|---|
| `Đang vận hành` | yes — this is the comparison |
| `Đang xây / đã ký site` | shown in its own column, read as pipeline |
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
value, `Nguồn`, `Ngày`, and `Độ chắc chắn` (Đã xác minh / Ước tính có cơ sở / Chưa xác minh).
Competitors ordered by bucket then by D1 operating ports.

**2. Đọc bảng.** Not a restatement of it — four short lists, each line naming the dimension and the
measured gap:
- **Mình hơn** — dimension, how much, and on what sourced comparison;
- **Mình kém** — same, and what it costs operationally;
- **Ngang nhau** — where nobody has an edge, so competing there spends money for nothing;
- **Chưa kết luận được** — dimension, which side is missing, what source would close it.

**3. Khoảng trống và hướng đi của họ.** Segments or geographies nobody in the set serves — with the
reason, since an empty segment is usually empty for a reason. Then where each competitor is putting
capital, read from C3/C4/C7 with dates: pipeline is direction, and direction is what we are actually
competing against, not today's port count.

**4. Rủi ro cạnh tranh.** Each one: what would have to happen, how likely on current evidence, and
which of our dimensions it hits. A competitor holding D10 advantages we cannot match goes here, not
in the strengths list.

## 7.7 Boundaries and budget

**No verdict.** This section reports position and exposure. It does not recommend entering, exiting,
pricing, or acquiring — those are the reader's, and §1's contract holds here as everywhere.

**No modelled internals.** A competitor's cost per cổng, margin, utilisation or payback is not public
and is not to be estimated into the table as though it were. Where the user asks for one, it is an
explicit `Ước tính` row with the formula and every assumption written out, kept out of the comparison
table itself.

**No scoring from marketing.** A CPO's own "mạng lưới lớn nhất Việt Nam" is class B wording about
itself — recorded as a claim, never as a D1 value.

**Budget:** roughly **12–18 searches, 4–6 opened documents**, inside the §9 quota. Cap the set at
**5 `Trực tiếp`** competitors plus whatever `Gián tiếp`/`Thay thế` genuinely bear on the objective;
beyond that, list the remainder by name in one line and say the comparison was capped. Run another
search before opening another document — §6.6's reasoning applies unchanged.
