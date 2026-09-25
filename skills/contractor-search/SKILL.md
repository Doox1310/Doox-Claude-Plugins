---
name: contractor-search
description: Use when a user asks to find, list, screen or shortlist contractors or local partners for an electric-taxi operation in a named market — tìm nhà thầu, danh sách nhà thầu, nhà thầu xây depot, lắp sạc cho đội xe, tổng thầu turnkey, find a contractor, trouver un prestataire — or to review a named contractor, vehicle OEM/distributor, fleet financier/lessor/insurer, maintenance workshop, dispatch/booking-technology vendor, daily fleet-services supplier or legal/tax adviser. Writes the full contractor list into `Bảng 3B` of the market workbook and summarises in RX3 shape.
---

# Contractor Search — tìm nhà thầu / đối tác

**Load `research-method` first** (`../research-method/SKILL.md`, beside this skill's Base
directory). Claims and statuses (§4), source classes (§5), freshness (§8), search and dispatch (§9),
ledger and cache (§10), audit (§13) and reply counts (§14) all come from there. Scope questions
(market, data-lock date, mode) follow `market-research` §2; a request that also evaluates the market
or compares competitors is **one** run with one ledger (`research-method` §1).

`<RM>` below = the absolute path of the `research-method` directory.

## 6. What this skill does

Two jobs, and they are not the same job:

| Request | Method | Output |
|---|---|---|
| **Full list** of contractors for a work package — default **nhà thầu xây depot & lắp sạc cho đội xe (turnkey)** | frame-first enumeration, role classification, scoring, saturation — `references/contractor-enumeration.md` | every company in `Bảng 3B` of the market workbook; the reply's summary in RX3 shape |
| **Review of a named counterparty or a short set** of any partner type | RX3 counterparty review (`<RM>/assets/form-research.md`), using the lens of that partner type | RX3 `.docx` per `research-method` §1 |

**Default target of the enumeration: tổng thầu xây depot & lắp sạc cho đội xe (turnkey)** — one
company that self-performs construction and carries the whole scope for a fleet depot: thiết kế, xây
dựng depot/bãi đỗ, hạ tầng điện và trạm biến áp, cung cấp và lắp đặt bộ sạc cho đội xe, xin phép (xây
dựng, đấu nối, PCCC), thử nghiệm/nghiệm thu, bàn giao. Lens R23 (contractor due diligence) governs
the claims; R19–R22 the scope. Only a user statement changes the target, and a user-stated target
carries the same enumeration method.

**Other partner types are counterparty reviews, not the 3B enumeration** — unless the user
explicitly asks for a full list of them. Each is reviewed in RX3 shape against its own lens row in
`<RM>/references/topic-lenses.md`:

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

When such a review is asked for alongside a market report, its summary goes into the matching
`Bảng 3` row of the workbook (`market-research` §12 cell rules) and the RX3 `.docx` holds the detail.
When a full list of one of these types is asked for, run the enumeration method with that type's
target profile stated in the ledger — the frames need re-mapping for a non-construction target
(e.g. F2 becomes the relevant licence registry, F3 the OEM's authorised-dealer list), and a frame with
no equivalent is a named blind spot — and write it to `Bảng 3B` only if the user wants it there;
otherwise to the RX3 `.docx`.

## The enumeration — read `references/contractor-enumeration.md`

**Before starting a candidate list, read `references/contractor-enumeration.md` and follow it.** It
carries the target profile and role taxonomy (§6.1), the frame-first enumeration frames F1–F10
(§6.2), mã ngành reading (§6.3), turnkey evidence (§6.4), credibility scoring (§6.5), the saturation
stop rule and separate budget (§6.6), and audit E (§13E). Everything in it is decision-grade.

Do not attempt contractor work from this summary: a generic web search ranks intermediaries first, so
a list built without the frames is a list of resellers.

**The frames as written are the Vietnam instantiation.** F1–F5 name Vietnamese portals
(`muasamcong.mpi.gov.vn`, `nangluchdxd.gov.vn`, `dangkykinhdoanh.gov.vn`, EVN provincial utilities,
Sở Xây dựng), §6.3 reads VSIC mã ngành, and the query strings are Vietnamese. **The method ports to
any market; those URLs and codes do not.** For a market outside Vietnam — Côte d'Ivoire, the
Philippines, Kenya — spend a bounded discovery pass, charged to the contractor budget (§6.6),
identifying that jurisdiction's equivalent of each frame before enumerating anything: its
public-procurement results portal, its construction-licence or contractor registry, its utility's
approved-contractor list, its company registry and industry-code scheme, its municipal permit and
fire-safety authority. Record the mapping in the ledger, name it in the reply, and key candidates on
that jurisdiction's own company identifier the way the Vietnam frames key on MST.

**A frame with no local equivalent is a named blind spot, not a frame quietly dropped.** Where the
discovery pass finds no public tender-results portal or no licence registry, say which frames could
not be worked and what that leaves unverifiable — an enumeration missing F1 and F2 cannot claim
saturation (§6.6), and a role classification with no registry behind it stays `Chưa xác định` (§6.1)
rather than resting on a company's own website.

## Where the list goes — `Bảng 3B`

The list lives in `Bảng 3B - Danh sách nhà thầu` of the market workbook. If the run has no workbook
yet (a contractor-only request), copy `../market-research/assets/khung-bao-cao-thi-truong.xlsx` to
`Báo cáo thị trường [Thị trường] dd_mm_yyyy.xlsx` in the working folder first (never edit the asset)
and fill only `Bảng 3B` plus row 30 of the report sheet (`Nhà thầu xây depot và lắp sạc`, the
summary row); the other report blocks stay as placeholders and the reply says so.

`Bảng 3B` **is** a repeatable-row sheet: one row per company, one row per exclusion, plus the coverage
block. It ships with blank rows already reserved for both lists — fill those first, and insert further
rows only when they run out, taking care not to overwrite the block titles below (`SỔ LOẠI TRỪ`,
`ĐỘ PHỦ TÌM KIẾM`). Inspect the actual row positions before writing, and re-inspect with `--rows` over
the affected rows only after inserting:

```bash
python "<RM>/scripts/wb.py" inspect <file.xlsx> --sheet "Bảng 3B - Danh sách nhà thầu"
python "<RM>/scripts/wb.py" write   <file.xlsx> cells.json
```

The reply's summary of the list takes the shape of **RX3** (`<RM>/assets/form-research.md`), at its
`default_length`, with no separate `.docx`: a fit verdict in plain words, the shortlist table with
proven scope separated from claimed scope, the conditions attached to each candidate, and the external
checks still outstanding. Candidates the evidence does not settle stay provisional — an unverified
firm is named as unverified, never scored into a number.

## 13–14. Audit and reply

Run `research-method` §13 gates A–D plus **audit E** (`references/contractor-enumeration.md`), then
reply per `research-method` §14. For the enumeration also state: the frame mapping used outside
Vietnam, frames worked, companies listed, how many are `Tổng thầu turnkey`, how many in Nhóm A,
whether saturation was reached, and the residual blind spots. For a counterparty review state the
lens used and which items stayed claimed rather than proven.
