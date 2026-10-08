# Exception Handling in Python
# Different Examples

print("=" * 50)
print("       PYTHON EXCEPTION HANDLING")
print("=" * 50)


# Case 1: Division by Zero
print("\nCase 1: Division by Zero")

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")


# Case 2: Invalid Number
print("\nCase 2: Invalid Number")

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Error: Please enter a valid number.")


# Case 3: List Index Error
print("\nCase 3: List Index Error")

try:
    fruits = ["Apple", "Banana", "Orange"]

    position = int(input("Enter the index of the fruit (0-2): "))
    print("Selected fruit:", fruits[position])

except IndexError:
    print("Error: Index is outside the list range.")

except ValueError:
    print("Error: Please enter a valid index.")


# Case 4: Dictionary Key Error
print("\nCase 4: Dictionary Key Error")

try:
    student = {
        "name": "Dharshini",
        "age": 20,
        "course": "Data Science"
    }

    key = input("Enter a key (name/age/course): ")
    print("Value:", student[key])

except KeyError:
    print("Error: The entered key does not exist.")


# Case 5: File Not Found
print("\nCase 5: File Not Found")

try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")
    content = file.read()

    print("File Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: The requested file was not found.")


# Case 6: Multiple Exceptions
print("\nCase 6: Multiple Exceptions")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    answer = a / b

    print("Division result:", answer)

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# Finally Example
print("\nCase 7: Finally Block")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Error: Invalid input.")

finally:
    print("This block always executes.")


print("\n" + "=" * 50)
print("Program Completed Successfully")
print("=" * 50)