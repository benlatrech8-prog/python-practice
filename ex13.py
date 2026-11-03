def get_names(bookings):
	names=[]
	for d in bookings:
		names.append(d["name"])

	return names
def total_for(bookings,service):
	sp=0
	for d in bookings:
		if d["service"]== service:
			sp+=d["price"]
	print("the total for  ",service,"is ")
	return sp
def costumer_of(bookings,service):
	names=[]
	for d in bookings:
		if d["service"]==service:
			names.append(d["name"])
	return names
def revenue_by_service(bookings):
	rev={}
	for d in bookings:
		service=d["service"]
		if service in rev:
			rev[service]+=d["price"]
		else:
			rev[service]=d["price"]
	return rev
bookings=[
        {"name":"Ali","service":"haircut","price":15},
        {"name":"Sara","service":"wash","price":5},
        {"name":"Omar","service":"haircut","price":15},
        {"name":"Lina","service":"beard","price":10},
]
print(get_names(bookings))
print(total_for(bookings,"haircut"))
print(total_for(bookings,"beard"))
print(costumer_of(bookings,"haircut"))
print(revenue_by_service(bookings))
