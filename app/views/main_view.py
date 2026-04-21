import customtkinter as ctk
from config import APP_TITLE, APP_GEOMETRY
from app.views.components.sidebar import Sidebar
from app.views.sales_view import SalesView
from app.views.inventory_view import InventoryView
from app.views.customer_view import CustomerView
from app.views.employee_view import EmployeeView
from app.views.import_view import ImportView
from app.views.report_view import ReportView
from app.views.promotion_view import PromotionView

# Registry: key → View class (thêm vào đây khi làm xong từng module)
MODULE_VIEWS: dict = {
    "sales": SalesView,
    "inventory": InventoryView,
    "customers": CustomerView,
    "employees": EmployeeView,
    "imports": ImportView,
    "reports": ReportView,
    "promotions": PromotionView,
}

class MainView(ctk.CTk):
    def __init__(self, employee: dict, on_logout: callable, **kwargs):
        super().__init__(**kwargs)
        self.employee = employee
        self.on_logout = on_logout

        self.title(APP_TITLE)
        self.geometry(APP_GEOMETRY)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # 1. Sidebar bên trái
        self.sidebar = Sidebar(
            self,
            employee=self.employee,
            on_navigate=self.switch_module,
            on_logout=self._handle_logout
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # 2. Main content area bên phải
        self.main_content = ctk.CTkFrame(self, fg_color="#F0F4FF", corner_radius=0)
        self.main_content.grid(row=0, column=1, sticky="nsew")
        self.main_content.grid_rowconfigure(0, weight=1)
        self.main_content.grid_columnconfigure(0, weight=1)

        self.current_view = None

        # Load mặc định màn hình Bán hàng khi đăng nhập
        self.switch_module("sales")

    def switch_module(self, module_id: str):
        if self.current_view is not None:
            self.current_view.destroy()

        view_class = MODULE_VIEWS.get(module_id)
        if view_class:
            self.current_view = view_class(self.main_content, employee=self.employee)
            self.current_view.grid(row=0, column=0, sticky="nsew")
        else:
            # Fallback nếu module chưa được xây dựng
            self.current_view = ctk.CTkFrame(self.main_content, fg_color="#F0F4FF")
            self.current_view.grid(row=0, column=0, sticky="nsew")
            ctk.CTkLabel(
                self.current_view,
                text="🛠 Tính năng đang được phát triển...",
                font=("Arial", 20, "bold"), text_color="#64748B"
            ).place(relx=0.5, rely=0.5, anchor="center")

    def _handle_logout(self):
        self.destroy()
        self.on_logout()
