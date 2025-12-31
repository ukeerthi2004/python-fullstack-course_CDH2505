# ============================================
# PYTHON FOR LOOP – SYNTAX & EXAMPLES
# ============================================

# --------------------------------------------
# BASIC FOR LOOP SYNTAX
# --------------------------------------------
"""
for variable in sequence:
    statements

sequence can be:
list, tuple, set, dictionary, string, range
"""

# --------------------------------------------
# Example 1: Looping through a dictionary
# --------------------------------------------
"""
products = {
    "qwer": 3445,
    "djjf": 5637,
    "jduks": 3484,
    "fjjd": 2344,
}

for i in products:                 # Iterates through dictionary KEYS
    print(f'{i}: ${products[i]}')  # Access value using key
    print(i, products[i])          # Prints key and value
"""

# --------------------------------------------
# Example 2: Vowel and Consonant checking
# --------------------------------------------
"""
s = 'Python Programming'
vol = 'aeiouAEIOU'                  # All vowels (lower + upper case)

for i in s:                         # Loop through each character
    if i in vol:                    # Check vowel
        print(f'{i} -- Vowel')
    else:
        print(f'{i} -- Consonant')
"""

# --------------------------------------------
# Example 3: Multiplication table (Forward)
# --------------------------------------------
"""
table = int(input("Enter the table: "))

for i in range(1, 21):              # 1 to 20
    print(f'{table} * {i} = {table * i}')
"""

# --------------------------------------------
# Example 4: Multiplication table (Reverse)
# --------------------------------------------
"""
table = int(input("Enter the table: "))

for i in range(10, 0, -1):           # Reverse order using step -1
    print(f'{table} * {i} = {table * i}')
"""

# --------------------------------------------
# Example 5: Loop using index (range + len)
# --------------------------------------------
"""
l = ['hgfgh', 'jhgfdfg', 'hgfdfgh', 'reert']

for i in range(len(l)):             # Index-based looping
    print(i, l[i])                  # Prints index and value
"""

# --------------------------------------------
# Example 6: enumerate() function
# --------------------------------------------

l = ('hgfgh', 'jhgfdfg', 'hgfdfgh', 'reert')

for i in enumerate(l):
    # enumerate() returns (index, value) as a tuple
    print(i)

# ============================================
# END OF FILE
# ============================================
