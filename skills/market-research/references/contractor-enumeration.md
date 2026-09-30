# Tìm nhà thầu / đối tác — §6 and audit E

Read when the objective includes a contractor or partner. Every other `§` cited here is in `SKILL.md`
(§1, §2, §4, §5, §9, §10, §14) or `references/workbook.md` (§3, §12).

## 6. Two jobs, not the same job

| Request | Method | Output |
|---|---|---|
| **Full list** of contractors for a work package — default **nhà thầu xây depot & lắp sạc cho đội xe (turnkey)** | frame-first enumeration, role classification, scoring, saturation — §6.0–6.6 below | every company in `Bảng 3B` of the market workbook; the reply's summary in RX3 shape |
| **Review of a named counterparty or a short set** of any partner type | RX3 counterparty review (`assets/form-research.md`) with the lens of that partner type | RX3 `.docx` (§1) |

Other partner types are counterparty reviews, not the `Bảng 3B` enumeration, unless the user asks
for a full list of them. Each is reviewed against its own lens row in `references/topic-lenses.md`:

| Partner type | Lens |
|---|---|
| Nguồn xe — OEM / nhà phân phối | R10 |
| Tài chính, thuê xe, bảo hiểm | R18 |
| Bảo dưỡng, sửa chữa, phụ tùng, cứu hộ | R25 |
| Công nghệ gọi xe & điều phối | R45 |
| Dịch vụ đội xe hằng ngày (vệ sinh, bãi, chuẩn bị xe) | R49 |
| Luật, thuế, kế toán, tư vấn | R51 |
| Tuyển dụng & đào tạo tài xế | R08 |
| Nhà cung cấp bộ sạc (thiết bị, không phải thi công) | R24 |

