import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute("""
    SELECT customers.name ,SUM(orders.price) AS total
    FROM customers LEFT JOIN orders
    ON customers.id = orders.customer_id
    GROUP BY customers.name
    ORDER BY total

""")
rows = cur.fetchall()

for name, total in rows:
    if total is None:
        total = 0
    print(f"{name} spent {total} euro")

conn.close()


