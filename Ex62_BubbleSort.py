

def BubbleSort(L1):
    for x in range(len(L1)-1, 0, -1):
        for i in range(x):
            if L1[i] > L1[i+1]:
                L1[i], L1[i+1] = L1[i+1], L1[i]
    return L1



def main():
    L1 = eval(input("Enter a list to be sorted using Bubble sort ::"))
    print("The list is bubble sorted as :: {}".format(L1, BubbleSort(L1)))



if __name__ == '__main__':
    main()