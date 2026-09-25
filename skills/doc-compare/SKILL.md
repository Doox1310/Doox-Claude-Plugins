---
name: doc-compare
description: Use when the user hands over one or more documents and asks to tóm tắt, đọc, đối chiếu, so sánh, or asks which document says what, what differs between them, or what looks bất thường; also when they ask for từ khoá chính / key terms of the documents, or to xác thực, kiểm chứng, đối chiếu nguồn công khai the figures and facts a document states. Covers standards, contracts, specs, reports, meeting minutes, drawings — any document supplied in the session.
---

# Doc Compare

Read the documents the user supplied and answer three questions: what does each one
say, where do they differ, and what looks wrong. Summarising a single document is
the one-document case of the same job.

Not for plan files — those are `project-report`, `reminder`, `project-insights`.
Not for scoring báo giá or hồ sơ năng lực — that is `bid-review`, which applies a
BOQ or a capability framework. Not for producing a translated file — that is
`doc-translate`.

**REQUIRED BACKGROUND:** read `../using-doox/references/document-rules.md`. Rules
`DR1` – `DR5` govern every line of output here — never substitute model knowledge for
what the document says, name missing data instead of filling it, pass codes and units
through untouched, compare only within the same scope, and source every finding.

Read that file, not `using-doox/SKILL.md`: this skill runs no identity gate and opens
no plan file, so nothing else in `using-doox` applies to it.

Read-only, no identity gate, no file written. Output is tables in the chat reply.
Offline: no web access unless the user asks for public-source verification (§7).

## 1. Identify before reading

One line per document, before producing anything:

```
1. Quy trinh bao duong xe taxi dien.docx | Quy trình nội bộ | VI | 24 trang
2. Asiatel Bacoor Layout (07-21-28).pdf  | Bản vẽ + thuyết minh | EN | 8 trang
```

A document whose type is not clear is asked about, not assumed.

## 2. Read the structure first, then the parts that matter

Take the outline — mục lục, tên sheet, tiêu đề slide, tên bảng — before any full
read. Then read the sections the user's question actually reaches. A 200-page
standard read cover to cover to answer one question about phạm vi áp dụng costs
more than the answer is worth, and buries the finding.

Extract along the document's **own** structure. The user has to find these things
again in the original.

## 3. Summarise

Default length is the four-part output in §8; `ngắn` (5–10 dòng) and `chi tiết`
(theo từng mục) on request. Several documents: summarise each, then one paragraph
across them — never one merged blob that loses which document said what.

**Shorten the prose, never the conditions attached to a number.** A summary that
keeps `1.850.000 đ/bộ` and drops `chưa bao gồm VAT, chưa bao gồm vận chuyển đến
chân công trình` is worse than no summary. Same for mốc thời gian, ngoại lệ,
điều kiện hiệu lực and kết luận.

## 4. What each document covers

Before comparing anything — this is what stops two documents of different scope
being compared as if they disagreed:

| Tài liệu | Loại | Phạm vi đề cập | Chủ đề chính | Chủ đề KHÔNG đề cập |
|---|---|---|---|---|

The last column carries as much as the others: silence is a finding.

## 5. Differences and anomalies

**Differences**, one line each, sourced per document and position:

- **Giống** — the documents agree;
- **Khác** — they differ without contradicting (different scope, different năm ban hành, different assumption);
- **Xung đột** — they cannot both be true.

`Xung đột` is never settled by picking the more plausible side. Print both, name
both sources, say what would settle it.

**Anomalies.** Every one names the baseline it is measured against — without a
baseline it is an opinion, not a finding. Four kinds:

| Loại | Ví dụ | Baseline |
|---|---|---|
| Mâu thuẫn nội bộ | tổng ≠ cộng các dòng; ngày ký sau ngày hiệu lực; số trong bảng ≠ số trong đoạn văn; đơn vị đổi giữa chừng | chính tài liệu đó |
| Lệch khung chuẩn | thiếu hạng mục bắt buộc, sai tiêu chuẩn kỹ thuật, điều khoản khác chuẩn | khung đã lưu hoặc user cung cấp |
| Lệch giữa các tài liệu | bảo hành 6 tháng khi các bên khác 24 tháng | các tài liệu còn lại, **cần ≥3 tài liệu cùng phạm vi** |
| Bất thường hình thức | thiếu chữ ký/ngày, số hiệu trùng, phiên bản cũ hơn, đơn vị phát hành khác tên trên hợp đồng | quy ước hồ sơ |

No khung chuẩn supplied means **no `lệch khung chuẩn` finding at all** — say that
plainly instead of inventing a standard to measure against. An outlier is reported
as `cần làm rõ`, never as `sai`: the odd one out may be the correct one.

