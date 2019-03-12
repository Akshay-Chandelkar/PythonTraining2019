
def SubSmallFromLarge(N1,N2):
    if N1 == N2:
        print("Both the numbers are same.")
    elif N1 > N2:
        N3 = N1 - N2
        return N3
    else:
        N3 = N2 - N1
        return N3


if __name__ == '__main__':
    N1 = int(input("Enter the first number :: "))
    N2 = int(input("Enter the second number :: "))
    res = SubSmallFromLarge(N1,N2)
    print("The result for the substraction = {}".format(res))