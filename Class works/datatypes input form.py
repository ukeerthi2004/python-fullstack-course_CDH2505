# ============================================
# PYTHON INPUT – ALL DATA TYPES
# ============================================

# --------------------------------------------
# 1. STRING INPUT
# --------------------------------------------
"""
name = input('Enter the name: ')   # Takes input as string by default
print(name, type(name))            # Prints value and its data type
"""

# --------------------------------------------
# 2. INTEGER INPUT
# --------------------------------------------
'''
age = int(input("Enter the age: "))  # Converts input string to integer
print(age, type(age))
'''

# --------------------------------------------
# 3. FLOAT INPUT
# --------------------------------------------
'''
price = float(input('Enter the price: '))  # Converts input to float
print(price, type(price))
'''

# --------------------------------------------
# 4. LIST INPUTS
# --------------------------------------------

# List of strings
'''
names = input("Enter names: ").split()   # split() creates list of strings
print(names, type(names))
'''

# List of integers
'''
inte = list(map(int, input("Enter numbers: ").split()))
# map(int, ...) converts each value to int
print(inte, type(inte))
'''

# List of floats
'''
inte = list(map(float, input("Enter float numbers: ").split()))
print(inte, type(inte))
'''

# --------------------------------------------
# 5. TUPLE INPUTS
# --------------------------------------------

# Tuple of integers
'''
inte = tuple(map(int, input("Enter numbers: ").split()))
print(inte, type(inte))
'''

# Tuple of strings
'''
names = tuple(input("Enter names: ").split())
print(names, type(names))
'''

# Tuple of floats
'''
inte = tuple(map(float, input("Enter float numbers: ").split()))
print(inte, type(inte))
'''

# --------------------------------------------
# 6. SET INPUTS
# --------------------------------------------

# Set of integers
'''
inte = set(map(int, input("Enter numbers: ").split()))
# Set removes duplicate values automatically
print(inte, type(inte))
'''

# Set of floats
'''
inte = set(map(float, input("Enter float numbers: ").split()))
print(inte, type(inte))
'''

# Set of strings
'''
names = set(input("Enter names: ").split())
print(names, type(names))
'''

# --------------------------------------------
# 7. USING eval() FOR ANY DATA TYPE
# --------------------------------------------
"""
data = eval(input("Enter any data type: "))
# eval() automatically detects type (list, tuple, set, int, etc.)
# ⚠️ Use carefully (not safe with unknown input)
print(data, type(data))
"""

# --------------------------------------------
# TAKING MULTIPLE INPUTS AT ONCE
# --------------------------------------------
'''
email, pwd = tuple(input("Enter email and password: ").split())
print(email, pwd)
'''

# --------------------------------------------
# PRINT STATEMENT FORMATTING
# --------------------------------------------
"""
a = 10
b = 18.3
c = "jiakna"

# Using sep (separator)
print("a=", a, "b=", b, "c=", c, sep=' ')
print("a=", a, "b=", b, "c=", c, sep='\n')

# Using end
print("a=", a, "b=", b, "c=", c, end=' ')

# Old-style formatting
print('a=%d b=%f c=%s' % (a, b, c))

# format() method
print('a={} b={} c={}'.format(a, b, c))
print('a={} b={} c={}'.format(b, a, c))
print('a={2} b={1} c={0}'.format(a, b, c))
"""

# ============================================
# END OF FILE
# ============================================
