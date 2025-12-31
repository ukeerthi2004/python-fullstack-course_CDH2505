# ============================================
# PYTHON LOOPS – FOR & WHILE (ALL IN ONE FILE)
# ============================================

# --------------------------------------------
# FOR LOOP EXAMPLES
# --------------------------------------------

# Example 1: Loop through a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:              # Takes each value from list
    print(f"Number: {number}")

print("----------------------------")

# Example 2: Loop through a range of numbers
for i in range(1, 6):               # range(1,6) → 1 to 5
    print(f"Range value: {i}")

print("----------------------------")

# Example 3: Loop through a string
text = "Python"
for char in text:                   # Iterates character by character
    print(f"Character: {char}")

print("----------------------------")

# Example 4: Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:                  # Even number check
        print("Even:", i)

print("----------------------------")

# Example 5: Sum of numbers in a list
nums = [10, 20, 30, 40]
total = 0
for n in nums:
    total += n                      # Add each number
print("Sum of list:", total)

print("----------------------------")

# Example 6: Count vowels in a string
word = "programming"
vowel_count = 0

for ch in word:
    if ch in "aeiou":               # Check for vowel
        vowel_count += 1

print("Vowel count:", vowel_count)

print("----------------------------")

# Example 7: FOR loop with else
for i in range(1, 4):
    print(i)
else:
    print("For loop completed")

print("============================")

# --------------------------------------------
# WHILE LOOP EXAMPLES
# --------------------------------------------

# Example 8: Print numbers from 1 to 5
i = 1
while i <= 5:                       # Condition check
    print(i)
    i += 1                          # Increment

print("----------------------------")

# Example 9: Sum of first 10 natural numbers
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum:", total)

print("----------------------------")

# Example 10: Reverse a number
num = 1234
rev = 0

while num > 0:
    digit = num % 10                # Last digit
    rev = rev * 10 + digit          # Build reverse
    num //= 10                      # Remove last digit

print("Reversed number:", rev)

print("----------------------------")

# Example 11: WHILE loop with else
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("While loop completed")

print("----------------------------")

# Example 12: WHILE loop to count digits
num = 56789
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digit count:", count)

# ============================================
# END OF FILE
# ============================================
