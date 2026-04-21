import customtkinter as ctk

# ── Màu sắc (đồng bộ login) ───────────────────────────────────────────────────
SIDEBAR_BG  = "#1B2A4A"
NAV_ACTIVE  = "#2563EB"
NAV_HOVER   = "#243A5E"
TEXT_WHITE  = "#FFFFFF"
TEXT_MUTED  = "#93C5FD"
TEXT_DRK    = "#1E293B"
DIVIDER     = "#263A5C"
LOGOUT_BG   = "#7F1D1D"
LOGOUT_HV   = "#991B1B"

# ── Cấu hình menu ─────────────────────────────────────────────────────────────
MENU_CONFIG = [
    {"key": "sales",     "label": "Bán hàng",  "icon": "🛍️ "},
    {"key": "inventory", "label": "Kho hàng",  "icon": "📦 "},
    {"key": "imports",   "label": "Nhà cung cấp", "icon": "🏢 "},
    {"key": "customers", "label": "Khách hàng","icon": "👥 "},
    {"key": "employees", "label": "Nhân viên", "icon": "👤 "},
    {"key": "reports",   "label": "Báo cáo",   "icon": "📊 "},
    {"key": "promotions","label": "Khuyến mãi","icon": "🎟️ "},
]

# Mỗi vai trò thấy những tab nào
ROLE_MENUS: dict[str, list[str]] = {
    "Quản lý":       ["sales", "inventory", "imports", "customers", "employees", "reports", "promotions"],
    "Thu ngân":      ["sales", "customers"],
    "Nhân viên kho": ["inventory", "imports"],
}


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, employee: dict, on_navigate, on_logout, **kwargs):
        super().__init__(parent, fg_color=SIDEBAR_BG, corner_radius=0, width=240, **kwargs)
        self.employee   = employee
        self.on_navigate = on_navigate
        self.on_logout   = on_logout
        self._active_key = None
        self._nav_buttons: dict[str, ctk.CTkButton] = {}

        self.grid_propagate(False)
        self.grid_rowconfigure(1, weight=1)   # khu vực nav co giãn
        self.grid_columnconfigure(0, weight=1)

        self._build_logo()
        self._build_nav()
        self._build_user_panel()

    # ── Logo ──────────────────────────────────────────────────────────────────

    def _build_logo(self):
        logo_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        logo_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        logo_frame.grid_propagate(False)
        logo_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            logo_frame, text="🛒  MiniSupermart",
            font=("Arial", 16, "bold"), text_color=TEXT_WHITE,
            anchor="center",
        ).place(relx=0.5, rely=0.5, anchor="center")

        # Đường kẻ phân cách
        ctk.CTkFrame(self, fg_color=DIVIDER, height=1).grid(
            row=0, column=0, sticky="sew", padx=16,
        )

    # ── Nav buttons ───────────────────────────────────────────────────────────

    def _build_nav(self):
        nav = ctk.CTkFrame(self, fg_color="transparent")
        nav.grid(row=1, column=0, sticky="nsew", padx=0, pady=(16, 0))
        nav.grid_columnconfigure(0, weight=1)

        allowed = ROLE_MENUS.get(self.employee["vai_tro"], [])
        visible = [m for m in MENU_CONFIG if m["key"] in allowed]

        for i, item in enumerate(visible):
            btn = ctk.CTkButton(
                nav,
                text=f"  {item['icon']}  {item['label']}",
                font=("Arial", 14), anchor="w",
                height=48, corner_radius=10,
                fg_color="transparent",
                hover_color=NAV_HOVER,
                text_color=TEXT_WHITE,
                border_width=0,
                command=lambda k=item["key"]: self._click(k),
            )
            btn.grid(row=i, column=0, sticky="ew", padx=12, pady=3)
            self._nav_buttons[item["key"]] = btn

        # Kích hoạt tab đầu tiên mặc định
        if visible:
            self.set_active(visible[0]["key"])

    # ── User panel ────────────────────────────────────────────────────────────

    def _build_user_panel(self):
        # Đường kẻ phân cách
        ctk.CTkFrame(self, fg_color=DIVIDER, height=1).grid(
            row=2, column=0, sticky="ew", padx=16, pady=(0, 0),
        )

        panel = ctk.CTkFrame(self, fg_color="transparent")
        panel.grid(row=3, column=0, sticky="ew", padx=16, pady=14)
        panel.grid_columnconfigure(0, weight=1)

        # Avatar tròn (chữ cái đầu)
        initials = self.employee["ho_ten"][0].upper()
        av_frame = ctk.CTkFrame(panel, fg_color=NAV_ACTIVE, width=40, height=40, corner_radius=20)
        av_frame.grid(row=0, column=0, sticky="w")
        av_frame.grid_propagate(False)
        ctk.CTkLabel(av_frame, text=initials, font=("Arial", 16, "bold"),
                     text_color=TEXT_WHITE).place(relx=0.5, rely=0.5, anchor="center")

        # Tên & vai trò
        info = ctk.CTkFrame(panel, fg_color="transparent")
        info.grid(row=0, column=1, sticky="ew", padx=(10, 0))
        panel.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(info, text=self.employee["ho_ten"],
                     font=("Arial", 12, "bold"), text_color=TEXT_WHITE,
                     anchor="w", wraplength=150).pack(anchor="w")
        ctk.CTkLabel(info, text=self.employee["vai_tro"],
                     font=("Arial", 11), text_color=TEXT_MUTED,
                     anchor="w").pack(anchor="w")

        # Nút đăng xuất
        ctk.CTkButton(
            panel, text="⏻  Đăng xuất",
            font=("Arial", 12), height=34,
            fg_color=LOGOUT_BG, hover_color=LOGOUT_HV,
            text_color=TEXT_WHITE, corner_radius=8,
            command=self.on_logout,
        ).grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    # ── Public API ────────────────────────────────────────────────────────────

    def set_active(self, key: str):
        if self._active_key and self._active_key in self._nav_buttons:
            self._nav_buttons[self._active_key].configure(fg_color="transparent")
        self._active_key = key
        if key in self._nav_buttons:
            self._nav_buttons[key].configure(fg_color=NAV_ACTIVE)

    def _click(self, key: str):
        self.set_active(key)
        self.on_navigate(key)
