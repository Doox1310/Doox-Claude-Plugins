---
name: bid-review
description: Use when the user hands over báo giá from several vendors or hồ sơ năng lực from several contractors and asks to duyệt, so sánh giá, chấm, xếp hạng or đề cử. Not for reading, translating or summarising documents in general.
---

# Bid Review

## 1. What this skill is for

Several quotations for the same scope, or several contractor dossiers, and a
decision to make: which ones qualify, how they compare on one basis, which to
shortlist.

| Request | Section |
|---|---|
| duyệt báo giá, so sánh giá, đề cử phương án | §3 |
| duyệt hồ sơ năng lực nhà thầu, chấm, xếp hạng | §4 |

Reading, translating, summarising or comparing documents in general is not this
skill: `doc-compare` reads and compares, `doc-translate` produces a translated file.
Those two usually run first — five quotations arrive, two in English, they are
translated and read before anything is scored here. Not for plan files, and not for
researching a market from public sources (`market-research`).

**Read-only, and no identity gate.** This skill shows nobody's rows and touches no
plan file, so it runs for either role without the `using-doox` identity check. It
changes no document it was given: the output is tables in the chat reply, plus the same
content in one new file (§6).

## 2. The rules that govern every line below

**REQUIRED BACKGROUND:** read `../using-doox/references/document-rules.md` — the five
document rules: never substitute model knowledge for what the document says, name
missing data instead of filling it, pass codes and units through untouched, compare
only within the same scope, source every finding. They are referred to below as rules
`DR1` – `DR5` and they are the whole reason this skill exists: scoring needs no
instructions, **not inventing** does.

Read that file, not `using-doox/SKILL.md`. This skill runs no identity gate and opens no
plan file, so nothing else in `using-doox` applies to it.

## 3. Reviewing quotations

### 3.1 Settle the basis first

Before comparing anything, establish and state:

- **thị trường / dự án** the quotations belong to;
- **hạng mục nhà cung cấp** — see §3.2;
- **the criteria in force** — see §3.2;
- **ngưỡng chênh lệch giá or nguyên tắc ưu tiên**, if the user set one. No threshold set means
  ranking reports the spread and does not apply a cut-off of its own invention.

Quotations for different scopes that the user believes are comparable: say so before normalising, and
name what differs.

### 3.2 Which criteria apply

Criteria come from one of three places, in this order:

1. **Criteria the user supplies in the session** — a list of tiêu chí, a reference BOQ, a spec. They
   override the saved framework wherever the two cover the same point; state that the review ran on
   user-supplied criteria and repeat them back before using them.
2. **The saved framework** — `assets/khung-tieu-chi-nha-cung-cap.md`, one section per hạng mục nhà
   cung cấp of GSM (xe, depot & hạ tầng sạc, thiết bị sạc, công nghệ đặt xe/điều phối, bảo hiểm, tài
   chính/thuê mua, bảo dưỡng/sửa chữa/cứu hộ, dịch vụ đội xe hằng ngày, dịch vụ chuyên môn). Pick the
   section from what the documents offer and the scope the user stated; state the pick. Documents
   spanning two sections (a charger supply-and-install bid) use both. Nothing fits, or the fit is
   unclear: ask, do not stretch a section over it. The framework names **what** to check and what
   evidence counts; a threshold it leaves open is not one to invent.
3. **The documents themselves** — when neither applies, the comparison is structural only:
   normalise onto a common scope, report differences, and rank on what the documents actually
   support. **Say plainly that no standard framework was applied, and that Đạt/Thiếu/Khác chuẩn
   cannot be judged** — only Có/Không có/Khác giữa các báo giá.

**A document the user sent is evidence, not a standard.** A vendor's own spec sheet does not become
the benchmark the other vendors are measured against just because it arrived first. Only case 1 and
case 2 set criteria.

### 3.3 Normalise

Put every quotation on the same basis, one row per hạng mục, before any comparison:

| Field | Note |
|---|---|
| Hạng mục | matched to the BOQ line, or to the equivalent line in the other quotations |
| Đơn vị tính | converted, with the conversion stated |
| Khối lượng | |
| Vật tư / model | mã hiệu passed through per rule `DR3` |
| Nhân công | separated from materials wherever the document allows |
| Thuế / phí | tax-inclusive vs exclusive made explicit |
| Vận chuyển | including whether it reaches site |
| Bảo hành | duration and scope |
| Điều kiện thanh toán | |
| Lead time | |
| Phần loại trừ | what the quotation explicitly does not cover |

A quotation that does not split a figure the others split — one lump sum against itemised lines — is
kept as one row marked `Không so sánh được ở cấp hạng mục`, compared at total level, and the
limitation is stated. Never split a lump sum by assumption.

Against a standard framework, each line gets: `Đạt` / `Thiếu` / `Khác chuẩn` / `Không so sánh được`.

**Separate the two causes of a price difference.** Chênh lệch do khối lượng and chênh lệch do đơn giá
are different problems with different fixes — a quotation that is cheaper because it quoted less
volume is not a cheaper quotation. Report them apart, per hạng mục and in total.

### 3.4 Elimination, then ranking

Eliminate first, on these grounds only, each naming the specific hạng mục or điều kiện:

