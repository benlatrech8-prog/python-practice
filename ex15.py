def uniq_services(bookings):
	uniser=[]
	for d in bookings:
		uniser.append(d["service"])
	return sorted(set(uniser))


def uniq_customer(bookings):
	unicus=[]
	s=0
	for d in bookings:
	        unicus.append(d["name"])
	for i in set(unicus):
		s+=1
	return s

def last_bookings(bookings,n):
        cus=[]
        for d in bookings:
                cus.append(d["name"])
        return cus[-n:]

bookings=[
	{"name":"Ali", "service":"haircut", "price":15},
	 {"name":"Sara", "service":"wash", "price":5},
	 {"name":"Omar", "service":"haircut", "price":15},
	 {"name":"Lina", "service":"beard", "price":10},
        {"name":"Ali", "service":"beard", "price":15},
]
print(uniq_services(bookings))
print(uniq_customer(bookings))
print(last_bookings(bookings,2))
print(last_bookings(bookings,3))

