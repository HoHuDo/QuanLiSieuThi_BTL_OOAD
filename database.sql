USE [QuanLySieuThiDB]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [CK__SanPham__TonKhoT__60A75C0F]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [CK__SanPham__SoLuong__5EBF139D]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [CK__SanPham__DonGia__5CD6CB2B]
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap] DROP CONSTRAINT [CK__ChiTietPh__SoLuo__6B24EA82]
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap] DROP CONSTRAINT [CK__ChiTietPh__GiaNh__6C190EBB]
GO
ALTER TABLE [dbo].[ChiTietHoaDon] DROP CONSTRAINT [CK__ChiTietHo__SoLuo__7C4F7684]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [FK__SanPham__MaDanhM__628FA481]
GO
ALTER TABLE [dbo].[PhieuNhapHang] DROP CONSTRAINT [FK__PhieuNhapH__MaNV__68487DD7]
GO
ALTER TABLE [dbo].[PhieuNhapHang] DROP CONSTRAINT [FK__PhieuNhap__MaNCC__6754599E]
GO
ALTER TABLE [dbo].[PhieuGiamGia] DROP CONSTRAINT [FK__PhieuGiamG__MaKH__52593CB8]
GO
ALTER TABLE [dbo].[PhanCaNhanVien] DROP CONSTRAINT [FK__PhanCaNhan__MaNV__44FF419A]
GO
ALTER TABLE [dbo].[PhanCaNhanVien] DROP CONSTRAINT [FK__PhanCaNhan__MaCa__45F365D3]
GO
ALTER TABLE [dbo].[NhanVien] DROP CONSTRAINT [FK__NhanVien__MaVaiT__3F466844]
GO
ALTER TABLE [dbo].[HoaDon] DROP CONSTRAINT [FK__HoaDon__MaNV__778AC167]
GO
ALTER TABLE [dbo].[HoaDon] DROP CONSTRAINT [FK__HoaDon__MaKM__797309D9]
GO
ALTER TABLE [dbo].[HoaDon] DROP CONSTRAINT [FK__HoaDon__MaKH__787EE5A0]
GO
ALTER TABLE [dbo].[DanhMuc] DROP CONSTRAINT [FK__DanhMuc__MaDanhM__5629CD9C]
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap] DROP CONSTRAINT [FK__ChiTietPhi__MaSP__6E01572D]
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap] DROP CONSTRAINT [FK__ChiTietPh__MaPhi__6D0D32F4]
GO
ALTER TABLE [dbo].[ChiTietHoaDon] DROP CONSTRAINT [FK__ChiTietHoa__MaSP__7E37BEF6]
GO
ALTER TABLE [dbo].[ChiTietHoaDon] DROP CONSTRAINT [FK__ChiTietHoa__MaHD__7D439ABD]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [DF__SanPham__TrangTh__619B8048]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [DF__SanPham__TonKhoT__5FB337D6]
GO
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [DF__SanPham__SoLuong__5DCAEF64]
GO
ALTER TABLE [dbo].[PhieuNhapHang] DROP CONSTRAINT [DF__PhieuNhap__TongT__66603565]
GO
ALTER TABLE [dbo].[PhieuNhapHang] DROP CONSTRAINT [DF__PhieuNhap__NgayN__656C112C]
GO
ALTER TABLE [dbo].[PhieuGiamGia] DROP CONSTRAINT [DF__PhieuGiam__DaSuD__5165187F]
GO
ALTER TABLE [dbo].[PhieuGiamGia] DROP CONSTRAINT [DF__PhieuGiam__NgayP__5070F446]
GO
ALTER TABLE [dbo].[NhanVien] DROP CONSTRAINT [DF__NhanVien__TrangT__3E52440B]
GO
ALTER TABLE [dbo].[NhanVien] DROP CONSTRAINT [DF__NhanVien__NgayVa__3D5E1FD2]
GO
ALTER TABLE [dbo].[NhaCungCap] DROP CONSTRAINT [DF__NhaCungCa__Trang__59063A47]
GO
ALTER TABLE [dbo].[KhachHang] DROP CONSTRAINT [DF__KhachHang__NgayT__4CA06362]
GO
ALTER TABLE [dbo].[KhachHang] DROP CONSTRAINT [DF__KhachHang__Trang__4BAC3F29]
GO
ALTER TABLE [dbo].[KhachHang] DROP CONSTRAINT [DF__KhachHang__DiemT__4AB81AF0]
GO
ALTER TABLE [dbo].[KhachHang] DROP CONSTRAINT [DF__KhachHang__HangT__49C3F6B7]
GO
ALTER TABLE [dbo].[HoaDon] DROP CONSTRAINT [DF__HoaDon__TrangTha__76969D2E]
GO
ALTER TABLE [dbo].[HoaDon] DROP CONSTRAINT [DF__HoaDon__TienGiam__75A278F5]
GO
ALTER TABLE [dbo].[HoaDon] DROP CONSTRAINT [DF__HoaDon__NgayLap__74AE54BC]
GO
ALTER TABLE [dbo].[DanhMuc] DROP CONSTRAINT [DF__DanhMuc__TrangTh__5535A963]
GO
ALTER TABLE [dbo].[ChuongTrinhKhuyenMai] DROP CONSTRAINT [DF__ChuongTri__Trang__71D1E811]
GO
ALTER TABLE [dbo].[ChuongTrinhKhuyenMai] DROP CONSTRAINT [DF__ChuongTri__PhanT__70DDC3D8]
GO
/****** Object:  Index [UQ__VaiTro__1DA5581441E3D623]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[VaiTro] DROP CONSTRAINT [UQ__VaiTro__1DA5581441E3D623]
GO
/****** Object:  Index [UQ__SanPham__8BBF4A1C2311385F]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[SanPham] DROP CONSTRAINT [UQ__SanPham__8BBF4A1C2311385F]
GO
/****** Object:  Index [UQ__PhieuGia__152C7C5CDD8DF6E0]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[PhieuGiamGia] DROP CONSTRAINT [UQ__PhieuGia__152C7C5CDD8DF6E0]
GO
/****** Object:  Index [UQ_NhanVien_Ca_Ngay]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[PhanCaNhanVien] DROP CONSTRAINT [UQ_NhanVien_Ca_Ngay]
GO
/****** Object:  Index [UQ__NhanVien__A955A0AA7DA31E4C]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[NhanVien] DROP CONSTRAINT [UQ__NhanVien__A955A0AA7DA31E4C]
GO
/****** Object:  Index [UQ__NhanVien__55F68FC07B3A873C]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[NhanVien] DROP CONSTRAINT [UQ__NhanVien__55F68FC07B3A873C]
GO
/****** Object:  Index [UQ__NhanVien__0389B7BD3EF289F3]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[NhanVien] DROP CONSTRAINT [UQ__NhanVien__0389B7BD3EF289F3]
GO
/****** Object:  Index [UQ__KhachHan__0389B7BD95B1A071]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[KhachHang] DROP CONSTRAINT [UQ__KhachHan__0389B7BD95B1A071]
GO
/****** Object:  Table [dbo].[VaiTro]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[VaiTro]') AND type in (N'U'))
DROP TABLE [dbo].[VaiTro]
GO
/****** Object:  Table [dbo].[SanPham]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[SanPham]') AND type in (N'U'))
DROP TABLE [dbo].[SanPham]
GO
/****** Object:  Table [dbo].[PhieuNhapHang]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[PhieuNhapHang]') AND type in (N'U'))
DROP TABLE [dbo].[PhieuNhapHang]
GO
/****** Object:  Table [dbo].[PhieuGiamGia]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[PhieuGiamGia]') AND type in (N'U'))
DROP TABLE [dbo].[PhieuGiamGia]
GO
/****** Object:  Table [dbo].[PhanCaNhanVien]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[PhanCaNhanVien]') AND type in (N'U'))
DROP TABLE [dbo].[PhanCaNhanVien]
GO
/****** Object:  Table [dbo].[NhanVien]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[NhanVien]') AND type in (N'U'))
DROP TABLE [dbo].[NhanVien]
GO
/****** Object:  Table [dbo].[NhaCungCap]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[NhaCungCap]') AND type in (N'U'))
DROP TABLE [dbo].[NhaCungCap]
GO
/****** Object:  Table [dbo].[KhachHang]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[KhachHang]') AND type in (N'U'))
DROP TABLE [dbo].[KhachHang]
GO
/****** Object:  Table [dbo].[HoaDon]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[HoaDon]') AND type in (N'U'))
DROP TABLE [dbo].[HoaDon]
GO
/****** Object:  Table [dbo].[DanhMuc]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DanhMuc]') AND type in (N'U'))
DROP TABLE [dbo].[DanhMuc]
GO
/****** Object:  Table [dbo].[ChuongTrinhKhuyenMai]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ChuongTrinhKhuyenMai]') AND type in (N'U'))
DROP TABLE [dbo].[ChuongTrinhKhuyenMai]
GO
/****** Object:  Table [dbo].[ChiTietPhieuNhap]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ChiTietPhieuNhap]') AND type in (N'U'))
DROP TABLE [dbo].[ChiTietPhieuNhap]
GO
/****** Object:  Table [dbo].[ChiTietHoaDon]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[ChiTietHoaDon]') AND type in (N'U'))
DROP TABLE [dbo].[ChiTietHoaDon]
GO
/****** Object:  Table [dbo].[CaLamViec]    Script Date: 4/21/2026 12:34:42 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[CaLamViec]') AND type in (N'U'))
DROP TABLE [dbo].[CaLamViec]
GO
/****** Object:  Table [dbo].[CaLamViec]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CaLamViec](
	[MaCa] [int] IDENTITY(1,1) NOT NULL,
	[TenCa] [nvarchar](50) NOT NULL,
	[GioBatDau] [time](7) NOT NULL,
	[GioKetThuc] [time](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[MaCa] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ChiTietHoaDon]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChiTietHoaDon](
	[MaHD] [varchar](20) NOT NULL,
	[MaSP] [varchar](20) NOT NULL,
	[SoLuong] [int] NOT NULL,
	[DonGia] [decimal](18, 2) NOT NULL,
	[ThanhTien] [decimal](18, 2) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[MaHD] ASC,
	[MaSP] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ChiTietPhieuNhap]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChiTietPhieuNhap](
	[MaPhieuNhap] [varchar](20) NOT NULL,
	[MaSP] [varchar](20) NOT NULL,
	[SoLuong] [int] NOT NULL,
	[GiaNhap] [decimal](18, 2) NOT NULL,
	[SoLo] [varchar](50) NULL,
	[HanSuDung] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaPhieuNhap] ASC,
	[MaSP] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ChuongTrinhKhuyenMai]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChuongTrinhKhuyenMai](
	[MaKM] [int] IDENTITY(1,1) NOT NULL,
	[TenKM] [nvarchar](150) NOT NULL,
	[PhanTramGiam] [decimal](5, 2) NULL,
	[NgayBatDau] [datetime] NOT NULL,
	[NgayKetThuc] [datetime] NOT NULL,
	[TrangThai] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaKM] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DanhMuc]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DanhMuc](
	[MaDanhMuc] [int] IDENTITY(1,1) NOT NULL,
	[TenDanhMuc] [nvarchar](100) NOT NULL,
	[MaDanhMucCha] [int] NULL,
	[TrangThai] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaDanhMuc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[HoaDon]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HoaDon](
	[MaHD] [varchar](20) NOT NULL,
	[MaNV] [varchar](20) NOT NULL,
	[MaKH] [varchar](20) NULL,
	[MaKM] [int] NULL,
	[NgayLap] [datetime] NULL,
	[TongTien] [decimal](18, 2) NOT NULL,
	[TienGiamGia] [decimal](18, 2) NULL,
	[TienThanhToan] [decimal](18, 2) NOT NULL,
	[PhuongThucThanhToan] [nvarchar](20) NOT NULL,
	[TrangThai] [nvarchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[MaHD] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KhachHang]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KhachHang](
	[MaKH] [varchar](20) NOT NULL,
	[HoTen] [nvarchar](100) NOT NULL,
	[SoDienThoai] [varchar](15) NOT NULL,
	[Email] [varchar](100) NULL,
	[NgaySinh] [date] NULL,
	[GioiTinh] [nvarchar](10) NULL,
	[DiaChi] [nvarchar](255) NULL,
	[HangThanhVien] [nvarchar](20) NULL,
	[DiemTichLuy] [int] NULL,
	[TrangThai] [bit] NULL,
	[NgayTao] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaKH] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NhaCungCap]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NhaCungCap](
	[MaNCC] [int] IDENTITY(1,1) NOT NULL,
	[TenNCC] [nvarchar](150) NOT NULL,
	[NguoiLienHe] [nvarchar](100) NULL,
	[SoDienThoai] [varchar](15) NOT NULL,
	[Email] [varchar](100) NULL,
	[DiaChi] [nvarchar](255) NULL,
	[TrangThai] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaNCC] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NhanVien]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NhanVien](
	[MaNV] [varchar](20) NOT NULL,
	[HoTen] [nvarchar](100) NOT NULL,
	[CCCD] [varchar](12) NOT NULL,
	[NgaySinh] [date] NULL,
	[GioiTinh] [nvarchar](10) NULL,
	[SoDienThoai] [varchar](15) NOT NULL,
	[Email] [varchar](100) NULL,
	[DiaChi] [nvarchar](255) NULL,
	[ViTri] [nvarchar](50) NOT NULL,
	[BoPhan] [nvarchar](50) NOT NULL,
	[NgayVaoLam] [date] NULL,
	[MaVaiTro] [int] NOT NULL,
	[TenDangNhap] [varchar](50) NOT NULL,
	[MatKhauHash] [varchar](255) NOT NULL,
	[TrangThai] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaNV] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhanCaNhanVien]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhanCaNhanVien](
	[MaPhanCa] [int] IDENTITY(1,1) NOT NULL,
	[MaNV] [varchar](20) NOT NULL,
	[MaCa] [int] NOT NULL,
	[NgayLamViec] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[MaPhanCa] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhieuGiamGia]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhieuGiamGia](
	[MaPhieu] [varchar](20) NOT NULL,
	[MaKH] [varchar](20) NOT NULL,
	[MaCode] [varchar](50) NOT NULL,
	[GiaTriGiam] [decimal](18, 2) NOT NULL,
	[NgayPhatHanh] [datetime] NULL,
	[HanSuDung] [datetime] NOT NULL,
	[DaSuDung] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaPhieu] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhieuNhapHang]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhieuNhapHang](
	[MaPhieuNhap] [varchar](20) NOT NULL,
	[MaNCC] [int] NOT NULL,
	[MaNV] [varchar](20) NOT NULL,
	[NgayNhap] [datetime] NULL,
	[TongTien] [decimal](18, 2) NULL,
	[GhiChu] [nvarchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[MaPhieuNhap] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SanPham]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SanPham](
	[MaSP] [varchar](20) NOT NULL,
	[MaVach] [varchar](50) NOT NULL,
	[TenSP] [nvarchar](150) NOT NULL,
	[MoTa] [nvarchar](500) NULL,
	[MaDanhMuc] [int] NOT NULL,
	[DonGia] [decimal](18, 2) NOT NULL,
	[DonViTinh] [nvarchar](20) NOT NULL,
	[HinhAnh] [varchar](255) NULL,
	[SoLuongTon] [int] NULL,
	[TonKhoToiThieu] [int] NULL,
	[TrangThai] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[MaSP] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[VaiTro]    Script Date: 4/21/2026 12:34:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[VaiTro](
	[MaVaiTro] [int] IDENTITY(1,1) NOT NULL,
	[TenVaiTro] [nvarchar](50) NOT NULL,
	[MoTa] [nvarchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[MaVaiTro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[CaLamViec] ON 

INSERT [dbo].[CaLamViec] ([MaCa], [TenCa], [GioBatDau], [GioKetThuc]) VALUES (1, N'Ca Sáng', CAST(N'06:00:00' AS Time), CAST(N'14:00:00' AS Time))
INSERT [dbo].[CaLamViec] ([MaCa], [TenCa], [GioBatDau], [GioKetThuc]) VALUES (2, N'Ca Chiều', CAST(N'14:00:00' AS Time), CAST(N'22:00:00' AS Time))
SET IDENTITY_INSERT [dbo].[CaLamViec] OFF
GO
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-001', N'SP-0001', 3, CAST(4500.00 AS Decimal(18, 2)), CAST(13500.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-001', N'SP-0002', 4, CAST(10000.00 AS Decimal(18, 2)), CAST(40000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-002', N'SP-0009', 3, CAST(5000.00 AS Decimal(18, 2)), CAST(15000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-003', N'SP-0004', 3, CAST(8000.00 AS Decimal(18, 2)), CAST(24000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-003', N'SP-0005', 10, CAST(12000.00 AS Decimal(18, 2)), CAST(120000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-003', N'SP-0006', 1, CAST(145000.00 AS Decimal(18, 2)), CAST(145000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-003', N'SP-0007', 1, CAST(45000.00 AS Decimal(18, 2)), CAST(45000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-003', N'SP-0010', 1, CAST(42000.00 AS Decimal(18, 2)), CAST(42000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-004', N'SP-0008', 10, CAST(8500.00 AS Decimal(18, 2)), CAST(85000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-005', N'SP-0006', 1, CAST(145000.00 AS Decimal(18, 2)), CAST(145000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-094339', N'SP-0001', 1, CAST(4500.00 AS Decimal(18, 2)), CAST(4500.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-094339', N'SP-0002', 1, CAST(10000.00 AS Decimal(18, 2)), CAST(10000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-094411', N'SP-0002', 1, CAST(10000.00 AS Decimal(18, 2)), CAST(10000.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-100519', N'SP-0001', 5, CAST(4500.00 AS Decimal(18, 2)), CAST(22500.00 AS Decimal(18, 2)))
INSERT [dbo].[ChiTietHoaDon] ([MaHD], [MaSP], [SoLuong], [DonGia], [ThanhTien]) VALUES (N'HD-20260421-121211', N'SP-0001', 1, CAST(4500.00 AS Decimal(18, 2)), CAST(4500.00 AS Decimal(18, 2)))
GO
INSERT [dbo].[ChiTietPhieuNhap] ([MaPhieuNhap], [MaSP], [SoLuong], [GiaNhap], [SoLo], [HanSuDung]) VALUES (N'PN-20260421-01', N'SP-0002', 200, CAST(7500.00 AS Decimal(18, 2)), N'B001', CAST(N'2027-04-20' AS Date))
INSERT [dbo].[ChiTietPhieuNhap] ([MaPhieuNhap], [MaSP], [SoLuong], [GiaNhap], [SoLo], [HanSuDung]) VALUES (N'PN-20260421-01', N'SP-0009', 500, CAST(2000.00 AS Decimal(18, 2)), N'B001', CAST(N'2028-04-20' AS Date))
INSERT [dbo].[ChiTietPhieuNhap] ([MaPhieuNhap], [MaSP], [SoLuong], [GiaNhap], [SoLo], [HanSuDung]) VALUES (N'PN-20260421-02', N'SP-0001', 500, CAST(3000.00 AS Decimal(18, 2)), N'B002', CAST(N'2026-10-20' AS Date))
INSERT [dbo].[ChiTietPhieuNhap] ([MaPhieuNhap], [MaSP], [SoLuong], [GiaNhap], [SoLo], [HanSuDung]) VALUES (N'PN-20260421-03', N'SP-0004', 300, CAST(8000.00 AS Decimal(18, 2)), N'B003', CAST(N'2026-10-21' AS Date))
INSERT [dbo].[ChiTietPhieuNhap] ([MaPhieuNhap], [MaSP], [SoLuong], [GiaNhap], [SoLo], [HanSuDung]) VALUES (N'PN-20260421-04', N'SP-0005', 480, CAST(12000.00 AS Decimal(18, 2)), N'B004', CAST(N'2027-04-21' AS Date))
GO
SET IDENTITY_INSERT [dbo].[ChuongTrinhKhuyenMai] ON 

INSERT [dbo].[ChuongTrinhKhuyenMai] ([MaKM], [TenKM], [PhanTramGiam], [NgayBatDau], [NgayKetThuc], [TrangThai]) VALUES (1, N'Khuyến mãi khai trương', CAST(10.00 AS Decimal(5, 2)), CAST(N'2026-04-01T00:00:00.000' AS DateTime), CAST(N'2026-04-30T00:00:00.000' AS DateTime), 0)
INSERT [dbo].[ChuongTrinhKhuyenMai] ([MaKM], [TenKM], [PhanTramGiam], [NgayBatDau], [NgayKetThuc], [TrangThai]) VALUES (2, N'Lễ 30/4 - 1/5', CAST(5.00 AS Decimal(5, 2)), CAST(N'2026-04-28T00:00:00.000' AS DateTime), CAST(N'2026-05-02T00:00:00.000' AS DateTime), 1)
SET IDENTITY_INSERT [dbo].[ChuongTrinhKhuyenMai] OFF
GO
SET IDENTITY_INSERT [dbo].[DanhMuc] ON 

INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (1, N'Thực phẩm', NULL, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (2, N'Đồ uống', NULL, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (3, N'Hóa mỹ phẩm', NULL, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (4, N'Đồ gia dụng', NULL, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (5, N'Mì ăn liền', 1, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (6, N'Sữa và các sản phẩm từ sữa', 1, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (7, N'Bánh kẹo', 1, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (8, N'Nước ngọt', 2, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (9, N'Nước suối', 2, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (10, N'Bia', 2, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (11, N'Dầu gội', 3, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (12, N'Bột giặt', 3, 1)
INSERT [dbo].[DanhMuc] ([MaDanhMuc], [TenDanhMuc], [MaDanhMucCha], [TrangThai]) VALUES (13, N'Nước rửa chén', 3, 1)
SET IDENTITY_INSERT [dbo].[DanhMuc] OFF
GO
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-001', N'EMP-0002', N'MEM-20250001', NULL, CAST(N'2026-04-21T09:10:14.460' AS DateTime), CAST(54000.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(54000.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-002', N'EMP-0002', NULL, NULL, CAST(N'2026-04-21T09:10:14.460' AS DateTime), CAST(15000.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(15000.00 AS Decimal(18, 2)), N'Thẻ', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-003', N'EMP-0004', N'MEM-20250003', NULL, CAST(N'2026-04-21T09:10:14.460' AS DateTime), CAST(380000.00 AS Decimal(18, 2)), CAST(38000.00 AS Decimal(18, 2)), CAST(342000.00 AS Decimal(18, 2)), N'Thẻ', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-004', N'EMP-0004', N'MEM-20250005', NULL, CAST(N'2026-04-21T09:10:14.460' AS DateTime), CAST(85000.00 AS Decimal(18, 2)), CAST(8500.00 AS Decimal(18, 2)), CAST(76500.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-005', N'EMP-0002', NULL, NULL, CAST(N'2026-04-21T09:10:14.460' AS DateTime), CAST(145000.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(145000.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-094339', N'EMP-0001', NULL, NULL, CAST(N'2026-04-21T09:43:39.983' AS DateTime), CAST(14500.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(14500.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-094411', N'EMP-0001', NULL, NULL, CAST(N'2026-04-21T09:44:11.580' AS DateTime), CAST(10000.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(10000.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-100519', N'EMP-0001', NULL, NULL, CAST(N'2026-04-21T10:05:19.287' AS DateTime), CAST(22500.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(22500.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
INSERT [dbo].[HoaDon] ([MaHD], [MaNV], [MaKH], [MaKM], [NgayLap], [TongTien], [TienGiamGia], [TienThanhToan], [PhuongThucThanhToan], [TrangThai]) VALUES (N'HD-20260421-121211', N'EMP-0001', NULL, NULL, CAST(N'2026-04-21T12:12:11.173' AS DateTime), CAST(4500.00 AS Decimal(18, 2)), CAST(0.00 AS Decimal(18, 2)), CAST(4500.00 AS Decimal(18, 2)), N'Tiền mặt', N'Hoàn thành')
GO
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20250001', N'Lê Văn Khách', N'0987654321', N'khachle@email.com', CAST(N'1985-08-12' AS Date), N'Nam', N'Cầu Giấy, Hà Nội', N'Bạc', 50, 1, CAST(N'2026-04-21T09:10:14.430' AS DateTime))
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20250002', N'Trần Thị Mua', N'0976543210', N'muatran@email.com', CAST(N'1992-11-05' AS Date), N'Khác', N'Đống Đa, Hà Nội', N'Vàng', 650, 1, CAST(N'2026-04-21T09:10:14.430' AS DateTime))
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20250003', N'Nguyễn Hải Yến', N'0911223344', N'yen.nguyen@email.com', CAST(N'1999-03-22' AS Date), N'Nữ', N'Thanh Xuân, Hà Nội', N'Kim Cương', 2100, 1, CAST(N'2026-04-21T09:10:14.430' AS DateTime))
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20250004', N'Đinh Tùng Lâm', N'0922334455', N'lam.dinh@email.com', CAST(N'1988-07-15' AS Date), N'Nam', N'Ba Đình, Hà Nội', N'Bạc', 120, 1, CAST(N'2026-04-21T09:10:14.430' AS DateTime))
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20250005', N'Hoàng Thu Thủy', N'0933445566', N'thuy.hoang@email.com', CAST(N'2001-12-01' AS Date), N'Nữ', N'Hoàn Kiếm, Hà Nội', N'Vàng', 1050, 1, CAST(N'2026-04-21T09:10:14.430' AS DateTime))
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20250006', N'Bùi Quang Sáng', N'0944556677', N'sang.bui@email.com', CAST(N'1975-04-30' AS Date), N'Nam', N'Hai Bà Trưng, Hà Nội', N'Bạc', 15, 1, CAST(N'2026-04-21T09:10:14.430' AS DateTime))
INSERT [dbo].[KhachHang] ([MaKH], [HoTen], [SoDienThoai], [Email], [NgaySinh], [GioiTinh], [DiaChi], [HangThanhVien], [DiemTichLuy], [TrangThai], [NgayTao]) VALUES (N'MEM-20260421-6879', N'Trịnh Quốc Hải', N'0399303513', N'trinhquochainb@gmail.com', CAST(N'2005-08-02' AS Date), N'Nam', N'Ninh Bình', N'Bạc', 0, 1, CAST(N'2026-04-21T10:42:27.063' AS DateTime))
GO
SET IDENTITY_INSERT [dbo].[NhaCungCap] ON 

INSERT [dbo].[NhaCungCap] ([MaNCC], [TenNCC], [NguoiLienHe], [SoDienThoai], [Email], [DiaChi], [TrangThai]) VALUES (1, N'Công ty TNHH Nước giải khát Suntory Pepsico', N'Mr. Bình', N'19001234', N'contact@pepsico.vn', N'KCN VSIP, Bắc Ninh', 1)
INSERT [dbo].[NhaCungCap] ([MaNCC], [TenNCC], [NguoiLienHe], [SoDienThoai], [Email], [DiaChi], [TrangThai]) VALUES (2, N'Công ty TNHH Unilever Việt Nam', N'Ms. Lan', N'19005678', N'sales@unilever.vn', N'KCN Tây Bắc Củ Chi, TP.HCM', 1)
INSERT [dbo].[NhaCungCap] ([MaNCC], [TenNCC], [NguoiLienHe], [SoDienThoai], [Email], [DiaChi], [TrangThai]) VALUES (3, N'Công ty Cổ phần Acecook Việt Nam', N'Mr. Hải', N'19009999', N'info@acecook.vn', N'KCN Tân Bình, TP.HCM', 1)
INSERT [dbo].[NhaCungCap] ([MaNCC], [TenNCC], [NguoiLienHe], [SoDienThoai], [Email], [DiaChi], [TrangThai]) VALUES (4, N'Công ty Cổ phần Sữa Việt Nam (Vinamilk)', N'Ms. Hoa', N'19001111', N'cskh@vinamilk.com.vn', N'Quận 7, TP.HCM', 1)
INSERT [dbo].[NhaCungCap] ([MaNCC], [TenNCC], [NguoiLienHe], [SoDienThoai], [Email], [DiaChi], [TrangThai]) VALUES (5, N'Tổng Công ty Cổ phần Bia - Rượu - Nước giải khát Hà Nội', N'Mr. Tuấn', N'19002222', N'info@habeco.com.vn', N'Ba Đình, Hà Nội', 1)
SET IDENTITY_INSERT [dbo].[NhaCungCap] OFF
GO
INSERT [dbo].[NhanVien] ([MaNV], [HoTen], [CCCD], [NgaySinh], [GioiTinh], [SoDienThoai], [Email], [DiaChi], [ViTri], [BoPhan], [NgayVaoLam], [MaVaiTro], [TenDangNhap], [MatKhauHash], [TrangThai]) VALUES (N'EMP-0001', N'Nguyễn Quốc Kỳ', N'001200300401', CAST(N'1990-01-01' AS Date), N'Nam', N'0901112223', N'ky.nguyen@minisuper.com', N'Hà Nội', N'Cửa hàng trưởng', N'Quản lý', CAST(N'2026-04-21' AS Date), 1, N'kyquoc', N'68a71ad31ca20d3bf8582c71ba04f4828f68a7d7eb2592a1a142baae3f594a98', 1)
INSERT [dbo].[NhanVien] ([MaNV], [HoTen], [CCCD], [NgaySinh], [GioiTinh], [SoDienThoai], [Email], [DiaChi], [ViTri], [BoPhan], [NgayVaoLam], [MaVaiTro], [TenDangNhap], [MatKhauHash], [TrangThai]) VALUES (N'EMP-0002', N'Đỗ Hữu Hoài', N'001200300402', CAST(N'2005-01-01' AS Date), N'Nam', N'0904445556', N'hoai.do@minisuper.com', N'Hà Nội', N'Thu ngân', N'Bán hàng', CAST(N'2026-04-21' AS Date), 2, N'hoaihuu', N'68a71ad31ca20d3bf8582c71ba04f4828f68a7d7eb2592a1a142baae3f594a98', 1)
INSERT [dbo].[NhanVien] ([MaNV], [HoTen], [CCCD], [NgaySinh], [GioiTinh], [SoDienThoai], [Email], [DiaChi], [ViTri], [BoPhan], [NgayVaoLam], [MaVaiTro], [TenDangNhap], [MatKhauHash], [TrangThai]) VALUES (N'EMP-0003', N'Phạm Ngọc Phúc', N'001200300403', CAST(N'1995-05-05' AS Date), N'Nam', N'0907778889', N'phuc.pham@minisuper.com', N'Hà Nội', N'Thủ kho', N'Kho', CAST(N'2026-04-21' AS Date), 3, N'phucngoc', N'68a71ad31ca20d3bf8582c71ba04f4828f68a7d7eb2592a1a142baae3f594a98', 1)
INSERT [dbo].[NhanVien] ([MaNV], [HoTen], [CCCD], [NgaySinh], [GioiTinh], [SoDienThoai], [Email], [DiaChi], [ViTri], [BoPhan], [NgayVaoLam], [MaVaiTro], [TenDangNhap], [MatKhauHash], [TrangThai]) VALUES (N'EMP-0004', N'Vũ Khánh Minh', N'001200300404', CAST(N'1998-08-08' AS Date), N'Nam', N'0909990001', N'minh.vu@minisuper.com', N'Hà Nội', N'Thu ngân', N'Bán hàng', CAST(N'2026-04-21' AS Date), 2, N'minhkhanh', N'68a71ad31ca20d3bf8582c71ba04f4828f68a7d7eb2592a1a142baae3f594a98', 1)
GO
SET IDENTITY_INSERT [dbo].[PhanCaNhanVien] ON 

INSERT [dbo].[PhanCaNhanVien] ([MaPhanCa], [MaNV], [MaCa], [NgayLamViec]) VALUES (1, N'EMP-0001', 1, CAST(N'2026-04-21' AS Date))
INSERT [dbo].[PhanCaNhanVien] ([MaPhanCa], [MaNV], [MaCa], [NgayLamViec]) VALUES (2, N'EMP-0002', 1, CAST(N'2026-04-21' AS Date))
INSERT [dbo].[PhanCaNhanVien] ([MaPhanCa], [MaNV], [MaCa], [NgayLamViec]) VALUES (3, N'EMP-0003', 1, CAST(N'2026-04-21' AS Date))
INSERT [dbo].[PhanCaNhanVien] ([MaPhanCa], [MaNV], [MaCa], [NgayLamViec]) VALUES (4, N'EMP-0004', 2, CAST(N'2026-04-21' AS Date))
SET IDENTITY_INSERT [dbo].[PhanCaNhanVien] OFF
GO
INSERT [dbo].[PhieuNhapHang] ([MaPhieuNhap], [MaNCC], [MaNV], [NgayNhap], [TongTien], [GhiChu]) VALUES (N'PN-20260421-01', 1, N'EMP-0003', CAST(N'2026-04-21T09:10:14.450' AS DateTime), CAST(2500000.00 AS Decimal(18, 2)), NULL)
INSERT [dbo].[PhieuNhapHang] ([MaPhieuNhap], [MaNCC], [MaNV], [NgayNhap], [TongTien], [GhiChu]) VALUES (N'PN-20260421-02', 3, N'EMP-0003', CAST(N'2026-04-21T09:10:14.450' AS DateTime), CAST(1500000.00 AS Decimal(18, 2)), NULL)
INSERT [dbo].[PhieuNhapHang] ([MaPhieuNhap], [MaNCC], [MaNV], [NgayNhap], [TongTien], [GhiChu]) VALUES (N'PN-20260421-03', 4, N'EMP-0003', CAST(N'2026-04-21T09:10:14.450' AS DateTime), CAST(2400000.00 AS Decimal(18, 2)), NULL)
INSERT [dbo].[PhieuNhapHang] ([MaPhieuNhap], [MaNCC], [MaNV], [NgayNhap], [TongTien], [GhiChu]) VALUES (N'PN-20260421-04', 5, N'EMP-0003', CAST(N'2026-04-21T09:10:14.450' AS DateTime), CAST(5760000.00 AS Decimal(18, 2)), NULL)
GO
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0001', N'8934567890123', N'Mì Hảo Hảo tôm chua cay', NULL, 5, CAST(4500.00 AS Decimal(18, 2)), N'Gói', NULL, 490, 50, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0002', N'8934567890124', N'Pepsi Cola chai 390ml', NULL, 8, CAST(10000.00 AS Decimal(18, 2)), N'Chai', NULL, 194, 30, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0003', N'8934567890125', N'Dầu gội Clear Men 630g', NULL, 11, CAST(165000.00 AS Decimal(18, 2)), N'Chai', NULL, 20, 5, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0004', N'8934567890126', N'Sữa tươi tiệt trùng Vinamilk 180ml', NULL, 6, CAST(8000.00 AS Decimal(18, 2)), N'Hộp', NULL, 55, 50, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0005', N'8934567890127', N'Bia Hà Nội lon 330ml', NULL, 10, CAST(12000.00 AS Decimal(18, 2)), N'Lon', NULL, 470, 72, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0006', N'8934567890128', N'Bột giặt OMO hệ chuyên gia 3kg', NULL, 12, CAST(145000.00 AS Decimal(18, 2)), N'Túi', NULL, 43, 10, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0007', N'8934567890129', N'Nước rửa chén Sunlight chanh 1.5kg', NULL, 13, CAST(45000.00 AS Decimal(18, 2)), N'Chai', NULL, 79, 15, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0008', N'8934567890130', N'Mì Omachi sườn hầm ngũ quả', NULL, 5, CAST(8500.00 AS Decimal(18, 2)), N'Gói', NULL, 240, 30, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0009', N'8934567890131', N'Nước suối Aquafina 500ml', NULL, 9, CAST(5000.00 AS Decimal(18, 2)), N'Chai', NULL, 497, 100, 1)
INSERT [dbo].[SanPham] ([MaSP], [MaVach], [TenSP], [MoTa], [MaDanhMuc], [DonGia], [DonViTinh], [HinhAnh], [SoLuongTon], [TonKhoToiThieu], [TrangThai]) VALUES (N'SP-0010', N'8934567890132', N'Bánh quy Cosy 400g', NULL, 7, CAST(42000.00 AS Decimal(18, 2)), N'Hộp', NULL, 59, 20, 1)
GO
SET IDENTITY_INSERT [dbo].[VaiTro] ON 

INSERT [dbo].[VaiTro] ([MaVaiTro], [TenVaiTro], [MoTa]) VALUES (1, N'Quản lý', N'')
INSERT [dbo].[VaiTro] ([MaVaiTro], [TenVaiTro], [MoTa]) VALUES (2, N'Thu ngân', N'')
INSERT [dbo].[VaiTro] ([MaVaiTro], [TenVaiTro], [MoTa]) VALUES (3, N'Nhân viên kho', N'')
SET IDENTITY_INSERT [dbo].[VaiTro] OFF
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__KhachHan__0389B7BD95B1A071]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[KhachHang] ADD UNIQUE NONCLUSTERED 
(
	[SoDienThoai] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__NhanVien__0389B7BD3EF289F3]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[NhanVien] ADD UNIQUE NONCLUSTERED 
(
	[SoDienThoai] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__NhanVien__55F68FC07B3A873C]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[NhanVien] ADD UNIQUE NONCLUSTERED 
(
	[TenDangNhap] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__NhanVien__A955A0AA7DA31E4C]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[NhanVien] ADD UNIQUE NONCLUSTERED 
(
	[CCCD] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ_NhanVien_Ca_Ngay]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[PhanCaNhanVien] ADD  CONSTRAINT [UQ_NhanVien_Ca_Ngay] UNIQUE NONCLUSTERED 
(
	[MaNV] ASC,
	[MaCa] ASC,
	[NgayLamViec] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__PhieuGia__152C7C5CDD8DF6E0]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[PhieuGiamGia] ADD UNIQUE NONCLUSTERED 
(
	[MaCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__SanPham__8BBF4A1C2311385F]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[SanPham] ADD UNIQUE NONCLUSTERED 
(
	[MaVach] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__VaiTro__1DA5581441E3D623]    Script Date: 4/21/2026 12:34:42 PM ******/
