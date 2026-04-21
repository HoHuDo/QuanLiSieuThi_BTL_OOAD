import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from app.models.khach_hang import get_customers, check_phone_exists, add_customer, update_customer

# ── Màu sắc ───────────────────────────────────────────────────────────────────
BG       = "#F0F4FF"
CARD     = "#FFFFFF"
HDR_BG   = "#1B2A4A"
ROW_ODD  = "#F8FAFC"
SEL_BG   = "#DBEAFE"
BORDER   = "#E2E8F0"
ACCENT   = "#2563EB"
ACCENT_H = "#1D4ED8"
TEXT_D   = "#1E293B"

def _init_tree_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Customer.Treeview",
        background=CARD, foreground=TEXT_D,
        rowheight=40, fieldbackground=CARD,
        font=("Arial", 12), borderwidth=0, relief="flat",
    )
    style.configure("Customer.Treeview.Heading",
        background=HDR_BG, foreground="#FFFFFF",
        font=("Arial", 12, "bold"), relief="flat", borderwidth=0, padding=(8, 10),
    )
    style.map("Customer.Treeview",
        background=[("selected", SEL_BG)], foreground=[("selected", TEXT_D)],
    )
    style.map("Customer.Treeview.Heading",
        background=[("active", "#243A5E")], relief=[("active", "flat")],
    )
    style.configure("Customer.Vertical.TScrollbar",
        background="#E2E8F0", troughcolor="#F1F5F9", arrowcolor="#94A3B8", relief="flat", borderwidth=0,
    )


