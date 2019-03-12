
# Posiyional arguments
def add(a,b):
    return a + b

res = add(10,20)
print("Result = %d"%res)

# Default arguments
def add(a,b=10):
    return a + b

res = add(100,200)
print("Result = %d"%res)
res = add(100)
print("Result = %d"%res)