# SQL Server connection settings
DB_CONFIG = {
    "server": "LAPTOP-HOAKR68B\SQLEXPRESS",       # hoặc tên máy chủ, VD: "DESKTOP-XYZ\\SQLEXPRESS"
    "database": "QuanLySieuThiDB",
    "trusted_connection": False,  # True = Windows Authentication (khuyên dùng)
    # Nếu dùng SQL Server Auth, đặt trusted_connection = False và điền:
    "username": "sa",
    "password": "123",
}

APP_TITLE = "Quản Lý Siêu Thị Mini"
APP_GEOMETRY = "1280x720"
