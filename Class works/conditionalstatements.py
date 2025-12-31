# ------------------------------
# IF STATEMENT SYNTAX
'''
1) Simple if
--------------
if condition:
    statements

👉 Executes statements only if condition is TRUE


2) if - else
--------------
if condition:
    statements
else:
    statements

👉 if block runs when condition is TRUE
👉 else block runs when condition is FALSE


3) if - elif - else
--------------------
if condition1:
    statements
elif condition2:
    statements
elif condition3:
    statements
else:
    statements

👉 Used when multiple conditions are checked
👉 Only ONE block executes


4) Nested if
-------------
if condition1:
    if condition2:
        statements
    else:
        statements
elif condition3:
    statements

👉 if inside another if is called Nested if
'''
# ------------------------------

# Example 1: Simple if (commented example)
'''
cf = {'rina', 'liki', 'juna', 'kaina'}   # Close friends list
user = 'rina'

if user in cf:                          # Check if user is in close friends
    print("You can see the story")
'''

# ------------------------------
# Example 2: if with OR condition (commented example)
'''
f = {'rina', 'liki', 'juna', 'kaina'}    # Friends list
ps = 'public'                           # Post status
user = 'liki'

if user in f or ps == 'public':         # Either friend OR public post
    print("View posts")
'''

# ------------------------------
# Example 3: Login system using if-else

data = {
    'lohit': 'li@34',
    'jikjkl': 'jh@657',
    'jhgfxxhjk': 'oi@1234',
    'oiusdfghjk': 't@34567'
}
# Dictionary stores username as KEY and password as VALUE

us, password = input("Enter the username and password: ").split()
# Takes two inputs in one line and splits them

if data.get(us) == password:
    # data.get(us) returns password of given username
    # If stored password matches entered password
    print(f'Hello {us}\nYour login successful!!!')
else:
    # Executes when username or password is wrong
    print("Invalid login.\nTry again!!!")

# ------------------------------
