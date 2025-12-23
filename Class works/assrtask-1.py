# STUDENT ADMISSION SYSTEM – ALL DATA TYPES

# String
student_name = input("Enter Student Name: ")

# Integer
student_id = int(input("Enter Student ID: "))

# Float
percentage = float(input("Enter Percentage: "))

# List (string) – Subjects chosen
subjects = input("Enter Subjects (Maths Science English): ").split()

# Tuple (integer) – Date of Birth (DD MM YYYY)
dob = tuple(map(int, input("Enter Date of Birth (DD MM YYYY): ").split()))

# Set (string) – Extra-curricular activities
activities = set(input("Enter Activities (Sports NCC Music): ").split())

# Dictionary – Student details
student_details = {
    "Name": student_name,
    "ID": student_id,
    "Percentage": percentage,
    "Subjects": subjects,
    "DOB": dob,
    "Activities": activities
}

print("\n--- STUDENT ADMISSION DETAILS ---\n")

# Comma separation
print("Name, ID, Percentage",
      student_details["Name"],
      student_details["ID"],
      student_details["Percentage"],
      sep=", ")

# Percentage / numeric formatting
print("Percentage: %.2f%%" % student_details["Percentage"])

# f-string
print(f"Date of Birth: {dob[0]}-{dob[1]}-{dob[2]}")
print(f"Subjects Chosen: {subjects}")
print(f": {activities}")

# format() method
print("Student Name: {}, Student ID: {}".format(
    student_details["Name"],
    student_details["ID"]
))
