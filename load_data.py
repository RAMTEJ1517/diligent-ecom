import sqlite3
import csv

# Create SQLite DB
conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cur.executescript(f.read())

print("Schema created successfully!")

# Function to load CSV into table
def load_csv(table, file):
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        cols = ", ".join(reader.fieldnames)
        placeholders = ", ".join("?" * len(reader.fieldnames))

        for row in reader:
            values = list(row.values())
            cur.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", values)

    print(f"{table} loaded.")

# Load each table
load_csv("users", "data/users.csv")
load_csv("products", "data/products.csv")
load_csv("orders", "data/orders.csv")
load_csv("order_items", "data/order_items.csv")
load_csv("reviews", "data/reviews.csv")

conn.commit()
conn.close()

print("All data loaded into ecom.db successfully!")
