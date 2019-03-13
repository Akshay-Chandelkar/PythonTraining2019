def ExtendList(L2,L3):
    j = 0
    while j < len(L3):
        if type(L3[j])!= list:
            L2.append(L3[j])
        else:
            ExtendList(L2,L3[j])
        j +=1
    return L2

def NeutralizeList(L1):
    i = 0
    L2 = []
    while i < len(L1):
        if type(L1[i]) != list:
            L2.append(L1[i])
        else:
            ExtendList(L2,L1[i])
        i+=1
    return L2



def main():
    L1 = eval(input("Enter a nested list :: "))
    print("The nested list {} is converted to single list :: {}".format(L1,NeutralizeList(L1)))

if __name__ == '__main__':
    main()