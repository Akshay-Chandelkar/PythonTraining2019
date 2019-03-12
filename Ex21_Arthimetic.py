
print("Free fall code to begin")

def add(num1,num2):
    sum = num1 + num2
    print("The sum of two numbers is : ", sum)

def sub(num1,num2):
    sub = num2 - num1
    print("The difference between the two numbers is : ", sub)

def mul(num1,num2):
    mul = num1 * num2
    print("The multiplication of the two numbers is : ", mul)

def div(num1,num2):
    div = num2/num1
    print("The division of the two numbers is :", div)

def Menu():
    while True:
        print("1. Add\n2. Substract\n3. Multiply\n4. Division\n5. Exit")
        choice = int(input("Enter your choice :: "))
        if(choice > 0 and choice <6):
            return choice
        else:
            print("Please enter the correct choice.")

def ArithmaticOperations(num1,num2):
    choice = 0
    while choice != 5:
        choice = Menu()
        if(choice == 1):
            add(num1,num2)
        elif (choice == 2):
            sub(num1,num2)
        elif (choice == 3):
            mul(num1,num2)
        elif (choice == 4):
            div(num1,num2)
        elif (choice == 5):
            break
        else:
            Menu()



def main():
    num1 =  int(input("Please enter first number : "))
    num2 = int(input("Please enter second number : "))
    ArithmaticOperations(num1,num2)
    #add(num2=30,num1=10)
    #sub(num1,num2)
    #mul(num1,num2)
    #div(num1,num2)

if __name__ == '__main__':
    main()
