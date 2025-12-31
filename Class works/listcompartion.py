# ------------------------------
# Example 1: Adding numbers 1 to 10 into a list (Normal method)
'''
l = []                     # Create an empty list
for i in range(1, 11):     # Loop from 1 to 10
    l.append(i)            # Add each number to the list
print(l)                   # Print the final list


# List Comprehension version (shorter and faster)
lc = [i for i in range(1, 11)]   # Create list directly using comprehension
print(lc)

# ------------------------------
# Example 2: Adding only EVEN numbers from 1 to 10

res = []                   # Empty list to store even numbers
for i in range(1, 11):     # Loop from 1 to 10
    if i % 2 == 0:         # Check if number is even
        res.append(i)      # Add even number to list
print(res)                 # Print even numbers list


# List Comprehension with condition
resl = [i for i in range(1, 11) if i % 2 == 0]  # Even numbers only
print(resl)

# ------------------------------
# Example 3: Taking user input and storing in a list

names = []                 # Empty list to store names
for i in range(5):         # Loop runs 5 times
    names.append(input("Enter the name: "))  # Take input and add to list
print(names)               # Print names list


# List Comprehension for input
names1 = [input("Enter the name: ") for i in range(5)]  # Input 5 names
print(names1)

# ------------------------------

s='Python Programming'
r=[]
v='aeiouAEIOU'
for i in s:
    if i in v:
        r.append(i)
    else:
        r.append(0)
print(r)

rl = [i if i in v else 0 for i in s]
print(rl)

s="Python Programming language" # in set form
r={i for i in s}
print(r)

s="Python Programming language" # in set form
r=tuple(i for i in s)
print(r)

d={}
for i in range(1,21):
    d[i]=i*i
print(d)

dl={i:i*i for i in range(1,11)}
print(dl)
'''
dl={input("enter the product:"):input("enter the price:")for i in range(1,5)}
print(dl)
