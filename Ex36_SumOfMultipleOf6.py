
def SumOfMul(LB, UB):
    sum = 0
    for x in range(LB, UB+1):
        if x % 6 == 0:
            sum +=x
        #x +=1
    print("The sum of multiple of 6 in range {} to {} is {} ".format(LB, UB, sum))

def main():
    LB,UB = eval(input("Enter a range for sum of multiple of 6 :: "))
    SumOfMul(LB, UB)

if __name__ == '__main__':
    main()