class vehicle:
    def __init__(self, name, model, brand):
        self.name = name
        self.model = model
        self.brand = brand
    def move(self):
        print("Moves!")

class car(vehicle):
    pass  # pass keyword when you do not want to add any other properties or methods to the class.

class boat(vehicle):
    def move(self):    # function overriding : change / extend base behavior 
        print("Sails")    
            
class plane(vehicle):
    def move(self):
        print("Flies")
        
c1 = car("Corolla", 2019, "Toyota")
b1 = boat("xyz Boat", 2024, "xyz brand")
p1 = plane("abc Plane", 2016, "abc Brand")

for x in (c1, b1, p1):
    print(x.name)
    print(x.model)
    print(x.brand)
    x.move()