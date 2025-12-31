# ============================================
# IF – ELIF – ELSE & NESTED IF EXAMPLES
# ============================================

# --------------------------------------------
# Example 1: WEEKEND PLANNER (if-elif-else)
# --------------------------------------------
'''
amount = int(input("Enter the amount: "))   # User enters available money

if amount >= 10000:                          # Highest budget check
    print("Trip to Goa")
elif 8000 <= amount < 10000:
    print("Clubing")
elif 5000 <= amount < 8000:
    print("Go to cafe")
elif 3000 <= amount < 5000:
    print("Shopping")
elif 1000 <= amount < 3000:
    print("Visit local places")
elif 500 <= amount < 1000:
    print("Order something")
else:
    print("Go for chai and sleep")
'''

# 👉 Concept:
# - if-elif-else is used when MULTIPLE conditions are checked
# - Only ONE block executes

# --------------------------------------------
# Example 2: Time-based wishes (WITHOUT else)
# --------------------------------------------
'''
hrs, mins = tuple(map(int, input("Enter the hours and mins: ").split()))
# Takes hour and minute as integer input

if 0 <= hrs < 4 and 0 <= mins <= 59:
    print("It's high time. Better go to sleep")
elif 4 <= hrs < 12 and 0 <= mins <= 59:
    print("Good Morning. Have a great day")
elif 12 <= hrs < 16 and 0 <= mins <= 59:
    print("Good Afternoon. Have a great day")
elif 16 <= hrs < 21 and 0 <= mins <= 59:
    print("Good Evening. Have a great dinner")
elif 21 <= hrs < 24 and 0 <= mins <= 59:
    print("Good Night. Scroll reels")
'''

# 👉 Concept:
# - No else block
# - If no condition matches → nothing prints

# --------------------------------------------
# Example 3: WhatsApp Chat Status
# --------------------------------------------
'''
chatStatus = int(input("Enter the chat status: "))

# 0 → Sent
# 1 → Delivered
# 2 → Seen

if chatStatus == 0:
    print("Sent, display single tick")
elif chatStatus == 1:
    print("Delivered, display double tick")
elif chatStatus == 2:
    print("Seen, display blue tick")
else:
    print("Unable to send message")
'''

# 👉 Concept:
# - Integer comparison using ==
# - else handles INVALID input

# --------------------------------------------
# Example 4: NESTED IF – VOTING ELIGIBILITY
# --------------------------------------------

cgh = int(input("Enter the voter ID: "))     # Input voter ID
id = {123, 345, 456, 678, 987}               # Valid voter IDs
age = int(input("Enter the age: "))          # Input age

if cgh in id:                                # Outer if (citizenship check)
    if age >= 18:                            # Inner if (age check)
        print("Congrats, you can vote")
    else:
        print("You are underage")
else:
    print("You need to be Indian to vote")

# 👉 Concept:
# - if inside another if = Nested if
# - First condition must be TRUE to check second condition

# ============================================
# END OF FILE
# ============================================
