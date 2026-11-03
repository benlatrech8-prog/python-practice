prices={"haircut": 15 , "beard" : 10 , "wash" : 5 }
	
def total_price(prices,services):
	res=0
	for s in services:
		if s in  prices:
			res+= prices[s]
	return res
print(total_price(prices,["haircut","beard"]))

print(total_price(prices,["wash","massage"]))

print(total_price(prices,["haircut","haircut"]))

