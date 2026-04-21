CREATE DATABASE QuanLySieuThiDB;
GO

USE QuanLySieuThiDB;
GO

CREATE TABLE VaiTro (
    MaVaiTro INT IDENTITY(1,1) PRIMARY KEY,
    TenVaiTro NVARCHAR(50) NOT NULL UNIQUE, 
    MoTa NVARCHAR(255)
);

CREATE TABLE NhanVien (
    MaNV VARCHAR(20) PRIMARY KEY, 
    HoTen NVARCHAR(100) NOT NULL,
    CCCD VARCHAR(12) NOT NULL UNIQUE,
    NgaySinh DATE,
    GioiTinh NVARCHAR(10),
    SoDienThoai VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100),
    DiaChi NVARCHAR(255),
    ViTri NVARCHAR(50) NOT NULL,
    BoPhan NVARCHAR(50) NOT NULL,
    NgayVaoLam DATE DEFAULT GETDATE(),
    MaVaiTro INT NOT NULL,
    TenDangNhap VARCHAR(50) NOT NULL UNIQUE,
    MatKhauHash VARCHAR(255) NOT NULL, 
    TrangThai BIT DEFAULT 1, 
    FOREIGN KEY (MaVaiTro) REFERENCES VaiTro(MaVaiTro)
);

CREATE TABLE CaLamViec (
    MaCa INT IDENTITY(1,1) PRIMARY KEY,
    TenCa NVARCHAR(50) NOT NULL, 
    GioBatDau TIME NOT NULL,
    GioKetThuc TIME NOT NULL
);

CREATE TABLE PhanCaNhanVien (
    MaPhanCa INT IDENTITY(1,1) PRIMARY KEY,
    MaNV VARCHAR(20) NOT NULL,
    MaCa INT NOT NULL,
    NgayLamViec DATE NOT NULL,
    FOREIGN KEY (MaNV) REFERENCES NhanVien(MaNV),
    FOREIGN KEY (MaCa) REFERENCES CaLamViec(MaCa),
    CONSTRAINT UQ_NhanVien_Ca_Ngay UNIQUE (MaNV, MaCa, NgayLamViec)
);

CREATE TABLE KhachHang (
    MaKH VARCHAR(20) PRIMARY KEY, 
    HoTen NVARCHAR(100) NOT NULL,
    SoDienThoai VARCHAR(15) NOT NULL UNIQUE,
    Email VARCHAR(100),
    NgaySinh DATE,
    GioiTinh NVARCHAR(10),
    DiaChi NVARCHAR(255),
    HangThanhVien NVARCHAR(20) DEFAULT N'Bạc', 
    DiemTichLuy INT DEFAULT 0,
    TrangThai BIT DEFAULT 1,
    NgayTao DATETIME DEFAULT GETDATE()
);

CREATE TABLE PhieuGiamGia (
    MaPhieu VARCHAR(20) PRIMARY KEY,
    MaKH VARCHAR(20) NOT NULL,
    MaCode VARCHAR(50) NOT NULL UNIQUE,
    GiaTriGiam DECIMAL(18,2) NOT NULL, 
    NgayPhatHanh DATETIME DEFAULT GETDATE(),
    HanSuDung DATETIME NOT NULL,
    DaSuDung BIT DEFAULT 0,
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);

CREATE TABLE DanhMuc (
    MaDanhMuc INT IDENTITY(1,1) PRIMARY KEY,
    TenDanhMuc NVARCHAR(100) NOT NULL,
    MaDanhMucCha INT NULL, 
    TrangThai BIT DEFAULT 1,
    FOREIGN KEY (MaDanhMucCha) REFERENCES DanhMuc(MaDanhMuc)
);

CREATE TABLE NhaCungCap (
    MaNCC INT IDENTITY(1,1) PRIMARY KEY,
    TenNCC NVARCHAR(150) NOT NULL,
    NguoiLienHe NVARCHAR(100),
    SoDienThoai VARCHAR(15) NOT NULL,
    Email VARCHAR(100),
    DiaChi NVARCHAR(255),
    TrangThai BIT DEFAULT 1
);

CREATE TABLE SanPham (
    MaSP VARCHAR(20) PRIMARY KEY, 
    MaVach VARCHAR(50) NOT NULL UNIQUE,
    TenSP NVARCHAR(150) NOT NULL,
    MoTa NVARCHAR(500),
    MaDanhMuc INT NOT NULL,
    DonGia DECIMAL(18,2) NOT NULL CHECK (DonGia >= 0),
    DonViTinh NVARCHAR(20) NOT NULL, 
    HinhAnh VARCHAR(255),
    SoLuongTon INT DEFAULT 0 CHECK (SoLuongTon >= 0),
    TonKhoToiThieu INT DEFAULT 10 CHECK (TonKhoToiThieu >= 0),
    TrangThai BIT DEFAULT 1,
    FOREIGN KEY (MaDanhMuc) REFERENCES DanhMuc(MaDanhMuc)
);

