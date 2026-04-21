import customtkinter as ctk
from app.controllers.account_controller import authenticate


# ── Màu sắc ──────────────────────────────────────────────────────────────────
BG_LEFT   = "#1B2A4A"   # xanh navy đậm – panel trái
BG_RIGHT  = "#F0F4FF"   # xanh nhạt – panel phải
CARD_BG   = "#FFFFFF"
ACCENT    = "#2563EB"   # xanh dương chủ đạo
ACCENT_HV = "#1D4ED8"   # hover
ERR_COLOR = "#DC2626"   # đỏ lỗi
OK_COLOR  = "#16A34A"   # xanh thành công
TEXT_DRK  = "#1E293B"
TEXT_MID  = "#64748B"


class LoginView(ctk.CTk):
    def __init__(self, on_success=None):
        super().__init__()
        self.on_success = on_success   # callback(employee_info) khi đăng nhập OK

        self.title("Đăng nhập – Quản Lý Siêu Thị Mini")
        self.geometry("860x520")
        self.minsize(720, 460)
        self.resizable(True, True)
        self._center_window(860, 520)

        self._build_ui()

    # ── Layout ────────────────────────────────────────────────────────────────

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self._build_left_panel()
        self._build_right_panel()

    def _build_left_panel(self):
        left = ctk.CTkFrame(self, fg_color=BG_LEFT, corner_radius=0)
        left.grid(row=0, column=0, sticky="nsew")
        # Một row duy nhất chiếm toàn bộ chiều cao → inner frame sẽ tự căn giữa
        left.grid_rowconfigure(0, weight=1)
        left.grid_columnconfigure(0, weight=1)

        # Frame con chứa logo + text, căn giữa hoàn toàn
        inner = ctk.CTkFrame(left, fg_color="transparent")
        inner.grid(row=0, column=0)

        ctk.CTkLabel(
            inner, text="🛒", font=("Segoe UI Emoji", 56),
            text_color="#FFFFFF", fg_color="transparent",
        ).pack(pady=(0, 8))

        ctk.CTkLabel(
            inner, text="MiniSupermart",
            font=("Arial", 22, "bold"), text_color="#FFFFFF",
        ).pack()

        ctk.CTkLabel(
            inner, text="Hệ thống quản lý\nsiêu thị mini",
            font=("Arial", 12), text_color="#93C5FD",
            justify="center",
        ).pack(pady=(6, 0))

    def _build_right_panel(self):
        right = ctk.CTkFrame(self, fg_color=BG_RIGHT, corner_radius=0)
        right.grid(row=0, column=1, sticky="nsew")
        right.grid_columnconfigure(0, weight=1)
        right.grid_rowconfigure(0, weight=1)

        # Card trắng giữa panel
        card = ctk.CTkFrame(
            right, fg_color=CARD_BG, corner_radius=16,
            border_width=1, border_color="#E2E8F0",
        )
        card.grid(row=0, padx=50, pady=50, sticky="nsew")
        card.grid_columnconfigure(0, weight=1)

        # Tiêu đề
        ctk.CTkLabel(
            card, text="Chào mừng trở lại",
            font=("Arial", 20, "bold"), text_color=TEXT_DRK,
        ).grid(row=0, padx=36, pady=(36, 4), sticky="w")

        ctk.CTkLabel(
            card, text="Vui lòng đăng nhập để tiếp tục",
            font=("Arial", 12), text_color=TEXT_MID,
        ).grid(row=1, padx=36, sticky="w")

        # Tên đăng nhập
        ctk.CTkLabel(
            card, text="Tên đăng nhập",
            font=("Arial", 13, "bold"), text_color=TEXT_DRK,
        ).grid(row=2, padx=36, pady=(28, 4), sticky="w")

        self.entry_username = ctk.CTkEntry(
            card, placeholder_text="Nhập tên đăng nhập...",
            height=42, font=("Arial", 13),
            border_color="#CBD5E1", fg_color="#F8FAFC",
            text_color=TEXT_DRK,
        )
        self.entry_username.grid(row=3, padx=36, sticky="ew")
        self.entry_username.bind("<Return>", lambda e: self.entry_password.focus())

        # Mật khẩu
        ctk.CTkLabel(
            card, text="Mật khẩu",
            font=("Arial", 13, "bold"), text_color=TEXT_DRK,
        ).grid(row=4, padx=36, pady=(16, 4), sticky="w")

        pw_frame = ctk.CTkFrame(card, fg_color="transparent")
        pw_frame.grid(row=5, padx=36, sticky="ew")
        pw_frame.grid_columnconfigure(0, weight=1)

        self.entry_password = ctk.CTkEntry(
            pw_frame, placeholder_text="Nhập mật khẩu...",
            height=42, font=("Arial", 13), show="●",
            border_color="#CBD5E1", fg_color="#F8FAFC",
            text_color=TEXT_DRK,
        )
        self.entry_password.grid(row=0, column=0, sticky="ew")
        self.entry_password.bind("<Return>", lambda e: self._on_login())

        self._pw_visible = False
        self.btn_eye = ctk.CTkButton(
            pw_frame, text="👁", width=42, height=42,
            fg_color="#E2E8F0", hover_color="#CBD5E1",
            text_color=TEXT_DRK, corner_radius=8,
            command=self._toggle_password,
        )
        self.btn_eye.grid(row=0, column=1, padx=(6, 0))

        # Thông báo lỗi / thành công
        self.lbl_msg = ctk.CTkLabel(
            card, text="", font=("Arial", 12),
            text_color=ERR_COLOR, wraplength=320,
        )
        self.lbl_msg.grid(row=6, padx=36, pady=(10, 0), sticky="w")

        # Nút đăng nhập
        self.btn_login = ctk.CTkButton(
            card, text="Đăng nhập",
            height=44, font=("Arial", 14, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_HV,
            corner_radius=10,
            command=self._on_login,
        )
        self.btn_login.grid(row=7, padx=36, pady=(14, 36), sticky="ew")

    # ── Xử lý sự kiện ─────────────────────────────────────────────────────────

    def _on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.btn_login.configure(state="disabled", text="Đang xác thực...")
        self.update()

        success, message, employee = authenticate(username, password)

        if success:
            self.lbl_msg.configure(text=message, text_color=OK_COLOR)
            print(f"[LOGIN] Đăng nhập thành công – {employee}")
            self.after(800, lambda: self._on_login_success(employee))
        else:
            self.lbl_msg.configure(text=message, text_color=ERR_COLOR)
            self.entry_password.delete(0, "end")
            self.entry_password.focus()
            self.btn_login.configure(state="normal", text="Đăng nhập")

    def _on_login_success(self, employee: dict):
        if self.on_success:
            self.on_success(employee)
        self.destroy()

    def _toggle_password(self):
        self._pw_visible = not self._pw_visible
        self.entry_password.configure(show="" if self._pw_visible else "●")
        self.btn_eye.configure(text="🙈" if self._pw_visible else "👁")

    # ── Tiện ích ──────────────────────────────────────────────────────────────

    def _center_window(self, w: int, h: int):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")
