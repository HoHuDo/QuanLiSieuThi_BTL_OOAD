"""Chạy file này để kiểm tra kết nối SQL Server trước khi chạy ứng dụng."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app.database import test_connection

if __name__ == "__main__":
    success, message = test_connection()
    print(message)
    sys.exit(0 if success else 1)
