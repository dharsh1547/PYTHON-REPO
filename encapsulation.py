# ENCAPSULATION IN PYTHON

class Student:

    def __init__(self, name, age, marks):
        # Public variable
        self.name = name

        # Protected variable
        self._age = age

        # Private variable
        self.__marks = marks

    # Public method
    def display_details(self):
        print("Student Details")
        print("--------")
        print("Name  :", self.name)
        print("Age   :", self._age)
        print("Marks :", self.__marks)

    # Getter method for private variable
    def get_marks(self):
        return self.__marks

    # Setter method for private variable
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully!")
        else:
            print("Invalid marks! Marks must be between 0 and 100.")


# CREATING OBJECT

student = Student("Dharshini", 20, 85)

# Accessing public variable
print("Name:", student.name)

# Accessing protected variable
print("Age:", student._age)

# Accessing private variable using getter
print("Marks:", student.get_marks())

print()


# MODIFYING PRIVATE VARIABLE USING SETTER

student.set_marks(92)

print("Updated Marks:", student.get_marks())

print()


# Trying to set invalid marks
student.set_marks(120)

print()


# Display complete student details
student.display_details()