# Python - Access Specifiers
# Public, Protected and Private
# Variables and Methods


class Student:

    def __init__(self):
        # Public variable
        self.name = "Dharshini"

        # Protected variable
        self._age = 20

        # Private variable
        self.__marks = 95

    # Public method
    def display_name(self):
        print("Name:", self.name)

    # Protected method
    def _display_age(self):
        print("Age:", self._age)

    # Private method
    def __display_marks(self):
        print("Marks:", self.__marks)

    # Public method to access private method
    def show_marks(self):
        self.__display_marks()


# Creating object
student = Student()

# Accessing Public Members

print("Public Variable:")
print(student.name)

print()

print("Public Method:")
student.display_name()

# Accessing Protected Members


print()

print("Protected Variable:")
print(student._age)

print()

print("Protected Method:")
student._display_age()



# Accessing Private Members
print()

print("Private Variable:")
print(student._Student__marks)

print()

print("Private Method:")
student.show_marks()