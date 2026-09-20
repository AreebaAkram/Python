print(10==9)
print(11 < 9 )

a = 2
b = 3
if a < b:
    print("a is smaller than b")
else:
    print("a is greater than b") 

print(bool("Heeloo")) #except empty values , all values are True in Python
print(bool(0))

class firstclass():
    def __len__(self):
        return 0
first_obj = firstclass()
print(bool(first_obj))

def firstfun():
    return True
if firstfun():
    print("Yes")
else:
    print("No")

x = 20
print(isinstance(x, int))
