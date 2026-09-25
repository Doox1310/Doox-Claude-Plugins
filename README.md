# Doox Assistant

Trợ lý AI hỗ trợ quản lý và vận hành dự án: cập nhật kế hoạch, theo dõi & dự báo tiến độ, nhắc việc,
tổng hợp báo cáo, quản lý tri thức; đồng thời phân tích tài liệu, BOQ, báo giá, hồ sơ nhà thầu và
nghiên cứu thị trường theo khung tiêu chuẩn.

16 skill markdown thuần (15 skill dùng trực tiếp + `research-method` là lõi nội bộ). Không có thư viện Python trung tâm; 3 skill mang script riêng.

Dùng được bằng **tiếng Việt, tiếng Anh và tiếng Pháp**. Luật ngôn ngữ nằm một chỗ — `using-doox`, mục
"Language" (và `DR3b` cho 3 skill tài liệu không nạp `using-doox`): nhãn theo ngôn ngữ user, **dữ liệu
giữ nguyên ngôn ngữ của nguồn**, mail theo ngôn ngữ người nhận, ngày luôn `dd/mm/yyyy`. Khung
`.xlsx` của `market-research` giữ tiếng Việt vì đó là hợp đồng đầu ra của file, không phải lựa chọn
dịch thuật.

Ba skill chạy theo **thư viện form** đặt trong `assets/`: `mail-draft` (EX1–EX5), `project-report`
(GX1–GX5, nhánh ngoài báo cáo tiến độ) và bộ skill nghiên cứu (RX1–RX5 trong `research-method`, cho phần trả lời ngoài workbook, ghi ra `.docx`,
kèm 2 reference tra cứu: topic lens và từ điển chỉ số — lấy từ khung taxi điện của khách). Sửa file form là đổi hành vi — không cần
sửa `SKILL.md`.

## Cài

```
/plugin marketplace add Doox1310/Doox-Claude-Plugins
/plugin install doox-assistant@doox
```

Khởi động lại phiên sau khi bật — skill nạp lúc session start.

Hai lệnh trên là của Claude Code. Trên Cowork: tab Cowork → Customize → Plugins → **Add marketplace**,
nhập `Doox1310/Doox-Claude-Plugins`, rồi cài `doox-assistant` như plugin thường.

## Skill

| Skill | Dùng khi | Ra |
|---|---|---|
| `using-doox` | luôn luôn, trước các skill đọc file kế hoạch | quy ước dùng chung, không in gì |
| `project-report` | hỏi một thị trường đang thế nào, kể cả từ checklist/tracker ngoài chuẩn; hoặc xin một báo cáo quản trị khác (quyết định, kế hoạch, rủi ro, biên bản) | 4 bảng trong chat, hoặc một form GX1–GX5 trong chat — kèm bản `.docx` |
| `reminder` | hỏi hôm nay phải xử lý gì | bảng trong chat + draft Outlook mỗi PIC (chỉ vai trò PM) |
| `project-insights` | hỏi đang vướng gì, rủi ro tiến độ, bao giờ xong | 4 mục trong chat; file khi được yêu cầu |
| `project-update` | báo một đầu việc đổi trạng thái / hạn / vướng mắc; cập nhật checklist/báo cáo từ nguồn khác | ghi vào file kế hoạch sau khi xác nhận; file ngoài chuẩn ra bản copy mới có ngày |
| `plan-consolidation` | quy hoạch nhiều kế hoạch về một form, hoặc gộp | file `.xlsx` mới |
| `market-research` | đánh giá thị trường / khu vực taxi điện | `.xlsx` theo khung taxi; câu hỏi lẻ ra `.docx` theo RX |
| `contractor-search` | tìm nhà thầu depot & sạc cho đội xe, đánh giá đối tác | `Bảng 3B` trong workbook + tóm tắt RX3 |
| `competitor-research` | so sánh mình với đối thủ taxi / gọi xe | `.docx` theo RX2 |
| `research-method` | không gọi trực tiếp — lõi phương pháp của 3 skill trên | không in gì |
| `doc-compare` | đọc, tóm tắt, so sánh tài liệu, rút từ khoá; xác thực nguồn công khai khi được yêu cầu | bảng trong chat |
| `doc-translate` | dịch `.docx` / `.xlsx` / `.pptx` giữ layout | file dịch mới |
| `bid-review` | duyệt báo giá, duyệt hồ sơ năng lực | bảng so sánh + shortlist trong chat + bản `.docx` |
| `candidate-review` | đánh giá CV / phỏng vấn ứng viên | bảng chấm trong chat + bản `.docx` |
| `mail-draft` | soạn mail từ memo hoặc dữ liệu có sẵn | draft Outlook + bản in trong chat, theo form EX1–EX5 |
| `calendar` | đặt lịch, xếp lịch, xem lịch | event Google Calendar sau khi xác nhận |

