# Python Inheritance - Complete Example

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "can eat")

    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # Method overriding
    def sound(self):
        print(self.name, "barks")

    def display_breed(self):
        print("Breed:", self.breed)


# Creating an object
dog = Dog("Bruno", "Labrador")

# Inherited method
dog.eat()

# Overridden method
dog.sound()

# Child class method
dog.display_breed()

# Checking inheritance
print("Is dog an instance of Dog?", isinstance(dog, Dog))
print("Is dog an instance of Animal?", isinstance(dog, Animal))
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))