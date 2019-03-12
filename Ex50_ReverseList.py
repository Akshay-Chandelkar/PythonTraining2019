def ReverseList(L1):
    # return L1[::-1]
    i = len(L1)
    L2 = []
    while i != 0:
        L2.append(L1[i-1])
        i -=1
    return L2


def main():
    L1 = eval(input("Enter a list to be reversed :: "))
    print("The reversed list of {} is {} ".format(L1,ReverseList(L1)))

if __name__ == '__main__':
    main()