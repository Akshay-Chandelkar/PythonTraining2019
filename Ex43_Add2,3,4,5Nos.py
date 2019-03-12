
def add(a, b, c=0, d=0, e=0):
    return a+b+c+d+e

def main():
    res = add(10, 20)
    print("The addition of two numbers :: {}".format(res))
    res = add(10, 20, 30)
    print("The addition of three numbers :: {}".format(res))
    res = add(10, 20, 30, 40)
    print("The addition of four numbers :: {}".format(res))
    res = add(10, 20, 30, 40, 50)
    print("The addition of five numbers :: {}".format(res))

if __name__ == '__main__':
    main()

'''
def add(a, b, c=20):
    return a+b+c

print(add(10,10))
print(add(10, b=30))
print(add(b=10, a=20))
print(add(1, c=200, b=100))
print(add(1, b=30, 100))
'''