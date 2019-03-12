
def Factorial(N1):
    if N1 < 0:
        return ("Cannot find factorial for negative number.")
    if N1 == 0 or N1 ==1:
        return 1
    N2 = 1
    for x in range(1,N1):
        N2 = N2 * x
        fact = N1 * N2
    return fact


if __name__ == '__main__':
    N1 = int(input("Enter a number to find factorial :: "))
    res = Factorial(N1)
    print("The factorial for the given number :: {}".format(res))