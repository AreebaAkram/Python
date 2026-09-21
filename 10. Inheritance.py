class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def myInfo(self):
        print(self.name, self.age, self.gender)
    def myFamily(Self):
        print("i have family of 5")

class Student(person):
    def __init__(self, name, age, gender, grade):
        # person.__init__(self, name, age, gender) #keeps the inheritance of parent class
        # child's init fun overrides the init of parent class 
        # e.g., def init 
        super().__init__(name, age, gender)  
        self.grade = grade
    def studentInfo(self):
        print(f"{self.age} {self.name} {self.grade}")

p1 = person("Areeba", 21, "Female")
s1 = Student("Alex", 22, "Male", 10)
s2 = Student("Areeba", 21, "Female", 9)

p1.myInfo()
s1.myInfo()
s2.studentInfo()
s2.myFamily()


class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name)
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
d1 = Dog("Rex")
d1.speak()