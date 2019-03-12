def SumOfCubes(N1):
    rem = 0
    S1 = 0
    while(N1!=0):
        rem = N1 % 10
        N1 = int(N1//10)
        S1 = S1 + rem**3

    return S1

def main():
    N1 = eval(input("Enter a number to get sum of cubes of digits :: "))
    #res = SumOfCubes(N1)
    print("The sum of cubes of digits for {} is {}".format(N1, SumOfCubes(N1)))

if __name__ == '__main__':
    main()