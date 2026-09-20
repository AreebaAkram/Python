print("Hello World!")
print ("Hey! 'Jenny' ")

a = "Hey!"
print(a)

#multi line string
b = """ Hi, this me areeba
i'm a python programmer
i love coding
"""
print(b)

# string as array
c = "This world is so beautiful"
print(c[2])

for x in "Hello World!":
    print(x)

# length of string
print(len(c))

print("Hello" in x)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# slicing string
text = "Hello, World!"
print(text[2:5]) #position 5 not included
print(text[:5])
print(text[2:])
print(text[-5:-2])

# modify strings
y = " Hey! This might be me hello"
print(y.upper())
print(y.lower())
print(y.strip())
print(y.split(","))
print(y.replace("me", "you"))