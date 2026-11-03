def revenue_by_service(bookings):
	li={}
	for d  in bookings:
		service=d["service"]
		if d["service"] in li:
			li[service]+=d["price"]
		else:
			li[service]=d["price"]
	return li
bookings=[
	{"name":"Ali", "service":"haircut", "price":15},
	 {"name":"Sare", "service":"wash", "price":5},
	 {"name":"Omar", "service":"haircut", "price":15},
	 {"name":"Lina", "service":"beard", "price":10},
]

print(revenue_by_service(bookings))
