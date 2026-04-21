import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.models.bao_cao import (
    get_revenue_summary, get_daily_revenue, 
    get_category_revenue, get_top_products, get_inventory_value_report
)

BG       = "#F0F4FF"
CARD     = "#FFFFFF"
HDR_BG   = "#1B2A4A"
TEXT_D   = "#1E293B"
ACCENT   = "#2563EB"

def _fmt(amount: float) -> str:
    return f"{int(amount):,}".replace(",", ".") + " ₫"

class ReportView(ctk.CTkFrame):
    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee

        if self.employee.get("vai_tro") not in ["Quản lý", "Quản trị viên"]:
            ctk.CTkLabel(self, text="🚫 BẠN KHÔNG CÓ QUYỀN XEM BÁO CÁO!", 
                         font=("Arial", 22, "bold"), text_color="#DC2626").place(relx=0.5, rely=0.5, anchor="center")
            return

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabview = ctk.CTkTabview(self, fg_color=CARD, text_color=TEXT_D, segmented_button_selected_color=ACCENT)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        self.tab_doanhthu = self.tabview.add("📈 Doanh thu & Bán hàng")
        self.tab_kho = self.tabview.add("📦 Báo cáo Tồn kho")
        
        self._build_revenue_tab()
        self._build_inventory_tab()
        
        self._load_revenue_data()
        self._load_inventory_data()

    # =========================================================================
    # TAB 1: DOANH THU & BÁN HÀNG
    # =========================================================================
    def _build_revenue_tab(self):
        self.tab_doanhthu.grid_rowconfigure(2, weight=1)
        self.tab_doanhthu.grid_columnconfigure((0, 1), weight=1)

        # 1. Filter Bar
        filter_frame = ctk.CTkFrame(self.tab_doanhthu, fg_color="transparent")
        filter_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        
        today = datetime.now()
        first_day = today.replace(day=1)
        
        ctk.CTkLabel(filter_frame, text="Từ ngày:", font=("Arial", 13, "bold")).pack(side="left", padx=(0, 10))
        self.entry_start = ctk.CTkEntry(filter_frame, width=120, height=36)
        self.entry_start.insert(0, first_day.strftime("%Y-%m-%d"))
        self.entry_start.pack(side="left", padx=(0, 20))
        
        ctk.CTkLabel(filter_frame, text="Đến ngày:", font=("Arial", 13, "bold")).pack(side="left", padx=(0, 10))
        self.entry_end = ctk.CTkEntry(filter_frame, width=120, height=36)
        self.entry_end.insert(0, today.strftime("%Y-%m-%d"))
        self.entry_end.pack(side="left", padx=(0, 20))
        
        ctk.CTkButton(filter_frame, text="Thống kê", height=36, font=("Arial", 13, "bold"), fg_color=ACCENT, command=self._load_revenue_data).pack(side="left")

        # 2. Summary Cards
        cards_frame = ctk.CTkFrame(self.tab_doanhthu, fg_color="transparent")
        cards_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.lbl_doanhthu = self._create_summary_card(cards_frame, 0, "💰 Tổng Doanh Thu", "#EFF6FF", ACCENT)
        self.lbl_loinhuan = self._create_summary_card(cards_frame, 1, "💎 Tổng Lợi Nhuận", "#F0FDF4", "#16A34A")
        self.lbl_hoadon = self._create_summary_card(cards_frame, 2, "🧾 Số Hóa Đơn", "#FEF2F2", "#DC2626")

        # 3. Charts & Top Products Area
        self.chart_frame = ctk.CTkFrame(self.tab_doanhthu, fg_color="transparent")
        self.chart_frame.grid(row=2, column=0, sticky="nsew", padx=(0, 10), pady=10)
        
        right_frame = ctk.CTkFrame(self.tab_doanhthu, fg_color="transparent")
        right_frame.grid(row=2, column=1, sticky="nsew", padx=(10, 0), pady=10)
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=1)
        
        self.pie_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
        self.pie_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        
        # Bảng Top SP
        top_sp_frame = ctk.CTkFrame(right_frame, fg_color="#F8FAFC", border_width=1, border_color="#E2E8F0")
        top_sp_frame.grid(row=1, column=0, sticky="nsew")
        ctk.CTkLabel(top_sp_frame, text="🏆 Top 10 Sản phẩm bán chạy", font=("Arial", 14, "bold"), text_color=TEXT_D).pack(pady=10)
        
        self.tree_top = ttk.Treeview(top_sp_frame, columns=("ma", "ten", "sl"), show="headings", height=8)
        self.tree_top.heading("ma", text="Mã SP"); self.tree_top.column("ma", width=80, anchor="center")
        self.tree_top.heading("ten", text="Tên sản phẩm"); self.tree_top.column("ten", width=200, anchor="w")
        self.tree_top.heading("sl", text="Đã bán"); self.tree_top.column("sl", width=80, anchor="center")
        self.tree_top.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Khởi tạo Figure Matplotlib
        self.fig_bar, self.ax_bar = plt.subplots(figsize=(6, 4), facecolor=CARD)
        self.canvas_bar = FigureCanvasTkAgg(self.fig_bar, master=self.chart_frame)
        self.canvas_bar.get_tk_widget().pack(fill="both", expand=True)
        
        self.fig_pie, self.ax_pie = plt.subplots(figsize=(4, 3), facecolor=CARD)
        self.canvas_pie = FigureCanvasTkAgg(self.fig_pie, master=self.pie_frame)
        self.canvas_pie.get_tk_widget().pack(fill="both", expand=True)

    def _create_summary_card(self, parent, col, title, bg_color, fg_color):
        card = ctk.CTkFrame(parent, fg_color=bg_color, corner_radius=10, border_width=1, border_color="#E2E8F0")
        card.grid(row=0, column=col, sticky="ew", padx=5)
        ctk.CTkLabel(card, text=title, font=("Arial", 14, "bold"), text_color="#64748B").pack(pady=(15, 5))
        lbl_val = ctk.CTkLabel(card, text="0", font=("Arial", 24, "bold"), text_color=fg_color)
        lbl_val.pack(pady=(0, 15))
        return lbl_val

    def _load_revenue_data(self):
        start = self.entry_start.get().strip()
        end = self.entry_end.get().strip()
        
        try:
            datetime.strptime(start, "%Y-%m-%d")
            datetime.strptime(end, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày tháng phải đúng định dạng YYYY-MM-DD")
            return

        # 1. Cập nhật thẻ tóm tắt
        summary = get_revenue_summary(start, end)
        self.lbl_doanhthu.configure(text=_fmt(summary["doanh_thu"]))
        self.lbl_loinhuan.configure(text=_fmt(summary["loi_nhuan"]))
        self.lbl_hoadon.configure(text=f"{summary['so_hd']} đơn")

        # 2. Vẽ biểu đồ cột (Doanh thu theo ngày)
        daily_data = get_daily_revenue(start, end)
        self.ax_bar.clear()
        if daily_data:
            days = [d["ngay"] for d in daily_data]
            revs = [d["doanh_thu"] for d in daily_data]
            self.ax_bar.bar(days, revs, color=ACCENT, width=0.5, align='center')
            self.ax_bar.set_title("Doanh thu theo ngày", fontsize=12, fontweight='bold', color=TEXT_D)
            self.ax_bar.tick_params(axis='x', rotation=45, labelsize=9)
            self.ax_bar.tick_params(axis='y', labelsize=9)
            self.ax_bar.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{int(x/1000)}k"))
            self.ax_bar.spines['top'].set_visible(False)
            self.ax_bar.spines['right'].set_visible(False)
        else:
            self.ax_bar.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center', fontsize=12)
        
        self.fig_bar.tight_layout()
        self.canvas_bar.draw()

        # 3. Vẽ biểu đồ tròn (Doanh thu theo danh mục)
        cat_data = get_category_revenue(start, end)
        self.ax_pie.clear()
        if cat_data:
            labels = [d["danh_muc"] for d in cat_data]
            sizes = [d["doanh_thu"] for d in cat_data]
            self.ax_pie.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
            self.ax_pie.set_title("Tỷ trọng Danh mục", fontsize=12, fontweight='bold', color=TEXT_D)
        else:
            self.ax_pie.text(0.5, 0.5, "Không có dữ liệu", ha='center', va='center')
            
        self.fig_pie.tight_layout()
        self.canvas_pie.draw()

        # 4. Cập nhật DataGrid Top Sản phẩm
        for iid in self.tree_top.get_children(): self.tree_top.delete(iid)
        top_prods = get_top_products(start, end)
        for p in top_prods:
            self.tree_top.insert("", "end", values=(p["ma_sp"], p["ten_sp"], p["so_luong"]))

    # =========================================================================
    # TAB 2: BÁO CÁO KHO HÀNG
    # =========================================================================
    def _build_inventory_tab(self):
        self.tab_kho.grid_rowconfigure(1, weight=1)
        self.tab_kho.grid_columnconfigure(0, weight=1)
        
        header = ctk.CTkFrame(self.tab_kho, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        ctk.CTkLabel(header, text="📋 Top Sản phẩm có giá trị Tồn kho cao nhất", font=("Arial", 16, "bold"), text_color=TEXT_D).pack(side="left")
        ctk.CTkButton(header, text="🔄 Làm mới", font=("Arial", 12), width=100, height=32, command=self._load_inventory_data).pack(side="right")

        self.tree_kho = ttk.Treeview(self.tab_kho, columns=("ma", "ten", "sl", "gia", "gt"), show="headings")
        
        col_cfg = [("ma", "Mã SP", 100, "center"), ("ten", "Tên sản phẩm", 300, "w"), 
                   ("sl", "SL Tồn", 100, "center"), ("gia", "Đơn giá", 150, "e"), ("gt", "Giá trị tồn (VNĐ)", 180, "e")]
                   
        for c, t, w, a in col_cfg:
            self.tree_kho.heading(c, text=t)
            self.tree_kho.column(c, width=w, anchor=a)
            
        vsb = ttk.Scrollbar(self.tab_kho, orient="vertical", command=self.tree_kho.yview)
        self.tree_kho.configure(yscrollcommand=vsb.set)
        self.tree_kho.grid(row=1, column=0, sticky="nsew")
        vsb.grid(row=1, column=1, sticky="ns")
        
        self.tree_kho.tag_configure("even", background="#F8FAFC")
        self.tree_kho.tag_configure("odd", background="#FFFFFF")

    def _load_inventory_data(self):
        for iid in self.tree_kho.get_children(): self.tree_kho.delete(iid)
        inv_data = get_inventory_value_report()
        
        for idx, item in enumerate(inv_data):
            tag = "even" if idx % 2 == 0 else "odd"
            self.tree_kho.insert("", "end", tags=(tag,), values=(
                item["MaSP"], item["TenSP"], item["SoLuongTon"], 
                _fmt(item["DonGia"]), _fmt(item["GiaTriTon"])
            ))