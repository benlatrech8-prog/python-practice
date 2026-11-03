from ex26 import Salon, Booking

# salon = Salon(...)
salon=Salon("Mays Perfumes")
# load من salon.json
salon.load("salon.json")

# while True:
while True:
    # اطبع الـ menu
    print("1. Add booking\n 2. Show all\n 3. Total\n 4. Save and quit") 
    # choice = input
    choice=input("Choose: ")
    # if "1":
    if choice == "1":
        name=input("name: ")
        service=input("service: ")
        while True:
            try:
                price=int(input("price: "))
                break
            except ValueError:
                print("please enter a number")
        b=Booking(name,service,price)
        salon.add(b)
        salon.save("salon.json")
        print("Added")

    elif choice=="2":
        print(salon.show_all())
    elif choice=="3":
        print(salon.total())
    elif choice=="4":
        salon.save("salon.json")
        print("Saved. Bye!")
        break
    else:
        print("invalid choice")
        # اسقسي الاسم و الخدمة
        # اسقسي السعر حتى يكون رقم (while True + try/except)
        # صنع Booking و زيدو بـ salon.add
    # elif "2": اطبع كامل الحجوزات
    # elif "3": اطبع المجموع
    # elif "4": save، اطبع "Saved"، break
    # else: "Invalid choice"
