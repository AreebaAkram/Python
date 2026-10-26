# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
mytuple = ("apple", "banana", "grapefruit")

myiter = iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# using loop
for i in mytuple:
    print(i)
    
# print(mytuple)

class myIterator:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
myclass = myIterator()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
