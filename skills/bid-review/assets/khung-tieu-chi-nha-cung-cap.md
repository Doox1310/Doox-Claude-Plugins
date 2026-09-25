# Khung tiêu chí nhà cung cấp — GSM

> **BẢN NHÁP.** Khung này do Doox soạn để skill chạy được ngay khi GSM chưa gửi khung chính thức.
> Sửa file này là đổi khung — không cần sửa `SKILL.md`. Tiêu chí user đưa trong phiên luôn thắng
> khung này cho phạm vi đó.

GSM tự vận hành đội taxi điện: sở hữu xe, thuê tài xế, app đặt xe + điều phối, sạc tại depot.
Mỗi loại nhà cung cấp có hai lớp:

- **Bắt buộc** — chấm `Đạt` / `Thiếu`. `Thiếu` ở một mục bắt buộc là căn cứ loại (§3.4 / §4.4).
  Mục chưa có bằng chứng là `Chưa xác minh`, không phải `Đạt`.
- **Chấm mức** — so mức đáp ứng giữa các bên; không tự đặt thang điểm nếu user không đưa trọng số.

Ngưỡng cụ thể (số năm bảo hành, uptime, hạn mức bảo hiểm…) do user nêu. Khung chỉ nói **xét gì** và
**bằng chứng nào được tính** — không tự điền con số.

---

## 1. Xe — hãng / nhà phân phối

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Đúng model/phiên bản được phép lưu hành tại nước sở tại (homologation) | Giấy chứng nhận / phê duyệt kiểu loại cho đúng model, năm, thị trường |
| Bắt buộc | Bảo hành áp dụng cho **xe dùng làm taxi** (xe, pin) | Điều khoản bảo hành bằng văn bản; bảo hành xe cá nhân thường loại trừ taxi |
| Bắt buộc | Là nhà phân phối được hãng uỷ quyền tại thị trường | Thư uỷ quyền của hãng |
| Chấm mức | Giá lăn bánh (landed cost): giá xe, thuế, phí, vận chuyển, đăng ký | Báo giá tách từng khoản |
| Chấm mức | Phụ tùng: sẵn kho tại chỗ, thời gian cấp | Danh mục + cam kết thời gian; catalog không phải tồn kho |
| Chấm mức | Tiến độ giao xe theo lô | Lịch giao cam kết trong báo giá/hợp đồng |
| Chấm mức | Quãng đường thực tế theo ca, sạc DC | Dữ liệu vận hành thực tế; quãng đường quảng cáo không tính |

## 2. Xây dựng depot & thi công hạ tầng sạc

Hồ sơ năng lực map lên 12 nhóm (là hàng của ma trận §4.5):

pháp lý/chứng chỉ · kinh nghiệm tương tự · năng lực civil · điện/utility · permit · HSE · QA/QC ·
nhân sự chủ chốt · tài chính · năng lực triển khai đồng thời · thầu phụ · bảo hành & phạm vi địa bàn

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Giấy phép hành nghề xây dựng / điện đúng cấp công việc | Bản chụp giấy phép, đúng pháp nhân dự thầu |
| Bắt buộc | Ít nhất một dự án tương tự đã bàn giao | Tên chủ đầu tư, phạm vi, năm; xác nhận của chủ đầu tư nếu có |
| Chấm mức | Các nhóm còn lại trong 12 nhóm | Hồ sơ dự án, chứng chỉ, báo cáo tài chính, hồ sơ nhân sự; ảnh/logo không tính |
| Chấm mức | Phần tự làm vs giao thầu phụ | Danh sách thầu phụ và phạm vi |

## 3. Thiết bị sạc

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Chứng nhận an toàn/hợp chuẩn cho đúng model tại thị trường | Chứng nhận ghi model, có thể tra với nơi cấp |
| Bắt buộc | Tương thích với xe GSM chọn (đầu nối, giao thức) | Kết quả thử với đúng xe/phiên bản; hỗ trợ giao thức ≠ tương thích đầy đủ |
| Chấm mức | Công suất, số cổng đồng thời, phân bổ công suất | Datasheet; công suất đỉnh ≠ công suất trung bình |
| Chấm mức | Phần mềm quản lý sạc, dữ liệu, chuyển đổi backend khi đổi nhà cung cấp | Tài liệu giao thức mở, điều khoản dữ liệu |
| Chấm mức | Hỗ trợ kỹ thuật tại chỗ, thời gian khắc phục, phụ tùng | Cam kết SLA; helpdesk toàn cầu ≠ đội hiện trường |
| Chấm mức | Tham chiếu vận hành | Địa điểm đang chạy, liên hệ xác minh được |

