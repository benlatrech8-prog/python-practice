import sqlite3

conn = sqlite3.connect("salon.db")
cur = conn.cursor()

name=input("Name: ").strip()
service=input("Service: ").strip()
price=int(input("Price: "))

cur.execute(
    "INSERT INTO bookings (name, service, price) VALUES (?, ?, ?)", (name,service,price)
)
#conn.commit()


conn.close()
print("Added")
