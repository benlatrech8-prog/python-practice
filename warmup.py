import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()
mo=int(input("items more than: "))
cur.execute("SELECT name, quantity FROM products WHERE quantity >?",(mo,))

rows=cur.fetchall()
for name, quantity in rows:
    print(f"{name} ({quantity})")
conn.close()
