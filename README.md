# 🛒 Hệ thống Quản Lý Siêu Thị Mini (MiniSupermart)

Dự án phần mềm quản lý siêu thị mini trên nền tảng Desktop (Windows), sử dụng Python (CustomTkinter) và SQL Server.

## 1. Yêu cầu hệ thống (Prerequisites)

- **Python** phiên bản 3.8 trở lên.
- **Microsoft SQL Server** (Bản Express hoặc Developer).
- **ODBC Driver for SQL Server** (Thường tự động có khi cài SQL Server. Nếu lỗi, hãy tải ODBC Driver 17 từ trang chủ Microsoft).

## 2. Cài đặt thư viện (Dependencies)

Mở Terminal (hoặc Command Prompt) tại thư mục chứa mã nguồn dự án và chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

_(Hoặc có thể cài thủ công bằng lệnh: `pip install customtkinter pyodbc matplotlib`)_

## 3. Cấu hình Cơ sở dữ liệu (Database)

1. Mở SQL Server Management Studio (SSMS) và chạy file Script tạo CSDL (nếu có) để tạo database `QuanLySieuThiDB` và các bảng dữ liệu.
2. Mở file `config.py` bằng trình soạn thảo code.
3. Thay đổi thông số trong `DB_CONFIG` cho khớp với SQL Server trên máy tính của bạn:
   - `server`: Tên Server Name của bạn (Ví dụ: `.\SQLEXPRESS` hoặc `MAYTINH-CUA-TOI\SQLEXPRESS`).
   - `trusted_connection`:
     - Đặt là `True` nếu bạn đăng nhập SQL bằng Windows Authentication (Không cần user/pass).
     - Đặt là `False` nếu bạn dùng tài khoản SQL Server, sau đó điền `username` (thường là `sa`) và `password` ở bên dưới.

## 4. Kiểm tra kết nối SQL Server

Để đảm bảo cấu hình đã chính xác, hãy chạy lệnh sau:

```bash
python test_connection.py
```

> Nếu terminal in ra thông báo kết nối thành công, bạn có thể đi tiếp. Nếu báo lỗi, hãy kiểm tra lại thông tin trong `config.py`.

## 5. Thiết lập Tài khoản đăng nhập

Mật khẩu trong cơ sở dữ liệu được mã hóa bảo mật (SHA-256). Lần đầu tiên tải code về, bạn cần chạy đoạn script sau để reset mật khẩu của tất cả nhân viên mẫu về mặc định:

```bash
python scripts/update_password_hashes.py
```

> Mật khẩu mặc định cho toàn bộ tài khoản sau khi chạy lệnh này là: **supermarket@123**

## 6. Khởi chạy Ứng dụng

Sau khi hoàn tất các bước trên, khởi động ứng dụng bằng lệnh:

```bash
python main.py
```

---

### 🔑 Hướng dẫn đăng nhập (Dành cho người Test)

- **Tên đăng nhập:** Hãy mở SQL Server, vào bảng `NhanVien` cột `TenDangNhap` để lấy một tên đăng nhập bất kỳ (Nên chọn nhân viên có `MaVaiTro` là Quản lý để xem được toàn bộ tính năng).
- **Mật khẩu:** `supermarket@123`

_Chúc bạn cài đặt thành công!_
"# QuanLiSieuThi_BTL_OOAD" 
