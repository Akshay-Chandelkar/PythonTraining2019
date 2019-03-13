def SelectionSort(L1):
    i = 0
    while i < len(L1):
        for j in range(i,len(L1)):
            if j+1 < len(L1) and L1[i]>L1[j+1]:
                L1[i], L1[j+1] = L1[j+1], L1[i]
        #print(L1)
        i +=1
    return L1

def main():
    L1 = eval(input("Enter a list to be sorted using selection sort :: "))
    print("The list is selection sorted as :: {}".format(SelectionSort(L1)))

if __name__ == '__main__':
    main()