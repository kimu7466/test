# Method Overriding
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Method Overloading (Python does not support method overloading directly, but we can achieve it in a different way)
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# We can achieve method overloading using default arguments or variable-length arguments
class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

# Polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()  # Output: "Woof!" and "Meow!"

calculator = Calculator()
print(calculator.add(2, 3))       # Output: 5
print(calculator.add(2, 3, 4))    # Output: 9
