def daily_total(bookings):

	s=0
	for d in bookings:
		s+=d["price"]
	return s
if __name__== "__main__":


	bookings=[
		{"name":"Ali","service":"haircut","price":15},
		{"name":"Sara","service":"wash","price":5},
		{"name":"Omar","service":"haircut","price":15},
		{"name":"Lina","service":"beard","price":10},
	]
	print(daily_total(bookings))
	print(bookings[0])
	print(bookings[0]["price"])