- thiếu hạng mục bắt buộc;
- sai tiêu chuẩn kỹ thuật trọng yếu;
- điều kiện thương mại không đáp ứng yêu cầu đã nêu;
- không đủ dữ liệu để xác minh.

**The first two grounds need a framework to exist.** Under §3.2 case 3 nothing defines what is
`bắt buộc` or what the `tiêu chuẩn` is, so eliminating on either one would be inventing the standard
this skill refuses to invent. In that case only the last two grounds are available — say so, and
report a missing hạng mục as a scope difference in the comparison table rather than as a
disqualification.

Rank what remains on: mức độ đáp ứng kỹ thuật/phạm vi → chi phí so với khung chuẩn → điều kiện
thương mại → tiến độ/bảo hành. Where the user set a priority rule in §3.1, it wins.

Shortlist size: more than 3 quotations → recommend at most 3; more than 5 → recommend at most 5.
**Never pad the shortlist to reach the number.** Three quotations of which one qualifies produces a
shortlist of one plus the reasons the others fell out.

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

Every eliminated quotation appears in section 3 with its reason. A quotation that entered the review
and appears nowhere in the output is a coverage failure.

## 4. Reviewing contractor dossiers

### 4.1 The capability groups

Every dossier is mapped onto the criteria of its hạng mục in the saved framework (§3.2, same pick
rule, same user override), and those are the row labels of the output matrix. For depot construction
and charging installation that is the framework's twelve capability groups.

A group the dossier does not address is `Chưa có thông tin` — a filled row, not an omitted one.

### 4.2 Evidence, or nothing

**Only data with evidence inside the dossier counts.** A capability statement with no dự án, chứng
chỉ, báo cáo tài chính or hồ sơ nhân sự behind it is recorded as `Chưa xác minh` and scored as
nothing — not as a low score, and not as a high one because the wording was confident.

Marketing description is not evidence. Neither is a client logo wall, a certificate named but not
attached, nor a project listed without owner, scope or year.

Per line: what the dossier claims, what evidence backs it, where that evidence sits (rule `DR5`), and
the resulting mức đáp ứng.

### 4.3 Mandatory criteria before scoring

State which groups are bắt buộc for this scope, and what disqualifies, **before scoring
anything** — a criterion promoted to mandatory after the results are visible is not a criterion.

Where the user or the saved framework supplies thresholds and weights, use them. Where neither does,
say so and rank on mức độ đáp ứng across the groups without inventing a point scale: the
matrix and the gaps carry the decision, and a made-up score would make it look settled when it is
not.

**With no framework that fits, the mandatory set is derived from the scope the user stated and from
nothing else.** `thi công depot sạc, đấu nối trung thế 22kV` carries its own requirements — a
construction licence covering that voltage, a licence to work grid-side, evidence of one comparable
delivered project. Derive only what the stated scope actually implies, print the list with the words
of the scope each item came from, and print it **before** the matrix. A criterion that cannot be
traced back to something the user said about the scope is an invented criterion; drop it. Where the
user stated no scope at all, ask for it rather than deriving a set from the dossiers.

### 4.4 Shortlist

More than 3 dossiers → at most 3 recommended; more than 5 → at most 5. A contractor failing a
mandatory criterion never enters the shortlist, whatever its other scores.

**Those are ceilings and there is no floor. Never pad the shortlist to reach a number** — the same
rule as §3.4, and it bites harder here, because a mandatory criterion is exactly the kind of thing a
strong dossier fails on. Three dossiers of which one qualifies produces a shortlist of one plus the
reasons the other two fell out; none qualifying produces an empty shortlist and the reasons, never
the least-bad promoted to fill it.

Every recommended contractor carries: năng lực nổi trội, điểm yếu, khoảng trống dữ liệu, and the risk
of handing them the stated scope.

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

Check, against the documents read in this run:

- every document handed over appears in the output, including the ones eliminated;
- no figure, model code, tên pháp lý or ngày tháng in the output that is not in a document or in a
  calculation whose inputs are (rules `DR1`, `DR3`);
- every conversion, normalisation and total reproduces from the stated inputs;
- every `Chưa có thông tin` / `Chưa xác minh` says what is missing and who would confirm it;
- nothing marked `Không so sánh được` was quietly compared anyway;
- the basis of the criteria (§3.2, §4.3) is stated in the output, not just decided internally;
- the shortlist was not padded to a target number;
- the file of §6 was written, and holds nothing the chat reply does not.

Then state in the reply: documents read, the criteria basis used, and what still needs to be
clarified before the user can decide. Offer follow-up work only when it closes a gap already named in
the output.

## 6. The file

Write the same content as the chat reply to the local working folder the user opened for the session
(in Cowork, what shows under Output; with none open, the session's outputs folder):
`Duyệt báo giá [Hạng mục] dd_mm_yyyy.docx` for §3, `Đánh giá hồ sơ năng lực [Hạng mục] dd_mm_yyyy.docx`
for §4. A `.md` of the same name only when a `.docx` cannot be produced; if the name exists, add
` (2)`, ` (3)`… rather than overwrite. The name must not split into three parts on ` - ` —
`using-doox` would read it as a project plan file. Never deliver it through Claude Docs, an artifact
or a connector.
