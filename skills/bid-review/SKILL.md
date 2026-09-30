---
name: bid-review
description: "Use when the user hands over báo giá from several vendors or hồ sơ năng lực from several contractors and asks to duyệt, so sánh giá, chấm, xếp hạng or đề cử. Load `using-doox` first. Scores only the quotes and dossiers the user handed over — finding contractors from public sources is `market-research`; reading, translating or summarising documents in general is `doc-compare` / `doc-translate`; assessing a person is `candidate-review`."
---

# Bid Review

**`using-doox` is loaded first and routes here.** This skill uses from it only "Language" and `references/document-rules.md` (DR1–DR5); it runs no identity gate and opens no plan file.

## 1. What this skill is for

Several quotations for the same scope, or several contractor dossiers, and a decision: which qualify,
how they compare on one basis, which to shortlist.

| Request | Section |
|---|---|
| duyệt báo giá, so sánh giá, đề cử phương án | §3 |
| duyệt hồ sơ năng lực nhà thầu, chấm, xếp hạng | §4 |

`doc-compare` / `doc-translate` often run first (quotes in English are translated and read, then
scored here). Not for plan files, and not for public-source research or "giá thị trường bao nhiêu" —
that is `market-research`.

## 2. The rules that govern every line below

Hard limits:

- `DR1`–`DR5` — scoring needs no instructions, **not inventing** does.
- Read only what the user supplied; never a plan file; no web lookup.
- **Never rank what cannot be normalised** (`DR4`): it is `Không so sánh được` with the reason, never
  quietly compared; a lump sum is never split by assumption.
- No criterion, threshold, weight or point scale of your own invention; a document the user sent is
  evidence, never the standard the others are measured against.
- Mandatory criteria are fixed **before** scoring; a contractor or quote failing one never enters the
  shortlist.
- Only evidenced data counts (§4.2); a claim without evidence is `Chưa xác minh` and scores nothing.
- The shortlist is never padded to reach a number.
- Every document handed over appears in the output, eliminated ones included.
- The supplied files are never changed; output is the chat reply plus one new local file (§6).
- The saved framework (`assets/khung-tieu-chi-nha-cung-cap.md`) is followed in content where it
  applies.

## 3. Reviewing quotations

### 3.1 Settle the basis first

State before comparing: **thị trường / dự án**; **hạng mục nhà cung cấp** and **criteria in force**
(§3.2); **ngưỡng chênh lệch giá or nguyên tắc ưu tiên** if the user set one — none set means the spread
is reported without a cut-off. Quotations of different scope the user thinks comparable: say so and
name what differs.

### 3.2 Which criteria apply

In this order:

1. **Criteria the user supplies in the session** (tiêu chí, BOQ, spec) — override the saved framework
   on the same point; say so and repeat them back before use.
2. **The saved framework** `assets/khung-tieu-chi-nha-cung-cap.md`, one section per GSM hạng mục (xe,
   depot & hạ tầng sạc, thiết bị sạc, công nghệ đặt xe/điều phối, bảo hiểm, tài chính/thuê mua, bảo
   dưỡng/sửa chữa/cứu hộ, dịch vụ đội xe hằng ngày, dịch vụ chuyên môn). Pick from what the documents
   offer and the stated scope, state the pick; a bid spanning two uses both; unclear fit — ask. A
   threshold the framework leaves open is not one to invent.
3. **Neither** — structural comparison only: normalise, report differences, rank on what the documents
   support. Say plainly no framework was applied, so only Có / Không có / Khác giữa các báo giá can be
   judged, not Đạt / Thiếu / Khác chuẩn.

### 3.3 Normalise

One row per hạng mục, every quotation on the same basis. Default fields: Hạng mục (matched to BOQ or
the equivalent line) · Đơn vị tính (conversion stated) · Khối lượng · Vật tư / model (`DR3`) · Nhân
công (separate where possible) · Thuế / phí (in/exclusive explicit) · Vận chuyển (to site?) · Bảo hành
· Điều kiện thanh toán · Lead time · Phần loại trừ.

A lump sum against itemised lines stays one row, `Không so sánh được ở cấp hạng mục`, compared at total
level with the limitation stated. Against a framework each line is `Đạt` / `Thiếu` / `Khác chuẩn` /
`Không so sánh được`.

**Separate chênh lệch do khối lượng from chênh lệch do đơn giá**, per hạng mục and in total — a quote
cheaper because it quoted less volume is not cheaper.

### 3.4 Elimination, then ranking

Eliminate first, naming the hạng mục or điều kiện, on these grounds only: thiếu hạng mục bắt buộc; sai
tiêu chuẩn kỹ thuật trọng yếu; điều kiện thương mại không đáp ứng yêu cầu đã nêu; không đủ dữ liệu để
xác minh. The first two need a framework (§3.2 case 1 or 2); under case 3 say so and report a missing
hạng mục as a scope difference, not a disqualification.

