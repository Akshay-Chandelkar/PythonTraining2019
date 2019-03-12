
def NumTable(N1):
    if N1 > 0:
        print("The table for the given number ::")
        for x in range(1,11):
            N2 = N1 * x
            print(N2)

    else:
        print("The entered number is 0 or negative.")


if __name__ == '__main__':
    N1 = int(input("Enter a number to get its table :: "))
    NumTable(N1)
    #print("The table for the given number :: {}".format(res))