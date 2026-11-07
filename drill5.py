import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

product_id=int(input("Enter the id of the item you want to delete it: "))

cur.execute(
    "DELETE FROM products WHERE id = ?",
    (product_id,)
    )
conn.commit()

conn.close()

print("Deleted row number",product_id)
