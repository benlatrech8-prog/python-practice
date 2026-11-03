"""
ex20.py
Booking class :each booking has a name ,service ,and price.
Practice:classes,__init__ ,self, methods.
methods:
	is_expensive: return true if price greater then 15 else return False
	apply_discount: take percent as parameter and count new price after dicount

to know: if we want to change something is the object we have to call it with #self#
"""

class Booking:
	def __init__(self, name, service, price):
		self.name=name
		self.service=service
		self.price=price
	def describe(self):
		return self.name + " - " + self.service

	def is_expensive(self):
		if self.price >= 15:
			return True
		else:
			return False
	def apply_discount(self,percent):
		self.price=self.price-self.price*percent/100

b1=Booking("Ali", "haircut",15)
b2=Booking("Sara", "wash",5)

print(b1.name)
print(b2.price)
print(b1.describe())
print(b2.describe())
print(b1.is_expensive())
print(b2.is_expensive())
b1.apply_discount(20)
print(b1.price)
