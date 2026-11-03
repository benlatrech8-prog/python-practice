while True:
    try:
        people = int(input("How many people: "))

        if 1 <= people <= 10:
            print("Booking for", people, "people")
            break
        else:
            print("The number must be between 1 and 10")

    except ValueError:
        print("Please enter a number")
