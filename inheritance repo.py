#single inheritance
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.eat()
dog.bark()

#multiple inheritance
class Father:
    def father_property(self):
        print("Property from Father")


class Mother:
    def mother_property(self):
        print("Property from Mother")


class Child(Father, Mother):
    def child_property(self):
        print("Property from Child")


child = Child()

child.father_property()
child.mother_property()
child.child_property()

#multilevel inheritance
class Grandparent:
    def house(self):
        print("Grandparent has a house")


class Parent(Grandparent):
    def car(self):
        print("Parent has a car")


class Child(Parent):
    def bike(self):
        print("Child has a bike")


child = Child()

child.house()
child.car()
child.bike()

#hierarchical
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

#hybrid inheitance
class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


class Pet(Dog, Cat):
    def play(self):
        print("Pet plays")


pet = Pet()

pet.eat()
pet.bark()
pet.meow()
pet.play()

#method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()

