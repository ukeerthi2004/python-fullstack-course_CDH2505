# =================================================
# PYTHON STRING METHODS – COMPLETE REFERENCE FILE
# Python 3.10+
# =================================================


# -------------------------------------------------
# BASIC STRING
# -------------------------------------------------
s = "  Python Class is Going Well  "


# -------------------------------------------------
# 1. CASE CONVERSION METHODS
# -------------------------------------------------
print(s.upper())        # Converts to uppercase
print(s.lower())        # Converts to lowercase
print(s.title())        # First letter of each word uppercase
print(s.capitalize())  # First letter uppercase
print(s.swapcase())    # Swaps upper <-> lower


# -------------------------------------------------
# 2. SPACE REMOVAL METHODS
# -------------------------------------------------
print(s.strip())        # Removes spaces from both sides
print(s.lstrip())       # Removes left spaces
print(s.rstrip())       # Removes right spaces


# -------------------------------------------------
# 3. SEARCHING METHODS
# -------------------------------------------------
print(s.find("Class"))      # Returns index (or -1 if not found)
print(s.rfind("i"))         # Last occurrence index
print(s.index("Class"))    # Same as find(), but error if not found
# print(s.index("Java"))    # ❌ ValueError

print(s.count("i"))         # Counts occurrences
print(s.startswith("  Py")) # True/False
print(s.endswith("Well  ")) # True/False


# -------------------------------------------------
# 4. CHECK METHODS (BOOLEAN)
# -------------------------------------------------
print("python".isalpha())      # Only letters
print("123".isdigit())        # Only digits
print("abc123".isalnum())     # Letters + digits
print("   ".isspace())        # Only spaces
print("python".islower())     # All lowercase
print("PYTHON".isupper())     # All uppercase
print("Python Class".istitle())  # Title case


# -------------------------------------------------
# 5. SPLITTING METHODS
# -------------------------------------------------
s2 = "python,class,is,good"

print(s2.split(","))          # Split by separator
print(s2.rsplit(",", 2))      # Split from right
print(s.split())              # Split by spaces
print(s.splitlines())         # Split by new lines


# -------------------------------------------------
# 6. JOIN METHOD
# -------------------------------------------------
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))         # Join list into string
print("-".join(chars))


# -------------------------------------------------
# 7. PARTITION METHODS
# -------------------------------------------------
s3 = "python class is good"

print(s3.partition("class"))   # (before, sep, after)
print(s3.rpartition("is"))     # Split from right


# -------------------------------------------------
# 8. REPLACE METHOD
# -------------------------------------------------
print(s3.replace("python", "java"))
print(s3.replace(" ", "_"))
print(s3.replace("o", "0", 1))   # Replace only once


# -------------------------------------------------
# 9. ALIGNMENT METHODS
# -------------------------------------------------
print("python".center(20, "*"))
print("python".ljust(15, "-"))
print("python".rjust(15, "-"))


# -------------------------------------------------
# 10. ENCODING & DECODING
# -------------------------------------------------
s4 = "python class"

b = s4.encode()        # String → bytes
print(b)

print(b.decode())      # Bytes → string


# -------------------------------------------------
# 11. TRANSLATION METHODS
# -------------------------------------------------
table = str.maketrans("aeiou", "12345")
print("education".translate(table))


# -------------------------------------------------
# 12. REMOVE PREFIX / SUFFIX (Python 3.9+)
# -------------------------------------------------
s5 = "unhappy"
print(s5.removeprefix("un"))
print(s5.removesuffix("py"))


# -------------------------------------------------
# 13. FORMAT METHODS
# -------------------------------------------------
name = "Keerthi"
age = 21

print("Name: {} Age: {}".format(name, age))
print(f"Name: {name} Age: {age}")   # f-string (recommended)


# -------------------------------------------------
# 14. ord() and chr()
# -------------------------------------------------
print(ord('A'))     # ASCII value
print(chr(65))      # Character from ASCII


# -------------------------------------------------
# 15. ESCAPE CHARACTERS
# -------------------------------------------------
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab
print("Hello\\World")   # Backslash


# =================================================
# END OF STRING METHODS FILE
# =================================================
