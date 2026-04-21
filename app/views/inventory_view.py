import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.models.kho_hang import get_inventory_products, update_stock

# ── Màu sắc ───────────────────────────────────────────────────────────────────
BG       = "#F0F4FF"
CARD     = "#FFFFFF"
HDR_BG   = "#1B2A4A"
ROW_ODD  = "#F8FAFC"
SEL_BG   = "#DBEAFE"
BORDER   = "#E2E8F0"
ACCENT   = "#2563EB"
TEXT_D   = "#1E293B"
TEXT_M   = "#64748B"

ERR_FG   = "#DC2626"   # Đỏ (Hết hàng)
ERR_BG   = "#FEE2E2"
WARN_FG  = "#D97706"   # Cam (Sắp hết)
WARN_BG  = "#FEF3C7"
OK_FG    = "#16A34A"   # Xanh lá (Toast)

def _init_tree_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Inventory.Treeview", background=CARD, foreground=TEXT_D,
                    rowheight=40, fieldbackground=CARD, font=("Arial", 12), borderwidth=0)
    style.configure("Inventory.Treeview.Heading", background=HDR_BG, foreground="#FFFFFF",
                    font=("Arial", 12, "bold"), borderwidth=0, padding=(8, 10))
    style.map("Inventory.Treeview", background=[("selected", SEL_BG)], foreground=[("selected", TEXT_D)])
    style.map("Inventory.Treeview.Heading", background=[("active", "#243A5E")])


