import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from app.models.nhan_vien import (
    get_active_employees, get_roles, check_unique, 
    add_employee, update_employee, disable_employee
)

# ── Màu sắc ───────────────────────────────────────────────────────────────────
BG       = "#F0F4FF"
CARD     = "#FFFFFF"
HDR_BG   = "#1B2A4A"
ROW_ODD  = "#F8FAFC"
SEL_BG   = "#DBEAFE"
BORDER   = "#E2E8F0"
ACCENT   = "#2563EB"
ACCENT_H = "#1D4ED8"
DANGER   = "#DC2626"
DANGER_H = "#B91C1C"
TEXT_D   = "#1E293B"

def _init_tree_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Employee.Treeview", background=CARD, foreground=TEXT_D,
                    rowheight=40, fieldbackground=CARD, font=("Arial", 12), borderwidth=0)
    style.configure("Employee.Treeview.Heading", background=HDR_BG, foreground="#FFFFFF",
                    font=("Arial", 12, "bold"), borderwidth=0, padding=(8, 10))
    style.map("Employee.Treeview", background=[("selected", SEL_BG)], foreground=[("selected", TEXT_D)])
    style.map("Employee.Treeview.Heading", background=[("active", "#243A5E")])


class EmployeeView(ctk.CTkFrame):
    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee
        
        # Kiểm tra Quyền truy cập
        if self.employee.get("vai_tro") != "Quản lý":
            ctk.CTkLabel(self, text="🚫 BẠN KHÔNG CÓ QUYỀN TRUY CẬP CHỨC NĂNG NÀY!", 
                         font=("Arial", 22, "bold"), text_color=DANGER).place(relx=0.5, rely=0.5, anchor="center")
            return
            
        self.current_ma_nv = None
        self._employees_map = {}
        
        # Tải danh sách quyền (Roles)
        db_roles = get_roles()
        self.role_map = {r["TenVaiTro"]: r["MaVaiTro"] for r in db_roles}
        self.role_names = list(self.role_map.keys())

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        _init_tree_style()
        self._build_form()
        self._build_table()
        
        self._load_data()

    def _build_form(self):
        form_card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        form_card.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        form_card.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(form_card, text="👤 Thông tin Nhân viên", font=("Arial", 16, "bold"), text_color=TEXT_D).grid(row=0, column=0, columnspan=4, sticky="w", padx=20, pady=(15, 10))

        font_lbl = ("Arial", 12, "bold")
        font_inp = ("Arial", 13)

        # --- Cột 1 ---
        ctk.CTkLabel(form_card, text="Họ tên (*)", font=font_lbl, text_color=TEXT_D).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_hoten = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_hoten.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(form_card, text="Ngày sinh", font=font_lbl, text_color=TEXT_D).grid(row=3, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_ngaysinh = ctk.CTkEntry(form_card, height=36, font=font_inp, placeholder_text="YYYY-MM-DD")
        self.entry_ngaysinh.grid(row=4, column=0, sticky="ew", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(form_card, text="Vị trí (Chức danh)", font=font_lbl, text_color=TEXT_D).grid(row=5, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_vitri = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_vitri.grid(row=6, column=0, sticky="ew", padx=20, pady=(0, 15))

        # --- Cột 2 ---
        ctk.CTkLabel(form_card, text="CCCD (*)", font=font_lbl, text_color=TEXT_D).grid(row=1, column=1, sticky="w", padx=20, pady=(0, 5))
        self.entry_cccd = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_cccd.grid(row=2, column=1, sticky="ew", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(form_card, text="Giới tính", font=font_lbl, text_color=TEXT_D).grid(row=3, column=1, sticky="w", padx=20, pady=(0, 5))
        self.cb_gioitinh = ctk.CTkComboBox(form_card, values=["Nam", "Nữ", "Khác"], height=36, font=font_inp, state="readonly")
        self.cb_gioitinh.grid(row=4, column=1, sticky="ew", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(form_card, text="Bộ phận", font=font_lbl, text_color=TEXT_D).grid(row=5, column=1, sticky="w", padx=20, pady=(0, 5))
        self.entry_bophan = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_bophan.grid(row=6, column=1, sticky="ew", padx=20, pady=(0, 15))

        # --- Cột 3 ---
        ctk.CTkLabel(form_card, text="Số điện thoại (*)", font=font_lbl, text_color=TEXT_D).grid(row=1, column=2, sticky="w", padx=20, pady=(0, 5))
        self.entry_sdt = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_sdt.grid(row=2, column=2, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(form_card, text="Email", font=font_lbl, text_color=TEXT_D).grid(row=3, column=2, sticky="w", padx=20, pady=(0, 5))
        self.entry_email = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_email.grid(row=4, column=2, sticky="ew", padx=20, pady=(0, 15))
        
        ctk.CTkLabel(form_card, text="Vai trò hệ thống (*)", font=font_lbl, text_color=TEXT_D).grid(row=5, column=2, sticky="w", padx=20, pady=(0, 5))
        self.cb_vaitro = ctk.CTkComboBox(form_card, values=self.role_names, height=36, font=font_inp, state="readonly")
        self.cb_vaitro.grid(row=6, column=2, sticky="ew", padx=20, pady=(0, 15))

        # --- Hàng cuối (Địa chỉ chiếm cả 3 cột) ---
        ctk.CTkLabel(form_card, text="Địa chỉ", font=font_lbl, text_color=TEXT_D).grid(row=7, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_diachi = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_diachi.grid(row=8, column=0, columnspan=3, sticky="ew", padx=20, pady=(0, 20))

        # --- Cột 4 (Buttons) ---
        btn_frame = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_frame.grid(row=1, column=3, rowspan=8, sticky="nsew", padx=20, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)

        self.btn_add = ctk.CTkButton(btn_frame, text="➕ Thêm mới", height=40, font=("Arial", 13, "bold"), fg_color="#10B981", hover_color="#059669", command=self._on_add)
        self.btn_add.grid(row=0, column=0, sticky="ew", pady=(10, 10))

        self.btn_update = ctk.CTkButton(btn_frame, text="💾 Cập nhật", height=40, font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H, state="disabled", command=self._on_update)
        self.btn_update.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        
        self.btn_disable = ctk.CTkButton(btn_frame, text="🗑 Vô hiệu hóa", height=40, font=("Arial", 13, "bold"), fg_color=DANGER, hover_color=DANGER_H, state="disabled", command=self._on_disable)
        self.btn_disable.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        self.btn_clear = ctk.CTkButton(btn_frame, text="🔄 Làm mới form", height=40, font=("Arial", 13, "bold"), fg_color="#64748B", hover_color="#475569", command=self._clear_form)
        self.btn_clear.grid(row=3, column=0, sticky="ew", pady=(0, 10))

    def _build_table(self):
        table_card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        table_card.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 20))
        table_card.grid_rowconfigure(1, weight=1)
        table_card.grid_columnconfigure(0, weight=1)

        # Search
        search_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        search_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=15)
        search_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(search_frame, text="🔍", font=("Arial", 16)).grid(row=0, column=0, padx=(0, 10))
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Tìm theo Họ tên, SĐT hoặc CCCD...", height=38, font=("Arial", 13))
        self.entry_search.grid(row=0, column=1, sticky="ew", padx=(0, 15))
        self.entry_search.bind("<Return>", lambda e: self._load_data())
        ctk.CTkButton(search_frame, text="Lọc", width=90, height=38, font=("Arial", 13, "bold"), fg_color=ACCENT, command=self._load_data).grid(row=0, column=2)

        # Treeview
        tree_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        cols = ("ma_nv", "ho_ten", "vai_tro", "cccd", "sdt", "vi_tri", "bo_phan")
        self.tree = ttk.Treeview(tree_frame, style="Employee.Treeview", columns=cols, show="headings", selectmode="browse")

        col_cfg = [
            ("ma_nv",    "Mã NV",     100, "center"),
            ("ho_ten",   "Họ tên",    200, "w"),
            ("vai_tro",  "Quyền",     130, "center"),
            ("cccd",     "CCCD",      130, "center"),
            ("sdt",      "SĐT",       120, "center"),
            ("vi_tri",   "Vị trí",    150, "center"),
            ("bo_phan",  "Bộ phận",   150, "center"),
        ]

        for cid, label, width, anchor in col_cfg:
            self.tree.heading(cid, text=label, anchor=anchor)
            self.tree.column(cid, width=width, minwidth=width, anchor=anchor, stretch=(cid == "ho_ten"))

        self.tree.tag_configure("odd",  background=ROW_ODD)
        self.tree.tag_configure("even", background=CARD)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(0, 2))
        vsb.grid(row=0, column=1, sticky="ns")
        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _load_data(self):
        for iid in self.tree.get_children(): self.tree.delete(iid)
        employees = get_active_employees(self.entry_search.get().strip())
        self._employees_map = {e["MaNV"]: e for e in employees}

        for idx, e in enumerate(employees):
            tag = "odd" if idx % 2 == 0 else "even"
            self.tree.insert("", "end", iid=e["MaNV"], tags=(tag,), values=(
                e["MaNV"], e["HoTen"], e.get("TenVaiTro", "N/A"), e["CCCD"],
                e["SoDienThoai"], e.get("ViTri", ""), e.get("BoPhan", "")
            ))

    def _clear_form(self):
        self.current_ma_nv = None
        for entry in (self.entry_hoten, self.entry_cccd, self.entry_sdt, self.entry_ngaysinh, 
                      self.entry_email, self.entry_vitri, self.entry_bophan, self.entry_diachi):
            entry.delete(0, 'end')
        self.cb_gioitinh.set("Nam")
        if self.role_names: self.cb_vaitro.set(self.role_names[0])
        
        self.btn_add.configure(state="normal")
        self.btn_update.configure(state="disabled")
        self.btn_disable.configure(state="disabled")
        if self.tree.selection(): self.tree.selection_remove(self.tree.selection()[0])

    def _on_row_select(self, event):
        selected = self.tree.selection()
        if not selected: return
        
        self.current_ma_nv = selected[0]
        
        for entry in (self.entry_hoten, self.entry_cccd, self.entry_sdt, self.entry_ngaysinh, 
                      self.entry_email, self.entry_vitri, self.entry_bophan, self.entry_diachi):
            entry.delete(0, 'end')
            
        e = self._employees_map.get(self.current_ma_nv)
        if e:
            self.entry_hoten.insert(0, e.get("HoTen") or "")
            self.entry_cccd.insert(0, e.get("CCCD") or "")
            self.entry_sdt.insert(0, e.get("SoDienThoai") or "")
            self.entry_ngaysinh.insert(0, e.get("NgaySinh") or "")
            self.entry_email.insert(0, e.get("Email") or "")
            self.entry_vitri.insert(0, e.get("ViTri") or "")
            self.entry_bophan.insert(0, e.get("BoPhan") or "")
            self.entry_diachi.insert(0, e.get("DiaChi") or "")
            self.cb_gioitinh.set(e.get("GioiTinh") or "Nam")
            self.cb_vaitro.set(e.get("TenVaiTro") or self.role_names[0])
            
        self.btn_add.configure(state="disabled")
        self.btn_update.configure(state="normal")
        self.btn_disable.configure(state="normal")

    def _get_form_data(self):
        return {
            "HoTen": self.entry_hoten.get().strip(), "CCCD": self.entry_cccd.get().strip(),
            "SoDienThoai": self.entry_sdt.get().strip(), "NgaySinh": self.entry_ngaysinh.get().strip(),
            "GioiTinh": self.cb_gioitinh.get(), "Email": self.entry_email.get().strip(),
            "ViTri": self.entry_vitri.get().strip(), "BoPhan": self.entry_bophan.get().strip(),
            "DiaChi": self.entry_diachi.get().strip(), "MaVaiTro": self.role_map.get(self.cb_vaitro.get())
        }

    def _validate(self):
        data = self._get_form_data()
        if not data["HoTen"] or not data["CCCD"] or not data["SoDienThoai"]:
            messagebox.showwarning("Thiếu thông tin", "Họ tên, CCCD và Số điện thoại không được để trống!")
            return None
        if check_unique(data["CCCD"], data["SoDienThoai"], self.current_ma_nv):
            messagebox.showerror("Trùng lặp", "CCCD hoặc Số điện thoại này đã tồn tại trong hệ thống!")
            return None
        return data

    def _on_add(self):
        data = self._validate()
        if not data: return
        
        success, result = add_employee(data)
        if success:
            messagebox.showinfo("Thành công", f"Đã tạo nhân viên.\n\nTài khoản mặc định:\n- Username: {result}\n- Password: supermarket@123")
            self._load_data()
            self._clear_form()
        else:
            messagebox.showerror("Lỗi", "Không thể thêm nhân viên: " + result)

    def _on_update(self):
        if not self.current_ma_nv: return
        data = self._validate()
        if not data: return
        
        try:
            update_employee(self.current_ma_nv, data)
            messagebox.showinfo("Thành công", "Đã cập nhật thông tin nhân viên!")
            self._load_data()
            self._clear_form()
        except Exception as e:
            messagebox.showerror("Lỗi", "Không thể cập nhật nhân viên: " + str(e))

    def _on_disable(self):
        if not self.current_ma_nv: return
        if self.current_ma_nv == self.employee.get("ma_nv"):
            messagebox.showerror("Từ chối thao tác", "Bạn không thể tự vô hiệu hóa tài khoản của chính mình!")
            return
            
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn vô hiệu hóa nhân viên này?\nNhân viên sẽ bị khóa đăng nhập và không thể truy cập hệ thống."):
            disable_employee(self.current_ma_nv)
            messagebox.showinfo("Đã vô hiệu hóa", "Nhân viên đã bị chuyển trạng thái vô hiệu hóa.")
            self._load_data()
            self._clear_form()