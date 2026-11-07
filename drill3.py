import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute(
    "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
    ("shoes", 50, 4)
)
cur.execute(
    "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
    ("cap", 15, 10)
)
cur.execute(
    "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
    ("socks", 5, 20)
)
conn.commit()

conn.close()
