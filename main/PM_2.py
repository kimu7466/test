class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} = {self.age}")

class student(person):
    def __init__(self, name , age):
        super().__init__(name, age)

p1 = student("imroz",24)

p1.info()