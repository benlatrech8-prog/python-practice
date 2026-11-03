def show_menu(prices):
	for k,v in prices.items():
		print(k,v)
def menu_total(prices):
	s=0
	for v in prices.values():
		s+= v
	return s
def checkout(prices):
	total=0
	while True:
		service=input("service (or done)")
		if service== "done":
			break
		price=prices.get(service)

		if price is None:
			print("service not found")
		else:
			total+=price
			print("Added",service,price)
	return total

prices={"haircut":15,"beard":10,"wash":5}
show_menu(prices)
print(menu_total(prices))
print(checkout(prices))
