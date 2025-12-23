# WEEKEND PLANER (if-elif-else condition)
'''amount=int(input("enter the amount:"))
if amount >= 10000:
    print("Trip to goa")
elif 8000 <= amount < 10000:
    print("Clubings")
elif 5000 <= amount < 8000:
    print("Go to cafe")
elif 3000 <= amount < 5000:
    print("shopping")
elif 1000 <= amount < 3000:
    print("Visit local places")
elif 500 <= amount < 1000:
    print("Order something")
else:
    print("Go for chai and sleep")
'''
# time and wishes without else
'''hrs,mins = tuple(map(int,input("Enter the hours and mins:").split()))
if 0<=hrs<4 and 0<=mins<=59:
    print("It's high time. Better go to sleep")
elif 4<= hrs < 12 and 0<=mins<=59:
    print("Good morning.Have a great day")
elif 12<= hrs < 16 and 0<=mins<=59:
    print("Good Afternoon. Have a great dinner")
elif 16<= hrs<21 and 0<=mins<=59:
    print("Good evening. Have a great dinner")
elif 21<=hrs<24 and 0<=mins<=59:
    print("Good night. Scroll reels")'''
# whatsapp chat with sent or not
# 0- sent
# 1 - Delivered
# 2 - Seen
'''chatStatus = int(input("enter the chat status:"))

if chatStatus == 0:
    print("sent,display single tick")
elif chatStatus == 1:
    print("Delivered,display double tick")
elif chatStatus == 2:
    print("Seen,display blue tick")
else:
    print("Unble send message")'''

# Nested if example
cgh = int(input("enter the voter id:"))
id={123,345,456,678,987}
age = int(input("Enter the age:"))

if cgh in id:
    if age>=18:
        print( "Congrats,You can Vote")
    else:
        print("You are under age")
else:
    print("you need to be Indian to vote")


