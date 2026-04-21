import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.models.san_pham import find_by_barcode
from app.models.hoa_don import create_invoice
from app.models.khuyen_mai import get_active_discount

# ── Màu sắc ───────────────────────────────────────────────────────────────────
BG       = "#F0F4FF"
CARD     = "#FFFFFF"
HDR_BG   = "#1B2A4A"
ROW_ODD  = "#F8FAFC"
SEL_BG   = "#DBEAFE"
BORDER   = "#E2E8F0"
ACCENT   = "#2563EB"
ACCENT_H = "#1D4ED8"
ERR_CLR  = "#DC2626"
OK_CLR   = "#16A34A"
OK_HV    = "#15803D"
WARN_CLR = "#D97706"
DEL_BG   = "#FEE2E2"
DEL_FG   = "#DC2626"
DEL_HV   = "#FECACA"
ACT_BG   = "#EFF6FF"
TEXT_D   = "#1E293B"
TEXT_M   = "#64748B"

# Mệnh giá tiền mặt phổ biến
QUICK_CASH = [10_000, 20_000, 50_000, 100_000, 200_000, 500_000]


def _fmt(amount: float) -> str:
    return f"{int(amount):,}".replace(",", ".") + " ₫"


def _init_tree_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Sales.Treeview",
        background=CARD, foreground=TEXT_D,
        rowheight=46, fieldbackground=CARD,
        font=("Arial", 12), borderwidth=0,
        relief="flat",
    )
    style.configure("Sales.Treeview.Heading",
        background=HDR_BG, foreground="#FFFFFF",
        font=("Arial", 12, "bold"),
        relief="flat", borderwidth=0,
        padding=(8, 10),
    )
    style.map("Sales.Treeview",
        background=[("selected", SEL_BG)],
        foreground=[("selected", TEXT_D)],
    )
    style.map("Sales.Treeview.Heading",
        background=[("active", "#243A5E")],
        relief=[("active", "flat")],
    )
    style.configure("Sales.Vertical.TScrollbar",
        background="#E2E8F0", troughcolor="#F1F5F9",
        arrowcolor="#94A3B8", relief="flat", borderwidth=0,
    )


