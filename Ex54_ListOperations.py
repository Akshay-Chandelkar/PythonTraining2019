def Intersection(L1, L2):
    L3 = []
    i = 0
    while i < len(L2):
        if L2[i] in L1:
            L3.append(L2[i])
        i +=1
    return L3

def InverseIntersection(L1, L2):
    L3 = []
    for i in L1:
        if i not in L2 and i not in L3:
            L3.append(i)
    for j in L2:
        if j not in L1 and j not in L3:
            L3.append(j)
    return L3

def Union(L1, L2):
    L3 = []
    for i in L1:
        if i not in L3:
            L3.append(i)
    for j in L2:
        if j not in L1:
            L3.append(j)
    return L3

def Menu():
    while True:
        print(" 1. Union \n 2. Intersection \n 3. Inverse Intersection \n 4. Exit")
        choice = int(input("Enter your choice :: "))
        if choice > 0 and choice < 5 :
            return choice
        else:
            print("Enter a valid choice.")

def ListOperations(L1, L2):
    choice = 0
    while choice != 4:
        choice = Menu()
        if (choice == 1):
            print("The union of {} and {} lists is {}".format(L1, L2, Union(L1, L2)))
        elif (choice == 2):
            print("The intersection of {} and {} lists is {}".format(L1, L2, Intersection(L1, L2)))
        elif (choice == 3):
            print("The inverse intersection of {} and {} lists is {}".format(L1, L2, InverseIntersection(L1, L2)))
        elif (choice == 4):
            break
        else:
            Menu()


def main():
    L1 = eval(input("Enter the first list :: "))
    L2 = eval(input("Enter the second list :: "))
    ListOperations(L1, L2)


if __name__ == '__main__':
    main()