CREATE TABLE PhieuNhapHang (
    MaPhieuNhap VARCHAR(20) PRIMARY KEY, 
    MaNCC INT NOT NULL,
    MaNV VARCHAR(20) NOT NULL,
    NgayNhap DATETIME DEFAULT GETDATE(),
    TongTien DECIMAL(18,2) DEFAULT 0,
    GhiChu NVARCHAR(255),
    FOREIGN KEY (MaNCC) REFERENCES NhaCungCap(MaNCC),
    FOREIGN KEY (MaNV) REFERENCES NhanVien(MaNV)
);

CREATE TABLE ChiTietPhieuNhap (
    MaPhieuNhap VARCHAR(20) NOT NULL,
    MaSP VARCHAR(20) NOT NULL,
    SoLuong INT NOT NULL CHECK (SoLuong > 0),
    GiaNhap DECIMAL(18,2) NOT NULL CHECK (GiaNhap >= 0),
    SoLo VARCHAR(50),
    HanSuDung DATE,
    PRIMARY KEY (MaPhieuNhap, MaSP),
    FOREIGN KEY (MaPhieuNhap) REFERENCES PhieuNhapHang(MaPhieuNhap),
    FOREIGN KEY (MaSP) REFERENCES SanPham(MaSP)
);

CREATE TABLE ChuongTrinhKhuyenMai (
    MaKM INT IDENTITY(1,1) PRIMARY KEY,
    TenKM NVARCHAR(150) NOT NULL,
    PhanTramGiam DECIMAL(5,2) DEFAULT 0, 
    NgayBatDau DATETIME NOT NULL,
    NgayKetThuc DATETIME NOT NULL,
    TrangThai BIT DEFAULT 1
);

CREATE TABLE HoaDon (
    MaHD VARCHAR(20) PRIMARY KEY, 
    MaNV VARCHAR(20) NOT NULL,
    MaKH VARCHAR(20) NULL, 
    MaKM INT NULL,
    NgayLap DATETIME DEFAULT GETDATE(),
    TongTien DECIMAL(18,2) NOT NULL, 
    TienGiamGia DECIMAL(18,2) DEFAULT 0,
    TienThanhToan DECIMAL(18,2) NOT NULL, 
    PhuongThucThanhToan NVARCHAR(20) NOT NULL, 
    TrangThai NVARCHAR(20) DEFAULT N'Hoàn thành', 
    FOREIGN KEY (MaNV) REFERENCES NhanVien(MaNV),
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH),
    FOREIGN KEY (MaKM) REFERENCES ChuongTrinhKhuyenMai(MaKM)
);

CREATE TABLE ChiTietHoaDon (
    MaHD VARCHAR(20) NOT NULL,
    MaSP VARCHAR(20) NOT NULL,
    SoLuong INT NOT NULL CHECK (SoLuong > 0),
    DonGia DECIMAL(18,2) NOT NULL,
    ThanhTien DECIMAL(18,2) NOT NULL,
    PRIMARY KEY (MaHD, MaSP),
    FOREIGN KEY (MaHD) REFERENCES HoaDon(MaHD),
    FOREIGN KEY (MaSP) REFERENCES SanPham(MaSP)
);

INSERT INTO VaiTro (TenVaiTro, MoTa) VALUES
(N'Quản lý', N'Quản lý toàn bộ siêu thị'),
(N'Thu ngân', N'Nhân viên thanh toán tại quầy'),
(N'Nhân viên kho', N'Quản lý hàng hóa trong kho');

INSERT INTO NhanVien (MaNV, HoTen, CCCD, NgaySinh, GioiTinh, SoDienThoai, Email, DiaChi, ViTri, BoPhan, MaVaiTro, TenDangNhap, MatKhauHash) VALUES
('EMP-0001', N'Nguyễn Tuấn Anh', '001200300400', '1990-05-15', N'Nam', '0901234567', 'tuananh@minisuper.com', N'Hà Nội', N'Cửa hàng trưởng', N'Quản lý', 1, 'emp0001', 'hash_of_supermarket@123'),
('EMP-0002', N'Phạm Thị Hoài Anh', '001200300401', '1998-10-20', N'Nữ', '0912345678', 'hoaianh@minisuper.com', N'Hà Nội', N'Thu ngân', N'Bán hàng', 2, 'emp0002', 'hash_of_supermarket@123'),
('EMP-0003', N'Phạm Mạnh Hùng', '001200300402', '1995-02-28', N'Nam', '0923456789', 'manhhung@minisuper.com', N'Hà Nội', N'Thủ kho', N'Kho', 3, 'emp0003', 'hash_of_supermarket@123');

INSERT INTO CaLamViec (TenCa, GioBatDau, GioKetThuc) VALUES
(N'Ca Sáng', '06:00:00', '14:00:00'),
(N'Ca Chiều', '14:00:00', '22:00:00');

