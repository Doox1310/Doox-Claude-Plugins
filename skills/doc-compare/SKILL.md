---
name: doc-compare
description: "Use when the user hands over one or more documents and asks to tóm tắt, đọc, đối chiếu, so sánh, or asks which document says what, what differs between them, or what looks bất thường; also when they ask for từ khoá chính / key terms of the documents, or to xác thực, kiểm chứng, đối chiếu nguồn công khai the figures and facts a document states. Covers standards, contracts, specs, reports, meeting minutes, drawings — any document supplied in the session. Load `using-doox` first. Works on supplied documents only: scoring quotes or contractor dossiers is `bid-review`, a translated file is `doc-translate`, researching a market is `market-research`."
---

# Doc Compare

**`using-doox` is loaded first and routes here.** This skill uses from it only "Language" and `references/document-rules.md` (DR1–DR5); it runs no identity gate and opens no plan file.

Read the documents the user supplied and answer: what does each say, where do they differ, what looks
wrong. A single-document summary is the one-document case. Not for plan files (`project-report`,
`reminder`), scoring báo giá / hồ sơ năng lực (`bid-review`), or a translated file (`doc-translate`).

## Hard limits

- `DR1`–`DR5` on every line.
- Read only the documents the user supplied; never a plan file.
- Never invent a figure, model code, tên pháp lý or date; never correct an anomalous figure — report
  both values and the position.
- `Xung đột` is never settled by picking the more plausible side.
- No `lệch khung chuẩn` finding without a khung chuẩn saved or supplied.
- A formatting signal with no legend in the document is not decoded — reading colour by convention is
  inventing data.
- Web lookup only when the user asks for public-source verification (§7); class X is never evidence;
  the web never overwrites the document.
- Output is tables in the chat; no file is written and no supplied file is changed.

## 1. Identify before reading

One line per document before anything else — name | loại | ngôn ngữ | size:

```
1. Quy trinh bao duong xe taxi dien.docx | Quy trình nội bộ | VI | 24 trang
```

A document whose type is unclear is asked about, not assumed.

## 2. Read the structure first, then the parts that matter

Take the outline (mục lục, sheet, slide, bảng) first, then read what the question reaches — a
cover-to-cover read of a 200-page standard buries the finding. Extract along the document's own
structure so the user can find things again in the original.

## 3. Summarise

Default: the output of §8, because it keeps each document separate; `ngắn` (5–10 dòng) or `chi tiết`
(theo từng mục) on request. Several documents: each separately, then one paragraph across them.

**Shorten the prose, never the conditions attached to a number** — `1.850.000 đ/bộ` without
`chưa bao gồm VAT, chưa bao gồm vận chuyển` is worse than no summary. Same for mốc thời gian, ngoại lệ,
điều kiện hiệu lực, kết luận.

## 4. What each document covers

Before comparing, so documents of different scope are not read as disagreeing:

| Tài liệu | Loại | Phạm vi đề cập | Chủ đề chính | Chủ đề KHÔNG đề cập |
|---|---|---|---|---|

Silence is a finding.

## 5. Differences and anomalies

**Differences**, one line each, sourced per side: **Giống** / **Khác** (differ without contradicting —
scope, năm ban hành, assumption) / **Xung đột** (cannot both be true — print both, name both sources,
say what would settle it).

**Anomalies** each name their baseline, otherwise they are opinion:

| Loại | Ví dụ | Baseline |
|---|---|---|
| Mâu thuẫn nội bộ | tổng ≠ cộng các dòng; ngày ký sau ngày hiệu lực; bảng ≠ đoạn văn; đơn vị đổi giữa chừng | chính tài liệu đó |
| Lệch khung chuẩn | thiếu hạng mục bắt buộc, sai tiêu chuẩn kỹ thuật | khung đã lưu hoặc user cung cấp |
| Lệch giữa các tài liệu | bảo hành 6 tháng khi các bên khác 24 tháng | các tài liệu còn lại, ≥3 cùng phạm vi |
| Bất thường hình thức | thiếu chữ ký/ngày, số hiệu trùng, phiên bản cũ, đơn vị phát hành khác tên trên hợp đồng | quy ước hồ sơ |

No khung chuẩn: say plainly there is no `lệch khung chuẩn` finding and why. An outlier is `cần làm rõ`,
never `sai` — the odd one out may be right.

### Bằng chứng không phải chữ

Requirements are often carried by formatting — cell shading against a colour legend, ✓/✗ matrices,
strike-through, merged cells. That is the document's own content (`DR1`): decode it against the legend
the document prints and name the mechanism (`ô nền cam FFC000 = "Bắt buộc" theo chú giải màu mục 1`).
Contradictions hide here (tests found both anomalies of T07 this way): a cell shaded `Bắt buộc` whose
Ghi chú says `Khuyến nghị` is a `Mâu thuẫn nội bộ` — quote both, neither wins. No legend: report that
the document encodes something it does not explain, and name the cells.

## 6. Từ khoá chính

Terms a reader needs: thuật ngữ định nghĩa, mã tiêu chuẩn, văn bản pháp lý viện dẫn, bên liên quan,
sản phẩm/mã model, đại lượng chính. Default 8–15 per document, because a longer list stops being
the terms a reader must know:

| Tài liệu | Từ khoá | Loại | Vị trí (mục/trang/ô) |
|---|---|---|---|

Several documents: add **Chung** (in every document — a different meaning or value is a §5
`Khác`/`Xung đột`) and **Riêng**. Terms are copied as written (`DR3`), no synonym merging unless the
document equates them, none the documents do not contain.

## 7. Xác thực với nguồn công khai — chỉ khi được yêu cầu

Only when the user asks to xác thực / kiểm chứng / đối chiếu nguồn công khai; otherwise stay offline.

List the claims worth checking before searching — figures, văn bản pháp lý viện dẫn (số hiệu, hiệu
lực), company facts (tên pháp lý, MST, địa chỉ, giấy phép). Judge sources with `market-research` §5
"Source quality": classes A/B/C are evidence, class X only points to one.

Budget: default ≤10 searches and ≤5 documents opened, because verification is a check, not research;
more if the user asks. Claims left over are `Chưa kiểm tra`.

| Nội dung (tài liệu, vị trí) | Tài liệu ghi | Nguồn công khai ghi | Kết quả | Nguồn (lớp, đơn vị, ngày, URL) |
|---|---|---|---|---|

- **Khớp** — an A/B/C source agrees;
- **Lệch** — an A/B/C source differs: both values, neither wins — a finding, not a correction;
- **Không tìm thấy nguồn công khai** — never read as wrong.

Cite only URLs opened in this session.

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

Section 6 drops with one document, section 8 without a verification request; section 9 always stays —
it is where "the document is silent" lands.

## Before replying

- every document appears in sections 1 and 2;
- nothing in the output that is not in a document, except the cited public value in section 8;
- every anomaly names its baseline; no `Xung đột` quietly resolved;
- every `Chưa có thông tin` says what is missing and who would confirm it;
- every từ khoá is at the position given;
- no web lookup without a request; every `Lệch` shows both values.
