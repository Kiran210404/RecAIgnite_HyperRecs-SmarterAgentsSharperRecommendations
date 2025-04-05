# Directory: hyperrecs/scripts/populate_databases.py

import sqlite3
import pandas as pd

# --- USERS DB  ---
users_df = pd.read_csv("C:/Users/KIRAN_MANE/OneDrive/Desktop/AgenticAI/backend/GFG_Dataset/GFG_Dataset/customer_data_collection.csv")

conn_users = sqlite3.connect("data/users.db")
cur_users = conn_users.cursor()

cur_users.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        preferences TEXT,
        segment TEXT
    )
""")

for _, row in users_df.iterrows():
    user_id = row["Customer_ID"]
    # Combine browsing and purchase history into a preference string
    browsing = eval(row["Browsing_History"]) if pd.notna(row["Browsing_History"]) else []
    purchase = eval(row["Purchase_History"]) if pd.notna(row["Purchase_History"]) else []
    preferences = ",".join(browsing + purchase)
    segment = row["Customer_Segment"]
    cur_users.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?)", (user_id, preferences, segment))

conn_users.commit()
conn_users.close()


# --- PRODUCTS DB (Updated to match actual CSV columns) ---
products_df = pd.read_csv("C:/Users/KIRAN_MANE/OneDrive/Desktop/AgenticAI/backend/GFG_Dataset/GFG_Dataset/product_recommendation_data.csv")


conn_products = sqlite3.connect("data/products.db")
cur_products = conn_products.cursor()

cur_products.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id TEXT PRIMARY KEY,
        category TEXT,
        subcategory TEXT,
        probability REAL
    )
""")

for _, row in products_df.iterrows():
    product_id = row["Product_ID"]
    category = row["Category"]
    subcategory = row["Subcategory"]
    probability = row.get("Probability_of_Recommendation", 0.5)
    cur_products.execute("INSERT OR REPLACE INTO products VALUES (?, ?, ?, ?)",
                         (product_id, category, subcategory, probability))

conn_products.commit()
conn_products.close()
