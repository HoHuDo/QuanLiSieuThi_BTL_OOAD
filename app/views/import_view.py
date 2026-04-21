import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from app.models.nha_cung_cap import get_suppliers, add_supplier, update_supplier, disable_supplier, get_supplier_columns

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
OK_FG    = "#16A34A"
TEXT_D   = "#1E293B"
TEXT_M   = "#64748B"

def _init_tree_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Supplier.Treeview",
        background=CARD, foreground=TEXT_D,
        rowheight=40, fieldbackground=CARD,
        font=("Arial", 12), borderwidth=0, relief="flat",
    )
    style.configure("Supplier.Treeview.Heading",
        background=HDR_BG, foreground="#FFFFFF",
        font=("Arial", 12, "bold"), relief="flat", borderwidth=0, padding=(8, 10),
    )
    style.map("Supplier.Treeview",
        background=[("selected", SEL_BG)], foreground=[("selected", TEXT_D)],
    )
    style.map("Supplier.Treeview.Heading",
        background=[("active", "#243A5E")], relief=[("active", "flat")],
    )
    style.configure("Supplier.Vertical.TScrollbar",
        background="#E2E8F0", troughcolor="#F1F5F9", arrowcolor="#94A3B8", relief="flat", borderwidth=0,
    )


class ImportView(ctk.CTkFrame):
    """Màn hình Quản lý Nhà cung cấp (Tái sử dụng tên class ImportView để không phải sửa main_view)"""
    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee
        self._suppliers = []
        self.current_pk = None
        
        # Tự động đọc cấu trúc bảng từ SQL
        try: self.db_cols = get_supplier_columns()
        except Exception: self.db_cols = ["MaNCC", "TenNCC", "SoDienThoai", "Email", "DiaChi"]
        self.form_fields = [c for c in self.db_cols]
        self.pk_col = self.db_cols[0] if self.db_cols else "MaNCC"

        self.grid_rowconfigure(0, weight=0) # Form
        self.grid_rowconfigure(1, weight=1) # Bảng DataGrid
        self.grid_columnconfigure(0, weight=1)

        _init_tree_style()
        self._build_form()
        self._build_table()
        
        self._load_data()

    def _build_form(self):
        form_card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        form_card.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        form_card.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(form_card, text="🏢 Thông tin Nhà cung cấp", font=("Arial", 16, "bold"), text_color=TEXT_D).grid(row=0, column=0, columnspan=4, sticky="w", padx=20, pady=(15, 10))

        # Tự động vẽ Form theo số lượng cột SQL
        self.entries = {}
        row, col = 1, 0
        for field in self.form_fields:
            ctk.CTkLabel(form_card, text=field, font=("Arial", 12, "bold"), text_color=TEXT_D).grid(row=row, column=col, sticky="w", padx=20, pady=(0, 5))
            if field.lower() == 'trangthai':
                ent = ctk.CTkComboBox(form_card, values=["True", "False"], height=36, font=("Arial", 13), state="readonly")
                ent.set("True")
            else:
                ent = ctk.CTkEntry(form_card, height=36, font=("Arial", 13))
            ent.grid(row=row+1, column=col, sticky="ew", padx=20, pady=(0, 15))
            self.entries[field] = ent
            
            col += 1
            if col > 2: col, row = 0, row + 2

        # Nút bấm 
        btn_frame = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_frame.grid(row=1, column=3, rowspan=max(row+2, 4), sticky="nsew", padx=20, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)

        self.btn_add = ctk.CTkButton(btn_frame, text="➕ Thêm mới", height=40, font=("Arial", 13, "bold"), fg_color="#10B981", hover_color="#059669", command=self._on_add)
        self.btn_add.grid(row=0, column=0, sticky="ew", pady=(10, 10))

        self.btn_update = ctk.CTkButton(btn_frame, text="💾 Cập nhật", height=40, font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H, state="disabled", command=self._on_update)
        self.btn_update.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        
        self.btn_disable = ctk.CTkButton(btn_frame, text="🗑 Xóa", height=40, font=("Arial", 13, "bold"), fg_color=DANGER, hover_color=DANGER_H, state="disabled", command=self._on_disable)
        self.btn_disable.grid(row=2, column=0, sticky="ew", pady=(0, 10))

        self.btn_clear = ctk.CTkButton(btn_frame, text="🔄 Làm mới form", height=40, font=("Arial", 13, "bold"), fg_color="#64748B", hover_color="#475569", command=self._clear_form)
        self.btn_clear.grid(row=3, column=0, sticky="ew", pady=(0, 10))

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
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Tìm kiếm nhanh...", height=38, font=("Arial", 13))
        self.entry_search.grid(row=0, column=1, sticky="ew", padx=(0, 15))
        self.entry_search.bind("<Return>", lambda e: self._load_data())

        ctk.CTkButton(search_frame, text="Lọc", width=90, height=38, font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H, command=self._load_data).grid(row=0, column=2)

        # DataGrid
        tree_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Cột tạo tự động
        self.tree = ttk.Treeview(tree_frame, style="Supplier.Treeview", show="headings", selectmode="browse")
        self.tree.configure(columns=self.db_cols)
        
        for col in self.db_cols:
            self.tree.heading(col, text=col, anchor="w")
            # Cột địa chỉ/tên cho rộng rãi hơn
            w = 200 if col.lower() in ('diachi', 'tenncc', 'email') else 120
            self.tree.column(col, width=w, minwidth=100, anchor="w")

        self.tree.tag_configure("odd",  background=ROW_ODD)
        self.tree.tag_configure("even", background=CARD)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview, style="Supplier.Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(0, 2))
        vsb.grid(row=0, column=1, sticky="ns")

        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _load_data(self):
        search_term = self.entry_search.get().strip()
        self._suppliers = get_suppliers(search_term)
        
        for iid in self.tree.get_children():
            self.tree.delete(iid)
            
        for idx, s in enumerate(self._suppliers):
            tag = "odd" if idx % 2 == 0 else "even"
            values = [str(s.get(col, '')) if s.get(col) is not None else '' for col in self.db_cols]
            pk_val = str(s.get(self.pk_col, idx))
            self.tree.insert("", "end", iid=pk_val, tags=(tag,), values=values)

    def _clear_form(self):
        self.current_pk = None
        for field, ent in self.entries.items(): 
            if field.lower() == 'trangthai':
                ent.set("True")
            else:
                ent.delete(0, 'end')
        
        self.btn_add.configure(state="normal")
        self.btn_update.configure(state="disabled")
        self.btn_disable.configure(state="disabled")
        
        if self.tree.selection(): 
            self.tree.selection_remove(self.tree.selection()[0])

    def _on_row_select(self, event):
        sel = self.tree.selection()
        if not sel: return
        
        self.current_pk = sel[0]
        
        item_values = self.tree.item(self.current_pk, "values")
        if item_values:
            for field, ent in self.entries.items(): 
                if field.lower() != 'trangthai':
                    ent.delete(0, 'end')
                
            for col, val in zip(self.db_cols, item_values):
                if col in self.entries:
                    if col.lower() == 'trangthai':
                        v = "True" if str(val) in ('1', 'True', 'true', 'TRUE') else "False"
                        self.entries[col].set(v)
                    else:
                        v = str(val) if val not in ('None', 'NULL', '') else ''
                        self.entries[col].insert(0, v)
            
            self.btn_add.configure(state="disabled")
            self.btn_update.configure(state="normal")
            self.btn_disable.configure(state="normal")

    def _get_form_data(self):
        data = {}
        for field, ent in self.entries.items():
            val = ent.get().strip()
            if field.lower() == 'trangthai':
                data[field] = 1 if val == "True" else 0
            else:
                data[field] = val
        return data

    def _on_add(self):
        d = self._get_form_data()
        ok, msg = add_supplier(d)
        if ok: 
            self._load_data()
            self._clear_form()
            messagebox.showinfo("Thành công", "Đã thêm Nhà cung cấp mới!")
        else:
            messagebox.showerror("Lỗi SQL", f"Lỗi không thể thêm:\n{msg}")

    def _on_update(self):
        if not self.current_pk: return
        d = self._get_form_data()
        ok, msg = update_supplier(self.current_pk, d)
        if ok: 
            self._load_data()
            self._clear_form()
            messagebox.showinfo("Thành công", "Đã cập nhật thông tin Nhà cung cấp!")
        else:
            messagebox.showerror("Lỗi SQL", f"Lỗi không thể cập nhật:\n{msg}")

    def _on_disable(self):
        if not self.current_pk: return
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa dòng này khỏi CSDL?"):
            ok, msg = disable_supplier(self.current_pk)
            if ok:
                self._load_data()
                self._clear_form()
            else:
                messagebox.showerror("Lỗi SQL", f"Lỗi không thể xóa:\n{msg}")