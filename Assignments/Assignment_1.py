# REDBUS BOOKING SYSTEM
# This program takes booking details from the user
# and stores them using different Python data types.

#Task 1 - Take Product Details as Input from the User
# Asking passenger name (text value)
user_name = input("Enter Passenger Name: ")


# Taking booking ID (number without decimals)
booking_id = int(input("Enter Booking ID: "))


# Taking ticket price (can have decimal value)
ticket_price = float(input("Enter Ticket Price: "))


# Taking seat numbers chosen by the user
# split() helps to store each seat separately in a list
seats = input("Enter Seat Numbers (A1 A2 B1): ").split()


# Taking journey date
# Date is fixed, so we store it in a tuple
journey_date = tuple(map(int, input("Enter Journey Date (DD MM YYYY): ").split()))


# Taking facilities selected by the user
# set is used so that duplicate facilities are not repeated
facilities = set(input("Enter Facilities (AC WiFi Sleeper): ").split())


# Storing all booking details in one place using dictionary
booking_details = {
    "Name": user_name,
    "Booking ID": booking_id,
    "Ticket Price": ticket_price,
    "Seats": seats,
    "Journey Date": journey_date,
    "Facilities": facilities
}

#Task 2 - Display Booking Details using Different Print Methods

# Displaying booking details
print("\n--- REDBUS BOOKING DETAILS ---\n")


# Printing main details using comma separation
print("Name, Booking ID, Ticket Price",
    booking_details["Name"],
    booking_details["Booking ID"],
    booking_details["Ticket Price"],
    sep=", ")


# Printing ticket price with 2 decimal places
print("Ticket Price: ₹%.2f" % booking_details["Ticket Price"])


# Showing journey date in DD-MM-YYYY format
print(f"Journey Date: {journey_date[0]}-{journey_date[1]}-{journey_date[2]}")


# Showing seats selected by the passenger
print(f"Seats Selected: {seats}")


# Showing facilities selected
print(f"Facilities Chosen: {facilities}")


# Printing passenger name and booking ID using format() method
print("Passenger Name: {}, Booking ID: {}".format(
    booking_details["Name"],
    booking_details["Booking ID"]
))
