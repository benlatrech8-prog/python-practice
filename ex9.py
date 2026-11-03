try:
	people=int(input("How many people :"))
	print("Booking for ",people," people")
except ValueError:
	print("Please enter a number")
