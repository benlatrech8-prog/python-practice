import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM products")
row = cur.fetchone()
count=row[0]

cur.execute("SELECT SUM(price*quantity) FROM products")
row1 = cur.fetchone()
sum=row1[0]

print(f"products: {count} \nstock values : {sum} euro")

conn.close()