INSERT INTO KhachHang (MaKH, HoTen, SoDienThoai, Email, NgaySinh, GioiTinh, DiaChi, HangThanhVien, DiemTichLuy) VALUES
('MEM-20250001', N'Lê Văn Khách', '0987654321', 'khachle@email.com', '1985-08-12', N'Nam', N'Cầu Giấy, Hà Nội', N'Bạc', 50),
('MEM-20250002', N'Trần Thị Mua', '0976543210', 'muatran@email.com', '1992-11-05', N'Nữ', N'Đống Đa, Hà Nội', N'Vàng', 650);

INSERT INTO DanhMuc (TenDanhMuc, MaDanhMucCha) VALUES
(N'Thực phẩm', NULL),
(N'Đồ uống', NULL),
(N'Hóa mỹ phẩm', NULL);

DECLARE @ThucPhamID INT = (SELECT MaDanhMuc FROM DanhMuc WHERE TenDanhMuc = N'Thực phẩm');
DECLARE @DoUongID INT = (SELECT MaDanhMuc FROM DanhMuc WHERE TenDanhMuc = N'Đồ uống');
DECLARE @HoaMyPhamID INT = (SELECT MaDanhMuc FROM DanhMuc WHERE TenDanhMuc = N'Hóa mỹ phẩm');

INSERT INTO DanhMuc (TenDanhMuc, MaDanhMucCha) VALUES
(N'Mì ăn liền', @ThucPhamID),
(N'Nước ngọt', @DoUongID),
(N'Dầu gội', @HoaMyPhamID);

INSERT INTO NhaCungCap (TenNCC, NguoiLienHe, SoDienThoai, Email, DiaChi) VALUES
(N'Công ty TNHH Nước giải khát Suntory Pepsico', N'Mr. Bình', '19001234', 'contact@pepsico.vn', N'KCN VSIP, Bắc Ninh'),
(N'Công ty TNHH Unilever Việt Nam', N'Ms. Lan', '19005678', 'sales@unilever.vn', N'KCN Tây Bắc Củ Chi, TP.HCM'),
(N'Công ty Cổ phần Acecook Việt Nam', N'Mr. Hải', '19009999', 'info@acecook.vn', N'KCN Tân Bình, TP.HCM');

DECLARE @CatMi INT = (SELECT MaDanhMuc FROM DanhMuc WHERE TenDanhMuc = N'Mì ăn liền');
DECLARE @CatNuoc INT = (SELECT MaDanhMuc FROM DanhMuc WHERE TenDanhMuc = N'Nước ngọt');
DECLARE @CatDau INT = (SELECT MaDanhMuc FROM DanhMuc WHERE TenDanhMuc = N'Dầu gội');

INSERT INTO SanPham (MaSP, MaVach, TenSP, MaDanhMuc, DonGia, DonViTinh, SoLuongTon, TonKhoToiThieu) VALUES
('SP-0001', '8934567890123', N'Mì Hảo Hảo tôm chua cay', @CatMi, 4500, N'Gói', 500, 50),
('SP-0002', '8934567890124', N'Pepsi Cola chai 390ml', @CatNuoc, 10000, N'Chai', 200, 30),
('SP-0003', '8934567890125', N'Dầu gội Clear Men 630g', @CatDau, 165000, N'Chai', 20, 5);

INSERT INTO ChuongTrinhKhuyenMai (TenKM, PhanTramGiam, NgayBatDau, NgayKetThuc) VALUES
(N'Khuyến mãi khai trương', 10.00, '2026-04-01', '2026-04-30');

INSERT INTO PhieuNhapHang (MaPhieuNhap, MaNCC, MaNV, TongTien) VALUES
('PN-20260421-01', 1, 'EMP-0003', 1500000),
('PN-20260421-02', 3, 'EMP-0003', 1500000);

INSERT INTO ChiTietPhieuNhap (MaPhieuNhap, MaSP, SoLuong, GiaNhap, SoLo, HanSuDung) VALUES
('PN-20260421-01', 'SP-0002', 200, 7500, 'B001', '2027-04-20'),
('PN-20260421-02', 'SP-0001', 500, 3000, 'B002', '2026-10-20');

INSERT INTO HoaDon (MaHD, MaNV, MaKH, TongTien, TienGiamGia, TienThanhToan, PhuongThucThanhToan) VALUES
('HD-20260421-001', 'EMP-0002', 'MEM-20250001', 54000, 0, 54000, N'Tiền mặt'),
('HD-20260421-002', 'EMP-0002', NULL, 10000, 0, 10000, N'Thẻ');

INSERT INTO ChiTietHoaDon (MaHD, MaSP, SoLuong, DonGia, ThanhTien) VALUES
('HD-20260421-001', 'SP-0001', 3, 4500, 13500), 
('HD-20260421-001', 'SP-0002', 4, 10000, 40000),
('HD-20260421-002', 'SP-0002', 1, 10000, 10000);
GO

UPDATE SanPham SET SoLuongTon = SoLuongTon - 3 WHERE MaSP = 'SP-0001';
UPDATE SanPham SET SoLuongTon = SoLuongTon - 5 WHERE MaSP = 'SP-0002';