Alongside a market report, a counterparty review's summary goes into the matching `Bảng 3` row
(§12 cell rules) and the RX3 `.docx` holds the detail. A full list of a non-construction type runs the
enumeration below with that type's target profile recorded in the ledger — re-map the frames to fit
(F2 becomes the relevant licence registry, F3 the OEM's authorised-dealer list), name any frame with
no equivalent as a blind spot, and write to `Bảng 3B` only if the user wants it there, otherwise to
the RX3 `.docx`.

**Why the method, not a quick search:** a generic web search ranks intermediaries first — resellers
buy the SEO that contractors do not need — so a list built without the frames is a list of resellers.
Everything in the enumeration is decision-grade.

### Where the list goes — `Bảng 3B`

The list lives in `Bảng 3B - Danh sách nhà thầu`. With no workbook yet (a contractor-only request),
copy `assets/khung-bao-cao-thi-truong.xlsx` to `Báo cáo thị trường [Thị trường] dd_mm_yyyy.xlsx`
first and fill only `Bảng 3B` plus row 30 of the report sheet (`Nhà thầu xây depot và lắp sạc`, the
summary row); the other blocks stay placeholders and the reply says so.

`Bảng 3B` is the one repeatable-row sheet: one row per company, one per exclusion, then the coverage
block. It ships with blank rows reserved for both lists — fill those first; insert more only when
they run out, without overwriting the block titles below (`SỔ LOẠI TRỪ`, `ĐỘ PHỦ TÌM KIẾM`). Inspect
the row positions before writing, and again over the affected rows after inserting.

The reply summarises the list in **RX3** shape at its `default_length`, with no separate `.docx`: a fit
verdict in plain words, the shortlist with proven scope separated from claimed scope, the conditions
on each candidate, and the checks still outstanding. A firm the evidence does not settle is named as
unverified, never scored into a number.

### 6.0 Which market these frames are written for

**Every concrete portal, registry, code scheme and query string below is Vietnam.** F1–F5 name
Vietnamese systems, §6.3 reads VSIC mã ngành, candidates are keyed on MST, and the search strings are
Vietnamese. F6 (project-reverse) and F7 (snowball) are the only jurisdiction-neutral frames.

What ports to another market is the **method**: enumerate from registries before searching, classify
role from independent evidence rather than self-description, key every candidate on one government
identifier, and stop on saturation rather than on a count. What does not port is every URL and code
on this page.

Running this for a market outside Vietnam starts with a bounded discovery pass — charged to the §6.6
budget, before any enumeration — that finds the local equivalent of each frame:

| Frame | What to look for in the target market |
|---|---|
| F1 | the public procurement / tender-results portal, and its term for design-and-build or turnkey packages |
| F2 | the construction-licence or contractor-qualification registry, and its grading scheme |
| F3 | the utility's or system operator's list of contractors approved for grid-side work |
| F4 | the company registry, and its industry-classification scheme — this supplies the identifier everything is keyed on |
| F5 | the provincial/municipal authority that issues building, electrical and fire-safety permits |
| F6, F7 | unchanged — these need no local system |

Record the mapping in the ledger and state it in the §14 reply, so the next report on that market
reuses it instead of rediscovering it.

The rest of §6 and audit E port the same way: MST becomes the jurisdiction's company identifier,
§6.3's VSIC reading becomes its industry-classification scheme, and §6.5's hạng I / II / III becomes
its contractor grading mapped to top / middle / lowest band. Record each mapping with its source; a
scheme with no grading scores that line `Chưa xác minh` rather than guessing a band. A §6.5 criterion
with no local equivalent at all (no public activity code, say) is dropped for every candidate alike,
and the Nhóm A/B thresholds scale to the points still available (Nhóm A ≈ two-thirds of the maximum)
— say so in the reply, since keeping ≥8 on a smaller maximum silently makes Nhóm A harder.

In `Bảng 3B` the column headers stay as they are; write the local equivalent in the Vietnam-named
column with its label — `KRA PIN: …` under `MST`, `KSIC …` under the mã ngành column, `NCA4
(building)` under the licence column — and `Không có tương đương công khai` where none exists.

The confirmed mapping is worth keeping beyond this run: add each confirmed frame to the evidence
cache as a `claim_type=contractor` record whose value names the frame (`F2 = NCA contractor register`)
and whose URL is the registry, so the next run on that market starts from it.

Model knowledge may suggest *where to look* for a frame; what the frame contains is only what the
discovery pass confirms.

**A frame with no local equivalent is named, never silently dropped.** Say which frames could not be
worked and what that costs: without F1 or F2 the list cannot claim saturation (§6.6), and a role
that no registry corroborates stays `Chưa xác định` (§6.1) rather than being settled by a company's
own website.

### 6.1 Target profile — say what "Cấp 1" means in this run

Default target: **tổng thầu xây depot & lắp sạc cho đội xe (turnkey, EPC/EC)** — one company that self-performs construction and carries the whole scope of a fleet depot: thiết kế, xây dựng depot/bãi đỗ, vật tư/thiết bị, hạ tầng điện và trạm biến áp, cung cấp và lắp đặt bộ sạc cho đội xe, xin phép (xây dựng, đấu nối, PCCC), thử nghiệm/nghiệm thu, bàn giao. Lens R23 (contractor due diligence) governs the claims and R19–R22 the scope. Only a user statement changes this, and a user-stated target keeps the same method. Fleet size, charger count and power, and whether a site exists
decide which licence grade or contractor class qualifies — ask for them in the §2 scope call, or keep
them `[INPUT NEEDED: …]` and say which grade the list assumed.

Classify every candidate into exactly one role:

| Role | Meaning | Counts for the shortlist |
|---|---|---|
| `Tổng thầu turnkey` | self-performs construction **and** carries end-to-end scope incl. design, materials/equipment, permits, commissioning | yes — this is the target |
| `Cấp 1 chuyên ngành` | self-performs, but only a trade slice (điện, xây dựng, đấu nối) under someone else's design/permit | secondary — usable as a package member, not as tổng thầu |
| `Trung gian / Đại lý (Cấp 2)` | sells/distributes equipment or subcontracts the work out; no self-performed construction evidence | no — list with reason, never in the shortlist |
| `Chưa xác định` | registry or independent corroboration not found | no — name what is missing |

A tổng thầu turnkey buying equipment through a distributor is normal. Distribution wording, an import/wholesale secondary mã ngành, or a brand-dealer page is **not** disqualifying on its own when the primary mã ngành is construction-execution and self-performance is independently evidenced. Only the absence of self-performance evidence disqualifies.

### 6.2 Enumeration is frame-first, never search-first

A generic web search ranks intermediaries first — they buy the SEO that contractors do not need. Generic search is **class X: it may produce a lead, never a role classification, and never the shape of the list.**

Work F1–F5 first — they carry registry evidence — then the loose frames; order within each group is free; each returns candidate names that go into the ledger keyed by **mã số thuế (MST)**. Legal name, trade name and website are attributes of an MST, not separate candidates.

| # | Frame | What it yields | Class |
|---|---|---|---|
| F1 | Hệ thống mạng đấu thầu quốc gia (`muasamcong.mpi.gov.vn`) — kết quả lựa chọn nhà thầu; filter gói `EC/EPC`, "thiết kế và thi công", "chìa khóa trao tay"; depot/bãi đỗ/nhà xưởng, hệ thống sạc đội xe, điện/trạm biến áp | winning contractor names + chủ đầu tư + scope + value + year — the strongest single frame | A |
| F2 | Chứng chỉ năng lực hoạt động xây dựng (`nangluchdxd.gov.vn` / Bộ Xây dựng, Sở Xây dựng tỉnh) — search by field and địa bàn | registry-listed firms with hạng I/II/III, field and validity. A pure trading company cannot hold one | A |
| F3 | Công ty điện lực tỉnh / EVN — danh sách đơn vị đủ điều kiện thi công đường dây và trạm biến áp | firms already accepted for grid-side work — decisive for depot interconnection | A |
| F4 | Cổng thông tin quốc gia về đăng ký doanh nghiệp (`dangkykinhdoanh.gov.vn`) — by mã ngành (§6.3) + địa bàn | legal name, MST, mã ngành chính, ngày cấp | A |
| F5 | Sở Xây dựng / Sở Công Thương tỉnh / cơ quan PCCC — công bố năng lực nhà thầu, giấy phép xây dựng đã cấp, nghiệm thu PCCC | local firms and the projects they were permitted for | A |
| F6 | Project-reverse: named EV depots, fleet-charging sites (bus/taxi/logistics) or comparable projects → who executed them (chủ đầu tư release, BQL khu công nghiệp, press) | firms with real delivered scope, often invisible to search | A/C |
| F7 | Snowball: subcontractors and consortium members named inside F1/F6 results; contractors that built depots for competing taxi/ride-hailing operators | second-ring firms — the main source of list completeness | A/C |
| F8 | Adjacent-trade transfer: nhà thầu điện / trạm biến áp / cơ điện M&E / nhà xưởng-bãi đỗ / hạ tầng viễn thông with no EV depot yet | capable candidates the market has not labelled "sạc xe điện" | A/C |
| F9 | Hiệp hội (VACC, hội nhà thầu / hội điện lực địa phương) — danh sách hội viên | membership frame | C |
| F10 | Brand pages: "hệ thống đại lý ủy quyền" / "nhà phân phối" of fleet-charger OEMs | used **inversely** — to recognise Cấp 2 candidates and to know which firms only resell | B |

Skipping a frame is allowed only when it demonstrably does not exist for the jurisdiction; record that as a coverage note, not silence.

Queries that work inside the Vietnam frames: `site:muasamcong.mpi.gov.vn "[EPC | thiết kế và thi công | chìa khóa trao tay]" "[lĩnh vực]" [tỉnh]`, `"chứng chỉ năng lực hoạt động xây dựng" "[lĩnh vực]" [tỉnh]`, `"[chủ đầu tư | dự án]" "nhà thầu thi công"`, `"[company]" "thi công" OR "tổng thầu" OR "EPC"` for role corroboration, `site:linkedin.com/company "[company]"` for the social-profile check. Do not exclude `-"đại lý" -"phân phối"` — it hides firms that both build and distribute (§6.1).

### 6.3 Mã ngành (VSIC) reading

Primary code in the construction-execution group is a positive signal: `4321` lắp đặt hệ thống điện, `4299`, `4290`, `4222`, `4212`, `4211`, `4100`, `4311`, `4312`, `4329`, `4330`. `7110` (kiến trúc, tư vấn kỹ thuật) is design/consulting — supportive of turnkey scope when combined with an execution code, never a substitute for one. `4610`, `4649`, `4659`, `4759`, `4791` are wholesale/retail — as the **primary** code with no execution code and no self-performance evidence, that is a Cấp 2 signal.

Record code, code description, registry URL and ngày cấp. Never classify a role from mã ngành alone.

### 6.4 Turnkey evidence

`Tổng thầu turnkey` requires at least one independent (non-first-party) item:

- a won EC/EPC/"thiết kế và thi công"/"chìa khóa trao tay" package in F1;
- chứng chỉ năng lực covering **both** thiết kế and thi công in the relevant field (F2);
- an owner/press/permit project reference that describes an end-to-end scope delivered by the firm.

First-party hồ sơ năng lực listing permits and commissioning is class B — it supports the claim but cannot establish it alone. Without an independent item, the role is `Cấp 1 chuyên ngành` (if self-performance is evidenced) or `Chưa xác định`, never turnkey.

### 6.5 Credibility scoring

Score every candidate; record the evidence for each line or write `Chưa xác minh` and what is missing. Never score from absence.

| Criterion | Required evidence | Points |
|---|---|---|
| Chứng chỉ năng lực hạng I / II / III | registry entry: số, lĩnh vực, hiệu lực | 3 / 2 / 1 |
| Delivered project | tender result or chủ đầu tư/permit record = 3; independent press = 2; self-published only = 1 | 3 / 2 / 1 |
| Longevity from ngày cấp ĐKKD | ≥5 years / 3–5 / <3 | 2 / 1 / 0 |
| Independent press naming a project | article with project name and date | 1 |
| Website and LinkedIn/social both describe thi công / xây lắp / tổng thầu / EPC | pages read in this run | 1 |
| Primary mã ngành in the execution group | code + registry source | 2 |

Grouping: **Nhóm A** ≥8 points **and** ≥1 independently sourced delivered project **and** role = `Tổng thầu turnkey`; **Nhóm B** 5–7, or ≥8 without the turnkey evidence; **Nhóm C** <5 or `Chưa xác định`. Longevity is a ranking input, not a cutoff: a young firm with an independently corroborated delivered project outranks an old firm with none — state which basis applies.

If the public description frames the company primarily around an unrelated line of business (real estate trading, general import-export, retail) and construction appears only as a secondary mention, cap the role at `Chưa xác định` regardless of mã ngành, and say so.

### 6.6 Completeness, budget and stop rule

"Đầy đủ" is a measurable claim, so measure it:

- one row per MST; merge duplicates across frames instead of listing them twice;
- every excluded candidate keeps a row in the exclusion ledger: MST, name, reason, source. Silent dropping is a coverage failure;
- record, per frame: searched yes/no, new MSTs produced;
- **stop rule: saturation** — two consecutive frames produce no new MST, and F1–F5 have all been worked. Not "3–5 found". The workbook's 3–5 minimum is a floor for the summary row, never a target for the list. Where some of F1–F5 do not exist publicly (common outside Vietnam), stop on the same two-frame rule over the frames that do, and call it saturation *over the available frames*, naming the missing ones — never full saturation;
- state residual blind spots (firms with no web presence, unpublished tender results, provinces not covered).

This enumeration runs on its **own budget, separate from both lines of the §9 report quota**, because registry pages are cheap to open and the report quota would otherwise cap the list at the first few SEO results. Default ceilings, set by the objective rather than the mode (exceed them with a stated reason when a market's registries are fragmented):

- contractor selection **is** a stated objective — roughly 35–60 searches and 20–30 opened documents;
- contractors appear only as one partner group in the `Bảng 3` overview — roughly 15–25 searches and 8–12 documents.

§9's "stop when sufficient" does not override the saturation rule.

Frames parallelise well — one worker per frame, non-overlapping, returning candidate rows (MST, name, role evidence, source URL, date) rather than document text. Because a frame already pins the authority and the domain, a frame worker may run the §9 triage itself inside that frame and report how many results it opened, instead of receiving a fixed URL list (`references/dispatch.md`). Frames F6–F10 are the loose ones — a worker there opens only what a registry-, owner- or permit-level snippet already supports.

### E. Contractor-list audit

Only when the objective includes contractor selection:

- F1–F5 were all worked or explicitly recorded as unavailable, and the saturation rule was met or the shortfall is stated;
- every listed company has an MST (or the local identifier), a mã ngành (or local code) with registry source, a role, and the evidence behind its role and score — no row scored from absence; an identifier or code the jurisdiction does not publish passes as `Không có tương đương công khai` when the frame mapping records why;
- no company appears twice under different names;
- every excluded candidate is in the exclusion ledger with a reason and source;
- no `Tổng thầu turnkey` rests on first-party evidence alone (§6.4);
- no candidate was dropped only for dealer/distribution wording (§6.1);
- the shortlist is drawn from Nhóm A, or the shortfall and the reason are stated;
- the `ĐỘ PHỦ TÌM KIẾM` coverage block on `Bảng 3B` is filled: frames worked, new identifiers per frame, saturation, blind spots.

Running out of budget is not a reason to skip this section — it is short by design. It is a reason to ship the workbook with named gaps.