### Bằng chứng không phải chữ

A requirement is often carried by formatting rather than words — a cell shaded against
a colour legend, a ✓/✗ matrix, a struck-through clause, a merged cell spanning columns
it does not belong to. **That is the document's own content, and reading it is rule `DR1`,
not outside knowledge.** Decode it against the legend the document itself prints, and
say which mechanism you read: `ô nền cam FFC000 = "Bắt buộc" theo chú giải màu mục 1`.

It is also where internal contradictions hide, because the colour and the footnote are
written by different people at different times. A cell shaded `Bắt buộc` whose Ghi chú
reads `Khuyến nghị` is a `Mâu thuẫn nội bộ` with baseline `chính tài liệu đó` — quote
both sides and neither wins.

A formatting signal with **no legend** in the document is not decoded and not guessed:
report that the document encodes something by colour/mark without saying what, and name
the cells. Reading a colour by convention is inventing data.

Never correct an anomalous figure. Report it with both values and its position.

## 6. Từ khoá chính

The terms a reader must know to use the document: thuật ngữ định nghĩa, mã tiêu chuẩn,
văn bản pháp lý viện dẫn, bên liên quan, sản phẩm/mã model, đại lượng chính. Per
document, **8–15 terms**, each with where it appears:

| Tài liệu | Từ khoá | Loại | Vị trí (mục/trang/ô) |
|---|---|---|---|

Several documents: add **Chung** (present in every document — note if the meaning or
value differs, that is a `Khác`/`Xung đột` for §5) and **Riêng** (present in one only).

Terms are copied as the document writes them (rule `DR3`): no translation, no synonym
merging unless the document itself equates them, no term the documents do not contain.

## 7. Xác thực với nguồn công khai — chỉ khi được yêu cầu

Runs **only** when the user asks to xác thực / kiểm chứng / đối chiếu nguồn công khai.
Otherwise skip this section and stay offline.

Pick the factual claims worth checking — figures, văn bản pháp lý viện dẫn (số hiệu,
hiệu lực), company facts (tên pháp lý, MST, địa chỉ, giấy phép). List them before
searching. Judge sources with skill `research-method`, section "Source quality":
evidence classes A/B/C are evidence, **class X is never evidence** — it may only
point to an A/B/C source.

Budget: ≤10 searches and ≤5 documents opened per request, unless the user asks for more.
Claims left unchecked when the budget runs out are listed as `Chưa kiểm tra`.

Result per claim:

| Nội dung (tài liệu, vị trí) | Tài liệu ghi | Nguồn công khai ghi | Kết quả | Nguồn (lớp, đơn vị, ngày, URL) |
|---|---|---|---|---|

- **Khớp** — an A/B/C source says the same;
- **Lệch** — an A/B/C source says otherwise: print both values, neither wins;
- **Không tìm thấy nguồn công khai** — nothing A/B/C found within budget; never read as wrong.

The web never overwrites the document. Every other section still reports what the
document says; a `Lệch` is a finding for the CEO, not a correction. Cite only URLs
actually opened in this session.

## 8. Output

```
Đọc tài liệu — [tên tài liệu / nhóm tài liệu]

1. Tài liệu đã đọc          (bảng §1)
2. Tóm tắt từng tài liệu
3. Nội dung mỗi tài liệu đề cập / không đề cập   (bảng §4)
4. Từ khoá chính             (bảng §6; Chung / Riêng khi nhiều tài liệu)
5. Số liệu & điều kiện quan trọng
   - Nội dung | Giá trị | Điều kiện áp dụng | Nguồn (tài liệu, vị trí)
6. Giống / Khác / Xung đột
7. Điểm bất thường
   - Loại | Mô tả | Bằng chứng (tài liệu, vị trí) | So với baseline nào | Cần ai xác nhận
8. Xác thực nguồn công khai  (bảng §7 — chỉ khi user yêu cầu)
9. Chưa đủ cơ sở kết luận
```

Section 6 collapses to nothing when there is one document; section 8 appears
only on a verification request; section 9 never collapses — it is where "the document
is silent on this" lands.

## Before replying

- every document handed over appears in section 1 and in section 2;
- no figure, model code, tên pháp lý or ngày tháng that is not in a document, except
  the cited public value in section 8;
- every anomaly names its baseline;
- nothing marked `Xung đột` was quietly resolved;
- every `Chưa có thông tin` says what is missing and who would confirm it;
- every từ khoá appears in its document at the position given;
- no web lookup without a verification request; no class X source cited as evidence;
  every `Lệch` shows both values.
