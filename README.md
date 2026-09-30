# Doox Assistant

Trợ lý AI hỗ trợ quản lý và vận hành dự án: cập nhật kế hoạch, theo dõi & dự báo tiến độ, nhắc việc,
tổng hợp báo cáo, quản lý tri thức; đồng thời phân tích tài liệu, BOQ, báo giá, hồ sơ nhà thầu và
nghiên cứu thị trường theo khung tiêu chuẩn.

12 skill markdown thuần. Không có thư viện Python trung tâm; 3 skill mang script riêng.

Dùng được bằng **tiếng Việt, tiếng Anh và tiếng Pháp**. Luật ngôn ngữ nằm một chỗ — `using-doox`, mục
"Language" (và `DR3b` cho 3 skill tài liệu): nhãn theo ngôn ngữ user, **dữ liệu
giữ nguyên ngôn ngữ của nguồn**, mail theo ngôn ngữ người nhận, ngày luôn `dd/mm/yyyy`. Khung
`.xlsx` của `market-research` giữ tiếng Việt vì đó là hợp đồng đầu ra của file, không phải lựa chọn
dịch thuật.

Ba skill chạy theo **thư viện form** đặt trong `assets/`: `mail-draft` (EX1–EX5), `project-report`
(GX1–GX5, nhánh ngoài báo cáo tiến độ) và `market-research` (RX1–RX5, cho phần trả lời ngoài workbook, ghi ra `.docx`,
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
| `using-doox` | **luôn luôn, trước mọi skill Doox** — bộ điều phối: chọn skill (hoặc chuỗi skill) cho yêu cầu, brief cho agent, luật cứng chung, cổng danh tính | không in gì |
| `project-report` | hỏi một thị trường đang thế nào, kể cả từ checklist/tracker ngoài chuẩn; hoặc xin một báo cáo quản trị khác (quyết định, kế hoạch, rủi ro, biên bản) | 4 bảng trong chat, hoặc một form GX1–GX5 trong chat — kèm bản `.docx` |
| `reminder` | hỏi hôm nay phải xử lý gì | bảng trong chat + draft Outlook mỗi PIC (chỉ vai trò PM) |
| `project-update` | báo một đầu việc đổi trạng thái / hạn / vướng mắc; cập nhật checklist/báo cáo từ nguồn khác | ghi vào file kế hoạch sau khi xác nhận; file ngoài chuẩn ra bản copy mới có ngày |
| `plan-consolidation` | quy hoạch nhiều kế hoạch về một form, hoặc gộp | file `.xlsx` mới |
| `market-research` | đánh giá thị trường / khu vực taxi điện, thông tin & từ khoá quan trọng; tìm nhà thầu depot & sạc cho đội xe, đánh giá đối tác; so sánh mình với đối thủ taxi / gọi xe — một skill, nhiều việc trong một câu vẫn là một run | `.xlsx` theo khung taxi (danh sách nhà thầu ở `Bảng 3B`); câu hỏi lẻ, đối tác có tên, so đối thủ ra `.docx` theo RX |
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
`bid-review` — cần case cho việc chọn đúng skill nghiên cứu và cho khung Excel taxi mới. Bản `1.2.1`
gộp lại `research-method`, `contractor-search`, `competitor-research` vào **một** `market-research`
(gọi tên cũ không còn chạy) và viết lại theo 3 tầng: ranh giới cứng giữ nguyên, còn lại là mặc định
có lý do mà model được lệch nếu nói rõ trong reply. Cũng trong `1.2.1`, `using-doox` thành bộ điều
phối nạp trước **mọi** yêu cầu Doox (định tuyến, chuỗi skill, brief cho agent, 7 luật cứng chung), và
cả 12 skill viết lại theo cùng 3 tầng.
Bản `1.2.2`, sau khi thử chuỗi prompt thật của khách (CIV): `using-doox` giữ job spec theo cuộc chat
("xác nhận hiểu" → tóm tắt rồi làm tiếp; "kế hoạch gốc vừa cập nhật" → chạy lại từ output gần nhất,
báo delta), quy đổi trạng thái theo từ vựng file đích, dịch nội dung khi user yêu cầu; `project-update`
đồng bộ đúng phạm vi, nối ghi chú, chế độ chỉ liệt kê, nguồn là sheet khác; `project-report` sheet
Details đủ mọi việc role được xem.
Bản `1.2.3`: `doc-translate` giữ đúng chỗ xuống dòng trong một đoạn (`<w:br/>`, `<a:br/>`) khi dịch —
trước đó bản dịch của một ô nhiều dòng dồn hết lên dòng đầu; `test_ooxml.py` chạy không tham số là tự kiểm.

Muốn dựng bộ test cho bản fork của mình thì cần: một file kế hoạch theo đúng quy ước
`[Thị trường] - [Tên dự án] - [Tên PM]`, một bộ đọc tham chiếu độc lập với skill để so kết quả,
và sandbox có/không có `README.md` để thử cổng danh tính.
