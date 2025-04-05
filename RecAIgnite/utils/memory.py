import sqlite3

def get_user_preferences(user_id, db_path="data/users.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT preferences FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    return result[0].split(",") if result else []
