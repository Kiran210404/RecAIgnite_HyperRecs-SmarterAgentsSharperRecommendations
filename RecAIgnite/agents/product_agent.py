import sqlite3

class ProductAgent:
    def __init__(self, db_path="data/products.db"):
        self.conn = sqlite3.connect(db_path)

    def get_top_products(self, limit=10):
        cur = self.conn.cursor()
        cur.execute("SELECT product_id, category, subcategory FROM products ORDER BY probability DESC LIMIT ?", (limit,))
        return cur.fetchall()

    def get_products_by_category(self, categories):
        cur = self.conn.cursor()
        placeholder = ','.join('?' for _ in categories)
        query = f"SELECT product_id FROM products WHERE category IN ({placeholder}) ORDER BY probability DESC"
        cur.execute(query, categories)
        return [row[0] for row in cur.fetchall()]
