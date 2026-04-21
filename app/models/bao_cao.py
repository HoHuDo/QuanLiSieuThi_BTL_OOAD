from app.database import get_connection

def get_revenue_summary(start_date: str, end_date: str):
    """Lấy tổng doanh thu, lợi nhuận, và số hóa đơn"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        WITH CTE_HoaDon AS (
            SELECT MaHD, TienThanhToan
            FROM HoaDon
            WHERE NgayLap >= ? AND NgayLap <= ? AND TrangThai = N'Hoàn thành'
        )
        SELECT 
            (SELECT COUNT(*) FROM CTE_HoaDon) AS TongSoHoaDon,
            (SELECT ISNULL(SUM(TienThanhToan), 0) FROM CTE_HoaDon) AS TongDoanhThu,
            (SELECT ISNULL(SUM(ct.SoLuong * (ct.DonGia - ISNULL(GiaVon.GiaNhap, ct.DonGia * 0.7))), 0)
             FROM CTE_HoaDon hd
             JOIN ChiTietHoaDon ct ON hd.MaHD = ct.MaHD
             OUTER APPLY (
                 SELECT TOP 1 pn.GiaNhap 
                 FROM ChiTietPhieuNhap pn 
                 WHERE pn.MaSP = ct.MaSP 
                 ORDER BY pn.MaPhieuNhap DESC
             ) AS GiaVon
            ) AS TongLoiNhuan
    """
    cursor.execute(query, (f"{start_date} 00:00:00", f"{end_date} 23:59:59"))
    row = cursor.fetchone()
    cursor.close()
    
    if row:
        return {"so_hd": row.TongSoHoaDon, "doanh_thu": row.TongDoanhThu, "loi_nhuan": row.TongLoiNhuan}
    return {"so_hd": 0, "doanh_thu": 0, "loi_nhuan": 0}

def get_daily_revenue(start_date: str, end_date: str):
    """Lấy doanh thu theo từng ngày để vẽ Biểu đồ cột"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT CAST(NgayLap AS DATE) as Ngay, SUM(TienThanhToan) as DoanhThu
        FROM HoaDon
        WHERE NgayLap >= ? AND NgayLap <= ? AND TrangThai = N'Hoàn thành'
        GROUP BY CAST(NgayLap AS DATE)
        ORDER BY Ngay
    """
    cursor.execute(query, (f"{start_date} 00:00:00", f"{end_date} 23:59:59"))
    results = [{"ngay": row.Ngay.strftime("%d/%m"), "doanh_thu": float(row.DoanhThu)} for row in cursor.fetchall()]
    cursor.close()
    return results

def get_category_revenue(start_date: str, end_date: str):
    """Lấy doanh thu theo danh mục để vẽ Biểu đồ tròn"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT dm.TenDanhMuc, SUM(ct.ThanhTien) as DoanhThu
        FROM ChiTietHoaDon ct
        JOIN SanPham sp ON ct.MaSP = sp.MaSP
        JOIN DanhMuc dm ON sp.MaDanhMuc = dm.MaDanhMuc
        JOIN HoaDon hd ON ct.MaHD = hd.MaHD
        WHERE hd.NgayLap >= ? AND hd.NgayLap <= ? AND hd.TrangThai = N'Hoàn thành'
        GROUP BY dm.TenDanhMuc
    """
    cursor.execute(query, (f"{start_date} 00:00:00", f"{end_date} 23:59:59"))
    results = [{"danh_muc": row.TenDanhMuc, "doanh_thu": float(row.DoanhThu)} for row in cursor.fetchall()]
    cursor.close()
    return results

def get_top_products(start_date: str, end_date: str):
    """Lấy top 10 sản phẩm bán chạy nhất"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT TOP 10 sp.MaSP, sp.TenSP, SUM(ct.SoLuong) as TongSL
        FROM ChiTietHoaDon ct
        JOIN SanPham sp ON ct.MaSP = sp.MaSP
        JOIN HoaDon hd ON ct.MaHD = hd.MaHD
        WHERE hd.NgayLap >= ? AND hd.NgayLap <= ? AND hd.TrangThai = N'Hoàn thành'
        GROUP BY sp.MaSP, sp.TenSP
        ORDER BY TongSL DESC
    """
    cursor.execute(query, (f"{start_date} 00:00:00", f"{end_date} 23:59:59"))
    results = [{"ma_sp": row.MaSP, "ten_sp": row.TenSP, "so_luong": row.TongSL} for row in cursor.fetchall()]
    cursor.close()
    return results

def get_inventory_value_report():
    """Lấy danh sách sản phẩm có giá trị tồn kho cao nhất"""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT TOP 50 MaSP, TenSP, SoLuongTon, DonGia, (SoLuongTon * DonGia) as GiaTriTon
        FROM SanPham
        WHERE SoLuongTon > 0
        ORDER BY GiaTriTon DESC
    """
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    return results