## 4. Công nghệ đặt xe / điều phối

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Các chức năng GSM yêu cầu: đặt xe, điều phối, app tài xế, quản lý đội xe, thanh toán | Demo/bản đang chạy của đúng phiên bản; roadmap không tính |
| Bắt buộc | Quyền sở hữu và xuất dữ liệu (khách, chuyến, tài xế) khi chấm dứt hợp đồng | Điều khoản hợp đồng, tài liệu API |
| Chấm mức | API tích hợp (sạc, thanh toán, kế toán) | Tài liệu API công bố |
| Chấm mức | Uptime cam kết, cơ chế đền bù | SLA bằng văn bản |
| Chấm mức | Bảo mật & dữ liệu cá nhân theo luật nước sở tại | Chứng nhận + mô tả kiểm soát; chứng nhận không phải bảo mật đầy đủ |
| Chấm mức | Tổng phí: bản quyền, theo chuyến, module thêm, triển khai, chuyển đổi, hỗ trợ | Bảng phí đầy đủ; phí ẩn = `Chưa có thông tin` |
| Chấm mức | Hỗ trợ ngôn ngữ/nội địa hoá, đội triển khai tại chỗ | Tài liệu, danh sách nhân sự |

## 5. Bảo hiểm

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Nhận bảo hiểm **xe taxi thương mại** (không phải xe cá nhân) | Điều khoản đơn bảo hiểm / thư chào ghi rõ mục đích sử dụng |
| Bắt buộc | Công ty được cấp phép kinh doanh bảo hiểm tại nước sở tại | Giấy phép / tra cứu cơ quan quản lý |
| Chấm mức | Phạm vi: vật chất xe, pin, trách nhiệm dân sự, hành khách, tài xế | Quy tắc bảo hiểm |
| Chấm mức | Điều khoản loại trừ | Toàn văn loại trừ; bản tóm tắt marketing không tính |
| Chấm mức | Quy trình và thời gian bồi thường, xưởng liên kết | Quy trình bằng văn bản |
| Chấm mức | Phí, mức khấu trừ | Báo giá tách từng hạng mục |

## 6. Tài chính / thuê mua xe

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Được cấp phép cho vay/cho thuê tài chính tại nước sở tại | Giấy phép |
| Bắt buộc | Chấp nhận xe dùng làm taxi | Điều kiện cấp vốn bằng văn bản |
| Chấm mức | Chi phí thực: lãi suất (quy về cùng cách tính), phí, đặt cọc | Bảng điều khoản; lãi phẳng và lãi dư nợ giảm dần phải quy đổi |
| Chấm mức | Rủi ro tỷ giá, điều kiện vỡ nợ, tất toán sớm, mua lại cuối kỳ | Dự thảo hợp đồng |

## 7. Bảo dưỡng, sửa chữa, cứu hộ

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Kỹ thuật viên có chứng chỉ an toàn điện cao áp | Chứng chỉ của nhân sự |
| Bắt buộc | Sửa không làm mất bảo hành hãng (xưởng được hãng uỷ quyền hoặc hãng chấp thuận) | Văn bản của hãng |
| Chấm mức | Thời gian xe nằm xưởng, không chỉ giờ công | Cam kết SLA |
| Chấm mức | Cứu hộ xe điện: thiết bị, thời gian tiếp cận, phạm vi địa bàn | Danh sách thiết bị, cam kết |
| Chấm mức | Đơn giá công, phụ tùng; xử lý pin thay ra | Bảng giá; đơn vị thu gom/tái chế pin |

## 8. Dịch vụ đội xe hằng ngày

Vệ sinh xe, bãi đỗ, chuẩn bị xe đầu ca, vật tư tiêu hao.

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Giấy phép hoạt động liên quan (nước thải, bãi đỗ) nếu có | Bản chụp giấy phép |
| Chấm mức | Năng lực giờ cao điểm, dự phòng khi gián đoạn | Cam kết số xe/giờ, phương án dự phòng |
| Chấm mức | Tổng giá: vật tư, điện nước, thuế, điều kiện khối lượng | Báo giá tách từng khoản |

## 9. Dịch vụ chuyên môn

Pháp lý, kế toán/thuế, tư vấn cấp phép, tuyển dụng.

| Loại | Tiêu chí | Bằng chứng được tính |
|---|---|---|
| Bắt buộc | Giấy phép hành nghề tại nước sở tại | Giấy phép / đăng ký hành nghề |
| Bắt buộc | Không xung đột lợi ích | Cam kết bằng văn bản |
| Chấm mức | Kinh nghiệm việc tương tự (vận tải, cấp phép taxi, nhà đầu tư nước ngoài) | Việc đã làm có tên khách hàng, năm |
| Chấm mức | Nhân sự trực tiếp phụ trách, ngôn ngữ làm việc | CV nhân sự chủ chốt |
| Chấm mức | Phí: trọn gói hay theo giờ, chi phí phát sinh | Thư chào phí |
