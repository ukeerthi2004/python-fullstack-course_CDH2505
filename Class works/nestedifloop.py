# =================================================
# NESTED FOR LOOP
# =================================================
# 👉 A nested for loop means:
#     One for loop inside another for loop
#
# Syntax:
# for outer in sequence1:
#     for inner in sequence2:
#         statement
#
# Outer loop → controls ROWS
# Inner loop → controls COLUMNS
# =================================================


# -------------------------------------------------
# Pattern 1: Square pattern using *
# -------------------------------------------------
for row in range(5):              # Controls number of rows
    for col in range(5):          # Controls number of columns
        print("*", end=' ')       # Print star in same line
    print()                       # Move to next line

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""


# -------------------------------------------------
# Pattern 2: Column number pattern
# -------------------------------------------------
for row in range(5):
    for col in range(5):
        print(col + 1, end=' ')   # Print column number
    print()

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


# -------------------------------------------------
# Pattern 3: Row number pattern
# -------------------------------------------------
for row in range(5):
    for col in range(6):
        print(row + 1, end=' ')   # Print row number
    print()

"""
1 1 1 1 1 1
2 2 2 2 2 2
3 3 3 3 3 3
4 4 4 4 4 4
5 5 5 5 5 5
"""


# -------------------------------------------------
# Pattern 4: Right angle triangle (increasing)
# -------------------------------------------------
for row in range(1, 6):           # Rows from 1 to 5
    for col in range(row):        # Columns depend on row
        print("*", end=' ')
    print()

"""
*
* *
* * *
* * * *
* * * * *
"""


# -------------------------------------------------
# Pattern 5: Inverted right angle triangle
# -------------------------------------------------
for row in range(5, 0, -1):       # Reverse rows
    for col in range(row):
        print("*", end=' ')
    print()

"""
* * * * *
* * * *
* * *
* *
*
"""


# -------------------------------------------------
# Pattern 6: Same using user input
# -------------------------------------------------
n = int(input("Enter n: "))
for row in range(n):
    for col in range(n - row):
        print("*", end=' ')
    print()

"""
* * * * *
* * * *
* * *
* *
*
"""


# -------------------------------------------------
# Pattern 7: Right aligned triangle
# -------------------------------------------------
n = int(input("Enter n: "))
for row in range(n):
    for spc in range(n - 1 - row):    # Print spaces
        print(" ", end=' ')
    for col in range(row + 1):        # Print stars
        print("*", end=' ')
    print()

"""
        *
      * *
    * * *
  * * * *
* * * * *
"""


# -------------------------------------------------
# Pattern 8: Inverted right aligned triangle
# -------------------------------------------------
n = int(input("Enter n: "))
for row in range(n):
    for spc in range(row):            # Leading spaces
        print(" ", end=' ')
    for col in range(n - row):
        print("*", end=' ')
    print()

"""
* * * * *
  * * * *
    * * *
      * *
        *
"""


# -------------------------------------------------
# Pattern 9: Hollow square pattern
# -------------------------------------------------
n = int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
* * * * *
*       *
*       *
*       *
* * * * *
"""


# -------------------------------------------------
# Pattern 10: X pattern (diagonal cross)
# -------------------------------------------------
n = int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        if row == col or row + col == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*       *
  *   *
    *
  *   *
*       *
"""
