# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Animal speaks
dog.bark()   # Output: Dog barks


# Multiple Inheritance
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")

c = C()
c.method_a()  # Output: Method A
c.method_b()  # Output: Method B
c.method_c()  # Output: Method C


# Multilevel Inheritance
class Grandparent:
    def method_grandparent(self):
        print("Method Grandparent")

class Parent(Grandparent):
    def method_parent(self):
        print("Method Parent")

class Child(Parent):
    def method_child(self):
        print("Method Child")

child = Child()
child.method_grandparent()  # Output: Method Grandparent
child.method_parent()       # Output: Method Parent
child.method_child()        # Output: Method Child


# Hierarchical Inheritance
class Parent1:
    def method_parent1(self):
        print("Method Parent1")

class Parent2:
    def method_parent2(self):
        print("Method Parent2")

class Child(Parent1):
    def method_child(self):
        print("Method Child")

class AnotherChild(Parent2):
    def method_another_child(self):
        print("Method Another Child")

child = Child()
another_child = AnotherChild()

child.method_parent1()        # Output: Method Parent1
another_child.method_parent2()# Output: Method Parent2


# Hybrid Inheritance
class A:
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

class C(A):
    def method_c(self):
        print("Method C")

class D(B, C):
    def method_d(self):
        print("Method D")

d = D()
d.method_a()  # Output: Method A (inherited from A)
d.method_b()  # Output: Method B
d.method_c()  # Output: Method C
d.method_d()  # Output: Method D