class CustomerView(ctk.CTkFrame):
    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee
        self.current_ma_kh = None
        self._customers_map = {}

        self.grid_rowconfigure(0, weight=0) # Form (Cố định chiều cao)
        self.grid_rowconfigure(1, weight=1) # Bảng DataGrid
        self.grid_columnconfigure(0, weight=1)

        _init_tree_style()
        self._build_form()
        self._build_table()
        
        self._load_data()

    def _build_form(self):
        form_card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        form_card.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        form_card.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkLabel(form_card, text="📝 Thông tin Khách hàng", font=("Arial", 16, "bold"), text_color=TEXT_D).grid(row=0, column=0, columnspan=4, sticky="w", padx=20, pady=(15, 10))

        # Hàng 1
        ctk.CTkLabel(form_card, text="Họ tên (*)", font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_hoten = ctk.CTkEntry(form_card, height=36, font=("Arial", 13))
        self.entry_hoten.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(form_card, text="Số điện thoại (*)", font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=1, column=1, sticky="w", padx=20, pady=(0, 5))
        self.entry_sdt = ctk.CTkEntry(form_card, height=36, font=("Arial", 13))
        self.entry_sdt.grid(row=2, column=1, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(form_card, text="Email", font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=1, column=2, sticky="w", padx=20, pady=(0, 5))
        self.entry_email = ctk.CTkEntry(form_card, height=36, font=("Arial", 13))
        self.entry_email.grid(row=2, column=2, sticky="ew", padx=20, pady=(0, 15))

        # Hàng 2
        ctk.CTkLabel(form_card, text="Ngày sinh (YYYY-MM-DD)", font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=3, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_ngaysinh = ctk.CTkEntry(form_card, height=36, font=("Arial", 13))
        self.entry_ngaysinh.grid(row=4, column=0, sticky="ew", padx=20, pady=(0, 20))

        ctk.CTkLabel(form_card, text="Giới tính", font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=3, column=1, sticky="w", padx=20, pady=(0, 5))
        self.cb_gioitinh = ctk.CTkComboBox(form_card, values=["Nam", "Nữ", "Khác"], height=36, font=("Arial", 13), state="readonly")
        self.cb_gioitinh.set("Nam")
        self.cb_gioitinh.grid(row=4, column=1, sticky="ew", padx=20, pady=(0, 20))

        ctk.CTkLabel(form_card, text="Địa chỉ", font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=3, column=2, sticky="w", padx=20, pady=(0, 5))
        self.entry_diachi = ctk.CTkEntry(form_card, height=36, font=("Arial", 13))
        self.entry_diachi.grid(row=4, column=2, sticky="ew", padx=20, pady=(0, 20))

        # Khu vực Nút bấm (Buttons)
        btn_frame = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_frame.grid(row=1, column=3, rowspan=4, sticky="nsew", padx=20, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)

        self.btn_add = ctk.CTkButton(btn_frame, text="➕ Thêm mới", height=40, font=("Arial", 13, "bold"), fg_color="#10B981", hover_color="#059669", command=self._on_add)
        self.btn_add.grid(row=0, column=0, sticky="ew", pady=(10, 10))

        self.btn_update = ctk.CTkButton(btn_frame, text="💾 Cập nhật", height=40, font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H, state="disabled", command=self._on_update)
        self.btn_update.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        self.btn_clear = ctk.CTkButton(btn_frame, text="🔄 Làm mới form", height=40, font=("Arial", 13, "bold"), fg_color="#64748B", hover_color="#475569", command=self._clear_form)
        self.btn_clear.grid(row=2, column=0, sticky="ew", pady=(0, 10))

    def _build_table(self):
        table_card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        table_card.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 20))
        table_card.grid_rowconfigure(1, weight=1)
        table_card.grid_columnconfigure(0, weight=1)

        # Thanh tìm kiếm
        search_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        search_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=15)
        search_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(search_frame, text="🔍", font=("Arial", 16)).grid(row=0, column=0, padx=(0, 10))
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Tìm theo tên hoặc số điện thoại...", height=38, font=("Arial", 13))
        self.entry_search.grid(row=0, column=1, sticky="ew", padx=(0, 15))
        self.entry_search.bind("<Return>", lambda e: self._load_data())

        ctk.CTkButton(search_frame, text="Lọc", width=90, height=38, font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H, command=self._load_data).grid(row=0, column=2)

        # DataGrid
        tree_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        cols = ("ma_kh", "ho_ten", "sdt", "ngay_sinh", "gioi_tinh", "hang_tv", "diem")
        self.tree = ttk.Treeview(tree_frame, style="Customer.Treeview", columns=cols, show="headings", selectmode="browse")

        col_cfg = [
            ("ma_kh",     "Mã KH",         130, "center", False),
            ("ho_ten",    "Họ tên",          0, "w",      True),
            ("sdt",       "SĐT",           120, "center", False),
            ("ngay_sinh", "Ngày sinh",     100, "center", False),
            ("gioi_tinh", "Giới tính",      80, "center", False),
            ("hang_tv",   "Hạng TV",       120, "center", False),
            ("diem",      "Điểm tích lũy", 120, "center", False),
        ]

        for cid, label, width, anchor, stretch in col_cfg:
            self.tree.heading(cid, text=label, anchor=anchor)
            kw = {"anchor": anchor, "stretch": stretch}
            if stretch: kw["minwidth"] = 200
            else: kw["width"] = width; kw["minwidth"] = width
            self.tree.column(cid, **kw)

        self.tree.tag_configure("odd",  background=ROW_ODD)
        self.tree.tag_configure("even", background=CARD)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview, style="Customer.Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(0, 2))
        vsb.grid(row=0, column=1, sticky="ns")

        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _load_data(self):
        for iid in self.tree.get_children():
            self.tree.delete(iid)

        search_term = self.entry_search.get().strip()
        customers = get_customers(search_term)
        
        self._customers_map = {c["MaKH"]: c for c in customers}

        for idx, c in enumerate(customers):
            tag = "odd" if idx % 2 == 0 else "even"
            ngay_sinh = c.get("NgaySinh") or ""
            values = (
                c["MaKH"], c["HoTen"], c["SoDienThoai"], 
                ngay_sinh, c.get("GioiTinh", "Khác"), c.get("HangThanhVien", "Bạc"), c.get("DiemTichLuy", 0)
            )
            self.tree.insert("", "end", iid=c["MaKH"], values=values, tags=(tag,))

    def _clear_form(self):
        self.current_ma_kh = None
        self.entry_hoten.delete(0, 'end')
        self.entry_sdt.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_ngaysinh.delete(0, 'end')
        self.cb_gioitinh.set("Nam")
        self.entry_diachi.delete(0, 'end')
        
        self.btn_add.configure(state="normal")
        self.btn_update.configure(state="disabled")
        
        if self.tree.selection():
            self.tree.selection_remove(self.tree.selection()[0])

    def _on_row_select(self, event):
        selected = self.tree.selection()
        if not selected: return
            
        ma_kh = selected[0]
        self.current_ma_kh = ma_kh
        
        # Xóa trắng các trường nhập liệu trước khi điền dữ liệu mới
        self.entry_hoten.delete(0, 'end')
        self.entry_sdt.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_ngaysinh.delete(0, 'end')
        self.entry_diachi.delete(0, 'end')
        
        c_details = self._customers_map.get(ma_kh)
        if c_details:
            self.entry_hoten.insert(0, c_details.get("HoTen") or "")
            self.entry_sdt.insert(0, c_details.get("SoDienThoai") or "")
            self.entry_email.insert(0, c_details.get("Email") or "")
            self.entry_ngaysinh.insert(0, c_details.get("NgaySinh") or "")
            self.cb_gioitinh.set(c_details.get("GioiTinh") or "Khác")
            self.entry_diachi.insert(0, c_details.get("DiaChi") or "")
            
        self.btn_add.configure(state="disabled")
        self.btn_update.configure(state="normal")

    def _validate_form(self):
        if not self.entry_hoten.get().strip():
            messagebox.showwarning("Cảnh báo", "Họ tên không được để trống!")
            return False
        if not self.entry_sdt.get().strip():
            messagebox.showwarning("Cảnh báo", "Số điện thoại không được để trống!")
            return False
        if check_phone_exists(self.entry_sdt.get().strip(), self.current_ma_kh):
            messagebox.showerror("Lỗi", "Số điện thoại này đã được đăng ký cho một thành viên khác!")
            return False
        return True

    def _get_form_data(self):
        return { "HoTen": self.entry_hoten.get().strip(), "SoDienThoai": self.entry_sdt.get().strip(), "Email": self.entry_email.get().strip(), "NgaySinh": self.entry_ngaysinh.get().strip(), "GioiTinh": self.cb_gioitinh.get(), "DiaChi": self.entry_diachi.get().strip() }

    def _on_add(self):
        if not self._validate_form(): return
        if add_customer(self._get_form_data()):
            messagebox.showinfo("Thành công", "Đã đăng ký hội viên mới thành công!")
            self._load_data(); self._clear_form()
        else: messagebox.showerror("Lỗi", "Đã xảy ra lỗi khi thêm vào CSDL.")

    def _on_update(self):
        if not self.current_ma_kh or not self._validate_form(): return
        if update_customer(self.current_ma_kh, self._get_form_data()):
            messagebox.showinfo("Thành công", "Đã cập nhật thông tin hội viên!")
            self._load_data(); self._clear_form()
        else: messagebox.showerror("Lỗi", "Đã xảy ra lỗi khi cập nhật CSDL.")