class Product():
	def __init__(self, name, price, quantity):
		self.name=name
		self.price=price
		self.quantity=quantity
	def total_value(self):
		return self.price*self.quantity
	def restock(self,amount):
		print("new quantity")
		self.quantity=self.quantity+amount
	def sell(self,amount):
		if self.quantity >= amount:
			self.quantity=self.quantity-amount
			return True
		else:
			print("the qnt is not enough")
			return False
class Store():
	def __init__(self,name):
		self.name=name
		self.products=[]
	def add(self,product):
		self.products.append(product)
	def find(self,name):
		for p in self.products:
			if p.name==name:
				return p
		return None

	def total(self):
		t=0
		for p in self.products:
			t+=p.total_value()
		return t


store=Store("nedjem Shop")
store.add(Product("shoes", 50, 4))
store.add(Product("cap", 15, 10))

"""print(store.total())
shoes=store.find("shoes")
print(shoes.sell(3))
print(shoes.quantity)
shoes.restock(10)
print(shoes.quantity)
print(store.find("hat"))
"""
print(store.find("cap").name)
print(store.find("hat"))
cap=store.find("cap")
print(cap.sell(10))
print(cap.quantity)
cap.restock(20)
print(cap.sell(11))
print(cap.quantity)
