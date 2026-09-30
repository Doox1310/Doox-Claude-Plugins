# Gộp 4 skill research thành `market-research`, viết lại theo 3 tầng (bản 1.2.1)

Duyệt 30/09/2026. Đợt 1 của hai đợt: đợt này chỉ đụng skill research; đợt 2 áp nguyên tắc 3 tầng
(§2) cho 12 skill còn lại, ưu tiên `using-doox`, `mail-draft`, `project-report` — spec riêng.

## 1. Gộp

`research-method`, `contractor-search`, `competitor-research` gộp vào `market-research`. Chỉ còn một
skill research, lo được: (1) tìm nhà thầu/đối tác, (2) đánh giá thị trường/khu vực và keyword quan
trọng, (3) so sánh đối thủ.

```
market-research/
  SKILL.md                             lõi phương pháp (§1, §4, §5, §8, §9, §10, §11, §13, §14)
                                       + §2 phạm vi + bảng "việc nào → đọc file nào"
  assets/khung-bao-cao-thi-truong.xlsx
  assets/form-research.md              RX1–RX5
  references/workbook.md               §3 đọc khung + §12 điền workbook
  references/contractor-enumeration.md §6 (thân contractor-search/SKILL.md làm phần mở đầu) + §13E, Bảng 3B
  references/competitor-comparison.md  §7 (thân competitor-research/SKILL.md làm phần mở đầu) + §13F, RX2
  references/topic-lenses.md, metrics.md, dispatch.md, final-audit.md
  scripts/wb.py, scripts/cache.py
```

- Nguồn nội dung: bản trong `research-method/`, `contractor-search/`, `competitor-research/` (bản
  25/09). Bản copy cũ untracked đang nằm trong `market-research/` (references/, scripts/,
  assets/form-research.md, `__pycache__`) là bản trước lần tách — chuyển ra
  `../_backup-stale-market-research-2026-09-30/` (ngoài plugin), không dùng.
- Số `§` giữ nguyên. Bảng "§ nằm ở skill nào" đổi thành "§ nằm ở file nào".
- Reference chỉ đọc khi việc đó có mặt trong yêu cầu. Yêu cầu gộp nhiều việc vẫn là một run: một
  lần hỏi phạm vi, một claim split, một ledger, một audit.
- `<RM>` bỏ; script gọi bằng đường dẫn tuyệt đối của thư mục skill này.
- §14 gộp các dòng reply riêng: nhà thầu (frame mapping, số turnkey, Nhóm A, saturation, blind spot;
  review đối tác: lens và mục còn là claimed) và đối thủ (bucket, C1–C3, số D-row
  `Chưa kết luận được`, own-side đủ hay thiếu) — mỗi nhóm ghi "khi mục tiêu có …".
- `description` viết lại ≤ 1024 ký tự, đủ trigger của cả 3 việc (vi/en/fr, thị trường mẫu), kèm ranh
  giới: báo giá/hồ sơ user đưa sang để duyệt → `bid-review`.

Đổi tham chiếu bên trong (tên skill cũ, `../`, `../../`): `form-research.md`, `final-audit.md`,
`metrics.md`, phần đầu `contractor-enumeration.md` và `competitor-comparison.md`, docstring
`cache.py`.

## 2. Nguyên tắc 3 tầng — chừa chỗ cho model tự phán đoán

Mỗi luật khi viết lại rơi vào đúng một tầng:

| Tầng | Giữ thế nào | Ví dụ trong research |
|---|---|---|
| **Ranh giới cứng** | giữ nguyên, câu lệnh ngắn | không bịa số/nguồn; nguồn X không làm bằng chứng; mọi URL trích dẫn đã mở trong run hoặc cache `FRESH`; 4 trạng thái viết đúng tiếng Việt; không đổi dòng khung; không sửa asset; file giao ra đĩa, không Claude Docs; tên file không tách 3 phần theo ` - `; kết luận không mạnh hơn tiền đề yếu nhất; không kết luận sẵn sàng khai trương khi thiếu 5 điều kiện; không ghi `Bảng 3B` ngoài việc nhà thầu |
| **Mặc định** | "mặc định X, vì Y"; lệch được nếu nói lý do trong reply | budget search/document; độ dài RX; `nhanh` trừ khi user xin `sâu`; ngưỡng ~1/3 claim `dg`; một tài liệu A cho một claim; thứ tự run; frame F1–F10, C1–C7 |
| **Thủ tục** | bỏ, chỉ giữ mục tiêu + lý do một câu | "inspect đúng 2 pha, không nơi nào khác"; mọi `lookup` trong một lần gọi shell; mẫu query viết sẵn; "không re-read block đã viết"; đoạn văn dài bảo vệ một luật |

Luật sinh ra từ lỗi đã ghi trong `tests/TEST-PLAN.md` (danh sách sửa) giữ lại thành một câu "vì …",
không viết thành thủ tục.

Ví dụ viết lại: đoạn "Inspection happens in exactly two phases…" (~20 dòng) → "Inspect cả report
sheet một lần lúc split — lần đó cho cả nội dung lẫn merged ranges. Inspect lại chỉ khi layout đổi;
mỗi lần dump tốn context cho cả phần còn lại của run."

Mục tiêu độ dài: `SKILL.md` ≤ ~450 dòng. Không đặt con số cho reference; chỉ cắt thủ tục.

## 3. Sửa file khác

- `using-doox/SKILL.md`: xoá dòng `research-method`, `contractor-search`, `competitor-research` trong
  bảng định tuyến, mở rộng dòng `market-research` cho cả 3 việc; dòng 302–303 (ai ghi `Bảng 3B`);
  bảng cổng danh tính (dòng 382); "seven ungated skills" → "five".
- `doc-compare/SKILL.md:136`: `research-method`, "Source quality" → `market-research` §5.
- `README.md`: bảng skill, "16 skill (15 + lõi)" → 12 skill, changelog 1.2.1 ghi rõ 3 skill đã gộp
  vào `market-research` (gọi tên cũ sẽ không còn chạy).
- `.claude-plugin/plugin.json`: version 1.2.1.
- Không sửa: `tests/TEST-PLAN.md`, `tests/results/` (lịch sử); `bid-review`, `mail-draft`,
  `project-report` (chỉ nhắc `market-research`).
- Ngoài phạm vi: `Huong dan su dung Doox plugin.docx` (ngoài repo) — hỏi user riêng.

## Kiểm chứng

Repo không có test runner cho skill; kiểm bằng:

- `grep -r "research-method\|contractor-search\|competitor-research"` trong `skills/`, `README.md`,
  `.claude-plugin/` → rỗng.
- Mọi đường dẫn file skill nhắc tới đều tồn tại.
- Frontmatter hợp lệ; `description` ≤ 1024 ký tự; còn 12 thư mục skill (`project-insights` đã bị xoá
  từ trước, ngoài đợt này).
- `python scripts/wb.py cells` trên asset chạy được và ra 158 ô ghi được.
- Mọi ranh giới cứng ở bảng §2 còn hiện diện trong bản mới (checklist so với bản cũ).
- Chạy lại T16 (`market-research`, gom thông tin thiếu vào một structured call) và T07
  (`doc-compare`, nay trỏ sang `market-research` §5) qua sandbox, so với kết quả ĐẠT cũ.
- TEST-PLAN không có ca nào chạy research thật (tìm nhà thầu, so đối thủ, điền workbook). Việc nới
  3 tầng ở những phần này chỉ được kiểm bằng checklist ranh giới cứng ở trên — ghi rõ trong reply.
