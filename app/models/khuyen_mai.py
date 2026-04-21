from app.database import get_connection

def get_promotions(search=""):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT MaKM, TenKM, PhanTramGiam, NgayBatDau, NgayKetThuc, TrangThai FROM ChuongTrinhKhuyenMai"
    params = []
    if search:
        query += " WHERE TenKM LIKE ?"
        params.append(f"%{search}%")
    query += " ORDER BY MaKM DESC"
    cursor.execute(query, params)
    cols = [column[0] for column in cursor.description]
    res = [dict(zip(cols, row)) for row in cursor.fetchall()]
    cursor.close()
    return res

def add_promotion(data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO ChuongTrinhKhuyenMai (TenKM, PhanTramGiam, NgayBatDau, NgayKetThuc, TrangThai)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (data['TenKM'], data['PhanTramGiam'], data['NgayBatDau'], data['NgayKetThuc'], data.get('TrangThai', 1)))
        conn.commit()
        return True, ""
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()

def update_promotion(ma_km, data):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE ChuongTrinhKhuyenMai 
            SET TenKM=?, PhanTramGiam=?, NgayBatDau=?, NgayKetThuc=?, TrangThai=?
            WHERE MaKM=?
        """
        cursor.execute(query, (data['TenKM'], data['PhanTramGiam'], data['NgayBatDau'], data['NgayKetThuc'], data.get('TrangThai', 1), ma_km))
        conn.commit()
        return True, ""
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()

def get_active_discount():
    """Lấy phần trăm giảm giá của chương trình đang chạy (Tích hợp POS)"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT TOP 1 PhanTramGiam 
        FROM ChuongTrinhKhuyenMai 
        WHERE NgayBatDau <= GETDATE() AND NgayKetThuc >= GETDATE() AND TrangThai = 1
        ORDER BY PhanTramGiam DESC
    """
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return float(row[0]) if row else 0.0