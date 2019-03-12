def SumOfCubes(N1):
    rem = 0
    S1 = 0
    while(N1!=0):
        rem = N1 % 10
        N1 = int(N1//10)
        S1 = S1 + rem**3
    return S1

def ArmstrongNum(N1):
    ArmNo = SumOfCubes(N1)
    if ArmNo == N1:
        print("The entered number is an armstrong number.")
    else:
        print("The entered number is not an armstrong number.")

def main():
    N1 = eval(input("Enter a number to check if it is an armstrong number :: "))
    ArmstrongNum(N1)

if __name__=='__main__':
    main()