import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from app.models.khuyen_mai import get_promotions, add_promotion, update_promotion

BG       = "#F0F4FF"
CARD     = "#FFFFFF"
HDR_BG   = "#1B2A4A"
ROW_ODD  = "#F8FAFC"
SEL_BG   = "#DBEAFE"
BORDER   = "#E2E8F0"
ACCENT   = "#2563EB"
ACCENT_H = "#1D4ED8"
TEXT_D   = "#1E293B"
OK_FG    = "#16A34A"

def _init_tree_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Promo.Treeview", background=CARD, foreground=TEXT_D, rowheight=40, borderwidth=0)
    style.configure("Promo.Treeview.Heading", background=HDR_BG, foreground="#FFFFFF", font=("Arial", 12, "bold"), borderwidth=0)
    style.map("Promo.Treeview", background=[("selected", SEL_BG)], foreground=[("selected", TEXT_D)])

class PromotionView(ctk.CTkFrame):
    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee
        self.current_pk = None
        
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
        form_card.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkLabel(form_card, text="🎟️ Tạo chương trình Khuyến mãi", font=("Arial", 16, "bold"), text_color=TEXT_D).grid(row=0, column=0, columnspan=4, sticky="w", padx=20, pady=(15, 10))

        font_lbl = ("Arial", 12, "bold")
        font_inp = ("Arial", 13)

        # Hàng 1
        ctk.CTkLabel(form_card, text="Tên chương trình (*)", font=font_lbl, text_color=TEXT_D).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_ten = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_ten.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(form_card, text="% Giảm giá (*)", font=font_lbl, text_color=TEXT_D).grid(row=1, column=1, sticky="w", padx=20, pady=(0, 5))
        self.entry_giam = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_giam.grid(row=2, column=1, sticky="ew", padx=20, pady=(0, 15))

        ctk.CTkLabel(form_card, text="Ngày bắt đầu (YYYY-MM-DD)", font=font_lbl, text_color=TEXT_D).grid(row=1, column=2, sticky="w", padx=20, pady=(0, 5))
        self.entry_start = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_start.grid(row=2, column=2, sticky="ew", padx=20, pady=(0, 15))

        # Hàng 2
        ctk.CTkLabel(form_card, text="Ngày kết thúc (YYYY-MM-DD)", font=font_lbl, text_color=TEXT_D).grid(row=3, column=0, sticky="w", padx=20, pady=(0, 5))
        self.entry_end = ctk.CTkEntry(form_card, height=36, font=font_inp)
        self.entry_end.grid(row=4, column=0, sticky="ew", padx=20, pady=(0, 20))

        ctk.CTkLabel(form_card, text="Trạng thái", font=font_lbl, text_color=TEXT_D).grid(row=3, column=1, sticky="w", padx=20, pady=(0, 5))
        self.cb_status = ctk.CTkComboBox(form_card, values=["Kích hoạt", "Vô hiệu hóa"], height=36, font=font_inp, state="readonly")
        self.cb_status.set("Kích hoạt")
        self.cb_status.grid(row=4, column=1, sticky="ew", padx=20, pady=(0, 20))

        # Nút bấm (Cột 3, chiếm 4 hàng)
        btn_frame = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_frame.grid(row=1, column=3, rowspan=4, sticky="nsew", padx=20, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)

        self.btn_add = ctk.CTkButton(btn_frame, text="➕ Tạo mới", height=40, font=("Arial", 13, "bold"), fg_color=OK_FG, command=self._on_add)
        self.btn_add.grid(row=0, column=0, sticky="ew", pady=(5, 10))

        self.btn_update = ctk.CTkButton(btn_frame, text="💾 Cập nhật", height=40, font=("Arial", 13, "bold"), fg_color=ACCENT, hover_color=ACCENT_H, state="disabled", command=self._on_update)
        self.btn_update.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        self.btn_clear = ctk.CTkButton(btn_frame, text="🔄 Làm mới form", height=40, font=("Arial", 13, "bold"), fg_color="#64748B", command=self._clear_form)
        self.btn_clear.grid(row=2, column=0, sticky="ew", pady=(0, 10))

    def _build_table(self):
        table_card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12, border_width=1, border_color=BORDER)
        table_card.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 20))
        table_card.grid_rowconfigure(1, weight=1)
        table_card.grid_columnconfigure(0, weight=1)

        search_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        search_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=15)
        search_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(search_frame, text="🔍", font=("Arial", 16)).grid(row=0, column=0, padx=(0, 10))
        self.entry_search = ctk.CTkEntry(search_frame, placeholder_text="Tìm theo tên Khuyến mãi...", height=38, font=("Arial", 13))
        self.entry_search.grid(row=0, column=1, sticky="ew", padx=(0, 15))
        self.entry_search.bind("<Return>", lambda e: self._load_data())
        ctk.CTkButton(search_frame, text="Lọc", width=90, height=38, font=("Arial", 13, "bold"), fg_color=ACCENT, command=self._load_data).grid(row=0, column=2)

        tree_frame = ctk.CTkFrame(table_card, fg_color="transparent")
        tree_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        cols = ("ma", "ten", "giam", "bd", "kt", "tt")
        self.tree = ttk.Treeview(tree_frame, style="Promo.Treeview", columns=cols, show="headings", selectmode="browse")

        col_cfg = [("ma", "Mã KM", 80, "center"), ("ten", "Tên Chương trình", 250, "w"), ("giam", "% Giảm", 100, "center"), 
                   ("bd", "Từ ngày", 120, "center"), ("kt", "Đến ngày", 120, "center"), ("tt", "Trạng thái", 120, "center")]

        for cid, label, width, anchor in col_cfg:
            self.tree.heading(cid, text=label, anchor=anchor)
            self.tree.column(cid, width=width, minwidth=width, anchor=anchor, stretch=(cid == "ten"))

        self.tree.tag_configure("odd",  background=ROW_ODD)
        self.tree.tag_configure("even", background=CARD)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(0, 2))
        vsb.grid(row=0, column=1, sticky="ns")
        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

    def _load_data(self):
        for iid in self.tree.get_children(): self.tree.delete(iid)
        data = get_promotions(self.entry_search.get().strip())
        for idx, item in enumerate(data):
            tag = "odd" if idx % 2 == 0 else "even"
            tt = "Kích hoạt" if item.get('TrangThai') else "Vô hiệu hóa"
            giam = f"{item['PhanTramGiam']}%"
            self.tree.insert("", "end", iid=str(item['MaKM']), tags=(tag,), 
                             values=(item['MaKM'], item['TenKM'], giam, item['NgayBatDau'], item['NgayKetThuc'], tt))

    def _clear_form(self):
        self.current_pk = None
        for e in [self.entry_ten, self.entry_giam, self.entry_start, self.entry_end]: e.delete(0, 'end')
        self.cb_status.set("Kích hoạt")
        self.btn_add.configure(state="normal")
        self.btn_update.configure(state="disabled")
        if self.tree.selection(): self.tree.selection_remove(self.tree.selection()[0])

    def _on_row_select(self, event):
        sel = self.tree.selection()
        if not sel: return
        self.current_pk = sel[0]
        vals = self.tree.item(self.current_pk, "values")
        if vals:
            self._clear_form()
            self.current_pk = sel[0]
            self.entry_ten.insert(0, vals[1])
            self.entry_giam.insert(0, vals[2].replace("%", ""))
            self.entry_start.insert(0, vals[3] if vals[3] != 'None' else '')
            self.entry_end.insert(0, vals[4] if vals[4] != 'None' else '')
            self.cb_status.set(vals[5])
            self.btn_add.configure(state="disabled")
            self.btn_update.configure(state="normal")

    def _get_data(self):
        try:
            return {
                "TenKM": self.entry_ten.get().strip(),
                "PhanTramGiam": float(self.entry_giam.get().strip()),
                "NgayBatDau": self.entry_start.get().strip(),
                "NgayKetThuc": self.entry_end.get().strip(),
                "TrangThai": 1 if self.cb_status.get() == "Kích hoạt" else 0
            }
        except ValueError: return None

    def _on_add(self):
        d = self._get_data()
        if not d: return messagebox.showerror("Lỗi", "% Giảm giá phải là một con số hợp lệ!")
        if not d['TenKM']: return messagebox.showerror("Lỗi", "Vui lòng điền Tên chương trình!")
        ok, msg = add_promotion(d)
        if ok:
            self._load_data(); self._clear_form(); messagebox.showinfo("OK", "Đã tạo chương trình khuyến mãi!")
        else: messagebox.showerror("Lỗi CSDL", msg)

    def _on_update(self):
        d = self._get_data()
        if not d or not self.current_pk: return
        ok, msg = update_promotion(self.current_pk, d)
        if ok:
            self._load_data(); self._clear_form(); messagebox.showinfo("OK", "Đã cập nhật chương trình!")
        else: messagebox.showerror("Lỗi CSDL", msg)