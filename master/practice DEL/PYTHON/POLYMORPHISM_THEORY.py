# Polymorphism, in the context of object-oriented programming, can manifest in various forms. The two main types are **compile-time polymorphism** and **runtime polymorphism**. Each type has its own subtypes or variations. Let's delve into each:

# ### Compile-Time Polymorphism:
# 1. **Method Overloading**: This occurs when multiple methods in the same class have the same name but different parameters. The compiler decides which method to call based on the number and type of arguments provided.

# ```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Called with different arguments
calculator = Calculator()
calculator.add(2, 3)        # Calls the first add method
calculator.add(2, 3, 4)     # Calls the second add method
# ```

# ### Runtime Polymorphism:
# 1. **Method Overriding**: This happens when a subclass provides a specific implementation of a method that is already defined in its superclass. The decision on which method to call is made at runtime based on the object type.

# ```python
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Polymorphism in action
dog = Dog()
cat = Cat()

dog.make_sound()  # Output: "Woof!"
cat.make_sound()  # Output: "Meow!"
# ```

# 2. **Duck Typing**: In languages like Python, where there is no strict type checking, polymorphism can occur implicitly based on the methods and properties present rather than the actual type.

# ```python
class Duck:
    def fly(self):
        print("Duck flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

# Polymorphism without inheritance
def make_object_fly(obj):
    obj.fly()

# Both Duck and Airplane objects can fly
duck = Duck()
airplane = Airplane()

make_object_fly(duck)      # Output: "Duck flies"
make_object_fly(airplane)  # Output: "Airplane flies"
# ```

# These are the main types of polymorphism in object-oriented programming. They provide flexibility in designing and structuring code, allowing for reuse and abstraction.