## Phụ thuộc ngoài — đọc trước khi trông cậy

Plugin này **không tự chạy được gì theo lịch**. Không hook, không cron, không slash command;
`plugin.json` chỉ khai metadata.

- **Run nhắc việc 9h sáng.** `reminder` viết cho tình huống "run 9h nổ" và nói rõ phải in báo cáo
  kể cả khi không có việc nào đến hạn, vì một buổi sáng im lặng phải có nghĩa là run hỏng. **Cái
  hẹn giờ đó là của Cowork, không nằm trong plugin.** Cài plugin ở nơi khác thì không có run 9h nào
  cả, và không có gì báo cho biết. Muốn có trong Claude Code thì phải tự dựng — `/schedule` hoặc
  một cron ngoài gọi vào.
- **Outlook** — `reminder` và `mail-draft` tạo draft qua connector Outlook. Không có thì in ra chat
  và nói rõ không tạo được draft. Không bao giờ rơi sang nhà cung cấp mail khác.
- **Google Calendar** — `calendar` dùng connector Google, là chỗ duy nhất trong plugin không phải
  Microsoft. Sắp xếp tạm thời.
- **Đọc `.xlsx`** — không harness nào parse `.xlsx` bằng tool đọc file, nên mọi run đọc kế hoạch
  đều chạy `openpyxl` qua shell với `data_only=True`. Cần Python có `openpyxl`.

## Test

Bộ test **không nằm trong repo này**, và đó là chủ ý: fixture của nó là file kế hoạch thật của
khách hàng, không publish được. Nó giữ nội bộ, bên cạnh mã nguồn.

Gồm 16 case phủ cả 13 skill, chấm hai thứ:

- **độ chính xác** — số liệu, phân loại, trích dẫn khớp bộ đọc tham chiếu (`groundtruth.py`);
- **độ kỷ luật** — không bịa dữ liệu, không ghi vào file khách ngoài `project-update`, không gửi
  mail hay tạo lịch khi chưa duyệt, không rò dữ liệu chéo giữa các vai trò.

Kết quả lần chạy gần nhất trên bản `0.9.x`: **16/16 ĐẠT**, SHA-256 của cả 5 bản copy file kế
hoạch trong sandbox giống hệt bản gốc — không skill nào ghi vào `.xlsx`. Bản `1.0.0` đổi tên
plugin và tách 3 reference, bản `1.1.0` thêm thư viện form EX/GX/RX và nhánh báo cáo quản trị của
`project-report` — cả hai đều cần chạy lại, và `1.1.0` cần thêm case cho việc chọn nhầm nhánh. Bản `1.2.0` chuyển bộ nghiên cứu sang taxi điện (GSM), tách
`market-research` thành 3 skill trên lõi `research-method` và thêm khung nháp cho `candidate-review`,
`bid-review` — cần case cho việc chọn đúng skill nghiên cứu và cho khung Excel taxi mới.

Muốn dựng bộ test cho bản fork của mình thì cần: một file kế hoạch theo đúng quy ước
`[Thị trường] - [Tên dự án] - [Tên PM]`, một bộ đọc tham chiếu độc lập với skill để so kết quả,
và sandbox có/không có `README.md` để thử cổng danh tính.
