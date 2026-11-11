import sqlite3

class ShopDB():
    def __init__(self,db_file):
        self.conn=sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT
            )
             """)
        cur.execute("""CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY,
            customer_id INTEGER ,
            product TEXT,
            price INTEGER
            )
             """)
        self.conn.commit()
    def add_order(self, customer_id, product, price):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO orders (customer_id, product, price) VALUES  (?,?,?)",(customer_id, product, price))
        self.conn.commit()

    def add_customer(self, name, city):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO customers (name, city) VALUES  (?,?)",(name, city))
        self.conn.commit()

    def orders_of(self, name):
        cur = self.conn.cursor()
        cur.execute("""SELECT customers.name, orders.product, orders.price
        FROM customers JOIN orders
        ON orders.customer_id = customers.id  WHERE customers.name = (?)""",(name,))
        rows=cur.fetchall()
        result = []
        for name, product,price in rows:
            result.append(f"{name} bought {product} for {price}")
        return result
    def close(self):
        self.conn.close()
if __name__ == "__main__":
    shop = ShopDB(':memory:')
    shop.add_customer("Ali", "wurzburg")
    shop.add_customer("Mays", "berlin")
    shop.add_order(1,"phone",300)
    shop.add_order(1,"laptop",500)
    shop.add_order(2,"PS5",450)
    print(shop.orders_of("Ali"))
#    print(shop.orders_of("Mays"))

    print(shop.conn.execute("SELECT * FROM customers").fetchall())
    shop.close()

