# Doox Assistant

Plugin Claude cho quản lý dự án: cập nhật kế hoạch, theo dõi tiến độ, nhắc việc, báo cáo; phân tích
tài liệu, báo giá, hồ sơ nhà thầu, ứng viên; nghiên cứu thị trường taxi điện.

- 12 skill viết bằng markdown, không có thư viện Python trung tâm; 3 skill có script riêng.
- Hỗ trợ tiếng Việt, Anh, Pháp. Nhãn theo ngôn ngữ người dùng, dữ liệu giữ ngôn ngữ nguồn, mail theo
  ngôn ngữ người nhận, ngày luôn `dd/mm/yyyy`. Chi tiết: `using-doox`, mục "Language" và `DR3b`.

## Cài đặt

**Claude Code**

```
/plugin marketplace add Doox1310/Doox-Claude-Plugins
/plugin install doox-assistant@doox
```

**Cowork:** Customize → Plugins → Add marketplace → `Doox1310/Doox-Claude-Plugins` → cài `doox-assistant`.

Khởi động lại phiên sau khi cài để nạp skill.

## Skill

| Skill | Dùng khi | Kết quả |
|---|---|---|
| `using-doox` | Tự nạp trước mọi yêu cầu Doox: định tuyến, chuỗi skill, luật chung, cổng danh tính | Không in gì |
| `project-report` | Hỏi tình hình một thị trường; xin báo cáo quản trị (quyết định, kế hoạch, rủi ro, biên bản) | Bảng trong chat hoặc form GX1–GX5, kèm `.docx` |
| `reminder` | Hỏi việc cần xử lý hôm nay | Bảng trong chat; draft Outlook cho từng PIC (chỉ vai trò PM) |
| `project-update` | Báo đổi trạng thái / hạn / vướng mắc; đồng bộ từ nguồn khác | Ghi vào file kế hoạch sau khi xác nhận; file ngoài chuẩn → bản copy có ngày |
| `plan-consolidation` | Chuẩn hoá hoặc gộp nhiều kế hoạch về một form | File `.xlsx` mới |
| `market-research` | Đánh giá thị trường taxi điện, tìm nhà thầu depot/sạc, đánh giá đối tác, so sánh đối thủ | `.xlsx` theo khung taxi; câu hỏi lẻ → `.docx` theo RX1–RX5 |
| `doc-compare` | Đọc, tóm tắt, so sánh tài liệu, rút từ khoá | Bảng trong chat |
| `doc-translate` | Dịch `.docx` / `.xlsx` / `.pptx`, giữ layout | File dịch mới |
| `bid-review` | Duyệt báo giá, hồ sơ năng lực | Bảng so sánh + shortlist, kèm `.docx` |
| `candidate-review` | Đánh giá CV, phỏng vấn ứng viên | Bảng chấm điểm, kèm `.docx` |
| `mail-draft` | Soạn mail từ memo hoặc dữ liệu có sẵn | Draft Outlook + bản in trong chat, theo form EX1–EX5 |
| `calendar` | Đặt, xếp, xem lịch | Event Google Calendar sau khi xác nhận |

`mail-draft`, `project-report`, `market-research` lấy mẫu đầu ra từ thư mục `assets/`. Sửa file form
để đổi hành vi, không cần sửa `SKILL.md`.

## Yêu cầu và giới hạn

Plugin không có hook, cron hay slash command; `plugin.json` chỉ chứa metadata.

- **Nhắc việc định kỳ** do Cowork hẹn giờ, không nằm trong plugin. Môi trường khác cần tự dựng
  (`/schedule` hoặc cron ngoài). `reminder` luôn in báo cáo kể cả khi không có việc đến hạn — không
  có báo cáo nghĩa là run lỗi.
- **Outlook** — `reminder`, `mail-draft` tạo draft qua connector Outlook. Thiếu connector thì in ra
  chat và báo rõ; không dùng nhà cung cấp mail khác.
- **Google Calendar** — `calendar` dùng connector Google (tạm thời).
- **Python + `openpyxl`** — bắt buộc để đọc `.xlsx` (`data_only=True`).

## Kiểm thử

Bộ test giữ nội bộ vì fixture là file kế hoạch thật của khách hàng. 16 case, chấm hai tiêu chí:

- **Chính xác** — số liệu, phân loại, trích dẫn khớp bộ đọc tham chiếu (`groundtruth.py`).
- **Kỷ luật** — không bịa dữ liệu, không ghi file khách ngoài `project-update`, không gửi mail / tạo
  lịch khi chưa duyệt, không rò dữ liệu giữa các vai trò.

Lần chạy gần nhất (`0.9.x`): 16/16 đạt; checksum 5 file kế hoạch không đổi. Từ `1.0.0` chưa chạy lại.

Để dựng test cho bản fork cần: file kế hoạch đặt tên `[Thị trường] - [Tên dự án] - [Tên PM]`, bộ đọc
tham chiếu độc lập với skill, và sandbox có/không có `README.md` để thử cổng danh tính.

## Lịch sử phiên bản

- **1.2.4** — Nhắc việc định kỳ không gắn cứng 9h: `reminder`, `using-doox` gọi là lần chạy theo lịch; README và mô tả plugin viết gọn.
- **1.2.3** — `doc-translate` giữ xuống dòng trong đoạn (`<w:br/>`, `<a:br/>`); `test_ooxml.py` tự kiểm khi chạy không tham số.
- **1.2.2** — `using-doox` giữ job spec theo cuộc chat, quy đổi trạng thái theo file đích; `project-update` đồng bộ đúng phạm vi, nối ghi chú, chế độ chỉ liệt kê; `project-report` sheet Details đủ mọi việc role được xem.
- **1.2.1** — Gộp `research-method`, `contractor-search`, `competitor-research` vào `market-research` (tên cũ không còn chạy). `using-doox` thành bộ điều phối. Viết lại cả 12 skill theo cấu trúc 3 tầng.
- **1.2.0** — Chuyển nghiên cứu sang taxi điện (GSM); thêm khung cho `candidate-review`, `bid-review`.
- **1.1.0** — Thư viện form EX/GX/RX; nhánh báo cáo quản trị cho `project-report`.
- **1.0.0** — Đổi tên plugin, tách 3 reference.
