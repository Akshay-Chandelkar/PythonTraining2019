def CompareList(L1, L2):
    if type(L1) != list or type(L2) != list:
        #print("L1 or L2 is not a list. ")
        return 0
    if len(L1) != len(L2):
        #print("The given {} and {} lists are not same.".format(L1, L2))
        return 0
    L1.sort()
    L2.sort()

    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            i +=1
            j +=1
            continue
        #print("The given {} and {} lists are not same.".format(L1, L2))
        return 0
        break

    else:
        #print("The given {} and {} lists are same.".format(L1, L2))
        return 1


    '''
    for i in range(len(L1)):
        if L1[i] == L2[i]:
            continue
        #print("The given {} and {} lists are not same.".format(L1, L2))
        return 0
        break

    else:
        #print("The given {} and {} lists are same.".format(L1, L2))
        return 1
    '''

def main():
    L1 = eval(input("Enter the first list :: "))
    L2 = eval(input("Enter the second list :: "))
    retval = CompareList(L1,L2)
    if retval == 1:
        print("The lists {} and {} are same.".format(L1, L2))
    else:
        print("The lists {} and {} are not same. ".format(L1, L2))



if __name__ == '__main__':
    main()