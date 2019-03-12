def SumOfDigit(S1):
    i = 0
    sum = 0
    while i < len(S1):
        if S1[i].isdigit():
            sum += int(S1[i])
        i +=1
    return sum

def main():
    S1 = eval(input("Enter an alpha numeric string ::"))
    print("The sum of digit in the string '{}' :: {}".format(S1, SumOfDigit(S1)))

if __name__ == '__main__':
    main()