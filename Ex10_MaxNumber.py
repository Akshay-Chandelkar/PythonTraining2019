
def MaxNumber(N1,N2,N3):
    if N1 > N2  and N1 > N3:
        return N1
    elif N2 > N3:
        return N2
    else:
        return N3

if __name__ == '__main__':
    N1,N2,N3 = eval(input("Enter 3 numbers to find max number :: "))
    print("The max number is :: {}".format(MaxNumber(N1,N2,N3)))