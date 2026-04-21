from app.database import get_connection


def find_by_barcode(ma_vach: str) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT MaSP, TenSP, DonGia, DonViTinh, SoLuongTon
        FROM   SanPham
        WHERE  MaVach = ? AND TrangThai = 1
        """,
        (ma_vach,),
    )
    row = cursor.fetchone()
    cursor.close()
    if row is None:
        return None
    return {
        "ma_sp":        row.MaSP,
        "ten_sp":       row.TenSP,
        "don_gia":      float(row.DonGia),
        "don_vi_tinh":  row.DonViTinh,
        "so_luong_ton": row.SoLuongTon,
    }
