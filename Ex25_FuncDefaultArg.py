
def multiply(a, b=1, c=1, d=1, e=1):
    return a*b*c*d*e

def add(a, b, c=0, d=0, e=0):
    return a+b+c+d+e

def main():
    print(multiply(2, 4))
    print(multiply(2, 4, 5))
    print(multiply(2, 4, 5, 6))
    print(multiply(2, 4, 5, 6, 7))
    print(add(2, 4))
    print(add(2, 4, 5))
    print(add(2, 4, 5, 6))
    print(add(2, 4, 5, 6, 7))

if __name__ == '__main__':
    main()