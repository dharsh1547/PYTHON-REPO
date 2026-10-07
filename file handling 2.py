# 1. WRITE MULTIPLE LINES

with open("subjects.txt", "w") as file:
    file.write("Python\n")
    file.write("SQL\n")
    file.write("Power BI\n")
    file.write("Machine Learning\n")

print("Subjects added successfully.")


# 2. READ FILE LINE BY LINE

with open("subjects.txt", "r") as file:
    for line in file:
        print(line.strip())


# 3. COUNT NUMBER OF LINES

with open("subjects.txt", "r") as file:
    lines = file.readlines()

print("\nNumber of lines:", len(lines))


# 4. SEARCH FOR A WORD

search = "Python"

with open("subjects.txt", "r") as file:
    content = file.read()

if search in content:
    print("Word found!")
else:
    print("Word not found!")


# 5. REPLACE CONTENT

with open("subjects.txt", "r") as file:
    content = file.read()

content = content.replace("SQL", "Advanced SQL")

with open("subjects.txt", "w") as file:
    file.write(content)

print("Content updated successfully.")


# 6. ADD DATA USING APPEND

with open("subjects.txt", "a") as file:
    file.write("Data Science\n")

print("New subject added.")


# 7. HANDLE FILE ERROR

try:
    with open("marks.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found!")


# 8. CHECK WHETHER A FILE EXISTS

import os

if os.path.exists("subjects.txt"):
    print("subjects.txt exists.")
else:
    print("File does not exist.")


