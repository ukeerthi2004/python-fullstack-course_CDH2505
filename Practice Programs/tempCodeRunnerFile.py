ch = input()
if ch.lower() in "aieou":
    print("Vowels")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("digit")
else:
    print("special character")