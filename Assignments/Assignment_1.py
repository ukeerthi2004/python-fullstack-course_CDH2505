# ============================================================
# REDBUS BOOKING SYSTEM – DEMONSTRATION OF ALL DATA TYPES
# This program collects booking details from a RedBus user
# and stores them using different Python data types.
# ============================================================

#Task -1
# ---------------- STRING DATA TYPE ----------------
# Used to store text data like passenger name
user_name = input("Enter Passenger Name: ")


# ---------------- INTEGER DATA TYPE ----------------
# Used to store whole numbers like booking ID
booking_id = int(input("Enter Booking ID: "))


# ---------------- FLOAT DATA TYPE ----------------
# Used to store decimal values like ticket price
ticket_price = float(input("Enter Ticket Price: "))


# ---------------- LIST DATA TYPE ----------------
# Used to store multiple seat numbers
# split() converts input string into a list
seats = input("Enter Seat Numbers (A1 A2 B1): ").split()


# ---------------- TUPLE DATA TYPE ----------------
# Used to store fixed journey date (DD MM YYYY)
# map(int, ...) converts each value to integer
# tuple() stores the date as an immutable collection
journey_date = tuple(
    map(int, input("Enter Journey Date (DD MM YYYY): ").split())
)


# ---------------- SET DATA TYPE ----------------
# Used to store unique facilities
# Duplicate values are automatically removed
facilities = set(
    input("Enter Facilities (AC WiFi Sleeper): ").split()
)


# ---------------- DICTIONARY DATA TYPE ----------------
# Used to store all booking details in key-value pairs
booking_details = {
    "Name": user_name,
    "Booking ID": booking_id,
    "Ticket Price": ticket_price,
    "Seats": seats,
    "Journey Date": journey_date,
    "Facilities": facilities
}

#Task -2
# ---------------- OUTPUT SECTION ----------------
# Printing heading for clarity
print("\n--- REDBUS BOOKING DETAILS ---\n")


# ---------------- COMMA SEPARATION PRINTING ----------------
# sep=", " is used to separate values with comma
print("Name, Booking ID, Ticket Price",
    booking_details["Name"],
    booking_details["Booking ID"],
    booking_details["Ticket Price"],
    sep=", ")


# ---------------- PERCENTAGE / NUMERIC FORMATTING ----------------
# %.2f formats the ticket price to 2 decimal places
print("Ticket Price: ₹%.2f" % booking_details["Ticket Price"])


# ---------------- F-STRING FORMATTING ----------------
# Used to display date in readable format
print(f"Journey Date: {journey_date[0]}-{journey_date[1]}-{journey_date[2]}")

# Display list of seats
print(f"Seats Selected: {seats}")

# Display selected facilities
print(f"Facilities Chosen: {facilities}")


# ---------------- FORMAT() METHOD ----------------
# Another way of formatting output
print("Passenger Name: {}, Booking ID: {}".format(
    booking_details["Name"],
    booking_details["Booking ID"]
))
