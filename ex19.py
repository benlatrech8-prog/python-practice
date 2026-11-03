def checkout(prices):
	total=0
	while True:
		service=input("service ( or done)")
		if service=="done":
			break

		price=prices.get(service)
		if price is None:
			print("service Not found")
		else:
			print("Added",service,price)
			total+=price
	return total
prices={"haircut":15 ,"beard":10 ,"wash":5}
print(checkout(prices))
