from app.database import get_connection

def get_supplier_columns():
    """Tự động đọc danh sách tất cả các cột của bảng NhaCungCap từ SQL"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 0 * FROM NhaCungCap")
    cols = [column[0] for column in cursor.description]
    cursor.close()
    return cols

def get_suppliers(search=""):
    conn = get_connection()
    cursor = conn.cursor()
    cols = get_supplier_columns()
    
    query = "SELECT * FROM NhaCungCap"
    conditions = []
    
    params = []
    if search:
        search_conds = []
        # Tự động tìm kiếm trên tất cả các cột có khả năng chứa chuỗi
        for c in cols:
            if c.lower() in ('tenncc', 'sodienthoai', 'email', 'diachi', 'mancc', 'nguoilienhe', 'masothue'):
                search_conds.append(f"{c} LIKE ?")
                params.append(f"%{search}%")
        if search_conds:
            conditions.append(f"({' OR '.join(search_conds)})")
            
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
        
    pk_col = 'MaNCC' if 'MaNCC' in cols else cols[0]
    query += f" ORDER BY {pk_col} DESC"
    
    cursor.execute(query, params)
    res = [dict(zip(cols, row)) for row in cursor.fetchall()]
    cursor.close()
    return res

def add_supplier(data):
    """Tự động INSERT dựa trên các Text Box đã điền"""
    conn = get_connection()
    cursor = conn.cursor()
    cols = get_supplier_columns()
    
    insert_cols = []
    insert_vals = []
    
    for k, v in data.items():
        if k in cols and v != "":
            insert_cols.append(k)
            insert_vals.append(v)
            
    if 'TrangThai' in cols and 'TrangThai' not in data:
        insert_cols.append('TrangThai')
        insert_vals.append(1)
        
    placeholders = ['?'] * len(insert_cols)
    query = f"INSERT INTO NhaCungCap ({', '.join(insert_cols)}) VALUES ({', '.join(placeholders)})"
    
    try:
        cursor.execute(query, tuple(insert_vals))
        conn.commit()
        return True, ""
    except Exception as e:
        # Trả về lỗi SQL để View hiển thị lên MessageBox
        return False, str(e)
    finally:
        cursor.close()

def update_supplier(pk_val, data):
    conn = get_connection()
    cursor = conn.cursor()
    cols = get_supplier_columns()
    pk_col = 'MaNCC' if 'MaNCC' in cols else cols[0]
    
    update_cols = []
    update_vals = []
    
    for k, v in data.items():
        if k in cols and k != pk_col:
            update_cols.append(f"{k} = ?")
            update_vals.append(v)
            
    if not update_cols:
        return False, "Không có dữ liệu mới để cập nhật"
        
    update_vals.append(pk_val)
    query = f"UPDATE NhaCungCap SET {', '.join(update_cols)} WHERE {pk_col} = ?"
    
    try:
        cursor.execute(query, tuple(update_vals))
        conn.commit()
        return True, ""
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()

def disable_supplier(pk_val):
    conn = get_connection()
    cursor = conn.cursor()
    cols = get_supplier_columns()
    pk_col = 'MaNCC' if 'MaNCC' in cols else cols[0]
    try:
        cursor.execute(f"DELETE FROM NhaCungCap WHERE {pk_col}=?", (pk_val,))
        conn.commit()
        return True, ""
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()