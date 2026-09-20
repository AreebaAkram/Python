class person:
    def __init__(self, name, age): 
        # used to initialize the attributes of an object immediately after it is created, used to assign values to object properties
        self.name = name 
        self.age = age
    def greet(self):
        print("My name is: ", self.name)
        print("My age is: ", self.age)

p1 = person("Areeba", 21)
p1.greet()

# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# it can be any word but necessarily to be the first para of the any method 


# without init fun
# class person2:
#     pass

#     def greet(self, name, age):
#         print("My name is: ", name)
#         print("My age is: ", age)

# p2 = person2()
# p2.name = "ariba"
# p2.age = 20
# p2.greet(p2.name, p2.age)

class Dog:
    def __init__(myObject, name, age, gender):
        myObject.name = name
        myObject.age = age
        myObject.gender = gender
    def bark(abc):
        print(abc.name + " says Woof!")
    def myproperties(self):
        print(f"{self.name} {self.age} {self.gender}")

        
d1 = Dog("Buddy", 3, "Male")
print(d1.name, d1.age)
d1.age = 5  # update property
d1.bark()
d1.myproperties()
del d1.gender #delete gender 
# print(d1.gender)    will produce an error