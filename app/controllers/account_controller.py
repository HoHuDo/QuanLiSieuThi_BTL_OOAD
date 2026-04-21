import hashlib
from app.models.nhan_vien import find_by_credentials


def hash_password(raw_password: str) -> str:
    return hashlib.sha256(raw_password.encode("utf-8")).hexdigest()


def authenticate(ten_dang_nhap: str, mat_khau: str) -> tuple[bool, str, dict | None]:
    """
    Xác thực đăng nhập.
    Trả về (success, message, employee_info).
    """
    if not ten_dang_nhap.strip() or not mat_khau.strip():
        return False, "Vui lòng nhập đầy đủ thông tin.", None

    pw_hash = hash_password(mat_khau)
    employee = find_by_credentials(ten_dang_nhap.strip(), pw_hash)

    if employee is None:
        return False, "Tên đăng nhập hoặc mật khẩu không đúng.", None

    return True, f"Đăng nhập thành công! Xin chào, {employee['ho_ten']}.", employee
