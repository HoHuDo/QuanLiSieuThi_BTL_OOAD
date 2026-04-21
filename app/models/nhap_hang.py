import uuid
from datetime import datetime
from app.database import get_connection

def create_import_receipt(ma_ncc, ma_nv, items, tong_tien):
    """
    Thực hiện Transaction: Lưu PhieuNhapHang, ChiTietPhieuNhap và Cập nhật Tồn kho
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        ma_phieu = f"IMP-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:4].upper()}"
        ngay_nhap = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 1. Tạo Phiếu Nhập
        cursor.execute("""
            INSERT INTO PhieuNhapHang (MaPhieuNhap, MaNCC, MaNV, NgayNhap, TongTien, GhiChu)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ma_phieu, ma_ncc, ma_nv, ngay_nhap, tong_tien, ''))

        # 2. Chi tiết + Cập nhật Kho
        for item in items:
            han_sd = item.get('han_sd')
            if not han_sd or han_sd.strip() == "": han_sd = None
                
            cursor.execute("""
                INSERT INTO ChiTietPhieuNhap (MaPhieuNhap, MaSP, SoLuong, DonGiaNhap, SoLo, HanSuDung, ThanhTien)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (ma_phieu, item['ma_sp'], item['so_luong'], item['gia_nhap'], item.get('so_lo', ''), han_sd, item['thanh_tien']))

            cursor.execute("""
                UPDATE SanPham SET SoLuongTon = SoLuongTon + ? WHERE MaSP = ?
            """, (item['so_luong'], item['ma_sp']))

        conn.commit() # Xác nhận toàn bộ thay đổi
        return True, ma_phieu
    except Exception as e:
        conn.rollback() # Hoàn tác nếu có bất kỳ lỗi nào
        return False, str(e)
    finally:
        cursor.close()