class InventoryView(ctk.CTkFrame):
    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee
        
        self._sort_col = None
        self._sort_reverse = False
        self._toast_timer = None
        self._current_items = []

        # Layout: Dọc 3 phần
        self.grid_rowconfigure(0, weight=0) # Top Bar
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0) # Bottom Panel
        self.grid_columnconfigure(0, weight=1)

        _init_tree_style()
        self._build_top_bar()
        self._build_main_grid()
        self._build_bottom_panel()
        
        # Shortcut Ctrl+F
        self.winfo_toplevel().bind("<Control-f>", self._focus_search)
        
        self._load_data()

    def _build_top_bar(self):
        top_bar = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        top_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        top_bar.grid_columnconfigure(0, weight=1)
        top_bar.grid_columnconfigure(1, weight=0)

        # Search Box
        search_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        search_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=15)
        search_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(search_frame, text="🔍 Tìm kiếm", font=("Arial", 14, "bold"), text_color=TEXT_D).grid(row=0, column=0, padx=(0, 15))
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Nhập Tên SP hoặc Mã vạch (Ctrl+F)...", height=40, font=("Arial", 13))
        self.entry_search.grid(row=0, column=1, sticky="ew")
        self.entry_search.bind("<KeyRelease>", lambda e: self._load_data()) # Real-time filtering

        # Filter Segmented Button
        self.seg_filter = ctk.CTkSegmentedButton(
            top_bar, 
            values=["Tất cả", "Đầy đủ", "Sắp hết hàng", "Đã hết hàng"],
            font=("Arial", 13), height=36,
            command=lambda val: self._load_data()
        )
        self.seg_filter.set("Tất cả")
        self.seg_filter.grid(row=0, column=1, padx=20, pady=15)

    def _build_main_grid(self):
        grid_frame = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        grid_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))
        grid_frame.grid_rowconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(0, weight=1)

        cols = ("ten_sp", "danh_muc", "ma_vach", "ton_kho", "tinh_trang")
        self.tree = ttk.Treeview(grid_frame, style="Inventory.Treeview", columns=cols, show="headings", selectmode="browse")

        col_cfg = [
            ("ten_sp",     "Sản phẩm",        0, "w", True),
            ("danh_muc",   "Danh mục",      160, "w", False),
            ("ma_vach",    "Mã vạch 📋",    160, "center", False),
            ("ton_kho",    "Tồn kho",       120, "center", False),
            ("tinh_trang", "Tình trạng",    160, "center", False),
        ]

        for cid, label, width, anchor, stretch in col_cfg:
            if cid in ("ten_sp", "ton_kho"):
                self.tree.heading(cid, text=label, anchor=anchor, command=lambda c=cid: self._sort_by(c))
            else:
                self.tree.heading(cid, text=label, anchor=anchor)
                
            kw = {"anchor": anchor, "stretch": stretch}
            if stretch: kw["minwidth"] = 200
            else: kw["width"] = width; kw["minwidth"] = width
            self.tree.column(cid, **kw)

        self.tree.tag_configure("het_hang", background=ERR_BG, foreground=ERR_FG)
        self.tree.tag_configure("sap_het", background=WARN_BG, foreground=WARN_FG)
        self.tree.tag_configure("odd",  background=ROW_ODD)
        self.tree.tag_configure("even", background=CARD)

        vsb = ttk.Scrollbar(grid_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(2,0), pady=2)
        vsb.grid(row=0, column=1, sticky="ns", pady=2)

        self.tree.bind("<ButtonPress-1>", self._on_tree_click)
        self.tree.bind("<Motion>", self._on_tree_motion)

    def _build_bottom_panel(self):
        bottom_panel = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER, height=80)
        bottom_panel.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        bottom_panel.grid_propagate(False)
        bottom_panel.grid_columnconfigure(1, weight=1)

        self.lbl_details = ctk.CTkLabel(bottom_panel, text="ℹ️ Chọn một sản phẩm để xem chi tiết", font=("Arial", 14), text_color=TEXT_D)
        self.lbl_details.grid(row=0, column=0, padx=20, pady=25, sticky="w")

        self.lbl_toast = ctk.CTkLabel(bottom_panel, text="", font=("Arial", 13, "italic"), text_color=OK_FG)
        self.lbl_toast.grid(row=0, column=1, padx=20, pady=25, sticky="e")

        self.btn_nhap_hang = ctk.CTkButton(
            bottom_panel, text="📦 Tạo phiếu điều chỉnh/Nhập hàng", 
            font=("Arial", 13, "bold"), fg_color=ACCENT, state="disabled",
            command=self._show_adjustment_dialog
        )
        self.btn_nhap_hang.grid(row=0, column=2, padx=20, pady=20)

    def _focus_search(self, event=None):
        if self.winfo_ismapped():
            self.entry_search.focus_set()

    def destroy(self):
        try:
            self.winfo_toplevel().unbind("<Control-f>")
        except Exception:
            pass
        super().destroy()

    def _sort_by(self, col):
        if self._sort_col == col:
            self._sort_reverse = not self._sort_reverse
        else:
            self._sort_col = col
            self._sort_reverse = False
            
        for cid in ("ten_sp", "danh_muc", "ma_vach", "ton_kho", "tinh_trang"):
            text = self.tree.heading(cid)["text"].replace(" ▴", "").replace(" ▾", "")
            if cid == col: text += " ▾" if self._sort_reverse else " ▴"
            self.tree.heading(cid, text=text)
            
        self._load_data()

    def _load_data(self):
        search_term = self.entry_search.get().strip()
        filter_val = self.seg_filter.get()
        
        # Lấy dữ liệu từ CSDL (tự động lọc theo từ khóa qua SQL)
        db_data = get_inventory_products(search_term)

        filtered = []
        for p in db_data:
            ton = p['SoLuongTon']
            min_ton = p['TonKhoToiThieu']
            if ton <= 0: status = 'Đã hết hàng'
            elif ton <= min_ton: status = 'Sắp hết hàng'
            else: status = 'Đầy đủ'
                
            if filter_val != 'Tất cả' and filter_val != status:
                continue
                
            p_copy = p.copy()
            p_copy['TinhTrang'] = status
            p_copy['TenDanhMuc'] = p_copy['TenDanhMuc'] or "Chưa phân loại"
            filtered.append(p_copy)
                
        if self._sort_col:
            def sort_key(item):
                if self._sort_col == "ten_sp": return item['TenSP'].lower()
                if self._sort_col == "ton_kho": return item['SoLuongTon']
                return ""
            filtered.sort(key=sort_key, reverse=self._sort_reverse)
            
        self._current_items = filtered
        for iid in self.tree.get_children(): self.tree.delete(iid)

        for idx, item in enumerate(filtered):
            if item['TinhTrang'] == 'Đã hết hàng': tag = "het_hang"
            elif item['TinhTrang'] == 'Sắp hết hàng': tag = "sap_het"
            else: tag = "odd" if idx % 2 == 0 else "even"
                
            ton_str = f"{item['SoLuongTon']} / {item['TonKhoToiThieu']}"
            values = (item['TenSP'], item['TenDanhMuc'], str(item['MaVach']) + " 📋", ton_str, item['TinhTrang'])
            
            self.tree.insert("", "end", iid=str(idx), values=values, tags=(tag,))
            
        self.lbl_details.configure(text="ℹ️ Chọn một sản phẩm để xem chi tiết")
        self.btn_nhap_hang.configure(state="disabled")

    def _on_tree_click(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region == "cell":
            col = self.tree.identify_column(event.x)
            row_id = self.tree.identify_row(event.y)
            if col == "#3": # Cột Mã vạch
                item_val = self.tree.item(row_id)['values']
                if item_val:
                    ma_vach = str(item_val[2]).replace(" 📋", "")
                    self.clipboard_clear()
                    self.clipboard_append(ma_vach)
                    self._show_toast(f"✅ Đã sao chép mã vạch: {ma_vach}")
                return "break"
        self.after(10, self._update_bottom_panel)
        
    def _on_tree_motion(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region == "cell":
            if self.tree.identify_column(event.x) == "#3":
                self.tree.config(cursor="hand2")
                return
        self.tree.config(cursor="")

    def _update_bottom_panel(self):
        sel = self.tree.selection()
        if not sel: return
        
        idx = int(sel[0])
        if idx < len(self._current_items):
            item = self._current_items[idx]
            don_gia_str = f"{int(item.get('DonGia', 0)):,}".replace(",", ".") + " ₫"
            self.lbl_details.configure(text=f"📦 Tên SP: {item['TenSP']}    |    💰 Đơn giá: {don_gia_str}")
            
            # Luôn cho phép điều chỉnh kho với mọi sản phẩm được chọn
            self.btn_nhap_hang.configure(state="normal")

    def _show_toast(self, msg):
        self.lbl_toast.configure(text=msg)
        if self._toast_timer:
            self.after_cancel(self._toast_timer)
        self._toast_timer = self.after(2000, lambda: self.lbl_toast.configure(text=""))

    def _show_adjustment_dialog(self):
        sel = self.tree.selection()
        if not sel: return
        
        idx = int(sel[0])
        if idx >= len(self._current_items): return
        item = self._current_items[idx]
        
        dlg = ctk.CTkToplevel(self)
        dlg.title("Điều chỉnh tồn kho")
        dlg.resizable(False, False)
        dlg.attributes("-topmost", True) # Luôn nổi lên trên cùng (thay cho grab_set dễ gây lỗi)
        
        # Căn giữa an toàn không cần update_idletasks()
        w, h = 450, 300
        sw, sh = dlg.winfo_screenwidth(), dlg.winfo_screenheight()
        dlg.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
        
        # Frame nền để Toplevel render đầy đủ tất cả phần tử
        bg_frame = ctk.CTkFrame(dlg, fg_color=CARD, corner_radius=0)
        bg_frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(bg_frame, text=f"Sản phẩm: {item['TenSP']}", font=("Arial", 16, "bold"), text_color=TEXT_D).pack(pady=(30, 5))
        ctk.CTkLabel(bg_frame, text=f"Tồn kho hiện tại: {item['SoLuongTon']}", font=("Arial", 14), text_color=TEXT_M).pack(pady=(0, 20))
        
        entry_frame = ctk.CTkFrame(bg_frame, fg_color="transparent")
        entry_frame.pack(pady=5)
        
        ctk.CTkLabel(entry_frame, text="Số lượng (+ nhập, - xuất):", font=("Arial", 14), text_color=TEXT_D).grid(row=0, column=0, padx=(0, 10))
        entry_qty = ctk.CTkEntry(entry_frame, width=100, font=("Arial", 15), justify="center")
        entry_qty.grid(row=0, column=1)
        
        lbl_err = ctk.CTkLabel(bg_frame, text="", font=("Arial", 13), text_color=ERR_FG)
        lbl_err.pack(pady=10)
        
        def on_confirm(*args):
            val = entry_qty.get().strip()
            if not val:
                lbl_err.configure(text="Lỗi: Vui lòng nhập số lượng!")
                return
            try:
                qty = int(val)
                if item['SoLuongTon'] + qty < 0:
                    lbl_err.configure(text="Lỗi: Tồn kho sau điều chỉnh không được nhỏ hơn 0!")
                    return
                if update_stock(item['MaSP'], qty):
                    dlg.destroy()
                    self._load_data()
                    self._show_toast(f"✅ Đã cập nhật tồn kho cho '{item['TenSP']}'")
                else:
                    lbl_err.configure(text="Lỗi: Không thể cập nhật CSDL!")
            except ValueError:
                lbl_err.configure(text="Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
                
        ctk.CTkButton(bg_frame, text="Xác nhận", font=("Arial", 14, "bold"), height=40, fg_color=OK_FG, hover_color="#15803D", command=on_confirm).pack(pady=10)
        entry_qty.bind("<Return>", on_confirm)
        
        # Tránh lỗi render Toplevel trên Windows bằng cách delay focus nhẹ
        dlg.after(200, entry_qty.focus_set)
