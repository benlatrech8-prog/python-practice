import  sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute(
   """DELETE FROM products 
    WHERE rowid = 2"""
)

conn.commit()

conn.close()
