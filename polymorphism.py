class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    return "Move!"

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    return super().move() #why is this returning none
    # return "Sail!"


car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object

for x in (car1, boat1):
  print(x.brand)
  print(x.model)
  print(x.move())
