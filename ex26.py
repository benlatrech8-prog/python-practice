import json
class Booking:
    def __init__(self, name, service, price):
            self.name= name
            self.service= service
            self.price= price
    def to_dict(self):
        return {"name": self.name, "service": self.service, "price": self.price}
    def describe(self):
        return self.name + " - " + self.service

    def is_expensive(self):
        if self.price >= 15:
            return True
        else:
            return False
    def apply_discount(self,percent):
        self.price=self.price-self.price*percent/100

class Salon:
    def __init__(self,name):
        self.name=name
        self.bookings=[]
    def save(self,filename):
        data=[]
        for b in self.bookings:
            data.append(b.to_dict())
        with open (filename, "w") as f:
            json.dump(data, f, indent=2)
    def load(self, filename):
        try:
            with open(filename, "r") as f:
                data=json.load(f)
        except FileNotFoundError:
            data=[]
        self.bookings= []
        for d in data:
            b = Booking(d["name"], d["service"], d["price"])
            self.bookings.append(b)

    def add(self,booking):
        self.bookings.append(booking)
    def count(self):
        n=0
        for b in self.bookings:
            n+=1
        return n

    def total(self):
        n=0
        for b in self.bookings:
                n+=b.price
        return n
    def show_all(self):
        l=[]
        for b in self.bookings:
            l.append( b.describe())
        return l

if __name__ == "__main__":

    salon= Salon("Nedjem Barber")
    salon.load("salon.json")
    print(salon.count())
    print(salon.total())
#    print(salon.bookings[0].describe())
"""
    b1=Booking("Ali", "haircut" ,15)
    b2=Booking("Sara", "wash" ,5)
    salon=Salon("Nedjem Barber")
    salon.add(b1)
    salon.add(b2)
    salon.add(Booking("nedjem","beard",10))
    print(salon.name)
    print(len(salon.bookings))
    print(salon.bookings[0].name)
    print(salon.bookings[-1].describe())
    print(salon.count())
    print(salon.total())
    print(salon.show_all())
    salon.save("salon.json")
"""
