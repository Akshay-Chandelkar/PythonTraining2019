
def FibonacciLimit(N1,N2):
    a = 1
    b = 1
    print(a,b)
    N1 -= 2
    while N1 != 0:
        c = a + b
        if c > N2:
            break
        print(c)
        a = b
        b = c
        N1 -=1

def main():
    N1,N2 = eval(input("Enter 2 numbers; first to generate series and second to print :: "))
    FibonacciLimit(N1,N2)

if __name__ == '__main__':
    main()