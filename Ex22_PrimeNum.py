
def PrimeNum(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("The number is not a prime number")
                break
        else:
            print("The number is a prime number")
    else:
        print("The number is not a prime number")


def main():
    num = int(input("Enter a number to verify if it is a prime number : "))
    PrimeNum(num)

if __name__ == '__main__':
    main()