
def ReverseNum(N1):
    rem = 0
    rev = 0
    while(N1!=0):
        rem = int(N1 % 10)
        rev = rev * 10 + rem
        N1 = int(N1//10)
    return rev

def main():
    N1 = eval(input("Enter a number to be reversed :: "))
    #res = ReverseNum(N1)
    print("The reverse number of {} is :: {}".format(N1, ReverseNum(N1)))

if __name__ == '__main__':
    main()