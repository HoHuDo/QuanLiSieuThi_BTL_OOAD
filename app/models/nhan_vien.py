from app.database import get_connection
import uuid
import hashlib
import unicodedata


def find_by_credentials(ten_dang_nhap: str, mat_khau_hash: str) -> dict | None:
    """
    Trả về dict thông tin nhân viên nếu username + hash khớp,
    trả về None nếu không tìm thấy hoặc tài khoản bị vô hiệu hóa.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT nv.MaNV, nv.HoTen, nv.ViTri, nv.BoPhan, nv.TrangThai,
               vt.TenVaiTro
        FROM   NhanVien nv
        JOIN   VaiTro   vt ON nv.MaVaiTro = vt.MaVaiTro
        WHERE  nv.TenDangNhap = ? AND nv.MatKhauHash = ? AND nv.TrangThai = 1
        """,
        (ten_dang_nhap, mat_khau_hash),
    )
    row = cursor.fetchone()
    cursor.close()
    if row is None:
        return None
    return {
        "ma_nv":     row.MaNV,
        "ho_ten":    row.HoTen,
        "vi_tri":    row.ViTri,
        "bo_phan":   row.BoPhan,
        "vai_tro":   row.TenVaiTro,
    }

def get_roles():
    """Lấy danh sách các vai trò (Quyền)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MaVaiTro, TenVaiTro FROM VaiTro")
    roles = [{"MaVaiTro": row.MaVaiTro, "TenVaiTro": row.TenVaiTro} for row in cursor.fetchall()]
    cursor.close()
    return roles

def get_active_employees(search_term=""):
    """Lấy danh sách nhân viên đang hoạt động (TrangThai = 1)"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT nv.MaNV, nv.HoTen, nv.CCCD, nv.NgaySinh, nv.GioiTinh, 
               nv.SoDienThoai, nv.Email, nv.DiaChi, nv.ViTri, nv.BoPhan, 
               nv.TenDangNhap, vt.TenVaiTro, nv.MaVaiTro
        FROM NhanVien nv
        JOIN VaiTro vt ON nv.MaVaiTro = vt.MaVaiTro
        WHERE nv.TrangThai = 1
    """
    params = []
    if search_term:
        query += " AND (nv.HoTen LIKE ? OR nv.SoDienThoai LIKE ? OR nv.CCCD LIKE ?)"
        term = f"%{search_term}%"
        params.extend([term, term, term])
        
    query += " ORDER BY nv.MaNV DESC"
    
    cursor.execute(query, params)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    return results

def check_unique(cccd, sdt, exclude_ma_nv=None):
    """Kiểm tra CCCD hoặc Số điện thoại có bị trùng không"""
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM NhanVien WHERE (CCCD = ? OR SoDienThoai = ?)"
    params = [cccd, sdt]
    if exclude_ma_nv:
        query += " AND MaNV != ?"
        params.append(exclude_ma_nv)
        
    cursor.execute(query, params)
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

def _remove_accents(input_str):
    s = input_str.lower().replace("đ", "d").replace(" ", "")
    return "".join(c for c in unicodedata.normalize('NFKD', s) if unicodedata.category(c) != 'Mn')

def add_employee(data):
    """Thêm mới nhân viên và tự động tạo tài khoản đăng nhập"""
    conn = get_connection()
    cursor = conn.cursor()
    
    ma_nv = f"EMP-{str(uuid.uuid4())[:4].upper()}"
    base_name = _remove_accents(data["HoTen"])
    username = f"{base_name}_{str(uuid.uuid4())[:4]}"
    
    # Băm mật khẩu mặc định (supermarket@123)
    pwd_hash = hashlib.sha256("supermarket@123".encode('utf-8')).hexdigest()
    
    query = """
        INSERT INTO NhanVien (
            MaNV, HoTen, CCCD, NgaySinh, GioiTinh, SoDienThoai, Email, DiaChi,
            ViTri, BoPhan, MaVaiTro, TenDangNhap, MatKhauHash, TrangThai
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
    """
    params = (
        ma_nv, data["HoTen"], data["CCCD"], data.get("NgaySinh", ""), data.get("GioiTinh", "Khác"),
        data["SoDienThoai"], data.get("Email", ""), data.get("DiaChi", ""),
        data.get("ViTri", ""), data.get("BoPhan", ""), data["MaVaiTro"],
        username, pwd_hash
    )
    try:
        cursor.execute(query, params)
        conn.commit()
        return True, username
    except Exception as e:
        print("Error add_employee:", e)
        return False, str(e)
    finally:
        cursor.close()

def update_employee(ma_nv, data):
    """Cập nhật thông tin nhân viên"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE NhanVien
        SET HoTen=?, CCCD=?, NgaySinh=?, GioiTinh=?, SoDienThoai=?,
            Email=?, DiaChi=?, ViTri=?, BoPhan=?, MaVaiTro=?
        WHERE MaNV=?
    """
    params = (
        data["HoTen"], data["CCCD"], data.get("NgaySinh", ""), data.get("GioiTinh", "Khác"), data["SoDienThoai"],
        data.get("Email", ""), data.get("DiaChi", ""), data.get("ViTri", ""), data.get("BoPhan", ""),
        data["MaVaiTro"], ma_nv
    )
    cursor.execute(query, params)
    conn.commit()
    cursor.close()

def disable_employee(ma_nv):
    """Soft delete: Đổi TrangThai = 0 thay vì xóa vật lý"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE NhanVien SET TrangThai = 0 WHERE MaNV = ?", (ma_nv,))
    conn.commit()
    cursor.close()
