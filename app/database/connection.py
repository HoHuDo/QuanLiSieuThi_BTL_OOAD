import pyodbc
from config import DB_CONFIG


_connection = None


def get_connection() -> pyodbc.Connection:
    """Trả về connection đã có hoặc tạo mới (singleton)."""
    global _connection
    if _connection is None or _connection.closed:
        _connection = _create_connection()
    return _connection


def _create_connection() -> pyodbc.Connection:
    cfg = DB_CONFIG
    if cfg.get("trusted_connection"):
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={cfg['server']};"
            f"DATABASE={cfg['database']};"
            "Trusted_Connection=yes;"
        )
    else:
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={cfg['server']};"
            f"DATABASE={cfg['database']};"
            f"UID={cfg['username']};"
            f"PWD={cfg['password']};"
        )
    return pyodbc.connect(conn_str, autocommit=False)


def close_connection():
    """Đóng connection khi thoát ứng dụng."""
    global _connection
    if _connection and not _connection.closed:
        _connection.close()
        _connection = None


def test_connection() -> tuple[bool, str]:
    """
    Kiểm tra kết nối đến SQL Server.
    Trả về (True, thông báo) nếu thành công, (False, lỗi) nếu thất bại.
    """
    try:
        conn = _create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DB_NAME() AS db, @@VERSION AS ver")
        row = cursor.fetchone()
        msg = (
            f"Kết nối thành công!\n"
            f"  Database : {row.db}\n"
            f"  SQL Server: {row.ver.splitlines()[0]}"
        )
        cursor.close()
        conn.close()
        return True, msg
    except pyodbc.Error as e:
        return False, f"Kết nối thất bại: {e}"
