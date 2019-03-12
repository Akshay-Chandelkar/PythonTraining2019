def ListMaxMin(L1):
    max = min = L1[0]
    i = 1
    while i<len(L1):
        if L1[i] > max:
            max = L1[i]
        if L1[i] < min:
            min = L1[i]
        i +=1
    return max,min



def main():
    L1 = eval(input("Enter a list with integers :: "))
    R1,R2 = ListMaxMin(L1)
    print("The max and min elements in the list {} are {} and {}".format(L1, R1, R2))

if __name__ == '__main__':
    main()