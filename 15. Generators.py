# Generators are functions that can pause and resume their execution.
# return ->yield

def fabonacci():
    a, b= 0,1
    while True:
        yield a # Pauses here and outputs '0'
        a,b = b, a+b
        
gen = fabonacci()
for _ in range(100):
    print(next(gen))