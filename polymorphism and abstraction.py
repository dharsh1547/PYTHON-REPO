#polymorphism
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

#abstraction
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display(self):
        pass


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def display(self):
        print("This is a Circle")


# Rectangle class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display(self):
        print("This is a Rectangle")


# Creating objects
circle = Circle(5)
rectangle = Rectangle(10, 5)

# Displaying results
circle.display()
print("Circle Area:", circle.area())

print()

rectangle.display()
print("Rectangle Area:", rectangle.area())