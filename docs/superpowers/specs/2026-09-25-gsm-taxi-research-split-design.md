# GSM taxi điện — tách market-research, chuyển domain, sửa form (bản 1.2.0)

Duyệt 25/09/2026. Khách là GSM: hãng taxi điện **tự vận hành đội xe**, mở rộng sang Bờ Biển Ngà,
Philippines, Kenya. Nguồn domain: khung của khách `CEO_External_Research_Framework_Electric_Taxi_v2`
(đã có trong plugin: RX1–RX5, R01–R52, K01–K56).

## 1. Tách market-research thành 3 skill + 1 lõi

| Skill | Nội dung |
|---|---|
| `research-method` (nội bộ, như `using-doox`) | §4 claim split, §5 nguồn A/B/C/X, §8 freshness, §9 engine + budget + dispatch, §10 ledger/cache, §11 normalise, audit A–D; `scripts/wb.py`, `scripts/cache.py`; `assets/form-research.md`; `references/topic-lenses.md`, `metrics.md`, `dispatch.md`, `final-audit.md` |
| `market-research` | Đánh giá thị trường/khu vực: workbook taxi, câu hỏi lẻ → RX1/RX4/RX5 `.docx` |
| `contractor-search` | Tìm nhà thầu/đối tác: Bảng 3B, frame-first, scoring, saturation; RX3 tóm tắt |
| `competitor-research` | So sánh mình với đối thủ: RX2 `.docx` |

Ba skill người dùng thấy đều "Load `research-method` first". Một run kết hợp (thị trường + nhà thầu +
đối thủ) dùng chung một ledger/cache.

## 2. Domain taxi điện

- Workbook `khung-bao-cao-thi-truong.xlsx`: giữ bố cục (Bảng 1–4, Kết luận pháp lý, Kết luận cuối,
  3B, 00 - Hướng dẫn), thay dòng theo lens R01–R52. Bảng 3B mặc định: nhà thầu xây depot + lắp sạc
  cho đội xe (R23). Đối tác khác (xe, bảo dưỡng, công nghệ gọi xe…) đánh giá theo RX3.
- Đối thủ: taxi/gọi xe ô tô (trực tiếp), xe ôm công nghệ/buýt (gián tiếp), OEM/tập đoàn vận tải
  (tiềm năng). Frame: cấp phép vận tải, đăng ký phương tiện, hồ sơ công ty, app/bảng giá, báo chí.
  10 tiêu chí: đội xe hoạt động, vùng phủ, điện hoá, phân khúc, giá cước/hoa hồng, chất lượng dịch
  vụ, kênh đặt xe, mô hình tài xế, hậu thuẫn, rào cản.
- Sạc chỉ còn là sạc cho đội xe (R11, R20–R22, R24).
- Dọn tham chiếu trạm sạc ở `using-doox`, `doc-compare`.

## 3. doc-compare
Thêm mục từ khoá chính; xác thực với nguồn công khai khi user yêu cầu (dùng lớp nguồn của
`research-method`).

## 4. Form các skill khác
- `mail-draft`: CEO/ngoài công ty dùng đúng `template_*` EX của khách (kể cả `template_subject`);
  form nhà 4 mục chỉ cho mail nội bộ dự án tiếng Việt. Bổ sung độ dài EX4/EX5; sửa mâu thuẫn mail
  tiếng Anh.
- Dấu thiếu dữ liệu thống nhất `[INPUT NEEDED: …]` cho mail/report/research.
- `project-report`: bỏ tham chiếu `core_output` không tồn tại; tên VN cho GX1–GX5; `[Thị trường]`
  tuỳ chọn; chat nói tên VN, không in mã.
- RX: giữ nhãn suy luận/kịch bản cạnh 4 trạng thái; áp `default_length`.
- `candidate-review`: khung 2 nhánh — A tài xế/kỹ thuật viên, B văn phòng/quản lý; ngôn ngữ theo
  thị trường; giấy phép lao động.
- `bid-review`: thêm `assets/` khung tiêu chí theo loại nhà cung cấp GSM; shortlist "tối đa";
  lưu thêm `.docx`.

## 5. Đi kèm
README, hướng dẫn `.docx`, version 1.2.0 (có skill mới). Không đọc video (chưa kiểm năng lực Cowork).

## Kiểm chứng
- `wb.py cells` chạy trên khung mới; số ô ghi được và dòng tiêu đề khớp với văn bản skill.
- `grep` không còn "trạm sạc/CPO/charging station" ngoài phạm vi sạc đội xe.
- Mọi đường dẫn file được skill nhắc tới đều tồn tại.
- Frontmatter 16 skill hợp lệ.
