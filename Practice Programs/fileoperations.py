"""import os

if os.path.exists("example.txt"):
    file = open("example.txt", "r")
    print("file opened successfully")
    print(file.read())
else:
    print("file doesnot exist")


file = open("example.txt","r")
content = file.read()
line = file.readline()
lines = file.readlines()
print(content)
#print(line)
#print(lines)
file.close()

with open("example.txt","r") as file:
    content = file.read()
    print(content)

text = "Hello, python"

with open("example.txt", "w") as file:
    file.write(text)

print(text)

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open('example.txt','a') as file:
    file.write('\nnew line added')

import os
file_path = os.path.join("example.txt")
print(file_path)
with open(file_path, "r") as file:
    print(file.read())
"""
import os
file_path = "example.txt"
if os.path.isfile(file_path):
    print("File size: ",os.path.getsize(file_path),bytes)
    print("Abosulate path: ",os.path.abspath(file_path))
else:
    print("file does not exist")

