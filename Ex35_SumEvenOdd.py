
print("Its fun", __name__)
def SumEvenOdd(LB,UB):
    even = 0
    odd = 0
    for i in range(LB,UB+1):
        if i % 2 == 0:
            even +=i
        else:
            odd +=i
    return even, odd
    #print("The sum of even numbers in range {} to {} is {}".format(LB, UB, even))
    #print("The sum of odd numbers in range {} to {} is {}" .format(LB, UB, odd))



def main():
    LB,UB = eval(input("Enter a lower bound and upper bound number for a range :: "))
    R1, R2 = SumEvenOdd(LB,UB)
    print("The sum of even numbers in range {} to {} is {}".format(LB, UB, R1))
    print("The sum of odd numbers in range {} to {} is {}".format(LB, UB, R2))

if __name__ == '__main__':
    main()