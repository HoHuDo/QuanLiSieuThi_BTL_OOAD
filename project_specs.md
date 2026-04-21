MỤC 4: YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)
4.1. Module Bán hàng (Sales Management)
Mã Tên yêu cầu Mô tả chi tiết
FR-S01 Tạo hóa đơn bán hàng Nhân viên thu ngân tạo hóa đơn mới, quét mã vạch sản phẩm để thêm vào hóa đơn. Hệ thống tự động tra cứu giá và tính tổng tiền.
FR-S02 Xử lý thanh toán Hệ thống hỗ trợ thanh toán bằng tiền mặt và thẻ. Tính tiền thối (nếu tiền mặt). In hóa đơn sau khi thanh toán thành công.
FR-S03 Áp dụng khuyến mãi Hệ thống tự động kiểm tra và áp dụng chương trình khuyến mãi hiện hành (giảm giá %, mua X tặng Y) cho hóa đơn.
FR-S04 Hủy/Sửa hóa đơn Cho phép hủy hóa đơn chưa thanh toán hoặc sửa số lượng sản phẩm trong hóa đơn (cần quyền quản lý nếu đã thanh toán).
FR-S05 Xem lịch sử bán hàng Quản lý có thể tra cứu lịch sử bán hàng theo ngày, theo nhân viên, theo sản phẩm. Xem chi tiết từng hóa đơn.
FR-S06 Báo cáo doanh thu Hệ thống tạo báo cáo doanh thu theo ngày/tuần/tháng/năm. Hiển thị dưới dạng bảng và biểu đồ.
4.2. Module Kho hàng (Inventory Management)
Mã Tên yêu cầu Mô tả chi tiết
FR-I01 Quản lý sản phẩm Thêm, sửa, xóa, tìm kiếm sản phẩm. Mỗi sản phẩm có: mã SP, tên, mô tả, đơn giá, đơn vị tính, danh mục, hình ảnh, mã vạch.
FR-I02 Nhập hàng Tạo phiếu nhập hàng từ nhà cung cấp. Ghi nhận số lượng, giá nhập, ngày nhập, lô hàng, hạn sử dụng. Tự động cập nhật tồn kho.
FR-I03 Kiểm kê tồn kho Hiển thị danh sách tồn kho hiện tại. Hỗ trợ lọc theo danh mục, theo trạng thái (còn hàng / sắp hết / hết hàng).
FR-I04 Cảnh báo tồn kho Hệ thống tự động cảnh báo khi số lượng tồn kho của sản phẩm xuống dưới mức tối thiểu đã cấu hình (min stock level).
FR-I05 Quản lý danh mục Thêm, sửa, xóa danh mục sản phẩm (Category). Hỗ trợ phân cấp danh mục (danh mục cha - con).
4.3. Module Khách hàng (Customer Management)
Mã Tên yêu cầu Mô tả chi tiết
FR-C01 Đăng ký thành viên Nhân viên đăng ký khách hàng mới: họ tên, SĐT, email, ngày sinh. Hệ thống tạo mã thành viên và thẻ tích điểm.
FR-C02 Quản lý thông tin KH Tìm kiếm, sửa, xóa (vô hiệu hóa) thông tin khách hàng. Xem lịch sử mua hàng và điểm tích lũy.
FR-C03 Tích điểm Mỗi hóa đơn được tích điểm theo quy tắc: 10.000 VNĐ = 1 điểm. Điểm được cộng tự động khi thanh toán.
FR-C04 Đổi điểm Khách hàng có thể đổi điểm tích lũy lấy voucher giảm giá. Quy tắc đổi: 100 điểm = Voucher giảm 50.000 VNĐ.
FR-C05 Phân hạng thành viên Hệ thống tự động phân hạng: Bạc (0-499 điểm), Vàng (500-1999 điểm), Kim cương (2000+ điểm) với mức ưu đãi tương ứng.
4.4. Module Nhân viên (Employee Management)
Mã Tên yêu cầu Mô tả chi tiết
FR-E01 Quản lý thông tin NV Thêm, sửa, xóa (vô hiệu hóa), tìm kiếm nhân viên. Thông tin: mã NV, họ tên, CCCD, SĐT, email, địa chỉ, ngày vào làm, vị trí, bộ phận.
FR-E02 Đăng nhập hệ thống Nhân viên đăng nhập bằng tài khoản (username/password). Hệ thống xác thực và cấp quyền truy cập tương ứng vai trò.
FR-E03 Phân quyền Quản lý gán vai trò (Cashier, Warehouse Staff, Manager) cho nhân viên. Mỗi vai trò có tập quyền truy cập chức năng khác nhau.
FR-E04 Quản lý ca làm việc Tạo và phân công ca làm việc cho nhân viên. Xem lịch làm việc theo tuần/tháng.

Boundary Classes:

- Giao diện Bán hàng: Hiển thị màn hình quét mã vạch, danh sách sản phẩm trong giỏ hàng, nút thanh toán và in hóa đơn.
- Giao diện Quản lý Kho: Hiển thị danh mục sản phẩm, nút nhập hàng, kiểm kê và cập nhật trạng thái tồn kho.
- Giao diện Quản lý Khách hàng: Biểu mẫu đăng ký thành viên, tra cứu điểm tích lũy và hạng thành viên.
- Giao diện Đăng nhập: Tiếp nhận thông tin tài khoản và mật khẩu từ nhân viên.

Control Classes:

- BanHangController: Tiếp nhận mã vạch từ giao diện, gọi thực thể Sản phẩm để lấy giá, tính tổng tiền, áp dụng khuyến mãi và yêu cầu lưu hóa đơn.
- KhoController: Xử lý logic nhập xuất kho, kiểm tra điều kiện tồn kho tối thiểu và cập nhật số lượng thực tế.
- KhachHangController: Xử lý logic tích điểm dựa trên giá trị hóa đơn và tự động cập nhật hạng thành viên.
- AccountController: Xác thực thông tin đăng nhập và phân quyền truy cập cho các nhân viên khác nhau.

Entity Classes:

- BanHangController: Tiếp nhận mã vạch từ giao diện, gọi thực thể Sản phẩm để - lấy giá, tính tổng tiền, áp dụng khuyến mãi và yêu cầu lưu hóa đơn.
- KhoController: Xử lý logic nhập xuất kho, kiểm tra điều kiện tồn kho tối thiểu và cập nhật số lượng thực tế.
- KhachHangController: Xử lý logic tích điểm dựa trên giá trị hóa đơn và tự động cập nhật hạng thành viên (Vàng, Bạc, Kim cương).
- AccountController: Xác thực thông tin đăng nhập và phân quyền truy cập cho các nhân viên khác nhau.
