# GPM-Profile-Copy-Tool
Copy thư mục profile GPM với tên profile của nó, giúp đỡ nhầm lẫn

# GPM Profile Copy Tool

**GPM Profile Copy Tool** là một công cụ mạnh mẽ giúp sao chép thư mục profile từ danh sách trong file Excel sang thư mục đích, sử dụng `robocopy` với hiệu suất cao. Công cụ được thiết kế dễ sử dụng, phù hợp với cả người không rành công nghệ.

---

## 🌟 Tính Năng
- **Sao chép thư mục hàng loạt**: Sử dụng thông tin từ file Excel để sao chép thư mục từ nguồn đến đích.
- **Hỗ trợ đa luồng**: Tăng tốc sao chép với `robocopy` (32 luồng mặc định).
- **Giao diện dễ sử dụng**: Hỗ trợ người dùng qua giao diện GUI đơn giản.

---

## 📂 Cấu Trúc Dự Án
```plaintext
GPM-Profile-Copy-Tool/
│
├── copy_dangiaosu.py         # File chính chứa mã nguồn của ứng dụng
├── start.bat                 # File chạy tự động cài đặt và khởi động tool
├── README.md                 # File hướng dẫn sử dụng
```

🛠️ Yêu Cầu Hệ Thống
Hệ điều hành: Windows 7, 8, 10, hoặc 11.
Python: Phiên bản 3.6 trở lên.
Dung lượng trống: Tối thiểu 1GB.
Kết nối mạng Internet (khi cài đặt lần đầu).

## 🔧 Cài Đặt

### 1. Cài đặt Python
- Truy cập trang [https://www.python.org/](https://www.python.org/).
- Tải phiên bản Python mới nhất.
- Trong quá trình cài đặt:
  - Tích chọn **"Add Python to PATH"**.
  - Nhấn **Install Now** để hoàn tất.

### 2. Tải công cụ
- Nếu sử dụng Git:
  - Mở CMD hoặc Terminal, gõ lệnh:
    ```bash
    git clone [https://github.com/yourusername/GPM-Profile-Copy-Tool.git](https://github.com/dangiaosu/GPM-Profile-Copy-Tool)
    ```
    và nhấn **Enter**.
- Hoặc tải file ZIP từ GitHub:
  - Truy cập repository GitHub.
  - Nhấn nút **Code** > **Download ZIP**.
  - Giải nén file ZIP vào một thư mục trên máy tính.

### 3. Chạy file `start.bat`
- Mở thư mục đã giải nén.
- Nhấp đúp chuột vào file **`start.bat`**.
- Hoặc mở CMD, chuyển tới thư mục chứa công cụ, và gõ:
  ```bash
  start.bat

### 4. Sử dụng công cụ
- Sau khi chạy start.bat, giao diện công cụ sẽ hiển thị:
- Chọn file Excel: Nhấn Browse và chọn file Excel chứa thông tin đường dẫn.
- Chọn thư mục đích: Nhấn Browse để chọn thư mục nơi lưu dữ liệu sao chép.
- Điền tên cột:
  - Cột thư mục mới: Nhập tên cột chứa tên thư mục mới từ file Excel.
  - Cột đường dẫn thư mục cũ: Nhập tên cột chứa đường dẫn nguồn từ file Excel.
  - Nhấn Bắt đầu Copy để sao chép dữ liệu.

## 🐔 Về Tác Giả

Xin chào, tôi là **Đan Giáo Sư** – chuyên gia hàng đầu trong việc "lùa gà" và hỗ trợ cộng đồng kiếm tiền online bằng airdrop một cách hiệu quả (và vui vẻ 😄). Với phương châm **"Đơn giản, nhanh gọn, hiệu quả"**, tôi mang đến những công cụ tiện lợi giúp bạn tiết kiệm thời gian và tối ưu hóa quy trình làm việc.

### 🌐 Liên Hệ
- **Facebook**: [Đan Giáo Sư](https://fb.com/prof.danta/)
- **Telegram**: [@dangiaosu](https://t.me/dangiaosu/)
- **Zalo**: [0828092390](tel:0828092390) (Đan Tạ)

📢 **Lời nhắn:** Nếu bạn sử dụng công cụ này và thấy hữu ích, hãy để lại phản hồi. Đọc hướng dẫn tự làm, thắc mắc hỏi đáp = trả tiền.
