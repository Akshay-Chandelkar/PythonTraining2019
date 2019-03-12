
def GCD(N1, N2):
    while (N1 != N2):
        if N1 > N2:
            N1 = N1 - N2
        else:
            N2 = N2 - N1
    return N1



def main():
    N1, N2 = eval(input("Enter two numbers to find the GCD :: "))
    res = GCD(N1, N2)
    print("The GCD for {} and {} is :: {}".format(N1, N2, res))


if __name__ == '__main__':
    main()