class SalesView(ctk.CTkFrame):

    def __init__(self, parent, employee: dict, **kw):
        super().__init__(parent, fg_color=BG, corner_radius=0, **kw)
        self.employee = employee
        self._cart: list[dict] = []
        self._selected_idx: int | None = None

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        _init_tree_style()
        self._build_input_bar()
        self._build_table()
        self._build_footer()

        self.after(150, self.entry_barcode.focus_set)

    # ── Input bar ─────────────────────────────────────────────────────────────

    def _build_input_bar(self):
        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12,
                            border_width=1, border_color=BORDER)
        card.grid(row=0, column=0, sticky="ew", padx=20, pady=(16, 6))
        card.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(card, text="📷  Mã vạch",
                     font=("Arial", 13, "bold"), text_color=TEXT_D,
                     ).grid(row=0, column=0, padx=(20, 12), pady=(16, 0))

        self.entry_barcode = ctk.CTkEntry(
            card, placeholder_text="Nhập hoặc quét mã vạch rồi nhấn Enter...",
            height=44, font=("Arial", 14),
            border_color="#CBD5E1", fg_color="#F8FAFC", text_color=TEXT_D,
        )
        self.entry_barcode.grid(row=0, column=1, sticky="ew", pady=(16, 0))
        self.entry_barcode.bind("<Return>", self._on_add)

        ctk.CTkButton(
            card, text="＋  Thêm", width=120, height=44,
            font=("Arial", 13, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_H, corner_radius=8,
            command=self._on_add,
        ).grid(row=0, column=2, padx=(10, 20), pady=(16, 0))

        self.lbl_error = ctk.CTkLabel(
            card, text="", font=("Arial", 12),
            text_color=ERR_CLR, anchor="w",
        )
        self.lbl_error.grid(row=1, column=0, columnspan=3,
                            padx=20, pady=(4, 10), sticky="ew")

    # ── Bảng giỏ hàng (ttk.Treeview) ─────────────────────────────────────────

    def _build_table(self):
        outer = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12,
                             border_width=1, border_color=BORDER)
        outer.grid(row=1, column=0, sticky="nsew", padx=20, pady=4)
        outer.grid_rowconfigure(0, weight=1)
        outer.grid_columnconfigure(0, weight=1)

        # ── Treeview + scrollbar ──────────────────────────────────────────
        tree_frame = ctk.CTkFrame(outer, fg_color=CARD, corner_radius=0)
        tree_frame.grid(row=0, column=0, sticky="nsew")
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        cols = ("stt", "ma_sp", "ten_sp", "don_gia", "so_luong", "thanh_tien")
        self.tree = ttk.Treeview(tree_frame, style="Sales.Treeview",
                                  columns=cols, show="headings",
                                  selectmode="browse")

        # Cấu hình từng cột: (heading text, width, anchor, stretch)
        col_cfg = [
            ("stt",        "STT",            50,  "center", False),
            ("ma_sp",      "Mã SP",          96,  "center", False),
            ("ten_sp",     "Tên sản phẩm",    0,  "w",      True),
            ("don_gia",    "Đơn giá",        118, "e",      False),
            ("so_luong",   "Số lượng",        90, "center", False),
            ("thanh_tien", "Thành tiền",     128, "e",      False),
        ]
        for cid, label, width, anchor, stretch in col_cfg:
            self.tree.heading(cid, text=label, anchor=anchor)
            kw = {"anchor": anchor, "stretch": stretch}
            if stretch:
                kw["minwidth"] = 160
            else:
                kw["width"] = width
                kw["minwidth"] = width
            self.tree.column(cid, **kw)

        self.tree.tag_configure("odd",  background=ROW_ODD)
        self.tree.tag_configure("even", background=CARD)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical",
                             command=self.tree.yview,
                             style="Sales.Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        self.tree.bind("<<TreeviewSelect>>", self._on_row_select)

        # Placeholder khi giỏ rỗng — đặt đè lên treeview bằng place
        self.lbl_empty = ctk.CTkLabel(
            tree_frame,
            text="🛒   Giỏ hàng trống — quét mã vạch để thêm sản phẩm",
            font=("Arial", 13), text_color=TEXT_M, fg_color=CARD,
        )
        self.lbl_empty.place(relx=0.5, rely=0.5, anchor="center")

        # ── Action bar (hiện khi chọn dòng) ──────────────────────────────
        self._build_action_bar(outer)

    def _build_action_bar(self, outer):
        sep = ctk.CTkFrame(outer, fg_color=BORDER, height=1)
        sep.grid(row=1, column=0, sticky="ew")

        self.action_bar = ctk.CTkFrame(outer, fg_color=ACT_BG,
                                       corner_radius=0, height=52)
        self.action_bar.grid(row=2, column=0, sticky="ew")
        self.action_bar.grid_propagate(False)
        self.action_bar.grid_columnconfigure(1, weight=1)
        self.action_bar.grid_remove()   # ẩn ban đầu

        # Tên sản phẩm đang chọn
        self.lbl_sel = ctk.CTkLabel(
            self.action_bar, text="",
            font=("Arial", 12, "bold"), text_color=TEXT_D, anchor="w",
        )
        self.lbl_sel.grid(row=0, column=0, padx=(16, 8), sticky="w")

        # Nút − / số lượng / nút +
        qty_box = ctk.CTkFrame(self.action_bar, fg_color="transparent")
        qty_box.grid(row=0, column=1)

        ctk.CTkButton(
            qty_box, text="−", width=36, height=36,
            font=("Arial", 20, "bold"),
            fg_color="#E2E8F0", hover_color="#CBD5E1",
            text_color=TEXT_D, corner_radius=8,
            command=self._dec_qty,
        ).pack(side="left", padx=3)

        self.lbl_sel_qty = ctk.CTkLabel(
            qty_box, text="1", width=48,
            font=("Arial", 16, "bold"), text_color=ACCENT,
        )
        self.lbl_sel_qty.pack(side="left")

        ctk.CTkButton(
            qty_box, text="+", width=36, height=36,
            font=("Arial", 20, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_H,
            text_color="#FFFFFF", corner_radius=8,
            command=self._inc_qty,
        ).pack(side="left", padx=3)

        # Nút xóa dòng
        ctk.CTkButton(
            self.action_bar, text="✕  Xóa dòng",
            width=112, height=36,
            font=("Arial", 12, "bold"),
            fg_color=DEL_BG, hover_color=DEL_HV,
            text_color=DEL_FG, corner_radius=8,
            command=self._del_selected,
        ).grid(row=0, column=2, padx=16)

    # ── Footer thanh toán ─────────────────────────────────────────────────────

    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12,
                              border_width=1, border_color=BORDER)
        footer.grid(row=2, column=0, sticky="ew", padx=20, pady=(4, 16))
        footer.grid_columnconfigure(1, weight=1)

        # ── Cột 0: đếm hàng + nhập tiền khách ────────────────────────────
        self.lbl_count = ctk.CTkLabel(
            footer, text="Giỏ hàng trống",
            font=("Arial", 12), text_color=TEXT_M,
        )
        self.lbl_count.grid(row=0, column=0, padx=24, pady=(14, 4), sticky="w")

        pay_left = ctk.CTkFrame(footer, fg_color="transparent")
        pay_left.grid(row=1, column=0, padx=20, pady=(0, 14), sticky="w")

        ctk.CTkLabel(pay_left, text="Tiền khách đưa:",
                     font=("Arial", 12, "bold"), text_color=TEXT_D,
                     ).grid(row=0, column=0, padx=(0, 8), sticky="w")

        self.entry_cash = ctk.CTkEntry(
            pay_left, width=150, height=38, font=("Arial", 13),
            placeholder_text="Nhập số tiền...",
            border_color="#CBD5E1", fg_color="#F8FAFC", text_color=TEXT_D,
        )
        self.entry_cash.grid(row=0, column=1)
        self.entry_cash.bind("<KeyRelease>", self._calc_change)
        self.entry_cash.bind("<Return>", self._on_checkout)

        # Mệnh giá nhanh
        quick = ctk.CTkFrame(pay_left, fg_color="transparent")
        quick.grid(row=1, column=0, columnspan=2, pady=(6, 0), sticky="w")

        for i, amount in enumerate(QUICK_CASH):
            label = f"{amount // 1000}K"
            ctk.CTkButton(
                quick, text=label, width=52, height=28,
                font=("Arial", 11, "bold"),
                fg_color="#EFF6FF", hover_color="#DBEAFE",
                text_color=ACCENT, corner_radius=6,
                border_width=1, border_color="#BFDBFE",
                command=lambda a=amount: self._set_cash(a),
            ).grid(row=0, column=i, padx=(0, 4))

        # ── Cột 1: TỔNG TIỀN + tiền thối ─────────────────────────────────
        right_info = ctk.CTkFrame(footer, fg_color="transparent")
        right_info.grid(row=0, column=1, rowspan=2, sticky="e", padx=8, pady=12)

        total_row = ctk.CTkFrame(right_info, fg_color="transparent")
        total_row.pack(anchor="e")
        ctk.CTkLabel(total_row, text="TỔNG TIỀN:",
                     font=("Arial", 14, "bold"), text_color=TEXT_M,
                     ).pack(side="left", padx=(0, 12))
        self.lbl_total = ctk.CTkLabel(total_row, text="0 ₫",
                                       font=("Arial", 28, "bold"), text_color=ACCENT)
        self.lbl_total.pack(side="left")

        change_row = ctk.CTkFrame(right_info, fg_color="transparent")
        change_row.pack(anchor="e", pady=(8, 0))
        ctk.CTkLabel(change_row, text="Tiền thối:",
                     font=("Arial", 12, "bold"), text_color=TEXT_M,
                     ).pack(side="left", padx=(0, 8))
        self.lbl_change = ctk.CTkLabel(change_row, text="—",
                                        font=("Arial", 20, "bold"), text_color=TEXT_M)
        self.lbl_change.pack(side="left")

        # ── Cột 2: nút THANH TOÁN ────────────────────────────────────────
        self.btn_checkout = ctk.CTkButton(
            footer, text="💳\nTHANH TOÁN",
            width=156, height=84,
            font=("Arial", 15, "bold"),
            fg_color=OK_CLR, hover_color=OK_HV, corner_radius=12,
            command=self._on_checkout,
        )
        self.btn_checkout.grid(row=0, column=2, rowspan=2, padx=20, pady=14)

    # ── Logic giỏ hàng ────────────────────────────────────────────────────────

    def _on_add(self, event=None):
        barcode = self.entry_barcode.get().strip()
        self.entry_barcode.delete(0, "end")
        self.after(10, self.entry_barcode.focus_set)

        if not barcode:
            return

        product = find_by_barcode(barcode)
        if product is None:
            self._set_error("⚠   Không tìm thấy sản phẩm với mã vạch này.")
            return
        if product["so_luong_ton"] <= 0:
            self._set_error(f"⚠   Sản phẩm \"{product['ten_sp']}\" đã hết hàng trong kho.")
            return

        self._clear_error()
        self._add_to_cart(product)

    def _add_to_cart(self, product: dict):
        # Lấy % giảm giá hiện hành từ CSDL và tính lại giá
        discount_percent = get_active_discount()
        original_price = float(product["don_gia"])
        final_price = original_price * (1 - discount_percent / 100)
        
        ten_sp_hien_thi = product["ten_sp"] + (f" (-{discount_percent}%)" if discount_percent > 0 else "")

        for item in self._cart:
            if item["ma_sp"] == product["ma_sp"]:
                item["so_luong"] += 1
                item["thanh_tien"] = item["don_gia"] * item["so_luong"]
                self._refresh_tree()
                self._update_totals()
                return

        self._cart.append({
            "ma_sp":      product["ma_sp"],
            "ten_sp":     ten_sp_hien_thi,
            "don_gia":    final_price,
            "so_luong":   1,
            "thanh_tien": final_price,
        })
        self._refresh_tree()
        self._update_totals()

    def _refresh_tree(self):
        # Ghi nhớ selection để khôi phục sau khi rebuild
        sel = self.tree.selection()
        prev_idx = int(sel[0]) if sel else None

        for iid in self.tree.get_children():
            self.tree.delete(iid)

        for idx, item in enumerate(self._cart):
            self.tree.insert("", "end", iid=str(idx),
                             values=(
                                 idx + 1,
                                 item["ma_sp"],
                                 item["ten_sp"],
                                 _fmt(item["don_gia"]),
                                 item["so_luong"],
                                 _fmt(item["thanh_tien"]),
                             ),
                             tags=("odd" if idx % 2 == 0 else "even",))

        if self._cart:
            self.lbl_empty.place_forget()
        else:
            self.lbl_empty.place(relx=0.5, rely=0.5, anchor="center")

        # Khôi phục selection → tự động trigger _on_row_select
        if prev_idx is not None and prev_idx < len(self._cart):
            self.tree.selection_set(str(prev_idx))

    def _on_row_select(self, event=None):
        sel = self.tree.selection()
        if not sel:
            self._selected_idx = None
            self.action_bar.grid_remove()
            return

        idx = int(sel[0])
        self._selected_idx = idx
        item = self._cart[idx]
        self.lbl_sel.configure(text=f"✏  {item['ten_sp']}")
        self.lbl_sel_qty.configure(text=str(item["so_luong"]))
        self.action_bar.grid()

    # ── Điều chỉnh số lượng ───────────────────────────────────────────────────

    def _inc_qty(self):
        if self._selected_idx is None:
            return
        item = self._cart[self._selected_idx]
        item["so_luong"] += 1
        item["thanh_tien"] = item["don_gia"] * item["so_luong"]
        self._refresh_tree()
        self._update_totals()

    def _dec_qty(self):
        if self._selected_idx is None:
            return
        item = self._cart[self._selected_idx]
        if item["so_luong"] > 1:
            item["so_luong"] -= 1
            item["thanh_tien"] = item["don_gia"] * item["so_luong"]
            self._refresh_tree()
            self._update_totals()
        else:
            self._del_selected()

    def _del_selected(self):
        if self._selected_idx is None:
            return
        del self._cart[self._selected_idx]
        self._selected_idx = None
        self.action_bar.grid_remove()
        self._refresh_tree()
        self._update_totals()

    def _update_totals(self):
        total   = sum(i["thanh_tien"] for i in self._cart)
        n_lines = len(self._cart)
        n_items = sum(i["so_luong"]   for i in self._cart)
        self.lbl_total.configure(text=_fmt(total))
        self.lbl_count.configure(
            text=f"{n_lines} mặt hàng  ·  {n_items} sản phẩm"
            if n_lines else "Giỏ hàng trống"
        )
        self._calc_change()

    # ── Logic thanh toán ──────────────────────────────────────────────────────

    def _set_cash(self, amount: int):
        self.entry_cash.delete(0, "end")
        self.entry_cash.insert(0, str(amount))
        self._calc_change()

    def _calc_change(self, event=None):
        tong_tien = sum(i["thanh_tien"] for i in self._cart)
        try:
            raw = self.entry_cash.get().replace(".", "").replace(",", "").strip()
            tien_khach = float(raw) if raw else 0.0
        except ValueError:
            self.lbl_change.configure(text="—", text_color=TEXT_M)
            return

        if tien_khach == 0:
            self.lbl_change.configure(text="—", text_color=TEXT_M)
            return

        change = tien_khach - tong_tien
        if change < 0:
            self.lbl_change.configure(text=f"Thiếu {_fmt(-change)}", text_color=WARN_CLR)
        else:
            self.lbl_change.configure(text=_fmt(change), text_color=OK_CLR)

    def _on_checkout(self, event=None):
        self._clear_error()

        if not self._cart:
            self._set_error("⚠   Giỏ hàng đang trống, vui lòng thêm sản phẩm.")
            return

        tong_tien = sum(i["thanh_tien"] for i in self._cart)

        try:
            raw = self.entry_cash.get().replace(".", "").replace(",", "").strip()
            tien_khach = float(raw) if raw else 0.0
        except ValueError:
            tien_khach = 0.0

        if tien_khach < tong_tien:
            self._set_error(
                f"⚠   Tiền khách ({_fmt(tien_khach)}) không đủ so với tổng tiền ({_fmt(tong_tien)})."
            )
            self.entry_cash.focus_set()
            return

        self.btn_checkout.configure(state="disabled", text="⏳\nĐang xử lý...")
        self.update()

        success, message, ma_hd = create_invoice(
            ma_nv=self.employee["ma_nv"],
            cart=self._cart.copy(),
            tong_tien=tong_tien,
        )

        self.btn_checkout.configure(state="normal", text="💳\nTHANH TOÁN")

        if success:
            self._show_success_dialog(ma_hd, tong_tien, tien_khach,
                                      tien_khach - tong_tien)
            self._reset_cart()
        else:
            self._set_error(f"⚠   {message}")

    def _reset_cart(self):
        self._cart.clear()
        self._selected_idx = None
        self.action_bar.grid_remove()
        self._refresh_tree()
        self._update_totals()
        self.entry_cash.delete(0, "end")
        self.lbl_change.configure(text="—", text_color=TEXT_M)
        self.entry_barcode.delete(0, "end")
        self.after(50, self.entry_barcode.focus_set)

    # ── Dialog thành công ─────────────────────────────────────────────────────

    def _show_success_dialog(self, ma_hd: str, tong_tien: float,
                             tien_khach: float, tien_thoi: float):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Thanh toán thành công")
        dlg.resizable(False, False)
        dlg.grab_set()
        dlg.focus_set()

        dlg.update_idletasks()
        W, H = 420, 390
        sw, sh = dlg.winfo_screenwidth(), dlg.winfo_screenheight()
        dlg.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")

        dlg.grid_columnconfigure(0, weight=1)
        dlg.grid_rowconfigure(3, weight=1)  # detail frame co giãn

        ctk.CTkLabel(dlg, text="✅",
                     font=("Segoe UI Emoji", 48),
                     ).grid(row=0, pady=(24, 6))

        ctk.CTkLabel(dlg, text="Thanh toán thành công!",
                     font=("Arial", 20, "bold"), text_color=OK_CLR,
                     ).grid(row=1)

        ctk.CTkLabel(dlg, text=f"Mã hóa đơn:  {ma_hd}",
                     font=("Arial", 12), text_color=TEXT_M,
                     ).grid(row=2, pady=(6, 0))

        # Chi tiết
        detail = ctk.CTkFrame(dlg, fg_color="#F0FDF4", corner_radius=10,
                              border_width=1, border_color="#BBF7D0")
        detail.grid(row=3, padx=30, pady=14, sticky="nsew")
        detail.grid_columnconfigure(1, weight=1)
        detail.grid_rowconfigure((0, 1, 2), weight=1)

        rows_data = [
            ("Tổng tiền",  _fmt(tong_tien), TEXT_D),
            ("Tiền khách", _fmt(tien_khach), TEXT_D),
            ("Tiền thối",  _fmt(tien_thoi),  OK_CLR),
        ]
        for i, (label, value, color) in enumerate(rows_data):
            ctk.CTkLabel(detail, text=label, font=("Arial", 12),
                         text_color=TEXT_M, anchor="w",
                         ).grid(row=i, column=0, padx=20, pady=8, sticky="w")
            ctk.CTkLabel(detail, text=value, font=("Arial", 13, "bold"),
                         text_color=color, anchor="e",
                         ).grid(row=i, column=1, padx=20, pady=8, sticky="e")

        ctk.CTkButton(
            dlg, text="OK  —  Khách hàng tiếp theo",
            height=48, font=("Arial", 13, "bold"),
            fg_color=OK_CLR, hover_color=OK_HV, corner_radius=10,
            command=dlg.destroy,
        ).grid(row=4, padx=30, pady=(0, 24), sticky="ew")

    # ── Tiện ích ──────────────────────────────────────────────────────────────

    def _set_error(self, msg: str):
        self.lbl_error.configure(text=msg)

    def _clear_error(self):
        self.lbl_error.configure(text="")
