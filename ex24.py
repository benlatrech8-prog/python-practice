import json
bookings= [
	{"name": "Ali", "service": "haircut", "price": 15},
	{"name": "Sara", "service": "wash", "price": 5},
]

with open("bookings.json","w") as f:
	json.dump(bookings, f, indent=2)

print("saved!")

