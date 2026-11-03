import json

class Product():
	def __init__(self, name, price, quantity):
		self.name=name
		self.price=price
		self.quantity=quantity
	def total_value(self):
		return self.price*self.quantity
	def sell(self, amount):
		if amount<=self.quantity:
			self.quantity=self.quantity-amount
			return True
		else:
			print("Not enough stock")
			return False

p= Product("shoes", 50, 4 )
print(p.total_value())
print(p.sell(4))
print(p.quantity)
print(p.sell(1))
