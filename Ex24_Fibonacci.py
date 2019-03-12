def Fibonacci(N1):
    a = 1
    b = 1
    print(a)
    print(b)
    N1 -= 2
    while N1 != 0:
        c = a + b
        print(c)
        a = b
        b = c
        N1 -=1

def main():
    N1 = int(input("Enter a number to get fibonacci series :: "))
    print("The fibonacci series is ::")
    Fibonacci(N1)


if __name__ == '__main__':
    main()
