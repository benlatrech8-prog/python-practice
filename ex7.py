def count_services(orders):
	counts={}
	for  s in orders:
		if s in counts:
			counts[s]+=1
		else:
			counts[s]=1
	return counts
orders=["haircut","beard","haircut","wash","haircut"]
print(count_services(orders))


