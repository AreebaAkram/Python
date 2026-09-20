x = 4
x = "Areeba"
print(x)

#casting
x = str("Areeba")
y = 6
print(x)
print(y)

#type fun
print(type(y))

#multi values to multi var
a, b, c = "x", "y", "z"
print(a)
print(b)
print(c)

#one value to multiple var
p = q= l = "Areeba"
print(p)
print(q)
print(l)

#unpack collection
animals = ["cat", "dog"]
j, k = animals
print(j)
print(j, k)
print(j +k) # these 2 will generate same output if they are of same data types
o = "hi!"

#global variables 
def firstfun():
    # x = "frog" A LOCAL VAR
    global t 
    # can be accessed outside function
    t = "Hello World!"
    global o 
    # value will be updated outside of function
    o = "Hey"
    print(x) 
firstfun()
print(t)
print (o)
