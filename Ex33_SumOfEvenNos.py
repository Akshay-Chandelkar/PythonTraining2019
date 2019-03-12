# Ex of while loop::
'''
N1 = int(input("Enter a number :: "))
sum = 0
i = 0
while i <= N1:
    sum += i
    i +=1
print("The sum of %d numbers from 0 is %d " %(N1, sum))
'''

def SumOfEven(N1):
    sum = 0
    i = 0
    '''
    while i <= N1:
        if i % 2 == 0:
            sum += i
        i +=1
    '''
    for x in range(2,N1+1,2):
        sum += x
    print("Sum of even numbers upto %d from 0 is %d" %(N1, sum))

def main():
    N1 = int(input("Enter a number :: "))
    SumOfEven(N1)

if __name__ == '__main__':
    main()
