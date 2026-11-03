def most_popular(orders):
	best_o=[]
	best_n=0
	for service,n in orders.items():
		if n>best_n:
			best_n=n
			best_o=[service]
		elif n==best_n:
			best_o.append(service)
	return best_o
print(most_popular({"beard":3,"haircut":3,"wash":1}))
print(most_popular({"beard":1,"haircut":5}))
print(most_popular({}))
