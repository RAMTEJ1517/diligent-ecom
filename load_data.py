import pandas as pd
import sqlite3
import os

DB_NAME = "ecommerce.db"
DATA_DIR = "data"

tables = {
    "users": "users.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "reviews": "reviews.csv",
}

conn = sqlite3.connect(DB_NAME)

for table, filename in tables.items():
    path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Loaded {table} from {filename}")

conn.close()
print("Database created successfully: ecommerce.db")
