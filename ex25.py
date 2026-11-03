import json
from ex12 import daily_total
with open("bookings.json", "r") as f:
        bookings= json.load(f)

print(bookings)
print(type(bookings))
print(bookings[0]["name"])
print(daily_total(bookings))
