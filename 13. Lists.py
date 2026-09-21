# ordered, changebale & allows duplicates

fruits = ['Banana', 'Apple', 'Orange', 'Apple', 'Grapefruit', 'Grapes']
print(len(fruits))
print(fruits[2])
print(fruits[0:4])
print(fruits[-2]) #2nd last items

fruits.append('Blueberries')
fruits.insert(3, "Walnuts")
fruits.remove('Orange')
print(fruits)

myInfo = ["Areeba", 21, "Graduate", True]
print(myInfo)
print(type(myInfo))

# fruits.extend(myInfo)
# print(fruits)

for i in range(len(myInfo)):
    print(myInfo[i])
    
print(range(len(myInfo)))

i = 0
while i < len(myInfo):
    print(myInfo[i])
    i+=1
    
myList = ["Cow", "Buffalo", "Dog", "Kangroo", "Elephant", "Zebra", "Giraffe"]
print(myList)
myList.pop(1)
print(myList)
myList.sort(reverse= True)  #alphabetically reverse -> start from Z-A
print(myList)

def myfunc(n):
  return abs(n - 50) # absolute of the number

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)