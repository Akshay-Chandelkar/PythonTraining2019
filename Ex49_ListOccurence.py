def ListOccurence(L1,E1):
    count = 0
    x = E1
    for y in L1:
        if x == y:
            count +=1
    return count




def main():
    L1 = eval(input("Enter a list to check the count of elements :: "))
    E1 = eval(input("Enter an element to be searched :: "))
    res = ListOccurence(L1, E1)
    print("The count of elemnt {} in the given list {} is {} ".format(E1, L1, res))


if __name__ == '__main__':
    main()