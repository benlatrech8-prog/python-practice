def customer_service(bookings,name):
	ser=[]
	for d in bookings:
		if d["name"]==name:
			ser.append(d["service"])
	return ser
def customer_total(bookings):
	tot={}
	for d in bookings:
		name=d["name"]
		if name in tot:
			tot[name]+=d["price"]
		else :
			tot[name]=d["price"]
	return tot
def best_customer(bookings):
	totals=customer_total(bookings)
	best_total=0
	best_name=""
	for name,total in totals.items():
		if total>best_total:
			best_total=total
			best_name=name
	return best_name
def add_booking(bookings):
	n=input("Enter the name :")
	s=input("Enter the service: " )
	while True:
		try:
			p=int(input("Enter the price :"))
			if p>0:
				break
			else:
				print("price must be greater than 0")
		except ValueError:
			print("please enter a number")
	new_booking={"name":n ,"service":s, "price":p}
	bookings.append(new_booking)
	print("Booking Added , Total bookings",len(bookings))
bookings=[
        {"name":"Ali", "service":"haircut", "price":15},
         {"name":"Sara", "service":"wash", "price":5},
         {"name":"Omar", "service":"haircut", "price":15},
         {"name":"Lina", "service":"beard", "price":10},
        {"name":"Ali", "service":"beard", "price":15},
]
print(customer_service(bookings,"Ali"))
print(customer_service(bookings,"Sara"))
print(customer_total(bookings))
print(best_customer(bookings))
add_booking(bookings)
