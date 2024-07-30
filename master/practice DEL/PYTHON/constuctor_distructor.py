class myClass:
# class myClass:

    def __init__(self, name , number):
        self.name = name 
        self.number= number

    def print_info(self):
        print(self.name, self.number)
    def __del__(self):
        print(f"{self.name} is being destroyed")

p1 = myClass("John", 123)
print(p1.name)
print(p1.number)
