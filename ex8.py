from ex7 import count_services
def most_popular(counts):
	best_n=0
	best_name=""
	for service,n in counts.items():
		if n> best_n:
			best_n=n
			best_name=service
	return best_name
orders=["wash","haircut","wash","haircut"]
print(most_popular(count_services(orders)))