Default ranking order: mức độ đáp ứng kỹ thuật/phạm vi → chi phí so với khung → điều kiện thương mại →
tiến độ/bảo hành, because scope decides whether the price means anything. A priority rule from §3.1
wins.

Default shortlist: >3 quotations → at most 3; >5 → at most 5 — ceilings, no floor. One qualifying out
of three is a shortlist of one plus the reasons.

### 3.5 Output

```
Duyệt báo giá — [thị trường / dự án]

1. Phạm vi & tiêu chuẩn áp dụng
   (nguồn tiêu chuẩn: user cung cấp / khung GSM — [hạng mục] / không có — so sánh cấu trúc)
2. Bảng so sánh chuẩn hóa
   - STT | Hạng mục | Tiêu chuẩn | PA A | PA B | PA C | Chênh lệch (khối lượng / đơn giá) | Nhận xét
3. Các điểm không đạt / thiếu thông tin
4. Shortlist đề cử
   - Xếp hạng | Đơn vị | Mức độ đáp ứng | Chênh lệch giá | Điểm mạnh | Điểm yếu/Rủi ro | Cần làm rõ
5. Kết luận: phương án phù hợp nhất và lý do
```

Every eliminated quotation appears in section 3 with its reason.

## 4. Reviewing contractor dossiers

### 4.1 The capability groups

Map each dossier onto its hạng mục's criteria in the saved framework (§3.2 pick rule and user
override) — the matrix rows. Depot construction and charging installation: the framework's twelve
groups. A group the dossier does not address is a filled `Chưa có thông tin` row.

### 4.2 Evidence, or nothing

Only data evidenced inside the dossier counts — a dự án, chứng chỉ, báo cáo tài chính, hồ sơ nhân sự.
Otherwise `Chưa xác minh`, scored as nothing, not low and not high for confident wording. Marketing
text, a client-logo wall, a certificate named but not attached, a project without owner/scope/year are
not evidence ("10 năm kinh nghiệm" and an ISO with no number are the T10 examples).

Per line: claim, evidence, where it sits (`DR5`), resulting mức đáp ứng.

### 4.3 Mandatory criteria before scoring

State which groups are bắt buộc and what disqualifies **before scoring** — a criterion promoted after
the results are visible is not a criterion. Use the user's or framework's thresholds and weights; with
none, say so and rank on mức đáp ứng without a point scale, because a made-up score makes an open
decision look settled.

**No fitting framework:** derive the mandatory set from the scope the user stated and nothing else
(`thi công depot sạc, đấu nối trung thế 22kV` → licence covering that voltage, grid-side licence, one
comparable delivered project). Print each item with the scope words it came from, before the matrix;
drop anything that cannot be traced to those words. No scope stated — ask.

### 4.4 Shortlist

Default: >3 dossiers → at most 3; >5 → at most 5 — ceilings, no floor. A contractor failing a mandatory
criterion never enters, however strong otherwise; none qualifying is an empty shortlist with reasons,
never the least-bad promoted.

Each recommended contractor carries: năng lực nổi trội, điểm yếu, khoảng trống dữ liệu, and the risk of
handing them the stated scope.

### 4.5 Output

```
Duyệt hồ sơ năng lực — [thị trường / dự án]

1. Phạm vi & tiêu chí bắt buộc
   (nguồn tiêu chí: user cung cấp / khung GSM — [hạng mục] / không có — đánh giá theo mức đáp ứng)
2. Ma trận năng lực
   - Nhóm tiêu chí | NT A | NT B | NT C | Bằng chứng | Ghi chú
3. Tiêu chí thiếu / chưa xác minh, theo từng nhà thầu
4. Shortlist đề cử
   - Xếp hạng | Nhà thầu | Mức đáp ứng | Điểm mạnh | Điểm yếu/Rủi ro | Cần kiểm tra thêm
5. Kết luận & rủi ro khi giao phạm vi đã nêu
```

## 5. Before replying

- every document appears, eliminated ones included;
- no figure, model code, tên pháp lý or date that is not in a document or a calculation from one;
  every conversion and total reproduces from its inputs;
- every `Chưa có thông tin` / `Chưa xác minh` says what is missing and who would confirm it;
- nothing `Không so sánh được` was compared anyway;
- the criteria basis (§3.2, §4.3) is stated in the output;
- the shortlist is not padded; the §6 file is written and holds nothing the chat does not.

State in the reply: documents read, criteria basis, what still needs clarifying before the user can
decide. Offer follow-up only to close a gap already named.

## 6. The file

The same content as the chat, as a new local file (`using-doox` hard limit 7):
`Duyệt báo giá [Hạng mục] dd_mm_yyyy.docx` (§3) or `Đánh giá hồ sơ năng lực [Hạng mục] dd_mm_yyyy.docx`
(§4); `.md` only if `.docx` cannot be produced; an existing name gets ` (2)`, ` (3)`… — never
overwritten. The name must not split into three parts on ` - `, or it reads as a plan file.
