import sqlite3
from utils.memory import get_user_preferences


def recommend_content(user_id, user_db="data/users.db", product_db="data/products.db"):
    print(f"[Content] Generating recommendations for User {user_id}")
    prefs = get_user_preferences(user_id, db_path=user_db)
    if not prefs:
        return []

    conn = sqlite3.connect(product_db)
    cur = conn.cursor()
    placeholder = ','.join('?' for _ in prefs)
    query = f"SELECT product_id FROM products WHERE category IN ({placeholder}) ORDER BY probability DESC LIMIT 5"
    cur.execute(query, prefs)
    return [row[0] for row in cur.fetchall()]
