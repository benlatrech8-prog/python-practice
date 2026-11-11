import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute("""
    SELECT customers.name ,SUM(orders.price) AS total
    FROM orders JOIN customers
    ON customers.id = orders.customer_id
    GROUP BY customers.name
    ORDER BY total DESC

""")
rows = cur.fetchall()

for name, total in rows:
    print(f"{name} spent {total} euro")

conn.close()
