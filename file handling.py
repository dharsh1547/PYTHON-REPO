# 1. CREATE AND WRITE TO A FILE

file = open("student.txt", "w")

file.write("Student Name: Dharshini\n")
file.write("Course: B.Tech Data Science\n")
file.write("Year: 2nd Year\n")
file.write("Subject: Python\n")

file.close()

print("File created and data written successfully!")

# 2. READ THE FILE

file = open("student.txt", "r")

content = file.read()

print("\n--- File Content ---")
print(content)

file.close()


# 3. READ LINE BY LINE


file = open("student.txt", "r")

print("--- Reading Line by Line ---")

for line in file:
    print(line.strip())

file.close()


# 4. READ ONLY THE FIRST LINE

file = open("student.txt", "r")

first_line = file.readline()

print("\nFirst Line:")
print(first_line)

file.close()


# 5. READ ALL LINES USING readlines()

file = open("student.txt", "r")

lines = file.readlines()

print("\n--- All Lines ---")

for line in lines:
    print(line.strip())

file.close()


# 6. APPEND DATA TO THE FILE

file = open("student.txt", "a")

file.write("Skill: Python Programming\n")
file.write("Goal: Become a Data Scientist\n")

file.close()

print("\nNew data appended successfully!")


# 7. USING 'with' STATEMENT

# The with statement automatically closes the file.

with open("student.txt", "r") as file:
    content = file.read()

print("\n--- File Using with Statement ---")
print(content)


# 8. CHECK WHETHER FILE EXISTS

import os

if os.path.exists("student.txt"):
    print("student.txt exists.")
else:
    print("student.txt does not exist.")


# 9. GET FILE SIZE

if os.path.exists("student.txt"):
    size = os.path.getsize("student.txt")

    print("File Size:", size, "bytes")

