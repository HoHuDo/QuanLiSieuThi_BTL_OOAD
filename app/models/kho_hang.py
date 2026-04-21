from app.database import get_connection

def get_inventory_products(search_term: str = "") -> list[dict]:
    """
    Lấy danh sách sản phẩm trong kho.
    Hỗ trợ lọc theo Tên sản phẩm hoặc Mã vạch.
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT sp.MaSP, sp.MaVach, sp.TenSP, dm.TenDanhMuc,
               sp.DonViTinh, sp.SoLuongTon, sp.TonKhoToiThieu, sp.DonGia
        FROM SanPham sp
        LEFT JOIN DanhMuc dm ON sp.MaDanhMuc = dm.MaDanhMuc
    """
    params = []
    
    if search_term:
        query += " WHERE sp.TenSP LIKE ? OR sp.MaVach LIKE ?"
        like_term = f"%{search_term}%"
        params.extend([like_term, like_term])
        
    query += " ORDER BY sp.MaSP"
    
    cursor.execute(query, params)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    cursor.close()
    return results

def update_stock(ma_sp: str, quantity_change: int) -> bool:
    """Cập nhật số lượng tồn kho của sản phẩm (cộng thêm hoặc trừ đi)"""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE SanPham
            SET SoLuongTon = SoLuongTon + ?
            WHERE MaSP = ?
        """
        cursor.execute(query, (int(quantity_change), str(ma_sp)))
        conn.commit()
        return True
    except Exception as e:
        print("Error update_stock:", e)
        return False
    finally:
        cursor.close()
