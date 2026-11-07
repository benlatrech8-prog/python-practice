import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute("SELECT name, price, quantity FROM products ")

rows=cur.fetchall()

for name, price, quantity in rows:
    print(f"{name}: {price} euro ({quantity} left)")

conn.close()

