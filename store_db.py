import sqlite3

class StoreDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()
    def close(self):
        self.conn.close()

    def create_table(self):
        cur = self.conn.cursor()
        t="""CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER)"""
        cur.execute(t)
        self.conn.commit()
    def add(self, name, price, quantity):
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO products (name, price, quantity)
             VALUES (?,?,?) """,
            (name, price, quantity)
             )
        self.conn.commit()

    def show_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT name, price, quantity FROM products")
        pro=[]
        rows=cur.fetchall()
        for name, price, quantity in rows:
            pro.append(f"{name}: {price} euro ({quantity} left)")
        return pro

    def stock_value(self):
        cur= self.conn.cursor()
        cur.execute("SELECT SUM(price*quantity) FROM products ")
        row=cur.fetchone()
        if row[0] is None:
            return 0
        else:
            return row[0]

    def update_quantity(self):
        cur = self.conn.cursor()
        n=input("Enter the name of product: ")
        q=int(input("Enter new quantity: "))
        cur.execute("""
            UPDATE products SET
             quantity = ?
              WHERE name =?
         """,(q,n))
        self.conn.commit()
if __name__== "__main__":
    store = StoreDB(":memory:")
    print("connected")
    print(store.stock_value())
    store.add("wallet", 5, 20)
    store.add("backbag", 25, 15)
    print("Added")
    print(store.show_all())
    print(store.stock_value())
    print(store.update_quantity())
    print(store.show_all())

    store.close()
