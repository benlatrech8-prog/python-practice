import sqlite3

class SalonDB:
    def __init__(self, db_file):
        self.conn=sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS bookings(
                id INTEGER PRIMARY KEY,
                name TEXT,
                service TEXT,
                price INTEGER
            )
        """)
        self.conn.commit()

    def add(self, name, service, price):
        cur= self.conn.cursor()
        cur.execute("""
            INSERT INTO bookings
            (name, service , price)
            VALUES (?,?,?)""",
            (name, service, price)
        )
        self.conn.commit()
    def close(self):
        self.conn.close()

    def total(self):
        cur= self.conn.cursor()
        cur.execute("""
            SELECT SUM(price) FROM bookings;
            """)
        row = cur.fetchone()
        if row[0] is None:
            return 0
        return row[0]

if __name__ == "__main__":
    salon=SalonDB("salon2.db")
    print(salon.total())
    salon.add("Ali", "haircut", 15)
    salon.add("Sara", "wash", 5)
    print(salon.total())
    salon.close()
    print("OK")
