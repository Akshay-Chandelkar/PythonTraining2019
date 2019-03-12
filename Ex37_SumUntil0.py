
def SumUntil(N1):
    sum = 0
    while N1 != 0:
        N1 = eval(input("Enter the number to stop enter 0 :: "))
        sum = sum + N1
    print("The sum of entered numbers :: %d"%sum)

def main():
    N1 = -1
    SumUntil(N1)

if __name__ == '__main__':
    main()



'''
number = -1
sum = 0
while number != 0:
    number = eval(input("Enter number to stop enter 0 :: "))
    sum = sum + number
print("The sum of the entered numbers :: %d "%sum)
'''