ALTER TABLE [dbo].[VaiTro] ADD UNIQUE NONCLUSTERED 
(
	[TenVaiTro] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[ChuongTrinhKhuyenMai] ADD  DEFAULT ((0)) FOR [PhanTramGiam]
GO
ALTER TABLE [dbo].[ChuongTrinhKhuyenMai] ADD  DEFAULT ((1)) FOR [TrangThai]
GO
ALTER TABLE [dbo].[DanhMuc] ADD  DEFAULT ((1)) FOR [TrangThai]
GO
ALTER TABLE [dbo].[HoaDon] ADD  DEFAULT (getdate()) FOR [NgayLap]
GO
ALTER TABLE [dbo].[HoaDon] ADD  DEFAULT ((0)) FOR [TienGiamGia]
GO
ALTER TABLE [dbo].[HoaDon] ADD  DEFAULT (N'Hoàn thành') FOR [TrangThai]
GO
ALTER TABLE [dbo].[KhachHang] ADD  DEFAULT (N'Bạc') FOR [HangThanhVien]
GO
ALTER TABLE [dbo].[KhachHang] ADD  DEFAULT ((0)) FOR [DiemTichLuy]
GO
ALTER TABLE [dbo].[KhachHang] ADD  DEFAULT ((1)) FOR [TrangThai]
GO
ALTER TABLE [dbo].[KhachHang] ADD  DEFAULT (getdate()) FOR [NgayTao]
GO
ALTER TABLE [dbo].[NhaCungCap] ADD  DEFAULT ((1)) FOR [TrangThai]
GO
ALTER TABLE [dbo].[NhanVien] ADD  DEFAULT (getdate()) FOR [NgayVaoLam]
GO
ALTER TABLE [dbo].[NhanVien] ADD  DEFAULT ((1)) FOR [TrangThai]
GO
ALTER TABLE [dbo].[PhieuGiamGia] ADD  DEFAULT (getdate()) FOR [NgayPhatHanh]
GO
ALTER TABLE [dbo].[PhieuGiamGia] ADD  DEFAULT ((0)) FOR [DaSuDung]
GO
ALTER TABLE [dbo].[PhieuNhapHang] ADD  DEFAULT (getdate()) FOR [NgayNhap]
GO
ALTER TABLE [dbo].[PhieuNhapHang] ADD  DEFAULT ((0)) FOR [TongTien]
GO
ALTER TABLE [dbo].[SanPham] ADD  DEFAULT ((0)) FOR [SoLuongTon]
GO
ALTER TABLE [dbo].[SanPham] ADD  DEFAULT ((10)) FOR [TonKhoToiThieu]
GO
ALTER TABLE [dbo].[SanPham] ADD  DEFAULT ((1)) FOR [TrangThai]
GO
ALTER TABLE [dbo].[ChiTietHoaDon]  WITH CHECK ADD FOREIGN KEY([MaHD])
REFERENCES [dbo].[HoaDon] ([MaHD])
GO
ALTER TABLE [dbo].[ChiTietHoaDon]  WITH CHECK ADD FOREIGN KEY([MaSP])
REFERENCES [dbo].[SanPham] ([MaSP])
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap]  WITH CHECK ADD FOREIGN KEY([MaPhieuNhap])
REFERENCES [dbo].[PhieuNhapHang] ([MaPhieuNhap])
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap]  WITH CHECK ADD FOREIGN KEY([MaSP])
REFERENCES [dbo].[SanPham] ([MaSP])
GO
ALTER TABLE [dbo].[DanhMuc]  WITH CHECK ADD FOREIGN KEY([MaDanhMucCha])
REFERENCES [dbo].[DanhMuc] ([MaDanhMuc])
GO
ALTER TABLE [dbo].[HoaDon]  WITH CHECK ADD FOREIGN KEY([MaKH])
REFERENCES [dbo].[KhachHang] ([MaKH])
GO
ALTER TABLE [dbo].[HoaDon]  WITH CHECK ADD FOREIGN KEY([MaKM])
REFERENCES [dbo].[ChuongTrinhKhuyenMai] ([MaKM])
GO
ALTER TABLE [dbo].[HoaDon]  WITH CHECK ADD FOREIGN KEY([MaNV])
REFERENCES [dbo].[NhanVien] ([MaNV])
GO
ALTER TABLE [dbo].[NhanVien]  WITH CHECK ADD FOREIGN KEY([MaVaiTro])
REFERENCES [dbo].[VaiTro] ([MaVaiTro])
GO
ALTER TABLE [dbo].[PhanCaNhanVien]  WITH CHECK ADD FOREIGN KEY([MaCa])
REFERENCES [dbo].[CaLamViec] ([MaCa])
GO
ALTER TABLE [dbo].[PhanCaNhanVien]  WITH CHECK ADD FOREIGN KEY([MaNV])
REFERENCES [dbo].[NhanVien] ([MaNV])
GO
ALTER TABLE [dbo].[PhieuGiamGia]  WITH CHECK ADD FOREIGN KEY([MaKH])
REFERENCES [dbo].[KhachHang] ([MaKH])
GO
ALTER TABLE [dbo].[PhieuNhapHang]  WITH CHECK ADD FOREIGN KEY([MaNCC])
REFERENCES [dbo].[NhaCungCap] ([MaNCC])
GO
ALTER TABLE [dbo].[PhieuNhapHang]  WITH CHECK ADD FOREIGN KEY([MaNV])
REFERENCES [dbo].[NhanVien] ([MaNV])
GO
ALTER TABLE [dbo].[SanPham]  WITH CHECK ADD FOREIGN KEY([MaDanhMuc])
REFERENCES [dbo].[DanhMuc] ([MaDanhMuc])
GO
ALTER TABLE [dbo].[ChiTietHoaDon]  WITH CHECK ADD CHECK  (([SoLuong]>(0)))
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap]  WITH CHECK ADD CHECK  (([GiaNhap]>=(0)))
GO
ALTER TABLE [dbo].[ChiTietPhieuNhap]  WITH CHECK ADD CHECK  (([SoLuong]>(0)))
GO
ALTER TABLE [dbo].[SanPham]  WITH CHECK ADD CHECK  (([DonGia]>=(0)))
GO
ALTER TABLE [dbo].[SanPham]  WITH CHECK ADD CHECK  (([SoLuongTon]>=(0)))
GO
ALTER TABLE [dbo].[SanPham]  WITH CHECK ADD CHECK  (([TonKhoToiThieu]>=(0)))
GO
