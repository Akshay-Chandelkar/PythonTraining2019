def MergeList(L1,L2):
    L1.sort()
    L2.sort()
    i = 0
    j = 0
    L3 = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i +=1
        else:
            L3.append(L2[j])
            j +=1
    if i < len(L1):
        L3.extend(L1[i:])
    if j < len(L2):
        L3.extend(L2[j:])
    return L3


def main():
    L1 = eval(input("Enter the first sorted list :: "))
    L2 = eval(input("Enter the second sorted list :: "))
    #SortList(L1,L2)
    retval = MergeList(L1, L2)
    print("The sorted merge list of {} and {} is {}".format(L1, L2, retval))

if __name__ == '__main__':
    main()