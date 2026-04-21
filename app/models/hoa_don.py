from datetime import datetime
from app.database import get_connection


def _gen_ma_hd() -> str:
    return f"HD-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


def create_invoice(
    ma_nv: str,
    cart: list[dict],
    tong_tien: float,
    phuong_thuc: str = "Tiền mặt",
) -> tuple[bool, str, str]:
    """
    Tạo hóa đơn trong một SQL Transaction.
    Trả về (success, message, ma_hd).

    cart item: {"ma_sp", "ten_sp", "don_gia", "so_luong", "thanh_tien"}
    """
    conn = get_connection()
    cursor = conn.cursor()
    ma_hd = _gen_ma_hd()

    try:
        # ── Bước 1: INSERT HoaDon ─────────────────────────────────────────
        cursor.execute(
            """
            INSERT INTO HoaDon
                (MaHD, MaNV, MaKH, MaKM, NgayLap,
                 TongTien, TienGiamGia, TienThanhToan,
                 PhuongThucThanhToan, TrangThai)
            VALUES (?, ?, NULL, NULL, GETDATE(),
                    ?, 0, ?,
                    ?, N'Hoàn thành')
            """,
            (ma_hd, ma_nv, tong_tien, tong_tien, phuong_thuc),
        )

        # ── Bước 2: INSERT ChiTietHoaDon + UPDATE tồn kho ─────────────────
        for item in cart:
            cursor.execute(
                """
                INSERT INTO ChiTietHoaDon (MaHD, MaSP, SoLuong, DonGia, ThanhTien)
                VALUES (?, ?, ?, ?, ?)
                """,
                (ma_hd, item["ma_sp"], item["so_luong"],
                 item["don_gia"], item["thanh_tien"]),
            )

            # WHERE SoLuongTon >= so_luong đảm bảo không xuống âm
            cursor.execute(
                """
                UPDATE SanPham
                SET    SoLuongTon = SoLuongTon - ?
                WHERE  MaSP = ? AND SoLuongTon >= ?
                """,
                (item["so_luong"], item["ma_sp"], item["so_luong"]),
            )
            if cursor.rowcount == 0:
                raise ValueError(
                    f'Sản phẩm "{item["ten_sp"]}" không đủ tồn kho để bán.'
                )

        conn.commit()
        return True, "Thanh toán thành công!", ma_hd

    except Exception as exc:
        conn.rollback()
        return False, str(exc), ""
    finally:
        cursor.close()
