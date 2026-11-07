import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

p_name=input("Product name: ")
pnew_qnt=int(input("New quantity: "))

cur.execute(""" UPDATE products SET
    quantity = ?
    WHERE name = ?
    """,(pnew_qnt,p_name,)
    )

conn.commit()
print("updated")
conn.close()
