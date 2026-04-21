"""
Chạy một lần để cập nhật MatKhauHash trong DB thành SHA-256 thực.
Mật khẩu mặc định cho tất cả tài khoản mẫu: supermarket@123
"""
import sys, os, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database import get_connection

DEFAULT_PASSWORD = "supermarket@123"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT MaNV, TenDangNhap FROM NhanVien")
    rows = cursor.fetchall()

    for row in rows:
        hashed = sha256(DEFAULT_PASSWORD)
        cursor.execute(
            "UPDATE NhanVien SET MatKhauHash = ? WHERE MaNV = ?",
            (hashed, row.MaNV),
        )
        print(f"  Updated {row.TenDangNhap} ({row.MaNV})")

    conn.commit()
    cursor.close()
    print(f"\nXong! Mật khẩu mặc định: {DEFAULT_PASSWORD}")
    print(f"SHA-256 hash           : {sha256(DEFAULT_PASSWORD)}")
