import sqlite3

def recommend_collaborative(user_id, db_path="data/users.db"):
    print(f"[Collaborative] Generating recommendations for User {user_id}")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT segment FROM users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    if not result:
        return []

    segment = result[0]
    if segment == "High Value":
        return ["P101", "P102", "P103"]
    elif segment == "Budget Buyer":
        return ["P201", "P202"]
    else:
        return ["P301"]
