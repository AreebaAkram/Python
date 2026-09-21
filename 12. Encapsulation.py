class person:
    def __init__(self, name, age, salary):
        self.name= name
        self.__age = age #private property
        self._salary = salary #protected property
        
    #a getter method to access a private property
    def getage(self):
        return self.__age
    
    #a setter method to change a private property
    def setage(self, age):
        if age > 0:
            self.__age = age
        else:
            print("age muste be positive")
            
        
p1 = person("Areeba", 21, 35000)
print(p1.name)
#print(p1.__age)  #causes error as private property can't be accessed directly outside the class
print(p1._salary)
print(p1.getage())
p1.setage(-10)
print(p1.getage())

# private methods

class calculator:
    def __init__(self):
        self.result = 0
    
    def __validate(self, num):
        if not isinstance (num, (int, float)):
            return False
        return True
    
    def sum(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("invalid number")
            
cal = calculator()
cal.sum(10)
print(cal.result)
