import customtkinter as ctk
from app.database import close_connection
from app.views.login_view import LoginView
from app.views.main_view import MainView


def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    _run_app()


def _run_app():
    employee_ref: list[dict | None] = [None]

    # ── Bước 1: Đăng nhập ─────────────────────────────────────────────────
    login = LoginView(on_success=lambda emp: employee_ref.__setitem__(0, emp))
    login.protocol("WM_DELETE_WINDOW", lambda: (close_connection(), login.destroy()))
    login.mainloop()

    if employee_ref[0] is None:
        close_connection()
        return

    # ── Bước 2: Mở cửa sổ chính ───────────────────────────────────────────
    app = MainView(
        employee=employee_ref[0],
        on_logout=_run_app,      # đăng xuất → quay lại màn hình đăng nhập
    )
    app.protocol("WM_DELETE_WINDOW", lambda: (close_connection(), app.destroy()))
    app.mainloop()


if __name__ == "__main__":
    main()
