'''
try:
    value = int(input())
    result = 10/value
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("successfull",result)

try:
    value = int(input())
    result = 10/value
except (ZeroDivisionError,ValueError) as e:
    print(f"an error occured:{e}")
else:
    print("successfull",result)


class Student:
    college = "RCE"   # Class attribute

    def __init__(self, name):
        self.name = name

s1 = Student("Keerthi")
s2 = Student("Anu")

print(s1.college)
print(s2.college)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Keerthi", 85)
s2 = Student("Anu", 90)

print(s1.name)
print(s2.name)

'''
