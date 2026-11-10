import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

n=input("Enter the name: ")
cur.execute("""
    SELECT customers.name, orders.product, orders.price
    FROM orders JOIN customers ON
    orders.customer_id =customers.id
    WHERE customers.name = ?
    """,(n,))

rows=cur.fetchall()
if not rows:
        print(f"No orders found for {n}")
else:
    for name,product, price in rows:
        print(f"{name} bought {product} for {price} euro")


conn.close()
