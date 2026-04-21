import uuid
from datetime import datetime
from app.database import get_connection

def generate_ma_kh():
    """Sinh mã KH theo định dạng MEM-YYYYMMDD-XXXX"""
    date_str = datetime.now().strftime("%Y%m%d")
    random_str = str(uuid.uuid4())[:4].upper()
    return f"MEM-{date_str}-{random_str}"

def get_customers(search_term: str = "") -> list[dict]:
    """Lấy danh sách khách hàng, hỗ trợ tìm kiếm theo Tên hoặc SĐT"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT MaKH, HoTen, SoDienThoai, Email, NgaySinh, GioiTinh, DiaChi,
               DiemTichLuy, HangThanhVien, TrangThai
        FROM KhachHang
    """
    params = []
    
    if search_term:
        query += " WHERE HoTen LIKE ? OR SoDienThoai LIKE ?"
        term = f"%{search_term}%"
        params.extend([term, term])
        
    query += " ORDER BY MaKH DESC"
    
    cursor.execute(query, params)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    return results

def check_phone_exists(phone: str, exclude_ma_kh: str = None) -> bool:
    """Kiểm tra SĐT đã tồn tại chưa (khi cập nhật thì bỏ qua chính khách hàng đó)"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT COUNT(*) FROM KhachHang WHERE SoDienThoai = ?"
    params = [phone]
    
    if exclude_ma_kh:
        query += " AND MaKH != ?"
        params.append(exclude_ma_kh)
        
    cursor.execute(query, params)
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

def add_customer(data: dict) -> bool:
    """Thêm mới khách hàng vào CSDL"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO KhachHang (
            MaKH, HoTen, SoDienThoai, Email, NgaySinh, GioiTinh, DiaChi,
            DiemTichLuy, HangThanhVien, TrangThai
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    ma_kh = generate_ma_kh()
    
    params = (
        ma_kh, data.get("HoTen"), data.get("SoDienThoai"), data.get("Email", ""),
        data.get("NgaySinh", ""), data.get("GioiTinh", "Khác"), data.get("DiaChi", ""),
        0, "Bạc", 1
    )
    
    try:
        cursor.execute(query, params)
        conn.commit()
        return True
    except Exception as e:
        print("Error add_customer:", e)
        return False
    finally:
        cursor.close()

def update_customer(ma_kh: str, data: dict) -> bool:
    """Cập nhật thông tin khách hàng"""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        UPDATE KhachHang
        SET HoTen = ?, SoDienThoai = ?, Email = ?, NgaySinh = ?,
            GioiTinh = ?, DiaChi = ?
        WHERE MaKH = ?
    """
    params = (
        data.get("HoTen"), data.get("SoDienThoai"), data.get("Email", ""),
        data.get("NgaySinh", ""), data.get("GioiTinh", "Khác"), data.get("DiaChi", ""),
        ma_kh
    )
    
    try:
        cursor.execute(query, params)
        conn.commit()
        return True
    except Exception as e:
        print("Error update_customer:", e)
        return False
    finally:
        cursor.close()